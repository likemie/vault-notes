---
title: Test-Retest Reliability
aliases:
  - 重测信度
  - 再测信度
  - test-retest
  - stability reliability
  - 稳定性信度
summary: "评估同一测量工具在多次施测间得分稳定程度的信度指标，用于判断量表在不同时间点是否产生可比的分数"
type: concept
domain: "research-methodology"
related_count: 10
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - method/measurement
  - quantitative-research
  - reliability
related_concepts:
  - "[[Reliability]]"
  - "[[Operationalization]]"
  - "[[Internal Consistency]]"
  - "[[Inter-Rater Reliability]]"
  - "[[Construct]]"
  - "[[Variable]]"
  - "[[Hypothesis]]"
related_theories: []
related_methods:
  - "[[Pearson Product-Moment Correlation]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_QiMei_2015_EducationalResearchMethods]]"
  - "[[Argument_Creswell_2022_SAGE]]"
confidence: medium
status: draft
created: 2026-06-01
updated: 2026-06-26
---

# Test-Retest Reliability

---

## 定义

> [!def] 重测[[Reliability|信度]]（Test-Retest Reliability）
> 重测信度是使用同一测量工具在不同时间重复测量结果的一致性程度（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015]], Ch.5）。它回答的问题是：量表在重复施测间是否合理稳定？例如，一组受试者在时间点 1 完成 Perceived Stress Scale（PSS），一个月后再次完成同一量表——两次得分是否具有可比性？（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）

> [!concept-lens] 概念透镜
> - **含义** 重测信度是[[Reliability|信度]]作为**稳定性（stability）**的[[Operationalization|操作化]]形式——衡量测量工具跨越时间的分数一致性。它属于"跨时间一致性的稳定系数"。
> - **用途** 判断量表是适合评估长期稳定特征（高重测信度）还是对近期事件更敏感（低重测信度），为研究者在工具选择和研究设计时提供依据。
> - **边界** 重测信度不同于[[Internal Consistency|内部一致性]]（同一时间点各条目间的一致性）和[[Inter-Rater Reliability|评分者间信度]]（不同评分者间的一致性）。某些[[Construct|构念]]本身就不应具有高重测信度——如"当前情绪状态"应在短期内波动，高重测信度反而说明量表不够灵敏。

> [!quote]
> 这种信度形式关注的是量表在重复施测间是否随时间保持合理的稳定——例如，一组受试者在时间点 1 完成 PSS，一个月后再次完成同一量表，两次得分是否具有可比性？（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）
>
> *This form of reliability concerns whether the scale is reasonably stable over time with repeated administrations (e.g., is there a comparable score on the PSS taken by a group of participants at time 1 and then one month later?).*

---

## 核心要素

### 评估逻辑

> [!proc] 重测[[Reliability|信度]]评估四步骤
> 1. **首次施测** 在时间点 1 对一组受试者施测目标量表
> 2. **间隔后重测** 在适当的时间间隔后对同一组受试者再次施测同一量表。常用适当间隔为两星期到一个月之间（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015]], Ch.5；Creswell & Creswell, 2022, Ch8）
> 3. **计算相关系数** 一般使用皮尔逊积矩相关系数（[[Pearson Product-Moment Correlation]]）计算两次测量之间的相关。高相关（如 r > .70）表明量表具有良好的重测信度
> 4. **报告均值差异** 评估是否存在系统性变化（如练习效应或疲劳效应）

### 计算公式与解读

重测信度一般使用皮尔逊积矩相关系数（Pearson product-moment correlation coefficient）计算（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015]], Ch.5）：

> [!formula] Pearson 积矩相关系数
> $$r = \frac{\sum_{i=1}^{n}(X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n}(X_i - \bar{X})^2} \cdot \sqrt{\sum_{i=1}^{n}(Y_i - \bar{Y})^2}}$$

其中 $X_i$ 和 $Y_i$ 分别为第 $i$ 个受试者在首次施测和重测中的得分，$\bar{X}$ 和 $\bar{Y}$ 为两次施测的均值，$n$ 为受试者人数。分子为两[[Variable|变量]]的协方差，分母为两变量标准差的乘积——本质上衡量的是两次测量**共变程度**相对于各自变异的大小。

> [!ref-table] r 值的解读
> | r 值范围 | 相关强度 | 信度判定 |
> |---|---|---|
> | 0.80–1.00 | 强相关 | 完全可接受 |
> | 0.70–0.80 | 中等偏强 | 可以接受 |
> | 0.65–0.70 | 中等 | 勉强可以接受 |
> | < 0.65 | 弱相关 | 不可接受，需修订工具 |

> [!warning] Pearson r 的前提[[Hypothesis|假设]]
> - **线性关系** Pearson r 仅适用于变量间具有线性关系，不适用于非线性关系（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015]], Ch.10）
> - **连续变量** 两变量应为等距或比率变量
> - **正态分布** 两变量应近似服从正态分布
> - **无极端值** 极端值会显著扭曲相关系数

---

### 适用条件

> [!info] 适用范围与注意事项
> 重测信度一般适用于**事实性的问卷调查**，或不易受环境影响的**态度、意识等主观状况**。但它易受某些活动的影响，因此时间间隔不宜过长。选择适当的时间间隔需要基于对[[Construct|构念]]稳定性的理论理解：间隔过短可能受记忆效应影响（受试者记住前次回答），间隔过长可能反映构念本身的真实变化而非测量不稳定（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015]], Ch.5；[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。

> [!example] PSS 重测信度
> Perceived Stress Scale（PSS; Cohen et al., 1983）在很多已发表报告中具有良好的[[Internal Consistency|内部一致性]]（α = .84–.86），同时研究者也可以评估其重测信度——即 PSS 在间隔一个月后重复施测时是否产生稳定的知觉压力估计值。这一信息有助于判断 PSS 是适合评估长期压力水平（高重测信度）还是对近期事件更敏感（低重测信度）（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。

---

## 概念辨析

> [!contrast-table] 重测[[Reliability|信度]] vs [[Internal Consistency|内部一致性]] vs [[Inter-Rater Reliability|评分者间信度]]
> | 维度 | 重测信度 | [[Internal Consistency\|内部一致性]] | [[Inter-Rater Reliability\|评分者间信度]] |
> |---|---|---|---|
> | 核心问题 | 同一量表在不同时间是否一致？ | 同一时间点各条目是否一致？ | 不同评分者之间是否一致？ |
> | 信度类型 | 纵向信度（稳定性） | 横截面信度（条目间一致） | 评分者间信度（等值性） |
> | 施测次数 | 至少两次（不同时间） | 一次即可 | 至少两位评分者 |
> | 计算方式 | Pearson 积矩相关系数 | Cronbach α、Spearman-Brown 等 | Pearson 或 Kendall/Spearman 等级相关系数 |

---

## 争议与批评

> [!warning] 注意事项
> - **时间间隔的选择** 重测[[Reliability|信度]]的高低取决于两次施测之间的时间间隔。间隔过短可能受记忆效应影响，间隔过长可能反映[[Construct|构念]]本身的真实变化。常用适当间隔为两星期到一个月之间（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015]], Ch.5）。
> - **工具修改失效** 当研究者修改工具或组合多个工具时，原有的重测信度证据不再适用于新工具，需重新评估（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。
> - **构念本身的特性** 某些构念本身就不应该具有高重测信度——例如"当前情绪状态"量表应在短期内波动，高重测信度反而说明量表不够灵敏。
> - **信度系数的评价标准** 一般认为信度系数低于 0.65 不可接受，0.65~0.70 勉强接受，0.70~0.80 可以接受，高于 0.80 完全接受（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015]], Ch.5）。
