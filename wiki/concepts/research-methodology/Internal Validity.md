---
title: Internal Validity
aliases:
  - 内部效度
  - internal validity threats
  - threats to internal validity
summary: "实验研究中因程序、处理或受试者经历而威胁研究者从数据对总体做出正确推论能力的因素，包括历史、成熟、回归、选择、流失、扩散、补偿性竞争等"
type: concept
tags:
  - method/experimental
  - quantitative-research
  - validity
related_concepts:
  - "[[Causality]]"
  - "[[Variable]]"
  - "[[External Validity]]"
related_theories: []
related_methods:
  - "[[Experimental Research]]"
  - "[[Intervention Research]]"
  - "[[Random Assignment]]"
related_persons: []
related_facts:
  - "[[Campbell Collaboration]]"
related_arguments: []
sources:
  - "[[Creswell_2022_SAGE]]"
confidence: medium
status: draft
created: 2026-05-31
updated: 2026-05-31
---

# Internal Validity

## 定义

> [!info]
> 内部效度（Internal Validity）是[[Experimental Research|实验研究]]中衡量[[Causality|因果推断]]质量的核心标准，指研究者能否从实验数据中正确推断出被操纵的[[Variable|变量]]确实导致了观察到的效果。内部效度越高，研究者越有信心将结果差异归因于处理本身，而非其他未控制的因素（Creswell & Creswell, 2022, Ch8）。

> [!quote]
> "Internal validity threats are experimental procedures, treatments, or experiences of the participants that threaten the researcher's ability to draw correct inferences from the data about the population in an experiment."（Creswell & Creswell, 2022, Ch8）

## 效度威胁

> [!abstract]
> 当存在内部效度威胁时，研究者无法确定观察到的效果是由被操纵的[[Variable|变量]]引起的，还是由其他未控制的因素所致。[[Campbell Collaboration|Campbell]] & Stanley (1963) 最早系统识别了这些威胁，Creswell & Guetterman (2018) 将其扩展为三组共 10 种（Creswell & Creswell, 2022, Ch8, Table 8.5）：

### 与受试者相关的威胁

| 威胁类型 | 描述 | 应对策略 |
|---|---|---|
| 历史（History） | 实验期间发生的外部事件不当地影响了结果，超出实验处理的影响。 | 让实验组和对照组经历相同的外部事件。 |
| 成熟（Maturation） | 受试者在实验期间自然成熟或变化，从而影响结果。 | 选择成熟或变化速率相同的受试者（如同龄人）。 |
| 回归均值（Regression to the Mean） | 选择极端得分的受试者，其得分自然会随时间向均值回归。 | 选择入组特征非极端得分的受试者。 |
| 选择（Selection） | 受试者因具有某些特征而倾向于产生特定结果。 | 随机选择受试者，使特征在各实验组中概率均等分布。 |
| 流失／研究减员（Mortality/Attrition） | 受试者因多种原因退出实验，其结果是未知的。 | 招募大样本以应对退出，或比较退出者与继续者的结果特征。 |

> [!example] 举例
> **历史**：一项为期一学期的数学教学法实验中，实验期间学校恰好推行了新的课后辅导政策。即使实验组后测成绩更高，也无法区分是教学法的效果还是课后辅导的效果。两组都经历了新政策时，这一威胁得到控制。
>
> **成熟**：一项为期一年的阅读[[Intervention Research|干预研究]]中，对照组学生的阅读成绩也在提高——因为他们自然长大了、认知能力在发展。如果不设对照组，这些自然成长会被误判为干预效果。选取同年级学生作为对照组可以控制这一威胁。
>
> **回归均值**：研究者从全年级中选出数学成绩最差的 30 名学生进行补习。即使补习完全无效，他们的成绩也会在第二次测试中自然上升——因为第一次测试包含了偶然的低分（测量误差），这些偶然因素不会在第二次测试中重复。选择非极端得分的学生入组可以避免这一问题。
>
> **选择**：某实验的"实验组"由自愿报名的学生组成，"对照组"由未报名的学生组成。两组在动机水平上可能存在系统性差异，后测差异可能反映的是动机差异而非处理效应。[[Random Assignment|随机分配]]可以消除这种系统性偏差。
>
> **流失**：一项为期三个月的减肥实验中，体重最重、效果最差的受试者在中期退出。如果只分析坚持到最后的人，实验效果会被高估。预先招募大样本，并在报告时比较退出者与继续者的基线特征，可以评估流失偏差的严重程度。

### 与实验处理相关的威胁

| 威胁类型 | 描述 | 应对策略 |
|---|---|---|
| 处理扩散／组间交叉污染（Diffusion of Treatment） | 对照组和实验组的受试者相互交流，影响两组的结果得分。 | 在实验期间尽可能保持两组分离。 |
| 补偿性／怨恨性士气低落（Compensatory/Resentful Demoralization） | 只有实验组接受处理时，两组获益不均可能引发不满。 | 向对照组在实验结束后提供处理，或给予不同类型的处理。 |
| 补偿性竞争（Compensatory Rivalry） | 对照组因未接受处理而感到被低估，从而产生竞争性行为。 | 降低对照组预期或明确说明对照组的价值，创造两组平等感。 |

> [!example] 举例
> **处理扩散**：同一所学校内，实验班使用新教学法，对照班使用传统教学法。课间休息时实验班的学生把新方法教给了对照班的朋友，导致对照班也部分接触了处理。两组结果因此趋同，处理效应被低估。将实验组和对照组放在不同学校可以解决，但成本更高。
>
> **补偿性怨恨**：学校推行一项新的免费午餐计划，只有实验班学生可以领取。对照班学生知道后感到不公平，在后期测试中消极应答或故意表现差，导致组间差异被人为放大。应对方式是承诺实验结束后给予对照组同等待遇。
>
> **补偿性竞争**：对照组的教师知道自己是"对照组"后，加倍努力教学以证明自己不比实验组差——对照组结果因此被拉高，处理效应被低估。这是 John Henry 效应的一种形式。应对方式是不过度强调"实验 vs 对照"的标签，或给予对照组一个有意义的替代任务，使其感到自己的工作同样重要。

### 与实验程序相关的威胁

| 威胁类型 | 描述 | 应对策略 |
|---|---|---|
| 测验（Testing） | 受试者熟悉结果测量工具，记住前测答案以用于后测。 | 延长前后测时间间隔，或在后测中使用不同于前测的题目。 |
| 工具（Instrumentation） | 前测和后测之间测量工具发生变化，影响结果得分。 | 前后测使用相同的测量工具。 |

> [!example] 举例
> **测验**：一项逻辑推理训练实验中，前后测使用了同一套题目。受试者后测成绩提高可能不是训练的效果，而是做前测时就记住了题目和答案。延长两次测试的时间间隔（如从一周延至两个月），或使用难度相当的平行题本，可以降低这一威胁。
>
> **工具**：一项写作教学实验中，前测由一位老师评分，后测由另一位评分标准更宽松的老师评分。后测"提高"可能纯粹是评分标准差异导致的，而非写作能力的真实提升。前后测使用相同的评分者和评分标准可以消除这一威胁。

## 争议与批评

> [!warning]
> 内部效度和[[External Validity|外部效度]]之间存在权衡：高度控制的实验环境虽能保障内部效度，但可能降低外部效度（即结果难以推广到自然情境）。[[Experimental Research|实验研究]]者需要在设计阶段明确识别潜在的内部效度威胁，并采取相应的应对措施（Creswell & Creswell, 2022, Ch8）。

## 来源

- [[Creswell_2022_SAGE]]
