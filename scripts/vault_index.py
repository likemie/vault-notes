#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

"""
vault_index.py

Run the vault's base maintenance in dependency order:
  1. Refresh citation aliases and indexes before citation fixes / linking.
  2. Fix changed Markdown and maintain book overview tables.
  3. In the explicit standard workflow, refresh wiki lookup, link, then sync relations.
  4. Refresh dates, relation counts and ratings after all content / relation writes.
  5. Refresh final indexes; the standard workflow finishes with lint.

This file is the daily unified entry point. Larger generated surfaces that
already have mature boundaries still live in their own scripts.
"""

import argparse
import datetime
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vaultlib  # noqa: E402
from vaultlib import parse_inline_list, parse_scalar, wikilink_target  # noqa: E402

if __name__ == "__main__":
    vaultlib.ensure_venv()

VAULT_ROOT = vaultlib.ROOT


ROOT = VAULT_ROOT
SCRIPTS_DIR = ROOT / "scripts"
BOOKS_DIR = ROOT / "wiki" / "arguments" / "books"
ARGUMENTS_DIR = ROOT / "wiki" / "arguments"
CONCEPTS_DIR = ROOT / "wiki" / "concepts"
METHODS_DIR = ROOT / "wiki" / "methods"
THEORIES_DIR = ROOT / "wiki" / "theories"
INSTRUMENTS_DIR = ROOT / "wiki" / "instruments"
FACTS_DIR = ROOT / "wiki" / "facts"
PERSONS_DIR = ROOT / "wiki" / "persons"
RESEARCH_MAP_PATH = ROOT / "wiki" / "research-map.md"
RESEARCH_MAP_STATS = (
    ("concepts", "concept", "概念"),
    ("arguments", "argument", "论证"),
    ("facts", "fact", "事实"),
    ("persons", "person", "人物"),
    ("theories", "theory", "理论"),
    ("methods", "method", "方法"),
    ("instruments", "instrument", "测量工具"),
)


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
INSTRUMENT_GENERATED_KEYS = {
    "instrument_related_count",
    "instrument_related_level",
    "instrument_related_stars",
    "instrument_related_color",
}
INSTRUMENT_COLORS = {
    "test": "#dbeafe",
    "scale": "#dcfce7",
    "questionnaire": "#fef3c7",
    "inventory": "#ede9fe",
    "rubric": "#ffedd5",
    "observation-tool": "#cffafe",
    "interview-tool": "#fce7f3",
}
ARGUMENT_GENERATED_KEYS = {
    "title",
    "argument_key",
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
FACT_GENERATED_KEYS = {
    "fact_region",
    "fact_kind",
    "fact_related_count",
    "fact_related_level",
    "fact_related_stars",
    "fact_related_color",
}
FACT_COLORS = {
    "policy": "#dbeafe",
    "event": "#fef3c7",
    "organization": "#dcfce7",
    "program": "#ede9fe",
    "region": "#e0e7ff",
    "phenomenon": "#fce7f3",
    "unknown": "#e5e7eb",
}
PERSON_GENERATED_KEYS = {
    "person_region",
    "person_related_count",
    "person_related_level",
    "person_related_stars",
    "person_related_color",
}
PERSON_COLORS = ["#e5e7eb", "#dbeafe", "#e0e7ff", "#ede9fe", "#fce7f3", "#ffedd5", "#fef3c7"]


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


# One run reads every Markdown file once: research-map counts and each
# *_base_fields pass previously re-read and re-parsed the same files.
_TEXT_CACHE: dict[Path, str] = {}


def read_md(path: Path) -> str:
    text = _TEXT_CACHE.get(path)
    if text is None:
        text = path.read_text(encoding="utf-8", errors="replace")
        _TEXT_CACHE[path] = text
    return text


def write_md(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
    _TEXT_CACHE[path] = text


def run_script(script_name: str, extra_args: list[str] | None = None) -> int:
    cmd = [sys.executable, str(SCRIPTS_DIR / script_name)]
    if extra_args:
        cmd.extend(extra_args)

    print(f"$ {Path(sys.executable).name} scripts/{script_name}" + (f" {' '.join(extra_args)}" if extra_args else ""), flush=True)
    completed = subprocess.run(cmd, cwd=ROOT)
    return completed.returncode


def run_scripts_parallel(jobs: list[tuple[str, list[str]]]) -> int:
    """Run independent scripts concurrently; print their output in job order."""
    procs = []
    for script_name, extra_args in jobs:
        cmd = [sys.executable, str(SCRIPTS_DIR / script_name), *extra_args]
        label = f"$ {Path(sys.executable).name} scripts/{script_name}" + (f" {' '.join(extra_args)}" if extra_args else "")
        procs.append((label, subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)))
    first_failure = 0
    for label, proc in procs:
        out, _ = proc.communicate()
        print(label, flush=True)
        if out:
            print(out, end="" if out.endswith("\n") else "\n", flush=True)
        if proc.returncode and not first_failure:
            first_failure = proc.returncode
    return first_failure


_FM_CACHE: dict[str, dict[str, Any]] = {}


def parse_frontmatter(text: str) -> dict[str, Any]:
    cached = _FM_CACHE.get(text)
    if cached is None:
        cached = _parse_frontmatter_uncached(text)
        _FM_CACHE[text] = cached
    return dict(cached)


def _parse_frontmatter_uncached(text: str) -> dict[str, Any]:
    return vaultlib.parse_frontmatter_light(vaultlib.frontmatter_raw(text))


def split_frontmatter(text: str) -> tuple[str, str] | None:
    """(raw YAML, body) or None without frontmatter."""
    split = vaultlib.split_frontmatter(text)
    return (split.raw, split.body) if split.found else None


def chapter_number_from_target(target: str) -> int | None:
    m = CHAPTER_FILE_RE.match(target)
    return int(m.group("num")) if m else None


def chapter_number_from_text(text: str) -> int | None:
    m = CHINESE_CHAPTER_RE.search(text)
    return int(m.group("num")) if m else None


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
    """No ``## 总览`` heading: the titled ``[!textbook-overview]`` callout carries the section.
    Insert it before ``## 章节`` (or ``## 来源``), else at the end of the note."""
    for name in ("## 章节", "## 来源", "## Sources"):
        for i, line in enumerate(lines):
            if line.strip() == name:
                cut = i
                while cut > 0 and lines[cut - 1].strip() in {"", "---"}:
                    cut -= 1
                return lines[:cut] + ["", *default_overview_block(chapters), ""] + lines[cut:]
    return lines + ["", *default_overview_block(chapters)]


def discover_book_overviews() -> list[BookOverview]:
    overviews: list[BookOverview] = []
    if not BOOKS_DIR.exists():
        return overviews
    for path in sorted(BOOKS_DIR.rglob("Argument_*.md")):
        text = read_md(path)
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
    text = read_md(overview.path)
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
        write_md(overview.path, new_text)
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


def count_typed_entries(directory: Path, entry_type: str) -> int:
    if not directory.exists():
        return 0
    count = 0
    for path in directory.rglob("*.md"):
        if not path.is_file():
            continue
        text = read_md(path)
        if parse_frontmatter(text).get("type") == entry_type:
            count += 1
    return count


def update_research_map_stats(dry_run: bool = False, check: bool = False) -> int:
    if not RESEARCH_MAP_PATH.exists():
        print(f"❌ research map not found: {RESEARCH_MAP_PATH.relative_to(ROOT)}")
        return 1

    text = read_md(RESEARCH_MAP_PATH)
    next_text = text
    counts: list[tuple[str, int]] = []

    for directory_name, entry_type, label in RESEARCH_MAP_STATS:
        count = count_typed_entries(ROOT / "wiki" / directory_name, entry_type)
        counts.append((label, count))
        pattern = re.compile(
            rf'(<a href="/bases/{re.escape(directory_name)}"><span>{re.escape(label)}</span><strong>)'
            r"\d+(</strong></a>)"
        )
        next_text, replacements = pattern.subn(rf"\g<1>{count}\g<2>", next_text, count=1)
        if replacements != 1:
            print(f"❌ research map stat card not found or duplicated: {directory_name}")
            return 1

    changed = next_text != text
    if changed and not dry_run and not check:
        write_md(RESEARCH_MAP_PATH, next_text)

    prefix = "would update" if dry_run or check else "updated"
    state = prefix if changed else "already current"
    summary = " · ".join(f"{label} {count}" for label, count in counts)
    print(f"🗺️  research map {state}: {summary}")
    if check:
        return 1 if changed else 0
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


def related_stars_for(count: int) -> tuple[int, str]:
    """Use ten relations per star and three stars per diamond for every type."""
    level = max(0, count // 10)
    diamonds, stars = divmod(level, 3)
    display = "💎" * diamonds + "⭐" * stars
    return level, display or "☆"


def concept_stars_for(count: int) -> tuple[int, str]:
    return related_stars_for(count)


def yaml_string(value: str) -> str:
    return vaultlib.yaml_quote(value)


def set_frontmatter_value(raw_frontmatter: str, key: str, value: str, insert_after_patterns: list[str] | None = None) -> str:
    lines = raw_frontmatter.rstrip("\n").splitlines()
    found = False
    new_lines = []
    for line in lines:
        if re.match(rf"^{re.escape(key)}:\s*", line):
            new_lines.append(f"{key}: {value}")
            found = True
        else:
            new_lines.append(line)
    if not found:
        insert_idx = None
        if insert_after_patterns:
            for pat in insert_after_patterns:
                for idx, line in enumerate(new_lines):
                    if re.match(pat, line):
                        insert_idx = idx + 1
                        break
                if insert_idx is not None:
                    break
        if insert_idx is None:
            insert_idx = len(new_lines)
        new_lines.insert(insert_idx, f"{key}: {value}")
    return "\n".join(new_lines).rstrip() + "\n"


def format_person_lifespan(born: str, died: str, existing_lifespan: str) -> str:
    born = str(born or "").strip()
    died = str(died or "").strip()
    existing_lifespan = str(existing_lifespan or "").strip()
    if ";" in existing_lifespan or "；" in existing_lifespan:
        return existing_lifespan
    if not born:
        return existing_lifespan
    if "BCE" in born or "BCE" in died:
        if died:
            return f"{born} – {died}".strip(" –")
        return born
    if not died:
        return f"{born}–至今"
    return f"{born}–{died}"


def infer_fact_subtype(body: str, current_subtype: str) -> str:
    if current_subtype in {"policy", "organization", "event", "program"}:
        return current_subtype
    if "[!policy-context]" in body or "[!policy-impact]" in body:
        return "policy"
    if "[!org-profile]" in body or "[!org-structure]" in body:
        return "organization"
    if "[!program-profile]" in body or "[!program-design]" in body:
        return "program"
    if "[!timeline]" in body or "[!event-profile]" in body or "[!fact-timeline]" in body:
        return "event"
    return current_subtype or "unknown"


FOLDER_TO_INSTRUMENT_TYPE = {
    "checklists": "checklist",
    "interview-tools": "interview-tool",
    "inventories": "inventory",
    "observation-tools": "observation-tool",
    "questionnaires": "questionnaire",
    "rubrics": "rubric",
    "scales": "scale",
    "tests": "test",
}


def iter_entry_files(directory: Path) -> list[Path]:
    return sorted(path for path in directory.rglob("*.md") if path.is_file())


def write_base_fields(
    path: Path, text: str, frontmatter: str, body: str, *,
    dry_run: bool, check: bool, update_date: bool,
) -> bool:
    next_text = f"---\n{frontmatter}---\n{body}"
    changed = next_text != text
    if changed and not dry_run and not check:
        if update_date:
            frontmatter = set_frontmatter_value(
                frontmatter, "updated", datetime.date.today().isoformat(), [r"^created:\s*"])
            next_text = f"---\n{frontmatter}---\n{body}"
        write_md(path, next_text)
    return changed


def maintain_base_fields(
    kind: str, marker: str, paths: list[Path],
    update: Callable[..., tuple[bool, tuple[int, str] | None]], *, dry_run: bool, check: bool,
) -> int:
    changed_count = 0
    summaries: list[tuple[int, str, str]] = []
    for path in paths:
        changed, summary = update(path, dry_run=dry_run, check=check)
        if summary:
            related_count, related_stars = summary
            summaries.append((related_count, related_stars, path.relative_to(ROOT).as_posix()))
        if changed:
            changed_count += 1
            prefix = "would update" if dry_run or check else "updated"
            print(f"{marker} {prefix}: {path.relative_to(ROOT).as_posix()}")

    summaries.sort(key=lambda item: item[0], reverse=True)
    print(f"{marker} {kind} base fields checked: {len(summaries)}; changed: {changed_count}")
    for related_count, related_stars, rel_path in summaries[:10]:
        print(f"{related_count:>3} {related_stars:<6} {rel_path}")
    return int(check and changed_count > 0)


def upsert_concept_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    return vaultlib.upsert_generated_fields(raw_frontmatter, CONCEPT_GENERATED_KEYS, [
        f"domain: {yaml_string(str(fields['domain']))}",
        f"related_count: {int(fields['related_count'])}",
        f"related_level: {int(fields['related_level'])}",
        f"related_stars: {yaml_string(str(fields['related_stars']))}",
        f"related_color: {yaml_string(str(fields['related_color']))}",
    ],
        stop_after=("type",))


def iter_concept_files() -> list[Path]:
    return iter_entry_files(CONCEPTS_DIR)


def update_concept_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = read_md(path)
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
        "related_color": CONCEPT_COLORS[min(related_level, len(CONCEPT_COLORS) - 1)],
    })
    changed = write_base_fields(path, text, next_frontmatter, body,
                                dry_run=dry_run, check=check, update_date=True)
    return changed, (related_count, related_stars)


def maintain_concept_base_fields(dry_run: bool = False, check: bool = False) -> int:
    return maintain_base_fields("concept", "✨", iter_concept_files(),
                                update_concept_base_fields, dry_run=dry_run, check=check)


def instrument_stars_for(count: int) -> tuple[int, str]:
    return related_stars_for(count)


def instrument_color_for(kind: str, level: int) -> str:
    if level >= 5:
        return "#fecdd3"
    return INSTRUMENT_COLORS.get(kind, "#e5e7eb")


def upsert_instrument_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    return vaultlib.upsert_generated_fields(raw_frontmatter, INSTRUMENT_GENERATED_KEYS, [
        f"instrument_related_count: {int(fields['instrument_related_count'])}",
        f"instrument_related_level: {int(fields['instrument_related_level'])}",
        f"instrument_related_stars: {yaml_string(str(fields['instrument_related_stars']))}",
        f"instrument_related_color: {yaml_string(str(fields['instrument_related_color']))}",
    ],
        stop_after=("instrument_type",), fallback_after=("type",))


def iter_instrument_files() -> list[Path]:
    return iter_entry_files(INSTRUMENTS_DIR)


def update_instrument_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = read_md(path)
    split = split_frontmatter(text)
    if not split:
        return False, None
    raw_frontmatter, body = split
    meta = parse_frontmatter(text)
    if meta.get("type") != "instrument":
        return False, None
    try:
        folder_type = path.relative_to(INSTRUMENTS_DIR).parts[0]
    except (IndexError, ValueError):
        folder_type = ""
    expected_inst_type = FOLDER_TO_INSTRUMENT_TYPE.get(folder_type)
    if expected_inst_type and str(meta.get("instrument_type") or "").strip() != expected_inst_type:
        raw_frontmatter = set_frontmatter_value(raw_frontmatter, "instrument_type", expected_inst_type, [r"^type:\s*"])
        kind = expected_inst_type
    else:
        kind = str(meta.get("instrument_type") or "unknown").strip() or "unknown"
    related_count = count_related_fields(meta)
    related_level, related_stars = instrument_stars_for(related_count)
    next_frontmatter = upsert_instrument_generated_fields(raw_frontmatter, {
        "instrument_related_count": related_count,
        "instrument_related_level": related_level,
        "instrument_related_stars": related_stars,
        "instrument_related_color": instrument_color_for(kind, related_level),
    })
    changed = write_base_fields(path, text, next_frontmatter, body,
                                dry_run=dry_run, check=check, update_date=True)
    return changed, (related_count, related_stars)


def maintain_instrument_base_fields(dry_run: bool = False, check: bool = False) -> int:
    return maintain_base_fields("instrument", "🧰", iter_instrument_files(),
                                update_instrument_base_fields, dry_run=dry_run, check=check)


def method_family_for(path: Path, meta: dict[str, Any]) -> str:
    method_type = str(meta.get("method_type") or "").strip()
    if method_type:
        return method_type
    try:
        return path.relative_to(METHODS_DIR).parts[0]
    except (IndexError, ValueError):
        return "other"


def method_stars_for(count: int) -> tuple[int, str]:
    return related_stars_for(count)


def upsert_method_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    return vaultlib.upsert_generated_fields(raw_frontmatter, METHOD_GENERATED_KEYS, [
        f"method_family: {yaml_string(str(fields['method_family']))}",
        f"method_related_count: {int(fields['method_related_count'])}",
        f"method_related_level: {int(fields['method_related_level'])}",
        f"method_related_stars: {yaml_string(str(fields['method_related_stars']))}",
        f"method_related_color: {yaml_string(str(fields['method_related_color']))}",
    ],
        stop_after=("method_type",), after=("type",))


def iter_method_files() -> list[Path]:
    return iter_entry_files(METHODS_DIR)


def update_method_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = read_md(path)
    split = split_frontmatter(text)
    if not split:
        return False, None
    raw_frontmatter, body = split
    meta = parse_frontmatter(text)
    if meta.get("type") != "method":
        return False, None
    try:
        folder_type = path.relative_to(METHODS_DIR).parts[0]
    except (IndexError, ValueError):
        folder_type = ""
    if folder_type in ("qualitative", "quantitative", "mixed") and str(meta.get("method_type") or "").strip() != folder_type:
        raw_frontmatter = set_frontmatter_value(raw_frontmatter, "method_type", folder_type, [r"^type:\s*"])
        family = folder_type
    else:
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
    changed = write_base_fields(path, text, next_frontmatter, body,
                                dry_run=dry_run, check=check, update_date=True)
    return changed, (related_count, related_stars)


def maintain_method_base_fields(dry_run: bool = False, check: bool = False) -> int:
    return maintain_base_fields("method", "🧭", iter_method_files(),
                                update_method_base_fields, dry_run=dry_run, check=check)


def theory_field_for(path: Path) -> str:
    try:
        return path.relative_to(THEORIES_DIR).parts[0]
    except (IndexError, ValueError):
        return "other"


def theory_stars_for(count: int) -> tuple[int, str]:
    return related_stars_for(count)


def upsert_theory_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    return vaultlib.upsert_generated_fields(raw_frontmatter, THEORY_GENERATED_KEYS, [
        f"theory_field: {yaml_string(str(fields['theory_field']))}",
        f"theory_related_count: {int(fields['theory_related_count'])}",
        f"theory_related_level: {int(fields['theory_related_level'])}",
        f"theory_related_stars: {yaml_string(str(fields['theory_related_stars']))}",
        f"theory_related_color: {yaml_string(str(fields['theory_related_color']))}",
    ],
        stop_after=("type",))


def iter_theory_files() -> list[Path]:
    return iter_entry_files(THEORIES_DIR)


def update_theory_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = read_md(path)
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
        "theory_related_color": THEORY_COLORS[min(related_level, len(THEORY_COLORS) - 1)],
    })
    changed = write_base_fields(path, text, next_frontmatter, body,
                                dry_run=dry_run, check=check, update_date=True)
    return changed, (related_count, related_stars)


def maintain_theory_base_fields(dry_run: bool = False, check: bool = False) -> int:
    return maintain_base_fields("theory", "🪜", iter_theory_files(),
                                update_theory_base_fields, dry_run=dry_run, check=check)


def fact_region_for(path: Path, meta: dict[str, Any]) -> str:
    region = str(meta.get("region") or "").strip()
    if region:
        return region
    try:
        return path.relative_to(FACTS_DIR).parts[0]
    except (IndexError, ValueError):
        return "unknown"


def fact_kind_for(meta: dict[str, Any]) -> str:
    return str(meta.get("subtype") or "unknown").strip() or "unknown"


def fact_stars_for(count: int) -> tuple[int, str]:
    return related_stars_for(count)


def fact_color_for(kind: str, level: int) -> str:
    if level >= 5:
        return "#fecdd3"
    return FACT_COLORS.get(kind, "#e5e7eb")


def upsert_fact_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    return vaultlib.upsert_generated_fields(raw_frontmatter, FACT_GENERATED_KEYS, [
        f"fact_region: {yaml_string(str(fields['fact_region']))}",
        f"fact_kind: {yaml_string(str(fields['fact_kind']))}",
        f"fact_related_count: {int(fields['fact_related_count'])}",
        f"fact_related_level: {int(fields['fact_related_level'])}",
        f"fact_related_stars: {yaml_string(str(fields['fact_related_stars']))}",
        f"fact_related_color: {yaml_string(str(fields['fact_related_color']))}",
    ],
        stop_after=("region",), after=("subtype",), fallback_after=("type",))


def iter_fact_files() -> list[Path]:
    return iter_entry_files(FACTS_DIR)


def update_fact_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = read_md(path)
    split = split_frontmatter(text)
    if not split:
        return False, None
    raw_frontmatter, body = split
    meta = parse_frontmatter(text)
    if meta.get("type") != "fact":
        return False, None
    try:
        folder_region = path.relative_to(FACTS_DIR).parts[0]
    except (IndexError, ValueError):
        folder_region = ""

    current_region = str(meta.get("region") or "").strip()
    if folder_region and current_region != folder_region:
        raw_frontmatter = set_frontmatter_value(raw_frontmatter, "region", folder_region, [r"^subtype:\s*", r"^type:\s*"])
        region = folder_region
    else:
        region = fact_region_for(path, meta)

    current_subtype = str(meta.get("subtype") or "").strip()
    inferred_subtype = infer_fact_subtype(body, current_subtype)
    if inferred_subtype in {"policy", "organization", "event", "program"} and current_subtype != inferred_subtype:
        raw_frontmatter = set_frontmatter_value(raw_frontmatter, "subtype", inferred_subtype, [r"^type:\s*"])
        kind = inferred_subtype
    else:
        kind = fact_kind_for(meta)

    related_count = count_related_fields(meta)
    related_level, related_stars = fact_stars_for(related_count)
    next_frontmatter = upsert_fact_generated_fields(raw_frontmatter, {
        "fact_region": region,
        "fact_kind": kind,
        "fact_related_count": related_count,
        "fact_related_level": related_level,
        "fact_related_stars": related_stars,
        "fact_related_color": fact_color_for(kind, related_level),
    })
    changed = write_base_fields(path, text, next_frontmatter, body,
                                dry_run=dry_run, check=check, update_date=True)
    return changed, (related_count, related_stars)


def maintain_fact_base_fields(dry_run: bool = False, check: bool = False) -> int:
    return maintain_base_fields("fact", "🧩", iter_fact_files(),
                                update_fact_base_fields, dry_run=dry_run, check=check)


def person_region_for(path: Path, meta: dict[str, Any]) -> str:
    nationality = str(meta.get("nationality") or "").strip()
    if nationality and nationality != "schools":
        return nationality
    try:
        part = path.relative_to(PERSONS_DIR).parts[0]
        if part == "schools":
            return nationality if (nationality and nationality != "schools") else "global"
        return part
    except (IndexError, ValueError):
        return "unknown"


def person_stars_for(count: int) -> tuple[int, str]:
    return related_stars_for(count)


def upsert_person_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    return vaultlib.upsert_generated_fields(raw_frontmatter, PERSON_GENERATED_KEYS, [
        f"person_region: {yaml_string(str(fields['person_region']))}",
        f"person_related_count: {int(fields['person_related_count'])}",
        f"person_related_level: {int(fields['person_related_level'])}",
        f"person_related_stars: {yaml_string(str(fields['person_related_stars']))}",
        f"person_related_color: {yaml_string(str(fields['person_related_color']))}",
    ],
        stop_after=("nationality", "subtype"), fallback_after=("type",))


def iter_person_files() -> list[Path]:
    return iter_entry_files(PERSONS_DIR)


def update_person_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = read_md(path)
    split = split_frontmatter(text)
    if not split:
        return False, None
    raw_frontmatter, body = split
    meta = parse_frontmatter(text)
    if meta.get("type") != "person":
        return False, None
    try:
        folder_nat = path.relative_to(PERSONS_DIR).parts[0]
    except (IndexError, ValueError):
        folder_nat = ""

    current_subtype = str(meta.get("subtype") or "").strip()
    current_nat = str(meta.get("nationality") or "").strip()

    if folder_nat == "schools":
        if current_subtype != "school":
            raw_frontmatter = set_frontmatter_value(raw_frontmatter, "subtype", "school", [r"^type:\s*"])
        if current_nat == "schools":
            raw_frontmatter = set_frontmatter_value(raw_frontmatter, "nationality", "global", [r"^subtype:\s*", r"^type:\s*"])
        region = person_region_for(path, meta)
    elif folder_nat and current_nat != folder_nat:
        raw_frontmatter = set_frontmatter_value(raw_frontmatter, "nationality", folder_nat, [r"^subtype:\s*", r"^type:\s*"])
        region = folder_nat
    else:
        region = person_region_for(path, meta)

    born = meta.get("born")
    died = meta.get("died")
    existing_lifespan = meta.get("lifespan")
    expected_lifespan = format_person_lifespan(str(born or ""), str(died or ""), str(existing_lifespan or ""))
    if expected_lifespan and str(existing_lifespan or "").strip() != expected_lifespan:
        lifespan_val = yaml_string(expected_lifespan) if (" " in expected_lifespan or "–" in expected_lifespan) else expected_lifespan
        raw_frontmatter = set_frontmatter_value(raw_frontmatter, "lifespan", lifespan_val, [r"^died:\s*", r"^born:\s*", r"^nationality:\s*"])

    if expected_lifespan:
        def _replace_body_lifespan(match: re.Match[str]) -> str:
            prefix = match.group(1).rstrip()
            return f"{prefix} {expected_lifespan}"
        body = re.sub(r"(>\s*-\s*\*\*生卒年份\*\*)(?:[^\n]*)", _replace_body_lifespan, body, count=1)

    related_count = count_related_fields(meta)
    related_level, related_stars = person_stars_for(related_count)
    next_frontmatter = upsert_person_generated_fields(raw_frontmatter, {
        "person_region": region,
        "person_related_count": related_count,
        "person_related_level": related_level,
        "person_related_stars": related_stars,
        "person_related_color": PERSON_COLORS[min(related_level, len(PERSON_COLORS) - 1)],
    })
    changed = write_base_fields(path, text, next_frontmatter, body,
                                dry_run=dry_run, check=check, update_date=True)
    return changed, (related_count, related_stars)


def maintain_person_base_fields(dry_run: bool = False, check: bool = False) -> int:
    return maintain_base_fields("person", "👤", iter_person_files(),
                                update_person_base_fields, dry_run=dry_run, check=check)


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
    return related_stars_for(count)


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
    publication_type = str(meta.get("publication_type") or "").strip()
    if book_title and publication_type != "book-chapter" and subtype in {"edited-volume", "monograph", "textbook"}:
        return book_title
    citation_title = title_from_citation(str(meta.get("citation") or ""))
    if citation_title:
        return citation_title
    if book_title and (subtype == "book-chapter" or publication_type == "book-chapter"):
        match = re.search(r"_Ch(?P<num>\d{1,3})\b", path.stem)
        if match:
            return f"{book_title} · Ch{int(match.group('num')):02d}"
    if book_title and kind == "book" and subtype != "book-chapter":
        return book_title
    if book_title:
        return book_title
    title = str(meta.get("title") or "").strip()
    return title or path.stem


def upsert_argument_generated_fields(raw_frontmatter: str, fields: dict[str, Any]) -> str:
    return vaultlib.upsert_generated_fields(raw_frontmatter, ARGUMENT_GENERATED_KEYS, [
        f"title: {yaml_string(str(fields['argument_key']))}",
        f"argument_key: {yaml_string(str(fields['argument_key']))}",
        f"argument_display_title: {yaml_string(str(fields['argument_display_title']))}",
        f"argument_kind: {yaml_string(str(fields['argument_kind']))}",
        f"argument_related_count: {int(fields['argument_related_count'])}",
        f"argument_related_level: {int(fields['argument_related_level'])}",
        f"argument_related_stars: {yaml_string(str(fields['argument_related_stars']))}",
        f"argument_related_color: {yaml_string(str(fields['argument_related_color']))}",
    ],
        stop_after=("publication_type",), after=("subtype",), fallback_after=("type",))


def iter_argument_files() -> list[Path]:
    return iter_entry_files(ARGUMENTS_DIR)


def update_argument_base_fields(path: Path, dry_run: bool, check: bool) -> tuple[bool, tuple[int, str] | None]:
    text = read_md(path)
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
        "argument_key": path.stem,
        "argument_display_title": argument_display_title_for(path, meta),
        "argument_kind": kind,
        "argument_related_count": related_count,
        "argument_related_level": related_level,
        "argument_related_stars": related_stars,
        "argument_related_color": argument_color_for(kind, related_level),
    })
    changed = write_base_fields(path, text, next_frontmatter, body,
                                dry_run=dry_run, check=check, update_date=False)
    return changed, (related_count, related_stars)


def maintain_argument_base_fields(dry_run: bool = False, check: bool = False) -> int:
    return maintain_base_fields("argument", "🔎", iter_argument_files(),
                                update_argument_base_fields, dry_run=dry_run, check=check)


# Frontmatter lines that tools maintain; a diff touching only these is not a
# body edit and must not bump `updated` (same rule vault_lint used for its
# former UPDATED_STALE warning).
AUTO_MAINTAINED_FM_RE = re.compile(
    r"^[+-]\s*(?:---\s*$|(?:related_[a-z_]+|sources|extracted_to|updated|created|domain|aliases|"
    r"citation_aliases|citation|tags|confidence|status|title|summary|type|subtype|journal|year|doi|isbn|"
    r"authors|editors|source_language|argument_display_title|publication_place|publisher|part_of|processed_date)\s*:"
    r"|\s+-\s|\s+\")"
)
GENERATED_WIKI_NAMES = {"index.md", "index.json"}
GENERATED_WIKI_PATHS = {"wiki/research-map.md"}
UPDATED_RE = re.compile(r"^updated\s*:\s*[\"']?(\d{4}-\d{2}-\d{2})", re.M)


def git_text(args: list[str]) -> str:
    return vaultlib.git_output(args)



def run_auto_fixes(link_citations: bool = True) -> int:
    """Apply vault_lint's mechanical fixes to git-changed Markdown files.

    Fixes: English two-author conjunctions, bold delimiter boundaries,
    summary quotes, [!axis] separators (see vault_lint.apply_fixes), then
    links raw APA citations to Argument pages (wiki_linker.py)."""
    if str(SCRIPTS_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPTS_DIR))
    import vault_lint as lint  # noqa: PLC0415 - heavy import, only when needed

    files = lint.git_changed_md_files()
    if not files:
        return 0
    argument_citations, _ = lint.build_argument_citation_maps([], [])
    changed_files, total = lint.apply_fixes(files, argument_citations)
    if changed_files:
        print(f"auto-fix: {total} issue(s) fixed in {changed_files} file(s)")
    linked_files, linked_total = auto_link_citations(files) if link_citations else (0, 0)
    if linked_files:
        print(f"auto-link: {linked_total} APA citation(s) linked in {linked_files} file(s)")
    if changed_files or linked_files:
        _TEXT_CACHE.clear()
        _FM_CACHE.clear()
    return 0


def auto_link_citations(files: list[Path]) -> tuple[int, int]:
    """Use the shared linker's citation-only mode in the base workflow."""
    import wiki_linker as linker

    if not linker.CITATION_FULL_JSON.exists():
        return 0, 0
    return linker.run_citation_sync(files)


def sync_updated_dates(dry_run: bool = False, check: bool = False) -> int:
    """Set `updated` to today on wiki entries whose body changed since HEAD."""
    status = git_text(["status", "--porcelain=v1", "-z", "--", "wiki"]).split("\0")
    candidates: list[str] = []
    i = 0
    while i < len(status):
        entry = status[i]
        i += 1
        if len(entry) < 4:
            continue
        code, rel = entry[:2], entry[3:]
        if code[0] in "RC":
            i += 1  # porcelain -z puts the rename source in the next field
        if code == "??" or "D" in code or not rel.endswith(".md"):
            continue
        path = ROOT / rel
        if (rel.startswith("wiki/templates/") or path.name in GENERATED_WIKI_NAMES
                or rel in GENERATED_WIKI_PATHS or not path.is_file()):
            continue
        candidates.append(rel)
    if not candidates:
        return 0

    diff = git_text(["diff", "-U0", "--no-color", "HEAD", "--", *candidates])
    body_changed: set[str] = set()
    current: str | None = None
    for line in diff.splitlines():
        if line.startswith("+++ b/"):
            current = line[6:].split("\t", 1)[0]
            continue
        if line.startswith("+++ "):
            current = None
            continue
        if current is None or not line or line[0] not in "+-" or line.startswith(("+++", "---")):
            continue
        if not AUTO_MAINTAINED_FM_RE.match(line):
            body_changed.add(current)

    today = datetime.date.today().isoformat()
    changed = 0
    for rel in sorted(body_changed):
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_md(path)
        split = split_frontmatter(text)
        if not split:
            continue
        raw_frontmatter, body = split
        m = UPDATED_RE.search(raw_frontmatter)
        if not m or m.group(1) == today:
            continue
        changed += 1
        prefix = "would update" if dry_run or check else "updated"
        print(f"{prefix} updated date: {rel} ({m.group(1)} -> {today})")
        if not dry_run and not check:
            next_frontmatter = set_frontmatter_value(raw_frontmatter + "\n", "updated", today)
            write_md(path, f"---\n{next_frontmatter}---\n{body}")
    return 1 if check and changed else 0


def run_base_index(
    book_check: bool = False,
    book_dry_run: bool = False,
    citation_args: list[str] | None = None,
    *,
    sync_links: bool = False,
    full: bool = False,
) -> int:
    # Citation maintenance validates journal naming before writing. Its output
    # must exist before mechanical citation fixes or APA linking read aliases.
    code = run_script("citation_index.py", citation_args or [])
    if code:
        return code
    _TEXT_CACHE.clear()
    _FM_CACHE.clear()
    code = run_auto_fixes(link_citations=not sync_links)
    if code:
        return code
    # Expire deleted/rewritten sentence exclusions even in the base workflow;
    # this command never adds/removes ordinary links in notes.
    code = run_script("wiki_linker.py", ["exceptions-clean"])
    if code:
        return code
    code = maintain_book_overviews(dry_run=book_dry_run, check=book_check)
    if code:
        return code
    # MetaX modules: match MetaX studies to Arguments by title (never by bare
    # author-year) and regenerate the `## Visible Learning MetaX` modules, so a
    # newly processed meta-analysis is linked wherever MetaX cites it.
    if (ROOT / "datasets/metax/metax.json").exists() and not (book_check or book_dry_run):
        code = run_script("metax_sync.py", ["sync"])
        if code:
            return code
        _TEXT_CACHE.clear()
        _FM_CACHE.clear()
    # EEF Toolkit modules ([!eef]) follow the same rules (scripts/eef_sync.py).
    if (ROOT / "datasets/eef/eef.json").exists() and not (book_check or book_dry_run):
        code = run_script("eef_sync.py", ["sync"])
        if code:
            return code
        _TEXT_CACHE.clear()
        _FM_CACHE.clear()

    if sync_links:
        # Ordinary linking and relation sync must see newly created / renamed
        # entries, so build their lookup before changing links.
        wiki_sync_args = ["sync", "--full"] if full else ["sync"]
        link_args = [*wiki_sync_args, "--fix-display"]
        for script_name, extra_args in [
            ("wiki_index.py", []),
            ("wiki_linker.py", link_args),
            ("wiki_relations.py", wiki_sync_args),
        ]:
            code = run_script(script_name, extra_args)
            if code:
                return code
        # The subprocesses wrote Markdown after this process cached it.
        _TEXT_CACHE.clear()
        _FM_CACHE.clear()

    # Date bumps include book table maintenance and unified linking. Ratings read
    # the final relation YAML, never the state from before wiki_relations.
    for maintain in (
        sync_updated_dates,
        update_research_map_stats,
        maintain_concept_base_fields,
        maintain_method_base_fields,
        maintain_theory_base_fields,
        maintain_instrument_base_fields,
        maintain_fact_base_fields,
        maintain_person_base_fields,
        maintain_argument_base_fields,
    ):
        code = maintain()
        if code:
            return code

    if sync_links:
        # wiki_linker can rewrite authors/editors as Person links. Refresh the
        # citation JSON too, so it reflects the final frontmatter values.
        return run_scripts_parallel([("wiki_index.py", []), ("citation_index.py", citation_args or [])])
    return run_script("wiki_index.py")


def run_standard_workflow(full: bool = False) -> int:
    code = run_base_index(sync_links=True, full=full)
    if code:
        return code
    return run_script("vault_lint.py", ["--full"] if full else [])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run wiki and citation base indexes.")
    parser.add_argument("--standard-workflow", action="store_true", help="Refresh lookup indexes, fix/link content, sync relations, rebuild ratings and final indexes, then lint.")
    parser.add_argument("--full-workflow", action="store_true", help="Run the full-vault version of --standard-workflow.")
    parser.add_argument("--book-only", action="store_true", help="Run only book overview maintenance.")
    parser.add_argument("--book-check", action="store_true", help="Fail if book overview tables are stale or missing.")
    parser.add_argument("--book-dry-run", action="store_true", help="Preview book overview table updates without writing.")
    parser.add_argument("--research-map-only", action="store_true", help="Run only research-map count maintenance.")
    parser.add_argument("--research-map-check", action="store_true", help="Fail if research-map counts are stale.")
    parser.add_argument("--research-map-dry-run", action="store_true", help="Preview research-map count updates without writing.")
    parser.add_argument("--concept-fields-only", action="store_true", help="Run only generated concept base-field maintenance.")
    parser.add_argument("--concept-fields-check", action="store_true", help="Fail if generated concept base fields are stale.")
    parser.add_argument("--concept-fields-dry-run", action="store_true", help="Preview generated concept base-field updates without writing.")
    parser.add_argument("--method-fields-only", action="store_true", help="Run only generated method base-field maintenance.")
    parser.add_argument("--method-fields-check", action="store_true", help="Fail if generated method base fields are stale.")
    parser.add_argument("--method-fields-dry-run", action="store_true", help="Preview generated method base-field updates without writing.")
    parser.add_argument("--theory-fields-only", action="store_true", help="Run only generated theory base-field maintenance.")
    parser.add_argument("--theory-fields-check", action="store_true", help="Fail if generated theory base fields are stale.")
    parser.add_argument("--theory-fields-dry-run", action="store_true", help="Preview generated theory base-field updates without writing.")
    parser.add_argument("--instrument-fields-only", action="store_true", help="Run only generated instrument base-field maintenance.")
    parser.add_argument("--instrument-fields-check", action="store_true", help="Fail if generated instrument base fields are stale.")
    parser.add_argument("--instrument-fields-dry-run", action="store_true", help="Preview generated instrument base-field updates without writing.")
    parser.add_argument("--fact-fields-only", action="store_true", help="Run only generated fact base-field maintenance.")
    parser.add_argument("--fact-fields-check", action="store_true", help="Fail if generated fact base fields are stale.")
    parser.add_argument("--fact-fields-dry-run", action="store_true", help="Preview generated fact base-field updates without writing.")
    parser.add_argument("--person-fields-only", action="store_true", help="Run only generated person base-field maintenance.")
    parser.add_argument("--person-fields-check", action="store_true", help="Fail if generated person base fields are stale.")
    parser.add_argument("--person-fields-dry-run", action="store_true", help="Preview generated person base-field updates without writing.")
    parser.add_argument("--argument-fields-only", action="store_true", help="Run only generated argument base-field maintenance.")
    parser.add_argument("--argument-fields-check", action="store_true", help="Fail if generated argument base fields are stale.")
    parser.add_argument("--argument-fields-dry-run", action="store_true", help="Preview generated argument base-field updates without writing.")
    parser.add_argument("--wiki-only", action="store_true", help="Run only scripts/wiki_index.py.")
    parser.add_argument("--citation-only", action="store_true", help="Run only scripts/citation_index.py.")
    parser.add_argument("--citation-check", action="store_true", help="Pass --check to scripts/citation_index.py.")
    parser.add_argument("--citation-dry-run", action="store_true", help="Pass --dry-run to scripts/citation_index.py.")
    parser.add_argument("--full", action="store_true", help="Pass --full to scripts/citation_index.py for workflow symmetry.")
    args = parser.parse_args(argv)

    # A check / dry-run flag implies its --*-only mode. Previously, e.g.
    # "--concept-fields-check" alone fell through to the full (writing) base index.
    for prefix in ("research_map", "concept_fields", "method_fields", "theory_fields",
                   "instrument_fields", "fact_fields", "person_fields", "argument_fields"):
        if getattr(args, f"{prefix}_check", False) or getattr(args, f"{prefix}_dry_run", False):
            setattr(args, f"{prefix}_only", True)
    if args.book_check or args.book_dry_run:
        args.book_only = True
    if (args.citation_check or args.citation_dry_run) and not args.wiki_only:
        args.citation_only = True

    workflow_flags = [args.standard_workflow, args.full_workflow]
    if sum(1 for flag in workflow_flags if flag) > 1:
        parser.error("--standard-workflow and --full-workflow cannot be combined")

    only_flags = [
        args.book_only,
        args.research_map_only,
        args.concept_fields_only,
        args.method_fields_only,
        args.theory_fields_only,
        args.instrument_fields_only,
        args.fact_fields_only,
        args.person_fields_only,
        args.argument_fields_only,
        args.wiki_only,
        args.citation_only,
    ]
    if sum(1 for flag in only_flags if flag) > 1:
        parser.error("--book-only, --research-map-only, --concept-fields-only, --method-fields-only, --theory-fields-only, --instrument-fields-only, --fact-fields-only, --person-fields-only, --argument-fields-only, --wiki-only, and --citation-only cannot be combined")
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

    if args.research_map_only:
        return update_research_map_stats(dry_run=args.research_map_dry_run, check=args.research_map_check)

    if args.concept_fields_only:
        return maintain_concept_base_fields(dry_run=args.concept_fields_dry_run, check=args.concept_fields_check)

    if args.method_fields_only:
        return maintain_method_base_fields(dry_run=args.method_fields_dry_run, check=args.method_fields_check)

    if args.theory_fields_only:
        return maintain_theory_base_fields(dry_run=args.theory_fields_dry_run, check=args.theory_fields_check)

    if args.instrument_fields_only:
        return maintain_instrument_base_fields(dry_run=args.instrument_fields_dry_run, check=args.instrument_fields_check)

    if args.fact_fields_only:
        return maintain_fact_base_fields(dry_run=args.fact_fields_dry_run, check=args.fact_fields_check)

    if args.person_fields_only:
        return maintain_person_base_fields(dry_run=args.person_fields_dry_run, check=args.person_fields_check)

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
