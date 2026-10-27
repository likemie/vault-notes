#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vaultlib.py

Shared helpers for the vault scripts. Every script used to carry its own copy
of these functions, and the copies had drifted apart (four frontmatter
splitters, three hand-written YAML readers, three YAML quoting writers, six
ways to list git-changed files). One behaviour now lives here.

Contents
  bootstrap        ensure_venv()
  paths            ROOT, rel(), rel_to_root(), is_under()
  frontmatter      split_frontmatter(), frontmatter_raw(), parse_frontmatter_light()
                   upsert_generated_fields() preserves type-specific field ordering
  YAML scalars     parse_scalar(), parse_inline_list(), yaml_quote()
  wikilinks        WIKILINK_RE, parse_wikilink(), wikilink_display(), wikilink_target()
  git              git_output(), git_files_at_ref(), parse_name_status_z(),
                   git_status_paths(), git_diff_paths()
  JSON / files     load_json() (optional required reads), dump_json() (optional atomic
                   replace for task state), write_if_changed()
  text             has_cjk(), dedupe(), norm_doi(), normalized_source_language(),
                   author_label(), chinese_author_part(), asset_url_for_path()

Rules
  * Pure standard library: importing this module never needs the venv.
  * Behaviour changes go here, with a note; scripts keep thin adapters only
    where their callers need a different return shape.
"""

from __future__ import annotations

import io
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]


ASSET_BASE_URL = "https://img.mylikemie.icu"


# =============================================================================
# Bootstrap
# =============================================================================

def ensure_venv() -> None:
    """Re-run the current script with the vault venv (<vault>/.venv) when it exists.

    Call it only under `if __name__ == "__main__"`; modules imported by other
    scripts must not re-exec the importing process.

    The check compares sys.prefix with the venv directory. Comparing resolved
    interpreter paths (the earlier copies in four scripts) never fires, because
    .venv/bin/python is a symlink to the base interpreter. VAULT_VENV_REEXEC
    guards against loops.
    """
    if os.environ.get("VAULT_VENV_REEXEC") == "1" or os.environ.get("VAULT_LINT_VENV_REEXEC") == "1":
        return
    venv_dir = ROOT / ".venv"
    venv_python = venv_dir / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
    if not venv_python.exists():
        return
    try:
        if Path(sys.prefix).resolve() == venv_dir.resolve():
            return
    except OSError:
        return
    env = os.environ.copy()
    env["VAULT_VENV_REEXEC"] = "1"
    script = str(Path(sys.argv[0]).resolve()) if sys.argv and sys.argv[0] else ""
    os.execve(str(venv_python), [str(venv_python), script, *sys.argv[1:]], env)


# =============================================================================
# Paths
# =============================================================================

def rel(path: Path) -> str:
    """Vault-relative POSIX path; falls back to the path itself outside the vault.

    The literal path is tried first so symlinked folders (raw/ on the NAS) keep
    their in-vault spelling; the resolved path is the fallback.
    """
    path = Path(path)
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        pass
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (ValueError, OSError):
        return path.as_posix()


rel_to_root = rel


def is_under(path: Path, parent: Path) -> bool:
    try:
        Path(path).resolve().relative_to(Path(parent).resolve())
        return True
    except (ValueError, OSError):
        return False


# =============================================================================
# Frontmatter
# =============================================================================

class FrontmatterSplit:
    """Result of split_frontmatter().

    raw        YAML text between the delimiters (no surrounding newlines), or None
    head       text from the opening `---` through the closing delimiter line and
               its newline, i.e. exactly the bytes that precede `body`
    body       everything after the closing delimiter line
    body_line  1-based line number where `body` starts
    """

    __slots__ = ("raw", "head", "body", "body_line")

    def __init__(self, raw: str | None, head: str, body: str, body_line: int) -> None:
        self.raw, self.head, self.body, self.body_line = raw, head, body, body_line

    @property
    def found(self) -> bool:
        return self.raw is not None


def split_frontmatter(text: str) -> FrontmatterSplit:
    """The one frontmatter boundary rule used by every script.

    The file must start with a `---` line; the frontmatter ends at the first
    following line that is exactly `---` (trailing spaces / CR allowed). A line
    such as `----` or `--- x` does not close it. A file that ends right after
    the closing `---` (no final newline) is accepted.
    """
    if not (text.startswith("---\n") or text.startswith("---\r\n")):
        return FrontmatterSplit(None, "", text, 1)
    start = text.index("\n") + 1
    pos = start
    while True:
        nl = text.find("\n", pos)
        line_end = len(text) if nl == -1 else nl
        line = text[pos:line_end]
        if line.rstrip(" \t\r") == "---":
            raw = text[start:pos]
            if raw.endswith("\r\n"):
                raw = raw[:-2]
            elif raw.endswith("\n"):
                raw = raw[:-1]
            after = len(text) if nl == -1 else nl + 1
            head = text[:after]
            return FrontmatterSplit(raw, head, text[after:], head.count("\n") + 1)
        if nl == -1:
            return FrontmatterSplit(None, "", text, 1)
        pos = nl + 1


def frontmatter_raw(text: str) -> str | None:
    return split_frontmatter(text).raw


def upsert_generated_fields(
    raw: str, keys: set[str], generated: list[str], *,
    stop_after: tuple[str, ...], after: tuple[str, ...] = (),
    fallback_after: tuple[str, ...] = (),
) -> str:
    """Replace generated YAML fields, preserving each caller's anchor rules.

    Stop at the first stop_after key; otherwise use the last after key, or
    the first fallback_after key if no insertion position has been found.
    Existing generated block-list continuations are removed with their key.
    """
    lines = raw.rstrip("\n").splitlines()
    filtered: list[str] = []
    i = 0
    while i < len(lines):
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", lines[i])
        if match and match[1] in keys:
            i += 1
            while i < len(lines) and re.match(r"^(?:\s+|-\s)", lines[i]):
                i += 1
            continue
        filtered.append(lines[i])
        i += 1

    insert_at = 0
    for idx, line in enumerate(filtered):
        match = re.match(r"^([A-Za-z0-9_-]+):\s*", line)
        if not match:
            continue
        key = match[1]
        if key in stop_after:
            insert_at = idx + 1
            break
        if key in after or (key in fallback_after and insert_at == 0):
            insert_at = idx + 1
    filtered[insert_at:insert_at] = generated
    return "\n".join(filtered).rstrip() + "\n"


_KEY_RE = re.compile(r"^([A-Za-z0-9_][A-Za-z0-9_-]*):(?:\s+(.*)|\s*)$")
_LIST_ITEM_RE = re.compile(r"^\s*-\s+(.*)$|^\s*-\s*$")


def parse_frontmatter_light(raw: str | None) -> dict[str, Any]:
    """Small, dependency-free reader for the flat frontmatter this vault uses.

    Supports `key: scalar`, `key: [a, b]` and block lists (`key:` followed by
    `- item` lines). Scalars follow YAML quoting rules (see parse_scalar). An
    empty value with no list items reads as "". Comment lines are skipped.
    Use PyYAML (vault_lint, source_record) when nested structures matter.
    """
    data: dict[str, Any] = {}
    if not raw:
        return data
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        m = _KEY_RE.match(line)
        if not m:
            i += 1
            continue
        key, val = m.group(1), (m.group(2) or "").strip()
        if val == "":
            items: list[str] = []
            j = i + 1
            while j < len(lines):
                item = _LIST_ITEM_RE.match(lines[j])
                if item:
                    items.append(parse_scalar(item.group(1) or ""))
                    j += 1
                    continue
                if not lines[j].strip() or lines[j].lstrip().startswith("#"):
                    j += 1
                    continue
                break
            data[key] = items if items else ""
            i = j
            continue
        if val.startswith("[") and val.endswith("]"):
            data[key] = parse_inline_list(val)
        else:
            data[key] = parse_scalar(val)
        i += 1
    return data


# =============================================================================
# YAML scalars
# =============================================================================

_DQ_ESCAPES = {
    "0": "\0", "a": "\a", "b": "\b", "t": "\t", "\t": "\t", "n": "\n", "v": "\v",
    "f": "\f", "r": "\r", "e": "\x1b", " ": " ", '"': '"', "/": "/", "\\": "\\",
    "N": "\x85", "_": "\xa0", "L": "\u2028", "P": "\u2029",
}


def _unescape_double_quoted(inner: str) -> str:
    out: list[str] = []
    i = 0
    while i < len(inner):
        ch = inner[i]
        if ch != "\\" or i + 1 >= len(inner):
            out.append(ch)
            i += 1
            continue
        nxt = inner[i + 1]
        width = {"x": 2, "u": 4, "U": 8}.get(nxt)
        if width:
            digits = inner[i + 2:i + 2 + width]
            if len(digits) == width and all(c in "0123456789abcdefABCDEF" for c in digits):
                out.append(chr(int(digits, 16)))
                i += 2 + width
                continue
        if nxt in _DQ_ESCAPES:
            out.append(_DQ_ESCAPES[nxt])
            i += 2
            continue
        # Not a YAML escape: keep it verbatim (lenient, PyYAML would reject it).
        out.append(ch)
        i += 1
    return "".join(out)


def parse_scalar(value: str) -> str:
    """Read one YAML scalar as text.

    Double-quoted values are unescaped (\\" -> ", \\\\ -> \\), single-quoted
    values turn '' into ', and plain values drop a trailing ` # comment`.
    null / ~ / empty read as "".

    Before vaultlib the readers kept backslashes, so a citation containing
    \\"...\\" was re-escaped on every write (Eisenhart & Towne 2003 had grown
    to \\\\\\"scientifically based\\\\\\").
    """
    value = value.strip()
    if value in {"", "null", "Null", "NULL", "None", "~"}:
        return ""
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return _unescape_double_quoted(value[1:-1])
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    hash_at = value.find(" #")
    if hash_at != -1:
        value = value[:hash_at].rstrip()
    return value


def parse_inline_list(value: str) -> list[str]:
    """Read a YAML flow list `[a, "b, c", 'd']`; empty items are dropped."""
    value = value.strip()
    inner = value[1:-1].strip() if value.startswith("[") and value.endswith("]") else value
    if not inner:
        return []
    items: list[str] = []
    current: list[str] = []
    quote = ""
    escape = False
    for ch in inner:
        if escape:
            current.append(ch)
            escape = False
            continue
        if ch == "\\" and quote == '"':
            current.append(ch)
            escape = True
            continue
        if ch in {"'", '"'}:
            # A quote opens a quoted item only at its start; an apostrophe
            # inside a plain item (Occam's razor) is text.
            if not quote and not "".join(current).strip():
                quote = ch
            elif quote == ch:
                quote = ""
            current.append(ch)
            continue
        if ch == "," and not quote:
            items.append(parse_scalar("".join(current)))
            current = []
            continue
        current.append(ch)
    if "".join(current).strip():
        items.append(parse_scalar("".join(current)))
    return [item for item in items if item]


def yaml_quote(value: str) -> str:
    """Write text as a double-quoted YAML scalar (round-trips with parse_scalar)."""
    escaped = str(value).replace("\\", "\\\\").replace('"', '\\"')
    escaped = escaped.replace("\n", "\\n").replace("\t", "\\t")
    return f'"{escaped}"'


def strip_yaml_quotes(value: str) -> str:
    return parse_scalar(value)


# =============================================================================
# Wikilinks
# =============================================================================

# [[target#heading|display]]; the pipe may be escaped (\|) inside tables.
WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\[\]\n]+?)\]\]")
WIKILINK_PARTS_RE = re.compile(
    r"\[\[(?P<target>[^\]|#\\\n]+?)(?:#(?P<heading>[^\]|\\\n]*))?(?:\\?\|(?P<display>[^\]\n]+))?\]\]"
)


def parse_wikilink(inner: str) -> tuple[str, str | None]:
    """Split the text inside [[...]] into (target, display).

    The first pipe wins, escaped (\\|, used inside tables) or not. The target
    loses any #heading or ^block suffix; display is None when absent.
    """
    idx = inner.find("|")
    if idx == -1:
        target, display = inner, None
    else:
        target = inner[:idx - 1] if idx > 0 and inner[idx - 1] == "\\" else inner[:idx]
        display = inner[idx + 1:]
    target = target.split("#", 1)[0].split("^", 1)[0].strip()
    return target, (display.strip() if display is not None else None)


def wikilink_target(text: str) -> str:
    """Target of the first wikilink in text, or ""."""
    m = WIKILINK_RE.search(text or "")
    return parse_wikilink(m.group(1))[0] if m else ""


def wikilink_display(value: str) -> str:
    """`[[T|D]]` -> D, `[[T]]` -> T; other text is returned stripped."""
    value = str(value or "").strip()
    m = re.fullmatch(r"\[\[([^\]]+)\]\]", value)
    if not m:
        return value
    target, display = parse_wikilink(m.group(1))
    return (display or target).strip()


def strip_wikilinks(value: str) -> str:
    """Replace every wikilink with its visible text."""
    return WIKILINK_RE.sub(lambda m: (lambda t, d: d or t)(*parse_wikilink(m.group(1))), value)


# =============================================================================
# Git
# =============================================================================

def git_output(args: list[str], *, cwd: Path = ROOT) -> str:
    """stdout of a git command ("" on failure); paths are never quoted."""
    try:
        result = subprocess.run(
            ["git", "-c", "core.quotePath=false", *args],
            cwd=cwd, check=False, capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
    except OSError:
        return ""
    return result.stdout if result.returncode == 0 else ""


def git_files_at_ref(ref: str, rel_paths: Iterable[str]) -> dict[str, str]:
    """Read many files at a ref with one `git cat-file --batch` process.

    Missing paths are skipped; a malformed stream keeps what was read so far.
    """
    paths = list(rel_paths)
    if not paths:
        return {}
    request = "".join(f"{ref}:{p}\n" for p in paths).encode("utf-8")
    try:
        result = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT, input=request,
                                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False)
    except OSError:
        return {}
    stream = io.BytesIO(result.stdout)
    files: dict[str, str] = {}
    for p in paths:
        header = stream.readline().rstrip(b"\n")
        if not header or header.endswith(b" missing"):
            continue
        try:
            size = int(header.rsplit(b" ", 1)[1])
        except (IndexError, ValueError):
            break
        files[p] = stream.read(size).decode("utf-8", errors="replace")
        stream.read(1)  # newline after each object
    return files


def parse_name_status_z(output: str) -> set[str]:
    """Paths from `git diff --name-status -z`; renames/copies give both sides."""
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
    return {p for p in paths if p}


def git_status_paths(pathspecs: Iterable[str], *, include_deleted: bool = False) -> list[str]:
    """Changed + untracked paths from `git status` (vault-relative, NFC).

    `git status` also refreshes the index stat cache, which keeps later git
    calls fast (a bare `git diff HEAD` re-verifies every stale entry: ~8 s vs
    ~0.1 s on this vault). Renames report the new path. Deleted paths are
    dropped unless include_deleted.
    """
    out = git_output(["status", "--porcelain=v1", "-z", "--untracked-files=all", "--", *pathspecs])
    parts = out.split("\0")
    paths: list[str] = []
    i = 0
    while i < len(parts):
        item = parts[i]
        i += 1
        if len(item) < 4:
            continue
        status, path = item[:2], item[3:]
        if status[0] in "RC":
            i += 1  # -z emits the rename source after the destination
        if "D" in status and not include_deleted:
            continue
        paths.append(unicodedata.normalize("NFC", path))
    return sorted(set(paths))


def git_diff_paths(base: str, head: str = "HEAD", pathspecs: Iterable[str] = (), *,
                   diff_filter: str = "ACMR") -> list[str]:
    """Paths changed between two commits (vault-relative, NFC)."""
    out = git_output(["diff", "--name-only", f"--diff-filter={diff_filter}", "-z", base, head, "--", *pathspecs])
    return sorted({unicodedata.normalize("NFC", p) for p in out.split("\0") if p})


# =============================================================================
# JSON / files
# =============================================================================

def load_json(path: Path, default: Any = None, *, required: bool = False) -> Any:
    """Parse JSON (UTF-8 BOM accepted); required=True raises on missing files."""
    path = Path(path)
    if not required and not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump_json(
    path: Path, data: Any, *, indent: int = 1, sort_keys: bool = False, atomic: bool = False,
) -> None:
    """Write JSON; atomic=True preserves related-update state via sibling replace."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    destination = path.with_suffix(path.suffix + ".tmp") if atomic else path
    destination.write_text(json.dumps(data, ensure_ascii=False, indent=indent, sort_keys=sort_keys) + "\n",
                           encoding="utf-8")
    if atomic:
        destination.replace(path)


def write_if_changed(path: Path, content: str, *, dry_run: bool = False, check: bool = False) -> bool:
    """Write content unless identical; returns True when the file is (or would be) changed."""
    path = Path(path)
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if current == content:
        return False
    if not dry_run and not check:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return True


# =============================================================================
# Text
# =============================================================================

_CJK_RE = re.compile(r"[\u3400-\u9fff]")


def has_cjk(text: str) -> bool:
    return bool(_CJK_RE.search(text or ""))


def dedupe(items: Iterable[Any]) -> list[Any]:
    """Keep first occurrences, drop empty values."""
    seen: set[Any] = set()
    result: list[Any] = []
    for item in items:
        if item and item not in seen:
            result.append(item)
            seen.add(item)
    return result


def norm_doi(value: Any) -> str:
    """Bare lower-case DOI: drops https://doi.org/, dx.doi.org and doi: prefixes."""
    text = str(value or "").strip()
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^doi:\s*", "", text, flags=re.IGNORECASE)
    return text.lower()


def normalized_source_language(value: Any) -> str:
    language = str(value or "").strip().lower().replace("_", "-")
    if language in {"zh", "zh-cn", "zh-hans", "chinese", "中文"}:
        return "zh"
    if language in {"en", "en-us", "en-gb", "english", "英文"}:
        return "en"
    return language


def author_label(author: Any) -> str:
    """Family-name label of one `authors` item (`[[Person|Ball, S. J.]]` -> Ball)."""
    text = wikilink_display(str(author or "")).replace("''", "'")
    text = re.sub(r"\s+", " ", text).strip()
    if "," in text:
        return text.split(",", 1)[0].strip()
    return text


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


def asset_url_for_path(path: Path) -> str:
    encoded = "/".join(quote(part, safe="-_.!~*'()") for part in rel(path).split("/"))
    return f"{ASSET_BASE_URL}/{encoded}"
