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

%% 论文集 overview 是结构入口，记录编者论点、全书结构和已处理章节关系；可引用文献以各章 Argument 为主。overview 不进入 citation 索引。 %%

>
> [!info]- Overview 规则
> - `title` 保持与文件名一致，使用稳定技术命名。
> - `editors` 使用 Person wikilink，每位编者单独一项。
> - `citation` 写整本论文集的 APA 完整引用，用于 source record。
> - overview 不填写 `citation_aliases`，不进入 `citation_full.json`。
> - 各章使用普通 Argument 模板，按章节作者和年份生成 citation 字段。
> - 正文引用当前 overview 对应材料时只写页码，如（p.12）或（pp.12–15）。
> - 正文引用其他已处理文献使用 APA 短引用，如 `(Ball, 2008a, p. 12)` 或 `Ball (2008a, p. 12)`。

> [!info]- Summary 规则
> `summary` 用一句话说明论文集的组织问题、编者立场和全书结构，不写成图书简介。

> [!warning]- 表达规则
> - 句子不要中英混合；除专名、引文、公式、代码、APA citation 和无法翻译的固定术语外，句子主体使用中文表达。
> - 人名第一次出现必须使用全名；中文正文优先写成中文全名（英文全名），后文再出现可按语境使用中文名、姓氏或代称。
> - 缩写第一次出现必须写成中文（英文全称，缩写）；后文才可单独使用缩写。

%% CONTENT_START: 以上为写作参考，以下为实际条目内容 %%
---

## 编者论点

> [!question]
> 前言、导论或编者说明中的核心问题与组织立场，附页码。

> [!quote]
> 中文译文或中文原文。（p.X）
> Original/English: Original text or English translation.

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

> [!example]
> - [[Argument_ChapterAuthor_Year_关键词]] — 该章核心贡献简述，涵盖主要论点、证据和发现。

---

## 来源

%% 只列论文集 overview source record wikilink。 %%

- [[Source_Name]]
