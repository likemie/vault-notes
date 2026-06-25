---
title: Internal Consistency
aliases:
  - 内部一致性
  - Cronbach alpha
  - Cronbach α
  - 克隆巴赫系数
  - internal consistency reliability
summary: "信度作为内部一致性的形式，衡量多项目量表中各条目测量同一底层构念的程度，通过半分法与Spearman-Brown公式或Cronbach alpha量化，后者等效于所有可能半分方式的Spearman-Brown校正值的平均值"
type: concept
domain: "research-methodology"
related_count: 12
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - method/measurement
  - quantitative-research
  - reliability
related_concepts:
  - "[[Reliability]]"
  - "[[Construct]]"
  - "[[Test-Retest Reliability]]"
  - "[[Inter-Rater Reliability]]"
  - "[[Heterogeneity]]"
  - "[[Split-Half Reliability]]"
  - "[[Document]]"
  - "[[Study Population and Sample]]"
  - "[[Purpose Statement]]"
related_methods:
  - "[[Survey Research]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10]]"
status: draft
created: 2026-05-31
updated: 2026-06-23
---
# Internal Consistency

---

## 定义

> [!def] 核心定义
> 内部一致性（Internal consistency）是[[Reliability|信度]]的一种形式，衡量多项目量表中各条目（items）是否在测量同一底层[[Construct|构念]]。与测试/重测和等价形式信度不同——它们要求两次测试或工具施测——内部一致性只需要**一次**施测。其基本逻辑是：如果量表的所有条目都在测量同一个构念，那么这些条目之间应该有适当的相互关联。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch8)]]

在 Carmines & Zeller (1979) 的量化信度三类型框架中，内部一致性是与稳定性（[[Test-Retest Reliability|重测信度]]）和等值性（等价形式和[[Inter-Rater Reliability|评分者间信度]]）并列的第三大信度类型（pp.202–204）。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10)]]

> [!citation-card]- Creswell 对内部一致性的定义
> 对于多项目工具来说，最重要的信度形式是工具的内部一致性——即工具上各组条目以相同方式运作的程度。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch8)]]
>
> *The most important form of reliability for multi-item instruments is the instrument's internal consistency—the degree to which sets of items on an instrument behave in the same way.*

> [!concept-lens] 概念透镜
> - **含义** 内部一致性回答的核心问题是：量表中的这些条目是否在协同一致地测量同一个东西？它衡量的是**项目之间**（而非受试者之间或时间点之间）的一致性。
> - **用途** 在多项目量表（如态度量表、人格测验、能力测试）的开发与验证中，内部一致性是最核心的信度指标。它是[[Survey Research|调查研究]]和量表开发中最常报告的信度形式。
> - **边界** 内部一致性不同于[[Test-Retest Reliability|重测信度]]（后者关注跨时间的稳定性），也不同于[[Inter-Rater Reliability|评分者间信度]]（后者关注跨评分者的一致性）。它衡量的是单一时间点、单次施测中条目间的相互关联。

---

## 概念辨析

> [!contrast-table] 内部一致性 vs [[Test-Retest Reliability|重测信度]] vs [[Inter-Rater Reliability|评分者间信度]]
> | 维度 | 内部一致性 | [[Test-Retest Reliability\|重测信度]] | [[Inter-Rater Reliability\|评分者间信度]] |
> |---|---|---|---|
> | **核心问题** | 条目是否一致地测量同一[[Construct\|构念]]？ | 测量在不同时间是否稳定？ | 不同评分者是否一致？ |
> | **施测次数** | 一次 | 两次（间隔一定时间） | 一次（但多位评分者） |
> | **偏差来源** | 条目之间的[[Heterogeneity\|异质性]] | 时间带来的变化 | 评分者之间的主观差异 |
> | **典型指标** | Cronbach's α、Spearman-Brown | 前后测相关系数 | Cohen's κ、Fleiss' κ、ICC |
> | **[[Reliability\|信度]]类型** | 内部一致性 | 稳定性 | 等值性 |

---

## 核心要素

### 半分法与 Spearman-Brown 公式

内部一致性的传统检验方法是**半分法**（[[Split-Half Reliability|split-half]] method），其操作步骤和公式如下（pp.202–203）：

> [!proc] 半分法的操作流程
> 1. **将测试对半分割** 将测试项目分为两半，确保每半在项目难度和内容上匹配。若测试有 20 个项目且难度递增，可将偶数号项目分给一组、奇数号分给另一组，使两半在内容和累积难度上更接近
> 2. **分别评分** 每半分单独评分，计算每位受试者在每半上的得分
> 3. **计算相关系数** 计算两半得分之间的相关系数 $r$（Pearson 或 Spearman）
> 4. **Spearman-Brown 校正** 因为将测试减半会降低[[Reliability|信度]]，需要用公式从半测试相关**推算出完整测试的信度**

> [!formula-step] Spearman-Brown 公式
> $$
> \text{reliability} = \frac{2r}{1 + r}
> $$
>
> **$r$ = 测试两半之间的实际相关系数**。公式校正了"项目减半导致信度降低"这一衰减效应——从两半之间的相关推算出完整测试的信度。
>
> **示例**：若 $r = 0.85$，则完整测试的信度为 $\frac{2 \times 0.85}{1 + 0.85} = \frac{1.70}{1.85} = 0.919$。鉴于系数最大值为 1.00，0.919 表明完整测试的内部一致性非常高。

[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, pp. 202–203)]]

---

### Cronbach's Alpha

Cronbach alpha 是内部一致性最常用的量化指标，提供了**跨项目相关**的系数——即每个项目与所有其他相关项目之和的相关。与半分法不同，alpha 不需要将测试分成两半：它**等效于所有可能半分方式的 Spearman-Brown 校正值的平均值**（p.203）。

> [!formula-step] Cronbach's Alpha 公式
> $$
> \alpha = \frac{k}{k - 1} \left(1 - \frac{\sum \sigma^2_i}{\sigma^2_{\text{total}}}\right)
> $$
>
> **$k$ = 量表中的项目总数**；$\sum \sigma^2_i$ = 所有项目各自方差的**总和**；$\sigma^2_{\text{total}}$ = 量表**总分**的方差。
>
> **公式逻辑**：$\frac{\sum \sigma^2_i}{\sigma^2_{\text{total}}}$ 衡量"各项目独自变异的比例"——项目之间越一致，该比值越小，$\left(1 - \text{比值}\right)$ 接近 1，$\alpha$ 就高。$\frac{k}{k-1}$ 是校正因子——项目数越少，校正力度越大，防止项目少的量表获得虚高值。

[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, p. 203)]]

---

### Alpha 的解读

> [!feature] Cronbach's α 解读标准
> - **α ≥ 0.90** 优秀——但可能暗示条目间存在**冗余**（条目过于相似，未提供独特增量信息）
> - **0.70 ≤ α < 0.90** 最佳范围——条目间有良好一致性且不过度冗余
> - **α < 0.70** 信度不足——条目可能未测量同一[[Construct|构念]]，需要检查或删除低相关条目
> - **条目数量效应** α 受条目数量影响——条目越多，α 倾向于越高。比较不同长度量表的 α 值需谨慎

> [!example] Perceived Stress Scale (PSS) 实例
> 10 项的 Perceived Stress Scale（PSS; Cohen et al., 1983）在原始发表[[Document|文献]]中报告了三个独立[[Study Population and Sample|研究样本]]的内部一致性值 α = .84–.86。这些值落在最佳范围内，表明 PSS 的 10 个条目在一致地测量"知觉压力"这一[[Construct|构念]]。该量表可免费用于[[Purpose Statement|研究目的]]，只需引用原始来源。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch8)]]

---

## 争议与批评

> [!warning] 使用 Alpha 的注意事项
> - α 受条目数量影响——条目越多，α 值倾向于越高。因此比较不同长度量表的 α 值需要谨慎。
> - 当研究者修改现有工具或组合多个工具时，原有量表的[[Reliability|信度]]值不再适用于新工具。重新建立内部一致性应成为数据分析计划的组成部分。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch8)]]
> - α > 0.90 虽然看似理想，但可能意味着部分条目在测量几乎相同的内容（条目冗余），而非提供独特的增量信息——此时应考虑是否可精简条目以缩短量表长度。
> - 半分法的有效性取决于两半是否在内容难度上真正匹配——如果测试有系统性难度梯度，前后半分割会产生不匹配的两半，此时奇偶分半法是必要的纠正手段。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, p. 203)]]
