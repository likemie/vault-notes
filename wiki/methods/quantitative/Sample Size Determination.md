---
title: Sample Size Determination
aliases:
  - 样本量确定
  - sample size
  - 样本量
  - determining sample size
  - sample size calculation
summary: "研究设计中确定样本大小的决策过程，权衡统计功效、抽样误差、异质性与代表性，并在二阶元分析数据提取中作为权重量化与复现审计的关键参数"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 38
method_related_level: 3
method_related_stars: "💎"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/sampling
  - quantitative-research
  - research-design
  - metascience
  - methodology
related_concepts:
  - "[[Research Purpose]]"
  - "[[Heterogeneity]]"
  - "[[Metascience]]"
  - "[[Document]]"
  - "[[Unit of Analysis]]"
  - "[[Variable]]"
  - "[[Paradigm]]"
  - "[[Purpose Statement]]"
  - "[[Epistemology]]"
  - "[[Reliability]]"
  - "[[Independent Variable]]"
  - "[[Attrition]]"
  - "[[Visible Learning]]"
  - "[[Effective Sample Size]]"
  - "[[Study Population and Sample]]"
  - "[[Preregistration]]"
related_theories: []
related_methods:
  - "[[Confidence Interval]]"
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Effect Size]]"
  - "[[Sampling Frame]]"
  - "[[Random Sampling]]"
  - "[[Chi-Squared Test]]"
  - "[[Multiple Regression]]"
  - "[[Exploratory Factor Analysis]]"
  - "[[Questionnaire]]"
  - "[[Meta-regression]]"
  - "[[Standard Error]]"
  - "[[Research Synthesis]]"
  - "[[Transcription in Qualitative Research]]"
  - "[[Power Analysis]]"
  - "[[Cluster Randomized Trials]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Quantitative Research]]"
related_persons:
  - "[[Louis Cohen]]"
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
  - "[[Argument_Kalmendal_2025_PsyArXiv]]"
confidence: high
status: draft
created: 2026-06-21
updated: 2026-11-04
---

---

> [!def] Sample Size Determination
> **样本量确定（Sample Size Determination）** 是指在实证研究设计阶段，研究者依据[[Research Purpose|研究目的]]、总体规模与[[Heterogeneity|异质性]]、期望统计功效（Power, $1-\beta$）、名义显著性水平（$\alpha$）、容许误差界线（[[Confidence Interval|margin of error]]）以及具体统计模型要求，科学测算并规划所需观测案例规模（学生个体、教师、学校或集群）的量化决策过程。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 143–145)]]
>
> 在[[Meta-analysis|元分析]]与[[Meta-meta-analysis|二阶元分析]]中，受试样本量（$N$ 或 $n$）不仅是计算[[Effect Size|效应量]]精度与逆方差权重（$w_i = 1/v_i$）的数学输入，更是[[Metascience|元科学]]质量审计中核验底层[[Document|文献]]数据提取可复现性的生命线。[[Argument_Kalmendal_2025_PsyArXiv|(Kalmendal et al., 2025, pp. 18–19)]]

> [!method-scope] 方法范围
> - **研究对象** 抽样设计中的个体、自然班级、学校集群、元分析中的受试者总体（$N$）。
> - **问题类型** 抽样精度规划、统计功效预估、资源成本约束下的规模最优化。
> - **[[Unit of Analysis|分析单位]]** 个体样本（Individual Sample）、集群单元（Clusters）、汇总报告受试总数。
> - **输出形式** 最低必需样本量（$N_{\min}$）、最小可检测效应量（MDES）、自由度分配方案。

> [!citation-card] 样本量与研究情境的动态依存
> 研究需要多大的样本量没有一刀切的简单答案。正确样本量取决于研究目的、被调查总体的特征、所要求的精确度、预期回应率、研究包含的[[Variable|变量]]数量，以及采用的[[Paradigm|研究范式]]是定量还是定性。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, p. 144)]]
>
> *A question that often plagues novice researchers is just how large their samples for the research should be. There is no clear-cut answer, because the correct sample size depends on the [[Purpose Statement|purpose of the study]]...*

---

> [!method-position] 方法定位
> - **统计功效平衡** 样本量确定本质上是在 I 型错误率（$\alpha$）与 II 型错误率（$\beta$）之间进行理性权衡，防范因样本过小导致统计检出力不足（Underpowered Studies），亦防范盲目超大样本使得微不足道的细微差异呈现伪显著。
> - **代表性与规模辩证** 样本绝对规模并不天然等同于代表性。缺乏良好[[Sampling Frame|抽样框架]]的大样本（如对偏态子群的过度访问）无法克服选择偏差；反之，在分层良好的前提下，中小规模概率样本亦能提供稳健推断。
> - **二阶综合中的[[Reliability|信度]]锚点** 在宏观[[Meta-meta-analysis|二阶元分析]]中，报告的样本量是判定一阶证据规模真实性的唯一客观依据。主观估算或缺失样本量将破坏证据的透明度与可审计性。

---

> [!formula-step] 步骤一　有限总体均值估计样本量计算公式（Krejcie & Morgan 经典模型）
> $$n = \frac{\chi^2 N P (1 - P)}{d^2 (N - 1) + \chi^2 P (1 - P)}$$
>
> **这个公式在做什么** 根据已知总体容量 $N$，在设定的[[Confidence Interval|置信水平]]（$\chi^2$）与边际误差界线 $d$ 下，计算出能够充分代表该总体的最低必需样本量 $n$。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, p. 145)]]
>
> **符号说明**
> - $n$：理论所需[[Random Sampling|随机样本]]量。
> - $N$：已知的总体容量（Population Size）。
> - $\chi^2$：对应所选置信水平下自由度为 1 的卡方值（如 95% 置[[Reliability|信度]]下为 $1.96^2 \approx 3.841$）。
> - $P$：总体比例参数（通常保守取最大方差假定 $P = 0.50$）。
> - $d$：可接受的边际误差绝对值（Margin of Error，如 $0.05$）。
>
> **数学直觉** 分子反映了最大可能方差与置信度要求的乘积，分母结合了边际误差平方并随总体规模 $N$ 进行有限总体校正。当 $N \to \infty$ 时，$n \to \frac{\chi^2 P(1-P)}{d^2} \approx 384$。
>
> > [!formula-reading] 结果解读与注意事项
> > 算出的 $n$ 为底线门槛。实际抽样方案中的最终发放量还必须除以预期回收有效率（Response Rate），并预留无应答与流失冗余。

> [!formula-step] 步骤二　[[Multiple Regression|多元回归]]与[[Independent Variable|自变量]]观测比率准则（Bartlett et al. 规则）
> $$N_{\text{regression}} \ge k \times 10 \quad \text{或} \quad N_{\text{regression}} \ge 50 + 8k$$
>
> **这个公式在做什么** 为多[[Meta-regression|元回归]]模型确立统计稳定性底线，防止由于自[[Variable|变量]]过多而样本过少导致的严重过度拟合与膨胀的[[Standard Error|标准误]]。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, p. 144)]]
>
> **符号说明**
> - $k$：纳入回归模型的自变量（协变量）总数。
>
> **数学直觉** 每一个引入模型的自由参数都需要一定自由度的残差方差进行锚定，样本与变量比值低于 5:1 将导致普通最小二乘估计极不稳定。

> [!method-stack] 数据口径
> - **数据来源** 调查抽样框、行政登记数据、教育追踪数据库或元分析纳入文献。
> - **时间与范围** 抽样调查时间窗、受试者纳入与排除标准（学段、地区、年龄等）。
> - **清洗与归属** 剔除无效作答与极端异常值，对问卷无应答与长期追踪中的[[Attrition|被试损耗]]进行 20%–50% 的安全冗余预留。
> - **有效性校正** 在[[Cluster Randomized Trials|集群随机试验]]中基于[[Intraclass Correlation Coefficient|群内相关系数]]（ICC）校正[[Effective Sample Size|有效样本量]]；在元分析中严格核验初级文献报告的真实受试样本数。

---

> [!method-fit] 适用判断
> - **适合使用** 实证调查抽样设计、实验与准实验设计的统计功效（[[Power Analysis|Power]]）前置规划、多元统计模型（多元回归、因子分析）的最低观测样本量论证。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 143–145)]]
> - **谨慎使用** 集群抽样与多阶段抽样（需结合群内相关系数校正有效样本量，避免直接套用简单随机抽样公式）；存在预期高流失率的长期追踪研究（需预留充分冗余）。
> - **不适合使用** 未界定目标总体与抽样框架时盲目套用公式；将样本绝对规模等同于代表性（缺乏科学抽样框架的偏差大样本无法通过增加数量弥补系统性偏差）。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, p. 144)]]

> [!ref-table]- 参照基准与经验法则
> | 场景或模型 | 推荐参照基准 | 说明与来源 |
> |:---|:---|:---|
> | 有限总体（$N > 100{,}000$） | $n \approx 384$ | 95% 置信水平与 $\pm 5\%$ 容许误差下的渐近随机样本容量。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|Cohen et al. (2011, p. 145)]] |
> | 多元回归分析 | $N \ge 50 + 8k$ 或 $10k$–$20k$ | 保障自变量系数估计稳健性与控制标准误膨胀的底线样本量（$k$ 为预测变量数）。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|Cohen et al. (2011, p. 144)]] |
> | 探索性因子分析 | $N \ge 100$ 至 $300$ | 保障因子载荷估计稳定性与参数可识别性的基本门槛。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|Cohen et al. (2011, p. 144)]] |
> | 问卷调查与追踪研究 | 预留 20%–50% 冗余 | 预防无应答与被试损耗导致有效样本跌破统计功效阈值。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|Cohen et al. (2011, p. 145)]] |

---

> [!method-limits] 方法局限
> - **偏误来源** 总体方差与效应量事前未知导致功效估计依赖先验猜测；问卷无应答与长期追踪中的被试流失导致最终有效样本产生选择性损耗。
> - **适用边界** 样本量确定依赖明确界定的抽样框架与概率抽样假定；对于非概率抽样或滚雪球抽样，公式计算结果无法保证统计推断有效性。
> - **误用风险** 机械崇拜样本绝对规模而忽视抽样偏差；在二阶元分析与证据综合中，研究者主观估算或拼凑初级文献样本量（如《可见的学习》全库中高达 72% 的伴随样本量提取错误），直接扭曲逆方差权重与综合结论。[[Argument_Kalmendal_2025_PsyArXiv|(Kalmendal et al., 2025, pp. 18–19)]]
> - **补救方式** 抽样前严格界定目标总体与分层框架；集群研究中基于 ICC 调整有效样本量；在元分析与证据库建设中建立双人独立提取与预注册核查机制，确保样本量提取依据的可审计性与可复现性。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Power Analysis]] | 配套方法 | 样本量确定在上游依赖统计功效分析以设定合理的样本规模。 |
> | [[Effective Sample Size]] | 概念扩展 | [[Cluster Randomized Trials\|集群随机试验]]中考虑[[Intraclass Correlation Coefficient\|群内相关系数]]（ICC）校正后的真实独立信息量。 |
> | [[Inverse-Variance Weighting]] | 下游应用 | [[Meta-analysis\|元分析]]中直接依托初级[[Study Population and Sample\|研究样本]]量及抽样方差为[[Effect Size\|效应量]]分配精度权重。 |
> | [[Random Sampling]] | 抽样原则 | 样本量公式发挥无偏代表性推断作用的数学前提。 |
> | [[Visible Learning]] | 审计案例 | 伴随受试样本量错误率高达 72%、充斥人为虚报的典型宏观数据库案例。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 经典[[Quantitative Research|量化研究]]设计指南，系统论述样本量规划的多重制约、Krejcie-Morgan 公式及经验法则。
> - [[Argument_Kalmendal_2025_PsyArXiv|Kalmendal et al. (2025)]] — 首个全库[[Preregistration|预注册]][[Metascience|元科学]]质量审计，穷尽核对 301 项宏观影响因素的一阶受试样本量与[[Effect Size|效应量]]，实证揭露 72% 的伴随样本量提取错误，确立了样本量透明度与可复现性审计标准。

