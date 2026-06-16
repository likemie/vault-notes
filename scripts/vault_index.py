#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

"""
vault_index.py

Run the vault's base index maintenance in the required order:
  1. scripts/book_overview.py
  2. scripts/wiki_index.py
  3. scripts/citation_index.py

The underlying scripts stay separate because they maintain different generated
surfaces: book overview skeletons, wiki indexes, and Argument citation
aliases/indexes. This file is the daily unified entry point.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

VAULT_ROOT = Path("/Users/shaoyangwu/Documents/MyNotes")
VENV_PYTHON = VAULT_ROOT / ".venv" / "bin" / "python"

if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"


def run_script(script_name: str, extra_args: list[str] | None = None) -> int:
    cmd = [sys.executable, str(SCRIPTS_DIR / script_name)]
    if extra_args:
        cmd.extend(extra_args)

    print(f"$ {Path(sys.executable).name} scripts/{script_name}" + (f" {' '.join(extra_args)}" if extra_args else ""), flush=True)
    completed = subprocess.run(cmd, cwd=ROOT)
    return completed.returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run wiki and citation base indexes.")
    parser.add_argument("--book-only", action="store_true", help="Run only scripts/book_overview.py.")
    parser.add_argument("--book-check", action="store_true", help="Pass --check to scripts/book_overview.py.")
    parser.add_argument("--book-dry-run", action="store_true", help="Pass --dry-run to scripts/book_overview.py.")
    parser.add_argument("--wiki-only", action="store_true", help="Run only scripts/wiki_index.py.")
    parser.add_argument("--citation-only", action="store_true", help="Run only scripts/citation_index.py.")
    parser.add_argument("--citation-check", action="store_true", help="Pass --check to scripts/citation_index.py.")
    parser.add_argument("--citation-dry-run", action="store_true", help="Pass --dry-run to scripts/citation_index.py.")
    parser.add_argument("--full", action="store_true", help="Pass --full to scripts/citation_index.py for workflow symmetry.")
    args = parser.parse_args(argv)

    only_flags = [args.book_only, args.wiki_only, args.citation_only]
    if sum(1 for flag in only_flags if flag) > 1:
        parser.error("--book-only, --wiki-only, and --citation-only cannot be combined")

    book_args: list[str] = []
    if args.book_check:
        book_args.append("--check")
    if args.book_dry_run:
        book_args.append("--dry-run")

    citation_args: list[str] = []
    if args.citation_check:
        citation_args.append("--check")
    if args.citation_dry_run:
        citation_args.append("--dry-run")
    if args.full:
        citation_args.append("--full")

    if args.book_only:
        return run_script("book_overview.py", book_args)

    if not args.wiki_only and not args.citation_only:
        code = run_script("book_overview.py", book_args)
        if code:
            return code

    if not args.citation_only and not args.book_only:
        code = run_script("wiki_index.py")
        if code:
            return code

    if not args.wiki_only and not args.book_only:
        code = run_script("citation_index.py", citation_args)
        if code:
            return code

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
