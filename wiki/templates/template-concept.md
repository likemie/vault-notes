---
title: <% tp.file.title %>
aliases: []
summary: ""
type: concept
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
confidence: medium
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

%% Concept 页写概念、术语、机制、分类或分析对象。具体字段、引用、写入和 callout 规则见 TEMPLATE-SPEC.md 与 CALLOUTS.md；正式条目不得保留这些说明注释。 %%

%% TEMPLATE BODY: 生成正式条目时删除所有模板说明注释。 %%

---

## 定义

> [!def] 核心定义
> 用一段话说明概念的核心含义、适用范围和边界，附 Argument citation。

> [!concept-lens] 概念透镜
> - **含义**：这个概念指向什么对象、关系或机制。
> - **用途**：它帮助研究者看见什么问题。
> - **边界**：它不适合解释什么，或容易与什么概念混淆。

> [!boundary]- 概念边界
> 说明本概念不等于什么、不适用于什么。
> - 不等于 [[相近概念]] — 区别说明。
> - 不适用于 — 适用范围限制说明。

---

## 概念辨析

> [!contrast-table] 概念辨析
> | 维度 | 本概念 | [[相近概念 A]] | [[相近概念 B]] |
> |------|--------|----------------|----------------|
> | 分析对象 | 说明 | 说明 | 说明 |
> | 核心机制 | 说明 | 说明 | 说明 |
> | 适用范围 | 说明 | 说明 | 说明 |

---

## 核心命题

> [!claim] 核心命题总览
> 用一两句话说明各命题的内在逻辑，例如"命题 A 确立机制 → 命题 B 说明条件 → 命题 C 延伸至空间尺度"。

> [!logic-map] 命题关系
> 
> ```mermaid
> flowchart LR
>     B(["条件/前提"]) -. 使得 .-> A["① 命题一"]
>     A -- 关系标签 --> C["② 命题三"]
>     C -- 关系标签 --> D["③ 命题五"]
>     A -- 关系标签 --> E["④ 命题七"]
>     E -- 关系标签 --> F["⑤ 命题九"]
> ```

> [!claim] 命题一（英文名）
> 命题内容说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!warrant]- 命题一的支撑理由
> 说明该命题依赖什么理论前提、经验材料或分类标准。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

> [!claim] 命题二（英文名）
> 命题内容说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!implication]- 命题后果
> - **解释后果**：该命题改变了什么解释路径。
> - **应用后果**：该命题适合用于哪些研究对象或案例。

---

## 概念演变

> [!timeline] 概念演变
> - **YYYY–YYYY** 起源阶段：关键节点、代表人物或重要文本。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **YYYY** 关键转向：概念内涵或适用范围发生重要变化。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **YYYY** 扩展阶段：概念被引入新领域或衍生出新分支。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 理论语境

> [!logic-map] 理论归属
> - [[理论 A]] — 本概念如何源自或扩展该理论。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - [[理论 B]] ←→ 本概念 — 对话或张力关系说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - [[研究传统 C]] — 本概念在该传统中的位置。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!warrant]- 理论位置说明
> 说明为什么这个概念应归入这些理论传统，而不是只列相关理论名称。

---

## 实证发现

> [!stat-cards]-
> - **数字或比例**
>   简短说明适用条件。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!finding-cards]
> 1. 发现描述，说明适用条件（学段、地区、样本或研究设计）。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 争议与批评

> [!tension] 核心争议
> 争议焦点说明——各方立场不是孰对孰错，而是理论路径差异。
> - **立场 A** — 观点说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **立场 B** — 观点说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!warning] 方法论批评与适用局限
> - 批评描述，说明批评对象和立场。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!critique-method] 方法论批评标题
> - 具体方法论问题描述。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!critique-logic] 逻辑/概念批评标题
> - 概念矛盾或推论跳跃的具体描述。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!critique-data] 实证批评标题
> - 与主张相悖的数据或研究描述。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!critique-fatal] 根本性缺陷标题
> - 无法修补的根本性问题描述。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 应用案例

> [!case] 案例 A
> - [[案例或研究]] — 说明该案例如何体现或应用这一概念。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!case] 案例 B
> - [[案例或研究]] — 说明该案例如何体现或应用这一概念。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!implication]- 可迁移性
> - **可迁移条件**：这个概念可以迁移到哪些相似情境。
> - **不可迁移边界**：哪些情境中使用它会造成误读。
