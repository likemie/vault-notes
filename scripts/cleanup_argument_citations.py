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

# Non-author Latin terms to exclude from replacement
EXCLUDED_TERMS = {
    "pfizer", "celgene", "squibb", "biopôle", "counts", "trust", "mathematica", 
    "elsevier", "google", "deepmind", "alphafold", "ofsted", "oecd", "mdrc", 
    "rand", "pew", "charitable", "saab", "woodside", "nexplore", "evonik", "fargo", 
    "shell", "bayer", "boeing", "leidos", "mantech", "dynamics", "parsons", "hamilton", 
    "northrop", "grumman", "lilly", "endowment", "hipaa", "ferpa", "gdpr", "nist", "uw", 
    "uva", "yale", "u-m", "madison", "internet", "gps", "eef", "fda", "abb", "ai",
    "emos", "emo", "timss", "pisa", "rct", "ebp", "cpd", "pgce", "ip", "guirr",
    "uidp", "iqvia", "ctti", "cip", "mcc", "cis", "aitsl", "ite", "clt", "sd",
    "se", "ci", "show", "open", "high", "low", "level", "figure", "table", "map",
    "step", "page", "chapter", "part", "section", "appendix", "volume", "issue",
    "analytics", "haloscience", "prescouter", "firstignite", "pillar", "pure", "pivot",
    "academy", "institute", "foundation", "university", "school", "college", "association",
    "center", "centre", "lab", "laboratory", "corporation", "company", "agency", "council",
    "department", "office", "government", "state", "union", "museum", "alliance", 
    "consortium", "network", "district", "park"
}

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

    # 3. General language cleanup for Latin author names (outside parentheses, followed by year)
    # E.g. "Rybnicek 和 Konigsgruber (2019)" -> "Rybnicek & Konigsgruber (2019)"
    # We restrict to matches followed by a year to avoid matching names in normal prose sentences.
    pattern_2names = re.compile(
        rf"\b({LATIN_NAME})\s+和\s+({LATIN_NAME})\s*(?=[(（]\d{{4}})"
    )
    def repl_2names(m):
        n1, n2 = m.group(1), m.group(2)
        if n1.lower() in EXCLUDED_TERMS or n2.lower() in EXCLUDED_TERMS:
            return m.group(0)
        return f"{n1} & {n2}"
    body = pattern_2names.sub(repl_2names, body)

    # E.g. "Tobin、Wu 和 Davidson (2019)" -> "Tobin et al. (2019)"
    # We require comma/semicolon separators (not space) and lookahead for a year.
    pattern_3plus = re.compile(
        rf"\b({LATIN_NAME})(?:[、,;]\s*{LATIN_NAME})+\s+和\s+({LATIN_NAME})\s*(?=[(（]\d{{4}})"
    )
    def repl_3plus(m):
        n1 = m.group(1)
        if n1.lower() in EXCLUDED_TERMS:
            return m.group(0)
        return f"{n1} et al."
    body = pattern_3plus.sub(repl_3plus, body)

    # E.g. "Biesta、Wrigley、Wiliam 等" -> "Biesta et al."
    # E.g. "Biesta 和 Wrigley 等人" -> "Biesta et al."
    pattern_deng_list = re.compile(
        rf"\b({LATIN_NAME})(?:(?:[、,;]\s*{LATIN_NAME})+(?:\s+和\s+{LATIN_NAME})?|(?:\s+和\s+{LATIN_NAME}))\s*(?:等人|等)"
    )
    def repl_deng_list(m):
        words = re.findall(rf"{LATIN_NAME}", m.group(0))
        if any(w.lower() in EXCLUDED_TERMS for w in words):
            return m.group(0)
        return f"{m.group(1)} et al."
    body = pattern_deng_list.sub(repl_deng_list, body)

    # E.g. "Perkmann 等人" / "Perkmann 等" -> "Perkmann et al."
    def repl_deng(m):
        n = m.group(1)
        if n.lower() in EXCLUDED_TERMS:
            return m.group(0)
        return f"{n} et al."
    body = re.sub(rf"\b({LATIN_NAME})\s*(?:等人|等)", repl_deng, body)

    # 4. Standardize any remaining CJK separators inside parenthetical citations
    # E.g. (Rybnicek 和 Konigsgruber, 2019) -> (Rybnicek & Konigsgruber, 2019)
    # We find parenthetical blocks and replace CJK separators/punctuation with English counterparts.
    def clean_paren_content(m):
        content = m.group(1)
        # Only touch if there is a year inside
        if re.search(r"\b\d{4}[a-z]?\b", content):
            def repl_2names_paren(m2):
                n1, n2 = m2.group(1), m2.group(2)
                if n1.lower() in EXCLUDED_TERMS or n2.lower() in EXCLUDED_TERMS:
                    return m2.group(0)
                return f"{n1} & {n2}"
            
            def repl_deng_paren(m2):
                n = m2.group(1)
                if n.lower() in EXCLUDED_TERMS:
                    return m2.group(0)
                return f"{n} et al."

            def repl_deng_list_paren(m2):
                words = re.findall(rf"{LATIN_NAME}", m2.group(0))
                if any(w.lower() in EXCLUDED_TERMS for w in words):
                    return m2.group(0)
                return f"{m2.group(1)} et al."

            content = re.sub(pattern_deng_list, repl_deng_list_paren, content)
            content = re.sub(rf"\b({LATIN_NAME})\s+和\s+({LATIN_NAME})\b", repl_2names_paren, content)
            content = re.sub(rf"\b({LATIN_NAME})\s*(?:等人|等)", repl_deng_paren, content)
            content = content.replace("，", ",").replace("；", ";")
        return f"({content})"
    
    body = re.sub(r"\(([^()\n]+)\)", clean_paren_content, body)

    # 5. Clean up any accidental leftover 'et al.人' or 'et al.等'
    body = re.sub(r"\bet\s+al\.\s*(?:人|等)", "et al.", body)

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
