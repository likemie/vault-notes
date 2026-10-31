---
title: Multiple Regression
aliases:
  - 多元回归
  - 多重回归
  - multiple linear regression
  - OLS regression
summary: "将皮尔逊相关扩展至多个预测变量的参数推断统计方法，通过最小二乘法估计各独立自变量在控制其他协变量条件下的偏回归系数与整体解释方差；因受制于可观测选择假设与遗漏变量偏差，促使现代因果计量学转向准实验与随机对照设计。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 22
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/model
  - quantitative-research
  - regression
related_concepts:
  - "[[Variable]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Research Question]]"
  - "[[Heterogeneity]]"
  - "[[Simplicity of Knowledge]]"
  - "[[Academic Achievement]]"
  - "[[Task Structure]]"
  - "[[Reflexivity]]"
  - "[[Causality]]"
  - "[[Credibility Revolution]]"
related_theories: []
related_methods:
  - "[[Meta-regression]]"
  - "[[Analysis of Variance]]"
  - "[[Analysis of Covariance]]"
  - "[[Survey Research]]"
  - "[[Sample Size Determination]]"
  - "[[Ordinary Least Squares]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Regression Discontinuity Design]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Lodewyk_2007_EducPsych]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit11]]"
confidence: high
status: active
created: 2026-05-31
updated: 2026-10-31
---

> [!def] Multiple Regression
> 多元回归（Multiple Regression）是将双变量相关扩展至两个或以上[[Independent Variable|预测变量]]的参数推断统计与计量建模方法。该方法通过[[Ordinary Least Squares|普通最小二乘法]]（OLS）将单一连续[[Dependent Variable|因变量]]对多个自变量展开线性投影，输出整体模型拟合优度（$R^2$、总体 $F$ 检验）以及各预测变量在控制其余变量影响下的偏回归系数（非标准化系数 $b$、标准化系数 $\beta$ 与个别 $t$ 检验统计量），用于评估特定因素在多元系统中的相对预测力。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch. 8, pp. 1326–1327)]]

> [!method-scope] 方法范围
> - **测量与估计对象** 连续结果变量与多个连续或离散自变量之间的线性条件期望关系。
> - **问题类型** 适合回答关联预测、变异分解与协变量控制分析；在满足可观测选择假设时用于条件关联识别。
> - **分析单位** 个体学生、教师、学校、文献成果或地区组织。
> - **输入数据** 横截面、时间序列或混合截面观测数据；因变量为连续变量，自变量为连续或二元指示变量。
> - **输出形式** 模型判定系数 $R^2$、回归截距与偏回归斜率向量 $\boldsymbol{\beta}$、稳健标准误、各系数 $t$ 检验与整体方差分析 $F$ 统计量。

> [!citation-card] 多元回归的选择标准与核心功能
> 多元线性回归用于分析两个或多个预测变量与一个结果变量之间的统计关系。当研究问题旨在探究哪些因素对某一结果具有最强的相对解释力时，该方法能够在保持其他协变量恒定的条件下，独立评估各预测变量的边际增量贡献。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch. 8, p. 1327)]]
>
> *Multiple regression is used to relate two or more predictor variables to a single dependent variable. It provides an overall assessment of the relationship and reveals which specific predictors make significant unique contributions to explaining variance in the outcome.*

---

> [!method-position] 认识论与方法定位
> - **知识观** 建立在经典线性投影与经验主义关联推断基础之上，假定条件期望函数近似呈现线性可加形态。
> - **研究者判断** 模型的有效性高度依赖研究者对自变量集合的选择与函数设定。控制变量的增减直接影响核心自变量的估计系数与符号稳定性。
> - **有效性标准** 遵循统计结论效度与模型设定诊断标准，依赖残差同方差性、正态性以及解释变量间低多重共线性（Variance Inflation Factor, VIF）。
> - **不声称回答的问题** 不能通过单纯添加控制变量直接建立确定性因果关系。当存在不可观测的个体异质性、反向因果或测量误差时，回归系数受制于遗漏变量偏差，无法替代严密的外生准实验或随机实验。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, p. 248)]]

> [!method-stack] 方法层级
> - **设计形态**
>   - **标准多元线性回归（Enter Regression）** 所有理论预测变量同时纳入模型。
>   - **分层回归（Hierarchical Regression）** 依据理论逻辑分步分块引入控制变量与核心自变量，检验 $\Delta R^2$ 的统计显著性。
>   - **逐步回归（Stepwise Regression）** 由算法依据经验显著性自动筛选变量，易诱发数据窥探与过拟合偏差，规范学术研究通常不予推荐。
> - **方法辨析**
>   - vs 皮尔逊相关（Pearson Correlation）：双变量相关反映零阶未控制相关；多元回归偏系数反映控制其他协变量后的净关联系数。
>   - vs 方差分析（[[Analysis of Variance|ANOVA]]）与协方差分析（[[Analysis of Covariance|ANCOVA]]）：方差分析主要处理类别自变量的组间均值差；多元回归容纳连续变量与类别虚拟变量，二者在广义线性模型框架下数理等价。

---

> [!proc] 通用估计程序
> 1. **明确因变量与自变量集合** 依据理论框架界定因变量 $Y$、核心自变量 $X_1$ 以及必须控制的混杂变量集合 $\mathbf{Z}$。
> 2. **数据清洗与分布检验** 检查连续变量的偏度、峰度与异常值，对偏态严重的变量（如引文量、收入）进行对数转换。
> 3. **模型形式设定** 构建线性回归方程，必要时加入交叉乘积项以刻画交互调节效应。
> 4. **OLS 参数求解** 最小化残差平方和，输出参数估计向量 $\hat{\boldsymbol{\beta}}$ 及协方差矩阵。
> 5. **计量诊断与稳健性检验** 检验残差分布形态、异方差性（怀特检验或布罗施-培根检验）与多重共线性（VIF 测度）；采用异方差稳健标准误（Huber-White Sandwich Estimator）。
> 6. **结果解释与汇报** 报告非标准化系数 $b$（结合原始测量单位）、标准化系数 $\beta$（横向比较相对权重）、模型 $R^2$ 与修正 $R^2$。

---

> [!formula-step] 步骤一　经典多元线性 OLS 估计模型
> $$Y_i = \beta_0 + \sum_{j=1}^k \beta_j X_{ij} + \varepsilon_i, \quad E[\varepsilon_i \mid \mathbf{X}_i] = 0$$
>
> **这个公式在做什么** 将样本个体 $i$ 的因变量观测值分解为可由 $k$ 个预测变量线性组合解释的确定性部分，与均值为零的随机残差扰动项 $\varepsilon_i$。
>
> **符号说明**
> - $Y_i$：个体 $i$ 的连续因变量数值。
> - $\beta_0$：回归常数项（截距），即所有自变量取零时 $Y$ 的条件均值。
> - $\beta_j$：自变量 $X_j$ 的偏回归系数，表示保持其他 $k-1$ 个自变量不变时，$X_j$ 每增加 1 个单位所伴随的 $Y$ 的期望变化量。
> - $\varepsilon_i$：不可观测的误差扰动项，涵盖测量误差与未进入模型的微观扰动。
>
> **数学直觉** 依托几何投影原理，在多维欧几里得空间中寻找距离样本散点垂直欧氏距离平方和最小的超平面，使得模型残差向量与所有自变量生成的线性子空间正交。
>
> > [!formula-reading] 结果解读与注意事项
> > | 指标 | 统计含义 | 注意要点 |
> > |---|---|---|
> > | $R^2$ | 所有自变量共同解释的 $Y$ 变异比例 | 变量越多数值单调不减，跨模型比较须使用调整后 Adjusted $R^2$。 |
> > | $\beta$（标准化系数） | 将变量全标准化为 $Z$ 分数后的回归斜率 | 允许跨越不同测量量纲对比自变量的相对相关强度。 |
> > | $t$ 检验值 | 单个系数是否显著异于零的显著性统计量 | 易受样本容量放大影响，显著并不直接等同于效应具有实质重要性。 |

---

> [!software-impl] 软件实现
> - **数据来源** 调查量表数据、宏观统计数据库或大规模文献计量底表。
> - **核心包与命令**
>   - R：基础包 `lm(Y ~ X1 + X2 + controls, data = df)`，稳健标准误使用 `sandwich` 与 `lmtest::coeftest()`。
>   - Python：`statsmodels.api.OLS` 或 `statsmodels.formula.api.ols`。
>   - Stata：`regress Y X1 X2 controls, robust`。
> - **报告标准** 完整呈现模型系数、标准误（或置信区间）、精确 $p$ 值、样本量 $N$、模型 $F$ 统计量及判定系数 $R^2$。

> [!method-stack] 变量与诊断
> - **数据结构** 经典横截面数据或跨期混合数据。
> - **关键变量** 因变量、理论自变量与控制变量。
> - **核心识别假设** 外生性假定（Zero Conditional Mean, $E[\varepsilon \mid \mathbf{X}] = 0$）与不可观测选择偏差排除。
> - **诊断与检验** 多重共线性诊断（方差膨胀因子 $\text{VIF} < 5$ 或 $10$）、异方差怀特检验、残差正态性 Q-Q 图检验与强影响点（Influence points）及极端离群值排查。

---

> [!method-fit] 适用判断
> - **适合使用** 需要评估多个因素对某一连续产出（如学业成绩、被引频次、科研产出）的独立预测贡献；需要控制人口统计学与背景特征后检验目标自变量的边际增量。[[Argument_Lodewyk_2007_EducPsych|(Lodewyk, 2007, pp. 312–314)]]
> - **谨慎使用** 自变量之间存在高度共线性（导致估计方差膨胀、符号反转）；样本容量过小而纳入过多控制变量（引发严重自由度损耗与样本内过拟合）。
> - **不适合使用** 因变量为二元离散变量（应使用 Logit/Probit 模型）；旨在识别严密因果效应但存在大量不可观测混杂变量或同时因果反馈机制的观测系统。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, p. 248)]]

---

> [!method-limits] 方法局限与因果革命批判
> - **遗漏变量偏差（Omitted Variable Bias）** 多元回归依赖“可观测选择（Selection on Observables）”假设。若存在未测量的混杂因素（如天赋能力、动机水平、隐性人脉），即便控制了大量显性指标，回归系数依然存在内生性偏误。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, p. 248)]]
> - **多重共线性风险** 预测变量高度相关时，自变量间的信息重叠使得 OLS 矩阵求逆不稳定，各变量独立贡献无法被稳健分离。
> - **过拟合与样本依赖** 变量数量相对样本过大时，模型过度拟合随机扰动噪音，使得样本内 $R^2$ 虚高而在新样本中外推预测力急剧崩溃。
> - **因果革命的范式转型** 面对多元回归在处理未观测混杂时的内在瓶颈，微观计量经济学发起的[[Credibility Revolution|可信性革命]]推动了范式转变，要求通过[[Randomised Controlled Trials|随机对照试验]]（RCT）或[[Regression Discontinuity Design|断点回归]]（RDD）等外生设计确立严格因果推断。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, p. 248)]]

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Ordinary Least Squares]] | 计算基础 | 多元回归的核心参数求解算法与线性无偏估计基石。 |
> | [[Analysis of Covariance]] | 相近方法 | 将类别组别与连续协变量结合的线性模型，在广义线性系统下与多元回归同构。 |
> | [[Meta-regression]] | 拓展方法 | 将多元回归原理推广至元分析中，用研究特征变量解释效应量间的异质性。 |
> | [[Credibility Revolution]] | 批判范式 | 反思多元回归在排除遗漏变量上的局限性，奠定因果识别准实验与实验转向。 |
> | [[Randomised Controlled Trials]] | 替代与升级 | 依托随机分配外生平衡所有已知与未知混杂变量，克服多元回归的内生性瓶颈。 |
> | [[Regression Discontinuity Design]] | 替代与升级 | 利用制度连续驱动变量切分阈值，在断点邻域内实现超越观察性多元回归的严格因果识别。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Lodewyk_2007_EducPsych|Lodewyk (2007)]] — 采用分层与多元线性回归分析，在控制学校导向后检验快速学习信念与简单知识信念对学业成就、良构/劣构任务表现及反思性判断的独立预测力（pp. 312–316）。
> - [[Argument_Creswell_2022_SAGE|Creswell and Creswell (2022)]] — 系统阐释多元回归在调查研究中的指标选择、自变量筛选与统计假设检验标准规范（Ch. 8, pp. 1326–1327）。
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Wang & Barabási (2021)]] — 阐明观察性多元回归在处理科学学大数据不可观测混杂变量时的内生局限，并论证微观计量因果识别范式（RCT 与 RDD）对回归建模的弥补作用（pp. 248–251）。
