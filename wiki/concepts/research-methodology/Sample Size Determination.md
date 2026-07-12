---
title: Sample Size Determination
aliases:
  - 样本量确定
  - sample size
  - 样本量
  - determining sample size
  - sample size calculation
summary: "研究设计中确定样本大小的决策过程，涉及研究目的、总体规模、置信水平与置信区间、变量类型、统计方法要求、子组数量和预期无回应率等多重因素，是抽样规划的核心环节"
type: concept
domain: "research-methodology"
related_count: 14
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - method/sampling
  - quantitative-research
  - research-design
related_concepts:
  - "[[Research Purpose]]"
  - "[[Heterogeneity]]"
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Confidence Interval]]"
  - "[[Independent Variable]]"
related_theories: []
related_methods:
  - "[[Power Analysis]]"
  - "[[Survey Research]]"
  - "[[Ethnography]]"
  - "[[Qualitative Research]]"
  - "[[Chi-Squared Test]]"
  - "[[Multiple Regression]]"
  - "[[Random Sampling]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
confidence: medium
status: draft
created: 2026-06-21
updated: 2026-06-21
---
# Sample Size Determination

## 定义

> [!def] 核心定义
> 样本量确定（Sample Size Determination）是研究设计中决定需要从总体中抽取多少个案例（个体、学校、班级等）作为样本的决策过程。正确的样本量取决于[[Research Purpose|研究目的]]、总体的性质与[[Heterogeneity|异质性]]、所需准确度、预期回应率、研究包含的[[Variable|变量]]数量、所需统计方法、子组数量以及研究是定量还是定性等多个相互交织的因素。样本量确定没有统一答案，但存在一系列经验法则、统计要求和数学公式可供参考。

> [!concept-lens] 概念透镜
> - **含义** 样本量确定指向在资源约束与研究精确度之间做出权衡的决策过程，核心问题是"多少案例才算足够"。
> - **用途** 帮助研究者提前规划数据收集规模，确保研究具有足够的统计功效、子组代表性和分析可行性。
> - **边界** 样本量确定不是纯粹数学计算——其中包含大量判断成分（如预期效应大小、可接受的误差范围）。它也不同于事后功效分析（post hoc [[Power Analysis]]）。

> [!citation-card]- 关键表述
> 一个经常困扰新手研究者的问题是：研究的样本应该多大？没有明确的答案，因为正确的样本量取决于[[Research Purpose|研究目的]]、所审视总体的性质、所需准确度、预期回应率、研究包含的变量数量，以及研究是定量还是定性。（第8章，p.144）
>
> *A question that often plagues novice researchers is just how large their samples for the research should be. There is no clear-cut answer...* (Ch. 8, p. 144)

---

## 核心要素

### 影响样本量的多重因素

> [!feature] 影响样本量的因素
> - **[[Research Purpose|研究目的]]与设计** [[Survey Research|调查研究]]通常需大样本（尤其是推论统计）；[[Ethnography|民族志]]或[[Qualitative Research|质性研究]]样本量通常较小。相关研究 ≥ 30 例，[[Causality|因果]]比较与实验 ≥ 15 例，调查每个主要子组 ≥ 100、每个次要子组 20–50（Borg & Gall, 1979: 194–5）。
> - **总体规模与[[Heterogeneity|异质性]]** 总体越大，所需样本越大；总体异质性越强，所需样本越大。但 Krejcie & Morgan（1970）发现，当总体增至一定程度后，所需样本量趋于恒定（约 384 例）。
> - **[[Confidence Interval|置信水平]]与[[Confidence Interval|置信区间]]** 置信水平越高（如 99% vs 95%），样本量越大；置信区间越小（如 ± 3% vs ± 5%），样本量越大。常规策略：95% 置信水平 + 3% 置信区间。
> - **[[Variable|变量]]类型** 类别数据（categorical data）通常比连续数据（continuous data）需要更大的样本。类别数据边际误差通常取 5%，连续数据取 3%（Bartlett et al., 2001: 45）。
> - **统计方法要求**[[Chi-Squared Test|卡方检验]]要求 80% 单元格 ≥ 5 例；[[Multiple Regression|多元回归]]要求观察值与[[Independent Variable|自变量]]比率 ≥ 5:1（连续数据建议 10:1）；因子分析要求 ≥ 100 例（Bartlett et al., 2001: 48–9）。
> - **子组数量** 子组（strata）越多，样本量越大——通常呈几何级增长而非算术级。Borg & Gall（1979: 186）建议从最小子组"向上"计算总样本量。
> - **预期无回应与流失** 需考虑无回应、不完整或无效回应、参与者流失和样本死亡。若无准入和回应保障，可能需要将所需样本量翻倍以建立冗余（Gorard, 2003: 60）。

### 定量研究的经验法则

> [!feature] 定量样本量经验法则
> - **30 规则** 若使用统计分析，30 是公认的最小案例数（但非常小）。
> - **每变量 30 案例** 每个变量至少需 30 个案例作为最低估计，此为"经验法则"。
> - **Gorard 公式** 从每个单元格最少案例数（如 6）出发，乘以总单元格数再翻倍。例如 10 个单元格 × 6 例 × 2 = 120 例（更稳妥可取 10 例/格 × 10 × 2 = 200 例）。
> - **Borg & Gall 子组推算** 若 5% 样本必须是青少年男生且该子组需 30 例，则总样本 = 30 ÷ 0.05 = 600 例。

### 概率样本的表格法

> [!feature] 概率样本量的表格法
> Krejcie & Morgan（1970）提供了从给定总体规模确定[[Random Sampling|随机样本]]量的数学公式表格：
> - 总体 ≤ 30 时，建议将整个总体作为样本。
> - 总体 100 时，需约 80 例（80%）。
> - 总体 1,200 时，需约 291 例（约 24%）。
> - 总体越大，样本所占比例越小，且最终趋于恒定（约 384 例）。

---

## 概念辨析

> [!contrast-table] 类别数据 vs 连续数据的样本量要求
> | 维度 | 类别数据 | 连续数据 |
> |---|---|---|
> | 常用边际误差 | 5% | 3% |
> | 样本量趋势 | 更大 | 相对较小 |
> | 总体 2,000+ 时样本量 | 仍随总体增加 | 不再变化 |
> | [[Multiple Regression\|多元回归]] 5:1 比率 | ≥ 313 例，自[[Variable\|变量]] ≤ 62 | ≥ 111 例，[[Independent Variable\|自变量]] ≤ 22 |
> | 多元回归 10:1 比率 | ≥ 313 例，自变量 ≤ 31 | ≥ 111 例，自变量 ≤ 11 |

---

## 围绕概念形成的命题

### 命题类型一：样本量与代表性的关系（Size–Representativeness）

> [!concept-lens] 大样本不保证代表性，小样本不一定无代表性
> 样本量与代表性之间的关系不是线性的——大样本可能因抽样偏差而缺乏代表性，小样本在特定条件下也能具有代表性。

> [!claim] 大样本不保证代表性
> 班级教师可以访谈 450 名女生，却仍然没有代表男生群体。同样，访谈 2 名学生而其中 1 名（50%）表示喜欢科学，也不代表总体（p.145）。

> [!claim] 过度抽样可能不可行
> 样本太大可能变得难以驾驭；样本太小可能无代表性。但 Borg & Gall（1979: 186）强调应从最小子组的最小案例数出发向上推算，而非反过来（p.146）。

> [!claim] 经验丰富 vs 经验不足的研究者
> 经验丰富的研究者从总体出发向下推导样本；经验不足者常先确定所需最少受访者数量，却不事先识别总体——这使得几乎无法评估样本的代表性（p.143）。

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 系统梳理样本量确定的多重因素、经验法则、统计方法要求和数学公式，涵盖 Krejcie & Morgan（1970）、Bartlett et al.（2001）、Borg & Gall（1979）和 Gorard（2003）等关键来源。
