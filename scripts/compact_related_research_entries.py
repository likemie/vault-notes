#!/usr/bin/env python3
"""Compact overlong top-level entries in related-research index callouts.

The first complete sentence is preferred. If it exceeds the configured limit,
the entry is closed at the last natural clause boundary that fits. Wikilinks are
kept whole so the result never leaves broken Markdown. The command is a dry run
unless ``--apply`` is supplied.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from typing import Iterable, Tuple

import vault_lint as lint


CALLOUT_HEADER_RE = re.compile(
    r"^(?P<quote>\s*(?:>\s*)+)\[![^\]\n]+\][+-]?\s*(?P<title>.*)$"
)
QUOTED_LINE_RE = re.compile(r"^(?P<quote>\s*(?:>\s*)+)(?P<content>.*)$")
BULLET_RE = re.compile(r"^(?P<marker>[-*+]\s+)(?P<body>.*)$")
SPECIAL_MARKDOWN_RE = re.compile(r"!?\[\[[^\]\n]+\]\]|\[[^\]\n]+\]\([^)\n]+\)|<[^>\n]+>")


def _special_visible_text(token: str) -> str:
    if token.startswith("![["):
        token = token[1:]
    wikilink = lint.WIKILINK_RE.fullmatch(token)
    if wikilink:
        return lint.markdown_visible_text(token)
    markdown_link = lint.MD_LINK_RE.fullmatch(token)
    if markdown_link:
        return markdown_link.group(1)
    return ""


def _strip_emphasis(text: str) -> str:
    # Keep underscores because they are common in wikilink targets.
    return re.sub(r"[*~`]", "", text)


def slice_markdown_visible(text: str, visible_limit: int) -> str:
    """Slice Markdown without splitting wikilinks or Markdown links."""
    text = _strip_emphasis(text)
    out: list[str] = []
    visible_count = 0
    cursor = 0

    for match in SPECIAL_MARKDOWN_RE.finditer(text):
        plain = text[cursor:match.start()]
        remaining = visible_limit - visible_count
        if len(plain) >= remaining:
            out.append(plain[:remaining])
            return "".join(out)
        out.append(plain)
        visible_count += len(plain)

        token = match.group(0)
        token_visible = _special_visible_text(token)
        if visible_count + len(token_visible) > visible_limit:
            return "".join(out)
        out.append(token)
        visible_count += len(token_visible)
        cursor = match.end()

    remaining = visible_limit - visible_count
    out.append(text[cursor:cursor + remaining])
    return "".join(out)


def compact_entry(entry: str, max_chars: int = lint.RELATED_RESEARCH_ENTRY_MAX_CHARS) -> str:
    """Compact one entry to a complete-looking sentence within ``max_chars``."""
    entry = _strip_emphasis(entry).strip()
    visible = lint.markdown_visible_text(entry)
    if len(visible) <= max_chars:
        return entry

    first_sentence = re.search(r"[。！？!?]", visible)
    if first_sentence and first_sentence.end() <= max_chars:
        visible_limit = first_sentence.end()
        ending = "sentence"
    else:
        search_area = visible[: max_chars - 1]
        strong = [match.end() for match in re.finditer(r"[；;]", search_area)]
        weak = [match.end() for match in re.finditer(r"[，,、：:]", search_area)]
        parenthetical = [match.start() for match in re.finditer(r"[（(]", search_area)]
        if strong and strong[-1] >= 60:
            visible_limit = strong[-1]
            ending = "clause"
        elif weak and weak[-1] >= 60:
            visible_limit = weak[-1]
            ending = "clause"
        elif parenthetical and parenthetical[-1] >= 60:
            visible_limit = parenthetical[-1]
            ending = "hard"
        else:
            spaces = [match.start() for match in re.finditer(r"\s+", search_area)]
            visible_limit = spaces[-1] if spaces and spaces[-1] >= 60 else max_chars - 2
            ending = "hard"

    result = slice_markdown_visible(entry, visible_limit).rstrip()
    if ending == "sentence":
        return result
    result = re.sub(r"[；;，,、：:\s]+$", "", result)
    if ending == "hard":
        result += "等"
    result += "。"

    while len(lint.markdown_visible_text(result)) > max_chars:
        result = slice_markdown_visible(result[:-1], max_chars - 1).rstrip() + "。"
    return result


def _update_date(text: str, value: str) -> str:
    frontmatter, body, _ = lint.split_frontmatter(text)
    if frontmatter is None:
        return text
    head = text[: len(text) - len(body)]
    head = re.sub(
        r"(?m)^(updated\s*:\s*)[^\r\n]*$",
        rf"\g<1>{value}",
        head,
        count=1,
    )
    return head + body


def compact_related_research_entries(
    text: str,
    *,
    max_chars: int = lint.RELATED_RESEARCH_ENTRY_MAX_CHARS,
    updated_date: str | None = None,
) -> Tuple[str, int]:
    lines = text.splitlines(keepends=True)
    replacements: dict[int, str] = {}
    in_index = False
    index_depth = 0

    for line_index, line in enumerate(lines):
        header = CALLOUT_HEADER_RE.match(line)
        if header:
            depth = header.group("quote").count(">")
            if in_index and depth > index_depth:
                continue
            title = header.group("title")
            in_index = "相关研究" in title and "索引" in title
            index_depth = depth if in_index else 0
            continue

        if not in_index:
            continue
        quoted = QUOTED_LINE_RE.match(line)
        if not quoted:
            if line.strip():
                in_index = False
            continue
        if quoted.group("quote").count(">") != index_depth:
            continue

        content = quoted.group("content").rstrip("\r\n")
        bullet = BULLET_RE.match(content)
        if not bullet:
            continue
        if len(lint.markdown_visible_text(bullet.group("body"))) <= max_chars:
            continue

        newline = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
        replacements[line_index] = (
            quoted.group("quote")
            + bullet.group("marker")
            + compact_entry(bullet.group("body"), max_chars=max_chars)
            + newline
        )

    if not replacements:
        return text, 0
    new_text = "".join(replacements.get(i, line) for i, line in enumerate(lines))
    if updated_date:
        new_text = _update_date(new_text, updated_date)
    return new_text, len(replacements)


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

    bases = [path if path.is_absolute() else lint.ROOT / path for path in (args.path or [lint.WIKI_DIR])]
    today = dt.date.today().isoformat()
    changed_files = 0
    changed_entries = 0
    for path in markdown_files(bases):
        text = path.read_text(encoding="utf-8")
        new_text, count = compact_related_research_entries(text, updated_date=today)
        if not count:
            continue
        changed_files += 1
        changed_entries += count
        action = "compacted" if args.apply else "would compact"
        print(f"{action} {count:3d}  {lint.rel(path)}")
        if args.apply:
            path.write_text(new_text, encoding="utf-8")

    mode = "applied" if args.apply else "dry run"
    print(f"{mode}: {changed_entries} overlong entries in {changed_files} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
