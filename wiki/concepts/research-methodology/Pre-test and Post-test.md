---
title: Pre-test and Post-test
aliases:
  - 前测与后测
  - pretest and posttest
  - pre-test and post-test
  - 前测
  - 后测
  - pretest
  - posttest
summary: "实验中在干预前后分别进行的测量，前测建立基线等价性，后测测量干预效应，两者的时机安排直接影响因果推断的有效性"
type: concept
domain: "research-methodology"
related_count: 8
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - subject/research-methodology
  - experiment
related_concepts:
  - "[[Internal Validity]]"
  - "[[Pre-test Sensitisation]]"
  - "[[Causality]]"
  - "[[Dependent Variable]]"
related_methods:
  - "[[Experimental Research]]"
  - "[[Pretest-Posttest Control Group Design]]"
  - "[[Repeated Measures Design]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-07-13
updated: 2026-07-13
---
# Pre-test and Post-test

## 定义

> [!def] 前测与后测
> 前测（Pre-test）和后测（Post-test）是[[Experimental Research|实验研究]]中两个关键的测量时间点：**前测**在干预开始前测量，用于建立基线、验证组间等价性；**后测**在干预结束后测量，用于评估干预对[[Dependent Variable|因变量]]的效应。在[[Pretest-Posttest Control Group Design|前后测控制组设计]]中，因果效应被量化为 (E₁−E₂) − (C₁−C₂)（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 314, 334–335]]）。

> [!concept-lens] 前测与后测在[[Causality|因果推断]]中的功能
> - **含义** 前测回答"两组在干预前是否等价"，后测回答"干预后两组是否存在差异"。二者共同构成了因果推断的**前后比较框架**。
> - **用途** 前测基线是因果推断的逻辑起点——只有基线等价时，后测差异才能归因于干预。后测是因果效应的直接证据——干预效果的量化取决于后测的准确性和时机。
> - **边界** 前测和后测不等于因果推断本身——它们提供的是测量数据，因果推断还需要[[Random Assignment|随机化]]、控制组和对替代解释的排除。

---

## 核心要素

> [!feature] 前测与后测的关键考量
> - **前测的功能** (1) 验证[[Random Assignment|随机化]]是否成功——两组前测均值应接近；(2) 建立基线——为个体的变化量提供参照；(3) 在有些设计中可作为配对[[Variable|变量]]的来源。
> - **后测的功能** (1) 测量干预后的结果状态；(2) 与前测比较以量化变化量；(3) 与控制组后测比较以分离干预的净效应。
> - **前测的时机** 应尽可能靠近干预开始时间，以减少干预前混淆效应的影响。前测与干预之间的间隔越长，期间发生的外部事件越可能混淆基线状态。
> - **后测的时机** 这是两者中更复杂的问题。Morrison (2009, p. 168) 指出实验程序容易遭遇时机问题——太早，效应可能尚未显现；太晚，效应可能已经消失或被其他因素淹没。

---

## 围绕概念形成的命题

### 后测时机是因果推断的关键决策

> [!claim] 后测时机的选择直接影响[[Causality|因果推断]]的有效性
> 实验通常只有两个测量时间点。尽早后测可以减少干预后混淆效应的影响，但可能错失**延迟效应**——例如 15 岁学完莎士比亚时可能极其厌恶英国文学，但多年后才意识到这段经历播下了热爱的种子。延迟后测可捕捉长期效果，但无法确定是特定[[Independent Variable|自变量]]还是干预后介入的其他因素导致了效应。近因效应（课程结束时立即考试的高分可能仅是近因效应而非真实学习效果）和排练效应（期末考试前集中复习的高分可能来自短时排练而非教学干预）进一步混淆了后测的解释。

### 前测本身可能成为威胁

> [!claim] [[Pre-test Sensitisation|前测敏感化]]是前后测设计的内在局限
> 前测可能使受试者对干预[[Variable|变量]]更加敏感（Good, 1963）。[[Interaction Effect|交互效应]]是联合效应——即使没有主效应也可能出现。前测×处理的交互效应意味着在有前测的设计中观察到的处理效应可能无法推广到无前测的情境。[[Solomon Four-Group Design|所罗门四组设计]]通过增设无前测组来分离和量化这一效应。

---

## 概念辨析

> [!contrast-table] 前测 vs 后测 vs 多次测量的时间序列
> | 维度 | 前测 | 后测 | 多次前后测（[[Time Series Design\|时间序列]]） |
> |---|---|---|---|
> | **目的** | 建立基线、验证等价 | 测量干预效应 | 观察趋势变化，区分即时/延迟/无效应 |
> | **时机** | 干预前 | 干预后 | 干预前后各多次 |
> | **主要威胁** | [[Pre-test Sensitisation\|前测敏感化]] | 时机选择（太早/太晚） | [[Order Effects\|练习效应]]、历史事件 |
> | **缺失时的代价** | 无法验证等价、无法测量个体变化 | 无法评估干预效应 | 无法区分干预效应与已有趋势 |

---

## 应用案例

> [!case] 莎士比亚的后测时机困境
> 学生 15 岁时学完莎士比亚单元后立即进行后测，可能因为近因效应得分较高。但如果他们在后测中报告"极其厌恶英国文学"，这可能是对刚结束的密集学习的真实反应。然而，多年后他们可能回顾这段经历是播下热爱莎士比亚的种子——一个立即后测无法捕捉的延迟效应。实施多个后测——一个在单元结束后不久、另一个等效版本在一个月后——可以区分即时反应和持久效果（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 335]]）。

> [!case] 博茨瓦纳教师培训的前后测
> Adeyemi (1992) 在研究生教育文凭课程的第一节课上以 Barth/Shermis 社会科偏好量表（BSSPS）进行前测，一年课程结束时再次施测（后测）。48 名学生从多数持有公民传递取向转向更认同社会科学和反思探究传统。研究者谨慎地承认"社会科课程可能是导致这一现象的原因，尽管其他外部[[Variable|变量]]也可能在起作用"——这种谨慎很到位，因为变化方向恰好与博茨瓦纳教育部 1989 年发布的九年社会科教学大纲的建议一致。前测和后测只能展示变化发生，但不能证明变化是由课程导致的（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 335–336]]）。
