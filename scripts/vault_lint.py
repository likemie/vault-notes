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
- Warnings do not fail unless --strict is used.

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
import json
import os
import re
import sys
import subprocess
import unicodedata
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import quote


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
    if os.environ.get("VAULT_LINT_VENV_REEXEC") == "1":
        return

    root = find_vault_root()
    if sys.platform == "win32":
        venv_python = root / ".venv" / "Scripts" / "python.exe"
    else:
        venv_python = root / ".venv" / "bin" / "python"

    if not venv_python.exists():
        return

    if Path(sys.prefix).resolve() == root.resolve() / ".venv":
        return

    env = os.environ.copy()
    env["VAULT_LINT_VENV_REEXEC"] = "1"
    os.execve(str(venv_python), [str(venv_python), str(Path(__file__).resolve()), *sys.argv[1:]], env)


maybe_reexec_with_vault_venv()

try:
    import yaml  # type: ignore
except Exception:
    yaml = None


# -----------------------------
# Configuration
# -----------------------------

ROOT = Path.cwd()
WIKI_DIR = ROOT / "wiki"
TEMPLATES_DIR = WIKI_DIR / "templates"
INDEX_JSON = WIKI_DIR / "index.json"
CITATION_DIR = ROOT / "citation"
CITATION_FULL_JSON = CITATION_DIR / "citation_full.json"
CITATION_AMBIGUOUS_JSON = CITATION_DIR / "citation_ambiguous.json"
ASSET_BASE_URL = "https://img.mylikemie.icu"

GENERATED_INDEX_FILES = {
    "index.md",
    "index.json",
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

# Schema-constrained APA short citations used for links to Argument pages.
CITATION_PARENT_RE = re.compile(r"^\([A-Z][A-Za-z0-9 .&和-]+,\s*(?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?\)$")
CITATION_NARRATIVE_RE = re.compile(r"^[A-Z][A-Za-z0-9 .&和-]+\s*[（(](?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?[）)]$")
RAW_CITATION_RE = re.compile(r"(?<![\w\[])(\([A-Z][A-Za-z0-9 .&和-]+,\s*(?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?\)|（[A-Z][A-Za-z0-9 .&和-]+,\s*(?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?）|[A-Z][A-Za-z0-9 .&和-]+\s*[（(](?:19|20)\d{2}[a-z]?(?:,\s*pp?\.\s*\d+(?:[–-]\d+)?)?[）)])")
ENGLISH_AUTHOR_AND_RE = re.compile(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])\s*(?:and|和)\s*(?=[A-ZÀ-ÖØ-Þ])")

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


def author_label(author: str) -> str:
    author = str(author).strip()
    m = re.fullmatch(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", author)
    if m:
        author = (m.group(2) or m.group(1)).strip()
    author = author.replace("''", "'")
    if "," in author:
        return author.split(",", 1)[0].strip()
    return re.sub(r"\s+", " ", author).strip()


def wikilink_target_and_display(value: str) -> Optional[Tuple[str, str]]:
    m = re.fullmatch(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", value.strip())
    if not m:
        return None
    target = m.group(1).strip()
    display = (m.group(2) or m.group(1)).strip()
    return target, display


def looks_like_forward_western_person_name(value: str) -> bool:
    value = re.sub(r"\s+", " ", value).strip()
    if not value or "," in value or has_cjk(value):
        return False
    parts = value.split()
    if len(parts) < 2:
        return False
    return all(re.fullmatch(r"[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÖØ-öø-ÿ'’.-]*", part) for part in parts)


def check_argument_creator_apa_display(path: Path, fm: str, field: str, item: str, issues: List[Issue]) -> None:
    parsed = wikilink_target_and_display(item)
    if not parsed:
        return
    target, display = parsed
    if "|" in item or "," in display:
        return
    if looks_like_forward_western_person_name(target):
        issues.append(Issue(
            "ERROR",
            rel(path),
            f"{field} Person wikilink should use APA inverted display name, e.g. [[{target}|{target.split()[-1]}, X.]]: {item!r}",
            line=frontmatter_line_number(fm, field),
            code=f"{field.upper()}_APA_DISPLAY",
        ))


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", text))


def dedupe(items: List[str]) -> List[str]:
    seen: set[str] = set()
    result: List[str] = []
    for item in items:
        if item and item not in seen:
            result.append(item)
            seen.add(item)
    return result


def chinese_author_part(citation: str, year: str) -> str:
    if not has_cjk(citation) or not year:
        return ""
    m = re.match(rf"^\s*(?P<authors>.+?)\s*(?:[.。]\s*)?[（(]\s*{re.escape(year)}\s*[）)]", citation)
    if not m:
        return ""
    raw = m.group("authors").strip(" ,，.。")
    if not has_cjk(raw):
        return ""
    parts = [p.strip() for p in re.split(r"[、，,；;]\s*", raw) if p.strip()]
    cjk_parts = [p for p in parts if has_cjk(p)]
    if not cjk_parts:
        return ""
    if len(cjk_parts) == 1:
        return cjk_parts[0]
    if len(cjk_parts) == 2:
        return f"{cjk_parts[0]}和{cjk_parts[1]}"
    return f"{cjk_parts[0]}等"


def normalized_source_language(value: Any) -> str:
    language = str(value or "").strip().lower().replace("_", "-")
    if language in {"zh", "zh-cn", "zh-hans", "chinese", "中文"}:
        return "zh"
    if language in {"en", "en-us", "en-gb", "english", "英文"}:
        return "en"
    return language


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
    aliases: List[str] = []
    for part in dedupe(parts):
        aliases.extend([f"{part}, {year}", f"{part} ({year})"])
    return aliases


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

def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except Exception:
        return path.as_posix()


def asset_url_for_path(path: Path) -> str:
    rel_path = rel(path)
    encoded = "/".join(quote(part, safe="-_.!~*'()") for part in rel_path.split("/"))
    return f"{ASSET_BASE_URL}/{encoded}"


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


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_git(args: List[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.stdout
    except Exception:
        return ""


def git_path_exists_at_head(path: Path) -> bool:
    r = rel(path)
    result = subprocess.run(
        ["git", "-c", "core.quotePath=false", "cat-file", "-e", f"HEAD:{r}"],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.returncode == 0


def git_changed_md_files() -> List[Path]:
    """Return changed Markdown files according to git status, including untracked files."""
    out = run_git(["status", "--porcelain", "--untracked-files=all"])
    files: List[Path] = []
    for line in out.splitlines():
        if not line:
            continue
        # Porcelain v1 uses two status columns followed by path.
        raw = line[3:] if len(line) > 3 else ""
        if " -> " in raw:
            raw = raw.split(" -> ", 1)[1]
        raw = raw.strip().strip('"')
        if not raw or not raw.endswith(".md"):
            continue
        p = ROOT / raw
        if p.exists() and p.suffix.lower() == ".md":
            files.append(p)
    return files


def embedded_file_exists_by_name(target_name: str) -> bool:
    """Cache expensive vault-wide filename lookups used for embedded PDFs/images."""
    key = unicodedata.normalize("NFC", target_name)
    if key in EMBED_FILE_EXISTS_CACHE:
        return EMBED_FILE_EXISTS_CACHE[key]
    found = False
    for c in ROOT.rglob("*"):
        if any(part in SKIP_DIR_NAMES for part in c.parts):
            continue
        if unicodedata.normalize("NFC", c.name) == key:
            found = True
            break
    EMBED_FILE_EXISTS_CACHE[key] = found
    return found


def split_frontmatter(text: str) -> Tuple[Optional[str], str, int]:
    """
    Return (frontmatter_raw, body, body_start_line).
    body_start_line is 1-indexed line number where body starts.
    """
    if not text.startswith("---\n"):
        return None, text, 1
    end = text.find("\n---", 4)
    if end == -1:
        return None, text, 1
    # Require delimiter line.
    after = end + len("\n---")
    if after < len(text) and text[after] not in "\n\r":
        return None, text, 1
    fm = text[4:end]
    body_start = text[:after].count("\n") + 1
    # Skip following newline if present.
    if after < len(text) and text[after] == "\n":
        after += 1
        body_start += 1
    return fm, text[after:], body_start


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
        data = yaml.safe_load(fm) or {}
        if not isinstance(data, dict):
            issues.append(Issue("ERROR", rel(path), "frontmatter is not a YAML mapping", code="FM_TYPE"))
            return {}
        return data
    except Exception as e:
        issues.append(Issue("ERROR", rel(path), f"frontmatter YAML parse error: {e}", code="YAML_PARSE"))
        return {}


def frontmatter_line_number(fm: str, key: str) -> Optional[int]:
    pattern = re.compile(rf"^\s*{re.escape(key)}\s*:", re.MULTILINE)
    m = pattern.search(fm)
    if not m:
        return None
    return fm[:m.start()].count("\n") + 2  # +1 for 1-indexed, +1 for opening ---


def is_generated_or_template(path: Path) -> bool:
    if path.name in GENERATED_INDEX_FILES:
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
    """
    [[Target]] or [[Target|Display]] or [[Target#Heading|Display]]
    Also handles Quartz-style [[Target\\|Display]].
    Return target before \\|, | and #.
    """
    # Quartz-style escaped pipe: Target\|Display
    target = raw.split("\\|", 1)[0].strip()
    # Standard Obsidian pipe: Target|Display
    target = target.split("|", 1)[0].strip()
    target = target.split("#", 1)[0].strip()
    return target


def extract_wikilinks(text: str) -> List[Tuple[str, int]]:
    clean = strip_code_blocks(text)
    return [(extract_wikilink_target(m.group(1)), m.start()) for m in WIKILINK_RE.finditer(clean)]


def extract_embeds(text: str) -> List[Tuple[str, int]]:
    clean = strip_code_blocks(text)
    return [(extract_wikilink_target(m.group(1)), m.start()) for m in EMBED_RE.finditer(clean)]


def normalize_title(s: str) -> str:
    return s.strip()


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
        ROOT / "scripts" / "citation_linker.py",
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
        if not title:
            issues.append(Issue("ERROR", rel(path), "missing frontmatter title", line=frontmatter_line_number(fm, "title"), code="TITLE_MISSING"))
        elif isinstance(title, str):
            stem = path.stem
            # Templater files use placeholders; normal entries should match filename.
            if "<%" not in title and title != stem and not title_matches_filename(title, stem):
                issues.append(Issue("WARN", rel(path), f"title differs from filename stem: title={title!r}, filename={stem!r}", line=frontmatter_line_number(fm, "title"), code="TITLE_FILENAME_MISMATCH"))

    # type checks
    if is_wiki_entry_path(path):
        if not typ:
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

    # Only Argument pages maintain source record links.
    if is_wiki_entry_path(path) and typ in {"concept", "theory", "method", "instrument", "person", "fact"} and "sources" in data:
        issues.append(Issue("ERROR", rel(path), "non-Argument wiki entries should not include YAML sources; use related_arguments via Argument links", line=frontmatter_line_number(fm, "sources"), code="NON_ARGUMENT_SOURCES_FIELD"))

    if typ == "argument" and "sources" not in data:
        issues.append(Issue("WARN", rel(path), "Argument entries should include sources field for source record links", code="ARGUMENT_SOURCES_MISSING"))

    if typ == "person":
        for field in ["family_name", "given_names", "initials", "citation_name"]:
            if field in data:
                issues.append(Issue("WARN", rel(path), f"person entry should not include legacy citation helper field {field}", line=frontmatter_line_number(fm, field), code=f"PERSON_{field.upper()}_LEGACY"))
        if isinstance(title, str) and "<%" not in title and path.stem != title:
            issues.append(Issue("WARN", rel(path), "person filename stem should match title exactly", line=frontmatter_line_number(fm, "title"), code="PERSON_TITLE_FILENAME_MISMATCH"))
        aliases = data.get("aliases")
        if isinstance(aliases, list):
            for alias in aliases:
                if isinstance(alias, str) and alias_is_single_english_family(alias):
                    issues.append(Issue("WARN", rel(path), f"person alias should not be a single English family name: {alias!r}", line=frontmatter_line_number(fm, "aliases"), code="PERSON_ALIAS_SINGLE_FAMILY"))

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

    if is_citation_eligible_argument(data):
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
            if aliases and expected_base and aliases != expected_base and not all(re.match(r"^.+(?:19|20)\d{2}[a-z]\)?$", str(a)) for a in aliases):
                issues.append(Issue("WARN", rel(path), f"citation_aliases differ from authors + year base form; run vault_index.py: {aliases!r}", line=frontmatter_line_number(fm, "citation_aliases"), code="CITATION_ALIASES_MISMATCH"))

    # summary checks
    if "summary" in data:
        check_summary(path, fm, data.get("summary"), issues)
    elif is_wiki_entry_path(path) and typ != "source":
        issues.append(Issue("WARN", rel(path), "missing summary field", code="SUMMARY_MISSING"))

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
        if publication_type in {"book", "edited-volume", "book-chapter"}:
            publisher = str(data.get("publisher") or "").strip()
            publication_place = str(data.get("publication_place") or "").strip()
            if not publication_place:
                issues.append(Issue(
                    "ERROR",
                    rel(path),
                    "book citation metadata must include publication_place",
                    line=frontmatter_line_number(fm, "publisher"),
                    code="BOOK_PUBLICATION_PLACE_MISSING",
                ))
            if not publisher:
                issues.append(Issue(
                    "ERROR",
                    rel(path),
                    "book citation metadata must include publisher",
                    line=frontmatter_line_number(fm, "publisher"),
                    code="BOOK_PUBLISHER_MISSING",
                ))
            if citation and publication_place and publisher:
                place_publisher = re.compile(
                    rf"{re.escape(publication_place)}\s*[:：]\s*{re.escape(publisher)}"
                )
                if not place_publisher.search(citation):
                    issues.append(Issue(
                        "ERROR",
                        rel(path),
                        f"book citation must place location before publisher: {publication_place}: {publisher}.",
                        line=frontmatter_line_number(fm, "citation"),
                        code="BOOK_CITATION_PLACE_PUBLISHER",
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

    return data


def check_summary(path: Path, fm: str, summary: Any, issues: List[Issue]) -> None:
    line = frontmatter_line_number(fm, "summary")

    if summary is None:
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

    if summary == "":
        return

    for ch in FORBIDDEN_SUMMARY_CHARS:
        if ch in summary:
            label = {"\"": "double quote", "'": "single quote", ":": "English colon", "_": "underscore"}[ch]
            issues.append(Issue("ERROR", rel(path), f"summary contains forbidden {label}: {summary!r}", line=line, code="SUMMARY_FORBIDDEN_CHAR"))

    banned_phrases = ["本文研究", "作者认为", "本研究发现", "本论文", "本章认为", "本文认为", "本文旨在", "本章旨在", "本研究旨在"]
    for phrase in banned_phrases:
        if phrase in summary:
            issues.append(Issue("WARN", rel(path), f"summary should not use phrase {phrase!r}", line=line, code="SUMMARY_STYLE"))


def check_wikilinks(path: Path, text: str, by_title: Dict[str, Dict[str, Any]], issues: List[Issue]) -> None:
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
    if data is not None and data.get("status") != "draft" and not links:
        issues.append(Issue("WARN", rel(path), "non-draft Argument has empty 来源 section", code="ARGUMENT_SOURCE_SECTION_EMPTY"))
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
        if "## 实证数据" not in body:
            issues.append(Issue("ERROR", rel(path), "concept template must include the mandatory conditional ## 实证数据 section", code="TEMPLATE_CONCEPT_EMPIRICAL_SECTION"))
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
        instrument_sections = [
            "工具定位",
            "测量构念与维度",
            "题项与作答方式",
            "使用该工具的研究",
            "版本与适配",
        ]
        for section in instrument_sections:
            if f"## {section}" not in body:
                issues.append(Issue("ERROR", rel(path), f"instrument template missing section: ## {section}", code="TEMPLATE_INSTRUMENT_SECTION_MISSING"))
        instrument_h2 = [line[3:].strip() for line in body.splitlines() if line.startswith("## ")]
        if instrument_h2 and instrument_h2[-1] != "版本与适配":
            issues.append(Issue("ERROR", rel(path), "instrument template must place ## 版本与适配 last", code="TEMPLATE_INSTRUMENT_VERSION_ORDER"))
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
            if expected_asset not in clean_body:
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
    title = data.get("title")
    if path.name in GENERATED_INDEX_FILES:
        return
    if r not in path_to_title:
        issues.append(Issue("WARN", r, "wiki entry is not present in wiki/index.json; run vault_index.py --wiki-only or check exclusions", code="ENTRY_NOT_INDEXED"))
    elif title and path_to_title.get(r) != title:
        issues.append(Issue("WARN", r, f"index title differs from frontmatter title: index={path_to_title.get(r)!r}, fm={title!r}", code="INDEX_TITLE_MISMATCH"))


def entry_metadata(path: Path) -> Optional[Dict[str, Any]]:
    try:
        text = read_text(path)
    except Exception:
        return None
    fm, _, _ = split_frontmatter(text)
    if not fm or yaml is None:
        return None
    try:
        data = yaml.safe_load(fm) or {}
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


def check_markdown_misc(path: Path, text: str, issues: List[Issue]) -> None:
    # Unclosed code fence.
    if text.count("```") % 2 != 0:
        issues.append(Issue("WARN", rel(path), "odd number of fenced code block markers ```", code="CODE_FENCE_UNCLOSED"))

    # DOI naked with problematic chars is just info.
    for m in DOI_RE.finditer(text):
        # If DOI is in markdown link URL, likely okay.
        issues.append(Issue("INFO", rel(path), f"DOI found; ensure special chars are safe or in frontmatter: {m.group(0)}", line=line_of_pos(text, m.start()), code="DOI_FOUND"))

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

    if is_wiki_entry_path(path) and "/arguments/" not in f"/{rel(path)}":
        source_subject_re = re.compile(
            r"(?:^|[。！？\n>|])\s*(?:[-*]\s*)?(?:\*\*[^*\n]+\*\*\s*)?"
            r"(论文|本文|本章|作者|研究者|本研究|本论证|第[一二三四五六七八九十百0-9]+章|全章)"
            r"\s*(认为|指出|发现|报告|显示|表明|提出|讨论|介绍|说明|分析|检验|考察|引用|援引|使用|采用|通过|将|把|未|没有|旨在|聚焦|关注|强调|主张)"
        )
        for m in source_subject_re.finditer(scan):
            subject = m.group(1)
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
        issues.append(
            Issue(
                "ERROR",
                rel(path),
                f"English annotation belongs inside the bold heading: **{chinese}{annotation}**",
                line=line_of_pos(scan, m.start(), body_start_line),
                code="BOLD_HEADING_ENGLISH_OUTSIDE",
            )
        )


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


def normalize_citation_alias_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"(?<=[A-Za-zÀ-ÖØ-öø-ÿ])\s*&\s*(?=[A-ZÀ-ÖØ-Þ])", " & ", text)
    return ENGLISH_AUTHOR_AND_RE.sub(" & ", text)


def has_english_author_and(text: str) -> bool:
    return bool(ENGLISH_AUTHOR_AND_RE.search(text))


def fix_english_author_and(text: str) -> str:
    return ENGLISH_AUTHOR_AND_RE.sub(" & ", text)


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


def citation_display_matches_aliases(display: str, aliases: List[str]) -> bool:
    display = display.strip()
    normalized_display = normalize_citation_alias_text(display)

    def author_year_key(text: str) -> str:
        text = normalize_citation_alias_text(text).strip("()（）[]【】 ")
        year_match = re.search(r"(?:19|20)\d{2}[a-z]?", text)
        if not year_match:
            return ""
        author = text[:year_match.start()].strip(" ,，([（")
        author = normalize_citation_alias_text(author).lower().rstrip(" .")
        return f"{author}|{year_match.group(0).lower()}" if author else ""

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


def strip_existing_wikilinks(text: str) -> str:
    def repl(m: re.Match) -> str:
        return " " * len(m.group(0))
    text = WIKILINK_RE.sub(repl, text)
    text = EMBED_RE.sub(repl, text)
    return text


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
            if has_english_author_and(display):
                issues.append(Issue("WARN", rel(path), f"English two-author citation should use '&': {display!r} -> {fix_english_author_and(display)!r}", line=line_of_pos(body_no_sources, m.start(), body_start_line), code="CITATION_ENGLISH_AND"))
            if not citation_display_matches_aliases(display, aliases):
                issues.append(Issue("WARN", rel(path), f"citation link display {display!r} does not match target citation_aliases {aliases!r}", line=line_of_pos(body_no_sources, m.start(), body_start_line), code="CITATION_LINK_TARGET_MISMATCH"))

    # Warn about raw, unlinked APA short citations.
    without_links = strip_existing_wikilinks(scan)
    for m in RAW_CITATION_RE.finditer(without_links):
        txt = m.group(1).strip()
        # Avoid matching page-only references and obvious template/examples.
        if not citation_display_text(txt):
            continue
        if has_english_author_and(txt):
            issues.append(Issue("WARN", rel(path), f"English two-author citation should use '&': {txt!r} -> {fix_english_author_and(txt)!r}", line=line_of_pos(body_no_sources, m.start(), body_start_line), code="CITATION_ENGLISH_AND"))
        has_matching_argument = any(
            citation_display_matches_aliases(txt, item.get("aliases", []))
            for item in argument_citations.values()
        )
        if has_matching_argument:
            issues.append(Issue("WARN", rel(path), f"APA short citation is not linked to an Argument: {txt}", line=line_of_pos(body_no_sources, m.start(), body_start_line), code="CITATION_UNLINKED"))


def lint_file(path: Path, by_title: Dict[str, Dict[str, Any]], path_to_title: Dict[str, str], argument_citations: Dict[str, Dict[str, Any]], issues: List[Issue]) -> None:
    try:
        text = read_text(path)
    except UnicodeDecodeError:
        issues.append(Issue("ERROR", rel(path), "cannot read as UTF-8", code="UTF8"))
        return

    check_old_references(path, text, issues)
    check_quartz_safety(path, text, issues)
    check_markdown_misc(path, text, issues)
    check_templater_placeholders(path, text, issues)

    data = check_frontmatter(path, text, by_title, issues)
    check_wikilinks(path, text, by_title, issues)
    check_sources_section(path, text, data, issues)
    check_template_consistency(path, text, issues)
    check_source_record(path, text, issues)
    check_path_and_index_consistency(path, data, path_to_title, issues)
    check_citation_links(path, text, data, argument_citations, issues)


def lint_vault(paths: List[Path], strict: bool = False, full: bool = False) -> List[Issue]:
    issues: List[Issue] = []
    check_required_files(issues)
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

    # Deduplicate preserving order.
    seen = set()
    unique_files = []
    for p in md_files:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            unique_files.append(p)

    for p in unique_files:
        lint_file(p, by_title, path_to_title, argument_citations, issues)

    argument_check_files = list(unique_files)
    # Even when lint is path-scoped, new extracted entries are a vault-level
    # invariant: they must be introduced from an Argument page. Include git
    # changed files so a new Person/Concept/etc. is not missed when the user
    # linted only the current Argument page.
    if paths:
        argument_check_files.extend(git_changed_md_files())
    check_new_entries_mentioned_in_arguments(argument_check_files, issues)
    check_citation_json_consistency(argument_citations, issues)

    return issues


# -----------------------------
# CLI
# -----------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Lint Obsidian / Quartz academic wiki vault.")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    parser.add_argument("--json", action="store_true", help="output JSON")
    parser.add_argument("--path", action="append", default=[], help="limit lint to path. Can be repeated. Overrides default git-incremental mode.")
    parser.add_argument("--full", action="store_true", help="lint the full vault instead of only git-changed Markdown files")
    parser.add_argument("--quiet", action="store_true", help="only print errors and summary")
    parser.add_argument("--show-info", action="store_true", help="include INFO items in text output")
    args = parser.parse_args()

    paths = [(ROOT / p).resolve() if not Path(p).is_absolute() else Path(p).resolve() for p in args.path]
    issues = lint_vault(paths, strict=args.strict, full=args.full)

    errors = [i for i in issues if i.severity == "ERROR"]
    warns = [i for i in issues if i.severity == "WARN"]
    infos = [i for i in issues if i.severity == "INFO"]

    if args.json:
        print(json.dumps([asdict(i) for i in issues], ensure_ascii=False, indent=2))
    else:
        for issue in issues:
            if args.quiet and issue.severity != "ERROR":
                continue
            if issue.severity == "INFO" and not args.show_info:
                continue
            print(issue.format())
        print()
        print(f"Summary: {len(errors)} error(s), {len(warns)} warning(s), {len(infos)} info item(s).")

    if errors:
        return 1
    if args.strict and warns:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
