# Vault Schema

本文件只保留 AI / Claude Code 处理文献时必须遵守的规则。具体页面结构以 `wiki/templates/` 中对应模板为准。

---

## 1. Core Principles

- 只读取当前任务需要的文件，避免扫描无关文件夹。
- 先读 `wiki/index.json` 判断条目是否可能已存在；若缺失、过期或有歧义，再按类型搜索对应二级文件夹。
- `wiki/index.json` 和 `wiki/index.md` 由 `scripts/wiki_index.py` 自动生成，不手动维护。
- `wiki/index.md` 是 Quartz 4 / Obsidian / GitHub 可读索引页面，可作为 `wiki/` 首页。
- 新建、移动、删除、重命名条目后，运行标准同步与检查流程。
- 修改已有条目必须使用 `str_replace`，只替换需要修改的段落，不重写整个文件。
- 写入前必须声明插入位置：
  > 本条内容属于 `## 章节名 > ### 子主题名`，插入位置在……之后／之前，理由是……
- 所有来源性陈述都必须标注页码：`（Author, year, p.X）`。
- 不使用来源以外的知识；不确定时宁可不写。
- AI 不手动维护 `related_*` 和 YAML `sources`；这些字段由 `scripts/wiki_relations.py` 根据正文 wikilink 与 `## 来源` 章节自动同步。
- Source 记录与阅读页面优先由 `scripts/source_record.py` 生成，不手写固定结构。
- 发布或提交前运行 `scripts/vault_lint.py` 检查格式、链接、模板、Quartz 风险和旧命令残留。

---

## 2. Folder Structure

```text
raw/                         待处理原始文献，不编辑
sources/                     已处理论文／报告 source 记录与 PDF
books/                       书籍工作区与书籍 schema
  schema-edited-volume.md
  schema-monograph-pdf.md
  schema-monograph-epub.md
templater/                   Obsidian Templater 插件模板，不供 AI 工作流读取
scripts/
  wiki_index.py               自动生成 wiki/index.json 与 wiki/index.md
  wiki_linker.py              根据 index.json 自动同步正文 wikilink
  wiki_relations.py           根据正文 wikilink 自动同步 YAML related_* 与 sources
  vault_lint.py               检查 vault 结构、frontmatter、链接、模板与 Quartz 风险
  source_record.py            创建 source 记录与 PDF / EPUB 阅读页面
wiki/
  index.json                 AI / Claude Code 检索用极简机器索引
  index.md                   Quartz 4 / Obsidian / GitHub 可读静态索引
  templates/                 AI / Claude Code 条目模板
  concepts/<field>/
  theories/<field>/
  methods/qualitative/
  methods/quantitative/
  methods/mixed/
  persons/<nationality-or-region>/
  facts/<region>/
  arguments/journal-articles/
  arguments/books/<book-folder>/
  arguments/reports-policy-documents/
```

### 二级／三级文件夹规则

| 条目类型 | 路径 | 归类规则 |
|---|---|---|
| Concept | `wiki/concepts/<field>/` | 按领域，如 `comparative-education`、`curriculum`、`educational-philosophy` |
| Theory | `wiki/theories/<field>/` | 按领域 |
| Method | `wiki/methods/qualitative/`、`quantitative/`、`mixed/` | 按方法类型 |
| Person | `wiki/persons/<nationality-or-region>/` | 按国籍／地区；不明或跨国身份放 `global` |
| Fact | `wiki/facts/<region>/` | 按地区；全球性放 `global`；多国比较放 `multi` |
| Argument | `wiki/arguments/journal-articles/`、`wiki/arguments/books/<book-folder>/`、`wiki/arguments/reports-policy-documents/` | 按文献类型；书籍 Argument 再按具体书籍文件夹分组 |

文件名、文件夹名、`title`、`tags` 使用英文；正文使用简体中文。

### File Names and Titles

`wiki/` 条目的文件名应尽量与 frontmatter `title` 一致，使用可读英文标题，不使用全小写 slug 作为条目文件名。

- 正确：`Piaget's Theory of Cognitive Development.md`
- 避免：`piagets-theory-of-cognitive-development.md`

命名规则：

- `title` 是知识对象的正式名称；文件名通常等于 `title`。
- `tags` 使用英文小写连字符；文件名和 `title` 不使用 tag 风格的 slug。
- 标题中需要表达归属关系时，优先使用自然英文结构：
  - `Van Leeuwen's Legitimation Theory`
  - `Teaching Theory of Gruschka`
  - `Piaget's Theory of Cognitive Development`
- 不用括号给标题补充来源、人名、年份、地区或缩写，除非该括号本身是概念固定名称的一部分。
  - 避免：`Theory of Teaching (Gruschka)`、`Codeswitcher (School)`、`Single-Case Design (SCD)`
  - 改为：`Teaching Theory of Gruschka`、`Codeswitcher`、`Single-Case Design`
  - 旧标题可放入 `aliases`，用于兼容检索和旧链接。
- 明确需要保留括号的例外可以保留，例如 `SF (Haraway)`。
- 缩写优先放入 `aliases`，不要为了缩写改变标题。

---

## 3. Script Rules

### Standard Sync and Lint

每次处理完条目、书籍章节、source 记录、模板或 schema 后，运行：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
python3 scripts/vault_lint.py
```

若只想检查某一目录：

```bash
python3 scripts/vault_lint.py --path wiki/concepts
```

更严格检查：

```bash
python3 scripts/vault_lint.py --strict
```

### Index

`scripts/wiki_index.py` 输出：

- `wiki/index.json`：AI / Claude Code 使用的极简索引，用于判断条目是否存在。
- `wiki/index.md`：Quartz 4 / GitHub / Obsidian 可读静态索引，也可作为 `wiki/` 首页。

不要手动编辑 `wiki/index.json` 或 `wiki/index.md`。

`wiki/index.json` 不承担展示功能，不需要包含 tags、status、sources、related_*、journal、book_title 等信息。若脚本保留 aliases，则仅用于判断已有条目和自动补链。

`summary` 只用于生成 `wiki/index.md` 的一行说明；修改 summary 后必须重新运行脚本。

### Automatic Wikilink

`scripts/wiki_linker.py` 根据 `wiki/index.json` 自动同步正文 wikilink。

运行：

```bash
python3 scripts/wiki_linker.py sync
```

规则：

- `title` 和 `aliases` 是自动补链依据。
- 如果某个 alias 太宽泛，直接从条目 frontmatter 的 `aliases` 中删除，再重新运行同步流程。
- 以每个 `##` 二级标题为一个 section。
- 每个 section 内，同一 target 只链接第一次出现。
- `###` 和更低层级不重新计算。
- 删除条目或删除 alias 后，脚本应把失效自动链接还原为纯文本。
- 不链接当前文件自身。
- 跳过 YAML frontmatter、标题行、代码块、已有 Markdown 链接、URL、DOI、HTML、PDF / EPUB 嵌入、blockquote、`[!quote]` callout。
- `## 来源` / `## Sources` 章节只补 source 记录链接，不按普通 wiki 条目补概念链接。
- source 记录可来自 `sources/` 与 `books/`；章节 source 如 `Ch4_Amos_2022` 也应可被补链。
- 单个汉字 alias 只允许在独立出现时补链，不能嵌入词中补链。

### Frontmatter Relations

`scripts/wiki_relations.py` 根据正文 wikilink 自动同步 YAML 中的关系字段。

自动维护：

```yaml
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
sources: []
```

规则：

- `related_*` 根据正文中出现的 wikilink 自动生成，并根据被链接条目的 `type` 分类。
- `## 来源` 或 `## Sources` 章节中的 wikilink 不写入 `related_*`，只写入 YAML `sources`。
- `![[...]]` 嵌入链接不计入关系。
- `## 来源` 中不在 `wiki/index.json` 的 source target 应按原 target 保留，不要用 `Path.stem` 误截断带点号或括号的 source ID。
- AI 不手动填写 `related_*` 和 YAML `sources`；如需建立关系，应在正文中自然使用 wikilink，并在 `## 来源` 章节列出来源。

### Source Record Creation

`scripts/source_record.py` 用于创建 source 记录与 PDF / EPUB 阅读页面。AI 先根据用户指令和 schema 判断来源类型，再调用对应子命令；脚本不负责自动猜类型。

可用子命令：

```bash
python3 scripts/source_record.py article
python3 scripts/source_record.py report
python3 scripts/source_record.py monograph-pdf
python3 scripts/source_record.py monograph-epub
python3 scripts/source_record.py edited-volume-overview
python3 scripts/source_record.py book-chapter
```

分类规则：

| 来源类型 | 子命令 | 输出位置 |
|---|---|---|
| 期刊论文 | `article` | `sources/` |
| 报告／政策文件／白皮书 | `report` | `sources/` |
| 专著 PDF 整本书 source | `monograph-pdf` | `books/<book-folder>/` |
| EPUB 专著 source | `monograph-epub` | `books/<book-folder>/` |
| 论文集／编著整体 overview | `edited-volume-overview` | `books/<book-folder>/` |
| 论文集章节 source | `book-chapter` | `books/<book-folder>/` |

普通论文示例：

```bash
python3 scripts/source_record.py article \
  --file raw/Thomas_2000_RER.pdf \
  --citation "Thomas, J. W. (2000). ..." \
  --journal "Review of Educational Research" \
  --extracted-to "[[Project-Based Learning]],[[Argument_Thomas_2000_RER]]"
```

专著 PDF 示例：

```bash
python3 scripts/source_record.py monograph-pdf \
  --book-folder Bourdieu_1984_HUP \
  --file books/Bourdieu_1984_HUP/Distinction.pdf \
  --citation "Bourdieu, P. (1984). Distinction. Harvard University Press." \
  --book-title "Distinction" \
  --authors "Pierre Bourdieu" \
  --publisher "Harvard University Press" \
  --argument "[[Argument_Bourdieu_1984_HUP]]"
```

EPUB 示例：

```bash
python3 scripts/source_record.py monograph-epub \
  --book-folder Vygotsky_1978_HUP \
  --file books/Vygotsky_1978_HUP/MindInSociety.epub \
  --citation "Vygotsky, L. S. (1978). Mind in society. Harvard University Press." \
  --book-title "Mind in Society" \
  --authors "Lev Vygotsky" \
  --publisher "Harvard University Press" \
  --argument "[[Argument_Vygotsky_1978_HUP]]"
```

论文集章节示例：

```bash
python3 scripts/source_record.py book-chapter \
  --book-folder AppleEd_2019_Routledge \
  --file books/AppleEd_2019_Routledge/Ch03_Biesta_2019.pdf \
  --citation "Biesta, G. (2019). Chapter title. In M. Apple (Ed.), Book title (pp. xx-xx). Routledge." \
  --book-title "Book Title" \
  --chapter-title "Chapter Title" \
  --authors "Gert Biesta" \
  --editors "Michael W. Apple" \
  --publisher "Routledge" \
  --extracted-to "[[Argument_Biesta_2019_purpose]]" \
  --part-of "[[AppleEd_2019_Routledge]]"
```

Source 记录统一 frontmatter：

```yaml
title: ""
type: source
subtype: ""
publication_type: ""
citation: ""
source_file: ""
book_file: ""
extracted_to: []
processed_date: YYYY-MM-DD
status: processed
```

可选字段：

```yaml
journal: ""
issuing_organization: ""
book_title: ""
chapter_title: ""
authors: []
editors: []
publisher: ""
part_of: ""
```

### Vault Lint

`scripts/vault_lint.py` 是只读检查脚本，默认不修改文件。

检查内容包括：

- summary YAML 安全规则
- frontmatter YAML 是否可解析
- Argument 是否误用 aliases
- tags 格式
- related_* / sources / part_of 格式
- 模板字段一致性
- 坏 wikilink
- 嵌入文件是否存在
- `## 来源` 是否存在
- source record 格式
- Quartz 风险
- 旧命令 `scripts/update_wiki_index.py` 残留
- 旧路径 `wiki/wiki-index.md` 残留
- `wiki/index.json` 与实际条目一致性

---

## 4. Source Files

### raw/

`raw/` 只放原始 PDF，不加 frontmatter。

### sources/

普通论文或报告处理完成后，优先使用 `source_record.py article` 或 `source_record.py report` 创建 source 记录。不要手写固定结构，除非脚本无法满足特殊情况。

```bash
python3 scripts/source_record.py article --file raw/FILENAME.pdf --citation "..." --extracted-to "[[...]]"
```

规则：

- `article` / `report` 默认将 `raw/*.pdf` 移入 `sources/`。
- `--copy` 表示复制而不是移动。
- `--no-move` 表示文件保留原位，但仍生成 source 记录。
- `extracted_to` 中每个 wikilink 必须加双引号，脚本会自动生成合法 YAML 数组。
- 书籍来源记录按对应 book schema 执行。
- `sources/` 下的 source 记录不是普通 wiki 条目，不进入 `related_*` 自动维护逻辑。

---

## 5. Workflow

### 普通论文／报告

1. 读取 `vault-schema.md`。
2. 若触发书籍任务，转入对应 book schema，不继续普通论文流程。
3. 提取 `raw/FILENAME.pdf` 文本。
4. 扫描文献，列出可提取条目：Concept / Theory / Fact / Person / Method / Argument。
5. 读取 `wiki/index.json` 判断候选条目是否已存在；必要时搜索对应二级文件夹确认。
6. 将候选分为：
   - 待更新条目
   - 待新建条目，并标注类型与目标二级文件夹
7. 逐条处理待更新条目：读取文件 → 判断插入位置 → 用 `str_replace` 精确整合。
8. 逐条处理待新建条目：只读取对应模板 → 按模板写入对应二级文件夹。
9. 在正文中自然使用 wikilink，在 `## 来源` 章节列出 source wikilink。
10. 使用 `source_record.py article` 或 `source_record.py report` 创建 source 记录。
11. 运行标准同步与检查流程。

### 书籍任务

只读取匹配的一种 schema：

| 触发条件 | 读取文件 |
|---|---|
| `(Ed.)` / 编著 / 论文集 | `books/schema-edited-volume.md` |
| 专著 PDF / 用户标注「专著」 | `books/schema-monograph-pdf.md` |
| `.epub` | `books/schema-monograph-epub.md` |

书籍任务每次只处理一章或用户当前指定的章节内容。处理完当前章节后停止。

---

## 6. Entry Perspective

### Knowledge-base perspective

除 Argument 外，所有条目都以知识对象本身为中心，论文只是证据来源。

- Concept：写概念本身。
- Theory：写理论本身。
- Method：写方法本身。
- Person：写人物本身。
- Fact：写现实中的政策、事件、制度或历史节点。
- Argument：写某篇论文、章节、报告或专著的论证结构。

禁止在非 Argument 条目中写：

> 本文研究了……  
> 作者认为……  
> 本研究发现……

应改为知识库陈述：

> 通识教育科于 2009 年在香港正式推行……  
> 该政策的主要影响包括……  
> 学界对此存在争议……

### Argument style

Argument 可以围绕文献本身，但也不要反复使用“本论文 / 本章 / 作者认为 / 本研究发现”。直接陈述论证思路。

Argument 必须详细拆解论证链：

1. 问题从哪里来
2. 使用了什么概念或理论
3. 依赖哪些前提
4. 证据如何支持前提
5. 中间推论如何连接到结论
6. 哪些地方可能存在跳跃、弱证据或过度推论

语言要易懂。抽象理论必须配例子；例子优先来自原文，原文没有时可用简短教育情境说明。

---

## 7. Extraction Criteria

### Fact

有明确时间 + 地点 + 主体的政策、事件、制度安排，应建 Fact 条目。

例：

- 政策、法案、课程纲要、白皮书
- 历史事件、课程改革节点
- 教育制度、考试制度、督学制度、分流制度

不要把具体政策或事件只当作概念例子一笔带过。

### Theory

论文提供以下任一信息时，可建 Theory 条目：

- 明确作为理论框架
- 用于解释现象或论证立场
- 有专门章节介绍核心主张、起源、代表人物或应用方式

只被点名但无介绍 → 不单独建条目，只在相关条目中链接。

### Method

论文提供以下任一信息时，可建 Method 条目：

- 研究设计
- 数据收集或分析方式
- 方法选择的理由
- 认识论立场
- 操作步骤、适用场景或局限

方法只被命名但无介绍 → 只记录在 Argument 的研究方法中，不单独建条目。

### Person

不是每个作者都建 Person。只有符合以下之一才建：

- 有独立理论、概念或框架贡献
- 在领域内有持续影响力
- 文献专门讨论其思想

只是论文作者、顺带引用一次、受访者 → 不建 Person 条目。

---

## 8. Writing and Template Rules

- 新建条目必须读取对应 `wiki/templates/template-*.md`。
- 模板提供结构和样式；有内容才写，没有内容可省略空章节。
- `summary` 只用于索引说明，不是摘要。
- `summary` 外层必须使用双引号包裹。
- `summary` 内容内部禁止出现英文冒号 `:`、双引号 `"`、单引号 `'`。
- 如果英文标题原本有冒号，用下划线 `_` 替代。
- 重要定义、关键数据、关键引用、争议、例子等，按模板使用 callout。
- 常用 callout：
  - `[!info]`：定义、背景、方法说明
  - `[!abstract]`：理论框架、结构、政策摘要
  - `[!success]`：主要发现、影响、效果
  - `[!warning]`：争议、局限、批评
  - `[!quote]`：原文引用
  - `[!example]`：案例、教育情境例子
  - `[!note]-`：可折叠补充说明
- 不要过度使用 callout；只在能增强可读性或区分信息类型时使用。
- 理论或哲学内容要避免纯定义堆砌；抽象主张后应有例子或说明。
- 写作必须自然中文，不直译英文，不写欧化长句。
- 避免 Markdown 加粗语法 `**...**`，用标题、列表或 callout 表达重点。

---

## 9. Updating Existing Entries

整合新内容时：

- 保留原有内容。
- 新信息补充到最相关章节。
- 相似内容要融合，不堆砌重复条目。
- 有分歧时放入“争议与批评”，不要覆盖原观点。
- 新旧内容之间加过渡句，保持段落自然。
- 每条新增信息附来源页码。
- 更新 frontmatter：
  - `updated`
  - 需要时更新 `confidence`
  - `related_*` 与 `sources` 不手动更新，交由脚本同步。
- 在正文中自然使用 wikilink，脚本会自动维护 frontmatter 关系。

### 章节组织

- 分点 < 8 条：按时间或逻辑顺序排列。
- 分点 ≥ 8 条：按 `###` 子主题分组，组内按时间排列。
- 争议章节：按立场分组。
- 发展脉络：按时间顺序。
- 来源列表：只按时间排序，不分主题。

---

## 10. Aliases and Tags

### aliases

`aliases` 同时承担两个功能：

1. Obsidian 检索别名
2. `wiki_linker.py` 自动 wikilink 的匹配词

因此 aliases 必须保持精确。若某个 alias 产生错误链接，直接从对应条目的 aliases 中删除，然后重新运行标准同步命令。

- Argument 不使用 `aliases`。
- Concept / Theory / Method / Fact 的 `aliases` 写中文译名、常见英文变体和缩写。
- Person 的 `aliases` 主要写中文全称；只有非常著名或中文文献中常用简称的人物才写简称，如 `杜威`、`皮亚杰`、`布迪厄`、`阿普尔`、`哈蒂`。
- 不要写过短或过宽泛的 aliases，如“资本”“文化”“教育”“政策”“课程”“能力”“国家”“公平”。
- 不要轻易写单个汉字 alias；只有该字作为独立术语有强识别度时才保留，例如特定儒学概念。单字 alias 过宽时应删除，避免正文词语内部误链接。
- 全小写连字符 alias 只在确有检索价值时保留；不要把 tag 风格 slug 当作默认 alias。

### tags

- tags 全部英文、小写连字符。
- 常用前缀：
  - `region/`
  - `level/`
  - `subject/`
  - `paradigm/`
  - `theme/`
  - `method/`
  - `theory/`
  - `policy/`
  - `source/`

---

## 11. Wikilink and Duplication Rules

核心原则：用 wikilink 减少重复。

- 详细内容只写在最相关的主条目中。
- 其他条目只写一句关系说明 + wikilink。
- 正文中第一次出现已有条目名称时加 wikilink；实际补链由 `wiki_linker.py` 以 `##` section 为作用域执行。
- 泛指某类事物时不链接；如自动链接不合适，删除对应 alias 后重新同步。
- 条目尚未建立时先写纯文字，建立后再补链接。
- AI 不手动维护 frontmatter `related_*`；正文链接是关系来源。

---

## 12. Quartz / Markdown Safety

写入 Markdown 时注意：

- HTML 颜色不要写 `#ccc`，改用 `rgb(204,204,204)`。
- DOI / URL 若含特殊字符，优先放 frontmatter，或用反引号包裹。
- 不在正文写内联 JS；脚本逻辑放外部文件。
- 数学公式：
  - 行内公式：`$d = 0.40$`
  - 独立公式：
    ```markdown
    $$d = ...$$
    ```
