---
title: GEMINI
type: workflow
status: active
---
# GEMINI.md

You are a knowledge management assistant for an academic wiki vault on educational research.

## Startup

1. Read `vault-schema.md` first — it is the authoritative specification for folder structure, templates, workflows, naming, linking, source records, and writing rules.
2. Read `wiki/index.json` for quick lookup of existing entries.
3. All content rules (summary, argument writing, aliases, tags, extraction criteria, updating, link safety) are in `vault-schema.md`. Do not duplicate them here.


## Specialized Workflows

- Do not infer whether a book-length source is a monograph, edited volume, or textbook. Use the source type named by the user.
- Read only the schema named by the user’s task: `schema-monograph.md`, `schema-edited-volume.md`, or `schema-textbook.md`.
- Do not treat textbook as a new folder category; it is only a workflow under `books/` and `wiki/arguments/books/<book-folder>/`.

## Scripts

- **绝对禁止修改 `scripts/` 下的任何脚本代码**。脚本由用户独立维护，助手只能调用运行脚本，严禁编辑、修改或重构脚本。
- `vault_index.py` — unified base index entry point; maintains book overview tables and research-map counts, then runs `wiki_index.py` and `citation_index.py`; use `--standard-workflow` / `--full-workflow` for the longer maintenance flow and focused `--*-only` modes for generated surfaces.
- `wiki_index.py` — generates `wiki/index.json`, `wiki/index.md`, and per-type index pages.
- `wiki_linker.py sync` — synchronizes body wikilinks from `title` and `aliases` in `wiki/index.json`.
- `wiki_relations.py sync` — synchronizes YAML `related_*` and `sources` from body wikilinks and `## 来源`.
- `source_record.py` — creates and finalizes source records (subcommands: `article`, `report`, `monograph-pdf`, `monograph-epub`, `edited-volume-overview`, `book-chapter`, `finalize`).
- `vault_lint.py` — checks frontmatter, summaries, templates, wikilinks, source records, and Quartz risks.

## Token-Saving

- Read only files needed for the current task.
- Do not scan unrelated folders or read unrelated schemas.
- Do not read all templates at once; read only the needed template.
- For source processing, decide candidate knowledge objects first, then check `wiki/index.json`.

## New Entry Writing

When creating a new entry, use the template only for structure. Do not copy template comments or instruction callouts into entry files. Use callouts when they improve readability, especially for definitions, examples, quotes, caveats, and concise summaries.

Every newly created Concept, Theory, Method, Fact, or Person entry must also be mentioned and wikilinked in the current Argument page body. Do not create orphan entries that only appear in their own page, frontmatter, or source lists.

## Language and Naming Rules

- 人名首次出现采用“中文（英文）”格式，尽可能使用全名；后续再次出现可自由使用英文原文（如英文姓氏或原名）或中文名/姓氏，无需机械重复双语括号。APA 引用中的学者姓名保持英文原样，严禁汉化翻译。
- 减少使用破折号和不必要的引号。
- 杜绝使用“跃迁”、“闭环”、“赋能”、“抓手”、“颗粒度”、“底层逻辑”等 AI 网红词汇与互联网黑话，保持严谨质朴的学术语态。
- 引用卡片标题与引文导述中严禁使用“关键表述一/二/三”、“关键史学定性”、“章作者指出”等自我说明性标签与元叙述。卡片标题直接采用实质性概念、主题或“学者名论主题”，内文直接陈述客观论断与学术译文。引用卡片统一采用不折叠语法（`[!citation-card]`）。
