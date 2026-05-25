#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync YAML frontmatter relation fields from body wikilinks.

What it does:
- Reads wiki/index.json as the authority for existing wiki entries.
- Scans wiki/ Markdown body wikilinks.
- Fills related_concepts / related_theories / related_methods / related_persons /
  related_facts / related_arguments according to the linked entry's type.
- Fills wiki entry sources from wikilinks in the ## 来源 / ## Sources section only.
- Fills source-record extracted_to by reversing wiki entry source links.

Default behavior:
- `sync` is incremental by default and only processes git-changed wiki Markdown files.
- Use `sync --full` to recompute all wiki relations and all source extracted_to fields.

Important:
- sources/ and books/ source records are NOT treated as normal wiki entries.
- source records only get extracted_to updated. They do not get related_* or sources fields.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = ROOT / "sources"
BOOKS_DIR = ROOT / "books"
INDEX_JSON = WIKI_DIR / "index.json"

EXCLUDE_DIR_PARTS = {"templates", "indexes", ".obsidian"}
EXCLUDE_FILENAMES = {"index.md", "index.json", "manifest.md", "manifest.json"}

RELATION_FIELDS = {
    "concept": "related_concepts",
    "theory": "related_theories",
    "method": "related_methods",
    "person": "related_persons",
    "fact": "related_facts",
    "argument": "related_arguments",
}
RELATION_KEYS = list(RELATION_FIELDS.values())
WIKI_SYNC_KEYS = RELATION_KEYS + ["sources"]
SOURCE_SYNC_KEYS = ["extracted_to"]

TYPE_DIRS = {
    "concepts": "concept",
    "theories": "theory",
    "methods": "method",
    "persons": "person",
    "facts": "fact",
    "arguments": "argument",
}

WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+?)\]\]")
CODE_FENCE_RE = re.compile(r"^\s*(```|~~~)")
H2_RE = re.compile(r"^##\s+(.+?)\s*$")


@dataclass(frozen=True)
class Entry:
    title: str
    path: str
    type: str
    aliases: tuple[str, ...] = ()


def rel_to_root(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def is_under(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def infer_type_from_index_path(path: str) -> str:
    parts = Path(path).parts
    if len(parts) >= 2 and parts[0] == "wiki":
        return TYPE_DIRS.get(parts[1], "unknown")
    return "unknown"


def load_index() -> dict[str, Entry]:
    if not INDEX_JSON.exists():
        raise SystemExit(f"Missing index: {INDEX_JSON}. Run python3 scripts/wiki_index.py first.")

    data = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    entries_raw: list[dict]
    if isinstance(data, list):
        entries_raw = data
    elif isinstance(data, dict):
        if isinstance(data.get("entries"), list):
            entries_raw = data["entries"]
        else:
            entries_raw = []
            for title, value in data.items():
                if isinstance(value, str):
                    entries_raw.append({"title": title, "path": value, "type": infer_type_from_index_path(value)})
                elif isinstance(value, dict):
                    item = dict(value)
                    item.setdefault("title", title)
                    entries_raw.append(item)
    else:
        entries_raw = []

    by_key: dict[str, Entry] = {}
    for item in entries_raw:
        title = str(item.get("title") or "").strip()
        path = str(item.get("path") or "").strip()
        typ = str(item.get("type") or infer_type_from_index_path(path)).strip() or "unknown"
        aliases_raw = item.get("aliases") or []
        if not isinstance(aliases_raw, list):
            aliases_raw = []
        aliases = tuple(str(a).strip() for a in aliases_raw if str(a).strip())
        if not title:
            continue
        entry = Entry(title=title, path=path, type=typ, aliases=aliases)

        keys = {title, title.lower()}
        if path:
            keys.add(path)
            keys.add(path.lower())
            if path.endswith(".md"):
                keys.add(path[:-3])
                keys.add(path[:-3].lower())
            keys.add(Path(path).stem)
            keys.add(Path(path).stem.lower())
        for alias in aliases:
            keys.add(alias)
            keys.add(alias.lower())
        for key in keys:
            if key:
                by_key[key] = entry
    return by_key


def split_frontmatter(text: str) -> tuple[str, str, str]:
    if not text.startswith("---\n"):
        return "", "", text
    end = text.find("\n---", 4)
    if end == -1:
        return "", "", text
    closing_end = text.find("\n", end + 4)
    if closing_end == -1:
        closing_end = len(text)
    yaml_text = text[4:end].strip("\n")
    body = text[closing_end + 1 :] if closing_end < len(text) else ""
    return "---\n", yaml_text, body


def strip_yaml_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def frontmatter_value(yaml_text: str, key: str) -> str:
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.+?)\s*$", re.MULTILINE)
    m = pattern.search(yaml_text)
    return strip_yaml_quotes(m.group(1)) if m else ""


def strip_code_fences(text: str) -> str:
    out: list[str] = []
    in_code = False
    for line in text.splitlines(keepends=True):
        if CODE_FENCE_RE.match(line):
            in_code = not in_code
            out.append("\n")
            continue
        out.append("\n" if in_code else line)
    return "".join(out)


def source_section_and_body_without_sources(body: str) -> tuple[str, str]:
    lines = body.splitlines(keepends=True)
    source_chunks: list[str] = []
    body_chunks: list[str] = []
    in_source = False

    for line in lines:
        h2 = H2_RE.match(line)
        if h2:
            title = h2.group(1).strip().lower()
            in_source = title in {"来源", "sources", "source"}
        if in_source:
            source_chunks.append(line)
        else:
            body_chunks.append(line)
    return "".join(source_chunks), "".join(body_chunks)


def parse_wikilink(raw: str) -> tuple[str, str | None]:
    if "|" in raw:
        target, display = raw.split("|", 1)
    else:
        target, display = raw, None
    target = target.strip()
    display = display.strip() if display is not None else None
    target = target.split("#", 1)[0].split("^", 1)[0].strip()
    return target, display


def extract_targets(text: str) -> list[str]:
    text = strip_code_fences(text)
    targets: list[str] = []
    seen: set[str] = set()
    for m in WIKILINK_RE.finditer(text):
        target, _display = parse_wikilink(m.group(1))
        if not target:
            continue
        if target.lower().endswith((".pdf", ".epub", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")):
            continue
        if target not in seen:
            targets.append(target)
            seen.add(target)
    return targets


def current_entry_for_file(path: Path, index: dict[str, Entry]) -> Entry | None:
    rel = rel_to_root(path)
    stem = path.stem
    for key in (rel, rel.lower(), rel[:-3] if rel.endswith(".md") else rel, stem, stem.lower()):
        if key in index:
            return index[key]
    return None


def infer_relations(body_without_sources: str, index: dict[str, Entry], self_entry: Entry | None) -> dict[str, list[str]]:
    result = {key: [] for key in RELATION_KEYS}
    seen_by_field = {key: set() for key in RELATION_KEYS}
    self_title = self_entry.title if self_entry else None

    for target in extract_targets(body_without_sources):
        entry = index.get(target) or index.get(target.lower()) or index.get(Path(target).stem) or index.get(Path(target).stem.lower())
        if not entry or entry.type not in RELATION_FIELDS:
            continue
        if self_title and entry.title == self_title:
            continue
        field = RELATION_FIELDS[entry.type]
        link = f"[[{entry.title}]]"
        if link not in seen_by_field[field]:
            result[field].append(link)
            seen_by_field[field].add(link)
    return result


def normalize_source_link_target(target: str, index: dict[str, Entry], source_title_lookup: dict[str, str] | None = None) -> str:
    entry = index.get(target) or index.get(target.lower()) or index.get(Path(target).stem) or index.get(Path(target).stem.lower())
    if entry:
        title = entry.title
    elif source_title_lookup and (target in source_title_lookup or target.lower() in source_title_lookup):
        title = source_title_lookup.get(target) or source_title_lookup[target.lower()]
    elif target.endswith(".md") or "/" in target:
        title = Path(target).stem
    else:
        title = target
    return f"[[{title}]]"


def infer_sources(source_section: str, index: dict[str, Entry], source_title_lookup: dict[str, str] | None = None) -> list[str]:
    sources: list[str] = []
    seen: set[str] = set()
    for target in extract_targets(source_section):
        link = normalize_source_link_target(target, index, source_title_lookup)
        if link not in seen:
            sources.append(link)
            seen.add(link)
    return sources


def yaml_key_at(line: str) -> str | None:
    if line.startswith(" ") or line.startswith("-") or not line.strip() or line.lstrip().startswith("#"):
        return None
    m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line)
    return m.group(1) if m else None


def find_key_span(lines: list[str], key: str) -> tuple[int, int] | None:
    start = None
    for i, line in enumerate(lines):
        if yaml_key_at(line) == key:
            start = i
            break
    if start is None:
        return None
    end = start + 1
    while end < len(lines) and yaml_key_at(lines[end]) is None:
        end += 1
    return start, end


def format_yaml_list(key: str, values: list[str]) -> list[str]:
    if not values:
        return [f"{key}: []"]
    return [f"{key}:"] + [f'  - "{v}"' for v in values]


def update_yaml_lists(
    yaml_text: str,
    updates: dict[str, list[str]],
    *,
    sync_keys: list[str],
    add_missing: bool = True,
    insert_anchors: tuple[str, ...] = ("confidence", "status", "created", "updated"),
) -> str:
    lines = yaml_text.splitlines()
    if not lines and not updates:
        return yaml_text

    existing_keys = {key for line in lines if (key := yaml_key_at(line))}

    for key in sync_keys:
        if key not in updates:
            continue
        span = find_key_span(lines, key)
        if span is not None:
            start, end = span
            lines[start:end] = format_yaml_list(key, updates[key])

    if add_missing:
        missing = [key for key in sync_keys if key in updates and key not in existing_keys and updates[key]]
        if missing:
            insert_at = len(lines)
            for anchor in insert_anchors:
                span = find_key_span(lines, anchor)
                if span is not None:
                    insert_at = span[0]
                    break
            new_lines: list[str] = []
            for key in missing:
                new_lines.extend(format_yaml_list(key, updates[key]))
            lines[insert_at:insert_at] = new_lines

    return "\n".join(lines).rstrip() + "\n"


def iter_markdown_files_in(base: Path) -> list[Path]:
    files: list[Path] = []
    if not base.exists():
        return []
    for path in base.rglob("*.md"):
        try:
            rel_parts = set(path.relative_to(ROOT).parts)
        except ValueError:
            continue
        if rel_parts & EXCLUDE_DIR_PARTS:
            continue
        if path.name in EXCLUDE_FILENAMES:
            continue
        files.append(path)
    return sorted(files)


def iter_wiki_files(target: str | None = None) -> list[Path]:
    if target:
        p = Path(target)
        if not p.is_absolute():
            p = ROOT / p
        if p.is_file():
            return [p] if is_under(p, WIKI_DIR) and p.suffix.lower() == ".md" else []
        if p.is_dir():
            return [f for f in iter_markdown_files_in(p) if is_under(f, WIKI_DIR)]
        raise SystemExit(f"No such file or directory: {target}")
    return iter_markdown_files_in(WIKI_DIR)


def iter_source_record_files(target: str | None = None) -> list[Path]:
    if target:
        p = Path(target)
        if not p.is_absolute():
            p = ROOT / p
        if p.is_file():
            candidates = [p]
        elif p.is_dir():
            candidates = iter_markdown_files_in(p)
        else:
            raise SystemExit(f"No such file or directory: {target}")
    else:
        candidates = iter_markdown_files_in(SOURCES_DIR) + iter_markdown_files_in(BOOKS_DIR)

    out: list[Path] = []
    for path in candidates:
        if not path.is_file() or path.suffix.lower() != ".md":
            continue
        if not (is_under(path, SOURCES_DIR) or is_under(path, BOOKS_DIR)):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        _prefix, yaml_text, _body = split_frontmatter(text)
        if not yaml_text:
            continue
        typ = frontmatter_value(yaml_text, "type").strip().lower()
        if typ == "source" or find_key_span(yaml_text.splitlines(), "extracted_to") is not None:
            out.append(path)
    return sorted(set(out))


def git_changed_markdown_files() -> list[Path]:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(ROOT), "status", "--porcelain", "-z"],
            text=False,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        return []
    parts = out.decode("utf-8", errors="replace").split("\0")
    files: list[Path] = []
    for item in parts:
        if not item:
            continue
        path_str = item[3:] if len(item) > 3 and item[2] == " " else item
        if not path_str.endswith(".md"):
            continue
        p = ROOT / path_str
        if p.exists() and p.is_file():
            files.append(p)
    return sorted(set(files))


def git_changed_wiki_files() -> list[Path]:
    return [p for p in git_changed_markdown_files() if is_under(p, WIKI_DIR) and p.name not in EXCLUDE_FILENAMES]


def process_wiki_file(
    path: Path,
    index: dict[str, Entry],
    source_title_lookup: dict[str, str],
    *,
    dry_run: bool = False,
    add_missing: bool = True,
) -> tuple[bool, Entry | None, list[str]]:
    original = path.read_text(encoding="utf-8")
    prefix, yaml_text, body = split_frontmatter(original)
    if not prefix:
        return False, None, []

    source_section, body_without_sources = source_section_and_body_without_sources(body)
    self_entry = current_entry_for_file(path, index)
    updates = infer_relations(body_without_sources, index, self_entry)
    sources = infer_sources(source_section, index, source_title_lookup)
    updates["sources"] = sources

    new_yaml = update_yaml_lists(
        yaml_text,
        updates,
        sync_keys=WIKI_SYNC_KEYS,
        add_missing=add_missing,
    )
    new_text = f"---\n{new_yaml}---\n{body}"

    changed = new_text != original
    if changed:
        if dry_run:
            print(f"DRY-RUN would update {rel_to_root(path)}")
        else:
            path.write_text(new_text, encoding="utf-8")
            print(f"updated {rel_to_root(path)}")
    return changed, self_entry, sources


def load_source_records() -> tuple[dict[str, Path], dict[str, str]]:
    title_to_path: dict[str, Path] = {}
    lookup: dict[str, str] = {}
    for path in iter_source_record_files(None):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        _prefix, yaml_text, _body = split_frontmatter(text)
        title = frontmatter_value(yaml_text, "title") or path.stem
        title = title.strip()
        if not title:
            continue
        title_to_path[title] = path
        rel = rel_to_root(path)
        rel_no_md = rel[:-3] if rel.endswith(".md") else rel
        keys = {title, title.lower(), path.stem, path.stem.lower(), rel, rel.lower(), rel_no_md, rel_no_md.lower()}
        for key in keys:
            if key:
                lookup[key] = title
    return title_to_path, lookup


def current_extracted_to(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []
    _prefix, yaml_text, _body = split_frontmatter(text)
    lines = yaml_text.splitlines()
    span = find_key_span(lines, "extracted_to")
    if span is None:
        return []
    start, end = span
    values: list[str] = []
    inline = lines[start]
    m = re.match(r"^extracted_to:\s*\[(.*)\]\s*$", inline)
    if m:
        for part in re.split(r"\s*,\s*", m.group(1).strip()):
            item = strip_yaml_quotes(part.strip())
            if item:
                values.append(item)
        return values

    for line in lines[start + 1 : end]:
        s = line.strip()
        if not s.startswith("-"):
            continue
        item = strip_yaml_quotes(s[1:].strip())
        if item:
            values.append(item)
    return values


def update_source_extracted_to(
    path: Path,
    extracted_to: list[str],
    *,
    dry_run: bool,
    add_missing: bool,
) -> bool:
    original = path.read_text(encoding="utf-8")
    prefix, yaml_text, body = split_frontmatter(original)
    if not prefix:
        return False
    new_yaml = update_yaml_lists(
        yaml_text,
        {"extracted_to": extracted_to},
        sync_keys=SOURCE_SYNC_KEYS,
        add_missing=add_missing,
        insert_anchors=("processed_date", "status"),
    )
    new_text = f"---\n{new_yaml}---\n{body}"
    if new_text != original:
        if dry_run:
            print(f"DRY-RUN would update {rel_to_root(path)}")
        else:
            path.write_text(new_text, encoding="utf-8")
            print(f"updated {rel_to_root(path)}")
        return True
    return False


def build_full_extracted_to_map(
    wiki_files: Iterable[Path],
    index: dict[str, Entry],
    source_title_lookup: dict[str, str],
) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    seen: dict[str, set[str]] = {}
    for path in wiki_files:
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        _prefix, yaml_text, body = split_frontmatter(original)
        if not yaml_text:
            continue
        self_entry = current_entry_for_file(path, index)
        if not self_entry:
            title = frontmatter_value(yaml_text, "title") or path.stem
            self_link = f"[[{title}]]"
        else:
            self_link = f"[[{self_entry.title}]]"
        source_section, _body_without_sources = source_section_and_body_without_sources(body)
        for source_link in infer_sources(source_section, index, source_title_lookup):
            result.setdefault(source_link, [])
            seen.setdefault(source_link, set())
            if self_link not in seen[source_link]:
                result[source_link].append(self_link)
                seen[source_link].add(self_link)
    return result


def sync_extracted_to_full(
    source_title_to_path: dict[str, Path],
    reverse_map: dict[str, list[str]],
    *,
    dry_run: bool,
    add_missing: bool,
) -> int:
    changed = 0
    for title, path in sorted(source_title_to_path.items()):
        link = f"[[{title}]]"
        extracted = reverse_map.get(link, [])
        if update_source_extracted_to(path, extracted, dry_run=dry_run, add_missing=add_missing):
            changed += 1
    return changed


def sync_extracted_to_incremental(
    changed_entries: list[tuple[Entry | None, Path, list[str]]],
    source_title_to_path: dict[str, Path],
    *,
    dry_run: bool,
    add_missing: bool,
) -> int:
    changed = 0
    for entry, path, current_source_links in changed_entries:
        if entry:
            entry_link = f"[[{entry.title}]]"
        else:
            try:
                text = path.read_text(encoding="utf-8")
                _prefix, yaml_text, _body = split_frontmatter(text)
                title = frontmatter_value(yaml_text, "title") or path.stem
            except Exception:
                title = path.stem
            entry_link = f"[[{title}]]"

        current_sources = set(current_source_links)
        for title, source_path in sorted(source_title_to_path.items()):
            source_link = f"[[{title}]]"
            old_values = current_extracted_to(source_path)
            new_values = [v for v in old_values if v != entry_link]
            if source_link in current_sources and entry_link not in new_values:
                new_values.append(entry_link)
            if new_values != old_values:
                if update_source_extracted_to(source_path, new_values, dry_run=dry_run, add_missing=add_missing):
                    changed += 1
    return changed


def cmd_sync(args: argparse.Namespace) -> int:
    index = load_index()
    source_title_to_path, source_title_lookup = load_source_records()

    explicit_target = bool(args.target)
    full = bool(args.full)
    incremental = not full and not explicit_target

    if explicit_target:
        target = Path(args.target)
        if not target.is_absolute():
            target = ROOT / target
        if target.exists() and (is_under(target, SOURCES_DIR) or is_under(target, BOOKS_DIR)):
            wiki_files = iter_wiki_files(None)
            reverse_map = build_full_extracted_to_map(wiki_files, index, source_title_lookup)
            target_sources = iter_source_record_files(args.target)
            changed = 0
            for path in target_sources:
                text = path.read_text(encoding="utf-8")
                _prefix, yaml_text, _body = split_frontmatter(text)
                title = frontmatter_value(yaml_text, "title") or path.stem
                extracted = reverse_map.get(f"[[{title}]]", [])
                if update_source_extracted_to(path, extracted, dry_run=args.dry_run, add_missing=not args.no_add_missing):
                    changed += 1
            print(("DRY-RUN complete" if args.dry_run else "Done") + f": {changed} source file(s) updated.")
            return 0
        wiki_files = iter_wiki_files(args.target)
    elif incremental:
        wiki_files = git_changed_wiki_files()
    else:
        wiki_files = iter_wiki_files(None)

    changed_wiki = 0
    changed_entries: list[tuple[Entry | None, Path, list[str]]] = []
    for path in wiki_files:
        try:
            changed, entry, sources = process_wiki_file(
                path,
                index,
                source_title_lookup,
                dry_run=args.dry_run,
                add_missing=not args.no_add_missing,
            )
            if changed:
                changed_wiki += 1
            changed_entries.append((entry, path, sources))
        except UnicodeDecodeError:
            print(f"skip non-utf8 file: {rel_to_root(path)}", file=sys.stderr)

    if full:
        reverse_map = build_full_extracted_to_map(iter_wiki_files(None), index, source_title_lookup)
        changed_sources = sync_extracted_to_full(
            source_title_to_path,
            reverse_map,
            dry_run=args.dry_run,
            add_missing=not args.no_add_missing,
        )
    else:
        changed_sources = sync_extracted_to_incremental(
            changed_entries,
            source_title_to_path,
            dry_run=args.dry_run,
            add_missing=not args.no_add_missing,
        )

    mode = "incremental" if incremental else ("full" if full else "targeted")
    if args.dry_run:
        print(f"DRY-RUN complete ({mode}): {changed_wiki} wiki file(s), {changed_sources} source file(s) would be updated.")
    else:
        print(f"Done ({mode}): {changed_wiki} wiki file(s), {changed_sources} source file(s) updated.")
    if incremental and not wiki_files:
        print("No git-changed wiki Markdown files found. Use --full to recompute all relations and extracted_to fields.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sync wiki related_*/sources and source extracted_to from Markdown wikilinks.")
    sub = parser.add_subparsers(dest="command")

    sync = sub.add_parser("sync", help="Synchronize relation frontmatter fields.")
    sync.add_argument("target", nargs="?", help="Optional file or directory to sync. Defaults to git-changed wiki files.")
    sync.add_argument("--dry-run", action="store_true", help="Show files that would change without writing.")
    sync.add_argument("--full", action="store_true", help="Recompute all wiki relations and all source extracted_to fields.")
    sync.add_argument("--git", action="store_true", help="Compatibility flag. Default behavior is already git-incremental.")
    sync.add_argument(
        "--no-add-missing",
        action="store_true",
        help="Only update fields already present in frontmatter; do not add missing non-empty fields.",
    )
    sync.set_defaults(func=cmd_sync)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return 2
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
