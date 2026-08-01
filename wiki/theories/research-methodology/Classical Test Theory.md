---
title: Classical Test Theory
aliases:
  - 经典测验理论
  - 经典测量理论
  - CTT
  - classical measurement theory
  - true score theory
summary: "将测验分数分解为真实分数与误差之和的测量理论，假设真实分数是无限次独立施测的期望值，是题目分析和信度计算的基础框架"
type: theory
theory_field: "research-methodology"
theory_related_count: 13
theory_related_level: 1
theory_related_stars: "⭐"
theory_related_color: "#dbeafe"
tags:
  - theme/measurement
  - method/test-theory
  - theme/psychometrics
related_concepts:
  - "[[Reliability]]"
  - "[[Item Analysis]]"
  - "[[Construct]]"
  - "[[Cultural Capital]]"
  - "[[Hypothesis]]"
  - "[[Epistemology]]"
  - "[[Ontology]]"
  - "[[Internal Consistency]]"
  - "[[Achievement and Aptitude Tests]]"
  - "[[Rating Scale]]"
  - "[[Computerized Adaptive Testing]]"
related_theories:
  - "[[Item Response Theory]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]]"
confidence: medium
status: draft
created: 2026-07-24
updated: 2026-07-26
---

# Classical Test Theory

---

## 理论定位

> [!theory-position] 理论定位
> - **解释对象** 测验分数的构成——为什么同一个体在不同次施测中获得不同的分数，以及如何估计测量误差。
> - **理论问题** 如何从不完美的、含误差的观测分数中推断个体的真实能力或特质水平。
> - **理论类型** 测量理论、心理计量学基础框架。
> - **知识位置** 心理测量学、教育测量学；起源于 Spearman（1904）等早期心理计量学家的[[Reliability|信度]]研究。

> [!claim] 核心主张
> 任何测验所得分数都是真实分数（true score）与测量误差（error）之和。真实分数是个体在该测验上无限次独立施测后所得分数的期望值；观测分数围绕真实分数上下波动，波动的幅度即为测量误差的大小。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!formula] CTT 基本公式
> $$X = T + E$$
>
> 观测分数（$X$）等于真实分数（$T$）加上误差（$E$）。真实分数是无限次独立施测的期望值，误差来自文化与社会经济背景、测验偏差、施测与评分过程以及受试者对测验的态度。
>
> CTT 的核心局限在于：真实分数依赖于测验内容而非受试者特征，[[Item Analysis|题目难度]]可能取决于样本特征而非题目本身的内在属性。这使得比较不同受试者在不同测验上的结果变得困难。

---

## 关键概念与理论构件

> [!entry-map]
>
> | 构件 | 类型 | 在理论中的功能 |
> |:-----|:-----|:--------------|
> | True Score（真实分数） | 概念 | 理论的核心[[Construct\|构念]]：个体在没有测量误差时本应获得的分数，是无限次独立施测的期望值 |
> | Observed Score（观测分数） | 概念 | 测验实际记录到的分数，等于真实分数加误差 |
> | Measurement Error（测量误差） | 概念 | 导致观测分数偏离真实分数的所有随机因素 |
> | [[Reliability]] | 概念 | 真实分数方差在观测分数方差中所占的比例，是 CTT 框架下量化测验质量的核心指标 |

---

## 核心命题与机制

> [!factors] 测量误差的来源
> - **文化与社经背景** 受试者的[[Cultural Capital|文化资本]]和社会经济条件可能系统性地影响测验表现
> - **测验偏差** 测验题目本身可能存在语言、内容或形式上的偏差
> - **施测与计分过程** 测验的施测条件、计分方式和评分者差异引入额外变异
> - **受试者态度** 受试者对测验的动机、焦虑或抵触情绪影响真实能力的展现

> [!proposition-chain] 核心命题一｜观测分数可以分解为真实分数与随机误差两部分
> - **前提一** [[Hypothesis|假设]]存在一个真实分数——即个体在完全无误差测量条件下本应获得的分数，等于无限次独立施测的期望均值。
> - **前提二** 在现实世界中，由于文化与社经背景、测验偏差、施测与计分方式、受试者态度等因素，误差不可避免地存在。
> - **推导** 每次施测得到的观测分数是真实分数叠加了误差项的结果：$X = T + E$。这是 CTT 最基本的数学模型。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!proposition-chain] 核心命题二｜真实分数的取值依赖于测验内容而非受试者特征
> - **前提一** CTT 中真实分数的定义是相对于特定测验内容的——它是该测验无限次施测的期望值，而非脱离测验而存在的绝对能力。
> - **前提二** 题目的难度可能取决于样本特征（抽样问题），而非题目本身的内在属性。
> - **推导** 在 CTT 框架下，很难直接比较不同受试者在不同测验上的结果——真实分数是测验内容依赖的，题目参数是样本依赖的。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!exegesis]- 教育研究例子
> 假设用同一套数学题测试重点学校和普通学校的学生。CTT 分析可能会显示某题目在重点学校难度低（很多人答对）、在普通学校难度高（很少人答对）。但 CTT 无法判断这种差异是题目本身简单还是重点学校学生能力强——因为难度是样本依赖的。这就是为什么 CTT 框架下，不同学校之间的成绩比较需要谨慎：题目参数会随施测群体而变。

---

## 理论立场与使用方式

> [!theory-stance] [[Epistemology|认识论]]立场
> - **[[Ontology|本体论]]** [[Hypothesis|假设]]存在稳定的个体差异（真实能力或特质），这些差异可以通过测验以概率方式被估计。
> - **认识论** 测量误差是随机的、不可消除但可估计的；通过[[Reliability|信度]]系数可以量化误差的大小。
> - **方法含义** 要求研究者通过信度分析（重测、复本、分半、[[Internal Consistency|内部一致性]]）评估测验质量；通过[[Item Analysis|题目分析]]筛选和改进题目。
> - **不能直接推出的东西** 不能从观测分数声称获得了真实分数；不能假设不同测验上的分数可以直接比较；不能假设题目参数独立于施测样本。

> [!theory-use] 如何用于研究
> - **作为理论框架** 为测验编制中的信度评估和题目分析提供基本概念框架。
> - **作为分析工具** 使用 $X = T + E$ 公式理解分数构成，通过信度系数估计误差方差。
> - **作为批判视角** 提醒研究者注意文化偏差、语言媒介和施测条件对观测分数的影响。
> - **报告方式** 在研究报告中应明确报告测验的信度系数（如 Cronbach's alpha）以及样本特征。

---

## 适用边界

> [!theory-boundary] 适用边界
> - **适合解释** 经典测验编制中的[[Reliability|信度]]评估和题目筛选；教育[[Achievement and Aptitude Tests|成就测验]]、[[Rating Scale|态度量表]]的基础测量属性分析。
> - **谨慎使用** 需要跨样本比较题目参数，或为每位受试者提供个性化测量精度估计时，CTT 的样本依赖性和内容依赖性成为重要限制。
> - **不适合解释** 题目参数在不同群体间的差异（需要 [[Item Response Theory|IRT]] 的测量不变性检验）；[[Computerized Adaptive Testing|计算机自适应测验]]中的题目选择逻辑。
> - **常见误用** 将观测分数直接等同于真实分数；忽略测验的文化偏差对误差的影响；在小样本中过分信任信度系数。

---

## 发展脉络

> [!dev-timeline] 发展脉络
> - **1904 — Spearman 提出[[Reliability|信度]]概念** 奠定 CTT 的数学基础
> - **20 世纪中期 — CTT 成为测验编制的标准框架** 广泛应用于教育测量和心理测量领域
> - **20 世纪后期 — [[Item Response Theory]] 兴起** 对 CTT 的题目参数样本依赖性和分数比较困难提出系统性改进。CTT 仍广泛用于课堂测验和研究者自编测验

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]] — 教材 24.5 节介绍 CTT 的基本公式 $X = T + E$、真实分数与观测分数的概念区分、误差来源，以及 CTT 在[[Item Analysis|题目分析]]和测验编制中的应用
