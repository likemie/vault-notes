# 模板：论证框架 Argument — 专著整体

此模板用于专著的整体 Argument（`Argument_作者姓_年份_出版社.md`）。各章提取的 wiki 条目正常写入 wiki/，本文件综合各章要点建立全书论证框架。

---

## 文件命名

`Argument_作者姓_年份_出版社.md`
例：`Argument_Vygotsky_1978_HUP.md`

---

## Frontmatter

```yaml
---
title: <% tp.file.title %>
type: argument
subtype: monograph
citation: ""
tags: []
# tag 建议：主题 tag + 理论 tag + 方法 tag + 教育阶段 tag + 地区 tag + 文献类型 tag
# 示例：[learning-theory, constructivism, level/k12, region/russia, source/monograph]
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
sources: []
part_of:
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---
```

> **Frontmatter 格式规范：**
> - `subtype: monograph` 用于与普通论文 Argument 及论文集 Argument 区分。
> - `tags` — 用方括号列表，所有内容 tag 使用英文小写连字符；可用 `source/monograph` 标注来源类型。
> - `related_*` 和 `sources` — 所有值必须加引号。
> - wikilink 必须包在引号内，否则 Obsidian 无法解析 frontmatter。

---

## 写入规则（每次写入前必须执行）

> ⚠️
> 1. 确定新内容属于哪个 `##` 章节。
> 2. 分点 ≥ 8 条 → 按主题建 `###` 子主题，组内按时间排列。
> 3. 分点 < 8 条 → 直接按时间顺序插入正确位置，禁止追加末尾。
> 4. 写入前声明：「归属章节 > 子主题 > 插入位置」，再用 str_replace 写入。

**论证拆解要求（强制执行）：**
- **逐步拆解，不跳跃** — 论证结构须完整还原每一个推论步骤，不得跳过中间环节直接给结论。
- **用易懂的语言** — 避免堆砌学术术语；术语首次出现须加括号解释。
- **抽象主张必须附例子** — 凡涉及抽象论证步骤，须紧跟一个具体例子说明。
- **例子优先来自论文** — 使用书中案例或数据，附页码；书中无例子时可用教育情境类比，但须注明「编者类比」。

---

## 页面结构

```markdown
# <% tp.file.title %>

## 研究问题
全书试图回答的核心问题，综合各章提炼。

---

## 理论框架
- [[理论名]] — 如何贯穿全书运用。

---

## 研究方法
- 方法：[[研究方法名]]
- 样本：描述。
- 数据来源：描述。

---

## 论证结构
全书整体论证脉络，综合各章要点：
1. 前提／观察：
2. 论证步骤：
3. 结论：

---

## 各章概览
每章处理完后直接追加，格式自由，忠实记录该章论点、论据、关键引用：

### 第X章 章节标题
本章主要论点、论据与关键引用的自由记录。
<!-- 不套模板，能记多详细记多详细，供最后整合用。 -->

---

## 主要发现
综合各章提炼的核心发现，附页码来源。
- 发现描述。（p.X）
<!-- 格式：有具体数字或效应量的关键数据用 info callout 高亮。 -->

---

## 关键引用
> "引用内容"（p.X）
<!-- 格式：用 blockquote 引用原文，保留最能代表全书立场的 1-2 条。 -->

---

## 局限性与批评
作者自身承认的局限，或他人对全书的批评。

---

## 来源
- [[来源条目名]]
```
