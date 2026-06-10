---
title: <% tp.file.title %>
aliases: []
summary: ""
type: concept
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
confidence: medium
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

%% 正文先按概念主题组织，再在主题内按时间、发展阶段或论证顺序排列；用 callout 区分定义、证据、例子、争议和引用。 %%

>
> [!info]- 自动维护字段（对齐脚本）
> - `related_*` 由 `scripts/wiki_relations.py` 自动维护，AI 不手动填写。
> - 正文中的 wikilink 会同步到对应 `related_*`。
> - 非 Argument 条目不写 YAML `sources`，也不写正文 `## 来源`。
> - 来源性陈述使用 APA 短引用链接到对应 Argument，例如 `[[Argument_Ball_2008a_JEP|(Ball, 2008a, p. 12)]]`。
> - 正文自动补链由 `scripts/wiki_linker.py sync` 完成；`aliases` 是自动补链白名单。
> - 处理完成后只自动运行基础索引：
>   ```bash
>   .venv/bin/python3 scripts/wiki_index.py
>   .venv/bin/python3 scripts/citation_index.py
>   ```
> - 如需继续维护链接、关系和检查，先询问用户是否运行标准脚本流程。


> [!info]- Summary 规则（索引用，不是摘要）
> `summary` 只用于索引说明，让读者一眼看出本条目的对象、核心含义和使用场景。
> 写法：`对象类型 + 核心含义/贡献 + 教育研究中的意义`。
> 不围绕某一篇论文写摘要，不堆材料细节；无法概括时留空：`summary: ""`。
>
> [!warning]- Summary YAML 安全规则
> `summary` 外层必须使用双引号包裹：`summary: "一句话索引说明"`。
> 内容内部避开英文冒号 `:`、双引号 `"`、单引号 `'`；需要断句时优先使用中文标点。

> [!warning]- 表达规则
> - 句子不要中英混合；除专名、引文、公式、代码、APA citation 和无法翻译的固定术语外，句子主体使用中文表达。
> - 人名第一次出现必须使用全名；中文正文优先写成中文全名（英文全名），后文再出现可按语境使用中文名、姓氏或代称。
> - 缩写第一次出现必须写成中文（英文全称，缩写）；后文才可单独使用缩写。

> [!info]- Frontmatter 格式规范
> - `tags` 用方括号列表，内容 tag 使用英文小写连字符。
> - 推荐 tag 前缀：`region/`、`field/`、`theory/`、`method/`、`discipline/`、`policy/`、`theme/`。
> - `related_*` 若引用条目，必须写成带引号的 wikilink，如 `"[[Cultural Capital]]"`。
> - `related_*` 由脚本自动同步；需要建立关系时，在正文自然使用 wikilink。
> - 不确定是否已有条目时先写纯文字，不在 frontmatter 中写普通文本。

> [!info]- Citation 写法
> - 非当前 Argument 的来源性陈述使用已处理文献的 APA 短引用，并链接到 Argument。
> - 括号式：`[[Argument_Thomas_2000_RER|(Thomas, 2000, p. 4)]]`
> - 叙述式：`[[Argument_Thomas_2000_RER|Thomas (2000, p. 4)]]`
> - 非 Argument 条目不直接链接 source record，不写 `## 来源`。



> [!info]- Callout 使用规则
>
> | Callout | 适用场景 | 何时改用其他 |
> |---------|----------|--------------|
> | `[!line-a]` + `[!line-b]`（嵌套）| 概念对：每项内容≥2句，命题→延伸的层级关系 | 内容简短时 → 改用 `[!finding-cards]` |
> | `[!finding-cards]` | 3–8条分点，每点1–2行；机制列举、发现清单 | 点数>8 → 建 `###` 子主题 |
> | `[!stat-cards]` | 纯数据：数字、百分比、统计量 | 非数值内容 |
> | `[!quad-grid]` | 恰好4项、权重相当的类型/案例/框架，2×2布局 | 项数≠4，或各项长度差距大 |
> | `[!abstract]` | 章节开头的核心主张摘要 | 替代详细论述 |
> | `[!logic-map]` | 因果链、机制图（Mermaid flowchart） | 关系是并列而非因果/流程 |
> | `[!citation-card]` | 关键逐字引文，附清晰归因 | 过多使用（每节最多1–2个）|
> | `[!tension]` | 理论争议、对立立场 | 方法论批评 → 用 `[!warning]` |
> | `[!phase]` | 有明确起止年代的历史阶段叙事 | 简单里程碑列表 → 用 `[!timeline]` |
> | `[!timeline]` | 概念演变的年代里程碑列表 | 需要段落叙事的阶段 → 用 `[!phase]` |
> | `[!warning]` | 方法论局限、适用边界、重要例外 | — |
> | `[!nav]` | 阅读导览与导航：告知读者本节组织逻辑、推荐阅读路径或指向相关条目；适用于长节开头或子主题群之间 | 内容是核心主张摘要时 → 改用 `[!abstract]` |
> | `[!frames-ref]` | 紧凑 2 列参考网格：数量固定的并列条目（框架、原则、要点），每项一行，适合 6–12 个条目 | 条目有层级或需要散文延伸时 → 改用 `[!finding-cards]` |
> | `[!dev-timeline]` | 大型分阶段发展时间轴：每个阶段含斜体摘要描述、琥珀色小事件点（`ul`）和详细散文；支持嵌套 callout；用 `+`/`-` 后缀控制折叠状态 | 只需里程碑列表 → `[!timeline]`；只需段落叙事 → `[!phase]` |
>
> **嵌套原则**：`[!line-a/b]` 嵌套适合内容丰富的命题对；内容简短时展平为 `[!finding-cards]`。不超过2层嵌套。列表项内嵌套 callout 语法：`>    > [!type]`（外层 `>` + 3 空格 + 内层 `>`）。
> **Mermaid 规则**：节点标签不使用 `\n`，保持单行简短标签。
> **可折叠规则**：任何 callout 加 `+`（默认展开可折叠）或 `-`（默认折叠）均可折叠，`[!dev-timeline]+` 为推荐用法。

> [!warning]- 写入规则（每次写入前必须执行）
> 1. 确定新内容属于哪个 `##` 章节。
> 2. 先判断新内容属于哪个主题或子主题，再判断该主题内部的时间位置、论证位置或概念层级。
> 3. 分点 ≥ 8 条时按主题建立 `###` 子主题，组内按时间或论证顺序排列；分点 < 8 条时按模板逻辑插入正确位置。
> 4. 写入前声明：「归属章节 > 子主题 > 插入位置」，再用 `str_replace` 精确写入。
> 5. 不使用来源以外的知识；资料不足时写”待核”或删除空章节。

> [!info]- 重构经验（Visible Learning 条目整理总结）
>
> **结构决策原则**
> - 主题优先于时间：先按概念主题组织章节，再在主题内部按时间或论证顺序排列，避免把结构变成流水账。
> - 密度触发 callout：内容少（≤3点）→ 散文；内容足够丰富 → callout；不要为了用 callout 而稀释内容。
> - 逻辑链先于排版：动笔前识别要素之间的逻辑关系（如”思维框架→评价性判断→学习意图→DIE→反馈文化”的五层链），再用 `[!logic-map]` Mermaid 显式化，再据此排序各子节。
>
> **内容归属判断**
> - 概念/框架本身 → `## 核心框架` 或对应功能章节。
> - 特定国家接受史、研究者再诠释 → `## 概念发展`（不放在框架或实施章节）。
> - 学术体制批评、期刊事件、争议立场 → `## 争议与批评`（不放在概念发展时间线内）。
> - `[!citation-card]` 统一移至页面末尾（`## 相关研究与案例` 之前），不散落在各节。
>
> **`[!dev-timeline]` 设计模式**
> - 外层 `[!dev-timeline]+`（可折叠，默认展开）；有序列表划分阶段。
> - 每个阶段结构：`**年代 — 标题**` → 斜体摘要（一句话）→ 子事件 `ul`（琥珀色小点，`- YYYY — 事件`）→ 详细散文段落。
> - 子事件列表在 CSS 中渲染为琥珀色小圆点（`rgb(185,140,55)`），与主阶段蓝色大点形成颜色区分。
> - 列表项内嵌套 callout：`>    > [!stat-cards]`，Obsidian 可正常渲染。
>
> **`[!frames-ref]` 设计模式**
> - 适用场景：数量固定的并列条目（框架、原则），每项一行，6–12 个。
> - CSS：钢蓝色 2 列 grid，计数器徽章，0.875em 字号，紧凑内边距。
> - 有层级或需散文延伸时改用 `[!finding-cards]`。
>
> **编辑操作规则**
> - 大文件或脚本修改后，一律用 Python 脚本（`mcp__workspace__bash`）写入，不用 Edit 工具（会触发”file modified since read”错误）。
> - 精确替换时，用 `content.index()` 定位边界标记，避免 `str.replace()` 因空白差异失败。
> - 新 CSS 追加到 `argument-callouts.css` 末尾（`cat >>` 或 Python append），不覆盖全文。


%% CONTENT_START: 以上为写作参考，以下为实际条目内容 %%

---

## 定义

> [!info] 核心定义
> 用一段话说明概念的核心含义、适用范围和边界，附 Argument citation。

> [!quote]
> 中文译文或中文原文。 [[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> Original/English: Original text or English translation.

> [!boundary]- 概念边界
> 说明本概念不等于什么、不适用于什么。
> - 不等于 [[相近概念]] — 区别说明。
> - 不适用于 — 适用范围限制说明。

---

## 概念辨析

> [!contrast-table] 概念辨析
> | 维度 | 本概念 | [[相近概念 A]] | [[相近概念 B]] |
> |------|--------|----------------|----------------|
> | 分析对象 | 说明 | 说明 | 说明 |
> | 核心机制 | 说明 | 说明 | 说明 |
> | 适用范围 | 说明 | 说明 | 说明 |

---

## 核心命题

> [!abstract]
> 用一两句话说明各命题的内在逻辑，例如"命题 A 确立机制 → 命题 B 说明条件 → 命题 C 延伸至空间尺度"。

> [!logic-map] 命题关系
> 
> ```mermaid
> flowchart LR
>     B(["条件/前提"]) -. 使得 .-> A["① 命题一"]
>     A -- 关系标签 --> C["② 命题三"]
>     C -- 关系标签 --> D["③ 命题五"]
>     A -- 关系标签 --> E["④ 命题七"]
>     E -- 关系标签 --> F["⑤ 命题九"]
> ```

> [!line-a] 命题一（英文名）
> 命题内容说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!line-b] 命题二 / 延伸（英文名）
> 与命题一的逻辑关系，以及具体说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

> [!line-a] 命题三（英文名）
> 命题内容说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!line-b] 命题四 / 延伸（英文名）
> 内容说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 概念演变

> [!timeline] 概念演变
> - **YYYY–YYYY** 起源阶段：关键节点、代表人物或重要文本。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **YYYY** 关键转向：概念内涵或适用范围发生重要变化。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **YYYY** 扩展阶段：概念被引入新领域或衍生出新分支。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 理论语境

> [!logic-map] 理论归属
> - [[理论 A]] — 本概念如何源自或扩展该理论。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - [[理论 B]] ←→ 本概念 — 对话或张力关系说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - [[研究传统 C]] — 本概念在该传统中的位置。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 实证发现

> [!stat-cards]-
> - **数字或比例**
>   简短说明适用条件。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!finding-cards]
> 1. 发现描述，说明适用条件（学段、地区、样本或研究设计）。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 争议与批评

> [!tension] 核心争议
> 争议焦点说明——各方立场不是孰对孰错，而是理论路径差异。
> - **立场 A** — 观点说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **立场 B** — 观点说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!warning] 方法论批评与适用局限
> - 批评描述，说明批评对象和立场。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 应用案例

> [!evidence-grid-a] 领域 A
> - [[案例或研究]] — 说明该案例如何体现或应用这一概念。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!evidence-grid-b] 领域 B
> - [[案例或研究]] — 说明该案例如何体现或应用这一概念。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
