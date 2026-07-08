---
title: Random Sampling
aliases:
  - 随机抽样
  - probability sampling
  - 概率抽样
  - random sample
  - 随机样本
  - simple random sampling
  - 简单随机抽样
summary: "从总体中按均等概率选取样本的抽样策略家族，每个个体有均等概率被选中，包括简单随机抽样、系统抽样、随机分层抽样、整群抽样、阶段抽样和多阶段抽样，目的是提升样本代表性并支持统计推论"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 12
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/sampling
  - quantitative-research
  - survey
related_concepts:
  - "[[Sampling Frame]]"
  - "[[External Validity]]"
  - "[[Causality]]"
  - "[[Internal Validity]]"
  - "[[Response Bias]]"
related_theories: []
related_methods:
  - "[[Systematic Sampling]]"
  - "[[Stratified Sampling]]"
  - "[[Cluster Sampling]]"
  - "[[Stage Sampling]]"
  - "[[Random Assignment]]"
  - "[[Multi-phase Sampling]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
confidence: medium
status: draft
created: 2026-06-01
updated: 2026-06-22
---
# Random Sampling

## 定义

> [!def] 方法定义
> 随机抽样（Random Sampling），亦称概率抽样（Probability Sampling），是从研究总体中按均等概率选取样本的抽样策略家族。总体中每个成员被选入样本的概率已知且相等，选择完全由概率决定。目标是提升样本对总体的代表性，支持从样本到总体的统计推广（generalization）。

> [!method-scope] 方法范围
> - **研究对象** 有可识别[[Sampling Frame|抽样框]]的总体
> - **问题类型** 需要统计推广到更广泛总体的研究
> - **分析单位** 个体、组织或可从抽样框中识别的任何单位
> - **输出形式** 概率样本，支持统计推论和误差范围报告

## 子类型总览

> [!taxonomy] 概率抽样六种类型
>
> | 类型 | 英文 | 核心特征 | 典型应用 |
> |---|---|---|---|
> | 简单随机抽样 | [[Random Sampling\|Simple Random Sampling]] | 每个成员等概率、独立选择；需完整[[Sampling Frame\|抽样框]] | 有完整名单的小规模研究 |
> | [[Systematic Sampling\|系统抽样]] | Systematic Sampling | 随机起点 + 固定频率间隔；操作简便 | 有完整名单的大规模抽样 |
> | [[Stratified Sampling\|随机分层抽样]] | Stratified Sampling | 按特征分层后在层内随机抽样；确保子组代表性 | 已知总体关键特征，需均衡比较子组 |
> | [[Cluster Sampling\|整群抽样]] | Cluster Sampling | 选择地理/组织群组，测试群内所有成员 | 总体大且分散，逐一接触不可行 |
> | [[Stage Sampling\|阶段抽样]] | Stage Sampling | 从样本中再抽取样本，多阶[[Random Assignment\|随机化]] | 总体嵌套在多层组织中，无完整个体名单 |
> | [[Multi-phase Sampling\|多阶段抽样]] | Multi-phase Sampling | 各阶段目的不同，基于不同标准筛选 | 需多重筛选标准的复杂抽样 |

## 概念辨析

> [!contrast-table] 随机抽样 vs [[Random Assignment|随机分配]]
> | 维度 | 随机抽样（Random Sampling） | [[Random Assignment\|随机分配]]（Random Assignment） |
> |---|---|---|
> | 问题 | **谁**进入样本 | 已入样本的人**如何**分配到各条件 |
> | 目标 | 样本 → 总体推广（[[External Validity\|外部效度]]） | 消除组间系统性偏差，支持[[Causality\|因果推断]]（[[Internal Validity\|内部效度]]） |
> | 可独立使用 | 是 | 是 |

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 研究目标是从样本结果推广到更广泛的总体；[[Sampling Frame|抽样框]]可获得且完整。
> - **谨慎使用** 抽样框不完整或难以获取时；低回应率可能使样本丧失随机性。
> - **不适合使用** 总体无法界定或无法构建抽样框；研究不追求统计推广。

## 局限性

> [!method-limits] 方法局限
> - **[[Sampling Frame|抽样框]]依赖** 完整总体名单往往不可行或成本极高。
> - **回应率偏差** 即使抽样随机，低回应率可能导致最终样本丧失随机性（[[Response Bias\|回应偏差]]）。
> - **行政管理成本** 简单随机抽样在总体大且分散时行政上不可行，需借助整群或[[Stage Sampling\|阶段抽样]]。
> - **子类型各有局限** 详见各子类型条目（周期性、层数膨胀、群内同质性、规模假定等）。

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 系统介绍概率抽样的六种类型及其操作程序。
