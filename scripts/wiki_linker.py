#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import bisect
import contextlib
import fcntl
import io
import json
import os
import sys
import re
import subprocess
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
INDEX_JSON = WIKI_DIR / "index.json"
SOURCES_DIR = ROOT / "sources"
BOOKS_DIR = ROOT / "books"
LINK_EXCEPTIONS = ROOT / "scripts/link_exceptions.json"

EXCLUDE_DIR_PARTS = {"templates", "indexes", ".obsidian"}
EXCLUDE_FILENAMES = {
    "index.md",
    "index.json",
    "manifest.md",
    "manifest.json",
    "research-map.md",
}

# A conservative skip list for generated/source-like areas. This is structural,
# not a semantic stopword list. The actual link whitelist is wiki/index.json.
SOURCE_DIRS = {"sources", "raw", "books", "scripts"}

WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]|#]+?)(?:#[^\]|]+)?(?:(?:\\\||\|)([^\]]+))?\]\]")
EMBED_RE = re.compile(r"!\[\[[^\]]+\]\]")
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\([^)]*\)")
URL_RE = re.compile(r"https?://\S+|doi:\s*\S+|10\.\d{4,9}/\S+", re.IGNORECASE)
HTML_TAG_RE = re.compile(r"<[^>]+>")
SOURCE_SECTION_NAMES = {"来源", "sources", "source"}
YAML_AUTHOR_LINK_KEYS = {"authors", "editors"}
CITATION_AUTHOR_PATTERN = r"[A-Z\u3400-\u9fff][A-Za-zÀ-ÖØ-öø-ÿ\u3400-\u9fff0-9'’ .&和等-]*(?:\s+(?:&|and)\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ0-9'’ .-]+|\s+et\s+al\.)?"
CITATION_PAREN_GROUP_RE = re.compile(r"(?<!\[)\([^()\n]*\b\d{4}[a-z]?[^()\n]*\)")
CITATION_FULLWIDTH_PAREN_GROUP_RE = re.compile(r"（[^（）\n]*\b\d{4}[a-z]?[^（）\n]*）")
CITATION_NARRATIVE_RE = re.compile(
    r"(?<![\w\]\)])"
    rf"{CITATION_AUTHOR_PATTERN}"
    r"\s*[（(]\d{4}[a-z]?(?:\s*[,，]\s*(?:p\.|pp\.)\s*[^)）]+)?[）)]"
)

CALLOUT_MARKER_RE = re.compile(r"^(?:>\s*)+\[![^\]\s]+(?:\]\])?\]")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")
TABLE_UNSAFE_CELL_RE = re.compile(
    r"`|\$|\[\[|\]\]|!?\[[^\]]*\]\([^)]*\)|https?://|doi:\s*\S+|10\.\d{4,9}/\S+|<[^>]+>",
    re.IGNORECASE,
)
BOLD_HEADING_COLON_RE = re.compile(r"(\*\*[^*\n]+?\*\*)[ \t]*[：:][ \t]*")
BOLD_HEADING_ENGLISH_OUTSIDE_RE = re.compile(
    r"\*\*([^*\n]*[\u3400-\u9fff][^*\n]*)\*\*[ \t]*([（(][^）)\n]*[A-Za-z][^）)\n]*[）)])"
)


LINK_EXCEPTION_LINK_RE = re.compile(r'(?<!!)\[\[([^\]|#]+?)(?:#[^\]|]+)?(?:(?:\\\||\|)([^\]]+))?\]\]')


@contextlib.contextmanager
def link_exception_lock(root):
    path = root / 'output/link-exceptions.lock'
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def clean_link_exceptions(root, registry, dry_run=False):
    with link_exception_lock(root):
        original = load_link_exceptions(registry)
        active = prune_link_exceptions(root, original)
        if active != original and not dry_run: save_link_exceptions(registry, active)
    return original, active


def link_exception_text(text):
    return unicodedata.normalize('NFC', re.sub(r'\s+', ' ', text).strip())


def link_exception_visible_map(text):
    """Visible wiki labels with source offsets, so linking does not change identity."""
    chars, offsets = [], []
    cursor = 0
    for match in LINK_EXCEPTION_LINK_RE.finditer(text):
        for pos in range(cursor, match.start()):
            chars.append(text[pos]); offsets.append((pos, pos + 1))
        label = match[2] if match[2] is not None else match[1]
        for char in label:
            chars.append(char); offsets.append((match.start(), match.end()))
        cursor = match.end()
    for pos in range(cursor, len(text)):
        chars.append(text[pos]); offsets.append((pos, pos + 1))
    return ''.join(chars), offsets


def link_exception_sentences(body):
    """Sentence units never cross a line or table cell; preserve raw offsets."""
    visible, offsets = link_exception_visible_map(body)
    # English full stops split only before whitespace/end, not within decimals/URLs.
    for match in re.finditer(r'[^\n|。！？!?]+(?:[。！？!?][”’」』\"\']*|(?=\n|\||$))', visible):
        start, end = match.span()
        unit = visible[start:end]
        prefix = re.match(r'^\s*(?:>\s*)*(?:(?:[-*+] |\d+[.)] )|#{1,6} )?', unit)
        start += prefix.end()
        while end > start and visible[end - 1].isspace(): end -= 1
        if start == end: continue
        for part in re.finditer(r'.+?(?:\.(?=\s|$)|$)', visible[start:end]):
            a, b = start + part.start(), start + part.end()
            while a < b and visible[a].isspace(): a += 1
            if a < b:
                yield link_exception_text(visible[a:b]), offsets[a][0], offsets[b - 1][1]


def link_exception_body(text):
    return re.sub(r'\A---\s*\n.*?\n---\s*\n', '', text, count=1, flags=re.S)


def valid_link_exception_path(name):
    if not isinstance(name, str): return False
    path = Path(name)
    return (isinstance(name, str) and name.startswith('wiki/') and path.suffix == '.md'
            and not path.is_absolute() and '..' not in path.parts and '\\' not in name
            and path.as_posix() == name and unicodedata.normalize('NFC', name) == name
            and 'templates' not in path.parts and 'indexes' not in path.parts)


def load_link_exceptions(path):
    if not path.exists(): return {}
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result: raise ValueError(f'重复例外路径: {key}')
            result[key] = value
        return result
    data = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs)
    if not isinstance(data, dict): raise ValueError('链接例外表必须是 JSON 对象')
    for name, records in data.items():
        if not valid_link_exception_path(name) or not isinstance(records, list): raise ValueError(f'无效例外路径: {name}')
        seen = set()
        for record in records:
            if (not isinstance(record, dict) or set(record) != {'sentence', 'target'}
                    or not isinstance(record['sentence'], str) or not record['sentence']
                    or link_exception_text(record['sentence']) != record['sentence']
                    or not isinstance(record['target'], str) or not valid_link_exception_path(record['target'])):
                raise ValueError(f'无效链接例外: {name}')
            key = record['sentence'], record['target']
            if key in seen: raise ValueError(f'重复链接例外: {name}')
            seen.add(key)
    return data


def save_link_exceptions(path, data):
    temp = path.with_suffix('.json.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(path)


def prune_link_exceptions(root, data):
    """Only confirmed absence expires records; read errors propagate, never delete."""
    kept = {}
    for name, records in data.items():
        path = root / name
        try: text = path.read_text(encoding='utf-8')
        except FileNotFoundError: continue
        units = {sentence for sentence, _, _ in link_exception_sentences(link_exception_body(text))}
        active = []
        for record in records:
            try: (root / record['target']).stat()
            except FileNotFoundError: continue
            if record['sentence'] in units: active.append(record)
        if active: kept[name] = active
    return kept


def mask_link_exceptions(body, records, entries, boundary):
    """Hide only excluded occurrences before the unchanged ordinary-link pipeline."""
    if not records: return body, {}
    entries = list(entries)
    by_path = {e.path: e for e in entries if e.type in {'concept', 'theory', 'method', 'instrument', 'person', 'fact'}}
    units = list(link_exception_sentences(body))
    counts = Counter(sentence for sentence, _, _ in units)
    if any(counts[r['sentence']] > 1 for r in records):
        raise ValueError('链接例外句子重复，请先改写区分或移除该例外')
    names = {}
    all_terms = []
    for entry in entries:
        for name in (entry.path, entry.path.removesuffix('.md'), entry.title, *entry.aliases):
            names.setdefault(link_exception_text(name).casefold(), set()).add(entry.path)
        if entry.path in by_path:
            all_terms.extend((term, entry.path) for term in {entry.title, *entry.aliases} if term)
    protected = []
    # Preserve code, embeds, Markdown links and HTML; exclusions never edit these.
    for rx in (r'(?ms)^\s*(?:>\s*)?(`{3,}|~{3,})[^\n]*\n.*?^\s*(?:>\s*)?\1[^\n]*',
               r'`+[^`\n]*`+', r'!\[\[[^\]]*\]\]', r'!?\[[^\]]*\]\([^)]*\)', r'<[^>]*>'):
        protected.extend(m.span() for m in re.finditer(rx, body))
    spans = []
    for sentence, start, end in units:
        blocked = {r['target'] for r in records if r['sentence'] == sentence and r['target'] in by_path}
        if not blocked: continue
        raw = body[start:end]
        links = list(LINK_EXCEPTION_LINK_RE.finditer(raw))
        for match in links:
            targets = names.get(link_exception_text(match[1]).casefold(), set())
            if len(targets) == 1 and targets <= blocked:
                label = match[2] if match[2] is not None else match[1]
                spans.append((start + match.start(), start + match.end(), label))
        for target in blocked:
            entry = by_path.get(target)
            if entry is None: continue
            terms = sorted({entry.title, *entry.aliases}, key=len, reverse=True)
            for term in terms:
                for match in re.finditer(re.escape(term), raw, re.I):
                    if any(a.start() < match.end() and a.end() > match.start() for a in links): continue
                    if boundary(raw, match.start(), match.end(), term):
                        # Do not mask a short alias inside another target's longer term.
                        longer = False
                        for other, other_target in all_terms:
                            if other_target == target or len(other) <= len(term): continue
                            for candidate in re.finditer(re.escape(other), raw, re.I):
                                if (candidate.start() <= match.start() and candidate.end() >= match.end()
                                        and boundary(raw, candidate.start(), candidate.end(), other)):
                                    longer = True
                                    break
                            if longer: break
                        if longer: continue
                        spans.append((start + match.start(), start + match.end(), match[0]))
    selected = []
    for a, b, label in sorted(set(spans), key=lambda s: (s[0], -s[1])):
        if any(p < b and q > a for p, q in protected): continue
        if selected and a < selected[-1][1]: continue
        selected.append((a, b, label))
    prefix = '\ue100'
    while prefix in body: prefix += '\ue100'
    out, replacements, cursor = [], {}, 0
    for number, (a, b, label) in enumerate(selected):
        token = prefix + '\ue102' * (number + 1) + '\ue101'
        replacements[token] = label
        out.extend((body[cursor:a], token)); cursor = b
    out.append(body[cursor:])
    return ''.join(out), replacements


def restore_link_exceptions(body, replacements):
    if not replacements: return body
    pattern = '|'.join(re.escape(t) for t in sorted(replacements, key=len, reverse=True))
    return re.sub(pattern, lambda m: replacements[m[0]], body)


def count_unescaped_pipes(line: str) -> int:
    count = 0
    escaped = False
    for ch in line.rstrip("\n"):
        if escaped:
            escaped = False
            continue
        if ch == "\\":
            escaped = True
            continue
        if ch == "|":
            count += 1
    return count


def unescaped_pipe_positions(line: str) -> list[int]:
    positions: list[int] = []
    escaped = False
    core = line.rstrip("\n")
    for i, ch in enumerate(core):
        if escaped:
            escaped = False
            continue
        if ch == "\\":
            escaped = True
            continue
        if ch == "|":
            positions.append(i)
    return positions


def markdown_table_content(line: str) -> str:
    stripped = line.strip()
    while stripped.startswith(">"):
        stripped = stripped[1:].lstrip()
    return stripped


def is_markdown_table_separator_line(line: str) -> bool:
    return bool(TABLE_SEPARATOR_RE.match(markdown_table_content(line)))


def is_markdown_table_line(line: str) -> bool:
    stripped = markdown_table_content(line)
    if not stripped or stripped.startswith("```"):
        return False
    if is_markdown_table_separator_line(line):
        return True
    # Require pipe-bounded Markdown tables. This avoids treating prose with two
    # alias wikilinks as a table just because wikilink aliases also contain pipes.
    return stripped.startswith("|") and count_unescaped_pipes(stripped) >= 2


def is_safe_table_cell(cell: str) -> bool:
    stripped = cell.strip()
    if not stripped:
        return False
    return TABLE_UNSAFE_CELL_RE.search(cell) is None


def unsafe_table_cell_spans(line: str) -> list[tuple[int, int]]:
    """Return character spans for Markdown table cells that should not be linked."""
    if is_markdown_table_separator_line(line):
        return []
    positions = unescaped_pipe_positions(line)
    if len(positions) < 2:
        return []

    spans: list[tuple[int, int]] = []
    cursor = positions[0] + 1
    for pipe_pos in positions[1:]:
        cell = line[cursor:pipe_pos]
        if cell.strip() and not is_safe_table_cell(cell):
            spans.append((cursor, pipe_pos))
        cursor = pipe_pos + 1
    return spans


def escape_table_wikilink_pipes_with_count(line: str) -> tuple[str, int]:
    """Escape wikilink alias separators inside Markdown table rows."""
    if not is_markdown_table_line(line):
        return line, 0

    escaped = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal escaped
        target = m.group(1)
        display = m.group(2)
        if display is None:
            return m.group(0)
        replacement = f"[[{target}\\|{display}]]"
        if replacement != m.group(0):
            escaped += 1
        return replacement

    return WIKILINK_RE.sub(repl, line), escaped


def escape_table_wikilink_pipes(line: str) -> str:
    return escape_table_wikilink_pipes_with_count(line)[0]


def escape_table_wikilink_pipes_in_text(text: str) -> str:
    """Normalize wikilink alias separators in all Markdown table rows."""
    return "".join(escape_table_wikilink_pipes(line) for line in text.splitlines(keepends=True))


def normalize_table_wikilink_pipes_in_text(text: str) -> tuple[str, int]:
    """Normalize wikilink alias separators in Markdown tables and count changes."""
    out: list[str] = []
    escaped = 0
    for line in text.splitlines(keepends=True):
        next_line, count = escape_table_wikilink_pipes_with_count(line)
        out.append(next_line)
        escaped += count
    return "".join(out), escaped


@dataclass(frozen=True)
class Entry:
    title: str
    path: str
    aliases: tuple[str, ...]
    type: str = ""


def is_argument_entry(entry: Entry | None) -> bool:
    return bool(entry and entry.type == "argument")


def is_argument_target(target: str, entries_by_title: dict[str, Entry] | None = None) -> bool:
    if entries_by_title is not None and target in entries_by_title:
        return is_argument_entry(entries_by_title[target])
    return target.startswith("Argument_")


@dataclass(frozen=True)
class Term:
    text: str
    target: str
    is_alias: bool
    entry_type: str = ""


class TermMatcher:
    """Index terms in tries so matching cost depends on term length, not term count."""

    _TERMINALS = ""

    def __init__(self, terms: list[Term]) -> None:
        self._exact: dict[str, dict] = {}
        self._folded: dict[str, dict] = {}
        self._rank = {term: rank for rank, term in enumerate(terms)}
        # Cheap prefilter used by link_plain_text: a position can only match if
        # its first char (1-char terms) or first two chars (longer terms) begin
        # some term, compared the same way the tries compare (exact / casefold).
        self.exact1: set[str] = set()
        self.exact2: set[str] = set()
        self.folded1: set[str] = set()
        self.folded2: set[str] = set()
        for term in terms:
            has_ascii_alpha = any(ch.isascii() and ch.isalpha() for ch in term.text)
            exact_only = not has_ascii_alpha or (len(term.text) <= 3 and term.text.isupper())
            root = self._exact if exact_only else self._folded
            keys = list(term.text) if exact_only else [ch.casefold() for ch in term.text]
            if keys:
                if len(keys) == 1:
                    (self.exact1 if exact_only else self.folded1).add(keys[0])
                else:
                    (self.exact2 if exact_only else self.folded2).add(keys[0] + keys[1])
            node = root
            for key in keys:
                node = node.setdefault(key, {})
            node.setdefault(self._TERMINALS, []).append(term)

    @staticmethod
    def _matches_from(root: dict[str, dict], text: str, start: int, *, folded: bool) -> list[Term]:
        # Walk by index: slicing text[start:] copied the rest of the chunk on
        # every call, making each chunk quadratic in its length.
        matches: list[Term] = []
        node = root
        terminals = TermMatcher._TERMINALS
        for idx in range(start, len(text)):
            char = text[idx]
            child = node.get(char.casefold() if folded else char)
            if child is None:
                break
            node = child
            found = node.get(terminals)
            if found:
                matches.extend(found)
        return matches

    def matches_at(self, text: str, start: int) -> list[Term]:
        first = text[start]
        if first not in self._exact and first.casefold() not in self._folded:
            return []
        matches = self._matches_from(self._exact, text, start, folded=False)
        matches.extend(self._matches_from(self._folded, text, start, folded=True))
        matches = [term for term in matches if match_term_at(text, start, term.text)]
        matches.sort(key=self._rank.__getitem__)
        return matches


@dataclass(frozen=True)
class PersonPrefixConflict:
    shorter: Term
    longer: Term


@dataclass
class PersonPrefixRegistry:
    """Person terms where one known name is a lexical prefix of another."""

    conflicts: tuple[PersonPrefixConflict, ...]
    longer_terms: frozenset[Term]


@dataclass
class LinkStats:
    files_changed: int = 0
    links_added: int = 0
    links_removed: int = 0
    table_pipes_escaped: int = 0
    heading_styles_normalized: int = 0


def load_entries() -> list[Entry]:
    if not INDEX_JSON.exists():
        raise SystemExit(f"index not found: {INDEX_JSON}. Run `python3 scripts/vault_index.py --wiki-only` first.")
    raw = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    entries: list[Entry] = []
    for item in raw:
        title = str(item.get("title") or "").strip()
        path = str(item.get("path") or "").strip()
        aliases = tuple(str(x).strip() for x in item.get("aliases", []) if str(x).strip())
        entry_type = str(item.get("type") or "").strip()
        if title and path:
            entries.append(Entry(title=title, path=path, aliases=aliases, type=entry_type))
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
                entries.append(Entry(title=title, path=rel_to_root(path), aliases=(), type="source"))
    return entries


def make_source_pattern(source_titles: set[str]) -> re.Pattern[str] | None:
    if not source_titles:
        return None
    alternatives = sorted((re.escape(t) for t in source_titles if t), key=len, reverse=True)
    if not alternatives:
        return None
    return re.compile(r"(?<![\w/])(" + "|".join(alternatives) + r")(?![\w/])")


def make_source_links(source_entries: list[Entry]) -> dict[str, str]:
    links: dict[str, str] = {}
    for entry in source_entries:
        target = entry.path[:-3] if entry.path.endswith(".md") else entry.path
        links[entry.title] = f"[[{target}|{entry.title}]]"
    return links


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
        # Argument pages are citation targets. They are not linked by the
        # ordinary title/alias linker, because citation links are governed by
        # citation/citation_full.json and citation/citation_ambiguous.json.
        if e.type == "argument":
            continue
        for text, is_alias in [(e.title, False), *[(a, True) for a in e.aliases]]:
            text = text.strip()
            if not text:
                continue
            key = (text, e.title)
            if key in seen:
                continue
            seen.add(key)
            terms.append(Term(text=text, target=e.title, is_alias=is_alias, entry_type=e.type))

    # Longest first prevents linking "Culture" inside "World Culture Theory".
    terms.sort(key=lambda t: len(t.text), reverse=True)
    return terms, entries_by_title, path_to_title


def is_person_prefix(shorter: Term, longer: Term) -> bool:
    if shorter.entry_type != "person" or longer.entry_type != "person":
        return False
    if shorter.target == longer.target or len(shorter.text) >= len(longer.text):
        return False
    if not longer.text.casefold().startswith(shorter.text.casefold()):
        return False

    remainder = longer.text[len(shorter.text) :]
    return bool(remainder and (remainder[0].isspace() or remainder[0] in ",.-–—()"))


def build_person_prefix_registry(terms: list[Term]) -> PersonPrefixRegistry:
    """Register cross-person prefix collisions such as Peterson, A. / Peterson, A. D. C."""

    person_terms = [term for term in terms if term.entry_type == "person"]
    conflicts: list[PersonPrefixConflict] = []
    seen: set[tuple[str, str, str, str]] = set()

    # Candidates for "longer starts with shorter" are contiguous after the
    # shorter text in casefold order, so look only there instead of comparing
    # every pair. Candidates keep their original order so dedupe below picks
    # the same Term objects as the previous all-pairs loop.
    folded = [term.text.casefold() for term in person_terms]
    order = sorted(range(len(person_terms)), key=folded.__getitem__)
    sorted_keys = [folded[i] for i in order]

    for shorter_idx, shorter in enumerate(person_terms):
        prefix = folded[shorter_idx]
        pos = bisect.bisect_left(sorted_keys, prefix)
        candidates = []
        while pos < len(sorted_keys) and sorted_keys[pos].startswith(prefix):
            candidates.append(order[pos])
            pos += 1
        for longer in (person_terms[i] for i in sorted(candidates)):
            if not is_person_prefix(shorter, longer):
                continue
            key = (shorter.text.casefold(), shorter.target, longer.text.casefold(), longer.target)
            if key in seen:
                continue
            seen.add(key)
            conflicts.append(PersonPrefixConflict(shorter=shorter, longer=longer))

    conflicts.sort(key=lambda item: (item.shorter.text.casefold(), item.longer.text.casefold(), item.longer.target))
    return PersonPrefixRegistry(
        conflicts=tuple(conflicts),
        longer_terms=frozenset(item.longer for item in conflicts),
    )


def entry_terms(entry: Entry) -> set[str]:
    return {t.text for t in make_terms([entry])[0]}


def parse_entry_from_text(rel_path: str, text: str) -> Entry | None:
    path = ROOT / rel_path
    if rel_path.startswith("sources/") and path.suffix.lower() == ".md":
        return Entry(title=path.stem, path=rel_path, aliases=(), type="source")

    fm, _ = split_frontmatter(text)
    if not fm:
        return None

    title = ""
    entry_type = ""
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
        elif stripped.startswith("type:"):
            entry_type = stripped.split(":", 1)[1].strip().strip("'\"")
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
    return Entry(title=title, path=rel_path, aliases=tuple(a for a in aliases if a), type=entry_type)


def git_output(args: list[str]) -> str:
    result = subprocess.run(
        ["git", "-c", "core.quotePath=false", *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        return ""
    return result.stdout


def git_files_at_ref(ref: str, rel_paths: Iterable[str]) -> dict[str, str]:
    """Read many historical files through one `git cat-file --batch` process."""
    paths = list(rel_paths)
    if not paths:
        return {}
    requests = "".join(f"{ref}:{path}\n" for path in paths).encode()
    result = subprocess.run(
        ["git", "cat-file", "--batch"],
        cwd=ROOT,
        input=requests,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        return {}

    stream = io.BytesIO(result.stdout)
    files: dict[str, str] = {}
    for path in paths:
        header = stream.readline().rstrip(b"\n")
        if not header or header.endswith(b" missing"):
            continue
        try:
            size = int(header.rsplit(b" ", 1)[1])
        except (IndexError, ValueError):
            return {}
        content = stream.read(size)
        stream.read(1)  # trailing newline emitted by cat-file --batch
        files[path] = content.decode("utf-8", errors="replace")
    return files


def parse_name_status_z(output: str) -> set[str]:
    parts = output.split("\0")
    paths: set[str] = set()
    i = 0
    while i < len(parts) and parts[i]:
        status = parts[i]
        i += 1
        if status.startswith(("R", "C")):
            if i + 1 >= len(parts):
                break
            paths.update((parts[i], parts[i + 1]))
            i += 2
        else:
            if i >= len(parts):
                break
            paths.add(parts[i])
            i += 1
    return {path for path in paths if path}


def git_changed_paths() -> set[str]:
    # `git status` refreshes and persists the index stat cache; a bare
    # `git diff HEAD` re-verifies stale entries every run without saving
    # (~8 s on this vault vs ~0.1 s after a refresh). Its output also gives
    # the untracked files, replacing a separate `ls-files --others` call.
    status = git_output(["status", "--porcelain=v1", "-z", "--untracked-files=all", "--", "wiki", "sources"])
    untracked = {entry[3:] for entry in status.split("\0") if entry.startswith("?? ")}
    changed = parse_name_status_z(
        git_output(
            ["diff", "--name-status", "-z", "--find-renames", "--diff-filter=ACDMRTUXB", "HEAD", "--", "wiki", "sources"]
        )
    )
    return changed | untracked


def git_commit_changed_paths(ref: str = "HEAD") -> set[str]:
    return parse_name_status_z(
        git_output(
            [
                "diff-tree",
                "--root",
                "--no-commit-id",
                "--name-status",
                "-z",
                "--find-renames",
                "-r",
                "--diff-filter=ACDMRTUXB",
                ref,
                "--",
                "wiki",
                "sources",
            ]
        )
    )


def git_changed_terms(paths: set[str], previous_ref: str = "HEAD") -> tuple[set[str], set[str], set[str]]:
    changed_files: set[str] = set()
    added_terms: set[str] = set()
    removed_terms: set[str] = set()
    markdown_paths = sorted(rel for rel in paths if rel.endswith(".md"))
    previous_texts = git_files_at_ref(previous_ref, markdown_paths)

    for rel in paths:
        path = ROOT / rel
        if path.suffix.lower() != ".md":
            continue
        if rel.startswith("wiki/"):
            if should_skip_file(path):
                continue
            if path.exists():
                changed_files.add(rel)
            elif rel not in previous_texts:
                continue
        elif not rel.startswith("sources/"):
            continue

        current_entry = None
        if path.exists():
            current_entry = parse_entry_from_text(rel, path.read_text(encoding="utf-8", errors="ignore"))
        previous_text = previous_texts.get(rel, "")
        previous_entry = parse_entry_from_text(rel, previous_text) if previous_text else None

        current_terms = entry_terms(current_entry) if current_entry else set()
        previous_terms = entry_terms(previous_entry) if previous_entry else set()
        added_terms.update(current_terms - previous_terms)
        removed_terms.update(previous_terms - current_terms)

    return changed_files, added_terms, removed_terms


def iter_git_target_files() -> list[Path]:
    paths = git_changed_paths()
    previous_ref = "HEAD"
    if not paths:
        paths = git_commit_changed_paths("HEAD")
        previous_ref = "HEAD^"
        if paths:
            print("No uncommitted wiki/source changes found; using files changed in HEAD instead of --full.")

    changed_files, added_terms, removed_terms = git_changed_terms(paths, previous_ref=previous_ref)
    search_terms = {t for t in added_terms | removed_terms if t}

    candidates = {ROOT / rel for rel in changed_files}
    if search_terms:
        search_pattern = re.compile("|".join(re.escape(term) for term in sorted(search_terms, key=len, reverse=True)))
        for path in iter_target_files([]):
            text = path.read_text(encoding="utf-8", errors="ignore")
            if search_pattern.search(text):
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


def split_protected_spans(text: str, protect_wikilinks: bool = True) -> list[tuple[bool, str]]:
    """
    Split section text into (protected, chunk).

    Protected chunks are not edited. This avoids frontmatter/body handled elsewhere,
    code blocks, headings, quote callouts, HTML, URLs/DOIs, Markdown links,
    existing wikilinks, and embeds. Other Obsidian callouts remain linkable;
    generated [!metax*] callouts are protected like quote callouts.

    `protect_wikilinks=False` is used by normalize_bold_heading_style(). Ordinary
    (non-Argument) wikilinks are left unprotected there, because protecting them
    would hide any CJK text inside a freshly-inserted `[[Target|CJK]]` link from
    the bold/English-annotation regex -- a term linked in the same sync_file()
    pass right inside a `**CJK**（English）` span could never be detected and
    repaired afterward. Argument links (citations, e.g.
    `[[Argument_X|Author, 2011, p. 12]]`) stay protected even then: a citation
    locator trailing a bold heading is a reference, not a translation, and must
    not be pulled inside the bold span the way vault_lint.py's fix_body_spans
    also excludes bare `(p. N)` locators.
    """
    protected: list[tuple[int, int]] = []

    def add(start: int, end: int) -> None:
        if start < end:
            protected.append((start, end))

    # Fenced code blocks.
    for m in re.finditer(r"(?ms)^```.*?^```\s*", text):
        add(m.start(), m.end())
    # Fenced code blocks inside blockquotes/callouts, e.g. `> ```mermaid`.
    # These render as code in Obsidian and must not be linked line-by-line.
    for m in re.finditer(r"(?ms)^>\s*```.*?^>\s*```\s*", text):
        add(m.start(), m.end())
    # Inline code.
    for m in re.finditer(r"`[^`\n]*`", text):
        add(m.start(), m.end())

    # Citation-like spans are reserved for the APA matching functions below. This prevents
    # ordinary Person linking from breaking author-year citations before the
    # citation linker can target the corresponding Argument page.
    for rx in (CITATION_NARRATIVE_RE, CITATION_PAREN_GROUP_RE, CITATION_FULLWIDTH_PAREN_GROUP_RE):
        for m in rx.finditer(text):
            add(m.start(), m.end())

    # Headings line-by-line. Also skip all lines in quote callouts.
    in_quote_callout = False
    pos = 0
    for line in text.splitlines(keepends=True):
        start, end = pos, pos + len(line)
        stripped = line.lstrip()
        if is_markdown_table_line(line):
            for cell_start, cell_end in unsafe_table_cell_spans(line):
                add(start + cell_start, start + cell_end)
        if re.match(r"^#{1,6}\s", stripped):
            add(start, end)
        # Protect the callout marker itself, e.g. `[!abstract]`, while leaving
        # the title/content on the line linkable. This supports nested quote
        # prefixes like `> > [!abstract]`. Otherwise aliases such as "abstract"
        # can corrupt the marker itself.
        marker = CALLOUT_MARKER_RE.match(stripped)
        if marker:
            marker_start = start + (len(line) - len(stripped)) + marker.start()
            marker_end = start + (len(line) - len(stripped)) + marker.end()
            add(marker_start, marker_end)
        # Quote callouts and generated MetaX modules ([!metax], [!metax-ma],
        # [!metax-errata]) are never linked; metax_sync.py writes their links.
        if re.match(r"^>\s*\[!(?:quote|metax[\w-]*|eef[\w-]*)(?:\|[^\]]*)?\]", stripped, re.IGNORECASE):
            in_quote_callout = True
        if in_quote_callout and stripped.startswith(">"):
            add(start, end)
        elif in_quote_callout:
            in_quote_callout = False
        pos = end

    for rx in (EMBED_RE, MD_LINK_RE, URL_RE, HTML_TAG_RE):
        for m in rx.finditer(text):
            add(m.start(), m.end())
    for m in WIKILINK_RE.finditer(text):
        if protect_wikilinks or is_argument_target(m.group(1).strip()):
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


def normalize_bold_heading_style(text: str) -> tuple[str, int]:
    """Normalize bold heading punctuation without touching protected Markdown."""
    out: list[str] = []
    changes = 0

    for protected, chunk in split_protected_spans(text, protect_wikilinks=False):
        if protected:
            out.append(chunk)
            continue

        def merge_bold_annotation(m: re.Match[str]) -> str:
            # A trailing "(p. 12)" / "(pp. 12-15)" is a citation locator, not an
            # English translation of the bold term. vault_lint.py's fix_body_spans
            # excludes the same shape; mirror it here so the two scripts agree.
            if re.fullmatch(r"[（(]\s*pp?\.\s*[^）)]+[）)]", m.group(2), flags=re.IGNORECASE):
                return m.group(0)
            # A bare "(Name, YEAR)" / "（Name, YEAR, p. N）" citation locator is not an
            # English translation either. Mirrors vault_lint.py's BARE_CITATION_PARENS_RE.
            if re.fullmatch(
                r"[（(][A-Z][A-Za-z0-9 .&和-]+,\s*(?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?[）)]",
                m.group(2),
            ):
                return m.group(0)
            return f"**{m.group(1).strip()}{m.group(2)}**"

        chunk, annotation_count = BOLD_HEADING_ENGLISH_OUTSIDE_RE.subn(
            merge_bold_annotation,
            chunk,
        )

        def remove_colon(m: re.Match[str]) -> str:
            next_char = chunk[m.end() : m.end() + 1]
            return m.group(1) + (" " if next_char and next_char != "\n" else "")

        chunk, colon_count = BOLD_HEADING_COLON_RE.subn(remove_colon, chunk)
        changes += annotation_count + colon_count
        out.append(chunk)

    return "".join(out), changes


def current_file_title(path: Path, path_to_title: dict[str, str]) -> str:
    rel = rel_to_root(path)
    return path_to_title.get(rel, path.stem)


def clean_invalid_links_in_text(text: str, entries_by_title: dict[str, Entry]) -> tuple[str, int, int]:
    """Clean invalid wikilinks, but leave Markdown table rows untouched.

    Table rows are structurally fragile: removing a display text that contains a
    pipe, URL, HTML, or other Markdown can alter the rendered column layout. Table
    linking is handled separately at cell level by link_table_row().
    """
    removed = 0
    table_pipes_escaped = 0

    def clean_line(line: str) -> str:
        nonlocal removed, table_pipes_escaped
        if is_markdown_table_line(line):
            next_line, count = escape_table_wikilink_pipes_with_count(line)
            table_pipes_escaped += count
            return next_line

        def repl(m: re.Match[str]) -> str:
            nonlocal removed
            target = m.group(1).strip()
            display = m.group(2)

            # Argument links include citation links such as
            # [[Argument_Ball_2008a_JEP|(Ball, 2008a)]]. They are governed by
            # the citation index/lint pipeline, not by the ordinary alias
            # linker. Preserve them even when the display text is not a title
            # or alias; broken Argument targets are left for vault_lint.py.
            if is_argument_target(target, entries_by_title):
                return m.group(0)

            if target not in entries_by_title:
                removed += 1
                return display if display is not None else target

            if display is not None and is_standalone_cjk_alias(display, entries_by_title[target]):
                if not valid_boundary(line, m.start(), m.end(), display):
                    removed += 1
                    return display

            if display is not None:
                display_clean = display.strip()
                entry = entries_by_title[target]
                valid_displays = {entry.title, *entry.aliases}
                if display_clean not in valid_displays and not is_case_variant_display(display_clean, valid_displays):
                    removed += 1
                    return display
            return m.group(0)

        return WIKILINK_RE.sub(repl, line)

    return "".join(clean_line(line) for line in text.splitlines(keepends=True)), removed, table_pipes_escaped


def clean_invalid_links(body: str, entries_by_title: dict[str, Entry]) -> tuple[str, int, int]:
    cleaned_sections: list[str] = []
    removed = 0
    table_pipes_escaped = 0

    for heading, section in split_h2_sections(body):
        if is_source_section_heading(heading):
            cleaned_sections.append(section)
            continue
        cleaned, count, table_count = clean_invalid_links_in_text(section, entries_by_title)
        cleaned_sections.append(cleaned)
        removed += count
        table_pipes_escaped += table_count

    return "".join(cleaned_sections), removed, table_pipes_escaped


def is_ascii_word_char(ch: str) -> bool:
    return ch.isascii() and (ch.isalnum() or ch == "_")


def is_cjk(ch: str) -> bool:
    return "\u4e00" <= ch <= "\u9fff"


def contains_cjk(text: str) -> bool:
    return any(is_cjk(ch) for ch in text)


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


def match_term_at(text: str, start: int, term: str) -> bool:
    candidate = text[start : start + len(term)]
    if len(candidate) != len(term):
        return False
    if candidate == term:
        return True

    # Long Latin terms should not need duplicate aliases only for casing.
    # Keep short all-caps acronyms exact, so aliases like US do not match "us".
    if any(ch.isascii() and ch.isalpha() for ch in term):
        if len(term) <= 3 and term.isupper():
            return False
        return candidate.casefold() == term.casefold()

    return False


def term_is_case_insensitive(text: str) -> bool:
    """Mirror TermMatcher: terms with ASCII letters match case-insensitively,
    except short all-caps acronyms (<= 3 chars) and terms without ASCII letters."""
    has_ascii_alpha = any(ch.isascii() and ch.isalpha() for ch in text)
    return has_ascii_alpha and not (len(text) <= 3 and text.isupper())


def is_case_variant_display(display: str, valid_displays: set[str]) -> bool:
    folded = display.casefold()
    return any(term_is_case_insensitive(v) and v.casefold() == folded for v in valid_displays)


def link_text(display: str, target: str, table_safe: bool = False) -> str:
    if display == target:
        return f"[[{target}]]"
    if table_safe:
        return f"[[{target}\\|{display}]]"
    return f"[[{target}|{display}]]"


def normalize_author_scalar(value: str) -> str:
    value = value.strip().strip("'\"").strip()
    value = re.sub(r"\s+", " ", value)
    # APA initials are sometimes written with a final period (S. J.) and
    # sometimes without (S. J). Treat those as the same for exact author-field
    # matching, but preserve the original display text when writing the link.
    value = value.rstrip(".").strip()
    return value.casefold()


def make_yaml_author_term_map(entries: list[Entry]) -> dict[str, str]:
    """Return normalized author/editor names to Person targets.

    This is intentionally Person-only. It lets frontmatter fields such as
    `authors:` and `editors:` link APA aliases like `Ball, S. J` to the
    Person page `Stephen Ball`, without allowing ordinary concept aliases or
    citation strings to be linked inside YAML.
    """
    mapping: dict[str, str] = {}
    for entry in entries:
        if entry.type != "person":
            continue
        for raw in (entry.title, *entry.aliases):
            key = normalize_author_scalar(raw)
            if key:
                mapping.setdefault(key, entry.title)
    return mapping


def split_inline_yaml_list(value: str) -> list[str] | None:
    stripped = value.strip()
    if not (stripped.startswith("[") and stripped.endswith("]")):
        return None
    inner = stripped[1:-1].strip()
    if not inner:
        return []
    # YAML flow lists that contain APA names should quote values because the
    # comma is part of the scalar. This lightweight splitter supports quoted
    # values and simple unquoted values; ambiguous malformed lists are left as-is.
    items: list[str] = []
    current: list[str] = []
    quote = ""
    escape = False
    for ch in inner:
        if escape:
            current.append(ch)
            escape = False
            continue
        if ch == "\\" and quote:
            current.append(ch)
            escape = True
            continue
        if ch in {"'", '"'}:
            if not quote:
                quote = ch
            elif quote == ch:
                quote = ""
            current.append(ch)
            continue
        if ch == "," and not quote:
            items.append("".join(current).strip())
            current = []
            continue
        current.append(ch)
    if quote:
        return None
    tail = "".join(current).strip()
    if tail:
        items.append(tail)
    return items


def yaml_quote(value: str) -> str:
    return '"' + value.replace('"', '\\"') + '"'


def strip_yaml_scalar(value: str) -> str:
    return value.strip().strip("'\"").strip()


def link_yaml_author_value(value: str, author_map: dict[str, str]) -> tuple[str, bool]:
    raw = value.strip()
    if not raw or raw in {"[]", "null", "~"}:
        return value, False
    if "[[" in raw and "]]" in raw:
        return value, False
    # Keep inline comments or complex YAML untouched; this field should be a
    # clean scalar in generated templates.
    if " #" in raw or raw.startswith("{"):
        return value, False
    display = strip_yaml_scalar(raw)
    target = author_map.get(normalize_author_scalar(display))
    if not target:
        return value, False
    linked = link_text(display, target)
    return yaml_quote(linked), True


def link_yaml_author_fields(fm: str, author_map: dict[str, str]) -> tuple[str, int]:
    """Link Person names in YAML `authors` / `editors` fields only.

    The ordinary body linker deliberately skips frontmatter. This function adds
    a narrow frontmatter pass so Argument author metadata can be normalized from
    APA aliases to Person wikilinks, for example:

      - "Ball, S. J"  ->  - "[[Stephen Ball|Ball, S. J]]"

    It does not touch citation fields, title, aliases, or arbitrary YAML values.
    """
    if not fm or not author_map:
        return fm, 0

    lines = fm.splitlines(keepends=True)
    out: list[str] = []
    additions = 0
    in_key: str | None = None
    list_indent = ""

    i = 0
    while i < len(lines):
        line = lines[i]
        line_no_nl = line.rstrip("\r\n")
        newline = line[len(line_no_nl):]

        key_match = re.match(r"^(\s*)([A-Za-z_][A-Za-z0-9_-]*):(.*)$", line_no_nl)
        if key_match and key_match.group(2) in YAML_AUTHOR_LINK_KEYS:
            indent, key, rest = key_match.groups()
            value = rest.strip()
            in_key = key
            list_indent = indent
            if not value:
                out.append(line)
                i += 1
                continue

            inline_items = split_inline_yaml_list(value)
            if inline_items is not None:
                if not inline_items:
                    out.append(line)
                else:
                    out.append(f"{indent}{key}:" + newline)
                    for item in inline_items:
                        linked, changed = link_yaml_author_value(item, author_map)
                        out.append(f"{indent}  - {linked}" + newline)
                        additions += int(changed)
                in_key = None
                i += 1
                continue

            linked, changed = link_yaml_author_value(value, author_map)
            out.append(f"{indent}{key}: {linked}" + newline)
            additions += int(changed)
            in_key = None
            i += 1
            continue

        if in_key and line_no_nl.startswith(list_indent + " "):
            item_match = re.match(r"^(\s*-\s+)(.*)$", line_no_nl)
            if item_match:
                prefix, value = item_match.groups()
                linked, changed = link_yaml_author_value(value, author_map)
                out.append(prefix + linked + newline)
                additions += int(changed)
                i += 1
                continue
            out.append(line)
            i += 1
            continue

        in_key = None
        out.append(line)
        i += 1

    return "".join(out), additions


def link_plain_text(
    chunk: str,
    terms: list[Term],
    current_title: str,
    already_linked: set[str],
    table_safe: bool = False,
    term_matcher: TermMatcher | None = None,
    person_prefix_registry: PersonPrefixRegistry | None = None,
) -> tuple[str, int]:
    term_matcher = term_matcher or TermMatcher(terms)
    additions = 0
    i = 0
    n = len(chunk)
    new_chunk: list[str] = []
    exact1, exact2 = term_matcher.exact1, term_matcher.exact2
    folded1, folded2 = term_matcher.folded1, term_matcher.folded2
    while i < n:
        # Skip, in one slice, every position where no term can start; this is
        # equivalent to the per-character "no candidates" branch below.
        j = i
        while j < n:
            c = chunk[j]
            if c in exact1 or chunk[j:j + 2] in exact2:
                break
            cf = c.casefold()
            if cf in folded1 or (j + 1 < n and (cf + chunk[j + 1].casefold()) in folded2):
                break
            j += 1
        if j > i:
            new_chunk.append(chunk[i:j])
            i = j
            if i >= n:
                break
        candidates = term_matcher.matches_at(chunk, i)

        # Reserve the longest known person span before applying the
        # once-per-section rule. Otherwise an already-linked longer person can
        # be skipped and a shorter cross-person prefix can capture the start of
        # the same name, e.g. Peterson, A. inside Peterson, A. D. C.
        if person_prefix_registry:
            protected_person: Term | None = None
            for term in candidates:
                if term not in person_prefix_registry.longer_terms:
                    continue
                protected_person = term
                break

            if protected_person is not None:
                end = i + len(protected_person.text)
                if (
                    protected_person.target != current_title
                    and protected_person.target not in already_linked
                    and valid_boundary(chunk, i, end, protected_person.text)
                ):
                    new_chunk.append(link_text(protected_person.text, protected_person.target, table_safe=table_safe))
                    already_linked.add(protected_person.target)
                    additions += 1
                else:
                    new_chunk.append(chunk[i:end])
                i = end
                continue

        preferred_cjk_length = max(
            (
                len(term.text)
                for term in candidates
                if term.target != current_title
                and contains_cjk(term.text)
                and valid_boundary(chunk, i, i + len(term.text), term.text)
            ),
            default=0,
        )
        matched: Term | None = None
        for term in candidates:
            if term.target == current_title or term.target in already_linked:
                continue
            if contains_cjk(term.text) and preferred_cjk_length > len(term.text):
                continue
            if not valid_boundary(chunk, i, i + len(term.text), term.text):
                continue
            matched = term
            break

        if matched is None:
            new_chunk.append(chunk[i])
            i += 1
            continue

        # Keep the source spelling: case-insensitive terms must not rewrite
        # "growth" as "Growth". The trie consumes one source char per term char.
        display = chunk[i:i + len(matched.text)]
        new_chunk.append(link_text(display, matched.target, table_safe=table_safe))
        already_linked.add(matched.target)
        additions += 1
        i += len(matched.text)

    return "".join(new_chunk), additions


def link_table_row(
    line: str,
    terms: list[Term],
    current_title: str,
    already_linked: set[str],
    term_matcher: TermMatcher | None = None,
    person_prefix_registry: PersonPrefixRegistry | None = None,
) -> tuple[str, int]:
    if is_markdown_table_separator_line(line):
        return line, 0

    line = escape_table_wikilink_pipes(line)
    original_pipe_count = count_unescaped_pipes(line)
    positions = unescaped_pipe_positions(line)
    if len(positions) < 2:
        return line, 0

    newline = "\n" if line.endswith("\n") else ""
    core = line[:-1] if newline else line
    out: list[str] = []
    additions = 0
    cursor = 0

    for idx, pipe_pos in enumerate(positions):
        # Copy the text before the first pipe and every pipe itself exactly.
        if idx == 0:
            out.append(core[cursor : pipe_pos + 1])
        else:
            cell = core[cursor:pipe_pos]
            if is_safe_table_cell(cell):
                linked_cell, added = link_plain_text(
                    cell,
                    terms,
                    current_title,
                    already_linked,
                    table_safe=True,
                    term_matcher=term_matcher,
                    person_prefix_registry=person_prefix_registry,
                )
                out.append(linked_cell)
                additions += added
            else:
                out.append(cell)
            out.append("|")
        cursor = pipe_pos + 1

    # Preserve trailing text after the final pipe exactly. In normal pipe-bounded
    # tables this is usually empty or whitespace.
    out.append(core[cursor:])
    new_line = "".join(out) + newline

    # Last-resort structural guard: if the table pipe count changed, discard the
    # edited line instead of risking a broken table.
    if count_unescaped_pipes(new_line) != original_pipe_count:
        return line, 0
    return new_line, additions


def link_unprotected_chunk(
    chunk: str,
    terms: list[Term],
    current_title: str,
    already_linked: set[str],
    term_matcher: TermMatcher | None = None,
    person_prefix_registry: PersonPrefixRegistry | None = None,
) -> tuple[str, int]:
    out: list[str] = []
    additions = 0
    for line in chunk.splitlines(keepends=True):
        if is_markdown_table_line(line):
            linked_line, added = link_table_row(
                line,
                terms,
                current_title,
                already_linked,
                term_matcher,
                person_prefix_registry,
            )
        else:
            linked_line, added = link_plain_text(
                line,
                terms,
                current_title,
                already_linked,
                term_matcher=term_matcher,
                person_prefix_registry=person_prefix_registry,
            )
        out.append(linked_line)
        additions += added
    return "".join(out), additions


def link_section(
    section: str,
    terms: list[Term],
    current_title: str,
    already_linked: set[str],
    person_prefix_registry: PersonPrefixRegistry | None = None,
    term_matcher: TermMatcher | None = None,
) -> tuple[str, int]:
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
        linked_chunk, added = link_unprotected_chunk(
            chunk,
            terms,
            current_title,
            already_linked,
            term_matcher,
            person_prefix_registry,
        )
        out.append(linked_chunk)
        additions += added

    return "".join(out), additions


def link_source_section(
    section: str,
    source_pattern: re.Pattern[str] | None,
    source_links: dict[str, str],
) -> tuple[str, int]:
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
        return source_links[source_id]

    for protected, chunk in chunks:
        if protected:
            out.append(chunk)
        else:
            out.append(source_pattern.sub(repl, chunk))

    return "".join(out), additions


def link_body(
    body: str,
    terms: list[Term],
    source_pattern: re.Pattern[str] | None,
    source_links: dict[str, str],
    current_title: str,
    person_prefix_registry: PersonPrefixRegistry | None = None,
    term_matcher: TermMatcher | None = None,
) -> tuple[str, int]:
    sections = split_h2_sections(body)
    linked_sections: list[str] = []
    additions = 0

    for heading, section in sections:
        if is_source_section_heading(heading):
            linked, added = link_source_section(section, source_pattern, source_links)
            linked_sections.append(linked)
            additions += added
            continue

        # Track links as we encounter them left-to-right so the first mention in
        # a ## section gets linked even when a later mention was already linked.
        already_linked: set[str] = set()
        linked, added = link_section(
            section,
            terms,
            current_title,
            already_linked,
            person_prefix_registry,
            term_matcher,
        )
        linked_sections.append(linked)
        additions += added

    return "".join(linked_sections), additions


def sync_file(
    path: Path,
    terms: list[Term],
    term_matcher: TermMatcher,
    source_pattern: re.Pattern[str] | None,
    source_links: dict[str, str],
    entries_by_title: dict[str, Entry],
    path_to_title: dict[str, str],
    author_map: dict[str, str],
    person_prefix_registry: PersonPrefixRegistry,
    dry_run: bool,
    tables_only: bool = False,
    citation_lookup: dict[str, dict[str, Any]] | None = None,
    citation_targets: dict[str, list[str]] | None = None,
    citation_stats: dict[str, int] | None = None,
    missing_citations: list[str] | None = None,
    exclusions: list[dict[str, str]] | None = None,
) -> tuple[bool, int, int, int, int]:
    original = path.read_text(encoding="utf-8", errors="ignore")
    working = original
    if citation_lookup is not None:
        if citation_stats is None:
            citation_stats = {"linked_parenthetical": 0, "linked_narrative": 0, "fixed_display": 0}
        if missing_citations is None:
            missing_citations = []
        working = link_citations(working, citation_lookup, citation_stats, missing_citations, path)
        if citation_targets is not None:
            working = citation_fix_display_suffixes(working, citation_targets, citation_stats)
    fm, body = split_frontmatter(working)
    current_title = current_file_title(path, path_to_title)

    if tables_only:
        linked_fm = fm
        linked_body, table_pipes_escaped = normalize_table_wikilink_pipes_in_text(body)
        heading_styles_normalized = 0
        added = 0
        removed = 0
    else:
        linked_fm, yaml_added = link_yaml_author_fields(fm, author_map)
        original_link_count = len(WIKILINK_RE.findall(body)) if exclusions else 0
        body, excluded_spans = mask_link_exceptions(body, exclusions or [],
                                                   entries_by_title.values(), valid_boundary)
        excluded_removed = original_link_count - len(WIKILINK_RE.findall(body)) if exclusions else 0
        cleaned_body, removed, cleaned_table_pipes = clean_invalid_links(body, entries_by_title)
        removed += excluded_removed
        linked_body, body_added = link_body(
            cleaned_body,
            terms,
            source_pattern,
            source_links,
            current_title,
            person_prefix_registry,
            term_matcher,
        )
        added = yaml_added + body_added
        # Final guard: regardless of which chunks were protected or linked,
        # never write table rows with raw wikilink alias pipes.
        linked_body, final_table_pipes = normalize_table_wikilink_pipes_in_text(linked_body)
        table_pipes_escaped = cleaned_table_pipes + final_table_pipes
        linked_body, heading_styles_normalized = normalize_bold_heading_style(linked_body)
        linked_body = restore_link_exceptions(linked_body, excluded_spans)
        if excluded_spans:
            linked_body, _ = normalize_table_wikilink_pipes_in_text(linked_body)
    updated = linked_fm + linked_body

    changed = updated != original
    if changed and not dry_run:
        path.write_text(updated, encoding="utf-8")
    return changed, added, removed, table_pipes_escaped, heading_styles_normalized


# APA citation matching shares this module's file selection and write pass.
CITATION_FULL_JSON = ROOT / "citation" / "citation_full.json"


APA_WIKILINK_RE = re.compile(r"\[\[[^\]]+\]\]")


APA_INLINE_CODE_RE = re.compile(r"`[^`]*`")


APA_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)


APA_OBSIDIAN_COMMENT_RE = re.compile(r"%%.*?%%", re.S)


APA_CODE_FENCE_RE = re.compile(r"```.*?```", re.S)


APA_AUTHOR_PATTERN = r"[A-Z\u3400-\u9fff][A-Za-zÀ-ÖØ-öø-ÿ\u3400-\u9fff0-9'’ .&和等-]*(?:\s+(?:&|and|和)\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ0-9'’ .-]+|\s+et\s+al\.)?"


APA_LOCATOR_PATTERN = r"(?:\s*[,，]\s*(?:(?:p|pp|ch|chap)\.?\s*|chapter\s+)[^,，;）)]+|\s*:\s*[^,，;）)]+)"


APA_PAREN_GROUP_RE = re.compile(r"(?<!\[)\(([^()\n]*\b\d{4}[a-z]?[^()\n]*)\)")


APA_FULLWIDTH_PAREN_GROUP_RE = re.compile(r"（([^（）\n]*\b\d{4}[a-z]?[^（）\n]*)）")


APA_PAREN_ITEM_RE = re.compile(
    r"^\s*"
    rf"(?P<author>{APA_AUTHOR_PATTERN})"
    r"\s*(?P<sep>[,，])\s*"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{APA_LOCATOR_PATTERN})?"
    r"\s*$"
)


APA_PAREN_ITEM_PREFIX_RE = re.compile(
    r"^\s*"
    rf"(?P<author>{APA_AUTHOR_PATTERN})"
    r"\s*(?P<sep>[,，])\s*"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{APA_LOCATOR_PATTERN})?"
    r"(?P<tail>\s*[,，].+)"
    r"\s*$"
)


APA_WIKILINK_PAREN_ITEM_RE = re.compile(
    r"^\s*"
    r"(?P<link>\[\[[^\]\n]+\]\])"
    r"\s*(?P<sep>[,，])\s*"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{APA_LOCATOR_PATTERN})?"
    r"(?P<tail>\s*[,，].+)?"
    r"\s*$"
)


APA_NARRATIVE_RE = re.compile(
    r"(?<![\w\]\)])"
    rf"(?P<author>{APA_AUTHOR_PATTERN})"
    r"\s*[（(]"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{APA_LOCATOR_PATTERN})?"
    r"[）)]"
)


APA_WIKILINK_NARRATIVE_RE = re.compile(
    r"(?<![\w\]\)])"
    r"(?P<link>\[\[[^\]\n]+\]\])"
    r"\s*[（(]"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{APA_LOCATOR_PATTERN})?"
    r"[）)]"
)


APA_TAIL_CITATION_RE = re.compile(
    r"(?P<label>(?:[,，]\s*(?:(?:引自|引|cited in)\s*)?|(?:引自|引|cited in)\s*))"
    rf"(?P<author>{APA_AUTHOR_PATTERN})"
    r"\s*(?P<sep>[,，])\s*"
    r"(?P<year>\d{4}[a-z]?)"
    rf"(?P<locator>{APA_LOCATOR_PATTERN})?",
    re.IGNORECASE,
)


def load_citation_lookup() -> dict[str, dict[str, Any]]:
    data = json.loads(CITATION_FULL_JSON.read_text(encoding="utf-8"))
    items = data.get("items", data) if isinstance(data, dict) else {}
    lookup: dict[str, dict[str, Any]] = {}

    def add_key(alias: str, entry: dict[str, Any]) -> None:
        lookup[alias] = entry
        lookup[citation_normalize_citation_alias(alias)] = entry

    if isinstance(items, dict):
        for alias, entry in items.items():
            if isinstance(entry, dict):
                add_key(str(alias), entry)
                for extra in entry.get("aliases") or []:
                    add_key(str(extra), entry)
    return lookup


def citation_normalize_citation_alias(alias: str) -> str:
    alias = re.sub(r"\s+", " ", alias).strip()
    return re.sub(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])(?:\s+and\s+|\s*&\s*|\s*和\s*)(?=[A-ZÀ-ÖØ-Þ])", " & ", alias)


def citation_normalize_author(author: str) -> str:
    return citation_normalize_citation_alias(author)


def citation_normalize_display_author(author: str, narrative: bool = False) -> str:
    author = re.sub(r"\s+", " ", author).strip()
    conjunction = " and " if narrative else " & "
    return re.sub(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])(?:\s+and\s+|\s*&\s*|\s*和\s*)(?=[A-ZÀ-ÖØ-Þ])", conjunction, author)


def citation_normalize_locator(locator: str) -> str:
    locator = locator.replace("，", ",")
    return re.sub(r"^\s*,\s*", ", ", locator)


def citation_display_parenthetical_author_year(author: str, sep: str, year: str) -> str:
    if sep == "，":
        return f"{author}，{year}"
    return f"{author}, {year}"


def citation_wikilink_display(raw: str) -> str:
    inner = raw.strip()[2:-2].strip()
    if "\\|" in inner:
        return inner.split("\\|", 1)[1].strip()
    if "|" in inner:
        return inner.split("|", 1)[1].strip()
    return inner.split("#", 1)[0].strip()


# Generated MetaX modules: citation links are owned by scripts/metax_sync.py,
# which matches by title rather than author-year.
METAX_BLOCK_RE = re.compile(r"^>[ \t]*\[!(?:metax|eef)[\w-]*(?:\|[^\]]*)?\][^\n]*(?:\n>[^\n]*)*", re.M)


def citation_mask_protected(text: str) -> tuple[str, list[str]]:
    protected: list[str] = []

    def repl(m: re.Match[str]) -> str:
        # Resolve earlier placeholders first: inline code may contain a
        # wikilink that was already masked, and unmask() is single-pass.
        protected.append(citation_unmask(m.group(0), protected))
        return f"\uE000{len(protected) - 1}\uE001"

    for rx in [METAX_BLOCK_RE, APA_CODE_FENCE_RE, APA_HTML_COMMENT_RE, APA_OBSIDIAN_COMMENT_RE, APA_WIKILINK_RE, APA_INLINE_CODE_RE]:
        text = rx.sub(repl, text)
    return text, protected


def citation_unmask(text: str, protected: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        return protected[int(m.group(1))]
    return re.sub(r"\uE000(\d+)\uE001", repl, text)


def citation_link_target(entry: dict[str, Any], display: str) -> str:
    return f"[[{entry['argument']}|{display}]]"


def citation_link_tail_citations(tail: str, lookup: dict[str, dict[str, Any]], missing: list[str]) -> tuple[str, bool]:
    changed = False

    def repl(m: re.Match[str]) -> str:
        nonlocal changed
        display_author = citation_normalize_display_author(m.group("author"))
        author = citation_normalize_author(display_author)
        year = m.group("year").strip()
        locator = citation_normalize_locator(m.group("locator") or "")
        key = f"{author}, {year}"
        entry = lookup.get(key)
        if not entry:
            missing.append(key)
            return m.group(0)
        changed = True
        display = f"{citation_display_parenthetical_author_year(display_author, m.group('sep'), year)}{locator}"
        return f"{m.group('label')}{citation_link_target(entry, display)}"

    return APA_TAIL_CITATION_RE.sub(repl, tail), changed


def citation_link_parenthetical_group(content: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str], opener: str = "(", closer: str = ")") -> str | None:
    parts = content.split(";")
    linked_parts: list[str] = []
    changed = False
    for raw in parts:
        item = raw.strip()
        m = APA_PAREN_ITEM_RE.match(item)
        prefix_only = False
        wikilink_author = False
        if not m:
            m = APA_PAREN_ITEM_PREFIX_RE.match(item)
            prefix_only = bool(m)
        if not m:
            m = APA_WIKILINK_PAREN_ITEM_RE.match(item)
            wikilink_author = bool(m)
            prefix_only = bool(m and m.group("tail"))
        if not m:
            linked_parts.append(item)
            continue
        display_author = citation_wikilink_display(m.group("link")) if wikilink_author else citation_normalize_display_author(m.group("author"))
        author = citation_normalize_author(display_author)
        year = m.group("year").strip()
        locator = citation_normalize_locator(m.group("locator") or "")
        key = f"{author}, {year}"
        entry = lookup.get(key)
        tail = m.group("tail") if "tail" in m.groupdict() else None
        if not entry:
            missing.append(key)
            if tail:
                linked_tail, tail_changed = citation_link_tail_citations(tail, lookup, missing)
                if tail_changed:
                    display_prefix = f"{citation_display_parenthetical_author_year(display_author, m.group('sep'), year)}{locator}"
                    linked_parts.append(f"{display_prefix}{linked_tail}")
                    changed = True
                else:
                    linked_parts.append(item)
            else:
                linked_parts.append(item)
            continue
        display_prefix = f"{citation_display_parenthetical_author_year(display_author, m.group('sep'), year)}{locator}"
        if prefix_only:
            linked_tail, _ = citation_link_tail_citations(tail or "", lookup, missing)
            linked_parts.append(f"{citation_link_target(entry, display_prefix)}{linked_tail}")
        else:
            linked_parts.append(citation_link_target(entry, display_prefix))
        changed = True
    if not changed:
        return None
    stats["linked_parenthetical"] += 1
    return opener + "; ".join(linked_parts) + closer


def citation_link_parenthetical(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        opener = m.group(0)[0]
        closer = "）" if opener == "（" else ")"
        linked = citation_link_parenthetical_group(m.group(1), lookup, stats, missing, opener, closer)
        return linked or m.group(0)

    text = APA_PAREN_GROUP_RE.sub(repl, text)
    text = APA_FULLWIDTH_PAREN_GROUP_RE.sub(repl, text)
    return text


def citation_link_wikilink_parenthetical(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        if "[[" not in m.group(1):
            return m.group(0)
        opener = m.group(0)[0]
        closer = "）" if opener == "（" else ")"
        linked = citation_link_parenthetical_group(m.group(1), lookup, stats, missing, opener, closer)
        return linked or m.group(0)

    text = APA_PAREN_GROUP_RE.sub(repl, text)
    text = APA_FULLWIDTH_PAREN_GROUP_RE.sub(repl, text)
    return text


def citation_is_cjk(ch: str) -> bool:
    return "\u3400" <= ch <= "\u9fff"


def citation_author_start_candidates(raw: str) -> list[int]:
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
        elif citation_is_cjk(ch) and not prev.isspace():
            starts.append(i)
        elif ch.isupper() and citation_is_cjk(prev):
            starts.append(i)
    # A suffix right after a conjunction is a co-author, not the first author:
    # "Yamamoto and Li (2012)" must never be linked as "Li (2012)".
    return [i for i in starts if i == 0 or not APA_CONJUNCTION_TAIL_RE.search(raw[:i])]


APA_CONJUNCTION_TAIL_RE = re.compile(r"[^\s&、,，]\s*(?:\band|&|与|和|及|、|[,，])\s*(?:[A-Z][\w'’.-]*\s+)*$")


def citation_link_narrative(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        raw_author = m.group("author")
        year = m.group("year").strip()
        locator = citation_normalize_locator(m.group("locator") or "")
        first_key = None
        for start in citation_author_start_candidates(raw_author):
            candidate = raw_author[start:]
            if not (candidate[:1].isupper() or citation_is_cjk(candidate[:1])):
                continue
            display_author = citation_normalize_display_author(candidate, narrative=True)
            key = f"{citation_normalize_author(display_author)} ({year})"
            first_key = first_key or key
            entry = lookup.get(key)
            if entry:
                stats["linked_narrative"] += 1
                return raw_author[:start] + citation_link_target(entry, f"{display_author} ({year}{locator})")
        missing.append(first_key or f"{raw_author} ({year})")
        return m.group(0)
    return APA_NARRATIVE_RE.sub(repl, text)


def citation_link_wikilink_narrative(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str]) -> str:
    def repl(m: re.Match[str]) -> str:
        display_author = citation_normalize_display_author(citation_wikilink_display(m.group("link")), narrative=True)
        author = citation_normalize_author(display_author)
        year = m.group("year").strip()
        locator = citation_normalize_locator(m.group("locator") or "")
        key = f"{author} ({year})"
        entry = lookup.get(key)
        if not entry:
            missing.append(key)
            return m.group(0)
        stats["linked_narrative"] += 1
        return citation_link_target(entry, f"{display_author} ({year}{locator})")
    return APA_WIKILINK_NARRATIVE_RE.sub(repl, text)


APA_YEAR_TOKEN_RE = re.compile(r"((?:19|20)\d{2})([a-z])?")


APA_DISPLAY_WIKILINK_RE = re.compile(r"\[\[([^\]\n|]+)\|([^\]\n]+)\]\]")


def citation_build_target_aliases(lookup: dict[str, dict[str, Any]]) -> dict[str, list[str]]:
    targets: dict[str, list[str]] = {}
    for alias, entry in lookup.items():
        arg = entry.get("argument")
        if not arg:
            continue
        targets.setdefault(arg, [])
        if alias not in targets[arg]:
            targets[arg].append(alias)
    return targets


def citation_rewrite_drifted_display(display: str, aliases: list[str]) -> str | None:
    """Rewrite an Argument link display whose a/b/c suffix drifted from citation_aliases.

    'Cohen et al., 2011, p. 30' -> 'Cohen et al., 2011a, p. 30' when the target's
    alias is 'Cohen et al., 2011a'. Returns None when no safe rewrite exists.
    """
    m = APA_YEAR_TOKEN_RE.search(display)
    if not m:
        return None
    narrative = display[: m.start()].rstrip().endswith(("(", "（"))
    d_author = citation_normalize_author(display[: m.start()].strip(" ,，（(")).lower()
    if not d_author:
        return None
    tail = display[m.end():]
    for alias in aliases:
        am = APA_YEAR_TOKEN_RE.search(alias)
        if not am:
            continue
        if alias[: am.start()].rstrip().endswith(("(", "（")) != narrative:
            continue
        if citation_normalize_author(alias[: am.start()].strip(" ,，（(")).lower() != d_author:
            continue
        if am.group(1) != m.group(1):
            continue
        # Replace only the year token so any wrapping text/parens are preserved.
        candidate = display[: m.start()] + am.group(0) + tail
        return candidate if candidate != display else None
    return None


def citation_fix_display_suffixes(text: str, targets: dict[str, list[str]], stats: dict[str, int]) -> str:
    fm, body = split_frontmatter(text)

    def repl(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        display = match.group(2).strip()
        aliases = targets.get(target)
        if not aliases:
            return match.group(0)
        fixed = citation_rewrite_drifted_display(display, aliases)
        if fixed is None:
            return match.group(0)
        stats["fixed_display"] += 1
        return f"[[{target}|{fixed}]]"

    return fm + APA_DISPLAY_WIKILINK_RE.sub(repl, body)


APA_SOURCES_HEADING_RE = re.compile(r"^##\s+(?:来源|Sources?)\s*$", re.M)


APA_HEADING_LINE_RE = re.compile(r"^#{1,6}\s.*$", re.M)


APA_PART_OF_RE = re.compile(r"^part_of:\s*[\"']?\[\[([^\]|#]+)", re.M)


def citation_self_targets_for(path: Path | None, fm: str) -> set[str]:
    if path is None:
        return set()
    targets = {path.stem}
    m = APA_PART_OF_RE.search(fm)
    if m:
        targets.add(m.group(1).strip())
    return targets


def link_citations(text: str, lookup: dict[str, dict[str, Any]], stats: dict[str, int], missing: list[str], path: Path | None = None) -> str:
    fm, body = split_frontmatter(text)
    # Reference lists under "## 来源/Sources" are bibliography, not prose.
    m = APA_SOURCES_HEADING_RE.search(body)
    body, sources_tail = (body[:m.start()], body[m.start():]) if m else (body, "")
    selfs = citation_self_targets_for(path, fm)
    if selfs:
        lookup = {k: v for k, v in lookup.items() if v.get("argument") not in selfs}
    body = citation_link_wikilink_parenthetical(body, lookup, stats, missing)
    body = citation_link_wikilink_narrative(body, lookup, stats, missing)
    masked, protected = citation_mask_protected(body)
    # Headings stay plain: a link in a heading changes its anchor.
    def protect_heading(h: re.Match[str]) -> str:
        protected.append(citation_unmask(h.group(0), protected))
        return f"\uE000{len(protected) - 1}\uE001"

    masked = APA_HEADING_LINE_RE.sub(protect_heading, masked)
    masked = citation_link_parenthetical(masked, lookup, stats, missing)
    masked = citation_link_narrative(masked, lookup, stats, missing)
    return fm + citation_escape_table_pipes(citation_unmask(masked, protected)) + sources_tail


APA_TABLE_LINE_RE = re.compile(r"^\s*(?:>\s*)*\|")


APA_UNESCAPED_ARG_LINK_RE = re.compile(r"\[\[(Argument_[^\]|\\\n]+)\|")


def citation_escape_table_pipes(body: str) -> str:
    """Inside Markdown table rows, a wikilink alias pipe must be written as \\|."""
    if "|" not in body:
        return body
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if APA_TABLE_LINE_RE.match(line) and "[[Argument_" in line:
            lines[i] = APA_UNESCAPED_ARG_LINK_RE.sub(lambda m: f"[[{m.group(1)}\\|", line)
    return "\n".join(lines)


def select_link_files(paths: list[str], git_only: bool, full: bool, *, citations_only: bool = False) -> list[Path]:
    if git_only and paths:
        raise SystemExit("`sync --git` does not accept explicit paths; use either --git or paths.")
    if full and paths:
        raise SystemExit("`sync --full` does not accept explicit paths; use either --full or paths.")
    if git_only and full:
        raise SystemExit("Use only one of --git or --full.")
    if paths or full:
        files = iter_target_files(paths)
    elif citations_only:
        # Daily citation-only maintenance keeps its existing local-change scope.
        files = [ROOT / name for name in git_changed_paths()]
    else:
        files = iter_git_target_files()
    return sorted({p for p in files if p.is_file() and p.suffix.lower() == ".md"
                   and WIKI_DIR.resolve() in p.resolve().parents and not should_skip_file(p)})


def require_citation_index() -> None:
    if not CITATION_FULL_JSON.exists():
        raise SystemExit("citation/citation_full.json missing; run scripts/vault_index.py first.")


def print_citation_stats(stats: dict[str, int], missing: list[str]) -> None:
    print(f"APA parenthetical groups linked: {stats['linked_parenthetical']}")
    print(f"APA narrative citations linked: {stats['linked_narrative']}")
    print(f"Citation displays fixed: {stats['fixed_display']}")
    if missing:
        print("Unresolved citation aliases:")
        for alias in sorted(set(missing))[:200]:
            print(f"  - {alias}")


def run_citation_sync(files: Iterable[Path], *, dry_run: bool = False, fix_display: bool = False) -> tuple[int, int]:
    """Citation-only maintenance for the base workflow and explicit CLI mode."""
    require_citation_index()
    lookup = load_citation_lookup()
    targets = citation_build_target_aliases(lookup) if fix_display else None
    stats = {"linked_parenthetical": 0, "linked_narrative": 0, "fixed_display": 0}
    missing: list[str] = []
    changed = 0
    for path in sorted({Path(path).resolve() for path in files}):
        if not path.is_file() or WIKI_DIR.resolve() not in path.resolve().parents or should_skip_file(path):
            continue
        original = path.read_text(encoding="utf-8")
        updated = link_citations(original, lookup, stats, missing, path)
        if targets is not None:
            updated = citation_fix_display_suffixes(updated, targets, stats)
        if updated != original:
            changed += 1
            print(f"{'Would update' if dry_run else 'Updated'}: {path.relative_to(ROOT)} (APA citations)")
            if not dry_run:
                path.write_text(updated, encoding="utf-8")
    print_citation_stats(stats, missing)
    return changed, stats['linked_parenthetical'] + stats['linked_narrative']


# Files are linked independently, so large runs (--full) use forked workers.
# Per-file results, stats and printed lines keep the serial order exactly.
PARALLEL_MIN_FILES = 200
_SYNC_SHARED: tuple = ()


def _sync_one(path: Path, shared: tuple, citation_stats: dict[str, int], missing: list[str]):
    (terms, term_matcher, source_pattern, source_links, entries_by_title, path_to_title,
     author_map, person_prefix_registry, dry_run, tables_only, citation_lookup,
     citation_targets, exclusions) = shared
    return sync_file(
        path, terms, term_matcher, source_pattern, source_links, entries_by_title,
        path_to_title, author_map, person_prefix_registry, dry_run,
        tables_only=tables_only, citation_lookup=citation_lookup,
        citation_targets=citation_targets, citation_stats=citation_stats,
        missing_citations=missing,
        exclusions=exclusions.get(path.relative_to(ROOT).as_posix(), []),
    )


def _sync_chunk(chunk: list[Path]):
    citation_stats = {"linked_parenthetical": 0, "linked_narrative": 0, "fixed_display": 0}
    missing: list[str] = []
    results = [(path, _sync_one(path, _SYNC_SHARED, citation_stats, missing)) for path in chunk]
    return results, citation_stats, missing


def sync_files(files: list[Path], shared: tuple, citation_stats: dict[str, int], missing: list[str]):
    global _SYNC_SHARED
    files = list(files)
    workers = min(os.cpu_count() or 1, 8)
    if len(files) >= PARALLEL_MIN_FILES and workers > 1 and not os.environ.get("VAULT_LINT_SERIAL"):
        import multiprocessing
        try:
            ctx = multiprocessing.get_context("fork")
        except ValueError:
            ctx = None
        if ctx is not None:
            _SYNC_SHARED = shared
            size = max(10, len(files) // (workers * 6))
            chunks = [files[i:i + size] for i in range(0, len(files), size)]
            try:
                with ctx.Pool(workers) as pool:
                    parts = pool.map(_sync_chunk, chunks)
            except Exception as exc:  # pragma: no cover - fall back to serial
                print(f"(parallel linking unavailable: {exc}; running serially)", file=sys.stderr)
            else:
                out = []
                for results, part_stats, part_missing in parts:
                    out.extend(results)
                    for key, value in part_stats.items():
                        citation_stats[key] = citation_stats.get(key, 0) + value
                    missing.extend(part_missing)
                return out
            finally:
                _SYNC_SHARED = ()
    return [(path, _sync_one(path, shared, citation_stats, missing)) for path in files]


def run_sync(paths: list[str], dry_run: bool, git_only: bool, full: bool, tables_only: bool,
             *, citations_only: bool = False, wiki_only: bool = False, fix_display: bool = False) -> None:
    files = select_link_files(paths, git_only, full, citations_only=citations_only)
    if citations_only:
        run_citation_sync(files, dry_run=dry_run, fix_display=fix_display)
        return
    citation_lookup = None
    citation_targets = None
    citation_stats = {"linked_parenthetical": 0, "linked_narrative": 0, "fixed_display": 0}
    missing_citations: list[str] = []
    if not wiki_only and not tables_only:
        require_citation_index()
        citation_lookup = load_citation_lookup()
        if fix_display:
            citation_targets = citation_build_target_aliases(citation_lookup)

    entries = load_entries()
    exclusions = {}
    if not tables_only:
        original_exclusions, exclusions = clean_link_exceptions(ROOT, LINK_EXCEPTIONS, dry_run)
        # A registry-only edit must also process its notes in incremental mode.
        previous = git_files_at_ref("HEAD", ["scripts/link_exceptions.json"]).get("scripts/link_exceptions.json")
        previous_data = json.loads(previous) if previous else {}
        affected = {name for name in set(original_exclusions) | set(previous_data)
                    if exclusions.get(name) != previous_data.get(name)}
        if not paths and not full:
            files = sorted(set(files) | {ROOT / name for name in affected
                           if valid_link_exception_path(name) and (ROOT / name).is_file()
                           and not should_skip_file(ROOT / name)})
    source_entries = load_source_entries()
    terms, entries_by_title, path_to_title = make_terms(entries)
    term_matcher = TermMatcher(terms)
    person_prefix_registry = build_person_prefix_registry(terms)
    author_map = make_yaml_author_term_map(entries)
    for source in source_entries:
        entries_by_title.setdefault(source.title, source)
    source_pattern = make_source_pattern({source.title for source in source_entries})
    source_links = make_source_links(source_entries)

    stats = LinkStats()
    shared = (terms, term_matcher, source_pattern, source_links, entries_by_title, path_to_title,
              author_map, person_prefix_registry, dry_run, tables_only, citation_lookup,
              citation_targets, exclusions)
    for path, result in sync_files(files, shared, citation_stats, missing_citations):
        changed, added, removed, table_pipes_escaped, heading_styles_normalized = result
        if changed:
            stats.files_changed += 1
            stats.links_added += added
            stats.links_removed += removed
            stats.table_pipes_escaped += table_pipes_escaped
            stats.heading_styles_normalized += heading_styles_normalized
            action = "Would update" if dry_run else "Updated"
            print(
                f"{action}: {path.relative_to(ROOT)} "
                f"(+{added}, -{removed}, table pipes {table_pipes_escaped}, "
                f"heading styles {heading_styles_normalized})"
            )

    if citation_lookup is not None:
        print_citation_stats(citation_stats, missing_citations)
    print("Done.")
    print(f"Files scanned: {len(files)}")
    print(f"Files changed: {stats.files_changed}")
    print(f"Links added: {stats.links_added}")
    print(f"Links removed: {stats.links_removed}")
    print(f"Table pipes escaped: {stats.table_pipes_escaped}")
    print(f"Heading styles normalized: {stats.heading_styles_normalized}")
    print(f"Person prefix conflicts registered: {len(person_prefix_registry.conflicts)}")
    for conflict in person_prefix_registry.conflicts:
        print(
            f"  {conflict.shorter.text} ({conflict.shorter.target}) -> "
            f"{conflict.longer.text} ({conflict.longer.target})"
        )


def register_exclusion(name: str, sentence: str, target: str, *, record_only: bool = False) -> None:
    with link_exception_lock(ROOT):
        _register_exclusion(name, sentence, target, record_only=record_only)


def _register_exclusion(name: str, sentence: str, target: str, *, record_only: bool = False) -> None:
    if not valid_link_exception_path(name) or not valid_link_exception_path(target):
        raise ValueError("请使用规范的 wiki/ 相对 Markdown 路径")
    entries = load_entries()
    by_path = {entry.path: entry for entry in entries}
    if name not in by_path or target not in by_path:
        raise ValueError("条目不在 wiki/index.json 中，请核对路径或刷新索引")
    if by_path[target].type not in {"concept", "theory", "method", "instrument", "person", "fact"}:
        raise ValueError("句子例外仅用于普通知识链接，不处理 Argument 引用")
    path = ROOT / name
    original = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(original)
    sentence = link_exception_text(sentence)
    matches = [unit for unit, _, _ in link_exception_sentences(body) if unit == sentence]
    if len(matches) != 1:
        raise ValueError("句子未找到或重复，不能唯一定位；请核对可见句子，重复句需先改写区分")
    record = {"sentence": sentence, "target": target}
    masked, replacements = mask_link_exceptions(body, [record], entries, valid_boundary)
    if not replacements:
        raise ValueError("句中未找到该目标的可处理链接或标题/别名")
    data = prune_link_exceptions(ROOT, load_link_exceptions(LINK_EXCEPTIONS))
    if record not in data.setdefault(name, []):
        data[name].append(record)
    save_link_exceptions(LINK_EXCEPTIONS, data)
    updated = fm + restore_link_exceptions(masked, replacements)
    if updated != original and not record_only:
        path.write_text(updated, encoding="utf-8")
    print("链接例外已登记。")


def run_link_exception_tests() -> int:
    """Regression tests; fixtures never touch the real vault."""
    import contextlib
    import io
    import json
    import tempfile
    import unittest
    from pathlib import Path
    from unittest.mock import patch

    import sys
    linker = sys.modules[__name__]


    class LinkExceptionsTest(unittest.TestCase):
        def setUp(self):
            self.temp = tempfile.TemporaryDirectory()
            self.addCleanup(self.temp.cleanup)
            self.root = Path(self.temp.name).resolve()
            self.note = 'wiki/arguments/Example.md'
            self.target = 'wiki/concepts/Research Hypothesis.md'
            self.other = 'wiki/concepts/Evidence.md'
            self.entries = [linker.Entry('Research Hypothesis', self.target, ('假设',), 'concept'),
                            linker.Entry('Evidence', self.other, ('证据',), 'concept'),
                            linker.Entry('Example', self.note, (), 'argument')]
            for entry in self.entries:
                path = self.root / entry.path
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('---\ntype: ' + entry.type + '\n---\n', encoding='utf-8')
            self.registry = self.root / 'scripts/link_exceptions.json'
            self.registry.parent.mkdir()
            self.patch = patch.multiple(linker, ROOT=self.root, WIKI_DIR=self.root / 'wiki',
                                        LINK_EXCEPTIONS=self.registry, INDEX_JSON=self.root / 'wiki/index.json')
            self.patch.start(); self.addCleanup(self.patch.stop)
            linker.INDEX_JSON.write_text(json.dumps([
                dict(title=e.title, path=e.path, aliases=e.aliases, type=e.type) for e in self.entries]))

        def record(self, sentence='这一假设需要证据。'):
            return {'sentence': sentence, 'target': self.target}

        def sync(self, body, records, dry_run=False):
            path = self.root / self.note
            path.write_text('---\ntype: argument\n---\n' + body)
            terms, by_title, path_to_title = linker.make_terms(self.entries)
            linker.sync_file(path, terms, linker.TermMatcher(terms), None, {}, by_title,
                             path_to_title, {}, linker.build_person_prefix_registry(terms),
                             dry_run, exclusions=records)
            return linker.split_frontmatter(path.read_text())[1]

        def test_only_one_sentence_target_and_first_valid_mention(self):
            body = '这一[[Research Hypothesis|假设]]需要证据。研究假设涉及证据。\n'
            result = self.sync(body, [self.record()])
            self.assertIn('这一假设需要[[Evidence|证据]]。', result)
            # Use a separate standalone occurrence for the original boundary rule.
            result = self.sync('这一假设需要证据。\n假设需要检验。\n', [self.record()])
            self.assertIn('这一假设需要[[Evidence|证据]]。', result)
            self.assertIn('[[Research Hypothesis|假设]]需要检验。', result)

        def test_removed_link_does_not_change_identity(self):
            plain = '这一假设需要证据。'
            linked = '这一[[Research Hypothesis|假设]]需要[[Evidence|证据]]。'
            self.assertEqual([s for s, _, _ in link_exception_sentences(plain)],
                             [s for s, _, _ in link_exception_sentences(linked)])
            result = self.sync(linked, [self.record()])
            self.assertEqual(result, self.sync(result, [self.record()]))

        def test_registration_removes_only_existing_mislink_and_deduplicates(self):
            path = self.root / self.note
            path.write_text('---\ntype: argument\n---\n这一[[Research Hypothesis|假设]]需要证据。\n')
            with contextlib.redirect_stdout(io.StringIO()):
                linker.register_exclusion(self.note, self.record()['sentence'], self.target)
                linker.register_exclusion(self.note, self.record()['sentence'], self.target)
            self.assertIn('这一假设需要证据。', path.read_text())
            self.assertEqual(load_link_exceptions(self.registry), {self.note: [self.record()]})

        def test_record_only_preserves_source_snapshot(self):
            path = self.root / self.note
            original = '---\ntype: argument\n---\n这一[[Research Hypothesis|假设]]需要证据。\n'
            path.write_text(original)
            with contextlib.redirect_stdout(io.StringIO()):
                linker.register_exclusion(self.note, self.record()['sentence'], self.target, record_only=True)
            self.assertEqual(path.read_text(), original)
            self.assertEqual(load_link_exceptions(self.registry), {self.note: [self.record()]})

        def test_short_exclusion_preserves_another_longer_term(self):
            entries = self.entries + [linker.Entry('Scientific Hypothesis', 'wiki/concepts/Scientific Hypothesis.md',
                                                 ('科学假设',), 'concept')]
            body = '科学假设需要证据。'
            masked, replacements = mask_link_exceptions(body, [self.record(body)], entries, linker.valid_boundary)
            self.assertEqual(masked, body)
            self.assertEqual(replacements, {})

        def test_prune_deleted_edited_missing_targets_and_dry_run(self):
            path = self.root / self.note
            path.write_text('---\ntype: argument\n---\n这一假设需要证据。\n')
            data = {self.note: [self.record(), self.record('已经删除的句子。')]}
            save_link_exceptions(self.registry, data)
            _, active = clean_link_exceptions(self.root, self.registry, dry_run=True)
            self.assertEqual(active, {self.note: [self.record()]})
            self.assertEqual(load_link_exceptions(self.registry), data)
            clean_link_exceptions(self.root, self.registry)
            path.write_text('---\ntype: argument\n---\n这一猜测需要证据。\n')
            self.assertEqual(prune_link_exceptions(self.root, load_link_exceptions(self.registry)), {})
            path.unlink()
            self.assertEqual(prune_link_exceptions(self.root, data), {})
            path.write_text('这一假设需要证据。')
            (self.root / self.target).unlink()
            self.assertEqual(prune_link_exceptions(self.root, data), {})

        def test_read_failure_never_rewrites_registry(self):
            data = {self.note: [self.record()]}
            save_link_exceptions(self.registry, data)
            original_read = Path.read_text
            def fail(path, *args, **kwargs):
                if path == self.root / self.note: raise PermissionError('unreadable')
                return original_read(path, *args, **kwargs)
            with patch.object(Path, 'read_text', fail), self.assertRaises(PermissionError):
                clean_link_exceptions(self.root, self.registry)
            self.assertEqual(load_link_exceptions(self.registry), data)

        def test_duplicate_sentence_and_bad_registration_rejected(self):
            path = self.root / self.note
            path.write_text('这一假设需要证据。\n这一假设需要证据。')
            with self.assertRaises(ValueError):
                linker.register_exclusion(self.note, self.record()['sentence'], self.target)
            with self.assertRaises(ValueError):
                mask_link_exceptions(path.read_text(), [self.record()], self.entries, linker.valid_boundary)
            with self.assertRaises(ValueError):
                linker.register_exclusion(self.note, self.record()['sentence'], self.note)

        def test_table_and_callout(self):
            for body in ('> 这一[[Research Hypothesis|假设]]需要证据。\n',
                         '| 这一[[Research Hypothesis\\|假设]]需要证据。 | 其他 |\n'):
                result = self.sync(body, [self.record()])
                self.assertNotIn('Research Hypothesis', result)
                self.assertIn('假设', result)
            body = '| 假设需要检验。 | 证据 |\n'
            result = self.sync(body, [self.record('假设需要检验。')])
            self.assertIn('| 假设需要检验。 |', result)
            self.assertIn('[[Evidence\\|证据]]', result)

        def test_code_protected_and_no_record_preserves_normal_behavior(self):
            body = '```text\n这一假设需要证据。\n```\n'
            masked, replacements = mask_link_exceptions(body, [self.record()], self.entries, linker.valid_boundary)
            self.assertEqual(masked, body)
            self.assertEqual(replacements, {})
            result = self.sync('假设需要检验。\n', [])
            self.assertIn('[[Research Hypothesis|假设]]', result)

        def test_incremental_registry_only_change_and_sync_dry_run(self):
            path = self.root / self.note
            original = '---\ntype: argument\n---\n这一[[Research Hypothesis|假设]]需要证据。\n'
            path.write_text(original)
            save_link_exceptions(self.registry, {self.note: [self.record()]})
            with patch.object(linker, 'select_link_files', return_value=[]), \
                 patch.object(linker, 'git_files_at_ref', return_value={}), \
                 patch.object(linker, 'load_source_entries', return_value=[]), \
                 contextlib.redirect_stdout(io.StringIO()):
                linker.run_sync([], True, False, False, False, wiki_only=True)
                self.assertEqual(path.read_text(), original)
                linker.run_sync([], False, False, False, False, wiki_only=True)
            self.assertNotIn('Research Hypothesis', path.read_text())

        def test_invalid_registry_fails_instead_of_resetting(self):
            self.registry.write_text('{"wiki/a.md":[],"wiki/a.md":[]}')
            with self.assertRaises(ValueError): load_link_exceptions(self.registry)
            self.registry.write_text('{"../outside.md":[]}')
            with self.assertRaises(ValueError): load_link_exceptions(self.registry)

        def test_removing_registry_record_rechecks_unchanged_note(self):
            path = self.root / self.note
            path.write_text('---\ntype: argument\n---\n这一假设需要证据。\n')
            save_link_exceptions(self.registry, {})
            previous = {'scripts/link_exceptions.json': json.dumps({self.note: [self.record()]})}
            with patch.object(linker, 'select_link_files', return_value=[]), \
                 patch.object(linker, 'git_files_at_ref', return_value=previous), \
                 patch.object(linker, 'load_source_entries', return_value=[]), \
                 contextlib.redirect_stdout(io.StringIO()):
                linker.run_sync([], False, False, False, False, wiki_only=True)
            self.assertIn('[[Research Hypothesis|假设]]', path.read_text())

        def test_lint_checks_registry_outside_incremental_scope(self):
            import vault_lint
            path = self.root / self.note
            path.write_text('---\ntype: argument\n---\n这一假设需要证据。\n')
            save_link_exceptions(self.registry, {self.note: [self.record()]})
            with patch.multiple(vault_lint, ROOT=self.root, WIKI_DIR=self.root / 'wiki'):
                issues = []
                vault_lint.check_link_exceptions(issues)
                self.assertEqual(issues, [])
                save_link_exceptions(self.registry, {self.note: [self.record('已删除的句子。')]})
                vault_lint.check_link_exceptions(issues)
                self.assertEqual(issues[0].code, 'LINK_EXCEPTION_INVALID')



    suite = unittest.defaultTestLoader.loadTestsFromTestCase(LinkExceptionsTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Synchronize APA citations and ordinary Obsidian wikilinks in one pass; link authors/editors to Person pages."
    )
    sub = parser.add_subparsers(dest="command")

    sync = sub.add_parser("sync", help="Clean invalid links and add missing wikilinks.")
    modes = sync.add_mutually_exclusive_group()
    modes.add_argument("--citations-only", action="store_true", help="Only link APA citations; no ordinary wikilinks or YAML author changes.")
    modes.add_argument("--wiki-only", action="store_true", help="Only synchronize ordinary wikilinks and YAML authors/editors.")
    sync.add_argument("--fix-display", action="store_true", help="Fix citation display year suffixes using the current citation index.")
    sync.add_argument("paths", nargs="*", help="Optional file or directory paths relative to vault root.")
    sync.add_argument("--dry-run", action="store_true", help="Show changes without writing files.")
    sync.add_argument("--git", action="store_true", help="Only process files affected by git changes. This is also the default when no path is supplied.")
    sync.add_argument("--full", action="store_true", help="Process the whole wiki. Use after bulk alias/title/path changes or before major releases.")
    sync.add_argument("--tables-only", action="store_true", help="Only normalize wikilink alias pipes inside Markdown tables; do not add or remove links.")

    exclude = sub.add_parser("exclude", help="Record one reviewed sentence/target and remove only its existing mislink.")
    exclude.add_argument("path", help="Vault-relative note path.")
    exclude.add_argument("--sentence", required=True, help="Exact visible sentence (without wikilink markup).")
    exclude.add_argument("--target", required=True, help="Canonical vault-relative target path from wiki/index.json.")
    exclude.add_argument("--record-only", action="store_true", help="Only register; defer existing-link removal to ordinary sync (preserves source snapshots).")
    sub.add_parser("self-test", help="Run sentence-exclusion regression tests in a temporary vault.")
    sub.add_parser("exceptions-clean", help="Remove expired sentence/target exclusions without linking notes.")

    return parser


def main() -> None:
    if not WIKI_DIR.exists():
        raise SystemExit(f"wiki directory not found: {WIKI_DIR}")
    parser = build_parser()
    args = parser.parse_args()
    if getattr(args, "tables_only", False) and (getattr(args, "citations_only", False) or getattr(args, "fix_display", False)):
        parser.error("--tables-only cannot be combined with citation options")
    if getattr(args, "wiki_only", False) and getattr(args, "fix_display", False):
        parser.error("--wiki-only cannot be combined with --fix-display")
    if args.command == "self-test":
        raise SystemExit(run_link_exception_tests())
    elif args.command == "exclude":
        register_exclusion(args.path, args.sentence, args.target, record_only=args.record_only)
    elif args.command == "exceptions-clean":
        original, active = clean_link_exceptions(ROOT, LINK_EXCEPTIONS)
        count = sum(map(len, original.values())) - sum(map(len, active.values()))
        if count:
            print(f"Expired link exceptions removed: {count}")
    elif args.command in {None, "sync"}:
        run_sync(
            getattr(args, "paths", []),
            getattr(args, "dry_run", False),
            getattr(args, "git", False),
            getattr(args, "full", False),
            getattr(args, "tables_only", False),
            citations_only=getattr(args, "citations_only", False),
            wiki_only=getattr(args, "wiki_only", False),
            fix_display=getattr(args, "fix_display", False),
        )
    else:
        parser.error(f"unknown command: {args.command}")


if __name__ == "__main__":
    main()
