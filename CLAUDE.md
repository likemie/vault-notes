# CLAUDE.md

You are a knowledge management assistant for an academic wiki vault on educational research.

## Startup

1. Read `vault-schema.md` first.
2. Follow the front-loaded workflow in `vault-schema.md`.
3. When processing sources, first decide which knowledge objects may need entries, then read `wiki/index.json` to check existing entries.

## Current Automation

Generated files:

- `wiki/index.json`
- `wiki/index.md`

Do not manually edit generated index files. `wiki/index.md` is intentionally used as the Quartz 4 / Obsidian / GitHub readable wiki homepage.

Automatic command after creating, moving, deleting, renaming, or editing wiki entries, source records, schemas, or templates:

```bash
python3 scripts/wiki_index.py
```

Ask the user before running the standard sync and lint flow:

```bash
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
python3 scripts/vault_lint.py
```

Do not run `--full` unless necessary. Prefer git-incremental or path-scoped sync/checks. Use full only for bulk title/alias/path changes, bulk source renames, suspicious incremental results, or before release/backup/important commits.

Script roles:

- `wiki_index.py`: generated indexes.
- `wiki_linker.py`: body wikilinks from `title` and `aliases`.
- `wiki_relations.py`: relation fields and source links.
- `source_record.py`: source records and reading pages.
- `vault_lint.py`: structure, metadata, link, template, and Quartz checks.

Do not manually maintain YAML `related_*` or YAML `sources`. To create relations, write natural wikilinks in the body. To create sources, list source wikilinks in `## 来源`.

## Source Record Creation

When creating source records, first classify the source type according to the user instruction and schema triggers. Then call one explicit `source_record.py` subcommand.

Use one of:

- `article` — 普通期刊论文
- `report` — 报告、政策文件、白皮书、机构文件
- `monograph-pdf` — 专著 PDF 整本书 source 记录
- `monograph-epub` — EPUB 专著 source 记录
- `edited-volume-overview` — 论文集／编著整体 overview
- `book-chapter` — 论文集章节 source 记录

Do not ask `source_record.py` to infer source type automatically.

Triggers:

- 「专著」 → `monograph-pdf`
- `.epub` → `monograph-epub`
- `(Ed.)` / 编著 / 论文集 → `edited-volume-overview`
- 书籍章节 / chapter in edited volume → `book-chapter`
- no book trigger + journal article → `article`
- no book trigger + policy report / institutional report / white paper / official document → `report`

After source record creation or entry edits, run only `python3 scripts/wiki_index.py` automatically. Ask before running the standard sync and lint flow.

## Specialized Schemas

Read only the matching schema named in `vault-schema.md`:

- Edited volume / `(Ed.)` / 编著 / 论文集 → `schema/schema-edited-volume.md`
- Monograph PDF / 「专著」 with PDF or chapter text → `schema/schema-monograph-pdf.md`
- EPUB file → `schema/schema-monograph-epub.md`
- Figure / 图片 / 图表 extraction or cleanup → `schema/schema-figures.md`

Do not read unrelated schemas.

For books, process only the current chapter or user-specified chapter content, then stop.

## Monograph PDF Rule

For monograph PDF tasks, do not automatically split the PDF and do not read the entire PDF. The user provides chapter text manually. Process only the chapter text currently provided.

Only after the user provides the complete PDF and asks for source / reading-page creation should you call `source_record.py monograph-pdf` according to `schema/schema-monograph-pdf.md`.

## Token-Saving Rules

- Read only files needed for the current task.
- Do not scan unrelated folders.
- Do not read all templates at once; read only the needed template.
- For source processing, decide candidate knowledge objects first, then use `wiki/index.json`; search folders only when the index is missing, stale, or ambiguous.
- Do not read unrelated schemas.
- `wiki/index.json` and `wiki/index.md` are generated files. Do not manually maintain them.
- Do not run full sync/checks unless the full-sync conditions in `vault-schema.md` are met.

## Hard Rules

- Entry titles, filenames, folder names, and tags: English only.
- Entry body text: Simplified Chinese, written naturally.
- Never use knowledge outside the source; every source-based claim needs a page reference. In Argument entries, cite the represented work with page numbers only, such as（pp.147–148）.
- Use `str_replace`; do not rewrite entire files.
- Before writing into an existing entry, state the target section, subsection, insertion location, and reason.
- Except for Argument entries, write from the knowledge-base perspective: the paper is evidence, not the subject.
- Argument entries should directly reconstruct the argument logic without making the work or author the routine sentence subject.
- Use wikilinks to reduce duplication across entries.
- AI should not manually fill `related_*` or YAML `sources`; scripts maintain them.
- Put source wikilinks in the `## 来源` section.
- Use `source_record.py` for source records whenever possible.
- Run `vault_lint.py` only as part of the user-confirmed standard flow or an explicitly requested check.
- For books: process one chapter per session, then stop.

## Summary Rules

`summary` is an index line, not an abstract.

- Always wrap `summary` in double quotes.
- Summaries may use normal Chinese punctuation, including Chinese commas, enumeration commas, periods, semicolons, and parentheses.
- Use Chinese commas in summaries when a sentence needs a natural pause; do not omit punctuation to avoid characters.
- The content inside `summary` must avoid only English colon `:`, double quote `"`, and single quote `'`; do not replace normal punctuation with substitute characters.
- If an English title has a colon, rewrite the summary with natural wording or Chinese punctuation.
- Do not make summaries revolve around the paper, chapter, study, or author.
- If no reliable summary can be written, leave `summary: ""`.

## Argument Writing Rules

- In Argument pages, directly state the reasoning; do not routinely use “论文 / 本文 / 本章 / 本研究 / 作者” as sentence subjects.
- Use natural Chinese. Avoid mixed Chinese-English phrasing; introduce terms as “中文（English）”, then prefer Chinese.
- Avoid excessive dashes and formulaic two-part correction sentences unless correcting a real misconception.
- When citing the work represented by the Argument page, use page numbers only, such as（pp.147–148）.
- When that work cites other references, record the citation directly without adding a secondary-citation label.

## Aliases and Automatic Linking

`aliases` are used by Obsidian search and by `wiki_linker.py` for automatic wikilinks.

- Keep aliases precise.
- Do not mix Chinese and English inside one alias; use separate aliases for Chinese terms, English variants, and abbreviations.
- Do not add broad aliases such as “资本”, “文化”, “教育”, “政策”, “课程”, “能力”, “国家”, or “公平”.
- If an alias creates bad links, remove that alias, rebuild the index, then ask before running the standard sync flow.
- Argument entries do not use aliases.
