---
title: <% tp.file.title %>
type: fact
subtype: policy
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

> [!abstract] 政策速览
> - **政策类型**：
> - **颁布时间**：
> - **实施地区**：
> - **负责机构**：
> - **涉及学段／领域**：
> - **核心目标**：
> - **相关概念／理论**：

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
> 政策出台的社会、教育背景。

---

## 政策文本摘要

> [!abstract]
> 核心条款与目标，附原文引用。

> [!quote]
> "原文引用"（文件名, year, p.X）

---

## 时间线

> [!note]
> - YYYY 政策提出／讨论
> - YYYY 正式颁布
> - YYYY 开始实施
> - YYYY 修订或评估

> [!note]- 2014–2016 研制阶段
> - 2014 启动课程改革讨论（p.X）
> - 2016 正式颁布新课程纲要（p.X）

---

## 实施情况

> [!example]
> 涉及哪些机构、学段、学科，如何落地。

---

## 效果与评价

> [!success]
> 有据可查的结果，附来源。（Author, year, p.X）

> [!info]- 核心数据
> 实施后学生跨学科项目参与率从 12% 升至 67%（Author, year, p.X）

---

## 争议与评论

> [!warning]
> - 支持或批评立场，附来源。（Author, year, p.X）

---

## 相关概念／理论

> [!tip]
> - [[项目式学习]]
> - [[建构主义]]

---

## 来源

- [[Finnish_curriculum_2016_Report]]
