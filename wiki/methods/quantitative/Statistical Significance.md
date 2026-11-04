---
title: Statistical Significance
aliases:
  - 统计显著性
  - 显著性检验
  - p-value
summary: "推断统计中用于判定样本观察差异是否足以拒绝零假设的数理判定规则；通过计算在零假设为真前提下获得当前或更极端统计量的概率（p 值）并与预设显著性水平对比，但显著性本身不直接度量效应大小或实践价值。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 0
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - statistics/hypothesis-testing
  - statistics/inference
  - field/research-methodology
confidence: high
status: active
created: '2026-05-05'
updated: 2026-11-05
---

---

> [!def] Statistical Significance
> **统计显著性（Statistical Significance）** 是推断统计与假设检验中用于判定经验观察差异是否足以拒绝[[Null Hypothesis|零假设]]的数理决策规则。其核心机制在于计算检验统计量（如 $t$ 值、$F$ 值、$\chi^2$ 值）在零假设分布下出现的条件概率（$p$ 值）；当该概率低于研究者预设的显著性水平 $\alpha$（通常设定为 0.05 或 0.01）时，表明观察到的样本差异难以归因于纯粹的随机抽样波动，从而判定该差异具有统计显著性（[[Argument_Allerup_2015_Paideia|Allerup, 2015, p. 45]]）。

> [!method-scope] 方法范围
> - **测量或估计对象** 检验处理组与对照组均值差异、回归模型系数或变量间相关性偏离随机预期的统计置信度。
> - **问题类型** 假设检验与推断统计决策（回答“观察到的样本变异是否仅仅是由随机抽样误差引起的”）。
> - **分析单位** 统计样本集合、经验估计参数及其抽样分布。
> - **输出形式** 检验统计量（$t$、$F$、$z$）、显著性概率值（$p$ 值）以及显著性标记（如 $p < 0.05$、$p < 0.01$）。

> [!citation-card] 关键定义
> 统计检验的核心在于确定检验统计量是否超过临界值。超过预设临界值时即可判定差异达到统计显著，能够拒绝两个总体均值相等的零假设；反之则表明样本数据不足以排除零假设成立的可能性。[[Argument_Allerup_2015_Paideia|(Allerup, 2015, p. 45)]]
>
> *Statistical significance tests determine whether the observed difference exceeds the critical value required to reject the null hypothesis of equal population means... failing to reject means the data are consistent with chance variation.*

---

> [!method-position] 认识论与方法定位
> - **知识观** 建立在频率主义抽样理论与反证逻辑之上，通过控制假阳性推断风险（I 型错误 $\alpha$）评估经验证据的稳健度。
> - **研究者角色** 研究者需在检验前客观选定适宜的单双侧假设、检验水平 $\alpha$ 及统计模型，防范事后 $p$ 值操纵（p-hacking）。
> - **有效性标准** 内部效度取决于统计模型对随机抽样误差的严密控制；统计结论效度需结合[[Standard Error|标准误]]与[[Confidence Interval|置信区间]]共同检验。
> - **不声称回答的问题** 统计显著性不度量效应大小（Effect Size），亦不说明干预措施在教育现实中的实践意义或政策效益。

> [!method-stack] 方法层级
> - **上位方法** [[Quantitative Research|量化实证研究]]、推断统计学（Inferential Statistics）。
> - **前置步骤** 确立理论假设、设立[[Null Hypothesis|零假设]]（$H_0$）与备择假设（$H_1$）、采集数据并清洗。
> - **实现模型** 双样本 $t$ 检验、方差分析（ANOVA）、卡方检验、线性与非线性回归显著性检验。
> - **互补指标** [[Effect Size|效应量]]（Cohen's $d$、Hedges' $g$）、95% [[Confidence Interval|置信区间]]、统计检力分析。

---

> [!proc] 通用程序
> 1. **设立检验假设与显著性水平** 确立研究假设并形式化设定 $H_0$（如 $\mu_1 - \mu_2 = 0$），确定可接受的 I 型错误率 $\alpha$。
> 2. **计算估计值及其标准误** 依据样本数据计算点估计值及其抽样标准误 $SE$。
> 3. **推导统计量与 p 值** 构造检验统计量并依据理论抽样分布推导其双尾或单尾 $p$ 值。
> 4. **统计决策与审慎解释** 比对 $p$ 值与 $\alpha$ 阈值，结合效应量与置信区间共同解读研究结果的实践价值。

---

> [!formula-step] 步骤一　检验统计量与样本量的数学关联
> $$t = \frac{\bar{X}_1 - \bar{X}_2}{SE} = d\sqrt{n}$$
>
> **这个公式在做什么** 揭示统计显著性检验量（如独立样本 $t$ 值）与标准化均值差[[Effect Size|效应量]] $d$ 及样本容量 $n$ 之间的代数关系。[[Argument_Allerup_2015_Paideia|(Allerup, 2015, p. 45)]]
>
> **符号说明** $d$ 为标准化效应量；$n$ 为各组样本容量；$SE$ 为差值的标准误。
>
> **数学直觉** 统计检验量由效应量与样本规模共同决定。在效应量固定时，样本容量越大，$t$ 检验量越大，越容易达到拒绝零假设的显著性门槛。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 临界值判断 | 当 $n = 25$ 时，$d \approx 0.412$ 对应 $t = 2.060$，恰好对应双侧检验 $p \approx 0.05$ 门槛。 |
> > | 注意 | 样本规模依存 | 相同的效应量在不同样本量下展现完全不同的统计显著性，显著性水平高度取决于样本规模的大小。 |

---

> [!method-fit] 适用判断
> - **适合使用** 评估随机对照试验或观察性研究中样本差异是否显著超出随机误差波动的参数假设检验。[[Argument_Allerup_2015_Paideia|(Allerup, 2015, p. 45)]]
> - **谨慎使用** 巨型大数据集分析（样本量极大时极微小的琐碎差异亦会产生极高显著性），需严格以效应量为主要研判依据。
> - **不适合使用** 探索性质性研究、无概率抽样的非代表性个案研究，或缺乏方差控制的单项描述性统计。

---

> [!method-limits] 方法局限
> - **显著不等于重要（Significance vs. Importance）** 统计显著性仅表明样本差异难以用抽样误差解释，绝不代表该差异具备实质教育效益或政策采纳价值。[[Argument_Terhart_2011_JCS|(Terhart, 2011, p. 427)]]
> - **二元标签诱发发表偏倚** 将连续的 $p$ 值粗暴划分为显著（$p < 0.05$）与不显著的二元标签，容易诱发选择性发表与数据挖掘偏误。
> - **忽略估计不确定性** 孤立报告 $p$ 值而省略置信区间与标准误，会导致读者无法评估估计值的精确度与相邻干预的重叠可能。[[Argument_Allerup_2015_Paideia|(Allerup, 2015, pp. 47–48)]]

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Null Hypothesis]] | 概念 | 统计显著性检验所设定并尝试予以拒绝的核心基准命题。 |
> | [[Effect Size]] | 方法 | 衡量差异实际大小的互补指标，弥补统计显著性受制于样本量的缺陷。 |
> | [[Standard Error]] | 方法 | 计算检验统计量分母所必需的核心抽样离散度指标。 |
> | [[Confidence Interval]] | 方法 | 反映参数估计精确范围的互补展示形式，优于单一显著性判定。 |
> | [[Sample Size Determination]] | 方法 | 决定统计检验功效（Power）与显著性检出能力的前置设计步骤。 |
> | [[Meta-analysis]] | 方法 | 综合多项初级研究检验结果并控制发表偏倚的宏观证据整合方法。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Allerup_2015_Paideia|Allerup (2015)]] — 推导显著性检验量与效应量在给定样本量下的代数关联，指出显著性受制于样本规模的数学机制。
> - [[Argument_Terhart_2011_JCS|Terhart (2011)]] — 强调统计显著性仅说明结果不属于随机噪音，不能直接等同于教育实践的重要程度。
> - [[Argument_Ross_Morrison_2021_ECNUROE|Ross and Morrison (2021)]] — 分析 141 项大型教育 RCT 发现仅 23% 达到统计显著，反思严格证据标准对项目采纳的过度约束。
