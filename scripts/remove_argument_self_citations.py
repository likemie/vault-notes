#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove self-citations and self-links in Argument pages.
- Finds any wikilinks pointing to the file's own stem.
- Replaces them with only the page numbers (e.g., p. 194) or clean author names if no page number.
"""
from __future__ import annotations

import os
import sys
import re
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
ARGUMENTS_DIR = WIKI_DIR / "arguments"

def clean_self_link_display(display: str, author_name: str) -> str:
    display = display.strip()
    if not display:
        return author_name
    
    # Search for page numbers first (e.g. 'Berk, 2011, p.194' or 'Berk (2011, p.199-200)')
    page_match = re.search(r"\b(pp?\.?\s*\d+.*)", display)
    if page_match:
        page_part = page_match.group(1).rstrip(")")
        # Check if it was in parentheses like 'Berk (2011, p.199-200)'
        if "(" in display and ")" not in page_part:
            author_part = display.split("(")[0].strip()
            return f"{author_part} ({page_part})"
        return page_part
    
    # If no page numbers, return the author part
    author_part = re.split(r"\(?\b(?:19|20)\d{2}\b\)?", display)[0].strip().rstrip(",").strip()
    if not author_part:
        author_part = author_name
    return author_part

def replace_self_citations(body: str, stem: str, author_name: str) -> tuple[str, list[tuple[str, str]]]:
    replacements = []
    pos = 0
    while True:
        idx = body.find(f"[[{stem}", pos)
        if idx == -1:
            break
        
        # Trace brackets to handle nested wikilinks correctly
        open_count = 1
        i = idx + len(f"[[{stem}")
        pipe_idx = -1
        if i < len(body) and body[i] == "|":
            pipe_idx = i
            i += 1
            
        while i < len(body) - 1:
            if body[i:i+2] == "[[":
                open_count += 1
                i += 2
            elif body[i:i+2] == "]]":
                open_count -= 1
                if open_count == 0:
                    outer_end_idx = i + 2
                    break
                i += 2
            else:
                i += 1
        else:
            # No matching closing brackets found, skip
            pos = idx + len(f"[[{stem}")
            continue
            
        if pipe_idx != -1:
            display = body[pipe_idx + 1 : outer_end_idx - 2]
        else:
            display = ""
            
        original_link = body[idx:outer_end_idx]
        cleaned = clean_self_link_display(display, author_name)
        
        replacements.append((original_link, cleaned))
        body = body[:idx] + cleaned + body[outer_end_idx:]
        pos = idx + len(cleaned)
        
    return body, replacements

def process_argument_file(path: Path, dry_run: bool = False) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {path.relative_to(ROOT)}: {e}", file=sys.stderr)
        return False

    if not content.startswith("---\n"):
        return False

    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return False

    prefix_yaml = parts[1]
    body = parts[2]
    stem = path.stem

    # Extract author name from stem, e.g. Argument_Ball_2008_SR -> Ball
    stem_parts = stem.split("_")
    author_name = stem_parts[1] if len(stem_parts) >= 2 else "Author"

    new_body, replacements = replace_self_citations(body, stem, author_name)

    if not replacements:
        return False

    if dry_run:
        print(f"Would update {path.relative_to(ROOT)}:")
        for orig, clean in replacements:
            print(f"  {orig} -> {clean}")
    else:
        new_content = f"---\n{prefix_yaml}---\n{new_body}"
        path.write_text(new_content, encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)} ({len(replacements)} replacement(s))")

    return True

def main() -> int:
    parser = argparse.ArgumentParser(description="Remove self-citations in argument files.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without saving.")
    args = parser.parse_args()

    if not ARGUMENTS_DIR.exists():
        print(f"Arguments directory not found: {ARGUMENTS_DIR}", file=sys.stderr)
        return 1

    changed_count = 0
    total_count = 0

    for root, _, files in os.walk(ARGUMENTS_DIR):
        for f in sorted(files):
            if f.endswith(".md") and f != "index.md" and not f.startswith("."):
                path = Path(root) / f
                total_count += 1
                if process_argument_file(path, dry_run=args.dry_run):
                    changed_count += 1

    mode = "dry-run" if args.dry_run else "active"
    print(f"Finished ({mode}): checked {total_count} files, updated {changed_count} files.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
