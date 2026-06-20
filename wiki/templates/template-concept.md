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

---

## 定义

> [!def] 核心定义
> 用一段话说明概念的核心含义、适用范围和边界，附 Argument citation。

> [!concept-lens] 概念透镜
> - **含义** 这个概念指向什么对象、关系或机制。
> - **用途** 它帮助研究者看见什么问题。
> - **边界** 它不适合解释什么，或容易与什么概念混淆。

> [!citation-card]- 关键表述
> 中文译文或中文原文。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
>
> *Original text or English translation.*

> [!boundary]- 概念边界
> - 不等于 [[相近概念]] — 区别说明。
> - 不适用于 — 适用范围限制说明。

---

## 概念辨析

%% 没有相近概念时可删除本节。可换用 [!tension-table]（强调立场差异）或 [!prop-table]（逐项比较属性）。 %%

> [!contrast-table] 概念辨析
> | 维度 | 本概念 | [[相近概念 A]] | [[相近概念 B]] |
> |------|--------|----------------|----------------|
> | 分析对象 | 说明 | 说明 | 说明 |
> | 核心机制 | 说明 | 说明 | 说明 |
> | 适用范围 | 说明 | 说明 | 说明 |

---

## 核心要素

%% 可综合使用 [!feature]、[!logic-map]、[!taxonomy]、[!frames-ref]、[!ref-table]、[!entry-map] 等。 %%

> [!feature] 核心要素
> - **要素一**：说明该要素在概念中的位置、功能或判断标准。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **要素二**：说明该要素与其他要素的关系。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **要素三**：说明该要素的边界、条件或典型表现。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart LR
>     A["要素一"]
>     B["要素二"]
>     C["要素三"]
>     D["概念整体"]
>     A --> D
>     B --> D
>     C --> D
> ```

---

## 围绕概念形成的命题

> [!claim] 命题总览
> 用一两句话说明围绕该概念形成了哪些可争辩命题，以及这些命题如何相互连接。

> [!logic-map]- 命题关系
>
> ```mermaid
> flowchart LR
>     B(["条件/前提"]) -. 使得 .-> A["① 命题一"]
>     A -- 关系标签 --> C["② 命题二"]
>     C -- 关系标签 --> D["③ 命题三"]
>     A -- 关系标签 --> E["④ 命题四"]
>     E -- 关系标签 --> F["⑤ 命题五"]
> ```

---

> [!claim] 命题一（英文名）
> 命题内容说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!warrant]- 命题一的支撑理由
> 说明该命题依赖什么理论前提、经验材料或分类标准。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!exegesis]- 教育研究例子
> 用一个具体教育情境说明这条命题如何工作。

---

> [!claim] 命题二（英文名）
> 命题内容说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!implication]- 命题后果
> - **解释后果**：该命题改变了什么解释路径。
> - **应用后果**：该命题适合用于哪些研究对象或案例。

---

## 概念演变

> [!dev-timeline] 概念演变
> - **YYYY — 起源阶段**：提出关键问题、概念或理论命题。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **YYYY–YYYY — 扩展阶段**：概念内涵或适用范围发生重要变化，或被引入新领域。
> - **YYYY — 教育研究应用**：说明该概念如何进入教育研究或政策讨论。

---

## 争议与批评

%% 三类内容分开记录，不要混用。
   - 多方学者争论 → [!debates]（立场 P1/P2/P3，无明确对错）
   - 两方直接对立 → [!tension]（蓝/红双栏，有 VS 感）
   - 外部指出缺陷 → [!critique] 系列
   - 作者自述局限 → [!warning]
   没有充分材料时可删除对应 callout。 %%

> [!debates] 学术争议
> - **争议类型一** 一句话说明这个维度上各方争什么。
>   - **学者 A（Year）** 一句话立场。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
>   - **学者 B（Year）** 一句话立场。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **争议类型二** 一句话说明另一维度的分歧。
>   - **学者 C（Year）** 一句话立场。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

%% 若争论恰好是两方正面对立（二元范式冲突），改用 [!tension]：%%

> [!tension] 核心张力（仅两方正面对立时使用）
> - **立场 A（蓝方）** 观点说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **立场 B（红方）** 观点说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!critique] 外部批评
> - **批评类型** 批评内容，说明批评者是谁、批评对象是什么。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!warning] 适用局限
> 只写原文或学界公认的边界条件，不写你自己的评价。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---
## 实证数据

%% 三类数据分开记录：一级研究效应量（effect-table）、元分析汇总（ma-table）、其他零散发现或应用案例（evidence-grid-a）。没有量化数据时可只用 evidence-grid-a。 %%

> [!effect-table]- 一级研究效应量
> | 研究 | 干预 | 结果变量 | n_t | n_c | d | SE | 设计 |
> |---|---|---|---|---|---|---|---|
> | [[Argument_Author_Year_Journal\|Author (Year)]] | 干预说明 | 结果变量 | — | — | — | — | RCT |

> [!ma-table]- 元分析汇总
> | 元分析 | k | N | ES | 95% CI | I² | GRADE |
> |---|---|---|---|---|---|---|
> | [[Argument_Author_Year_Journal\|Author (Year)]] | — | — | — | — | — | — |

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Author_Year_Journal|Author (Year)]] — 一句话说明该研究如何使用、检验或修正这个概念，或说明应用案例与迁移条件。
