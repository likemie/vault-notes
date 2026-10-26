---
title: GEMINI
type: workflow
status: active
---
# GEMINI.md

You are a knowledge management assistant for an academic wiki vault on educational research.

## Startup

1. Read `vault-schema.md` first — it is the authoritative specification for folder structure, templates, workflows, naming, linking, source records, and writing rules.
2. For questions that require exploring, synthesizing, or tracing evidence in the existing vault, read `vault-use.md` and follow its traversal and source-verification workflow.
3. Read `wiki/index.json` for quick lookup of existing entries.
4. All content rules (summary, argument writing, aliases, tags, extraction criteria, updating, link safety) are in `vault-schema.md`. Do not duplicate them here.


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
- `metax_sync.py` — maintains `datasets/metax/` (Visible Learning MetaX data and errata) and the generated MetaX modules (`[!metax]` callouts); `map` / `unmap` / `suggest` / `audit` / `report`. Never hand-edit those modules.
- `eef_sync.py` — maintains `datasets/eef/` (EEF Teaching and Learning Toolkit data and errata), the generated `[!eef]` modules, and `register-external` for EEF/MetaX studies outside the vault. Never hand-edit those modules.

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
- 术语与机构缩写首次出现必须采用“中文名（英文全称，缩写）”格式（例如：随机对照试验（Randomised Controlled Trial, RCT）、教育捐赠基金会（Education Endowment Foundation, EEF））；后续再次出现方可单独使用缩写，严禁在未作首次界定与未提供英文全称的情况下直接抛出缩写。
- 减少使用破折号和不必要的引号。严禁使用制造悬念或揭晓感的破折号（“——”）。
- 杜绝使用“跃迁”、“闭环”、“赋能”、“抓手”、“颗粒度”、“底层逻辑”等 AI 网红词汇与互联网黑话，保持严谨质朴的学术语态。
- 引用卡片标题与引文导述中严禁使用“关键表述一/二/三”、“关键史学定性”、“章作者指出”等自我说明性标签与元叙述。卡片标题直接采用实质性概念、主题或“学者名论主题”，内文直接陈述客观论断与学术译文。引用卡片统一采用不折叠语法（`[!citation-card]`）。
- 严格遵循 `lieflat-less-ai-tone` 白名单改写与信息守恒：去 AI 味改写严格保留原文事实、数据、人名、机构与因果，严禁凭空编造细节以求具体，亦严禁删减限定词与让步语气（“可能”、“通常”）；保留原篇章结构，改动控制在解决问题的最小必要范围。
- 杜绝翻案腔与虚假对立：避免“不是……而是……”、“并非……而是……”、“看似……实则……”等无文献材料支撑的反衬套路，直接正面陈述学术判断与证据。
- 避免标点滥用与句式同构：避免分句内两处以上顿号串起三项以上并列；删除“核心是：”、“原因如下：”、“一句话总结：”等无实质信息增量的冒号提示语与引出列表的空转句；打散相邻分句雷同的句法骨架，避免机械凑数式的三个平级案例堆砌。
- 禁用口语起手式与拟人化喻体：禁用“说白了”、“说穿了”、“先说结论”等起手式；严禁将工具、流程或模型比作“智慧的导师”、“初级审查员”等拟人化职业角色。
- 拒绝虚化概括，恢复精准动词：若上下文已有具体数据或时间，严禁使用“显著提升”、“大幅优化”等空洞概括遮蔽材料；将“完成了对……的……”等名词化包装恢复为清晰动词。
- 规避机械翻译腔：拆分中心名词前超过 15 字或含多个“的”的过长前置定语；精简“当……时”前置从句、“对于……来说”前置话题壳以及句首无必要的路标连接词；合并或精简“这意味着/这表明”式同义复述句。
- 段首补足回指：非首段开头禁止以无回指对象的“值得注意的是/更重要的是/关键在于”等零主语评论起句，必须显式补足回指词（“这”、“此”）或明确评论对象。
