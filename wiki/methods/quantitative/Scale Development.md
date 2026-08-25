---
title: Scale Development
aliases:
  - 量表编制
  - 量表开发
  - 量表构建
  - Scale Construction
  - Scale Validation
summary: "在心理学与教育学中开发和验证测量不可直接观测潜变量的标准化自陈或评定量表的全流程方法论，涵盖构念界定、题池生成、专家评审、探索性因子分析（EFA）、验证性因子分析（CFA）、信效度检验及跨群体测量等值性确立。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 13
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - theme/scale-development
  - theme/psychometrics
related_concepts:
  - "[[Construct]]"
  - "[[Construct Validity]]"
  - "[[Content Validity]]"
  - "[[Likert Scale]]"
related_theories:
  - "[[Classical Test Theory]]"
related_methods:
  - "[[Exploratory Factor Analysis]]"
  - "[[Confirmatory Factor Analysis]]"
  - "[[Pilot Testing]]"
  - "[[Survey Research]]"
related_instruments:
  - "[[Research Literacy Scale for Teachers]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
  - "[[Argument_Bergeron_2015_TeachingTOK]]"
  - "[[Argument_Greene_2010_JEP]]"
confidence: high
status: draft
created: 2026-08-26
updated: 2026-08-26
---

# Scale Development

---

## 定义

> [!def] 方法定义
> **量表编制（Scale Development）** 是指在心理学、教育学及社会科学中，依据严密测量理论（如[[Classical Test Theory|经典测量理论]]（Classical Test Theory, [[Classical Test Theory|CTT]]）或[[Item Response Theory|项目反应理论]]（Item Response Theory, IRT）），将抽象且不可直接观测的[[Construct|理论构念]]（如态度、信念、素养、动机等潜[[Variable|变量]]）[[Operationalization|操作化]]为一组标准化、可定量测度的指标题项，并通过跨样本实证检验确立其构念结构、[[Content Validity|内容效度]]、[[Construct Validity|结构效度]]、[[Reliability|信度]]指标及跨群体测量等值性的系统方法论流程。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, pp. 4–6)]]

> [!method-scope] 方法范围
> - **研究对象** 无法直接物理测量的个体心理特质、认知结构、专业素养、态度倾向、行为意向或组织感知。
> - **问题类型** 测量工具构建、维度结构探索与确证、跨群体测量不变性识别、心理计量属性评定。
> - **分析单位** 被试个体的逐题自陈作答数据。
> - **输出形式** 标准化量表手册（题项清单、作答格式与计分规则）、因子载荷矩阵、模型拟合指数、平均方差抽取量（Average Variance Extracted, AVE）与组合信度（Composite Reliability, CR）效度矩阵、各分量表与总量表信度系数。

> [!citation-card]- 关键定义
> 量表编制是一个多阶段、迭代演进的过程，研究者首先界定构念的理论边界，生成初始题池并进行专家内容效度评审，随后在独立样本中分别执行[[Exploratory Factor Analysis|探索性因子分析]]（Exploratory Factor Analysis, EFA）以精简题项与发现维度，以及[[Confirmatory Factor Analysis|验证性因子分析]]（Confirmatory Factor Analysis, CFA）以确证因子结构、检验收敛与[[Convergent and Discriminant Validity|区分效度]]并确立测量等值性。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, pp. 4–5)]]
>
> *Scale development is an iterative, multi-phase process in which researchers define the theoretical boundaries of a construct, generate an item pool, assess content validity with experts, and administer the instrument across independent samples to conduct EFA for dimension discovery and CFA for structural verification, convergent/discriminant validity, and measurement invariance.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 假定潜在特质虽然无法直接观测，但可以通过一系列反映该特质的外显行为指标进行概率性、线性加权推断。
> - **研究者角色** 研究者必须在[[Construct|构念]]界定、题项拟定、因子截断标准选择及模型误差修正中保持高度理论自觉，避免陷入纯粹的数据驱动拟合。
> - **有效性标准** 遵循严密的测量学阶梯：[[Face Validity|表面效度]] $\rightarrow$ [[Content Validity|内容效度]] $\rightarrow$ 探索性[[Construct Validity|结构效度]]（[[Exploratory Factor Analysis|EFA]]） $\rightarrow$ 验证性结构效度（[[Confirmatory Factor Analysis|CFA]]） $\rightarrow$ 收敛与[[Convergent and Discriminant Validity|区分效度]]（Fornell-Larcker 准则） $\rightarrow$ 跨群体测量等值性。
> - **不声称回答的问题** 量表本身仅提供测量构念的有效工具，量表得分之间的相关或群体差异无法直接推断[[Causality|因果关系]]，需结合实验设计或纵向追踪模型。

> [!method-stack] 方法层级
> - **研究设计** 测量工具开发设计、两阶段横断面调查设计。
> - **数据收集** 专家[[Delphi Technique|德尔菲法]]、认知访谈预试、大规模纸笔或在线[[Questionnaire|问卷调查]]。
> - **分析方法** 题总相关分析、探索性因子分析（EFA）、验证性因子分析（CFA）、多组验证性因子分析（Multigroup Confirmatory Factor Analysis, MG-CFA）、多[[Variable|变量]][[Analysis of Variance|方差分析]]（Multivariate Analysis of Variance, MANOVA）。
> - **辅助技术** 缺失值期望极大化算法（Expectation-Maximization algorithm, EM）插补、马氏距离多变量离群值筛查、Bootstrap 稳健估计、方差最大正交旋转（Varimax Rotation）或斜交旋转（Promax/Oblimin）。

---

## 研究程序

> [!proc] 量表编制与验证的标准全流程（DeVellis 经典[[Paradigm|范式]]与现代三阶段模型）
> 1. **第一阶段：[[Construct|构念]]界定与题项生成（Item Generation & [[Content Validity]]）**
>    - **理论构念[[Operationalization|操作化]]** 深入梳理[[Document|文献]]，明确构念的理论内涵、子维度及边界条件。
>    - **初始题池编写** 编写 3–4 倍于目标长度的陈述句题池（通常 40–80 题），避免双重陈述（Double-barreled items）、双重否定与模糊表述；确定李克特计分锚点（如 5 级或 7 级）。
>    - **专家效度评审** 邀请 5–10 位领域专家与心理测量学者对题项的相关性、代表性与表述清晰度进行内容效度比率（Content Validity Ratio, CVR）或内容效度指数（Content Validity Index, CVI）打分。
>    - **目标群体预试与认知访谈** 选取 10–20 名目标群体成员进行试读，评估题意理解度并修正歧义。
> 2. **第二阶段：量表初测与结构探索（Scale Development & [[Exploratory Factor Analysis|EFA]]）**
>    - **第一阶段样本施测** 在代表性样本 1（推荐 $N \ge 300$ 或[[Sample Size Determination|样本量]]与题项比 $\ge 5:1$）中施测。
>    - **题项初筛** 计算矫正题总相关，剔除 $r < .30$ 的低区分度题项；检查极端值与方差接近零的题项。
>    - **数据适宜性检验** 检验相关矩阵（大部分 $> .30$）、Anti-image 对角线值（$> .70$）、Kaiser-Meyer-Olkin 抽样适宜性系数（KMO $> .80$）及 Bartlett 球形检验（$p < .001$）。
>    - **探索性因子分析（EFA）** 选用主轴因子提取法（Principal Axis Factoring, PAF）或极大似然估计（Maximum Likelihood, ML），结合碎石图（Scree Plot）、特征值大于 1（Kaiser 准则）及平行分析（Parallel Analysis）确定因子数；执行正交或斜交旋转，依据载荷 $> .32$ 且跨载荷差值 $> .10$ 逐题剔除杂题，提炼出清晰的潜在因子结构。
> 3. **第三阶段：量表确证与高级心理测量（Scale Validation & [[Confirmatory Factor Analysis|CFA]]）**
>    - **第二阶段独立样本施测** 收集全新独立样本 2（$N \ge 200\sim300$）以避免单一样本过拟合偏差。
>    - **验证性因子分析（CFA）** 使用结构方程模型（Structural Equation Modeling, [[Causal Modeling|SEM]]）软件对比竞争模型（单因子模型 vs 一阶多因子模型 vs 二阶高阶因子模型）；评估模型拟合指数（$\chi^2/df < 3$、近似误差均方根 $\text{RMSEA} < 0.08$、标准均方根残差 $\text{SRMR} < 0.08$、比较拟合指数 $\text{CFI} \ge 0.90$、非规范拟合指数 $\text{NNFI/TLI} \ge 0.90$）；基于理论与修正指数审慎释放误差协方差。
>    - **[[Convergent and Discriminant Validity|收敛效度]]与区分效度检验** 计算各因子的平均方差抽取量（AVE $\ge .50$）与组合[[Reliability|信度]]（CR $\ge .70$）；验证 Fornell-Larcker 准则（因子间相关系数平方 $r^2 < \text{AVE}$）。
>    - **复合信度电池检验** 报告 Cronbach's $\alpha$、McDonald's $\omega$、Armor's $\theta$、[[Split-Half Reliability|折半信度]]（Spearman-Brown）与 Guttman $\lambda$。
>    - **跨群体多组测量等值性（Measurement Invariance）** 执行阶梯约束检验：形态等值（Configural） $\rightarrow$ 弱等值（Metric，因子载荷等值） $\rightarrow$ 强等值（Scalar，截距等值） $\rightarrow$ 严格等值（Strict，残差等值），以 $\Delta\text{CFI} \le .010$ 和 $\Delta\text{RMSEA} \le .010$ 为不变性成立判据。
>    - **[[Criterion-related Validity|效标关联效度]]与实证应用** 检验量表得分与外部[[Dependent Variable|效标变量]]的相关性，或通过[[Analysis of Variance|方差分析]]（ANOVA/MANOVA）检验人口统计学与经验[[Variable|变量]]的主效应。

---

## 量化方法模块

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** 独立双样本（样本 1 用于 [[Exploratory Factor Analysis|EFA]]，样本 2 用于 [[Confirmatory Factor Analysis|CFA]] 及效度验证）多题项等级数据。
> - **[[Sample Size Determination|样本量]]原则** 普遍要求样本量 $N \ge 200\sim300$，且每题项被试比（Participant-to-Item Ratio）在 EFA 阶段不低于 5:1–10:1。
> - **变量构成** 观测题项（Observed Items $X_1, X_2, \dots, X_p$）、一阶潜变量（First-order Latent Factors $\xi_1, \dots, \xi_k$）、二阶潜变量（Second-order Latent Factor $\Xi$）、测量误差项（$\delta_i$）。
> - **拟合评估** $\chi^2$、自由度 $df$、$\chi^2/df$、RMSEA、SRMR、NNFI/TLI、CFI。

> [!formula-step] 公式步骤　平均变异抽取量（AVE）与组合[[Reliability|信度]]（CR）
> $$\text{AVE} = \frac{\sum_{i=1}^{k} \lambda_i^2}{\sum_{i=1}^{k} \lambda_i^2 + \sum_{i=1}^{k} \theta_i}, \quad \text{CR} = \frac{\left(\sum_{i=1}^{k} \lambda_i\right)^2}{\left(\sum_{i=1}^{k} \lambda_i\right)^2 + \sum_{i=1}^{k} \theta_i}$$
>
> **这个公式在做什么** 输入 CFA 得到的标准化因子载荷 $\lambda_i$ 与误差方差 $\theta_i = 1 - \lambda_i^2$，计算潜变量对观测指标的平均方差解释力（AVE）与综合[[Internal Consistency|内部一致性]]（CR）。
>
> **数学直觉** AVE 衡量潜变量真正解释的变异占总变异（真实变异 + 测量误差）的比例；CR 则衡量指标加总后合成潜变量得分的信度水平。
>
> > [!result-reading]- 结果怎么读
> > - **AVE 判定** AVE $\ge .50$ 表明潜变量能够解释指标超过半数的变异，[[Convergent and Discriminant Validity|收敛效度]]良好；若 AVE 小于各因子间的决定系数（$r^2$），则提示区分效度不足。
> > - **CR 判定** CR $\ge .70$ 表明潜变量指标合成具备高内部一致性，优于受题项数影响较大的传统 Cronbach's $\alpha$。

> [!formula-step] 公式步骤　多组验证性因子分析测量等值性检验（Cheung & Rensvold 标准）
> $$\Delta\text{CFI} = \text{CFI}_{\text{restricted}} - \text{CFI}_{\text{base}}, \quad \Delta\text{RMSEA} = \text{RMSEA}_{\text{restricted}} - \text{RMSEA}_{\text{base}}$$
>
> **这个公式在做什么** 评估在多组 CFA 中依次施加更严格参数等值约束（载荷等值、截距等值、残差等值）后模型拟合指数的变化量。
>
> **数学直觉** 由于样本量较大时 $\Delta\chi^2$ 差异检验过度敏感容易拒绝等值[[Hypothesis|假设]]，现代心理测量学采用拟合指数改变量作为稳健判据。
>
> > [!result-reading]- 结果怎么读
> > 当 $|\Delta\text{CFI}| \le .010$ 且 $|\Delta\text{RMSEA}| \le .010$（样本量 $<300$ 时 Chen 2007 建议 $|\Delta\text{RMSEA}| \le .010$）时，表明增加的跨组等值约束没有引起模型拟合的实质性恶化，对应水平的测量等值性成立。

> [!software-impl] 软件实现
> - **推荐软件** R（`psych`, `lavaan`, `semTools`）、SPSS、LISREL、Mplus、Jamovi。
> - **核[[Flow|心流]]程**
>   1. **EFA 阶段（SPSS / R psych）** 使用 `fa(r, nfactors=4, rotate="varimax", fm="pa")` 执行主轴因子分解与方差最大旋转。
>   2. **CFA 阶段（R lavaan / LISREL）** 使用 `cfa(model, data=sample2, estimator="ML")` 估计一阶与二阶模型拟合。
>   3. **测量等值性（R semTools）** 使用 `measurementInvariance(model, data=sample2, group="gender")` 阶梯检验跨组不变性。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 需要开发全新测量工具、修订已有量表以适应新文化与语言情境、确立测量[[Construct|构念]]的理论结构、或评估测量工具在不同人群中是否具备可比性时。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, pp. 4–5)]]
> - **谨慎使用** [[Sample Size Determination|样本量]]不足（$N < 150$）时，因参数估计不稳定容易导致因子结构畸变；当题项严重偏态（非正态李克特数据）时，使用传统极大似然估计（ML）需谨慎，应采用稳健估计法（MLR/WLSMV）。
> - **不适合使用** 测量客观单一事实（如年龄、教龄、考试卷面分数）或简单二元记录时，无需开展复杂的潜[[Variable|变量]]量表编制。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 自陈量表固有的社会赞许偏差（Social Desirability Bias）、中心化倾向、同源方法变异（[[Common Method Variance]], CMV）。
> - **样本依赖性** [[Exploratory Factor Analysis|EFA]] 提炼出的因子结构对特定样本特征高度敏感，若不在独立样本中通过 [[Confirmatory Factor Analysis|CFA]] 交叉验证，容易出现样本假象（sample-specific artifact）。
> - **误用风险** 混淆探索性与验证性阶段（在同一数据集上既跑 EFA 又跑 CFA 导致循环论证）；盲目根据修正指数释放无关题项的误差协方差以人为提升模型拟合。
> - **补救方式** 坚持双独立样本分离施测、严格执行理论引导的误差协方差修正、结合多组 CFA 检验跨人口学[[Variable|变量]]的不变性。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Classical Test Theory]] | 理论 | 为真分数模型、测量误差分解及[[Reliability\|信度]]估计提供基础理论支撑。 |
> | [[Construct Validity]] | 理论 | 量表编制追求的核心效度目标，包括[[Convergent and Discriminant Validity\|收敛效度]]、区分效度与因子结构效度。 |
> | [[Content Validity]] | 理论 | 量表编制前期的关键效度保障，依托[[Document\|文献]]梳理与专家德尔菲评审。 |
> | [[Exploratory Factor Analysis]] | 前置方法 | 量表开发初期的维度精简与结构探索核心工具。 |
> | [[Confirmatory Factor Analysis]] | 后续方法 | 量表验证阶段确证因子模型、检验 AVE 与 CR 以及测量等值性的核心工具。 |
> | [[Pilot Testing]] | 补充方法 | 在大规模施测前检验题意清晰度与作答流畅度的必要环节。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 严格遵循 DeVellis 规范开发 20 题四维度《[[Research Literacy Scale for Teachers|教师研究素养量表]]》（RLS），利用样本 1（$N=310$）完成 [[Exploratory Factor Analysis|EFA]] 维度精简，利用独立样本 2（$N=258$）完成 [[Confirmatory Factor Analysis|CFA]] 结构确证、AVE 与 CR 效度检验及跨性别严格测量等值性验证。
> - [[Argument_Bergeron_2015_TeachingTOK|Bergeron & Rogers (2015)]] — 编制并验证包含 11 道题的[[Confidence Teaching TOK Scale|知识论教学信心量表]]（Confidence Teaching [[Theory of Knowledge|TOK]] Scale），通过 EFA 确立单因子结构并解释 35.03% 方差。
> - [[Argument_Greene_2010_JEP|Greene et al. (2010)]] — 编制并检验《[[Epistemic and Ontological Cognition Questionnaire|认识论与本体论认知问卷]]》（EOCQ），通过 CFA 检验数学和历史领域的维度结构及其跨领域拟合度。
