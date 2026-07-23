---
title: Computerized Adaptive Testing
aliases:
  - 计算机自适应测验
  - 计算机化自适应测验
  - CAT
  - adaptive testing
  - 适应性测验
summary: "基于项目反应理论、由计算机根据受试者先前反应动态选择后续项目难度的测验方式，首题置于假设能力范围中位，答对则加大难度、答错则减轻难度，可减少约50%测验项目并即时计分"
type: concept
domain: "research-methodology"
related_count: 7
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - theme/measurement
  - theme/assessment
  - method/quantitative
  - theme/technology
related_concepts:
  - "[[Hypothesis]]"
  - "[[Construct Validity]]"
  - "[[Reliability]]"
  - "[[Standard Error]]"
related_methods:
  - "[[Pilot Testing]]"
related_theories:
  - "[[Item Response Theory]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]]"
confidence: medium
status: draft
created: 2026-07-24
updated: 2026-07-24
---

# Computerized Adaptive Testing

---

## 定义

> [!def] 核心定义
> 计算机自适应测验（computerized adaptive testing, CAT）是一种测验方式，其中具体施测哪些测验项目的决定是基于受试者对先前项目的反应做出的（Wainer, 1990; Aiken, 2003, pp. 50–52）。首题置于[[Hypothesis|假设]]能力范围的中位难度；如果受试者答对，则下一题难度增加；如果答错，则下一题难度降低。受试者按自己的节奏作答，测验即时计分并提供反馈。

> [!concept-lens] 概念透镜
> - **含义** CAT 不是一种新的测验内容，而是一种新的测验实施逻辑——它动态改变施测项目的顺序和难度，使每个受试者获得一套"量身定制"的测验。
> - **用途** 特别适用于大规模测验场景，预期受试者能力范围极广时，CAT 避免了高能力者因大量简单题而浪费时间、低能力者因大量难题而受挫和猜测的困境。
> - **边界** CAT 依赖大型、经过校准的项目库和[[Item Response Theory|项目反应理论]]（IRT）的数学基础；不适用于项目数量有限的小规模自编测验。

---

## 核心要素

> [!feature] 核心特征
> - **适应性施测逻辑** 首题置于能力范围中位 → 答对则加大下一题难度 → 答错则降低下一题难度；每题后的决策基于对受试者当前能力的最新估计。
> - **大幅减少项目数量** CAT 可减少约 50% 的测验项目（Aiken, 2003, p. 51），因为大量过易或过难的无效项目被自动跳过。
> - **即时计分与反馈** 计算机会在测验结束时自动给出分数，受试者可即时获得表现信息。
> - **测验安全性增强** 每位受试者看到不同的项目序列，减少了项目泄露和作弊风险。
> - **避免答题纸问题** 不需要答题纸，受试者不会因涂卡错误而损失分数。

> [!feature] 技术要求
> - **大型经校准的项目库** 每个内容领域需要足够数量、足够多样性和难度跨度的项目（Flaugher, 1990）。
> - **项目独立性** 每位受试者对任一项目的反应不应影响其对其他项目的反应（[[Item Response Theory|IRT]] 局部独立性[[Hypothesis|假设]]）。
> - **单维性验证** 所有项目必须测量单一能力或维度，项目需经过[[Pilot Testing|预测试]]并验证其难度和区分度。
> - **项目选择算法** 需要明确的规则决定何时终止测验（达到预定精度、达到最大项目数或能力估计稳定）。

---

## 争议与批评

> [!critique] CAT 的信效度挑战
> - **认知过程差异** 使用计算机屏幕和程序所需的心理过程与纸笔测验不同（如阅读屏幕 vs. 阅读纸张），可能改变测验的[[Construct Validity|构念效度]]。
> - **动机与焦虑影响** 受试者使用计算机时的动机和焦虑水平可能升高或降低，影响表现的真实性。
> - **物理环境影响** 光照条件、屏幕眩光、机器噪音、软件加载和运行过程等物理因素可能对受试者产生显著影响。
> - **[[Reliability|信度]]含义的转换** 在 [[Item Response Theory|IRT]] 框架中，信度从测验变异性的指标转变为受试者表现[[Standard Error|标准误]]的指标。传统标准误公式[[Hypothesis|假设]]所有分数的误差方差相同，而 IRT 假设误差方差取决于每位受试者的能力——传统的单一平均误差方差在此框架下可能非常粗糙甚至误导（Thissen, 1990）。
> - **项目池质量风险** 项目数量越大，纳入质量较差项目的风险也相应增加。

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]] — 教材 24.9 节介绍 CAT 的工作原理、对大规模测验的优势（减少项目数、即时计分、增加测验安全性）以及信效度方面的挑战。
