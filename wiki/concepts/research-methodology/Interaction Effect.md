---
title: Interaction Effect
aliases:
  - 交互效应
  - 交互作用
  - interaction effects
  - moderation effect
  - 调节效应
summary: "因子设计中一个自变量的效应依赖于另一个自变量的水平时出现的效应，是因子设计区别于单因子实验的核心价值"
type: concept
domain: "research-methodology"
related_count: 8
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - subject/research-methodology
  - experiment
  - causal-inference
related_concepts:
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Sample Size Determination]]"
related_methods:
  - "[[Factorial Design]]"
  - "[[Analysis of Variance]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-07-12
updated: 2026-07-13
---
# Interaction Effect

## 定义

> [!def] 交互效应
> 交互效应（Interaction Effect）指在[[Factorial Design|因子设计]]中，一个[[Independent Variable|自变量]]对[[Dependent Variable|因变量]]的效应**依赖于**另一个自[[Variable|变量]]的水平——即两个自变量的效应不是简单相加的，而是相互调节的（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 323–324]]）。

交互效应是与**主效应（main effect）**相对的概念——主效应指一个自变量独立于其他自变量的平均效应，交互效应指一个自变量的效应**因另一个自变量的水平不同而不同**。检验交互效应是因子设计区别于单因子实验的核心价值。

> [!concept-lens] 交互效应在[[Causality|因果推断]]中的位置
> - **含义** 交互效应意味着"X₁ 对 Y 的效应取决于 X₂ 的值"——这不是两个独立因果关系的叠加，而是一个条件性的因果结构。
> - **用途** 它帮助研究者发现**条件性因果关系**——哪些条件下干预有效、哪些条件下无效或反向。这在教育研究中尤为关键，因为教学干预的效果通常因学生特征、学校环境和实施条件而异。
> - **边界** 交互效应不等于主效应的缺失——可能两个主效应都不显著，但交互效应显著；也可能主效应显著但交互效应不显著。交互效应的存在意味着报告主效应时必须同时报告交互效应，否则结论可能是误导性的。

> [!boundary]- 概念边界
> - 不等于主效应的缺失 — 可能两个主效应都不显著但交互效应显著，也可能主效应显著但交互效应不显著。交互效应的存在意味着报告主效应时必须同时报告交互效应。
> - 不等于[[Causality|因果关系]]本身 — 交互效应描述的是多个原因之间的结构关系（X₁ 的效应取决于 X₂），而非单个原因与效果之间的关系。
> - 不适用于单因子设计 — 交互效应只在存在两个或以上[[Independent Variable|自变量]]的[[Factorial Design|因子设计]]中才能被检验，单因子实验无法检测交互效应。

---

## 核心要素

> [!feature] 交互效应的关键特征
> - **条件依赖性** 一个[[Independent Variable|自变量]]的效应不是恒定的，而是随另一个自[[Variable|变量]]的水平变化。例如，资源可用性对成绩的效应可能取决于学习动机水平——高动机时资源效应强，低动机时资源效应弱。
> - **非可加性** 交互效应意味着两个自变量的联合效应不等于各自独立效应之和。在[[Analysis of Variance|方差分析]]中，交互效应项捕获了这种非可加性。
> - **图示特征** 在交互效应图中，两条线不平行——当一条线的斜率因另一条线的水平而不同时，即存在交互效应。两条线交叉是最强的交互形式（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, Figure 16.3]]）。
> - **三向或更高阶交互** 当存在三个或更多自变量时，可能出现三向交互效应——解释难度随阶数指数增长，且通常需要很大的[[Sample Size Determination|样本量]]才能检测到。

---

## 概念辨析

> [!contrast-table] 交互效应 vs 主效应
> | 维度 | 主效应（Main Effect） | 交互效应（Interaction Effect） |
> |---|---|---|
> | **含义** | 一个[[Independent Variable|自变量]]对[[Dependent Variable|因变量]]的独立平均效应 | 一个自[[Variable|变量]]的效应依赖于另一个自变量的水平 |
> | **检验方式** | 比较该自变量各水平的边际均值 | 比较一个自变量在不同条件下的简单效应 |
> | **图示** | 平行线（各水平的效应恒定） | 不平行线（各水平的效应因另一变量而变化） |
> | **[[Causality|因果]]含义** | "X 对 Y 有效应" | "X 对 Y 的效应**取决于** Z" |

---

## 应用案例

> [!case] 性别 × 年龄对数学学习动机的交互效应
> 以性别和年龄为两个[[Independent Variable|自变量]]研究数学学习动机时（Figure 16.3），男女之间的动机差异不是恒定的，而是**随年龄变化**——在低年龄段男女差异可能较小，进入青春期后差异可能扩大或逆转。性别效应取决于年龄，年龄效应也因性别而异。如果只检验性别的主效应，会发现"男女在数学动机上存在差异"；但如果同时检验交互效应，会发现这一差异**只在某些年龄段成立（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 324]]）**。

> [!case] 资源可用性 × 学习动机的交互效应
> 在 3×3 [[Factorial Design|因子设计]]中，资源可用性（有限、中等、高）和学习动机（低、中等、高）各为自[[Variable|变量]]。可能发现：有限资源+低动机的组合对考试成绩有显著负面影响，而中等资源+高动机的组合没有显著效应。如果只检验两个主效应，会得出"资源可用性影响成绩"和"学习动机影响成绩"两个独立结论——但交互效应揭示了更精细的条件性关系：资源的影响**取决于**动机水平（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 323–324]]）。
