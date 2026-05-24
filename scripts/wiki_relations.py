#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync YAML frontmatter relation fields from body wikilinks.

What it does:
- Reads wiki/index.json as the authority for existing wiki entries.
- Scans Markdown body wikilinks.
- Fills related_concepts / related_theories / related_methods / related_persons /
  related_facts / related_arguments according to the linked entry's type.
- Fills sources from wikilinks in the ## 来源 / ## Sources section only.

Recommended order:
  python3 scripts/wiki_index.py
  python3 scripts/wiki_linker.py sync
  python3 scripts/wiki_relations.py sync
  python3 scripts/wiki_index.py

The script intentionally does not modify semantic fields such as title, aliases,
summary, tags, citation, journal, book_title, authors, editors, publisher,
part_of, confidence, status, created, or updated.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
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
SYNC_KEYS = RELATION_KEYS + ["sources"]

# Matches non-embedded wikilinks. ![[file.pdf]] is ignored by negative lookbehind.
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


def load_index() -> dict[str, Entry]:
    if not INDEX_JSON.exists():
        raise SystemExit(f"Missing index: {INDEX_JSON}. Run python3 scripts/wiki_index.py first.")

    data = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    entries_raw: list[dict]
    if isinstance(data, list):
        entries_raw = data
    elif isinstance(data, dict):
        # Accept either {"entries": [...]} or {"Title": "path"} style indexes.
        if isinstance(data.get("entries"), list):
            entries_raw = data["entries"]
        else:
            entries_raw = []
            for title, value in data.items():
                if isinstance(value, str):
                    entries_raw.append({"title": title, "path": value, "type": "unknown"})
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
        typ = str(item.get("type") or "unknown").strip() or "unknown"
        aliases_raw = item.get("aliases") or []
        if not isinstance(aliases_raw, list):
            aliases_raw = []
        aliases = tuple(str(a).strip() for a in aliases_raw if str(a).strip())
        if not title:
            continue
        entry = Entry(title=title, path=path, type=typ, aliases=aliases)
        # Support [[Title]], [[File Stem]], and [[wiki/path/File.md]].
        for key in {title, Path(path).stem if path else title, path[:-3] if path.endswith(".md") else path, path}:
            key = str(key).strip()
            if key:
                by_key[key] = entry
    return by_key


def iter_markdown_files(target: str | None = None) -> list[Path]:
    if target:
        p = Path(target)
        if not p.is_absolute():
            p = ROOT / p
        if p.is_file():
            return [p]
        if p.is_dir():
            base = p
        else:
            raise SystemExit(f"No such file or directory: {target}")
    else:
        base = WIKI_DIR

    files: list[Path] = []
    for path in base.rglob("*.md"):
        rel_parts = set(path.relative_to(ROOT).parts)
        if rel_parts & EXCLUDE_DIR_PARTS:
            continue
        if path.name in EXCLUDE_FILENAMES:
            continue
        files.append(path)
    return sorted(files)


def split_frontmatter(text: str) -> tuple[str, str, str]:
    """Return (prefix_before_yaml, yaml_text, body). prefix is normally '---\n'."""
    if not text.startswith("---\n"):
        return "", "", text
    end = text.find("\n---", 4)
    if end == -1:
        return "", "", text
    # Include exactly the opening marker separately; yaml excludes --- markers.
    closing_end = text.find("\n", end + 4)
    if closing_end == -1:
        closing_end = len(text)
    yaml_text = text[4:end].strip("\n")
    body = text[closing_end + 1 :] if closing_end < len(text) else ""
    return "---\n", yaml_text, body


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
    """Return (source_section, body_without_source_sections). H2-level only."""
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
    # Drop anchors/blocks for lookup: [[Entry#Section|text]] -> Entry.
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
    for key in (rel, rel[:-3] if rel.endswith(".md") else rel, stem):
        if key in index:
            return index[key]
    return None


def infer_relations(body_without_sources: str, index: dict[str, Entry], self_entry: Entry | None) -> dict[str, list[str]]:
    result = {key: [] for key in RELATION_KEYS}
    seen_by_field = {key: set() for key in RELATION_KEYS}
    self_title = self_entry.title if self_entry else None

    for target in extract_targets(body_without_sources):
        entry = index.get(target) or index.get(Path(target).stem)
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


def infer_sources(source_section: str, index: dict[str, Entry]) -> list[str]:
    sources: list[str] = []
    seen: set[str] = set()
    for target in extract_targets(source_section):
        entry = index.get(target) or index.get(Path(target).stem)
        # If it is in the index, normalize to title. If not, preserve target.
        title = entry.title if entry else Path(target).stem
        link = f"[[{title}]]"
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


def update_yaml_lists(yaml_text: str, updates: dict[str, list[str]], add_missing: bool = True) -> str:
    lines = yaml_text.splitlines()
    if not lines and not updates:
        return yaml_text

    existing_keys = {key for line in lines if (key := yaml_key_at(line))}

    # Replace existing fields first.
    for key in SYNC_KEYS:
        if key not in updates:
            continue
        span = find_key_span(lines, key)
        if span is not None:
            start, end = span
            lines[start:end] = format_yaml_list(key, updates[key])

    if add_missing:
        missing = [key for key in SYNC_KEYS if key in updates and key not in existing_keys and updates[key]]
        if missing:
            insert_at = len(lines)
            for anchor in ("confidence", "status", "created", "updated"):
                span = find_key_span(lines, anchor)
                if span is not None:
                    insert_at = span[0]
                    break
            new_lines: list[str] = []
            for key in missing:
                new_lines.extend(format_yaml_list(key, updates[key]))
            lines[insert_at:insert_at] = new_lines

    return "\n".join(lines).rstrip() + "\n"


def process_file(path: Path, index: dict[str, Entry], dry_run: bool = False, add_missing: bool = True) -> bool:
    original = path.read_text(encoding="utf-8")
    prefix, yaml_text, body = split_frontmatter(original)
    if not prefix:
        return False

    source_section, body_without_sources = source_section_and_body_without_sources(body)
    self_entry = current_entry_for_file(path, index)
    updates = infer_relations(body_without_sources, index, self_entry)
    updates["sources"] = infer_sources(source_section, index)

    new_yaml = update_yaml_lists(yaml_text, updates, add_missing=add_missing)
    new_text = f"---\n{new_yaml}---\n{body}"

    if new_text != original:
        if dry_run:
            print(f"DRY-RUN would update {rel_to_root(path)}")
        else:
            path.write_text(new_text, encoding="utf-8")
            print(f"updated {rel_to_root(path)}")
        return True
    return False


def cmd_sync(args: argparse.Namespace) -> int:
    index = load_index()
    files = iter_markdown_files(args.target)
    changed = 0
    for path in files:
        try:
            if process_file(path, index, dry_run=args.dry_run, add_missing=not args.no_add_missing):
                changed += 1
        except UnicodeDecodeError:
            print(f"skip non-utf8 file: {rel_to_root(path)}", file=sys.stderr)
    if args.dry_run:
        print(f"DRY-RUN complete: {changed} file(s) would be updated.")
    else:
        print(f"Done: {changed} file(s) updated.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sync YAML related_* and sources from Markdown wikilinks.")
    sub = parser.add_subparsers(dest="command")

    sync = sub.add_parser("sync", help="Synchronize relation frontmatter fields.")
    sync.add_argument("target", nargs="?", help="Optional file or directory to sync. Defaults to wiki/.")
    sync.add_argument("--dry-run", action="store_true", help="Show files that would change without writing.")
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
