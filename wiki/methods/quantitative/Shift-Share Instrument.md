---
title: Shift-Share Instrument
aliases:
  - "Bartik Instrument"
  - "Bartik工具变量"
  - "shift-share IV"
  - "份额转移工具变量"
summary: "利用初始份额分布与总体冲击的交互项构建工具变量的因果识别方法，排除了当期策略性行为引起的内生性"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 8
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - instrumental-variable
  - causal-inference
  - econometrics
  - panel-data
related_concepts:
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Causality]]"
  - "[[Dependent Variable]]"
  - "[[Epistemology]]"
  - "[[Heterogeneity]]"
related_theories: []
related_methods:
  - "[[Fixed-Effect and Random-Effects Models]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Glitz_2020_AER]]"
confidence: medium
status: draft
created: 2026-06-26
updated: 2026-07-13
---

# Shift-Share Instrument

---

## 定义

> [!def] 方法定义
> Shift-Share Instrument（份额转移工具[[Variable|变量]]，也称 Bartik Instrument）利用初始时期的截面分布（share）与总时间序列变化（shift）的交互构造预测值，作为内生解释变量的工具变量。其识别[[Hypothesis|假设]]是初始份额分布是前定的，不受后续时期策略性行为的影响，因此由初始份额和总体变化交互产生的变异是外生的。

> [!method-scope] 方法范围
> - **研究对象** 当个体（行业、地区、国家）层面的某变量同时受总体趋势和个体策略选择影响时，用于分离外生变异。
> - **问题类型** [[Causality|因果]]识别——估计某处理变量对[[Dependent Variable|结果变量]]的因果效应，尤其在处理变量的分配本身可能是内生的情况下。
> - **分析单位** 行业、地区、城市、国家等面板数据中的横截面单位。
> - **输出形式** 工具变量回归的系数估计、一阶段 F 统计量、二阶段因果效应估计。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 计量经济学[[Causality|因果推断]]框架。前提是存在一个可用的初始截面分布，其本身不受后续处理分配策略的影响。
> - **研究者角色** 研究者需要论证初始份额的历史或制度外生性，并在实证中报告一阶段 F 统计量和弱工具[[Variable|变量]]检验。
> - **有效性标准** 相关性（一阶段 F > 10）和外生性（排他性约束），通常需结合定性论证和安慰剂检验。
> - **不声称回答的问题** Shift-share IV 识别的局部平均处理效应（LATE）——只能识别对"依从者"（compliers）的因果效应，不能直接推广到对整个样本的平均处理效应。

> [!method-stack] 方法层级
> - **研究设计** 面板数据因果推断，通常结合[[Fixed-Effect and Random-Effects Models|固定效应模型]]
> - **数据收集** 需两个数据源——初始截面份额分布和总体时间序列
> - **分析方法** 两阶段最小二乘法（2SLS）
> - **辅助技术** 弱工具变量检验（F 统计量）、过度识别检验、安慰剂检验

---

## 研究程序

> [!proc] 构建 Shift-Share 工具[[Variable|变量]]
> 1. 确定需要工具化的内生变量（如行业层面间谍情报流入）。
> 2. 选择一个初始时期（基准年），计算每个横截面单位中各子单位的份额权重 $\theta_{i,base}$。
> 3. 计算各子单位的行业分布 $\lambda_{ij,base}$（子单位 i 在行业 j 的活动占比）。
> 4. 计算总体层面的时间序列变化（shift），如子单位总活动量 $\sum_s I_s$。
> 5. 构造行业层面预测值：$Z_{jt} = \sum_{i \in base} \theta_{i,base} \cdot \lambda_{ij,base} \cdot \sum_{s=t-2}^{t} I_s$。
> 6. 将构造的预测值作为内生变量的工具变量进行 2SLS 估计。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 存在可信的初始截面分布且该分布不受后续处理分配策略影响的情况。特别是当处理[[Variable|变量]]的分配可能策略性地响应预期结果时。[[Argument_Glitz_2020_AER|Glitz & Meyersson (2020, pp.1080–1081)]]
> - **谨慎使用** 初始份额分布本身可能与未观测的截面特征相关，需要控制截面固定效应；总体 shift 本身可能受共同冲击驱动而与误差项相关。
> - **不适合使用** 无法获得可信的前定截面分布；初始时期本身已是策略选择的结果；shift 部分存在明显内生性。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 初始份额可能不是真正外生的——如果初始分布本身就是更早时期策略选择的结果，则工具[[Variable|变量]]仍可能存在内生性。总体 shift 可能存在未观测的共同冲击。
> - **适用边界** LATE 解释范围局限于"依从者"群体——即其处理状态确实被初始份额和总体变化交互驱动的那部分单位。
> - **误用风险** 将 LATE 直接解释为 ATE（平均处理效应）而忽略依从者[[Heterogeneity|异质性]]。
> - **补救方式** 结合定性历史论证初始份额的外生性；报告安慰剂检验结果；使用替代工具变量作为稳健性检验。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Glitz_2020_AER|Glitz & Meyersson (2020)]] — 使用 1970 年已在活动的斯塔西"老线人"的初始行业分布和相对生产率构造 shift-share 工具[[Variable|变量]]，处理工业间谍情报分配的内生性问题。
