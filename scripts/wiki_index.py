#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

# Auto-use the vault virtual environment when available.
# This keeps scripts runnable as `python3 scripts/<script>.py` while using
# dependencies installed in /Users/shaoyangwu/Documents/MyNotes/.venv.
import os
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = VAULT_ROOT / ".venv" / "bin" / "python"

# Only when run as a script: wiki_linker.py imports this module for the
# organization registry and must not be re-executed.
if __name__ == "__main__" and VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])


import argparse
import json
import re
import unicodedata
from typing import Any, Iterable

ROOT = VAULT_ROOT
WIKI_DIR = ROOT / "wiki"

# Machine index for AI lookup.
INDEX_JSON = WIKI_DIR / "index.json"

# Human-readable static Markdown index for Obsidian / Quartz / GitHub.
INDEX_MD = WIKI_DIR / "index.md"

# Per-type local indexes. These are generated too; do not edit manually.
LOCAL_INDEX_FILES = {
    "concept": WIKI_DIR / "concepts" / "index.md",
    "theory": WIKI_DIR / "theories" / "index.md",
    "method": WIKI_DIR / "methods" / "index.md",
    "instrument": WIKI_DIR / "instruments" / "index.md",
    "person": WIKI_DIR / "persons" / "index.md",
    "fact": WIKI_DIR / "facts" / "index.md",
    "argument": WIKI_DIR / "arguments" / "index.md",
}

EXCLUDE_DIR_PARTS = {"templates", "indexes", ".obsidian"}
EXCLUDE_FILENAMES = {
    "index.md",
    "index.json",
    "manifest.md",
    "manifest.json",
}

TYPE_ORDER = ["concept", "theory", "method", "instrument", "person", "fact", "argument", "source", "unknown"]

TYPE_LABELS = {
    "concept": "Concepts",
    "theory": "Theories",
    "method": "Methods",
    "instrument": "Instruments",
    "person": "Persons",
    "fact": "Facts",
    "argument": "Arguments",
    "source": "Sources",
    "unknown": "Unknown",
}

TYPE_DIRS = {
    "concept": "concepts",
    "theory": "theories",
    "method": "methods",
    "instrument": "instruments",
    "person": "persons",
    "fact": "facts",
    "argument": "arguments",
}

SECOND_LEVEL_LABELS = {
    "journal-articles": "Journal Articles",
    "books": "Books",
    "reports-policy-documents": "Reports & Policy Documents",
    "qualitative": "Qualitative",
    "quantitative": "Quantitative",
    "mixed": "Mixed",
    "scales": "Scales",
    "questionnaires": "Questionnaires",
    "tests": "Tests",
    "inventories": "Inventories",
    "rubrics": "Rubrics",
    "checklists": "Checklists",
    "observation-tools": "Observation Tools",
    "interview-tools": "Interview Tools",
    "comparative-education": "Comparative Education",
    "curriculum": "Curriculum",
    "educational-philosophy": "Educational Philosophy",
    "sociology-of-education": "Sociology of Education",
    "globalization-and-education": "Globalization and Education",
    "policy-studies": "Policy Studies",
    "methodology": "Methodology",
    "global": "Global",
    "multi": "Multi-country",
    "schools": "Schools",
    "us": "US",
    "uk": "UK",
    "eu": "EU",
    "hongkong": "Hong Kong",
    "newzealand": "New Zealand",
}

LIST_KEYS = {
    "aliases",
    "tags",
    "sources",
    "authors",
    "editors",
    "developers",
    "languages",
    "related_concepts",
    "related_theories",
    "related_methods",
    "related_instruments",
    "related_persons",
    "related_facts",
    "related_arguments",
    "extracted_to",
}


def title_case_slug(slug: str) -> str:
    if not slug:
        return "Uncategorized"
    if slug in SECOND_LEVEL_LABELS:
        return SECOND_LEVEL_LABELS[slug]
    return " ".join(part.capitalize() for part in slug.replace("_", "-").split("-"))


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and ((value[0] == value[-1] == '"') or (value[0] == value[-1] == "'")):
        value = value[1:-1]
    return value.strip()


def parse_inline_list(value: str) -> list[str]:
    inner = value[1:-1].strip()
    if not inner:
        return []

    items: list[str] = []
    current = ""
    quote: str | None = None

    for ch in inner:
        if ch in ("'", '"'):
            if quote == ch:
                quote = None
            elif quote is None:
                quote = ch
            current += ch
        elif ch == "," and quote is None:
            if current.strip():
                items.append(clean_scalar(current.strip()))
            current = ""
        else:
            current += ch

    if current.strip():
        items.append(clean_scalar(current.strip()))

    return items


def extract_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        return {}

    end = text.find("\n---", 4)
    if end == -1:
        return {}

    raw = text[4:end].strip("\n")
    data: dict[str, Any] = {}
    current_key: str | None = None

    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        if current_key and re.match(r"^\s*-\s+", line):
            item = re.sub(r"^\s*-\s+", "", line).strip()
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(clean_scalar(item))
            continue

        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            current_key = None
            continue

        key, value = m.group(1), m.group(2).strip()
        current_key = None

        if value == "":
            if key in LIST_KEYS:
                data[key] = []
                current_key = key
            else:
                data[key] = ""
                current_key = key
        elif value.startswith("[") and value.endswith("]"):
            data[key] = parse_inline_list(value)
        else:
            data[key] = clean_scalar(value)

    for list_key in LIST_KEYS:
        if data.get(list_key) is None:
            data[list_key] = []

    return data


def normalize_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]
    if isinstance(value, str):
        return [value.strip()] if value.strip() else []
    return []


def should_skip(path: Path) -> bool:
    rel = path.relative_to(WIKI_DIR)
    if path.name in EXCLUDE_FILENAMES:
        return True
    return any(part in EXCLUDE_DIR_PARTS for part in rel.parts)


def infer_type_from_path(path: Path) -> str:
    parts = path.relative_to(WIKI_DIR).parts
    if not parts:
        return "unknown"
    reverse = {v: k for k, v in TYPE_DIRS.items()}
    return reverse.get(parts[0], "unknown")


def second_level_from_path(path: Path, entry_type: str) -> str:
    parts = path.relative_to(WIKI_DIR).parts
    type_dir = TYPE_DIRS.get(entry_type)
    if not type_dir or len(parts) < 2 or parts[0] != type_dir:
        return "uncategorized"
    return parts[1]


def third_folder_from_path(path: Path, entry_type: str) -> str:
    parts = path.relative_to(WIKI_DIR).parts
    type_dir = TYPE_DIRS.get(entry_type)
    if not type_dir or len(parts) < 3 or parts[0] != type_dir:
        return ""
    return parts[2]


# =============================================================================
# Organization registry (formerly scripts/org_registry.py)
#
# Organization registry for YAML `issuing_organization` links.
#
# Organization entries are Fact pages with `subtype: organization`. They play the
# same role for report / policy metadata that Person pages play for `authors`:
# `wiki_linker.py` links a name in `issuing_organization` when it equals an
# organization title, alias, or a registered variant.
#
# Registry file: wiki/organizations.json (written by `wiki_index.py`)
#
#   variants       EDITABLE. "name as written" -> "organization entry title".
#                  Use it for spellings that should link but do not belong in the
#                  entry's aliases (e.g. "美国国会（United States Congress）").
#                  Entries here are kept on every rebuild.
#   organizations  GENERATED. Every organization entry with its path and all
#                  names that link to it (title + aliases + variants).
#   unresolved     GENERATED. Names found in issuing_organization that match no
#                  organization, with seen_in paths. Create an organization Fact,
#                  add an alias, or add a variant to resolve one; it then
#                  disappears on the next index run.
#   invalid_variants GENERATED. Variants whose target is not an organization entry.
# =============================================================================

ORG_REGISTRY_JSON = ROOT / "wiki" / "organizations.json"

ORG_NOTE = (
    "variants is editable: map a name as written in issuing_organization to an organization "
    "Fact title. organizations, unresolved and invalid_variants are generated by "
    "scripts/wiki_index.py; scripts/wiki_linker.py links issuing_organization from "
    "organization titles, aliases and variants."
)

ORG_PAREN_RE = re.compile(r"^(?P<outer>[^（()）,，、;；&/]+?)\s*[（(](?P<inner>[^（()）]+)[）)]\s*$")
ORG_ABBREVIATION_RE = re.compile(r"^[A-Za-z0-9.&\-/]{1,12}$")
ORG_STRONG_SEP_RE = re.compile(r"(\s*(?:,|，|、|;|；|&)\s*|\s*/\s+|\s+/\s*)")
ORG_WEAK_SEP_RE = re.compile(r"(\s+and\s+|\s*(?:与|及)\s*)")
WIKILINK_DISPLAY_RE = re.compile(r"\[\[([^\]|]+?)(?:\\?\|([^\]]+))?\]\]")


def normalize_name(value: str) -> str:
    value = value.strip().strip("'\"").strip()
    value = re.sub(r"\s+", " ", value)
    return value.rstrip(".").strip().casefold()


def strip_wikilinks(value: str) -> str:
    """[[Target|Display]] -> Display, [[Target]] -> Target."""
    return WIKILINK_DISPLAY_RE.sub(lambda m: m.group(2) or m.group(1), value)


# --- registry file ------------------------------------------------------------

def load_registry(path: Path = ORG_REGISTRY_JSON) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def load_variants(path: Path = ORG_REGISTRY_JSON) -> dict[str, str]:
    raw = load_registry(path).get("variants") or {}
    if not isinstance(raw, dict):
        return {}
    return {str(k).strip(): str(v).strip() for k, v in raw.items() if str(k).strip() and str(v).strip()}


def build_name_map(
    organizations: Iterable[tuple[str, Iterable[str]]],
    variants: dict[str, str] | None = None,
) -> dict[str, str]:
    """normalized name -> organization title, from (title, aliases) pairs plus variants."""
    mapping: dict[str, str] = {}
    titles: set[str] = set()
    for title, aliases in organizations:
        titles.add(title)
        for raw in (title, *aliases):
            key = normalize_name(str(raw))
            if key:
                mapping.setdefault(key, title)
    for name, target in (variants or {}).items():
        key = normalize_name(name)
        if key and target in titles:
            mapping.setdefault(key, target)
    return mapping


# --- matching -----------------------------------------------------------------

def match_segment(segment: str, name_map: dict[str, str]) -> str | None:
    seg = segment.strip()
    if not seg:
        return None
    target = name_map.get(normalize_name(seg))
    if target:
        return target
    m = ORG_PAREN_RE.match(seg)
    if not m:
        return None
    # 中文名（English Name, ABBR） / English Name (ABBR): the name itself or a
    # full name in the parentheses may identify it. A bare abbreviation in the
    # parentheses is not enough (奥地利联邦教育部（BMBF） is not German BMBF).
    inner_parts = [part for part in re.split(r"\s*[,，]\s*", m.group("inner")) if part]
    candidates = [m.group("outer")] + [
        part for part in [m.group("inner"), *inner_parts] if not ORG_ABBREVIATION_RE.match(part.strip())
    ]
    found = {name_map.get(normalize_name(c)) for c in candidates} - {None}
    return found.pop() if len(found) == 1 else None


def split_outside_parens(text: str, sep_re: re.Pattern[str]) -> list[str]:
    """Like sep_re.split (separators at odd indexes), ignoring separators in （）/()."""
    depth_at: list[int] = []
    depth = 0
    for ch in text:
        if ch in "（(":
            depth += 1
        depth_at.append(depth)
        if ch in "）)":
            depth = max(0, depth - 1)
    pieces: list[str] = []
    last = 0
    for m in sep_re.finditer(text):
        if m.start() == m.end() or depth_at[m.start()] or depth_at[m.end() - 1]:
            continue
        pieces.extend([text[last:m.start()], m.group(0)])
        last = m.end()
    pieces.append(text[last:])
    return pieces


def resolve(text: str, name_map: dict[str, str]) -> list[tuple[str, str | None, bool]]:
    """Split a value into (piece, target, is_separator) triples.

    The whole value is tried first, then strong separators (, ; & /), then weak
    separators (and / 与 / 及) inside pieces that still do not match.
    """
    target = match_segment(text, name_map)
    if target:
        return [(text, target, False)]
    parts = _resolve_parts(text, name_map, ORG_STRONG_SEP_RE)
    # Nothing matched: keep the value whole, so "Department for Science,
    # Innovation and Technology" is reported as one unresolved name.
    return parts if any(t for _, t, _ in parts) else [(text, None, False)]


def _resolve_parts(text: str, name_map: dict[str, str], sep_re: re.Pattern[str]) -> list[tuple[str, str | None, bool]]:
    pieces = split_outside_parens(text, sep_re)
    if len(pieces) == 1:
        if sep_re is ORG_STRONG_SEP_RE:
            return _resolve_parts(text, name_map, ORG_WEAK_SEP_RE)
        return [(text, None, False)]
    out: list[tuple[str, str | None, bool]] = []
    for idx, piece in enumerate(pieces):
        if idx % 2 == 1:
            out.append((piece, None, True))
            continue
        target = match_segment(piece, name_map)
        if target or sep_re is not ORG_STRONG_SEP_RE:
            out.append((piece, target, False))
            continue
        sub = _resolve_parts(piece, name_map, ORG_WEAK_SEP_RE)
        # Keep an unmatched strong-level piece whole for reporting when the
        # weak split found nothing either ("Department for Science, Innovation and Technology").
        out.extend(sub if any(t for _, t, _ in sub) else [(piece, None, False)])
    return out


def unresolved_names(value: str, name_map: dict[str, str]) -> list[str]:
    text = strip_wikilinks(value).strip().strip("'\"").strip()
    if not text:
        return []
    # Report runs of unmatched pieces together, so "Department for Science,
    # Innovation and Technology, [[Cabinet Office]]" yields one name.
    names: list[str] = []
    run: list[str] = []
    def flush() -> None:
        joined = "".join(run).strip().strip(",，、;；&/ ").strip()
        if joined:
            names.append(joined)
        run.clear()

    for piece, target, _is_sep in resolve(text, name_map):
        if target:
            flush()
        else:
            run.append(piece)
    flush()
    return names


# --- generation (called from wiki_index.py) ------------------------------------

def build_registry(entries: list[dict[str, Any]], variants: dict[str, str]) -> dict[str, Any]:
    orgs = sorted(
        (e for e in entries if e.get("type") == "fact" and e.get("subtype") == "organization"),
        key=lambda e: e["title"].casefold(),
    )
    titles = {e["title"] for e in orgs}
    name_map = build_name_map(((e["title"], e.get("aliases") or []) for e in orgs), variants)

    organizations: dict[str, Any] = {}
    for e in orgs:
        names = [e["title"], *(e.get("aliases") or [])]
        names += sorted(n for n, t in variants.items() if t == e["title"])
        seen: set[str] = set()
        uniq = [n for n in names if not (normalize_name(n) in seen or seen.add(normalize_name(n)))]
        organizations[e["title"]] = {"path": e["path"], "names": uniq}

    unresolved: dict[str, dict[str, list[str]]] = {}
    for e in entries:
        value = str(e.get("issuing_organization") or "")
        if not value or e["path"].startswith("wiki/templates/"):
            continue
        for name in unresolved_names(value, name_map):
            if name == e.get("title"):
                continue
            unresolved.setdefault(name, {"seen_in": []})["seen_in"].append(e["path"])
    for item in unresolved.values():
        item["seen_in"] = sorted(set(item["seen_in"]))

    return {
        "_note": ORG_NOTE,
        "variants": dict(sorted(variants.items(), key=lambda kv: kv[0].casefold())),
        "invalid_variants": sorted(k for k, v in variants.items() if v not in titles),
        "organizations": organizations,
        "unresolved": dict(sorted(unresolved.items(), key=lambda kv: (-len(kv[1]["seen_in"]), kv[0].casefold()))),
    }


def render_registry(entries: list[dict[str, Any]], path: Path = ORG_REGISTRY_JSON) -> str:
    data = build_registry(entries, load_variants(path))
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def third_level(entry: dict[str, Any]) -> str:
    typ = entry["type"]
    second = entry.get("second_level", "")
    third_folder = entry.get("third_folder", "")

    if typ == "argument":
        if second == "books":
            return third_folder or entry.get("book_title") or "Unknown Book"
        if second == "journal-articles":
            return entry.get("journal") or "Unknown Journal"
        if second == "reports-policy-documents":
            return entry.get("issuing_organization") or "Unknown Organization"

        subtype = entry.get("subtype", "")
        if subtype == "journal-article":
            return entry.get("journal") or "Unknown Journal"
        if subtype in {"monograph", "edited-volume", "book-chapter"}:
            return third_folder or entry.get("book_title") or "Unknown Book"
        if subtype in {"report", "policy-document"}:
            return entry.get("issuing_organization") or "Unknown Organization"
        return third_folder or "Other"

    if typ == "fact":
        return entry.get("subtype") or "unknown"

    if typ == "person":
        if second == "schools" or entry.get("subtype") == "school":
            return "school"
        return entry.get("nationality") or "unknown"

    return ""


def collect_entries() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []

    for path in sorted(WIKI_DIR.rglob("*.md")):
        if should_skip(path):
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        fm = extract_frontmatter(text)
        # APFS hands back NFD names (e.g. "Håkansson"), while titles typed in
        # links are NFC. Index NFC forms so titles, paths and folder groups match.
        path = Path(unicodedata.normalize("NFC", str(path)))

        typ = str(fm.get("type") or infer_type_from_path(path)).strip()
        entry = {
            "title": unicodedata.normalize("NFC", str(fm.get("title") or path.stem).strip()),
            "type": typ,
            "subtype": str(fm.get("subtype") or "").strip(),
            "second_level": second_level_from_path(path, typ),
            "third_folder": third_folder_from_path(path, typ),
            "path": path.relative_to(ROOT).as_posix(),
            "aliases": normalize_list(fm.get("aliases")),
            "tags": normalize_list(fm.get("tags")),
            "summary": str(fm.get("summary") or "").strip(),
            # These are only used to generate index.md group headings.
            "journal": str(fm.get("journal") or "").strip(),
            "book_title": str(fm.get("book_title") or "").strip(),
            "issuing_organization": strip_wikilinks(str(fm.get("issuing_organization") or "").strip()),
            "nationality": str(fm.get("nationality") or "").strip(),
            "created": str(fm.get("created") or "").strip(),
            "updated": str(fm.get("updated") or "").strip(),
            "status": str(fm.get("status") or "").strip(),
        }
        entry["third_level"] = third_level(entry)
        entries.append(entry)

    def sort_key(e: dict[str, Any]) -> tuple[int, str, str, str]:
        order = TYPE_ORDER.index(e["type"]) if e["type"] in TYPE_ORDER else len(TYPE_ORDER)
        return (
            order,
            title_case_slug(e.get("second_level", "")).lower(),
            str(e.get("third_level", "")).lower(),
            e["title"].lower(),
        )

    return sorted(entries, key=sort_key)


def write_if_changed(path: Path, content: str, *, dry_run: bool = False, check: bool = False) -> bool:
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if current == content:
        return False
    if not dry_run and not check:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return True


def write_json(entries: list[dict[str, Any]], *, dry_run: bool = False, check: bool = False) -> bool:
    """
    Keep this intentionally minimal.

    Purpose:
    - Let AI / Claude Code quickly know whether an entry exists.
    - Provide the file path if it needs to open the entry.
    - Include aliases for matching Chinese names / abbreviations.
    - Include type so wiki_relations.py can classify links safely.
    - Include subtype for Fact entries so organization links can be resolved.

    Do not store tags, status, journal, book_title, citation fields, sources, or related_* here.
    Citation metadata is maintained separately under citation/.
    """
    compact = []
    for e in entries:
        item = {
            "title": e["title"],
            "type": e["type"],
            "path": e["path"],
        }
        if e.get("aliases"):
            item["aliases"] = e["aliases"]
        # Fact subtype lets wiki_linker.py link YAML issuing_organization to
        # Fact(subtype=organization) entries, as authors link to Person entries.
        if e["type"] == "fact" and e.get("subtype"):
            item["subtype"] = e["subtype"]
        compact.append(item)

    return write_if_changed(
        INDEX_JSON,
        json.dumps(compact, ensure_ascii=False, indent=2),
        dry_run=dry_run,
        check=check,
    )


def md_line(entry: dict[str, Any]) -> str:
    summary = entry.get("summary", "").strip()
    if summary:
        return f"- [[{entry['title']}]] — {summary}"
    return f"- [[{entry['title']}]]"


def append_callout(lines: list[str], title: str, item_lines: list[str], callout_type: str = "index-list") -> None:
    count = len(item_lines)
    lines.append(f"> [!{callout_type}]- {title} ({count})")
    for item in item_lines:
        lines.append(f"> {item}")
    lines.append("")


def group_entries(entries: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for e in entries:
        groups.setdefault(str(e.get(key) or "uncategorized"), []).append(e)
    return groups


def count_values(entries: list[dict[str, Any]], key: str) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for e in entries:
        value = str(e.get(key) or "unknown").strip() or "unknown"
        counts[value] = counts.get(value, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], title_case_slug(item[0]).lower()))


def count_tags(entries: list[dict[str, Any]], prefixes: tuple[str, ...] = ()) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for e in entries:
        for tag in e.get("tags", []):
            if prefixes and not tag.startswith(prefixes):
                continue
            counts[tag] = counts.get(tag, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0].lower()))


def table_row(label: str, count: int) -> str:
    return f"| {label} | {count} |"


def format_tag(tag: str) -> str:
    if "/" in tag:
        prefix, rest = tag.split("/", 1)
        return f"{title_case_slug(rest)} `#{prefix}`"
    return tag


def append_fact_dashboard(lines: list[str], facts: list[dict[str, Any]]) -> None:
    if not facts:
        return

    by_region = count_values(facts, "second_level")
    by_subtype = count_values(facts, "third_level")
    topic_tags = count_tags(
        facts,
        (
            "theme/",
            "subject/",
            "policy/",
            "level/",
            "critique/",
            "method/",
        ),
    )

    lines.extend(
        [
            "## At a Glance",
            "",
            "| Lens | Count |",
            "|---|---:|",
            table_row("Fact entries", len(facts)),
            table_row("Regions / contexts", len(by_region)),
            table_row("Fact types", len(by_subtype)),
            "",
            "## Region Hotspots",
            "",
            "| Region | Entries |",
            "|---|---:|",
        ]
    )

    for region, count in by_region[:12]:
        lines.append(table_row(title_case_slug(region), count))

    lines.extend(["", "## Fact Types", "", "| Type | Entries |", "|---|---:|"])
    for subtype, count in by_subtype:
        lines.append(table_row(title_case_slug(subtype), count))

    if topic_tags:
        lines.extend(["", "## Topic Signals", "", "| Signal | Entries |", "|---|---:|"])
        for tag, count in topic_tags[:12]:
            lines.append(table_row(format_tag(tag), count))

    lines.extend(
        [
            "",
            "## Fast Trails",
            "",
        ]
    )

    trails = [
        ("Evidence infrastructure", ("evidence", "what-works")),
        ("Curriculum and assessment", ("curriculum", "assessment")),
        ("Innovation systems", ("innovation",)),
        ("China and Hong Kong", ("region/china", "region/hongkong")),
        ("University-industry links", ("industry", "technology-transfer")),
    ]

    for title, needles in trails:
        matches = [
            e
            for e in facts
            if any(
                needle.lower() in " ".join([*e.get("tags", []), e["title"], e.get("summary", "")]).lower()
                for needle in needles
            )
        ]
        if matches:
            append_callout(lines, title, [md_line(e) for e in sorted(matches, key=lambda x: x["title"].lower())[:8]], "trail")

    lines.extend(["---", ""])


def third_label(typ: str, value: str) -> str:
    if typ == "fact":
        return title_case_slug(value)
    if typ == "person":
        if value == "school":
            return "Academic Schools"
        return value or "Unknown"
    return value or "Unknown"


def write_markdown(entries: list[dict[str, Any]], *, dry_run: bool = False, check: bool = False) -> bool:
    by_type = group_entries(entries, "type")

    lines = [
        "# Wiki Index",
        "",
        "> Generated by `scripts/wiki_index.py`. Do not edit manually.",
        "",
        f"Total entries: **{len(entries)}**",
        "",
    ]

    for typ in TYPE_ORDER:
        type_items = by_type.get(typ, [])
        if not type_items:
            continue

        lines.extend(["---", "", f"## {TYPE_LABELS.get(typ, typ.title())}", ""])

        by_second = group_entries(type_items, "second_level")
        for second_key in sorted(by_second, key=lambda x: title_case_slug(x).lower()):
            second_items = by_second[second_key]

            if typ in {"argument", "fact", "person"}:
                lines.extend([f"### {title_case_slug(second_key)}", ""])
                by_third = group_entries(second_items, "third_level")
                for third_key in sorted(by_third, key=lambda x: str(x).lower()):
                    third_items = sorted(by_third[third_key], key=lambda x: x["title"].lower())
                    append_callout(lines, third_label(typ, third_key), [md_line(e) for e in third_items])
            else:
                sorted_items = sorted(second_items, key=lambda x: x["title"].lower())
                append_callout(lines, title_case_slug(second_key), [md_line(e) for e in sorted_items])

    for typ in sorted(k for k in by_type if k not in TYPE_ORDER):
        lines.extend(["---", "", f"## {typ.title()}", ""])
        sorted_items = sorted(by_type[typ], key=lambda x: x["title"].lower())
        append_callout(lines, typ.title(), [md_line(e) for e in sorted_items])

    return write_if_changed(
        INDEX_MD,
        "\n".join(lines).rstrip() + "\n",
        dry_run=dry_run,
        check=check,
    )



def write_local_indexes(entries: list[dict[str, Any]], *, dry_run: bool = False, check: bool = False) -> list[Path]:
    """
    Generate local indexes inside each major wiki folder.

    Examples:
    - wiki/concepts/index.md
    - wiki/theories/index.md
    - wiki/methods/index.md
    - wiki/instruments/index.md
    - wiki/persons/index.md
    - wiki/facts/index.md
    - wiki/arguments/index.md

    The grouping rule is the same as index.md, but each file contains
    only entries of that type.
    """
    by_type = group_entries(entries, "type")
    changed: list[Path] = []

    for typ, out_path in LOCAL_INDEX_FILES.items():
        type_items = by_type.get(typ, [])

        label = TYPE_LABELS.get(typ, typ.title())
        lines = [
            f"# {label} Index",
            "",
            "> Generated by `scripts/wiki_index.py`. Do not edit manually.",
            "",
            f"Total entries: **{len(type_items)}**",
            "",
        ]

        if not type_items:
            if write_if_changed(out_path, "\n".join(lines).rstrip() + "\n", dry_run=dry_run, check=check):
                changed.append(out_path)
            continue

        if typ == "fact":
            append_fact_dashboard(lines, type_items)

        by_second = group_entries(type_items, "second_level")

        for second_key in sorted(by_second, key=lambda x: title_case_slug(x).lower()):
            second_items = by_second[second_key]

            if typ in {"argument", "fact", "person"}:
                lines.extend([f"## {title_case_slug(second_key)}", ""])
                by_third = group_entries(second_items, "third_level")
                for third_key in sorted(by_third, key=lambda x: str(x).lower()):
                    third_items = sorted(by_third[third_key], key=lambda x: x["title"].lower())
                    append_callout(lines, third_label(typ, third_key), [md_line(e) for e in third_items])
            else:
                sorted_items = sorted(second_items, key=lambda x: x["title"].lower())
                append_callout(lines, title_case_slug(second_key), [md_line(e) for e in sorted_items])

        if write_if_changed(out_path, "\n".join(lines).rstrip() + "\n", dry_run=dry_run, check=check):
            changed.append(out_path)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate machine-readable and Markdown wiki indexes.")
    parser.add_argument("--dry-run", action="store_true", help="Report stale generated files without writing them.")
    parser.add_argument("--check", action="store_true", help="Exit non-zero when generated files are stale.")
    args = parser.parse_args()

    if not WIKI_DIR.exists():
        raise SystemExit(f"wiki directory not found: {WIKI_DIR}")

    entries = collect_entries()
    changed: list[Path] = []
    if write_json(entries, dry_run=args.dry_run, check=args.check):
        changed.append(INDEX_JSON)
    if write_markdown(entries, dry_run=args.dry_run, check=args.check):
        changed.append(INDEX_MD)
    changed.extend(write_local_indexes(entries, dry_run=args.dry_run, check=args.check))
    # Organization registry for issuing_organization links (keeps editable variants).
    if write_if_changed(ORG_REGISTRY_JSON, render_registry(entries), dry_run=args.dry_run, check=args.check):
        changed.append(ORG_REGISTRY_JSON)

    action = "Would update" if args.dry_run or args.check else "Generated"
    for path in changed:
        print(f"{action} {path.relative_to(ROOT)}")
    if not changed:
        print("Indexes are up to date.")
    print(f"Entries: {len(entries)}")
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
