# Vault Schema

本文件只保留 AI / Claude Code 处理 Obsidian vault 时必须遵守的规则。具体页面结构以 `wiki/templates/` 中对应模板为准；脚本实现细节以 `scripts/` 为准。

---

## 1. Core Principles

- 只读取当前任务需要的文件，避免扫描无关文件夹。
- 先读 `wiki/index.json` 判断条目是否可能已存在；若缺失、过期或有歧义，再按类型搜索对应二级文件夹。
- `wiki/index.json`、`wiki/index.md` 和各类型索引页由 `scripts/wiki_index.py` 自动生成，不手动维护。
- 修改已有条目必须使用 `str_replace` 精确替换相关段落，不重写整个文件。
- 所有来源性陈述都必须标注页码。非 Argument 条目使用来源与页码；Argument 条目引用当前对应文献时只写页码，如（pp.147–148）。
- 不使用来源以外的知识；不确定时宁可不写。
- AI 不手动维护生成字段：`related_*`、YAML `sources`、source record 的 `extracted_to`。
- Source 记录与阅读页面优先由 `scripts/source_record.py` 生成，不手写固定结构。
- 普通论文 / 报告 source record 初始阶段只负责固定 PDF 与来源入口；完整 citation 与最终命名在 Argument 页完成后由 `source_record.py finalize` 回填。
- 新建、移动、删除、重命名条目后，自动运行 `python3 scripts/wiki_index.py` 重建索引；是否继续运行补链、关系同步与 lint，由用户确认。

---

## 2. Folder Structure and Entry Types

```text
raw/                         待处理原始文献，不编辑
sources/                     已处理论文／报告 source 记录、PDF 与可选配套文件夹
books/                       书籍工作区
schema/                      专项工作流 schema，按任务触发读取
  schema-edited-volume.md
  schema-figures.md
  schema-monograph-pdf.md
  schema-monograph-epub.md
templater/                   Obsidian Templater 插件模板，不供 AI 工作流读取
scripts/
  wiki_index.py               自动生成 wiki/index.json 与 wiki/index.md
  wiki_linker.py              根据 index.json 自动同步正文 wikilink
  wiki_relations.py           同步 related_*、sources 与 source record extracted_to
  vault_lint.py               检查 vault 结构、frontmatter、链接、模板与 Quartz 风险
  source_record.py            创建、固定、finalize source 记录与 PDF / EPUB 阅读页面
wiki/
  index.json                  AI / Claude Code 检索用极简机器索引
  index.md                    Quartz 4 / Obsidian / GitHub 可读静态索引
  templates/                  AI / Claude Code 条目模板
  concepts/<field>/
  theories/<field>/
  methods/qualitative/
  methods/quantitative/
  methods/mixed/
  persons/<nationality-or-region>/
  facts/<region>/
  arguments/journal-articles/<journal-name>/
  arguments/books/<book-folder>/
  arguments/reports-policy-documents/
```

| 条目类型 | 路径 | 归类规则 |
|---|---|---|
| Concept | `wiki/concepts/<field>/` | 按领域，如 `comparative-education`、`curriculum`、`educational-philosophy`、`educational-leadership-administration` |
| Theory | `wiki/theories/<field>/` | 只放可作为理论框架、解释机制或分析视角的理论／框架／模型 |
| Method | `wiki/methods/qualitative/`、`quantitative/`、`mixed/` | 只放研究方法、研究设计、资料收集／分析方法、项目评价方法；课堂教学法放 Concept |
| Person | `wiki/persons/<nationality-or-region>/` | 按国籍／地区；不明或跨国身份放 `global` |
| Fact | `wiki/facts/<region>/` | 按地区；全球性放 `global`；多国比较放 `multi` |
| Argument | `wiki/arguments/journal-articles/<journal-name>/`、`wiki/arguments/books/<book-folder>/`、`wiki/arguments/reports-policy-documents/` | 按文献类型；期刊论文 Argument 按 `journal` 字段对应的期刊名称分组；书籍 Argument 再按具体书籍文件夹分组 |

文件名、文件夹名、`title`、`tags` 使用英文；正文使用简体中文。

期刊论文 Argument 的二级归档规则：

- 目标路径为 `wiki/arguments/journal-articles/<journal-name>/Argument_<Author>_<Year>_<JournalAbbrev>.md`。
- `<journal-name>` 使用条目 frontmatter 的 `journal` 全称；若期刊名称含 `/` 或 `:` 等不适合作为路径的字符，用空格替换并压缩连续空格。
- 文件名保留 `Argument_<Author>_<Year>_<JournalAbbrev>.md` 格式，不因移动到期刊目录而改名。
- 对应 source record 的最终文件名为 `<Author>_<Year>_<JournalAbbrev>.md`，即去掉 Argument 文件名前缀 `Argument_`。

---

## 3. Naming, Aliases and Tags

### File Names and Titles

`wiki/` 条目的文件名应尽量与 frontmatter `title` 一致，使用可读英文标题，不使用全小写 slug 作为条目文件名。

- 正确：`Piaget's Theory of Cognitive Development.md`
- 避免：`piagets-theory-of-cognitive-development.md`

命名规则：

- `title` 是知识对象的正式名称；文件名通常等于 `title`。
- 文件名和 `title` 不使用 tag 风格 slug。
- 标题表达归属关系时，优先使用自然英文结构，如 `Van Leeuwen's Legitimation Theory`、`Teaching Theory of Gruschka`。
- 不用括号给标题补充来源、人名、年份、地区或缩写，除非括号本身是固定名称的一部分，如 `SF (Haraway)`。
- 缩写、中文译名、常见变体放入 `aliases`，不要为了缩写改变标题。
- 如果正式英文标题含冒号，frontmatter `title` 可保留；文件名需要规避 `:` 时用空格或短横，不用 `_`。

### Source Record Names

普通论文 / 报告 source record 的最终命名规则：

```text
<Author>_<Year>_<JournalOrPublisherAbbrev>
```

例如：

```text
Simpson_2019_ERE
Marginson_2024_CE
Zhu_2023_BJSE
OECD_2018_GlobalCompetence
```

规则：

- 期刊论文优先使用 `Author_Year_JournalAbbrev`。
- 报告、政策文件、白皮书可使用 `Organization_Year_ShortTitle` 或 `Organization_Year_PublisherAbbrev`。
- source record 文件名和 PDF 文件名保持一致。
- 初始处理阶段可使用临时 `record-name`；最终命名由 `source_record.py finalize --rename` 根据 Argument 页文件名确定。
- AI 不从 PDF 文件名或 DOI 直接猜最终命名；最终命名以 Argument 页路径和文件名为准。

### aliases

`aliases` 同时用于 Obsidian 检索和 `wiki_linker.py` 自动补链，因此必须精确。若 alias 产生错误链接，直接从对应条目删除后重新同步。

- Argument 不使用 `aliases`。
- Concept / Theory / Method / Fact 的 `aliases` 写中文译名、常见英文变体和缩写。
- Person 的 `aliases` 主要写中文全称；只有非常著名或中文文献中常用简称的人物才写简称，如 `杜威`、`皮亚杰`、`布迪厄`、`阿普尔`、`哈蒂`。
- 英文 alias 默认不区分大小写；不要同时写只差大小写的重复 alias。
- 若 title 与缩写已经分别覆盖，不再写 `Full Name (ABBR)` 形式的 alias。
- 不要写过短、过宽或 tag 风格 slug alias，如“资本”“文化”“教育”“政策”“课程”“能力”“国家”“公平”。
- 不要轻易写单个汉字 alias；只有该字作为独立术语有强识别度时才保留。

### tags

- tags 全部英文、小写连字符。
- 常用前缀：`region/`、`level/`、`subject/`、`paradigm/`、`theme/`、`method/`、`theory/`、`policy/`、`source/`。

---

## 4. Script Rules and Sync Commands

脚本用于维护索引、补链、关系字段和 source 记录。`wiki_linker.py sync`、`wiki_relations.py sync` 与 `vault_lint.py` 默认使用 git 增量模式，只处理当前变动文件；日常不需要显式添加 `--git`。

### Automatic Step

每次处理完条目、书籍章节、source 记录、模板或 schema 后，AI 只自动运行索引重建：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/wiki_index.py
```

不要自动运行 `wiki_linker.py`、`wiki_relations.py` 或 `vault_lint.py`。完成索引重建后，询问用户是否运行标准脚本流程。

### Standard Script Flow

用户确认后，再运行：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
python3 scripts/vault_lint.py
```

按路径缩小同步或检查范围：

```bash
python3 scripts/wiki_linker.py sync wiki/concepts
python3 scripts/wiki_relations.py sync wiki/concepts
python3 scripts/wiki_relations.py sync sources
python3 scripts/vault_lint.py --path wiki/concepts
python3 scripts/vault_lint.py --path "wiki/concepts/comparative-education/World Culture Theory.md"
```

### Full Sync

只有在以下情况才全量同步与检查：

- 批量修改 `title` 或 `aliases`。
- 批量移动、删除、重命名 wiki 条目。
- 使用 `source_record.py finalize --rename` 批量重命名 source record 和 PDF 后。
- 怀疑 wikilink、`related_*`、YAML `sources` 或 source record 的 `extracted_to` 状态不同步。
- 增量同步或增量检查结果异常。
- 发布、备份或重要提交前。

全量流程：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync --full
python3 scripts/wiki_relations.py sync --full
python3 scripts/wiki_index.py
python3 scripts/vault_lint.py --full
```

严格检查只在发布、备份或重要提交前运行：

```bash
python3 scripts/vault_lint.py --full --strict
```

移动 wiki 条目时：

- 只移动文件本身，不手动编辑 `wiki/index.json`、`wiki/index.md`、各类型索引页或 generated fields。
- 批量移动 journal article Argument 时，按 `journal` 字段创建或复用 `wiki/arguments/journal-articles/<journal-name>/`，移动后立即运行 `python3 scripts/wiki_index.py`。
- 若移动涉及正文中的 vault-root 图片路径、source record 的反向关系，或移动后索引 / 链接检查异常，再运行 `wiki_linker.py sync --full`、`wiki_relations.py sync --full` 与 `vault_lint.py --full`。

### Generated Fields

不要手动编辑或维护：

- `wiki/index.json`
- `wiki/index.md`
- 各类型索引页，如 `wiki/concepts/index.md`
- frontmatter 中的 `related_*`
- wiki 条目 frontmatter 中的 YAML `sources`
- source record frontmatter 中的 `extracted_to`

### Wikilink and Relation Rules

- wikilink 由 `wiki_linker.py` 自动维护，依据是 `title` 和 `aliases`。
- `## 来源` / `## Sources` 章节只放 source wikilink。
- wiki 条目的 YAML `sources` 由 `wiki_relations.py` 从 `## 来源` 章节同步。
- source record 的 YAML `extracted_to` 由 `wiki_relations.py` 从所有 wiki 条目的 `## 来源` 章节反向同步。
- `sources/` 与 `books/` 下的 source record 不是普通 wiki 条目，不进入 `related_*` 自动维护逻辑。

---

## 5. Source Records and Source Files

### Source Record Principle

Source record 不是完整文献数据库条目，而是来源入口页。普通论文 / 报告 source record 采用极简结构：

```markdown
---
citation: ""
extracted_to: []
processed_date: 2026-05-25
---

# Simpson_2019_ERE

![[Simpson_2019_ERE.pdf]]
```

最终完成后应为：

```markdown
---
citation: "Simpson, A. (2019). Separating arguments from conclusions: The mistaken role of effect size in educational policy research. Educational Research and Evaluation, 25(1-2), 99-109."
extracted_to: []
processed_date: 2026-05-25
---

# Simpson_2019_ERE

![[Simpson_2019_ERE.pdf]]
```

规则：

- source record frontmatter 只保留 `citation`、`extracted_to`、`processed_date`；书籍任务可按专项 schema 额外保留必要的 `part_of`。
- source record 正文只保留一级标题和 PDF / EPUB 嵌入；不要写摘要、关键词、研究问题、作者信息、期刊信息等。
- `citation` 初始可为空；完整 citation 应在 Argument 页完成后由 `source_record.py finalize` 从 Argument frontmatter 回填。
- `extracted_to` 始终由 `wiki_relations.py` 反向同步，AI 和 `source_record.py finalize` 不手动维护。
- source record 文件名、一级标题、PDF 文件名应保持一致。
- source record 不是普通 wiki 条目，不写 `type`、`subtype`、`tags`、`status`、`related_*`。

### Source Record Commands

Source 记录与阅读页面优先由 `scripts/source_record.py` 生成。AI 先判断来源类型，再调用对应子命令；脚本不负责自动猜类型。

| 来源类型 | 子命令 | 输出位置 |
|---|---|---|
| 期刊论文 | `article` | `sources/` |
| 报告／政策文件／白皮书 | `report` | `sources/` |
| 专著 PDF 整本书 source | `monograph-pdf` | `books/<book-folder>/` |
| EPUB 专著 source | `monograph-epub` | `books/<book-folder>/` |
| 论文集／编著整体 overview | `edited-volume-overview` | `books/<book-folder>/` |
| 论文集章节 source | `book-chapter` | `books/<book-folder>/` |
| 从 Argument 页回填 source record | `finalize` | `sources/` 或 `books/<book-folder>/` |

普通论文初始入口：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/source_record.py article \
  --file raw/FILENAME.pdf \
  --record-name temp_or_known_name
```

报告初始入口：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/source_record.py report \
  --file raw/FILENAME.pdf \
  --record-name temp_or_known_name
```

Argument 页完成后的 finalize：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/source_record.py finalize \
  --argument "wiki/arguments/journal-articles/<journal-name>/Argument_<Author>_<Year>_<JournalAbbrev>.md" \
  --rename
```

`finalize` 的职责：

- 读取 Argument 页 frontmatter 的 `citation`。
- 从 Argument 页 frontmatter `sources` 或正文 `## 来源` 找到对应 source record。
- 将 source record 改写为极简结构。
- 使用 `--rename` 时，把 source record 和 PDF 重命名为 Argument 文件名去掉 `Argument_` 后的名称。
- 如发生重命名，同步替换 Argument 页中的 source wikilink。
- 不维护 `extracted_to`，不运行 `wiki_relations.py`。

### Source Files

- `raw/` 只放原始 PDF，不加 frontmatter，不编辑。
- 普通论文或报告处理开始时，先用 `source_record.py article` 或 `source_record.py report` 固定 source record 和 PDF。
- 普通论文或报告处理完成并写好 Argument 页后，再用 `source_record.py finalize --rename` 回填 citation 与最终命名。
- 若 source 有配套 figure，按 `schema/schema-figures.md` 整理。
- 书籍来源记录按对应专项 schema 执行。
- `sources/` 与 `books/` 下的 source record 不进入 `related_*` 自动维护逻辑，但 `extracted_to` 由 `wiki_relations.py` 反向同步。

---

## 6. Source Processing Workflow

### 普通论文／报告

1. 读取 `vault-schema.md`。
2. 若触发书籍任务，转入对应 book schema，不继续普通论文流程。
3. 判断来源类型：期刊论文用 `article`，报告／政策文件／白皮书用 `report`。
4. 使用 `source_record.py article` 或 `source_record.py report` 创建初始 source record，并将 PDF 固定到 `sources/`。
5. 提取 `sources/<record-name>.pdf` 文本。
6. 扫描文献，列出可提取条目：Concept / Theory / Fact / Person / Method / Argument；同时判断文献是否属于实证研究。若属于实证研究，必须识别至少一种核心研究方法，并准备写入对应 Method 条目的 `## 使用此方法的研究`。
7. 读取 `wiki/index.json` 判断候选条目是否已存在；必要时搜索对应二级文件夹确认。
8. 将候选分为待更新条目与待新建条目，并标注类型与目标二级文件夹。
9. 更新已有条目：读取文件 → 判断插入位置 → 用 `str_replace` 精确整合。
10. 新建条目：只读取对应模板 → 按模板写入对应二级文件夹。
11. 对实证研究，更新或新建至少一个 Method 条目，在 `## 使用此方法的研究` 中加入一条方法案例，并链接到当前 Argument 页。
12. 创建或更新 Argument 页。Argument 页必须在 frontmatter 写入 `citation`，并在 `## 来源` 章节列出 source wikilink。
13. 运行 `source_record.py finalize --argument <Argument路径> --rename`，根据 Argument 页回填 source record 的 citation，并在需要时重命名 source record 与 PDF。
14. 自动运行 `python3 scripts/wiki_index.py` 重建索引。
15. 询问用户是否继续运行标准脚本流程。

### Argument 页与 Source Record 的分工

Argument 页负责保存文献的结构化知识信息：

- `title`
- `summary`
- `type`
- `subtype`
- `publication_type`
- `journal` 或 `publisher`
- `citation`
- `tags`
- `related_*`
- `sources`
- `status`
- `created`
- `updated`
- 研究问题、理论框架、研究方法、核心论证、主要发现、关键引用、自述局限

Source record 只负责保存来源入口：

- `citation`
- `extracted_to`
- `processed_date`
- PDF / EPUB 嵌入

因此，不要把 Argument 页的结构化字段复制到 source record。

### 书籍任务

只读取匹配的一种专项 schema：

| 触发条件 | 读取文件 |
|---|---|
| `(Ed.)` / 编著 / 论文集 | `schema/schema-edited-volume.md` |
| 专著 PDF / 用户标注「专著」 | `schema/schema-monograph-pdf.md` |
| `.epub` | `schema/schema-monograph-epub.md` |

书籍任务每次只处理一章或用户当前指定的章节内容。处理完当前章节后停止。

若书籍任务同时涉及 figure / 图片 / 图表，再额外读取 `schema/schema-figures.md`。

---

## 7. Specialized Schemas

专项 schema 只在触发对应任务时读取；不要为普通条目更新读取无关 schema。

| 触发条件 | 读取文件 |
|---|---|
| `(Ed.)` / 编著 / 论文集 | `schema/schema-edited-volume.md` |
| 专著 PDF / 用户标注「专著」 | `schema/schema-monograph-pdf.md` |
| `.epub` | `schema/schema-monograph-epub.md` |
| 提取、整理、移动、删除、重画或引用文献 figure / 图片 / 图表 | `schema/schema-figures.md` |

---

## 8. Entry Perspective and Writing Style

### Knowledge-base perspective

除 Argument 外，所有条目都以知识对象本身为中心，论文只是证据来源。

- Concept：写概念本身。
- Theory：写理论本身。
- Method：写方法本身。
- Person：写人物本身。
- Fact：写现实中的政策、事件、制度或历史节点。
- Argument：写某篇论文、章节、报告或专著的论证结构。

非 Argument 条目不得以文献、文章、章节或作者作为常规主语，应改为知识库陈述：

> 通识教育科于 2009 年在香港正式推行……  
> 该政策的主要影响包括……  
> 学界对此存在争议……

### Argument style

Argument 可以围绕文献本身，但正文应直接陈述论证思路，不以“论文 / 本文 / 本章 / 文章 / 研究 / 作者”等作为常规句子主语。

Argument 必须详细拆解论证链：问题来源、概念或理论、前提、证据如何支持前提、中间推论如何连接到结论，以及可能存在的跳跃、弱证据或过度推论。

语言要易懂。抽象理论必须配例子；例子优先来自原文，原文没有时可用简短教育情境说明。

Argument 引用规则：

- 引用当前 Argument 对应文献时，只写页码，如（p.147）或（pp.147–148），不写作者与年份。
- 当前文献引用其他文献时，按原引用内容直接记录，不额外添加二手引文标记。
- 只有引用当前 Argument 对应文献之外的独立来源时，才写作者、年份与页码。

### Writing and Template Rules

- 新建条目必须读取对应 `wiki/templates/template-*.md`。
- 模板提供结构和样式；有内容才写，没有内容可省略空章节。
- `summary` 只用于索引说明，不是摘要；必须围绕条目本身写，不围绕某篇论文或章节写。
- `summary` 外层必须使用双引号包裹；内容内部禁止出现英文冒号 `:`、双引号 `"`、单引号 `'`；不要用 `_` 代替标点。
- 重要定义、关键数据、关键引用、争议、例子等，按模板使用 callout。
- 常用 callout：`[!info]` 定义、背景、方法说明；`[!abstract]` 理论框架、结构、政策摘要；`[!success]` 主要发现、影响、效果；`[!warning]` 争议、局限、批评；`[!quote]` 原文引用；`[!example]` 案例、教育情境例子；`[!note]-` 可折叠补充说明。
- 不要过度使用 callout；只在能增强可读性或区分信息类型时使用。
- 理论或哲学内容要避免纯定义堆砌；抽象主张后应有例子或说明。
- 写作必须自然中文，不直译英文，不写欧化长句。
- 避免中英混杂表达；术语首次出现时使用“中文（English）”格式，后文优先使用中文。
- 避免过度使用破折号；能用逗号、句号、冒号或拆句表达时，优先使用更平实的中文句式。
- 避免套用先否定再转折的二元对立句式；只有真正需要纠正常见误解时才使用。
- 避免 Markdown 加粗语法 `**...**`，用标题、列表或 callout 表达重点。

---

## 9. Extraction Criteria

### Fact

有明确时间 + 地点 + 主体的政策、事件、制度安排，应建 Fact 条目。包括政策、法案、课程纲要、白皮书、历史事件、课程改革节点、教育制度、考试制度、督学制度、分流制度。不要把具体政策或事件只当作概念例子一笔带过。

### Theory

论文提供以下任一信息时，可建 Theory 条目：明确作为理论框架；用于解释现象或论证立场；有专门章节介绍核心主张、起源、代表人物或应用方式。只被点名但无介绍时，不单独建条目，只在相关条目中链接。

### Method

论文提供以下任一信息时，可建 Method 条目：研究设计、数据收集或分析方式、方法选择的理由、认识论立场、操作步骤、适用场景或局限。方法只被命名但无介绍时，不因其定义新建或扩写 Method 条目，但实证研究仍需按下面规则记录方法案例。

除思辨类、评论类、理论建构类和概念辨析类文献外，所有实证研究都必须至少记录一条方法案例。量化、质性和混合方法研究都适用。

处理实证研究时，AI 必须识别至少一种核心研究方法，并更新对应 Method 条目的 `## 使用此方法的研究` 章节。若对应 Method 条目不存在，则新建 Method 条目。方法案例只写一句话，并链接到当前 Argument 页。

方法案例只说明该研究如何使用方法，不展开文献摘要。若文献只命名方法但没有提供方法论说明，仍可作为案例记录；但不据此扩展方法定义、研究程序或局限性。

### Person

不是每个作者都建 Person。只有符合以下之一才建：有独立理论、概念或框架贡献；在领域内有持续影响力；文献专门讨论其思想。只是论文作者、顺带引用一次、受访者，不建 Person 条目。

---

## 10. Updating Existing Entries

整合新内容时：

- 保留原有内容。
- 新信息补充到最相关章节。
- 相似内容要融合，不堆砌重复条目。
- 有分歧时放入“争议与批评”，不要覆盖原观点。
- 新旧内容之间加过渡句，保持段落自然。
- 每条新增信息附来源页码。
- 更新 frontmatter 的 `updated`，需要时更新 `confidence`。
- 不手动更新 `related_*`、`sources`、`extracted_to`，交由脚本同步。
- 在正文中自然使用 wikilink，脚本会自动维护 frontmatter 关系。

章节组织：分点少于 8 条时按时间或逻辑顺序排列；分点达到 8 条或以上时按 `###` 子主题分组，组内按时间排列；争议章节按立场分组；发展脉络按时间顺序；来源列表只按时间排序，不分主题。

---

## 11. Link, Duplication and Markdown Safety

### Link and Duplication Rules

核心原则：用链接减少重复，具体补链交给脚本。

- 详细内容只写在最相关的主条目中。
- 其他条目只写一句关系说明。
- 泛指某类事物时不需要强行链接。
- 条目尚未建立时先写纯文字。
- AI 不手动维护 frontmatter 关系字段。

### Quartz / Markdown Safety

写入 Markdown 时注意：

- HTML 颜色不要写 `#ccc`，改用 `rgb(204,204,204)`。
- DOI / URL 若含特殊字符，优先放 frontmatter，或用反引号包裹。
- 不在正文写内联 JS；脚本逻辑放外部文件。
- 数学公式：行内公式写 `$d = 0.40$`；独立公式写：

```markdown
$$d = ...$$
```
