---
title: Meta-regression
aliases:
  - 元回归
  - meta-regression analysis
summary: "在元分析框架下，通过加权回归检验研究特征（调节变量）对效应量异质性的解释力，输出回归系数 b 及置信区间。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 34
method_related_level: 4
method_related_stars: "⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/statistical
  - meta-analysis
  - moderator-analysis
related_concepts:
  - "[[Effect Size]]"
  - "[[Dependent Variable]]"
  - "[[Variable]]"
  - "[[Independent Variable]]"
  - "[[Heterogeneity]]"
  - "[[Standard Error]]"
  - "[[Confidence Interval]]"
  - "[[Epistemology]]"
  - "[[Positivism]]"
  - "[[Sampling Error]]"
  - "[[Document]]"
  - "[[Reliability]]"
  - "[[Ecological Fallacy]]"
  - "[[Literature Search]]"
  - "[[Publication Bias]]"
  - "[[Interaction Effect]]"
  - "[[Hypothesis]]"
  - "[[Sample Size Determination]]"
  - "[[Epistemic Cognition]]"
  - "[[Academic Achievement]]"
  - "[[Questionnaire]]"
  - "[[Internal Consistency]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Preregistration]]"
  - "[[Analytic Framework]]"
related_arguments:
  - "[[Argument_Greene_2018_JEP]]"
related_theories:
  - "[[Classical Test Theory]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Systematic Review]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Chi-Squared Test]]"
  - "[[Moderator Analysis]]"
  - "[[Analysis of Variance]]"
status: active
created: 2026-08-19
updated: 2026-08-19
---

# Meta-regression

---

## 定义

> [!def] 方法定义
> 元回归（Meta-regression）是在[[Meta-analysis|元分析]]框架下，以各纳入研究的[[Effect Size|效应量]]为[[Dependent Variable|因变量]]、研究层面特征（调节[[Variable|变量]]）为[[Independent Variable|自变量]]，通过加权回归分析检验调节变量对效应量[[Heterogeneity|异质性]]的解释力的统计方法。它将调节分析从离散子组比较推广到连续变量及多元模型，并依据各研究的抽样精度（权重）校正估计方差。

> [!method-scope] 方法范围
> - **研究对象** 跨原始研究的效应量变异性及其研究层面的潜在预测变量（调节变量）。
> - **问题类型** 解释性与机制性问题：哪些研究设计、测量工具、样本特征或干预属性能够系统性解释效应量的大小差异？
> - **分析单位** 研究（study）或独立样本（sample），每条数据对应一项纳入元分析的研究或效应量估计值。
> - **输出形式** 回归系数 $b$（未标准化）或 $eta$（标准化）、[[Standard Error|标准误]]、95% [[Confidence Interval|置信区间]]、模型检验量 $Q_{\text{model}}$ 以及残余异质性指标 $\tau^2$ 与 $I^2$。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** [[Positivism|实证主义]]后设整合：将单项实证研究视为带有[[Sampling Error|抽样误差]]与方法学特征的观测点，通过跨研究建模提取深层稳健规律。
> - **研究者角色** 预先依据实质理论设定候选调节[[Variable|变量]]，对[[Document|文献]]纳入标准、[[Effect Size|效应量]]提取口径和测量[[Coding in Qualitative Research|编码]][[Reliability|信度]]负责，避免事后数据挖掘导致的 I 型错误膨胀。
> - **有效性标准** 统计结论效度（检验功效取决于纳入研究数量 $k$）、测量效度（调节变量编码准确性与一致性）以及外部推广边界。
> - **不声称回答的问题** 元回归揭示的是研究层面的生态关联（ecological association），不能直接等同于个体层面的因果机制，不可犯[[Ecological Fallacy|生态谬误]]。

> [!method-stack] 方法层级
> - **研究设计** [[Systematic Review|系统综述]]与[[Meta-analysis|元分析]]（证据合成与二次分析设计）。
> - **数据收集** 系统[[Literature Search|文献检索]]、PRISMA 流程筛选、效应量与研究特征双盲编码。
> - **分析方法** 加权最小二乘法（WLS）、限制性最大似然法（REML）或完全贝叶斯元回归。
> - **辅助技术** [[Heterogeneity|异质性]]检验（$Q$ 检验、$I^2$、$\tau^2$）、[[Publication Bias|发表偏倚]]敏感性分析、多重共线性诊断。

---

## 研究程序

> [!proc] 通用程序
> 1. 明确理论问题：预设哪些研究特征（如[[Reliability|信度]]、学段、任务类型）可能[[Interaction Effect|调节效应]]量大小。
> 2. 系统检索与[[Document|文献]]筛选，提取各研究的[[Effect Size|效应量]]指标（如 $r$、$d$、$g$）及其抽样方差 $v_i$，并对调节[[Variable|变量]]进行标准化[[Coding in Qualitative Research|编码]]。
> 3. 计算合并效应与[[Heterogeneity|异质性]]检验，评估总异质性 $Q_{\text{total}}$ 与研究间方差 $\tau^2$ 是否支持进行元回归。
> 4. 构建加权元回归模型（固定效应或随机效应），估计截距 $\beta_0$、偏回归系数 $\beta_j$、[[Confidence Interval|置信区间]]及模型解释比例 $R^2_{\text{analog}}$。
> 5. 进行模型诊断：检查残余异质性 $Q_{\text{residual}}$、多重共线性、高杠杆异常点及[[Publication Bias|发表偏倚]]影响。

### 量化方法模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 研究层面汇总数据矩阵（每行代表一个独立效应量，列包含效应量点估计、抽样方差及若干调节变量）。
> - **样本与单位** 纳入研究数 $k$；经验法则建议每个调节变量至少需要 10 项独立研究支撑（$k/p \ge 10$）。
> - **变量或指标** 
>   - [[Dependent Variable|因变量]]：效应量估计值 $\hat{\theta}_i$（如 Pearson 相关系数 $r$、Fisher's $z$ 或 Cohen's $d$）。
>   - [[Independent Variable|自变量]]：研究特征调节变量 $x_{ij}$（连续变量如发表年份、量表信度；分类虚拟变量如学段、出版类型）。
>   - 权重：研究精度倒数 $w_i = 1 / (v_i + \tau^2)$。
> - **模型或统计量** 混合效应元回归模型（Mixed-effects meta-regression）。
> - **诊断与检验** $Q_{\text{model}}$（模型解释方差检验）、$Q_{\text{residual}}$（未解释残差异质性检验）、$I^2_{\text{residual}}$。

> [!formula-step] 公式步骤　基础加权元回归模型
> $$\hat{\theta}_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_p x_{ip} + u_i + \epsilon_i$$
>
> **这个公式在做什么** 以第 $i$ 项研究的效应量估计值 $\hat{\theta}_i$ 为因变量，通过 $p$ 个研究特征调节变量 $x_{i1}, \dots, x_{ip}$ 预测效应量大小，并同时分解研究间异质性误差 $u_i$ 与[[Sampling Error|抽样误差]] $\epsilon_i$。
>
> **符号说明**
> - $\hat{\theta}_i$ 第 $i$ 项研究观察到的效应量（如 $r_i$ 或 $d_i$）
> - $\beta_0$ 截距，代表所有调节变量为 0 时的基线效应量
> - $\beta_j$ 第 $j$ 个调节变量的偏回归系数，表示其他特征固定时，该变量每增加 1 个单位时效应量的预期改变量
> - $x_{ij}$ 第 $i$ 项研究在调节变量 $j$ 上的取值
> - $u_i$ 研究间随机效应残差，$u_i \sim N(0, \tau^2)$
> - $\epsilon_i$ 研究内抽样误差，$\epsilon_i \sim N(0, v_i)$，其中 $v_i$ 为第 $i$ 项研究效应量的抽样方差
>
> **数学直觉** 普通最小二乘法（OLS）[[Hypothesis|假设]]所有观测值具有同方差，而元回归中大样本研究的抽样误差远小于小样本研究，因此必须以各研究的方差倒数为权重进行广义加权最小二乘估计。
>
> **结果怎么读** $\beta_j > 0$ 且置信区间不包含 0 时，表明该研究特征与效应量显著正相关；$\beta_j < 0$ 表明负向调节；$p < .05$ 拒绝无调节效应的零假设。
>
> **注意事项** 若调节变量过多而研究量 $k$ 较小，模型极易产生过拟合与假阳性结果；分类变量需转换为哑变量（Dummy variables）处理。

> [!formula-step] 公式步骤　随机效应加权权重与方差估计
> $$w_i = \frac{1}{v_i + \tau^2}$$
>
> **这个公式在做什么** 为第 $i$ 项研究分配在加权回归求解过程中的精确权重，综合权衡抽样精度与研究间真实异质性。
>
> **符号说明**
> - $w_i$ 第 $i$ 项研究的综合分析权重
> - $v_i$ 第 $i$ 项研究内部的抽样方差（Sampling Variance），由该研究的[[Sample Size Determination|样本量]] $N_i$ 及效应量本身计算得到
> - $\tau^2$ 真实效应量在不同研究间的总体方差（Between-study Variance / Residual Heterogeneity），通常通过限制性最大似然法（REML）估计
>
> **数学直觉** [[Fixed-Effect and Random-Effects Models|固定效应模型]]假定所有研究共享单一真实真值（$\tau^2 = 0$），权重完全由样本量决定（$w_i = 1/v_i$）；而在存在异质性的现实情境中，分母加入 $\tau^2$ 对过大的极值样本权重施加平滑惩罚，使各研究权重更为平衡。
>
> **结果怎么读** 当 $\tau^2 \to 0$ 时，权重退化为纯抽样精度权重；当 $\tau^2$ 极大时，各研究权重趋于均等，表明研究间方法学差异构成了方差的主导来源。
>
> **注意事项** $\tau^2$ 必须在纳入调节变量后重新估计为残余方差 $\tau^2_{\text{residual}}$，并通过对比调节前后的方差下降比例计算解释方差 $R^2_{\text{analog}} = 1 - \frac{\tau^2_{\text{residual}}}{\tau^2_{\text{total}}}$。

> [!formula-step] 公式步骤　[[Argument_Greene_2018_JEP|Greene et al. (2018)]] 信度决定论元回归应用
> $$\hat{r}_i = \beta_0 + \beta_1 \cdot \text{Reliability}_i + \epsilon_i$$
>
> **这个公式在做什么** 以各研究报告的[[Epistemic Cognition|认识论认知]]与[[Academic Achievement|学业成就]]相关系数 $r$ 为因变量，以[[Questionnaire|问卷]][[Internal Consistency|内部一致性]]信度（Cronbach's $\alpha$ 或 McDonald's $\omega$）为唯一预测变量，检验测量误差对可观测效应量的系统性衰减机制。
>
> **符号说明**
> - $\hat{r}_i$ 第 $i$ 项研究所报告的认识论认知与学业成绩之间的相关系数
> - $\text{Reliability}_i$ 第 $i$ 项研究所用[[Epistemology|认识论]]量表的内部一致性信度系数（取值范围 0 到 1）
> - $\beta_1$ 信度元回归斜率估计值（Greene et al. 报告为 $b = .300, p < .001$）
>
> **数学直觉** [[Classical Test Theory|经典测量理论]]表明测量误差会导致相关系数发生统计衰减（Attenuation）。元回归从实证层面验证了这一规律：问卷信度越高，可观测到的效应量越大；若信度为 0，效应量归零；若信度达到完美的 1.0，理论真实相关性可达 $r = .300$。
>
> **结果怎么读** 结果证实了方法学决定论：大量低信度自陈问卷直接压低了以往文献的效应量，造成了认识论认知对学业成绩无影响的虚假印象。[[Argument_Greene_2018_JEP|(Greene et al., 2018, p. 1102)]]
>
> **注意事项** 该分析在综合[[Meta-analysis|元分析]]软件（CMA）中完成，提示研究者在解读认知变量效应时必须控制测量工具的信度基线。

> [!software-impl] 软件实现
> - **推荐软件** R（`metafor` 包）、Comprehensive Meta-Analysis (CMA)、Stata（`meta regress` 命令）、Python（`statsmodels`）
> - **核心包或命令**
>   - R `metafor` 实现：
>     ```R
>     library(metafor)
>     # 估计随机效应多元元回归
>     res <- rma(yi = r_z, vi = var_z, mods = ~ reliability + grade_level, data = meta_data, method = "REML")
>     summary(res)
>     ```
>   - CMA 软件实现：在主界面选择 `Analyses -> Meta-regression`，选定 Moderator 变量并指定 Mixed Effects 模型运行。
> - **实现流程** 数据清洗 -> 效应量转换（如 $r$ 转 Fisher's $z$）-> 连续调节变量中心化 -> REML 模型估计 -> 残差诊断与报告。
> - **报告标准** 完整报告样本量 $k$、回归系数 $b$ 与[[Standard Error|标准误]]、95% CI、$p$ 值、模型[[Chi-Squared Test|卡方检验]]量 $Q_{\text{model}}$、残差异质性 $\tau^2$ 及解释比例 $R^2$。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 纳入[[Meta-analysis|元分析]]的研究间存在显著[[Heterogeneity|异质性]]（$I^2 > 25\%$ 或 $Q$ 检验 $p < .05$），且研究者希望在连续维度上检验假设的调节变量（如样本年龄、干预时长、信度系数）。[[Argument_Greene_2018_JEP|(Greene et al., 2018)]]
> - **谨慎使用** 纳入研究数量较少（$k < 10$）时模型自由度不足；调节变量间存在高度多重共线性时系数难以分离；调节变量为事后未预注册变量时需声明探索性质。
> - **不适合使用** 旨在推断个体层面的微观因果中介机制；[[Primary and Secondary Documents|原始文献]]中关键调节[[Variable|变量]]大面积缺失且无法补齐。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** [[Ecological Fallacy|生态谬误]]（研究层面的[[Variable|变量]]关联无法直接推导至学生个体）；混杂变量遗漏（由于 $k$ 有限无法同时控制所有潜在混杂因素）；[[Publication Bias|发表偏倚]]与小样本效应干扰。
> - **适用边界** 需要充足的独立研究数量；模型结论受制于原始研究报告的质量（Garbage in, garbage out）。
> - **误用风险** 在高维调节变量空间中进行无理论指导的逐步回归，导致假阳性率激增。
> - **补救方式** [[Preregistration|预注册]]调节[[Hypothesis|假设]]；采用置换检验（Permutation test）校正小样本推断；结合散点气泡图（Bubble plot）直观展示[[Effect Size|效应量]]与调节变量的关系。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Meta-analysis]] | 前置方法 | 元回归依附于元[[Analytic Framework\|分析框架]]，以元分析提取的[[Effect Size\|效应量]]与抽样方差作为建模输入。 |
> | [[Moderator Analysis]] | 关联方法 | 元回归是调节分析的高阶形态，弥补了传统子组[[Analysis of Variance\|方差分析]]无法处理连续[[Variable\|变量]]的缺陷。 |
> | [[Heterogeneity]] | 诊断基础 | 研究间异质性是实施元回归的前提依据，元回归的核心目标即为解释此异质性。 |
> | [[Effect Size]] | [[Dependent Variable\|因变量]] | 各项研究的效应量点估计构成元回归模型的响应变量。 |
> | [[Reliability]] | 核心应用 | [[Argument_Greene_2018_JEP\|Greene et al. (2018)]] 通过元回归证明了测量信度是决定效应量大小的底层方法学变量。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Greene_2018_JEP|Greene et al. (2018)]] — 在[[Epistemic Cognition|认识论认知]][[Meta-analysis|元分析]]中运用元回归检验[[Questionnaire|问卷]][[Reliability|信度]]对[[Effect Size|效应量]]的预测力，发现信度回归系数达 $b = .300$。
