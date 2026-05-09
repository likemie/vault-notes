---
title: <% tp.file.title %>
aliases: []
type: concept
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
sources: []
confidence: medium
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

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


---

## 定义

> [!info]
> 写出该概念的核心定义，优先使用来源中的明确定义；如有不同定义，应标明差异。

> [!quote]
> "原文引用"（Author, year, p.X）

---

## 概念辨析

> [!example]
> 辨析容易混淆的概念，说明相同点、差异和适用边界。
> - vs [[问题式学习]] — 区别说明

---

## 概念演变

> [!note]
> 说明概念的起源、发展脉络、关键转折和代表人物，关键节点附来源。

> [!note]- 分期示例
> - 1920s [[Dewey]] 提出做中学理念（p.X）
> - 1950s [[Kilpatrick]] 发展为项目法（p.X）

---

## 核心要素

> [!abstract]
> 构成要素逐条列出，每条附来源；不要把泛泛描述写成要素。

---

## 理论基础

> [!tip]
> 说明该概念依托哪些理论，以及理论与概念之间的关系。
> - [[建构主义]] — 一句话说明关系

---

## 实证发现

> [!success]
> 有数据或明确结论支撑的发现，每条注明来源与适用条件：学段、地区、样本、研究设计等。
> - 发现描述，适用条件（学段、地区、样本）。（Author, year, p.X）

> [!info]- 核心数据
> 有具体效应量、样本量、比例或统计结果时放在这里。（Author, year, p.X）

---

## 争议与批评

> [!warning]
> 记录概念争议、批评意见和不同立场，避免只写正面定义。
> - 批评描述，附来源和立场。（Author, year, p.X）

---

## 相关案例／政策

> [!example]
> - [[芬兰国家核心课程2016]]

---

## 来源

- [[Thomas_2000_RER]]
