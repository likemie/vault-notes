---
title: Exploratory Factor Analysis
aliases:
  - "探索性因子分析"
  - "EFA"
summary: "一种多变量统计技术，用于在没有预设明确结构的情况下，从一组观测变量中提取出较少数量的潜在因子，常用于新量表的开发和维度探索。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 14
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags: []
related_concepts:
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Questionnaire]]"
  - "[[Construct]]"
  - "[[Epistemology]]"
  - "[[Sample Size Determination]]"
  - "[[Simplicity of Knowledge]]"
related_theories: []
related_methods:
  - "[[Scale Development]]"
  - "[[Confirmatory Factor Analysis]]"
  - "[[KMO and Bartlett's Test of Sphericity]]"
related_instruments:
  - "[[Schommer's Modified Epistemological Questionnaire]]"
related_persons: []
related_facts:
  - "[[Sense about Science]]"
related_arguments:
  - "[[Argument_Bergeron_2015_TeachingTOK]]"
  - "[[Argument_Lodewyk_2007_EP]]"
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
confidence: medium
status: draft
created: 2026-08-17
updated: 2026-08-29
---

# Exploratory Factor Analysis

---

## 定义

> [!def] 方法定义
> 探索性因子分析（Exploratory Factor Analysis, EFA）是一种用于识别数据底层结构的降维技术。它在没有特定关于哪个观测[[Variable|变量]]测量哪个潜在因子[[Hypothesis|假设]]的情况下，通过分析变量之间的相关矩阵，归纳提取出少数几个潜在的公共因子，以解释观测变量之间的大部分方差。

> [!method-scope] 方法范围
> - **研究对象** 新开发的[[Questionnaire|问卷]]量表数据、尚未确立维度结构的指标体系。
> - **问题类型** 回答这组题目背后隐藏着几个潜在特质（[[Construct|构念]]），以及每个题项分别归属于哪个特质。
> - **分析单位** 个体。
> - **输出形式** 因子数量、特征值（Eigenvalues）、方差贡献率、因子载荷矩阵（Factor Loadings）、碎石图（Scree Plot）。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为复杂的人类行为和特质可以归结为少数几个深层结构或潜在因素。
> - **研究者角色** 研究者基于统计标准（如特征值、累积方差）和理论可解释性综合判断因子的数量和命名，具有一定的探索和主观判断性质。
> - **有效性标准** 提取出的因子具有理论意义上的可解释性，同时满足统计标准（如 KMO 检验、Bartlett 球形检验）。

> [!method-stack] 方法层级
> - **分析方法** 探索性因子分析（EFA）。
> - **辅助技术** 主成分分析法（PCA，常被借用为因子提取方法）、最大方差正交旋转（Varimax）、斜交旋转（Promax 或 Oblimin）。

---

## 研究程序

> [!proc] 通用程序
> 1. **适用性检验** 进行 KMO 检验（通常要求 > 0.6 或 0.7）和 Bartlett 球形检验（要求显著，$p < .05$），确保变量间有足够相关性以进行因子提取。
> 2. **因子提取** 根据特征值大于 1（Kaiser 准则）、碎石图拐点或累积方差贡献率（如 > 50%）来决定保留几个潜在因子。
> 3. **因子旋转** 为了让结果更容易解释，通常进行因子旋转（如果认为因子间独立则用正交旋转，若相关则用斜交旋转），使得每个题项在一个因子上具有高载荷，在其他因子上载荷较低。
> 4. **题项筛选** 剔除最大载荷过低（如 < 0.4）或发生严重跨载荷（Cross-loading）的题项。
> 5. **因子命名** 根据在各个因子上高载荷的题项特征，为每个潜在因子命名。

### 量化方法模块

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** 大样本的横截面数据（通常要求[[Sample Size Determination|样本量]]是题项数的 5-10 倍，或至少 $N > 100$）。
> - **变量或指标** 多个连续或类别级别的观测变量。
> - **模型或统计量** KMO 统计量、因子载荷、特征值、方差解释率。

> [!formula-step] 公式步骤　KMO 样本充分性度量
> $$ KMO = \frac{\sum \sum r_{ij}^2}{\sum \sum r_{ij}^2 + \sum \sum a_{ij}^2} $$
>
> **这个公式在做什么** 判断你的数据适不适合做因子分析。
>
> **符号说明** $r_{ij}$ 是变量间的简单相关系数，$a_{ij}$ 是偏相关系数。
>
> **数学直觉** 如果变量之间有共同的潜在因子，它们的偏相关系数（排除了其他变量影响后的纯粹相关性）应该很小。这样公式的分子分母接近，KMO 值趋近于 1；反之，若变量独立，KMO 趋近于 0。
>
> **结果怎么读** 越接近 1 越好。> 0.9 极佳，> 0.8 良好，> 0.7 中等，< 0.6 勉强，< 0.5 不适合做 EFA。

> [!software-impl] 软件实现
> - **推荐软件** SPSS, R (psych 包), [[Sense about Science|SAS]]。
> - **报告标准** 需要报告 KMO 值、Bartlett 检验结果、因子的特征值与方差贡献率、旋转方法以及最终保留题项的因子载荷矩阵。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 处于新工具开发阶段，或试图精简大量[[Variable|变量]]找出核心维度模式时。

---

## 局限性

> [!method-limits] 方法局限
> - **误用风险** 经常与主成分分析（PCA）混淆（软件中常默认 PCA），而两者的理论[[Hypothesis|假设]]不同（EFA 假设观测[[Variable|变量]]受潜在因子影响并包含误差，PCA 仅是数据的数学降维重组）。
> - **适用边界** EFA 只是一个探索过程，不能提供模型整体拟合程度的显著性检验。[[Scale Development|量表编制]]完成后，通常还需要重新收集另一个独立样本的数据，进行[[Confirmatory Factor Analysis|验证性因子分析]]（CFA）来确认该结构。

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Bergeron_2015_TeachingTOK|Bergeron & Rogers (2015)]] — 量化部分利用探索性因子分析（EFA，带主成分提取）检验了包含 11 道题的教学信心量表结构，确认其单一维度结构并解释了 35.03% 的累积方差。
> - [[Argument_Lodewyk_2007_EP|Lodewyk (2007)]] — 对 447 名十年级中学生的 Schommer 修订版[[Epistemology|认识论]][[Questionnaire|问卷]]（[[Schommer's Modified Epistemological Questionnaire|SMEQ]]）52 个题项进行主轴探索性因子分析与方差最大旋转，提取出固定与快速学习能力（FQAL）、[[Simplicity of Knowledge|简单知识]]（SK）和确定知识（CK）三个核心因子（解释 16.81% 方差）。
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 对 310 名中小学教师的 56 个初测题项进行主轴因子提取法（Principal Axis Factoring, PAF）与方差最大正交旋转（Varimax Rotation），经矫正题总相关（$r < .30$ 剔除 3 题）与载荷准则（载荷 $> .32$、跨载荷差 $> .10$）逐题筛选，在 [[KMO and Bartlett's Test of Sphericity|Kaiser-Meyer-Olkin]] 抽样适宜性系数（KMO = .966）支持下，最终提取出涵盖技能（46.90% 方差）、态度（7.20% 方差）、使用（4.60% 方差）与意识（3.80% 方差）的 4 因子 20 题结构（解释 62.602% 累积方差）。
