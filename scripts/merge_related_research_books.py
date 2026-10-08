#!/usr/bin/env python3
"""Merge same-book entries in related-research index callouts.

The first top-level entry for a book remains in place. Later top-level entries
from the same ``wiki/arguments/books/<book>/`` directory are appended to it as
inline chapter/source details, so every original link and explanation is kept.

The command is a dry run by default. Pass ``--apply`` to write changes.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import vault_lint as lint


CALLOUT_HEADER_RE = re.compile(
    r"^(?P<quote>\s*(?:>\s*)+)\[![^\]\n]+\][+-]?\s*(?P<title>.*)$"
)
QUOTED_LINE_RE = re.compile(r"^(?P<quote>\s*(?:>\s*)+)(?P<content>.*)$")
BULLET_RE = re.compile(r"^(?P<marker>[-*+]\s+)(?P<body>.*)$")


def _join_entry_bodies(bodies: List[str]) -> str:
    merged = bodies[0].rstrip()
    for body in bodies[1:]:
        body = body.strip()
        if not body:
            continue
        separator = " " if merged.endswith(("。", "！", "？", ".", "!", "?", "；", ";")) else "；"
        merged += separator + body
    return merged


def _update_date(text: str, value: str) -> str:
    frontmatter, body, _ = lint.split_frontmatter(text)
    if frontmatter is None:
        return text
    head = text[: len(text) - len(body)]
    updated = re.sub(
        r"(?m)^(updated\s*:\s*)[^\r\n]*$",
        rf"\g<1>{value}",
        head,
        count=1,
    )
    return updated + body


def merge_duplicate_book_entries(
    text: str,
    by_title: Dict[str, Dict[str, Any]],
    *,
    updated_date: str | None = None,
) -> Tuple[str, int]:
    """Return ``(new_text, removed_top_level_entries)`` for one Markdown file."""
    lines = text.splitlines(keepends=True)
    groups: List[List[int]] = []
    current_entries: List[Tuple[int, str]] = []
    in_index = False
    index_depth = 0

    def finish_index() -> None:
        nonlocal current_entries
        by_book: Dict[str, List[int]] = {}
        for line_index, book_key in current_entries:
            by_book.setdefault(book_key, []).append(line_index)
        groups.extend(indices for indices in by_book.values() if len(indices) > 1)
        current_entries = []

    for line_index, line in enumerate(lines):
        header = CALLOUT_HEADER_RE.match(line)
        if header:
            depth = header.group("quote").count(">")
            if in_index and depth > index_depth:
                continue
            if in_index:
                finish_index()
            title = header.group("title")
            in_index = "相关研究" in title and "索引" in title
            index_depth = depth if in_index else 0
            continue

        if not in_index:
            continue

        quoted = QUOTED_LINE_RE.match(line)
        if not quoted:
            if line.strip():
                finish_index()
                in_index = False
            continue

        if quoted.group("quote").count(">") != index_depth:
            continue
        bullet = BULLET_RE.match(quoted.group("content").rstrip("\r\n"))
        if not bullet:
            continue

        target = ""
        for match in lint.WIKILINK_RE.finditer(bullet.group("body")):
            candidate = lint.extract_wikilink_target(match.group(1))
            if candidate.startswith("Argument_"):
                target = candidate
                break
        book_key = lint.argument_book_key(target, by_title) if target else None
        if book_key:
            current_entries.append((line_index, book_key))

    if in_index:
        finish_index()
    if not groups:
        return text, 0

    replacements: Dict[int, str] = {}
    removals: set[int] = set()
    for indices in groups:
        bodies: List[str] = []
        first_prefix = ""
        first_newline = ""
        for position, line_index in enumerate(indices):
            line = lines[line_index]
            newline = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
            plain = line[: -len(newline)] if newline else line
            quoted = QUOTED_LINE_RE.match(plain)
            if not quoted:
                continue
            bullet = BULLET_RE.match(quoted.group("content"))
            if not bullet:
                continue
            if position == 0:
                first_prefix = quoted.group("quote") + bullet.group("marker")
                first_newline = newline
            bodies.append(bullet.group("body"))
        if len(bodies) < 2:
            continue
        replacements[indices[0]] = first_prefix + _join_entry_bodies(bodies) + first_newline
        removals.update(indices[1:])

    if not removals:
        return text, 0

    new_lines = [replacements.get(i, line) for i, line in enumerate(lines) if i not in removals]
    new_text = "".join(new_lines)
    if updated_date:
        new_text = _update_date(new_text, updated_date)
    return new_text, len(removals)


def markdown_files(paths: Iterable[Path]) -> Iterable[Path]:
    seen: set[Path] = set()
    for base in paths:
        for path in lint.iter_md_files(base):
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            if (
                lint.TEMPLATES_DIR in path.parents
                or lint.is_schema_or_workflow_doc(path)
                or lint.is_generated_content_page(path)
                or not lint.is_wiki_entry_path(path)
            ):
                continue
            yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", action="append", type=Path, help="file or directory to scan; repeatable")
    parser.add_argument("--apply", action="store_true", help="write changes instead of reporting a dry run")
    args = parser.parse_args()

    index_issues: List[lint.Issue] = []
    by_title, _ = lint.load_index(index_issues)
    if not by_title:
        for issue in index_issues:
            print(issue.format())
        return 2

    bases = [path if path.is_absolute() else lint.ROOT / path for path in (args.path or [lint.WIKI_DIR])]
    today = dt.date.today().isoformat()
    changed_files = 0
    merged_entries = 0
    for path in markdown_files(bases):
        text = path.read_text(encoding="utf-8")
        new_text, count = merge_duplicate_book_entries(
            text,
            by_title,
            updated_date=today,
        )
        if not count:
            continue
        changed_files += 1
        merged_entries += count
        action = "merged" if args.apply else "would merge"
        print(f"{action} {count:3d}  {lint.rel(path)}")
        if args.apply:
            path.write_text(new_text, encoding="utf-8")

    mode = "applied" if args.apply else "dry run"
    print(f"{mode}: {merged_entries} duplicate entries in {changed_files} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
