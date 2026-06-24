---
title: Time Series Design
aliases:
  - 时间序列设计
  - time series quasi-experiment
  - interrupted time series
summary: "准实验设计的一种，对非随机取样的组在接受实验处理前后各进行多次重复测量，通过比较前后测数列的变化趋势来判断处理效果"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 1
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
tags:
  - method/experimental-design
  - source/textbook
  - paradigm/positivist
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_QiMei_2015_EducationalResearchMethods]]"
confidence: medium
status: draft
created: 2026-06-25
updated: 2026-06-25
---

# Time Series Design

---

## 定义

> [!def] 时间序列设计（Time Series Design）
> 时间序列设计是对一个非随机取样的实验组（或控制组），在接受实验处理之前和之后，重复接受若干次测量，而非仅在处理前后各接受一次测量的准实验设计（齐梅, 2015, Ch.4）。若前测每一次所得分数大致相同，但后测平均数高于前测，则表示该实验处理产生了正向效果。

> [!method-scope] 方法范围
> - **研究对象**：固定整组，常用于学校课堂教学研究。
> - **问题类型**：检验干预或处理是否引起结果的稳定变化趋势。
> - **分析单位**：组的时间序列测量数据。
> - **输出形式**：前后测数列的平均数比较，或两组时间序列的对比分析。

---

## 设计类型

### 单组时间序列设计

基本模式为：O₁ O₂ O₃ X O₄ O₅ O₆（处理前多次测量 → 处理 → 处理后多次测量）。处理前的观察称重复前测（repeated pretests），处理后的观察称重复后测（repeated posttests）（齐梅, 2015, Ch.4）。

### 相等时间样本设计

相等时间样本设计是时间序列的变体，实验处理与控制处理在相等的时间内交互间隔出现，每位被试均重复接受这些处理。模式为：X₁ O₁ X₀ O₂ X₁ O₃ X₀ O₄ …（X₁ 为实验处理，X₀ 为不实施处理）。为控制练习效应，可设计成 ABBA 顺序安排（A 为无处理，B 为实施处理）（齐梅, 2015, Ch.4）。

### 控制组时间序列设计

增加一个控制组，两组各有一系列时间前测和后测。基本模式为：

O₁ O₂ O₃ X O₄ O₅ O₆（实验组）
O₁ O₂ O₃ — O₄ O₅ O₆（控制组）

统计分析上，可以将两组各自的一系列时间前测成绩的平均数与一系列后测成绩的平均数加以比较，从成绩增减说明处理效果；也可以将两组之间的一系列时间前后测成绩相比较，判断两组接受不同处理所产生的效果（齐梅, 2015, Ch.4）。

---

## 效度特征

> [!feature] 时间序列设计的控制能力
> - **可有效控制**：成熟、测验、测量工具、统计回归、选择偏差、被试流失——通过系列前测与后测对一组被试的稳定变化有所了解，也能对两组处理前后的稳定变化进行比较。
> - **无法避免**：同时事件（历史因素）、霍桑效应、练习误差——测验的反作用或交互作用效果以及实验安排的反作用效果无法避免。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**：固定整组的课堂教学研究；需要在自然情境下检验干预效果；无法随机分组的场景。
> - **谨慎使用**：实验时间较长时，历史事件的影响可能增大；需要对练习效应和霍桑效应有额外控制措施。
> - **不适合使用**：需要严格因果推断的研究（优先选择真实验设计）。

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_QiMei_2015_EducationalResearchMethods|齐梅 (2015, Ch.4)]] — 系统介绍时间序列设计的三种形式及其效度控制特征。
