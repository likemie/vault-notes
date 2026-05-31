---
title: Analysis of Covariance
aliases:
  - 协方差分析
  - ANCOVA
summary: "在方差分析基础上加入一个或多个协变量以控制其影响后比较调整组间均值的推断统计方法，使用F统计量"
type: method
method_type: quantitative
tags:
  - method/statistical
  - quantitative-research
  - group-comparison
related_concepts:
  - "[[Variable]]"
  - "[[Research Question]]"
related_theories: []
related_methods:
  - "[[Analysis of Variance]]"
  - "[[Multiple Regression]]"
  - "[[Experimental Research]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Random Assignment]]"
  - "[[Survey Research]]"
related_persons: []
related_facts: []
related_arguments: []
sources:
  - "[[Creswell_2022_SAGE]]"
confidence: medium
status: draft
created: 2026-06-01
updated: 2026-06-01
---

# Analysis of Covariance

## 定义

> [!info]
> 协[[Analysis of Variance|方差分析]]（Analysis of Covariance, ANCOVA）是 [[Analysis of Variance|ANOVA]] 的扩展，在比较组间均值差异时控制一个或多个协[[Variable|变量]]（covariates）的影响。它通过统计手段移除协变量对因变量的效应后，比较调整后的组间均值（adjusted means），从而更精确地评估自变量对因变量的独立效应（Creswell & Creswell, 2022, Ch8）。

## 研究程序

> [!example]
> Creswell & Creswell (2022, Ch8, Table 8.3) 提供的选择标准：
> - [[Research Question|研究问题]]性质：组间比较
> - 自[[Variable|变量]]数量：1 个或以上
> - 因变量数量：1
> - 协变量数量：1
> - 变量类型：类别（自变量）/ 连续（因变量和协变量）
> - 分数分布：正态

> [!note] ANCOVA 的核心逻辑
> ANCOVA 将因变量的总变异分解为三部分：协变量的效应、自变量的效应（组间差异）、以及残差。通过先移除协变量的效应，ANCOVA 能够减少组内误差方差，提高检验的统计功效，同时校正各组在协变量上的初始差异可能导致的偏差（Creswell & Creswell, 2022, Ch8）。

## 方法变体与相近方法

> [!tip]
> - vs [[Analysis of Variance|ANOVA]] — ANOVA 直接比较组间均值；ANCOVA 在控制协[[Variable|变量]]后比较调整均值。当各组在某一连续变量（如前测分数）上存在初始差异且该变量与因变量相关时，ANCOVA 比 ANOVA 更合适。
> - vs [[Multiple Regression|多元回归]] — 多元回归使用连续预测变量；ANCOVA 同时包含类别自变量和连续协变量，可视为 ANOVA 和回归的混合形式。

## 适用场景

> [!success]
> - [[Experimental Research|实验研究]]中，各组在前测分数上存在初始差异时，使用前测作为协[[Variable|变量]]进行 ANCOVA 可以更准确地评估处理效应。
> - [[Quasi-Experimental Designs|准实验设计]]中，由于缺乏[[Random Assignment|随机分配]]，各组可能在关键特征上不等价——ANCOVA 通过统计控制来减少这种选择偏差。
> - [[Survey Research|调查研究]]中，需要在控制人口学变量（如年龄、收入）后比较不同群体在某结果上的均值差异时（Creswell & Creswell, 2022, Ch8）。

## 局限性

> [!warning]
> - ANCOVA 假设协[[Variable|变量]]与因变量之间存在线性关系，且各组回归斜率相同（homogeneity of regression slopes）。若这一假设不成立，ANCOVA 的结果不可靠。
> - 协变量应在处理之前测量——若协变量本身可能受到处理的影响，则使用 ANCOVA 是不适当的（因为控制处理效应的中介变量会人为削弱处理效应）。
> - 与其他[[Analysis of Variance|方差分析]]方法一样，对正态分布和方差同质性假设敏感。

## 来源

- [[Creswell_2022_SAGE]]
