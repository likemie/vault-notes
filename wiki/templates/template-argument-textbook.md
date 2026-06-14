---
title: <% tp.file.title %>
authors:
  - "[[Author, A. A.]]"
summary: ""
type: argument
subtype: textbook
publication_type: book
book_title: ""
publisher: ""
year:
doi: ""
isbn: ""
citation_aliases: []
citation: ""
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
sources: []
part_of:
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

%% BEFORE USE:
1. Read wiki/templates/TEMPLATE-SPEC.md.
2. Read wiki/templates/CALLOUTS.md.
3. Then use this template.
%%

%% Textbook Argument 记录教材的知识推进结构，具体定义、分类、方法步骤、理论说明和案例优先沉淀到对应 wiki 条目。具体字段、引用、写入和 callout 规则见 TEMPLATE-SPEC.md、CALLOUTS.md 与 schema/schema-textbook.md；正式条目不得保留这些说明注释。 %%

%% TEMPLATE BODY: 生成正式条目时删除所有模板说明注释。 %%
---

## 章节结构

> [!ref-table] 章节结构
> | 章节 | 内容概要 | 主要关联条目 |
> |---|---|---|
> | 第X章 章节标题 | 用一两句话说明这一章主要讲什么。 | Concept A、Theory B、Fact C |

---

## 章节概览

### 第X章 章节标题

> [!chapter-question]
> 一句话说明本章在教材知识推进中的位置，以及本章引入的核心概念或方法。

#### 概览

跟随教材自身逻辑，记录知识如何展开。已建条目只简单提及，详细内容写入具体条目。

> [!ref-table]- 本章知识索引
> | 类型 | 条目 | 本章作用 |
> |---|---|---|
> | Concept | [[Concept A]] | 一句话说明本章如何定义或使用该概念。 |
> | Theory | [[Theory B]] | 一句话说明该理论在本章中的作用。 |

> [!citation-card]- 重要图表或摘录
> 中文译文或图表说明。（第X章，p.X）
> Original/English: Original text or English translation.

---

## 重要摘录

> [!citation-card] 重要摘录
> 中文译文或中文原文。（第X章，p.X）
> Original/English: Original text or English translation.

---

## 来源

%% 只列教材 source record wikilink。 %%

- [[Source_Name]]
