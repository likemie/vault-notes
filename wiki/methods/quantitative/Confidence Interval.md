---
title: Confidence Interval
aliases:
  - 置信区间
  - confidence level
  - 置信水平
summary: "围绕点估计给出的可能取值范围，由置信水平和边际误差共同定义，既用于抽样设计中的样本量确定，又在研究报告与证据综合中表征估计精度与统计不确定性。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 28
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - confidence-interval
  - standard-error
  - statistical-inference
  - effect-size
  - research-methodology
related_concepts:
  - "[[Sampling Error]]"
  - "[[Null Hypothesis]]"
  - "[[Counterfactual]]"
  - "[[Attrition]]"
  - "[[Effective Sample Size]]"
  - "[[Heterogeneity]]"
  - "[[Visible Learning]]"
  - "[[Statistical Analysis Plan]]"
related_theories: []
related_methods:
  - "[[Sample Size Determination]]"
  - "[[Prediction Interval]]"
  - "[[Statistical Significance]]"
  - "[[Effect Size]]"
  - "[[Standard Error]]"
  - "[[Meta-analysis]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Rasch Measurement]]"
  - "[[Meta-meta-analysis]]"
  - "[[Correlational Research]]"
  - "[[Random Sampling]]"
related_instruments:
  - "[[EEF Padlock Security Rating]]"
related_persons: []
related_facts:
  - "[[Education Endowment Foundation]]"
  - "[[EEF Teaching and Learning Toolkit]]"
  - "[[National Center for Education Evaluation and Regional Assistance]]"
  - "[[PISA]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
  - "[[Argument_Allerup_2015_Paideia]]"
  - "[[Argument_Wecker_2016_ZfE]]"
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
confidence: high
status: draft
created: 2026-05-05
updated: 2026-09-17
---
# Confidence Interval

## 定义

> [!def] 核心定义
> 置信区间（Confidence Interval, CI）是在点估计周围给出的可能取值范围，表示估计值的不确定性程度。95% 置信区间意味着若从同一总体中反复抽样，95% 的样本产生的区间将包含总体真值。CI 同时服务于两个场景：在抽样设计中，它是确定[[Sample Size Determination\|样本量]]的关键参数；在研究报告中，它呈现点估计的精度，帮助读者判断差异是否具有实质意义。

> [!concept-lens] 概念透镜
> - **含义** CI 指向估计值的不确定性范围——点估计是单一数值，CI 给出这个数值可能的波动区间。
> - **用途** 在抽样设计中，CI 帮助确定需要多大的样本才能达到目标精度；在报告中，它让读者看到排名或比较背后的不确定性。
> - **边界** CI 不等于[[Prediction Interval\|预测区间]]；CI 反映的是估计精度而非个体值的散布范围。CI 也不直接等价于显著性检验，尽管区间是否包含零值常被用作显著性判断的替代。

> [!citation-card] 置信区间的变异度表征
> 置信区间是希望确保的变异程度或变异范围。例如民调中 ± 3% 意味着若某党获 52% 选票，实际可能在 49%–55% 之间。常规抽样策略使用 95% 置信水平和 3% 置信区间。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|(Cohen et al., 2011, pp. 147–148)]]
>
> *The confidence interval is that degree of variation or variation range that one wishes to ensure. A conventional sampling strategy will be to use a 95 per cent confidence level and a 3 per cent confidence interval.*

---

## 概念辨析

### 置信水平 vs 置信区间

> [!contrast-table] 置信水平 vs 置信区间
> | 维度 | 置信水平（Confidence Level） | 置信区间（Confidence Interval） |
> |---|---|---|
> | 定义 | 对结果落在给定范围内的确信程度 | 希望确保的变异范围 |
> | 典型取值 | 90%、95%、99% | $\pm 1\%$、$\pm 3\%$、$\pm 5\%$ |
> | 在公式中的角色 | 决定 $Z$ 值（95% → $Z = 1.96$） | 决定 $e$（边际误差） |
> | 对[[Sample Size Determination\|样本量]]的影响 | 越高 → $n$ 越大 | 越小 → $n$ 越大 |
> | 常规策略 | 95% | $\pm 3\%$ |

两者的组合直接进入[[Sample Size Determination|样本量]]公式：$n = (Z \cdot \sigma / e)^2$，其中 $Z$ 由置信水平决定，$e$ 等于置信区间半宽。

### 与相关概念的区别

> [!contrast-table] CI vs 邻近概念
> | 维度 | 置信区间（CI） | [[Statistical Significance\|统计显著性]] | [[Effect Size\|效应量]] | [[Sampling Error\|标准误]] |
> |---|---|---|---|---|
> | 回答的问题 | 真值大概在哪个范围 | 是否拒绝[[Null Hypothesis\|零假设]] | 差异有多大 | 样本估计的变异程度 |
> | 输出形式 | 区间 $[L, U]$ | $p$ 值 | $d$、$r$ 等 | $SE$ 数值 |
> | 关系 | $CI = \text{估计值} \pm Z \times SE$ | $p < 0.05$ 等价于 95% CI 不含零 | CI 说明效应量的不稳定性 | $SE$ 是 CI 的构建材料 |

---

## 核心要素

> [!feature] 核心要素
> - **点估计** 点估计给出一个数值，但不说明估计精度。[[Effect Size\|效应量]]排名若只给 $d$ 值，就无法呈现该估计可能的误差范围。[[Argument_Allerup_2015_Paideia\|Allerup (2015, p. 47)]]
> - **置信水平** 对区间覆盖真值的确信程度。常用 95% 或 99%。95% 意味着若重复抽样 100 次，约 95 个区间会包含总体真值。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|Cohen et al. (2011, Ch. 8, p. 147)]]
> - **边际误差** 区间半宽 $e$，由研究者的精度需求决定。$e$ 越小，CI 越窄，所需[[Sample Size Determination\|样本量]]越大。
> - **[[Standard Error\|标准误]]** CI 的构建材料，$CI = \text{估计值} \pm Z \times SE$。二级[[Meta-analysis\|元分析]]若缺少 $SE$，读者无法自行判断联合效应量估计是否稳定。[[Argument_Wecker_2016_ZfE\|Wecker et al. (2016, p. 29)]]
> - **区间重叠规则** 当两个估计值的 CI 重叠时，仅凭点估计大小不能判断二者有统计显著差异。$d = 0.71$ 与 $d = 0.72$ 这类相邻值本身不足以证明两个干预不同。Allerup
> - **常规策略** 抽样中使用 95% 置信水平和 $\pm 3\%$ 置信区间作为折中方案。Cohen et al.

---

## 围绕概念形成的命题

### CI 在抽样设计中的角色

> [!claim] CI and CL 共同决定[[Sample Size Determination\|样本量]]
> 置信水平越高（99% vs 95%）→ $Z$ 值越大 → 所需 $n$ 越大。置信区间越窄（$\pm 3\%$ vs $\pm 5\%$）→ $e$ 越小 → 所需 $n$ 越大。两者通过 $n = (Z \cdot \sigma / e)^2$ 联合驱动样本量。抽样设计的常规折中是 95% CL + $\pm 3\%$ CI。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|Cohen et al. (2011, Ch. 8, pp. 147–148)]]

> [!claim] 384 天花板的 CI 解释
> Krejcie & Morgan 的 384 例天花板基于 95% CL 和 $\pm 5\%$ CI。将 $e$ 从 $\pm 5\%$ 缩到 $\pm 3\%$，$n$ 从 384 跳至约 1,067——民调追求更严的 CI，因而需要 1,000–1,500 而非 384 的样本量。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|Cohen et al. (2011, Ch. 8, pp. 146–148)]]

### CI 在研究报告中的角色

> [!claim] 没有 CI 的排名不可靠
> 只给点估计的[[Effect Size\|效应量]]表不像带有横向误差范围的排名那样呈现估计精度，因此无法知道 $d = 0.71$ 与 $d = 0.72$ 这类相邻值是否有统计上可区分的差异。在面向实践者的证据工具中，CI 常被省略以换取简洁排名，但这种简洁会把估计精度隐藏起来，使排名看起来比实际更确定。[[Argument_Allerup_2015_Paideia\|Allerup (2015, pp. 47–48)]]

> [!claim] 报告标准要求 CI
> [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]]在二级[[Meta-analysis\|元分析]]方法要求中明确提出，联合效应量应报告[[Standard Error\|标准误]]和 95% CI，并进行显著性检验；缺少这些信息会使排名中的相邻位置无法解释。Hattie 的二级综合通常不进行显著性检验或不给出效应量估计的 CI，对于效应量较小的因素，是否存在效应因此并不清楚。[[Argument_Wecker_2016_ZfE\|Wecker et al. (2016, pp. 29–30)]]

### 证据传播与实践转化中的不确定性呈现困局

> [!claim] 统计不确定性报告与实践可操作性传达的制度张力
> 统计学界日益主张摒弃基于 $p < 0.05$ 任意阈值的机械二分法，转向全面报告点估计与其 95% 置信区间（Wasserstein et al., 2019；Amrhein et al., 2019）。然而，在教育证据向一线实践者转化的传播端，置信区间常被视作认知负荷过重的专业壁垒。以英国[[Education Endowment Foundation\|教育捐赠基金会]]（EEF）为例，尽管其独立试验评估报告和统计分析计划（SAP）强制要求报告效应量估计的 95% CI，但在面向校长的[[EEF Teaching and Learning Toolkit\|教学与学习工具包]]中，干预效应被单维度转换为“额外学习月数”（months of additional progress）。这种将连续区间估计折叠为离散整数的简化策略，虽然提升了证据在时间匮乏的教育决策者中的易读性，却隐蔽了估计精度较宽时的统计不确定性，构成了证据中介机构在“科学严谨性”与“行动易读性”之间的长期制度张力（[[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill, 2021, pp. 57–58]]）。

> [!claim] 试验信息量判断中区间宽度与因果效度维度的争辩
> 对大规模教育现场试验中 CI 宽度的评价存在方法论争议。对英国 EEF 与美国 [[National Center for Education Evaluation and Regional Assistance\|NCEE]] 资助的 141 项大样本 [[Randomised Controlled Trials\|RCT]]（覆盖逾 122 万名学生）的元分析重析显示，许多试验效应量微弱（均值 0.06 SD）且 95% 置信区间过宽（平均宽度达 0.30 SD），因而被部分研究者定性为“无法提供有效信息”（uninformative）（Lortie-Forgues & Inglis, 2019）。但证据治理视角对此提出反驳：仅凭估计精度单项指标判定试验价值过于狭隘，试验的实际价值还取决于[[Counterfactual\|反事实]]构建质量、[[Attrition\|流失]]率控制与偏倚防范；且随着设计经验积累与[[Effective Sample Size\|有效样本量]]（Effective Sample Size）的逐年翻倍提升，大规模现场 RCT 的置信区间精度正稳步改善（[[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill, 2021, pp. 56–57]]）。

---

## 历史沿革

> [!timeline] CI 在方法讨论中的关键节点
> - **2015** — 教育[[Effect Size\|效应量]]排名批评中，[[PISA]] 的区间呈现常被用来对照只列出 $d$ 值的效应量排名：前者显示估计误差，后者难以判断相邻教学干预是否真的不同。[[Argument_Allerup_2015_Paideia\|Allerup (2015, pp. 47–48)]]
> - **2016** — Wecker et al. 在二级[[Meta-analysis\|元分析]]方法要求中明确提出，联合效应量应报告[[Standard Error\|标准误]]和 95% CI 并进行显著性检验。[[Argument_Wecker_2016_ZfE\|Wecker et al. (2016, p. 30)]]
> - **2019** — 统计学界掀起告别[[Statistical Significance\|统计显著性]]、全面报告置信区间的倡议（Wasserstein et al., 2019；Amrhein et al., 2019）；同年度 Lortie-Forgues & Inglis (2019) 针对 141 项英美教育试验置信区间平均达 0.30 SD 展开“试验信息量”争辩。
> - **2021** — Edovald & Nevill 系统梳理英国 [[Education Endowment Foundation\|EEF]] 评估体系，反思底层严谨 CI 报告与顶层工具包单维度转化之间的制度张力，提出兼顾不确定性报告与行动转化价值的证据治理路径。[[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021, pp. 56–58)]]

---

## 实证发现

> [!finding-cards] 关键实证发现
> - **Hattie 排名缺少 CI** Hattie 的二级综合通常不进行显著性检验或不给出[[Effect Size\|效应量]]估计的 CI；对于效应量较小的因素，是否存在效应因此并不清楚。[[Argument_Wecker_2016_ZfE\|Wecker et al. (2016, p. 30)]]
> - **点估计排名的误导性** 只给点估计的效应量表不像带有横向误差范围的排名那样呈现精度，无法判断 $d = 0.71$ 与 $d = 0.72$ 是否有统计可区分差异。[[Argument_Allerup_2015_Paideia\|Allerup (2015, p. 47)]]
> - **SE 缺失使 CI 无法计算** 如果[[Standard Error\|标准误]]本身计算错误或缺失，即使读者想自行判断相邻排名是否显著不同，也缺少必要信息。Wecker et al.
> - **英美大规模现场 [[Randomised Controlled Trials\|RCT]] 的置信区间普遍偏宽** 对英美中介资助的 141 项大规模教育随机对照试验分析显示，干预平均效应量仅为 0.06 SD，而平均 95% 置信区间宽度达 0.30 SD，表明教育试验受学校[[Heterogeneity\|异质性]]与群集效应影响，常面临区间过宽、统计功效不足的现实挑战（Lortie-Forgues & Inglis, 2019；[[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill, 2021, p. 56]]）。

---

## 应用案例

> [!case] [[Visible Learning]]
> Hattie 排名仅列出 $d$ 值，未系统报告各干预的 CI/SE，成为 Allerup and Wecker et al. 方法论批评的共同焦点。缺失 CI 意味着读者无法判断相邻排名的差异是真实效应还是估计噪声。

> [!case] [[Rasch Measurement]] 与 [[PISA]]
> [[PISA]] 等国际评估中的 Rasch 分数排名通常伴随误差区间，能帮助读者避免过度解释相邻排名——这是 CI 在报告实践中的正面案例。[[Argument_Allerup_2015_Paideia\|Allerup (2015, pp. 47–48)]]

> [!case] 抽样设计中的 CI-CL 组合
> 抽样规划中研究者需同时确定置信水平（常用 95%）和置信区间（常用 $\pm 3\%$），两者组合通过 $n = (Z \cdot \sigma / e)^2$ 直接决定所需[[Sample Size Determination\|样本量]]。这是 CI 在研究设计阶段（而非报告阶段）的核心应用。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|Cohen et al. (2011, Ch. 8, pp. 147–148)]]

> [!case] 英国 [[Education Endowment Foundation\|EEF]] 证据工具包的不确定性表征争议：置信区间 vs 额外学习月数
> 英国[[Education Endowment Foundation\|教育捐赠基金会]]在研究报告与公众传播中采取了分轨呈现机制：底层独立技术报告与[[Statistical Analysis Plan\|统计分析计划]]（SAP）中强制要求逐项报告点估计与 95% 置信区间；而在面向学校管理者的前端[[EEF Teaching and Learning Toolkit\|教学与学习工具包]]中，干预效应被转换为直观的“额外学习月数”（如 +3 个月）。针对单一月数指标掩盖置信区间不确定性的方法性质疑，EEF 增设了由独立方法专家评定的[[EEF Padlock Security Rating\|挂锁安全评级]]（Padlock Rating, 1–5 把锁），以综合视觉图标传达[[Attrition\|样本流失]]、统计功效与设计严谨度带来的不确定性风险，在置信区间的专业度与实践决策的可读性之间形成制度折中（[[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill, 2021, pp. 56–58]]）。

---

## 相关方法与工具

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Meta-analysis]] | 方法 | 元分析中平均[[Effect Size\|效应量]]需伴随[[Standard Error\|标准误]]或置信区间才能说明估计精度。 |
> | [[Meta-meta-analysis]] | 方法 | 联合 SE 与 CI 是二级元分析报告联合效应量时的必要信息。[[Argument_Wecker_2016_ZfE\|Wecker et al. (2016, p. 30)]] |
> | [[Sample Size Determination]] | 概念 | CI 与置信水平是确定概率样本量的两个核心参数。 |
> | [[Randomised Controlled Trials]] | 方法 | 随机对照试验中干预效应量必须依托置信区间报告，以展示[[Sampling Error\|抽样误差]]与聚类效应引起的不确定性。 |
> | [[EEF Padlock Security Rating]] | 工具 | 在证据中介传播中充当置信区间的直观补充指标，以综合评级表征研究效度与不确定性。[[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021, p. 57)]] |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research\|相关研究]]索引
> - [[Argument_Allerup_2015_Paideia\|Allerup (2015)]] — 借助置信区间分析批判点估计排名的统计虚假精确性。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|Cohen et al. (2011)]] — 系统阐释置信区间与置信水平在[[Random Sampling\|概率抽样]][[Sample Size Determination\|样本量]]计算中的数理逻辑。
> - [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]] — 在[[Meta-meta-analysis\|二级元分析]]规范中要求报告联合[[Effect Size\|效应量]]的[[Standard Error\|标准误]]与 95% 置信区间。
> - [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]] — 探讨大规模教育现场试验中置信区间宽度争议，反思证据中介在统计不确定性与实践易读性之间的治理张力。
