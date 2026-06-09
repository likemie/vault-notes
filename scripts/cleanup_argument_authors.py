#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cleanup argument authors to follow APA style:
- Format plain names to Lastname, Initials. (e.g. Wolf, B. J.)
- Format wikilinks to include APA display text: [[PersonName|Lastname, Initials.]] (e.g. [[Terry Wrigley|Wrigley, T.]])
- Combine incorrectly split authors (e.g. 'Wolff' and 'L.-A' -> 'Wolff, L.-A.')
"""
from __future__ import annotations

import os
import sys
import re
import argparse
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
ARGUMENTS_DIR = WIKI_DIR / "arguments"

# Heuristic to find the APA alias from Person entry data
def find_apa_alias(title: str, aliases: list[str]) -> str:
    if title in {"Confucius", "Xunzi", "Mencius", "Zhuangzi", "Socrates", "Plato"}:
        return title
    candidates = []
    for a in aliases:
        if "," in a:
            parts = a.split(",", 1)
            after = parts[1].strip()
            if len(after) <= 15 and any(c.isupper() for c in after):
                candidates.append(a)
    if candidates:
        candidates.sort(key=lambda x: x.count("."), reverse=True)
        return candidates[0]
    return title

# Build Person mapping (case-insensitive title -> (title, apa_alias))
def build_person_map() -> dict[str, tuple[str, str]]:
    person_map = {}
    persons_dir = WIKI_DIR / "persons"
    if not persons_dir.exists():
        return person_map

    for root, _, files in os.walk(persons_dir):
        for f in files:
            if f.endswith(".md") and f != "index.md" and not f.startswith("."):
                path = Path(root) / f
                try:
                    content = path.read_text(encoding="utf-8")
                    _, yaml_text, _ = split_frontmatter(content)
                    data = yaml.safe_load(yaml_text) or {}
                    title = data.get("title", "")
                    aliases = data.get("aliases", [])
                    if title:
                        apa = find_apa_alias(title, aliases)
                        person_map[title.lower()] = (title, apa)
                except Exception:
                    pass
    return person_map

def format_plain_name_to_apa(name: str) -> str:
    name = name.strip()
    if not name:
        return ""
    if "," in name:
        parts = [p.strip() for p in name.split(",", 1)]
        family = parts[0]
        given = parts[1]
        initials = []
        if "-" in given:
            sub_parts = given.split("-")
            for sp in sub_parts:
                sp_clean = "".join(c for c in sp if c.isalpha())
                if sp_clean:
                    initials.append(f"{sp_clean[0].upper()}.")
            initials_str = "-".join(initials)
        else:
            words = re.findall(r"[A-Za-z]+", given)
            for w in words:
                initials.append(f"{w[0].upper()}.")
            initials_str = " ".join(initials)
        return f"{family}, {initials_str}"
    
    words = [w for w in re.split(r"\s+", name) if w]
    if len(words) == 1:
        return words[0]
        
    last_word_is_initials = False
    last_word_clean = words[-1].replace(".", "").replace("-", "")
    if last_word_clean.isupper() and len(last_word_clean) <= 4:
        last_word_is_initials = True
        
    if last_word_is_initials:
        family = words[0]
        given_words = words[1:]
    else:
        family = words[-1]
        given_words = words[:-1]
        
    initials = []
    for gw in given_words:
        gw_clean = gw.replace(".", "")
        if "-" in gw_clean:
            sub_parts = gw_clean.split("-")
            init_sub = []
            for sp in sub_parts:
                if sp:
                    init_sub.append(f"{sp[0].upper()}.")
            initials.append("-".join(init_sub))
        else:
            if len(gw_clean) > 1 and gw_clean.isupper():
                for char in gw_clean:
                    initials.append(f"{char}.")
            else:
                initials.append(f"{gw_clean[0].upper()}.")
    initials_str = " ".join(initials)
    return f"{family}, {initials_str}"

def combine_split_authors(authors: list[str]) -> list[str]:
    new_authors = []
    i = 0
    while i < len(authors):
        auth = authors[i].strip()
        if (i + 1 < len(authors) and 
            not "," in auth and not "." in auth and auth.replace("-", "").isalpha() and
            ("." in authors[i+1] or "-" in authors[i+1] or len(authors[i+1].strip()) <= 6)):
            combined = f"{auth}, {authors[i+1].strip()}"
            new_authors.append(combined)
            i += 2
        else:
            new_authors.append(auth)
            i += 1
    return new_authors

def clean_author(auth: str, person_map: dict[str, tuple[str, str]]) -> str:
    auth = auth.strip()
    m = re.fullmatch(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", auth)
    if m:
        target = m.group(1).strip()
        display = m.group(2).strip() if m.group(2) else ""
        target_lower = target.lower()
        if target_lower in person_map:
            actual_title, apa = person_map[target_lower]
            return f"[[{actual_title}|{apa}]]"
        else:
            disp = display if display else target
            disp_apa = format_plain_name_to_apa(disp)
            return f"[[{target}|{disp_apa}]]"
    else:
        return format_plain_name_to_apa(auth)

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

def parse_yaml_list_from_span(lines: list[str], start: int, end: int) -> list[str]:
    # Extract list values from block format or inline flow format
    block_lines = lines[start:end]
    first_line = block_lines[0]
    rest = first_line.split(":", 1)[1].strip()
    if rest.startswith("[") and rest.endswith("]"):
        return [x.strip().strip("'\"") for x in rest[1:-1].split(",") if x.strip()]
    
    values = []
    for line in block_lines[1:]:
        s = line.strip()
        if s.startswith("-"):
            values.append(s[1:].strip().strip("'\""))
    return values

def format_yaml_list(key: str, values: list[str]) -> list[str]:
    if not values:
        return [f"{key}: []"]
    return [f"{key}:"] + [f'  - "{v}"' for v in values]

def process_argument_file(path: Path, person_map: dict[str, tuple[str, str]], dry_run: bool = False) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {path.relative_to(ROOT)}: {e}", file=sys.stderr)
        return False

    prefix, yaml_text, body = split_frontmatter(content)
    if not prefix:
        return False

    lines = yaml_text.splitlines()
    span = find_key_span(lines, "authors")
    if span is None:
        return False

    start, end = span
    authors = parse_yaml_list_from_span(lines, start, end)
    if not authors:
        return False

    combined = combine_split_authors(authors)
    cleaned = [clean_author(x, person_map) for x in combined if x]

    if cleaned == authors:
        return False

    if dry_run:
        print(f"Would update {path.relative_to(ROOT)}:")
        print(f"  Old: {authors}")
        print(f"  New: {cleaned}")
    else:
        new_span_lines = format_yaml_list("authors", cleaned)
        lines[start:end] = new_span_lines
        new_yaml = "\n".join(lines).rstrip() + "\n"
        new_content = f"---\n{new_yaml}---\n{body}"
        path.write_text(new_content, encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)}")
    return True

def main() -> int:
    parser = argparse.ArgumentParser(description="Cleanup argument authors to APA style.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without saving.")
    args = parser.parse_args()

    if not ARGUMENTS_DIR.exists():
        print(f"Arguments directory not found: {ARGUMENTS_DIR}", file=sys.stderr)
        return 1

    person_map = build_person_map()
    changed_count = 0
    total_count = 0

    for root, _, files in os.walk(ARGUMENTS_DIR):
        for f in sorted(files):
            if f.endswith(".md") and f != "index.md" and not f.startswith("."):
                path = Path(root) / f
                total_count += 1
                if process_argument_file(path, person_map, dry_run=args.dry_run):
                    changed_count += 1

    mode = "dry-run" if args.dry_run else "active"
    print(f"Finished ({mode}): checked {total_count} files, updated {changed_count} files.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
