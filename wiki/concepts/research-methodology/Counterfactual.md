---
title: Counterfactual
aliases:
  - 反事实
  - 反事实推理
  - counterfactuals
  - counterfactual reasoning
summary: "因果推断中通过设想原因不存在时效果是否仍会发生来判断因果关系的一种推理方式，由 Mackie (1993) 系统引入因果分析"
type: concept
domain: "research-methodology"
related_count: 8
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - subject/research-methodology
  - topic/causation
related_concepts:
  - "[[Causality]]"
  - "[[Hypothesis]]"
  - "[[Emergence]]"
  - "[[Necessary and Sufficient Conditions]]"
  - "[[Fundamental Problem of Causal Inference]]"
related_theories: []
related_methods:
  - "[[Experimental Research]]"
  - "[[Random Assignment]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]"
confidence: medium
status: draft
created: 2026-06-17
updated: 2026-06-17
---

# Counterfactual

## 定义

> [!def] 核心定义
> 反事实（counterfactual）是识别[[Causality|因果关系]]是否正在发生或已经发生的一种推理方式：如果[[Hypothesis|假设]]的原因 X 不存在，那么效果 Y 也不会发生。由此提出的检验问题是："如果那个假设的原因不存在，效果还会发生或还是原来的样子吗？"如果答案是"否"，则可以推断 X 是一个真正的原因（Mackie, 1993）。

> [!concept-lens] 概念透镜
> - **含义** 反事实是对"如果情况不同，结果会怎样"的系统思考——它追问原因不存在时的替代结果。
> - **用途** 它帮助研究者区分真正的因果关系与单纯的伴随关系——两件事一前一后发生，并不意味着前者导致了后者。
> - **边界** 反事实推理不能独自证明因果性——它依赖关于替代情境的假设，而这些假设本身可能是不确定的。它也不适合没有明确反事实对照的情境，如复杂系统中多重交互因果的[[Emergence|涌现]]效应。

## 核心要素

> [!feature] 反事实推理的操作逻辑
> - **识别[[Hypothesis|假设]]原因 X**：明确哪个因素是待检验的候选原因。
> - **设想 X 不存在的情境** 构建"如果没有 X"的替代可能世界。
> - **判断 Y 是否仍会发生** 评估效果在此替代情境中的状态。
> - **归因判断** 如果 Y 不会发生或不会是原样，则 X 是一个促成原因——但通常只是众多原因之一（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 55–56]]）。

## 围绕概念形成的命题

> [!claim] 反事实作为[[Causality|因果]]识别的标志
> 一个区分因果是否发生的标志是反事实的存在——即确定 X（[[Hypothesis|假设]]的原因）的缺失会导致 Y（效果）的缺失（Mackie, 1993）。这与单纯的时间先后形成对比：休谟的"优先性"标准（原因先于效果）只是因果的[[Necessary and Sufficient Conditions|必要条件]]，反事实则提供了一个更强的检验。

> [!claim] 反事实推理在实验与非[[Experimental Research|实验研究]]中的不对称性
> 在真实验中，反事实问题通过设置控制组来回答——控制组被假定为指示如果干预未发生会怎样。但在大量非实验的教育研究中，控制组不存在或不可行，反事实推理依赖更不确定的假设和统计建模。

> [!warning] 反事实推理的局限
> - 如何知道替代情境中会发生什么？无法以确定性证明效果在没有某原因时就不会发生。
> - 在多重因果情境中，即使 X 不存在，效果可能仍会因其他原因而发生——反事实不能单独决定因果权重。
> - Holland（1986: 947）提出了"[[Fundamental Problem of Causal Inference|因果推断的基本问题]]"：同一个人不能同时处于接受和不接受处理的状态，因此反事实在个体层面无法被观察。

## 应用案例

> [!case] 冰面摔倒的例子
> 如果路上没有冰，我不会摔倒并骨折——因此冰的存在是效果的促成原因之一。但冰不是充分原因：即使有冰，如果我的平衡感好、视力好、光线充足、鞋底有抓地力、骨质不脆，我也不会摔断手臂。这说明了反事实推理在多重[[Causality|因果]]情境中的使用边界（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 55–56]]）。

> [!case] 实验控制组作为反事实
> 在教育实验中，控制组充当了反事实的代理——控制组的结果被假定为反映了实验组"如果没有接受干预"会发生的情况。这一假定的有效性取决于[[Random Assignment|随机分配]]是否成功实现了 ceteris paribus（其他条件相同）条件（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 56]]）。
