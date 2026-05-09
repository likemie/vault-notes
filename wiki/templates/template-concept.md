---
title: <% tp.file.title %>
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

> [!abstract] 速览
> - **一句话定义**：
> - **所属领域**：
> - **相关理论**：
> - **相关人物**：
> - **常见混淆**：
> - **使用风险**：

> [!info]- Frontmatter 格式规范
> - `tags` — 用方括号列表，内容 tag 建议使用英文小写连字符。
> - 推荐 tag 前缀：`level/`、`region/`、`method/`、`theory/`、`policy/`、`subject/`、`theme/`、`source/`。
> - `related_*` 和 `sources` — 所有值必须加引号。
> - wikilink 必须包在引号内，否则 Obsidian 无法解析 frontmatter。
> - 单个值也需要引号和方括号：`related_concepts: ["[[项目式学习]]"]`

> [!warning]- 写入规则（每次写入前必须执行）
> 1. 确定新内容属于哪个 `##` 章节。
> 2. 分点 ≥ 8 条 → 按主题建 `###` 子主题，组内按时间排列。
> 3. 分点 < 8 条 → 直接按时间顺序插入正确位置，禁止追加末尾。
> 4. 写入前声明：「归属章节 > 子主题 > 插入位置」，再用 str_replace 写入。


---

## 定义

> [!info] 核心定义
> 核心定义，附原文引用。

> [!quote]
> "原文引用"（Author, year, p.X）

---

## 概念辨析

> [!example]
> - vs [[问题式学习]] — 区别说明

---

## 概念演变

> [!note]
> 概念的起源与发展脉络，关键节点附来源。

> [!note]- 1920s–1950s 早期发展
> - 1920s [[Dewey]] 提出做中学理念（p.X）
> - 1950s [[Kilpatrick]] 发展为项目法（p.X）

---

## 核心要素

> [!abstract]
> 构成要素逐条列出，每条附来源。

---

## 理论基础

> [!tip]
> - [[建构主义]] — 一句话说明关系

---

## 实证发现

> [!success]
> 有数据或明确结论支撑的发现，每条注明来源与适用条件：
> - 发现描述，适用条件（学段、地区、样本）。（Author, year, p.X）

> [!info]- 核心数据
> 效应量 d = 0.40，样本量 N = 2000（Author, year, p.X）

---

## 争议与批评

> [!warning]
> - 批评描述，附来源和立场。（Author, year, p.X）

---

## 相关案例／政策

> [!example]
> - [[芬兰国家核心课程2016]]

---

## 来源

- [[Thomas_2000_RER]]
