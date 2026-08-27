---
title: Computerized Adaptive Testing
aliases:
  - 计算机自适应测验
  - 计算机化自适应测验
  - adaptive testing
  - 适应性测验
summary: "基于项目反应理论、由计算机根据受试者先前反应动态选择后续题目难度的测验方式，首题置于假设能力范围中位，答对则加大难度、答错则减轻难度，可减少约50%测验题目并即时计分"
type: concept
domain: "research-methodology"
related_count: 9
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
  - "[[Reliability]]"
  - "[[Item Analysis]]"
  - "[[Construct Validity]]"
  - "[[Standard Error]]"
related_theories:
  - "[[Item Response Theory]]"
related_methods:
  - "[[Pilot Testing]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]]"
related_instruments:
  - "[[Consensual Assessment Technique]]"
confidence: medium
status: draft
created: 2026-07-24
updated: '2026-08-27'
---

# Computerized Adaptive Testing

---

## 定义

> [!def] 核心定义
> 计算机自适应测验（computerized adaptive testing, [[Consensual Assessment Technique|CAT]]）是一种测验实施方式，其中具体施测哪些题目的决定基于受试者对先前题目的反应（Wainer, 1990; Aiken, 2003, pp. 50–52; Wainer & Dorans, 2000）。首题置于[[Hypothesis|假设]]能力范围的中位难度；如果受试者答对，下一题难度增加；如果答错，下一题难度降低。受试者按自己的节奏作答，测验即时计分并提供反馈。

> [!concept-lens] 概念透镜
> - **含义** CAT 不是一种新的测验内容，而是一种新的测验实施逻辑——它动态改变施测题目的顺序和难度，使每个受试者获得一套量体裁衣的测验。
> - **用途** 特别适用于大规模测验场景。当预期受试者能力范围极广时，CAT 避免了高能力者因大量简单题而浪费时间、低能力者因大量难题而受挫和猜测。
> - **边界** CAT 依赖大型经校准的题目库和[[Item Response Theory|项目反应理论]]（IRT）的数学基础；不适用于题目数量有限的小规模自编测验。

---

## 核心要素

> [!info] [[Consensual Assessment Technique|CAT]] 解决的核心问题
> 在大规模测验中，受试者能力范围极广。题目太容易则无法测量高能力者的能力范围（所有人全对），太困难则无法测量低能力者的能力范围（所有人全错）。高能力者需要浪费时间做大量简单题才能到达难题，低能力者需要猜测难题答案。CAT 通过使测验灵活且适应受试者来解决这些效率与[[Reliability|信度]]问题。

> [!strength] CAT 的优势（Aiken, 2003, p. 51; Wainer & Dorans, 2000）
> - **减少题目数约 50%** 大量过易或过难的无效题目被自动跳过
> - **按自己节奏作答** 受试者不会被打击但可被挑战
> - **即时计分与反馈** 计算机自动给出分数
> - **更广泛的题目范围** 题库可包含远超传统测验数量的题目
> - **更高的测量精度和信度** [[Item Analysis|题目难度]]与受试者能力匹配
> - **测验安全性增强** 每位受试者看到不同的题目组合，减少了题目泄露和作弊风险
> - **避免答题纸问题** 不需要答题纸，受试者不会因涂卡错误而损失分数

> [!feature] CAT 的技术前提（Flaugher, 1990）
> - **大型经校准的题目库** 每个内容领域需要足够数量、足够多样性和难度跨度的题目
> - **题目独立性** 每位受试者对任一题目的反应不应影响其对其他题目的反应（[[Item Response Theory|IRT]] 局部独立性[[Hypothesis|假设]]）
> - **单维性验证** 所有题目必须测量单一能力或维度，需经[[Pilot Testing|预测试]]并验证难度和区分度
> - **题目选择算法** 需要明确的规则决定何时终止测验（达到预定精度、达到最大题目数或能力估计稳定）
> - **干扰项控制** 减少干扰项的影响，明确单维性和多维性的测量能力

---

## 争议与批评

> [!warning] [[Consensual Assessment Technique|CAT]] 的信效度挑战
> - **认知过程差异** 使用计算机屏幕和程序所需的心理过程与纸笔测验不同（如阅读屏幕与阅读纸张），可能改变测验的[[Construct Validity|构念效度]]
> - **动机与焦虑影响** 受试者使用计算机时的动机和焦虑水平可能升高或降低，影响表现的真实性
> - **物理环境影响** 光照条件、屏幕眩光、机器噪音、软件加载和运行过程可能对受试者产生显著影响
> - **[[Reliability|信度]]含义的转换** 在 [[Item Response Theory|IRT]] 框架中，[[Reliability|信度]]从测验变异性的指标转变为受试者表现[[Standard Error|标准误]]的指标。传统标准误公式[[Hypothesis|假设]]所有分数的误差方差相同，而 IRT 假设误差方差取决于每位受试者的能力——传统单一平均误差方差在此框架下可能非常粗糙甚至误导（Thissen, 1990）
> - **题目池质量风险** 题目数量越大，纳入质量较差题目的风险也相应增加

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]] — 教材 24.9 节介绍 [[Consensual Assessment Technique|CAT]] 的工作原理、七项优势、五项信效度挑战以及 Flaugher（1990）的技术前提
