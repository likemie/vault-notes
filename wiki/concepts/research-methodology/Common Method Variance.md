---
title: Common Method Variance
aliases:
  - 共同方法变异
  - 共同方法偏差
  - 共同方法效应
  - CMV
  - common method bias
summary: "由测量方法本身（而非所测构念的真实差异）造成的系统方差，当多个构念使用同一方法施测时会放大观察相关，威胁构念间关系估计的效度"
type: concept
domain: "research-methodology"
related_count: 16
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/measurement
  - theme/validity
  - theme/psychometrics
related_concepts:
  - "[[Construct]]"
  - "[[Questionnaire]]"
  - "[[Construct Validity]]"
  - "[[Self-report Bias]]"
  - "[[Response Bias]]"
  - "[[Creativity]]"
  - "[[Critical Thinking]]"
  - "[[Interaction Effect]]"
  - "[[Document]]"
  - "[[Effect Size]]"
  - "[[Variable]]"
related_theories: []
related_methods:
  - "[[Triangulation]]"
  - "[[Meta-analysis]]"
  - "[[Three-Level Meta-Analysis]]"
  - "[[Meta-regression]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Park_2026_TSC]]"
confidence: medium
status: draft
created: 2026-08-25
updated: 2026-08-25
---

# Common Method Variance

---

## 定义

> [!def] 核心定义
> 共同方法变异（Common Method Variance, CMV）是指由测量方法本身、而非所测[[Construct|构念]]的真实差异造成的系统方差。当两个或多个构念使用同一种测量方法（尤其是同一份自陈[[Questionnaire|问卷]]）获得数据时，测量方法共享的方法成分成为共同来源，使观察到的构念间相关被系统性放大，可能产生虚假或偏高的关系估计。[[Argument_Park_2026_TSC|(Park et al., 2026, p. 9)]]

> [!concept-lens] 概念透镜
> - **含义** 指向同一方法（如问卷作答）在多个构念测量之间共享的系统方差成分。
> - **用途** 帮助研究者判断构念间观察相关有多少来自真实构念重叠、多少来自测量方法的共享成分，从而评估关系估计的[[Construct Validity|构念效度]]威胁。
> - **边界** 共同方法变异不等于测量的随机误差，也不等于构念间真实的因果或结构关系。

> [!boundary]- 概念边界
> - 不等于 [[Self-report Bias|自报偏差]]：自报偏差指受访者回答系统性偏离真实值（低报、高报、理解不一致）；共同方法变异强调方法共享成分对构念间观察相关的影响，自报偏差只是其中一种可能的驱动机制。
> - 不等于 [[Response Bias|回应偏差]]：回应偏差关乎"谁回应"（回应者与非回应者的系统差异）；共同方法变异关乎"回应如何被方法共享成分塑造"。
> - 不等于 随机测量误差：测量误差包含随机成分，共同方法变异专指与测量方法绑定、在多个测量间共享的系统成分。

---

## 核心要素

> [!feature] 共同方法变异的核心要素
> - **方法共享来源** 自陈作答方式、同一评分者、相同施测情境等方法的共同特征在多个[[Construct|构念]]测量中重叠。
> - **放大机制** 共享的作答倾向——如社会期望、默许、自尊或一般能力自评——使个体在两个构念上给出系统相关的回答。
> - **影响方向** 通常使观察相关虚高（正向偏置），具体大小取决于共享方法成分的结构与强度。
> - **缓解路径** 多方法[[Triangulation|三角验证]]、引入绩效或行为指标、错开测量时点，以及统计控制（如潜在方法因子）。[[Argument_Park_2026_TSC|(Park et al., 2026, p. 9)]]

---

## 围绕概念形成的命题

### 命题一　当两个构念都用自陈测量时，共同方法变异会放大观察相关

> [!concept-lens] 测量类型与观察相关的依赖
> 方法学与心理测量研究关注[[Construct|构念]]间观察相关在多大程度上随测量方式（主观自陈 vs 客观任务表现）而变化，以及这种变化是否指向共享的方法方差。

> [!claim] [[Argument_Park_2026_TSC|Park et al. (2026)]]
> **双主观组合相关虚高** 在[[Meta-analysis|元分析]]综合学生样本中[[Creativity|创造力]]与[[Critical Thinking|批判性思维]]的相关时，双主观（双自陈）测量组合的合并相关 $r = 0.509$ 显著高于双客观组合（$r = 0.317$）与混合组合（$r = 0.195$–$0.260$），测量类型及其交互项的[[Interaction Effect|调节效应]]均达显著，方向符合共同方法变异放大观察相关的预测。经典方法学[[Document|文献]]（Podsakoff et al., 2003）把这种共享作答倾向称为"共同方法偏差"的来源。[[Argument_Park_2026_TSC|(Park et al., 2026, p. 9)]]

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **自陈测量放大观察相关** | 双主观测量组合的构念间相关显著高于客观与混合组合，指向共同方法方差 | 自陈[[Questionnaire\|问卷]]研究、元分析调节检验 | Podsakoff et al. (2003); [[Argument_Park_2026_TSC\|Park et al. (2026)]] |

---

## 实证数据

> [!ref-table]- 其他实证结果（无[[Effect Size|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Park_2026_TSC\|Park et al. (2026)]] | $k = 51$，$N = 12{,}548$，学生样本（中学/高中、大学、研究生） | [[Three-Level Meta-Analysis\|三水平元分析]]的[[Meta-regression\|元回归]]调节分析 | 测量类型组合的合并相关与组间检验 | 双主观组合 $r = 0.509$；双客观组合 $r = 0.317$；创造力客观×批判性思维主观 $r = 0.260$；创造力主观×批判性思维客观 $r = 0.195$ | 测量类型交互项 $Q_M(1) = 6.524, p = .011$；批判性思维测量类型 $Q_M(1) = 5.234, p = .022$；创造力测量类型 $Q_M(1) = 10.133, p = .002$ | 双主观组合相关显著最高，方向符合共同方法变异放大观察相关的预测；研究未直接测量 CMV，故为间接证据，需回到 [[Argument_Park_2026_TSC\|Park et al. (2026)]] 图 4 查看逐组合 95% CI |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Park_2026_TSC|Park et al. (2026)]] 在学生样本[[Creativity|创造力]]与[[Critical Thinking|批判性思维]]相关的[[Three-Level Meta-Analysis|三水平元分析]]中，发现双主观（自陈）测量组合的相关（$r = 0.509$）显著高于双客观组合（$r = 0.317$），据此将测量类型[[Interaction Effect|调节效应]]解释为自陈测量中共同方法变异的证据，并建议未来研究以表现型或行为指标对自陈测量进行[[Triangulation|三角验证]]。
