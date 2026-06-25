---
title: Perpetual Inventory Method
aliases:
  - "永续盘存法"
  - PIM
  - "perpetual inventory equation"
summary: "通过投资流量数据和折旧率递推估算资本存量的标准方法，广泛用于增长核算和TFP测算"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 8
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - capital-stock
  - growth-accounting
  - tfp-measurement
  - national-accounting
related_concepts:
  - "[[Total Factor Productivity]]"
  - "[[Epistemology]]"
  - "[[Data Transformation]]"
  - "[[Heterogeneity]]"
  - "[[Hypothesis]]"
  - "[[Causality]]"
  - "[[Variable]]"
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Glitz_2020_AER]]"
confidence: medium
status: draft
created: 2026-06-26
updated: 2026-06-26
---

# Perpetual Inventory Method

---

## 定义

> [!def] 方法定义
> 永续盘存法（Perpetual Inventory Method, PIM）是通过投资流量数据递推估算资本存量的标准方法。其核心方程为 $K_{jt} = I_{jt} + (1-\delta) K_{j,t-1}$，其中 $K_{jt}$ 为资本存量，$I_{jt}$ 为固定资本投资，$\delta$ 为折旧率。初始资本存量通常通过稳态公式 $K_{j0} = I_{j0} / (g_j + \delta)$ 估算，其中 $g_j$ 为投资序列的平均几何增长率。

> [!method-scope] 方法范围
> - **研究对象** 国民经济核算或行业层面分析中的实物资本存量。
> - **问题类型** 测量——估计不可直接观测的资本存量水平，为 [[Total Factor Productivity|TFP]] 测算和增长核算提供输入。
> - **分析单位** 国家、行业、地区等宏观经济单位。
> - **输出形式** 资本存量时间序列、资本劳动比、人均资本等。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 国民经济核算传统——通过间接推算法将可观测的流量[[Data Transformation|数据转换]]为不可观测的存量估计。
> - **研究者角色** 研究者需要选择折旧率、设定初始资本存量计算方式和处理资产[[Heterogeneity|异质性]]。
> - **有效性标准** 资本存量估计对折旧率和初始存量[[Hypothesis|假设]]的敏感性应在合理范围内；与独立数据源（如企业调查或财富调查）的交叉验证。
> - **不声称回答的问题** PIM 本身不提供[[Causality|因果推断]]；仅提供资本存量这一个投入[[Variable|变量]]的测量。

> [!method-stack] 方法层级
> - **研究设计** 增长核算、发展核算、[[Total Factor Productivity|TFP]] 测算
> - **数据收集** 固定资本投资时间序列（通常来自国民经济核算）、资产价格指数
> - **分析方法** 递推计算
> - **辅助技术** 初始存量稳态假设、折旧率校准、不同资产类型的加权

---

## 研究程序

> [!proc] 通用程序
> 1. 获取行业层面（或国家层面）的固定资本投资时间序列 $I_{jt}$。
> 2. 选择折旧率 $\delta$（文献常用 0.04–0.08，Caselli 2005 使用 0.06）。
> 3. 计算初始资本存量：$K_{j0} = I_{j0} / (g_j + \delta)$，其中 $g_j$ 为投资在前几年的平均几何增长率。
> 4. 递推计算各年资本存量：$K_{jt} = I_{jt} + (1-\delta) K_{j,t-1}$。
> 5. 结合就业数据计算资本劳动比 $k_{jt} = K_{jt} / L_{jt}$，代入 [[Total Factor Productivity|TFP]] 计算公式。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 国民经济核算、行业生产率比较、增长核算——只要存在可靠的投资流量数据和适当的折旧率校准。[[Argument_Glitz_2020_AER|Glitz & Meyersson (2020, p.1075)]]
> - **谨慎使用** 投资序列较短时初始存量估算对稳态[[Hypothesis|假设]]较敏感；转型经济体或结构性断裂时期（如战争、制度变革）的稳态假设可能不成立。
> - **不适合使用** 缺少投资流量数据；资产构成高度异质且折旧率差异很大但无法区分资产类型的情况。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 初始资本存量估计对早期投资数据质量敏感；折旧率选择直接影响资本存量水平；未能区分不同类型资本（建筑、设备、软件）的异质折旧率。
> - **适用边界** 适用于宏观加总层面；微观企业层面数据若可得则直接使用账面资本存量更可靠。
> - **误用风险** 将不同折旧率设定下的资本存量直接进行水平比较而不做敏感性分析。
> - **补救方式** 报告不同折旧率（如 $\delta = 0.04, 0.06, 0.08$）下的结果；使用 Penn World Table 的替代方法（固定资本产出比计算初始存量）；与独立数据源交叉验证。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Total Factor Productivity]] | 概念 | PIM 提供资本存量估计，是 TFP 测算的关键上游步骤 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Glitz_2020_AER|Glitz & Meyersson (2020)]] — 使用 PIM 对 16 个行业 1950–1989 年的两德资本存量进行递推估算（基线 $\delta = 0.06$），并检验了 $\delta = 0.04$ 到 0.08 范围内的敏感性。
