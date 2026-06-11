---
title: Combined Weighting AHP-EWM
aliases:
  - AHP-熵权法组合赋权
  - AHP-EWM Combined Weighting Method
  - 主客观组合赋权
summary: "一种综合主观层次分析法（AHP）与客观熵权法（EWM）的指标赋权方法，通过最小二乘决策（LSD）模型最小化主客观权重偏差，平衡专家判断与数据变异两种信息来源"
type: method
method_type: quantitative
tags:
  - method/weighting
  - method/composite-index
  - method/decision-analysis
related_concepts: []
related_theories: []
related_methods:
  - "[[Coupling Coordination Model]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Fan_Song_Zhai_2024_RSEE]]"
confidence: medium
status: draft
created: 2026-06-12
updated: 2026-06-12
---

# Combined Weighting AHP-EWM

---

## 定义

> [!info]
> AHP-熵权法组合赋权（Combined Weighting AHP-EWM）是一种将主观赋权和客观赋权相结合的多指标权重确定方法。它分别采用层次分析法（Analytic Hierarchy Process, AHP）获取基于专家判断的主观权重，采用熵权法（Entropy Weight Method, EWM）获取基于数据变异程度的客观权重，再通过最小二乘决策（Least Square Decision, LSD）模型求解综合权重，使综合权重与两种来源权重的总偏差最小。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 66–67)]]

> [!quote]
> 综合权重向量 $f = (f_1, f_2, \dots, f_n)^T$，通过最小化与主观权重向量 $v$ 和客观权重向量 $g$ 的偏差平方和求解，约束条件为 $\sum f_i = 1, f_i \geq 0$。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 67)]]
> Original: The least square decision (LSD) model is established to control the deviation of the judgment index decision results in a small range.

---

## 研究程序

> [!abstract]
> 组合赋权分为三个独立模块，各模块可独立执行，LSD模型作为最终的融合机制。

> [!line-a] 模块一：层次分析法（AHP）——主观赋权
> AHP依赖专家知识对指标进行两两比较。操作流程：组织专家对 $n$ 个指标进行两两重要性打分（通常使用1–9标度法）→ 构造判断矩阵 → 计算特征向量得到主观权重向量 $v$。AHP的优势在于融入领域知识，但结果依赖专家背景和判断质量，存在主观偏误风险。

> [!line-b] 模块二：熵权法（EWM）——客观赋权
> EWM基于信息熵原理：指标变异越大→信息量越大→权重越高。操作流程：计算每个指标的熵值 $e_j = -k \sum p_{ij} \ln p_{ij}$ → 计算信息效用值 $1 - e_j$ → 归一化得到客观权重向量 $g$。EWM的优势在于忠实于数据分布，但可能赋予实际不重要但变异大的指标过高权重。

> [!line-b] 模块三：LSD模型——偏差最小化
> LSD模型求解综合权重 $f$，使 $f$ 与主观权重 $v$ 和客观权重 $g$ 的偏差平方和最小：$\min H(f) = \sum_{i=1}^{m} \sum_{j=1}^{n} \{[(g_j - f_j)X_{ij}]^2 + [(v_j - f_j)X_{ij}]^2\}$。LSD的数学本质是在"专家认为重要"和"数据表现重要"之间寻找最优折中。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 67)]]

---

## 适用场景

> [!success]
> 适合构建综合评价指标体系时需要确定指标权重的场景，尤其当：
> - 既有领域专家知识可用、又有充分数据支撑时
> - 单一赋权方法（纯主观或纯客观）难以令人信服时
> - 指标体系中同时包含"易于量化的硬指标"和"难以量化的软指标"时（如教育关注度、技术复杂度）

> [!warning]
> 当AHP专家过程和评判质量不透明时，组合赋权可能实际退化为以EWM为主的客观驱动模式，失去"组合"的方法论意义。

---

## 局限性

> [!warning]
> - **AHP过程不透明**：若未报告专家数量、背景及评判过程，AHP方法论的严谨性无法评估。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 71)]]
> - **时间不变性假设**：组合权重基于全时段数据计算，未考虑指标重要性随时间推移的变化
> - **LSD模型的对称性假设**：LSD对主观和客观权重偏差施以同等惩罚，但两者的可靠性在实际中可能不等

---

## 相关方法

> [!tip]
> - Analytic Hierarchy Process — AHP是该组合方法的子模块
> - Entropy Weight Method — EWM是该组合方法的子模块
> - [[Coupling Coordination Model]] — 组合赋权常与耦合协调模型配合使用，前者确定指标权重，后者计算系统协同水平

---

## 使用此方法的研究

> [!example]
> - [[Argument_Fan_Song_Zhai_2024_RSEE]] — 使用AHP-EWM-LSD组合赋权确定15项EST评价指标的权重，为[[Coupling Coordination Model|耦合协调模型]]提供综合权重输入
