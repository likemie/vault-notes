---
title: Coupling Coordination Model
aliases:
  - 耦合协调模型
  - CCDM
  - Coupling Coordination Degree Model
summary: "一种基于系统论的多子系统协同发展水平测度方法，通过耦合度C衡量相互作用强度、协调度D综合评估协同演进水平，广泛应用于教育、经济、环境等复杂系统的综合评价"
type: method
method_type: quantitative
tags:
  - method/composite-index
  - method/spatial-analysis
  - theme/systems-theory
related_concepts:
  - "[[Causality]]"
related_theories:
  - "[[Coupling Coordination Theory]]"
related_methods:
  - "[[LISA Time Path]]"
  - "[[LISA Spatiotemporal Transition]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Fan_Song_Zhai_2024_RSEE]]"
confidence: medium
status: draft
created: 2026-06-12
updated: 2026-06-12
---

# Coupling Coordination Model

---

## 定义

> [!info]
> 耦合协调模型（Coupling Coordination Degree Model, CCDM）是一种基于系统论的多子系统协同发展水平测度方法。它同时评估两个维度：耦合度（$C$）衡量子系统之间相互作用的强度，协调度（$D$）综合评估耦合强度与发展水平的协同演进程度。该模型的核心贡献在于避免了仅使用耦合度可能出现的"低水平高耦合"误判————当所有子系统均处于低发展水平时，耦合度仍可接近最大值。

> [!quote]
> 耦合指两个或多个子系统之间相互影响和相互作用的程度，也可以反映不同子系统之间的约束程度。耦合度可以衡量不同子系统之间的协同发展水平，并在一定程度上描述不同子系统发展水平的差异。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 67)]]
> Original: Coupling refers to the extent of mutual influence and interaction among two or more subsystems, and it can also reflect the degree of constraint between different subsystems. The degree of coupling can measure the level of collaborative development between different subsystems.

---

## 研究程序

> [!abstract] 核心公式体系
> 耦合协调模型的计算包含三个核心步骤。

> [!line-a] 步骤一：计算有序度
> 首先对各指标进行min-max归一化处理消除量纲，得到取值 $[0, 1]$ 的标准化值 $g_{ij}$。各子系统的综合有序度 $G_j = \sum f_i g_{ij}$，其中 $f_i$ 为综合权重。

> [!line-b] 步骤二：计算耦合度 $C$
> $C = \left[ \dfrac{e_1 \times e_2 \times e_3}{\left(\frac{e_1+e_2+e_3}{3}\right)^3} \right]^{\frac{1}{3}}$。耦合度 $C$ 的本质是衡量子系统之间的离散程度：当三个值完全相等时几何平均值等于算术平均值，$C=1$（完美耦合）；差异越大 $C$ 趋近于 $0$。该公式借鉴了物理学中的容量耦合概念。

> [!line-b] 步骤三：计算协调度 $D$
> $D = \sqrt{C \times T}$，其中 $T = \alpha e_1 + \beta e_2 + \gamma e_3$ 为综合发展指数，$\alpha$、$\beta$、$\gamma$ 为各子系统权重（通常等权，$\alpha = \beta = \gamma = 1/3$）。协调度采用几何平均而非算术平均，具有天然的"短板惩罚"特性————耦合度 $C$ 或发展水平 $T$ 任一偏低都会拉低 $D$，只有两者同时达到较高水平才能得高分。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 67–68)]]

---

## 资料与分析

> [!info]
> 该模型所需资料为面板数据或多截面数据，每个子系统需构建包含多项指标的评价指标体系。分析流程通常包括：
> - **指标赋权**：可采用主观赋权（如层次分析法AHP）、客观赋权（如熵权法EWM）或组合赋权确定各指标权重
> - **有序度计算**：逐年度逐地区计算各子系统综合有序度
> - **耦合协调度计算**：代入选定的子系统权重计算 $C$ 和 $D$
> - **等级划分**：常用自然断点法（Natural Breaks）将 $D$ 值分为低、中、高等级，也可采用等间距法或分位数法

---

## 适用场景

> [!success]
> 适合回答"多个系统之间的协同发展程度如何？在哪些区域/时间段协同水平较高或较低？"这类综合评价问题。尤其适合以下场景：
> - 教育、科技、人才等社会子系统的耦合协调评价
> - 经济-环境-能源等可持续发展系统评价
> - 城镇化与生态环境的交互关系测度
> - 不适合回答[[Causality|因果性]]问题————高 $D$ 值不能推断因果关系，可能由第三个共同因素同时驱动

---

## 局限性

> [!warning]
> - **耦合度陷阱**：当子系统均处于低发展水平时 $C$ 可能虚高，必须结合 $D$ 综合判断。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 67)]]
> - **[[Causality|因果性]]缺失**：$D$ 是描述性指标而非因果推断工具，高耦合协调度不等于存在因果关系
> - **权重敏感性**：$T$ 中子系统权重 $\alpha$、$\beta$、$\gamma$ 的选择影响 $D$ 值，不同权重设定可能导致不同等级划分
> - **时间不变性假设**：当权重基于全时段数据计算时，未考虑指标重要性随时间的变化

---

## 相关理论

> [!tip]
> - General Systems Theory — 耦合协调模型以系统论为理论基础，将各子系统视为相互关联、相互制约的组成部分
> - [[Coupling Coordination Theory]] — 耦合协调理论为模型提供了机制层面的解释框架

---

## 使用此方法的研究

> [!example]
> - [[Argument_Fan_Song_Zhai_2024_RSEE]] — 使用耦合协调模型测度中国30个省份教育-科技-人才（EST）一体化发展水平，结合[[LISA Time Path|LISA时空路径]]和[[LISA Spatiotemporal Transition|空间转移矩阵]]分析时空格局演变
