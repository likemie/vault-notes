# 模板：概念 Concept

## Frontmatter

```yaml
---
title: <% tp.file.title %>
type: concept
tags: []
# tag 建议：概念主题 + 学科领域 + 教育阶段 + 地区/语境
# 示例：[educational-equity, subject/sociology-of-education, level/higher-education, region/china]
related_concepts: []
related_theories: []
related_persons: []
related_methods: []
related_facts: []
sources: []
confidence: medium
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---
```

> **Frontmatter 格式规范：**
> - `tags` — 用方括号列表，使用英文小写连字符；可使用命名空间：`subject/`、`level/`、`region/`、`theory/`、`policy/`。
> - `related_*` 和 `sources` — 所有值必须加引号：`related_theories: ["[[建构主义]]", "[[情境学习]]"]`。
> - wikilink 必须包在引号内，否则 Obsidian 无法解析 frontmatter。
> - 单个值也需要引号和方括号：`related_concepts: ["[[项目式学习]]"]`。

---

## 写入规则（每次写入前必须执行）

> ⚠️
> 1. 确定新内容属于哪个 `##` 章节。
> 2. 分点 ≥ 8 条 → 按主题建 `###` 子主题，组内按时间排列。
> 3. 分点 < 8 条 → 直接按时间顺序插入正确位置，禁止追加末尾。
> 4. 写入前声明：「归属章节 > 子主题 > 插入位置」，再用 str_replace 写入。

---

## 页面结构

```markdown
# <% tp.file.title %>

## 定义
核心定义，附原文引用。
> "原文引用"（Author, year, p.X）
<!-- 格式：定义后紧跟 blockquote 引用原文，引用块用 > 开头。 -->

---

## 概念辨析
辨析容易混淆的概念，附来源。
- vs [[概念名]] — 区别说明。

---

## 概念演变
概念的起源与发展脉络，关键节点附来源。
<!-- 格式：事件 < 8 条用普通列表；≥ 8 条改用 callout 分期，每个时期一个 callout。 -->

---

## 核心要素
构成要素逐条列出，每条附来源。

---

## 理论基础
- [[理论名]] — 一句话说明关系。

---

## 实证发现
有数据或明确结论支撑的发现，每条注明来源与适用条件：
- 发现描述，适用条件（学段、地区、样本）。（Author, year, p.X）
<!-- 格式：有具体数字或效应量的关键数据，用 info callout 单独高亮。 -->

---

## 争议与批评
- 批评描述，附来源和立场。（Author, year, p.X）

---

## 相关案例／政策
- [[政策或案例名]]

---

## 来源
- [[来源条目名]]
```
