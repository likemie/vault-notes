---
title: Quota Sampling
aliases:
  - 配额抽样
  - quota sample
summary: "非概率版的分层抽样，力求按总体中的比例代表显著特征，通过三步程序确保样本中各特征比例与总体一致"
type: method
method_type: mixed
method_family: "mixed"
method_related_count: 6
method_related_level: 0
method_related_stars: ""
method_related_color: "#fef3c7"
tags:
  - method/sampling
  - quantitative-research
  - qualitative-research
related_concepts:
  - "[[Sample Size Determination]]"
  - "[[Sampling Error]]"
related_theories: []
related_methods:
  - "[[Non-probability Sampling]]"
  - "[[Stratified Sampling]]"
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
# Quota Sampling

## 定义

> [!def] 方法定义
> 配额抽样（Quota Sampling）是[[Non-probability Sampling|非概率抽样]]中对应[[Stratified Sampling|分层抽样]]的方法，力求按总体中的比例代表显著特征（层，strata）。与分层抽样的关键区别在于：层内个体的选择不是随机的，而是由研究者根据可得性和配额要求进行。

> [!method-scope] 方法范围
> - **研究对象** 已知关键特征分布的总体
> - **问题类型** 需要在非概率条件下确保子组代表性的研究
> - **分析单位** 个体，按预设特征分组
> - **输出形式** 比例上与总体匹配的非概率样本

## 研究程序

> [!proc] 三步程序
> 1. 识别总体中必须在样本中出现的特征，划分为同质离散组（层）。
> 2. 确定各特征在总体中的百分比比例。
> 3. 确保样本中各特征的百分比比例与总体一致。

> [!example] 最小配额[[Sample Size Determination|样本量]]
> 某校 1,700 名学生，院系构成比例为 $3:3:6:5$（表演艺术 300、自然科学 300、人文学科 600、商业与社会科学 500），最小配额样本为 $3 + 3 + 6 + 5 = 17$ 名学生。这仅为最小值，实际操作中应更高。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 已知总体关键特征的比例但无法进行[[Random Sampling|随机抽样]]时。
> - **谨慎使用** 层数多时——层数越多，最小[[Sample Size Determination|样本量]]越快增长，通常呈几何级数而非算术级数。
> - **不适合使用** 总体中的比例未知或难以接触时——可能需要先做试点调查。

## 局限性

> [!method-limits] 方法局限
> - **层数膨胀** 层数越多，[[Sample Size Determination|样本量]]呈几何级增长。配额抽样中层数应尽量少。
> - **非随机选择** 层内个体的非随机选择可能引入未知偏差。
> - **比例不确定性** 若总体比例未知，需试点调查确定——试点数据本身可能有[[Sampling Error|抽样误差]]。

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 介绍配额抽样的三步程序和最小[[Sample Size Determination|样本量]]计算。
