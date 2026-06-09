#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cleanup parenthetical self-citations in Argument pages.
either simplifies them to page numbers or secondary sources, or deletes them.
"""
from __future__ import annotations

import os
import sys
import re
import argparse
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
ARGUMENTS_DIR = WIKI_DIR / "arguments"

def parse_frontmatter(content: str) -> tuple[dict, str] | None:
    if not content.startswith("---\n"):
        return None
    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1]), parts[2]
    except Exception:
        return None

def get_base_names(fm: dict, filename: str) -> list[str]:
    names = set()
    
    # 1. From citation_aliases
    aliases = fm.get("citation_aliases", [])
    if aliases:
        for alias in aliases:
            cleaned = re.sub(r"\(?\b(?:19|20)\d{2}\b\)?", "", alias)
            cleaned = cleaned.replace(",", "").replace("，", "").replace("等", "").replace("et al.", "").replace("et al", "").strip()
            if cleaned:
                names.add(cleaned)
    
    # 2. From authors list
    authors = fm.get("authors", [])
    for author in authors:
        if "[[" in author and "|" in author:
            display = author.split("|")[1].replace("]]", "").strip()
            surname = display.split(",")[0].strip()
            names.add(surname)
            target = author.split("|")[0].replace("[[", "").strip()
            if " " in target:
                names.add(target.split()[-1].strip())
            else:
                names.add(target)
        else:
            cleaned_author = author.replace("[[", "").replace("]]", "").strip()
            if "," in cleaned_author:
                names.add(cleaned_author.split(",")[0].strip())
            elif " " in cleaned_author:
                names.add(cleaned_author.split()[-1].strip())
            else:
                names.add(cleaned_author)

    # 3. From filename (supplementary fallback)
    stem = filename[:-3] if filename.endswith(".md") else filename
    if stem.startswith("Argument_"):
        stem = stem[len("Argument_"):]
    year_match = re.search(r"_(19|20)\d{2}_", stem)
    if year_match:
        authors_part = stem[:year_match.start()]
    else:
        parts = stem.split("_")
        authors_part = []
        for p in parts:
            if p.isdigit():
                break
            authors_part.append(p)
        authors_part = "_".join(authors_part)
        
    for part in re.split(r"_+|_+and_+|_+&_+", authors_part):
        part = part.strip()
        if part and part.lower() not in ("ed", "eds", "editor", "editors"):
            names.add(part)

    # Filter out empty or too short names
    names = {n for n in names if len(n) >= 2 or re.search(r"[\u4e00-\u9fff]", n)}
    return list(names)

def clean_inner_text(inner: str, names: list[str], year: int) -> str | None:
    # Construct combined name pattern
    name_patterns = []
    for name in names:
        escaped_name = re.escape(name)
        pattern = rf"(?:\[\[[^\]|]+\|)?{escaped_name}(?:\]\])?"
        pattern = rf"{pattern}(?:\s*(?:et\s+al\.?|等|本人))?"
        name_patterns.append(pattern)
    combined_name_pattern = "|".join(name_patterns)

    year_str = str(year)
    preposition_pattern = r"(?:引自|引|cited\s+in|citing|in)\s*"

    # Patterns to match and remove, ordered from most specific to least specific:
    preposition_patterns = [
        rf"{preposition_pattern}(?:{combined_name_pattern})[,，\s]+{year_str}",
        rf"{preposition_pattern}{year_str}[,，\s]+(?:{combined_name_pattern})",
        rf"{preposition_pattern}(?:{combined_name_pattern})",
    ]
    
    modified = inner
    matched = False
    for p in preposition_patterns:
        modified, count = re.subn(p, "", modified, flags=re.IGNORECASE)
        if count > 0:
            matched = True
            break
            
    if not matched:
        # If no preposition match, then if there's a different year (e.g. Zhao 2012), keep it.
        years_in_inner = re.findall(r"\b(?:19|20)\d{2}\b", inner)
        if years_in_inner and year_str not in years_in_inner:
            return inner
            
        # Otherwise, match name + year
        name_year_patterns = [
            rf"(?:{combined_name_pattern})[,，\s]+{year_str}",
            rf"{year_str}[,，\s]+(?:{combined_name_pattern})",
        ]
        for p in name_year_patterns:
            modified, count = re.subn(p, "", modified, flags=re.IGNORECASE)
            if count > 0:
                matched = True
                break
                
    if not matched:
        # Check if the name is completely standalone (leaving nothing but punctuation/spaces)
        temp = re.sub(combined_name_pattern, "", modified, flags=re.IGNORECASE)
        temp_cleaned = re.sub(r"^[，,；;\s]+", "", temp)
        temp_cleaned = re.sub(r"[，,；;\s]+$", "", temp_cleaned)
        if not temp_cleaned:
            modified = temp

    # Clean up punctuation and spaces
    modified = re.sub(r"^[，,；;\s]+", "", modified)
    modified = re.sub(r"[，,；;\s]+$", "", modified)
    modified = re.sub(r"\s*[,，;；]\s*[,，;；]\s*", ", ", modified)
    modified = re.sub(r"\s*[,，;；]\s*", ", ", modified)
    
    if not modified.strip():
        return None
    return modified

def process_argument_file(path: Path, dry_run: bool = False) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {path.relative_to(ROOT)}: {e}", file=sys.stderr)
        return False

    res = parse_frontmatter(content)
    if not res:
        return False
    
    fm, body = res
    year = fm.get("year")
    if not year:
        # Get year from filename
        year_match = re.search(r"_(19|20)\d{2}_", path.name)
        if year_match:
            year = int(year_match.group(1))
        else:
            return False
            
    base_names = get_base_names(fm, path.name)
    if not base_names:
        return False

    new_body = body
    replacements = []
    
    # Matches both standard ( ) and CJK （ ） parentheses
    pattern = r"\(([^)]+)\)|（([^）]+)）"
    
    pos = 0
    while True:
        m = re.search(pattern, new_body[pos:])
        if not m:
            break
        
        start_idx = pos + m.start()
        end_idx = pos + m.end()
        full_match = m.group(0)
        inner_text = m.group(1) if m.group(1) is not None else m.group(2)
        
        is_self = False
        for name in base_names:
            if re.search(r"[\u4e00-\u9fff]", name):
                if name in inner_text:
                    is_self = True
                    break
            else:
                if re.search(rf"\b{re.escape(name)}\b", inner_text, re.IGNORECASE):
                    is_self = True
                    break
        
        if is_self and not (inner_text.startswith("http") or inner_text.endswith(".png") or inner_text.endswith(".jpg") or inner_text.endswith(".jpeg")):
            cleaned_inner = clean_inner_text(inner_text, base_names, year)
            if cleaned_inner is None:
                # Remove the entire parenthetical citation
                replacement = ""
            else:
                # Keep same brackets
                open_bracket = full_match[0]
                close_bracket = full_match[-1]
                replacement = f"{open_bracket}{cleaned_inner}{close_bracket}"
            
            replacements.append((full_match, replacement))
            new_body = new_body[:start_idx] + replacement + new_body[end_idx:]
            pos = start_idx + len(replacement)
        else:
            pos = end_idx

    if not replacements:
        return False

    if dry_run:
        print(f"Would update {path.relative_to(ROOT)}:")
        for orig, rep in replacements:
            print(f"  {orig} -> {rep if rep else '[DELETED]'}")
    else:
        # Reconstruct the file with frontmatter and updated body
        # Ensure we preserve original frontmatter formatting
        parts = content.split("---\n", 2)
        new_content = f"---\n{parts[1]}---\n{new_body}"
        path.write_text(new_content, encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)} ({len(replacements)} replacement(s))")

    return True

def main() -> int:
    parser = argparse.ArgumentParser(description="Cleanup parenthetical self-citations in argument files.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without saving.")
    parser.add_argument("--file", type=str, help="Process a single file instead of all.")
    args = parser.parse_args()

    if args.file:
        path = Path(args.file).resolve()
        if not path.exists():
            print(f"File not found: {path}", file=sys.stderr)
            return 1
        process_argument_file(path, dry_run=args.dry_run)
        return 0

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
