#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cleanup person YAML frontmatter fields.
- Removes legacy citation fields: family_name, given_names, initials, citation_name.
- Ensures all template keys are present:
  title, aliases, summary, type, nationality, tags, related_concepts,
  related_theories, related_methods, related_persons, related_facts,
  related_arguments, confidence, status, created, updated.
"""
from __future__ import annotations

import os
import sys
import re
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
PERSONS_DIR = WIKI_DIR / "persons"

TEMPLATE_KEYS_ORDER = [
    "title",
    "aliases",
    "summary",
    "type",
    "nationality",
    "tags",
    "related_concepts",
    "related_theories",
    "related_methods",
    "related_persons",
    "related_facts",
    "related_arguments",
    "confidence",
    "status",
    "created",
    "updated",
]

LEGACY_KEYS = {"family_name", "given_names", "initials", "citation_name"}

def split_frontmatter(text: str) -> tuple[str, str, str]:
    if not text.startswith("---\n"):
        return "", "", text
    end = text.find("\n---", 4)
    if end == -1:
        return "", "", text
    closing_end = text.find("\n", end + 4)
    if closing_end == -1:
        closing_end = len(text)
    yaml_text = text[4:end].strip("\n")
    body = text[closing_end + 1 :] if closing_end < len(text) else ""
    return "---\n", yaml_text, body

def yaml_key_at(line: str) -> str | None:
    if line.startswith(" ") or line.startswith("-") or not line.strip() or line.lstrip().startswith("#"):
        return None
    m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line)
    return m.group(1) if m else None

def find_key_span(lines: list[str], key: str) -> tuple[int, int] | None:
    start = None
    for i, line in enumerate(lines):
        if yaml_key_at(line) == key:
            start = i
            break
    if start is None:
        return None
    end = start + 1
    while end < len(lines) and yaml_key_at(lines[end]) is None:
        end += 1
    return start, end

def remove_yaml_keys(lines: list[str], keys_to_remove: set[str]) -> list[str]:
    # We copy to avoid modifying while iterating
    res = list(lines)
    for key in keys_to_remove:
        span = find_key_span(res, key)
        if span is not None:
            start, end = span
            res[start:end] = []
    return res

def insert_missing_key(lines: list[str], key: str, template_keys: list[str]) -> list[str]:
    res = list(lines)
    # Determine default format
    if key in {"aliases", "tags"} or key.startswith("related_"):
        val = "[]"
    elif key in {"confidence"}:
        val = "medium"
    elif key in {"status"}:
        val = "draft"
    else:
        val = '""'

    # Find the next key present
    idx = template_keys.index(key)
    insert_before_key = None
    for k in template_keys[idx + 1:]:
        if find_key_span(res, k) is not None:
            insert_before_key = k
            break

    if insert_before_key is not None:
        span = find_key_span(res, insert_before_key)
        insert_at = span[0]
    else:
        insert_at = len(res)

    res.insert(insert_at, f"{key}: {val}")
    return res

def process_file(path: Path, dry_run: bool = False) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {path.relative_to(ROOT)}: {e}", file=sys.stderr)
        return False

    prefix, yaml_text, body = split_frontmatter(content)
    if not prefix:
        return False

    lines = yaml_text.splitlines()
    present_keys = set()
    for line in lines:
        k = yaml_key_at(line)
        if k:
            present_keys.add(k)

    keys_to_remove = present_keys & LEGACY_KEYS
    keys_to_add = [k for k in TEMPLATE_KEYS_ORDER if k not in present_keys]

    if not keys_to_remove and not keys_to_add:
        return False

    # Process removals
    updated_lines = remove_yaml_keys(lines, keys_to_remove)

    # Process additions (in order of template to preserve layout)
    for key in TEMPLATE_KEYS_ORDER:
        if key in keys_to_add:
            updated_lines = insert_missing_key(updated_lines, key, TEMPLATE_KEYS_ORDER)

    new_yaml = "\n".join(updated_lines).rstrip() + "\n"
    new_content = f"---\n{new_yaml}---\n{body}"

    if dry_run:
        print(f"Would update {path.relative_to(ROOT)}")
        if keys_to_remove:
            print(f"  Removals: {sorted(keys_to_remove)}")
        if keys_to_add:
            print(f"  Additions: {sorted(keys_to_add)}")
    else:
        path.write_text(new_content, encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)}")

    return True

def main() -> int:
    parser = argparse.ArgumentParser(description="Cleanup person frontmatter keys.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without saving.")
    args = parser.parse_args()

    if not PERSONS_DIR.exists():
        print(f"Persons directory not found: {PERSONS_DIR}", file=sys.stderr)
        return 1

    changed_count = 0
    total_count = 0
    for root, _, files in os.walk(PERSONS_DIR):
        for f in sorted(files):
            if f.endswith(".md") and f != "index.md" and not f.startswith("."):
                path = Path(root) / f
                total_count += 1
                if process_file(path, dry_run=args.dry_run):
                    changed_count += 1

    mode = "dry-run" if args.dry_run else "active"
    print(f"Finished ({mode}): checked {total_count} files, updated {changed_count} files.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
