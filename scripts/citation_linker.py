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

AUTHOR_PATTERN = r"[A-Z\u3400-\u9fff][A-Za-zÀ-ÖØ-öø-ÿ\u3400-\u9fff0-9'’ .&和等-]*(?:\s+(?:&|and|和)\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ0-9'’ .-]+|\s+et\s+al\.)?"
LOCATOR_PATTERN = r"(?:\s*[,，]\s*(?:(?:p|pp|ch|chap)\.?\s*|chapter\s+)[^,，;）)]+|\s*:\s*[^,，;）)]+)"
PAREN_GROUP_RE = re.compile(r"(?<!\[)\(([^()\n]*\b\d{4}[a-z]?[^()\n]*)\)")
FULLWIDTH_PAREN_GROUP_RE = re.compile(r"（([^（）\n]*\b\d{4}[a-z]?[^（）\n]*)）")
PAREN_ITEM_RE = re.compile(
    r"^\s*"
    rf"(?P<author>{AUTHOR_PATTERN})"
    r"\s*(?P<sep>[,，])\s*"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{LOCATOR_PATTERN})?"
    r"\s*$"
)
PAREN_ITEM_PREFIX_RE = re.compile(
    r"^\s*"
    rf"(?P<author>{AUTHOR_PATTERN})"
    r"\s*(?P<sep>[,，])\s*"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{LOCATOR_PATTERN})?"
    r"(?P<tail>\s*[,，].+)"
    r"\s*$"
)
WIKILINK_PAREN_ITEM_RE = re.compile(
    r"^\s*"
    r"(?P<link>\[\[[^\]\n]+\]\])"
    r"\s*(?P<sep>[,，])\s*"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{LOCATOR_PATTERN})?"
    r"(?P<tail>\s*[,，].+)?"
    r"\s*$"
)
NARRATIVE_RE = re.compile(
    r"(?<![\w\]\)])"
    rf"(?P<author>{AUTHOR_PATTERN})"
    r"\s*[（(]"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{LOCATOR_PATTERN})?"
    r"[）)]"
)
WIKILINK_NARRATIVE_RE = re.compile(
    r"(?<![\w\]\)])"
    r"(?P<link>\[\[[^\]\n]+\]\])"
    r"\s*[（(]"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{LOCATOR_PATTERN})?"
    r"[）)]"
)
TAIL_CITATION_RE = re.compile(
    r"(?P<label>(?:[,，]\s*(?:(?:引自|引|cited in)\s*)?|(?:引自|引|cited in)\s*))"
    rf"(?P<author>{AUTHOR_PATTERN})"
    r"\s*(?P<sep>[,，])\s*"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{LOCATOR_PATTERN})?",
    re.IGNORECASE,
)


def run_git_changed() -> list[Path] | None:
    # Run `git status` first: it refreshes and persists the index stat cache,
    # which a bare `git diff HEAD` re-verifies on every run without saving.
    # Its untracked entries replace a separate `ls-files --others` call.
    untracked = subprocess.run(
        ["git", "-c", "core.quotePath=false", "status", "--porcelain=v1", "-z", "--untracked-files=all", "--", "wiki"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    untracked_paths = [entry[3:] for entry in untracked.stdout.split("\0") if entry.startswith("?? ")]
    changed = subprocess.run(
        ["git", "-c", "core.quotePath=false", "diff", "--name-only", "--diff-filter=ACMRTUXB", "HEAD", "--", "wiki"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if changed.returncode != 0 or untracked.returncode != 0:
        return None
    paths: list[Path] = []
    for line in [*changed.stdout.splitlines(), *untracked_paths]:
        path = ROOT / line.strip()
        if path.suffix.lower() == ".md" and WIKI_DIR in path.parents and path.exists():
            paths.append(path)
    return paths


def iter_target_markdown(full: bool, paths: list[str] | None = None) -> list[Path]:
    if paths:
        targets: list[Path] = []
        for raw in paths:
            path = (ROOT / raw).resolve() if not Path(raw).is_absolute() else Path(raw).resolve()
            try:
                path.relative_to(ROOT)
            except ValueError:
                continue
            if path.suffix.lower() == ".md" and WIKI_DIR in path.parents and path.exists():
                targets.append(path)
        return sorted(set(targets))
    if full:
        return sorted(WIKI_DIR.rglob("*.md")) if WIKI_DIR.exists() else []
    changed = run_git_changed()
    return sorted(set(changed)) if changed is not None else sorted(WIKI_DIR.rglob("*.md"))


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
    return re.sub(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])(?:\s+and\s+|\s*&\s*|\s*和\s*)(?=[A-ZÀ-ÖØ-Þ])", " & ", alias)


def normalize_author(author: str) -> str:
    return normalize_citation_alias(author)


def normalize_display_author(author: str, narrative: bool = False) -> str:
    author = re.sub(r"\s+", " ", author).strip()
    conjunction = " and " if narrative else " & "
    return re.sub(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])(?:\s+and\s+|\s*&\s*|\s*和\s*)(?=[A-ZÀ-ÖØ-Þ])", conjunction, author)


def normalize_locator(locator: str) -> str:
    locator = locator.replace("，", ",")
    return re.sub(r"^\s*,\s*", ", ", locator)


def display_parenthetical_author_year(author: str, sep: str, year: str) -> str:
    if sep == "，":
        return f"{author}，{year}"
    return f"{author}, {year}"


def wikilink_display(raw: str) -> str:
    inner = raw.strip()[2:-2].strip()
    if "\\|" in inner:
        return inner.split("\\|", 1)[1].strip()
    if "|" in inner:
        return inner.split("|", 1)[1].strip()
    return inner.split("#", 1)[0].strip()


def split_frontmatter(text: str) -> tuple[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return text[:m.end()], text[m.end():]


def mask_protected(text: str) -> tuple[str, list[str]]:
    protected: list[str] = []

    def repl(m: re.Match[str]) -> str:
        # Resolve earlier placeholders first: inline code may contain a
        # wikilink that was already masked, and unmask() is single-pass.
        protected.append(unmask(m.group(0), protected))
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


def link_tail_citations(tail: str, lookup: dict[str, dict[str, Any]], missing: list[str]) -> tuple[str, bool]:
    changed = False

    def repl(m: re.Match[str]) -> str:
        nonlocal changed
        display_author = normalize_display_author(m.group("author"))
        author = normalize_author(display_author)
        year = m.group("year").strip()
        locator = normalize_locator(m.group("locator") or "")
        key = f"{author}, {year}"
        entry = lookup.get(key)
        if not entry:
            missing.append(key)
            return m.group(0)
        changed = True
        display = f"{display_parenthetical_author_year(display_author, m.group('sep'), year)}{locator}"
        return f"{m.group('label')}{link_target(entry, display)}"

    return TAIL_CITATION_RE.sub(repl, tail), changed


def link_parenthetical_group(content: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str], opener: str = "(", closer: str = ")") -> str | None:
    parts = content.split(";")
    linked_parts: list[str] = []
    changed = False
    for raw in parts:
        item = raw.strip()
        m = PAREN_ITEM_RE.match(item)
        prefix_only = False
        wikilink_author = False
        if not m:
            m = PAREN_ITEM_PREFIX_RE.match(item)
            prefix_only = bool(m)
        if not m:
            m = WIKILINK_PAREN_ITEM_RE.match(item)
            wikilink_author = bool(m)
            prefix_only = bool(m and m.group("tail"))
        if not m:
            linked_parts.append(item)
            continue
        display_author = wikilink_display(m.group("link")) if wikilink_author else normalize_display_author(m.group("author"))
        author = normalize_author(display_author)
        year = m.group("year").strip()
        locator = normalize_locator(m.group("locator") or "")
        key = f"{author}, {year}"
        entry = lookup.get(key)
        tail = m.group("tail") if "tail" in m.groupdict() else None
        if not entry:
            missing.append(key)
            if tail:
                linked_tail, tail_changed = link_tail_citations(tail, lookup, missing)
                if tail_changed:
                    display_prefix = f"{display_parenthetical_author_year(display_author, m.group('sep'), year)}{locator}"
                    linked_parts.append(f"{display_prefix}{linked_tail}")
                    changed = True
                else:
                    linked_parts.append(item)
            else:
                linked_parts.append(item)
            continue
        display_prefix = f"{display_parenthetical_author_year(display_author, m.group('sep'), year)}{locator}"
        if prefix_only:
            linked_tail, _ = link_tail_citations(tail or "", lookup, missing)
            linked_parts.append(f"{link_target(entry, display_prefix)}{linked_tail}")
        else:
            linked_parts.append(link_target(entry, display_prefix))
        changed = True
    if not changed:
        return None
    stats["linked_parenthetical"] += 1
    return opener + "; ".join(linked_parts) + closer


def link_parenthetical(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        opener = m.group(0)[0]
        closer = "）" if opener == "（" else ")"
        linked = link_parenthetical_group(m.group(1), lookup, stats, missing, opener, closer)
        return linked or m.group(0)

    text = PAREN_GROUP_RE.sub(repl, text)
    text = FULLWIDTH_PAREN_GROUP_RE.sub(repl, text)
    return text


def link_wikilink_parenthetical(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        if "[[" not in m.group(1):
            return m.group(0)
        opener = m.group(0)[0]
        closer = "）" if opener == "（" else ")"
        linked = link_parenthetical_group(m.group(1), lookup, stats, missing, opener, closer)
        return linked or m.group(0)

    text = PAREN_GROUP_RE.sub(repl, text)
    text = FULLWIDTH_PAREN_GROUP_RE.sub(repl, text)
    return text


def _is_cjk(ch: str) -> bool:
    return "\u3400" <= ch <= "\u9fff"


def author_start_candidates(raw: str) -> list[int]:
    """Offsets where an author name could start inside a greedy AUTHOR_PATTERN match.

    AUTHOR_PATTERN allows CJK characters and spaces so that Chinese authors and
    multi-word names match, but in running Chinese prose that lets the match
    swallow the preceding sentence ("对称对比条目，共同构成 Li"). Trying the
    suffixes that start at a word/script boundary recovers the real author.
    """
    starts = [0]
    for i in range(1, len(raw)):
        prev, ch = raw[i - 1], raw[i]
        if prev.isspace() and not ch.isspace():
            starts.append(i)
        elif _is_cjk(ch) and not prev.isspace():
            starts.append(i)
        elif ch.isupper() and _is_cjk(prev):
            starts.append(i)
    # A suffix right after a conjunction is a co-author, not the first author:
    # "Yamamoto and Li (2012)" must never be linked as "Li (2012)".
    return [i for i in starts if i == 0 or not CONJUNCTION_TAIL_RE.search(raw[:i])]


# Conjunction, optionally followed by given names: "Bolton 与 John Hattie".
# Only when a name precedes the conjunction inside the match; "Li (2012) 与 Li (2012)"
# starts its second match at "与", so nothing precedes it there.
CONJUNCTION_TAIL_RE = re.compile(r"[^\s&、,，]\s*(?:\band|&|与|和|及|、|[,，])\s*(?:[A-Z][\w'’.-]*\s+)*$")


def link_narrative(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        raw_author = m.group("author")
        year = m.group("year").strip()
        locator = normalize_locator(m.group("locator") or "")
        first_key = None
        for start in author_start_candidates(raw_author):
            candidate = raw_author[start:]
            if not (candidate[:1].isupper() or _is_cjk(candidate[:1])):
                continue
            display_author = normalize_display_author(candidate, narrative=True)
            key = f"{normalize_author(display_author)} ({year})"
            first_key = first_key or key
            entry = lookup.get(key)
            if entry:
                stats["linked_narrative"] += 1
                return raw_author[:start] + link_target(entry, f"{display_author} ({year}{locator})")
        missing.append(first_key or f"{raw_author} ({year})")
        return m.group(0)
    return NARRATIVE_RE.sub(repl, text)


def link_wikilink_narrative(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        display_author = normalize_display_author(wikilink_display(m.group("link")), narrative=True)
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
    return WIKILINK_NARRATIVE_RE.sub(repl, text)


YEAR_TOKEN_RE = re.compile(r"((?:19|20)\d{2})([a-z])?")
DISPLAY_WIKILINK_RE = re.compile(r"\[\[([^\]\n|]+)\|([^\]\n]+)\]\]")


def build_target_aliases(lookup: dict[str, dict[str, Any]]) -> dict[str, list[str]]:
    targets: dict[str, list[str]] = {}
    for alias, entry in lookup.items():
        arg = entry.get("argument")
        if not arg:
            continue
        targets.setdefault(arg, [])
        if alias not in targets[arg]:
            targets[arg].append(alias)
    return targets


def rewrite_drifted_display(display: str, aliases: list[str]) -> str | None:
    """Rewrite an Argument link display whose a/b/c suffix drifted from citation_aliases.

    'Cohen et al., 2011, p. 30' -> 'Cohen et al., 2011a, p. 30' when the target's
    alias is 'Cohen et al., 2011a'. Returns None when no safe rewrite exists.
    """
    m = YEAR_TOKEN_RE.search(display)
    if not m:
        return None
    narrative = display[: m.start()].rstrip().endswith(("(", "（"))
    d_author = normalize_author(display[: m.start()].strip(" ,，（(")).lower()
    if not d_author:
        return None
    tail = display[m.end():]
    for alias in aliases:
        am = YEAR_TOKEN_RE.search(alias)
        if not am:
            continue
        if alias[: am.start()].rstrip().endswith(("(", "（")) != narrative:
            continue
        if normalize_author(alias[: am.start()].strip(" ,，（(")).lower() != d_author:
            continue
        if am.group(1) != m.group(1):
            continue
        # Replace only the year token so any wrapping text/parens are preserved.
        candidate = display[: m.start()] + am.group(0) + tail
        return candidate if candidate != display else None
    return None


def fix_display_suffixes(text: str, targets: dict[str, list[str]], stats: dict[str, int]) -> str:
    fm, body = split_frontmatter(text)

    def repl(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        display = match.group(2).strip()
        aliases = targets.get(target)
        if not aliases:
            return match.group(0)
        fixed = rewrite_drifted_display(display, aliases)
        if fixed is None:
            return match.group(0)
        stats["fixed_display"] += 1
        return f"[[{target}|{fixed}]]"

    return fm + DISPLAY_WIKILINK_RE.sub(repl, body)


SOURCES_HEADING_RE = re.compile(r"^##\s+(?:来源|Sources?)\s*$", re.M)
HEADING_LINE_RE = re.compile(r"^#{1,6}\s.*$", re.M)
PART_OF_RE = re.compile(r"^part_of:\s*[\"']?\[\[([^\]|#]+)", re.M)


def self_targets_for(path: Path | None, fm: str) -> set[str]:
    if path is None:
        return set()
    targets = {path.stem}
    m = PART_OF_RE.search(fm)
    if m:
        targets.add(m.group(1).strip())
    return targets


def link_text(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str], path: Path | None = None) -> str:
    fm, body = split_frontmatter(text)
    # Reference lists under "## 来源/Sources" are bibliography, not prose.
    m = SOURCES_HEADING_RE.search(body)
    body, sources_tail = (body[:m.start()], body[m.start():]) if m else (body, "")
    selfs = self_targets_for(path, fm)
    if selfs:
        lookup = {k: v for k, v in lookup.items() if v.get("argument") not in selfs}
    body = link_wikilink_parenthetical(body, lookup, stats, missing)
    body = link_wikilink_narrative(body, lookup, stats, missing)
    masked, protected = mask_protected(body)
    # Headings stay plain: a link in a heading changes its anchor.
    def protect_heading(h: re.Match[str]) -> str:
        protected.append(unmask(h.group(0), protected))
        return f"\uE000{len(protected) - 1}\uE001"

    masked = HEADING_LINE_RE.sub(protect_heading, masked)
    masked = link_parenthetical(masked, lookup, stats, missing)
    masked = link_narrative(masked, lookup, stats, missing)
    return fm + escape_table_pipes(unmask(masked, protected)) + sources_tail


TABLE_LINE_RE = re.compile(r"^\s*(?:>\s*)*\|")
UNESCAPED_ARG_LINK_RE = re.compile(r"\[\[(Argument_[^\]|\\\n]+)\|")


def escape_table_pipes(body: str) -> str:
    """Inside Markdown table rows, a wikilink alias pipe must be written as \\|."""
    if "|" not in body:
        return body
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if TABLE_LINE_RE.match(line) and "[[Argument_" in line:
            lines[i] = UNESCAPED_ARG_LINK_RE.sub(lambda m: f"[[{m.group(1)}\\|", line)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Link APA short citations to Argument pages.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing.")
    parser.add_argument("--full", action="store_true", help="Process all wiki Markdown files.")
    parser.add_argument("--fix-display", action="store_true", help="Also rewrite Argument link displays whose a/b/c year suffix drifted from citation_aliases.")
    parser.add_argument("paths", nargs="*", help="Optional wiki Markdown files to process.")
    args = parser.parse_args()

    if not CITATION_FULL_JSON.exists():
        print("❌ citation/citation_full.json missing; run scripts/vault_index.py first.")
        return 1

    lookup = load_lookup()
    stats = {"linked_parenthetical": 0, "linked_narrative": 0, "fixed_display": 0}
    targets = build_target_aliases(lookup) if args.fix_display else {}
    missing: list[str] = []
    changed = 0
    for path in iter_target_markdown(full=args.full, paths=args.paths):
        if should_skip(path):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        before = dict(stats)
        new_text = link_text(text, lookup, stats, missing, path)
        if args.fix_display:
            new_text = fix_display_suffixes(new_text, targets, stats)
        if new_text != text:
            changed += 1
            rel = path.relative_to(ROOT)
            print(f"✏️  {rel} parenthetical={stats['linked_parenthetical'] - before['linked_parenthetical']} narrative={stats['linked_narrative'] - before['linked_narrative']}")
            if not args.dry_run:
                path.write_text(new_text, encoding="utf-8")

    print(f"{'[dry-run] ' if args.dry_run else ''}files changed: {changed}")
    print(f"🔗 linked parenthetical groups: {stats['linked_parenthetical']}")
    print(f"🔗 linked narrative citations: {stats['linked_narrative']}")
    if args.fix_display:
        print(f"🔧 fixed drifted citation displays: {stats['fixed_display']}")
    if missing:
        print("⚠️ unresolved citation aliases:")
        for item in sorted(set(missing))[:200]:
            print(f"  - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
