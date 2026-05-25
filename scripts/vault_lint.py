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
import re
import sys
import subprocess
import unicodedata
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

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
    "journal",
    "book_title",
    "authors",
    "editors",
    "publisher",
    "part_of",
    "confidence",
    "status",
    "created",
    "updated",
]

VALID_TYPES = {
    "concept",
    "theory",
    "method",
    "person",
    "fact",
    "argument",
    "source",
}

TYPE_PATH_HINTS = {
    "concept": "wiki/concepts/",
    "theory": "wiki/theories/",
    "method": "wiki/methods/",
    "person": "wiki/persons/",
    "fact": "wiki/facts/",
    "argument": "wiki/arguments/",
}

TYPE_TO_RELATED_FIELD = {
    "concept": "related_concepts",
    "theory": "related_theories",
    "method": "related_methods",
    "person": "related_persons",
    "fact": "related_facts",
    "argument": "related_arguments",
}

FORBIDDEN_SUMMARY_CHARS = [":", '"', "'", "_"]

TAG_RE = re.compile(r"^[a-z0-9]+(?:[-/][a-z0-9]+)*$")

WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
EMBED_RE = re.compile(r"!\[\[([^\]\n]+)\]\]")

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)

EMBED_FILE_EXISTS_CACHE: Dict[str, bool] = {}


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


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def line_of_pos(text: str, pos: int, offset: int = 1) -> int:
    return text[:pos].count("\n") + offset


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
    Return target before | and #.
    """
    target = raw.split("|", 1)[0].strip()
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
        issues.append(Issue("ERROR", rel(INDEX_JSON), "missing wiki/index.json. Run python3 scripts/wiki_index.py first.", code="INDEX_MISSING"))
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
        ROOT / "scripts" / "wiki_index.py",
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
    if is_wiki_entry_path(path) and typ in {"concept", "theory", "method", "person", "fact"} and "aliases" not in data:
        issues.append(Issue("WARN", rel(path), f"type {typ!r} should include aliases field", code="ALIASES_MISSING"))

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

    banned_phrases = ["本文研究", "作者认为", "本研究发现", "本论文", "本章认为", "本文认为"]
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
    source_sec = section_text(body, ["来源", "Sources"])
    if "## 来源" not in body and "## Sources" not in body:
        issues.append(Issue("WARN", rel(path), "missing ## 来源 / ## Sources section", code="SOURCE_SECTION_MISSING"))
        return

    links = [target for target, _ in extract_wikilinks(source_sec)]
    if data is not None and data.get("status") != "draft" and not links:
        issues.append(Issue("WARN", rel(path), "non-draft entry has empty 来源 section", code="SOURCE_SECTION_EMPTY"))


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
    common = ["title", "summary", "type", "tags", "sources", "status", "created", "updated"]
    for field in common:
        if field not in data:
            issues.append(Issue("WARN", rel(path), f"template missing common field: {field}", code="TEMPLATE_FIELD_MISSING"))

    for field in RELATED_FIELDS:
        if field not in data:
            issues.append(Issue("WARN", rel(path), f"template missing relation field: {field}", code="TEMPLATE_REL_MISSING"))

    if typ == "argument" and "aliases" in data:
        issues.append(Issue("WARN", rel(path), "argument template should not include aliases", code="TEMPLATE_ARGUMENT_ALIASES"))
    if typ in {"concept", "theory", "method", "person", "fact"} and "aliases" not in data:
        issues.append(Issue("WARN", rel(path), f"{typ} template should include aliases", code="TEMPLATE_ALIASES_MISSING"))

    if "## 来源" not in body and "## Sources" not in body:
        issues.append(Issue("WARN", rel(path), "template missing ## 来源 / ## Sources section", code="TEMPLATE_SOURCE_SECTION"))


def check_source_record(path: Path, text: str, issues: List[Issue]) -> None:
    if not is_source_record_path(path) and not ("/books/" in rel(path)):
        return
    fm, body, _ = split_frontmatter(text)
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

    if "processed_date" not in data:
        issues.append(Issue("WARN", rel(path), "source record missing processed_date", code="PROCESSED_DATE_MISSING"))

    # Source record should embed a PDF or EPUB viewer, unless it is some special source.
    if "![[ " in body:
        issues.append(Issue("WARN", rel(path), "possible malformed embed with space after [[", code="EMBED_SPACE"))


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
        issues.append(Issue("WARN", r, "wiki entry is not present in wiki/index.json; run wiki_index.py or check exclusions", code="ENTRY_NOT_INDEXED"))
    elif title and path_to_title.get(r) != title:
        issues.append(Issue("WARN", r, f"index title differs from frontmatter title: index={path_to_title.get(r)!r}, fm={title!r}", code="INDEX_TITLE_MISMATCH"))


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


def lint_file(path: Path, by_title: Dict[str, Dict[str, Any]], path_to_title: Dict[str, str], issues: List[Issue]) -> None:
    try:
        text = read_text(path)
    except UnicodeDecodeError:
        issues.append(Issue("ERROR", rel(path), "cannot read as UTF-8", code="UTF8"))
        return

    check_old_references(path, text, issues)
    check_quartz_safety(path, text, issues)
    check_markdown_misc(path, text, issues)

    data = check_frontmatter(path, text, by_title, issues)
    check_wikilinks(path, text, by_title, issues)
    check_sources_section(path, text, data, issues)
    check_template_consistency(path, text, issues)
    check_source_record(path, text, issues)
    check_path_and_index_consistency(path, data, path_to_title, issues)


def lint_vault(paths: List[Path], strict: bool = False, full: bool = False) -> List[Issue]:
    issues: List[Issue] = []
    check_required_files(issues)
    by_title, path_to_title = load_index(issues)

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
        lint_file(p, by_title, path_to_title, issues)

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

    paths = [Path(p) for p in args.path]
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
