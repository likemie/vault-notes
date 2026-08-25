---
title: Meta-regression
aliases:
  - 元回归
  - meta-regression analysis
  - 元回归分析
summary: "在元分析框架下，通过加权回归检验研究特征与连续型调节变量对效应量异质性的解释力，输出回归系数、模型显著性及解释方差比例"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 49
method_related_level: 5
method_related_stars: "⭐⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/statistical
  - meta-analysis
  - moderator-analysis
  - quantitative-synthesis
related_concepts:
  - "[[Effect Size]]"
  - "[[Dependent Variable]]"
  - "[[Variable]]"
  - "[[Independent Variable]]"
  - "[[Heterogeneity]]"
  - "[[Interaction Effect]]"
  - "[[Document]]"
  - "[[Reliability]]"
  - "[[Standard Error]]"
  - "[[Confidence Interval]]"
  - "[[Epistemology]]"
  - "[[Positivism]]"
  - "[[Sampling Error]]"
  - "[[Ecological Fallacy]]"
  - "[[Construct]]"
  - "[[Hypothesis]]"
  - "[[Between-Study Variance]]"
  - "[[Publication Bias]]"
  - "[[Graphic Organizer]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Epistemic Cognition]]"
  - "[[Academic Achievement]]"
  - "[[Questionnaire]]"
  - "[[Internal Consistency]]"
  - "[[Sample Size Determination]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Preregistration]]"
  - "[[Analytic Framework]]"
  - "[[Creativity]]"
  - "[[Critical Thinking]]"
related_arguments:
  - "[[Argument_Greene_2018_JEP]]"
  - "[[Argument_Lei_Ding_Chiu_2026_ERR]]"
  - "[[Argument_Gungor_2026_CP]]"
  - "[[Argument_Unal_2026_JECR]]"
  - "[[Argument_Park_2026_TSC]]"
related_theories:
  - "[[Classical Test Theory]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Multiple Regression]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Second-Order Meta-Regression]]"
  - "[[Pairwise Wald Tests]]"
  - "[[Correlated and Hierarchical Effects Model]]"
  - "[[Robust Variance Estimation]]"
  - "[[Effect Size Conversion]]"
  - "[[Meta-meta-analysis]]"
  - "[[Moderator Analysis]]"
  - "[[Analysis of Variance]]"
  - "[[Three-Level Meta-Analysis]]"
status: active
confidence: high
created: 2026-08-19
updated: 2026-08-25
---

# Meta-regression

---

## 定义

> [!def] 方法定义
> 元回归（Meta-regression）是在[[Meta-analysis|元分析]]框架下，以各纳入初级研究的[[Effect Size|效应量]]为[[Dependent Variable|因变量]]、研究层面的特征（调节[[Variable|变量]]）为[[Independent Variable|自变量]]，通过加权回归分析检验调节变量对效应量[[Heterogeneity|异质性]]解释力的统计方法体系。它将元分析的[[Interaction Effect|调节效应]]检验从离散分类子组比较推广到连续数值变量及多元复合模型，依据各研究的抽样精度（抽样方差倒数）与研究间真实异质性方差进行广义[[Inverse-Variance Weighting|逆方差加权]]估计。[[Argument_Greene_2018_JEP|(Greene et al., 2018, pp. 1098–1102)]]; [[Argument_Lei_Ding_Chiu_2026_ERR|(Lei et al., 2026, pp. 5–6, 10–11)]]

> [!method-scope] 方法范围
> - **研究对象** 跨原始研究的效应量矩阵及其对应的样本特征、测量工具信效度、干预参数、宏观社会经济背景及[[Document|文献]]发表年份等协变量。
> - **问题类型** 机制解释、异质性来源探索与因果调节识别：哪些连续型特征（如干预时长、量表[[Reliability|信度]]、人均 GDP）或离散特征系统性预测效应量大小？
> - **分析单位** 独立实证研究（Study）或独立样本（Sample），每条数据对应一项纳入元分析的效应量估计值。
> - **输出形式** 回归截距 $\beta_0$、斜率系数 $\beta_j$、[[Standard Error|标准误]]、95% [[Confidence Interval|置信区间]]（CI）、模型整体检验量 $F$ 或 $Q_{\text{model}}$、残余异质性 $\tau^2_{\text{residual}}$ 及拟 $R^2$ 解释比例。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** [[Positivism|实证主义]]后设整合：将单项实证研究视为带有[[Sampling Error|抽样误差]]与情境约束的数据点，通过跨研究的[[Multiple Regression|多元回归]]建模提取超越单一情境的稳健调节规律。
> - **研究者角色** 预先依据实质理论设定候选调节[[Variable|变量]]，对[[Document|文献]]纳入标准、[[Effect Size|效应量]]提取口径和变量[[Coding in Qualitative Research|编码]][[Reliability|信度]]负责，避免无理论指导的事后逐步数据挖掘。
> - **有效性标准** 统计结论效度（检验功效高度依赖纳入研究数 $k$，经验要求每个[[Independent Variable|自变量]]至少对应 10 项独立研究）与模型设定准确性。
> - **不声称回答的问题** 元回归揭示的是研究层面的生态关联（Ecological Association），不能直接推断个体层面的微观因果中介，不可犯[[Ecological Fallacy|生态谬误]]。

> [!contrast-table] 经典一阶元回归 vs [[Second-Order Meta-Regression|二阶元回归]] vs 分类亚组检验
> | 比较维度 | 经典一阶元回归（[[Meta-regression]]） | 二阶元回归（[[Second-Order Meta-Regression]]） | 分类亚组检验与[[Pairwise Wald Tests\|成对 Wald 检验]] |
> |---|---|---|---|
> | **分析单位** | 原始实证研究（Primary Studies） | 一阶[[Meta-analysis\|元分析]]汇总效应量集群（Meta-Analysis Clusters） | 原始实证研究按属性划分的离散子群 |
> | **自变量形态** | 连续型变量（如信度、人均 GDP、年份）或哑变量 | 宏观[[Construct\|理论构念]]与跨领域特征指标 | 离散分类变量（如学段、干预形态、学科） |
> | **依赖性处理** | 假定各研究抽样独立或采用简单多水平结构 | 采用 [[Correlated and Hierarchical Effects Model\|CHE]] 块对角协方差与 [[Robust Variance Estimation\|RVE]] 经验三明治估计 | 假定各亚组效应量独立或分层建模 |
> | **统计推断核心** | 估计连续斜率 $\beta_1$ 与模型 $F / Q_M$ 检验 | 跨越数千项研究检验全领域理论边界 | 检验组间总异质性 $Q_{between}$ 与两两 Wald 级差 |
> | **典型代表应用** | [[Argument_Greene_2018_JEP\|Greene et al. (2018)]]; [[Argument_Lei_Ding_Chiu_2026_ERR\|Lei et al. (2026)]] | [[Argument_Gungor_2026_CP\|Güngör et al. (2026)]]; [[Argument_Unal_2026_JECR\|Ünal et al. (2026)]] | [[Argument_Lei_Ding_Chiu_2026_ERR\|Lei et al. (2026)]] 工具与学段级差比较 |

---

## 研究程序

> [!proc] 通用程序
> 1. 明确理论[[Hypothesis|假设]]：预设哪些连续型或分类型研究特征（如量表[[Reliability|信度]]、人均 GDP、发表年份、干预时长）可能系统性[[Interaction Effect|调节效应]]量大小。
> 2. 系统检索与[[Document|文献]]筛选，提取各研究的[[Effect Size|效应量]]指标（如 Hedges' $g$、Pearson $r$、Fisher's $z$）及其抽样方差 $v_i$，并对调节[[Variable|变量]]进行标准化[[Coding in Qualitative Research|编码]]。
> 3. 计算合并效应与[[Heterogeneity|异质性]]检验，评估总异质性 $Q_{\text{total}}$ 与[[Between-Study Variance|研究间方差]] $\tau^2$ 是否显著，确立开展元回归的统计前提。
> 4. 构建加权随机效应元回归模型，估计截距 $\beta_0$、偏回归系数 $\beta_j$、[[Confidence Interval|置信区间]]及模型解释方差比例 $R^2_{\text{analog}}$。
> 5. 进行模型诊断：检验残余异质性 $Q_{\text{residual}}$、多重共线性、高杠杆异常点及[[Publication Bias|发表偏倚]]影响。

### 量化方法模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 研究层面汇总数据矩阵（每行代表一个独立效应量，列包含效应量点估计、抽样方差及若干协变量）。
> - **样本与单位** 纳入研究数 $k$；经验法则建议每个调节变量至少需要 10 项独立研究支撑（$k/p \ge 10$）。
> - **变量或指标** 
>   - [[Dependent Variable|因变量]]：效应量估计值 $\hat{\theta}_i$（如 Hedges' $g$、Pearson $r$ 或 Fisher's $z$）。
>   - [[Independent Variable|自变量]]：研究特征连续变量（如人均 GDP_Z 分数、发表年份、量表信度）或分类虚拟变量。
>   - 权重：加权逆方差 $w_i^* = 1 / (v_i + \tau^2_{\text{residual}})$。
> - **模型或统计量** 随机效应元回归模型（Random-Effects Meta-Regression）与混合效应模型。
> - **诊断与检验** $F$ 检验 / $Q_{\text{model}}$（模型联合显著性）、$Q_{\text{residual}}$（残差异质性检验）、拟 $R^2$ 解释度。

> [!formula-step] 公式步骤　基础随机效应多元元回归模型
> $$\hat{\theta}_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} + u_i + \epsilon_i$$
>
> **这个公式在做什么** 以第 $i$ 项研究的效应量估计值 $\hat{\theta}_i$ 为因变量，通过 $p$ 个研究特征调节变量 $x_{i1}, \dots, x_{ip}$ 预测效应量大小，并同时分解研究间真实异质性误差 $u_i$ 与研究内[[Sampling Error|抽样误差]] $\epsilon_i$。
>
> **符号说明**
> - $\hat{\theta}_i$ 第 $i$ 项研究观察到的效应量估计值（如 $g_i$ 或 $r_i$）
> - $\beta_0$ 回归截距，代表所有协变量取值为 0 时的基线效应量
> - $\beta_j$ 第 $j$ 个调节变量的偏回归系数，表示其他特征固定时该变量每增加 1 个单位时效应量的预期变化量
> - $x_{ij}$ 第 $i$ 项研究在协变量 $j$ 上的取值
> - $u_i$ 研究间随机效应残差，$u_i \sim N(0, \tau^2_{\text{residual}})$
> - $\epsilon_i$ 研究内抽样误差，$\epsilon_i \sim N(0, v_i)$，其中 $v_i$ 为抽样方差
>
> **数学直觉** 普通最小二乘法假定所有观测值具有同方差，而元回归中大样本研究的抽样误差远小于小样本研究，因此必须以各研究的综合方差倒数（$1/(v_i + \tau^2)$）为权重进行加权最小二乘估计。
>
> **结果怎么读** $\beta_j > 0$ 且置信区间不包含 0 时，表明该特征与效应量显著正相关；$\beta_j < 0$ 表明负向调节；模型 $F$ 检验或 $Q_{\text{model}}$ 检验判定模型整体是否显著。
>
> **注意事项** 若调节变量过多而研究量 $k$ 较小，模型极易产生过拟合与假阳性结果；分类变量需转换为哑变量（Dummy variables）处理。

> [!formula-step] 公式步骤　[[Argument_Lei_Ding_Chiu_2026_ERR|Lei et al. (2026)]] 宏观环境变量与时间趋势元回归
> $$\hat{g}_i = \beta_0 + \beta_1 \cdot \text{GDP\_Z}_i + \beta_2 \cdot \text{PublishYear}_i + u_i + \epsilon_i$$
>
> **这个公式在做什么** 以[[Graphic Organizer|图形组织器]]干预的效应量 Hedges' $g$ 为因变量，以纳入国家的人均国内生产总值 Z 分数（$\text{GDP\_Z}$）与文献发表年份（$\text{PublishYear}$）为连续型协变量，检验宏观经济技术投入与教学法演进对微观干预成效的跨层调节效应。
>
> **符号说明**
> - $\hat{g}_i$ 第 $i$ 项研究报告的图形组织器对[[Higher-Order Thinking Skills|高阶思维]]干预效应量 Hedges' $g$
> - $\text{GDP\_Z}_i$ 该研究所在国家世界银行人均国内生产总值的标准化 Z 分数
> - $\text{PublishYear}_i$ 该文献的发表年份
> - $\beta_1, \beta_2$ 对应的元回归斜率系数（Lei et al. 报告人均 GDP 斜率 $\beta_1 = 0.197, p < .01$；发表年份斜率 $\beta_1 = 0.032, p < .05$）
>
> **数学直觉** 将宏观国家经济数据与微观教育干预效应量并轨建模，量化揭示了高收入国家因拥有更先进的可视化数字工具与更高水平的师资培训，显著放大了图形组织器的教学赋能效应。
>
> **结果怎么读** $\beta_1 = 0.197$ 表明人均 GDP 每提升 1 个标准差，图形组织器对高阶思维的干预效应量增加 0.197；$\beta_2 = 0.032$ 表明随着发表年份推移，教学技术发展使干预效应稳步递增。[[Argument_Lei_Ding_Chiu_2026_ERR|(Lei et al., 2026, pp. 10–11)]]
>
> **注意事项** 跨国环境变量属于宏观生态数据，解释时需明确其代表的是国家教育技术与资本环境红利，不可直接推论至微观家庭贫富差距对个体学习的影响。

> [!formula-step] 公式步骤　[[Argument_Greene_2018_JEP|Greene et al. (2018)]] 测量信度衰减机制元回归
> $$\hat{r}_i = \beta_0 + \beta_1 \cdot \text{Reliability}_i + \epsilon_i$$
>
> **这个公式在做什么** 以各研究报告的[[Epistemic Cognition|认识论认知]]与[[Academic Achievement|学业成就]]相关系数 $r$ 为因变量，以[[Questionnaire|问卷]][[Internal Consistency|内部一致性]]信度（Cronbach's $\alpha$）为预测变量，检验测量误差对可观测效应量的系统性衰减机制。
>
> **符号说明**
> - $\hat{r}_i$ 第 $i$ 项研究报告的相关系数
> - $\text{Reliability}_i$ [[Epistemology|认识论]]问卷的内部一致性信度系数（0 到 1）
> - $\beta_1$ 信度元回归斜率估计值（Greene et al. 报告为 $b = .300, p < .001$）
>
> **数学直觉** [[Classical Test Theory|经典测量理论]]表明测量误差会导致相关系数发生统计衰减。元回归实证验证了这一规律：问卷信度越高，可观测到的效应量越大；若信度为 0，效应量归零；若信度达 1.0，理论真实相关性可达 $r = .300$。
>
> **结果怎么读** 证实了方法学决定论：大量低信度自陈问卷直接压低了以往文献的效应量，造成了认识论认知对学业成绩无影响的虚假印象。[[Argument_Greene_2018_JEP|(Greene et al., 2018, p. 1102)]]
>
> **注意事项** 提示研究者在解读认知变量效应时必须控制测量工具的信度基线。

> [!software-impl] 软件实现
> - **推荐软件** R（`metafor` 包）、Comprehensive [[Meta-analysis]] (CMA)、Stata（`meta regress` 命令）、Python（`statsmodels`）。
> - **核心包或命令**
>   - R `metafor` 连续与分类多变量元回归：
>     ```r
>     library(metafor)
>     # 拟合包含人均 GDP 与发表年份的随机效应元回归模型
>     res_mod <- rma(yi = g_val, vi = g_var, mods = ~ gdp_z + publish_year, data = meta_data, method = "REML")
>     summary(res_mod)
>     ```
> - **实现流程** 数据清洗 -> [[Effect Size Conversion|效应量转换]]与方差提取 -> 连续调节变量标准化与中心化 -> REML 模型估计 -> 残差诊断与气泡图（Bubble Plot）绘制。
> - **报告标准** 完整报告[[Sample Size Determination|样本量]] $k$、截距与斜率系数 $B$、[[Standard Error|标准误]] SE、95% CI、$p$ 值、模型 $F$ 检验量、残差异质性 $\tau^2_{\text{residual}}$ 及解释方差比例 $R^2$。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 纳入[[Meta-analysis|元分析]]的研究间存在显著[[Heterogeneity|异质性]]（$I^2 > 25\%$ 或 $Q$ 检验 $p < .05$），且研究者希望在连续维度上检验假设的调节变量（如样本年龄、干预时长、国家人均 GDP、发表年份、量表信度）。[[Argument_Greene_2018_JEP|(Greene et al., 2018)]]; [[Argument_Lei_Ding_Chiu_2026_ERR|(Lei et al., 2026)]]
> - **谨慎使用** 纳入研究数量较少（$k < 10$）时模型自由度不足；调节变量间存在高度多重共线性时系数难以分离；探索性质的元回归需明确声明。
> - **不适合使用** 旨在推断个体层面的微观因果中介机制；[[Primary and Secondary Documents|原始文献]]中关键调节[[Variable|变量]]大面积缺失且无法补齐。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** [[Ecological Fallacy|生态谬误]]（研究层面的[[Variable|变量]]关联无法直接推导至学生个体）；混杂变量遗漏（由于 $k$ 有限无法同时控制所有潜在混杂因素）；[[Publication Bias|发表偏倚]]与小样本效应干扰。
> - **适用边界** 需要充足的独立研究数量；模型结论受制于原始研究报告的质量（Garbage in, garbage out）。
> - **误用风险** 在高维调节变量空间中进行无理论指导的逐步回归，导致假阳性率激增。
> - **补救方式** [[Preregistration|预注册]]调节[[Hypothesis|假设]]；采用置换检验（Permutation test）校正小样本推断；结合散点气泡图直观展示[[Effect Size|效应量]]与调节变量的关系。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Meta-analysis]] | 前置方法 | 元回归依附于元[[Analytic Framework\|分析框架]]，以元分析提取的[[Effect Size\|效应量]]与抽样方差作为建模输入。 |
> | [[Pairwise Wald Tests]] | 互补方法 | 元回归处理连续型协[[Variable\|变量]]与多变量线性趋势，成对 Wald 检验处理离散多亚组的事后成对级差推断。 |
> | [[Second-Order Meta-Regression]] | 进阶方法 | 在[[Meta-meta-analysis\|二阶元分析]]多层嵌套与文献重叠数据下，运用 [[Correlated and Hierarchical Effects Model\|CHE]] 与 [[Robust Variance Estimation\|RVE]] 检验宏观[[Interaction Effect\|调节效应]]的高阶形态。 |
> | [[Moderator Analysis]] | 关联方法 | 元回归是调节分析的高阶形态，弥补了传统子组[[Analysis of Variance\|方差分析]]无法处理连续变量的缺陷。 |
> | [[Heterogeneity]] | 诊断基础 | 研究间异质性是实施元回归的前提依据，元回归的核心目标即为解释此异质性。 |
> | [[Effect Size]] | [[Dependent Variable\|因变量]] | 各项研究的效应量点估计构成元回归模型的响应变量。 |
> | [[Reliability]] | 核心应用 | [[Argument_Greene_2018_JEP\|Greene et al. (2018)]] 通过元回归证明了测量信度是决定效应量大小的底层方法学变量。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Lei_Ding_Chiu_2026_ERR|Lei et al. (2026)]] 运用随机效应元回归检验国家人均国内生产总值 Z 分数（$F = 9.430, p < .01, \beta_1 = 0.197$）、文献发表年份（$F = 7.006, p < .05, \beta_1 = 0.032$）及样本性别比例对图形组织器干预效应的连续调节作用。
> - [[Argument_Greene_2018_JEP|Greene et al. (2018)]] 在[[Epistemic Cognition|认识论认知]][[Meta-analysis|元分析]]中运用元回归检验[[Questionnaire|问卷]][[Reliability|信度]]对[[Effect Size|效应量]]的预测力，发现信度回归系数达 $b = .300$。
> - [[Argument_Park_2026_TSC|Park et al. (2026)]] 在[[Three-Level Meta-Analysis|三水平元分析]]框架下运用元回归检验参与者年龄、学段、地理区域、发表年份及[[Creativity|创造力]]与[[Critical Thinking|批判性思维]]测量类型对相关量的调节作用，并检验两类测量类型的交互项（$Q_M(1) = 6.524, p = .011$）。
