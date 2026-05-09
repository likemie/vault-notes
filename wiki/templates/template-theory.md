# 模板：理论 Theory

## Frontmatter

```yaml
---
title: <% tp.file.title %>
type: theory
tags: []
# tag 建议：理论名称/学派 + 研究范式 + 学科领域 + 地区/传统
# 示例：[constructivism, paradigm/constructivist, subject/learning-theory, region/europe]
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
> - `tags` — 用方括号列表，使用英文小写连字符；可使用命名空间：`paradigm/`、`subject/`、`region/`、`tradition/`。
> - `related_*` 和 `sources` — 所有值必须加引号。
> - wikilink 必须包在引号内，否则 Obsidian 无法解析 frontmatter。

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

## 核心主张
理论的基本立场，附原文引用。
> "原文引用"（Author, year, p.X）
<!-- 格式：主张后紧跟 blockquote 引用原文。 -->

---

## 核心命题
主要命题或子理论，逐条列出并附来源。

---

## 发展脉络
- YYYY [[人物名]] 提出／发展某一理论主张。（p.X）
<!-- 格式：事件 < 8 条用普通列表；≥ 8 条改用 callout 分期，每个时期一个 callout。 -->

---

## 认识论立场
- 本体论与认识论立场：简述。
- 常用研究方法：[[研究方法名]]。

---

## 争议与批评
- 批评描述，附来源和立场。（Author, year, p.X）

---

## 相关研究
链接到以此理论为框架的论证框架条目：
- [[Argument_来源]] — 一句话说明如何使用此理论。

---

## 应用领域
- [[概念或领域名]] — 一句话说明。

---

## 来源
- [[来源条目名]]
```
