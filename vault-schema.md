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
| Concept | `wiki/concepts/<field>/` | 按领域，如 `comparative-education`、`curriculum`、`educational-philosophy`、`educational-leadership-administration` |
| Theory | `wiki/theories/<field>/` | 只放可作为论文理论框架、解释机制或分析视角的理论／框架／模型 |
| Method | `wiki/methods/qualitative/`、`quantitative/`、`mixed/` | 只放研究方法、研究设计、资料收集／分析方法、项目评价方法；课堂教学法放 Concept |
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
  - 缩写、中文译名、常见变体放入 `aliases`。
- 明确需要保留括号的例外可以保留，例如 `SF (Haraway)`。
- 缩写优先放入 `aliases`，不要为了缩写改变标题。

---

## 3. Script Rules

脚本用于维护索引、补链、关系字段和 source 记录。schema 只规定使用边界，脚本实现细节以 `scripts/` 为准。

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

常用检查：

```bash
python3 scripts/vault_lint.py --path wiki/concepts
python3 scripts/vault_lint.py --strict
```

### Generated Fields

不要手动编辑或维护以下生成内容：

- `wiki/index.json`
- `wiki/index.md`
- 各类型索引页，如 `wiki/concepts/index.md`
- frontmatter 中的 `related_*`
- frontmatter 中的 YAML `sources`

### Wikilink Rules

- wikilink 由 `wiki_linker.py` 自动维护，依据是 `title` 和 `aliases`。
- `## 来源` / `## Sources` 章节只放 source wikilink。
- alias 必须精确；过宽或错误的 alias 直接删除后重新同步。
- 单个汉字 alias 只在必要时保留。

### Source Records

Source 记录与阅读页面优先由 `scripts/source_record.py` 生成。AI 先判断来源类型，再调用对应子命令；脚本不负责自动猜类型。

| 来源类型 | 子命令 | 输出位置 |
|---|---|---|
| 期刊论文 | `article` | `sources/` |
| 报告／政策文件／白皮书 | `report` | `sources/` |
| 专著 PDF 整本书 source | `monograph-pdf` | `books/<book-folder>/` |
| EPUB 专著 source | `monograph-epub` | `books/<book-folder>/` |
| 论文集／编著整体 overview | `edited-volume-overview` | `books/<book-folder>/` |
| 论文集章节 source | `book-chapter` | `books/<book-folder>/` |

`sources/` 下的 source 记录不是普通 wiki 条目，不进入 `related_*` 自动维护逻辑。

---

## 4. Source Files

### raw/

`raw/` 只放原始 PDF，不加 frontmatter。

### sources/

- 普通论文或报告处理完成后，优先使用 `source_record.py article` 或 `source_record.py report` 创建 source 记录。
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
- `summary` 必须围绕条目本身写，不围绕某篇论文或章节写；不要用 `_` 代替标点。
- 如果正式英文标题含冒号，frontmatter `title` 可保留原题名；仅在文件名需要规避 `:` 时改用空格或短横，不用 `_`。
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
- 英文 alias 默认不区分大小写；不要同时写只差大小写的重复 alias。
- 若 title 与缩写已经分别覆盖，不再写 `Full Name (ABBR)` 形式的 alias。
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

## 11. Link and Duplication Rules

核心原则：用链接减少重复，具体补链交给脚本。

- 详细内容只写在最相关的主条目中。
- 其他条目只写一句关系说明。
- 泛指某类事物时不需要强行链接。
- 条目尚未建立时先写纯文字。
- AI 不手动维护 frontmatter `related_*`；关系由正文链接同步生成。

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
