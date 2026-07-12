---
title: Binary Logistic Regression
aliases: [二元逻辑回归, Binary Logistic Regression Model, 二元逻辑回归模型]
summary: "一种用于预测二分类因变量（如是否陪读、是否择校）的统计分析方法，通过 Logit 变换将因变量的发生概率（Odds）转换为线性模型，用以估计各预测变量的优势比（Odds Ratio, Exp(B)）并检验其统计显著性。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 3
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/regression
related_concepts:
  - "[[Variable]]"
  - "[[Statistical Significance]]"
  - "[[Study Population and Sample]]"
  - "[[Standard Error]]"
  - "[[Epistemology]]"
  - "[[Positivism]]"
  - "[[Hypothesis]]"
  - "[[Causality]]"
  - "[[Confidence Interval]]"
  - "[[Sample Size Determination]]"
related_theories: []
related_methods:
  - "[[Quantitative Research]]"
  - "[[Mixed Methods Research]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Longitudinal Study]]"
  - "[[Multiple Regression]]"
  - "[[Qualitative Interview]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Peidu]]"
related_arguments:
  - "[[Argument_Teng_2025_CE]]"
confidence: high
status: draft
created: 2026-07-12
updated: 2026-07-12
---

# Binary Logistic Regression

---

## 定义

> [!def] 方法定义
> 二元 Logistic 回归模型（Binary Logistic Regression Model）是一种专门用于因[[Variable|变量]]为二分类变量（Binary/Dichotomous Variable，例如是否[[Peidu|陪读]]、是否录取、是否流失）的广义线性回归分析方法。它通过 Logit 变换，将因变量发生的概率与不发生概率之比的对数（即 Logit 变换值）表示为自变量的线性组合，并在不受自变量分布限制的情况下，估计各预测因子的优势比（Odds Ratio, OR）并检验其[[Statistical Significance|统计显著性]]。

> [!method-scope] 方法范围
> - **研究对象** 二分类分类变量与一组连续或分类自变量之间的统计预测关系。
> - **问题类型** 适合回答预测、影响因素筛选、发生比测度以及自变量对行为选择的预测力检验。
> - **分析单位** 个体、家庭、学校、组织等微观或宏观[[Study Population and Sample|研究样本]]。
> - **输出形式** 回归系数（B）、[[Standard Error|标准误]]（SE）、华氏统计量（Wald）、显著性水平（p值）、优势比（Exp(B) / Odds Ratio）以及模型整体的拟合优度指标。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 基于概率论和[[Positivism|实证主义]]，认为社会选择行为在群体层面上遵循特定的概率分布规律，可以通过数学模型加以测度和预测。
> - **研究者角色** 模型构建与参数解释者。研究者需基于理论[[Hypothesis|假设]]选择自[[Variable|变量]]与控制变量，指定参照组，并进行共线性诊断以避免过拟合。
> - **有效性标准** 统计结论效度（显著性水平）、模型拟合优度（如 Nagelkerke $R^2$ 或 Hosmer-Lemeshow 检验的 p 值）、预测准确率以及共线性指标（VIF）。
> - **不声称回答的问题** 该模型本身无法直接推导[[Causality|因果]]方向。若使用横截面数据，显著的回归系数仅代表预测因子与因变量之间的关联，不能排除反向因果或遗漏变量偏误。

> [!method-stack] 方法层级
> - **研究设计** [[Quantitative Research|量化研究]]、[[Mixed Methods Research|混合方法研究]]（解释性顺序设计）。
> - **数据收集** 问卷调查、行政登记数据、大规模统计调查等。
> - **分析方法** 最大似然估计（Maximum Likelihood Estimation, MLE）、Logit 变换、优势比计算。
> - **辅助技术** 多重共线性诊断（VIF）、分类截断值敏感性检验。

---

## 研究程序

> [!proc] 量化分析程序
> 1. **明确因[[Variable|变量]]和参考组** 将二分类因变量[[Coding in Qualitative Research|编码]]为 0 和 1（1 代表目标事件发生，0 代表未发生），并为分类自变量指定合理的参照组。
> 2. **筛选自变量与共线性诊断** 依据理论筛选自变量，并通过相关系数矩阵或方差膨胀因子（VIF）检验，确保预测变量间不存在严重的多重共线性。
> 3. **模型估计与求解** 代入分析数据，采用最大似然估计法计算各变量的回归系数 $B$、[[Standard Error|标准误]] $SE$ 及其指数化后的优势比 $Exp(B)$。
> 4. **模型拟合与诊断** 通过似然比检验评估模型整体显著性，采用 Hosmer-Lemeshow 检验诊断拟合程度，并计算 Pseudo $R^2$ 评估解释力。
> 5. **结果汇报与解释** 汇报优势比 $Exp(B)$ 及其 95% [[Confidence Interval|置信区间]]。若 $Exp(B) > 1$，说明自变量增加（或相对于参照组）会提升目标事件发生的发生比；若 $Exp(B) < 1$，则说明降低发生比。

---

## 量化方法模块

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** 横截面数据（Cross-sectional Data）、时点统计数据或[[Longitudinal Study|纵向调查]]数据。
> - **样本与单位** 通常要求较大的[[Sample Size Determination|样本量]]（每个自变量对应的最少事件数一般推荐为 10–20 个），分析单位为个体、家庭或学校。
> - **变量或指标** 因变量为二分类（0/1）变量；自变量可为连续变量或分类变量（引入虚拟变量）。
> - **模型或统计量** 回归系数（B）、优势比（Exp(B)）、Wald $\chi^2$ 统计量、Pseudo $R^2$。
> - **诊断与检验** Hosmer-Lemeshow 拟合优度检验、VIF 共线性诊断、异常值诊断（如 Cook's 距离）。

> [!formula-step] 公式一　二元 Logistic 回归模型与 Logit 变换
> $$\ln\left(\frac{P}{1 - P}\right) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k$$
>
> **这个公式在做什么** 将事件发生的概率 $P$ 进行 Logit 变换，将其取值范围从 $(0, 1)$ 映射到整个实数集 $(-\infty, +\infty)$，从而使右侧的自变量线性组合可以正常进行回归拟合。
>
> **符号说明** 
> - $P$：目标事件发生的概率（例如家庭选择进城[[Peidu|陪读]]的概率）。
> - $1 - P$：目标事件不发生的概率。
> - $\frac{P}{1 - P}$：发生比（Odds）。
> - $\beta_0$：常数项（截距）。
> - $\beta_i$：自变量 $X_i$ 的回归系数。
>
> **数学直觉** 由于概率 $P$ 只能在 0 到 1 之间，直接对其进行线性回归拟合会突破概率的物理边界。通过计算发生比 $\frac{P}{1 - P}$，可将范围扩展到 $(0, +\infty)$；进一步取自然对数后，其取值范围变为了整个实数集。这确保了线性拟合的有效性。
>
> **结果怎么读** 当自变量 $X_i$ 增加 1 个单位时，在控制其他变量不变的前提下，发生比的对数（Log-odds）增加 $\beta_i$ 个单位。

> [!formula-step] 公式二　优势比（Odds Ratio, OR）与概率预测
> $$\text{Odds Ratio} = \text{Exp}(\beta_i) = e^{\beta_i}$$
> $$P = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X_1 + \dots + \beta_k X_k)}}$$
>
> **这个公式在做什么** 第一个公式将回归系数 $\beta_i$ 转换为更容易直观解释的优势比（Odds Ratio, OR，即 $Exp(B)$）；第二个公式根据估计出的模型系数直接预测特定样本发生目标事件的概率 $P$。
>
> **符号说明** 
> - $\text{Exp}(\beta_i)$ 或 $e^{\beta_i}$：优势比（Odds Ratio, OR），即 $X_i$ 每增加一个单位（或相对于参照组）时，目标事件发生比发生的变化倍数。
> - $e$：自然对数的底数（约等于 2.718）。
>
> **结果怎么读** 
> - 若 $\text{Exp}(\beta_i) > 1$，说明该自变量是目标事件发生的促进因素，发生比变为原来的 $\text{Exp}(\beta_i)$ 倍。
> - 若 $\text{Exp}(\beta_i) < 1$，说明该自变量是阻碍因素，发生比降低。
> - 若 $\text{Exp}(\beta_i) = 1$，说明该自变量对发生比无影响。
>
> > [!math-principle] 核心统计量与估计原理的实证理解
> > - **回归系数 $\beta$ 的估计（极大似然估计 MLE）** 
> >   由于二元分类的非线性特征，Logistic 回归不使用普通最小二乘法（OLS）进行拟合，而是采用最大似然估计（Maximum Likelihood Estimation, MLE）。其数学逻辑是：软件通过多次迭代，寻找一组最优的回归系数，使得在该参数设定下，整个样本中所有观测个体实际被观察到的选择概率的乘积（似然值）达到最大。该组系数是让模型预测与真实观测最吻合的数学最优解。
> > - **回归系数 $\beta$ 与优势比 $\text{Exp}(B)$ 的数学关系** 
> >   自变量每增加一单位，因变量发生比的对数 $\ln(P/(1-P))$ 变动 $\beta$。由于对数尺度不直观，我们对其进行指数化（即求 $e^{\beta}$）来转化为优势比（Odds Ratio, OR，即软件输出的 $\text{Exp}(B)$）。它代表自变量增加一单位时，事件发生比变为原来的多少倍。当 $\text{Exp}(B) > 1$（$\beta > 0$）时，为正向影响；当 $\text{Exp}(B) < 1$（$\beta < 0$）时，为负向影响。
> > - **[[Multiple Regression|多元回归]]中的“控制效应”** 
> >   每一个自变量的回归系数（或 OR 值）代表的均是**在控制模型中其他所有自变量完全固定不变的前提下**，该变量的独立预测净贡献。这排除了混杂因素的干扰，计算出各个变量的纯净效果。
> > - **常数项（Constant）与“极端参照组”** 
> >   常数项 $\beta_0$ 代表当**模型中所有自变量均取值为 $0$ 时**，因变量对数发生比的基准值。这在实证研究中共同构建了一个处于最不利资源或最基础状态的“极端参照组”（Extreme Reference Group）。常数项折算的基准概率 $P_0 = e^{\beta_0}/(1 + e^{\beta_0})$ 反映了在没有其他任何资本优势和外部推力下的决策发生底线，不能将其等同于无条件下的全样本平均概率。
> > - **华氏检验（Wald Test）与显著性星号** 
> >   表格中回归系数旁的星号（如 $*p < 0.05$）是通过 Wald 检验计算的。其统计量计算为 $W = (\beta / SE)^2$。当 $Z = \beta / SE$ 的绝对值大于 $1.96$（即双尾检验 $95\%$ 置信度）时，即可拒绝“该变量系数在总体中为 0”的虚无假设。星号代表该效应稳定存在，并非由于抽样误差偶然产生。
> > - **拟合优度（Pseudo $R^2$）的社会科学解读** 
> >   由于无法计算传统线性回归的 $R^2$，Logistic 回归采用 Pseudo $R^2$（如 Nagelkerke $R^2$）来评估模型整体解释力。在社会学微观行为和决策研究中，**Pseudo $R^2$ 处于 0.2 到 0.4 之间即可视为极佳的拟合度**。人类行为极其复杂，包含大量不可控或未测量的随机/主观因素，能用几个核心结构性变量解释 20% 以上的决策变动就已是非常强有力的实证发现。
>
> > [!software-impl] 软件实现
> - **数据处理** 对分类自变量进行虚拟变量（Dummy Variable）[[Coding in Qualitative Research|编码]]并指定参照组，自变量标准化（若需比较不同量纲的系数）。
> - **推荐软件** SPSS, R, Stata, Python。
> - **核心包或命令** 
>   - R: `glm(y ~ x1 + x2, family = binomial(link = "logit"), data)`
>   - Stata: `logit y x1 x2` 或 `logistic y x1 x2`
>   - SPSS: `Analyze -> Regression -> Binary Logistic`
>   - Python: `statsmodels.formula.api.logit` 或 `sklearn.linear_model.LogisticRegression`
> - **报告标准** 报告估计值（$B$）、[[Standard Error|标准误]]（$SE$）、Wald $\chi^2$、p值、优势比（$Exp(B)$）及其 95% [[Confidence Interval|置信区间]]，以及模型拟合度（如 Nagelkerke $R^2$ 或 Hosmer-Lemeshow 检验的 $p$ 值）。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 因[[Variable|变量]]是二分类属性变量，自变量可以是连续或分类变量，旨在分析不同因素对选择行为、状态转变的预测效力与相对重要性时。
> - **谨慎使用** [[Sample Size Determination|样本量]]较小（如目标事件发生次数少于 30 次），可能导致模型不稳定，[[Confidence Interval|置信区间]]过宽；或存在严重的自变量多重共线性时。
> - **不适合使用** 因变量是多分类非顺序变量（改用多项 Logistic 回归）或因变量是连续变量（改用多元线性回归）。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 遗漏关键[[Variable|变量]]偏误、多重共线性、因变量分类偏倚。
> - **适用边界** 要求自变量间不存在高度线性相关，且[[Sample Size Determination|样本量]]需满足一定规模。
> - **误用风险** 容易将优势比（OR）直接解释为发生概率的增长倍数。在目标事件发生率较高（如 $>10\%$）时，OR 会高估自变量的影响力，不宜直接等同于比例或概率的增长倍数。
> - **补救方式** 进行共线性检验（VIF）；结合 Hosmer-Lemeshow 检验诊断模型拟合；若事件发生率极高且旨在说明相对风险，可改用 Poisson 回归或 Log-linear 模型。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Variable]] | 概念 | 本方法的核心输入和输出载体，因变量和自变量均由各种类型的变量构成。 |
> | [[Mixed Methods Research]] | 补充方法 | 在混合研究中，回归模型可作为第一阶段量化筛选，后续辅以[[Qualitative Interview\|质性访谈]]以深化对回归系数背后机制的阐释。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Teng_2025_CE|Teng & Wang (2025)]] — 建立三个二元 Logistic 回归模型分析家庭资本（经济、文化、社会资本）对是否[[Peidu|陪读]]、进城陪读以及进入重点小学的预测显著度与优势比 (p.310)。

---

## 模仿与延伸研究设想

> [!pathways] 基于多阶段回归漏斗模型的研究设计设想
> - **设想一 学生参与课外补习（影子教育的层级化资本购买）**
>   - **Model 1（是否补习）** 因[[Variable|变量]] $Y_1 \in \{0, 1\}$。全体样本（$N$）。预测家庭资本如何突破进入补习市场的“第一道门槛”。
>   - **Model 2（补习质量）** 因变量 $Y_2 \in \{0, 1\}$（1 = 昂贵优质的一对一或名师辅导，0 = 低廉的大班或线上辅导）。补习样本（$n_1$）。分析资本在补习市场内部的二次分化。
>   - **Model 3（学科与提分）** 因变量 $Y_3 \in \{0, 1\}$（1 = 数理化等硬核提分主科，0 = 艺术兴趣类或单纯托管）。优质补习样本（$n_2$）。分析资本如何精准转化为升学应试工具。
> - **设想二 大学生毕业出路（分流与体制变现的漏斗模型）**
>   - **Model 1（继续深造 vs 直接就业）** 因变量 $Y_1 \in \{0, 1\}$。全体毕业生（$N$）。检验家庭资本对子女推迟就业、进行学历通胀投资的保护伞效应。
>   - **Model 2（体制内 vs 体制外）** 因变量 $Y_2 \in \{0, 1\}$。直接就业样本（$n_1$）。探讨在经济下行期，家庭背景（尤其是父母的体制内背景）对子女成功进入公务员、国企、事业单位等安全避风港的预测力。
>   - **Model 3（体制层级分化）** 因变量 $Y_3 \in \{0, 1\}$（1 = 省部级/中央企业核心单位，0 = 基层公务员/乡镇事业单位）。体制内样本（$n_2$）。剖析在体制层级深层分化中，社会分层的权力变现与阶层复制机制。
