# Vault Schema

## Folder Structure
- `raw/` — 待处理原始文献（不可编辑）
- `sources/` — 已处理论文存档（从 raw/ 移入，不可编辑）
- `books/` — 书籍处理工作区与书籍处理 schema
  - `books/schema-edited-volume.md` — 论文集处理方案
  - `books/schema-monograph-pdf.md` — 专著 PDF 处理方案
  - `books/schema-monograph-epub.md` — 专著 epub 处理方案
  - `books/Author(Ed.)_Year_Publisher/` — 论文集文件夹
  - `books/Author_Year_Publisher/` — 专著文件夹
- `wiki/` — 知识条目根目录
  - `wiki/index.json` — AI / Claude Code 检索用机器索引，由脚本自动生成，不手动维护
  - `wiki/index.md` — GitHub / Quartz / Obsidian 可读的静态索引，由脚本自动生成，不手动维护
  - `wiki/concepts/` — 概念，按领域二级分类
    - `wiki/concepts/comparative-education/`
    - `wiki/concepts/curriculum/`
    - `wiki/concepts/educational-philosophy/`
    - 其他领域按需新增，文件夹名使用小写英文连字符
  - `wiki/theories/` — 理论，按领域二级分类
    - `wiki/theories/comparative-education/`
    - `wiki/theories/curriculum/`
    - `wiki/theories/educational-philosophy/`
    - 其他领域按需新增，文件夹名使用小写英文连字符
  - `wiki/methods/` — 研究方法，按方法类型二级分类
    - `wiki/methods/qualitative/`
    - `wiki/methods/quantitative/`
    - `wiki/methods/mixed/`
  - `wiki/persons/` — 人物，按国籍／地区二级分类
    - `wiki/persons/china/`
    - `wiki/persons/us/`
    - `wiki/persons/uk/`
    - `wiki/persons/france/`
    - `wiki/persons/germany/`
    - `wiki/persons/japan/`
    - `wiki/persons/russia/`
    - `wiki/persons/global/` — 国籍不明、跨国组织人物或难以归入单一国家者
    - 其他国家／地区按需新增，文件夹名使用小写英文
  - `wiki/facts/` — 事实／政策／事件，按国家／地区二级分类
    - `wiki/facts/china/`
    - `wiki/facts/finland/`
    - `wiki/facts/hongkong/`
    - `wiki/facts/singapore/`
    - `wiki/facts/us/`
    - `wiki/facts/global/` — 国际组织主导或全球性政策（PISA、UNESCO 等）
    - `wiki/facts/multi/` — 涉及多个特定国家的比较或联合政策
    - 其他国家按需新建，文件夹名用小写英文
  - `wiki/arguments/` — 论证框架，按文献类型二级分类
    - `wiki/arguments/journal-articles/`
    - `wiki/arguments/books/`
    - `wiki/arguments/reports-policy-documents/`
  - `wiki/templates/` — AI / Claude Code 条目模板（新建条目时按需读取；不等同于 Obsidian Templater 插件目录）
- `templater/` — Obsidian Templater 插件模板目录（仅供插件插入模板使用，不替代 `wiki/templates/`）
- `scripts/update_wiki_index.py` — 扫描 `wiki/` 并生成 `wiki/index.json` 与 `wiki/index.md`
- `vault-schema.md` — 本文件（位于根文件夹，不在 wiki/ 内）

---

## Wiki 文件存放规范

| 条目类型 | 存放路径 | 文件名格式 | 示例 |
|---------|---------|-----------|------|
| 概念 | `wiki/concepts/<field>/` | `English Title.md` | `wiki/concepts/comparative-education/Cross-National Attraction.md` |
| 理论 | `wiki/theories/<field>/` | `English Title.md` | `wiki/theories/educational-philosophy/Constructivism.md` |
| 研究方法 | `wiki/methods/qualitative/`、`wiki/methods/quantitative/`、`wiki/methods/mixed/` | `English Title.md` | `wiki/methods/qualitative/Ethnography.md` |
| 人物 | `wiki/persons/<nationality-or-region>/` | `English Name.md` | `wiki/persons/us/John Dewey.md` |
| 事实／政策／事件 | `wiki/facts/<region>/` | `English Title.md` | `wiki/facts/finland/Finnish National Core Curriculum 2016.md` |
| 期刊论文 Argument | `wiki/arguments/journal-articles/` | `Argument_Author_Year_Journal.md` | `wiki/arguments/journal-articles/Argument_Thomas_2000_RER.md` |
| 书籍 Argument | `wiki/arguments/books/` | `Argument_Author_Year_Publisher.md` | `wiki/arguments/books/Argument_Vygotsky_1978_HUP.md` |
| 报告／政策文件 Argument | `wiki/arguments/reports-policy-documents/` | `Argument_Organization_Year_Report.md` | `wiki/arguments/reports-policy-documents/Argument_OECD_2012_Report.md` |


**二级文件夹归类规则：**
- Concepts / Theories 按主要学术领域归类，例如 `comparative-education`、`curriculum`、`educational-philosophy`。
- Persons 按国籍／地区归类；若国籍不明、跨国身份明显或难以归入单一国家，放入 `global`。
- Methods 按方法类型归类：`qualitative`、`quantitative`、`mixed`。
- Facts 按地区归类：主要发生在某一国／地区 → 对应地区文件夹；国际组织主导或全球性 → `global`；涉及多个特定国家 → `multi`。
- Arguments 按文献类型归类：期刊论文 → `journal-articles`；专著／论文集整体／书籍章节 → `books`；报告或政策文件 → `reports-policy-documents`。
- 遇到新领域时可按需新建二级文件夹，命名一律使用小写英文连字符。
- Obsidian wikilink 不含路径，移动文件不会断链；但 frontmatter `sources` 与脚本生成的 `wiki/index.json` 需要同步更新。

**所有条目直接写入对应正式文件夹，修改已有条目用 `str_replace` 替换特定段落，不重写整个文件。**

**Facts 子文件夹判断规则：**
- 主要发生在某一国／地区 → 放该国文件夹，tag 标注其他相关国家
- 国际组织主导或全球性（PISA、UNESCO、世界银行等）→ 放 `global/`
- 涉及两三个特定国家的比较或联合政策 → 放 `multi/`
- 遇到新国家 → 按需新建子文件夹，文件夹名用小写英文（如 `uk/`、`japan/`）
- Obsidian wikilink 不含路径，移动文件不会断链；但 frontmatter sources 字段须同步更新路径

---

## Raw / Sources 文件规范

### 命名格式
`作者姓_年份_期刊缩写`（PDF 和 md 同名）

| 文献类型 | 期刊／出版社缩写 | 示例 |
|---------|----------------|------|
| 期刊论文 | 期刊缩写（如 RER、JCS、TTE） | `Thomas_2000_RER` |
| 书籍 | 出版社缩写（如 HUP、MIT、Routledge） | `Vygotsky_1978_HUP` |
| 报告／政策文件 | Report | `OECD_2012_Report` |

### raw/ 文件
只放原始 PDF，无需任何 frontmatter，直接以论文原文存档：
```
raw/
  Thomas_2000_RER.pdf
  Vygotsky_1978_HUP.pdf
```

### sources/ 文件
处理完成后，PDF 移入 sources/，同时新建同名 md 文件作为文献档案：
```
sources/
  Thomas_2000_RER.pdf
  Thomas_2000_RER.md   ← 同名 md，嵌入 PDF 并记录提取信息
```

md 文件结构：
```markdown
---
citation: "Thomas, J. W. (2000). A review of research on project-based learning. Review of Educational Research."
extracted_to: ["[[项目式学习]]", "[[建构主义]]", "[[Argument_Thomas_2000_RER]]"]
processed_date: 2026-04-30
---

# Thomas_2000_RER

![[Thomas_2000_RER.pdf]]
```

- `citation` — APA 完整引用，用双引号包裹整个字符串
- `extracted_to` — 本论文提取出的所有条目；**每个 wikilink 必须用双引号包裹，整体为数组格式**，否则 Obsidian 无法解析 frontmatter
- `processed_date` — 处理日期，格式 YYYY-MM-DD
- `![[文件名.pdf]]` — 嵌入 PDF，点开 md 即可预览原文

> ⚠️ **常见错误：** `extracted_to: [[条目A]], [[条目B]]` 会导致 frontmatter 显示为原始代码。
> **正确写法：** `extracted_to: ["[[条目A]]", "[[条目B]]"]`

---

## 术语定义

- **条目** — 一个 wiki 页面文件（如 `项目式学习.md`）
- **章节** — 条目页面内的 `##` 标题段落（如 `## 定义`、`## 实证发现`）
- **分点** — 章节内的列表项（`-` 开头的一行）
- **子主题** — 分点数量达到阈值时，在章节内用 `###` 小标题归组

---

## 工作流

每次处理论文时，严格按以下顺序执行，以减少不必要的文件读取：

```
1. 读取 vault-schema.md（规则，必读）
2. 检查触发条件：
   看到「(Ed.)」标注 → 读取 books/schema-edited-volume.md，按论文集流程处理，不继续以下步骤
   看到「专著」标注 → 读取 books/schema-monograph-pdf.md，按专著 PDF 流程处理，不继续以下步骤
   文件为 .epub 格式 → 读取 books/schema-monograph-epub.md，按专著 epub 流程处理，不继续以下步骤
   以上均无 → 继续以下论文流程

3. 用 Python 提取 PDF 文本：
   python3 -c "
   import fitz  # pymupdf
   doc = fitz.open('raw/FILENAME.pdf')
   text = ''.join(page.get_text() for page in doc)
   print(text)
   "
4. 基于「提取规范」扫描论文，列出所有可提取的条目名单
   （严格按各类型判断标准筛选，不符合的不列入）

5. 判断条目是否已存在：
   - 读取 `wiki/index.json` 作为机器可读索引，用于快速识别可能已存在的条目
   - `wiki/index.json` 与 `wiki/index.md` 由 `scripts/update_wiki_index.py` 自动生成，不手动维护
   - 若 `wiki/index.json` 不存在、过期或结果有歧义，再按条目类型搜索对应正式文件夹：
     Concept → `wiki/concepts/<field>/`
     Theory → `wiki/theories/<field>/`
     Method → `wiki/methods/qualitative/`、`wiki/methods/quantitative/`、`wiki/methods/mixed/`
     Person → `wiki/persons/<nationality-or-region>/`
     Policy / Event / Fact → `wiki/facts/<region>/`
     Argument → `wiki/arguments/journal-articles/`、`wiki/arguments/books/`、`wiki/arguments/reports-policy-documents/`
   - 以文件名、frontmatter `title`、`aliases`、已有 wikilink 为依据判断是否已存在
   - 已存在 → 待更新列表
   - 不存在 → 待新建列表，同时标注条目类型与目标二级文件夹
     （Concept / Theory / Policy / Event / Person / Method / Argument）

6. 移动 PDF 并建立文献档案：
   mv raw/FILENAME.pdf sources/FILENAME.pdf
   在 sources/ 新建同名 md，填入 citation、extracted_to、processed_date，嵌入 PDF

7. 处理待更新列表（逐条执行）：
   读取条目文件
   → 检查格式是否符合当前规范，不符合则顺带更新：
      - 章节之间是否有 `---` 分割线，没有则补上
      - 时间线类章节事件 ≥ 8 条但尚未用 callout 分期，则重构为 callout
      - 有具体数字的关键数据是否已用 `[!info]` callout 高亮，没有则补上
      - 原文引用是否已用 blockquote 格式，没有则补上
   → 检查各章节是否需要重构（分点 ≥ 8 条未分子主题？有重复？顺序混乱？）
   → 需要重构 → 先用 str_replace 重构章节，再写入新内容
   → 写入前必须先声明（不可跳过）：
      「本条内容属于 ## [章节名] > ### [子主题名]（如有），
        插入位置在 [前一条内容] 之后 / [后一条内容] 之前，
        理由：[时间顺序 or 主题归属]」
   → 声明完毕后，用 str_replace 精确插入该位置，不追加到末尾
   → 禁止在声明位置以外的地方写入

8. 处理待新建列表（按类型逐条执行）：
   读取该条目对应的模板文件（同类型连续处理时模板只读一次）：
   - Concept   → wiki/templates/template-concept.md
   - Theory    → wiki/templates/template-theory.md
   - Policy    → wiki/templates/template-fact-policy.md
   - Event     → wiki/templates/template-fact-event.md
   - Person    → wiki/templates/template-person.md
   - Method    → wiki/templates/template-method.md
   - Argument  → wiki/templates/template-argument.md
   → 按模板新建条目，写入对应类型的二级正式文件夹
   → 新建时内容已超过 8 条分点的章节，直接按子主题分组写入
   → 写完后检查各章节内部顺序是否符合「先主题后时间」逻辑
   → 完成后处理下一条

9. 双向链接维护：
    对本次新建或修改的每个条目，逐一检查其正文中出现的所有 wikilink：
    a. 被链接的条目已存在 → 读取该条目，在对应章节用 str_replace 补入反向链接
    b. 被链接的条目尚不存在 → 跳过，等该条目建立时再补
    同时更新被链接条目的 frontmatter related_* 字段，确保双向引用完整

10. 运行 `python3 scripts/update_wiki_index.py`，自动更新 `wiki/index.json` 和 `wiki/index.md`
```

**原则：按论文内容匹配条目，按需读取。**
具体做法：扫描论文，识别出现的概念、理论、人物、政策、方法等名称 → 按类型搜索对应正式文件夹，判断待更新和待新建 → 更新组直接读取条目文件整合，新建组按类型读取模板后新建 → 未在论文中出现的条目一律不读取。

**关于 `wiki/index.json` 与 `wiki/index.md`：**
- `wiki/index.json` 是 AI / Claude Code 使用的机器索引，用于减少逐文件搜索和 token 消耗
- `wiki/index.md` 是 GitHub / Quartz / Obsidian 可读的静态 Markdown 索引
- 两者都由 `scripts/update_wiki_index.py` 自动生成，不手动维护
- 新建、移动、删除或重命名条目后，必须重新运行脚本

---

## 语言与写作规范

**标题与 Tag（英文）：**
- 条目 `title` 字段使用英文，如 `Project-Based Learning`、`Vygotsky`、`Hong Kong Liberal Studies 2009`
- 所有 `tags` 使用英文，包括内容 tag 和属性 tag
- 文件名与 title 保持一致，使用英文

**正文内容（简体中文）：**
- 正文全部使用简体中文，frontmatter 字段名保持英文
- 专有名词、人名、期刊名保留英文，首次出现时加中文注解，如 scaffolding（脚手架）
- 引用格式保持原文语言：(Author, year, p.X)

**写作风格（强制执行）：**
- 不得直译英文原文，须用流畅自然的中文重新表述
- 句式遵循中文表达习惯，避免欧化长句、过度"的"字结构、直译造成的生硬表达
- 参考标准：母语为中文的学术写作者是否会这样表达？

**数学公式：**
- 行内公式用单美元符号：`$d = 0.40$`
- 独立公式块用双美元符号，放在单独段落：
  ```
  $$d = \frac{\sum_{i} w_i d_i}{\sum_{i} w_i}$$
  ```
- 需要编号或标注的公式，用 blockquote 包裹整个公式块：
  ```
  > **公式 (9)**：$$d = \frac{\sum_{\text{all }i} w_i d_i}{\sum_{\text{all }i} w_i}$$
  ```
- 公式后须附来源页码：（Author, year, p.X）

---

## 提取规范

### 模板样式与 callout 使用原则

所有新建条目和重构条目都应尽量遵循对应 `wiki/templates/` 模板的页面结构与样式。

**样式要求：**
- 按模板保留 `##` 章节结构；有内容才写，没有内容可省略空章节。
- 重要定义、关键数据、关键引用、争议、例子等，应按模板使用 callout，而不是写成单调列表。
- 常用 callout：
  - `[!info]` — 定义、背景、方法说明
  - `[!abstract]` — 理论框架、核心结构、政策摘要
  - `[!success]` — 主要发现、影响、效果
  - `[!warning]` — 争议、局限、批评
  - `[!quote]` — 原文引用
  - `[!example]` — 案例、教育情境例子
  - `[!note]-` — 可折叠说明、分期、规则或补充材料
- 不要过度使用 callout；只有能增强可读性或区分信息类型时才使用。
- 已有条目若格式明显旧，应在整合新内容时顺带按当前模板优化样式，但只替换相关章节，不重写整个文件。


### 条目模板的使用原则

模板提供的章节结构是参考框架，不是强制要求：
- **有内容才写，没有就跳过** — 若论文未提供某章节所需信息，直接省略该章节，不留空标题
- **章节可按需增减** — 若论文提供了模板未覆盖的重要信息，可新增合适的章节

### 条目视角：除 Argument 外，所有条目都以知识库为中心

这是最常见的错误，必须严格避免。

**核心原则：**
- **Argument 条目**可以以论文、报告、专著或章节为中心，记录该文献的研究问题、论证结构、方法、发现与局限。
- 但 Argument 也不要用“本论文 / 本章 / 作者认为 / 本研究发现”作为主要表达方式；应直接陈述论证思路、问题意识、推理链和证据。
- **Concept / Theory / Method / Person / Fact 条目**必须以知识库对象本身为中心，论文只是证据来源，不是条目的主角。
- 换言之：除了 `wiki/arguments/` 里的 Argument 可以记录文献自身的论证结构，其他条目都不是论文摘要，也不是“某篇论文说了什么”的整理。

**错误写法（论文视角）：**
> 本文研究了香港通识教育科的实施情况，发现……
> 作者认为……
> 本研究的结论是……

**正确写法（知识库视角）：**
> 通识教育科于2009年在香港正式推行……
> 该政策的主要影响包括……
> 学界对此存在争议……

**判断标准：**
- 把论文拿走，条目内容仍然成立 → 写对了
- 条目内容依赖“这篇论文研究了什么 / 发现了什么 / 作者认为……” → 写错了
- 若确实需要记录“论文如何论证”，应写入对应 `Argument_*.md`，而不是写进 Concept / Theory / Method / Person / Fact 条目

具体规则：
- Concept 条目描述概念本身：定义、要素、演变、争议、应用；论文只作为来源。
- Theory 条目描述理论本身：核心主张、命题、发展脉络、争议；论文只作为来源。
- Method 条目描述方法本身：定义、认识论立场、程序、适用场景、局限；论文只作为来源。
- Person 条目描述人物本身：生平、著作、核心思想、影响、争议；论文只作为来源。
- Fact 条目描述现实中的政策、事件、制度或历史节点；论文只作为来源。
- Argument 条目才描述某篇论文 / 报告 / 章节 / 专著的研究问题、理论框架、方法、论证结构、主要发现和局限；但表达上仍应直接陈述论证思路，而不是反复写“本论文 / 本章 / 作者认为”。
- “结果与影响”章节 → 写该事件 / 政策 / 制度本身的结果与影响，不写该论文的研究结论。
- “争议与批评”章节 → 写学界对该概念 / 理论 / 政策 / 事件 / 人物的争议，不写对该论文的评价。
- 引用论文时使用括号标注来源，如 `（Author, year, p.X）`，不要让“本文”“作者”“本研究”成为句子的主语。

### Argument 条目的写作要求

Argument 虽然以某篇论文、章节、报告或专著为中心，但写法也应避免摘要腔，重点是还原“论证如何成立”。

**表达方式：**
- 不要频繁使用“本论文”“本章”“作者认为”“本文发现”“本研究指出”等主语。
- 优先直接陈述论证思路，例如：
  - 错误：本论文认为全球胜任力政策体现了国际组织的话语扩张。
  - 正确：全球胜任力政策被解释为国际组织扩展教育治理话语的一种方式。
- 必要时可以用“该研究”指代文献，但不要让它成为每段的主语。

**论证拆解：**
- 必须详细拆解推理链，不能只写结论。
- 至少说明：
  1. 问题从哪里来
  2. 文献使用了什么概念或理论
  3. 论证依赖哪些前提
  4. 证据如何支持这些前提
  5. 中间推论如何连接到结论
  6. 哪些地方可能存在跳跃、弱证据或过度推论
- 论证结构要写成读者能看懂的连续推理，而不是几个抽象名词的堆叠。

**语言要求：**
- 使用易懂、自然的中文解释复杂理论。
- 避免连续堆砌抽象术语，如“治理性、主体化、再语境化、制度同构”。
- 术语首次出现时必须用括号或一句话解释其含义。

**例子要求：**
- 如果论证过于抽象，必须加入例子。
- 例子优先来自原文案例、数据、访谈材料或政策文本，并标注页码。
- 原文没有例子时，可加入一句简短的教育情境说明，帮助读者理解抽象论证。
- 格式建议：
  > [!example] 例子
  > 具体说明该抽象论证在教育情境中意味着什么。（Author, year, p.X）

### 严格限定在论文内容之内
- **只提取论文中明确出现的信息** — 不补充、不推断、不延伸
- **禁止使用论文以外的背景知识** — 即使某个概念有更广泛的定义，只写论文里的表述
- **每条信息必须能在论文中找到对应原文** — 附页码引用 `（Author, year, p.X）`
- **不确定出处时宁可不写** — 避免混入未经核验的信息

### 必须新建 Fact 条目的情况

Fact 条目容易被忽略，扫描论文时须主动识别以下信号，发现即新建独立条目：

**政策文件**
- 论文提到具体政策、法案、课程纲要、白皮书
- 例：香港2009年推行通识教育科、芬兰2016年国家核心课程、No Child Left Behind法案

**历史事件**
- 论文描述某个具体的历史节点或社会事件
- 例：2019年香港社会运动、2021年通识科被公民科取代、某国课程改革风波

**制度安排**
- 论文描述某国某时期具体的教育制度、考试制度、师资培训制度
- 例：香港会考制度、英国OFSTED督学制度、新加坡分流制度

**判断标准：有明确的时间 + 地点 + 主体（谁在哪里做了什么）→ 必须建 Fact 条目**

不要把政策或事件仅作为概念或理论条目的例子一笔带过，每个具体的政策／事件都应该有自己独立的条目。

### 必须新建 Theory 条目的情况

Theory 容易被当作背景一笔带过，扫描论文时须主动识别：

**明确作为理论框架使用**
- 论文在 Theoretical Framework 或 Literature Review 章节明确援引某理论
- 例：世界体系理论、政策网络理论、批判实在论、制度同构理论

**用于解释现象或论证立场**
- 论文用某理论解释研究发现，或以某理论批评现有做法
- 例：用再情境化理论解释课程移植、用合法周边参与理论解释学习过程

**有专门章节介绍**
- 论文专门介绍该理论的核心主张、起源、主要学者

**判断标准：论文提供了足够信息写出有内容的条目 → 才建 Theory 条目**

论文提供该理论任意一项信息即可建条目（核心主张、起源、主要学者、应用方式等），后续论文可继续补充构造全貌。
仅被点名引用但无任何介绍 → 只在相关条目的「理论基础」一行记录，不单独建条目。

### 必须新建 Method 条目的情况

Method 容易被忽略，扫描论文时须主动识别：

**有专门的研究方法章节**
- 论文有 Methodology 或 Research Design 章节，描述具体研究设计
- 例：案例研究、比较历史分析、系统性文献综述、话语分析

**具体的数据收集或分析方式**
- 论文描述如何收集或分析数据
- 例：半结构式访谈、文件分析、民族志田野工作、内容分析、元分析

**对方法选择有明确辩护**
- 论文解释为何选择该方法，或讨论该方法的认识论立场
- 例：为何选质性而非量性、为何采用批判话语分析

**判断标准：论文提供了足够信息写出有内容的条目 → 才建 Method 条目**

论文提供该方法任意一项信息即可建条目（操作步骤、认识论立场、适用场景、局限性等），后续论文可继续补充构造全貌。
方法只被命名但无任何介绍 → 只在论证框架条目的「研究方法」一行记录，不单独建条目。

### Person 条目的筛选标准

**不是每个作者都建条目**，只有符合以下条件之一才建：

**有独立理论或概念贡献**
- 该人物提出了有名称的理论、概念或框架
- 例：Vygotsky（ZPD）、Bourdieu（文化资本）、Biesta（教育的三重功能）

**在领域内有持续影响力**
- 被多篇论文反复引用，或在某议题上代表一个学派／立场
- 例：某课程改革的主要倡导者、某理论的主要批评者

**论文专门讨论其思想**
- 论文以该人物的思想作为主要理论资源，并详细介绍其主张

**不建条目的情况：**
- 只是论文的作者或共同作者，但思想未被专门讨论
- 只被顺带引用一次，没有专门介绍
- 只是某研究的数据来源或受访者

**判断标准：该人物的思想本身是知识库需要记录的内容 → 才建 Person 条目**

---

## 修改已有条目规范

读取现有条目后，按以下规则整合新论文的内容：

### 整合原则
- **使用 str_replace** — 只替换需要修改的段落，不重写整个文件，节省 token
- **尽量详细** — 从论文中提取尽可能多的细节，充实每个章节；不要三言两语，能展开的尽量展开
- **补充优先** — 新信息补充到对应章节，附来源；内容越丰富越好
- **不删除原有内容** — 即使新论文有不同观点，保留原有内容，在争议章节标注分歧
- **保持流畅性** — 新增内容须与上下文衔接自然，避免生硬拼接；必要时可重写该段落或章节的总结句使其连贯，但不改变原有论点；重写范围限于单个段落或章节，不重写整个文件
- **来源必须标注** — 每条新增信息附 `（Author, year, p.X）`

### 各类新信息的处理方式

**与现有内容一致或互补**
→ 整合进对应章节，详细补充新论文提供的细节、数据、例证，附新来源；不满足于一句话，能写多详细写多详细

**与现有内容有细微差异**
→ 整合时用措辞体现差异，如"在X情境下……""也有研究指出……"，附来源

**与现有内容明显矛盾**
→ 不修改原有论述，在「争议与批评」章节详细展开，须包含：
  1. 争议的核心问题是什么
  2. 各方立场分别是什么，各自的论据是什么
  3. 争议的背景或根源（理论立场、方法论、情境差异等）
  4. 目前是否有共识或仍悬而未决
  格式：
```
### [争议标题]
[争议背景与核心问题，2-3句]
- **[一方立场]**：[具体论据，附来源]（Author, year, p.X）
- **[另一方立场]**：[具体论据，附来源]（Author, year, p.X）
[目前状态：共识／持续争论／情境依赖]
```

**现有章节没有的全新信息**
→ 直接追加到对应章节，详细展开；若现有模板无合适章节，追加到最相关章节末尾并注明

**合并与融会贯通**
每次整合新内容后，检查该章节是否需要重新梳理：
- 相似或重复的观点合并成一段，不要堆砌重复意思的条目
- 同一议题下的多个来源整合成连贯论述，而非各自独立的碎片
- 有内在逻辑关系的内容重新排列，使论述有层次（如从定义→要素→应用→争议）
- 新旧内容之间加过渡句，保持段落流畅，避免生硬拼接
- 合并后确保每条信息仍附来源，不丢失引用

**内容组织原则（每次写入必须执行，不可跳过）**

每次新增或修改任何章节后，必须主动判断该章节是否需要重构，步骤如下：

1. **判断内容量**
   - 该章节分点 < 8 条 → 按时间顺序排列
   - 该章节分点 ≥ 8 条 → 按子主题分组（用 `###` 小标题），子主题内再按时间排列

2. **判断新分点的归属**
   - 分点 < 8 条时：找到时间上正确的插入位置
   - 分点 ≥ 8 条时：先找该分点属于哪个子主题，再在子主题内按时间插入
   - 不要直接追加到末尾

3. **组织规则**
   - 子主题之间用 `###` 小标题区隔，子主题内早期在前，近期在后
   - **例外：争议章节** → 按立场分组（支持方／批评方），组内按时间
   - **例外：发展脉络章节** → 纯时间顺序，不按主题

4. **所有章节适用，但来源列表例外：**
   - 正文各章节（定义、核心要素、实证发现等）→ 分点 ≥ 8 条按主题分组，否则按时间
   - 相关案例／政策、相关研究列表 → 同上规则
   - **来源列表** → 永远只按时间排序，不分主题分组

5. **重构时用 str_replace** — 只替换需要重新排列的章节，不重写整个文件

6. **读取已有条目时，主动检测是否需要重构**
   对每个读取的已有条目，在整合新内容之前先检查：
   - 各章节的分点是否已按正确逻辑组织（时间 or 子主题+时间）
   - 是否有章节分点 ≥ 8 条但尚未按子主题分组
   - 是否有相似或重复的分点尚未合并
   如发现需要重构 → 先用 str_replace 重构该章节，再整合新内容
   无需重构 → 直接整合新内容

### 理论与哲学内容的写作要求
理论和哲学概念抽象难懂，每次写作须：
- **必须附具体例子** — 每个抽象主张后跟一个具体的教育情境例子，格式：
  > 例：[具体场景说明这个主张在实践中意味着什么]
- **避免纯定义堆砌** — 不要连续写多个抽象句子，每隔1-2句插入一个例子或类比
- **例子优先来自论文** — 优先使用论文本身提供的例子或案例，附页码；论文无例子时可用一句简短的教育情境说明帮助理解。

### 修改后检查
- frontmatter `updated` 字段更新为今日日期
- frontmatter `sources` 字段追加新来源
- frontmatter `confidence` 视新证据质量酌情提升

---

## Tag 体系

### 属性 Tag
- `region/` — 地区：`region/finland` `region/china` `region/us` `region/uk` `region/singapore` `region/global`
- `level/` — 学段：`level/early-childhood` `level/k12` `level/higher-ed` `level/corporate`
- `subject/` — 学科领域（见概念分组）
- `paradigm/` — 研究范式：`paradigm/constructivist` `paradigm/behaviourist` `paradigm/interpretivist` `paradigm/critical` `paradigm/positivist`

### 内容 Tag
条目名本身即为 tag，提取时自动添加。所有内容 tag 一律使用英文小写连字符格式：
- `project-based-learning`、`constructivism`、`zone-of-proximal-development`
- 人名保留原拼写：`Vygotsky`、`Dewey`

---

## 书籍处理

看到以下标识或格式时，只读取 `books/` 下对应的一个书籍处理方案，不读取其他书籍 schema，也不继续普通论文流程：

| 触发条件 | 读取文件 | 处理对象 |
|---------|---------|---------|
| 用户标注「(Ed.)」 | `books/schema-edited-volume.md` | 论文集／编著 |
| 用户标注「专著」且文件为 PDF | `books/schema-monograph-pdf.md` | 专著 PDF |
| 文件为 `.epub` 格式 | `books/schema-monograph-epub.md` | 专著 epub |


---

## 链接规则

- `[[条目名]]` — 正文跳转链接
- frontmatter `related_*` — 索引字段，Claude Code 自动维护
- frontmatter `sources` — 按时间先后排序，早期来源在前，新来源追加到对应时间位置
- tag — 横切检索，不建立跳转

### 链接方向
- 概念 ↔ 理论（双向）
- 概念 → 事实（案例）
- 人物 → 理论／概念
- 理论 → 研究方法
- 研究方法 → 论证框架
- 论证框架 → 概念／理论

### Wikilink 使用规范

**核心原则：用 wikilink 取代重复，不要在多个条目里重复写同样的内容。**

条目之间应形成“主条目详细说明 + 其他条目一句话概括并链接”的结构。若某段内容本质上属于另一个条目，应移到或保留在那个条目中；当前条目只写最必要的关系说明，并用 wikilink 指向详细内容。

**何时使用 wikilink：**
- 正文中第一次出现某个已有条目的名称时，必须加 wikilink
- 同一页面内同一名称只链接一次（第一次出现），后续不重复加链接
- 章节列表中提及其他条目时，用 `[[条目名]] — 一句话说明关系` 格式

**何时不用 wikilink：**
- 泛指某类事物而非特定条目时（如"许多理论认为……"不需要链接）
- 该条目尚未建立时，先写纯文字，等条目建立后再补链接

**用链接取代重复内容：**
- **详细内容只写一次，写在最相关的条目里** — 判断标准：这段内容是在描述哪个条目的本质？就写在那个条目里。其他条目提到时，一句话概括 + wikilink，不重复展开
- 例：ZPD 的详细机制写在 `[[最近发展区]]`，不在 `[[Vygotsky]]` 或 `[[建构主义]]` 里重复展开
- 例：Vygotsky 的生平只写在 `[[Vygotsky]]`，理论条目里只写 `[[Vygotsky]] — 社会建构主义的奠基者`
- 例：概念条目的「理论基础」章节只写 `[[建构主义]] — 为PBL提供认识论基础`，不展开建构主义的内容

**交叉引用要双向维护（frontmatter + 正文都要）：**

frontmatter 层面：
- A 条目链接到 B，B 的 frontmatter `related_*` 字段也须包含 A
- 新建条目后，检查其链接到的所有条目，在对应条目的 frontmatter 里补上反向引用

正文层面：
- A 条目正文提到 B，须去 B 的对应章节补一条反向说明 + wikilink
- 例：新建 `[[建构主义]]` 条目，其「应用领域」章节须加 `[[项目式学习]] — 以建构主义为核心理论依据`
- 例：新建 `[[Vygotsky]]` 条目，须去 `[[建构主义]]` 的「发展脉络」章节确认已有 `[[Vygotsky]]` 链接
- 反向链接放在最相关的章节，用 str_replace 插入，不重写整个条目
- 若反向条目尚不存在，记录在当前条目的正文中，等该条目建立后补链接
---

## Quartz 渲染注意事项

写入 md 文件时，以下符号会导致 Quartz 构建失败或渲染异常，必须避免：

**颜色值**：`#ccc` 等以 `#` 开头的颜色值会被 Obsidian 误解析为 wikilink → 改用 `rgb(204,204,204)` 等 rgb 格式

**内联 script 引号**：script 标签内的引号会被 Quartz 转义为 `&quot;` 导致 JS 语法错误 → 改用 `data-` 属性传参，所有逻辑移至外部 js 文件

**`&` 符号**：内联 script 中的 `&` 会被 Quartz 转义为 `&amp;` → 所有含 `&` 的逻辑移至外部 js 文件

**`$` 符号**：HTML 属性或内联 script 中的 `$` 可能被 Quartz 的 LaTeX 插件误判为数学公式 → 避免在 HTML 内容中使用

**DOI 及 URL 中的特殊字符**：md 文件中的 DOI 链接（如 `https://doi.org/10.1080/03057925`）里含有的 `/` 或其他字符，若被 Quartz 误判为标签或路径，会导致该文件构建失败 → 将含特殊字符的 URL 放在 frontmatter 的 `doi:` 字段或用反引号包裹，不直接暴露在正文中；或将该文件夹加入 `quartz.config.ts` 的 `ignorePatterns`
