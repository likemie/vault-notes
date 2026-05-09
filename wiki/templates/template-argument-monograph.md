---
title: <% tp.file.title %>
aliases: []
type: argument
subtype: monograph
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
> `Argument_作者姓_年份_出版社.md`
> 
> 例：`Argument_Vygotsky_1978_HUP.md`

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

## 研究问题

> [!question]
> 全书试图回答的核心问题，综合各章提炼。

---

## 理论框架

> [!abstract]
> 说明贯穿全书的理论资源、概念框架或分析视角。
> - [[理论名]] — 如何贯穿全书运用

---

## 研究方法

> [!info]
> - 方法：[[研究方法名]]
> - 样本：描述
> - 数据来源：描述

---

## 论证结构

> [!example]
> 全书整体论证脉络，综合各章要点：
> 1. 前提／观察
> 2. 论证步骤
> 3. 结论

---

## 各章概览

每章处理完后直接追加，格式自由，忠实记录该章论点、论据、关键引用：

### 第X章 章节标题

本章主要论点、论据与关键引用的自由记录。

---

## 主要发现

> [!success]
> 综合各章提炼的核心发现，附页码来源。
> - 发现描述。（p.X）

> [!info]- 核心数据
> 有具体数字、效应量、样本量或关键证据时放在这里。（p.X）

---

## 关键引用

> [!quote]
> "引用内容"（p.X）

---

## 局限性与批评

> [!warning]
> 作者自身承认的局限，或他人对全书的批评。

---

## 来源

- [[作者姓_年份_出版社]]
