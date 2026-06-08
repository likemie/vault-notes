#!/usr/bin/env python3
"""Build citation indexes for Argument pages.

Outputs:
  citation/citation_full.json
  citation/citation_ambiguous.json

This script keeps citation metadata separate from wiki/index.json. It scans
wiki/arguments/**/*.md and includes only citeable Argument pages, based on
frontmatter citation_* fields. Edited-volume overview pages are structural
entries and are not included in citation indexes.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT_DEFAULT = Path.cwd()
ARGUMENTS_DIR = Path("wiki/arguments")
CITATION_DIR = Path("citation")
FULL_INDEX = "citation_full.json"
AMBIGUOUS_INDEX = "citation_ambiguous.json"

REQUIRED_FIELDS = ("citation_stem", "citation_key", "citation_short", "year")
SKIP_SUBTYPES = {"edited-volume-overview"}


def strip_quotes(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Parse a conservative YAML frontmatter subset used by the vault templates."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].splitlines()
    body = text[end + len("\n---") :]

    data: dict[str, Any] = {}
    i = 0
    key_re = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
    while i < len(raw):
        line = raw[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        m = key_re.match(line)
        if not m:
            i += 1
            continue
        key, rest = m.group(1), (m.group(2) or "").strip()
        if rest == "":
            # YAML block list, e.g. authors:\n  - "[[Ball, S. J.]]"
            items: list[str] = []
            j = i + 1
            while j < len(raw):
                nxt = raw[j]
                if key_re.match(nxt):
                    break
                item = nxt.strip()
                if item.startswith("- "):
                    items.append(strip_quotes(item[2:].strip()))
                elif item:
                    # Unknown nested structure; keep as plain line for diagnostics.
                    items.append(strip_quotes(item))
                j += 1
            data[key] = items if items else ""
            i = j
        else:
            # Inline list support: ["a", "b"]
            if rest.startswith("[") and rest.endswith("]"):
                inner = rest[1:-1].strip()
                if not inner:
                    data[key] = []
                else:
                    parts = [strip_quotes(p.strip()) for p in inner.split(",")]
                    data[key] = [p for p in parts if p]
            else:
                data[key] = strip_quotes(rest)
            i += 1
    return data, body


def as_list(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    return [str(value).strip()]


def clean_year(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip().strip('"\'')
    m = re.search(r"\d{4}", text)
    return m.group(0) if m else text


@dataclass
class CitationItem:
    citation_key: str
    citation_stem: str
    citation_suffix: str
    citation_short: str
    year: str
    authors: list[str]
    title: str
    doi: str
    citation: str
    argument_path: str
    subtype: str
    publication_type: str
    journal: str
    book_title: str


def is_citeable_argument(fm: dict[str, Any]) -> bool:
    if str(fm.get("type", "")).strip() != "argument":
        return False
    if str(fm.get("subtype", "")).strip() in SKIP_SUBTYPES:
        return False
    return True


def build_item(path: Path, fm: dict[str, Any], root: Path) -> tuple[CitationItem | None, list[str]]:
    errors: list[str] = []
    if not is_citeable_argument(fm):
        return None, errors
    missing = [k for k in REQUIRED_FIELDS if not str(fm.get(k, "")).strip()]
    if missing:
        errors.append(f"{path}: missing citation fields: {', '.join(missing)}")
        return None, errors
    rel = path.relative_to(root).as_posix() if path.is_absolute() else path.as_posix()
    item = CitationItem(
        citation_key=str(fm.get("citation_key", "")).strip(),
        citation_stem=str(fm.get("citation_stem", "")).strip(),
        citation_suffix=str(fm.get("citation_suffix", "")).strip(),
        citation_short=str(fm.get("citation_short", "")).strip(),
        year=clean_year(fm.get("year", "")),
        authors=as_list(fm.get("authors")),
        title=str(fm.get("title", path.stem)).strip() or path.stem,
        doi=str(fm.get("doi", "")).strip(),
        citation=str(fm.get("citation", "")).strip(),
        argument_path=rel,
        subtype=str(fm.get("subtype", "")).strip(),
        publication_type=str(fm.get("publication_type", "")).strip(),
        journal=str(fm.get("journal", "")).strip(),
        book_title=str(fm.get("book_title", "")).strip(),
    )
    return item, errors


def scan_arguments(root: Path) -> tuple[list[CitationItem], list[str]]:
    base = root / ARGUMENTS_DIR
    items: list[CitationItem] = []
    errors: list[str] = []
    if not base.exists():
        return items, [f"Missing arguments directory: {base}"]
    for path in sorted(base.rglob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        item, item_errors = build_item(path, fm, root)
        errors.extend(item_errors)
        if item:
            items.append(item)
    return items, errors


def make_indexes(items: list[CitationItem]) -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    warnings: list[str] = []
    by_key: dict[str, dict[str, Any]] = {}
    by_stem: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for item in items:
        obj = asdict(item)
        if item.citation_key in by_key:
            warnings.append(f"Duplicate citation_key: {item.citation_key}")
        by_key[item.citation_key] = obj
        by_stem[item.citation_stem].append(obj)

    for stem, group in by_stem.items():
        group.sort(key=lambda x: (str(x.get("citation_suffix", "")), str(x.get("citation_key", ""))))
        if len(group) == 1:
            suffix = str(group[0].get("citation_suffix", ""))
            if suffix:
                warnings.append(f"Single item stem {stem} has suffix {suffix}; suffix is usually empty when no ambiguity exists.")
        else:
            suffixes = [str(g.get("citation_suffix", "")) for g in group]
            if any(not s for s in suffixes):
                warnings.append(f"Ambiguous stem {stem} has item(s) without citation_suffix.")
            dup_suffixes = {s for s in suffixes if s and suffixes.count(s) > 1}
            if dup_suffixes:
                warnings.append(f"Ambiguous stem {stem} has duplicate suffixes: {', '.join(sorted(dup_suffixes))}")

    generated_at = datetime.now(timezone.utc).isoformat()
    full = {
        "generated_at": generated_at,
        "count": len(items),
        "items": by_key,
        "by_stem": dict(sorted(by_stem.items())),
    }
    ambiguous = {
        "generated_at": generated_at,
        "count": sum(1 for group in by_stem.values() if len(group) > 1),
        "items": {stem: group for stem, group in sorted(by_stem.items()) if len(group) > 1},
    }
    return full, ambiguous, warnings


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build citation indexes from Argument frontmatter.")
    parser.add_argument("--root", default=str(ROOT_DEFAULT), help="Vault root. Default: current directory.")
    parser.add_argument("--check", action="store_true", help="Do not write files; report diagnostics only.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    items, errors = scan_arguments(root)
    full, ambiguous, warnings = make_indexes(items)

    if not args.check:
        out_dir = root / CITATION_DIR
        write_json(out_dir / FULL_INDEX, full)
        write_json(out_dir / AMBIGUOUS_INDEX, ambiguous)

    print(f"Citation items: {len(items)}")
    print(f"Ambiguous stems: {ambiguous['count']}")
    if not args.check:
        print(f"Wrote: {CITATION_DIR / FULL_INDEX}")
        print(f"Wrote: {CITATION_DIR / AMBIGUOUS_INDEX}")
    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  - {e}")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
