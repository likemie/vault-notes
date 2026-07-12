---
title: Order Effects
aliases:
  - 顺序效应
  - carry-over effect
  - 延续效应
  - practice effect
  - 练习效应
  - sequence effect
summary: "重复测量设计中因干预呈现顺序而非干预本身导致结果差异的混淆效应，主要包括延续效应和早期优势效应，可通过拉丁方排列或随机化顺序来均衡"
type: concept
domain: "research-methodology"
related_count: 5
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - subject/research-methodology
  - experiment
  - bias-control
related_concepts:
  - "[[Internal Validity]]"
related_methods:
  - "[[Repeated Measures Design]]"
  - "[[Pilot Testing]]"
  - "[[Random Assignment]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-07-12
updated: 2026-07-13
---
# Order Effects

## 定义

> [!def] 顺序效应
> 顺序效应（Order Effects）是[[Repeated Measures Design|重复测量设计]]中的核心威胁——指因干预或实验条件的**呈现顺序**而非干预本身导致的结果差异。当同一组参与者接受多种实验条件时，先接受的条件可能影响后续条件的表现，使得比较结果不仅反映条件本身的效应，还包含了顺序带来的混淆（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 325–326]]）。

> [!concept-lens] 顺序效应在效度威胁中的位置
> - **含义** 顺序效应是重复测量设计中特有的[[Internal Validity|内部效度]]威胁——它混淆了"干预 A 真的比干预 B 更有效吗"和"干预 A 只是因为在干预 B 之前出现才显得更有效吗"这两个问题。
> - **用途** 识别顺序效应帮助研究者区分处理效应和位置效应，从而更准确地比较不同干预条件。如果顺序效应未被控制，研究结论可能指向错误的干预。
> - **边界** 顺序效应只存在于**同一组参与者接受多个条件**的设计中——在组间设计中不存在（因为每人只接受一个条件）。顺序效应不等于干预本身的"学习效应"或"适应效应"——它是因呈现顺序而产生的系统性偏差，而非干预内容的必然结果。

---

## 核心要素

> [!feature] 顺序效应的三种形式与均衡策略
> - **延续效应（Carry-over Effect）** 第一次干预的影响**持续**到第二次干预的测量时段——即前一次干预的效果没有完全消退，残留到了后续条件的评估中。例如，先接受一种记忆策略训练的学生，在使用另一种策略时可能仍在无意中使用前一种策略，导致第二种策略的"纯效果"无法被独立评估。
> - **早期优势效应** 早期的干预可能比后期的干预产生更大的效应——不是因为早期干预更有效，而是因为参与者在研究初期更投入、更专注或更不疲倦。
> - **拉丁方排列的均衡逻辑** 在三干[[Pilot Testing|预实验]]中，通过系统性排列六种序列使每种干预出现在每个位置的概率相等，顺序效应在各干预之间被**均衡**——它仍然存在，但不再系统性地偏向某一干预。也可通过[[Random Assignment|随机化]]顺序来应对，但不保证平衡序列（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 325–326]]）。

> [!boundary]- 概念边界
> - 不等于干预本身的"学习效应" — 学习效应是干预内容的必然结果（学会了一项技能），顺序效应是因呈现顺序而非干预内容而产生的系统性偏差。
> - 只存在于[[Repeated Measures Design|重复测量设计]]中 — 组间设计中每人只接受一个条件，不存在顺序效应。

---

## 应用案例

> [!case] 反馈类型的重复测量研究
> 同一组学生在三次写作任务后分别收到即时反馈、延迟反馈和无反馈，比较三次修改稿的质量差异。如果所有学生都按"即时→延迟→无反馈"的顺序接受条件，那么即时反馈的优势可能被延续效应放大（学生已经从前一次反馈中获得了写作改进），延迟反馈的优势可能被早期优势效应掩盖（学生在研究后期更疲劳）。拉丁方排列让六分之一的学生接受"延迟→无反馈→即时"、六分之一接受"无反馈→即时→延迟"等序列，使顺序效应在三种反馈类型之间均衡。

> [!case] 教学方法的重复测量比较
> 同一批学生在三个不同单元分别接受讲授法、讨论法和翻转课堂教学。如果所有学生都按"讲授→讨论→翻转"的顺序学习，翻转课堂可能因为出现在最后而承受疲劳效应的不利影响，也可能因为学生已经通过前两个单元积累了知识而获得延续效应的有利影响——两种顺序效应方向相反，无法判断净偏差的方向。通过拉丁方排列安排方法顺序，每种方法在不同单元位置上的分布均衡，确保比较的公平性（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 325–326]]）。
