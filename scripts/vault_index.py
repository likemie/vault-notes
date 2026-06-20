#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

"""
vault_index.py

Run the vault's base index maintenance in the required order:
  1. Maintain textbook/monograph overview chapter tables.
  2. scripts/wiki_index.py
  3. scripts/citation_index.py

This file is the daily unified entry point. Larger generated surfaces that
already have mature boundaries still live in their own scripts.
"""

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

VAULT_ROOT = Path("/Users/shaoyangwu/Documents/MyNotes")
VENV_PYTHON = VAULT_ROOT / ".venv" / "bin" / "python"

if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
BOOKS_DIR = ROOT / "wiki" / "arguments" / "books"
ARGUMENTS_DIR = ROOT / "wiki" / "arguments"
CONCEPTS_DIR = ROOT / "wiki" / "concepts"
METHODS_DIR = ROOT / "wiki" / "methods"
THEORIES_DIR = ROOT / "wiki" / "theories"

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
SPLIT_FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
OVERVIEW_RE = re.compile(r"^>\s*\[!textbook-overview\]")
CHAPTER_FILE_RE = re.compile(r"^(?P<parent>Argument_.+)_Ch(?P<num>\d{1,3})(?:[_-].+)?$")
CHINESE_CHAPTER_RE = re.compile(r"第\s*(?P<num>\d{1,3})\s*章")
CONCEPT_GENERATED_KEYS = {"domain", "related_count", "related_level", "related_stars", "related_color"}
CONCEPT_COLORS = ["#e5e7eb", "#bfdbfe", "#99f6e4", "#fde68a", "#fdba74", "#fecdd3", "#ddd6fe"]
METHOD_GENERATED_KEYS = {
    "method_family",
    "method_related_count",
    "method_related_level",
    "method_related_stars",
    "method_related_color",
}
METHOD_COLORS = {
    "qualitative": "#dbeafe",
    "quantitative": "#dcfce7",
    "mixed": "#fef3c7",
}
THEORY_GENERATED_KEYS = {
    "theory_field",
    "theory_related_count",
    "theory_related_level",
    "theory_related_stars",
    "theory_related_color",
}
THEORY_COLORS = ["#e5e7eb", "#dbeafe", "#e0e7ff", "#ede9fe", "#fce7f3", "#ffedd5", "#fef3c7"]
ARGUMENT_GENERATED_KEYS = {
    "title",
    "argument_display_title",
    "argument_kind",
    "argument_related_count",
    "argument_related_level",
    "argument_related_stars",
    "argument_related_color",
}
ARGUMENT_COLORS = {
    "journal-article": "#dbeafe",
    "book": "#ede9fe",
    "book-chapter": "#fef3c7",
    "report": "#dcfce7",
    "policy-document": "#ffedd5",
}


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
class BookOverview:
    path: Path
    target: str
    chapters: list[Chapter]

    @property
    def rel_path(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def run_script(script_name: str, extra_args: list[str] | None = None) -> int:
    cmd = [sys.executable, str(SCRIPTS_DIR / script_name)]
    if extra_args:
        cmd.extend(extra_args)

    print(f"$ {Path(sys.executable).name} scripts/{script_name}" + (f" {' '.join(extra_args)}" if extra_args else ""), flush=True)
    completed = subprocess.run(cmd, cwd=ROOT)
    return completed.returncode


def parse_scalar(value: str) -> str:
    value = value.strip()
    if value in {"", "null", "None", "~"}:
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        inner = value[1:-1]
        return inner.replace("''", "'") if value[0] == "'" else inner
    return value


def parse_inline_list(value: str) -> list[str]:
    inner = value[1:-1].strip()
    if not inner:
        return []
    items: list[str] = []
    current = ""
    quote = ""
    for ch in inner:
        if ch in {"'", '"'}:
            quote = "" if quote == ch else ch if not quote else quote
            current += ch
        elif ch == "," and not quote:
            items.append(parse_scalar(current))
            current = ""
        else:
            current += ch
    if current.strip():
        items.append(parse_scalar(current))
    return [item for item in items if item]


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
            continue
        if val.startswith("[") and val.endswith("]"):
            data[key] = parse_inline_list(val)
        else:
            data[key] = parse_scalar(val)
        i += 1
    return data


def split_frontmatter(text: str) -> tuple[str, str] | None:
    m = SPLIT_FRONTMATTER_RE.match(text)
    if not m:
        return None
    return m.group(1), text[m.end():]


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


def default_overview_block(chapters: list[Chapter]) -> list[str]:
    rows = [
        "> [!textbook-overview] 章节总览",
        "> | 章节 | 内容概要 | 主要关联条目 |",
        "> |---|---|---|",
    ]
    rows.extend(f"> | {chapter.link_cell} | | |" for chapter in chapters)
    return rows


def update_overview_block(block: list[str], chapters: list[Chapter]) -> tuple[list[str], list[str]]:
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

    if not table_rows and chapters:
        rendered = default_overview_block(chapters)

    return rendered, issues


def insert_overview_block(lines: list[str], chapters: list[Chapter]) -> list[str]:
    for i, line in enumerate(lines):
        if line.strip() == "## 总览":
            insert_at = i + 1
            while insert_at < len(lines) and lines[insert_at].strip() == "":
                insert_at += 1
            while insert_at < len(lines) and not lines[insert_at].startswith("## "):
                if lines[insert_at].startswith("> [!"):
                    break
                insert_at += 1
            return lines[:insert_at] + ["", *default_overview_block(chapters)] + lines[insert_at:]
    return lines + ["", "## 总览", "", *default_overview_block(chapters)]


def discover_book_overviews() -> list[BookOverview]:
    overviews: list[BookOverview] = []
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
            if match and match.group("parent") == parent_target:
                chapters.append(Chapter(path=chapter_path, target=chapter_path.stem, number=int(match.group("num"))))
        if chapters:
            overviews.append(BookOverview(path=path, target=parent_target, chapters=chapters))
    return overviews


def update_book_overview(overview: BookOverview, dry_run: bool, check: bool) -> tuple[bool, list[str]]:
    text = overview.path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    block_range = find_overview_block(lines)
    issues: list[str] = []
    if block_range:
        start, end = block_range
        new_block, issues = update_overview_block(lines[start:end], overview.chapters)
        new_lines = lines[:start] + new_block + lines[end:]
    else:
        new_lines = insert_overview_block(lines, overview.chapters)
        issues.append("missing textbook-overview block")

    new_text = "\n".join(new_lines).rstrip() + "\n"
    changed = new_text != text
    if changed and not dry_run and not check:
        overview.path.write_text(new_text, encoding="utf-8")
    return changed, issues


def maintain_book_overviews(dry_run: bool = False, check: bool = False) -> int:
    overviews = discover_book_overviews()
    changed_count = 0
    issue_count = 0
    for overview in overviews:
        changed, issues = update_book_overview(overview, dry_run=dry_run, check=check)
        if changed:
            changed_count += 1
            prefix = "would update" if dry_run or check else "updated"
            print(f"📚 {prefix}: {overview.rel_path}")
        for issue in issues:
            issue_count += 1
            print(f"⚠️  {overview.rel_path}: {issue}")

    print(f"📖 book overviews with chapter files: {len(overviews)}")
    if check:
        return 1 if changed_count or issue_count else 0
    return 0


def count_related_fields(meta: dict[str, Any]) -> int:
    total = 0
    for key, value in meta.items():
        if not key.startswith("related_") or key in CONCEPT_GENERATED_KEYS:
            continue
        if isinstance(value, list):
            total += sum(1 for item in value if str(item).strip())
        elif value is not None and str(value).strip():
            total += 1
    return total


def concept_stars_for(count: int) -> tuple[int, str]:
    if count <= 9:
        return 0, "☆"
    if count >= 100:
        return 6, "⭐" * 6
    level = min(5, count // 10)
    return level, "⭐" * level


def yaml_string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def upsert_concept_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    lines = raw_frontmatter.replace("\n", "\n").rstrip("\n").splitlines()
    filtered: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m_key = KEY_RE.match(line)
        if m_key and m_key.group(1) in CONCEPT_GENERATED_KEYS:
            i += 1
            while i < len(lines) and re.match(r"^(?:\s+|-\s)", lines[i]):
                i += 1
            continue
        filtered.append(line)
        i += 1

    insert_at = 0
    for idx, line in enumerate(filtered):
        if re.match(r"^type:\s*", line):
            insert_at = idx + 1
            break

    generated = [
        f"domain: {yaml_string(str(fields['domain']))}",
        f"related_count: {int(fields['related_count'])}",
        f"related_level: {int(fields['related_level'])}",
        f"related_stars: {yaml_string(str(fields['related_stars']))}",
        f"related_color: {yaml_string(str(fields['related_color']))}",
    ]
    filtered[insert_at:insert_at] = generated
    return "\n".join(filtered).rstrip() + "\n"


def iter_concept_files() -> list[Path]:
    if not CONCEPTS_DIR.exists():
        return []
    return sorted(path for path in CONCEPTS_DIR.rglob("*.md") if path.is_file())


def update_concept_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = path.read_text(encoding="utf-8", errors="replace")
    split = split_frontmatter(text)
    if not split:
        return False, None
    raw_frontmatter, body = split
    meta = parse_frontmatter(text)
    if meta.get("type") != "concept":
        return False, None
    try:
        domain = path.relative_to(CONCEPTS_DIR).parts[0]
    except (IndexError, ValueError):
        domain = ""
    related_count = count_related_fields(meta)
    related_level, related_stars = concept_stars_for(related_count)
    next_frontmatter = upsert_concept_generated_fields(raw_frontmatter, {
        "domain": domain,
        "related_count": related_count,
        "related_level": related_level,
        "related_stars": related_stars,
        "related_color": CONCEPT_COLORS[related_level],
    })
    next_text = f"---\n{next_frontmatter}---\n{body}"
    changed = next_text != text
    if changed and not dry_run and not check:
        path.write_text(next_text, encoding="utf-8")
    return changed, (related_count, related_stars)


def maintain_concept_base_fields(dry_run: bool = False, check: bool = False) -> int:
    changed_count = 0
    summaries: list[tuple[int, str, str]] = []
    for path in iter_concept_files():
        changed, summary = update_concept_base_fields(path, dry_run=dry_run, check=check)
        if summary:
            related_count, related_stars = summary
            rel_path = path.relative_to(ROOT).as_posix()
            summaries.append((related_count, related_stars, rel_path))
        if changed:
            changed_count += 1
            prefix = "would update" if dry_run or check else "updated"
            print(f"✨ {prefix}: {path.relative_to(ROOT).as_posix()}")

    summaries.sort(key=lambda item: item[0], reverse=True)
    print(f"✨ concept base fields checked: {len(summaries)}; changed: {changed_count}")
    for related_count, related_stars, rel_path in summaries[:10]:
        print(f"{related_count:>3} {related_stars:<6} {rel_path}")
    if check:
        return 1 if changed_count else 0
    return 0


def method_family_for(path: Path, meta: dict[str, Any]) -> str:
    method_type = str(meta.get("method_type") or "").strip()
    if method_type:
        return method_type
    try:
        return path.relative_to(METHODS_DIR).parts[0]
    except (IndexError, ValueError):
        return "other"


def method_stars_for(count: int) -> tuple[int, str]:
    if count <= 4:
        return 0, "☆"
    if count >= 50:
        return 6, "⭐" * 6
    level = min(5, count // 8)
    return level, "⭐" * level


def upsert_method_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    lines = raw_frontmatter.replace("\n", "\n").rstrip("\n").splitlines()
    filtered: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m_key = KEY_RE.match(line)
        if m_key and m_key.group(1) in METHOD_GENERATED_KEYS:
            i += 1
            while i < len(lines) and re.match(r"^(?:\s+|-\s)", lines[i]):
                i += 1
            continue
        filtered.append(line)
        i += 1

    insert_at = 0
    for idx, line in enumerate(filtered):
        if re.match(r"^method_type:\s*", line):
            insert_at = idx + 1
            break
        if re.match(r"^type:\s*", line):
            insert_at = idx + 1

    generated = [
        f"method_family: {yaml_string(str(fields['method_family']))}",
        f"method_related_count: {int(fields['method_related_count'])}",
        f"method_related_level: {int(fields['method_related_level'])}",
        f"method_related_stars: {yaml_string(str(fields['method_related_stars']))}",
        f"method_related_color: {yaml_string(str(fields['method_related_color']))}",
    ]
    filtered[insert_at:insert_at] = generated
    return "\n".join(filtered).rstrip() + "\n"


def iter_method_files() -> list[Path]:
    if not METHODS_DIR.exists():
        return []
    return sorted(path for path in METHODS_DIR.rglob("*.md") if path.is_file())


def update_method_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = path.read_text(encoding="utf-8", errors="replace")
    split = split_frontmatter(text)
    if not split:
        return False, None
    raw_frontmatter, body = split
    meta = parse_frontmatter(text)
    if meta.get("type") != "method":
        return False, None
    family = method_family_for(path, meta)
    related_count = count_related_fields(meta)
    related_level, related_stars = method_stars_for(related_count)
    next_frontmatter = upsert_method_generated_fields(raw_frontmatter, {
        "method_family": family,
        "method_related_count": related_count,
        "method_related_level": related_level,
        "method_related_stars": related_stars,
        "method_related_color": METHOD_COLORS.get(family, "#e5e7eb"),
    })
    next_text = f"---\n{next_frontmatter}---\n{body}"
    changed = next_text != text
    if changed and not dry_run and not check:
        path.write_text(next_text, encoding="utf-8")
    return changed, (related_count, related_stars)


def maintain_method_base_fields(dry_run: bool = False, check: bool = False) -> int:
    changed_count = 0
    summaries: list[tuple[int, str, str]] = []
    for path in iter_method_files():
        changed, summary = update_method_base_fields(path, dry_run=dry_run, check=check)
        if summary:
            related_count, related_stars = summary
            rel_path = path.relative_to(ROOT).as_posix()
            summaries.append((related_count, related_stars, rel_path))
        if changed:
            changed_count += 1
            prefix = "would update" if dry_run or check else "updated"
            print(f"🧭 {prefix}: {path.relative_to(ROOT).as_posix()}")

    summaries.sort(key=lambda item: item[0], reverse=True)
    print(f"🧭 method base fields checked: {len(summaries)}; changed: {changed_count}")
    for related_count, related_stars, rel_path in summaries[:10]:
        print(f"{related_count:>3} {related_stars:<6} {rel_path}")
    if check:
        return 1 if changed_count else 0
    return 0


def theory_field_for(path: Path) -> str:
    try:
        return path.relative_to(THEORIES_DIR).parts[0]
    except (IndexError, ValueError):
        return "other"


def theory_stars_for(count: int) -> tuple[int, str]:
    if count <= 4:
        return 0, "☆"
    if count >= 50:
        return 6, "⭐" * 6
    level = min(5, count // 8)
    return level, "⭐" * level


def upsert_theory_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    lines = raw_frontmatter.replace("\n", "\n").rstrip("\n").splitlines()
    filtered: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m_key = KEY_RE.match(line)
        if m_key and m_key.group(1) in THEORY_GENERATED_KEYS:
            i += 1
            while i < len(lines) and re.match(r"^(?:\s+|-\s)", lines[i]):
                i += 1
            continue
        filtered.append(line)
        i += 1

    insert_at = 0
    for idx, line in enumerate(filtered):
        if re.match(r"^type:\s*", line):
            insert_at = idx + 1
            break

    generated = [
        f"theory_field: {yaml_string(str(fields['theory_field']))}",
        f"theory_related_count: {int(fields['theory_related_count'])}",
        f"theory_related_level: {int(fields['theory_related_level'])}",
        f"theory_related_stars: {yaml_string(str(fields['theory_related_stars']))}",
        f"theory_related_color: {yaml_string(str(fields['theory_related_color']))}",
    ]
    filtered[insert_at:insert_at] = generated
    return "\n".join(filtered).rstrip() + "\n"


def iter_theory_files() -> list[Path]:
    if not THEORIES_DIR.exists():
        return []
    return sorted(path for path in THEORIES_DIR.rglob("*.md") if path.is_file())


def update_theory_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = path.read_text(encoding="utf-8", errors="replace")
    split = split_frontmatter(text)
    if not split:
        return False, None
    raw_frontmatter, body = split
    meta = parse_frontmatter(text)
    if meta.get("type") != "theory":
        return False, None
    field = theory_field_for(path)
    related_count = count_related_fields(meta)
    related_level, related_stars = theory_stars_for(related_count)
    next_frontmatter = upsert_theory_generated_fields(raw_frontmatter, {
        "theory_field": field,
        "theory_related_count": related_count,
        "theory_related_level": related_level,
        "theory_related_stars": related_stars,
        "theory_related_color": THEORY_COLORS[related_level],
    })
    next_text = f"---\n{next_frontmatter}---\n{body}"
    changed = next_text != text
    if changed and not dry_run and not check:
        path.write_text(next_text, encoding="utf-8")
    return changed, (related_count, related_stars)


def maintain_theory_base_fields(dry_run: bool = False, check: bool = False) -> int:
    changed_count = 0
    summaries: list[tuple[int, str, str]] = []
    for path in iter_theory_files():
        changed, summary = update_theory_base_fields(path, dry_run=dry_run, check=check)
        if summary:
            related_count, related_stars = summary
            rel_path = path.relative_to(ROOT).as_posix()
            summaries.append((related_count, related_stars, rel_path))
        if changed:
            changed_count += 1
            prefix = "would update" if dry_run or check else "updated"
            print(f"🪜 {prefix}: {path.relative_to(ROOT).as_posix()}")

    summaries.sort(key=lambda item: item[0], reverse=True)
    print(f"🪜 theory base fields checked: {len(summaries)}; changed: {changed_count}")
    for related_count, related_stars, rel_path in summaries[:10]:
        print(f"{related_count:>3} {related_stars:<6} {rel_path}")
    if check:
        return 1 if changed_count else 0
    return 0


def argument_kind_for(path: Path, meta: dict[str, Any]) -> str:
    publication_type = str(meta.get("publication_type") or "").strip()
    subtype = str(meta.get("subtype") or "").strip()
    if publication_type:
        return publication_type
    if subtype:
        return subtype
    try:
        return path.relative_to(ARGUMENTS_DIR).parts[0]
    except (IndexError, ValueError):
        return "other"


def argument_stars_for(count: int) -> tuple[int, str]:
    if count <= 9:
        return 0, "☆"
    if count >= 100:
        return 6, "⭐" * 6
    level = min(5, count // 15)
    return level, "⭐" * level


def argument_color_for(kind: str, level: int) -> str:
    if level >= 5:
        return "#fecdd3"
    return ARGUMENT_COLORS.get(kind, "#e5e7eb")


def clean_citation_title(value: str) -> str:
    value = re.sub(r"https?://\S+", "", value)
    value = value.replace("*", "").replace("_", "")
    value = re.sub(r"\s+", " ", value).strip()
    return value.strip(" .")


def title_from_citation(citation: str) -> str:
    citation = clean_citation_title(citation)
    if not citation:
        return ""
    match = re.search(r"\(\d{4}[a-z]?\)\.\s+(?P<title>.+?)(?=\.\s+(?:In\s|[A-Z][^.]*(?:Journal|Review|Education|Studies|Research|Policy|Psychology|Science|Sciences|Sociology|Forecast|Development|Philosophy|Evaluation|Economics|Paideia|Intersect)\b)|\.\s*$)", citation)
    if match:
        return clean_citation_title(match.group("title"))
    match = re.search(r"\b\d{4}[a-z]?\)\.?\s+(?P<title>.+?)(?=\.\s+|$)", citation)
    if match:
        return clean_citation_title(match.group("title"))
    return ""


def argument_display_title_for(path: Path, meta: dict[str, Any]) -> str:
    book_title = str(meta.get("book_title") or "").strip()
    kind = argument_kind_for(path, meta)
    subtype = str(meta.get("subtype") or "").strip()
    if book_title and subtype in {"edited-volume", "monograph", "textbook"}:
        return book_title
    citation_title = title_from_citation(str(meta.get("citation") or ""))
    if citation_title:
        return citation_title
    if book_title and kind == "book" and subtype != "book-chapter":
        return book_title
    if book_title:
        return book_title
    title = str(meta.get("title") or "").strip()
    return title or path.stem


def upsert_argument_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    lines = raw_frontmatter.replace("\n", "\n").rstrip("\n").splitlines()
    filtered: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m_key = KEY_RE.match(line)
        if m_key and m_key.group(1) in ARGUMENT_GENERATED_KEYS:
            i += 1
            while i < len(lines) and re.match(r"^(?:\s+|-\s)", lines[i]):
                i += 1
            continue
        filtered.append(line)
        i += 1

    insert_at = 0
    for idx, line in enumerate(filtered):
        if re.match(r"^publication_type:\s*", line):
            insert_at = idx + 1
            break
        if re.match(r"^subtype:\s*", line):
            insert_at = idx + 1
        if re.match(r"^type:\s*", line) and insert_at == 0:
            insert_at = idx + 1

    generated = [
        f"title: {yaml_string(str(fields['argument_display_title']))}",
        f"argument_display_title: {yaml_string(str(fields['argument_display_title']))}",
        f"argument_kind: {yaml_string(str(fields['argument_kind']))}",
        f"argument_related_count: {int(fields['argument_related_count'])}",
        f"argument_related_level: {int(fields['argument_related_level'])}",
        f"argument_related_stars: {yaml_string(str(fields['argument_related_stars']))}",
        f"argument_related_color: {yaml_string(str(fields['argument_related_color']))}",
    ]
    filtered[insert_at:insert_at] = generated
    return "\n".join(filtered).rstrip() + "\n"


def iter_argument_files() -> list[Path]:
    if not ARGUMENTS_DIR.exists():
        return []
    return sorted(path for path in ARGUMENTS_DIR.rglob("*.md") if path.is_file())


def update_argument_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = path.read_text(encoding="utf-8", errors="replace")
    split = split_frontmatter(text)
    if not split:
        return False, None
    raw_frontmatter, body = split
    meta = parse_frontmatter(text)
    if meta.get("type") != "argument":
        return False, None
    kind = argument_kind_for(path, meta)
    related_count = count_related_fields(meta)
    related_level, related_stars = argument_stars_for(related_count)
    next_frontmatter = upsert_argument_generated_fields(raw_frontmatter, {
        "argument_display_title": argument_display_title_for(path, meta),
        "argument_kind": kind,
        "argument_related_count": related_count,
        "argument_related_level": related_level,
        "argument_related_stars": related_stars,
        "argument_related_color": argument_color_for(kind, related_level),
    })
    next_text = f"---\n{next_frontmatter}---\n{body}"
    changed = next_text != text
    if changed and not dry_run and not check:
        path.write_text(next_text, encoding="utf-8")
    return changed, (related_count, related_stars)


def maintain_argument_base_fields(dry_run: bool = False, check: bool = False) -> int:
    changed_count = 0
    summaries: list[tuple[int, str, str]] = []
    for path in iter_argument_files():
        changed, summary = update_argument_base_fields(path, dry_run=dry_run, check=check)
        if summary:
            related_count, related_stars = summary
            rel_path = path.relative_to(ROOT).as_posix()
            summaries.append((related_count, related_stars, rel_path))
        if changed:
            changed_count += 1
            prefix = "would update" if dry_run or check else "updated"
            print(f"🔎 {prefix}: {path.relative_to(ROOT).as_posix()}")

    summaries.sort(key=lambda item: item[0], reverse=True)
    print(f"🔎 argument base fields checked: {len(summaries)}; changed: {changed_count}")
    for related_count, related_stars, rel_path in summaries[:10]:
        print(f"{related_count:>3} {related_stars:<6} {rel_path}")
    if check:
        return 1 if changed_count else 0
    return 0


def run_base_index(book_check: bool = False, book_dry_run: bool = False, citation_args: list[str] | None = None) -> int:
    code = maintain_book_overviews(dry_run=book_dry_run, check=book_check)
    if code:
        return code
    code = maintain_concept_base_fields()
    if code:
        return code
    code = maintain_method_base_fields()
    if code:
        return code
    code = maintain_theory_base_fields()
    if code:
        return code
    code = maintain_argument_base_fields()
    if code:
        return code
    code = run_script("wiki_index.py")
    if code:
        return code
    return run_script("citation_index.py", citation_args or [])


def run_standard_workflow(full: bool = False) -> int:
    code = run_base_index()
    if code:
        return code

    linker_args = ["--full"] if full else []
    wiki_sync_args = ["sync", "--full"] if full else ["sync"]
    lint_args = ["--full"] if full else []

    for script_name, extra_args in [
        ("citation_linker.py", linker_args),
        ("wiki_linker.py", wiki_sync_args),
        ("wiki_relations.py", wiki_sync_args),
        ("wiki_index.py", []),
        ("vault_lint.py", lint_args),
    ]:
        code = run_script(script_name, extra_args)
        if code:
            return code
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run wiki and citation base indexes.")
    parser.add_argument("--standard-workflow", action="store_true", help="Run base index, linkers, relation sync, wiki index refresh, and lint.")
    parser.add_argument("--full-workflow", action="store_true", help="Run the full-vault version of --standard-workflow.")
    parser.add_argument("--book-only", action="store_true", help="Run only book overview maintenance.")
    parser.add_argument("--book-check", action="store_true", help="Fail if book overview tables are stale or missing.")
    parser.add_argument("--book-dry-run", action="store_true", help="Preview book overview table updates without writing.")
    parser.add_argument("--concept-fields-only", action="store_true", help="Run only generated concept base-field maintenance.")
    parser.add_argument("--concept-fields-check", action="store_true", help="Fail if generated concept base fields are stale.")
    parser.add_argument("--concept-fields-dry-run", action="store_true", help="Preview generated concept base-field updates without writing.")
    parser.add_argument("--method-fields-only", action="store_true", help="Run only generated method base-field maintenance.")
    parser.add_argument("--method-fields-check", action="store_true", help="Fail if generated method base fields are stale.")
    parser.add_argument("--method-fields-dry-run", action="store_true", help="Preview generated method base-field updates without writing.")
    parser.add_argument("--theory-fields-only", action="store_true", help="Run only generated theory base-field maintenance.")
    parser.add_argument("--theory-fields-check", action="store_true", help="Fail if generated theory base fields are stale.")
    parser.add_argument("--theory-fields-dry-run", action="store_true", help="Preview generated theory base-field updates without writing.")
    parser.add_argument("--argument-fields-only", action="store_true", help="Run only generated argument base-field maintenance.")
    parser.add_argument("--argument-fields-check", action="store_true", help="Fail if generated argument base fields are stale.")
    parser.add_argument("--argument-fields-dry-run", action="store_true", help="Preview generated argument base-field updates without writing.")
    parser.add_argument("--wiki-only", action="store_true", help="Run only scripts/wiki_index.py.")
    parser.add_argument("--citation-only", action="store_true", help="Run only scripts/citation_index.py.")
    parser.add_argument("--citation-check", action="store_true", help="Pass --check to scripts/citation_index.py.")
    parser.add_argument("--citation-dry-run", action="store_true", help="Pass --dry-run to scripts/citation_index.py.")
    parser.add_argument("--full", action="store_true", help="Pass --full to scripts/citation_index.py for workflow symmetry.")
    args = parser.parse_args(argv)

    workflow_flags = [args.standard_workflow, args.full_workflow]
    if sum(1 for flag in workflow_flags if flag) > 1:
        parser.error("--standard-workflow and --full-workflow cannot be combined")

    only_flags = [
        args.book_only,
        args.concept_fields_only,
        args.method_fields_only,
        args.theory_fields_only,
        args.argument_fields_only,
        args.wiki_only,
        args.citation_only,
    ]
    if sum(1 for flag in only_flags if flag) > 1:
        parser.error("--book-only, --concept-fields-only, --method-fields-only, --theory-fields-only, --argument-fields-only, --wiki-only, and --citation-only cannot be combined")
    if any(workflow_flags) and any(only_flags):
        parser.error("workflow options cannot be combined with --book-only, --concept-fields-only, --wiki-only, or --citation-only")

    citation_args: list[str] = []
    if args.citation_check:
        citation_args.append("--check")
    if args.citation_dry_run:
        citation_args.append("--dry-run")
    if args.full:
        citation_args.append("--full")

    if args.standard_workflow:
        return run_standard_workflow(full=False)
    if args.full_workflow:
        return run_standard_workflow(full=True)

    if args.book_only:
        return maintain_book_overviews(dry_run=args.book_dry_run, check=args.book_check)

    if args.concept_fields_only:
        return maintain_concept_base_fields(dry_run=args.concept_fields_dry_run, check=args.concept_fields_check)

    if args.method_fields_only:
        return maintain_method_base_fields(dry_run=args.method_fields_dry_run, check=args.method_fields_check)

    if args.theory_fields_only:
        return maintain_theory_base_fields(dry_run=args.theory_fields_dry_run, check=args.theory_fields_check)

    if args.argument_fields_only:
        return maintain_argument_base_fields(dry_run=args.argument_fields_dry_run, check=args.argument_fields_check)

    if not args.wiki_only and not args.citation_only:
        code = run_base_index(book_check=args.book_check, book_dry_run=args.book_dry_run, citation_args=citation_args)
        return code

    if not args.citation_only and not args.book_only:
        code = run_script("wiki_index.py")
        if code:
            return code

    if not args.wiki_only and not args.book_only:
        code = run_script("citation_index.py", citation_args)
        if code:
            return code

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
