#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
source_record.py

Create source records and reading pages for an Obsidian / Quartz academic vault.

Design:
- AI / user classifies source type first.
- This script does NOT infer source type from PDF content.
- This script validates parameters and creates standardized source Markdown records.

Supported subcommands:
  article
  report
  monograph-pdf
  monograph-epub
  edited-volume-overview
  book-chapter

Expected location:
  /Users/shaoyangwu/Documents/MyNotes/scripts/source_record.py
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import shutil
import sys
from pathlib import Path
from typing import List, Optional


ROOT = Path.cwd()
RAW_DIR = ROOT / "raw"
SOURCES_DIR = ROOT / "sources"
BOOKS_DIR = ROOT / "books"

WIKILINK_RE = re.compile(r"^\[\[[^\]\n]+\]\]$")


# -----------------------------
# Basic helpers
# -----------------------------

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


def yaml_string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_list(items: List[str]) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(yaml_string(i) for i in items) + "]"


def parse_wikilink_list(value: str | None) -> List[str]:
    if not value:
        return []
    out: List[str] = []
    seen = set()
    for part in value.split(","):
        s = part.strip()
        if not s:
            continue
        if not WIKILINK_RE.match(s):
            die(f"Invalid wikilink item: {s!r}. Use [[Entry Name]].")
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def ensure_wikilink(value: str, name: str) -> str:
    s = value.strip()
    if not WIKILINK_RE.match(s):
        die(f"{name} must be a wikilink like [[Entry_Name]], got: {value!r}")
    return s


def is_under(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def validate_file(path: Path, suffixes: set[str]) -> None:
    if not path.exists():
        die(f"File does not exist: {rel(path)}")
    if not path.is_file():
        die(f"Path is not a file: {rel(path)}")
    if path.suffix.lower() not in suffixes:
        die(f"Expected suffix {sorted(suffixes)}, got {path.suffix}: {rel(path)}")


def validate_book_file(path: Path, book_dir: Path, suffixes: set[str]) -> None:
    validate_file(path, suffixes)
    if not is_under(path, book_dir):
        die(f"Book file must be under {rel(book_dir)}, got: {rel(path)}")


def book_folder_path(book_folder: str) -> Path:
    if "/" in book_folder or "\\" in book_folder:
        die("--book-folder must be a folder name, not a path")
    return BOOKS_DIR / book_folder


def move_or_copy_file(
    src: Path,
    dest: Path,
    *,
    copy: bool,
    no_move: bool,
    overwrite: bool,
    dry_run: bool,
) -> Path:
    if no_move:
        info(f"Leaving file in place: {rel(src)}")
        return src

    if dest.exists() and dest.resolve() != src.resolve() and not overwrite:
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


def safe_write(path: Path, content: str, *, overwrite: bool, dry_run: bool) -> None:
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


def extracted_section(items: List[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- "


def source_frontmatter(
    *,
    title: str,
    subtype: str,
    citation: str,
    extracted_to: List[str],
    processed_date: str,
    status: str = "processed",
    source_file: Optional[str] = None,
    book_file: Optional[str] = None,
    part_of: Optional[str] = None,
    publication_type: Optional[str] = None,
    book_title: Optional[str] = None,
    chapter_title: Optional[str] = None,
    journal: Optional[str] = None,
    issuing_organization: Optional[str] = None,
    authors: Optional[List[str]] = None,
    editors: Optional[List[str]] = None,
    publisher: Optional[str] = None,
) -> str:
    """
    Unified source-record YAML header.

    Core fields:
      title
      type: source
      subtype
      citation
      source_file or book_file
      extracted_to
      processed_date
      status

    Optional bibliographic fields are included only when provided.
    """
    lines = [
        "---",
        f"title: {yaml_string(title)}",
        "type: source",
        f"subtype: {subtype}",
    ]

    if publication_type:
        lines.append(f"publication_type: {publication_type}")
    if book_title:
        lines.append(f"book_title: {yaml_string(book_title)}")
    if chapter_title:
        lines.append(f"chapter_title: {yaml_string(chapter_title)}")
    if journal:
        lines.append(f"journal: {yaml_string(journal)}")
    if issuing_organization:
        lines.append(f"issuing_organization: {yaml_string(issuing_organization)}")
    if authors:
        lines.append(f"authors: {yaml_list(authors)}")
    if editors:
        lines.append(f"editors: {yaml_list(editors)}")
    if publisher:
        lines.append(f"publisher: {yaml_string(publisher)}")

    lines.append(f"citation: {yaml_string(citation)}")

    if source_file:
        lines.append(f"source_file: {yaml_string(source_file)}")
    if book_file:
        lines.append(f"book_file: {yaml_string(book_file)}")
    if part_of:
        lines.append(f"part_of: {yaml_string(part_of)}")

    lines.extend([
        f"extracted_to: {yaml_list(extracted_to)}",
        f"processed_date: {processed_date}",
        f"status: {status}",
        "---",
    ])
    return "\n".join(lines)


# -----------------------------
# Record builders
# -----------------------------

def create_article_or_report(
    *,
    subtype: str,
    publication_type: str,
    source_file: Path,
    citation: str,
    extracted_to: List[str],
    processed_date: str,
    overwrite: bool,
    copy: bool,
    no_move: bool,
    dry_run: bool,
    journal: Optional[str] = None,
    issuing_organization: Optional[str] = None,
) -> None:
    validate_file(source_file, {".pdf"})

    if no_move:
        final_pdf = source_file
    else:
        final_pdf = SOURCES_DIR / source_file.name
        if not is_under(source_file, RAW_DIR) and not is_under(source_file, SOURCES_DIR):
            die(f"{subtype} source PDF should come from raw/ or sources/, got: {rel(source_file)}. Use --no-move if intentional.")

    final_pdf = move_or_copy_file(
        source_file,
        final_pdf,
        copy=copy,
        no_move=no_move,
        overwrite=overwrite,
        dry_run=dry_run,
    )

    title = final_pdf.stem
    md_path = SOURCES_DIR / f"{title}.md"

    fm = source_frontmatter(
        title=title,
        subtype=subtype,
        publication_type=publication_type,
        citation=citation,
        source_file=rel(final_pdf),
        extracted_to=extracted_to,
        processed_date=processed_date,
        journal=journal,
        issuing_organization=issuing_organization,
    )

    content = f"""{fm}

# {title}

## Citation

{citation}

---

## Extracted to

{extracted_section(extracted_to)}

---

## PDF Reader

![[{final_pdf.name}]]
"""

    safe_write(md_path, content, overwrite=overwrite, dry_run=dry_run)


def create_monograph_pdf(
    *,
    book_folder: str,
    source_file: Path,
    citation: str,
    argument: str,
    extracted_to: List[str],
    processed_date: str,
    overwrite: bool,
    dry_run: bool,
    book_title: Optional[str] = None,
    authors: Optional[List[str]] = None,
    publisher: Optional[str] = None,
) -> None:
    book_dir = book_folder_path(book_folder)
    validate_book_file(source_file, book_dir, {".pdf"})

    arg = ensure_wikilink(argument, "--argument")
    all_extracted = [arg] + [x for x in extracted_to if x != arg]

    md_path = book_dir / f"{book_folder}.md"

    fm = source_frontmatter(
        title=book_folder,
        subtype="monograph-pdf",
        publication_type="book",
        book_title=book_title,
        authors=authors,
        publisher=publisher,
        citation=citation,
        book_file=rel(source_file),
        extracted_to=all_extracted,
        processed_date=processed_date,
    )

    content = f"""{fm}

# {book_folder}

## Citation

{citation}

---

## Extracted to

{extracted_section(all_extracted)}

---

## PDF Reader

![[{source_file.name}]]

---

## Notes

- 本记录用于整本专著 PDF 的 source 与阅读页面。
- 章节内容应累积在对应 Argument 的「各章概览」中。
"""

    safe_write(md_path, content, overwrite=overwrite, dry_run=dry_run)


def create_monograph_epub(
    *,
    book_folder: str,
    source_file: Path,
    citation: str,
    argument: str,
    extracted_to: List[str],
    processed_date: str,
    overwrite: bool,
    dry_run: bool,
    book_title: Optional[str] = None,
    authors: Optional[List[str]] = None,
    publisher: Optional[str] = None,
) -> None:
    book_dir = book_folder_path(book_folder)
    validate_book_file(source_file, book_dir, {".epub"})

    arg = ensure_wikilink(argument, "--argument")
    all_extracted = [arg] + [x for x in extracted_to if x != arg]

    md_path = book_dir / f"{book_folder}.md"
    data_epub = "/" + rel(source_file)

    fm = source_frontmatter(
        title=book_folder,
        subtype="monograph-epub",
        publication_type="book",
        book_title=book_title,
        authors=authors,
        publisher=publisher,
        citation=citation,
        book_file=rel(source_file),
        extracted_to=all_extracted,
        processed_date=processed_date,
    )

    content = f"""{fm}

# {book_folder}

## Citation

{citation}

---

## Extracted to

{extracted_section(all_extracted)}

---

## EPUB Reader

<div id="epub-viewer" style="width:100%;height:560px;border:1px solid rgb(204,204,204);" data-epub="{data_epub}"></div>

---

## Notes

- Obsidian 本地不渲染此 HTML，本地阅读用 Epub Reader 插件直接打开 epub。
- Quartz 网页端通过 `/static/` 中已配置的脚本渲染。
- 不要在本文件中重复写入 `epub-loader.js` 或 `epub-init.js` 源码。
"""

    safe_write(md_path, content, overwrite=overwrite, dry_run=dry_run)


def create_edited_volume_overview(
    *,
    book_folder: str,
    source_file: Optional[Path],
    citation: str,
    argument: str,
    extracted_to: List[str],
    processed_date: str,
    overwrite: bool,
    dry_run: bool,
    book_title: Optional[str] = None,
    editors: Optional[List[str]] = None,
    publisher: Optional[str] = None,
) -> None:
    book_dir = book_folder_path(book_folder)
    if source_file is not None:
        validate_book_file(source_file, book_dir, {".pdf", ".epub"})

    arg = ensure_wikilink(argument, "--argument")
    all_extracted = [arg] + [x for x in extracted_to if x != arg]
    md_path = book_dir / f"{book_folder}_overview.md"

    fm = source_frontmatter(
        title=book_folder,
        subtype="edited-volume-overview",
        publication_type="book",
        book_title=book_title,
        editors=editors,
        publisher=publisher,
        citation=citation,
        book_file=rel(source_file) if source_file else None,
        extracted_to=all_extracted,
        processed_date=processed_date,
    )

    embed = ""
    if source_file:
        if source_file.suffix.lower() == ".pdf":
            embed = f"\n![[{source_file.name}]]\n"
        elif source_file.suffix.lower() == ".epub":
            embed = f'\n<div id="epub-viewer" style="width:100%;height:560px;border:1px solid rgb(204,204,204);" data-epub="/{rel(source_file)}"></div>\n'

    content = f"""{fm}

# {book_folder}
{embed}
## Citation

{citation}

---

## Extracted to

{extracted_section(all_extracted)}

---

## 已处理章节

"""

    safe_write(md_path, content, overwrite=overwrite, dry_run=dry_run)


def create_book_chapter(
    *,
    book_folder: str,
    source_file: Path,
    citation: str,
    extracted_to: List[str],
    part_of: str,
    processed_date: str,
    overwrite: bool,
    dry_run: bool,
    book_title: Optional[str] = None,
    chapter_title: Optional[str] = None,
    authors: Optional[List[str]] = None,
    editors: Optional[List[str]] = None,
    publisher: Optional[str] = None,
) -> None:
    book_dir = book_folder_path(book_folder)
    validate_book_file(source_file, book_dir, {".pdf"})

    po = ensure_wikilink(part_of, "--part-of")
    title = source_file.stem
    md_path = book_dir / f"{title}.md"

    fm = source_frontmatter(
        title=title,
        subtype="book-chapter",
        publication_type="book",
        book_title=book_title,
        chapter_title=chapter_title,
        authors=authors,
        editors=editors,
        publisher=publisher,
        citation=citation,
        source_file=rel(source_file),
        part_of=po,
        extracted_to=extracted_to,
        processed_date=processed_date,
    )

    content = f"""{fm}

# {title}

![[{source_file.name}]]

## Citation

{citation}

---

## Extracted to

{extracted_section(extracted_to)}
"""

    safe_write(md_path, content, overwrite=overwrite, dry_run=dry_run)


# -----------------------------
# CLI
# -----------------------------

def parse_people(value: Optional[str]) -> Optional[List[str]]:
    if not value:
        return None
    return [x.strip() for x in value.split(",") if x.strip()]


def add_common_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--citation", required=True, help="APA or other citation string.")
    p.add_argument("--extracted-to", default="", help='Comma-separated wikilinks, e.g. "[[A]],[[B]]".')
    p.add_argument("--date", default=today(), help="processed_date, default today.")
    p.add_argument("--overwrite", action="store_true", help="overwrite existing output files.")
    p.add_argument("--dry-run", action="store_true", help="preview without writing files.")


def add_biblio_args(p: argparse.ArgumentParser, *, book: bool = False, chapter: bool = False, periodical: bool = False) -> None:
    if book:
        p.add_argument("--book-title", default=None)
        p.add_argument("--publisher", default=None)
        p.add_argument("--authors", default=None, help="Comma-separated author names.")
        p.add_argument("--editors", default=None, help="Comma-separated editor names.")
    if chapter:
        p.add_argument("--chapter-title", default=None)
    if periodical:
        p.add_argument("--journal", default=None)
        p.add_argument("--issuing-organization", default=None)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create source records for the academic wiki vault.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("article", help="Create ordinary journal article source record under sources/.")
    p.add_argument("--file", required=True, type=Path)
    add_common_args(p)
    add_biblio_args(p, periodical=True)
    p.add_argument("--copy", action="store_true")
    p.add_argument("--no-move", action="store_true")

    p = sub.add_parser("report", help="Create report / policy document source record under sources/.")
    p.add_argument("--file", required=True, type=Path)
    add_common_args(p)
    add_biblio_args(p, periodical=True)
    p.add_argument("--copy", action="store_true")
    p.add_argument("--no-move", action="store_true")

    p = sub.add_parser("monograph-pdf", help="Create monograph PDF source record under books/<book-folder>/.")
    p.add_argument("--book-folder", required=True)
    p.add_argument("--file", required=True, type=Path)
    p.add_argument("--argument", required=True)
    add_common_args(p)
    add_biblio_args(p, book=True)

    p = sub.add_parser("monograph-epub", help="Create monograph EPUB source record under books/<book-folder>/.")
    p.add_argument("--book-folder", required=True)
    p.add_argument("--file", required=True, type=Path)
    p.add_argument("--argument", required=True)
    add_common_args(p)
    add_biblio_args(p, book=True)

    p = sub.add_parser("edited-volume-overview", help="Create edited volume overview source record under books/<book-folder>/.")
    p.add_argument("--book-folder", required=True)
    p.add_argument("--file", required=False, type=Path)
    p.add_argument("--argument", required=True)
    add_common_args(p)
    add_biblio_args(p, book=True)

    p = sub.add_parser("book-chapter", help="Create edited volume chapter source record under books/<book-folder>/.")
    p.add_argument("--book-folder", required=True)
    p.add_argument("--file", required=True, type=Path)
    p.add_argument("--part-of", required=True)
    add_common_args(p)
    add_biblio_args(p, book=True, chapter=True)

    args = parser.parse_args()
    extracted_to = parse_wikilink_list(getattr(args, "extracted_to", ""))
    processed_date = args.date

    if args.cmd == "article":
        create_article_or_report(
            subtype="journal-article",
            publication_type="journal-article",
            source_file=args.file,
            citation=args.citation,
            extracted_to=extracted_to,
            processed_date=processed_date,
            overwrite=args.overwrite,
            copy=args.copy,
            no_move=args.no_move,
            dry_run=args.dry_run,
            journal=args.journal,
            issuing_organization=args.issuing_organization,
        )

    elif args.cmd == "report":
        create_article_or_report(
            subtype="report-policy-document",
            publication_type="report",
            source_file=args.file,
            citation=args.citation,
            extracted_to=extracted_to,
            processed_date=processed_date,
            overwrite=args.overwrite,
            copy=args.copy,
            no_move=args.no_move,
            dry_run=args.dry_run,
            journal=args.journal,
            issuing_organization=args.issuing_organization,
        )

    elif args.cmd == "monograph-pdf":
        create_monograph_pdf(
            book_folder=args.book_folder,
            source_file=args.file,
            citation=args.citation,
            argument=args.argument,
            extracted_to=extracted_to,
            processed_date=processed_date,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
            book_title=args.book_title,
            authors=parse_people(args.authors),
            publisher=args.publisher,
        )

    elif args.cmd == "monograph-epub":
        create_monograph_epub(
            book_folder=args.book_folder,
            source_file=args.file,
            citation=args.citation,
            argument=args.argument,
            extracted_to=extracted_to,
            processed_date=processed_date,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
            book_title=args.book_title,
            authors=parse_people(args.authors),
            publisher=args.publisher,
        )

    elif args.cmd == "edited-volume-overview":
        create_edited_volume_overview(
            book_folder=args.book_folder,
            source_file=args.file,
            citation=args.citation,
            argument=args.argument,
            extracted_to=extracted_to,
            processed_date=processed_date,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
            book_title=args.book_title,
            editors=parse_people(args.editors),
            publisher=args.publisher,
        )

    elif args.cmd == "book-chapter":
        create_book_chapter(
            book_folder=args.book_folder,
            source_file=args.file,
            citation=args.citation,
            extracted_to=extracted_to,
            part_of=args.part_of,
            processed_date=processed_date,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
            book_title=args.book_title,
            chapter_title=args.chapter_title,
            authors=parse_people(args.authors),
            editors=parse_people(args.editors),
            publisher=args.publisher,
        )

    else:
        die(f"Unknown command: {args.cmd}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
