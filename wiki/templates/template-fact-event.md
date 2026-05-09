# 模板：事实／事件 Fact — Event

## Frontmatter

```yaml
---
title: <% tp.file.title %>
type: fact
subtype: event
tags: []
# tag 建议：事件主题 + 地区 + 教育阶段 + 机构/政策领域
# 示例：[international-assessment, region/global, level/k12, org/oecd]
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
> - `tags` — 用方括号列表，使用英文小写连字符；建议使用：`region/`、`level/`、`org/`、`policy/`。
> - `related_*` 和 `sources` — 所有值必须加引号。
> - wikilink 必须包在引号内，否则 Obsidian 无法解析 frontmatter。

**Facts 子文件夹判断规则：**
- 主要发生在某一国／地区 → 放该国文件夹，tag 标注其他相关国家。
- 国际组织主导或全球性（PISA、UNESCO、世界银行等）→ 放 `global/`。
- 涉及两三个特定国家的比较或联合政策 → 放 `multi/`。
- 遇到新国家 → 按需新建子文件夹，文件夹名用小写英文（如 `uk/`、`japan/`）。

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

## 背景
事件发生的背景。

---

## 经过
事件的主要经过，时间顺序呈现。
- YYYY-MM 事件节点。
<!-- 格式：事件 < 8 条用普通列表；≥ 8 条改用 callout 分期，每个阶段一个 callout。 -->

---

## 关键文件／声明
> "原文引用"（来源, year）
<!-- 格式：关键声明用 blockquote 引用原文。 -->

---

## 影响与后果
对政策、学界、实践的影响，附来源。

---

## 争议与评论
- 不同立场的评论，附来源。（Author, year, p.X）

---

## 相关概念／政策
- [[相关概念或政策名]]

---

## 来源
- [[来源条目名]]
```
