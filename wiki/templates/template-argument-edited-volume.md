---
title: <% tp.file.title %>
summary: ""
type: argument
subtype: edited-volume-overview
publication_type: edited-volume
authors: []
editors:
  - "[[Editor, E. E.]]"
source_language: en
book_title: ""
publication_place: ""
publisher: ""
year:
doi: ""
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

---

## 编著定位

> [!volume-profile] 编著档案
> - **核心议题** 这本编著围绕什么共同问题、领域、对象或争议组织。
> - **材料边界** 说明本 overview 依据前言、导论、编者说明、目录还是已处理章节。
> - **章节关系** 各章是递进论证、主题分区、案例集合、方法集合、争论集合，还是手册式覆盖。
> - **使用方式** 说明本页用于导航章节 Argument、沉淀全书结构，还是作为某一研究主题的阅读入口。

---

## 编者问题与组织主张

> [!question] 编者问题
> 直接陈述前言、导论或编者说明中的核心问题、选题边界和组织关切。不要只写“本书讨论……”。（p.X）

> [!volume-argument] 编者组织主张
> - **共同问题** 编者如何把不同章节纳入同一个问题框架。（p.X）
> - **组织逻辑** 为什么这些章节按当前顺序、部分或主题组合在一起。（p.X）
> - **整体贡献** 这本编著作为整体改变了什么理解，而不是单章贡献的简单相加。（p.X）

> [!citation-card]- 编者关键表述
> 中文译文或中文原文。（p.X）
>
> *Original text or English translation.*

---

## 全书结构与章节路线

> [!volume-structure] 全书结构
> - **Part I / Ch. X-Y — 部分标题** 说明该部分回应什么子问题、承担什么论证功能、与前后部分如何衔接。（p.X）
> - **Part II / Ch. X-Y — 部分标题** 说明该部分如何推进、对比或转向。（p.X）
> - **Part III / Ch. X-Y — 部分标题** 说明该部分如何收束、扩展或提出实践含义。（p.X）

> [!volume-map]- 结构图
> ![](https://img.mylikemie.icu/books/<book-folder>/figures/Figure_Structure_Map.jpg)

%% 结构图只显示全书组织逻辑，不替代各章概览。无扫描图时可改用 Mermaid flowchart。 %%

---

## 理论、方法与关键词

> [!volume-tools] 理论与方法工具箱
> - **[[<理论名>]] / [[<概念名>]]** 说明该理论或概念在全书中的角色，是共同框架、部分章节工具，还是编者定位语言。（p.X）
> - **[[<方法名>]]** 说明该方法是否为全书共同方法，还是某些章节的材料处理方式。（p.X）
> - **关键词** 列出贯穿全书的关键词，并说明它们如何连接不同章节。

%% 不要把所有相关理论概念塞进这里。只写能解释全书结构或跨章关系的工具。 %%

---

## 跨章主题线索

> [!cross-chapter] 跨章主题线索
> - **主题线索一** 说明哪些章节共同处理同一概念、理论、对象、案例或争议。
>   - **相关章节** Ch. X [[<Argument_章节作者_年份_关键词>]]；Ch. Y [[<Argument_章节作者_年份_关键词>]]。
>   - **阅读价值** 说明为什么应把这些章节放在一起读。
> - **主题线索二** 说明另一条跨章关系。

%% 跨章主题线索用于发现章节之间的横向关系。不要重复目录，不要替代各章概览。 %%

---

## 章节处理路线

> [!chapter-roadmap] 章节处理路线
> - **已处理章节** Ch. X、Ch. Y。说明目前 overview 依据哪些章节已经深入处理。
> - **优先处理章节** Ch. X、Ch. Y。说明优先级理由，例如导论核心章、理论枢纽、方法枢纽、案例代表性或被其他条目频繁引用。
> - **可暂缓章节** Ch. X、Ch. Y。说明暂缓理由，例如重复性高、与当前研究问题关联弱、资料不足。
> - **缺口提醒** 说明目前对全书结构判断还缺哪些章节或材料支撑。

---

## 各章概览

> [!chapter-index] 章节索引
> - **Ch. <X> — <章节标题>** [[<Argument_章节作者_年份_关键词>]] — 一句话说明该章的问题、核心论点和在全书结构中的位置。
> - **Ch. <Y> — <章节标题>** Argument_ChapterAuthor_Year_关键词 — 若尚未建 Argument，保留技术文件名候选并说明待处理。

%% 各章概览只写导航性索引。章节的完整论证结构、方法、发现、引用和局限写入对应章节 Argument。 %%

---

## 整体贡献与使用边界

> [!volume-contribution] 整体贡献
> - **研究议题贡献** 这本编著作为整体如何推进某个研究议题。
> - **理论／方法贡献** 是否提供跨章理论框架、方法谱系、案例集或争议地图。
> - **资料价值** 它适合作为什么类型的来源，例如领域综述、案例入口、理论争论入口、教学阅读清单或政策材料集合。

> [!volume-limits] 使用边界
> - **不能直接代表单章观点** overview 只记录编者组织逻辑，不能替代章节作者的独立论证。
> - **不能当作系统综述** 除非编者明确采用系统综述方法，否则不要把章节集合当成穷尽性证据。
> - **章节异质性** 提醒各章方法、理论、对象或立场可能不同，引用时必须回到具体章节。

---

## 来源

%% 只列论文集 overview source record wikilink。章节 source 写入对应章节 Argument。 %%

- [[books/<book-folder>/Source_Name|Source_Name]]
