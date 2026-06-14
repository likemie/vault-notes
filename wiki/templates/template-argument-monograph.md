---
title: <% tp.file.title %>
authors:
  - "[[Author, A. A.]]"
summary: ""
type: argument
subtype: monograph
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

%% Monograph Argument 是整本专著的论证入口，粒度由用户指定。具体字段、引用、写入和 callout 规则见 TEMPLATE-SPEC.md、CALLOUTS.md 与 schema/schema-monograph.md；正式条目不得保留这些说明注释。 %%

%% TEMPLATE BODY: 生成正式条目时删除所有模板说明注释。 %%
---

## 研究问题

> [!question] 全书问题
> 直接陈述全书要回答的核心问题，综合各章提炼，不以“本书、本章、作者、研究者、论证”等作常规句子主语。

---

## 理论框架

> [!framework-table] 理论框架
> | 理论 / 概念 | 在全书中的作用 |
> |---|---|
> | [[理论名]] | 一句话说明如何贯穿全书运用。（p.X） |

---

## 研究方法

> [!method-panel] 研究方法
> | 环节 | 说明 |
> |---|---|
> | 方法 | [[研究方法名]] |
> | 样本 | 描述。（p.X） |
> | 数据来源 | 描述。（p.X） |

---

## 论证结构

> [!argument-map] 全书论证路径
> 综合各章要点，详细拆解整体论证脉络。每一个论证步骤独立成段，步骤之间使用分割线。抽象处加入例子。

1. 问题起点：全书从什么经验、理论或政策问题出发。

---

2. 理论／概念工具：哪些概念组织全书解释。

---

3. 关键前提：作者依赖什么历史、制度、方法或价值判断。

---

4. 证据支撑：哪些章节或材料提供主要证据。

---

5. 中间推论：从证据到结论之间有哪些推理步骤。

---

6. 结论：全书最终改变了什么理解。

---

7. 可疑跳跃：只记录原书论证中需要谨慎处理的跳跃或边界，不写外部批评。

---

## 各章概览

### 第X章 章节标题

> [!chapter-question]

说明该章要回答的问题，或它在全书论证中的位置。

#### 论证链条

按前提、证据、中间推论、结论拆解章节论证。每一个论证步骤独立成段，步骤之间使用分割线。

---

## 主要发现

> [!finding-cards] 主要发现
> 综合各章提炼的核心发现，附页码来源。
> - **发现一**：发现描述。（p.X）
> - **发现二**：发现描述。（p.X）

> [!stat-cards]- 核心数据
> 有具体数字、样本量、效应量或比例时，单独放在这里。（p.X）

---

## 关键引用

> [!citation-card] 关键引用
> 中文译文。（第X章，p.X）
> Original/English: Original text or English translation.

---

## 自述局限

> [!warning]
> 只写书中明确自述的局限、边界条件或未来研究方向，并附页码。不要补写外部批评或原书没有说明的缺陷。

---

## 来源

%% 只列整本书 source record wikilink。 %%

- [[Source_Name]]
