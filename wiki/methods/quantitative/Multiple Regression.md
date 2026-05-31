---
title: Multiple Regression
aliases:
  - 多元回归
  - 多重回归
  - multiple linear regression
  - OLS regression
summary: "将Pearson相关扩展到两个或多个预测变量的推断统计方法，用于评估多个预测变量对一个结果变量的相对预测力"
type: method
method_type: quantitative
tags:
  - method/statistical
  - quantitative-research
  - regression
related_concepts:
  - "[[Variable]]"
  - "[[Statistical Significance]]"
  - "[[Effect Size]]"
  - "[[Causality]]"
related_theories: []
related_methods:
  - "[[Quantitative Research]]"
  - "[[Survey Research]]"
  - "[[Pearson Product-Moment Correlation]]"
  - "[[ANOVA]]"
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

# Multiple Regression

## 定义

> [!info]
> 多元回归（Multiple Regression）是将 [[Pearson Product-Moment Correlation|Pearson 相关]]扩展到两个或以上预测变量（predictor variables）的推断统计方法。它用于评估多个预测变量（自变量）与一个结果变量（因变量）之间的关系，提供整体模型拟合指标（R² 和 F 统计量）以及每个预测变量的相对贡献（b 系数和 t 统计量）。多元回归揭示了众多变量中哪一个变量对结果的相对预测力最强（Creswell & Creswell, 2022, Ch8）。

## 研究程序

> [!example]
> Creswell & Creswell (2022, Ch8, Table 8.3) 提供的选择标准：
> - 研究问题性质：关联变量（relate variables）
> - 自变量数量：2 个或以上
> - 因变量数量：1
> - 协变量数量：0
> - 变量类型：连续／连续（预测变量和结果变量均为连续变量）
> - 分数分布：正态分布

> [!note] 多元回归的输出指标
> - **R²** — 模型整体拟合度，表示所有预测变量共同解释的结果变量方差比例。
> - **F 统计量** — 检验整体模型是否显著优于仅使用均值的零模型。
> - **b（非标准化回归系数）** — 每个预测变量一个单位变化时结果变量的原始单位变化量。
> - **β（标准化回归系数）** — 使不同量表的预测变量之间可以比较相对预测力。
> - **t 统计量** — 检验每个单独预测变量的贡献是否显著（Creswell & Creswell, 2022, Ch8）。

## 方法变体与相近方法

> [!tip]
> - **层级回归（Hierarchical Regression）**：按理论驱动的顺序逐步加入预测变量块，考察每块变量对 R² 的增量贡献。
> - **逐步回归（Stepwise Regression）**：由统计程序自动选择进入或退出模型的变量——但因其结果依赖样本特征且缺乏理论驱动，Creswell 未推荐此方法。
> - vs [[Pearson Product-Moment Correlation|Pearson 相关]] — Pearson 相关是双变量分析（一次两个变量）；多元回归是多变量分析（多个预测变量同时进入模型）。
> - vs [[ANOVA|ANOVA／ANCOVA]] — ANOVA 比较组间均值，通常使用类别预测变量；多元回归使用连续预测变量。ANCOVA 可视为 ANOVA 和回归的混合形式——组间比较中加入连续协变量。

## 适用场景

> [!success]
> - 调查研究中当研究问题涉及"哪些因素最能预测某一结果？"时。
> - 需要同时评估多个预测变量的独立贡献时。
> - 需要在控制其他变量（如人口学特征）后检验某一特定变量的预测力时。

## 局限性

> [!warning]
> - 多重共线性（multicollinearity）——当预测变量之间高度相关时，回归系数估计不稳定，难以区分各变量的独立贡献。
> - 与 Pearson 相关一样，回归揭示的是关联而非因果——即使控制了多个变量，未测量的混淆变量仍可能驱动结果。
> - 对异常值、非线性关系和方差异质性（heteroscedasticity）敏感。
> - 预测变量数量大而样本量小会导致过拟合（overfitting）——R² 被夸大且模型在新样本中表现差。

## 来源

- [[Creswell_2022_SAGE]]
