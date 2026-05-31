---
title: Analysis of Variance (ANOVA)
aliases:
  - 方差分析
  - ANOVA
  - ANCOVA
  - 协方差分析
  - MANOVA
  - 多元方差分析
  - F-test
  - one-way ANOVA
summary: "比较两组或多组均值差异的推断统计方法族，包括ANOVA、ANCOVA和MANOVA等变体"
type: method
method_type: quantitative
tags:
  - method/statistical
  - quantitative-research
  - group-comparison
related_concepts:
  - "[[Variable]]"
  - "[[Effect Size]]"
  - "[[Confidence Interval]]"
related_theories: []
related_methods:
  - "[[Factorial Design]]"
  - "[[t-test]]"
  - "[[Experimental Research]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
sources:
  - "[[Creswell_2022_SAGE]]"
confidence: medium
status: draft
created: 2026-05-31
updated: 2026-05-31
---

# Analysis of Variance (ANOVA)

## 定义

> [!info]
> 方差分析（Analysis of Variance, ANOVA）是一族用于比较两组或多组均值差异的推断统计方法，使用 F 检验统计量。ANOVA 的核心思想是将总变异分解为组间变异和组内变异，通过比较两者的比值来判断各组均值是否存在显著差异。ANCOVA（协方差分析）是 ANOVA 的扩展，在比较组间差异时控制一个或多个协[[Variable|变量]]的影响；MANOVA（多元方差分析）则将 ANOVA 扩展到同时比较多个因变量（Creswell & Creswell, 2022, Ch8）。

## 研究程序

> [!example]
> 方差分析的典型使用步骤（Creswell & Creswell, 2022, Ch8）：

1. 明确自[[Variable|变量]]（分组变量，通常为类别变量）和因变量（连续变量）。
2. 检查正态分布假设和方差同质性假设。
3. 计算 F 统计量 = 组间均方 / 组内均方。
4. 比较 p 值与预设显著性水平（通常为 .05）。
5. 若 ANOVA 结果显著，进行事后比较（post hoc tests）以确定哪些组之间存在差异。
6. 报告[[Effect Size|效应量]]（如 η² 或 Cohen's d）和[[Confidence Interval|置信区间]]以评估实际意义。

## 方法变体

> [!tip]
> - **单因素 ANOVA（One-Way ANOVA）**：比较一个自[[Variable|变量]]（两个或多个水平）在一个因变量上的均值差异。使用 F 统计量。
> - **ANCOVA（Analysis of Covariance）**：在 ANOVA 基础上加入一个或多个协变量，控制其影响后比较调整后的组间均值。
> - **MANOVA（Multivariate Analysis of Variance）**：同时比较两个或多个因变量在组间的差异。
> - **因子 ANOVA**：在[[Factorial Design|因子设计]]中检验多个自变量的主效应和交互效应。
> - vs [[t-test]] — ANOVA 可视为 t 检验在两组以上比较中的推广；两组比较时 ANOVA 的 F 值等于 t 值的平方。

## 适用场景

> [!success]
> - [[Experimental Research|实验研究]]中比较不同处理条件组在连续结果[[Variable|变量]]上的均值差异。
> - 需要有控制变量时使用 ANCOVA。
> - 需要同时比较多个相关结果变量时使用 MANOVA（Creswell & Creswell, 2022, Ch8）。

## 局限性

> [!warning]
> - 对正态分布和方差同质性假设敏感；假设违反时可能需要使用非参数替代方法。
> - ANOVA 显著只表明至少有一组均值与其他组不同，无法直接指出差异发生在哪些组之间，需要事后比较。
> - 多重比较会增加第一类错误（Type I error）的概率，需要校正。

## 使用此方法的研究

> [!example]
> - [[Argument_Creswell_2022_SAGE]] — 说明 ANOVA、ANCOVA 和 MANOVA 是[[Experimental Research|实验研究]]中比较组间差异最常使用的推断统计方法。（Ch8）

## 来源

- [[Creswell_2022_SAGE]]
