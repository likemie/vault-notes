---
title: Item Response Theory
aliases:
  - 项目反应理论
  - IRT
  - latent trait theory
  - 潜在特质理论
summary: "基于潜在特质假设的现代测量理论，认为题目难度和区分度可以独立于施测样本被描述，受试者能力也可以独立于具体测验题目被估计，是计算机自适应测验的理论基础"
type: theory
theory_field: "research-methodology"
theory_related_count: 12
theory_related_level: 1
theory_related_stars: "⭐"
theory_related_color: "#dbeafe"
tags:
  - theme/measurement
  - method/test-theory
  - theme/psychometrics
related_concepts:
  - "[[Construct]]"
  - "[[Item Analysis]]"
  - "[[Hypothesis]]"
  - "[[Computerized Adaptive Testing]]"
  - "[[Standard Error]]"
  - "[[Epistemology]]"
  - "[[Ontology]]"
related_theories:
  - "[[Classical Test Theory]]"
related_methods:
  - "[[Rasch Measurement]]"
related_facts:
  - "[[PISA]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]]"
related_instruments:
  - "[[Consensual Assessment Technique]]"
confidence: medium
status: draft
created: 2026-07-24
updated: 2026-07-26
---

# Item Response Theory

---

## 理论定位

> [!theory-position] 理论定位
> - **解释对象** 个体的潜在特质（能力、态度、知识水平等不可直接观测的[[Construct|构念]]）如何决定其对每个测验题目的反应概率。
> - **理论问题** 如何在不依赖特定施测样本的情况下描述题目属性，以及如何在不依赖特定测验题目的情况下估计个体能力。
> - **理论类型** 测量理论、心理计量学模型。
> - **知识位置** 心理测量学；Rasch（1960）、Lord（1980）、Hambleton（1993）等为其主要奠基者和发展者。

> [!claim] 核心主张
> 可以测量单一、特定的潜在特质（latent traits）——这些特质本身不可观测，但可以通过个体对测验题目的反应模式被量化估计。IRT 的核心突破在于：[[Item Analysis|题目难度]]和区分度可以独立于任何特定的受试者样本被描述（样本无关性），同时受试者的能力也可以独立于任何特定的题目样本被估计（题目无关性）。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!formula] [[Rasch Measurement|Rasch 模型]]（一参数 IRT）
> $$P(X_i = 1 \mid \theta, b_i) = \frac{e^{(\theta - b_i)}}{1 + e^{(\theta - b_i)}}$$
>
> - $P$：能力为 $\theta$ 的人答对题目 $i$ 的概率（0–1）
> - $\theta$：受试者的潜在特质水平（能力）
> - $b_i$：题目 $i$ 的难度
>
> 核心逻辑：答对概率只取决于能力与难度的差距。当 $\theta = b_i$ 时概率为 50%；$\theta > b_i$ 时概率大于 50%；$\theta < b_i$ 时小于 50%。两参数模型（2PL）增加区分度参数 $a_i$，三参数模型（3PL）再增加猜测参数 $c_i$。

---

## 关键概念与理论构件

> [!entry-map]
>
> | 构件 | 类型 | 在理论中的功能 |
> |:-----|:-----|:--------------|
> | Latent Trait（潜在特质） | 概念 | 理论的核心解释对象：不可直接观测的个体属性（如言语能力、数学能力），IRT 通过题目反应模式推断其水平 |
> | [[Item Analysis|item difficulty]]（题目难度） | 概念 | 题目本身的属性，不依赖于试测样本——与 [[Classical Test Theory|CTT]] 的样本依赖难度形成根本区别 |
> | Item Discriminability（题目区分度） | 概念 | 题目区分高低能力受试者的有效性 |
> | [[Rasch Measurement|Rasch 模型]] | 方法 | IRT 中最简单的一参数模型，仅含难度参数，是客观测量的理想化模型 |
> | Unidimensionality（单维性） | 概念 | IRT 的基本[[Hypothesis|假设]]：每个题目只测量单一的潜在特质 |

---

## 核心命题与机制

> [!proposition-chain] 核心命题一｜题目属性可以独立于特定受试者样本被描述
> - **前提一** IRT [[Hypothesis|假设]]每个题目有其内在的难度水平（客观难度），不依赖于哪些人回答了该题目。
> - **前提二** IRT 通过数学模型（如 [[Rasch Measurement|Rasch 模型]]（Wainer & Mislevy, 1990））将[[Item Analysis|题目难度]]与受试者能力放在同一量尺上，从而可以独立估计题目参数。
> - **推导** 与 [[Classical Test Theory|CTT]] 不同，IRT 的题目难度不是群体依赖的（is not group-dependent），因此在一个样本中校准的题目参数可直接用于其他样本而无需重新标准化。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!proposition-chain] 核心命题二｜受试者能力可以独立于特定题目样本被估计
> - **前提一** 受试者对任一测验题目的反应不会影响其对其他题目的反应（局部独立性假设）。
> - **前提二** 正确答案的概率不取决于有多少其他受试者处于同一能力水平（不依赖常模分布）。
> - **推导** 用不同题目组合施测同一位受试者得到的能力估计应当一致。这意味着可以为每位受试者选择与其能力水平匹配的题目（适应性施测），这是[[Computerized Adaptive Testing|计算机自适应测验]]的理论基础。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!proposition-chain] 核心命题三｜可以计算每位受试者能力估计的个性化精度
> - **前提一** IRT 为每个受试者提供能力估计及其[[Standard Error|标准误]]。
> - **前提二** 这一精度统计量取决于受试者自身的能力水平、施测题目的数量和属性。
> - **推导** 与 CTT 计算单一平均误差方差不同，IRT 承认误差方差随受试者能力水平变化——能力极高或极低的受试者，其能力估计精度通常低于中等能力受试者。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!proposition-chain] 核心命题四｜单维性与局部独立性是 IRT 参数估计可识别的前提
> - **前提一** 单维性假设：特质是可指定的单一维度（如言语能力独立于数学能力），该维度足以解释测验结果。
> - **前提二** 局部独立性假设：一组题目测量一个共同的特质，受试者对任何一个题目的反应不影响其对其他题目的反应。
> - **推导** 这两个假设是 IRT 参数估计在数学上可识别的前提条件。违背单维性假设时需要使用多维 IRT 模型。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!exegesis]- 教育研究例子：IRT and CTT 的对比
> 用同一套数学题测试重点学校和普通学校学生。CTT 分析会显示某题目在重点学校难度 0.3（容易）、在普通学校难度 0.7（困难）——但这无法判断差异来自题目还是学生。IRT 则将该题目的难度估计为 0.5（中等），独立于两校样本。反之，两个水平相同的学生分别做了题库中不同的 10 道题，CTT 无法直接比较他们的分数（题目不同），但 IRT 给出的能力估计一致——这就是为什么 [[PISA]] 等国际测评中不同国家的学生可以做不同的题目却获得可比较的分数。

---

## 理论立场与使用方式

> [!contrast-table] IRT 与 [[Classical Test Theory|CTT]] 的关键区别
> | 维度 | CTT | IRT |
> |------|-----|-----|
> | **题目参数** | 样本依赖——难度随试测群体而变 | 样本独立——难度是题目自身属性 |
> | **能力估计** | 依赖于具体题目集合 | 独立于具体题目集合 |
> | **误差估计** | 单一平均误差方差，[[Hypothesis|假设]]所有人相同 | 个性化误差，取决于每位受试者的能力水平 |
> | **测验等值** | 需要复杂等值程序 | 通过共同题目或共同受试者自然等值 |
> | **适应性施测** | 不支持——题目参数随群体变化 | 支持——题目参数稳定，可动态选择 |
> | **适用场景** | 课堂测验、小规模自编测验 | 大规模标准化测验、[[Computerized Adaptive Testing|CAT]]、跨国比较测评 |

> [!theory-stance] [[Epistemology|认识论]]立场
> - **[[Ontology|本体论]]** 假设存在不可直接观测但可以通过概率模型还原的潜在特质；这些特质是连续的、可量化的。
> - **认识论** 测量精度因人而异——IRT 为每位受试者提供个性化的能力估计及其误差，而非假设所有人共享同一误差方差。
> - **方法含义** 支持通过数学模型预测测验属性（在施测前即可预测）；支持[[Computerized Adaptive Testing|计算机自适应测验]]；要求大规模题目池的开发与校准。
> - **不能直接推出的东西** IRT 参数估计依赖于模型假设（单维性、局部独立性）被满足；违反假设时能力估计可能有偏；不能自动保证不同 IRT 模型产生相同的能力排序。

> [!theory-use] 如何用于研究
> - **作为理论框架** 为标准化测验的编制、等值和题库建设提供数学基础。
> - **作为分析工具** 通过 [[Rasch Measurement|Rasch 模型]]分析[[Item Analysis|题目难度]]与受试者能力的匹配度；通过多参数模型（2PL、3PL）评估区分度和猜测效应；通过差异题目功能（DIF）分析检测测验偏差。
> - **作为批判视角** 提醒研究者 [[Classical Test Theory|CTT]] 的题目参数样本依赖性如何限制跨研究比较，以及为什么大规模测评项目（如 [[PISA]]、TIMSS、NAEP）选择 IRT 为基础。
> - **报告方式** 在研究报告中应明确使用的 IRT 模型类型、模型拟合指标、题目参数估计结果以及能力估计的精度。

---

## 适用边界

> [!theory-boundary] 适用边界
> - **适合解释** 大规模标准化测验的题目等值与题库建设；[[Computerized Adaptive Testing|计算机自适应测验]]的题目选择；跨群体测量不变性检验。
> - **谨慎使用** 小样本条件下 IRT 参数估计不稳定；多维度特质需要多维 IRT 模型，分析复杂度大幅提升。
> - **不适合解释** 常规课堂测验中几十个学生的[[Item Analysis|题目分析]]（[[Classical Test Theory|CTT]] 通常已足够）；非认知测验中缺乏明确潜在特质定义的测量。
> - **常见误用** 未检验单维性[[Hypothesis|假设]]就直接应用 IRT；夸大 IRT 对 CTT 的替代关系——二者各有适用场景，非简单替代。

---

## 发展脉络

> [!dev-timeline] 发展脉络
> - **1960 — [[Rasch Measurement|Rasch 模型]]提出** Georg Rasch 提出一参数逻辑斯蒂模型，奠定客观测量的概率基础
> - **1980 — Lord 出版《项目反应理论在实践测验问题中的应用》** 系统化 IRT 的理论框架和实际应用
> - **1990 — Rasch 测量成为教育测评主流** Wainer & Mislevy 等学者的推广使 IRT 进入大规模测评项目（如 NAEP、TIMSS、[[PISA]]）
> - **2000 年代 — [[Computerized Adaptive Testing|计算机自适应测验]]普及** IRT 成为 [[Consensual Assessment Technique|CAT]] 的核心算法基础

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]] — 教材 24.5 节介绍 IRT 的基本原理，包括潜在特质[[Hypothesis|假设]]、[[Item Analysis|题目难度]]与区分度的样本独立性、单维性假设、[[Rasch Measurement|Rasch 模型]]，以及 IRT 在[[Computerized Adaptive Testing|计算机自适应测验]]中的应用
