---
title: Stratified Sampling
aliases:
  - 分层抽样
  - stratified random sampling
  - 随机分层抽样
  - stratified sample
summary: "概率抽样方法，将总体按关键特征划分为互斥且同质的层，并在各层内独立随机抽样，确保样本在各关键维度上的比例结构与总体保持一致，提升参数估计精度并保障亚群代表性。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 28
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/sampling
  - quantitative-research
related_concepts:
  - "[[Socioeconomic Status]]"
  - "[[Variable]]"
  - "[[Study Population and Sample]]"
  - "[[Sampling Error]]"
  - "[[Heterogeneity]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Positivism]]"
  - "[[Causality]]"
  - "[[Evaluation Research]]"
  - "[[Research Question]]"
  - "[[Construct]]"
  - "[[Response Bias]]"
related_theories: []
related_methods:
  - "[[Random Sampling]]"
  - "[[Effect Size]]"
  - "[[Standard Error]]"
  - "[[Cross-sectional Study]]"
  - "[[Cohort Study]]"
  - "[[Sampling Frame]]"
  - "[[Sample Size Determination]]"
  - "[[Systematic Sampling]]"
  - "[[Cluster Sampling]]"
  - "[[Random Assignment]]"
  - "[[Experimental Research]]"
  - "[[Survey Research]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
  - "[[Argument_Hogan_2013_ROE]]"
  - "[[Argument_Nordtveit_2011_IJED]]"
confidence: high
status: active
created: 2026-06-22
updated: 2026-11-19
---

---

> [!def] Stratified Sampling
> 随机分层抽样（Stratified [[Random Sampling]]）是将研究总体依据预先设定的关键特征（如学校类型、学业分流轨道、[[Socioeconomic Status|社会经济地位]]）划分为互斥且同质的子总体（层，strata），随后在各个层内分别独立执行[[Random Sampling|简单随机抽样]]的概率抽样方法。该方法确保样本在核心分层[[Variable|变量]]上的分布比例与[[Study Population and Sample|目标总体]]保持精确对应，有效减少[[Sampling Error|抽样误差]]并保障关键亚组在统计推断中的充分代表性。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, pp. 145–146)]]

> [!method-scope] 方法范围
> - **研究对象** 具备已知关键分层特征（如学校办学层次、学生学段分流、地区与[[Socioeconomic Status|社会经济地位]]）的大规模调查总体。
> - **问题类型** 需要在保证总体代表性的同时开展亚组比较、控制群际[[Heterogeneity|异质性]]、或估计关键群体均值与[[Effect Size|效应量]]分布的量化实证研究。
> - **[[Unit of Analysis|分析单位]]** 个体受访者、班级或机构单元（依分层变量界定）。
> - **输出形式** 按各层比例或最优配置抽取的代表性概率样本数据集及其加权权重。

> [!citation-card] 分层抽样的代表性保障
> 分层抽样通过将总体划分为同质的子群体，并在每一层内独立进行随机抽样，克服了纯粹简单随机抽样可能遗漏少数群体的风险，确保了样本对总体结构特征的精确再现。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, p. 145)]]
>
> *Stratified sampling involves dividing the population into homogeneous groups, each group containing subjects with similar characteristics. A sample is then drawn from each group, ensuring that the sample accurately reflects the population structure.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** [[Positivism|实证主义]]与概率论取向；将研究总体理解为由结构性特征分化的多群异质网络，通过分类控制内部方差，可以以最小方差估计总体真实参数。
> - **研究者角色** 抽样设计者；需在抽样前基于先验理论与普查统计信息合理选择分层变量，权衡等比例配置与非等比例最优配置。
> - **有效性标准** 样本对总体的结构代表性、分层估计量的[[Standard Error|标准误]]缩减程度（设计效应 Deff）以及统计结论效度。
> - **不声称回答的问题** 不能通过横截面抽样设计直接确立变量间的时序[[Causality|因果关系]]；当分层变量与研究结果无关时，分层抽样不会自动提高估计精度。

> [!method-stack] 方法层级
> - **研究设计** 大规模[[Cross-sectional Study|横截面调查]]研究、教育纵向追踪[[Cohort Study|队列研究]]、[[Evaluation Research|评估研究]]。
> - **抽样分类** 等比例分层抽样（Proportional Stratified Sampling）、非等比例最优化分层抽样（Disproportional / Optimal Stratified Sampling）。
> - **辅助技术** [[Sampling Frame|抽样框]]清理、层内随机数生成、设计效应校正、事后分层加权（Post-stratification Weighting）。

---

> [!proc] 通用程序
> 1. **明确目标总体与分层变量** 依据[[Research Question|研究问题]]与先验人口普查或行政数据，选定 1–3 个与研究核心变量高度相关的外生分类特征作为分层变量。
> 2. **划分互斥同质层** 将总体成员无遗漏且无交叉地分配至各个离散层中，确保层内方差尽可能小、层间方差尽可能大。
> 3. **计算各层[[Sample Size Determination|样本量]]配额** 依据等比例配置原则（各层样本量与总体层容量成正比）或最优配置原则（考虑层内方差与抽样成本）分配样本量。
> 4. **层内独立随机抽样** 在各层内分别运用简单随机抽样或[[Systematic Sampling|系统抽样]]抽取目标样本，合成全样本数据集。
> 5. **样本代表性评估与加权调整** 检验样本分层比例与总体参数的一致性，在需要时计算并施加抽样权重。

> [!method-stack] 数据与变量
> - **数据结构** 嵌套或分层的多源观察数据。
> - **样本与单位** 抽样框名单、总体容量 $N$、总样本量 $n$、各层容量 $N_h$ 与层样本量 $n_h$。
> - **变量或测量** 分层指标（名义或等级变量）、调查核心观测变量与潜变量[[Construct|构念]]。

---

> [!method-fit] 适用判断
> - **适合使用** 目标总体的关键背景特征已知且存在显著群际差异（如不同办学层次学校、不同学术分流轨道、城乡地域差异）；需要在同一研究中兼顾全域推论与特定子群体深度比较。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8)]]; [[Argument_Hogan_2013_ROE|(Hogan et al., 2013, p. 89)]]
> - **谨慎使用** 分层变量过多的情境；每增加一个分层维度，子层总数呈几何级数膨胀，导致边缘子层样本过小甚至为空。
> - **不适合使用** 目标总体的基本人口学或结构特征完全未知、缺乏完整抽样框或分层信息无法采集的研究场景。

---

> [!method-limits] 方法局限
> - **偏误来源** 总体抽样框信息过时、分类归属错误、层内无[[Response Bias|应答偏差]]（部分亚层回收率偏低导致结构失衡）。
> - **适用边界** 严重依赖高质量先验信息；若选定的分层变量与核心研究指标完全不相关，分层抽样并不能显著降低抽样误差。
> - **层数膨胀风险** 纳入过多交叉变量会导致层数急剧膨胀，所需最小总样本量迅速超标（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen et al., 2011, p. 146]]）。
> - **补救方式** 精简分层变量至最关键的 1–2 项；采用事后分层加权调整应答偏差；结合复合抽样设计（Complex Sampling）修正标准误估计。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Random Sampling]] | 基础方法 | 分层抽样在每一个层内部严格执行简单随机抽样。 |
> | [[Cluster Sampling]] | 替代方法 | 整群抽样以自然群体为抽样单位追求实地便利性，而分层抽样旨在通过层间控制降低方差。 |
> | [[Sample Size Determination]] | 前置技术 | 依据统计功效与可接受误差界定各层所需分配的样本量配额。 |
> | [[Random Assignment]] | 对应方法 | 随机分配用于[[Experimental Research\|实验设计]]中的组别平衡，分层抽样用于[[Survey Research\|调查研究]]中的样本代表性控制。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Nordtveit_2011_IJED|Nordtveit (2011)]] — 在质性实地调研中采用分层抽样策略，按机构职能与利益相关方分层选取覆盖孔子学院师生、政府官员、驻喀外交官及国际组织代表等 31 位知情人。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen et al. (2011)]] — 系统阐述分层抽样的统计原理、两步操作规程、等比例与非等比例配置以及层数膨胀风险控制（Ch. 8, pp. 145–146）。
> - [[Argument_Hogan_2013_ROE|Hogan et al. (2013)]] — 采用两阶段分层随机抽样设计，按学校办学声誉层次与中三学术轨道（快捷源流、普通学术源流、普通工艺源流）分层抽取新加坡 31 所中学 5,420 名学生与对应教师样本（pp. 88–90）。
