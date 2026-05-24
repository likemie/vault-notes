# Vault Schema

本文件只保留 AI / Claude Code 处理文献时必须遵守的规则。具体页面结构以 `wiki/templates/` 中对应模板为准。

---

## 1. Core Principles

- 只读取当前任务需要的文件，避免扫描无关文件夹。
- 先读 `wiki/index.json` 判断条目是否可能已存在；若缺失、过期或有歧义，再按类型搜索对应二级文件夹。
- `wiki/index.json` 和 `wiki/index.md` 由 `scripts/wiki_index.py` 自动生成，不手动维护。
- `wiki/index.md` 是 Quartz 4 / Obsidian / GitHub 可读索引页面，可作为 `wiki/` 首页。
- 新建、移动、删除、重命名条目后，运行完整同步流程：
  ```bash
  python3 scripts/wiki_index.py
  python3 scripts/wiki_linker.py sync
  python3 scripts/wiki_relations.py sync
  python3 scripts/wiki_index.py
  ```
- 修改已有条目必须使用 `str_replace`，只替换需要修改的段落，不重写整个文件。
- 写入前必须声明插入位置：
  > 本条内容属于 `## 章节名 > ### 子主题名`，插入位置在……之后／之前，理由是……
- 所有来源性陈述都必须标注页码：`（Author, year, p.X）`。
- 不使用来源以外的知识；不确定时宁可不写。
- AI 不手动维护 `related_*` 和 YAML `sources`；这些字段由 `scripts/wiki_relations.py` 根据正文 wikilink 与 `## 来源` 章节自动同步。

---

## 2. Folder Structure

```text
raw/                         待处理原始文献，不编辑
sources/                     已处理论文档案
books/                       书籍工作区与书籍 schema
  schema-edited-volume.md
  schema-monograph-pdf.md
  schema-monograph-epub.md
templater/                   Obsidian Templater 插件模板，不供 AI 工作流读取
scripts/
  wiki_index.py               自动生成 wiki/index.json 与 wiki/index.md
  wiki_linker.py              根据 index.json 自动同步正文 wikilink
  wiki_relations.py           根据正文 wikilink 自动同步 YAML related_* 与 sources
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

---

## 3. Script Rules

### Index

`scripts/wiki_index.py` 的实际路径是：

```text
/Users/shaoyangwu/Documents/MyNotes/scripts/wiki_index.py
```

运行方式：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/wiki_index.py
```

脚本输出：

- `wiki/index.json`：AI / Claude Code 使用的极简索引，用于判断条目是否存在。
- `wiki/index.md`：Quartz 4 / GitHub / Obsidian 可读静态索引，也可作为 `wiki/` 首页。

不要手动编辑 `wiki/index.json` 或 `wiki/index.md`。

`wiki/index.json` 不承担展示功能，不需要包含 tags、status、sources、related_*、journal、book_title 等信息。是否保留 aliases 由脚本实现决定；aliases 若进入 index，则仅用于判断已有条目和自动补链。

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

### Frontmatter Relations

`scripts/wiki_relations.py` 根据正文 wikilink 自动同步 YAML 中的关系字段。

运行：

```bash
python3 scripts/wiki_relations.py sync
```

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
- AI 不手动填写 `related_*` 和 YAML `sources`；如需建立关系，应在正文中自然使用 wikilink，并在 `## 来源` 章节列出来源。

脚本不得修改：

```yaml
title:
aliases:
summary:
type:
subtype:
tags:
citation:
journal:
book_title:
authors:
editors:
publisher:
part_of:
confidence:
status:
created:
```

### Standard Sync Command

每次处理完条目、书籍章节、source 记录或模板更新后，运行：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

---

## 4. Source Files

### raw/

`raw/` 只放原始 PDF，不加 frontmatter。

### sources/

普通论文或报告处理完成后，将 PDF 移入 `sources/`，并建立同名 `.md`：

```markdown
---
citation: "APA citation"
extracted_to: ["[[Entry A]]", "[[Argument_Author_Year_Journal]]"]
processed_date: YYYY-MM-DD
---

# FileName

![[FileName.pdf]]
```

规则：

- `extracted_to` 中每个 wikilink 必须加双引号。
- `sources` / `extracted_to` 字段使用数组格式。
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
7. 移动 PDF 到 `sources/`，新建同名 source `.md`。
8. 逐条处理待更新条目：读取文件 → 判断插入位置 → 用 `str_replace` 精确整合。
9. 逐条处理待新建条目：只读取对应模板 → 按模板写入对应二级文件夹。
10. 在正文中自然使用 wikilink，在 `## 来源` 章节列出 source wikilink。
11. 运行标准同步命令。

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

Argument 可以围绕文献本身，但也不要反复使用“本论文 / 本章 / 作者认为 / 本研究发现”。直接陈述论证思路：

- 错误：本论文认为全球胜任力政策体现了国际组织的话语扩张。
- 正确：全球胜任力政策被解释为国际组织扩展教育治理话语的一种方式。

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

例：

- ZPD 的详细机制写在 `[[Zone of Proximal Development]]`，不要在 `[[Vygotsky]]` 和 `[[Constructivism]]` 中重复展开。
- `[[Vygotsky]]` 生平只写在人物条目，理论条目中只写一句关系说明。

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
