---
title: Post Hoc Ergo Propter Hoc Fallacy
aliases:
  - 事后归因谬误
  - post hoc fallacy
  - post hoc, ergo propter hoc
summary: "一种逻辑谬误，指仅因一个事件在时间上先于另一个事件，就推断前者是后者的原因。是事后回溯研究中的核心风险之一。"
type: concept
domain: "research-methodology"
related_count: 13
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - logic/fallacy
  - causal-inference
  - subject/research-methodology
related_concepts:
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Necessary and Sufficient Conditions]]"
  - "[[Hypothesis]]"
  - "[[Falsification]]"
  - "[[Academic Achievement]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Alternative Hypothesis]]"
related_methods:
  - "[[Experimental Research]]"
  - "[[Ex Post Facto Research]]"
  - "[[Random Assignment]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15]]"
confidence: medium
status: draft
created: 2026-07-12
updated: 2026-07-12
---
# Post Hoc Ergo Propter Hoc Fallacy

---

## 定义

> [!def] 事后归因谬误（Post Hoc Ergo Propter Hoc Fallacy）
> 事后归因谬误是一种逻辑谬误，指仅因一个[[Variable|变量]]在时间上先于另一个变量，就推断前者是后者的原因。拉丁文全称为 post hoc, ergo propter hoc，意为"在此之后，因此因为此"（after this, therefore because of this）。该谬误的根本问题在于：时间上的先后顺序不能单独作为[[Causality|因果关系]]成立的[[Necessary and Sufficient Conditions|充分条件]]（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15|Cohen et al., 2011, Ch. 15, p. 309]]）。

> [!concept-lens] 概念透镜
> - **含义** 事后归因谬误指向因果推断中的一种典型错误：将时间序列（temporal sequence）误认为因果序列（causal sequence）。两个事件 A 和 B 先后发生，并不意味 A 导致了 B。
> - **用途** 识别和命名这一谬误有助于研究者警惕非[[Experimental Research|实验研究]]设计中因果推断的脆弱性，特别是在[[Ex Post Facto Research|事后回溯研究]]中，[[Hypothesis|假设]]是从已收集的数据中生成的，无法在同一数据上被检验。
> - **边界** 事后归因谬误仅指出时间顺序≠因果关系的逻辑问题，本身不提供如何正确建立因果关系的正面方案。它不同于反向因果（reverse causation，因果方向可能相反）和第三变量问题（common cause，两者都是共同原因的结果），尽管这三者在事后回溯研究中经常同时出现（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15|Cohen et al., 2011, Ch. 15, pp. 309–310]]）。

---

## 核心要素

> [!feature] 事后归因谬误的三个层面
> - **逻辑层面** 时间先后是[[Causality|因果关系]]的[[Necessary and Sufficient Conditions|必要条件]]而非充分条件。即使 A 每次都先于 B 发生，也不能在逻辑上排除其他解释。
> - **统计层面** 两个[[Variable|变量]]的相关（correlation）不能单独确立因果关系。在[[Ex Post Facto Research|事后回溯研究]]中，即使发现强相关，也可能存在三种竞争性解释：X 导致 O、O 导致 X、第三变量导致二者。
> - **方法层面** 事后回溯研究的[[Hypothesis|假设]]是在数据收集之后生成的，因此无法在同一数据上被[[Falsification|证伪]]（Babbie, 2010, p. 462）。证据只能说明假设，不能检验假设（Lord, 1973, p. 7）。

---

## 应用案例

> [!case] 咖啡与失眠
> 喝咖啡然后失眠，并不意味咖啡导致了失眠。可能有其他原因，如当天的工作压力、身体不适或环境噪音等（Cohen & Nagel, 1961）。这个简单案例说明：日常生活中的因果直觉经常犯事后归因谬误，科学研究需要更严格的控制和检验程序（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15|Cohen et al., 2011, Ch. 15, p. 309]]）。

> [!case] 看电视与[[Academic Achievement|学业表现]]
> 看电视的时间与学业表现差之间存在相关。可能看电视导致学业差（因果正方向），也可能学业差导致看更多电视（反向因果），但更可能的是第三种解释：学生的能力或动机水平（第三[[Variable|变量]]）同时导致看电视多和学业表现差。注意在第三种解释中，是第三变量作为[[Independent Variable|自变量]]同时引发了两个[[Dependent Variable|因变量]]（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15|Cohen et al., 2011, Ch. 15, p. 309]]）。

---

## 争议与批评

Cohen & Nagel（1961）从逻辑哲学角度指出，[[Causality|因果关系]]的建立常常仅仅基于"任何先于现象发生的相关事件就是其原因"这一脆弱前提。该谬误的识别本身不提供因果推断的正面方法论，需要结合实验控制、[[Random Assignment|随机化]]和[[Alternative Hypothesis|替代假设]]检验等手段来弥补。
