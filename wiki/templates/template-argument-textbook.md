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

---

## 总览

%% 用一段话说明教材对象、读者、课程用途和全书主线。 %%

> [!textbook-overview] 章节总览
> | 章节 | 内容概要 | 主要关联条目 |
> |---|---|---|
> | [[Argument_BookFolder_Ch01\|第1章 <章节标题>]] | 用一两句话说明这一章主要讲什么。 | [[<概念名>]]、[[<方法名>]]、[[<理论名>]] |
> | 第<X>章 <章节标题> | 若不分章节建页，保留普通章节名即可。 | [[<概念名>]]、[[<方法名>]]、[[<理论名>]] |

> [!knowledge-map]- 知识路线图
> ![](https://img.mylikemie.icu/books/<book-folder>/figures/Figure_Knowledge_Map.jpg)

---

## 章节

### 第<X>章 <章节标题>

#### 概念地图

> [!knowledge-map]- 第X章：概念地图
> ![](https://img.mylikemie.icu/books/<book-folder>/figures/Figure_X-X_Concept_Map.jpg)

#### 章节内容

%% 按教材自身思路整理，不强行套固定小标题。可以使用普通段落，也可以综合使用 abstract、info、note、example、tip、warning、quote 等 callout。 %%

本章首先说明……

> [!abstract] 核心结构
> - **知识点一**：说明教材如何引入、定义或区分它。
> - **知识点二**：说明它与上一知识点的关系。
> - **知识点三**：说明它如何转化为方法、案例或练习。

> [!example]- 图X-X：图名或案例名
> ![](https://img.mylikemie.icu/books/<book-folder>/figures/Figure_X-X_Descriptive_Name.jpg)

%% <book-folder> 与 sources/ 下的教材文件夹名一致。案例或练习无图时，删除图片行，改为说明文字或链接到对应条目。 %%

#### 关键引用

> [!citation-card]- 关键引用
> 中文译文或中文原文。（第X章，p.X）
>
> *Original text or English translation.*

---

## 来源

%% 只列教材 source record wikilink。 %%

- [[Source_Name]]
