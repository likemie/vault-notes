#!/usr/bin/env python3
"""Minimal journal-name → unique filename-code registry; no generated metadata."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "citation/journals.json"
ARTICLES = ROOT / "wiki/arguments/journal-articles"


def name_key(value: str) -> str:
    return unicodedata.normalize("NFC", value).casefold()


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate journal name: {key!r}")
        result[key] = value
    return result


def load_registry(path: Path | None = None) -> dict[str, str]:
    data = json.loads((path or REGISTRY).read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)
    if not isinstance(data, dict):
        raise ValueError("journal registry must be a journal-name to code mapping")
    names, codes = set(), {}
    for journal, code in data.items():
        if not journal.strip() or journal != journal.strip() or name_key(journal) in names:
            raise ValueError(f"invalid or duplicate journal name: {journal!r}")
        if not isinstance(code, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", code):
            raise ValueError(f"invalid journal code for {journal!r}: {code!r}")
        if code.casefold() in codes:
            raise ValueError(f"journal code {code!r} is shared by {codes[code.casefold()]!r} and {journal!r}")
        names.add(name_key(journal))
        codes[code.casefold()] = journal
    return data


def metadata(text: str) -> dict:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    data = yaml.safe_load(match.group(1)) if match else None
    return data if isinstance(data, dict) else {}


def article_problem(path: Path, meta: dict, registry: dict[str, str]) -> str | None:
    journal = str(meta.get("journal") or "").strip()
    if not journal:
        return "journal full name is missing"
    code = registry.get(journal)
    if code is None:
        return f"journal is not registered in citation/journals.json: {journal!r}"
    if not re.fullmatch(r"Argument_.+_(?:19|20)\d{2}[a-z]?_" + re.escape(code), path.stem):
        return f"journal filename must end in _<Year>_{code}: {journal!r}"
    return None


def is_legacy(path: Path, meta: dict, base: str | None = None) -> bool:
    """Grandfather an unchanged journal/name pair, never a new or renamed path."""
    ref = base or os.environ.get("VAULT_JOURNAL_BASE") or "HEAD"
    if set(ref) == {"0"}:
        return False
    try:
        relative = path.relative_to(ROOT).as_posix()
        result = subprocess.run(["git", "show", f"{ref}:{relative}"], cwd=ROOT,
                                capture_output=True, text=True)
        return result.returncode == 0 and str(metadata(result.stdout).get("journal") or "").strip() == str(meta.get("journal") or "").strip()
    except (ValueError, OSError, yaml.YAMLError):
        return False


def check_articles(registry: dict[str, str], base: str | None = None) -> list[str]:
    errors = []
    for path in sorted(ARTICLES.rglob("*.md")):
        if path.name == "index.md":
            continue
        meta = metadata(path.read_text(encoding="utf-8"))
        if meta.get("type") != "argument":
            continue
        problem = article_problem(path, meta, registry)
        if problem and not is_legacy(path, meta, base):
            errors.append(f"{path.relative_to(ROOT)}: {problem}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Read-only check (also the default).")
    parser.add_argument("--register", nargs=2, metavar=("JOURNAL", "CODE"), help="Register a new journal explicitly; existing assignments cannot be changed here.")
    args = parser.parse_args()
    try:
        registry = load_registry()
        if args.register:
            journal, code = args.register
            if journal in registry and registry[journal] != code:
                raise ValueError(f"journal already registered as {registry[journal]!r}; changing it requires a naming review")
            registry[journal] = code
            # Validate the proposed table before replacing the authoritative file.
            encoded = json.dumps(dict(sorted(registry.items())), ensure_ascii=False, separators=(",", ":")) + "\n"
            proposed = REGISTRY.with_suffix(".json.tmp")
            try:
                proposed.write_text(encoded, encoding="utf-8")
                load_registry(proposed)
                proposed.replace(REGISTRY)
            finally:
                proposed.unlink(missing_ok=True)
        errors = check_articles(registry)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"Journal registry error: {exc}")
        return 1
    for error in errors:
        print(f"Journal naming error: {error}")
    print(f"Journal registry: {len(registry)} journals; {len(errors)} error(s).")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
