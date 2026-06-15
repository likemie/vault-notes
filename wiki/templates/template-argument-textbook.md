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

%% Textbook Argument 记录教材的知识推进结构、学习路径和章节知识索引。具体定义、分类、方法步骤、理论说明和案例优先沉淀到对应 wiki 条目；正式条目必须删除所有模板说明注释。 %%

---

## 教材定位

> [!textbook-profile] 教材档案
> - **学习对象**：教材面向什么读者、课程、能力层级或学科领域。
> - **知识范围**：教材覆盖哪些核心主题、方法、理论或实践任务。
> - **组织方式**：教材按概念递进、研究流程、方法类型、历史发展、问题任务还是案例场景组织。
> - **处理粒度**：`single-argument` 或 `chapter-arguments`。说明章节细节累积在本页，还是另建章节 Argument。

---

## 学习路径

> [!learning-path] 全书学习路径
> - **起点模块**：读者需要先理解什么背景、术语、问题意识或基础框架。
> - **核心模块**：教材中最重要的概念、理论、方法、步骤或分类体系是什么。
> - **应用模块**：教材如何把知识转化为研究设计、分析步骤、写作任务、案例判断或实践操作。
> - **收束模块**：教材最终希望读者掌握什么能力，或能独立完成什么任务。

> [!knowledge-map]- 知识路线图
> ```mermaid
> flowchart LR
>   A["入门概念"] --> B["核心框架"]
>   B --> C["方法/步骤"]
>   C --> D["案例/图表"]
>   D --> E["应用任务"]
> ```

---

## 章节路线

> [!textbook-chapter-map] 章节路线
> - **第X章 — 章节标题**：说明这一章主要引入什么知识块、服务哪个学习目标、连接哪些核心条目。
> - **第Y章 — 章节标题**：说明这一章如何推进前一章，或转向新的知识模块。

> [!chapter-index] 章节索引
> - **第X章 — 章节标题**：[[Argument_BookFolder_ChXX]] — 若采用 chapter-arguments，链接章节 Argument；若采用 single-argument，用一句话说明该章知识功能。

%% 教材 overview 不默认使用大表格。只有课程大纲、章节很多且信息非常规则时，才把章节路线降级为三列表格。 %%

---

## 章节概览

### 第X章 章节标题

> [!chapter-learning] 本章学习目标
> - **本章位置**：说明本章在全书学习路径中的作用。
> - **核心问题**：本章帮助读者回答什么问题。
> - **应掌握内容**：本章结束后应掌握哪些概念、方法、分类、步骤或判断标准。

> [!knowledge-index] 本章知识索引
> - **Concept**：[[Concept]] — 本章如何定义、区分或使用该概念。
> - **Theory**：[[Theory]] — 该理论在本章中承担什么解释或组织作用。
> - **Method**：[[Method]] — 本章介绍什么操作步骤、研究设计或分析程序。
> - **Fact / Person**：[[Fact]] / [[Person]] — 本章用作案例、背景或思想来源。

> [!learning-sequence] 本章知识推进
> - **1. 引入**：教材如何引出本章主题，是否从问题、案例、图表、定义或任务开始。
> - **2. 定义／分类**：本章如何界定核心术语、区分类型或建立框架。
> - **3. 方法／步骤**：本章是否提供操作流程、写作脚本、分析步骤或判断标准。
> - **4. 例子／图表**：哪些例子、表格、图或练习最能帮助理解。
> - **5. 小结／迁移**：本章如何连接下一章，或如何迁移到实际研究/学习任务。

> [!textbook-artifact]- 图表、模板或练习
> - **图/表/模板名称**：说明它教会读者什么，是否需要沉淀到 Concept / Method / Fact 条目。（第X章，p.X）

%% 章节概览只记录教材如何推进知识。定义、分类、方法步骤、争议和案例细节应写入对应 wiki 条目。 %%

---

## 跨章知识结构

> [!textbook-synthesis] 跨章知识结构
> - **概念线索**：哪些概念跨章节反复出现，含义是否发生扩展。
> - **方法线索**：哪些方法或步骤在不同章节中逐步展开。
> - **比较线索**：教材如何比较不同理论、方法、路径、案例或范式。
> - **学习难点**：读者最容易混淆、误用或跳过的知识点。

---

## 重要摘录

> [!textbook-extract] 重要摘录
> 只保留有启发、表述精炼或可作为条目定义来源的观点。标注章节与页码；没有页码时只标注章节，不编造页码。
>
> 中文译文或中文原文。（第X章，p.X）
>
> Original text or English translation.

---

## 使用边界

> [!textbook-limits] 使用边界
> - **教材定位边界**：教材是入门、进阶、手册、课程用书还是方法指南；不要把入门概述当作完整研究综述。
> - **知识更新边界**：说明哪些方法、统计规则、软件工具、政策或领域状态可能已经更新。
> - **条目沉淀提醒**：本页只作教材路径和章节索引；稳定知识写入 Concept / Theory / Method / Fact / Person。

---

## 来源

%% 只列教材 source record wikilink。 %%

- [[Source_Name]]
