---
title: Imputation Methods
aliases:
  - 插补方法
  - 缺失值插补
  - imputation
  - missing data imputation
summary: "用合理值填充缺失数据以呈现完整数据集并减少无回应偏倚的统计技术，包括回归插补、热卡方法、最近邻、多重插补和倾向得分赋权等方法"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 10
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - quantitative-research
  - survey
  - missing-data
  - data-processing
related_concepts:
  - "[[Questionnaire]]"
  - "[[Variable]]"
  - "[[Epistemology]]"
  - "[[Hypothesis]]"
  - "[[Standard Error]]"
  - "[[Sample Size Determination]]"
  - "[[Heterogeneity]]"
  - "[[Response Bias]]"
related_methods:
  - "[[Survey Research]]"
  - "[[Multiple Regression]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch13]]"
confidence: medium
status: draft
created: 2026-07-11
updated: 2026-07-11
---

# Imputation Methods

## 定义

> [!def] 方法定义
> 插补方法（Imputation Methods）是用"合理值"填充缺失数据的技术，使数据集完整同时减少无回应偏倚——无回应者的值可能系统性不同于有回应者，直接删除会扭曲结果（Durrant, 2009, p. 295）。Rubin (1987)、Little & Rubin (1989)、Allison (2001)、Dale (2006, p. 149–150)和 Durrant (2006, 2009)系统回顾了这一方法家族。

> [!method-scope] 方法范围
> - **研究对象** 调查或实验数据中的缺失值（整份[[Questionnaire|问卷]]缺失或特定题项缺失）。
> - **问题类型** 减少因无回应导致的偏倚、呈现完整数据集、支持后续统计分析。
> - **分析单位** [[Variable|变量]]或个案层面的缺失数据。
> - **输出形式** 替换缺失值后的完整数据集。

插补方法的选择首先取决于无回应集中在一个变量还是多个变量、是否存在可识别的无回应模式：如果无回应在多个变量之间随机分布且无明显模式，问题可能较小；如果是对一个或多个变量的系统性无回应，则更严重（Durrant, 2009, p. 295）。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch13|Cohen et al. (2011d)]]

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 在缺失数据机制[[Hypothesis|假设]]（完全随机缺失 MCAR、随机缺失 MAR、非随机缺失 MNAR）下，利用可观测数据的信息推断不可观测数据。
> - **研究者角色** 需判断缺失模式、选择适合的插补方法、检查插补后数据的合理性。
> - **有效性标准** 插补值是否合理（不超出[[Variable|变量]]取值范围）、插补后数据的分布是否与原数据一致、多重插补的[[Standard Error|标准误]]是否适当反映了不确定性。
> - **不声称回答的问题** 插补不能恢复已丢失的真实信息——它只是基于已有数据的合理推断；不能纠正因非随机缺失导致的系统性偏倚（除非模型正确指定了缺失机制）。

---

## 主要方法

> [!chain-link] 插补方法链：从简单均值到倾向得分赋权
> - **回归插补**
>   使用辅助[[Variable|变量]]通过回归技术计算缺失值（p.296）。
>   *原理：利用缺失变量与已知辅助变量之间的统计关系进行预测。*
> - **热卡方法（hot deck）**
>   基于辅助变量分数构建参与者子群体，将无回应者的结果与该子群体中有回应者的非缺失结果比较（p.297）。
>   *原理：相似背景的人倾向于给出相似回答，同一子群体内的值可以合理替代。*
> - **最近邻方法（nearest neighbour）**
>   使用数据与缺失者差异尽可能最小的人的结果替代缺失值。
>   *原理：在多个变量上最接近的个案是最佳"捐赠者"。*
> - **多重插补（multiple imputation）**
>   生成多个完整数据集（每个缺失值用不同合理值填充），分别分析后综合结果，从而反映插补的不确定性。
>   *原理：单次插补低估了[[Standard Error|标准误]]，多次插补通过结果间的变异来校正。*
> - **分数插补（fractional imputation）**
>   为每个缺失值生成多个候选值并赋予分数权重，在后续分析中加权使用，避免丢弃任何可能值。
> - **倾向得分赋权（propensity score weighting）**
>   基于参与倾向进行赋权调整。
>   *原理：根据可观测特征估计每位受访者的回应概率，对低概率群体赋予更高权重以校正偏倚。*

方法选择取决于分析目的、涉及的变量、数据类型、缺失模式以及插补方法[[Hypothesis|假设]]的特征和适合性。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch13|Cohen et al. (2011d)]]

---

## 研究程序

> [!proc] 插补方法的选择与应用
> 1. 识别缺失数据的模式和范围（单位无回应还是题项无回应、随机还是系统性缺失）。
> 2. 判断缺失数据机制（MCAR、MAR 还是 MNAR）——这决定了适用的方法范围。
> 3. 根据分析目的、[[Variable|变量]]类型和数据特征选择插补方法。
> 4. 执行插补，检查插补值的合理性（是否在变量有效取值范围内）。
> 5. 若使用多重插补，分别分析各数据集后综合结果；若使用倾向得分赋权，检查权重的分布和极端值。
> 6. 进行敏感性分析以评估插补方法和[[Hypothesis|假设]]对结论的影响。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 缺失数据比例不高且存在可用于预测缺失值的辅助[[Variable|变量]]；缺失机制为 MAR（随机缺失）时，多重插补和回归插补效果良好；调查数据中个别题项缺失而非整份[[Questionnaire|问卷]]缺失的场景。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch13|Cohen et al. (2011d)]]
> - **谨慎使用** 缺失比例较高（如超过 30–40%）时，即使最复杂的插补方法也难以可靠恢复信息；缺失机制可能为 MNAR 时，需明确报告插补[[Hypothesis|假设]]的局限性；[[Sample Size Determination|样本量]]较小时，复杂插补方法的优势可能不显著。
> - **不适合使用** 缺失数据占绝大多数（接近完全缺失）；缺失机制明确为 MNAR 且无法合理指定缺失模型；缺失是由研究设计本身决定的结构性缺失（如跳转逻辑过滤的题项）——此时不应插补。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 插补值依赖于插补模型的[[Hypothesis|假设]]——模型错误指定会导致系统性偏倚；单次插补低估[[Standard Error|标准误]]，使后续推断过于"显著"；插补可能掩盖数据质量的真实问题，使研究者对结论过度自信。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch13|Cohen et al. (2011d)]]
> - **适用边界** 插补的有效性取决于辅助[[Variable|变量]]的质量——辅助变量需与缺失变量高度相关且自身几乎完整；不同插补方法假设不同的缺失机制，方法选择错误会导致偏倚。
> - **误用风险** 对[[Heterogeneity|异质性]]总体使用均值插补，假设同质性可能严重扭曲结果；将插补后的数据当作真实观测值进行后续分析而不报告插补过程；忽视插补引入的额外不确定性。
> - **补救方式** 优先使用多重插补而非单一插补以反映不确定性；进行敏感性分析（比较不同插补方法的结果稳定性）；明确报告缺失比例、缺失模式、插补方法和假设；当缺失比例较高时，同时报告完整案例分析作为参照。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Survey Research]] | 前置方法 | 调查中的无回应（单位/题项）是插补方法最主要的应用场景。 |
> | [[Response Bias]] | 相关概念 | 无回应偏倚是插补方法试图校正的核心问题——无回应者的值可能系统性不同于有回应者。 |
> | [[Multiple Regression]] | 基础方法 | 回归插补以多元回归为数学基础。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch13|Cohen et al. (2011)]] — 系统介绍了回归插补、热卡方法、最近邻方法、多重插补、分数插补和倾向得分赋权的原理与选择框架。
