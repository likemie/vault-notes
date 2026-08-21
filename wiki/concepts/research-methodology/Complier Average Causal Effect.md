---
title: Complier Average Causal Effect
aliases:
  - 顺从者平均因果效应
  - 依从者平均因果效应
  - CACE
  - Local Average Treatment Effect in RCTs
  - 依从者效应
summary: "在存在不完全依从（Non-compliance）的实验中，通过工具变量法估计真正接受干预的顺从者群体因果净效应的计量方法，与评估政策推广效能的意向治疗分析（ITT）构成互补。"
type: concept
domain: "research-methodology"
related_count: 21
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - subject/research-methodology
  - causal-inference
  - econometrics
  - compliance
  - instrumental-variable
related_concepts:
  - "[[Causality]]"
  - "[[Counterfactual]]"
  - "[[Internal Validity]]"
  - "[[External Validity]]"
  - "[[Construct Validity]]"
  - "[[Effect Size]]"
  - "[[Educational Evidence Clearinghouses]]"
  - "[[Attrition]]"
  - "[[Statistical Significance]]"
  - "[[Variable]]"
related_theories:
  - "[[Campbellian Validity Framework]]"
related_methods:
  - "[[Randomised Controlled Trials]]"
  - "[[Intent-to-Treat Analysis]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Regression Discontinuity Design]]"
  - "[[Cluster Randomized Trials]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[What Works Clearinghouse]]"
  - "[[Social Programs That Work]]"
  - "[[Blueprints for Healthy Youth Development]]"
related_arguments:
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
confidence: high
status: active
created: 2026-08-22
updated: 2026-08-22
---

# Complier Average Causal Effect

---

## 定义

> [!def] 概念定义
> **顺从者平均因果效应（Complier Average Causal Effect, CACE）**，亦称**依从者平均因果效应**，是由统计学家 Donald B. Rubin 与经济学家 Joshua Angrist、Guido Imbens 于 1996 年形式化建立的现代因果推断核心概念，是指在存在**不完全依从（Non-compliance / Treatment Non-adherence）**的随机实验中，干预措施对那些“若被分配至干预组就会实际接受干预、若被分配至对照组就会实际接受对照”的**顺从者群体（Compliers）**所产生的平均因果净效应([[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, p. 10]])。
>
> 在现代因果计量框架中，CACE 与[[Intent-to-Treat Analysis|意向治疗分析（ITT）]]构成了因果推断的两大支柱：ITT 评估的是“干预机会的分配政策效应（Effect of Assignment）”，而 CACE 借助初始随机分配作为[[Variable|工具变量]]（Instrumental Variable, IV），在排除性约束（Exclusion Restriction）下准确剥离了中途违约与逃避行为，估计出干预措施本身的“纯净生理/教学效能（Pure Treatment Efficacy）”([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, pp. 333–334]])。

> [!concept-lens] 效度视角与方法学定位
> - **效度张力化解** 真实教育现场中学生常有缺勤或拒绝参与现象。若直接对比实际接受者与未接受者（As-Treated 分析），会引入严重的选择偏差（破坏内部效度）；若仅看 ITT，效应量会被大量未依从者稀释。CACE 在不破坏随机化基础的前提下精确识别出干预的真实效能。
> - **四类潜在子群体的划分** Rubin 因果模型将受试总体严格划分为四类互斥子群：**顺从者（Compliers）**、**始终接受者（Always-Takers）**、**从不接受者（Never-Takers）**与**对抗违约者（Defiers）**。
> - **清算体系中的哲学分歧** 公共卫生类机构（如 [[Blueprints for Healthy Youth Development|Blueprints]]、[[Social Programs That Work|SPTW]]）坚持必须报告 ITT 以评估现实政策推广价值；而 [[What Works Clearinghouse|WWC]] 允许在满足排除性约束时报告 CACE 估计值。

> [!citation-card]- 关键定义
> 意向治疗分析（ITT）回答的是政策制定者的问题：‘提供这一项目能带来什么改变？’而顺从者平均因果效应（CACE）回答的是学习者和教师的问题：‘如果我真正按要求完整参与了这一项目，它能为我带来多大成效？’两者在因果推断中不可偏废。[[Argument_Wadhwa_2024_RER|(Wadhwa et al., 2024, p. 10)]]
>
> *Complier Average Causal Effect (CACE) identifies the causal effect of an intervention specifically for the subgroup of participants who comply with their assigned treatment status. Using randomized assignment as an instrumental variable, CACE bridges the gap between policy intent and actual intervention efficacy.*

---

## 核心机制与数理模型

> [!mechanism] 四大潜在顺从行为子群
> 在双盲或单侧依从实验中，基于分配状态 $Z \in \{0, 1\}$ 与实际接受状态 $D \in \{0, 1\}$，总体被分解为：
> 1. **顺从者（Compliers）** $D(1)=1$ 且 $D(0)=0$；分配到干预组就参与、分配到对照组就不参与（因果效应可识别的核心主体）。
> 2. **从不接受者（Never-Takers）** $D(1)=0$ 且 $D(0)=0$；无论分到哪组都绝不参与干预（如报了名但一节课都不上的学生）。
> 3. **始终接受者（Always-Takers）** $D(1)=1$ 且 $D(0)=1$；无论分到哪组都会设法获取干预（如对照组学生私下购买实验教材自学）。
> 4. **对抗者（Defiers）** $D(1)=0$ 且 $D(0)=1$；分配到干预组反而故意不参加、分配到对照组反而设法参加。现代因果推断通常引入**单调性假设（Monotonicity / No-Defiers Assumption）**排除此类群体。

---

### 工具变量法与局部瓦尔德估计

> [!formula-step] CACE 局部平均处理效应计算公式
> 在满足**独立性假设**、**排除性约束**与**单调性假设**的前提下，CACE 的两阶段最小二乘（2SLS）/ 瓦尔德估计量表达为：
>
> $$\text{CACE} = \frac{\text{ITT}_Y}{\text{ITT}_D} = \frac{E[Y \mid Z=1] - E[Y \mid Z=0]}{E[D \mid Z=1] - E[D \mid Z=0]} = \frac{\text{分配状态对结果的意向效应}}{\text{分配状态对实际参与的顺从率}}$$
>
> - **$\text{ITT}_Y$** 意向治疗效应（Intention-to-Treat Effect on Outcome）；
> - **$\text{ITT}_D = P(\text{Complier})$** 顺从者在总样本中所占的比例（参与率差值）；
> - **因果缩放机理** 若某课后辅导项目的 ITT 效应量为 $+0.15\text{ SD}$，但实际只有 50% 的学生真正按时出勤（顺从率 $\text{ITT}_D = 0.50$），则干预对真正顺从者的真实成效为：
>   $$\text{CACE} = \frac{+0.15}{0.50} = \mathbf{+0.30\text{ SD}}$$
> - **排除性约束（Exclusion Restriction）** 假定随机分组 $Z$ 仅通过影响实际参与状态 $D$ 进而影响结果 $Y$，分组本身不产生直接心理影响（如未因知道自己被分入对照组而产生挫败感）。

---

### 循证清算中心对 ITT 与 CACE 的审查分歧

> [!contrast-table] 循证清算中心对依从性偏差的处理哲学（基于 Wadhwa et al., 2024）
> | 评价机构 | 核心审查倾向 | 允许的估计量与门槛要求 | 政策与实践取向 |
> |:---|:---|:---|:---|
> | **[[What Works Clearinghouse\|WWC]] (联邦官方)** | **兼顾政策与纯效能** | 优先审查 ITT；在严格满足工具变量排除性约束且第一阶段 $F > 10$ 时，**完全认可 CACE 估计值**并据此评级。 | 既关注政策推广净值，也重视对干预纯教学功效的度量。 |
> | **[[Blueprints for Healthy Youth Development\|Blueprints]]** | **严格公共卫生 ITT** | **强制要求 ITT**；拒绝单独采信去除不依从者后的 CACE 或 Per-Protocol 估计作为最高认证依据。 | 防范由于自选择依从性导致的虚假疗效夸大，确保现实可推广性。 |
> | **[[Social Programs That Work\|SPTW]]** | **保守因果推断** | 仅认可基于全体初始分配样本的 ITT 结果，严防依从性分析中的潜变量偏倚。 | 避免财政资金资助仅在极少数高度自律学生中起效的脆弱项目。 |

---

## 概念边界与常见误区

> [!boundary] 概念辨析与适用边界
> - **CACE vs 完工者分析（Per-Protocol / As-Treated）** 完工者分析简单粗暴地剔除违约者，直接对比实际完成者与对照组，彻底破坏了随机化平衡（引入严重选择偏倚）；CACE 运用工具变量模型，利用外生随机分配 $Z$ 作为杠杆，因果推断具有严密的无偏数学保证。
> - **CACE vs ATE（总体平均处理效应）** ATE 代表若强制全员 100% 接受干预时的理论总体平均值；CACE 仅代表自然状态下愿意顺从该干预的子群体效应（若干预强制推广至从不接受者，效应可能大幅下降）。
> - **排除性约束失效风险** 若实验组学生得知自己入组后产生了强烈的期望效应（心理安慰剂），即使未实际使用干预也提高了成绩，此时工具变量排除性假设被击穿，CACE 估计将产生系统偏误。

---

## 典型应用与反思案例

> [!case] 特许学校抽签入学与 CACE 估计（Angrist et al., 2002）
> 某城市优质特许学校提供 200 个入学名额，400 名申请者参与随机摇号：
> - **分配与顺从** 200 名中签者中，160 人实际报到入学（顺从），40 人因搬家放弃（Never-Takers）；200 名未中签者中，全部入读普通公立校（无 Defiers，顺从率 $\text{ITT}_D = 80\%$）。
> - **效应计算** 中签对全体申请者的 ITT 提分效应为 $+0.24\text{ SD}$；运用 CACE 计算特许学校对真正入读学生的净增益为 $\text{CACE} = +0.24 / 0.80 = \mathbf{+0.30\text{ SD}}$。

---

## 相关概念与方法网络

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Intent-to-Treat Analysis]] | 孪生方法 | 因果推断的两大基石：ITT 关注分配意向，CACE 关注顺从者净效能。 |
> | [[Randomised Controlled Trials]] | 实验母方法 | CACE 专门用于解决 RCT 现场实施中的不完全依从与中途脱落难题。 |
> | [[Regression Discontinuity Design]] | 关联方法 | 模糊断点回归（Fuzzy RDD）在数理本质上就是局域维度的 CACE 估计。 |
> | [[Attrition]] | 关联概念 | 受试脱落是不完全依从的一种极端形态，CACE 提供部分流失纠偏手段。 |
> | [[Campbellian Validity Framework]] | 理论基础 | 解释构念效度（理论效能）与统计结论效度（估计无偏性）的桥梁。 |
