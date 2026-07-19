---
title: Split-Half Reliability
aliases:
  - 折半信度
  - 分半信度
  - split-half
summary: "将测量项目分成对等两半所测结果的一致性程度，是内部一致性的一种估计方法，常用奇偶数分半并辅以 Spearman-Brown 等公式校正"
type: concept
domain: "research-methodology"
related_count: 6
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - method/measurement
  - quantitative-research
  - reliability
related_concepts:
  - "[[Reliability]]"
  - "[[Internal Consistency]]"
  - "[[Test-Retest Reliability]]"
  - "[[Parallel-Forms Reliability]]"
  - "[[Questionnaire]]"
  - "[[Construct]]"
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_QiMei_2015_EducationalResearchMethods]]"
confidence: medium
status: draft
created: 2026-06-26
updated: 2026-06-26
---

# Split-Half Reliability

---

## 定义

> [!def] 折半[[Reliability|信度]]（Split-Half Reliability）
> 折半信度是把测量项目分成对等两半所测结果的一致性程度（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015]], Ch.5）。它是一种估计[[Internal Consistency|内部一致性]]的方法，只需一次施测即可完成——将一份量表的条目按一定规则分为两半，分别计分，计算两半个分之间的相关，再通过校正公式推估整份量表的信度。

> [!concept-lens] 概念透镜
> - **含义** 折半信度是[[Internal Consistency|内部一致性]]的一种估计策略。它将量表的"条目间一致性"问题转化为"两半个分间的一致性"问题，然后通过统计校正还原为全量表的信度估计。
> - **用途** 当研究者只有一次施测数据、无法进行重测或开发复本时，折半信度提供了便捷的信度估计方法。
> - **边界** 折半信度不同于[[Test-Retest Reliability|重测信度]]（跨时间）和[[Parallel-Forms Reliability|复本信度]]（跨形式）。由于只涉及一次施测，它无法反映时间稳定性或工具等值性。

---

## 核心要素

### 分半方法

> [!warning] 分半的两个条件
> 折半[[Reliability|信度]]的有效性依赖于两个条件（[[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015]], Ch.5）：
> - **两部分在难度、区分度和测量目标上高度趋同或相似**
> - **被测者以相同的状态对待两部分问题或项目**（如情绪、压力、疲劳等状态）

常用**奇偶数分半**而非前后折半——因为[[Questionnaire|问卷]]内在结构往往具有前易后难的差异，前后折半会导致两半个分系统性不等价。

### 校正公式

由于折半后的每一半只有原量表的一半长度，直接计算的两半相关会**低估**全量表的信度。因此需要通过校正公式还原：

> [!ref-table] 常用折半信度校正公式
> | 公式名称 | 说明 |
> |---|---|
> | Spearman-Brown 公式 | 最常用的校正公式，适用于两半等长且方差相等的理想情况 |
> | Flanagan 系数 | 基于两半个分的方差分别估计 |
> | Rulon 系数 | 基于两半个分差值的方差估计，不要求两半等方差 |
> | Kuder-Richardson 系数（KR-20、KR-21） | 适用于二分计分（0/1）的条目 |
> | [[Internal Consistency\|Cronbach α]] 系数 | 将折半思路推广至逐条目层面，是当前最通用的[[Internal Consistency\|内部一致性]]指标 |

> [!note] 从折半到 α
> Cronbach α 可以理解为**所有可能折半方式的平均信度**——它将折半的思路推广到每一个条目，计算的是条目间的平均协方差相对于总方差的比例。因此在实际应用中，α 系数已在很大程度上取代了传统的折半信度。

---

## 概念辨析

> [!contrast-table] 折半[[Reliability|信度]] vs [[Internal Consistency|内部一致性]] vs [[Test-Retest Reliability|重测信度]]
> | 维度 | 折半信度 | [[Internal Consistency\|内部一致性（Cronbach α）]] | [[Test-Retest Reliability\|重测信度]] |
> |---|---|---|---|
> | 核心逻辑 | 将条目分两半→计算两半相关→校正 | 逐条目计算平均协方差 | 同一工具两次施测 |
> | 施测次数 | 一次 | 一次 | 至少两次 |
> | 反映的信度类型 | 条目间一致性 | 条目间一致性 | 跨时间稳定性 |
> | 与 α 的关系 | α 是"所有可能折半的平均" | — | — |

---

## 争议与批评

> [!warning] 局限性
> - **分半方式敏感** 不同的分半方式（奇偶、随机、按内容）可能产生不同的折半[[Reliability|信度]]估计值，结果的稳定性依赖于分半策略的选择。
> - **已被 α 系数取代**[[Internal Consistency|Cronbach α]] 提供了更稳定且不依赖特定分半方式的一致性估计，在实际研究中折半信度的使用已大幅减少。
> - **不适用于多维量表** 如果量表测量多个不同的[[Construct|构念]]维度，折半可能导致两半测量了不同的构念，此时折半信度没有意义。
> - **不反映时间稳定性** 由于只需一次施测，折半信度不能替代[[Test-Retest Reliability|重测信度]]来证明量表跨时间的稳定性。
