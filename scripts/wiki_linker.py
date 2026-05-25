#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
INDEX_JSON = WIKI_DIR / "index.json"
SOURCES_DIR = ROOT / "sources"
BOOKS_DIR = ROOT / "books"

EXCLUDE_DIR_PARTS = {"templates", "indexes", ".obsidian"}
EXCLUDE_FILENAMES = {
    "index.md",
    "index.json",
    "manifest.md",
    "manifest.json",
}

# A conservative skip list for generated/source-like areas. This is structural,
# not a semantic stopword list. The actual link whitelist is wiki/index.json.
SOURCE_DIRS = {"sources", "raw", "books", "scripts"}

WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
EMBED_RE = re.compile(r"!\[\[[^\]]+\]\]")
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\([^)]*\)")
URL_RE = re.compile(r"https?://\S+|doi:\s*\S+|10\.\d{4,9}/\S+", re.IGNORECASE)
HTML_TAG_RE = re.compile(r"<[^>]+>")
SOURCE_SECTION_NAMES = {"来源", "sources", "source"}


@dataclass(frozen=True)
class Entry:
    title: str
    path: str
    aliases: tuple[str, ...]


@dataclass(frozen=True)
class Term:
    text: str
    target: str
    is_alias: bool


@dataclass
class LinkStats:
    files_changed: int = 0
    links_added: int = 0
    links_removed: int = 0


def load_entries() -> list[Entry]:
    if not INDEX_JSON.exists():
        raise SystemExit(f"index not found: {INDEX_JSON}. Run `python3 scripts/wiki_index.py` first.")
    raw = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    entries: list[Entry] = []
    for item in raw:
        title = str(item.get("title") or "").strip()
        path = str(item.get("path") or "").strip()
        aliases = tuple(str(x).strip() for x in item.get("aliases", []) if str(x).strip())
        if title and path:
            entries.append(Entry(title=title, path=path, aliases=aliases))
    return entries


def load_source_entries() -> list[Entry]:
    entries: list[Entry] = []
    for root in (SOURCES_DIR, BOOKS_DIR):
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            if path.name.startswith("schema-") or path.name.startswith("vault-schema-"):
                continue
            title = path.stem.strip()
            if title:
                entries.append(Entry(title=title, path=rel_to_root(path), aliases=()))
    return entries


def make_source_pattern(source_titles: set[str]) -> re.Pattern[str] | None:
    if not source_titles:
        return None
    alternatives = sorted((re.escape(t) for t in source_titles if t), key=len, reverse=True)
    if not alternatives:
        return None
    return re.compile(r"(?<![\w/])(" + "|".join(alternatives) + r")(?![\w/])")


def rel_to_root(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def should_skip_file(path: Path) -> bool:
    if path.name in EXCLUDE_FILENAMES:
        return True
    try:
        rel_wiki = path.resolve().relative_to(WIKI_DIR)
    except ValueError:
        return True
    if any(part in EXCLUDE_DIR_PARTS for part in rel_wiki.parts):
        return True
    if rel_wiki.parts and rel_wiki.parts[0] in SOURCE_DIRS:
        return True
    return False


def iter_target_files(args_paths: list[str]) -> list[Path]:
    if args_paths:
        files: list[Path] = []
        for raw in args_paths:
            path = Path(raw).expanduser()
            if not path.is_absolute():
                path = ROOT / path
            if path.is_dir():
                files.extend(p for p in sorted(path.rglob("*.md")) if not should_skip_file(p))
            elif path.suffix.lower() == ".md" and not should_skip_file(path):
                files.append(path)
        return sorted(set(files))
    return [p for p in sorted(WIKI_DIR.rglob("*.md")) if not should_skip_file(p)]


def make_terms(entries: list[Entry]) -> tuple[list[Term], dict[str, Entry], dict[str, str]]:
    entries_by_title = {e.title: e for e in entries}
    path_to_title = {e.path: e.title for e in entries}
    terms: list[Term] = []
    seen: set[tuple[str, str]] = set()

    for e in entries:
        for text, is_alias in [(e.title, False), *[(a, True) for a in e.aliases]]:
            text = text.strip()
            if not text:
                continue
            key = (text, e.title)
            if key in seen:
                continue
            seen.add(key)
            terms.append(Term(text=text, target=e.title, is_alias=is_alias))

    # Longest first prevents linking "Culture" inside "World Culture Theory".
    terms.sort(key=lambda t: len(t.text), reverse=True)
    return terms, entries_by_title, path_to_title


def entry_terms(entry: Entry) -> set[str]:
    return {t.text for t in make_terms([entry])[0]}


def parse_entry_from_text(rel_path: str, text: str) -> Entry | None:
    path = ROOT / rel_path
    if rel_path.startswith("sources/") and path.suffix.lower() == ".md":
        return Entry(title=path.stem, path=rel_path, aliases=())

    fm, _ = split_frontmatter(text)
    if not fm:
        return None

    title = ""
    aliases: list[str] = []
    lines = fm.splitlines()
    i = 1
    while i < len(lines):
        line = lines[i]
        if line == "---":
            break
        stripped = line.strip()
        if stripped.startswith("title:"):
            title = stripped.split(":", 1)[1].strip().strip("'\"")
        elif stripped.startswith("aliases:"):
            value = stripped.split(":", 1)[1].strip()
            if value.startswith("[") and value.endswith("]"):
                aliases.extend(x.strip().strip("'\"") for x in value[1:-1].split(",") if x.strip())
            elif value:
                aliases.append(value.strip("'\""))
            else:
                j = i + 1
                while j < len(lines):
                    child = lines[j]
                    if not child.startswith((" ", "\t")):
                        break
                    child_stripped = child.strip()
                    if child_stripped.startswith("- "):
                        aliases.append(child_stripped[2:].strip().strip("'\""))
                    j += 1
                i = j - 1
        i += 1

    if not title:
        title = path.stem
    return Entry(title=title, path=rel_path, aliases=tuple(a for a in aliases if a))


def git_output(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return ""
    return result.stdout


def git_file_at_head(rel_path: str) -> str:
    return git_output(["show", f"HEAD:{rel_path}"])


def git_changed_paths() -> set[str]:
    changed = set(
        line.strip()
        for line in git_output(["diff", "--name-only", "--diff-filter=ACMRTUXB", "HEAD", "--", "wiki", "sources"]).splitlines()
        if line.strip()
    )
    untracked = set(
        line.strip()
        for line in git_output(["ls-files", "--others", "--exclude-standard", "--", "wiki", "sources"]).splitlines()
        if line.strip()
    )
    return changed | untracked


def git_changed_terms(paths: set[str]) -> tuple[set[str], set[str], set[str]]:
    changed_files: set[str] = set()
    added_terms: set[str] = set()
    removed_terms: set[str] = set()

    for rel in paths:
        path = ROOT / rel
        if path.suffix.lower() != ".md":
            continue
        if rel.startswith("wiki/"):
            if not path.exists() or should_skip_file(path):
                continue
            changed_files.add(rel)
        elif not rel.startswith("sources/"):
            continue

        current_entry = None
        if path.exists():
            current_entry = parse_entry_from_text(rel, path.read_text(encoding="utf-8", errors="ignore"))
        previous_text = git_file_at_head(rel)
        previous_entry = parse_entry_from_text(rel, previous_text) if previous_text else None

        current_terms = entry_terms(current_entry) if current_entry else set()
        previous_terms = entry_terms(previous_entry) if previous_entry else set()
        added_terms.update(current_terms - previous_terms)
        removed_terms.update(previous_terms - current_terms)

    return changed_files, added_terms, removed_terms


def iter_git_target_files() -> list[Path]:
    paths = git_changed_paths()
    changed_files, added_terms, removed_terms = git_changed_terms(paths)
    search_terms = {t for t in added_terms | removed_terms if t}

    candidates = {ROOT / rel for rel in changed_files}
    if search_terms:
        for path in iter_target_files([]):
            text = path.read_text(encoding="utf-8", errors="ignore")
            if any(term in text for term in search_terms):
                candidates.add(path)

    return sorted(p for p in candidates if p.exists() and not should_skip_file(p))


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---", 4)
    if end == -1:
        return "", text
    end += len("\n---")
    if end < len(text) and text[end] == "\n":
        end += 1
    return text[:end], text[end:]


def split_h2_sections(body: str) -> list[tuple[str, str]]:
    """Return [(h2_heading_or_empty, section_text_including_heading)]."""
    matches = list(re.finditer(r"(?m)^## (?!#).*$", body))
    if not matches:
        return [("", body)]

    sections: list[tuple[str, str]] = []
    if matches[0].start() > 0:
        sections.append(("", body[: matches[0].start()]))

    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        sections.append((m.group(0), body[start:end]))
    return sections


def is_source_section_heading(heading: str) -> bool:
    if not heading:
        return False
    title = heading[3:].strip().lower() if heading.startswith("## ") else heading.strip().lower()
    return title in SOURCE_SECTION_NAMES


def split_protected_spans(text: str) -> list[tuple[bool, str]]:
    """
    Split section text into (protected, chunk).

    Protected chunks are not edited. This avoids frontmatter/body handled elsewhere,
    code blocks, headings, quote callouts, HTML, URLs/DOIs, Markdown links,
    existing wikilinks, and embeds. Non-quote Obsidian callouts remain linkable.
    """
    protected: list[tuple[int, int]] = []

    def add(start: int, end: int) -> None:
        if start < end:
            protected.append((start, end))

    # Fenced code blocks.
    for m in re.finditer(r"(?ms)^```.*?^```\s*", text):
        add(m.start(), m.end())

    # Headings line-by-line. Also skip all lines in quote callouts.
    in_quote_callout = False
    pos = 0
    for line in text.splitlines(keepends=True):
        start, end = pos, pos + len(line)
        stripped = line.lstrip()
        if re.match(r"^#{1,6}\s", stripped):
            add(start, end)
        if re.match(r"^>\s*\[!quote\]", stripped, re.IGNORECASE):
            in_quote_callout = True
        if in_quote_callout and stripped.startswith(">"):
            add(start, end)
        elif in_quote_callout:
            in_quote_callout = False
        pos = end

    for rx in (EMBED_RE, WIKILINK_RE, MD_LINK_RE, URL_RE, HTML_TAG_RE):
        for m in rx.finditer(text):
            add(m.start(), m.end())

    if not protected:
        return [(False, text)]

    protected.sort()
    merged: list[tuple[int, int]] = []
    for start, end in protected:
        if not merged or start > merged[-1][1]:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))

    chunks: list[tuple[bool, str]] = []
    cursor = 0
    for start, end in merged:
        if cursor < start:
            chunks.append((False, text[cursor:start]))
        chunks.append((True, text[start:end]))
        cursor = end
    if cursor < len(text):
        chunks.append((False, text[cursor:]))
    return chunks


def current_file_title(path: Path, path_to_title: dict[str, str]) -> str:
    rel = rel_to_root(path)
    return path_to_title.get(rel, path.stem)


def clean_invalid_links_in_text(text: str, entries_by_title: dict[str, Entry]) -> tuple[str, int]:
    removed = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal removed
        target = m.group(1).strip()
        display = m.group(2)
        if target not in entries_by_title:
            removed += 1
            return display if display is not None else target

        if display is not None and is_standalone_cjk_alias(display, entries_by_title[target]):
            if not valid_boundary(text, m.start(), m.end(), display):
                removed += 1
                return display

        if display is not None:
            display_clean = display.strip()
            entry = entries_by_title[target]
            valid_displays = {entry.title, *entry.aliases}
            if display_clean not in valid_displays:
                removed += 1
                return display
        return m.group(0)

    return WIKILINK_RE.sub(repl, text), removed


def clean_invalid_links(body: str, entries_by_title: dict[str, Entry]) -> tuple[str, int]:
    cleaned_sections: list[str] = []
    removed = 0

    for heading, section in split_h2_sections(body):
        if is_source_section_heading(heading):
            cleaned_sections.append(section)
            continue
        cleaned, count = clean_invalid_links_in_text(section, entries_by_title)
        cleaned_sections.append(cleaned)
        removed += count

    return "".join(cleaned_sections), removed


def is_ascii_word_char(ch: str) -> bool:
    return ch.isascii() and (ch.isalnum() or ch == "_")


def is_cjk(ch: str) -> bool:
    return "\u4e00" <= ch <= "\u9fff"


def is_standalone_cjk_alias(text: str, entry: Entry) -> bool:
    return len(text) == 1 and is_cjk(text) and text in set(entry.aliases)


def valid_boundary(text: str, start: int, end: int, term: str) -> bool:
    before = text[start - 1] if start > 0 else ""
    after = text[end] if end < len(text) else ""

    # For Latin-like terms, prevent partial-word matches.
    if any(ch.isascii() and ch.isalnum() for ch in term):
        if before and is_ascii_word_char(before):
            return False
        if after and is_ascii_word_char(after):
            return False

    # Single-character CJK aliases are meaningful, but only when they stand
    # alone. This prevents 義/熟/精/圣 from linking inside 定义/成熟/精英/圣杯.
    if len(term) == 1 and is_cjk(term):
        if before and is_cjk(before):
            return False
        if after and is_cjk(after):
            return False

    # Multi-character CJK terms may be adjacent because Chinese does not use
    # spaces. Longest-first matching handles most overlap cases.
    return True


def link_text(display: str, target: str) -> str:
    if display == target:
        return f"[[{target}]]"
    return f"[[{target}|{display}]]"


def link_section(section: str, terms: list[Term], current_title: str, already_linked: set[str]) -> tuple[str, int]:
    additions = 0
    chunks = split_protected_spans(section)
    out: list[str] = []

    for protected, chunk in chunks:
        if protected:
            for m in WIKILINK_RE.finditer(chunk):
                already_linked.add(m.group(1).strip())
            out.append(chunk)
            continue
        if not chunk:
            continue

        i = 0
        new_chunk: list[str] = []
        while i < len(chunk):
            matched: Term | None = None
            for term in terms:
                if term.target == current_title or term.target in already_linked:
                    continue
                if not chunk.startswith(term.text, i):
                    continue
                if not valid_boundary(chunk, i, i + len(term.text), term.text):
                    continue
                matched = term
                break

            if matched is None:
                new_chunk.append(chunk[i])
                i += 1
                continue

            new_chunk.append(link_text(matched.text, matched.target))
            already_linked.add(matched.target)
            additions += 1
            i += len(matched.text)

        out.append("".join(new_chunk))

    return "".join(out), additions


def link_source_section(section: str, source_pattern: re.Pattern[str] | None) -> tuple[str, int]:
    # Source sections are bibliography-like lists: only canonical source IDs are linked here.
    if source_pattern is None:
        return section, 0
    additions = 0
    chunks = split_protected_spans(section)
    out: list[str] = []

    def repl(m: re.Match[str]) -> str:
        nonlocal additions
        source_id = m.group(1)
        additions += 1
        return f"[[{source_id}]]"

    for protected, chunk in chunks:
        if protected:
            out.append(chunk)
        else:
            out.append(source_pattern.sub(repl, chunk))

    return "".join(out), additions


def link_body(body: str, terms: list[Term], source_pattern: re.Pattern[str] | None, current_title: str) -> tuple[str, int]:
    sections = split_h2_sections(body)
    linked_sections: list[str] = []
    additions = 0

    for heading, section in sections:
        if is_source_section_heading(heading):
            linked, added = link_source_section(section, source_pattern)
            linked_sections.append(linked)
            additions += added
            continue

        # Track links as we encounter them left-to-right so the first mention in
        # a ## section gets linked even when a later mention was already linked.
        already_linked: set[str] = set()
        linked, added = link_section(section, terms, current_title, already_linked)
        linked_sections.append(linked)
        additions += added

    return "".join(linked_sections), additions


def sync_file(
    path: Path,
    terms: list[Term],
    source_pattern: re.Pattern[str] | None,
    entries_by_title: dict[str, Entry],
    path_to_title: dict[str, str],
    dry_run: bool,
) -> tuple[bool, int, int]:
    original = path.read_text(encoding="utf-8", errors="ignore")
    fm, body = split_frontmatter(original)
    current_title = current_file_title(path, path_to_title)

    cleaned_body, removed = clean_invalid_links(body, entries_by_title)
    linked_body, added = link_body(cleaned_body, terms, source_pattern, current_title)
    updated = fm + linked_body

    changed = updated != original
    if changed and not dry_run:
        path.write_text(updated, encoding="utf-8")
    return changed, added, removed


def run_sync(paths: list[str], dry_run: bool, git_only: bool) -> None:
    if git_only and paths:
        raise SystemExit("`sync --git` does not accept explicit paths; use either --git or paths.")

    entries = load_entries()
    source_entries = load_source_entries()
    terms, entries_by_title, path_to_title = make_terms(entries)
    for source in source_entries:
        entries_by_title.setdefault(source.title, source)
    source_pattern = make_source_pattern({source.title for source in source_entries})
    files = iter_git_target_files() if git_only else iter_target_files(paths)

    stats = LinkStats()
    for path in files:
        changed, added, removed = sync_file(path, terms, source_pattern, entries_by_title, path_to_title, dry_run)
        if changed:
            stats.files_changed += 1
            stats.links_added += added
            stats.links_removed += removed
            action = "Would update" if dry_run else "Updated"
            print(f"{action}: {path.relative_to(ROOT)} (+{added}, -{removed})")

    print("Done.")
    print(f"Files scanned: {len(files)}")
    print(f"Files changed: {stats.files_changed}")
    print(f"Links added: {stats.links_added}")
    print(f"Links removed: {stats.links_removed}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Synchronize Obsidian wikilinks from wiki/index.json."
    )
    sub = parser.add_subparsers(dest="command")

    sync = sub.add_parser("sync", help="Clean invalid links and add missing wikilinks.")
    sync.add_argument("paths", nargs="*", help="Optional file or directory paths relative to vault root.")
    sync.add_argument("--dry-run", action="store_true", help="Show changes without writing files.")
    sync.add_argument("--git", action="store_true", help="Only process files affected by git changes.")

    return parser


def main() -> None:
    if not WIKI_DIR.exists():
        raise SystemExit(f"wiki directory not found: {WIKI_DIR}")
    parser = build_parser()
    args = parser.parse_args()
    if args.command in {None, "sync"}:
        run_sync(getattr(args, "paths", []), getattr(args, "dry_run", False), getattr(args, "git", False))
    else:
        parser.error(f"unknown command: {args.command}")


if __name__ == "__main__":
    main()
