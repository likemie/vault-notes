---
title: <% tp.file.title %>
aliases: []
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

> [!info]- 筛选标准
> - 有独立理论或概念贡献（提出了有名称的理论、概念或框架）。
> - 在领域内有持续影响力（被多篇论文反复引用，或代表一个学派／立场）。
> - 论文专门讨论其思想（以该人物的思想作为主要理论资源并详细介绍）。
>
> 不建条目的情况：只是论文作者但思想未被专门讨论；只被顺带引用一次；只是受访者。

> [!info]- Frontmatter 格式规范
> - `tags` — 用方括号列表，内容 tag 建议使用英文小写连字符。
> - 推荐 tag 前缀：`region/`、`field/`、`theory/`、`method/`、`discipline/`、`school/`。
> - `related_*` 和 `sources` — 所有值必须加引号。
> - wikilink 必须包在引号内，否则 Obsidian 无法解析 frontmatter。
> - 单个值也需要引号和方括号：`related_theories: ["[[Social Constructivism]]"]`

> [!info]- Aliases 规则（用于 Automatic Linker 自动补链）
> - `aliases` 用于中英文人名映射，建议包含英文全名、中文译名、常见简称、姓氏常用写法。
> - 文件名／标题可以保持英文；中文正文常用译名应写入 `aliases`。
> - 不要加入过于宽泛的普通词或单个字母。
> - 示例：`Pierre Bourdieu` 的 aliases 可写 `Bourdieu`、`布迪厄`、`皮埃尔·布迪厄`。

> [!warning]- 写入规则（每次写入前必须执行）
> 1. 确定新内容属于哪个 `##` 章节。
> 2. 分点 ≥ 8 条 → 按主题建 `###` 子主题，组内按时间排列。
> 3. 分点 < 8 条 → 直接按时间顺序插入正确位置，禁止追加末尾。
> 4. 写入前声明：「归属章节 > 子主题 > 插入位置」，再用 str_replace 写入。
> 5. 不要编造生平、著作、格言或影响；资料不足时写“未提供”或“待核”。

---

## 简介

> [!info]
> 身份、国籍、时代背景、主要活跃领域简述。重点说明此人在教育学、社会学、哲学或相关领域中的位置。

---

## 生平与职涯

> [!note]
> 人生轨迹、主要任职、重要活动，按时间顺序记录。资料不足时只写与思想形成有关的关键信息，不强行补传记细节。
> - YYYY 出生于／就读于／任职于……
> - YYYY 主要事件或转折点
> - YYYY 逝世（如适用）

---

## 主要著作

> [!abstract]
> APA 格式列出代表性著作，并用一句话概括每本著作的核心内容或理论贡献。没有足够资料时，只列已知著作，不补不存在的信息。

- Author, A. A. (YYYY). *Title*. Publisher. — 一句话概括核心内容。

---

## 核心思想

> [!tip]
> 综合其主要著作和研究脉络，概括最核心的理论主张。不要与“主要著作”简单重复；这里应提炼跨著作、跨时期的稳定思想。

> [!quote]
> "原文引用"（Author, year, p.X）

---

## 思想发展

> [!note]
> 可选模块。只有资料足够时才写。优先按著作或阶段分段说明思想如何延续、转向或深化；资料不足时保留“未提供”或删除本节内容。

### YYYY — *著作名或阶段名*

- 核心内容：
- 思想发展：
- 相关概念／理论：

---

## 影响

> [!success]
> 单独记录此人对后续理论、教育研究、政策话语、研究方法或具体学者的影响。优先写“影响了谁／什么领域／以何种方式”。
> - 影响了 [[理论名]] 在教育研究中的使用。

---

## 格言／关键表述

> [!quote]
> 可选模块。只有能确认出处时才写。记录最能代表该人物思想的短句、格言或高频引用；无法确认原文出处时标注“待核”，不要编造。

> "引用内容"（Author, year, p.X）

---

## 争议与批评

> [!warning]
> - 批评描述，附来源。（Author, year, p.X）

---

## 来源

- [[Source_Name]]
