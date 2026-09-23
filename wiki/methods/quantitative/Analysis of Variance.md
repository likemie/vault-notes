---
title: Analysis of Variance
aliases:
  - 方差分析
  - 单因素方差分析
  - One-Way ANOVA
  - ANOVA
  - Analysis of Variance (ANOVA)
  - F-test
  - F检验
summary: "基于方差分解比较两组或多组连续变量均值差异的推断统计方法族，涵盖单因素ANOVA、因子设计ANOVA、ANCOVA与MANOVA，并提供η²与ω²等效应量估计"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 39
method_related_level: 4
method_related_stars: "⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/statistical
  - quantitative-research
  - group-comparison
  - hypothesis-testing
related_concepts:
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Dependent Variable]]"
  - "[[Interaction Effect]]"
  - "[[Unit of Analysis]]"
  - "[[Independent Variable]]"
  - "[[Homework]]"
  - "[[Epistemic Stances]]"
  - "[[Multiplist]]"
  - "[[Epistemology]]"
  - "[[Paradigm]]"
  - "[[Type I and Type II Errors]]"
  - "[[Internal Validity]]"
  - "[[Academic Achievement]]"
  - "[[Construct]]"
  - "[[Generative Artificial Intelligence]]"
  - "[[Document]]"
  - "[[Falsification]]"
  - "[[Teaching Assistant]]"
  - "[[Heterogeneity]]"
  - "[[Metacognition]]"
related_theories:
  - "[[Central Limit Theorem]]"
related_methods:
  - "[[Analysis of Covariance]]"
  - "[[Multivariate Analysis of Variance]]"
  - "[[Effect Size]]"
  - "[[Experimental Research]]"
  - "[[Omega-Squared]]"
  - "[[Sample Size Determination]]"
  - "[[Random Assignment]]"
  - "[[True Experimental Design]]"
  - "[[Factorial Design]]"
  - "[[Pre-test and Post-test]]"
  - "[[Confidence Interval]]"
  - "[[Repeated Measures Design]]"
  - "[[t-test]]"
  - "[[Chi-Squared Test]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Wu_2025_ER]]"
confidence: high
status: active
created: 2026-05-31
updated: 2026-09-22
---

# Analysis of Variance (ANOVA)

---

## 定义

> [!def] 方法定义
> 方差分析（Analysis of Variance, ANOVA）是一族用于检验三个或更多处理组（或两个及以上独立样本）在连续数值因[[Variable\|变量]]上的总体均值是否存在统计学显著差异的推断统计方法，由罗纳德·费希尔（Ronald Fisher）开创并以 $F$ 检验统计量为核心判定工具。其数学本质在于将总离差平方和（Total Sum of Squares, $SS_{\text{total}}$）正交分解为可由实验处理解释的“组间变异”（Between-group Variance / $SS_{\text{between}}$）与由随机误差造成的“组内变异”（Within-group Variance / $SS_{\text{within}}$），通过两类均方的比值 $F = MS_{\text{between}} / MS_{\text{within}}$ 检验各组总体均值相等的原[[Hypothesis\|假设]]。[[Argument_Creswell_2022_SAGE\|(Creswell & Creswell, 2022, Ch8)]]; [[Argument_Wu_2025_ER\|(Wu et al., 2025, pp. 362–365)]]

> [!method-scope] 方法范围
> - **研究对象** 多组独立或相关实验处理条件下的连续[[Dependent Variable\|因变量]]测量数据。
> - **问题类型** 组间均值差异检验、主效应（Main Effect）评估、[[Interaction Effect\|交互效应]]（Interaction Effect）识别、控制协变量后的均值比较（[[Analysis of Covariance\|ANCOVA]]）以及多元结果同步比较（[[Multivariate Analysis of Variance\|MANOVA]]）。
> - **[[Unit of Analysis\|分析单位]]** 参与实验或调查的被试个体、教学班级、学校、干预组与对照组。
> - **输出形式** 变异分解表（ANOVA Table）、$F$ 统计量、组间自由度 $df_{\text{between}}$、误差自由度 $df_{\text{within}}$、$p$ 值、事后多重比较（Post-Hoc Tests，如 Tukey HSD、Bonferroni、Scheffé）以及方差解释[[Effect Size\|效应量]]（$\eta^2$、偏 $\eta_p^2$、$\omega^2$）。

> [!citation-card] 实验设计中的标准推断统计选择
> 在[[Experimental Research\|实验研究]]设计中，当[[Independent Variable\|自变量]]为包含两个或多个水平的分类变量、因变量为连续数值变量时，方差分析（ANOVA）及其衍生方法（ANCOVA、MANOVA）是比较组间处理效应最标准且最广泛使用的参数推断统计方法族。[[Argument_Creswell_2022_SAGE\|(Creswell & Creswell, 2022, Ch8, Table 8.3)]]
>
> *ANOVA is the primary statistical technique in experimental research for comparing group means on continuous outcome variables across categorical factor levels.*

> [!citation-card] 人机协同中的效应量多公式辨析
> 在高级统计学[[Homework\|作业]]中，单因素方差分析的效应量指标 $\omega^2$ 存在多种数学表述（基于离差平方和与基于 $F$ 值的公式）。具备多元论[[Epistemic Stances\|认识立场]]的学习者能够借助大语言模型（如 ChatGPT）探索多种公式背后的数学等价性与小样本偏差校正机制，深化对参数估计边界的理解。[[Argument_Wu_2025_ER\|(Wu et al., 2025, pp. 362–365)]]
>
> *[[Multiplist]] learners engage in multi-turn dialogues with ChatGPT to dissect equivalent representations of [[Omega-Squared]] in one-way ANOVA, understanding how different formulas adjust for sample-size bias.*

---

## 方法定位

> [!method-position] [[Epistemology\|认识论]]与方法定位
> - **知识观** 遵循经典参数统计的方差分解[[Paradigm\|范式]]，认为总体测量变异由“确定性系统变异（因子处理效应）”与“不可控随机误差”线性叠加而成；通过控制[[Type I and Type II Errors\|第一类错误]]率，在概率意义上判定处理因素的真实效力。
> - **研究者角色** 研究者必须在前瞻设计阶段进行[[Sample Size Determination\|样本量]]估算与统计功效（Power）规划；在分析前严格诊断正态性（Normality）、方差齐性（Homoscedasticity）与独立性[[Hypothesis\|假设]]；在方差分析显著后审慎选择事后比较程序，并报告无偏[[Effect Size\|效应量]]以防过度夸大实验效果。
> - **有效性标准** [[Internal Validity\|内部效度]]（依赖[[Random Assignment\|随机分配]]控制混淆[[Variable\|变量]]）、统计结论效度（满足球形假设/方差齐性假定）、测度效度与模型稳健性。
> - **不声称回答的问题** 单纯的 ANOVA 显著仅证明“至少存在两组均值不相等”，不能直接指出具体哪两组不同（必须依赖事后比较）；在非随机分配的观察性研究中，ANOVA 显著不能直接断言因果效应。

> [!method-stack] 方法层级
> - **研究设计** [[True Experimental Design\|真实验设计]]（完全随机设计、随机区组设计）、[[Factorial Design\|因子设计]]、准实验前[[Pre-test and Post-test\|后测]]对照设计。
> - **数据收集** 连续尺度量表得分、[[Academic Achievement\|学业成绩]]测验、反应时、生理指标、任务完成时间。
> - **分析方法**
>   - 单因素方差分析（One-Way ANOVA）：单个分类[[Independent Variable\|自变量]]（$\ge 2$ 水平）对单一连续[[Dependent Variable\|因变量]]。
>   - 因子方差分析（Factorial ANOVA）：多个分类自变量的主效应与[[Interaction Effect\|交互效应]]。
>   - [[Analysis of Covariance\|协方差分析]]（ANCOVA）：引入连续协变量进行方差扣除。
>   - [[Multivariate Analysis of Variance\|多元方差分析]]（MANOVA）：同时检验多个相关连续因变量。
> - **诊断与事后修正**
>   - 方差齐性检验（Levene's Test / Bartlett's Test）
>   - 方差不齐校正：Welch's ANOVA / Brown-Forsythe 检验
>   - 事后多重比较校正：Tukey HSD、Bonferroni、Games-Howell（方差不齐时）
>   - 效应量计算：$\eta^2$、$\eta_p^2$、$\omega^2$（小样本无偏估计量）

---

## 研究程序

> [!proc] 通用检验程序
> 1. **明确实验设计与[[Variable\|变量]]界定** 确定自[[Independent Variable\|自变量]]（因子及水平数 $k$）与[[Dependent Variable\|因变量]]（连续数值），设定显著性水平（通常 $\alpha = .05$）。
> 2. **[[Hypothesis\|假设]]前提诊断** 检查残差正态性（Shapiro-Wilk 检验或 Q-Q 图）与各组方差齐性（Levene 检验）；若方差显著不齐，选用 Welch 修正法。
> 3. **变异分解与构建 ANOVA 表** 计算总离差平方和 $SS_{\text{total}}$、组间离差平方和 $SS_{\text{between}}$ 与组内误差平方和 $SS_{\text{within}}$，除以各自自由度得到均方 $MS$，计算检验统计量 $F = MS_{\text{between}} / MS_{\text{within}}$。
> 4. **统计决策与事后多重检验** 依据 $F$ 分布获得 $p$ 值。若 $p < .05$，拒绝均值相等的原假设，进一步开展事后检验（Post-Hoc Tests）明确具体的两两组间差异。
> 5. **[[Effect Size\|效应量]]估计与[[Confidence Interval\|置信区间]]呈现** 计算并报告方差解释度效应量（小样本优先报告 $\omega^2$ 或 $\eta_p^2$），附带均值差异的 95% [[Confidence Interval\|置信区间]]。

> [!method-stack] 数据、变量与模型
> - **数据结构** 长格式（Long format）数据框，包含一列因子分组标签（Factor）与一列因变量测量值（Value）。
> - **样本容量** 组数 $k \ge 2$，每组[[Sample Size Determination\|样本量]]推荐 $n \ge 15$ 以保证[[Central Limit Theorem\|中心极限定理]]对偏态的抗击力。
> - **数学假设**
>   - 独立性：各组被试独立抽样，测量无相互干扰。
>   - 正态性：各处理水平下的总体呈正态分布 $Y_{ij} \sim N(\mu_i, \sigma^2)$。
>   - 方差齐性：各处理组的总体方差相等 $\sigma_1^2 = \sigma_2^2 = \dots = \sigma_k^2$。

> [!formula-step] 公式步骤一　变异分解与 F 检验统计量（Sum of Squares Decomposition & F-ratio）
> $$SS_{\text{total}} = SS_{\text{between}} + SS_{\text{within}}$$
> $$F = \frac{MS_{\text{between}}}{MS_{\text{within}}} = \frac{SS_{\text{between}} / (k - 1)}{SS_{\text{within}} / (N - k)}$$
>
> **这个公式在做什么** 将总变异分解为组间变异与组内变异，通过组间均方（包含处理效应+误差）与组内均方（仅包含随机误差）的比值，构建服从 $F(k-1, N-k)$ 分布的检验统计量。
>
> **符号说明**
> - $k$：自变量因子的水平数（组数，如 3 个教学干预组）。
> - $N$：全样本总被试数（$N = \sum n_i$）。
> - $SS_{\text{between}} = \sum_{i=1}^k n_i (\bar{Y}_i - \bar{Y})^2$：组间离差平方和，自由度 $df_b = k - 1$。
> - $SS_{\text{within}} = \sum_{i=1}^k \sum_{j=1}^{n_i} (Y_{ij} - \bar{Y}_i)^2$：组内/误差平方和，自由度 $df_w = N - k$。
>
> **数学直觉** 若各组总体均值完全相等（原假设成立），则组间均方 $MS_{\text{between}}$ 与组内均方 $MS_{\text{within}}$ 均是对同一随机误差方差 $\sigma^2$ 的无偏估计，两者的商 $F \approx 1$；若实验处理产生了实质差异，组间均方将额外包含处理效应项 $\sum n_i \alpha_i^2 / (k-1)$，使 $F$ 值显著大于 1。
>
> **结果怎么读** 当 $F > F_{\text{crit}}$ 且 $p < .05$ 时，拒绝原假设，表明各组均值不全相等。
>
> **注意事项** 当组数 $k=2$ 时，单因素方差分析等价于独立样本 $t$ 检验，且严格满足 $F = t^2$。

> [!formula-step] 公式步骤二　样本方差解释度效应量 Eta-Squared（$\eta^2$ 与 $\eta_p^2$）
> $$\eta^2 = \frac{SS_{\text{between}}}{SS_{\text{total}}}$$
> $$\eta_p^2 = \frac{SS_{\text{between}}}{SS_{\text{between}} + SS_{\text{error}}}$$
>
> **这个公式在做什么** 计算自变量处理所能解释的因变量变异占总变异的百分比（类似于回归分析中的 $R^2$）。
>
> **数学直觉** 在单因素方差分析中，因只有单一因素，总变异仅由组间与误差构成，故偏 Eta 平方与全 Eta 平方数值完全相等（$\eta^2 = \eta_p^2$）。但在多因素方差分析中，$\eta_p^2$ 扣除了其他主效应与[[Interaction Effect\|交互效应]]的平方和，仅以本因子变异与误差变异之和为基准。
>
> **注意事项** $\eta^2$ 是基于样本离差平方和计算的描述性指标，会系统性高估总体效应量（有向上偏倚），在小样本实验中尤其严重。

> [!formula-step] 公式步骤三　总体无偏效应量 [[Omega-Squared]]（$\omega^2$）及其等价形式
> $$\omega^2 = \frac{SS_{\text{between}} - (k - 1) MS_{\text{error}}}{SS_{\text{total}} + MS_{\text{error}}} = \frac{(p - 1)(F - 1)}{(p - 1)(F - 1) + np}$$
>
> **这个公式在做什么** 扣除样本随机误差对均方估计的虚高影响，提供总体方差解释比例（Population Variance Explained）的无偏估计量。
>
> **符号说明与参数等价性**
> - $k$（或 $p$）：处理组数（Number of groups/conditions）。
> - $n$：每组样本量（假设平衡设计，总样本 $N = np$）。
> - $F$：方差分析计算所得的 $F$ 统计量。
> - $MS_{\text{error}} = MS_{\text{within}}$：组内均方误差。
>
> **数学推导直觉**
> 因为组间均方的期望为 $E(MS_{\text{between}}) = \sigma^2 + \frac{n \sum \alpha_i^2}{k-1}$，而 $E(MS_{\text{error}}) = \sigma^2$。为了估计纯粹的处理变异 $\sigma_{\alpha}^2 = \frac{\sum \alpha_i^2}{k} = \frac{k-1}{nk}(E(MS_{\text{between}}) - E(MS_{\text{error}}))$，分子中必须减去 $(k-1)MS_{\text{error}}$ 作为小样本偏差修正项。
> 代入 $SS_{\text{between}} = (p-1)MS_{\text{between}} = (p-1)F \cdot MS_{\text{error}}$ 与 $SS_{\text{total}} = (p-1)F \cdot MS_{\text{error}} + p(n-1)MS_{\text{error}}$，约去 $MS_{\text{error}}$，即严格推导出右侧基于 $F$ 值与组容量 $n$ 的无偏表述。
>
> **结果怎么读** $\omega^2 \in [0, 1]$（极微弱效应时可能为微负，此时约定记为 0）。按照 Cohen 标准：$\omega^2 \approx 0.01$ 为小效应，$\omega^2 \approx 0.06$ 为中等效应，$\omega^2 \ge 0.14$ 为大效应。

> [!software-impl] 软件实现
> - **R 语言**
>   - 单因素 ANOVA：`fit <- aov(score ~ group, data = my_data)`
>   - 变异表提取：`summary(fit)`
>   - 方差齐性检验：`car::leveneTest(score ~ group, data = my_data)`
>   - 方差不齐时的 Welch ANOVA：`oneway.test(score ~ group, data = my_data, var.equal = FALSE)`
>   - 事后检验：`TukeyHSD(fit)`
>   - 效应量计算：`effectsize::omega_squared(fit)` 或 `effectsize::eta_squared(fit)`
> - **Python**
>   - `import statsmodels.api as sm`
>   - `from statsmodels.formula.api import ols`
>   - `model = ols('score ~ C(group)', data=df).fit()`
>   - `anova_table = sm.stats.anova_lm(model, typ=2)`
>   - 事后检验：`from statsmodels.stats.multicomp import pairwise_tukeyhsd; print(pairwise_tukeyhsd(df['score'], df['group']))`
> - **SPSS**
>   - 菜单路径：`Analyze -> Compare Means -> One-Way ANOVA`，在 `Options` 中勾选 `Homogeneity of variance test` 与 `Welch`，在 `Post Hoc` 中选 `Tukey`，在 `Effect Size` 中勾选 `Estimate effect size`（报告 Eta-squared 与 Omega-squared）。

---

## 方法变体与家族谱系

> [!tension-table] 方差分析方法族（ANOVA Family）及相近推断统计方法辨析
> | 方法名称 | [[Independent Variable\|自变量]]（因子）结构 | [[Dependent Variable\|因变量]]结构 | 控制[[Variable\|变量]]（协变量） | 核心解决问题 | 关键[[Hypothesis\|假设]]与局限 |
> |---|---|---|---|---|---|
> | 单因素方差分析（One-Way ANOVA） | 1 个分类变量（$\ge 2$ 水平） | 1 个连续变量 | 无 | 比较单因子不同水平下的组间均值差异 | 独立性、正态性、方差齐性（Levene 检验） |
> | 双因素/多因素方差分析（Factorial ANOVA） | $\ge 2$ 个分类变量（交叉分组） | 1 个连续变量 | 无 | 分离检验各因子主效应与[[Interaction Effect\|交互效应]] | 需警惕高阶交互效应解释困难与单元格不平衡 |
> | 重复测量方差分析（[[Repeated Measures Design\|repeated measures]] ANOVA） | 组内因子（同一被试多次测量） | 1 个连续变量 | 无 | 消除个体间系统变异，提高检验被试自身前后变化的功效 | 需满足球形假设（Sphericity，违反时用 GG 校正） |
> | [[Analysis of Covariance\|协方差分析（ANCOVA）]] | 1 个或多个分类变量 | 1 个连续变量 | $\ge 1$ 个连续协变量 | 扣除与因变量相关的混淆变量（基线分等），提高处理效应估计精度 | 要求回归斜率同质性（Homogeneity of Regressions） |
> | [[Multivariate Analysis of Variance\|多元方差分析（MANOVA）]] | 1 个或多个分类变量 | $\ge 2$ 个**相互关联的连续因变量** | 无 | 控制族误差率（Familywise Error），综合评估组别对多维结果[[Construct\|构念]]的影响 | 需满足多元正态性与协方差矩阵同质性（Box's M 检验） |
> | 独立样本 [[t-test]] | 1 个分类变量（**严格限定 2 水平**） | 1 个连续变量 | 无 | 检验两组总体均值是否相等 | $t^2 \equiv F$；无法直接扩展至 3 组以上（会膨胀 Type I 错误） |
> | Kruskal-Wallis 检验 | 1 个分类变量（$\ge 2$ 水平） | 1 个连续或等级变量 | 无 | ANOVA 前提严重违背时的非参数替代方案（基于秩次） | 仅检验中位数/分布位置，统计功效略低于满足正态假定的 ANOVA |
> | [[Chi-Squared Test\|卡方检验]] | 1 个或 2 个分类变量 | 分类/类别因变量（频数） | 无 | 检验分类特征间的独立性或比例吻合度 | 仅处理频数计数，不处理连续数值均值 |

---

## 人机交互中的认识论审问与公式辨析案例

在借助[[Generative Artificial Intelligence|生成式人工智能]]（ChatGPT）推导和应用统计公式时，不同的[[Epistemic Stances|认识立场]]会引导出截然不同的认知加工模式（[[Argument_Wu_2025_ER|Wu et al., 2025, pp. 362–365]]）：

> [!case] Case 2: Student B —— 单因素方差分析[[Effect Size\|效应量]] $\omega^2$ 公式辨析与多元论探索（[[Argument_Wu_2025_ER\|Wu et al., 2025]]）
> - **任务背景** 高级统计学[[Homework\|作业]]：计算单因素方差分析（One-Way ANOVA）的总体效应量指标 [[Omega-Squared]]（$\omega^2$）。
> - **人机交互记录复刻**
>   - **学生提问** *"I noticed two different formulas for calculating $\omega^2$ in one-way ANOVA. One is $\omega^2 = \frac{\text{SS}_{\text{between}} - \text{df}_{\text{between}} \times \text{MS}_{\text{error}}}{\text{SS}_{\text{total}} + \text{MS}_{\text{error}}}$, and another is $\omega^2 = \frac{(p - 1)(F - 1)}{(p - 1)(F - 1) + np}$. Why are there two different formulas? Which one should I use?"*
>   - **ChatGPT 回复** *"Both formulas are mathematically equivalent under a balanced design where each of the $p$ groups has [[Sample Size Determination\|sample size]] $n$ (total sample $N = np$). The first formula uses the sums of squares directly from the ANOVA table, while the second formula derives $\omega^2$ directly from the $F$-statistic and sample sizes. Both formulas adjust for the positive sample bias of $\eta^2$..."*
>   - **学生多轮追问** 学生并未追问“哪个公式才是唯一正确答案”，而是进一步追问参数含义：*"In the second formula, what does $p$ represent? Does $n$ refer to the sample size per group or total sample size? How does this formula perform in unbalanced designs?"*
>   - **ChatGPT 回答** 澄清 $p$ 为组数（水平数），$n$ 为单组样本量；在非平衡设计中通常推荐使用基于离差平方和的第一种通用公式。
> - **[[Epistemology\|认识论]]机制诊断** 展现出鲜明的多元论（[[Multiplist]]）特征。学生认识到同一统计学概念在不同[[Document\|文献]]与推导视角下存在多种合法形式，能够主动通过多轮人机追问探究公式背后的等价条件与参数边界，克服了非黑即白的绝对论盲从；但多元论者的局限在于倾向于将所有形式视为“各具合理性”，较少进一步进行排他性优劣裁决或主动寻找极端边界条件进行[[Falsification\|证伪]]。

> [!figure]- 图2：Student B 与 ChatGPT 的交互对话记录（多元论立场）
> ![](https://img.mylikemie.icu/sources/Wu_2025_ER/figures/Wu_2025_ER_Fig2_Student_B_Interaction_Dialog.jpg)

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - [[Experimental Research\|实验研究]]与准实验中比较 3 组或更多组被试在连续数值[[Dependent Variable\|结果变量]]上的平均水平差异（如传统教学法 vs 翻转课堂 vs AI 辅[[Teaching Assistant\|助教]]学的[[Pre-test and Post-test\|后测]]均值对比）。[[Argument_Creswell_2022_SAGE\|(Creswell & Creswell, 2022, Ch8)]]
>   - [[Factorial Design\|因子设计]]中同时检验两个或多个[[Independent Variable\|自变量]]（如教学模式 $\times$ 学习动机水平）对成绩的独立贡献及两者之间是否存在[[Interaction Effect\|交互效应]]。
>   - [[Sample Size Determination\|样本量]]中等以上且经检验满足正态性与方差齐性假定的连续测量数据。
> - **谨慎使用**
>   - 方差不齐（Levene 检验 $p < .05$）：必须报告 Welch's ANOVA 与 Games-Howell 事后检验结果。
>   - 非平衡样本（各组 $n_i$ 差异巨大）：在多因素方差分析中必须采用 Type III 离差平方和（Type III Sum of Squares）以避免主效应与交互效应混淆。
>   - 小样本实验（每组 $n < 10$）：$\eta^2$ 存在严重向上偏倚，必须强制报告 $\omega^2$ 作为无偏估计。[[Argument_Wu_2025_ER\|(Wu et al., 2025, p. 363)]]
> - **不适合使用**
>   - 因[[Variable\|变量]]为名义分类或频数计数（应使用 [[Chi-Squared Test\|卡方检验]] 或 Logistic 回归）。
>   - 严重偏态且无法通过数学变换（对数/平方根）恢复正态的极小样本数据（应使用非参数 Kruskal-Wallis 检验）。
>   - 仅包含 2 个处理组的简单设计（直接使用独立样本 [[t-test]] 更为简便，两者数学等价）。

---

## 局限性

> [!method-limits] 方法局限
> - **整体检验的模糊性** ANOVA 的 $F$ 检验仅为综合检验（Omnibus Test），显著结果仅说明各组均值不全相等，不能直接告知具体是哪些组之间存在差异，必须附加事后多重比较。
> - **多重比较[[Type I and Type II Errors\|第一类错误]]膨胀** 进行两两事后比较时（如 4 组产生 6 次成对比较），若不采用 Bonferroni 或 Tukey 等校正手段，全实验的第一类错误率（Familywise Error Rate, FWER）将急剧膨胀（$\alpha_{\text{total}} = 1 - (1 - 0.05)^6 \approx 26.5\%$）。
> - **对分布[[Hypothesis\|假设]]的敏感性** 极端异常值或严重的方差[[Heterogeneity\|异质性]]会破坏 $F$ 检验的稳健性，导致假阳性率显著上升。
> - **主观[[Effect Size\|效应量]]指标选择偏误** 许多研究者因习惯而报告高估的 $\eta^2$ 而非无偏的 $\omega^2$，在小样本研究中容易夸大干预措施的实际效能。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Analysis of Covariance]] | 扩展方法 | 在 ANOVA 模型中引入连续协[[Variable\|变量]]（如[[Pre-test and Post-test\|前测]]基线分），消除无关混淆变异以提升组间效应检验功效。 |
> | [[Multivariate Analysis of Variance]] | 扩展方法 | 将单一[[Dependent Variable\|因变量]]的 ANOVA 推广至多个相互关联连续因变量的同步组间比较。 |
> | [[t-test]] | 特殊基准方法 | 当自变量仅包含 2 个水平时，独立样本 $t$ 检验与 ANOVA 完全同构（$F = t^2$）。 |
> | [[Chi-Squared Test]] | 对照方法 | 卡方检验处理类别因变量关联；ANOVA 处理连续因变量均值差异。 |
> | [[Factorial Design]] | 关联设计 | 为多因素 ANOVA 提供两因子及以上的正交或平衡实验架构。 |
> | [[Effect Size]] | 补充方法 | 提供 $\eta^2$、$\eta_p^2$ 与 $\omega^2$ 计算，量化处理因素解释因变量变异的实际强度。 |
> | [[Multiplist]] | [[Epistemic Stances\|认识论立场]] | 解释学习者在面对 ANOVA 效应量 $\omega^2$ 多种等价公式时的人机追问与容忍思维。 |
> | [[Metacognition]] | 调控机制 | 监控 ANOVA [[Hypothesis\|假设]]前提（正态性、方差齐性）与效应量指标选择的关键高阶认知机能。 |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research\|相关研究]]索引
> - [[Argument_Creswell_2022_SAGE\|Creswell & Creswell (2022)]] — 阐释方差分析（ANOVA）、[[Analysis of Covariance\|协方差分析]]（ANCOVA）与[[Multivariate Analysis of Variance\|多元方差分析]]（MANOVA）作为[[Experimental Research\|实验研究]]设计中组间均值检验的核心推断统计工具。（Ch8）
> - [[Argument_Wu_2025_ER\|Wu et al. (2025)]] — 实证剖析研究生在计算单因素方差分析[[Effect Size\|效应量]]指标 $\omega^2$ 时，与 ChatGPT 展开公式数学等价性与小样本偏差校正的多轮追问案例。（pp. 362–365）
