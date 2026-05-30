#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
source_record.py

Create and finalize minimal source records for an Obsidian / Quartz academic vault.

Design aligned with vault-schema.md:
- AI / user classifies source type first; this script does not infer source type.
- For article / report sources, creation is intentionally early and minimal.
- Citation is normally finalized later from the corresponding Argument page.
- source record `extracted_to` is treated as generated data and should be synced by
  wiki_relations.py, not maintained by this script.

Typical article workflow:
  1) Create a minimal source record and move/copy the PDF:
     python3 scripts/source_record.py article --file raw/paper.pdf --record-name temp_name

  2) After the Argument page is written, finalize citation and optionally rename:
     python3 scripts/source_record.py finalize \
       --argument "wiki/arguments/journal-articles/Educational Research and Evaluation/Argument_Simpson_2019_ERE.md" \
       --rename

Supported subcommands:
  article
  report
  finalize
  monograph-pdf
  monograph-epub
  edited-volume-overview
  book-chapter

Expected location:
  /Users/shaoyangwu/Documents/MyNotes/scripts/source_record.py
"""

from __future__ import annotations

# Auto-use the vault virtual environment when available.
# This keeps scripts runnable as `python3 scripts/<script>.py` while using
# dependencies installed in /Users/shaoyangwu/Documents/MyNotes/.venv.
import os
import sys
from pathlib import Path

VAULT_ROOT = Path("/Users/shaoyangwu/Documents/MyNotes")
VENV_PYTHON = VAULT_ROOT / ".venv" / "bin" / "python"

if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])


import argparse
import datetime as _dt
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

ROOT = Path.cwd()
RAW_DIR = ROOT / "raw"
SOURCES_DIR = ROOT / "sources"
BOOKS_DIR = ROOT / "books"

WIKILINK_RE = re.compile(r"^\[\[([^\]|#\n]+)(?:[#|][^\]\n]*)?\]\]$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
SOURCE_SECTION_RE = re.compile(r"(^##\s+(?:来源|Sources)\s*$)(.*?)(?=^##\s+|\Z)", re.DOTALL | re.MULTILINE)

FORBIDDEN_FILENAME_CHARS = r'<>:"/\\|?*'


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except Exception:
        return path.as_posix()


def die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def info(msg: str) -> None:
    print(msg)


def today() -> str:
    return _dt.date.today().isoformat()


def ensure_parent(path: Path, dry_run: bool = False) -> None:
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)


def validate_file(path: Path, suffixes: set[str]) -> None:
    if not path.exists():
        die(f"File does not exist: {rel(path)}")
    if not path.is_file():
        die(f"Path is not a file: {rel(path)}")
    if path.suffix.lower() not in suffixes:
        die(f"Expected suffix {sorted(suffixes)}, got {path.suffix}: {rel(path)}")


def validate_record_name(name: str) -> str:
    s = name.strip()
    if not s:
        die("Record name cannot be empty")
    s = Path(s).stem if s.endswith(".md") else s
    if any(ch in s for ch in FORBIDDEN_FILENAME_CHARS):
        die(f"Record name contains path-unsafe characters: {name!r}")
    if s in {".", ".."}:
        die(f"Invalid record name: {name!r}")
    return s


def safe_stem_from_file(path: Path) -> str:
    stem = path.stem.strip()
    stem = re.sub(rf"[{re.escape(FORBIDDEN_FILENAME_CHARS)}]", " ", stem)
    stem = re.sub(r"\s+", " ", stem).strip()
    stem = stem.replace(" ", "_")
    return validate_record_name(stem or "source")


def yaml_scalar(value: str) -> str:
    # Always write YAML scalars in double quotes for predictable frontmatter.
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_block_list(items: List[str]) -> str:
    if not items:
        return " []"
    return "\n" + "\n".join(f"  - {yaml_scalar(item)}" for item in items)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str, *, overwrite: bool = True, dry_run: bool = False) -> None:
    if path.exists() and not overwrite:
        die(f"Output file already exists: {rel(path)}. Use --overwrite.")
    if dry_run:
        info(f"DRY RUN: would write {rel(path)}")
        print("\n--- preview ---\n")
        print(content)
        return
    ensure_parent(path)
    path.write_text(content, encoding="utf-8")
    info(f"Wrote {rel(path)}")


def move_or_copy(src: Path, dest: Path, *, copy: bool, overwrite: bool, dry_run: bool = False) -> Path:
    if dest.exists() and src.resolve() != dest.resolve() and not overwrite:
        die(f"Destination file already exists: {rel(dest)}. Use --overwrite.")
    if dry_run:
        action = "copy" if copy else "move"
        info(f"DRY RUN: would {action} {rel(src)} -> {rel(dest)}")
        return dest
    ensure_parent(dest)
    if src.resolve() == dest.resolve():
        info(f"File already in place: {rel(dest)}")
        return dest
    if copy:
        shutil.copy2(src, dest)
        info(f"Copied {rel(src)} -> {rel(dest)}")
    else:
        shutil.move(str(src), str(dest))
        info(f"Moved {rel(src)} -> {rel(dest)}")
    return dest


def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, "", text
    raw = m.group(1)
    body = text[m.end():]
    if yaml is None:
        die("PyYAML is required to parse frontmatter")
    try:
        data = yaml.safe_load(raw) or {}
    except Exception as exc:
        die(f"Cannot parse YAML frontmatter: {exc}")
    if not isinstance(data, dict):
        die("Frontmatter must be a YAML mapping")
    return data, raw, body


def dump_minimal_source_frontmatter(citation: str, processed_date: str) -> str:
    # Keep extracted_to as an empty generated field placeholder for compatibility.
    return "\n".join([
        "---",
        f"citation: {yaml_scalar(citation)}",
        "extracted_to: []",
        f"processed_date: {processed_date}",
        "---",
    ])


def source_record_content(record_name: str, pdf_filename: str, *, citation: str = "", processed_date: Optional[str] = None) -> str:
    fm = dump_minimal_source_frontmatter(citation, processed_date or today())
    return f"{fm}\n\n# {record_name}\n\n![[{pdf_filename}]]\n"


def create_article_or_report(args: argparse.Namespace, kind: str) -> None:
    src = Path(args.file)
    validate_file(src, {".pdf"})

    record_name = validate_record_name(args.record_name) if args.record_name else safe_stem_from_file(src)
    md_path = SOURCES_DIR / f"{record_name}.md"
    pdf_path = SOURCES_DIR / f"{record_name}.pdf"

    move_or_copy(src, pdf_path, copy=args.copy, overwrite=args.overwrite, dry_run=args.dry_run)
    content = source_record_content(
        record_name,
        pdf_path.name,
        citation=args.citation or "",
        processed_date=args.processed_date or today(),
    )
    write_text(md_path, content, overwrite=args.overwrite, dry_run=args.dry_run)
    info(f"Created minimal {kind} source record: {rel(md_path)}")
    info("Next: write the Argument page, then run `source_record.py finalize --argument ... --rename` if needed.")


def wikilink_target(value: str) -> Optional[str]:
    m = WIKILINK_RE.match(value.strip())
    if not m:
        return None
    return m.group(1).strip()


def first_source_from_argument(fm: Dict[str, Any], body: str) -> Optional[str]:
    sources = fm.get("sources")
    if isinstance(sources, list):
        for item in sources:
            if isinstance(item, str) and wikilink_target(item):
                return wikilink_target(item)

    m = SOURCE_SECTION_RE.search(body)
    if m:
        for link in re.findall(r"\[\[[^\]\n]+\]\]", m.group(2)):
            target = wikilink_target(link)
            if target:
                return target
    return None


def argument_default_record_name(argument_path: Path) -> str:
    stem = argument_path.stem
    if stem.startswith("Argument_"):
        stem = stem[len("Argument_"):]
    return validate_record_name(stem)


def update_source_record_text(old_text: str, *, new_name: str, citation: str, pdf_filename: str, processed_date: Optional[str]) -> str:
    fm, raw_fm, body = parse_frontmatter(old_text)
    if processed_date is None:
        processed_date = str(fm.get("processed_date") or today())

    # Do not preserve or rewrite extracted_to values here. It is generated by wiki_relations.py.
    new_fm = dump_minimal_source_frontmatter(citation, processed_date)

    # Keep the source record body intentionally minimal. This also removes older complex sections.
    return f"{new_fm}\n\n# {new_name}\n\n![[{pdf_filename}]]\n"


def replace_source_link_in_argument(text: str, old_name: str, new_name: str) -> str:
    if old_name == new_name:
        return text

    # Update only exact source wikilinks. This changes both frontmatter sources and ## 来源 body if present.
    # That is intentional after a source record rename; relation fields can be resynced afterwards.
    patterns = [
        (f"[[{old_name}]]", f"[[{new_name}]]"),
        (f"[[{old_name}|", f"[[{new_name}|"),
        (f"[[{old_name}#", f"[[{new_name}#"),
    ]
    out = text
    for old, new in patterns:
        out = out.replace(old, new)
    return out


def maybe_rename_file(old_path: Path, new_path: Path, *, overwrite: bool, dry_run: bool) -> Path:
    if old_path.resolve() == new_path.resolve():
        return old_path
    if new_path.exists() and not overwrite:
        die(f"Rename target already exists: {rel(new_path)}. Use --overwrite.")
    if dry_run:
        info(f"DRY RUN: would rename {rel(old_path)} -> {rel(new_path)}")
        return new_path
    ensure_parent(new_path)
    if new_path.exists() and overwrite:
        new_path.unlink()
    old_path.rename(new_path)
    info(f"Renamed {rel(old_path)} -> {rel(new_path)}")
    return new_path


def finalize_source(args: argparse.Namespace) -> None:
    argument_path = Path(args.argument)
    validate_file(argument_path, {".md"})
    arg_text = read_text(argument_path)
    arg_fm, _raw_arg_fm, arg_body = parse_frontmatter(arg_text)

    citation = str(arg_fm.get("citation") or "").strip()
    if not citation:
        die("Argument frontmatter has no `citation`; finalize cannot infer citation from PDF metadata.")

    old_source_name: Optional[str] = None
    if args.source:
        source_path = Path(args.source)
        if source_path.suffix != ".md":
            source_path = source_path.with_suffix(".md")
        old_source_name = source_path.stem
    else:
        old_source_name = first_source_from_argument(arg_fm, arg_body)
        if not old_source_name:
            die("Cannot find source wikilink from Argument frontmatter `sources` or `## 来源`. Pass --source.")
        source_path = SOURCES_DIR / f"{old_source_name}.md"

    validate_file(source_path, {".md"})

    if args.new_name:
        new_name = validate_record_name(args.new_name)
    elif args.rename:
        new_name = argument_default_record_name(argument_path)
    else:
        new_name = source_path.stem

    new_md_path = source_path.with_name(f"{new_name}.md")

    old_pdf_path = source_path.with_suffix(".pdf")
    new_pdf_path = new_md_path.with_suffix(".pdf")
    pdf_filename = new_pdf_path.name if (args.rename or args.new_name) else old_pdf_path.name

    old_source_text = read_text(source_path)
    new_source_text = update_source_record_text(
        old_source_text,
        new_name=new_name,
        citation=citation,
        pdf_filename=pdf_filename,
        processed_date=args.processed_date,
    )

    # Write source content before rename if same file; otherwise write after deciding path.
    if new_md_path.resolve() == source_path.resolve():
        write_text(source_path, new_source_text, overwrite=True, dry_run=args.dry_run)
    else:
        if new_md_path.exists() and not args.overwrite:
            die(f"Finalize target already exists: {rel(new_md_path)}. Use --overwrite.")
        if args.dry_run:
            info(f"DRY RUN: would write finalized source to {rel(new_md_path)}")
            print("\n--- finalized source preview ---\n")
            print(new_source_text)
            info(f"DRY RUN: would remove old source record {rel(source_path)}")
        else:
            ensure_parent(new_md_path)
            new_md_path.write_text(new_source_text, encoding="utf-8")
            source_path.unlink()
            info(f"Finalized and renamed source record {rel(source_path)} -> {rel(new_md_path)}")

    if old_pdf_path.exists():
        maybe_rename_file(old_pdf_path, new_pdf_path, overwrite=args.overwrite, dry_run=args.dry_run)
    else:
        info(f"WARNING: expected PDF not found next to source record: {rel(old_pdf_path)}")

    if old_source_name and old_source_name != new_name:
        updated_arg_text = replace_source_link_in_argument(arg_text, old_source_name, new_name)
        if updated_arg_text != arg_text:
            write_text(argument_path, updated_arg_text, overwrite=True, dry_run=args.dry_run)
            info(f"Updated source wikilink in Argument page: [[{old_source_name}]] -> [[{new_name}]]")

    info("Finalize complete. Run `python3 scripts/wiki_index.py`; run relations/lint only after user confirmation per vault-schema.")


# -----------------------------
# Book-source helpers
# -----------------------------


def book_folder_path(book_folder: str) -> Path:
    if "/" in book_folder or "\\" in book_folder:
        die("--book-folder must be a folder name, not a path")
    return BOOKS_DIR / book_folder


def ensure_wikilink(value: str, name: str) -> str:
    s = value.strip()
    if not WIKILINK_RE.match(s):
        die(f"{name} must be a wikilink like [[Entry Name]], got: {value!r}")
    return s


def parse_wikilink_list(value: Optional[str]) -> List[str]:
    if not value:
        return []
    out: List[str] = []
    seen = set()
    for part in value.split(","):
        s = part.strip()
        if not s:
            continue
        ensure_wikilink(s, "wikilink list item")
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def book_source_frontmatter(citation: str, processed_date: str, part_of: Optional[str] = None) -> str:
    lines = [
        "---",
        f"citation: {yaml_scalar(citation)}",
        "extracted_to: []",
        f"processed_date: {processed_date}",
    ]
    if part_of:
        lines.append(f"part_of: {yaml_scalar(part_of)}")
    lines.append("---")
    return "\n".join(lines)


def create_book_source_record(
    *,
    md_path: Path,
    record_title: str,
    citation: str,
    embedded_file: Optional[str],
    part_of: Optional[str],
    processed_date: str,
    overwrite: bool,
    dry_run: bool,
) -> None:
    fm = book_source_frontmatter(citation, processed_date, part_of)
    body = f"# {record_title}\n"
    if embedded_file:
        body += f"\n![[{embedded_file}]]\n"
    content = f"{fm}\n\n{body}"
    write_text(md_path, content, overwrite=overwrite, dry_run=dry_run)


def monograph_pdf(args: argparse.Namespace) -> None:
    book_dir = book_folder_path(args.book_folder)
    src = Path(args.file)
    validate_file(src, {".pdf"})
    record_name = validate_record_name(args.record_name or book_dir.name)
    pdf_path = book_dir / f"{record_name}.pdf"
    md_path = book_dir / f"{record_name}.md"
    move_or_copy(src, pdf_path, copy=args.copy, overwrite=args.overwrite, dry_run=args.dry_run)
    create_book_source_record(
        md_path=md_path,
        record_title=record_name,
        citation=args.citation or "",
        embedded_file=pdf_path.name,
        part_of=None,
        processed_date=args.processed_date or today(),
        overwrite=args.overwrite,
        dry_run=args.dry_run,
    )


def monograph_epub(args: argparse.Namespace) -> None:
    book_dir = book_folder_path(args.book_folder)
    src = Path(args.file)
    validate_file(src, {".epub"})
    record_name = validate_record_name(args.record_name or book_dir.name)
    epub_path = book_dir / f"{record_name}.epub"
    md_path = book_dir / f"{record_name}.md"
    move_or_copy(src, epub_path, copy=args.copy, overwrite=args.overwrite, dry_run=args.dry_run)
    create_book_source_record(
        md_path=md_path,
        record_title=record_name,
        citation=args.citation or "",
        embedded_file=epub_path.name,
        part_of=None,
        processed_date=args.processed_date or today(),
        overwrite=args.overwrite,
        dry_run=args.dry_run,
    )


def edited_volume_overview(args: argparse.Namespace) -> None:
    book_dir = book_folder_path(args.book_folder)
    record_name = validate_record_name(args.record_name or book_dir.name)
    md_path = book_dir / f"{record_name}.md"
    create_book_source_record(
        md_path=md_path,
        record_title=record_name,
        citation=args.citation or "",
        embedded_file=None,
        part_of=None,
        processed_date=args.processed_date or today(),
        overwrite=args.overwrite,
        dry_run=args.dry_run,
    )


def book_chapter(args: argparse.Namespace) -> None:
    book_dir = book_folder_path(args.book_folder)
    record_name = validate_record_name(args.record_name)
    md_path = book_dir / f"{record_name}.md"
    part_of = ensure_wikilink(args.part_of, "--part-of") if args.part_of else None
    create_book_source_record(
        md_path=md_path,
        record_title=record_name,
        citation=args.citation or "",
        embedded_file=None,
        part_of=part_of,
        processed_date=args.processed_date or today(),
        overwrite=args.overwrite,
        dry_run=args.dry_run,
    )


# -----------------------------
# CLI
# -----------------------------


def add_common_create_flags(p: argparse.ArgumentParser) -> None:
    p.add_argument("--record-name", help="Source record/PDF basename without extension. Optional early; can be finalized later.")
    p.add_argument("--citation", default="", help="Optional early citation. Prefer leaving empty and using finalize from Argument page.")
    p.add_argument("--processed-date", help="ISO date. Defaults to today.")
    p.add_argument("--copy", action="store_true", help="Copy file instead of moving it.")
    p.add_argument("--overwrite", action="store_true", help="Overwrite existing destination files.")
    p.add_argument("--dry-run", action="store_true", help="Preview actions without writing files.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create/finalize minimal source records for MyNotes vault.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_article = sub.add_parser("article", help="Create an early minimal journal-article source record in sources/.")
    p_article.add_argument("--file", required=True, help="PDF file, usually under raw/.")
    add_common_create_flags(p_article)
    p_article.set_defaults(func=lambda args: create_article_or_report(args, "article"))

    p_report = sub.add_parser("report", help="Create an early minimal report/policy-document source record in sources/.")
    p_report.add_argument("--file", required=True, help="PDF file, usually under raw/.")
    add_common_create_flags(p_report)
    p_report.set_defaults(func=lambda args: create_article_or_report(args, "report"))

    p_fin = sub.add_parser("finalize", help="Finalize citation from an Argument page and optionally rename source record/PDF.")
    p_fin.add_argument("--argument", required=True, help="Path to the completed Argument page.")
    p_fin.add_argument("--source", help="Path to source record md. If omitted, inferred from Argument `sources` or `## 来源`.")
    p_fin.add_argument("--rename", action="store_true", help="Rename source record/PDF to Argument filename without `Argument_` prefix.")
    p_fin.add_argument("--new-name", help="Explicit final source record/PDF basename. Implies rename target name.")
    p_fin.add_argument("--processed-date", help="Override processed_date; default preserves existing value or uses today.")
    p_fin.add_argument("--overwrite", action="store_true", help="Overwrite rename targets if they already exist.")
    p_fin.add_argument("--dry-run", action="store_true", help="Preview actions without writing files.")
    p_fin.set_defaults(func=finalize_source)

    p_mpdf = sub.add_parser("monograph-pdf", help="Create a minimal monograph PDF source record under books/<book-folder>/.")
    p_mpdf.add_argument("--book-folder", required=True)
    p_mpdf.add_argument("--file", required=True)
    add_common_create_flags(p_mpdf)
    p_mpdf.set_defaults(func=monograph_pdf)

    p_mepub = sub.add_parser("monograph-epub", help="Create a minimal monograph EPUB source record under books/<book-folder>/.")
    p_mepub.add_argument("--book-folder", required=True)
    p_mepub.add_argument("--file", required=True)
    add_common_create_flags(p_mepub)
    p_mepub.set_defaults(func=monograph_epub)

    p_ev = sub.add_parser("edited-volume-overview", help="Create a minimal edited-volume overview source record.")
    p_ev.add_argument("--book-folder", required=True)
    p_ev.add_argument("--record-name", required=True)
    p_ev.add_argument("--citation", default="")
    p_ev.add_argument("--processed-date")
    p_ev.add_argument("--overwrite", action="store_true")
    p_ev.add_argument("--dry-run", action="store_true")
    p_ev.set_defaults(func=edited_volume_overview)

    p_ch = sub.add_parser("book-chapter", help="Create a minimal book-chapter source record.")
    p_ch.add_argument("--book-folder", required=True)
    p_ch.add_argument("--record-name", required=True)
    p_ch.add_argument("--part-of", help="Parent source wikilink, e.g. [[Book_Source_Record]].")
    p_ch.add_argument("--citation", default="")
    p_ch.add_argument("--processed-date")
    p_ch.add_argument("--overwrite", action="store_true")
    p_ch.add_argument("--dry-run", action="store_true")
    p_ch.set_defaults(func=book_chapter)

    return parser


def main(argv: Optional[List[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
