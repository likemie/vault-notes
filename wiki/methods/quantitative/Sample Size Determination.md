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
method_related_count: 37
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
updated: 2026-10-29
---

---

> [!def] Sample Size Determination
> **样本量确定（Sample Size Determination）** 是指在实证研究设计阶段，研究者依据[[Research Purpose|研究目的]]、总体规模与[[Heterogeneity|异质性]]、期望统计功效（Power, $1-\beta$）、名义显著性水平（$\alpha$）、容许误差界线（[[Confidence Interval|margin of error]]）以及具体统计模型要求，科学测算并规划所需观测案例规模（学生个体、教师、学校或集群）的量化决策过程。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 143–145)]]
>
> 在[[Meta-analysis|元分析]]与[[Meta-meta-analysis|二阶元分析]]中，受试样本量（$N$ 或 $n$）不仅是计算[[Effect Size|效应量]]精度与逆方差权重（$w_i = 1/v_i$）的数学输入，更是[[Metascience|元科学]]质量审计中核验底层文献数据提取可复现性的生命线。[[Argument_Kalmendal_2025_PsyArXiv|(Kalmendal et al., 2025, pp. 18–19)]]

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

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **统计功效平衡** 样本量确定本质上是在 I 型错误率（$\alpha$）与 II 型错误率（$\beta$）之间进行理性权衡，防范因样本过小导致统计检出力不足（Underpowered Studies），亦防范盲目超大样本使得微不足道的细微差异呈现伪显著。
> - **代表性与规模辩证** 样本绝对规模并不天然等同于代表性。缺乏良好[[Sampling Frame|抽样框架]]的大样本（如对偏态子群的过度访问）无法克服选择偏差；反之，在分层良好的前提下，中小规模概率样本亦能提供稳健推断。
> - **二阶综合中的[[Reliability|信度]]锚点** 在宏观[[Meta-meta-analysis|二阶元分析]]中，报告的样本量是判定一阶证据规模真实性的唯一客观依据。主观估算或缺失样本量将彻底破坏证据的透明度与可审计性。

> [!feature] 影响样本量规划的核心参数
> - **总体规模与[[Heterogeneity|异质性]]** 总体异质性越大，所需样本量呈指数级增加。但对于同质性较高的大规模总体（$N > 100{,}000$），[[Random Sampling|随机样本]]量在 95% [[Confidence Interval|置信水平]]与 5% 边际误差下渐近收敛至 384 左右（Krejcie & Morgan, 1970）。
> - **置信水平与区间宽度** 99% 置信水平所需样本显著高于 95%；要求 $\pm 3\%$ 的边际误差所需样本量数倍于 $\pm 5\%$ 容许误差。
> - **模型与分析方法门槛** [[Chi-Squared Test|卡方检验]]要求 80% 单元格频数 $\ge 5$；[[Multiple Regression|多元回归]]建议每个[[Independent Variable|自变量]]至少对应 10–20 个观测案例；[[Exploratory Factor Analysis|探索性因子分析]]常规要求 $N \ge 100$ 至 $300$。
> - **损耗与流失冗余** 针对[[Questionnaire|问卷]]无应答、长期追踪中的[[Attrition|样本流失]]，必须预先在理论样本量基础上增设 20%–50% 的安全冗余（Gorard, 2003）。

---

> [!formula-step] 公式步骤一　有限总体均值估计样本量计算公式（Krejcie & Morgan 经典模型）
> $$n = \frac{\chi^2 N P (1 - P)}{d^2 (N - 1) + \chi^2 P (1 - P)}$$
>
> **这个公式在做什么** 根据已知总体容量 $N$，在设定的[[Confidence Interval|置信水平]]（$\chi^2$）与边际误差界线 $d$ 下，计算出能够充分代表该总体的最低必需样本量 $n$。
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
> **结果怎么读** 算出的 $n$ 为底线门槛。实际抽样方案中的最终发放量还必须除以预期回收有效率（Response Rate）。

> [!formula-step] 公式步骤二　[[Multiple Regression|多元回归]]与[[Independent Variable|自变量]]观测比率准则（Bartlett et al. 规则）
> $$N_{\text{regression}} \ge k \times 10 \quad \text{或} \quad N_{\text{regression}} \ge 50 + 8k$$
>
> **这个公式在做什么** 为多[[Meta-regression|元回归]]模型确立统计稳定性底线，防止由于自[[Variable|变量]]过多而样本过少导致的严重过度拟合与膨胀的[[Standard Error|标准误]]。
>
> **符号说明**
> - $k$：纳入回归模型的自变量（协变量）总数。
>
> **数学直觉** 每一个引入模型的自由参数都需要一定自由度的残差方差进行锚定，样本与变量比值低于 5:1 将导致普通最小二乘估计极不稳定。

---

## 围绕样本量的学术命题

### 命题一　样本规模与抽样代表性之间存在深刻的方法学解耦

> [!concept-lens] 规模崇拜与抽样偏差的辩证
> 围绕大样本是否等价于高质代表性展开，破除对单纯样本规模的机械崇拜。

> [!claim] [[Louis Cohen|Cohen, L.]]
> **大样本不保证代表性，小样本不必然缺乏代表性。** 教师可以访谈 450 名女生，却依然完全未能代表该校男生群体的观点；反之，一个经过严格分层随机抽取的 100 人样本，在反映群体均值上可能远胜于成千上万个自发填写的网络偏差样本。经验不足的研究者往往急于设定所需样本数量却未事先界定总体，导致样本代表性完全不可检验。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 143–146)]]

---

### 命题二　二阶证据综合中伴随样本量的失真暴露了底层提取质量的系统性溃败

> [!concept-lens] [[Meta-meta-analysis|二阶元分析]]与证据库审计中的样本量准确度危机
> 探讨宏观[[Research Synthesis|证据综合]]项目在[[Transcription in Qualitative Research|转录]]一阶文献时样本量报告的[[Reliability|信度]]危机。

> [!claim] Kalmendal, A.
> **二阶[[Meta-analysis|元分析]]中伴随受试样本量的高失误率证实了底层数据整理机制的系统性失效。** 对《[[Visible Learning|可见的学习]]》全库开展的独立复现检验显示，在 301 项可查影响因素中，仅有 2 项能成功复现。即使在[[Effect Size|效应量]]数值勉强核对正确的少数案例中，伴随的学生受试样本量错误率仍高达 **72%**。大量的学生样本量在原文中完全不存在，充斥着无根据的人为主观估算。样本量的虚假膨胀与胡乱拼凑直接扭曲了宏观证据的综合权重，构成了二阶综合面临的最根本[[Metascience|元科学]]质量危机。[[Argument_Kalmendal_2025_PsyArXiv|(Kalmendal et al., 2025, pp. 18–19)]]

---

> [!entry-map] 相关理论与方法
> | 条目 | 类型 | 关系说明 |
> |---|---|---|
> | [[Power Analysis]] | 配套方法 | 样本量确定在上游依赖统计功效分析以设定合理的样本规模。 |
> | [[Effective Sample Size]] | 概念扩展 | [[Cluster Randomized Trials\|集群随机试验]]中考虑[[Intraclass Correlation Coefficient\|群内相关系数]]（ICC）校正后的真实独立信息量。 |
> | [[Inverse-Variance Weighting]] | 下游应用 | [[Meta-analysis\|元分析]]中直接依托初级[[Study Population and Sample\|研究样本]]量及抽样方差为[[Effect Size\|效应量]]分配精度权重。 |
> | [[Random Sampling]] | 抽样原则 | 样本量公式发挥无偏代表性推断作用的数学前提。 |
> | [[Visible Learning]] | 审计案例 | 伴随受试样本量错误率高达 72%、充斥人为虚报的典型宏观数据库案例。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 经典[[Quantitative Research|量化研究]]设计指南，系统论述样本量规划的多重制约、Krejcie-Morgan 公式及经验法则。
> - [[Argument_Kalmendal_2025_PsyArXiv|Kalmendal et al. (2025)]] — 首个全库[[Preregistration|预注册]][[Metascience|元科学]]质量审计，穷尽核对 301 项宏观影响因素的一阶受试样本量与[[Effect Size|效应量]]，实证揭露 72% 的伴随样本量提取错误，确立了样本量透明度与可复现性审计标准。
