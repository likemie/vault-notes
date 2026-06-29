---
title: Standard Error
aliases:
  - 标准误
  - SE
  - SEM
  - standard error of the mean
  - 均值的标准误
  - standard error of proportions
summary: "抽样分布的标准差，度量样本统计量对总体参数的估计精度，是中心极限定理的直接推论和置信区间构建的核心材料"
type: concept
domain: "research-methodology"
related_count: 11
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - statistics
  - quantitative-research
  - sampling
related_concepts:
  - "[[Sampling Error]]"
  - "[[School Effectiveness]]"
  - "[[Confidence Interval]]"
  - "[[Sample Size Determination]]"
  - "[[Variable]]"
  - "[[Effect Size]]"
related_theories:
  - "[[Central Limit Theorem]]"
  - "[[Cognitive Load Theory]]"
related_methods:
  - "[[Causal Modeling]]"
  - "[[Random Sampling]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
confidence: medium
status: draft
created: 2026-06-22
updated: 2026-06-22
---
# Standard Error

## 定义

> [!def] 核心定义
> [[Sampling Error|标准误]]（Standard Error, [[School Effectiveness|SE]]）是抽样分布的标准差，度量样本统计量（如均值、比例）围绕总体参数的理论变异程度。它是[[Central Limit Theorem|中心极限定理]]的直接推论——[[Cognitive Load Theory|CLT]] 表明样本均值趋近正态分布，SE 则量化了该分布的宽度。SE 越小，样本估计越精确。SE 是[[Confidence Interval|置信区间]]的核心构建材料：$CI = \text{点估计} \pm Z \times SE$。

> [!concept-lens] 概念透镜
> - **含义** SE 指向从样本推断总体时固有的不确定性——不是某个具体样本的误差，而是抽样过程本身产生的理论变异。
> - **用途** SE 用于构建置信区间、进行显著性检验，以及根据目标精度反推所需[[Sample Size Determination|样本量]]。
> - **边界** SE 不等于标准差（SD）——SD 描述原始数据的离散程度，SE 描述样本统计量的估计精度。SE 也不等于[[Sampling Error|抽样误差]]——抽样误差通常指样本均值与总体均值之间的具体差距，SE 是这一差距的理论期望幅度。

> [!citation-card]- 关键表述
> 抽样分布的标准差是抽样误差的度量，称为均值的标准误（[[Causal Modeling|SEM]]）。抽样误差取决于总体的变异性和样本量：总体变异性越小，抽样误差越小；样本量越大，抽样误差越小。（第8章，pp.150–151）
>
> *The standard deviation of the theoretical distribution of sample means is a measure of sampling error and is called the standard error of the mean (SEM).* (Ch. 8, pp. 150–151)

---

## 核心要素

### 均值的标准误（SEM）

> [!formula] [[Sampling Error|均值的标准误]]
> $$[[Causal Modeling|SEM]] = \frac{SD_s}{\sqrt{N}}$$
>
> - $SD_s$：样本标准差（严格公式以 $SD_{pop}$ 为分母，因总体标准差通常未知，故用样本标准差替代）
> - $N$：[[Sample Size Determination|样本量]]
>
> SEM 是抽样误差的基本度量。$N$ 在分母——样本量越大，SEM 越小。但这种收益是边际递减的：$N$ 从 25 增到 100，SEM 减半；从 100 增到 400，SEM 再减半。少于 30 的样本危险地小，超过约 80 例后进一步增加 $N$ 对 SEM 的影响很小（p.152）。

### 比例的标准误

> [!formula] 比例的标准误
> $$[[School Effectiveness|SE]] = \sqrt{\frac{P \times Q}{N}}$$
>
> - $P$：某类别的百分比
> - $Q$：$100\% - P$
> - $N$：样本量
>
> 适用于分类/百分比数据。通常在[[Random Sampling|简单随机抽样]]基础上应用有限总体校正（fpc）：$fpc = \sqrt{1 - f}$，其中 $f = n/N$ 为抽样比例。当样本占总体比例较大时（$> 5\%$），fpc 适当缩小 SE。

---

## 概念辨析

> [!contrast-table] [[School Effectiveness|SE]] vs 邻近概念
> | 维度 | [[Sampling Error\|标准误]]（SE） | 标准差（SD） | [[Sampling Error\|抽样误差]] |
> |---|---|---|---|
> | 描述对象 | 样本统计量的估计精度 | 原始数据的离散程度 | 样本值与总体值的具体差距 |
> | 公式 | $SE = SD/\sqrt{N}$ | $SD = \sqrt{\sum(x_i - \bar{x})^2/(n-1)}$ | $\bar{x} - \mu$ |
> | 随 $N$ 增大 | 减小（$\propto 1/\sqrt{N}$） | 趋于稳定 | 减小 |
> | 核心用途 | 构建 [[Confidence Interval\|CI]]、显著性检验 | 描述数据分布 | 评估样本代表性 |

---

## 围绕概念形成的命题

### 命题类型一：SE 与样本量的非线性关系（SE–Sample Size Relationship）

> [!concept-lens] [[School Effectiveness|SE]] 随 N 增大而减小，但边际收益递减
> SE 与 $\sqrt{N}$ 成反比：$N$ 扩大 4 倍，SE 减半；$N$ 扩大 100 倍，SE 缩小到 1/10。这意味着从小样本到大样本的初期收益巨大，后期收益递减。

> [!claim] 少于 30 例危险地小
> 少于 30 例的样本允许相当程度的[[Sampling Error|标准误]]存在。超过约 80 例后，进一步增加[[Sample Size Determination|样本量]]对标准误的影响很小（p.152）。

> [!claim] 变异性放大 SE
> 若总体变异性（$SD_{pop}$）很大，则需要大得多的 $N$ 才能将 SE 控制在可接受水平。Gorard（2003: 62）指出，调查 IQ 这类高变异[[Variable|变量]]（范围约 70–150）可能需要比低变异变量更大的样本。

### 命题类型二：SE 是 CI 和显著性检验的基础（SE as Inference Foundation）

> [!concept-lens] SE 本身不是结论，但所有推论结论都依赖它
> SE 不直接回答"差异是否显著"或"真值在哪里"，但它提供了回答这些问题所需的精度信息。

> [!claim] [[Confidence Interval|CI]] 依赖于 SE
> 95% CI = 点估计 $\pm 1.96 \times SE$。没有 SE 就无法构建 CI，也无法判断点估计的稳定性。

> [!claim] 统计功效依赖于 SE
> Gorard（2003: 62）强调：功效（power）是对检验将[[Effect Size|效应量]]与随机变异区分开来之能力的估计。SE 越小（$N$ 越大），功效越强。

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 系统介绍 [[Causal Modeling|SEM]] 和比例[[Sampling Error|标准误]]的公式、推导和应用。
