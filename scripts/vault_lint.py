#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vault_lint.py

Lint an Obsidian / Quartz academic wiki vault.

Default behavior:
- Read-only checks.
- Does not modify files.
- By default, lint only Markdown files changed in git status, including untracked files.
- Use --full for a full-vault lint.
- Exits with non-zero status when errors are found.
- Unreviewed writing findings also fail; other warnings fail only with --strict.

Expected location:
  /Users/shaoyangwu/Documents/MyNotes/scripts/vault_lint.py

Usage:
  cd /Users/shaoyangwu/Documents/MyNotes
  python3 scripts/vault_lint.py                 # default incremental git lint
  python3 scripts/vault_lint.py --strict
  python3 scripts/vault_lint.py --json
  python3 scripts/vault_lint.py --path wiki/concepts
  python3 scripts/vault_lint.py --full          # full-vault lint
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import subprocess
import unicodedata
from dataclasses import dataclass, asdict
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vaultlib  # noqa: E402
from vaultlib import (  # noqa: E402
    ASSET_BASE_URL,
    asset_url_for_path,
    author_label,
    chinese_author_part,
    dedupe,
    has_cjk,
    normalized_source_language,
    rel,
)


def find_vault_root() -> Path:
    """Find the vault root so the script can prefer the vault-local .venv."""
    script_path = Path(__file__).resolve()

    # Expected layout: <vault>/scripts/vault_lint.py
    if script_path.parent.name == "scripts":
        return script_path.parent.parent

    # Fallback: current working directory or one of its parents.
    cwd = Path.cwd().resolve()
    for candidate in [cwd, *cwd.parents]:
        if (candidate / ".venv").exists() or (candidate / "wiki").exists():
            return candidate

    return cwd


def maybe_reexec_with_vault_venv() -> None:
    """If <vault>/.venv exists, rerun this script with that Python automatically."""
    vaultlib.ensure_venv()


# Only when run as a script: importing this module (e.g. from vault_index.py)
# must never re-exec the importing process.
if __name__ == "__main__":
    maybe_reexec_with_vault_venv()

try:
    import yaml  # type: ignore
except Exception:
    yaml = None


if yaml is not None:
    class DuplicateFrontmatterKey(yaml.constructor.ConstructorError):
        """An explicit mapping key was declared twice in the same mapping."""


    # libyaml-backed loader is 5-10x faster; fall back to pure Python if absent.
    FAST_SAFE_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

    class UniqueKeySafeLoader(FAST_SAFE_LOADER):  # type: ignore[misc, valid-type]
        def flatten_mapping(self, node):
            # Check the original pairs before SafeLoader expands merge keys.
            # Inherited defaults may be overridden by an explicit local key.
            checked = getattr(self, "_checked_mapping_nodes", set())
            self._checked_mapping_nodes = checked
            if id(node) not in checked:
                checked.add(id(node))
                seen = {}
                for key_node, _ in node.value:
                    key = "<<" if key_node.tag == "tag:yaml.org,2002:merge" else self.construct_object(key_node)
                    try:
                        if key in seen:
                            raise DuplicateFrontmatterKey(
                                f"first declaration of key {key!r}", seen[key],
                                f"duplicate mapping key {key!r}", key_node.start_mark,
                            )
                        seen[key] = key_node.start_mark
                    except TypeError:
                        # Let SafeLoader report invalid, unhashable mapping keys.
                        pass
            return super().flatten_mapping(node)


# -----------------------------
# Configuration
# -----------------------------

ROOT = find_vault_root()
WIKI_DIR = ROOT / "wiki"
TEMPLATES_DIR = WIKI_DIR / "templates"
INDEX_JSON = WIKI_DIR / "index.json"
CITATION_DIR = ROOT / "citation"
CITATION_FULL_JSON = CITATION_DIR / "citation_full.json"
CITATION_AMBIGUOUS_JSON = CITATION_DIR / "citation_ambiguous.json"
CITATION_EXTERNAL_JSON = CITATION_DIR / "citation_external.json"
EXTERNAL_CITATION_IDENTITY = "EXTERNAL_CITATION_IDENTITY"


GENERATED_INDEX_FILES = {
    "index.md",
    "index.json",
}

GENERATED_CONTENT_PATHS = {
    "wiki/research-map.md",
}

SKIP_DIR_NAMES = {
    ".git",
    ".obsidian",
    ".trash",
    "node_modules",
    "__pycache__",
    ".quartz-cache",
}

SOURCE_RECORD_DIRS = {
    "sources",
}

RELATED_FIELDS = [
    "related_concepts",
    "related_theories",
    "related_methods",
    "related_instruments",
    "related_persons",
    "related_facts",
    "related_arguments",
]

AUTO_RELATION_FIELDS = RELATED_FIELDS + ["sources"]

PROTECTED_FIELDS = [
    "title",
    "aliases",
    "summary",
    "type",
    "subtype",
    "tags",
    "citation",
    "citation_aliases",
    "year",
    "doi",
    "isbn",
    "journal",
    "book_title",
    "authors",
    "editors",
    "publisher",
    "publication_place",
    "source_language",
    "part_of",
    "instrument_type",
    "developers",
    "original_year",
    "languages",
    "item_count",
    "administration_mode",
    "response_format",
    "license",
    "confidence",
    "status",
    "born",
    "died",
    "lifespan",
    "nationality",
    "region",
    "method_type",
    "issuing_organization",
    "created",
    "updated",
]

VALID_TYPES = {
    "concept",
    "theory",
    "method",
    "instrument",
    "person",
    "fact",
    "argument",
    "source",
}

ARGUMENT_REQUIRED_NEW_ENTRY_TYPES = {"concept", "theory", "method", "instrument", "person", "fact"}

TYPE_PATH_HINTS = {
    "concept": "wiki/concepts/",
    "theory": "wiki/theories/",
    "method": "wiki/methods/",
    "instrument": "wiki/instruments/",
    "person": "wiki/persons/",
    "fact": "wiki/facts/",
    "argument": "wiki/arguments/",
}

PERSONS_DIR = WIKI_DIR / "persons"

PERSON_YEAR_PATTERN = re.compile(
    r"^(?:c\.\s*)?\d{1,4}(?:\s*BCE)?(?:\s*/\s*(?:(?:c\.\s*)?\d{1,4}(?:\s*BCE)?|\s*))*$"
)
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
ALLOWED_STATUS = {"draft", "in-progress", "stable", "archived", "active", "published", "completed"}
RELATED_RESEARCH_ENTRY_MAX_CHARS = 150
MERGEABLE_BOOK_SUBTYPES = ("monograph", "textbook")
EDITED_VOLUME_BOOK_SUBTYPES = ("edited-volume", "edited-volume-overview")

TYPE_TO_RELATED_FIELD = {
    "concept": "related_concepts",
    "theory": "related_theories",
    "method": "related_methods",
    "instrument": "related_instruments",
    "person": "related_persons",
    "fact": "related_facts",
    "argument": "related_arguments",
}

FORBIDDEN_SUMMARY_CHARS = [":", '"', "'", "_"]

TAG_RE = re.compile(r"^[a-z0-9]+(?:[-/][a-z0-9]+)*$")

WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
EMBED_RE = re.compile(r"!\[\[([^\]\n]+)\]\]")
EPUB_VIEWER_RE = re.compile(r'data-epub="([^"]+\.epub)"')

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
TEMPLATER_PLACEHOLDER_RE = re.compile(r"<%.*?%>")

# `[!axis]` is a nested card inside `[!debates]`.  A blank `> >` line before
# the next card keeps that card inside the previous child callout, so Quartz
# renders the marker as ordinary text.  The separator must step back to the
# outer quote level with a single `>` line.
AXIS_CALLOUT_LINE_RE = re.compile(
    r"^(?P<indent>[ \t]*)(?P<quotes>(?:>[ \t]*)*)\[!axis\][+-]?(?:[ \t]|$)",
    re.MULTILINE | re.IGNORECASE,
)
AXIS_BAD_SIBLING_SEPARATOR_RE = re.compile(
    r"^(?P<indent>[ \t]*)>[ \t]+>[ \t]*(?P<newline>\r?\n)"
    r"(?=(?P=indent)>[ \t]+>[ \t]+\[!axis\][+-]?(?:[ \t]|$))",
    re.MULTILINE | re.IGNORECASE,
)

# Schema-constrained APA short citations used for links to Argument pages.
CITATION_PARENT_RE = re.compile(r"^\([A-Z][A-Za-z0-9 .&和-]+,\s*(?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?\)$")
CITATION_NARRATIVE_RE = re.compile(r"^[A-Z][A-Za-z0-9 .&和-]+\s*[（(](?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?[）)]$")
RAW_CITATION_RE = re.compile(r"(?<![\w\[])(\([A-Z][A-Za-z0-9 .&和-]+,\s*(?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?\)|（[A-Z][A-Za-z0-9 .&和-]+,\s*(?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?）|[A-Z][A-Za-z0-9 .&和-]+\s*[（(](?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?[）)])")
# A bare "(Name, YEAR)" / "（Name, YEAR, p. N）" citation locator immediately after a
# bold CJK term is not an English translation of that term — it's a citation, and
# should stay outside the bold (same principle as the Argument-wikilink exclusion below).
BARE_CITATION_PARENS_RE = re.compile(r"[（(][A-Z][A-Za-z0-9 .&和-]+,\s*(?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?[）)]")
PAGE_ONLY_REF_RE = re.compile(
    r"([（(]\s*pp?\.\s*\d+(?:\s*[–-]\s*\d+)?"
    r"(?:\s*[,，]\s*\d+(?:\s*[–-]\s*\d+)?)*\s*[）)])",
    re.IGNORECASE,
)
ENGLISH_AUTHOR_AND_RE = re.compile(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])(?:\s+and\s+|\s*和\s*)(?=[A-ZÀ-ÖØ-Þ])")
APA_INVERTED_PERSON_RE = re.compile(
    r"^[A-Za-zÀ-ÖØ-öø-ÿĀ-ſ'’.-]+(?:[ -][A-Za-zÀ-ÖØ-öø-ÿĀ-ſ'’.-]+)*,\s*"
    r"(?:[A-ZÀ-ÖØ-ÞĀ-ſ]\.(?:-[A-ZÀ-ÖØ-ÞĀ-ſ]\.)?\s*)+$"
)
ORGANIZATION_CREATOR_RE = re.compile(
    r"\b(?:academy|agency|assessment|association|board|center|centre|college|commission|company|"
    r"corporation|council|department|foundation|group|institute|laboratory|ministry|office|"
    r"organization|service|society|team|university)\b",
    re.IGNORECASE,
)

EMBED_FILE_EXISTS_CACHE: Dict[str, bool] = {}


def alias_is_single_english_family(alias: str, family_name: str = "") -> bool:
    alias = alias.strip()
    if not alias or " " in alias or "·" in alias:
        return False
    if not re.match(r"^[A-Z][A-Za-z'-]+$", alias):
        return False
    if family_name and alias.lower() != family_name.strip().lower():
        return False
    return True


def is_citation_eligible_argument(data: Optional[Dict[str, Any]]) -> bool:
    if not data or data.get("type") != "argument":
        return False
    if data.get("subtype") == "edited-volume-overview":
        return False
    if data.get("publication_type") == "book-chapter" and data.get("subtype") in {"textbook", "monograph"}:
        part_of = str(data.get("part_of") or "").strip()
        if part_of.startswith("[[Argument_") and part_of.endswith("]]"):
            return False
    authors = data.get("authors")
    has_authors = bool(authors) if isinstance(authors, list) else bool(str(authors or "").strip())
    return bool(has_authors and str(data.get("year") or "").strip())


def is_argument_entry(data: Optional[Dict[str, Any]]) -> bool:
    return bool(data and data.get("type") == "argument")


def is_non_argument_semantic_entry(data: Optional[Dict[str, Any]]) -> bool:
    return bool(data and data.get("type") in {"concept", "theory", "method", "instrument", "person", "fact"})


def wikilink_target_and_display(value: str) -> Optional[Tuple[str, str]]:
    m = re.fullmatch(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", value.strip())
    if not m:
        return None
    target = m.group(1).strip()
    display = (m.group(2) or m.group(1)).strip()
    return target, display


def check_argument_creator_apa_display(path: Path, fm: str, field: str, item: str, issues: List[Issue]) -> None:
    display = creator_display(item)
    if (
        has_cjk(display)
        or APA_INVERTED_PERSON_RE.fullmatch(display)
        or looks_like_organization_creator(display)
    ):
        return
    issues.append(Issue(
        "ERROR",
        rel(path),
        f"{field} personal names must use APA inverted form such as 'Lakhani, R. T.'; "
        f"Person wikilinks must use the same form as their display text: {item!r}",
        line=frontmatter_line_number(fm, field),
        code=f"{field.upper()}_APA_DISPLAY",
    ))


def looks_like_organization_creator(value: str) -> bool:
    value = re.sub(r"\s+", " ", value).strip()
    if not value:
        return False
    if ORGANIZATION_CREATOR_RE.search(value):
        return True
    if re.fullmatch(r"[A-Z][A-Z0-9&.-]*", value):
        return True
    if re.fullmatch(r"[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÖØ-öø-ÿ'’.-]+", value):
        return True
    return False


def check_instrument_developers(path: Path, fm: str, value: Any, issues: List[Issue]) -> None:
    line = frontmatter_line_number(fm, "developers")
    if not isinstance(value, list):
        issues.append(Issue(
            "ERROR",
            rel(path),
            "developers must be a YAML list",
            line=line,
            code="DEVELOPERS_TYPE",
        ))
        return

    for item in value:
        if not isinstance(item, str) or not item.strip():
            issues.append(Issue(
                "ERROR",
                rel(path),
                f"developers items must be non-empty strings: {item!r}",
                line=line,
                code="DEVELOPERS_ITEM",
            ))
            continue

        display = creator_display(item)
        if has_cjk(display) or APA_INVERTED_PERSON_RE.fullmatch(display) or looks_like_organization_creator(display):
            continue

        issues.append(Issue(
            "ERROR",
            rel(path),
            f"personal developer names must use APA inverted form such as 'Marsh, H. W.'; "
            f"corporate authors keep their formal organization name: {item!r}",
            line=line,
            code="DEVELOPERS_APA_FORMAT",
        ))


def source_language_from_meta(data: Dict[str, Any]) -> str:
    explicit = normalized_source_language(data.get("source_language"))
    if explicit:
        return explicit
    citation = str(data.get("citation") or "").strip()
    year = str(data.get("year") or "").strip()
    return "zh" if chinese_author_part(citation, year) else "en"


def creator_display(value: str) -> str:
    parsed = wikilink_target_and_display(value)
    return parsed[1] if parsed else re.sub(r"\s+", " ", value).strip()


def expected_citation_aliases_from_meta(data: Dict[str, Any], suffix: str = "") -> List[str]:
    raw_authors = data.get("authors") or []
    authors = raw_authors if isinstance(raw_authors, list) else [raw_authors]
    labels = [author_label(str(a)) for a in authors if author_label(str(a))]
    year = f"{str(data.get('year') or '').strip()}{suffix}"
    if not labels or not year:
        return []
    chinese_part = chinese_author_part(str(data.get("citation") or ""), str(data.get("year") or "").strip())
    if source_language_from_meta(data) == "zh" or chinese_part:
        parts = [chinese_part] if chinese_part else []
    else:
        if len(labels) == 1:
            parts = [labels[0]]
        elif len(labels) == 2:
            parts = [f"{labels[0]} & {labels[1]}"]
        else:
            parts = [f"{labels[0]} et al."]
    import citation_index  # noqa: PLC0415 - one alias rule for lint and index
    return citation_index.aliases_for_parts(dedupe(parts), year)


def apa7_disambiguated_aliases(aliases: List[Any], expected_base: List[str]) -> bool:
    """APA 7 (8.18, 8.20) forms that citation_index writes when two works share
    a base short cite: more co-authors ("Kim, Lee, et al., 2020") or initials
    ("J. Zhang et al., 2022"). Same first surname and year as the base form."""
    m = re.match(r"^(.+?)[,\s].*?((?:19|20)\d{2})", expected_base[0])
    if not m:
        return False
    surname, year = m.group(1), m.group(2)
    pattern = re.compile(rf"^(?:[A-Z][\w.\- ]*\s)?{re.escape(surname)}\b.*{year}[a-z]?\)?$")
    return all(pattern.match(str(a)) for a in aliases)


def citation_display_text(text: str) -> bool:
    text = text.strip()
    return bool(
        re.match(r"^\(?[A-Z\u3400-\u9fff][A-Za-zÀ-ÖØ-öø-ÿ\u3400-\u9fff0-9'’ .&和等-]+[,，]\s*(?:19|20)\d{2}[a-z]?(?:[,，]\s*pp?\.\s*[^)）]+)?\)?$", text)
        or re.match(r"^[A-Z\u3400-\u9fff][A-Za-zÀ-ÖØ-öø-ÿ\u3400-\u9fff0-9'’ .&和等-]+\s*[（(](?:19|20)\d{2}[a-z]?(?:[,，]\s*pp?\.\s*[^)）]+)?[）)]$", text)
    )


# -----------------------------
# Data model
# -----------------------------

@dataclass
class Issue:
    severity: str  # ERROR / WARN / INFO
    path: str
    message: str
    line: Optional[int] = None
    code: str = ""

    def format(self) -> str:
        loc = self.path
        if self.line is not None:
            loc += f":{self.line}"
        code = f" [{self.code}]" if self.code else ""
        return f"{self.severity:<5} {loc}{code} - {self.message}"


# -----------------------------
# Utilities
# -----------------------------


def iter_md_files(base: Path) -> Iterable[Path]:
    if not base.exists():
        return
    if base.is_file() and base.suffix.lower() == ".md":
        yield base
        return

    for p in base.rglob("*.md"):
        if any(part in SKIP_DIR_NAMES for part in p.parts):
            continue
        yield p


# Text overrides let lint_file() check a file's HEAD version (see
# baseline_warning_keys) without touching the working tree.
_TEXT_OVERRIDES: Dict[Path, str] = {}


@lru_cache(maxsize=None)
def _read_text_disk(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_text(path: Path) -> str:
    override = _TEXT_OVERRIDES.get(path)
    if override is not None:
        return override
    return _read_text_disk(path)


read_text.cache_clear = _read_text_disk.cache_clear  # type: ignore[attr-defined]


def git_files_at_head(rel_paths: List[str]) -> Dict[str, str]:
    """Read baseline versions through one `git cat-file --batch` call."""
    return vaultlib.git_files_at_ref(comparison_ref(), rel_paths)


_REVIEW_ID_RE = re.compile(r"待审查 \[[0-9a-f]{16}\]")


def writing_baseline_key(issue: "Issue") -> Tuple[str, str, str, str]:
    """CI (--base) only: identify a writing hit by its visible context, not by
    its review ID. The ID hashes the raw line, so link-only edits (relinking,
    alias cleanup) change it although the sentence itself is unchanged."""
    # Link rendering adds spaces around link text and the context is cut at
    # 160 chars, so compare whitespace-free text over a stable prefix.
    head, _, context = _REVIEW_ID_RE.sub("待审查", issue.message).partition(" 语境：")
    # Mechanical auto-fixes (等 -> et al., and the citation links they enable)
    # must not turn an old hit into a new one.
    context = re.sub(r"et al\.|等人|等", "", unicodedata.normalize("NFKC", context))
    return ("WRITING", issue.path, issue.code, head + "|" + re.sub(r"\s+", "", context)[:100])


def baseline_warning_keys(files: List[Path], by_title, path_to_title, argument_citations) -> "Counter[Tuple[str, str, str]]":
    """WARN/INFO findings each file already had at the baseline, keyed by
    (path, code, message) - line numbers ignored so shifted text still matches."""
    from collections import Counter as _Counter
    keys: "Counter[Tuple[str, str, str]]" = _Counter()
    rels = {p: unicodedata.normalize("NFC", rel(p)) for p in files}
    head = git_files_at_head(sorted(set(rels.values())))
    jobs = [(p, head[rels[p]]) for p in files if rels[p] in head]
    base_mode = bool(os.environ.get("VAULT_LINT_BASE"))
    for issue in lint_files(jobs, by_title, path_to_title, argument_citations, baseline=True):
        if issue.severity in ("WARN", "INFO") and issue.code not in WRITING_REMINDER_CODES:
            keys[(issue.path, issue.code, issue.message)] += 1
        elif base_mode and issue.code in WRITING_REMINDER_CODES:
            keys[writing_baseline_key(issue)] += 1
    entry_metadata.cache_clear()
    return keys


def run_git(args: List[str]) -> str:
    return vaultlib.git_output(args)


@lru_cache(maxsize=1)
def git_head_paths() -> frozenset[str]:
    """Load tracked baseline paths once instead of spawning git per file."""
    output = run_git(["-c", "core.quotePath=false", "ls-tree", "-r", "--name-only", comparison_ref()])
    return frozenset(line for line in output.splitlines() if line)


@lru_cache(maxsize=1)
def git_nfd_index_paths() -> frozenset[str]:
    out = run_git(["-c", "core.quotePath=false", "ls-files", "-z"])
    return frozenset(p for p in out.split("\0") if p and unicodedata.normalize("NFC", p) != p)


def git_tracks_nfd_path(path: Path) -> bool:
    return rel(path) in git_nfd_index_paths()


def comparison_ref() -> str:
    """Use the same baseline for changed paths, old warnings and new entries."""
    return os.environ.get("VAULT_LINT_BASE") or "HEAD"


def git_path_exists_at_head(path: Path) -> bool:
    return rel(path) in git_head_paths()


# Shared local / CI file selection. CI supplies the pre-push or PR baseline.
GIT_STATUS_PATHSPECS = ["wiki", "books", "sources", "schema", "vault-schema.md", "vault-use.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md"]


@lru_cache(maxsize=1)
def _git_changed_md_files_cached() -> Tuple[Path, ...]:
    return tuple(_git_changed_md_files_uncached())


def git_changed_md_files() -> List[Path]:
    """Return local changes or the committed CI range, including renamed paths."""
    return list(_git_changed_md_files_cached())


def _git_changed_md_files_uncached() -> List[Path]:
    base = os.environ.get("VAULT_LINT_BASE")
    if base and set(base) == {"0"}:
        rel_paths = [p for p in vaultlib.git_output(["ls-files", "-z", "--", *GIT_STATUS_PATHSPECS]).split("\0") if p]
    elif base:
        rel_paths = vaultlib.git_diff_paths(base, "HEAD", GIT_STATUS_PATHSPECS)
    else:
        # git status also refreshes the index stat cache (fast after the first run).
        rel_paths = vaultlib.git_status_paths(GIT_STATUS_PATHSPECS)
    files: Set[Path] = set()
    for raw in rel_paths:
        path = ROOT / raw
        if path.suffix.lower() == ".md" and path.is_file():
            files.add(path)
    return sorted(files)


def embedded_file_exists_by_name(target_name: str) -> bool:
    """Cache expensive vault-wide filename lookups used for embedded PDFs/images."""
    key = unicodedata.normalize("NFC", target_name)
    if key in EMBED_FILE_EXISTS_CACHE:
        return EMBED_FILE_EXISTS_CACHE[key]
    found = key in vault_file_names()
    EMBED_FILE_EXISTS_CACHE[key] = found
    return found


@lru_cache(maxsize=1)
def vault_file_names() -> frozenset[str]:
    """All file and folder names in the vault, collected in one walk.

    Skip-listed folders are pruned instead of walked and filtered afterwards."""
    names: Set[str] = set()
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_NAMES]
        names.update(unicodedata.normalize("NFC", d) for d in dirnames)
        names.update(unicodedata.normalize("NFC", f) for f in filenames)
    return frozenset(names)


def split_frontmatter(text: str) -> Tuple[Optional[str], str, int]:
    """
    Return (frontmatter_raw, body, body_start_line).
    body_start_line is 1-indexed line number where body starts.
    """
    split = vaultlib.split_frontmatter(text)
    return split.raw, split.body, split.body_line


def yaml_quote_is_escaped(value: str, idx: int, quote: str) -> bool:
    if quote == '"':
        backslashes = 0
        j = idx - 1
        while j >= 0 and value[j] == "\\":
            backslashes += 1
            j -= 1
        return backslashes % 2 == 1
    if quote == "'":
        return (idx + 1 < len(value) and value[idx + 1] == "'") or (idx > 0 and value[idx - 1] == "'")
    return False


def suggest_yaml_quote_fix(key: str, value: str, quote: str) -> str:
    inner = value[1:-1] if len(value) >= 2 and value.endswith(quote) else value[1:]
    other = "'" if quote == '"' else '"'
    if other not in inner:
        return f"Suggested fix: {key}: {other}{inner}{other}"
    if quote == '"':
        return f"Suggested fix: escape inner double quotes as \\\" or wrap the value in single quotes if it has no apostrophes."
    return "Suggested fix: double inner single quotes as '' or wrap the value in double quotes if it has no double quotes."


def check_frontmatter_raw_yaml_style(path: Path, fm: str, issues: List[Issue]) -> None:
    """Catch common Quartz-breaking YAML mistakes with actionable messages."""
    lines = fm.splitlines()
    prev_allows_indent = False
    for idx, line in enumerate(lines, start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        indent = len(line) - len(line.lstrip(" "))
        if indent > 0 and not stripped.startswith("- ") and not prev_allows_indent:
            issues.append(Issue(
                "ERROR",
                rel(path),
                "indented frontmatter line is not a list item or block-scalar continuation. Remove the stray line or attach it to the previous field with proper YAML quoting.",
                line=idx,
                code="FM_BAD_INDENT",
            ))

        m = re.match(r"^\s*([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.+?)\s*$", line)
        if m:
            key = m.group(1)
            value = m.group(2).strip()
            if value and value[0] in {"'", '"'}:
                quote = value[0]
                if len(value) >= 2 and value.endswith(quote):
                    for qidx, ch in enumerate(value[1:-1], start=1):
                        if ch == quote and not yaml_quote_is_escaped(value, qidx, quote):
                            issues.append(Issue(
                                "ERROR",
                                rel(path),
                                f"{key} uses {quote}...{quote} but contains an unescaped inner {quote}. {suggest_yaml_quote_fix(key, value, quote)}",
                                line=idx,
                                code="FM_NESTED_QUOTE",
                            ))
                            break
                elif value.count(quote) > 1:
                    issues.append(Issue(
                        "ERROR",
                        rel(path),
                        f"{key} starts with {quote} but is not safely closed. {suggest_yaml_quote_fix(key, value, quote)}",
                        line=idx,
                        code="FM_QUOTE_UNCLOSED",
                    ))

        prev_allows_indent = bool(re.match(r"^\s*[^:#][^:]*:\s*[|>]", line))


def parse_yaml_fm(fm: str, path: Path, issues: List[Issue]) -> Dict[str, Any]:
    if yaml is None:
        issues.append(Issue("ERROR", rel(path), "PyYAML is not installed. Install with: pip install pyyaml", code="YAML_LIB"))
        return {}
    try:
        data = yaml.load(fm, Loader=UniqueKeySafeLoader) or {}
        if not isinstance(data, dict):
            issues.append(Issue("ERROR", rel(path), "frontmatter is not a YAML mapping", code="FM_TYPE"))
            return {}
        return data
    except DuplicateFrontmatterKey as e:
        issues.append(Issue(
            "ERROR", rel(path),
            f"frontmatter YAML {e.problem}; first declared on line {e.context_mark.line + 2}",
            line=e.problem_mark.line + 2,
            code="YAML_DUPLICATE_KEY",
        ))
        return {}
    except Exception as e:
        issues.append(Issue("ERROR", rel(path), f"frontmatter YAML parse error: {e}", code="YAML_PARSE"))
        return {}


def frontmatter_line_number(fm: str, key: str) -> Optional[int]:
    pattern = re.compile(rf"^\s*{re.escape(key)}\s*:", re.MULTILINE)
    m = pattern.search(fm)
    if not m:
        return None
    return fm[:m.start()].count("\n") + 2  # +1 for 1-indexed, +1 for opening ---


def is_generated_content_page(path: Path) -> bool:
    if path.name in GENERATED_INDEX_FILES or rel(path) in GENERATED_CONTENT_PATHS:
        return True
    return False


def is_generated_or_template(path: Path) -> bool:
    if is_generated_content_page(path):
        return True
    if TEMPLATES_DIR in path.parents:
        return True
    return False


def is_schema_or_workflow_doc(path: Path) -> bool:
    r = rel(path)
    return (
        r in {"vault-schema.md", "CLAUDE.md"}
        or r.startswith("schema/schema-")
        or path.name == "vault-schema-manifest-patch.md"
    )


def comparable_title(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r"([A-Za-z])['’]s\b", r"\1s", value)
    value = value.replace("&", " and ")
    value = re.sub(r"[^0-9A-Za-z]+", "-", value)
    return value.strip("-").lower()


def title_matches_filename(title: str, filename_stem: str) -> bool:
    title_key = comparable_title(title)
    filename_key = comparable_title(filename_stem)
    if title_key == filename_key:
        return True

    stopwords = {"and", "of", "the", "s"}
    title_words = [w for w in title_key.split("-") if w and w not in stopwords]
    filename_words = [w for w in filename_key.split("-") if w and w not in stopwords]

    def word_matches(a: str, b: str) -> bool:
        return a == b or a.rstrip("s") == b.rstrip("s")

    def is_subsequence(shorter: list[str], longer: list[str]) -> bool:
        pos = 0
        for word in longer:
            if pos < len(shorter) and word_matches(shorter[pos], word):
                pos += 1
        return pos == len(shorter)

    return is_subsequence(title_words, filename_words) or is_subsequence(filename_words, title_words)


def remove_h2_sections(body: str, names: Iterable[str]) -> str:
    targets = {n.lower() for n in names}
    lines = body.splitlines(keepends=True)
    out: list[str] = []
    skipping = False
    for line in lines:
        if line.startswith("## "):
            title = line[3:].strip().lower()
            skipping = title in targets
        out.append("\n" if skipping else line)
    return "".join(out)


def is_wiki_entry_path(path: Path) -> bool:
    if not str(path).startswith(str(WIKI_DIR)):
        return False
    if is_generated_or_template(path):
        return False
    return True


def is_source_record_path(path: Path) -> bool:
    try:
        parts = path.relative_to(ROOT).parts
    except Exception:
        parts = path.parts
    return bool(parts and parts[0] in SOURCE_RECORD_DIRS)


def is_book_source_record_path(path: Path) -> bool:
    try:
        parts = path.relative_to(ROOT).parts
    except Exception:
        parts = path.parts
    return bool(len(parts) >= 2 and parts[0] == "books")


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def mask_markdown_code(text: str) -> str:
    """Mask fenced and inline code while preserving offsets and line numbers."""

    def mask(m: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))

    text = re.sub(r"```.*?```", mask, text, flags=re.DOTALL)
    return re.sub(r"`[^`\n]*`", mask, text)


def line_of_pos(text: str, pos: int, offset: int = 1) -> int:
    return text[:pos].count("\n") + offset


def has_h2_section(body: str, heading_names: Iterable[str]) -> bool:
    names = set(heading_names)
    for line in body.splitlines():
        if line.startswith("## "):
            h = line[3:].strip()
            if h in names:
                return True
    return False


def section_text(body: str, heading_names: Iterable[str]) -> str:
    """
    Extract content of a top-level H2 section matching any name.
    """
    names = set(heading_names)
    lines = body.splitlines()
    capture = False
    out: List[str] = []
    for line in lines:
        if line.startswith("## "):
            h = line[3:].strip()
            if capture:
                break
            capture = h in names
            continue
        if capture:
            out.append(line)
    return "\n".join(out)


def extract_wikilink_target(raw: str) -> str:
    """Target of [[Target]], [[Target|Display]], [[Target#Heading|Display]] or [[Target\\|Display]]."""
    return vaultlib.parse_wikilink(raw)[0]


def extract_wikilinks(text: str) -> List[Tuple[str, int]]:
    clean = strip_code_blocks(text)
    return [(extract_wikilink_target(m.group(1)), m.start()) for m in WIKILINK_RE.finditer(clean)]


def extract_embeds(text: str) -> List[Tuple[str, int]]:
    clean = strip_code_blocks(text)
    return [(extract_wikilink_target(m.group(1)), m.start()) for m in EMBED_RE.finditer(clean)]


def normalize_title(s: str) -> str:
    return s.strip()


@lru_cache(maxsize=None)
def book_folder_subtype(book_folder: str) -> str:
    """Read the overview subtype that determines how a book folder is indexed."""
    directory = WIKI_DIR / "arguments" / "books" / book_folder
    if not directory.exists():
        return ""
    subtypes: set[str] = set()
    for path in directory.glob("*.md"):
        data = entry_metadata(path)
        subtype = str((data or {}).get("subtype") or "").strip()
        if subtype:
            subtypes.add(subtype)
    # Safety first: any edited-volume marker prevents chapter consolidation,
    # even if inconsistent metadata also contains a mergeable subtype.
    for subtype in EDITED_VOLUME_BOOK_SUBTYPES:
        if subtype in subtypes:
            return subtype
    for subtype in MERGEABLE_BOOK_SUBTYPES:
        if subtype in subtypes:
            return subtype
    return ""


def argument_book_key(target: str, by_title: Dict[str, Dict[str, Any]]) -> Optional[str]:
    """Return a shared folder key only for monograph/textbook Arguments."""
    item = by_title.get(target)
    if not item or item.get("type") != "argument":
        return None

    parts = Path(str(item.get("path") or "")).parts
    if len(parts) < 5 or parts[:3] != ("wiki", "arguments", "books"):
        return None
    subtype = str(item.get("book_subtype") or book_folder_subtype(parts[3])).strip()
    return parts[3] if subtype in MERGEABLE_BOOK_SUBTYPES else None


def markdown_visible_text(text: str) -> str:
    """Return compact reader-visible text for a single Markdown line."""
    def wikilink_label(match: re.Match[str]) -> str:
        raw = match.group(1)
        if "\\|" in raw:
            return raw.split("\\|", 1)[1].strip()
        if "|" in raw:
            return raw.split("|", 1)[1].strip()
        return extract_wikilink_target(raw)

    visible = WIKILINK_RE.sub(wikilink_label, text)
    visible = MD_LINK_RE.sub(lambda match: match.group(1), visible)
    visible = re.sub(r"[*_~`]", "", visible)
    visible = re.sub(r"<[^>]+>", "", visible)
    return re.sub(r"\s+", " ", visible).strip()


def check_related_research_entry_length(path: Path, text: str, issues: List[Issue]) -> None:
    """Warn when a top-level related-research index entry is too long."""
    if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path) or not is_wiki_entry_path(path):
        return

    _, body, body_start_line = split_frontmatter(text)
    callout_header_re = re.compile(
        r"^(?P<quote>\s*(?:>\s*)+)\[![^\]\n]+\][+-]?\s*(?P<title>.*)$"
    )
    quoted_line_re = re.compile(r"^(?P<quote>\s*(?:>\s*)+)(?P<content>.*)$")
    in_index = False
    index_depth = 0
    line_number = body_start_line

    for line in body.splitlines(keepends=True):
        header = callout_header_re.match(line)
        if header:
            depth = header.group("quote").count(">")
            if in_index and depth > index_depth:
                line_number += line.count("\n")
                continue
            title = header.group("title")
            in_index = "相关研究" in title and "索引" in title
            index_depth = depth if in_index else 0
            line_number += line.count("\n")
            continue

        if not in_index:
            line_number += line.count("\n")
            continue

        quoted = quoted_line_re.match(line)
        if not quoted:
            if line.strip():
                in_index = False
            line_number += line.count("\n")
            continue

        content = quoted.group("content").rstrip("\r\n")
        if quoted.group("quote").count(">") != index_depth or not re.match(r"^[-*+]\s+", content):
            line_number += line.count("\n")
            continue

        entry = re.sub(r"^[-*+]\s+", "", content, count=1)
        visible_length = len(markdown_visible_text(entry))
        if visible_length > RELATED_RESEARCH_ENTRY_MAX_CHARS:
            issues.append(Issue(
                "WARN",
                rel(path),
                f"相关研究索引顶层条目的可见文字为 {visible_length} 个字符，"
                f"超过上限 {RELATED_RESEARCH_ENTRY_MAX_CHARS}；请压缩为一句话索引",
                line=line_number,
                code="RELATED_RESEARCH_ENTRY_TOO_LONG",
            ))

        line_number += line.count("\n")


def check_related_research_duplicate_books(
    path: Path,
    text: str,
    by_title: Dict[str, Dict[str, Any]],
    issues: List[Issue],
) -> None:
    """Warn when one index lists several chapters of one monograph/textbook.

    Only the top-level bullets of callouts titled ``相关研究索引`` count as
    source entries. Links inside an entry's explanation remain free to point to
    several chapters, which supports the preferred consolidated-book format.
    """
    if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path) or not is_wiki_entry_path(path):
        return

    _, body, body_start_line = split_frontmatter(text)
    lines = body.splitlines(keepends=True)
    callout_header_re = re.compile(
        r"^(?P<quote>\s*(?:>\s*)+)\[![^\]\n]+\][+-]?\s*(?P<title>.*)$"
    )
    quoted_line_re = re.compile(r"^(?P<quote>\s*(?:>\s*)+)(?P<content>.*)$")

    in_index = False
    index_depth = 0
    seen_books: Dict[str, Tuple[str, int]] = {}
    line_number = body_start_line

    for line in lines:
        header = callout_header_re.match(line)
        if header:
            title = header.group("title")
            depth = header.group("quote").count(">")
            if in_index and depth > index_depth:
                line_number += line.count("\n")
                continue
            in_index = "相关研究" in title and "索引" in title
            index_depth = depth if in_index else 0
            seen_books = {}
            line_number += line.count("\n")
            continue

        if not in_index:
            line_number += line.count("\n")
            continue

        quoted = quoted_line_re.match(line)
        if not quoted:
            if line.strip():
                in_index = False
                seen_books = {}
            line_number += line.count("\n")
            continue

        depth = quoted.group("quote").count(">")
        content = quoted.group("content")
        if depth != index_depth or not re.match(r"^[-*+]\s+", content):
            line_number += line.count("\n")
            continue

        target = ""
        for match in WIKILINK_RE.finditer(content):
            candidate = extract_wikilink_target(match.group(1))
            if candidate.startswith("Argument_"):
                target = candidate
                break
        if not target:
            line_number += line.count("\n")
            continue

        book_key = argument_book_key(target, by_title)
        if not book_key:
            line_number += line.count("\n")
            continue

        previous = seen_books.get(book_key)
        if previous:
            previous_target, previous_line = previous
            issues.append(Issue(
                "WARN",
                rel(path),
                f"相关研究索引重复列出同一本专著或教材：[[{previous_target}]]（第 {previous_line} 行）与 "
                f"[[{target}]]；请合并为一个顶层来源条目，并在说明中保留所需章节链接",
                line=line_number,
                code="RELATED_RESEARCH_DUPLICATE_BOOK",
            ))
        else:
            seen_books[book_key] = (target, line_number)

        line_number += line.count("\n")


# -----------------------------
# Index loading
# -----------------------------

def load_index(issues: List[Issue]) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, str]]:
    """
    Return:
      by_title: title -> item
      path_to_title: relative path -> title
    """
    by_title: Dict[str, Dict[str, Any]] = {}
    path_to_title: Dict[str, str] = {}

    if not INDEX_JSON.exists():
        issues.append(Issue("ERROR", rel(INDEX_JSON), "missing wiki/index.json. Run python3 scripts/vault_index.py --wiki-only first.", code="INDEX_MISSING"))
        return by_title, path_to_title

    try:
        data = json.loads(read_text(INDEX_JSON))
    except Exception as e:
        issues.append(Issue("ERROR", rel(INDEX_JSON), f"cannot parse index.json: {e}", code="INDEX_PARSE"))
        return by_title, path_to_title

    if isinstance(data, dict):
        # Support both {"entries": [...]} and {"Title": "path"}-like variants.
        if "entries" in data and isinstance(data["entries"], list):
            entries = data["entries"]
        else:
            entries = []
            for title, value in data.items():
                if isinstance(value, str):
                    entries.append({"title": title, "path": value})
                elif isinstance(value, dict):
                    v = dict(value)
                    v.setdefault("title", title)
                    entries.append(v)
    elif isinstance(data, list):
        entries = data
    else:
        issues.append(Issue("ERROR", rel(INDEX_JSON), "index.json must be a list or object", code="INDEX_TYPE"))
        return by_title, path_to_title

    for item in entries:
        if not isinstance(item, dict):
            continue
        title = str(item.get("title", "")).strip()
        path = str(item.get("path", "")).strip()
        if not title or not path:
            continue
        if title in by_title:
            issues.append(Issue("ERROR", rel(INDEX_JSON), f"duplicate title in index: {title}", code="INDEX_DUP_TITLE"))
        by_title[title] = item
        path_to_title[path] = title

    # Alias uniqueness across the vault. Aliases drive wiki_linker targets,
    # so an alias shared by two entries makes auto-linking nondeterministic.
    norm_title_owner = {unicodedata.normalize("NFC", t).lower().strip(): t for t in by_title}
    alias_owners: Dict[str, List[Tuple[str, str]]] = {}
    for item in entries:
        if not isinstance(item, dict):
            continue
        owner = str(item.get("title", "")).strip()
        if not owner:
            continue
        for alias in item.get("aliases") or []:
            key = unicodedata.normalize("NFC", str(alias)).lower().strip()
            if key:
                alias_owners.setdefault(key, []).append((owner, str(alias)))
    for key, owners in alias_owners.items():
        titles = sorted({t for t, _ in owners})
        if len(titles) > 1:
            issues.append(Issue(
                "ERROR", rel(INDEX_JSON),
                f"alias {owners[0][1]!r} is used by multiple entries: {', '.join(titles)}",
                code="ALIAS_DUPLICATE_CROSS_ENTRY",
            ))
        shadowed = norm_title_owner.get(key)
        if shadowed and all(t != shadowed for t in titles):
            issues.append(Issue(
                "ERROR", rel(INDEX_JSON),
                f"alias {owners[0][1]!r} of {titles[0]!r} duplicates the title of another entry: {shadowed!r}",
                code="ALIAS_DUPLICATE_CROSS_ENTRY",
            ))

    return by_title, path_to_title


# -----------------------------
# Checks
# -----------------------------

def check_required_files(issues: List[Issue]) -> None:
    required = [
        WIKI_DIR,
        INDEX_JSON,
        WIKI_DIR / "index.md",
        ROOT / "scripts" / "vault_index.py",
        ROOT / "scripts" / "wiki_index.py",
        ROOT / "scripts" / "citation_index.py",
        CITATION_DIR,
        CITATION_FULL_JSON,
        CITATION_AMBIGUOUS_JSON,
        ROOT / "scripts" / "wiki_linker.py",
        ROOT / "scripts" / "wiki_relations.py",
        ROOT / "vault-schema.md",
        ROOT / "CLAUDE.md",
    ]
    for p in required:
        if not p.exists():
            issues.append(Issue("ERROR", rel(p), "required file or directory missing", code="REQUIRED_MISSING"))


def check_old_references(path: Path, text: str, issues: List[Issue]) -> None:
    if is_schema_or_workflow_doc(path):
        return
    patterns = [
        ("scripts/update_wiki_index.py", "old index script name; use scripts/wiki_index.py"),
        ("wiki/wiki-index.md", "old wiki index path; use wiki/index.md"),
        ("wiki-index.md", "old wiki index filename; use index.md if referring to generated wiki homepage"),
        ("schema/schema-monograph-pdf.md", "old monograph schema; use schema/schema-monograph.md"),
        ("schema/schema-monograph-epub.md", "old monograph schema; use schema/schema-monograph.md"),
        ("schema/schema-figures.md", "removed figures schema; use image placeholders in the current Argument page"),
        ("schema-figures.md", "removed figures schema; use image placeholders in the current Argument page"),
    ]
    for pattern, msg in patterns:
        start = 0
        while True:
            idx = text.find(pattern, start)
            if idx == -1:
                break
            issues.append(Issue("WARN", rel(path), msg, line=line_of_pos(text, idx), code="OLD_REFERENCE"))
            start = idx + len(pattern)


RETIRED_SECTION_HEADINGS = {"相关研究", "领域应用", "总览", "实证数据", "条目关联", "相关条目"}


def expected_def_title(fm: Dict[str, Any]) -> Optional[str]:
    """主定义标题：条目英文名（frontmatter title），不加中文翻译。"""
    title = str(fm.get("title") or "").strip()
    if not title:
        return None
    return title


def check_figure_callouts(path: Path, text: str, issues: List[Issue]) -> None:
    """[!figure] 只放图片或图片占位，固定写 [!figure]- 默认折叠。"""
    if is_schema_or_workflow_doc(path) or "/templates/" in rel(path) or "[!figure" not in text:
        return
    lines = text.split("\n")
    for i, line in enumerate(lines):
        m = re.match(r"^> \[!figure(\|[^\]]*)?\]([+-]?)", line)
        if not m:
            continue
        if m.group(2) != "-":
            issues.append(Issue("ERROR", rel(path), "[!figure] 固定写 [!figure]- 默认折叠", line=i + 1, code="FIGURE_NOT_COLLAPSED"))
        j = i + 1; body = []
        while j < len(lines) and lines[j].startswith(">"):
            body.append(lines[j]); j += 1
        has_img = any("![" in b or "<img" in b for b in body)
        if not has_img and not any("待上传" in b or "待补" in b for b in body):
            issues.append(Issue("ERROR", rel(path), "[!figure] 只放图片或图片占位（写“原文图 X：图名（待上传）”）；文字、表格、框架改用对应 callout", line=i + 1, code="FIGURE_NO_IMAGE"))


def check_def_title(path: Path, text: str, issues: List[Issue]) -> None:
    """正文第一个 callout 是 [!def] 时，它是条目的主定义，标题统一写条目名称。"""
    if is_schema_or_workflow_doc(path) or "/templates/" in rel(path) or yaml is None:
        return
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return
    try:
        fm = yaml.load(m.group(1), Loader=FAST_SAFE_LOADER) or {}
    except Exception:
        return
    if not isinstance(fm, dict) or str(fm.get("type") or "") in {"argument", "person"}:
        return
    body = text[m.end():]
    cm = re.search(r"^> \[!([^\]|]+)[^\]]*\][+-]?(.*)$", body, re.M)
    if cm and cm.group(1) != "def":
        # 主定义前有其他 callout 时，只认标题仍为通用占位（核心定义等）的第一个 [!def]
        dm = re.search(r"^> \[!(def)[^\]]*\][+-]?(.*)$", body, re.M)
        cm = dm if dm and dm.group(2).strip() in {"核心定义", "方法定义", "核心界定", "概念定义", "定义", ""} else None
    if not cm or cm.group(1) != "def":
        return
    nxt = re.search(r"^> \[!([^\]|]+)", body[cm.end():], re.M)
    if nxt and nxt.group(1) == "def" and "\n## " not in body[cm.end():cm.end() + nxt.start()] and nxt.start() < 1500:
        return  # 并列定义（如 不伤害 / 行善）各自写术语名
    want = expected_def_title(fm)
    if want and cm.group(2).strip() != want:
        issues.append(Issue("ERROR", rel(path),
            f"主定义 callout 标题应为条目名称：> [!def] {want}（现为“{cm.group(2).strip()}”）",
            line=text[:m.end() + cm.start()].count("\n") + 1, code="DEF_TITLE"))


def check_retired_headings(path: Path, text: str, issues: List[Issue]) -> None:
    """这些章节标题已废止：内容由带标题的 callout 承担（相关研究索引 / 条目关联 / 章节总览 / 实证表格 marker）。
    脚本不再依赖它们；只有 ``## 来源`` 仍是固定章节。"""
    if is_schema_or_workflow_doc(path) or "/templates/" in rel(path):
        return
    in_fence = False
    for n, line in enumerate(text.split("\n"), 1):
        if line.startswith("```"):
            in_fence = not in_fence
        if in_fence or not line.startswith("## "):
            continue
        name = line[3:].strip()
        if name in RETIRED_SECTION_HEADINGS:
            issues.append(Issue("ERROR", rel(path),
                f"已废止的章节标题 ## {name}：删去标题，把章节名写进下方 callout 标题（如 [!evidence-grid-a] 相关研究索引、[!entry-map] 条目关联），标题下的过渡句一并删除",
                line=n, code="RETIRED_HEADING"))


def check_effect_tables(path: Path, text: str, issues: List[Issue]) -> None:
    """实证表格：指标白名单、数值格式、效应条一致性；新增行必须有数据。见 scripts/effect_table.py。"""
    if "table-marker" not in text:
        return
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from effect_table import lint_file
    except Exception as e:  # pragma: no cover
        issues.append(Issue("WARN", rel(path), f"effect_table.py unavailable: {e}", code="EFFECT_TABLE_TOOL"))
        return
    try:
        head_text = subprocess.run(["git", "show", f"HEAD:{rel(path)}"], capture_output=True, text=True, cwd=str(ROOT)).stdout
    except Exception:
        head_text = ""
    for q in lint_file(path, text, head_text):
        issues.append(Issue(q.sev, rel(path), q.msg, line=q.line, code=q.code))


def check_quartz_safety(path: Path, text: str, issues: List[Issue]) -> None:
    if is_schema_or_workflow_doc(path):
        return
    if "#ccc" in text:
        issues.append(Issue("WARN", rel(path), "HTML color #ccc found; use rgb(204,204,204)", line=line_of_pos(text, text.find("#ccc")), code="QUARTZ_COLOR"))

    # Inline script tag risk. External script files are allowed.
    for m in re.finditer(r"<script\b[^>]*>", text, flags=re.IGNORECASE):
        if re.search(r"\bsrc\s*=", m.group(0), flags=re.IGNORECASE):
            continue
        issues.append(Issue("WARN", rel(path), "inline <script> found; put script logic in external static files", line=line_of_pos(text, m.start()), code="QUARTZ_SCRIPT"))

    # Absolute local path risk.
    for m in re.finditer(r"/Users/[^)\]\s\"']+", text):
        val = m.group(0)
        # Allow explicit schema note for script path; still warn, not error.
        issues.append(Issue("WARN", rel(path), f"absolute local path found: {val}", line=line_of_pos(text, m.start()), code="LOCAL_PATH"))


_ALIAS_TITLE_MAPS_CACHE: Dict[int, Tuple[Dict[str, str], Dict[str, Set[str]]]] = {}


def get_global_alias_and_title_maps(by_title: Dict[str, Dict[str, Any]]) -> Tuple[Dict[str, str], Dict[str, Set[str]]]:
    cached = _ALIAS_TITLE_MAPS_CACHE.get(id(by_title))
    if cached is None:
        title_map: Dict[str, str] = {}
        alias_map: Dict[str, Set[str]] = {}
        for t, item in by_title.items():
            t_norm = unicodedata.normalize("NFC", str(t)).lower().strip()
            if t_norm:
                title_map[t_norm] = t
            if isinstance(item, dict):
                for al in item.get("aliases") or []:
                    a_norm = unicodedata.normalize("NFC", str(al)).lower().strip()
                    if a_norm:
                        alias_map.setdefault(a_norm, set()).add(t)
        cached = (title_map, alias_map)
        _ALIAS_TITLE_MAPS_CACHE[id(by_title)] = cached
    return cached


_HOMONYM_INDEX_CACHE: Dict[int, Tuple[Dict[str, Set[Tuple[str, str]]], Dict[str, Set[Tuple[str, str]]]]] = {}
_PAREN_ABBR_RE = re.compile(r"[(（]\s*([^()（）]+?)\s*[)）]")


def _is_declared_abbreviation(inner: str, before: str) -> bool:
    """True when '(XYZ)' abbreviates the words right before it.

    'Education for All (EFA)' qualifies; a qualifier such as
    '创新联盟（欧盟）' or 'Youth Guarantee (EU)' does not."""
    letters = re.sub(r"[^A-Za-z]", "", inner).lower()
    if len(letters) < 2 or re.search(r"[^A-Za-z0-9&\-./ ]", inner):
        return False
    words = re.findall(r"[A-Za-z][A-Za-z'’-]*", before)
    initials = "".join(w[0].lower() for w in words)
    if not initials:
        return False
    # Abbreviation letters must appear in order among the initials of the
    # preceding words, starting at one of the last few words' initials.
    for start in range(max(0, len(initials) - len(letters) - 3), len(initials)):
        if initials[start] != letters[0]:
            continue
        pos = start
        ok = True
        for ch in letters[1:]:
            pos = initials.find(ch, pos + 1)
            if pos < 0:
                ok = False
                break
        if ok:
            return True
    return False


def _homonym_index(by_title: Dict[str, Dict[str, Any]]):
    """Build once: parenthetical abbreviations and Chinese person surnames -> owners."""
    cached = _HOMONYM_INDEX_CACHE.get(id(by_title))
    if cached is not None:
        return cached
    paren: Dict[str, Set[Tuple[str, str]]] = {}
    surname: Dict[str, Set[Tuple[str, str]]] = {}
    for t, item in by_title.items():
        title = str(item.get("title") or t)
        if title.startswith("Argument_"):
            continue
        is_person = item.get("type") == "person"
        for term in [title] + [str(x) for x in (item.get("aliases") or [])]:
            term = unicodedata.normalize("NFC", term)
            for m in _PAREN_ABBR_RE.finditer(term):
                inner = m.group(1).strip()
                if inner and _is_declared_abbreviation(inner, term[:m.start()]):
                    paren.setdefault(inner, set()).add((title, term))
                    if not inner.isupper():
                        paren.setdefault(inner.lower(), set()).add((title, term))
            if is_person and "·" in term:
                last = term.rsplit("·", 1)[1].strip()
                if last:
                    surname.setdefault(last, set()).add((title, term))
    cached = (paren, surname)
    _HOMONYM_INDEX_CACHE[id(by_title)] = cached
    return cached


def alias_homonym_hits(alias: str, owner_title: Any, by_title: Dict[str, Dict[str, Any]]) -> List[str]:
    """Hard homonyms that the exact-duplicate check misses.

    1. Another entry declares this string as its abbreviation in parentheses,
       e.g. 'Education for All (EFA)' vs alias 'EFA' on another entry.
    2. Another Person's Chinese full-name alias ends with this surname,
       e.g. '卡尔·皮尔逊' vs surname alias '皮尔逊' on another person."""
    if not by_title:
        return []
    a = unicodedata.normalize("NFC", alias.strip())
    if not a:
        return []
    paren, surname = _homonym_index(by_title)
    owner = str(owner_title or "")
    found = set(paren.get(a, set()))
    if not a.isupper():
        found |= paren.get(a.lower(), set())
    found |= surname.get(a, set())
    return sorted(f"{title} [{term}]" for title, term in found if title != owner)


def check_frontmatter(path: Path, text: str, by_title: Dict[str, Dict[str, Any]], issues: List[Issue]) -> Optional[Dict[str, Any]]:
    fm, body, _ = split_frontmatter(text)
    if fm is None:
        if path.name in GENERATED_INDEX_FILES or is_schema_or_workflow_doc(path):
            return None
        # Source files may have frontmatter too; templates always do. Warn generally.
        issues.append(Issue("WARN", rel(path), "missing or malformed frontmatter delimiters", code="FM_MISSING"))
        return None

    check_frontmatter_raw_yaml_style(path, fm, issues)
    data = parse_yaml_fm(fm, path, issues)
    if not data:
        return data

    title = data.get("title")
    typ = data.get("type")

    # title checks
    if is_wiki_entry_path(path):
        if not title or (isinstance(title, str) and not title.strip()):
            issues.append(Issue("ERROR", rel(path), "missing frontmatter title", line=frontmatter_line_number(fm, "title"), code="TITLE_MISSING"))
        elif isinstance(title, str):
            stem = path.stem
            # Templater files use placeholders; normal entries should match filename.
            if "<%" not in title and title != stem and not title_matches_filename(title, stem):
                issues.append(Issue("WARN", rel(path), f"title differs from filename stem: title={title!r}, filename={stem!r}", line=frontmatter_line_number(fm, "title"), code="TITLE_FILENAME_MISMATCH"))
            # Schema section 4: no brackets, colons, or quote marks in titles of
            # Concept / Theory / Method / Instrument / Fact entries (apostrophes allowed).
            if "<%" not in title and typ in {"concept", "theory", "method", "instrument", "fact"}:
                bad = re.findall(r"[()（）:：\"“”]", title)
                if bad:
                    issues.append(Issue("ERROR", rel(path), f"title must not contain brackets, colons, or quote marks (move abbreviations to aliases): {title!r}", line=frontmatter_line_number(fm, "title"), code="TITLE_FORBIDDEN_CHAR"))

    # type checks
    if is_wiki_entry_path(path):
        if not typ or (isinstance(typ, str) and not typ.strip()):
            issues.append(Issue("ERROR", rel(path), "missing frontmatter type", line=frontmatter_line_number(fm, "type"), code="TYPE_MISSING"))
        elif typ not in VALID_TYPES:
            issues.append(Issue("ERROR", rel(path), f"unknown type: {typ}", line=frontmatter_line_number(fm, "type"), code="TYPE_INVALID"))
        elif typ in TYPE_PATH_HINTS:
            expected = TYPE_PATH_HINTS[typ]
            if expected not in rel(path):
                issues.append(Issue("WARN", rel(path), f"type {typ!r} does not match expected path hint {expected!r}", line=frontmatter_line_number(fm, "type"), code="TYPE_PATH_MISMATCH"))

    # Argument should not use aliases.
    if typ == "argument" and "aliases" in data and data.get("aliases") not in (None, [], ""):
        issues.append(Issue("ERROR", rel(path), "Argument entries should not use aliases", line=frontmatter_line_number(fm, "aliases"), code="ARGUMENT_ALIASES"))

    # Non-argument wiki semantic entries should usually have aliases key.
    if is_wiki_entry_path(path) and typ in {"concept", "theory", "method", "instrument", "person", "fact"} and "aliases" not in data:
        issues.append(Issue("WARN", rel(path), f"type {typ!r} should include aliases field", code="ALIASES_MISSING"))

    # Alias quality (schema section 4): precise, single-language, non-redundant.
    if is_wiki_entry_path(path) and typ in {"concept", "theory", "method", "instrument", "person", "fact"}:
        aliases_val = data.get("aliases")
        if isinstance(aliases_val, list):
            alias_line = frontmatter_line_number(fm, "aliases")
            seen_alias_keys = set()
            title_key = unicodedata.normalize("NFC", str(title)).lower().strip() if isinstance(title, str) else ""
            title_map, alias_map = get_global_alias_and_title_maps(by_title) if by_title else ({}, {})
            for alias in aliases_val:
                if not isinstance(alias, str) or not alias.strip():
                    continue
                a = alias.strip()
                key = unicodedata.normalize("NFC", a).lower()
                if key in seen_alias_keys:
                    issues.append(Issue("WARN", rel(path), f"duplicate alias within entry (case or width variants count as one): {alias!r}", line=alias_line, code="ALIAS_QUALITY"))
                seen_alias_keys.add(key)
                if title_key and key == title_key:
                    issues.append(Issue("WARN", rel(path), f"alias duplicates the entry title and is redundant: {alias!r}", line=alias_line, code="ALIAS_QUALITY"))

                # Check cross-entry duplicate alias or alias duplicating another entry's title
                other_title = title_map.get(key)
                if other_title and other_title != title:
                    issues.append(Issue("ERROR", rel(path), f"alias {alias!r} duplicates the title of another entry: {other_title!r}", line=alias_line, code="ALIAS_DUPLICATE_CROSS_ENTRY"))
                other_owners = sorted({o for o in alias_map.get(key, set()) if o != title})
                if other_owners:
                    issues.append(Issue("ERROR", rel(path), f"alias {alias!r} is already used by another entry: {', '.join(other_owners)}", line=alias_line, code="ALIAS_DUPLICATE_CROSS_ENTRY"))

                # Names/acronyms inside Chinese terms are normal usage
                # ("Pearson相关", "PISA素养", "IB文凭项目"). Flag only a bilingual
                # gloss copied into the alias, e.g. "可见的学习（Visible Learning，VL）批评".
                alias_has_cjk = any("㐀" <= ch <= "鿿" for ch in a)
                if alias_has_cjk and re.search(r"[（(][^（）()]*[A-Za-z]{2,}[^（）()]*[）)]", a):
                    issues.append(Issue("WARN", rel(path), f"alias embeds a bilingual gloss; keep the Chinese and English names as separate aliases: {alias!r}", line=alias_line, code="ALIAS_QUALITY"))
                homonyms = alias_homonym_hits(a, title, by_title)
                if homonyms:
                    issues.append(Issue(
                        "ERROR", rel(path),
                        f"alias {alias!r} is a homonym of another entry: {', '.join(homonyms[:5])}. "
                        "Aliases must not be shared across entries; delete it or replace it with a longer specific form.",
                        line=alias_line, code="ALIAS_HOMONYM",
                    ))

    # Only Argument pages maintain source record links.
    if is_wiki_entry_path(path) and typ in {"concept", "theory", "method", "instrument", "person", "fact"} and "sources" in data:
        issues.append(Issue("ERROR", rel(path), "non-Argument wiki entries should not include YAML sources; use related_arguments via Argument links", line=frontmatter_line_number(fm, "sources"), code="NON_ARGUMENT_SOURCES_FIELD"))

    if typ == "argument" and "sources" not in data:
        issues.append(Issue("WARN", rel(path), "Argument entries should include sources field for source record links", code="ARGUMENT_SOURCES_MISSING"))

    if typ == "person":
        for field in ["family_name", "given_names", "initials", "citation_name"]:
            if field in data:
                issues.append(Issue("WARN", rel(path), f"person entry should not include legacy citation helper field {field}", line=frontmatter_line_number(fm, field), code=f"PERSON_{field.upper()}_LEGACY"))
        # "William F. Buckley Jr." is stored as "William F. Buckley Jr.md": the
        # title's final period merges with the extension separator.
        if (isinstance(title, str) and "<%" not in title
                and unicodedata.normalize("NFC", path.stem) not in {unicodedata.normalize("NFC", title), unicodedata.normalize("NFC", title.rstrip("."))}):
            issues.append(Issue("WARN", rel(path), "person filename stem should match title exactly", line=frontmatter_line_number(fm, "title"), code="PERSON_TITLE_FILENAME_MISMATCH"))
        aliases = data.get("aliases")
        if isinstance(aliases, list):
            for alias in aliases:
                if isinstance(alias, str) and alias_is_single_english_family(alias):
                    issues.append(Issue("WARN", rel(path), f"person alias should not be a single English family name: {alias!r}", line=frontmatter_line_number(fm, "aliases"), code="PERSON_ALIAS_SINGLE_FAMILY"))
        if is_wiki_entry_path(path):
            born = data.get("born")
            died = data.get("died")
            if born is None or str(born).strip() == "":
                issues.append(Issue("ERROR", rel(path), "person entry missing born year", line=frontmatter_line_number(fm, "born"), code="PERSON_BORN_MISSING"))
            elif not PERSON_YEAR_PATTERN.match(str(born).strip()):
                issues.append(Issue("ERROR", rel(path), f"invalid born year format: {born!r}", line=frontmatter_line_number(fm, "born"), code="PERSON_BORN_FORMAT"))
            if died is not None and str(died).strip() != "":
                if not PERSON_YEAR_PATTERN.match(str(died).strip()):
                    issues.append(Issue("ERROR", rel(path), f"invalid died year format: {died!r}", line=frontmatter_line_number(fm, "died"), code="PERSON_DIED_FORMAT"))
            if "wiki/persons/schools/" in rel(path):
                if data.get("subtype") != "school":
                    issues.append(Issue("WARN", rel(path), "school entry under wiki/persons/schools/ should specify subtype: school", line=frontmatter_line_number(fm, "subtype"), code="PERSON_SCHOOL_SUBTYPE_MISSING"))
                if data.get("nationality") == "schools":
                    issues.append(Issue("WARN", rel(path), "school nationality should be a country/region, not 'schools'", line=frontmatter_line_number(fm, "nationality"), code="PERSON_NATIONALITY_INVALID"))

    if typ == "instrument":
        allowed_instrument_types = {
            "scale",
            "questionnaire",
            "test",
            "inventory",
            "rubric",
            "checklist",
            "observation-tool",
            "interview-tool",
            "other",
        }
        instrument_type = data.get("instrument_type")
        if instrument_type not in allowed_instrument_types:
            issues.append(
                Issue(
                    "ERROR",
                    rel(path),
                    f"instrument_type must be one of {sorted(allowed_instrument_types)}: {instrument_type!r}",
                    line=frontmatter_line_number(fm, "instrument_type"),
                    code="INSTRUMENT_TYPE_INVALID",
                )
            )
        if is_wiki_entry_path(path):
            if "developers" not in data or data.get("developers") in (None, "", []):
                issues.append(Issue(
                    "ERROR",
                    rel(path),
                    "instrument entries must include developers",
                    line=frontmatter_line_number(fm, "developers"),
                    code="DEVELOPERS_MISSING",
                ))
            else:
                check_instrument_developers(path, fm, data.get("developers"), issues)

    if is_citation_eligible_argument(data):
        citation = data.get("citation")
        if not isinstance(citation, str) or not citation.strip():
            issues.append(Issue("ERROR", rel(path), "citation-eligible Argument must include a non-empty full citation", line=frontmatter_line_number(fm, "citation"), code="ARGUMENT_FULL_CITATION_MISSING"))
        for field in ["year", "citation_aliases"]:
            if field not in data or data.get(field) in (None, "", []):
                issues.append(Issue("WARN", rel(path), f"citation-eligible Argument missing {field}", line=frontmatter_line_number(fm, field), code=f"CITATION_{field.upper()}_MISSING"))
        for field in ["citation_stem", "citation_suffix", "citation_key", "citation_short"]:
            if field in data and data.get(field) not in (None, "", []):
                issues.append(Issue("WARN", rel(path), f"Argument should not include legacy citation field {field}; run vault_index.py", line=frontmatter_line_number(fm, field), code=f"CITATION_{field.upper()}_LEGACY"))
        year = data.get("year")
        if year not in (None, "") and not re.match(r"^(19|20)\d{2}$", str(year)):
            issues.append(Issue("ERROR", rel(path), f"year should be four digits: {year!r}", line=frontmatter_line_number(fm, "year"), code="CITATION_YEAR_FORMAT"))
        aliases = data.get("citation_aliases") or []
        if aliases and not isinstance(aliases, list):
            issues.append(Issue("ERROR", rel(path), "citation_aliases must be a YAML list", line=frontmatter_line_number(fm, "citation_aliases"), code="CITATION_ALIASES_TYPE"))
        elif isinstance(aliases, list):
            expected_base = expected_citation_aliases_from_meta(data)
            if aliases and expected_base and aliases != expected_base and not all(re.match(r"^.+(?:19|20)\d{2}[a-z]\)?$", str(a)) for a in aliases) \
                    and not apa7_disambiguated_aliases(aliases, expected_base):
                issues.append(Issue("WARN", rel(path), f"citation_aliases differ from authors + year base form; run vault_index.py: {aliases!r}", line=frontmatter_line_number(fm, "citation_aliases"), code="CITATION_ALIASES_MISMATCH"))

    # summary checks
    if "summary" in data:
        check_summary(path, fm, data.get("summary"), issues)
    elif is_wiki_entry_path(path) and typ != "source":
        issues.append(Issue("ERROR", rel(path), "missing required summary field", code="SUMMARY_MISSING"))

    # tags
    tags = data.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            issues.append(Issue("ERROR", rel(path), "tags must be a YAML list", line=frontmatter_line_number(fm, "tags"), code="TAGS_TYPE"))
        else:
            for tag in tags:
                if not isinstance(tag, str) or not TAG_RE.match(tag):
                    issues.append(Issue("WARN", rel(path), f"tag should be lowercase English slash/hyphen style: {tag!r}", line=frontmatter_line_number(fm, "tags"), code="TAG_FORMAT"))

    # Creator fields.
    for field in ["authors", "editors"]:
        if field in data:
            val = data.get(field)
            if not isinstance(val, list):
                issues.append(Issue("ERROR", rel(path), f"{field} must be a YAML list", line=frontmatter_line_number(fm, field), code=f"{field.upper()}_TYPE"))
            else:
                for item in val:
                    if not isinstance(item, str):
                        issues.append(Issue("ERROR", rel(path), f"{field} items must be strings: {item!r}", line=frontmatter_line_number(fm, field), code=f"{field.upper()}_ITEM"))
                    elif typ == "argument":
                        check_argument_creator_apa_display(path, fm, field, item, issues)

    if typ == "argument":
        explicit_language = normalized_source_language(data.get("source_language"))
        source_language = source_language_from_meta(data)
        citation = str(data.get("citation") or "").strip()
        year = str(data.get("year") or "").strip()

        if data.get("source_language") not in (None, "") and explicit_language not in {"zh", "en"}:
            issues.append(Issue(
                "ERROR",
                rel(path),
                f"source_language must be zh or en: {data.get('source_language')!r}",
                line=frontmatter_line_number(fm, "source_language"),
                code="SOURCE_LANGUAGE_INVALID",
            ))

        if source_language == "zh":
            if not explicit_language:
                issues.append(Issue(
                    "WARN",
                    rel(path),
                    "Chinese original publication should declare source_language: zh",
                    line=frontmatter_line_number(fm, "citation"),
                    code="SOURCE_LANGUAGE_MISSING",
                ))
            if not chinese_author_part(citation, year):
                issues.append(Issue(
                    "ERROR",
                    rel(path),
                    "Chinese original citation must begin with Chinese author name(s) followed by the year",
                    line=frontmatter_line_number(fm, "citation"),
                    code="CHINESE_CITATION_AUTHOR",
                ))
            for author in data.get("authors") or []:
                display = creator_display(str(author))
                if not (has_cjk(display) and re.search(r"[A-Za-z]", display)):
                    issues.append(Issue(
                        "ERROR",
                        rel(path),
                        f"Chinese original author display must be bilingual, e.g. 中文名（Surname, X.）: {author!r}",
                        line=frontmatter_line_number(fm, "authors"),
                        code="CHINESE_AUTHOR_BILINGUAL",
                    ))
            aliases = data.get("citation_aliases") or []
            if isinstance(aliases, list):
                for alias in aliases:
                    if not has_cjk(str(alias)):
                        issues.append(Issue(
                            "ERROR",
                            rel(path),
                            f"Chinese original citation_aliases must be Chinese-only: {alias!r}",
                            line=frontmatter_line_number(fm, "citation_aliases"),
                            code="CHINESE_CITATION_ALIAS_LANGUAGE",
                        ))

        publication_type = str(data.get("publication_type") or "").strip()
        if publication_type in {"book", "edited-volume", "book-chapter"} and TEMPLATES_DIR not in path.parents:
            publisher = str(data.get("publisher") or "").strip()
            if not publisher:
                issues.append(Issue(
                    "ERROR",
                    rel(path),
                    "book citation metadata must include publisher",
                    line=frontmatter_line_number(fm, "publisher"),
                    code="BOOK_PUBLISHER_MISSING",
                ))

    # Full references follow APA 7 mechanics (no publisher location, en dash
    # ranges, https://doi.org DOIs, group author not repeated as publisher).
    if typ in {"argument", "source"} and isinstance(data.get("citation"), str) and data.get("citation").strip() \
            and TEMPLATES_DIR not in path.parents:
        import citation_index  # noqa: PLC0415
        fixed, codes = citation_index.apa7_reference(data["citation"], str(data.get("publication_place") or ""))
        if codes:
            labels = {"location": "drop publisher location (APA 7)", "dash": "en dash in ranges",
                      "doi": "DOI as https://doi.org/", "publisher_is_author": "group author not repeated as publisher"}
            issues.append(Issue(
                "WARN", rel(path),
                f"citation is not APA 7 ({'; '.join(labels[c] for c in codes)}); run vault_lint.py --fix: {fixed!r}",
                line=frontmatter_line_number(fm, "citation"), code="CITATION_APA7_FORMAT",
            ))

    # Argument entries should include authors field for AI-filled creator metadata.
    if typ == "argument" and "authors" not in data:
        issues.append(Issue("WARN", rel(path), "argument entry should include authors field", code="ARGUMENT_AUTHORS_MISSING"))

    # related_* and sources are script-maintained but should be valid lists.
    for field in AUTO_RELATION_FIELDS:
        if field in data:
            val = data.get(field)
            if not isinstance(val, list):
                issues.append(Issue("ERROR", rel(path), f"{field} must be a YAML list", line=frontmatter_line_number(fm, field), code="REL_FIELD_TYPE"))
            else:
                for item in val:
                    if not (isinstance(item, str) and item.startswith("[[") and item.endswith("]]")):
                        issues.append(Issue("ERROR", rel(path), f"{field} item must be a quoted wikilink string: {item!r}", line=frontmatter_line_number(fm, field), code="REL_FIELD_ITEM"))

    # part_of can be empty or wikilink string.
    if "part_of" in data:
        part_of = data.get("part_of")
        if part_of not in (None, ""):
            if isinstance(part_of, list):
                for item in part_of:
                    if not (isinstance(item, str) and item.startswith("[[") and item.endswith("]]")):
                        issues.append(Issue("ERROR", rel(path), f"part_of list item must be wikilink string: {item!r}", line=frontmatter_line_number(fm, "part_of"), code="PART_OF_ITEM"))
            elif not (isinstance(part_of, str) and part_of.startswith("[[") and part_of.endswith("]]")):
                issues.append(Issue("ERROR", rel(path), f"part_of must be empty or wikilink string: {part_of!r}", line=frontmatter_line_number(fm, "part_of"), code="PART_OF_TYPE"))

    # created / updated presence
    if is_wiki_entry_path(path) and typ != "source":
        for k in ["created", "updated", "status"]:
            if k not in data:
                issues.append(Issue("WARN", rel(path), f"missing {k} field", code=f"{k.upper()}_MISSING"))
        if "confidence" in data:
            conf = data.get("confidence")
            if conf not in (None, "") and conf not in ALLOWED_CONFIDENCE:
                issues.append(Issue("ERROR", rel(path), f"confidence must be one of {sorted(ALLOWED_CONFIDENCE)}: {conf!r}", line=frontmatter_line_number(fm, "confidence"), code="CONFIDENCE_INVALID"))
        if "status" in data:
            st = data.get("status")
            if st not in (None, "") and st not in ALLOWED_STATUS:
                issues.append(Issue("ERROR", rel(path), f"status must be one of {sorted(ALLOWED_STATUS)}: {st!r}", line=frontmatter_line_number(fm, "status"), code="STATUS_INVALID"))

    return data


def check_summary(path: Path, fm: str, summary: Any, issues: List[Issue]) -> None:
    line = frontmatter_line_number(fm, "summary")

    if summary is None:
        if is_wiki_entry_path(path):
            issues.append(Issue("ERROR", rel(path), "summary must not be empty", line=line, code="SUMMARY_EMPTY"))
        return
    if not isinstance(summary, str):
        issues.append(Issue("ERROR", rel(path), "summary must be a string", line=line, code="SUMMARY_TYPE"))
        return

    # Check raw line for double quotes around summary.
    raw_line = None
    for l in fm.splitlines():
        if re.match(r"^\s*summary\s*:", l):
            raw_line = l
            break
    if raw_line is not None:
        after = raw_line.split(":", 1)[1].strip()
        if not (after.startswith('"') and after.endswith('"')):
            issues.append(Issue("ERROR", rel(path), 'summary must be wrapped in double quotes: summary: "..."', line=line, code="SUMMARY_QUOTES"))

    if not summary.strip():
        if is_wiki_entry_path(path):
            issues.append(Issue("ERROR", rel(path), "summary must not be empty", line=line, code="SUMMARY_EMPTY"))
        return

    if len(summary) > 250:
        issues.append(Issue("ERROR", rel(path), f"summary must not exceed 250 characters (currently {len(summary)}): {summary[:50]}...", line=line, code="SUMMARY_TOO_LONG"))

    if is_wiki_entry_path(path):
        if "<%" in summary or re.search(r"\b(?:todo|tbd|暂无)\b", summary, re.IGNORECASE):
            issues.append(Issue("ERROR", rel(path), f"summary contains unreplaced template placeholder or TODO: {summary!r}", line=line, code="SUMMARY_PLACEHOLDER"))

    for ch in FORBIDDEN_SUMMARY_CHARS:
        if ch in summary:
            label = {"\"": "double quote", "'": "single quote", ":": "English colon", "_": "underscore"}[ch]
            issues.append(Issue("ERROR", rel(path), f"summary contains forbidden {label}: {summary!r}", line=line, code="SUMMARY_FORBIDDEN_CHAR"))

    banned_phrases = ["本文研究", "作者认为", "本研究发现", "本论文", "本章认为", "本文认为", "本文旨在", "本章旨在", "本研究旨在"]
    for phrase in banned_phrases:
        if phrase in summary:
            issues.append(Issue("WARN", rel(path), f"summary should not use phrase {phrase!r}", line=line, code="SUMMARY_STYLE"))


def check_wikilinks(path: Path, text: str, by_title: Dict[str, Dict[str, Any]], issues: List[Issue], data: Optional[Dict[str, Any]] = None) -> None:
    if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path):
        return

    fm, body, body_start_line = split_frontmatter(text)
    if fm is None:
        body = text
        body_start_line = 1

    body_for_links = remove_h2_sections(body, ["来源", "Sources", "Source"])

    # Existing normal wikilinks.
    for m in WIKILINK_RE.finditer(strip_code_blocks(body_for_links)):
        raw = m.group(1)
        if not raw.strip():
            issues.append(Issue("ERROR", rel(path), "empty wikilink [[]]", line=line_of_pos(body, m.start(), body_start_line), code="EMPTY_WIKILINK"))
            continue
        target = extract_wikilink_target(raw)
        # Ignore relative headings only.
        if not target:
            continue

        # Argument entries must not cite themselves via wikilink.
        if is_argument_entry(data):
            self_targets = {path.stem}
            if data and data.get("title"):
                self_targets.add(str(data["title"]).strip())
            if data and data.get("argument_key"):
                self_targets.add(str(data["argument_key"]).strip())
            if target in self_targets:
                issues.append(Issue(
                    "ERROR",
                    rel(path),
                    f"argument page should not cite itself via wikilink: [[{raw}]]",
                    line=line_of_pos(body, m.start(), body_start_line),
                    code="ARGUMENT_SELF_CITATION",
                ))
                continue

        # Ignore attachments and non-md obvious files in normal links? Normal [[file.pdf]] should warn.
        if Path(target).suffix.lower() in {".pdf", ".epub", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}:
            issues.append(Issue("WARN", rel(path), f"file link should usually be embedded with ![[...]] or placed in source page: [[{raw}]]", line=line_of_pos(body, m.start(), body_start_line), code="FILE_WIKILINK"))
            continue
        if target not in by_title:
            issues.append(Issue("WARN", rel(path), f"wikilink target not found in wiki/index.json: [[{target}]]", line=line_of_pos(body, m.start(), body_start_line), code="BROKEN_WIKILINK"))

    # Embed checks: only verify obvious local embedded target exists somewhere.
    for m in EMBED_RE.finditer(strip_code_blocks(body)):
        target = extract_wikilink_target(m.group(1))
        if not target:
            continue
        suffix = Path(target).suffix.lower()
        if suffix in {".pdf", ".epub", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}:
            # Search common locations by filename. This can be expensive, so cache by filename.
            target_name = Path(target).name
            if not embedded_file_exists_by_name(target_name):
                issues.append(Issue("WARN", rel(path), f"embedded file not found in vault: ![[{target}]]", line=line_of_pos(body, m.start(), body_start_line), code="MISSING_EMBED_FILE"))

    # Raw markdown links to local absolute path.
    for m in MD_LINK_RE.finditer(body):
        url = m.group(2)
        if url.startswith("/Users/"):
            issues.append(Issue("WARN", rel(path), f"Markdown link points to absolute local path: {url}", line=line_of_pos(body, m.start(), body_start_line), code="MD_LOCAL_LINK"))


def check_sources_section(path: Path, text: str, data: Optional[Dict[str, Any]], issues: List[Issue]) -> None:
    if not is_wiki_entry_path(path):
        return
    if data and data.get("type") == "source":
        return

    fm, body, _ = split_frontmatter(text)
    has_source_section = has_h2_section(body, ["来源", "Sources"])

    if is_non_argument_semantic_entry(data):
        if has_source_section:
            issues.append(Issue("ERROR", rel(path), "non-Argument wiki entries should not have ## 来源 / ## Sources; use Argument links and related_arguments", code="NON_ARGUMENT_SOURCE_SECTION"))
        return

    if not is_argument_entry(data):
        return

    if not has_source_section:
        issues.append(Issue("WARN", rel(path), "Argument entry missing ## 来源 / ## Sources section", code="ARGUMENT_SOURCE_SECTION_MISSING"))
        return

    source_sec = section_text(body, ["来源", "Sources"])
    links = [target for target, _ in extract_wikilinks(source_sec)]
    if not links:
        issues.append(Issue("WARN", rel(path), "Argument 来源 section must contain source record wikilinks", code="ARGUMENT_SOURCE_SECTION_EMPTY"))
    for target in links:
        if "/" not in target:
            issues.append(
                Issue(
                    "ERROR",
                    rel(path),
                    f"source wikilink must use a vault-root-relative path to avoid Quartz folder-note 404s: [[{target}]]",
                    code="SOURCE_LINK_NOT_PATH_QUALIFIED",
                )
            )
            continue
        source_path = ROOT / (target if target.endswith(".md") else f"{target}.md")
        if not source_path.exists():
            issues.append(
                Issue(
                    "ERROR",
                    rel(path),
                    f"source wikilink target does not exist: [[{target}]]",
                    code="SOURCE_LINK_TARGET_MISSING",
                )
            )


def check_template_consistency(path: Path, text: str, issues: List[Issue]) -> None:
    if TEMPLATES_DIR not in path.parents:
        return
    fm, body, _ = split_frontmatter(text)
    if fm is None:
        issues.append(Issue("ERROR", rel(path), "template missing frontmatter", code="TEMPLATE_FM_MISSING"))
        return
    data = parse_yaml_fm(fm, path, issues)
    typ = data.get("type")

    # Common fields.
    common = ["title", "summary", "type", "tags", "status", "created", "updated"]
    for field in common:
        if field not in data:
            issues.append(Issue("WARN", rel(path), f"template missing common field: {field}", code="TEMPLATE_FIELD_MISSING"))

    if typ != "template":
        for field in RELATED_FIELDS:
            if field not in data:
                issues.append(Issue("WARN", rel(path), f"template missing relation field: {field}", code="TEMPLATE_REL_MISSING"))

    if typ == "argument":
        if "aliases" in data:
            issues.append(Issue("WARN", rel(path), "argument template should not include aliases", code="TEMPLATE_ARGUMENT_ALIASES"))
        for field in ["citation_stem", "citation_suffix", "citation_key", "citation_short"]:
            if field in data:
                issues.append(Issue("WARN", rel(path), f"argument template should not include legacy citation field: {field}", code="TEMPLATE_ARGUMENT_CITATION_LEGACY"))
        if "authors" not in data:
            issues.append(Issue("WARN", rel(path), "argument template should include authors field", code="TEMPLATE_ARGUMENT_AUTHORS_MISSING"))
        if data.get("subtype") != "edited-volume-overview" and "citation_aliases" not in data:
            issues.append(Issue("WARN", rel(path), "citation-eligible argument template should include citation_aliases field", code="TEMPLATE_ARGUMENT_CITATION_ALIASES_MISSING"))
        if "sources" not in data:
            issues.append(Issue("WARN", rel(path), "argument template should include sources field", code="TEMPLATE_ARGUMENT_SOURCES_MISSING"))
        if "## 来源" not in body and "## Sources" not in body:
            issues.append(Issue("WARN", rel(path), "argument template missing ## 来源 / ## Sources section", code="TEMPLATE_ARGUMENT_SOURCE_SECTION"))
    if typ == "concept":
        if "[!ref-table]" not in body:
            issues.append(Issue("ERROR", rel(path), "concept template must include the general empirical-data table", code="TEMPLATE_CONCEPT_EMPIRICAL_TABLE"))
    if typ == "instrument":
        instrument_fields = [
            "instrument_type",
            "developers",
            "original_year",
            "languages",
            "item_count",
            "administration_mode",
            "response_format",
        ]
        for field in instrument_fields:
            if field not in data:
                issues.append(Issue("ERROR", rel(path), f"instrument template missing field: {field}", code="TEMPLATE_INSTRUMENT_FIELD_MISSING"))
        for callout in ["[!ref-table]", "[!instrument-profile]", "[!instrument-items]"]:
            if callout not in body:
                issues.append(Issue("ERROR", rel(path), f"instrument template missing required callout: {callout}", code="TEMPLATE_INSTRUMENT_CALLOUT_MISSING"))
    if typ in {"concept", "theory", "method", "instrument", "person", "fact"}:
        if "aliases" not in data:
            issues.append(Issue("WARN", rel(path), f"{typ} template should include aliases", code="TEMPLATE_ALIASES_MISSING"))
        if "sources" in data:
            issues.append(Issue("ERROR", rel(path), f"{typ} template should not include sources field", code="TEMPLATE_NON_ARGUMENT_SOURCES"))
        if "## 来源" in body or "## Sources" in body:
            issues.append(Issue("ERROR", rel(path), f"{typ} template should not include ## 来源 / ## Sources section", code="TEMPLATE_NON_ARGUMENT_SOURCE_SECTION"))


def check_source_record(path: Path, text: str, issues: List[Issue]) -> None:
    is_book_source = is_book_source_record_path(path)
    if not is_source_record_path(path) and not is_book_source:
        return
    fm, body, body_start_line = split_frontmatter(text)
    if fm is None:
        return
    data = parse_yaml_fm(fm, path, issues)
    if not data:
        return

    # Only apply when it looks like source record.
    if data.get("type") != "source" and "extracted_to" not in data:
        return

    if "citation" not in data or not data.get("citation"):
        issues.append(Issue("WARN", rel(path), "source record missing citation", code="SOURCE_CITATION_MISSING"))

    extracted = data.get("extracted_to")
    if extracted is not None:
        if not isinstance(extracted, list):
            issues.append(Issue("ERROR", rel(path), "extracted_to must be a list", code="EXTRACTED_TO_TYPE"))
        else:
            for item in extracted:
                if not (isinstance(item, str) and item.startswith("[[") and item.endswith("]]")):
                    issues.append(Issue("ERROR", rel(path), f"extracted_to item must be quoted wikilink string: {item!r}", code="EXTRACTED_TO_ITEM"))
                elif not item.strip("[]").startswith("Argument_"):
                    issues.append(Issue("WARN", rel(path), f"extracted_to should normally point to Argument pages only: {item!r}", code="EXTRACTED_TO_NON_ARGUMENT"))

    if "processed_date" not in data:
        issues.append(Issue("WARN", rel(path), "source record missing processed_date", code="PROCESSED_DATE_MISSING"))

    # Source record should embed a PDF or EPUB viewer, unless it is some special source.
    if "![[ " in body:
        issues.append(Issue("WARN", rel(path), "possible malformed embed with space after [[", code="EMBED_SPACE"))
    clean_body = strip_code_blocks(body)
    for m in EMBED_RE.finditer(clean_body):
        target = extract_wikilink_target(m.group(1))
        if target.lower().endswith(".epub"):
            issues.append(Issue("WARN", rel(path), "EPUB source records should use the epub.js viewer instead of Obsidian embed", line=line_of_pos(clean_body, m.start(), body_start_line), code="SOURCE_EPUB_OBSIDIAN_EMBED"))
        elif target.lower().endswith(".pdf"):
            expected_asset = asset_url_for_path(path.parent / target)
            published_pdf = re.search(r'<iframe\b[^>]*\bsrc=["\']https://img\.mylikemie\.icu/[^"\']+\.pdf["\']', clean_body, re.S)
            if expected_asset not in clean_body and not published_pdf:
                issues.append(Issue("WARN", rel(path), f"PDF source record missing NAS iframe URL: {expected_asset}", line=line_of_pos(clean_body, m.start(), body_start_line), code="SOURCE_PDF_NAS_URL_MISSING"))

    if is_book_source:
        sibling_epub = path.with_suffix(".epub")
        body_mentions_epub = ".epub" in clean_body.lower()
        if sibling_epub.exists() or body_mentions_epub:
            viewer_matches = list(EPUB_VIEWER_RE.finditer(clean_body))
            if not viewer_matches:
                issues.append(Issue("WARN", rel(path), "book EPUB source record missing data-epub viewer", code="SOURCE_EPUB_VIEWER_MISSING"))
            elif sibling_epub.exists():
                expected = f"/books/{path.parent.name}/{sibling_epub.name}"
                expected_asset = asset_url_for_path(sibling_epub)
                seen_asset = False
                for m in viewer_matches:
                    viewer_path = m.group(1)
                    if viewer_path == expected_asset:
                        seen_asset = True
                        continue
                    if viewer_path != expected:
                        issues.append(Issue("WARN", rel(path), f"book EPUB viewer path should be {expected!r} or {expected_asset!r}", line=line_of_pos(clean_body, m.start(), body_start_line), code="SOURCE_EPUB_VIEWER_PATH"))
                if not seen_asset:
                    issues.append(Issue("WARN", rel(path), f"book EPUB source record missing NAS viewer URL: {expected_asset}", code="SOURCE_EPUB_NAS_URL_MISSING"))


def check_path_and_index_consistency(path: Path, data: Optional[Dict[str, Any]], path_to_title: Dict[str, str], issues: List[Issue]) -> None:
    if not is_wiki_entry_path(path):
        return
    if data is None:
        return
    if data.get("type") == "source":
        return

    r = rel(path)
    key = unicodedata.normalize("NFC", r)  # wiki_index stores NFC paths; APFS names are NFD
    title = data.get("title")
    if isinstance(title, str):
        title = unicodedata.normalize("NFC", title)
    if path.name in GENERATED_INDEX_FILES:
        return
    if key not in path_to_title:
        issues.append(Issue("WARN", r, "wiki entry is not present in wiki/index.json; run vault_index.py --wiki-only or check exclusions", code="ENTRY_NOT_INDEXED"))
    elif title and path_to_title.get(key) != title:
        issues.append(Issue("WARN", r, f"index title differs from frontmatter title: index={path_to_title.get(key)!r}, fm={title!r}", code="INDEX_TITLE_MISMATCH"))


@lru_cache(maxsize=None)
def entry_metadata(path: Path) -> Optional[Dict[str, Any]]:
    try:
        text = read_text(path)
    except Exception:
        return None
    fm, _, _ = split_frontmatter(text)
    if not fm or yaml is None:
        return None
    try:
        data = yaml.load(fm, Loader=FAST_SAFE_LOADER) or {}
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def argument_body_links() -> set[str]:
    links: set[str] = set()
    argument_dir = WIKI_DIR / "arguments"
    if not argument_dir.exists():
        return links
    for path in iter_md_files(argument_dir):
        if is_generated_or_template(path):
            continue
        data = entry_metadata(path)
        if not data or data.get("type") != "argument":
            continue
        try:
            text = read_text(path)
        except Exception:
            continue
        _, body, _ = split_frontmatter(text)
        body = remove_h2_sections(body, ["来源", "Sources", "Source"])
        for target, _ in extract_wikilinks(body):
            if target:
                links.add(target)
    return links


def check_new_entries_mentioned_in_arguments(paths: List[Path], issues: List[Issue]) -> None:
    new_entries: list[tuple[Path, str, str]] = []
    seen_paths: set[Path] = set()
    for path in paths:
        resolved = path.resolve()
        if resolved in seen_paths:
            continue
        seen_paths.add(resolved)
        if not is_wiki_entry_path(path):
            continue
        if git_path_exists_at_head(path):
            continue
        data = entry_metadata(path)
        if not data:
            continue
        typ = str(data.get("type") or "").strip()
        if typ not in ARGUMENT_REQUIRED_NEW_ENTRY_TYPES:
            continue
        tags = data.get("tags") or []
        if isinstance(tags, list) and ("metax" in tags or "eef" in tags):
            # MetaX stub entries are created from datasets/metax/mapping.json and indexed from the
            # Visible Learning Meta-X fact entry, not from an Argument page.
            continue
        title = str(data.get("title") or path.stem).strip()
        if title:
            new_entries.append((path, title, typ))

    if not new_entries:
        return

    linked_from_arguments = argument_body_links()
    for path, title, typ in new_entries:
        if title in linked_from_arguments:
            continue
        issues.append(
            Issue(
                "ERROR",
                rel(path),
                f"new {typ} entry must be mentioned and wikilinked in an Argument page body: [[{title}]]",
                code="NEW_ENTRY_NOT_IN_ARGUMENT",
            )
        )


def bold_boundary_insertions(body: str) -> list[int]:
    """Find simple ** spans whose punctuation boundary prevents CommonMark bold.

    Keep triple/nested emphasis and escaped delimiters out of automatic fixes.
    Code and comments are masked while preserving source offsets.
    """
    scan = mask_markdown_code(body)
    insertions: set[int] = set()
    scan = re.sub(r"<!--.*?-->|%%.*?%%", lambda m: re.sub(r"[^\n]", " ", m.group(0)), scan, flags=re.DOTALL)

    def punctuation(char: str) -> bool:
        return bool(char) and unicodedata.category(char)[0] in "PS"

    def word_side(char: str) -> bool:
        return bool(char) and not char.isspace() and not punctuation(char)

    for match in re.finditer(r"(?<![\\*])\*\*(?!\*)([^*\n]+?)(?<![\\*])\*\*(?!\*)", scan):
        content = match.group(1)
        before = scan[match.start() - 1] if match.start() else ""
        after = scan[match.end()] if match.end() < len(scan) else ""
        if punctuation(content[0]) and word_side(before):
            insertions.add(match.start())
        if punctuation(content[-1]) and word_side(after):
            insertions.add(match.end())
    return sorted(insertions)


def fix_bold_boundaries(text: str) -> Tuple[str, int]:
    _, body, _ = split_frontmatter(text)
    head = text[:len(text) - len(body)]
    positions = bold_boundary_insertions(body)
    for position in reversed(positions):
        body = body[:position] + " " + body[position:]
    return head + body, len(positions)


# Latin-script author + 等/等人 -> "et al." (silent auto-fix, like table-pipe
# escaping; no lint warning). "Hopkins 等, 1996" -> "Hopkins et al., 1996",
# "Cai 等人（2025）" -> "Cai et al.（2025）", "Hattie 等人指出" -> "Hattie et al. 指出".
# A name counts as a person when a year follows or it is a known Person surname /
# cited author. Left alone: acronyms and organisations (OECD、PISA 等), non-persons
# (Teach 等工具), lists of names (Mignolo、Dussel 等; Holmes 和 King 等人), words
# beginning with 等 (等级, 等同 …) and Chinese authors (王等, 2025).
LATIN_DENG_RE = re.compile(
    r"(?<![A-Za-zÀ-ɏ'’\-])"
    r"(?P<name>[A-Z][A-Za-zÀ-ɏ'’\-]*[A-Za-zÀ-ɏ]\.?)"
    r"\s*(?P<deng>等人(?!员)|等(?![级同于待价值距量效式号比位差高长分]|学者|研究者|作者|专家|人员))"
    r"(?:(?:\s*(?P<comma>[，,])\s*|\s*(?P<paren>[（(])\s*)(?P<year>(?:19|20)\d{2}[a-z]?)(?![0-9]))?"
)
_LIST_BEFORE_RE = re.compile(r"[A-Za-z\u00C0-\u024F.]\s*(?:、|和|与|及|&|\band|,)\s*(?:[A-Z][\w\u00C0-\u024F'’.\-]*\s+){0,3}$")


@lru_cache(maxsize=1)
def known_person_surnames() -> frozenset:
    """Surnames of Person entries (not schools) and of cited Argument authors."""
    names: Set[str] = set()
    try:
        entries = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    except Exception:
        entries = []
    for e in entries if isinstance(entries, list) else []:
        if not isinstance(e, dict) or e.get("type") != "person" or "/schools/" in str(e.get("path", "")):
            continue
        title = str(e.get("title", ""))
        if title.split():
            names.add(title.split()[-1])
        for alias in e.get("aliases") or []:
            m = re.match(r"([A-Z][\wÀ-ɏ'’\-]+),\s", str(alias))
            if m:
                names.add(m.group(1))
    try:
        data = json.loads(CITATION_FULL_JSON.read_text(encoding="utf-8"))
        items = data.get("items", {}) if isinstance(data, dict) else {}
        for item in items.values() if isinstance(items, dict) else []:
            for author in (item.get("authors") or []) if isinstance(item, dict) else []:
                m = re.match(r"([A-Z][\w\u00C0-\u024F'’\-]+(?:\s[A-Z][\w\u00C0-\u024F'’\-]+)?),\s", str(author))
                if m:
                    names.add(m.group(1).split()[-1])
    except Exception:
        pass
    return frozenset(n for n in names if not n.isupper())


def _latin_deng_replacement(m: "re.Match[str]", before: str = "") -> Optional[str]:
    name = m.group("name")
    if name.rstrip(".").isupper():
        return None  # acronyms / organisations: OECD 等, PISA 等
    if _LIST_BEFORE_RE.search(before):
        return None  # several named people: "A、B 等", "A 和 B 等人"
    if m.group("year"):
        if m.group("comma"):
            return f"{name} et al., {m.group('year')}"
        paren = m.group("paren")
        return f"{name} et al.{' ' if paren == '(' else ''}{paren}{m.group('year')}"
    if name.rstrip(".") not in known_person_surnames():
        return None
    return f"{name} et al."


def fix_latin_deng(text: str) -> Tuple[str, int]:
    """Replace 等/等人 after Latin-script cited authors with et al. (code untouched)."""
    masked = mask_markdown_code(text)
    out: List[str] = []
    pos = 0
    count = 0
    for m in LATIN_DENG_RE.finditer(masked):
        rep = _latin_deng_replacement(m, masked[max(0, m.start() - 60):m.start()])
        if rep is None:
            continue
        nxt = text[m.end():m.end() + 1]
        if not m.group("year") and nxt and not nxt.isspace() and nxt not in "，。、；：,.;:)）]」”'\"*":
            rep += " "
        out.append(text[pos:m.start()])
        out.append(rep)
        pos = m.end()
        count += 1
    out.append(text[pos:])
    return "".join(out), count


def check_markdown_misc(path: Path, text: str, issues: List[Issue]) -> None:
    # Unclosed code fence.
    if text.count("```") % 2 != 0:
        issues.append(Issue("WARN", rel(path), "odd number of fenced code block markers ```", code="CODE_FENCE_UNCLOSED"))


    # HTML hex colors generally.
    for m in re.finditer(r"#[0-9a-fA-F]{3,6}\b", text):
        if m.group(0).lower() == "#ccc":
            continue
        # Not all hex is bad, warn only in html-ish contexts.
        line_start = text.rfind("\n", 0, m.start()) + 1
        line_end = text.find("\n", m.start())
        line = text[line_start: line_end if line_end != -1 else len(text)]
        if "<" in line and ">" in line:
            issues.append(Issue("WARN", rel(path), f"HTML hex color found; prefer rgb(...): {m.group(0)}", line=line_of_pos(text, m.start()), code="HTML_HEX_COLOR"))

    if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path):
        return

    _, body, body_start_line = split_frontmatter(text)
    scan = mask_markdown_code(body)

    for position in bold_boundary_insertions(body):
        issues.append(Issue(
            "WARN", rel(path),
            "bold delimiter touches punctuation inside and prose outside; "
            "Quartz may display literal **; insert a space outside the delimiter",
            line=line_of_pos(body, position, body_start_line),
            code="BOLD_DELIMITER_BOUNDARY",
        ))

    if is_wiki_entry_path(path) and "/arguments/" not in f"/{rel(path)}":
        source_subject_re = re.compile(
            r"(?:^|[。！？\n>|])\s*(?:[-*]\s*)?(?:\*\*[^*\n]+\*\*\s*)?"
            # "研究者" is left out: in method/concept entries the researcher is the
            # actor of the method ("研究者通过统计证据来判断"), not a source being narrated.
            r"(论文|本文|本章|作者|本研究|本论证|第[一二三四五六七八九十百0-9]+章|全章)"
            r"\s*(认为|指出|发现|报告|显示|表明|提出|讨论|介绍|说明|分析|检验|考察|引用|援引|使用|采用|通过|将|把|未|没有|旨在|聚焦|关注|强调|主张)"
        )
        for m in source_subject_re.finditer(scan):
            subject = m.group(1)
            line_start = scan.rfind("\n", 0, m.start(1)) + 1
            line_end = scan.find("\n", m.start(1))
            if "____" in scan[line_start: line_end if line_end != -1 else len(scan)]:
                continue  # fill-in writing templates ("本研究将解决____")
            issues.append(
                Issue(
                    "WARN",
                    rel(path),
                    f"wiki prose should state the knowledge claim directly instead of using {subject!r} as the routine subject",
                    line=line_of_pos(scan, m.start(), body_start_line),
                    code="WIKI_SOURCE_CENTERED_SUBJECT",
                )
            )

    for m in re.finditer(r"\*\*([^*\n]+?)\*\*\s*[：:]", scan):
        title = m.group(1).strip()
        issues.append(
            Issue(
                "ERROR",
                rel(path),
                f"bold heading must not be followed by a colon: **{title}**",
                line=line_of_pos(scan, m.start(), body_start_line),
                code="BOLD_HEADING_COLON",
            )
        )

    for m in re.finditer(
        r"\*\*([^*\n]*[\u3400-\u9fff][^*\n]*)\*\*\s*([（(][^）)\n]*[A-Za-z][^）)\n]*[）)])",
        scan,
    ):
        chinese = m.group(1).strip()
        annotation = m.group(2)
        if re.fullmatch(r"[（(]\s*pp?\.\s*[^）)]+[）)]", annotation, flags=re.IGNORECASE):
            continue
        if re.fullmatch(r"[（(]\s*\[\[Argument_[^\]]*\]\]\s*[）)]", annotation):
            continue
        if BARE_CITATION_PARENS_RE.fullmatch(annotation):
            continue
        issues.append(
            Issue(
                "ERROR",
                rel(path),
                f"English annotation belongs inside the bold heading: **{chinese}{annotation}**",
                line=line_of_pos(scan, m.start(), body_start_line),
                code="BOLD_HEADING_ENGLISH_OUTSIDE",
            )
        )


def check_stat_card_titles(path: Path, text: str, issues: List[Issue]) -> None:
    """Check only the display-number heading of each direct stat-cards item."""
    if not is_wiki_entry_path(path) or is_schema_or_workflow_doc(path):
        return
    _, body, body_start_line = split_frontmatter(text)
    body = re.sub(r"<!--[\s\S]*?-->|%%[\s\S]*?%%",
                  lambda m: re.sub(r"[^\n]", " ", m[0]), body)
    quoted_re = re.compile(r"^[ \t]*(?P<quotes>(?:>[ \t]?)+)(?P<content>.*)$")
    header_re = re.compile(r"^\[!(?P<kind>[^\]\n]+)\][+-]?(?:[ \t]|$)", re.I)
    item_re = re.compile(r"^(?P<indent>[ \t]*)[-*+]\s+\*\*(?P<title>.+?)\*\*(?:\s|$)")
    # Each callout owns only items at its quote depth and list indentation.
    stack = []
    fence = None
    for number, line in enumerate(body.splitlines(), body_start_line):
        quoted = quoted_re.match(line)
        content = quoted['content'] if quoted else line
        marker = re.match(r"^[ \t]*(`{3,}|~{3,})", content)
        if marker:
            token = marker[1]
            if fence is None:
                fence = (token[0], len(token))
            elif token[0] == fence[0] and len(token) >= fence[1]:
                fence = None
            continue
        if fence is not None:
            continue
        if not quoted:
            stack.clear()
            continue
        depth = quoted['quotes'].count('>')
        while stack and stack[-1]['depth'] > depth:
            stack.pop()
        header = header_re.match(content.lstrip())
        if header:
            while stack and stack[-1]['depth'] >= depth:
                stack.pop()
            stack.append({'depth': depth, 'kind': header['kind'].lower(), 'indent': None})
            continue
        if not stack or stack[-1]['kind'] != 'stat-cards' or stack[-1]['depth'] != depth:
            continue
        item = item_re.match(content)
        if not item:
            continue
        current = stack[-1]
        indent = len(item['indent'].expandtabs(4))
        if current['indent'] is None:
            current['indent'] = indent
        if indent != current['indent']:
            continue
        title = markdown_visible_text(item['title'])
        if re.search(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U000323af]", title):
            issues.append(Issue(
                'WARN', rel(path),
                f'stat-cards 数值子标题含汉字：{title!r}。尽量使用数字与符号，'
                '币种可用 $、¥、€、£；数量级可用科学记数法或 K/M/B。'
                '量词和说明移入释义，保留原数值、币种与近似/范围条件；不自动换算。',
                line=number, code='STAT_CARDS_TITLE_TEXT',
            ))


def check_axis_callouts(path: Path, text: str, issues: List[Issue]) -> None:
    """Validate the two-level `[!debates]` / `[!axis]` Markdown contract."""
    scan = mask_markdown_code(text)

    for match in AXIS_BAD_SIBLING_SEPARATOR_RE.finditer(scan):
        issues.append(Issue(
            "ERROR",
            rel(path),
            "sibling [!axis] cards must be separated by a single '>' line; "
            "run vault_lint.py --fix to replace this blank '> >' separator",
            line=line_of_pos(scan, match.start()),
            code="AXIS_SIBLING_SEPARATOR",
        ))

    for match in AXIS_CALLOUT_LINE_RE.finditer(scan):
        depth = match.group("quotes").count(">")
        if depth == 2:
            continue
        issues.append(Issue(
            "ERROR",
            rel(path),
            f"[!axis] must be a two-level nested callout written as '> > [!axis]' "
            f"(found quote depth {depth}); run vault_lint.py --fix to normalize it",
            line=line_of_pos(scan, match.start()),
            code="AXIS_NESTING",
        ))

def check_templater_placeholders(path: Path, text: str, issues: List[Issue]) -> None:
    if TEMPLATES_DIR in path.parents:
        return
    for m in TEMPLATER_PLACEHOLDER_RE.finditer(text):
        issues.append(Issue("ERROR", rel(path), f"Templater placeholder left in non-template file: {m.group(0)!r}", line=line_of_pos(text, m.start()), code="TEMPLATER_PLACEHOLDER"))



def load_citation_full(issues: List[Issue]) -> Dict[str, Dict[str, Any]]:
    result: Dict[str, Dict[str, Any]] = {}
    if not CITATION_FULL_JSON.exists():
        issues.append(Issue("WARN", rel(CITATION_FULL_JSON), "citation_full.json missing; run vault_index.py", code="CITATION_FULL_MISSING"))
        return result
    try:
        data = json.loads(read_text(CITATION_FULL_JSON))
    except Exception as e:
        issues.append(Issue("ERROR", rel(CITATION_FULL_JSON), f"cannot parse citation_full.json: {e}", code="CITATION_FULL_PARSE"))
        return result

    items: dict[str, Any]
    if isinstance(data, dict):
        if isinstance(data.get("items"), dict):
            items = data["items"]
        elif isinstance(data.get("entries"), dict):
            items = data["entries"]
        else:
            items = {k: v for k, v in data.items() if isinstance(v, dict)}
    else:
        issues.append(Issue("ERROR", rel(CITATION_FULL_JSON), "citation_full.json must be a list or object", code="CITATION_FULL_TYPE"))
        return result

    for key, item in items.items():
        if not isinstance(item, dict):
            continue
        result[str(key)] = item
        path = str(item.get("path") or item.get("argument_path") or "").strip()
        target = str(item.get("argument") or item.get("argument_target") or "").strip()
        if path:
            result[path] = item
        if target:
            result[target] = item
        for alias in item.get("aliases") or []:
            result[str(alias)] = item
    return result


def build_argument_citation_maps(paths: List[Path], issues: List[Issue]) -> tuple[Dict[str, Dict[str, Any]], Dict[str, list[Dict[str, Any]]]]:
    by_target: Dict[str, Dict[str, Any]] = {}
    by_stem: Dict[str, list[Dict[str, Any]]] = {}
    argument_dir = WIKI_DIR / "arguments"
    if not argument_dir.exists():
        return by_target, by_stem

    for path in iter_md_files(argument_dir):
        if is_generated_or_template(path):
            continue
        data = entry_metadata(path)
        if not is_citation_eligible_argument(data):
            continue
        aliases = data.get("citation_aliases") or []
        if not isinstance(aliases, list) or not aliases:
            continue
        base_aliases = expected_citation_aliases_from_meta(data)
        stem = base_aliases[0] if base_aliases else str(aliases[0])
        item = {
            "path": rel(path),
            "target": path.stem,
            "aliases": [str(a) for a in aliases],
            "citation_short": str(aliases[0]),
            "citation_stem": stem,
            "year": str(data.get("year") or "").strip(),
        }
        by_target[path.stem] = item
        by_stem.setdefault(stem, []).append(item)
    return by_target, by_stem


def check_citation_json_consistency(argument_citations: Dict[str, Dict[str, Any]], issues: List[Issue]) -> None:
    if not CITATION_FULL_JSON.exists():
        return
    try:
        data = json.loads(read_text(CITATION_FULL_JSON))
    except Exception:
        return

    raw_items = data.get("items", data) if isinstance(data, dict) else {}
    json_items = [x for x in raw_items.values() if isinstance(x, dict)] if isinstance(raw_items, dict) else []

    json_by_target = {
        str(item.get("argument") or item.get("argument_target") or Path(str(item.get("argument_path") or item.get("path") or "")).stem): item
        for item in json_items
        if (item.get("argument_target") or item.get("argument_path") or item.get("path"))
    }

    for target, fm_item in argument_citations.items():
        item = json_by_target.get(target)
        if not item:
            issues.append(Issue("WARN", fm_item["path"], "citation_full.json missing this Argument; run vault_index.py", code="CITATION_INDEX_STALE"))
            continue
        if [str(a) for a in item.get("aliases", [])] != fm_item["aliases"]:
            issues.append(Issue("WARN", fm_item["path"], "citation_full.json aliases differ from frontmatter; run vault_index.py", code="CITATION_INDEX_ALIAS_MISMATCH"))


def expected_citation_prefix(short: str) -> str:
    return short.strip()


@lru_cache(maxsize=None)
def normalize_citation_alias_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])\s*&\s*(?=[A-ZÀ-ÖØ-Þ])", " & ", text)
    return ENGLISH_AUTHOR_AND_RE.sub(" & ", text)


def has_invalid_english_author_conjunction(text: str) -> bool:
    return fix_english_author_and(text) != text


def fix_english_author_and(text: str) -> str:
    """Use 'and' in narrative displays and '&' in parenthetical displays.

    Canonical citation aliases still use '&'; display style does not change
    the author-year lookup key. Chinese author conjunctions are untouched.
    """
    year = re.search(r"(?:19|20)\d{2}[a-z]?", text)
    if not year:
        return text
    prefix = text[:year.start()]
    narrative = not text.lstrip().startswith(("(", "（")) and prefix.rstrip().endswith(("(", "（"))
    conjunction = " and " if narrative else " & "
    prefix = re.sub(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])(?:\s+and\s+|\s*&\s*|\s*和\s*)(?=[A-ZÀ-ÖØ-Þ])", conjunction, prefix)
    return prefix + text[year.start():]


def citation_display_has_author_year(display: str) -> bool:
    text = re.sub(r"\s+", " ", display).strip()
    m = re.search(r"(?:19|20)\d{2}[a-z]?", text)
    if not m:
        return False
    prefix = text[:m.start()].strip(" \t([{（【,，")
    prefix_key = prefix.strip().lower().rstrip(" .:：")
    if not prefix_key:
        return False
    if re.match(r"^(?:p|pp|ch|chap|chapter)\.?(?:\s*\d+.*)?$", prefix_key):
        return False
    if re.match(r"^第.+[页章節节]$", prefix_key):
        return False
    return any(ch.isalpha() or "\u3400" <= ch <= "\u9fff" for ch in prefix)


def raw_citation_is_reference_fragment(display: str) -> bool:
    """True for fragments of APA inverted-name reference lists, e.g. 'S. N. (2019)'.

    RAW_CITATION_RE cannot include commas in the author part, so inside a
    bibliography line like 'Larsen, S. N. (2019). ...' it matches only the
    initials fragment. Those are references, not in-text citations.
    """
    prefix = re.split(r"[（(]", display, maxsplit=1)[0].strip().rstrip(",， ")
    return bool(re.fullmatch(r"(?:[A-ZÀ-ÖØ-Þ]\.(?:\s*-\s*[A-ZÀ-ÖØ-Þ]\.)?\s*)+", prefix))


@lru_cache(maxsize=None)
def citation_author_year_key(text: str) -> str:
    text = normalize_citation_alias_text(text).strip("()（）[]【】 ")
    year_match = re.search(r"(?:19|20)\d{2}[a-z]?", text)
    if not year_match:
        return ""
    author = text[:year_match.start()].strip(" ,，([（")
    author = normalize_citation_alias_text(author).lower().rstrip(" .")
    return f"{author}|{year_match.group(0).lower()}" if author else ""


_CITATION_SEGMENT_SPLIT_RE = re.compile(r";|[,，]?\s*(?:cited in|quoted in|as cited in|引自|转引自|引用自)\s*", re.IGNORECASE)


def citation_display_matches_aliases(display: str, aliases: List[str]) -> bool:
    """True if the display, or any citation segment inside it, matches the target.

    Composite displays such as '(Moisio, 2018, cited in Parreira do Amaral, 2022)'
    or '(Grundy, 1987; Darwish, 2009)' match when one segment names the target."""
    if _citation_display_matches_aliases_single(display, aliases):
        return True
    segments = [s.strip(" ()（）") for s in _CITATION_SEGMENT_SPLIT_RE.split(display)]
    if len(segments) > 1:
        return any(seg and _citation_display_matches_aliases_single(seg, aliases) for seg in segments)
    return False


def _citation_display_matches_aliases_single(display: str, aliases: List[str]) -> bool:
    display = display.strip()
    normalized_display = normalize_citation_alias_text(display)

    author_year_key = citation_author_year_key

    display_key = author_year_key(display)
    for alias in aliases:
        alias = str(alias).strip()
        if not alias:
            continue
        normalized_alias = normalize_citation_alias_text(alias)
        if display_key and display_key == author_year_key(alias):
            return True
        if normalized_display == normalized_alias or normalized_display.startswith(normalized_alias + ","):
            return True
        if normalized_alias.endswith(")") and normalized_display.startswith(normalized_alias[:-1] + ","):
            return True
    return False


def citation_identity(display: str, target: str = "") -> str:
    display = normalize_citation_alias_text(display).strip()
    year_match = re.search(r"(?:19|20)\d{2}[a-z]?", display)
    if not year_match:
        return ""

    author = display[:year_match.start()].strip(" \t([{（【,，")
    author = normalize_citation_alias_text(author).lower().rstrip(" .,，")
    source = author or target.strip().lower()
    if not source:
        return ""

    tail = display[year_match.end():]
    locator_match = re.search(r"\bpp?\.\s*([^)\]）]+)", tail, flags=re.IGNORECASE)
    locator = ""
    if locator_match:
        locator = re.sub(r"\s+", "", locator_match.group(0).lower())
        locator = locator.replace("，", ",").replace("–", "-")

    return f"{source}|{year_match.group(0).lower()}|{locator}"


def citation_units(text: str) -> List[Tuple[str, int, str]]:
    """Return paragraph and callout units while preserving offsets."""
    lines = text.splitlines(keepends=True)
    units: List[Tuple[str, int, str]] = []
    offsets: List[int] = []
    pos = 0
    for line in lines:
        offsets.append(pos)
        pos += len(line)

    callout_start_re = re.compile(r"^\s*(?:>\s*)+\[![^\]\n]+\]")
    quote_line_re = re.compile(r"^\s*>")
    standalone_block_re = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+|^\s*\||^\s*#{1,6}\s+")
    i = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue

        start = i
        if callout_start_re.match(lines[i]):
            i += 1
            while i < len(lines) and quote_line_re.match(lines[i]):
                i += 1
            # Inside a callout, each list item / table row / quoted paragraph is
            # its own unit, matching how lists outside callouts are split.
            sub_start = start
            for j in range(start + 1, i):
                inner = re.sub(r"^\s*(?:>\s?)+", "", lines[j])
                if not inner.strip() or standalone_block_re.match(inner) or inner.startswith("**"):
                    if sub_start < j:
                        units.append(("".join(lines[sub_start:j]), offsets[sub_start], "callout"))
                    sub_start = j
            if sub_start < i:
                units.append(("".join(lines[sub_start:i]), offsets[sub_start], "callout"))
            continue

        i += 1
        while i < len(lines):
            if not lines[i].strip() or callout_start_re.match(lines[i]):
                break
            if standalone_block_re.match(lines[start]) or standalone_block_re.match(lines[i]):
                break
            i += 1
        units.append(("".join(lines[start:i]), offsets[start], "paragraph"))

    return units


def check_duplicate_citations(
    path: Path,
    text: str,
    data: Optional[Dict[str, Any]],
    issues: List[Issue],
) -> None:
    if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path) or not is_wiki_entry_path(path):
        return

    _, body, body_start_line = split_frontmatter(text)
    scan = remove_h2_sections(body, ["来源", "Sources", "Source"])
    scan = mask_markdown_code(scan)

    def mask_comment(m: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))

    scan = re.sub(r"%%.*?%%", mask_comment, scan, flags=re.DOTALL)
    scan = re.sub(r"<!--.*?-->", mask_comment, scan, flags=re.DOTALL)

    for unit, unit_offset, unit_kind in citation_units(scan):
        occurrences: Dict[str, List[Tuple[int, str]]] = {}
        masked_unit = list(unit)

        def on_table_row(pos: int) -> bool:
            line_start = unit.rfind("\n", 0, pos) + 1
            return bool(_TABLE_ROW_RE.match(unit[line_start:pos + 1]))

        for match in WIKILINK_RE.finditer(unit):
            raw = match.group(1)
            target = extract_wikilink_target(raw)
            display = raw.split("|", 1)[1].strip() if "|" in raw else ""
            display = display.lstrip("\\").strip()
            if (target.startswith("Argument_") and citation_display_has_author_year(display)
                    and not on_table_row(match.start()) and not is_narrative_citation(display)):
                key = citation_identity(display, target)
                if key:
                    occurrences.setdefault(key, []).append((match.start(), display))
            for idx in range(match.start(), match.end()):
                if masked_unit[idx] != "\n":
                    masked_unit[idx] = " "

        without_links = "".join(masked_unit)
        for match in RAW_CITATION_RE.finditer(without_links):
            display = match.group(1).strip()
            if not citation_display_text(display):
                continue
            if raw_citation_is_reference_fragment(display):
                continue
            if on_table_row(match.start()) or is_narrative_citation(display):
                continue
            key = citation_identity(display)
            if key:
                occurrences.setdefault(key, []).append((match.start(), display))

        if data and data.get("type") == "argument":
            for match in PAGE_ONLY_REF_RE.finditer(without_links):
                if on_table_row(match.start()):
                    continue
                display = match.group(1).strip()
                locator = re.sub(r"\s+", "", display.lower())
                locator = locator.strip("()（）").replace("，", ",").replace("–", "-")
                key = f"current-argument-source|{locator}"
                occurrences.setdefault(key, []).append((match.start(), display))

        for repeated in occurrences.values():
            if len(repeated) < 2:
                continue
            repeated.sort(key=lambda item: item[0])
            duplicate_pos, display = repeated[1]
            issues.append(Issue(
                "WARN",
                rel(path),
                f"the same citation and page appears {len(repeated)} times in one {unit_kind}; keep it once: {display!r}",
                line=line_of_pos(scan, unit_offset + duplicate_pos, body_start_line),
                code="CITATION_DUPLICATE_IN_UNIT",
            ))


def citation_line_language(text: str) -> str:
    visible = re.sub(r"\[\[[^|\]]+\|([^\]]+)\]\]", r"\1", text)
    visible = re.sub(r"\[\[([^\]]+)\]\]", r"\1", visible)
    visible = re.sub(r"[*_`>#\[\]()（）]", " ", visible)
    cjk_count = len(re.findall(r"[\u3400-\u9fff]", visible))
    latin_count = len(re.findall(r"[A-Za-z]", visible))
    if cjk_count and cjk_count * 2 >= latin_count:
        return "zh"
    if latin_count >= 8 and latin_count > cjk_count * 2:
        return "en"
    return ""


def check_citation_card_language_order(path: Path, text: str, issues: List[Issue]) -> None:
    if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path) or not is_wiki_entry_path(path):
        return

    _, body, body_start_line = split_frontmatter(text)
    scan = mask_markdown_code(body)
    for unit, unit_offset, unit_kind in citation_units(scan):
        if unit_kind != "callout":
            continue
        lines = unit.splitlines(keepends=True)
        if not lines or not re.match(r"^\s*(?:>\s*)+\[!citation-card\]", lines[0], flags=re.IGNORECASE):
            continue

        content: List[Tuple[int, str, str]] = []
        relative_offset = len(lines[0])
        for line in lines[1:]:
            visible = re.sub(r"^\s*(?:>\s*)+", "", line).strip()
            language = citation_line_language(visible) if visible else ""
            if language:
                content.append((relative_offset, visible, language))
            relative_offset += len(line)

        first_english = next((item for item in content if item[2] == "en"), None)
        first_chinese = next((item for item in content if item[2] == "zh"), None)
        if not first_english or not first_chinese or first_chinese[0] < first_english[0]:
            continue

        issues.append(Issue(
            "ERROR",
            rel(path),
            "citation-card must place the Chinese translation above the English original",
            line=line_of_pos(scan, unit_offset + first_english[0], body_start_line),
            code="CITATION_CARD_LANGUAGE_ORDER",
        ))


def strip_existing_wikilinks(text: str) -> str:
    def repl(m: re.Match) -> str:
        return " " * len(m.group(0))
    text = WIKILINK_RE.sub(repl, text)
    text = EMBED_RE.sub(repl, text)
    return text


_CITATION_LINKER: Any = None
_CITATION_LINKER_LOOKUP: Optional[Dict[str, Any]] = None
_NEW_ARG_LINK_RE = re.compile(r"\[\[(Argument_[^\]|\\\n]+)\\?\|([^\]\n]+)\]\]")


def citation_linker_suggestions(path: Path, text: str) -> List[Tuple[int, str]]:
    """(line, display) for each citation link wiki_linker.py would add."""
    global _CITATION_LINKER, _CITATION_LINKER_LOOKUP
    if _CITATION_LINKER is None:
        scripts_dir = str(Path(__file__).resolve().parent)
        if scripts_dir not in sys.path:
            sys.path.insert(0, scripts_dir)
        import wiki_linker  # noqa: PLC0415
        _CITATION_LINKER = wiki_linker
    cl = _CITATION_LINKER
    if _CITATION_LINKER_LOOKUP is None:
        _CITATION_LINKER_LOOKUP = cl.load_citation_lookup() if cl.CITATION_FULL_JSON.exists() else {}
    if not _CITATION_LINKER_LOOKUP:
        return []
    stats = {"linked_parenthetical": 0, "linked_narrative": 0, "fixed_display": 0}
    linked = cl.link_citations(text, _CITATION_LINKER_LOOKUP, stats, [], path)
    if linked == text:
        return []
    out: List[Tuple[int, str]] = []
    for idx, (old, new) in enumerate(zip(text.split("\n"), linked.split("\n")), start=1):
        if old == new:
            continue
        before = [m.group(2) for m in _NEW_ARG_LINK_RE.finditer(old)]
        for m in _NEW_ARG_LINK_RE.finditer(new):
            display = m.group(2)
            if display in before:
                before.remove(display)
            else:
                out.append((idx, display))
    return out


def check_citation_links(path: Path, text: str, data: Optional[Dict[str, Any]], argument_citations: Dict[str, Dict[str, Any]], issues: List[Issue]) -> None:
    if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path):
        return
    if not is_wiki_entry_path(path):
        return

    fm, body, body_start_line = split_frontmatter(text)
    if fm is None:
        body = text
        body_start_line = 1

    body_no_sources = remove_h2_sections(body, ["来源", "Sources", "Source"])
    scan = strip_code_blocks(body_no_sources)

    # Check existing citation-style Argument links.
    for m in WIKILINK_RE.finditer(scan):
        raw = m.group(1)
        target = extract_wikilink_target(raw)
        if not target or target not in argument_citations:
            continue
        display = raw.split("|", 1)[1].strip() if "|" in raw else ""
        aliases = argument_citations[target]["aliases"]
        if is_non_argument_semantic_entry(data) and not citation_display_has_author_year(display):
            expected = aliases[0] if aliases else f"{target.replace('Argument_', '')}, YEAR"
            issues.append(Issue("WARN", rel(path), f"non-Argument entries should cite Argument links with author-year display, not page-only display: {display!r}; expected like {expected!r}", line=line_of_pos(body_no_sources, m.start(), body_start_line), code="ARGUMENT_LINK_AUTHOR_YEAR_MISSING"))
        if display and citation_display_text(display):
            if has_invalid_english_author_conjunction(display):
                issues.append(Issue("WARN", rel(path), f"English two-author citation conjunction does not match narrative/parenthetical style: {display!r} -> {fix_english_author_and(display)!r}", line=line_of_pos(body_no_sources, m.start(), body_start_line), code="CITATION_ENGLISH_AND"))
            if not citation_display_matches_aliases(display, aliases):
                issues.append(Issue("WARN", rel(path), f"citation link display {display!r} does not match target citation_aliases {aliases!r}", line=line_of_pos(body_no_sources, m.start(), body_start_line), code="CITATION_LINK_TARGET_MISMATCH"))

    # Warn about raw, unlinked APA short citations.
    without_links = strip_existing_wikilinks(scan)
    for m in RAW_CITATION_RE.finditer(without_links):
        txt = m.group(1).strip()
        # Avoid matching page-only references and obvious template/examples.
        if not citation_display_text(txt):
            continue
        if raw_citation_is_reference_fragment(txt):
            continue
        if has_invalid_english_author_conjunction(txt):
            issues.append(Issue("WARN", rel(path), f"English two-author citation conjunction does not match narrative/parenthetical style: {txt!r} -> {fix_english_author_and(txt)!r}", line=line_of_pos(body_no_sources, m.start(), body_start_line), code="CITATION_ENGLISH_AND"))

    # Unlinked citations: ask wiki_linker's APA engine what it would link, so lint and
    # the auto-linker (run by vault_index) can never disagree.
    for line_no, display in citation_linker_suggestions(path, text):
        issues.append(Issue("WARN", rel(path), f"APA short citation is not linked to an Argument (run scripts/vault_index.py to auto-link): {display}", line=line_no, code="CITATION_UNLINKED"))

    check_external_citation_identity(path, text, issues)


# EXTERNAL_CITATION_IDENTITY is INFO. Existing entries already contain unlinked
# short citations with no DOI or title. A WARN would become a new finding on
# every touched old file and block sync. Incremental lint still lists a citation
# that was not in the baseline file. --full collapses the backlog to one line.
_EXTERNAL_IDENTITY_LOOKUP: Optional[Dict[str, Dict[str, Any]]] = None


def external_identity_message(key: str) -> str:
    return (
        f"库外引用 {key!r} 还没有 DOI、ISBN 或篇名。"
        "可在来源原文的参考文献中补记，写入 citation/external_identities.json。"
    )


def external_identity_lookup() -> Dict[str, Dict[str, Any]]:
    global _EXTERNAL_IDENTITY_LOOKUP
    if _EXTERNAL_IDENTITY_LOOKUP is not None:
        return _EXTERNAL_IDENTITY_LOOKUP
    result: Dict[str, Dict[str, Any]] = {}
    if CITATION_EXTERNAL_JSON.exists():
        try:
            data = json.loads(CITATION_EXTERNAL_JSON.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            data = {}
        items = data.get("items") if isinstance(data, dict) else None
        by_identity = data.get("by_identity") if isinstance(data, dict) else None
        if isinstance(items, dict):
            for alias, entry in items.items():
                if isinstance(entry, dict):
                    result.setdefault(str(alias), entry)
            if isinstance(by_identity, dict):
                for key, canonical in by_identity.items():
                    entry = items.get(canonical)
                    if isinstance(entry, dict):
                        result[str(key)] = entry
    _EXTERNAL_IDENTITY_LOOKUP = result
    return result


def check_external_citation_identity(path: Path, text: str, issues: List[Issue]) -> None:
    if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path) or not is_wiki_entry_path(path):
        return
    lookup = external_identity_lookup()
    if not lookup:
        return
    scripts_dir = str(Path(__file__).resolve().parent)
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import citation_index

    for key, offset in citation_index.first_sightings(text):
        entry = lookup.get(key)
        if not entry:
            continue
        if str(entry.get("doi") or "").strip() or str(entry.get("isbn") or "").strip() or str(entry.get("title") or "").strip():
            continue
        issues.append(Issue(
            "INFO",
            rel(path),
            external_identity_message(key),
            line=line_of_pos(text, offset),
            code=EXTERNAL_CITATION_IDENTITY,
        ))


def collapse_external_identity_issues(issues: List[Issue]) -> List[Issue]:
    """--full keeps one backlog line instead of one INFO per old citation."""
    kept: List[Issue] = []
    count = 0
    for issue in issues:
        if issue.code == EXTERNAL_CITATION_IDENTITY:
            count += 1
            continue
        kept.append(issue)
    if count:
        kept.append(Issue(
            "INFO",
            rel(CITATION_DIR / "external_identities.json"),
            f"库外引用有 {count} 处还没有 DOI、ISBN 或篇名。"
            "这是存量提示，不阻挡已有条目同步；补记写入 citation/external_identities.json。",
            code=EXTERNAL_CITATION_IDENTITY,
        ))
    return kept


# ARGUMENT_RAW_SELF_ALIAS: an Argument page citing its own source as raw text,
# e.g. "(Ball, 2008, p. 12)". Books and reports become page locators. Journal
# articles drop the self-cite, including its pages. A same-year sibling such as
# "(Ball, 2008b)" is a different work and is left for the citation linker.
# ARGUMENT_SELF_CITATION only sees wikilinks, so this raw form slipped through.
PAREN_GROUP_RE = re.compile(r"[（(]([^（）()\n]{2,300})[）)]")
PAGE_LOCATOR_RE = re.compile(r"^(pp?)\.?\s*(\d[\d\s,–—-]*\d|\d)$", re.IGNORECASE)
SELF_PART_OF_RE = re.compile(r"^part_of:\s*[\"']?\[\[([^\]|#]+)", re.M)


def _norm_citation_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    return re.sub(r"\s+", " ", value).strip().casefold()


def argument_self_parenthetical_aliases(path: Path, fm: Optional[str], data: Dict[str, Any], argument_citations: Dict[str, Dict[str, Any]]) -> Set[str]:
    """Parenthetical ("Author, Year") forms of this page's own citation:
    its citation_aliases, its index entry, and the part_of parent it inherits from."""
    aliases: Set[str] = set()
    own = data.get("citation_aliases")
    if isinstance(own, list):
        aliases.update(a for a in own if isinstance(a, str))
    targets = {path.stem}
    m = SELF_PART_OF_RE.search(fm or "")
    if m:
        targets.add(m.group(1).strip())
    for target in targets:
        info = argument_citations.get(target) or {}
        aliases.update(a for a in info.get("aliases", []) if isinstance(a, str))
    # Narrative forms ("Ball (2008)") are not parenthetical citations.
    # Keep a/b/c on the year. "Author, 2008" is not a self-cite of "Author, 2008a",
    # and citation_stem is the unsuffixed form, so it is not added here.
    return {_norm_citation_text(a) for a in aliases if a.strip() and not re.search(r"[（(）)]", a)}


SELF_PREFIX_RE = re.compile(r"^(?:据|基于|根据|nach|based on|adapted from)\s*", re.IGNORECASE)
CITED_IN_RE = re.compile(r"[,，]?\s*(?:(?:as\s+)?(?:cited|quoted)\s+in|引用见|转引自?|引自)\s*", re.IGNORECASE)


def _self_alias_locator(segment: str, aliases: Set[str]) -> Optional[str]:
    r"""'' if the segment is a bare self alias, the page locator if alias + pages, else None.
    A leading "|" / "\|" is residue of a removed self-wikilink "[[Argument_…|";
    "据 / 基于 / Nach / Adapted from …" prefixes still cite this source."""
    norm = _norm_citation_text(re.sub(r"^[\s\\|]+", "", segment))
    norm = SELF_PREFIX_RE.sub("", norm)
    for alias in aliases:
        if norm == alias:
            return ""
        if norm.startswith(alias) and norm[len(alias):len(alias) + 1] == ",":
            loc = PAGE_LOCATOR_RE.match(norm[len(alias) + 1:].strip())
            if loc:
                pages = re.sub(r"\s+", "", loc.group(2)).replace("-", "–").replace("—", "–")
                pages = re.sub(r",(?=\d)", ", ", pages)
                return f"{loc.group(1).lower()}. {pages}"
    return None


def self_alias_rewrite(group: str, aliases: Set[str], drop_pages: bool = False) -> Optional[Tuple[str, str]]:
    """Rewrite a parenthetical group that cites this Argument's own source.

    Returns (replacement, kind) or None. The replacement keeps the original
    bracket style; "" means the parenthetical should be removed.
      self      (Ball, 2008, p. 3)                       -> (p. 3)   books and reports
      journal   (Ball, 2008a, p. 3)                      -> delete    drop_pages
      mixed     (Law, 1992; Ball, 2008, p. 3)            -> (Law, 1992)
      cited_in  (Law, 1992, p. 9; cited in Ball, 2008)   -> (Law, 1992, p. 9)
    A different work by the same author and year ("Ball, 2008b") does not match
    the suffixed alias and is left unchanged.
    """
    opening, closing = ("（", "）") if group.startswith("（") else ("(", ")")
    segments = re.split(r"[;；]", group[1:-1])
    kept: List[str] = []
    pages: List[str] = []
    cited_in = mixed_self = False
    for seg in segments:
        loc = _self_alias_locator(seg, aliases)
        if loc is not None:
            mixed_self = True
            if loc:
                pages.append(loc)
            continue
        cut = None
        for m in CITED_IN_RE.finditer(seg):
            if _self_alias_locator(seg[m.end():], aliases) is not None:
                cut = m
                break
        if cut is not None:
            cited_in = True
            original = seg[:cut.start()].strip()
            if original:
                kept.append(original)
            continue
        kept.append(seg.strip())
    if not (mixed_self or cited_in):
        return None
    sep = "；" if "；" in group and "; " not in group else "; "
    if cited_in:
        # Cite the original source directly; this source's pages are dropped.
        return (f"{opening}{sep.join(kept)}{closing}" if kept else "", "cited_in")
    if not kept:
        if drop_pages:
            return ("", "self")
        return (f"{opening}{'; '.join(pages)}{closing}" if pages else "", "self")
    # Mixed with other sources: keep the others; this source's pages are dropped.
    return (f"{opening}{sep.join(kept)}{closing}", "mixed")


def is_journal_argument(path: Path, data: Optional[Dict[str, Any]]) -> bool:
    """Journal article arguments omit self-citation, including page locators."""
    if not is_argument_entry(data) or "journal-articles" not in path.parts:
        return False
    markers = [
        str((data or {}).get(key) or "").strip()
        for key in ("argument_kind", "subtype", "publication_type")
    ]
    present = [item for item in markers if item]
    return bool(present) and all(item == "journal-article" for item in present)


# A journal self-locator is a parenthetical that contains only this article's
# page, table, figure, or footnote tokens. "p=0.011" and "p<0.05" are statistics.
_JOURNAL_LOCATOR_TOKEN_RE = re.compile(
    r"(?:(?<![\w.])pp?\.\s*\d[\d\s,，、–—\-]*"
    r"|tables?\s*\d+[A-Za-z]?"
    r"|figures?\s*\d+[A-Za-z]?"
    r"|figs?\.\s*\d+[A-Za-z]?"
    r"|fn\.?\s*\d+"
    r"|footnotes?\s*\d+"
    r"|脚注\s*\d+"
    r"|图表\s*\d+"
    r"|表\s*\d+"
    r"|图\s*\d+)",
    re.IGNORECASE,
)
_JOURNAL_LOCATOR_GLUE_RE = re.compile(r"[\s,，;；、.。:：\-–—()（）]+")
_STAT_P_RE = re.compile(r"(?<![\w.])p\s*[=<>≤≥]", re.IGNORECASE)


def is_journal_self_page_group(group: str) -> bool:
    """True when the whole parenthetical only locates the current journal article."""
    if len(group) < 3 or group[0] not in "（(" or group[-1] not in "）)":
        return False
    inner = group[1:-1]
    if _STAT_P_RE.search(inner) or not _JOURNAL_LOCATOR_TOKEN_RE.search(inner):
        return False
    rest = _JOURNAL_LOCATOR_GLUE_RE.sub("", _JOURNAL_LOCATOR_TOKEN_RE.sub(" ", inner))
    return rest == ""


def check_argument_raw_self_alias(path: Path, text: str, data: Optional[Dict[str, Any]], argument_citations: Dict[str, Dict[str, Any]], issues: List[Issue]) -> None:
    if not is_argument_entry(data) or not is_wiki_entry_path(path):
        return
    if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path):
        return
    fm, body, body_start_line = split_frontmatter(text)
    if fm is None:
        return
    aliases = argument_self_parenthetical_aliases(path, fm, data or {}, argument_citations)
    if not aliases:
        return
    journal = is_journal_argument(path, data)
    scan = strip_existing_wikilinks(mask_markdown_code(mask_h2_sections_preserve(body, ["来源", "Sources", "Source"])))
    for m in PAREN_GROUP_RE.finditer(scan):
        result = self_alias_rewrite(m.group(0), aliases, drop_pages=journal)
        if result is None:
            continue
        replacement, kind = result
        if kind == "cited_in":
            advice = f"转引改为直接引用原来源 {replacement}" if replacement else "转引改为直接引用原来源"
        elif journal and kind == "self":
            advice = f"删除本篇自引，保留 {replacement}" if replacement else "删除该括注（期刊论证不记本篇自引）"
        elif replacement:
            advice = f"简化为 {replacement}"
        else:
            advice = "删除该括注（本文献无需作者年份）"
        if "|" in m.group(1):
            advice += "；括注内残留的 | 来自已删除的自引链接，一并去掉"
        issues.append(Issue(
            "WARN", rel(path),
            f"Argument 页以裸文本括注引用了本文献 {m.group(0)!r}；{advice}",
            line=line_of_pos(body, m.start(), body_start_line),
            code="ARGUMENT_RAW_SELF_ALIAS",
        ))


def check_journal_self_pages(path: Path, text: str, data: Optional[Dict[str, Any]], issues: List[Issue]) -> None:
    if not is_journal_argument(path, data) or not is_wiki_entry_path(path):
        return
    if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path):
        return
    fm, body, body_start_line = split_frontmatter(text)
    if fm is None:
        return
    scan = strip_existing_wikilinks(mask_markdown_code(mask_h2_sections_preserve(body, ["来源", "Sources", "Source"])))
    for m in PAREN_GROUP_RE.finditer(scan):
        if not is_journal_self_page_group(m.group(0)):
            continue
        issues.append(Issue(
            "WARN", rel(path),
            f"期刊论证不记本篇页码或图表脚注定位 {m.group(0)!r}；删除该括注",
            line=line_of_pos(body, m.start(), body_start_line),
            code="JOURNAL_SELF_PAGE",
        ))


def check_journal_naming(path: Path, data: Dict[str, Any], issues: List[Issue]) -> None:
    from citation_index import article_problem, is_legacy, load_registry
    try:
        registry = load_registry()
    except (OSError, ValueError):
        return  # Report the registry error once at vault level.
    problem = article_problem(path, data, registry)
    if problem and not is_legacy(path, data):
        issues.append(Issue("ERROR", rel(path), problem, code="JOURNAL_NAMING"))



ACADEMIC_BUZZWORDS = (
    "跃迁", "闭环", "沉淀", "托举", "内核", "跃升", "底座", "破局", "颗粒度",
    "耦合", "统摄", "统合", "链路", "蜕变", "坍塌", "杠杆", "闭合",
    "靶向", "解耦", "归约", "收敛", "规约", "收束",
)
NEGATIVE_CONTRAST_MARKERS = ("不是", "并非", "绝非", "不在于", "而是", "而在于")
SELF_REFERENCE_MARKERS = ("论文", "本文", "本章", "作者", "原文")
WRITING_REMINDER_CODES = {"ACADEMIC_BUZZWORD", "ACADEMIC_NEGATIVE_CONTRAST", "ACADEMIC_SELF_REFERENCE"}
SELF_REFERENCE_REMINDER = (
    "去掉自我说明性文字，避免以论文、本文、本章、作者或原文作为常规叙述主语；"
    "直接陈述具体判断、知识对象、机制、证据或结论，必要出处放在引用中。"
    "需区分自我说明与实质讨论研究文献、章节或作者的必要表达，不机械删除。"
)
BUZZWORD_REMINDER = (
    "除非具有明确的概念内涵、切合具体语境且确有表达必要，否则避免使用此类互联网黑话和泛化的抽象词汇，"
    "优先采用准确、具体、自然的学术表达。"
)
NEGATIVE_CONTRAST_REMINDER = (
    "使用否定转折句式前，必须检查所否定的观点是否真实存在、前后概念是否构成实质性对立、"
    "是否涉及真实的学术争论，以及转折是否带来明确的信息增量；"
    "若存在虚构论争对象、制造虚假对立或缺乏实质性论证的情况，应改用直接的肯定式表述。"
)

# Each pending writing item prints only its ID, hits and context; the rule
# text is printed once per code after the summary (writing_review_legend).
WRITING_REMINDERS = {
    "ACADEMIC_BUZZWORD": BUZZWORD_REMINDER,
    "ACADEMIC_NEGATIVE_CONTRAST": NEGATIVE_CONTRAST_REMINDER,
    "ACADEMIC_SELF_REFERENCE": SELF_REFERENCE_REMINDER,
}
WRITING_REVIEW_ACTION = "必须修改表达，或在 scripts/writing_exceptions.json 的本条目路径下添加经审查批准的 ID；未处理会阻断检查。"


def writing_review_legend(codes: Iterable[str]) -> List[str]:
    present = set(codes)
    lines = [f"  [{code}] {WRITING_REMINDERS[code]}" for code in WRITING_REMINDERS if code in present]
    if lines:
        lines.append(f"  每个待审查项：{WRITING_REVIEW_ACTION}")
    return lines


def academic_prose_scan(text: str) -> str:
    """Keep visible prose and source offsets; ignore code, comments and link targets."""
    def blank(match: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", match.group(0))

    # Match fence lengths, quoted fences and unfinished blocks without letting
    # delimiters inside one code block open a different block.
    lines = []
    fence = ""
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^[ \t]*(?:>[ \t]*)*(?P<fence>`{3,}|~{3,})(?P<tail>[^\n]*)", line)
        if fence:
            lines.append(re.sub(r"[^\n]", " ", line))
            if marker and marker['fence'][0] == fence[0] and len(marker['fence']) >= len(fence) and not marker['tail'].strip():
                fence = ""
        elif marker and (marker['fence'][0] == "~" or "`" not in marker['tail']):
            fence = marker['fence']
            lines.append(re.sub(r"[^\n]", " ", line))
        else:
            lines.append(line)
    scan = "".join(lines)
    scan = re.sub(r"<!--.*?-->|%%.*?%%", blank, scan, flags=re.S)
    scan = re.sub(r"(?P<ticks>`+)(?!`)[^\n]*?(?P=ticks)(?!`)", blank, scan)
    scan = mask_h2_sections_preserve(scan, ["来源", "Sources", "Source", "References", "参考文献"])
    # Generated data blocks (MetaX / EEF modules) are tables, not prose.
    scan = re.sub(r"^>[ \t]*\[!(?:metax|eef)[\w-]*(?:\|[^\]]*)?\][^\n]*(?:\n>[^\n]*)*", blank, scan, flags=re.M)
    scan = EMBED_RE.sub(blank, scan)
    scan = re.sub(r"!\[[^\]\n]*\]\([^\n]*?\)", blank, scan)

    def visible_label(match: re.Match[str]) -> str:
        raw = match.group(0)
        if raw.startswith("[["):
            inner = match.group(1)
            sep = re.search(r"\\?\|", inner)
            start = match.start(1) - match.start() + (sep.end() if sep else 0)
            end = match.end(1) - match.start()
        else:
            start, end = match.start(1) - match.start(), match.end(1) - match.start()
        return re.sub(r"[^\n]", " ", raw[:start]) + raw[start:end] + re.sub(r"[^\n]", " ", raw[end:])

    scan = WIKILINK_RE.sub(visible_label, scan)
    scan = MD_LINK_RE.sub(visible_label, scan)
    scan = re.sub(r"https?://[^\s<>]+|<[^>\n]+>", blank, scan)
    scan = re.sub(r"\$\$[\s\S]*?\$\$|(?<!\\)\$[^\n$]+(?<!\\)\$", blank, scan)
    return scan



WRITING_EXCEPTIONS_PATH = ROOT / "scripts" / "writing_exceptions.json"


def check_link_exceptions(issues: List[Issue]) -> None:
    """Validate the small registry even when notes are outside incremental scope."""
    from wiki_linker import load_link_exceptions, link_exception_sentences, link_exception_body
    registry_path = ROOT / "scripts/link_exceptions.json"
    try:
        registry = load_link_exceptions(registry_path)
        for name, records in registry.items():
            path = ROOT / name
            units = [s for s, _, _ in link_exception_sentences(link_exception_body(path.read_text(encoding="utf-8")))]
            if not is_wiki_entry_path(path) or not entry_metadata(path):
                raise ValueError(f"链接例外所在文件必须是正式 wiki 条目: {name}")
            for record in records:
                if units.count(record["sentence"]) != 1:
                    raise ValueError(f"链接例外句子已失效或不唯一: {name}；运行 exceptions-clean 或改写区分")
                target = ROOT / record["target"]
                meta = entry_metadata(target) if target.is_file() else None
                if not meta or meta.get("type") not in {"concept", "theory", "method", "instrument", "person", "fact"}:
                    raise ValueError(f"链接例外目标必须是现有普通知识条目: {record['target']}")
    except (OSError, ValueError) as exc:
        issues.append(Issue("ERROR", rel(registry_path), str(exc), code="LINK_EXCEPTION_INVALID"))


@lru_cache(maxsize=1)
def load_writing_exceptions() -> Dict[str, List[str]]:
    """Read approved expression exceptions; never store them in note YAML."""
    if not WRITING_EXCEPTIONS_PATH.exists():
        return {}

    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate writing exception key: {key!r}")
            result[key] = value
        return result

    data = json.loads(WRITING_EXCEPTIONS_PATH.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)
    if not isinstance(data, dict):
        raise ValueError("例外表必须是条目相对路径到审查 ID 列表的 JSON 对象。")
    for name, reviews in data.items():
        path = Path(name)
        if (not name.startswith("wiki/") or "\\" in name or path.is_absolute()
                or ".." in path.parts or path.suffix != ".md"
                or path.as_posix() != name or name != unicodedata.normalize("NFC", name) or not isinstance(reviews, list)):
            raise ValueError(f"无效审查条目路径或 ID 列表：{name!r}")
    return data


def check_writing_exceptions(issues: List[Issue]) -> None:
    """Validate records even when their notes are outside the incremental scope."""
    load_writing_exceptions.cache_clear()
    try:
        registry = load_writing_exceptions()
    except (OSError, ValueError) as exc:
        issues.append(Issue("ERROR", rel(WRITING_EXCEPTIONS_PATH), str(exc), code="ACADEMIC_REVIEW_INVALID"))
        return
    for name in registry:
        path = ROOT / name
        if not path.is_file():
            issues.append(Issue("ERROR", rel(WRITING_EXCEPTIONS_PATH), f"审查对应条目已移动或删除：{name}", code="ACADEMIC_REVIEW_STALE"))
            continue
        if not is_wiki_entry_path(path):
            issues.append(Issue("ERROR", rel(WRITING_EXCEPTIONS_PATH), f"审查记录必须指向正式 wiki 条目：{name}", code="ACADEMIC_REVIEW_INVALID"))
            continue
        metadata = entry_metadata(path)
        if not metadata or metadata.get("type") not in VALID_TYPES - {"source"}:
            issues.append(Issue("ERROR", rel(WRITING_EXCEPTIONS_PATH), f"审查对应文件缺少有效条目类型：{name}", code="ACADEMIC_REVIEW_INVALID"))
            continue
        findings: List[Issue] = []
        check_academic_language(path, read_text(path), metadata, findings)
        issues.extend(issue for issue in findings if issue.severity == "ERROR")


def writing_exception_changed_notes() -> List[Path]:
    """Recheck affected notes when exceptions are added, edited or removed."""
    name = rel(WRITING_EXCEPTIONS_PATH)
    previous = git_files_at_head([name]).get(name)
    try:
        current = WRITING_EXCEPTIONS_PATH.read_text(encoding="utf-8") if WRITING_EXCEPTIONS_PATH.exists() else None
    except OSError:
        return []  # The registry validator reports unreadable files.
    if current == previous:
        return []
    names = set()
    for raw in (previous, current):
        try:
            registry = json.loads(raw) if raw is not None else {}
        except ValueError:
            continue
        if not isinstance(registry, dict):
            continue
        for key in registry:
            path = Path(key)
            if (key.startswith("wiki/") and "\\" not in key and ".." not in path.parts
                    and path.as_posix() == key and path.suffix == ".md"
                    and key == unicodedata.normalize("NFC", key) and (ROOT / path).is_file()):
                names.add(key)
    return [ROOT / key for key in sorted(names)]


_REVIEW_LINK_DISPLAY_RE = re.compile(r"\[\[([^\]|\\\n]+)(?:\\?\|[^\]\n]*)?\]\]")


def normalize_review_line(line: str) -> str:
    """The source line a review is bound to, with wikilink display text removed.

    `[[Target|display]]` -> `[[Target]]`, so mechanical display rewrites
    (citation suffixes, APA author forms, alias pipes) keep an approved review
    valid while any change to the prose itself still invalidates it.
    """
    return _REVIEW_LINK_DISPLAY_RE.sub(lambda m: f"[[{m.group(1).strip()}]]", line.strip())


def writing_review_id(code: str, location: str, original_line: str) -> str:
    """Bind each review to its rule, prose/summary location and source line (link displays ignored)."""
    payload = json.dumps([code, location, normalize_review_line(original_line)], ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def check_academic_language(path: Path, text: str, data: Optional[Dict[str, Any]], issues: List[Issue]) -> None:
    """Require edits or a context-bound approved exception for each new match."""
    if not is_wiki_entry_path(path) or not data or data.get("type") not in VALID_TYPES - {"source"}:
        return
    fm, body, first_line = split_frontmatter(text)
    review_line = None
    if "writing_reviews" in data or "writing_exceptions" in data:
        issues.append(Issue("ERROR", rel(path), "写作审查记录不得写入条目 YAML；请移至 scripts/writing_exceptions.json。", code="ACADEMIC_REVIEW_INVALID"))
    try:
        reviews = load_writing_exceptions().get(unicodedata.normalize("NFC", rel(path)), [])
    except (OSError, ValueError):
        reviews = []  # The vault-level registry check reports malformed JSON.
    valid_reviews = set()
    for review_id in reviews:
        valid = isinstance(review_id, str) and bool(re.fullmatch(r"[0-9a-f]{16}", review_id))
        valid = valid and review_id not in valid_reviews
        if not valid:
            issues.append(Issue(
                "ERROR", rel(path),
                f"scripts/writing_exceptions.json 的 {rel(path)} / {review_id} 无效：必须是未重复的 16 位小写十六进制审查 ID。",
                line=review_line, code="ACADEMIC_REVIEW_INVALID",
            ))
        else:
            valid_reviews.add(review_id)

    segments = [(body, first_line, "正文")]
    if fm is not None and isinstance(data.get("summary"), str):
        segments.append((data["summary"], frontmatter_line_number(fm, "summary") or 2, "summary"))
    active_ids = set()
    for content, offset, location in segments:
        original_lines = content.splitlines()
        for index, line in enumerate(academic_prose_scan(content).splitlines()):
            context = markdown_visible_text(line).strip()
            if not context:
                continue
            context = re.sub(r"\s+", " ", context)[:160]
            for words, code in (
                (ACADEMIC_BUZZWORDS, "ACADEMIC_BUZZWORD"),
                (NEGATIVE_CONTRAST_MARKERS, "ACADEMIC_NEGATIVE_CONTRAST"),
                (SELF_REFERENCE_MARKERS, "ACADEMIC_SELF_REFERENCE"),
            ):
                hits = [word for word in words if word in line]
                if not hits:
                    continue
                review_id = writing_review_id(code, location, original_lines[index])
                active_ids.add(review_id)
                if review_id in valid_reviews:
                    # This exact expression was already justified. Reuse the
                    # exception silently; do not ask the AI to review it again.
                    continue
                else:
                    issues.append(Issue(
                        "WARN", rel(path),
                        f"{location}待审查 [{review_id}]（命中：{'、'.join(hits)}） 语境：{context}",
                        line=offset + index, code=code,
                    ))
    for review_id in valid_reviews - active_ids:
        issues.append(Issue(
            "ERROR", rel(path),
            f"scripts/writing_exceptions.json 的 {rel(path)} / {review_id} 已失效：原句已变化或命中已消失。删除旧记录；如需保留新表述，重新审查并添加新的 ID。",
            line=review_line, code="ACADEMIC_REVIEW_STALE",
        ))


def lint_file(path: Path, by_title: Dict[str, Dict[str, Any]], path_to_title: Dict[str, str], argument_citations: Dict[str, Dict[str, Any]], issues: List[Issue]) -> None:
    if is_generated_content_page(path):
        return

    # What breaks Linux CI / Quartz is an NFD path recorded in git, not the
    # on-disk name: APFS stores names as NFD but treats both forms as equal,
    # and macOS git (core.precomposeUnicode) records NFC.
    if unicodedata.normalize("NFC", path.name) != path.name and git_tracks_nfd_path(path):
        issues.append(Issue(
            "WARN", rel(path),
            "git tracks this file under a non-NFC (NFD) path; Linux CI / Quartz may see broken or duplicate paths — re-register it in the index under its NFC name",
            code="FILENAME_NFD",
        ))

    try:
        text = read_text(path)
    except UnicodeDecodeError:
        issues.append(Issue("ERROR", rel(path), "cannot read as UTF-8", code="UTF8"))
        return

    check_old_references(path, text, issues)
    check_quartz_safety(path, text, issues)
    check_effect_tables(path, text, issues)
    check_retired_headings(path, text, issues)
    check_def_title(path, text, issues)
    check_figure_callouts(path, text, issues)
    check_axis_callouts(path, text, issues)
    check_stat_card_titles(path, text, issues)
    check_markdown_misc(path, text, issues)
    check_templater_placeholders(path, text, issues)

    data = check_frontmatter(path, text, by_title, issues)
    check_academic_language(path, text, data, issues)
    if data and data.get("type") == "argument" and "journal-articles" in path.parts:
        check_journal_naming(path, data, issues)
    check_wikilinks(path, text, by_title, issues, data)
    check_sources_section(path, text, data, issues)
    check_template_consistency(path, text, issues)
    check_source_record(path, text, issues)
    check_path_and_index_consistency(path, data, path_to_title, issues)
    check_citation_links(path, text, data, argument_citations, issues)
    check_argument_raw_self_alias(path, text, data, argument_citations, issues)
    check_journal_self_pages(path, text, data, issues)
    check_duplicate_citations(path, text, data, issues)
    check_related_research_duplicate_books(path, text, by_title, issues)
    check_related_research_entry_length(path, text, issues)
    check_citation_card_language_order(path, text, issues)


# -----------------------------
# Auto-fix (--fix)
# -----------------------------

def mask_h2_sections_preserve(body: str, names: Iterable[str]) -> str:
    """Like remove_h2_sections but length-preserving (blanks section content)."""
    targets = {n.lower() for n in names}
    lines = body.splitlines(keepends=True)
    out: list[str] = []
    skipping = False
    for line in lines:
        if line.startswith("## "):
            skipping = line[3:].strip().lower() in targets
        out.append(re.sub(r"[^\n]", " ", line) if skipping else line)
    return "".join(out)


def fix_body_spans(text: str, argument_citations: Dict[str, Dict[str, Any]]) -> Tuple[str, int]:
    """Fix BOLD_HEADING_COLON, BOLD_HEADING_ENGLISH_OUTSIDE and CITATION_ENGLISH_AND."""
    fm, body, _ = split_frontmatter(text)
    head = text[: len(text) - len(body)]
    scan = mask_markdown_code(body)
    edits: List[Tuple[int, int, str]] = []  # (start, end, replacement) on body

    # Bold heading followed by a colon: **X**： -> **X** (colon dropped, single space).
    for m in re.finditer(r"(\*\*[^*\n]+?\*\*)[ \t]*[：:][ \t]*", scan):
        seg = body[m.start(1):m.end(1)]
        end = m.end()
        trailing = " " if end < len(body) and body[end] not in "\n" else ""
        edits.append((m.start(), end, seg + trailing))

    # English annotation outside the bold heading: **中文**（English） -> **中文（English）**
    for m in re.finditer(
        r"\*\*([^*\n]*[㐀-鿿][^*\n]*)\*\*\s*([（(][^）)\n]*[A-Za-z][^）)\n]*[）)])",
        scan,
    ):
        if re.fullmatch(r"[（(]\s*pp?\.\s*[^）)]+[）)]", m.group(2), flags=re.IGNORECASE):
            continue
        if re.fullmatch(r"[（(]\s*\[\[Argument_[^\]]*\]\]\s*[）)]", m.group(2)):
            continue
        if BARE_CITATION_PARENS_RE.fullmatch(m.group(2)):
            continue
        chinese = body[m.start(1):m.end(1)]
        annotation = body[m.start(2):m.end(2)]
        edits.append((m.start(), m.end(), f"**{chinese.strip()}{annotation}**"))

    # Format two-author displays by narrative/parenthetical style; keep lookup aliases canonical.
    cite_scan = mask_h2_sections_preserve(scan, ["来源", "Sources", "Source"])
    for m in WIKILINK_RE.finditer(cite_scan):
        raw = m.group(1)
        target = extract_wikilink_target(raw)
        if "|" not in raw or target not in argument_citations:
            continue
        display = raw.split("|", 1)[1].strip()
        if citation_display_text(display) and has_invalid_english_author_conjunction(display):
            fixed = fix_english_author_and(display)
            inner_start = m.start(1) + raw.index("|") + 1
            edits.append((inner_start, m.end(1), fixed))
    masked_links = strip_existing_wikilinks(cite_scan)
    for m in RAW_CITATION_RE.finditer(masked_links):
        txt = m.group(1).strip()
        if not citation_display_text(txt) or raw_citation_is_reference_fragment(txt):
            continue
        if has_invalid_english_author_conjunction(txt):
            edits.append((m.start(1), m.end(1), fix_english_author_and(body[m.start(1):m.end(1)])))

    if not edits:
        return text, 0
    # Apply non-overlapping edits right-to-left.
    edits.sort(key=lambda e: -e[0])
    applied = 0
    last_start = len(body) + 1
    new_body = body
    for s, e, repl in edits:
        if e > last_start:
            continue
        if new_body[s:e] == repl:
            continue
        new_body = new_body[:s] + repl + new_body[e:]
        last_start = s
        applied += 1
    return head + new_body, applied


def fix_apa7_reference(text: str) -> Tuple[str, int]:
    """CITATION_APA7_FORMAT: rewrite the frontmatter `citation` line in APA 7 form."""
    split = vaultlib.split_frontmatter(text)
    if not split.found:
        return text, 0
    import citation_index  # noqa: PLC0415
    meta = vaultlib.parse_frontmatter_light(split.raw)
    citation = meta.get("citation")
    if not isinstance(citation, str) or not citation.strip():
        return text, 0
    fixed, codes = citation_index.apa7_reference(citation, str(meta.get("publication_place") or ""))
    if not codes:
        return text, 0
    lines = split.raw.split("\n")
    for i, line in enumerate(lines):
        if re.match(r"^citation:\s", line):
            lines[i] = f"citation: {vaultlib.yaml_quote(fixed)}"
            break
    else:
        return text, 0
    head = split.head
    new_head = head[: head.index(split.raw)] + "\n".join(lines) + head[head.index(split.raw) + len(split.raw):]
    return new_head + split.body, 1


def fix_summary_quotes(text: str) -> Tuple[str, int]:
    fm, body, _ = split_frontmatter(text)
    if fm is None:
        return text, 0
    lines = text.split("\n")
    fixed = 0
    for i, l in enumerate(lines[: fm.count("\n") + 3]):
        m = re.match(r"^(\s*summary\s*:\s*)(.+?)\s*$", l)
        if not m:
            continue
        val = m.group(2)
        if val.startswith('"') and val.endswith('"'):
            break
        stripped = val.strip("'\"")
        if '"' in stripped:
            break
        lines[i] = f'{m.group(1)}"{stripped}"'
        fixed = 1
        break
    return "\n".join(lines), fixed


def fix_axis_callouts(text: str) -> Tuple[str, int]:
    """Normalize axis nesting and step back between consecutive sibling cards."""
    scan = mask_markdown_code(text)
    edits: List[Tuple[int, int, str]] = []
    for match in AXIS_CALLOUT_LINE_RE.finditer(scan):
        if match.group("quotes").count(">") == 2:
            continue
        edits.append((
            match.start("quotes"),
            match.end("quotes"),
            "> > ",
        ))
    new_text = text
    for start, end, replacement in reversed(edits):
        new_text = new_text[:start] + replacement + new_text[end:]

    # Re-scan after normalizing title depth.  A formerly three-level title can
    # expose its preceding `> >` blank as the newly malformed sibling boundary.
    nesting_fixes = len(edits)
    scan = mask_markdown_code(new_text)
    edits = []
    for match in AXIS_BAD_SIBLING_SEPARATOR_RE.finditer(scan):
        edits.append((
            match.start(),
            match.end(),
            f'{match.group("indent")}>{match.group("newline")}',
        ))
    for start, end, replacement in reversed(edits):
        new_text = new_text[:start] + replacement + new_text[end:]
    return new_text, nesting_fixes + len(edits)


_YEAR_SUFFIX_RE = re.compile(r"((?:19|20)\d{2})([a-z]?)")


def _with_year_suffix(display: str, aliases: List[str]) -> Optional[str]:
    """Insert the target's a/b/c suffix when the display only lacks it."""
    suffixed = None
    for alias in aliases:
        m = _YEAR_SUFFIX_RE.search(str(alias))
        if m and m.group(2):
            suffixed = m
            break
    if not suffixed:
        return None
    year, suffix = suffixed.group(1), suffixed.group(2)
    hits = [m for m in _YEAR_SUFFIX_RE.finditer(display) if m.group(1) == year and not m.group(2)]
    if len(hits) != 1:
        return None
    pos = hits[0].end(1)
    candidate = display[:pos] + suffix + display[pos:]
    return candidate if citation_display_matches_aliases(candidate, aliases) else None


def _narrative_display(aliases: List[str]) -> Optional[str]:
    for alias in aliases:
        alias = str(alias).strip()
        if alias.endswith(")") and "(" in alias:
            return fix_english_author_and(alias)
    return None


_SOURCE_SECTION_RE = re.compile(r"^##\s+(?:来源|Sources?)\s*$", re.M)
_FENCE_RE = re.compile(r"(?ms)^\s*(?:>\s*)*```.*?^\s*(?:>\s*)*```[^\n]*$")


def fix_citation_link_displays(text: str, argument_citations: Dict[str, Dict[str, Any]]) -> Tuple[str, int]:
    """Mechanical citation-link fixes.

    1. Add a missing a/b/c year suffix taken from the link target
       (fixes CITATION_LINK_TARGET_MISMATCH when only the suffix is missing).
    2. In non-Argument entries, give bare [[Argument_X]] links the target's
       narrative author-year display (fixes ARGUMENT_LINK_AUTHOR_YEAR_MISSING).
    Source sections, code blocks and table rows are left untouched."""
    fm, body, _ = split_frontmatter(text)
    if fm is None:
        return text, 0
    type_m = re.search(r"^type:\s*[\"']?([A-Za-z]+)", fm, re.M)
    entry_type = type_m.group(1).lower() if type_m else ""
    non_argument = entry_type in {"concept", "theory", "method", "instrument", "person", "fact"}

    src = _SOURCE_SECTION_RE.search(body)
    head, tail = (body[:src.start()], body[src.start():]) if src else (body, "")
    protected = [(m.start(), m.end()) for m in _FENCE_RE.finditer(head)]

    def in_protected(pos: int) -> bool:
        return any(a <= pos < b for a, b in protected)

    count = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal count
        if in_protected(m.start()):
            return m.group(0)
        line_start = head.rfind("\n", 0, m.start()) + 1
        line_end = head.find("\n", m.end())
        line = head[line_start: line_end if line_end != -1 else len(head)]
        if line.lstrip().startswith("|"):
            return m.group(0)
        raw = m.group(1)
        target = extract_wikilink_target(raw)
        info = argument_citations.get(target)
        if not info:
            return m.group(0)
        aliases = info.get("aliases") or []
        sep_m = re.search(r"\\?\|", raw)
        if sep_m:
            display = raw[sep_m.end():]
            if display.strip() and citation_display_text(display.strip()) and not citation_display_matches_aliases(display.strip(), aliases):
                fixed = _with_year_suffix(display, aliases)
                if fixed:
                    count += 1
                    return "[[" + raw[:sep_m.end()] + fixed + "]]"
            return m.group(0)
        if non_argument and "#" not in raw:
            narrative = _narrative_display(aliases)
            if narrative:
                count += 1
                return f"[[{raw}|{narrative}]]"
        return m.group(0)

    new_head = WIKILINK_RE.sub(repl, head)
    if not count:
        return text, 0
    return text[: len(text) - len(body)] + new_head + tail, count


# A Markdown table row, also inside callouts ("> | a | b |").
_TABLE_ROW_RE = re.compile(r"^\s*(?:>\s*)*\|")
_NARRATIVE_CITATION_RE = re.compile(r"^[^()（）]*\S\s*[(（]\s*(?:19|20)\d{2}")


def is_narrative_citation(display: str) -> bool:
    """'Smith (2020, p. 3)' is a sentence constituent, not a parenthetical
    reference; repeating it in one paragraph is normal prose."""
    d = display.strip()
    return not d.startswith(("(", "（")) and bool(_NARRATIVE_CITATION_RE.match(d))


def fix_duplicate_parenthetical_links(text: str) -> Tuple[str, int]:
    """Within one paragraph/callout unit keep the first of identical
    parenthetical citation links such as [[Argument_X|(Smith, 2020, p. 3)]]
    and delete later repeats (CITATION_DUPLICATE_IN_UNIT). Table rows,
    narrative citations and links embedded in prose are left alone."""
    fm, body, _ = split_frontmatter(text)
    if fm is None:
        return text, 0
    src = _SOURCE_SECTION_RE.search(body)
    head, tail = (body[:src.start()], body[src.start():]) if src else (body, "")
    cuts: List[Tuple[int, int]] = []
    for unit, offset, _kind in citation_units(head):
        seen: Set[str] = set()
        for m in WIKILINK_RE.finditer(unit):
            raw = m.group(1)
            target = extract_wikilink_target(raw)
            if not target.startswith("Argument_"):
                continue
            sep = re.search(r"\\?\|", raw)
            if not sep:
                continue
            display = raw[sep.end():].strip()
            if not (display.startswith(("(", "（")) and display.endswith((")", "）"))):
                continue
            line_start = unit.rfind("\n", 0, m.start()) + 1
            if _TABLE_ROW_RE.match(unit[line_start:m.start() + 1]):
                continue
            key = citation_identity(display, target)
            if not key:
                continue
            if key not in seen:
                seen.add(key)
                continue
            start, end = offset + m.start(), offset + m.end()
            while start > 0 and head[start - 1] in " \t":
                start -= 1
            cuts.append((start, end))
    if not cuts:
        return text, 0
    for start, end in sorted(cuts, reverse=True):
        head = head[:start] + head[end:]
    return text[: len(text) - len(body)] + head + tail, len(cuts)


def fix_alias_title_duplicates(text: str) -> Tuple[str, int]:
    """Drop aliases identical to the entry title (case/width-insensitive)."""
    fm, _, _ = split_frontmatter(text)
    if fm is None:
        return text, 0
    title_m = re.search(r"^title:\s*(.+)$", fm, re.M)
    if not title_m:
        return text, 0
    title_key = unicodedata.normalize("NFKC", title_m.group(1).strip().strip("\"'")).casefold()
    lines = fm.split("\n")
    out: List[str] = []
    removed = 0
    in_aliases = False
    for line in lines:
        if re.match(r"^aliases:\s*$", line):
            in_aliases = True
            out.append(line)
            continue
        if in_aliases:
            item = re.match(r"^\s+-\s+(.*)$", line)
            if item:
                value = item.group(1).strip().strip("\"'")
                if unicodedata.normalize("NFKC", value).casefold() == title_key:
                    removed += 1
                    continue
                out.append(line)
                continue
            in_aliases = False
        inline = re.match(r"^(aliases:\s*\[)(.*)(\]\s*)$", line)
        if inline:
            items = [s.strip() for s in inline.group(2).split(",") if s.strip()]
            kept = [s for s in items if unicodedata.normalize("NFKC", s.strip("\"'")).casefold() != title_key]
            if len(kept) != len(items):
                removed += len(items) - len(kept)
                line = inline.group(1) + ", ".join(kept) + inline.group(3)
        out.append(line)
    if not removed:
        return text, 0
    new_fm = "\n".join(out)
    return text.replace(fm, new_fm, 1), removed


def _replace_parentheticals(head: str, rewrite) -> Tuple[str, int]:
    """Apply rewrite(group) -> replacement or None. Empty replacement deletes the group."""
    scan = strip_existing_wikilinks(mask_markdown_code(head))
    edits: List[Tuple[int, int, str]] = []
    for m in PAREN_GROUP_RE.finditer(scan):
        replacement = rewrite(m.group(0))
        if replacement is None:
            continue
        start, end = m.start(), m.end()
        if not replacement:
            while start > 0 and head[start - 1] in " \t":
                start -= 1
        edits.append((start, end, replacement))
    if not edits:
        return head, 0
    for start, end, repl in sorted(edits, key=lambda item: item[0], reverse=True):
        head = head[:start] + repl + head[end:]
    return head, len(edits)


def _split_body_before_sources(body: str) -> Tuple[str, str]:
    src = _SOURCE_SECTION_RE.search(body)
    return (body[:src.start()], body[src.start():]) if src else (body, "")


def fix_argument_raw_self_aliases(path: Path, text: str, argument_citations: Dict[str, Dict[str, Any]]) -> Tuple[str, int]:
    """Rewrite parenthetical self-citations. Books and reports keep page locators; journals delete them."""
    if not is_wiki_entry_path(path):
        return text, 0
    fm, body, _ = split_frontmatter(text)
    if fm is None:
        return text, 0
    data = entry_metadata(path)
    if not is_argument_entry(data):
        return text, 0
    aliases = argument_self_parenthetical_aliases(path, fm, data or {}, argument_citations)
    if not aliases:
        return text, 0
    journal = is_journal_argument(path, data)
    head, tail = _split_body_before_sources(body)

    def rewrite(group: str) -> Optional[str]:
        res = self_alias_rewrite(group, aliases, drop_pages=journal)
        return None if res is None else res[0]

    new_head, count = _replace_parentheticals(head, rewrite)
    if not count:
        return text, 0
    return text[: len(text) - len(body)] + new_head + tail, count


def fix_journal_self_pages(path: Path, text: str) -> Tuple[str, int]:
    """Delete page, table, figure, and footnote locators on journal arguments (JOURNAL_SELF_PAGE)."""
    if not is_wiki_entry_path(path):
        return text, 0
    fm, body, _ = split_frontmatter(text)
    if fm is None:
        return text, 0
    data = entry_metadata(path)
    if not is_journal_argument(path, data):
        return text, 0
    head, tail = _split_body_before_sources(body)
    new_head, count = _replace_parentheticals(
        head, lambda group: "" if is_journal_self_page_group(group) else None
    )
    if not count:
        return text, 0
    return text[: len(text) - len(body)] + new_head + tail, count


def apply_fixes(files: List[Path], argument_citations: Dict[str, Dict[str, Any]]) -> Tuple[int, int]:
    changed_files = 0
    total = 0
    for path in files:
        if TEMPLATES_DIR in path.parents or is_schema_or_workflow_doc(path) or is_generated_content_page(path):
            continue
        try:
            text = read_text(path)
        except Exception:
            continue
        new_text, n1 = text, 0
        for _ in range(3):  # english-outside fixes can expose new colon issues
            new_text, n = fix_body_spans(new_text, argument_citations)
            n1 += n
            if not n:
                break
        new_text, n2 = fix_summary_quotes(new_text)
        new_text, n_apa = fix_apa7_reference(new_text)
        n2 += n_apa
        new_text, n3 = fix_axis_callouts(new_text)
        new_text, n4 = fix_bold_boundaries(new_text)
        if is_wiki_entry_path(path):
            new_text, n_deng = fix_latin_deng(new_text)
            n4 += n_deng
        n5 = n6 = 0
        if is_wiki_entry_path(path):
            new_text, n5 = fix_citation_link_displays(new_text, argument_citations)
            new_text, n6 = fix_alias_title_duplicates(new_text)
            new_text, n7 = fix_duplicate_parenthetical_links(new_text)
            new_text, n8 = fix_argument_raw_self_aliases(path, new_text, argument_citations)
            new_text, n9 = fix_journal_self_pages(path, new_text)
            n6 += n7 + n8 + n9
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed_files += 1
            n = n1 + n2 + n3 + n4 + n5 + n6
            total += n
            print(f"fixed {n:3d}  {rel(path)}")
    return changed_files, total


# -----------------------------
# Shared local / CI commit gate
# -----------------------------

GATE_SKIP_ENV = "VAULT_LINT_SKIP_GATE"


def start_gate_checks() -> List[Tuple[str, str, str, "subprocess.Popen[str]"]]:
    """Start registry and index checks in parallel with the lint pass.

    Returns (code, issue_path, fix_hint, process) tuples; collect with finish_gate_checks()."""
    if os.environ.get(GATE_SKIP_ENV):
        return []
    checks = [
        ("INDEX_STALE", "wiki/index.json", "run: python3 scripts/vault_index.py", ["scripts/wiki_index.py", "--check"]),
        ("CITATION_INDEX_STALE", "citation/citation_full.json", "run: python3 scripts/vault_index.py", ["scripts/citation_index.py", "--check"]),
        ("METAX_STALE", "datasets/metax/metax.json", "run: python3 scripts/vault_index.py", ["scripts/metax_sync.py", "sync", "--check"]),
        ("EEF_STALE", "datasets/eef/eef.json", "run: python3 scripts/vault_index.py", ["scripts/eef_sync.py", "sync", "--check"]),
    ]
    env = dict(os.environ, **{GATE_SKIP_ENV: "1"})
    started = []
    for code, issue_path, hint, cmd in checks:
        if cmd[0].startswith("scripts/") and not (ROOT / cmd[0]).exists():
            continue
        try:
            proc = subprocess.Popen([sys.executable, "-B", *cmd], cwd=ROOT, env=env, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except Exception as exc:  # pragma: no cover - environment failure
            started.append((code, issue_path, f"could not start check: {exc}", None))
            continue
        started.append((code, issue_path, hint, proc))
    return started


def finish_gate_checks(started, issues: List[Issue]) -> None:
    for code, issue_path, hint, proc in started:
        if proc is None:
            issues.append(Issue("ERROR", issue_path, hint, code=code))
            continue
        out, _ = proc.communicate()
        if proc.returncode == 0:
            continue
        tail = " | ".join(line.strip() for line in (out or "").strip().splitlines()[-4:] if line.strip())
        issues.append(Issue("ERROR", issue_path, f"commit gate check failed ({hint}); output: {tail}", code=code))


# Per-file checks are independent, so large batches (--full, --base, big diffs)
# are split across forked workers. Results keep the serial order exactly.
PARALLEL_MIN_FILES = 200
_LINT_SHARED: Tuple[Any, ...] = ()


def _lint_one(item, by_title, path_to_title, argument_citations, out: List[Issue], baseline: bool) -> None:
    if not baseline:
        lint_file(item, by_title, path_to_title, argument_citations, out)
        return
    # Baseline: lint the comparison-ref text of this path; failures are ignored.
    path, text = item
    _TEXT_OVERRIDES[path] = text
    try:
        lint_file(path, by_title, path_to_title, argument_citations, out)
    except Exception:
        pass
    finally:
        _TEXT_OVERRIDES.pop(path, None)


def _lint_chunk(chunk) -> List[Issue]:
    by_title, path_to_title, argument_citations, baseline = _LINT_SHARED
    out: List[Issue] = []
    for item in chunk:
        _lint_one(item, by_title, path_to_title, argument_citations, out, baseline)
    return out


def lint_files(items, by_title, path_to_title, argument_citations, baseline: bool = False) -> List[Issue]:
    global _LINT_SHARED
    items = list(items)
    workers = min(os.cpu_count() or 1, 8)
    if len(items) >= PARALLEL_MIN_FILES and workers > 1 and not os.environ.get("VAULT_LINT_SERIAL"):
        import multiprocessing
        try:
            ctx = multiprocessing.get_context("fork")
        except ValueError:  # no fork (Windows): stay serial
            ctx = None
        if ctx is not None:
            # Workers inherit the loaded index maps through fork (no pickling).
            _LINT_SHARED = (by_title, path_to_title, argument_citations, baseline)
            size = max(10, len(items) // (workers * 6))
            chunks = [items[i:i + size] for i in range(0, len(items), size)]
            try:
                with ctx.Pool(workers) as pool:
                    return [issue for part in pool.map(_lint_chunk, chunks) for issue in part]
            except Exception as exc:  # pragma: no cover - fall back to serial
                print(f"(parallel lint unavailable: {exc}; running serially)", file=sys.stderr)
            finally:
                _LINT_SHARED = ()
    issues: List[Issue] = []
    for item in items:
        _lint_one(item, by_title, path_to_title, argument_citations, issues, baseline)
    return issues


# Set by lint_vault(): how many pre-existing warnings were hidden.
HIDDEN_PREEXISTING_WARNINGS = 0
# --base only: writing hits already present at the base commit.
HIDDEN_PREEXISTING_WRITING = 0


def lint_vault(paths: List[Path], strict: bool = False, full: bool = False, fix: bool = False, gate: bool = True, all_warnings: bool = False) -> List[Issue]:
    issues: List[Issue] = []
    check_required_files(issues)
    check_writing_exceptions(issues)
    check_link_exceptions(issues)
    from citation_index import load_registry
    try:
        load_registry()
    except (OSError, ValueError) as exc:
        issues.append(Issue("ERROR", "citation/journals.json", str(exc), code="JOURNAL_REGISTRY_INVALID"))
    by_title, path_to_title = load_index(issues)
    argument_citations, citation_stems = build_argument_citation_maps([], issues)

    md_files: List[Path] = []
    if paths:
        for p in paths:
            if not p.exists():
                issues.append(Issue("ERROR", rel(p), "path does not exist", code="PATH_MISSING"))
                continue
            md_files.extend(iter_md_files(p))
    elif full:
        # Main vault markdown files.
        for base in [WIKI_DIR, ROOT / "books", ROOT / "sources", ROOT / "vault-schema.md", ROOT / "CLAUDE.md"]:
            if base.exists():
                md_files.extend(iter_md_files(base))
    else:
        # Default incremental mode: only files changed in git status.
        md_files.extend(git_changed_md_files())

    md_files.extend(writing_exception_changed_notes())

    # Deduplicate preserving order.
    seen = set()
    unique_files = []
    for p in md_files:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            unique_files.append(p)

    if fix:
        changed_files, total_fixes = apply_fixes(unique_files, argument_citations)
        if changed_files:
            read_text.cache_clear()
            entry_metadata.cache_clear()
        print(f"--fix: {total_fixes} issue(s) fixed in {changed_files} file(s)\n")

    gate_checks = start_gate_checks() if gate else []

    # Outside --full, hide baseline warnings except unresolved writing reviews.
    # Writing requirements must survive auto-commits and cannot be grandfathered.
    global HIDDEN_PREEXISTING_WARNINGS
    baseline = None
    if not full and not all_warnings:
        baseline = baseline_warning_keys(unique_files, by_title, path_to_title, argument_citations)

    file_issues = lint_files(unique_files, by_title, path_to_title, argument_citations)
    if full:
        file_issues = collapse_external_identity_issues(file_issues)
    hidden = 0
    hidden_writing = 0
    if baseline:
        # CI (--base) gates only writing hits that are new relative to the
        # base commit; local incremental lint still lists every unresolved one.
        base_mode = bool(os.environ.get("VAULT_LINT_BASE"))
        kept: List[Issue] = []
        for issue in file_issues:
            key = (issue.path, issue.code, issue.message)
            if issue.severity in ("WARN", "INFO") and issue.code not in WRITING_REMINDER_CODES and baseline.get(key, 0) > 0:
                baseline[key] -= 1
                hidden += 1
                continue
            if base_mode and issue.code in WRITING_REMINDER_CODES:
                wkey = writing_baseline_key(issue)
                if baseline.get(wkey, 0) > 0:
                    baseline[wkey] -= 1
                    hidden_writing += 1
                    continue
            kept.append(issue)
        file_issues = kept
    HIDDEN_PREEXISTING_WARNINGS = hidden
    global HIDDEN_PREEXISTING_WRITING
    HIDDEN_PREEXISTING_WRITING = hidden_writing
    issues.extend(file_issues)

    argument_check_files = list(unique_files)
    # Even when lint is path-scoped, new extracted entries are a vault-level
    # invariant: they must be introduced from an Argument page. Include git
    # changed files so a new Person/Concept/etc. is not missed when the user
    # linted only the current Argument page.
    if paths:
        argument_check_files.extend(git_changed_md_files())
    check_new_entries_mentioned_in_arguments(argument_check_files, issues)
    check_citation_json_consistency(argument_citations, issues)
    finish_gate_checks(gate_checks, issues)

    return issues


# -----------------------------
# CLI
# -----------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Lint Obsidian / Quartz academic wiki vault.")
    parser.add_argument("--base", help="Read-only CI check of changes from this commit to HEAD, including clean checkouts.")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    parser.add_argument("--json", action="store_true", help="output JSON")
    parser.add_argument("--path", action="append", default=[], help="limit lint to path. Can be repeated. Overrides default git-incremental mode.")
    parser.add_argument("--full", action="store_true", help="lint the full vault instead of only git-changed Markdown files")
    parser.add_argument("--quiet", action="store_true", help="only print errors and summary")
    parser.add_argument("--show-info", action="store_true", help="include INFO items in text output")
    parser.add_argument("--all-warnings", action="store_true", help="also show warnings that already existed at HEAD (default outside --full: only newly introduced warnings)")
    parser.add_argument("--no-gate", action="store_true", help="skip the commit-gate checks (journal registry and index freshness)")
    parser.add_argument("--fix", action="store_true", help="auto-fix mechanical issues (including malformed sibling [!axis] separators) before linting")
    args = parser.parse_args()
    if args.base is not None:
        if args.fix:
            parser.error("--base is read-only and cannot be combined with --fix")
        if not args.base:
            parser.error("--base must name a commit")
        if set(args.base) != {"0"}:
            result = subprocess.run(["git", "rev-parse", "--verify", "--end-of-options", f"{args.base}^{{commit}}"], cwd=ROOT, capture_output=True)
            if result.returncode:
                parser.error("--base does not resolve to a commit")
            args.base = result.stdout.decode("ascii").strip()
        os.environ["VAULT_LINT_BASE"] = args.base
        os.environ["VAULT_JOURNAL_BASE"] = args.base
        _git_changed_md_files_cached.cache_clear()
        git_head_paths.cache_clear()

    paths = [(ROOT / p).resolve() if not Path(p).is_absolute() else Path(p).resolve() for p in args.path]
    issues = lint_vault(paths, strict=args.strict, full=args.full, fix=args.fix,
                        gate=not args.no_gate,
                        all_warnings=args.all_warnings)

    errors = [i for i in issues if i.severity == "ERROR"]
    warns = [i for i in issues if i.severity == "WARN"]
    infos = [i for i in issues if i.severity == "INFO"]
    pending_writing = [i for i in warns if i.code in WRITING_REMINDER_CODES]

    if args.json:
        print(json.dumps([asdict(i) for i in issues], ensure_ascii=False, indent=2))
    else:
        for issue in issues:
            if args.quiet and issue.severity != "ERROR":
                continue
            if issue.severity == "INFO" and not args.show_info and issue.code != EXTERNAL_CITATION_IDENTITY:
                continue
            print(issue.format())
        print()
        print(f"Summary: {len(errors)} error(s), {len(warns)} warning(s), {len(infos)} info item(s).")
        if pending_writing:
            print(f"Writing review required: {len(pending_writing)} item(s). 修改表达或在 scripts/writing_exceptions.json 添加经审查批准的 ID 后再运行 lint。")
            for line in writing_review_legend(i.code for i in pending_writing):
                print(line)
        if HIDDEN_PREEXISTING_WRITING:
            print(f"(--base: {HIDDEN_PREEXISTING_WRITING} writing review item(s) already present at the base commit are not gated; run lint locally to review them.)")
        if HIDDEN_PREEXISTING_WARNINGS:
            print(f"(Unresolved writing reviews are always listed; {HIDDEN_PREEXISTING_WARNINGS} other baseline warning/info item(s) hidden. Use --all-warnings to show them.)")

    if errors or pending_writing:
        return 1
    if args.strict and warns:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
