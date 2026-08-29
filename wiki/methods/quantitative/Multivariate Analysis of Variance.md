---
title: Multivariate Analysis of Variance
aliases:
  - 多变量方差分析
  - 多元方差分析
  - MANOVA
  - Multivariate ANOVA
  - 多因变量方差分析
summary: "用于同时检验一个或多个分类自变量对两个或多个相互关联的连续因变量产生显著主效应与交互效应的多元统计推断方法，通过构建因变量线性组合最大化组间与组内方差之比，在严格控制族系一类错误率（Familywise Type I Error）的同时揭示因变量系统的多维协同变异结构。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 28
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/inferential
  - statistics/multivariate
  - research-design/experimental
  - research-design/comparative
related_concepts:
  - "[[Variable]]"
  - "[[Metainferences]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Interaction Effect]]"
  - "[[Effect Size]]"
  - "[[Type I and Type II Errors]]"
  - "[[Epistemology]]"
  - "[[Epistemological Beliefs]]"
  - "[[Hypothesis]]"
  - "[[Construct Validity]]"
  - "[[Construct]]"
  - "[[Sample Size Determination]]"
  - "[[Research Literacy]]"
  - "[[Reliability]]"
  - "[[Academic Achievement]]"
related_theories:
  - "[[Classical Test Theory]]"
related_methods:
  - "[[Analysis of Variance]]"
  - "[[Random Assignment]]"
  - "[[Observation Method]]"
  - "[[Causal Modeling]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Factorial Design]]"
  - "[[Analysis of Covariance]]"
  - "[[Confirmatory Factor Analysis]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[CREATES Project]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
  - "[[Argument_Lodewyk_2007_EP]]"
confidence: high
status: draft
created: 2026-08-29
updated: 2026-08-29
---

# Multivariate Analysis of Variance

---

## 定义

> [!def] 方法定义
> **多[[Variable|变量]][[Analysis of Variance|方差分析]]（Multivariate Analysis of Variance, MANOVA）** 是一种拓展单变量[[Analysis of Variance|方差分析]]（ANOVA）的多[[Metainferences|元推断]]统计方法。它用于在一个或多个分类[[Independent Variable|自变量]]（因子）的设计下，同时评估多个连续[[Dependent Variable|因变量]]构成的向量均值在各组间是否存在显著差异。通过将多个相关因变量线性组合为一个或多个综合潜变量，MANOVA 能够在最大化组间变异与组内变异比率的同时，有效控制多重检验导致的族系一类错误率膨胀，并捕捉单个因变量无法单独显现的多维交互结构。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, pp. 315–317)]]

> [!method-scope] 方法范围
> - **研究对象** 包含 1 个或多个分类自变量（如教学干预组别、年级、教师科研经历）以及 2 个或以上具有理论相关性的连续数值型因变量（如多维学习动机、多维度素养得分、不同认知层次成绩）。
> - **问题类型** 组间多维差异检验、多因子主效应与[[Interaction Effect|交互效应]]识别、综合干预的多维效果评价。
> - **分析单位** 个体被试（学生、教师、管理者）或聚合组织单元（班级、学校、学区）。
> - **输出形式** 多元检验统计量（Wilks' $\Lambda$、Pillai's Trace、Hotelling-Lawley Trace、Roy's Largest Root）、$F$ 近似值与自由度、$p$ 显著性水平、多元偏[[Effect Size|效应量]]（Partial $\eta^2$）、各分维度单变量 ANOVA 后续检验及事后多重比较结果。

> [!citation-card]- 关键定义
> 当研究者拥有两个或更多因变量且这些变量彼此相关时，多变量方差分析（MANOVA）是适宜的分析技术。它不是孤立地对每个因变量进行单独的 ANOVA 检验，而是检验由所有因变量组合而成的整体系统是否在自变量各组间存在差异，从而保护研究免受一类错误率累积的威胁。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, p. 316)]]
>
> *Multivariate analysis of variance (MANOVA) is an extension of ANOVA used when the researcher investigates the effect of one or more independent variables on two or more dependent variables. Rather than conducting multiple univariate ANOVAs, which inflate the familywise [[Type I and Type II Errors|Type I error]] rate, MANOVA [[CREATES Project|CREATES]] a linear combination of dependent variables to test for overall group differences.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 秉持系统论与整体主义的量化认识论，认为复杂心理与教育现象（如学业素养、[[Epistemological Beliefs|认识论信念]]、职业倦怠）是由多个相互关联的子维度共同表征的有机系统，单维度的孤立测量容易割裂[[Variable|变量]]间的内在关联。
> - **研究者角色** 研究者需基于严谨的实质性理论预先确定[[Dependent Variable|因变量]]集合，避免盲目堆砌不相关的因变量；在模型设定、前置[[Hypothesis|假设]]诊断（多元正态性、协方差齐性）以及事后分解路径中行使审慎的统计判断。
> - **有效性标准** 核心致力于保障统计结论效度（有效控制 $\alpha$ 错误膨胀并提升统计功效）与[[Construct Validity|构念效度]]（通过多维指标联合表征复杂[[Construct|构念]]）。
> - **不声称回答的问题** MANOVA 本身属于观察或实验组间均值比较技术，**不能仅凭多元显著性直接推断因果机制（在非[[Random Assignment|随机分配]]的[[Observation Method|观察研究]]中仍受选择偏差制约）**；同时不能替代结构方程模型（[[Causal Modeling|SEM]]）对因变量间双向因果路径与测量误差的直接建模。

> [!method-stack] 方法层级
> - **研究设计** 析因实验设计（Factorial Experiments）、[[Quasi-Experimental Designs|准实验设计]]（[[Quasi-Experimental Designs|QED]]）、横断面比较调查（Cross-sectional Comparative Surveys）。
> - **数据收集** 结构化标准化量表（如包含多个子维度的测评工具）、实验任务多维反应时与准确率数据、学业多科目成绩档案。
> - **分析方法**
>   - 多元假设检验（MANOVA）
>   - 协方差矩阵分解（SSCP 矩阵计算）
>   - 事后单变量[[Analysis of Variance|方差分析]]（Follow-up Univariate ANOVAs with Bonferroni Correction）
>   - 描述性判别分析（Descriptive Discriminant Analysis）
> - **辅助技术** Mardia 多元正态检验、Box's M 协方差同质性检验、Levene 方差齐性检验、多元偏 $\eta^2$ 计算。

---

## 研究程序与数学原理

### 量化分析与公式推导

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** $N$ 个观测样本，$k$ 个[[Independent Variable|自变量]]处理组（或多因子交叉单元），每个被试包含 $p$ 个连续[[Dependent Variable|因变量]]向量 $\mathbf{y}_{ij} = [y_{ij1}, y_{ij2}, \dots, y_{ijp}]^T$。
> - **样本与单位** [[Sample Size Determination|样本量]]要求各单元格样本数大于因变量个数（推荐每格 $n > 20$ 或 $n \ge 3p$ 以保证统计检验力）。
> - **变量定义**
>   - 自变量（Factor $A, B$）：分类变量（如实验组 vs 对照组；期刊追踪 是 vs 否；开展科研 是 vs 否）。
>   - 因变量向量（$\mathbf{Y}$）：$p$ 个具有理论内在关联的连续变量。
> - **模型架构** 矩阵形式的多元线性模型：
>   $$\mathbf{Y} = \mathbf{X}\mathbf{B} + \mathbf{E}$$
> - **诊断与检验** 多元异常值（Mahalanobis 距离）、多元正态性、方差-协方差矩阵齐性（Box's M）、因变量间适度相关（$r \in [0.30, 0.70]$，避免多重共线性）。

> [!formula-step] 公式步骤一　离差平方和与交叉乘积矩阵分解（SSCP Decomposition）
> $$\mathbf{T} = \mathbf{H} + \mathbf{E}$$
>
> **这个公式在做什么** 将多元总离差平方和与交叉乘积矩阵（$\mathbf{T}$，Total SSCP）解构为组间[[Hypothesis|假设]]矩阵（$\mathbf{H}$，Hypothesis/Between SSCP）与组内误差矩阵（$\mathbf{E}$，Error/Within SSCP）。
>
> **符号说明**
> - $\mathbf{T}$：$p \times p$ 维总变异矩阵，对角线为各因变量的总方差，非对角线为因变量间的总协方差。
> - $\mathbf{H}$：$p \times p$ 维组间效应矩阵，$\mathbf{H} = \sum_{j=1}^{k} n_j (\mathbf{\bar{y}}_j - \mathbf{\bar{y}})(\mathbf{\bar{y}}_j - \mathbf{\bar{y}})^T$。
> - $\mathbf{E}$：$p \times p$ 维组内误差矩阵，$\mathbf{E} = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (\mathbf{y}_{ij} - \mathbf{\bar{y}}_j)(\mathbf{y}_{ij} - \mathbf{\bar{y}}_j)^T$。
>
> **数学直觉** 对应单变量 [[Analysis of Variance|ANOVA]] 的标量分解 $SS_{total} = SS_{between} + SS_{within}$，但在多维空间中，不仅分解各个因变量自身的方差，同时精确分解因变量两两之间的协方差。
>
> **结果怎么读** 当 $\mathbf{H}$ 相对 $\mathbf{E}$ 越大，意味着自变量分组能够解释越多的因变量联合空间变异。

> [!formula-step] 公式步骤二　四大多元检验统计量构建（Multivariate Test Statistics）
> $$\mathbf{H}\mathbf{E}^{-1}\mathbf{v}_i = \lambda_i \mathbf{v}_i \quad (i = 1, \dots, s; \ s = \min(k-1, p))$$
>
> **这个公式在做什么** 通过求解矩阵 $\mathbf{H}\mathbf{E}^{-1}$ 的特征根 $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_s$，构建综合反映多维组间差异的统计量。
>
> **核心四大统计量**
> 1. **Wilks' Lambda ($\Lambda$)**
>    $$\Lambda = \frac{|\mathbf{E}|}{|\mathbf{H} + \mathbf{E}|} = \prod_{i=1}^{s} \frac{1}{1 + \lambda_i}$$
>    似然比检验准则，取值范围 $[0, 1]$，值越接近 0 表明组间差异越显著，是最通用的标准统计量。
> 2. **Pillai's Trace ($V$)**
>    $$V = \text{tr}(\mathbf{H}(\mathbf{H} + \mathbf{E})^{-1}) = \sum_{i=1}^{s} \frac{\lambda_i}{1 + \lambda_i}$$
>    取值范围 $[0, s]$，对违背多元正态性和协方差齐性假定最为稳健（Robust），小样本或异方差时首选。
> 3. **Hotelling-Lawley Trace ($T$)**
>    $$T = \text{tr}(\mathbf{H}\mathbf{E}^{-1}) = \sum_{i=1}^{s} \lambda_i$$
>    直接度量特征根之和，在大样本下功效逼近 Wilks' $\Lambda$。
> 4. **Roy's Largest Root ($\theta$)**
>    $$\theta = \frac{\lambda_1}{1 + \lambda_1}$$
>    仅基于第一主特征根，在组间差异仅存在于单一维度时具有最高的统计检验力。

> [!formula-step] 公式步骤三　多元偏[[Effect Size|效应量]]计算（Multivariate Partial $\eta^2$）
> $$\eta_p^2 = 1 - \Lambda^{1/s}$$
>
> **这个公式在做什么** 量化自变量对因变量向量系统整体联合变异的解释比例（效应量）。
>
> **符号说明**
> - $\eta_p^2$：多元偏 Eta 平方效应量。
> - $\Lambda$：Wilks' Lambda 统计量。
> - $s$：有效特征根数 $s = \min(k-1, p)$。
>
> **结果怎么读** 按照 Cohen 经验标准，$\eta_p^2 = 0.01$ 为小效应，$\eta_p^2 = 0.06$ 为中等效应，$\eta_p^2 = 0.14$ 为大效应。

---

## 分析流程与决策路径

> [!proc] MANOVA 标准操作与事后检验全流程
> ```mermaid
> flowchart TD
>   A["研究设计：确定因子（IVs）与多维因变量（DVs）"] --> B["数据前提诊断：缺失值 / 多元异常值 / 多元正态性 / 协方差齐性"]
>   B --> C{"假设检验是否达标？"}
>   C --"协方差不齐 / 小样本"--> D["选用稳健统计量：Pillai's Trace"]
>   C --"基本满足多元正态与齐性"--> E["选用经典统计量：Wilks' Lambda"]
>   D --> F["执行多元综合检验（MANOVA Omnibus Test）"]
>   E --> F
>   F --> G{"多元检验是否显著（p < .05）？"}
>   G --"否"--> H["终止后续检验，接受虚无假设（无多维组间差异）"]
>   G --"是"--> I["事后两步分解检验"]
>   I --> J["1. 单变量 ANOVA 检验（采用 Bonferroni 调整 α 阈值）"]
>   I --> K["2. 描述性判别分析（识别区分组别的核心因变量维度）"]
>   J --> L["各分维度事后两两多重比较（Tukey HSD / Games-Howell）"]
>   L --> M["报告多元与一元效应量、参数估计与教育实践启示"]
>   K --> M
> ```

> [!software-impl] 软件实现与报告规范
> - **R 语言**
>   ```R
>   # 模型估计
>   fit <- manova(cbind(DV1, DV2, DV3, DV4) ~ FactorA * FactorB, data = mydata)
>   # 多元检验报告
>   summary(fit, test = "Wilks")
>   summary(fit, test = "Pillai")
>   # 事后单变量分解
>   summary.aov(fit)
>   ```
> - **Python (`statsmodels`)**
>   ```python
>   from statsmodels.multivariate.manova import MANOVA
>   ma = MANOVA.from_formula('DV1 + DV2 + DV3 + DV4 ~ FactorA * FactorB', data=df)
>   print(ma.mv_test())
>   ```
> - **SPSS**
>   `Analyze -> General Linear Model -> Multivariate`，勾选 `Descriptive statistics`、`Estimates of effect size`、`Homogeneity tests` 及 `Post Hoc`。
> - **规范报告格式**
>   应当完整汇报统计量名称、近似 $F$ 值、[[Hypothesis|假设]]自由度与误差自由度、$p$ 值以及偏 $\eta^2$。例：*“多[[Variable|变量]][[Analysis of Variance|方差分析]]表明，教师开展科研的主效应显著，$F(4, 251) = 3.73, p = .006, \text{Wilks' } \Lambda = .944, \text{partial } \eta^2 = .056$。”*

---

## 适用场景与对比

> [!method-fit] 适用判断
> - **适合使用**
>   1. **多维度[[Construct|构念]]评估** 当[[Dependent Variable|因变量]]是同一心理构念（如[[Research Literacy|研究素养]]的意识、态度、技能、使用）或学习成果的多个紧密关联子维度时。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 12)]]
>   2. **控制整体一类错误** 避免针对 $p$ 个因[[Variable|变量]]分别做独立 [[Analysis of Variance|ANOVA]] 导致名义假阳性率从 $\alpha$ 急剧膨胀为 $1 - (1-\alpha)^p$。
>   3. **发现潜在协同效应** 两个组别在每个单项因变量上的微弱差异均未达显著性，但其在联合空间中的向量距离极其显著。[[Argument_Lodewyk_2007_EP|(Lodewyk, 2007, p. 318)]]
> - **谨慎使用**
>   - 因变量之间几乎不相关（$r < .20$，此时联合检验不增加统计效能，直接做独立 ANOVA 即可）。
>   - 因变量之间极度高度相关（$r > .85$，存在多重共线性，提示指标冗余，应先进行因子降维）。
> - **不适合使用**
>   - 因变量为分类或名义变量（应采用多项 Logistic 回归或对数线性模型）。
>   - 单个单元格[[Sample Size Determination|样本量]]小于因变量个数（自由度不足导致奇异矩阵崩溃）。

---

## 局限性与风险防范

> [!method-limits] 方法局限
> - **偏误与稳健性风险**
>   - **Box's M 检验极度敏感** Box's M 对轻微偏离多元正态极度敏感（容易假报警），在[[Sample Size Determination|样本量]]较大且各组样本量接近相等时（最大组/最小组 $< 1.5$），即使 Box's M 显著，Pillai's Trace 仍表现稳健。
>   - **一元事后检验的掩蔽风险** 单纯依靠事后单[[Variable|变量]] [[Analysis of Variance|ANOVA]] 可能丢失变量间的协方差信息，推荐结合判别分析（Discriminant Analysis）理解多维分离机制。
> - **常见误用**
>   - **变量堆砌（Data Fishing）** 将所有测量到的变量不加理论筛选地全部放入 MANOVA 模型中，导致自由度大量损耗与检验力急剧下降。
>   - **忽略单元格不平衡** 在非等样本量[[Factorial Design|析因设计]]中，需指定 Type III 离差平方和以避免主效应与[[Interaction Effect|交互效应]]的混淆。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Analysis of Variance]] | 基础方法 | MANOVA 的单变量特例（$p=1$），MANOVA 多元检验显著后的主要分解工具。 |
> | [[Analysis of Covariance]] | 拓展方法 | 引入连续协[[Variable\|变量]]进行控制的多元协方差分析（MANCOVA）的单变量对应物。 |
> | 判别分析（Discriminant Analysis） | 对偶方法 | MANOVA 关注“组别（IV）如何影响变量组合（DV）”，判别分析关注“变量组合如何反向预测组别归属”。 |
> | [[Confirmatory Factor Analysis\|结构方程模型（SEM）]] | 进阶替代 | 当[[Dependent Variable\|因变量]]包含测量误差或需要同时拟合复杂中介/调节链条时的现代结构化替代框架。 |
> | [[Classical Test Theory]] | 测量理论 | 为多维度量表的[[Reliability\|信度]]与因变量相关结构提供心理测量学理论基础。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 在教师[[Research Literacy|研究素养]]研究中建立 2×2 MANOVA 模型，同时检验期刊追踪与亲身做研究对教师研究素养 4 个分维度的独立赋能主效应与[[Interaction Effect|交互效应]]。
> - [[Argument_Lodewyk_2007_EP|Lodewyk (2007)]] — 在高中生科学学习研究中运用 MANOVA 检验不同[[Academic Achievement|学业成就]]组（高/中/低）与性别在固定能力观、知识简单性等[[Epistemological Beliefs|认识论信念]]三因子上的多维显著差异。
> - [[Argument_Creswell_2022_SAGE|Creswell & Guetterman (2022, Ch. 11)]] — 详细阐述量化实验与组间比较设计中 [[Analysis of Variance|ANOVA]]、[[Analysis of Covariance|ANCOVA]] 与 MANOVA 的方法选择矩阵及错误率控制机制。
