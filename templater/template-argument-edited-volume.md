---
title: <% tp.file.title %>
authors:
  - ""
summary: ""
type: argument
subtype: edited-volume
publication_type: book
book_title: ""
editors: []
publisher: ""
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

%% 正文按编者论点、全书结构和章节关系组织；各章概览按章节顺序追加。用 callout 区分核心问题、结构、理论框架和章节案例。 %%

---

## 编者论点

> [!question]
> 前言中编者提出的核心问题或立场，附原文引用。

> [!quote]
> "原文引用"（p.X）

---

## 全书结构

> [!abstract]
> 编者对各章的分组逻辑与组织框架，说明全书如何回应编者论点。

---

## 理论框架

> [!tip]
> 全书共用的理论视角或分析框架（如有），附来源。
> - [[理论名]] — 一句话说明在全书中的角色

---

## 各章概览

每章处理完后用 str_replace 逐条追加：

> [!example]
> - [[Argument_ChapterAuthor_Year_关键词]] — 该章核心贡献简述（可多句，涵盖主要论点与发现）

---

## 来源

%% 只列 source wikilink；按来源年份从早到晚排序，同一年按作者或机构字母顺序。 %%

- [[Author(Ed.)_Year_Publisher]]
