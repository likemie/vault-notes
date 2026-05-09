---
title: <% tp.file.title %>
aliases: []
type: argument
subtype: edited-volume
citation: ""
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
sources: []
part_of:
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

> [!note]- 文件命名
> `Argument_编者姓(Ed.)_年份_出版社.md`
>
> 例：`Argument_Apple(Ed.)_2019_Routledge.md`

> [!info]- Frontmatter 格式规范
> - `tags` — 用方括号列表，内容 tag 建议使用英文小写连字符。
> - 推荐 tag 前缀：`level/`、`region/`、`method/`、`theory/`、`policy/`、`subject/`、`theme/`、`source/`。
> - `related_*` 和 `sources` — 所有值必须加引号。
> - wikilink 必须包在引号内，否则 Obsidian 无法解析 frontmatter。
> - 单个值也需要引号和方括号：`related_concepts: ["[[项目式学习]]"]`

> [!info]- Aliases 规则（用于 Automatic Linker 自动补链）
> - `aliases` 用于中英文术语映射，建议包含中文译名、英文原名、常见缩写和常见变体。
> - 文件名／标题可以保持英文；中文正文常用术语应写入 `aliases`，例如 `文化资本` → `Cultural Capital`。
> - 不要加入过于宽泛的普通词，如“资本”“文化”“政策”“课程”“能力”“国家”“公平”。
> - 推荐写完整术语：`文化资本`、`教育分层`、`批判话语分析`、`global competence`、`critical discourse analysis`。
> - 缩写可以写入 aliases，例如 `CDA`、`PISA`、`OECD`，但避免单个字母或过短词。

> [!warning]- 写入规则（每次写入前必须执行）
> 1. 确定新内容属于哪个 `##` 章节。
> 2. 分点 ≥ 8 条 → 按主题建 `###` 子主题，组内按时间排列。
> 3. 分点 < 8 条 → 直接按时间顺序插入正确位置，禁止追加末尾。
> 4. 写入前声明：「归属章节 > 子主题 > 插入位置」，再用 str_replace 写入。


> [!warning]- 论证拆解要求（强制执行）
> - **逐步拆解，不跳跃** — 论证结构须完整还原每一个推论步骤，不得跳过中间环节直接给结论；读者应能看清从前提到结论的完整推理链。
> - **用易懂的语言** — 避免堆砌学术术语；每个步骤用一句清晰的中文说明其逻辑，术语首次出现须加括号解释。
> - **抽象主张必须附例子** — 凡涉及抽象论证步骤，须紧跟一个具体例子说明该步骤在实践中的含义。
> - **例子优先来自论文** — 使用论文本身提供的案例或数据，附页码；论文无例子时可用一句话的教育情境类比，但须注明「（编者类比）」。


---

## 编者论点

> [!question]
> 前言中编者提出的核心问题或立场，附原文引用。

> [!quote]
> "原文引用"（Editor, year, p.X）

---

## 全书结构

> [!abstract]
> 编者对各章的分组逻辑与组织框架，说明全书如何回应编者论点。

---

## 理论框架

> [!tip]
> 全书共用的理论视角或分析框架（如有），附来源。
> - [[理论名]] — 一句话说明在全书中的角色

---

## 各章概览

每章处理完后用 str_replace 逐条追加：

> [!example]
> - [[Argument_ChapterAuthor_Year_关键词]] — 该章核心贡献简述（可多句，涵盖主要论点与发现）

---

## 来源

- [[Author(Ed.)_Year_Publisher]]
