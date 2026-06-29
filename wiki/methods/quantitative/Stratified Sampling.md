---
title: Stratified Sampling
aliases:
  - 分层抽样
  - stratified random sampling
  - 随机分层抽样
  - stratified sample
summary: "将总体按关键特征划分为同质层后在各层内分别随机抽样的概率抽样方法，确保样本在各特征上的比例与总体一致，兼具随机化与分类化优势"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 6
method_related_level: 0
method_related_stars: ""
method_related_color: "#dcfce7"
tags:
  - method/sampling
  - quantitative-research
related_concepts:
  - "[[Sample Size Determination]]"
  - "[[Variable]]"
  - "[[Research Question]]"
related_theories: []
related_methods:
  - "[[Random Sampling]]"
  - "[[Random Assignment]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
confidence: medium
status: draft
created: 2026-06-22
updated: 2026-06-22
---
# Stratified Sampling

## 定义

> [!def] 方法定义
> 随机分层抽样（Random Stratified Sampling）是将总体按关键特征划分为同质组（层，strata），然后在各组内分别[[Random Sampling|随机抽样]]的概率抽样方法。它确保样本在所选特征上的比例与总体一致，是[[Random Assignment|随机化]]与分类化的结合。特征选择应尽量简洁——因素越多，不仅抽样越复杂，样本往往也越大。

> [!method-scope] 方法范围
> - **研究对象** 已知关键特征（如性别、社会经济地位、族裔）的总体
> - **问题类型** 需要对关键子组进行均衡比较或确保子组代表性的研究
> - **分析单位** 个体，按预设特征分组
> - **输出形式** 各层分别具有代表性的概率样本

## 研究程序

> [!proc] 两步程序
> 1. **划分层次** 识别总体中必须在样本中出现的关键特征，将总体划分为同质的离散组（层），如男性组和女性组。
> 2. **层内[[Random Sampling|随机抽样]]**：在各组内独立进行[[Random Sampling|简单随机抽样]]，各组[[Sample Size Determination|样本量]]由研究者判断或参照随机样本量表确定。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 已知总体关键特征、希望对关键子组进行均衡比较、同时需要定量（推论统计）和定性（针对性接触特定群体）分析。
> - **谨慎使用** 特征数过多时——层数越多，样本越快膨胀。
> - **不适合使用** 总体关键特征的分布未知或无法获取分层信息时。

## 局限性

> [!method-limits] 方法局限
> - **层数膨胀** 特征选择越多，层数呈几何增长，所需总[[Sample Size Determination|样本量]]迅速膨胀。
> - **特征信息依赖** 依赖对总体关键特征的先验知识，若分层[[Variable|变量]]选择不当，分层无益甚至引入偏差。
> - **缓解方式** 特征选择尽量简洁，只纳入对[[Research Question|研究问题]]最关键的分层变量。

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 介绍分层抽样的两步程序和层数膨胀问题。
