---
title: Statistical Significance
aliases:
  - 统计显著性
summary: "用于判断观察到的差异是否足以拒绝零假设的统计判断标准，其解释需要结合样本量、效应大小和研究设计。"
type: concept
domain: "research-methodology"
related_count: 24
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
- statistical-significance
- p-value
- hypothesis-testing
- effect-size
- research-methodology
related_concepts:
  - "[[Null Hypothesis]]"
  - "[[Hypothesis]]"
  - "[[Praxis]]"
  - "[[Threats to Internal Validity]]"
  - "[[Sample Size Determination]]"
  - "[[Effect Size]]"
  - "[[Confidence Interval]]"
  - "[[Standard Error]]"
  - "[[Evaluation Research]]"
  - "[[Internal Validity]]"
  - "[[Educational Evidence Clearinghouses]]"
  - "[[Publication Bias]]"
  - "[[Visible Learning]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Quasi-Experimental Designs]]"
related_persons: []
related_facts:
  - "[[ESSA 2015 Evidence Standards]]"
related_arguments:
  - "[[Argument_Allerup_2015_Paideia]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
  - "[[Argument_Terhart_2011_JCS]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Ross_Morrison_2021_ROE]]"
  - "[[Argument_Wecker_2016_ZfE]]"
confidence: low
status: draft
created: '2026-05-05'
updated: 2026-07-15
---

## 定义

> [!def] 核心定义
> 统计显著性（Statistical Significance）用于判断观察到的差异是否足以拒绝"两个总体均值相同"之类的[[Null Hypothesis|零假设]]。统计检验的核心不是把差异评为"大"或"小"，而是判断检验统计量是否超过临界值；超过则认为差异具有统计显著性，否则不能排除零[[Hypothesis|假设]]仍然成立的可能（[[Argument_Allerup_2015_Paideia|Allerup, 2015, p.45]]）。

> [!concept-lens] 概念透镜
> - **含义** 统计显著性回答"观察到的差异是否可能仅由随机因素造成"，而非"差异有多大"或"差异是否重要"。
> - **用途** 为研究者在[[Null Hypothesis|零假设]]框架下提供可否拒绝零假设的标准化判断依据，是假设检验的核心决策工具。
> - **边界** 统计显著性不说明效应大小、[[Praxis|实践]]意义或政策价值。它只是众多[[Threats to Internal Validity|内部效度威胁]]中的一个，而非研究价值的最终裁判。

> [!boundary] 概念边界
> - **不等于效应大小** 统计显著性受[[Sample Size Determination|样本量]]驱动——大样本可使微小效应显著，小样本可使大效应不显著。详见 [[Effect Size]]。
> - **不等于实践重要性** 显著结果可能对应微不足道的实际差异，非显著结果可能对应有实践价值的效应。
> - **不替代[[Confidence Interval|置信区间]]** 仅报告 p 值而不报告[[Confidence Interval|置信区间]]或[[Standard Error|标准误]]，无法判断估计的稳定性。

### 与效应量的数学关系

Fitz-Gibbon（1985）在[[Meta-analysis|元分析]]发展早期即主张以效应量替代统计显著性作为[[Evaluation Research|评估研究]]的主要指标，将统计显著性重新定位为"[[Internal Validity|内部效度]]众多可能威胁中的一个"（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, pp.339–340]]）。

> [!formula-step] 统计显著性与效应量的数学关系
> $$t = d\sqrt{n}$$
>
> **读法** 其中 $d$ 为标准化均值差（[[Effect Size|效应量]]），$n$ 为观测数。样本量越大，同样 $d$ 值对应的 $t$ 值越大，越容易达到统计显著。
>
> **示例** 以 $n = 25$ 为例，$d \approx 0.412$ 对应 $t = 2.060$，接近双侧检验 $p \approx 0.05$ 的临界值。这意味着 Hattie 的 $d = 0.40$ 关节点在特定样本量下恰好与 $p \approx 0.05$ 相连，并非脱离样本量的普遍边界（[[Argument_Allerup_2015_Paideia|Allerup, 2015, p.45]]）。

---

## 历史沿革

> [!dev-timeline] 统计显著性的概念演变
> - **2011 — Terhart 的区分** Terhart 在解释 Hattie 的 [[Effect Size|效应量]]时区分了统计显著性和效应大小：统计显著性只说明结果不太可能由随机因素造成，却不说明效应有多大或[[Praxis|实践]]意义是什么（[[Argument_Terhart_2011_JCS|Terhart, 2011, p.427]]）。
> - **2015 — Allerup 的数学联系** 效应量与显著性检验在给定[[Sample Size Determination|样本量]]时可通过 $t = d\sqrt{n}$ 建立数学联系（[[Argument_Allerup_2015_Paideia|Allerup, 2015, p.45]]）。
> - **2024 — 清算中心标准分化** Wadhwa et al. 发现不同[[Educational Evidence Clearinghouses|教育证据清算中心]]对统计显著性和效应量阈值的要求不一致：有的要求统计显著正向效果，有的还额外要求最低效应量（[[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, pp.12–15]]）。

---

## 核心要素

> [!feature] 核心要素
> - **[[Null Hypothesis|零假设]]** 在两个分布均值比较中，零[[Hypothesis|假设]]写作 $H_0: \mu_1 = \mu_2$（[[Argument_Allerup_2015_Paideia|Allerup, 2015, p.45]]）。
> - **t 值与[[Sample Size Determination|样本量]]** 在[[Effect Size|效应量]] $d$ 已知时，若观测数为 $n$，可构造 $t = d\sqrt{n}$；样本量越大，同样 $d$ 值越容易达到统计显著。
> - **p 值** p 值表示在零假设成立时获得当前或更极端 $t$ 值的概率，是统计分析结果的核心呈现形式。
> - **显著不等于重要** Terhart 强调统计显著性不说明效应大小和[[Praxis|实践]]意义，需[[Effect Size|效应量]]或原始量表差异补充（[[Argument_Terhart_2011_JCS|Terhart, 2011, p.427]]）。
> - **显著不等于可采购** 学校项目选择中，统计显著性不能说明项目成本、实施难度、教师接受度或本地适配性（[[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021, pp.120-121]]）。

---

## 与相关概念的区别

> [!contrast-table] 与相关概念的区别
> - **vs [[Effect Size]]** 统计显著性回答"差异是否足以排除随机波动"，效应量回答"差异有多大"。二者可通过 $t = d\sqrt{n}$ 在特定[[Sample Size Determination|样本量]]下关联，但不能相互替代（[[Argument_Allerup_2015_Paideia|Allerup, 2015, p.45]]）。
> - **vs [[Confidence Interval]]** 统计显著性以是否越过临界值或 p 值阈值呈现；置信区间把估计值的误差范围显示出来，使读者能判断相邻估计是否可能重叠（[[Argument_Allerup_2015_Paideia|Allerup, 2015, pp.47–48]]）。

## 相关方法

> [!info] 相关方法
> - [[Meta-analysis]] — 元分析若只合并点估计而忽略显著性检验和[[Confidence Interval|置信区间]]，容易把不同精度的研究结果放在同一层级比较。
> - [[Meta-meta-analysis]] — 联合[[Standard Error|标准误]]、95% CI 和显著性检验是判断二级综合点估计是否稳定的必要信息（[[Argument_Wecker_2016_ZfE|Wecker et al., 2016, p.30]]）。

---

## 实证发现

> [!success] 实证发现
> - 在 $n = 25$ 的示例中，$d \approx 0.412$ 对应 $t = 2.060$，接近双侧检验 $p \approx 0.05$ 的临界值；换成其他[[Sample Size Determination|样本量]]，这一对应关系会改变（[[Argument_Allerup_2015_Paideia|Allerup, 2015, p.45]]）。
> - 在[[Educational Evidence Clearinghouses|教育证据清算中心]]中，统计显著性并不总是以同样方式进入评级标准；部分机构要求统计显著正向效果，部分机构还加入最低[[Effect Size|效应量]]门槛（[[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, pp.12–15]]）。
> - 在 141 项大型教育 [[Randomised Controlled Trials|RCT]] 中，只有 23% 的成就效应显著大于零；这提示”严格设计”并不自动带来统计显著的教育成就效果（[[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021, p.112]]）。

---

## 争议与批评

> [!warning] 争议与批评
> - 如果只报告统计显著性，研究者可能忽略实际效应大小；如果只报告[[Effect Size|效应量]]点估计，则无法判断该估计是否稳定。只有 $d$ 值而缺少 [[Confidence Interval]]、[[Standard Error|标准误]]或相邻排名显著性检验时，读者无法判断数值接近的干预是否真的不同（[[Argument_Allerup_2015_Paideia|Allerup, 2015, pp.47–48]]）。
> - [[Publication Bias|发表偏倚]]与统计显著性偏好相关：发表系统更容易接纳显著或正面结果，从而使[[Meta-analysis|元分析]]平均效应量偏高。
> - 现行证据标准容易把中等或强”有效性”缩小为严格实验中的统计显著效果，忽略实施质量、结果类型和地方上重视的非成就目标（[[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021, pp.110-112]]）。

---

## 应用案例

> [!evidence-grid-a] 相关案例索引
> - [[Educational Evidence Clearinghouses]] — 清算中心把统计显著性、效应方向和最低[[Effect Size|效应量]]阈值组合成项目评级规则（[[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, pp.12–15]]）
> - [[ESSA 2015 Evidence Standards]] — ESSA 证据层级把 [[Randomised Controlled Trials|RCT]]、[[Quasi-Experimental Designs|QED]] 和相关研究与项目有效性标准连接起来（[[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021, p.109]]）
> - [[Visible Learning]] — Hattie 将 $d = 0.40$ 作为[[Praxis|实践]]阈值，但该值与显著性的关系依赖[[Sample Size Determination|样本量]]（[[Argument_Allerup_2015_Paideia|Allerup, 2015, p.45]]）

