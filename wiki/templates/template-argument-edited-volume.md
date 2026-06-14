---
title: <% tp.file.title %>
summary: ""
type: argument
subtype: edited-volume-overview
publication_type: edited-volume
authors: []
editors:
  - "[[Editor, E. E.]]"
book_title: ""
publisher: ""
isbn: ""
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

%% Edited volume overview 是论文集结构入口，记录编者论点、全书结构和已处理章节关系。具体字段、引用、写入和 callout 规则见 TEMPLATE-SPEC.md、CALLOUTS.md 与 schema/schema-edited-volume.md；正式条目不得保留这些说明注释。 %%

%% TEMPLATE BODY: 生成正式条目时删除所有模板说明注释。 %%
---

## 编者论点

> [!question] 编者问题
> 前言、导论或编者说明中的核心问题、选题边界和组织立场，附页码。

> [!claim] 编者组织主张
> 用一两句话说明编者如何把各章放进同一个问题框架。

> [!citation-card]- 编者关键表述
> 中文译文或中文原文。（p.X）
> Original text or English translation.

---

## 全书结构

> [!framework-table] 全书结构
> 编者对各章的分组逻辑与组织框架，说明全书如何回应编者论点。
> | 部分 / 章节组 | 组织逻辑 |
> |---|---|
> | Part I / Ch. X–Y | 一句话说明该部分如何回应编者论点。（p.X） |
> | Part II / Ch. X–Y | 一句话说明该部分与上一部分的推进关系。（p.X） |

---

## 理论框架

> [!framework-table] 理论框架
> 全书共用的理论视角或分析框架（如有），附来源。
> | 理论 / 概念 | 在全书中的角色 |
> |---|---|
> | [[理论名]] | 一句话说明在全书中的角色。（p.X） |

---

## 各章概览

> [!evidence-grid-a] 章节索引
> - [[Argument_ChapterAuthor_Year_关键词]] — 一句话说明该章的问题、核心论点和在全书结构中的位置。

---

## 来源

%% 只列论文集 overview source record wikilink。 %%

- [[Source_Name]]
