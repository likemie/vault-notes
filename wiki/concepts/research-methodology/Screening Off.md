---
title: Screening Off
aliases:
  - 筛选隔离
  - 屏蔽
  - screening off
summary: "Reichenbach (1956) 提出的因果分析概念，指两个看似相关的变量因被第三个共同原因隔开而彼此不存在因果关系"
type: concept
domain: "research-methodology"
related_count: 3
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - subject/research-methodology
  - topic/causation
related_concepts:
  - "[[Variable]]"
  - "[[Causality]]"
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]"
confidence: medium
status: draft
created: 2026-06-17
updated: 2026-06-17
---

# Screening Off

## 定义

> [!def] 核心定义
> 筛选隔离（screening off）是指两个[[Variable|变量]]看似存在关联（covariance 或 correlation），但实际上被一个共同的原因隔离开来——二者只有相关关系而没有[[Causality|因果关系]]。这一概念由 Reichenbach（1956）提出，后由 Salmon（1998）进一步发展。

> [!concept-lens] 概念透镜
> - **含义**：当变量 C 同时导致变量 A 和变量 B 时，A 和 B 之间表现出的相关关系仅仅是 C 的效应——A 和 B 之间不存在直接的因果连接。C "筛选隔离"了 A 和 B。
> - **用途**：它在因果分析中用于排除虚假相关（spurious correlation），帮助研究者区分真正的因果关系与统计伴随关系。
> - **边界**：筛选隔离假定研究者能正确识别共同原因 C——但在多重因果情境中，识别全部的筛选因素可能是极其困难甚至不可能的。

## 核心要素

> [!feature] 筛选隔离的逻辑结构
> - **共同原因 C**：一个第三[[Variable|变量]]同时导致 A 和 B。
> - **表面关联 A ↔ B**：A 和 B 在数据上表现出伴随变化，但这完全由 C 解释。
> - **因果独立**：在控制 C 的条件下，A 和 B 之间的关联消失——它们彼此不产生因果影响。
> - **操作化**：通过偏相关（partial correlation）或结构方程模型等技术"筛掉"不相关的因变量。

## 围绕概念形成的命题

> [!claim] 筛选隔离区分相关与因果
> 筛选隔离的核心洞见是：两个[[Variable|变量]]之间的相关关系不能自动等同于[[Causality|因果关系]]。气压计读数下降与暴风雨高度相关，但气压计读数下降不导致暴风雨——两者都被第三个因素（气压下降）所引起（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 59–60]]）。

> [!claim] 筛选隔离要求识别并控制额外变量
> 在确认真正的因果性时，研究者必须筛掉与所研究情境直接相关的变量无关的因变量——例如通过控制额外变量的效应（先验/外生变量或中介/内生变量），以确保一个变量不会被认为对另一个有影响而事实上并非如此（Pearl, 2009: 423–7）。

## 应用案例

> [!case] 脚大与手大的虚假相关
> 一个人的手可能因脚大而被预测为大——但手大并不导致脚大。共同原因在于对二者的遗传倾向。这体现了筛选隔离的基本逻辑：表面相关掩盖了一个共同的（遗传）因果来源（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 60]]）。

> [!case] 吸烟-运动-心脏病
> 吸烟（A）与运动（C）高度相关——吸烟者比不吸烟者运动更多。尽管吸烟导致心脏病（B），但运动实际上是对抗心脏病的更强预防措施。表面上，出现了吸烟"预防"心脏病的悖论——因为运动（C）这一第三[[Variable|变量]]筛选隔离了吸烟（A）和心脏病（B）之间的真正关系（Morrison, 2009: 45; Hitchcock, 2002: 9）（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 68]]）。

## 相关方法

- **偏相关**（partial correlation）——用于在统计上控制第三[[Variable|变量]]的效应
- **结构方程模型**（structural equation modelling）——用于检验包含多个变量和因果路径的复杂因果模型
