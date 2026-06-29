---
title: Fundamental Problem of Causal Inference
aliases:
  - 霍兰德因果推断基本问题
  - 因果推断的基本问题
  - fundamental problem of causal inference
  - Holland's fundamental problem
  - Fundamental Problem of Causal Inference
summary: "Holland (1986) 提出的因果推断根本性困难：同一个人不能同时处于接受和不接受干预的状态，因此因果效应在个体层面无法被观察"
type: concept
domain: "research-methodology"
related_count: 7
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - subject/research-methodology
  - topic/causation
related_concepts:
  - "[[Causality]]"
  - "[[Counterfactual]]"
  - "[[Variable]]"
  - "[[Hypothesis]]"
related_theories: []
related_methods:
  - "[[Random Assignment]]"
  - "[[Experimental Research]]"
  - "[[Randomised Controlled Trials]]"
related_persons: []
related_facts: []
related_arguments: []
confidence: medium
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# Fundamental Problem of Causal Inference

## 定义

> [!def] 核心定义
> Holland（1986: 947）提出的[[Causality|因果推断]]基本问题（fundamental problem of causal inference）是指：**同一个人不能同时处于接受干预和不接受干预的状态**。因此，因果效应——即同一人在接受干预与未接受干预时的结果差异——在个体层面**永远无法被观察**。研究者只能在群体层面比较处理组和对照组的平均值，用群体平均差异来推断因果效应。

> [!concept-lens] 概念透镜
> - **含义** 这是一个逻辑问题而非技术问题——无论实验设计多么完美、[[Random Assignment|随机分配]]多么严格，个体层面的[[Counterfactual|反事实]]永远不可观察。
> - **用途** 它解释了为什么随机化不能完全解决因果推断问题——随机化只能在群体层面近似反事实，永远无法在个体层面证明因果。
> - **边界** 这一基本问题在真实验（随机分配）中通过群体平均得到缓解，但无法被消除。在非[[Experimental Research|实验研究]]中，这一问题更为严重。

## 核心要素

> [!feature] 基本问题的三层含义
> - **个体[[Counterfactual|反事实]]的不可观察性**：对于任何个体，我们只能观察到其接受干预的结果，或未接受干预的结果，永远不能同时观察两种状态。
> - **群体平均的替代性**[[Randomised Controlled Trials|随机对照试验]]通过比较处理组均值与对照组均值来近似平均[[Causality|因果]]效应，但这是群体层面的近似，不是个体层面的证明。
> - **[[Random Assignment|随机化]]的局限**：随机分配通过让未控制[[Variable|变量]]在组间均匀分布来克服混淆，但"无论随机分配多么完美，都只能在群体层面比较平均值，永远无法在个体层面观察反事实"。

## 概念辨析

> [!contrast-table] 基本问题 vs 相关概念
> | 概念 | 核心问题 | 与基本问题的关系 |
> |------|---------|----------------|
> | **基本问题** | 个体[[Counterfactual\|反事实]]不可观察 | — |
> | [[Counterfactual\|反事实推理]] | 如果 X 不存在，Y 是否仍会发生？ | 反事实推理本身也受制于基本问题——反事实永远不可观察 |
> | [[Random Assignment\|随机分配]] | 通过群体平均近似反事实 | 缓解但无法消除基本问题 |
> | 混淆[[Variable\|变量]] | 未测量变量同时影响 X 和 Y | 混淆是额外的问题，叠加在基本问题之上 |

## 围绕概念形成的命题

> [!claim] 基本问题无法仅通过[[Random Assignment|随机化]]充分缓解
> 这一问题可能无法仅通过随机化充分缓解——因为无论随机分配多么完美，都只能在群体层面比较平均值，永远无法在个体层面观察[[Counterfactual|反事实]]。随机化采纳ceteris paribus（其他条件相同）条件，[[Hypothesis|假设]]未控制[[Variable|变量]]在组间均匀分布——但这本身是一个"大胆且可能危险的假设"。

> [!claim] 基本问题对教育研究的实际意义
> 在教育情境中，由于学校班级通常是预成的、家长可能干预分配、缺失数据在不同组间分布不均，基本问题变得更加尖锐。这意味着即使是设计良好的[[Randomised Controlled Trials|RCT]]，其推论的效度也是临时且局部的。

## 应用案例

> [!case] 个体层面[[Causality|因果推断]]的不可能性
> [[Hypothesis|假设]]一项研究评估新的阅读教学法对学生阅读成绩的影响。对于任何一个特定学生，我们只能观察到她在新教学法下的成绩，或者她在传统教学法下的成绩——永远不能同时观察两种状态。因此，我们永远不能说"这个学生因新教学法提高了 X 分"。我们只能说"平均而言，接受新教学法的学生比对照组高 Y 分"。这就是 Holland 基本问题的实际含义。
