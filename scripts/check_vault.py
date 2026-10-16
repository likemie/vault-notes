#!/usr/bin/env python3
"""Read-only validation for local changes or a committed CI change range."""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE_ENV = dict(os.environ, VAULT_LINT_SKIP_GATE="1")


def git_paths(*args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, stdout=subprocess.PIPE,
    )
    return [p.decode("utf-8") for p in result.stdout.split(b"\0") if p]


def changed_markdown(base: str | None) -> list[str]:
    if base:
        if set(base) == {"0"}:
            paths = git_paths("ls-files", "-z")
        else:
            paths = git_paths("diff", "--name-only", "--diff-filter=ACMR", "-z", base, "HEAD", "--")
    else:
        paths = git_paths("diff", "--name-only", "--diff-filter=ACMR", "-z", "HEAD", "--")
        paths += git_paths("ls-files", "--others", "--exclude-standard", "-z")
    return sorted({
        p for p in paths
        if p.endswith(".md") and (ROOT / p).is_file()
        and (p.startswith(("wiki/", "sources/", "books/", "schema/"))
             or p in {"vault-schema.md", "vault-use.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md"})
    })


def run_checks(base: str | None = None) -> int:
    commands = [
        ["-m", "unittest", "discover", "-s", "tests", "-q"],
        ["scripts/journal_index.py", "--check"],
        ["scripts/wiki_index.py", "--check"],
        ["scripts/citation_index.py", "--check"],
    ]
    paths = changed_markdown(base)
    lint_args = ["scripts/vault_lint.py"]
    for path in paths:
        lint_args.extend(["--path", path])
    commands.append(lint_args)
    print(f"[check] Markdown files selected: {len(paths)}", flush=True)
    for command in commands:
        print(f"[check] {' '.join(command[:5])}", flush=True)
        # vault_lint.py also runs these gate checks; skip them there since
        # this script has already run tests and both index checks above.
        env = dict(GATE_ENV)
        if base:
            env["VAULT_JOURNAL_BASE"] = base
        result = subprocess.run([sys.executable, "-B", *command], cwd=ROOT, env=env)
        if result.returncode:
            return result.returncode
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="Compare this commit with HEAD; use the push-before or PR base SHA in CI.")
    args = parser.parse_args()
    return run_checks(args.base)


if __name__ == "__main__":
    raise SystemExit(main())
