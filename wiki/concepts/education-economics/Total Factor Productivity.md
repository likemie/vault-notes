---
title: Total Factor Productivity
aliases:
  - 全要素生产率
  - TFP
  - multi-factor productivity
  - Solow residual
summary: "衡量扣除资本和劳动投入贡献后产出增长剩余部分的生产率指标，用于衡量技术进步和技术效率变化"
type: concept
domain: "education-economics"
related_count: 7
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - productivity
  - economic-growth
  - technological-change
  - production-function
  - measurement
related_concepts:
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Alternative Hypothesis]]"
  - "[[Technology Transfer]]"
related_theories: []
related_methods:
  - "[[Perpetual Inventory Method]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Glitz_2020_AER]]"
related_instruments:
  - "[[VALUE Rubrics]]"
confidence: medium
status: draft
created: 2026-06-26
updated: 2026-06-26
---

# Total Factor Productivity

---

## 定义

> [!def] 核心定义
> 全要素生产率（Total Factor Productivity, TFP）衡量产出增长中无法由要素投入（资本和劳动）增长解释的剩余部分，反映技术进步、效率改善、规模经济以及知识积累等无法直接观测的因素对生产率的贡献。在 C-D 生产函数框架下，TFP 通常通过索洛残差（Solow residual）方法推算：$\ln A_{jt} = \ln y_{jt} - \alpha_j \ln k_{jt}$，其中 $y_{jt}$ 是人均产出，$k_{jt}$ 是资本劳动比，$\alpha_j$ 是资本份额。

> [!concept-lens] 概念透镜
> - **含义** TFP 指向生产函数中不能用可观测要素投入解释的部分——它是"我们无知程度的度量"（Abramovitz, 1956），包含了技术进步、组织创新、管理效率、知识溢出和测量误差等。
> - **用途** 在增长核算、跨国生产率比较和技术扩散研究中，TFP 是衡量技术差距和追赶速度的核心指标。[[Argument_Glitz_2020_AER|Glitz & Meyersson (2020)]] 利用两德行业 TFP 差距的变化作为工业间谍效果的因[[Variable|变量]]。
> - **边界** TFP 不区分技术进步的具体来源（自主创新还是技术采用）；TFP 水平的跨国比较高度依赖价格折算、资本份额校准和折旧率[[Hypothesis|假设]]，不同校准可能导致显著差异。

---

## 核心要素

> [!feature] TFP 测算的核心要素
> - **产出度量** 通常使用总增加值（gross [[VALUE Rubrics|VALUE]] added），需转换为不变价格以消除通胀影响。[[Argument_Glitz_2020_AER|Glitz & Meyersson (2020)]] 在处理东德数据时，面临中央计划价格非市场决定的特殊困难，通过 Heske (2009, 2013) 的回顾性国民经济核算数据解决。
> - **资本存量估算** 使用[[Perpetual Inventory Method|永续盘存法]]（[[Perpetual Inventory Method]]）从投资序列推算：$K_{jt} = I_{jt} + (1-\delta) K_{j,t-1}$，需要设定初始资本存量和折旧率 $\delta$。
> - **资本份额参数** $\alpha_j$ 在竞争市场中等于资本收入在增加值中的份额；在非竞争环境（如东德计划经济）中需要用代理[[Variable|变量]]或[[Alternative Hypothesis|替代假设]]校准。
> - **劳动投入** 通常以就业人数或工时度量，隐含[[Hypothesis|假设]]人力资本同质。

---

## 围绕概念形成的命题

### 命题类型一：TFP 作为技术差距的度量

> [!claim] Abramovitz (1956)
> TFP 本质上是"我们无知程度的度量"（a measure of our ignorance），它不仅包含技术进步，还包含测量误差、省略[[Variable|变量]]、规模经济和外部性等无法一一分离的因素。

> [!claim] [[Argument_Glitz_2020_AER|Glitz & Meyersson (2020)]]
> 在两德比较中，log TFP 差距的变动（$\Delta \ln A_{Wjt} - \Delta \ln A_{Ejt}$）可以作为工业间谍[[Technology Transfer|技术转移]]效果的度量——间谍情报流入缩小了 TFP 差距，即加速了东德相对于西德的技术追赶。[[Argument_Glitz_2020_AER|Glitz & Meyersson (2020, pp.1075–1078)]]

---

## 实证发现

> [!stat-cards]- 两德行业 TFP 数据（[[Argument_Glitz_2020_AER|Glitz & Meyersson, 2020]]）
> - **1.490** 两德 log TFP 的非加权平均差距（1970–1989）。（p.1077, Table 1）
> - **21.8%** 1989 年东德 TFP 相对于西德的比率（就业加权平均）。（p.1097）
> - **19.2%** 1979 年东德相对西德的 TFP 比率——1970 年代持续下降。（p.1097）

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Glitz_2020_AER|Glitz & Meyersson (2020)]] — 利用行业 TFP 差距变化评估工业间谍的生产率效应，详细展示了在非竞争环境中校准 TFP 的方法论挑战和应对策略。
