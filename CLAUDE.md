# CLAUDE.md

You are a knowledge management assistant for an academic wiki vault on educational research.

## Startup

1. Read `vault-schema.md` first.
2. Read `wiki/index.json` for quick lookup of existing entries.
3. Follow `vault-schema.md` for folder structure, templates, workflows, writing rules, linking rules, automation rules, and book-processing rules.

## Current Automation

Generated files:

- `wiki/index.json`
- `wiki/index.md`

Do not manually edit generated index files. `wiki/index.md` is intentionally used as the Quartz 4 / Obsidian / GitHub readable wiki homepage.

Standard sync command after creating, moving, deleting, renaming, or editing wiki entries:

```bash
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

Automation responsibilities:

- `wiki_index.py` generates `wiki/index.json` and `wiki/index.md`.
- `wiki_linker.py` synchronizes body wikilinks from `title` and `aliases` in `wiki/index.json`.
- `wiki_relations.py` synchronizes YAML `related_*` from body wikilinks, and YAML `sources` from the `## 来源` / `## Sources` section.

Do not manually maintain YAML `related_*` or YAML `sources`. To create relations, write natural wikilinks in the body. To create sources, list source wikilinks in `## 来源`.

## Book Routing

If the task involves a book, read only the matching schema named in `vault-schema.md`:

- Edited volume / `(Ed.)` / 编著 / 论文集 → `books/schema-edited-volume.md`
- Monograph PDF / 「专著」 with PDF or chapter text → `books/schema-monograph-pdf.md`
- EPUB file → `books/schema-monograph-epub.md`

Do not read unrelated book schemas.

For books, process only the current chapter or user-specified chapter content, then stop.

## Monograph PDF Rule

For monograph PDF tasks, do not automatically split the PDF and do not read the entire PDF. The user provides chapter text manually. Process only the chapter text currently provided.

Only after the user provides the complete PDF and asks for source / reading-page creation should you create the book source record and PDF reading page according to `books/schema-monograph-pdf.md`.

## Token-Saving Rules

- Read only files needed for the current task.
- Do not scan unrelated folders.
- Do not read all templates at once; read only the needed template.
- Use `wiki/index.json` first; search folders only when the index is missing, stale, or ambiguous.
- Do not read unrelated book schemas.
- `wiki/index.json` and `wiki/index.md` are generated files. Do not manually maintain them.

## Hard Rules

- Entry titles, filenames, folder names, and tags: English only.
- Entry body text: Simplified Chinese, written naturally.
- Never use knowledge outside the source; every source-based claim needs `(Author, year, p.X)`.
- Use `str_replace`; do not rewrite entire files.
- Before writing into an existing entry, state the target section, subsection, insertion location, and reason.
- Except for Argument entries, write from the knowledge-base perspective: the paper is evidence, not the subject.
- Argument entries should directly reconstruct the argument logic, not repeatedly say “this paper / this chapter / the author argues.”
- Use wikilinks to reduce duplication across entries.
- AI should not manually fill `related_*` or YAML `sources`; scripts maintain them.
- Put source wikilinks in the `## 来源` section.
- For books: process one chapter per session, then stop.

## Summary Rules

`summary` is an index line, not an abstract.

- Always wrap `summary` in double quotes.
- The content inside `summary` must not contain English colon `:`, double quote `"`, or single quote `'`.
- If an English title has a colon, replace the colon with `_`.
- Do not write “本文研究……”, “作者认为……”, or “本研究发现……” in summaries.
- If no reliable summary can be written, leave `summary: ""`.

## Aliases and Automatic Linking

`aliases` are used by Obsidian search and by `wiki_linker.py` for automatic wikilinks.

- Keep aliases precise.
- Do not add broad aliases such as “资本”, “文化”, “教育”, “政策”, “课程”, “能力”, “国家”, or “公平”.
- If an alias creates bad links, remove that alias and rerun the standard sync command.
- Argument entries do not use aliases.
