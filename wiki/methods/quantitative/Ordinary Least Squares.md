---
title: Ordinary Least Squares
aliases:
  - 普通最小二乘法
  - 最小二乘回归模型
  - 普通最小二乘回归
  - 最小二乘法
  - OLS
  - Ordinary Least Squares Regression
summary: "线性回归参数估计的最经典基准模型，通过最小化观测值与线性拟合值之间的残差平方和求解回归系数，在高斯-马尔可夫假定下具备最佳线性无偏估计（BLUE）性质。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 43
method_related_level: 5
method_related_stars: "⭐⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/statistical
  - method/regression
  - method/econometrics
related_concepts:
  - "[[Dependent Variable]]"
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Unit of Analysis]]"
  - "[[Model Dependency]]"
  - "[[Absorptive Capacity]]"
  - "[[Type I and Type II Errors]]"
  - "[[Epistemology]]"
  - "[[Independent Variable]]"
  - "[[Hypothesis]]"
  - "[[Heterogeneity]]"
  - "[[Interaction Effect]]"
  - "[[Academic Achievement]]"
  - "[[Effective Sample Size]]"
  - "[[Evidence-Based Education]]"
related_theories: []
related_methods:
  - "[[Randomised Controlled Trials]]"
  - "[[Pre-test and Post-test]]"
  - "[[Analysis of Covariance]]"
  - "[[Covariate Adjustment]]"
  - "[[Standard Error]]"
  - "[[Multiple Regression]]"
  - "[[Accounts]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Meta-regression]]"
  - "[[Generalized Estimating Equations]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Experimental Research]]"
  - "[[Regression Discontinuity Design]]"
  - "[[Difference-in-Differences]]"
  - "[[Questionnaire]]"
  - "[[Random Assignment]]"
  - "[[Confidence Interval]]"
  - "[[Effect Size Conversion]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Propensity Score Matching]]"
  - "[[Statistical Significance]]"
  - "[[Effect Size]]"
  - "[[Simple Difference in Means Model]]"
  - "[[Analysis of Variance]]"
related_instruments: []
related_persons:
  - "[[Steve Higgins]]"
related_facts:
  - "[[Education Endowment Foundation]]"
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
confidence: high
status: active
created: 2026-09-15
updated: 2026-09-15
---

# Ordinary Least Squares

---

## 定义

> [!def] 方法定义
> **普通最小二乘法（Ordinary Least Squares，简称 OLS）**是统计学、计量经济学与实证教育研究中最核心、应用最广泛的参数化线性回归估计方法。该方法以代数投影原理为基础，通过最小化样本观测值[[Dependent Variable|因变量]]与模型线性预测值之间的残差平方和（Sum of Squared Residuals, SSR），求解使误差达到全局最小的回归参数向量 $\hat{\boldsymbol{\beta}}$。在满足高斯-马尔可夫定理（Gauss-Markov Theorem）的古典线性假定下，OLS 估计量是所有线性无偏估计量中方差最小的最佳线性无偏估计（Best Linear Unbiased Estimator, BLUE）。在[[Randomised Controlled Trials|随机对照试验]]（RCT）中，引入基线[[Pre-test and Post-test|前测]]的 OLS 模型（即[[Analysis of Covariance|协方差分析]] ANCOVA 回归形式）能够大幅吸收个体基线能力变异，是[[Covariate Adjustment|协变量调整]]的主流基准。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 52–53)]]

> [!method-scope] 方法范围
> - **研究对象** 连续型因[[Variable|变量]]与一组解释变量（连续、离散或分类虚拟变量）之间的线性相关或条件均值关系。
> - **问题类型** 线性关联检验、条件均值预测、边际效应估计、[[Causality|因果推断]]协变量控制与平均处理效应评估。
> - **[[Unit of Analysis|分析单位]]** 学生个体、教师、学校、地区或年份横截面数据。
> - **输出形式** 回归系数向量 $\hat{\boldsymbol{\beta}}$、判定系数 $R^2$、回归[[Standard Error|标准误]]、系数 $t$ 统计量及总体拟合度 $F$ 检验。

> [!citation-card] 基线前测 OLS 回归在教育试验中的方差吸收与[[Model Dependency|模型敏感性]]（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]; Xiao et al., 2016）
> 在杜伦大学学者齐·肖（ZhiMin Xiao）、[[Steve Higgins|史蒂夫·希金斯]]（Steve Higgins）与阿迪特·卡西姆（Adetayo Kasim）针对英国 [[Education Endowment Foundation|EEF]] 早期 17 项大规模教育 RCT 开展的四模型并行复算中，引入基线前测成绩的普通最小二乘回归模型（OLS with pre-test）展现出强大的方差[[Absorptive Capacity|吸收能力]]，使干预效应的残差标准误大幅收缩、统计功效显著提高。然而，复算同时暴露了标准 OLS 在面对学校和班级嵌套数据时的脆弱性：由于忽略了同校学生误差项的群聚相关性，未校正聚类结构的 OLS 会严重低估标准误，导致原本不显著的效应呈现虚假显著。这一发现直接促成了《EEF 评估统计分析指南》（*Statistical Analysis Guidance for EEF Evaluations*; The EEF, 2018）对协变量选择与聚类稳健标准误的强制规范。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 52–53)]]
>
> *“In education trials, [[Multiple Regression|OLS regression]] controlling for prior attainment explains substantial outcome variance, reducing standard errors. However, Xiao et al. (2016) demonstrated that failing to [[Accounts|account]] for school-level clustering in standard OLS inflates [[Type I and Type II Errors|Type I error]] rates, highlighting the need for clustered standard errors or multilevel specifications.”*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 建立在条件期望函数（Conditional Expectation Function, CEF）线性逼近论之上。假定复杂的现实因果与关联模式可通过[[Independent Variable|自变量]]的线性组合进行局部最优逼近；在[[Causality|因果推断]]视角下，若满足条件独立性假定（CIA），回归系数可被赋予净因果边际贡献的解释。
> - **核心理论假定** 古典高斯-马尔可夫假定：线性函数设定、设计矩阵列满秩（无完全多重共线性）、条件均值为零（严格外生性 $E[\varepsilon|\mathbf{X}] = 0$）、球形扰动项（同方差性 $\text{Var}(\varepsilon_i|\mathbf{X}) = \sigma^2$ 与无自相关 $\text{Cov}(\varepsilon_i, \varepsilon_j|\mathbf{X}) = 0$）。
> - **有效性标准** 估计量的无偏性取决于外生性假定；有效性（BLUE）取决于球形扰动；[[Hypothesis|假设]]检验有效性依赖残差正态性或渐进正态性。
> - **不声称回答的问题** 不能在存在遗漏[[Variable|变量]]混杂或逆向因果的非实验数据中直接宣称因果；不能在未校正群聚相关的多层嵌套数据中直接套用常规[[Standard Error|标准误]]。

> [!contrast-table] OLS vs 加权/广义最小二乘（WLS/GLS） vs [[Hierarchical Linear Model|多层线性模型]]（HLM）
> | 比较维度 | 普通最小二乘法（OLS） | 加权/广义最小二乘（WLS/GLS） | 多层线性模型（HLM） |
> |---|---|---|---|
> | **误差结构假定** | 同方差、无序列相关（球形扰动） | 允许异方差或已知相关矩阵（非球形） | 显式分解为组内误差与组间多重随机效应 |
> | **异方差应对** | 需外挂怀特（White/HC）稳健标准误 | [[Inverse-Variance Weighting\|逆方差加权]]消除异方差（如[[Meta-regression\|元回归]]） | 在随机效应方程中建模方差[[Heterogeneity\|异质性]] |
> | **群聚相关处理** | 常规标准误严重低估，需 CRSE 校正 | 依赖块对角工作协方差矩阵（如 [[Generalized Estimating Equations\|GEE]]） | 模型内自然估计 [[Intraclass Correlation Coefficient\|ICC]] 并校正标准误 |
> | **计算求解方式** | 解析闭式解 $\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}$ | 解析广义矩估计 $(\mathbf{X}'\boldsymbol{\Omega}^{-1}\mathbf{X})^{-1}\mathbf{X}'\boldsymbol{\Omega}^{-1}\mathbf{Y}$ | 迭代限制性极大似然（REML）数值优化 |
> | **跨层级交互** | 仅能构建平面交互项（易共线性） | 平面交互项 | 原生支持跨层级随机斜率交互解释 |

> [!method-stack] 方法层级
> - **研究设计** [[Experimental Research|实验研究]]（[[Covariate Adjustment|协变量调整]]回归）、观察性截面调查、[[Regression Discontinuity Design|断点回归]]局部线性拟合（RDD）、[[Difference-in-Differences|双重差分]]双向固定效应（TWFE）。
> - **数据收集** 学业测验考分、调查[[Questionnaire|问卷]]连续量表总分、国家学生普查行政数据库（NPD）。
> - **分析方法** 简单一元线性回归、多元线性回归、[[Analysis of Covariance|协方差分析]]模型（ANCOVA）、[[Interaction Effect|调节效应]]与交互项模型。
> - **辅助技术** 异方差稳健标准误（HC1/HC2/HC3）、聚类稳健标准误（CRSE）、方差膨胀因子（VIF）共线性诊断、Cook 距离异常点诊断。

---

## 研究程序

> [!proc] 通用程序
> 1. **明确模型设定与[[Variable|变量]]界定** 界定[[Dependent Variable|因变量]] $Y$、核心[[Independent Variable|自变量]] $T$（干预状态或政策暴露）以及控制协变量集合 $\mathbf{X}$。
> 2. **探索性数据分析与共线性筛查** 绘制散点图与残差分布图，计算变量方差膨胀因子（VIF），确认不存在严重多重共线性（VIF $< 5$）。
> 3. **参数求解与主效应估计** 基于解析闭式矩阵方程求解回归系数向量 $\hat{\boldsymbol{\beta}}$ 及判定系数 $R^2$。
> 4. **残差诊断与假定检验** 检验残差正态性（Q-Q 图）、同方差性（Breusch-Pagan 检验）及线性函数设定误设检验（Ramsey RESET）。
> 5. **稳健推断与[[Standard Error|标准误]]校正** 若存在异方差则汇报 Huber-White 稳健标准误；若存在班级或学校嵌套，则采用群聚稳健标准误（CRSE）或转入[[Hierarchical Linear Model|多层线性模型]]。

### 量化分析模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 包含 $N$ 个独立观测个体和 $k$ 个解释变量的设计矩阵 $\mathbf{X}$（维度 $N \times (k+1)$）。
> - **核心变量**
>   - 因变量 $Y_i$：[[Pre-test and Post-test|后测]]标准化考试成绩或连续型测量指标。
>   - 处理变量 $T_i$：实验组与对照组分配指示变量（0/1）。
>   - 基线前测 $Y_{\text{pre},i}$：干预实施前采集的同构[[Academic Achievement|学业成绩]]（核心协变量）。
>   - 背景协变量 $\mathbf{Z}_i$：学生性别、特殊教育需求（SEN）、免费校餐资格（FSM）等。
> - **诊断与检验** Breusch-Pagan 异方差检验、Durbin-Watson 自相关检验、Cook's 距离高杠杆异常值剔除敏感性分析。

> [!formula-step] 公式步骤　OLS 矩阵参数估计与几何正交投影
> $$\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}$$
>
> $$\mathbf{e} = \mathbf{Y} - \hat{\mathbf{Y}} = (\mathbf{I} - \mathbf{H})\mathbf{Y}, \quad \text{其中 } \mathbf{H} = \mathbf{X}(\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'$$
>
> **这个公式在做什么** 通过矩阵投影算子将观测因变量向量 $\mathbf{Y}$ 正交分解为线性拟合空间内的预测值 $\hat{\mathbf{Y}}$ 与残差向量 $\mathbf{e}$，解析求解使残差平方和最小的回归系数。
>
> **符号说明**
> - $\mathbf{Y}$：因变量的 $N \times 1$ 维列向量。
> - $\mathbf{X}$：包含常数项与全部解释变量的 $N \times (k+1)$ 维设计矩阵。
> - $\hat{\boldsymbol{\beta}}$：包含截距与各项斜率的 $(k+1) \times 1$ 维参数估计向量。
> - $\mathbf{H}$：帽子矩阵（Hat Matrix），将 $\mathbf{Y}$ 投影到 $\mathbf{X}$ 列空间的对称幂等投影矩阵。
>
> **数学直觉** 最小二乘法的几何本质是将高维空间中的观测点正交投影到由自变量列向量张成的低维超平面上。当且仅当残差向量与该超平面完全正交（即 $\mathbf{X}'\mathbf{e} = \mathbf{0}$）时，残差向量的欧氏长度平方达到全局唯一极小值。
>
> **结果怎么读** 系数 $\hat{\beta}_j$ 表示在控制模型中所有其他协变量保持不变（Ceteris Paribus）的前提下，解释变量 $X_j$ 每增加一个测量单位，因变量 $Y$ 的条件期望平均变动 $\hat{\beta}_j$ 个单位。
>
> **注意事项** 该解析解要求设计矩阵 $\mathbf{X}'\mathbf{X}$ 可逆，即解释变量之间不得存在完全共线性。

> [!formula-step] 公式步骤　试验[[Covariate Adjustment|协变量调整]]回归（[[Analysis of Covariance|ANCOVA]] 模型）
> $$Y_i = \alpha + \tau T_i + \beta_{\text{pre}} Y_{\text{pre},i} + \mathbf{Z}_i' \boldsymbol{\gamma} + \varepsilon_i$$
>
> $$\text{Var}(\hat{\tau}) \approx \frac{(1 - R_{Y|X}^2) \sigma_Y^2}{N \cdot \text{Var}(T)}$$
>
> **这个公式在做什么** 在[[Randomised Controlled Trials|随机对照试验]]中，通过纳入基线前测成绩 $Y_{\text{pre},i}$ 与背景协变量 $\mathbf{Z}_i$，大幅吸收后测结果的未解释变异，压缩处理效应 $\tau$ 的抽样方差。
>
> **符号说明**
> - $\tau$：平均处理效应（ATE）的 OLS 估计值。
> - $\beta_{\text{pre}}$：基线前测成绩对后测成绩的回归系数。
> - $R_{Y|X}^2$：协变量对后测方差的联合解释率。
> - $\sigma_Y^2$：后测成绩的总体原始方差。
>
> **数学直觉** 在教育测验中，基线前测成绩与后测成绩通常具有极高相关性（$r \approx 0.70 \sim 0.85$），可解释后测方差的 50% 到 70%。纳入前测能够将误差方差从 $\sigma_Y^2$ 压缩至 $(1 - r^2)\sigma_Y^2$，使标准误收缩 30% 到 50%，等效于成倍扩充了[[Effective Sample Size|有效样本量]]。
>
> **结果怎么读** $\tau$ 的点估计值即为调整后的干预净效应；在完全[[Random Assignment|随机分配]]下，$\tau$ 与无协变量模型的点估计在渐进意义上趋于一致，但其[[Confidence Interval|置信区间]]大幅缩窄，显著提高检验灵敏度。
>
> **注意事项** 协变量必须在干预发生之前采集，严禁纳入受到干预影响的中间结果变量（Bad Controls），否则会导致内生控制偏误。

> [!software-impl] 软件实现
> - **推荐软件** R, Stata, Python.
> - **核心命令**
>   - R (常规 OLS): `fit <- lm(post_score ~ treat + pre_score + sen + fsm, data = df)`
>   - R (聚类稳健标准误): `fixest::feols(post_score ~ treat + pre_score + sen + fsm, cluster = ~school_id, data = df)`
>   - Stata: `reg post_score treat pre_score sen fsm, vce(cluster school_id)`
>   - Python: `statsmodels.formula.api.ols('post_score ~ treat + pre_score + sen + fsm', data=df).fit(cov_type='cluster', cov_kwds={'groups': df['school_id']})`
> - **实现流程**
>   1. 数据前处理：标准化连续预测变量，设置基准参照组虚拟变量；
>   2. 拟合 OLS 模型：提取系数表、标准误、置信区间与判定系数 $R^2$；
>   3. 稳健推断校正：若数据存在学校聚类，强制启用学校层面聚类稳健协方差估计；
>   4. [[Effect Size Conversion|效应量换算]]：根据全样本合并对照组标准差计算标准化 Hedges' $g$。
> - **报告标准** 报告未标准化系数 $B$、标准误（标明是否为聚类稳健）、标准化系数 $\beta$、$t$ 统计量、$p$ 值、模型 $R^2$ 与调整后 $R^2$。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - [[Randomised Controlled Trials|随机对照试验]]中控制基线[[Pre-test and Post-test|前测]]成绩以提升统计功效的[[Covariate Adjustment|协变量调整]]分析（[[Analysis of Covariance|ANCOVA]]）；
>   - 探索连续型教育[[Dependent Variable|结果变量]]与学生、家庭背景[[Variable|变量]]之间的多元线性相关性；
>   - [[Quasi-Experimental Designs|准实验设计]]中作为[[Propensity Score Matching|倾向得分匹配]]（PSM）前后的回归调整基准或[[Regression Discontinuity Design|断点回归]]（RDD）的局部线性估计器。
> - **谨慎使用**
>   - 存在显著学校或班级嵌套结构的数据（必须外挂聚类稳健[[Standard Error|标准误]]，否则标准误严重失真）；
>   - 解释变量之间存在高多重共线性的情形（导致单项系数方差膨胀、正负号反转）。
> - **不适合使用**
>   - 因变量为离散二分类或有序多分类变量（应转向 Logistic 回归或 Probit 回归）；
>   - 缺乏外生分配机制且存在不可观测混杂因素的横截面[[Causality|因果推断]]（因内生性偏误无法成立因果解释）。

---

## 局限性

> [!method-limits] 方法局限
> - **群聚数据[[Standard Error|标准误]]严重低估** OLS 建立在各观测误差项独立同分布的严苛假定上。教育现场中学生嵌套于学校，同校学生的同质性导致误差项正自相关；直接套用传统 OLS 会将集群共有的变异错误记为独立自由度，导致标准误被大幅低估 30% 至 60%，制造大量虚假的[[Statistical Significance|统计显著性]]（[[Type I and Type II Errors|Type I error]]）。
> - **极端值与杠杆点敏感性** 残差平方和的二次惩罚机制赋予远离拟合平面的极端离群点与高杠杆点过高的权重，单个异常点即可显著扭曲回归斜率。
> - **函数形式误设偏误** 当[[Variable|变量]]间存在明显的非线性关系（如阈值效应或加速递减）时，强行采用线性 OLS 会导致系统性的残差结构化偏误。
> - **补救方式** 面对教育嵌套数据，应采用聚类稳健标准误（CRSE）或直接升级至[[Hierarchical Linear Model|多层线性模型]]（HLM）；面对异常值，可辅以分位数回归（Quantile Regression）或稳健回归算法。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] OLS 聚类稳健[[Standard Error|标准误]] vs [[Hierarchical Linear Model|多层线性模型]]（HLM）
> > 计量经济学派与多层统计学派在处理嵌套试验数据上的方法论论争。
> >
> > - **计量经济学派立场** 倾向于坚持 OLS 回归架构，辅以聚类稳健标准误（Cluster-Robust SE）。他们主张 OLS 算法透明、计算简捷，且即便多层随机效应分布误设，CRSE 依然能够提供渐进无偏的标准误推断，避免了多层复杂参数模型收敛失败的风险。
> > - **教育统计学派立场** 认为单纯靠 CRSE 给 OLS 贴补丁无法替代多层模型。教育系统具有不可约减的层级生态，HLM 不仅能纠正标准误，更能显式分解校内与校际方差、估计[[Intraclass Correlation Coefficient|群内相关系数]]（ICC），并允许探究跨层级[[Interaction Effect|交互作用]]，具有更丰富的实体教育解释力。肖等学者（Xiao et al., 2016）在 NPD 复算中证实，两类模型在[[Effect Size|效应量]]点估计和区间覆盖上存在显著分歧，推动了[[Evidence-Based Education|循证教育]]界对建模标准的审慎反思（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Simple Difference in Means Model]] | 前置/基准方法 | 无协[[Variable\|变量]]时的 OLS 特例，两者构成方差吸收与功效提升的鲜明对比。 |
> | [[Hierarchical Linear Model]] | 进阶模型 | 突破 OLS 独立同分布[[Hypothesis\|假设]]、显式建模层级嵌套结构的现代高级回归模型。 |
> | [[Covariate Adjustment]] | 核心技术 | OLS 在 [[Randomised Controlled Trials\|RCT]] 中作为吸收基线变异、校正偶然不平衡的主要统计载体。 |
> | [[Analysis of Covariance]] | 等价形式 | OLS 纳入类别处理变量与连续[[Pre-test and Post-test\|前测]]变量时的经典[[Analysis of Variance\|方差分析]]表达形式。 |
> | [[Standard Error]] | 推断基础 | OLS 参数推断的核心指标，在嵌套数据中易发生系统性低估。 |
> | [[Statistical Significance]] | 决策指标 | OLS 模型设定与标准误校正直接左右的统计显著性结论。 |
> | [[Model Dependency]] | 风险现象 | 解释了为什么 OLS 与简单均值模型、多层模型之间的选择会引发[[Effect Size\|效应量]]漂移。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 综述了齐·肖（ZhiMin Xiao）、[[Steve Higgins|史蒂夫·希金斯]]（Steve Higgins）与阿迪特·卡西姆（Adetayo Kasim）利用英格兰 NPD 数据开展的 17 项试验复算，证实了基线[[Pre-test and Post-test|前测]] OLS 回归在方差吸收与功效提升方面的核心价值，同时也警示了未校正聚类结构的 OLS 会诱发严重的[[Standard Error|标准误]]低估与伪显著性，促成了英国试验统计指南的确立。
