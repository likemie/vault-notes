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

%% Textbook Argument 是教材总览和章节整理页。总览页保留章节表格与知识地图；各章按“概念地图 → 章节内容 → 关键引用”整理。具体定义、分类、方法步骤、理论说明和案例优先沉淀到对应 wiki 条目；正式条目必须删除所有模板说明注释。 %%

---

## 总览

%% 用一段话说明教材对象、读者、课程用途和全书主线。 %%

> [!textbook-overview] 章节总览
> | 章节 | 内容概要 | 主要关联条目 |
> |---|---|---|
> | [[Argument_BookFolder_Ch01\|第1章 章节标题]] | 用一两句话说明这一章主要讲什么。 | [[Concept]]、[[Method]]、[[Theory]] |
> | 第X章 章节标题 | 若不分章节建页，保留普通章节名即可。 | [[Concept]]、[[Method]]、[[Theory]] |

> [!knowledge-map]- 知识路线图
> 通常先占位。等章节处理较完整后，再把全书知识推进关系画出来。
>
> ```mermaid
> flowchart LR
>   A["起点"] --> B["核心概念"]
>   B --> C["方法/框架"]
>   C --> D["案例/练习"]
>   D --> E["综合应用"]
> ```

---

## 章节

### 第X章 章节标题

#### 概念地图

> [!knowledge-map]- 第X章概念地图
> 通常先占位。可以放章节概念图、Mermaid、图片链接，或列出待绘制的概念关系。

#### 章节内容

%% 按教材自身思路整理，不强行套固定小标题。可以使用普通段落，也可以综合使用 abstract、info、note、example、tip、warning、quote 等 callout。 %%

本章首先说明……

> [!abstract] 核心结构
> - **知识点一**：说明教材如何引入、定义或区分它。
> - **知识点二**：说明它与上一知识点的关系。
> - **知识点三**：说明它如何转化为方法、案例或练习。

> [!example]- 图表、案例或练习
> 说明这个图表/案例/练习在本章中教会读者什么。必要时附图或链接到对应条目。

#### 关键引用

> [!citation-card]
> 中文译文或中文原文。（第X章，p.X）
>
> Original text or English translation.

---

## 来源

%% 只列教材 source record wikilink。 %%

- [[Source_Name]]
