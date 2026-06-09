#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cleanup_argument_citations.py

Correct non-standard and mixed Chinese-English citation formats in argument page bodies.
- Standardizes brackets wrapping years and pages.
- Replaces CJK separators (和, 等) for English/Latin author citations with standard APA formats.
- Resolves specific missing year citations.
- Removes redundant self-citations.
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

# Protected masking regexes
FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.S)
WIKILINK_RE = re.compile(r"\[\[[^\]]+\]\]")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
OBSIDIAN_COMMENT_RE = re.compile(r"%%.*?%%", re.S)
CODE_FENCE_RE = re.compile(r"```.*?```", re.S)

# Latin name pattern to match English author names (capital followed by letters, requiring at least one lowercase letter to avoid all-uppercase acronyms like GPS, EEF, FDA)
LATIN_NAME = r"\b[A-ZÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ'-]*[a-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ'-]*\b"

def mask_protected(text: str) -> tuple[str, list[str]]:
    protected = []
    def repl(m):
        protected.append(m.group(0))
        return f"\uE000{len(protected) - 1}\uE001"
    for rx in [CODE_FENCE_RE, HTML_COMMENT_RE, OBSIDIAN_COMMENT_RE, WIKILINK_RE, INLINE_CODE_RE]:
        text = rx.sub(repl, text)
    return text, protected

def unmask(text: str, protected: list[str]) -> str:
    def repl(m):
        return protected[int(m.group(1))]
    return re.sub(r"\uE000(\d+)\uE001", repl, text)

def clean_body_citations(body: str, rel_path: str) -> str:
    # 1. File-specific hardcoded replacements (handled before general cleanup)
    # This resolves missing years and specific complex cases cleanly.
    
    # Brock_2025:
    if "Argument_Brock_2025_DataAccessGenerationUse.md" in rel_path:
        body = body.replace("学术文献（Tedersoo et al.、Wilkinson et al.、Klein & Verhulst）", 
                            "学术文献 (Tedersoo et al., 2021; Wilkinson et al., 2016; Klein & Verhulst, 2017)")
        body = body.replace("学术文献（Tedersoo et al.、Wilkinson et al.、Klein 和 Verhulst）", 
                            "学术文献 (Tedersoo et al., 2021; Wilkinson et al., 2016; Klein & Verhulst, 2017)")
        
    # Wolf_2025:
    if "Argument_Wolf_2025_InternationalResearchCollab.md" in rel_path:
        body = body.replace("图17.2：Dollinger et al. 国际", "图17.2：Dollinger et al. (2018) 国际")
        
    # Golovchin_2019:
    if "Argument_Golovchin_2019_ESC.md" in rel_path:
        body = body.replace("（Snook et al., Jones）", "(Snook et al., 2009; Jones)")
        body = body.replace("（Snook et al.）", "(Snook et al., 2009)")
        body = body.replace("（Terhart, Snook et al.）", "(Terhart, 2011; Snook et al., 2009)")
        body = body.replace("（Snook et al., Terhart）", "(Snook et al., 2009; Terhart, 2011)")
        body = body.replace("(Snook et al.)", "(Snook et al., 2009)")
        
    # Nelson_2017:
    if "Argument_Nelson_2017_ER.md" in rel_path:
        body = body.replace("Wentworth et al.（本期特刊）", "Wentworth et al. (2017)")
        body = body.replace("Wentworth et al. (本期特刊)", "Wentworth et al. (2017)")
        
    # ONeill_2016:
    if "Argument_ONeill_2016_Report.md" in rel_path:
        body = re.sub(r"\s*\(O'Neill et al\.\)", "", body)
        body = re.sub(r"\s*（O'Neill et al\.\)", "", body)

    # 2. General bracket normalization
    # Convert CJK brackets to half-width brackets around years
    body = re.sub(r"[（(](\d{4}[a-z]?)[）)]", r"(\1)", body)
    
    # Convert CJK brackets to half-width brackets around page ranges
    body = re.sub(r"[（(](pp?\.?\s*\d+[^（）()]*)[）)]", r"(\1)", body)
    
    # Convert CJK brackets to half-width brackets around standard parenthetical citations
    # E.g. （Perkmann et al., 2013） -> (Perkmann et al., 2013)
    # （Ankrah & Al-Tabbaa, 2015） -> (Ankrah & Al-Tabbaa, 2015)
    body = re.sub(r"（([A-Za-zÀ-ÖØ-öø-ÿ\s&.,;’'-]+,\s*\d{4}[a-z]?[^（）]*)）", r"(\1)", body)

    # 3. General language cleanup for Latin author names
    # E.g. "Tobin、Wu 和 Davidson" -> "Tobin et al."
    # E.g. "Qin, Way 和 Mukherjee" -> "Qin et al."
    # We match three or more capitalized Latin names separated by CJK commas and CJK '和'
    pattern_3plus = re.compile(
        rf"\b({LATIN_NAME})(?:[、,\s]+{LATIN_NAME})+\s+和\s+({LATIN_NAME})\b"
    )
    body = pattern_3plus.sub(r"\1 et al.", body)

    # E.g. "Rybnicek 和 Konigsgruber" -> "Rybnicek & Konigsgruber"
    # E.g. "Ankrah 和 Al-Tabbaa" -> "Ankrah & Al-Tabbaa"
    pattern_2names = re.compile(
        rf"\b({LATIN_NAME})\s+和\s+({LATIN_NAME})\b"
    )
    body = pattern_2names.sub(r"\1 & \2", body)

    # E.g. "Perkmann 等人" / "Perkmann 等" -> "Perkmann et al."
    body = re.sub(rf"\b({LATIN_NAME})\s*(?:等|等人)", r"\1 et al.", body)

    # 4. Standardize any remaining CJK separators inside parenthetical citations
    # E.g. (Rybnicek 和 Konigsgruber, 2019) -> (Rybnicek & Konigsgruber, 2019)
    # We find parenthetical blocks and replace ' 和 ' with ' & '
    def clean_paren_content(m):
        content = m.group(1)
        # Only touch if there is a year inside
        if re.search(r"\b\d{4}[a-z]?\b", content):
            # Replace CJK separators with English ones
            content = re.sub(rf"\b({LATIN_NAME})\s+和\s+({LATIN_NAME})\b", r"\1 & \2", content)
            content = re.sub(rf"\b({LATIN_NAME})\s*(?:等|等人)", r"\1 et al.", content)
            content = content.replace("，", ",")
        return f"({content})"
    
    body = re.sub(r"\(([^()\n]+)\)", clean_paren_content, body)

    return body

def process_file(path: Path, dry_run: bool = False) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
        return False

    if not content.startswith("---\n"):
        return False

    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return False

    frontmatter = parts[1]
    body = parts[2]
    rel_path = str(path.relative_to(ROOT))

    # Mask protected regions in body to avoid modifying code blocks or wikilinks
    masked_body, protected = mask_protected(body)
    
    # Process citations in body
    cleaned_masked_body = clean_body_citations(masked_body, rel_path)
    
    # Unmask body
    cleaned_body = unmask(cleaned_masked_body, protected)

    if cleaned_body != body:
        if dry_run:
            print(f"Would update {rel_path}")
            # print diff of lines
            lines_before = body.splitlines()
            lines_after = cleaned_body.splitlines()
            for idx, (lbl, la) in enumerate(zip(lines_before, lines_after)):
                if lbl != la:
                    print(f"  Line {idx+1}:")
                    print(f"    - {lbl.strip()}")
                    print(f"    + {la.strip()}")
        else:
            new_content = f"---\n{frontmatter}---\n{cleaned_body}"
            path.write_text(new_content, encoding="utf-8")
            print(f"Updated {rel_path}")
        return True

    return False

def main() -> int:
    parser = argparse.ArgumentParser(description="Cleanup argument page citations.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing.")
    args = parser.parse_args()

    if not ARGUMENTS_DIR.exists():
        print(f"Arguments directory not found: {ARGUMENTS_DIR}", file=sys.stderr)
        return 1

    changed = 0
    total = 0
    for root, _, files in os.walk(ARGUMENTS_DIR):
        for f in sorted(files):
            if f.endswith(".md") and f != "index.md" and not f.startswith("."):
                path = Path(root) / f
                total += 1
                if process_file(path, dry_run=args.dry_run):
                    changed += 1

    mode = "dry-run" if args.dry_run else "active"
    print(f"Finished ({mode}): checked {total} files, updated {changed} files.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
