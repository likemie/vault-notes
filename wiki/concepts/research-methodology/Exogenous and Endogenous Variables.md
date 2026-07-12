---
title: Exogenous and Endogenous Variables
aliases:
  - 外生变量与内生变量
  - exogenous variable
  - endogenous variable
summary: "因果模型中对变量的结构区分：外生变量不被模型中其他变量所引起，内生变量受模型中其他变量的影响。与递归/非递归模型和因果网络密切相关"
type: concept
domain: "research-methodology"
related_count: 8
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - subject/research-methodology
  - paradigm/positivist
related_concepts:
  - "[[Variable]]"
  - "[[Dependent Variable]]"
  - "[[Document]]"
  - "[[Causality]]"
  - "[[Independent Variable]]"
related_theories: []
related_methods:
  - "[[Causal Modeling]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]"
confidence: medium
status: draft
created: 2026-05-31
updated: 2026-06-17
---

# Exogenous and Endogenous Variables

## 定义

> [!info]
> 外生[[Variable|变量]]（exogenous variable）和内生变量（endogenous variable）是因果模型中对变量的一种结构性区分。外生变量不被模型中其他变量所引起，作为模型的输入端。内生变量受模型中其他变量的影响，处于模型的因果链之中([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.59]])。

## 在因果模型中的角色

在 Blalock 所倡导的[[Causal Modeling|因果建模]]传统中，视觉模型从左到右排列[[Variable|变量]]，独立的外生变量位于最左侧，内生变量位于中段和右侧。箭头从外生变量流出，流向内生变量和最终的[[Dependent Variable|因变量]]。这种区分帮助研究者明确模型的因果结构，理清哪些变量是"给定"的起点，哪些变量是模型试图解释的中间或终结环节。

> [!example]
> Jungnickel (1990) 在研究药学院教师研究生产力的因果模型中，从护理学[[Document|文献]]（Megel et al., 1987）中改编了一个理论框架。该模型将所有外生变量置于最左侧，包括：
> - 人口统计学变量（demographic variables）
> - 机构终身教职标准（institutional tenure standards）
> - 终身教职轨聘任（tenure-track appointment）
> - 是否位于健康科学中心（college in health sciences center）
> - 自视为研究者（self-perception as researcher）
> - 先前研究训练（prior research training）
> - 聘任类型（type of appointment，系主任 vs 教师）
>
> 内生变量位于模型中部，包括非研究工作负荷（workload, non-research）、研究压力（pressure to conduct research）、合作（collaboration）、资源（resources）、同事支持（support from colleagues）和系主任支持（support from department chair）。这些内生变量共同影响最终的结果变量——学术绩效（scholarly performance），后者被细分为：非研究性报告、研究性报告、非审稿期刊论文、审稿研究论文、审稿非研究论文、书章、专著、获批联邦资助、已拨付联邦资助、非联邦资助和合同（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, pp.59–60]]; 图 3.3）。

## 递归与非递归因果模型

外生[[Variable|变量]]和内生变量的区分在两种因果模型结构中扮演不同角色（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 66–67]]）：

> [!contrast-table] 递归模型 vs 非递归模型
> | 维度 | 递归模型（Recursive） | 非递归模型（Non-Recursive） |
> |------|---------------------|--------------------------|
> | **因果方向** | 单向（unidirectional） | 一个或多个方向——因果可以双向或多向流动 |
> | **变量关系** | 外生 → 内生，方向固定 | 变量可以同时是外生和内生——取决于因果链中的位置 |
> | **复杂性** | 可能过度简化因果方向 | 更能捕捉因果网络（causal nets）——原因集群以多方向共同作用 |
> | **典型应用** | 简单因果链 | 结构方程模型 |

在递归模型中，[[Causality|因果关系]]是单向的——外生变量只向内生变量施加因果影响。在非递归模型中，一个变量可以同时作为原因和效果——它是上游变量的内生变量（被引起），同时又是下游变量的外生变量（引起者）。许多结构方程模型是非递归的，因为它们捕捉了变量之间更复杂的双向或多向因果依赖关系。

### 因果网络（Causal Nets）

因果网络（causal nets）是非递归因果模型的自然延伸——它描述的不是单条因果链，而是原因集群以多方向共同作用的网络结构。在因果网络中，变量之间不仅有链式关系，还有互向关系，以及多个原因同时对多个效果施加因果力的网状结构（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 66–67]]）。因果网络不预设单一的因果方向或线性关系，而是承认在多因多果的情境中，关系及其分析是概率性、条件性和虚拟的——因果网络和因果条件比因果线或因果事件链更恰切地描述因果性。

## 概念辨析

> [!example]
> **外生/内生 vs 自[[Variable|变量]]/[[Dependent Variable|因变量]]**。[[Independent Variable|自变量]]和因变量描述的是变量之间"谁影响谁"的二元关系。外生和内生描述的是变量在完整因果模型中的结构位置。一个内生变量可以是某个下游变量的自变量，同时又是上游外生变量的因变量。两者的区分层次不同。

> [!example]
> **外生变量 vs 混淆变量**。外生变量是模型中明确指定的输入变量，研究者有意将其纳入模型结构。混淆变量是未测量的、可能同时影响自变量和因变量的第三变量，它带来的是模型设定偏误的风险。前者是模型的设计特征，后者是效度威胁。

## 相关概念

- [[Variable]] — 外生和内生变量是变量的结构性分类
- [[Causal Modeling]] — 因果建模是外生和内生变量区分的主要应用语境
- [[Causality]] — 因果性是这一区分的逻辑基础

