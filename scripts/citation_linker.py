#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
citation_linker.py

Link unlinked APA short citations in wiki Markdown body text.

Reads only:
  citation/citation_full.json
  citation/citation_ambiguous.json
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
CITATION_FULL_JSON = ROOT / "citation" / "citation_full.json"

FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.S)
WIKILINK_RE = re.compile(r"\[\[[^\]]+\]\]")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
OBSIDIAN_COMMENT_RE = re.compile(r"%%.*?%%", re.S)
CODE_FENCE_RE = re.compile(r"```.*?```", re.S)

AUTHOR_PATTERN = r"[A-Z\u3400-\u9fff][A-Za-zÀ-ÖØ-öø-ÿ\u3400-\u9fff0-9'’ .&和等-]*(?:\s+(?:&|and)\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ0-9'’ .-]+|\s+et\s+al\.)?"
PAREN_GROUP_RE = re.compile(r"(?<!\[)\(([^()\n]*\b\d{4}[a-z]?[^()\n]*)\)")
FULLWIDTH_PAREN_GROUP_RE = re.compile(r"（([^（）\n]*\b\d{4}[a-z]?[^（）\n]*)）")
PAREN_ITEM_RE = re.compile(
    r"^\s*"
    rf"(?P<author>{AUTHOR_PATTERN})"
    r"\s*[,，]\s*"
    r"(?P<year>\d{4}[a-z]?)"
    r"(?P<locator>\s*[,，]\s*(?:p\.|pp\.)\s*.+)?"
    r"\s*$"
)
NARRATIVE_RE = re.compile(
    r"(?<![\w\]\)])"
    rf"(?P<author>{AUTHOR_PATTERN})"
    r"\s*[（(]"
    r"(?P<year>\d{4}[a-z]?)"
    r"(?P<locator>\s*[,，]\s*(?:p\.|pp\.)\s*[^)）]+)?"
    r"[）)]"
)


def run_git_changed() -> list[Path] | None:
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        return None
    paths: list[Path] = []
    for line in result.stdout.splitlines():
        path = ROOT / line.strip()
        if path.suffix.lower() == ".md" and WIKI_DIR in path.parents and path.exists():
            paths.append(path)
    return paths


def iter_target_markdown(full: bool) -> list[Path]:
    if full:
        return sorted(WIKI_DIR.rglob("*.md")) if WIKI_DIR.exists() else []
    changed = run_git_changed()
    return sorted(set(changed)) if changed else sorted(WIKI_DIR.rglob("*.md"))


def should_skip(path: Path) -> bool:
    return "templates" in path.parts or path.name == "index.md"


def load_lookup() -> dict[str, dict[str, Any]]:
    data = json.loads(CITATION_FULL_JSON.read_text(encoding="utf-8"))
    items = data.get("items", data) if isinstance(data, dict) else {}
    lookup: dict[str, dict[str, Any]] = {}

    def add_key(alias: str, entry: dict[str, Any]) -> None:
        lookup[alias] = entry
        lookup[normalize_citation_alias(alias)] = entry

    if isinstance(items, dict):
        for alias, entry in items.items():
            if isinstance(entry, dict):
                add_key(str(alias), entry)
                for extra in entry.get("aliases") or []:
                    add_key(str(extra), entry)
    return lookup


def normalize_citation_alias(alias: str) -> str:
    alias = re.sub(r"\s+", " ", alias).strip()
    return re.sub(r"\s+(?:&|and)\s+", " & ", alias)


def normalize_author(author: str) -> str:
    return normalize_citation_alias(author)


def normalize_display_author(author: str) -> str:
    return re.sub(r"\s+", " ", author).strip()


def normalize_locator(locator: str) -> str:
    locator = locator.replace("，", ",")
    return re.sub(r"^\s*,\s*", ", ", locator)


def split_frontmatter(text: str) -> tuple[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return text[:m.end()], text[m.end():]


def mask_protected(text: str) -> tuple[str, list[str]]:
    protected: list[str] = []

    def repl(m: re.Match[str]) -> str:
        protected.append(m.group(0))
        return f"\uE000{len(protected) - 1}\uE001"

    for rx in [CODE_FENCE_RE, HTML_COMMENT_RE, OBSIDIAN_COMMENT_RE, WIKILINK_RE, INLINE_CODE_RE]:
        text = rx.sub(repl, text)
    return text, protected


def unmask(text: str, protected: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        return protected[int(m.group(1))]
    return re.sub(r"\uE000(\d+)\uE001", repl, text)


def link_target(entry: dict[str, Any], display: str) -> str:
    return f"[[{entry['argument']}|{display}]]"


def link_parenthetical_group(content: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str | None:
    parts = content.split(";")
    linked_parts: list[str] = []
    changed = False
    for raw in parts:
        item = raw.strip()
        m = PAREN_ITEM_RE.match(item)
        if not m:
            return None
        display_author = normalize_display_author(m.group("author"))
        author = normalize_author(display_author)
        year = m.group("year").strip()
        locator = normalize_locator(m.group("locator") or "")
        key = f"{author}, {year}"
        entry = lookup.get(key)
        if not entry:
            missing.append(key)
            linked_parts.append(item)
            continue
        linked_parts.append(link_target(entry, f"{display_author}, {year}{locator}"))
        changed = True
    if not changed:
        return None
    stats["linked_parenthetical"] += 1
    return "(" + "; ".join(linked_parts) + ")"


def link_parenthetical(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        linked = link_parenthetical_group(m.group(1), lookup, stats, missing)
        return linked or m.group(0)

    text = PAREN_GROUP_RE.sub(repl, text)
    text = FULLWIDTH_PAREN_GROUP_RE.sub(repl, text)
    return text


def link_narrative(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        display_author = normalize_display_author(m.group("author"))
        author = normalize_author(display_author)
        year = m.group("year").strip()
        locator = normalize_locator(m.group("locator") or "")
        key = f"{author} ({year})"
        entry = lookup.get(key)
        if not entry:
            missing.append(key)
            return m.group(0)
        stats["linked_narrative"] += 1
        return link_target(entry, f"{display_author} ({year}{locator})")
    return NARRATIVE_RE.sub(repl, text)


def link_text(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    fm, body = split_frontmatter(text)
    masked, protected = mask_protected(body)
    masked = link_parenthetical(masked, lookup, stats, missing)
    masked = link_narrative(masked, lookup, stats, missing)
    return fm + unmask(masked, protected)


def main() -> int:
    parser = argparse.ArgumentParser(description="Link APA short citations to Argument pages.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing.")
    parser.add_argument("--full", action="store_true", help="Process all wiki Markdown files.")
    args = parser.parse_args()

    if not CITATION_FULL_JSON.exists():
        print("❌ citation/citation_full.json missing; run scripts/citation_index.py first.")
        return 1

    lookup = load_lookup()
    stats = {"linked_parenthetical": 0, "linked_narrative": 0}
    missing: list[str] = []
    changed = 0
    for path in iter_target_markdown(full=args.full):
        if should_skip(path):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        before = dict(stats)
        new_text = link_text(text, lookup, stats, missing)
        if new_text != text:
            changed += 1
            rel = path.relative_to(ROOT)
            print(f"✏️  {rel} parenthetical={stats['linked_parenthetical'] - before['linked_parenthetical']} narrative={stats['linked_narrative'] - before['linked_narrative']}")
            if not args.dry_run:
                path.write_text(new_text, encoding="utf-8")

    print(f"{'[dry-run] ' if args.dry_run else ''}files changed: {changed}")
    print(f"🔗 linked parenthetical groups: {stats['linked_parenthetical']}")
    print(f"🔗 linked narrative citations: {stats['linked_narrative']}")
    if missing:
        print("⚠️ unresolved citation aliases:")
        for item in sorted(set(missing))[:200]:
            print(f"  - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
