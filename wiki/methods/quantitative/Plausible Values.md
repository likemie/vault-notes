---
title: Plausible Values
aliases:
  - 似真值
  - PV
  - Plausible Value
  - 似真值技术
  - 似真值插补
summary: "大规模跨国与国家教育评估（如 PISA、NAEP）中用于群体能力估计的现代多重插补统计技术，针对矩阵抽样下受试者作答题量较少导致的个体能力估计极大测量误差，基于被试作答反应与丰富背景问卷变量构建后验能力分布，抽取多个具有代表性的拟随机潜在能力数值，以在不偏倚群体方差与回归系数的前提下开展无偏统计推断。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 29
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - statistics/psychometrics
  - statistics/imputation
  - theme/large-scale-assessment
related_concepts:
  - "[[Variable]]"
  - "[[Socioeconomic Status]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Construct]]"
  - "[[Sampling Error]]"
  - "[[Independent Variable]]"
  - "[[Model Dependency]]"
  - "[[School Effectiveness]]"
  - "[[Paradigm]]"
  - "[[Heterogeneity]]"
  - "[[Objectivism]]"
related_theories: []
related_methods:
  - "[[Matrix Sampling]]"
  - "[[Questionnaire]]"
  - "[[Multiple Regression]]"
  - "[[Standard Error]]"
  - "[[Survey Research]]"
  - "[[Imputation Methods]]"
  - "[[Item Response Theory]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Statistical Significance]]"
  - "[[Differential Item Functioning]]"
  - "[[Secondary Analysis]]"
related_instruments: []
related_facts:
  - "[[PISA]]"
  - "[[National Assessment of Educational Progress]]"
  - "[[Educational Testing Service]]"
  - "[[OECD]]"
related_persons: []
related_arguments:
  - "[[Argument_Grek_2009_JEdPolicy]]"
  - "[[Argument_Morgan_Shahjahan_2014_CE]]"
confidence: high
status: draft
created: 2026-10-21
updated: 2026-10-29
---

---

> [!def] Plausible Values
> **似真值（Plausible Values, PV）** 是大规模教育评估（如[[PISA|国际学生评估项目]]，[[PISA]]；美国国家教育进展评估，[[National Assessment of Educational Progress|NAEP]]）中用于宏观群体特征估计的贝叶斯多重插补统计技术。在大规模评估采用[[Matrix Sampling|矩阵抽样]]设计时，每位受试者仅作答题库中的一部分题项，导致单人能力水平的极大似然估计或后验期望估计（EAP）伴随极大的测量误差。似真值技术通过将被试的客观试题作答反应与详尽的背景调查[[Questionnaire|问卷]][[Variable|变量]]（如家庭[[Socioeconomic Status|社会经济地位]]、学校特征、学习动机）联合建模，计算每名被试后验潜在能力分布，并从中独立抽取若干组（通常为 5 到 10 个）拟随机数值。这组数值代表了被试在给定作答表现与背景特征下可能具有的能力水平取样，用于在群体层面开展无偏的均值、方差、分位数及[[Multiple Regression|多元回归]]参数推断。[[Argument_Grek_2009_JEdPolicy|(Grek, 2009, pp. 26–27)]]; [[Argument_Morgan_Shahjahan_2014_CE|(Morgan & Shahjahan, 2014, pp. 197–198)]]

> [!method-scope] 方法范围
> - **研究对象** 矩阵抽样下受试者的不完全作答反应矩阵、背景问卷协变量向量及潜在特质连续量尺。
> - **问题类型** 消除个体能力点估计测量误差导致的群体方差低估与回归系数衰减偏差。
> - **[[Unit of Analysis|分析单位]]** 宏观受试群体、亚群体（如按性别、移民背景或社会经济地位划分）及多层嵌套数据单元。
> - **输出形式** 多重插补潜在能力数据集（PV1 至 PV10）、合并群体均值、合并方差与两级误差分解估计。

> [!citation-card] 测量误差矫正与群体推断
> 大规模评估关注的是整个教育系统在总体与结构层面的能力分布，通过多重后验抽样生成的似真值，能够消除矩阵抽样带来的测量误差污染，准确恢复总体方差与背景协变量关联。[[Argument_Grek_2009_JEdPolicy|(Grek, 2009, pp. 26–27)]]
>
> *The generation of plausible values draws on the combination of cognitive responses and rich background data... treating individual scores as random draws from a latent distribution, ensuring that macro-level indicators accurately reflect population variance without bias.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 似真值技术明确放弃了“测出单个被试精确分数”的传统[[Construct|构念]]假设，将个体潜在能力视为一个具有条件概率分布的不确定随机[[Variable|变量]]；其认识论核心在于通过保留个体能力的不确定性，换取群体统计推断的无偏性。
> - **研究者角色** 数据分析人员必须严格遵循多重插补合并准则（Rubin's Rules），对每一个 PV 变量独立运行相同统计模型，再汇总合成最终点估计与混合[[Standard Error|标准误]]。
> - **有效性标准** 群体均值与方差估计的无偏性、分位数边界精度、背景回归斜率的非衰减性。
> - **不声称回答的问题** 似真值仅用于宏观群体统计推断；单个学生的 10 个 PV 数值之间存在离散度，无法用于评定学生个人的学业等级或开展个别诊断。

> [!method-stack] 方法层级
> - **研究设计** 复杂大样本抽样[[Survey Research|调查研究]]、大规模教育监测。
> - **数据收集** [[Matrix Sampling|矩阵抽样]]测试作答数据与背景特征[[Questionnaire|问卷调查]]。
> - **分析方法** 边际极大似然潜在回归模型（Marginal Maximum Likelihood Latent Regression）、马尔可夫链蒙特卡罗抽样（MCMC）或后验直接抽样。
> - **辅助技术** 多重插补技术（Multiple [[Imputation Methods|Imputation]]）、刀切法（Jackknife）与平衡半样本重复抽样赋权（BRR）。

---

> [!proc] 通用程序
> 1. **标定题目参数** 依托全域样本，利用[[Item Response Theory|项目反应理论]]（IRT）边际极大似然法估计所有测验题目的难度与区分度参数，并保持参数固定。
> 2. **拟合潜在回归模型（Latent Regression Model）** 将被试的所有背景[[Questionnaire|问卷]]信息（经主成分降维提取的正交特征向量 $\boldsymbol{X}_j$）作为外生解释[[Variable|变量]]，与学生潜在能力 $\theta_j$ 拟合高维线性回归模型：$\theta_j = \boldsymbol{\beta}' \boldsymbol{X}_j + \epsilon_j$。
> 3. **推导个体条件后验分布** 结合个体作答反应向量 $\boldsymbol{Y}_j$ 的似然函数与基于背景特征的先验分布，推导个体潜在能力后验条件概率密度函数 $P(\theta \mid \boldsymbol{Y}_j, \boldsymbol{X}_j)$。
> 4. **蒙特卡罗随机抽取（PV 抽样）** 从每个个体的后验分布中独立抽取 $M$ 个数值（PISA 早期轮次抽取 5 个，2015 年起抽取 10 个），生成 $M$ 列似真值变量。
> 5. **二级分析多重合并** 研究者在开展二级数据分析时，必须分别对 $M$ 个数据集进行估计，应用鲁宾公式（Rubin's Rules）合并[[Sampling Error|抽样误差]]与测量插补误差。

> [!formula-step] 公式步骤一　个体条件后验概率密度
> $$P(\theta \mid \boldsymbol{Y}_j, \boldsymbol{X}_j, \boldsymbol{\xi}, \boldsymbol{\beta}, \sigma^2) = \frac{P(\boldsymbol{Y}_j \mid \theta, \boldsymbol{\xi}) \cdot \phi(\theta \mid \boldsymbol{\beta}' \boldsymbol{X}_j, \sigma^2)}{\int P(\boldsymbol{Y}_j \mid \vartheta, \boldsymbol{\xi}) \cdot \phi(\vartheta \mid \boldsymbol{\beta}' \boldsymbol{X}_j, \sigma^2) \, d\vartheta}$$
>
> **这个公式在做什么** 计算在已知被试试卷实际作答反应 $\boldsymbol{Y}_j$ 与背景协变量 $\boldsymbol{X}_j$ 的条件下，该被试潜在能力 $\theta$ 落在不同数值上的概率分布。
>
> **符号说明**
> - $P(\boldsymbol{Y}_j \mid \theta, \boldsymbol{\xi})$：给定能力 $\theta$ 与固定题目参数 $\boldsymbol{\xi}$ 时作答反应的 IRT 似然函数。
> - $\phi(\theta \mid \boldsymbol{\beta}' \boldsymbol{X}_j, \sigma^2)$：以背景回归预测值 $\boldsymbol{\beta}' \boldsymbol{X}_j$ 为均值、$\sigma^2$ 为残差方差的正态先验概率密度。

> [!formula-step] 公式步骤二　参数估计的多重插补合并准则（Rubin's Rules）
> $$\bar{Q} = \frac{1}{M} \sum_{m=1}^M \hat{Q}_m, \quad V_{\text{total}} = U + \left(1 + \frac{1}{M}\right) B$$
>
> **这个公式在做什么** 将 $M$ 个似真值独立估计出的统计量 $\hat{Q}_m$ 合并为最终点估计，并计算包含抽样方差与测量不确定性插补方差的总方差。
>
> **符号说明**
> - $\bar{Q}$：最终合并统计量（如跨国均值、回归系数）。
> - $U = \frac{1}{M} \sum_{m=1}^M V_m$：平均抽样方差（Within-[[Imputation Methods|Imputation]] Variance，由样本抽样导致）。
> - $B = \frac{1}{M - 1} \sum_{m=1}^M (\hat{Q}_m - \bar{Q})^2$：插补间方差（Between-Imputation Variance，由测量误差与题目抽样导致）。

---

> [!method-fit] 适用判断
> - **适合使用**
>   1. **宏观教育均值与极差测度** 计算国家、地区、公私立学校之间的阅读、数学或科学平均表现与能力等级百分比分布。
>   2. **教育公平与背景差距回归** 构建以学生家庭社会经济文化地位指数（ESCS）为[[Independent Variable|自变量]]的多元线性回归或[[Hierarchical Linear Model|分层线性模型]]（HLM）。
>   3. **历时教育质量趋势追踪** 依托统一量表，对比国家在多次测验周期中的整体学术素养升降态势。
> - **谨慎使用**
>   - 在二级分析中使用潜在回归模型未纳入的全新背景[[Variable|变量]]；若原始插补模型未包含该变量，可能导致二级回归系数受到向零收缩的轻微偏误。
> - **不适合使用**
>   - 提取某一个具体的似真值（如仅使用 PV1）当作确定的考试分数进行单一常规分析（会导致[[Standard Error|标准误]]被严重低估 20% 至 40%，引发显著的伪阳性推断错误）。
>   - 严禁将似真值还原至单所学校内部对具体教师进行绩效问责或对单个学生实施选拔分类。

---

> [!method-limits] 方法局限与风险
> - **计算分析门槛高昂** 二级研究者若缺乏专业计量训练，极易忽视 Rubin 合并准则与复杂调查复抽样权重的联立计算，导致文献中普遍存在错误使用单一 PV 汇报[[Statistical Significance|统计显著性]]的乱象。
> - **背景[[Variable|变量]]调节作用的[[Model Dependency|模型依赖性]]** 似真值的生成依赖于数据管理方建立的先验回归模型；如果原始调查未采集特定文化变量，该变量在后续统计推断中的方差可能被平滑或稀释。
> - **公众沟通中的黑箱与反直觉特征** 向政策制定者与社会公众解释“为什么同一个学生会有 10 个不同的测验分数”面临巨大的沟通障碍，常引发外界对数据人工编造或算法操纵的质疑。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Matrix Sampling]] | 方法 | 造成每个学生作答数据稀疏、从而必须使用似真值技术的前提性抽样设计。 |
> | [[Item Response Theory]] | 方法 | 计算题目似然函数并建立潜在能力尺度的核心计量模型。 |
> | [[Differential Item Functioning]] | 方法 | 确保跨群体题目参数恒常、为似真值后验生成提供无偏题项参数的方法。 |
> | [[Secondary Analysis]] | 方法 | 运用 [[PISA]]、[[National Assessment of Educational Progress\|NAEP]] 等公开数据库中使用似真值开展研究的通用方法。 |
> | [[Hierarchical Linear Model]] | 方法 | 结合似真值与学生—学校两层结构开展[[School Effectiveness\|学校效能]]分析的经典分析工具。 |
> | [[PISA]] | 事实 | 似真值技术最为系统化、规模化运用的跨国评估标杆工程。 |
> | [[National Assessment of Educational Progress]] | 事实 | 在 1980 年代率先开发并正式确立似真值技术[[Paradigm\|范式]]的国家评估体系。 |
> | [[Educational Testing Service]] | 事实 | 阿尔伯特·贝顿（Albert Beaton）与罗伯特·米斯莱维（Robert Mislevy）等 ETS 统计学家奠定了似真值理论。 |
> | [[Argument_Grek_2009_JEdPolicy\|Grek (2009)]] | 论证 | 剖析 PISA 依托高级统计建模过滤情境[[Heterogeneity\|异质性]]、建构跨国数据治理权威的文献。 |
> | [[Argument_Morgan_Shahjahan_2014_CE\|Morgan and Shahjahan (2014)]] | 论证 | 剖析大规模跨国测验技术规程与心理测量专家共同体合法性建构机制的文献。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Grek_2009_JEdPolicy|Grek (2009)]] — 揭示[[OECD|经合组织]]如何运用以似真值多重插补与[[Matrix Sampling|矩阵抽样]]为核心的高阶数理技术，确立国际大规模测验中无可辩驳的[[Objectivism|客观主义]]品牌声誉。
> - [[Argument_Morgan_Shahjahan_2014_CE|Morgan and Shahjahan (2014)]] — 论证跨国测评研制如何依赖专业测量专家财团的统计黑箱技术，将宏观教育目标转化为特定的计量分析规程。
