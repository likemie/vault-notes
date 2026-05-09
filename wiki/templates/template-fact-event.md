---
title: <% tp.file.title %>
type: fact
subtype: event
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

> [!abstract] 事件速览
> - **事件类型**：
> - **发生时间**：
> - **发生地区**：
> - **涉及机构／人物**：
> - **相关政策／概念**：
> - **主要影响**：

> [!info]- Facts 子文件夹判断规则
> - 主要发生在某一国／地区 → 放该国文件夹，tag 标注其他相关国家。
> - 国际组织主导或全球性（PISA、UNESCO、世界银行等）→ 放 `global/`。
> - 涉及两三个特定国家的比较或联合政策 → 放 `multi/`。
> - 遇到新国家 → 按需新建子文件夹，文件夹名用小写英文（如 `uk/`、`japan/`）。

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

## 背景

> [!info]
> 事件发生的背景。

---

## 经过

> [!note]
> 事件的主要经过，时间顺序呈现。
> - YYYY-MM 事件节点

> [!note]- 2012 数据发布阶段
> - 2012-12 PISA 成绩公布，多国哗然（p.X）
> - 2013-01 各国政府相继召开紧急教育峰会（p.X）

---

## 关键文件／声明

> [!quote]
> "原文引用"（来源, year）

---

## 影响与后果

> [!success]
> 对政策、学界、实践的影响，附来源。

---

## 争议与评论

> [!warning]
> - 不同立场的评论，附来源。（Author, year, p.X）

---

## 相关概念／政策

> [!example]
> - [[国际比较评估]]

---

## 来源

- [[OECD_2012_Report]]
