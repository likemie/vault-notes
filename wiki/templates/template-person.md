# 模板：人物 Person

## Frontmatter

```yaml
---
title: <% tp.file.title %>
type: person
tags: []
# tag 建议：人物姓名/学派 + 研究范式 + 地区 + 领域
# 示例：[vygotsky, paradigm/constructivist, region/russia, subject/learning-theory]
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
sources: []
confidence: medium
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---
```

> **Frontmatter 格式规范：**
> - `tags` — 用方括号列表，使用英文小写连字符；人物姓名 tag 推荐使用常见英文姓氏或全名小写连字符。
> - `related_*` 和 `sources` — 所有值必须加引号。
> - wikilink 必须包在引号内，否则 Obsidian 无法解析 frontmatter。

**筛选标准（不是每个作者都建条目）：**
- 有独立理论或概念贡献（提出了有名称的理论、概念或框架）。
- 在领域内有持续影响力（被多篇论文反复引用，或代表一个学派／立场）。
- 论文专门讨论其思想（以该人物的思想作为主要理论资源并详细介绍）。

不建条目的情况：只是论文作者但思想未被专门讨论；只被顺带引用一次；只是受访者。

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

## 简介
身份、国籍、时代背景、主要活跃领域简述。

---

## 生平与职涯
人生轨迹、主要任职、重要活动，按时间顺序：
- YYYY 出生于／就读于／任职于……
- YYYY 主要事件或转折点。
<!-- 格式：事件 < 8 条用普通列表；≥ 8 条改用 callout 分期，按人生阶段归组。 -->

---

## 主要著作
APA 格式，附每本著作的核心主张简述：
- Author, A. A. (Year). *Title*. Publisher. — 核心主张简述。

---

## 核心思想
主要理论主张，附原文引用。
> "原文引用"（Author, year, p.X）
<!-- 格式：核心主张后紧跟 blockquote 引用原文。 -->

---

## 主要贡献
链接到该人物提出或发展的概念／理论：
- [[概念或理论名]] — 一句话说明。

---

## 思想发展与影响
该人物思想的演变，以及对后续学者或理论的影响：
- 影响了 [[人物或理论名]]。

---

## 争议与批评
- 批评描述，附来源。（Author, year, p.X）

---

## 来源
- [[来源条目名]]
```
