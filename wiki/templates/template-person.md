---
title: <% tp.file.title %>
type: person
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_arguments: []
sources: []
confidence: medium
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

> [!abstract] 人物速览
> - **身份**：
> - **国别／地区**：
> - **活跃时期**：
> - **主要领域**：
> - **代表贡献**：
> - **相关理论／概念**：

> [!info]- 筛选标准
> - 有独立理论或概念贡献（提出了有名称的理论、概念或框架）。
> - 在领域内有持续影响力（被多篇论文反复引用，或代表一个学派／立场）。
> - 论文专门讨论其思想（以该人物的思想作为主要理论资源并详细介绍）。
>
> 不建条目的情况：只是论文作者但思想未被专门讨论；只被顺带引用一次；只是受访者。

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

## 简介

> [!info]
> 身份、国籍、时代背景、主要活跃领域简述。

---

## 生平与职涯

> [!note]
> 人生轨迹、主要任职、重要活动，按时间顺序：
> - YYYY 出生于／就读于／任职于……
> - YYYY 主要事件或转折点
> - YYYY 逝世（如适用）

> [!note]- 1896–1920 早年与求学
> - 1896 出生于俄罗斯奥尔沙（p.X）
> - 1917 毕业于莫斯科大学法律系（p.X）

> [!note]- 1924–1934 学术生涯
> - 1924 加入莫斯科心理研究所（p.X）
> - 1934 逝世，享年 37 岁（p.X）

---

## 主要著作

> [!abstract]
> APA 格式，附每本著作的核心主张简述：
> - Vygotsky, L. S. (1978). *Mind in society*. Harvard University Press. — 核心主张简述
> - Vygotsky, L. S. (1986). *Thought and language*. MIT Press. — 核心主张简述

---

## 核心思想

> [!tip]
> 主要理论主张，附原文引用。

> [!quote]
> "原文引用"（Vygotsky, year, p.X）

---

## 主要贡献

> [!success]
> 链接到该人物提出或发展的概念／理论：
> - [[最近发展区]] — 一句话说明
> - [[脚手架]] — 一句话说明（含后续发展者）

---

## 思想发展与影响

> [!example]
> 该人物思想的演变，以及对后续学者或理论的影响：
> - 影响了 [[Bruner]] 的发现学习理论

---

## 争议与批评

> [!warning]
> - 批评描述，附来源。（Author, year, p.X）

---

## 来源

- [[Vygotsky_1978_HUP]]
