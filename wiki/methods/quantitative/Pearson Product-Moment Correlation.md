---
title: Pearson Product-Moment Correlation
aliases:
  - Pearson相关
  - 皮尔逊相关
  - Pearson's correlation
  - Pearson's r
  - 积差相关
summary: "测量两个连续变量间关联强度与方向的推断统计方法，使用r统计量，适用于正态分布的连续数据"
type: method
method_type: quantitative
tags:
  - method/statistical
  - quantitative-research
  - correlation
related_concepts:
  - "[[Statistical Significance]]"
  - "[[Effect Size]]"
  - "[[Variable]]"
related_theories: []
related_methods:
  - "[[Quantitative Research]]"
  - "[[Survey Research]]"
  - "[[Multiple Regression]]"
  - "[[t-test]]"
related_persons: []
related_facts: []
related_arguments: []
sources:
  - "[[Creswell_2022_SAGE]]"
confidence: medium
status: draft
created: 2026-05-31
updated: 2026-05-31
---

# Pearson Product-Moment Correlation

## 定义

> [!info]
> Pearson 积差相关（Pearson Product-Moment Correlation），通常简称为 Pearson 相关，是一种测量两个连续变量之间关联强度（magnitude）和方向（direction）的推断统计方法，使用 r 统计量。r 值范围在 -1 到 +1 之间：正值表示正相关（一个变量增加、另一个也增加），负值表示负相关（一个增加、另一个减少），0 表示无线性关联。报告时 r 应以斜体呈现（Creswell & Creswell, 2022, Ch8）。

## 研究程序

> [!example]
> Creswell & Creswell (2022, Ch8, Table 8.3) 提供的选择标准：
> - 研究问题性质：关联变量（relate variables）
> - 自变量数量：1
> - 因变量数量：1
> - 协变量数量：0
> - 变量类型：连续／连续（两个变量均为连续变量，如等距或比率量表）
> - 分数分布：正态分布

## 方法变体与相近方法

> [!tip]
> - vs [[Multiple Regression|多元回归]] — Pearson 相关是双变量（bivariate）分析，一次只考察两个变量间的关系；多元回归将相关分析扩展到两个或以上的预测变量，同时评估多个预测变量对一个结果变量的相对预测力。
> - vs Spearman 等级相关 — 当变量为顺序量表或分数非正态分布时，应使用 Spearman's ρ（rho）而非 Pearson's r。
> - vs [[t-test|t 检验]] — t 检验比较两组均值差异，Pearson 相关考察两个连续变量间的线性关联。

## 适用场景

> [!success]
> - 调查研究中检验两个连续变量之间是否存在线性关联。
> - 研究报告中的相关矩阵——展示多个研究变量之间的两两关联。
> - 实验研究的初步分析阶段——检验关键研究变量间的关联。

## 局限性

> [!warning]
> - 只衡量线性关系——两个变量可能存在强的非线性关系但 r 值接近 0。
> - 对异常值（outliers）敏感——少数极端值可以显著改变 r 值。
> - 相关不等于因果——高相关不意味着一个变量导致了另一个变量的变化；混淆变量（第三变量 Z）可能同时驱动两个变量的变化（Creswell & Creswell, 2022, Ch8）。

## 来源

- [[Creswell_2022_SAGE]]
