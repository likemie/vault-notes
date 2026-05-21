#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
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

TYPE_ORDER = ["concept", "theory", "method", "person", "fact", "argument", "source", "unknown"]

TYPE_LABELS = {
    "concept": "Concepts",
    "theory": "Theories",
    "method": "Methods",
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
    "comparative-education": "Comparative Education",
    "curriculum": "Curriculum",
    "educational-philosophy": "Educational Philosophy",
    "sociology-of-education": "Sociology of Education",
    "globalization-and-education": "Globalization and Education",
    "policy-studies": "Policy Studies",
    "methodology": "Methodology",
    "global": "Global",
    "multi": "Multi-country",
    "us": "US",
    "uk": "UK",
}

LIST_KEYS = {
    "aliases",
    "tags",
    "sources",
    "authors",
    "editors",
    "related_concepts",
    "related_theories",
    "related_methods",
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
        return entry.get("nationality") or "unknown"

    return ""


def collect_entries() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []

    for path in sorted(WIKI_DIR.rglob("*.md")):
        if should_skip(path):
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        fm = extract_frontmatter(text)

        typ = str(fm.get("type") or infer_type_from_path(path)).strip()
        entry = {
            "title": str(fm.get("title") or path.stem).strip(),
            "type": typ,
            "subtype": str(fm.get("subtype") or "").strip(),
            "second_level": second_level_from_path(path, typ),
            "third_folder": third_folder_from_path(path, typ),
            "path": path.relative_to(ROOT).as_posix(),
            "aliases": normalize_list(fm.get("aliases")),
            "summary": str(fm.get("summary") or "").strip(),
            # These are only used to generate index.md group headings.
            "journal": str(fm.get("journal") or "").strip(),
            "book_title": str(fm.get("book_title") or "").strip(),
            "issuing_organization": str(fm.get("issuing_organization") or "").strip(),
            "nationality": str(fm.get("nationality") or "").strip(),
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


def write_json(entries: list[dict[str, Any]]) -> None:
    """
    Keep this intentionally minimal.

    Purpose:
    - Let AI / Claude Code quickly know whether an entry exists.
    - Provide the file path if it needs to open the entry.
    - Include aliases for matching Chinese names / abbreviations.

    Do not store type, tags, status, journal, book_title, sources, or related_* here.
    """
    compact = []
    for e in entries:
        item = {
            "title": e["title"],
            "path": e["path"],
        }
        if e.get("aliases"):
            item["aliases"] = e["aliases"]
        compact.append(item)

    INDEX_JSON.write_text(json.dumps(compact, ensure_ascii=False, indent=2), encoding="utf-8")


def md_line(entry: dict[str, Any]) -> str:
    summary = entry.get("summary", "").strip()
    if summary:
        return f"- [[{entry['title']}]] — {summary}"
    return f"- [[{entry['title']}]]"


def group_entries(entries: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for e in entries:
        groups.setdefault(str(e.get(key) or "uncategorized"), []).append(e)
    return groups


def third_label(typ: str, value: str) -> str:
    if typ == "fact":
        return title_case_slug(value)
    return value or "Unknown"


def write_markdown(entries: list[dict[str, Any]]) -> None:
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
            lines.extend([f"### {title_case_slug(second_key)}", ""])

            if typ in {"argument", "fact", "person"}:
                by_third = group_entries(second_items, "third_level")
                for third_key in sorted(by_third, key=lambda x: str(x).lower()):
                    lines.extend([f"#### {third_label(typ, third_key)}", ""])
                    for e in sorted(by_third[third_key], key=lambda x: x["title"].lower()):
                        lines.append(md_line(e))
                    lines.append("")
            else:
                for e in sorted(second_items, key=lambda x: x["title"].lower()):
                    lines.append(md_line(e))
                lines.append("")

    for typ in sorted(k for k in by_type if k not in TYPE_ORDER):
        lines.extend(["---", "", f"## {typ.title()}", ""])
        for e in sorted(by_type[typ], key=lambda x: x["title"].lower()):
            lines.append(md_line(e))
        lines.append("")

    INDEX_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")



def write_local_indexes(entries: list[dict[str, Any]]) -> None:
    """
    Generate local indexes inside each major wiki folder.

    Examples:
    - wiki/concepts/index.md
    - wiki/theories/index.md
    - wiki/methods/index.md
    - wiki/persons/index.md
    - wiki/facts/index.md
    - wiki/arguments/index.md

    The grouping rule is the same as index.md, but each file contains
    only entries of that type.
    """
    by_type = group_entries(entries, "type")

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
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
            continue

        by_second = group_entries(type_items, "second_level")

        for second_key in sorted(by_second, key=lambda x: title_case_slug(x).lower()):
            second_items = by_second[second_key]
            lines.extend([f"## {title_case_slug(second_key)}", ""])

            if typ in {"argument", "fact", "person"}:
                by_third = group_entries(second_items, "third_level")
                for third_key in sorted(by_third, key=lambda x: str(x).lower()):
                    lines.extend([f"### {third_label(typ, third_key)}", ""])
                    for e in sorted(by_third[third_key], key=lambda x: x["title"].lower()):
                        lines.append(md_line(e))
                    lines.append("")
            else:
                for e in sorted(second_items, key=lambda x: x["title"].lower()):
                    lines.append(md_line(e))
                lines.append("")

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    if not WIKI_DIR.exists():
        raise SystemExit(f"wiki directory not found: {WIKI_DIR}")

    entries = collect_entries()
    write_json(entries)
    write_markdown(entries)
    write_local_indexes(entries)

    print(f"Generated {INDEX_JSON.relative_to(ROOT)}")
    print(f"Generated {INDEX_MD.relative_to(ROOT)}")
    for local_index in LOCAL_INDEX_FILES.values():
        print(f"Generated {local_index.relative_to(ROOT)}")
    print(f"Entries: {len(entries)}")


if __name__ == "__main__":
    main()
