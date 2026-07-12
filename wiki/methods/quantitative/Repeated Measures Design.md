---
title: Repeated Measures Design
aliases:
  - 重复测量设计
  - repeated measures
  - within-subjects design
  - 受试者内设计
  - crossover design
summary: "真实验设计变体，同一组受试者在两种或多种实验条件下接受测试，以自身为控制消除个体差异，但需应对顺序效应和延续效应"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 5
method_related_level: 0
method_related_stars: ""
method_related_color: "#dcfce7"
tags:
  - method/experimental
  - quantitative-research
  - design-type
related_concepts:
  - "[[Order Effects]]"
related_theories: []
related_methods:
  - "[[Matched Pairs Design]]"
  - "[[Pilot Testing]]"
  - "[[Random Assignment]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
confidence: medium
status: draft
created: 2026-07-12
updated: 2026-07-13
---
# Repeated Measures Design

## 定义

> [!def] 重复测量设计
> 重复测量设计（Repeated Measures Design）是真实验设计的变体，实验组的受试者在两种或多种实验条件下接受测试——同一受试者可能接受不止一种干预，其中可能包含或不包含控制条件（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16]]）。

该设计是[[Matched Pairs Design|配对设计]]的变体，具有显著的控制潜力：**完全相同的个体**接受不同干预，从而消除了组间个体差异的混淆。

## 研究程序

核心挑战是**[[Order Effects|顺序效应]]（order effects）** 干预的呈现顺序可能影响结果——第一次干预可能对第二次产生延续效应（carry-over effect），早期干预可能比后期干预效应更大。

### 应对顺序效应

在三干[[Pilot Testing|预实验]]中，可通过系统排列顺序来控制（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16]]）：

> [!proc] 拉丁方排列示例
> 1. 组 1 接受干预 1 → 干预 2 → 干预 3
> 2. 组 2 接受干预 2 → 干预 3 → 干预 1
> 3. 组 3 接受干预 3 → 干预 1 → 干预 2
> 4. 组 4 接受干预 1 → 干预 3 → 干预 2
> 5. 组 5 接受干预 2 → 干预 1 → 干预 3
> 6. 组 6 接受干预 3 → 干预 2 → 干预 1

也可以[[Random Assignment|随机化]]干预顺序并将受试者随机分配至不同序列，但这不一定保证平衡的序列安排。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** [[Order Effects|顺序效应]]不重要或不太可能时；研究者无法确定个体差异是否会掩盖处理效应时。
> - **谨慎使用** 干预可能产生长期延续效应时；干预本身的性质可能在序列中发生变化时。
> - **不适合使用** 干预效应不可逆时（如学习效应）。

## 局限性

> [!method-limits]
> - [[Order Effects|顺序效应]]是最主要的威胁：前一次干预可能影响后一次干预的结果。
> - 延续效应难以完全消除，即使通过拉丁方排列也只能均衡而非消除。
> - 受试者疲劳或练习效应可能混淆处理效应。

## 使用此方法的研究

> [!example]
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 介绍重复测量设计的逻辑、[[Order Effects|顺序效应]]挑战及拉丁方排列应对方案。
