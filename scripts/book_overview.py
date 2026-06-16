#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
book_overview.py

Maintain chapter overview table skeletons for textbook/monograph overview
Argument pages.

The script only maintains structural links in the first table column. Existing
chapter summaries and related-entry cells are preserved.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BOOKS_DIR = ROOT / "wiki" / "arguments" / "books"

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
OVERVIEW_RE = re.compile(r"^>\s*\[!textbook-overview\]")
CHAPTER_FILE_RE = re.compile(r"^(?P<parent>Argument_.+)_Ch(?P<num>\d{1,3})(?:[_-].+)?$")
CHINESE_CHAPTER_RE = re.compile(r"第\s*(?P<num>\d{1,3})\s*章")


@dataclass
class Chapter:
    path: Path
    target: str
    number: int

    @property
    def link_cell(self) -> str:
        return f"[[{self.target}\\|第{self.number}章]]"


@dataclass
class TableRow:
    cells: list[str]
    target: str = ""
    chapter_number: int | None = None
    is_separator: bool = False

    def render(self) -> str:
        rendered = "> |"
        for cell in self.cells:
            rendered += f" {cell} |" if cell else " |"
        return rendered


@dataclass
class Overview:
    path: Path
    target: str
    subtype: str
    chapters: list[Chapter]

    @property
    def rel_path(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def parse_scalar(value: str) -> str:
    value = value.strip()
    if value in {"", "null", "None", "~"}:
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        inner = value[1:-1]
        return inner.replace("''", "'") if value[0] == "'" else inner
    return value


def parse_frontmatter(text: str) -> dict[str, Any]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    data: dict[str, Any] = {}
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m_key = KEY_RE.match(line)
        if not m_key:
            i += 1
            continue
        key, val = m_key.group(1), m_key.group(2).strip()
        if val == "":
            items: list[str] = []
            j = i + 1
            while j < len(lines) and re.match(r"^\s*-\s+", lines[j]):
                items.append(parse_scalar(re.sub(r"^\s*-\s+", "", lines[j])))
                j += 1
            data[key] = items if items else ""
            i = j
        else:
            data[key] = parse_scalar(val)
            i += 1
    return data


def chapter_number_from_target(target: str) -> int | None:
    m = CHAPTER_FILE_RE.match(target)
    return int(m.group("num")) if m else None


def chapter_number_from_text(text: str) -> int | None:
    m = CHINESE_CHAPTER_RE.search(text)
    return int(m.group("num")) if m else None


def wikilink_target(text: str) -> str:
    m = re.search(r"\[\[([^|\]\\]+)(?:\\?\|[^\]]+)?\]\]", text)
    return m.group(1).strip() if m else ""


def split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith(">"):
        stripped = stripped[1:].strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]

    cells: list[str] = []
    current = ""
    escaped = False
    for ch in stripped:
        if escaped:
            current += "\\" + ch
            escaped = False
            continue
        if ch == "\\":
            escaped = True
            continue
        if ch == "|":
            cells.append(current.strip())
            current = ""
            continue
        current += ch
    if escaped:
        current += "\\"
    cells.append(current.strip())
    return cells


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def parse_table_row(line: str) -> TableRow:
    cells = split_table_row(line)
    first_link = wikilink_target(cells[0]) if cells else ""
    linked_chapter_number = chapter_number_from_target(first_link) if first_link else None
    target = first_link if linked_chapter_number is not None else ""
    number = linked_chapter_number if linked_chapter_number is not None else chapter_number_from_text(cells[0] if cells else "")
    return TableRow(
        cells=(cells + ["", ""])[:3],
        target=target,
        chapter_number=number,
        is_separator=is_separator_row(cells),
    )


def find_overview_block(lines: list[str]) -> tuple[int, int] | None:
    for i, line in enumerate(lines):
        if OVERVIEW_RE.match(line):
            j = i + 1
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            return i, j
    return None


def default_block(chapters: list[Chapter]) -> list[str]:
    rows = [
        "> [!textbook-overview] 章节总览",
        "> | 章节 | 内容概要 | 主要关联条目 |",
        "> |---|---|---|",
    ]
    rows.extend(f"> | {chapter.link_cell} | | |" for chapter in chapters)
    return rows


def update_block(block: list[str], chapters: list[Chapter]) -> tuple[list[str], list[str]]:
    table_rows: list[TableRow] = []
    non_table_lines: list[str] = []
    for line in block[1:]:
        if line.startswith("> |"):
            row = parse_table_row(line)
            if not row.is_separator and row.cells[:3] != ["章节", "内容概要", "主要关联条目"]:
                table_rows.append(row)
        else:
            non_table_lines.append(line)

    issues: list[str] = []
    actual_targets = {chapter.target for chapter in chapters}
    row_by_target = {row.target: row for row in table_rows if row.target}

    for row in table_rows:
        if row.target and row.target.startswith("Argument_") and row.target not in actual_targets:
            issues.append(f"stale chapter link: {row.target}")

    for chapter in chapters:
        if chapter.target in row_by_target:
            row_by_target[chapter.target].cells[0] = row_by_target[chapter.target].cells[0] or chapter.link_cell
            continue
        plain_row = next((row for row in table_rows if not row.target and row.chapter_number == chapter.number), None)
        if plain_row:
            issues.append(f"plain chapter row should link to: {chapter.target}")
            plain_row.cells[0] = chapter.link_cell
            plain_row.target = chapter.target
            continue
        issues.append(f"missing chapter row: {chapter.target}")
        table_rows.append(TableRow(cells=[chapter.link_cell, "", ""], target=chapter.target, chapter_number=chapter.number))

    rendered = [
        block[0],
        "> | 章节 | 内容概要 | 主要关联条目 |",
        "> |---|---|---|",
    ]
    rendered.extend(row.render() for row in table_rows)
    rendered.extend(non_table_lines)

    # Keep a stable chapter order when the table was newly created or contains
    # only generated chapter rows.
    if not table_rows and chapters:
        rendered = default_block(chapters)

    return rendered, issues


def insert_block(lines: list[str], chapters: list[Chapter]) -> tuple[list[str], bool]:
    for i, line in enumerate(lines):
        if line.strip() == "## 总览":
            insert_at = i + 1
            while insert_at < len(lines) and lines[insert_at].strip() == "":
                insert_at += 1
            while insert_at < len(lines) and not lines[insert_at].startswith("## "):
                if lines[insert_at].startswith("> [!"):
                    break
                insert_at += 1
            block = ["", *default_block(chapters)]
            return lines[:insert_at] + block + lines[insert_at:], True
    return lines + ["", "## 总览", "", *default_block(chapters)], True


def discover_overviews() -> list[Overview]:
    overviews: list[Overview] = []
    if not BOOKS_DIR.exists():
        return overviews
    for path in sorted(BOOKS_DIR.rglob("Argument_*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        meta = parse_frontmatter(text)
        if meta.get("type") != "argument":
            continue
        if meta.get("publication_type") != "book":
            continue
        if meta.get("subtype") not in {"textbook", "monograph"}:
            continue
        parent_target = path.stem
        chapters: list[Chapter] = []
        for chapter_path in sorted(path.parent.glob(f"{parent_target}_Ch*.md")):
            match = CHAPTER_FILE_RE.match(chapter_path.stem)
            if not match or match.group("parent") != parent_target:
                continue
            chapters.append(Chapter(path=chapter_path, target=chapter_path.stem, number=int(match.group("num"))))
        if chapters:
            overviews.append(Overview(path=path, target=parent_target, subtype=str(meta.get("subtype")), chapters=chapters))
    return overviews


def update_overview(overview: Overview, dry_run: bool, check: bool) -> tuple[bool, list[str]]:
    text = overview.path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    block_range = find_overview_block(lines)
    issues: list[str] = []
    if block_range:
        start, end = block_range
        new_block, issues = update_block(lines[start:end], overview.chapters)
        new_lines = lines[:start] + new_block + lines[end:]
    else:
        new_lines, _ = insert_block(lines, overview.chapters)
        issues.append("missing textbook-overview block")

    new_text = "\n".join(new_lines).rstrip() + "\n"
    changed = new_text != text
    if changed and not dry_run and not check:
        overview.path.write_text(new_text, encoding="utf-8")
    return changed, issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Maintain textbook/monograph chapter overview table skeletons.")
    parser.add_argument("--dry-run", action="store_true", help="Show files that would change without writing.")
    parser.add_argument("--check", action="store_true", help="Fail if overview tables are stale or missing.")
    args = parser.parse_args(argv)

    overviews = discover_overviews()
    changed_count = 0
    issue_count = 0
    for overview in overviews:
        changed, issues = update_overview(overview, dry_run=args.dry_run, check=args.check)
        if changed:
            changed_count += 1
            prefix = "would update" if args.dry_run or args.check else "updated"
            print(f"📚 {prefix}: {overview.rel_path}")
        for issue in issues:
            issue_count += 1
            print(f"⚠️  {overview.rel_path}: {issue}")

    print(f"📖 book overviews with chapter files: {len(overviews)}")
    if args.check:
        return 1 if changed_count or issue_count else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
