---
title: Item Response Theory
aliases:
  - 项目反应理论
  - IRT
  - latent trait theory
  - 潜在特质理论
summary: "基于潜在特质假设的现代测量理论，认为项目难度和区分度可以独立于施测样本被描述，受试者能力也可以独立于具体测验项目被估计，是计算机自适应测验的理论基础"
type: theory
theory_field: "research-methodology"
theory_related_count: 11
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
confidence: medium
status: draft
created: 2026-07-24
updated: 2026-07-24
---

# Item Response Theory

---

## 理论定位

> [!theory-position] 理论定位
> - **解释对象** 个体的潜在特质（能力、态度、知识水平等不可直接观测的[[Construct|构念]]）如何决定其对每个测验项目的反应概率。
> - **理论问题** 如何在不依赖特定施测样本的情况下描述项目属性，以及如何在不依赖特定测验项目的情况下估计个体能力。
> - **理论类型** 测量理论、心理计量学模型。
> - **知识位置** 心理测量学；Rasch（1960）、Lord（1980）、Hambleton（1993）等为其主要奠基者和发展者。

> [!claim] 核心主张
> 可以测量单一、特定的潜在特质（latent traits）——这些特质本身不可观测，但可以通过个体对测验项目的反应模式被量化估计。IRT 的核心突破在于：[[Item Analysis|项目难度]]和区分度可以独立于任何特定的受试者样本被描述（样本无关性），同时受试者的能力也可以独立于任何特定的项目样本被估计（项目无关性）。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

---

## 关键概念与理论构件

> [!entry-map]
>
> | 构件 | 类型 | 在理论中的功能 |
> |:-----|:-----|:--------------|
> | Latent Trait（潜在特质） | 概念 | 理论的核心解释对象：不可直接观测的个体属性（如言语能力、数学能力），IRT 通过项目反应模式推断其水平 |
> | [[Item Analysis\|item difficulty]]（项目难度） | 概念 | 表示项目本身有多"难"：在 IRT 中，难度是项目自身的属性，不依赖于试测样本 |
> | Item Discriminability（项目区分度） | 概念 | 表示项目区分高低能力受试者的有效性：区分度高的项目能有效拉开不同能力水平受试者的得分差距 |
> | [[Rasch Measurement\|Rasch 模型]] | 方法 | IRT 中最简单的一参数模型，仅包含难度参数，是客观测量的理想化模型 |
> | Unidimensionality（单维性） | 概念 | IRT 的基本[[Hypothesis\|假设]]：每个项目只测量单一的潜在特质，一组项目测量一个共同的特质或能力 |

---

## 核心命题与机制

> [!proposition-chain] 核心命题一｜项目属性可以独立于特定受试者样本被描述
> - **前提一** IRT [[Hypothesis|假设]]每个项目有其内在的难度水平（客观难度），这一属性不依赖于哪些人回答了该项目。
> - **前提二** IRT 通过数学模型（如 [[Rasch Measurement|Rasch 模型]]（Wainer & Mislevy, 1990））将[[Item Analysis|项目难度]]与受试者能力放在同一量尺上，从而可以独立估计项目参数。
> - **推导** 与 [[Classical Test Theory|CTT]] 不同，IRT 的项目难度"不是群体依赖的"（is not group-dependent），因此研究者可以在一个样本中校准项目参数，再将同一测验用于其他样本而无需重新标准化。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!proposition-chain] 核心命题二｜受试者能力可以独立于特定项目样本被估计
> - **前提一** 受试者对任一测验项目的反应不会影响其对其他项目的反应（局部独立性假设）。
> - **前提二** 正确答案的概率不取决于有多少其他受试者处于同一能力水平（不依赖常模分布）。
> - **推导** 因此，用不同项目组合施测同一位受试者，得到的能力估计应当一致。这意味着可以为每位受试者选择与其能力水平匹配的项目（适应性施测），这是[[Computerized Adaptive Testing|计算机自适应测验]]的理论基础。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!proposition-chain] 核心命题三｜可以计算每位受试者能力估计的精度
> - **前提一** IRT 为每个受试者提供能力估计及其[[Standard Error|标准误]]。
> - **前提二** 这一精度统计量取决于受试者自身的能力水平、施测项目的数量和属性。
> - **推导** 与 CTT 计算单一平均误差方差不同，IRT 承认误差方差随受试者能力水平变化——能力极高或极低的受试者，其能力估计精度通常低于中等能力受试者。这比 CTT 的"一刀切"误差估计更精确。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

> [!proposition-chain] 核心命题四｜IRT 假设特质是单维的且项目之间存在局部独立性
> - **前提一** 单维性假设：特质是可指定的单一维度（如言语能力是独立于数学能力的单一维度），该维度足以解释测验结果和表现。
> - **前提二** 局部独立性假设：一组项目测量一个共同的特质或能力，受试者对任何一个项目的反应不影响其对其他项目的反应。
> - **推导** 这两个假设是 IRT 参数估计在数学上可识别的前提条件。违背单维性假设时需要使用多维 IRT 模型。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24|(Ch24, 24.5 节)]]

---

## 理论立场与使用方式

> [!theory-stance] [[Epistemology|认识论]]立场
> - **[[Ontology|本体论]]** [[Hypothesis|假设]]存在不可直接观测但可以通过概率模型还原的潜在特质；这些特质是连续的、可量化的。
> - **认识论** 测量精度因人而异——IRT 为每位受试者提供个性化的能力估计及其误差，而非假设所有人共享同一误差方差。
> - **方法含义** 支持通过数学模型预测测验属性（在施测前即可预测）；支持[[Computerized Adaptive Testing|计算机自适应测验]]；要求大规模项目池的开发与校准。
> - **不能直接推出的东西** IRT 参数估计依赖于模型假设（单维性、局部独立性）被满足；违反假设时能力估计可能有偏；不能自动保证不同IRT模型产生相同的能力排序。

> [!theory-use] 如何用于研究
> - **作为理论框架** 为标准化测验的编制、等值和题库建设提供数学基础。
> - **作为分析工具** 通过 [[Rasch Measurement|Rasch 模型]]分析[[Item Analysis|项目难度]]与受试者能力的匹配度；通过多参数模型（2PL、3PL）评估区分度和猜测效应；通过差异项目功能（DIF）分析检测测验偏差。
> - **作为批判视角** 提醒研究者 [[Classical Test Theory|CTT]] 的项目参数样本依赖性如何限制跨研究比较，以及为什么大规模测评项目（如 [[PISA]]）选择 IRT 为基础。
> - **报告方式** 在研究报告中应明确使用的 IRT 模型类型、模型拟合指标、项目参数估计结果以及能力估计的精度。

---

## 适用边界

> [!theory-boundary] 适用边界
> - **适合解释** 大规模标准化测验的项目等值与题库建设；[[Computerized Adaptive Testing|计算机自适应测验]]的项目选择；跨群体测量不变性检验。
> - **谨慎使用** 小样本条件下，IRT 参数估计不稳定；多维度特质需要多维 IRT 模型，分析复杂度大幅提升。
> - **不适合解释** 常规课堂测验中几十个学生的[[Item Analysis|项目分析]]（[[Classical Test Theory|CTT]] 通常已足够）；非认知测验中缺乏明确潜在特质定义的测量。
> - **常见误用** 未检验单维性[[Hypothesis|假设]]就直接应用 IRT；夸大 IRT 对 CTT 的"替代"关系——二者各有适用场景，非简单替代关系。

---

## 发展脉络

> [!dev-timeline] 发展脉络
> - **1960 — [[Rasch Measurement|Rasch 模型]]提出** Georg Rasch 提出一参数逻辑斯蒂模型，奠定了客观测量的概率基础。
> - **1980 — Lord 出版 *Applications of Item Response Theory to Practical Testing Problems*** 系统化 IRT 的理论框架和实际应用。
> - **1990 — Rasch 测量成为教育测评主流工具** Wainer & Mislevy 等学者的推广使 IRT 进入大规模测评项目（如 NAEP、TIMSS、[[PISA]]）。
> - **2000 年代 — [[Computerized Adaptive Testing|计算机自适应测验]]普及** IRT 成为 CAT 的核心算法基础，大幅减少测验长度并提高测量精度。

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]] — 教材专章介绍 IRT 的基本原理，包括潜在特质[[Hypothesis|假设]]、[[Item Analysis|项目难度]]与区分度的样本独立性、单维性假设、[[Rasch Measurement|Rasch 模型]]，以及 IRT 在[[Computerized Adaptive Testing|计算机自适应测验]]中的应用。
