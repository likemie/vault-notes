---
title: Measurement Invariance
aliases:
  - 测量等值性
  - 测量等值性检验
  - 测量不变性
  - 测量不变性检验
  - 多组测量等值性
  - 多组测量等值性检验
  - 测量等同性
  - 跨组测量不变性
  - 跨群体测量等值性
  - 测量恒常性
summary: "在多组验证性因子分析（MG-CFA）中检验测量工具在不同群体或时间点是否具有相同测量特性的系统统计方法，按形态等值、弱等值（负荷等值）、强等值（截距等值）和严格等值（残差等值）四个层级递进检验，以确保潜变量跨组均值与关系的有效比较。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 17
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/psychometrics
  - statistics/sem
  - theme/scale-development
related_concepts:
  - "[[Construct]]"
  - "[[Scale of Measurement]]"
  - "[[Variable]]"
  - "[[Sample Size Determination]]"
  - "[[External Validity]]"
  - "[[Construct Validity]]"
  - "[[Cross-cultural Validity]]"
  - "[[Sampling Error]]"
related_theories:
  - "[[Classical Test Theory]]"
related_methods:
  - "[[Confirmatory Factor Analysis]]"
  - "[[Model Fit Indices in SEM and CFA]]"
  - "[[Analysis of Variance]]"
  - "[[Scale Development]]"
  - "[[Multivariate Analysis of Variance]]"
  - "[[Exploratory Factor Analysis]]"
related_instruments:
  - "[[Research Literacy Scale for Teachers]]"
related_facts: []
related_persons: []
related_arguments:
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
confidence: high
status: draft
created: 2026-08-28
updated: 2026-08-30
---

# Measurement Invariance

---

## 定义

> [!def] 方法定义
> **测量等值性（Measurement Invariance, MI）**（亦称测量不变性、测量等同性或测量恒常性）是指在多组[[Confirmatory Factor Analysis|验证性因子分析]]（Multigroup CFA, MG-CFA）中，通过对不同群体（如性别、年龄、文化、地域）或不同时间点的测量模型施加阶梯式参数等值约束，系统检验测量工具是否在所有被试子群体中衡量了完全相同心理[[Construct|构念]]与[[Scale of Measurement|测量尺度]]的统计方法。它是开展跨群体均值比较、结构方程路径对比与跨文化研究的前提性方法论门槛。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, pp. 6–8)]]

> [!method-scope] 方法范围
> - **研究对象** 嵌套在不同人口学（如性别、种族、教龄）、文化背景（跨国测验如 PISA/TIMSS）或纵向追踪时点（Longitudinal Invariance）的多组观测协方差与均值向量结构。
> - **问题类型** 检验测量工具是否存在跨群体测量偏倚（Measurement Bias）、项目功能差异（Differential Item Functioning, DIF）或文化特异性理解偏差；判定跨组均值与路径系数比较的合法性。
> - **分析单位** 多组独立样本的观测[[Variable|变量]]、潜变量因子载荷、测量截距与测量残差方差。
> - **输出形式** 形态、弱、强、严格四阶段嵌套模型的拟合指数矩阵（$\chi^2$、$df$、[[Model Fit Indices in SEM and CFA|RMSEA]]、SRMR、CFI）及其改变量（$\Delta\text{CFI}$、$\Delta\text{RMSEA}$）。

> [!citation-card]- 关键定义
> 测量等值性确立了量表在不同子群体中具有相同的测量意义与单位。只有当强等值（截距等值）成立时，跨组潜变量均值比较才具有实质解释力；否则观测到的群体均值差异可能仅仅源于题项反应偏差而非真实的特质水平差异。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, pp. 6–7)]]
>
> *Measurement invariance evaluates whether an instrument measures the same construct across different groups. Establishing scalar invariance is a necessary prerequisite for meaningful latent mean comparisons.*

---

## 方法定位

> [!method-position] 认识论与方法定位
> - **知识观** 建立在现代潜变量测量理论之上：主张观测得分的跨组差异不仅受潜变量真实水平驱动，更可能受到题项表述偏倚、文化反应定势（Response Style）或测量参数异质性的系统污染。
> - **研究者角色** 研究者在开展任何跨组均值检验（如 $t$ 检验、[[Analysis of Variance|ANOVA]]、[[Multivariate Analysis of Variance|MANOVA]]）或跨组结构方程模型（SEM）路径比较前，**必须先行确立测量等值性**；未经等值性检验的直接跨组比较在方法论上属于非法推论（Comparison Fallacy）。
> - **有效性标准** 
>   - 比较因子协方差/回归路径：需达到**弱等值（Metric Invariance）**；
>   - 比较潜变量均值/方差分析：需达到**强等值（Scalar Invariance）**或部分强等值；
>   - 直接使用简易加总总分比较：需达到**严格等值（Strict Invariance）**。
> - **不声称回答的问题** 测量等值性仅检验测量尺度本身的跨组同质性，不能解释为何某群体潜变量水平显著高于另一群体（群体间真实水平差异由后续实质性因果模型解释）。

---

## 四阶段等值阶梯与推论权限

> [!contrast-table] 测量等值性的四阶递进模型与推论权限
> | 等值阶梯 | 模型约束条件 | 心理测量学含义 | 解锁的统计推论权限 |
> |---|---|---|---|
> | **1. 形态等值<br>（Configural Invariance）** | 无跨组参数约束；各组仅保持**相同的因子构型与题项归属**。 | 基线结构等值：不同群体使用相同的概念框架理解[[Construct\|构念]]维度。 | 确认量表的维度划分在各组中普遍适用，但不允许跨组进行任何数值比较。 |
> | **2. 弱等值 / 负荷等值<br>（Metric / Weak Invariance）** | 约束各组对应题项的因子载荷跨组相等（$\boldsymbol{\Lambda}^{(1)} = \boldsymbol{\Lambda}^{(2)}$）。 | 测量单位等值：潜[[Variable\|变量]]每变动一个单位，各组题项观测分的变动幅度完全一致。 | 允许跨组比较潜变量方差、协方差、相关系数及结构方程回归系数。 |
> | **3. 强等值 / 截距等值<br>（Scalar / Strong Invariance）** | 在弱等值基础上，进一步约束各题项的测量截距跨组相等（$\boldsymbol{\tau}^{(1)} = \boldsymbol{\tau}^{(2)}$）。 | 测量零点/原点等值：在潜变量水平相同时，不同群体的题项期望观测得分完全相同（无系统偏倚）。 | 允许跨组比较潜变量的均值差异（Latent Mean Comparisons / [[Analysis of Variance\|ANOVA]]）。 |
> | **4. 严格等值 / 残差等值<br>（Strict Invariance）** | 在强等值基础上，进一步约束各题项的测量残差与误差方差跨组相等（$\boldsymbol{\Theta}^{(1)} = \boldsymbol{\Theta}^{(2)}$）。 | 测量精度完全等值：测量误差在各组中完全均等。 | 允许直接使用量表简易加总分/均分进行跨群体 $t$ 检验或方差分析。 |

---

## 数学原理与测量方程

> [!formula-step] 公式步骤一　多组验证性因子分析测量基本方程
> $$\boldsymbol{x}_g = \boldsymbol{\tau}_g + \boldsymbol{\Lambda}_g \boldsymbol{\xi}_g + \boldsymbol{\delta}_g$$
>
> **这个公式在做什么** 将第 $g$ 组被试在题项上的观测得分向量 $\boldsymbol{x}_g$，分解为题项截距向量 $\boldsymbol{\tau}_g$、因子载荷矩阵与潜变量向量之积 $\boldsymbol{\Lambda}_g \boldsymbol{\xi}_g$ 以及测量残差误差向量 $\boldsymbol{\delta}_g$。
>
> **符号说明**
> - $g$：组别标识（如 $g = 1$ 男性，$g = 2$ 女性）。
> - $\boldsymbol{\tau}_g$：第 $g$ 组题项截距向量（表示当潜变量 $\boldsymbol{\xi}=0$ 时观测指标的基线期望值）。
> - $\boldsymbol{\Lambda}_g$：第 $g$ 组因子载荷矩阵（度量潜变量对观测指标的斜率驱动强度）。
> - $\boldsymbol{\xi}_g$：第 $g$ 组潜在特质构念向量（潜在均值为 $\boldsymbol{\kappa}_g$，协方差为 $\boldsymbol{\Phi}_g$）。
> - $\boldsymbol{\delta}_g$：第 $g$ 组测量误差向量（误差协方差矩阵为 $\boldsymbol{\Theta}_g$）。
>
> **数学直觉** 只有当两组的斜率（$\boldsymbol{\Lambda}_1 = \boldsymbol{\Lambda}_2$）与截距（$\boldsymbol{\tau}_1 = \boldsymbol{\tau}_2$）完全相同时，观测指标均值的差异（$\bar{\boldsymbol{x}}_1 - \bar{\boldsymbol{x}}_2$）才完全等于潜变量真实均值的差异（$\boldsymbol{\kappa}_1 - \boldsymbol{\kappa}_2$）。否则，观测得分的组间差异将被不同组别的截距偏倚（$\boldsymbol{\tau}_1 - \boldsymbol{\tau}_2$）严重污染。

> [!formula-step] 公式步骤二　嵌套模型拟合改变量决策公式（Cheung & Rensvold 与 Chen 标准）
> $$\Delta\text{CFI} = \text{CFI}_{\text{restricted}} - \text{CFI}_{\text{base}}, \quad \Delta\text{RMSEA} = \text{RMSEA}_{\text{restricted}} - \text{RMSEA}_{\text{base}}$$
>
> **为什么不用传统卡方差（$\Delta\chi^2$）检验** 
> 传统卡方差异检验对[[Sample Size Determination|样本量]]极度敏感。在大样本（$N > 200$）下，哪怕参数仅存在微不足道的微弱差异，$\Delta\chi^2$ 也会呈统计学显著（$p < .05$），从而导致严重的过度拒绝（Type I 错误膨胀）。因此，现代心理测量学全面采用实际拟合指数的改变量作为稳健决策标准。
>
> **判定门槛**
> - **Cheung & Rensvold (2002) 准则** $|\Delta\text{CFI}| \le .010$ 且 $|\Delta\text{NNFI}| \le .010$ 时，约束模型成立。
> - **Chen (2007) 综合样本量准则** 
>   - 弱等值检验：$|\Delta\text{CFI}| \le .010$ 且 $\Delta\text{RMSEA} \le .015$（$\Delta\text{SRMR} \le .030$）；
>   - 强等值与严格等值检验：$|\Delta\text{CFI}| \le .010$ 且 $\Delta\text{RMSEA} \le .015$（$\Delta\text{SRMR} \le .015$）。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 12)]]

---

## 检验流程与部分等值性策略

> [!proc] 测量等值性检验标准决策流
> ```mermaid
> flowchart TD
>   A["建立多组基线模型（形态等值）"] --> B{"形态等值拟合良好？"}
>   B --"否"--> C["修正因子构型或剔除跨组不稳定题项"]
>   B --"是"--> D["约束因子载荷跨组相等（弱等值）"]
>   D --> E{"|ΔCFI| ≤ .010 且 ΔRMSEA ≤ .015？"}
>   E --"否"--> F["检验部分弱等值：释放载荷差异最大的题项"]
>   E --"是"--> G["解锁潜变量方差/协方差/回归路径比较权限"]
>   G --> H["进一步约束测量截距跨组相等（强等值）"]
>   H --> I{"|ΔCFI| ≤ .010 且 ΔRMSEA ≤ .015？"}
>   I --"否"--> J["检验部分强等值：释放截距差异最大的题项 (需保证≥2题严格等值)"]
>   I --"是"--> K["解锁跨组潜变量均值比较权限 (Latent Mean ANOVA)"]
>   K --> L["进一步约束残差方差跨组相等（严格等值）"]
>   L --> M{"严格等值成立？"}
>   M --"是"--> N["允许直接使用简易加总总分开展跨组比较"]
>   M --"否"--> O["仅使用潜变量均值进行组间推断"]
> ```

> [!warning] 部分测量等值性（Partial Invariance）操作规范
> 当全等值模型（Full Invariance）被拒绝时，研究者可依据修正指数（Modification Indices, MI）逐步释放非等值题项的约束（Byrne et al., 1989; Steenkamp & Baumgartner, 1998）：
> 1. **最低保留门槛** 每个潜变量必须保留至少 **2 个跨组严格等值的题项**（1 个参考指标 + 1 个非基准指标）；
> 2. **推论权限限定** 若达到部分强等值（Partial Scalar Invariance），仍被允许开展跨组潜变量均值比较，但不可使用简易总分比较。

---

## 软件实现与代码规程

> [!software-impl] R 语言 (`lavaan` + `semTools`) 多组 CFA 测量等值性完整代码
> ```R
> library(lavaan)
> library(semTools)
> 
> # 1. 定义测量模型语法
> cfa_model <- '
>   Awareness =~ R1 + R2 + R3 + R4
>   Attitude  =~ R5 + R6 + R7
>   Skills    =~ R8 + R9 + R10 + R11 + R12 + R13
>   Usage     =~ R14 + R15 + R16 + R17 + R18 + R19 + R20
> '
> 
> # 2. 执行阶梯等值性检验 (形态 -> 弱 -> 强 -> 严格)
> # 形态等值 (Configural)
> fit_config <- cfa(cfa_model, data = my_data, group = "gender")
> 
> # 弱等值 (Metric: 约束 loadings)
> fit_metric <- cfa(cfa_model, data = my_data, group = "gender", group.equal = "loadings")
> 
> # 强等值 (Scalar: 约束 loadings + intercepts)
> fit_scalar <- cfa(cfa_model, data = my_data, group = "gender", group.equal = c("loadings", "intercepts"))
> 
> # 严格等值 (Strict: 约束 loadings + intercepts + residuals)
> fit_strict <- cfa(cfa_model, data = my_data, group = "gender", group.equal = c("loadings", "intercepts", "residuals"))
> 
> # 3. 提取拟合改变量对比表
> anova_tab <- anova(fit_config, fit_metric, fit_scalar, fit_strict)
> fitMeasures(fit_config, c("cfi", "rmsea", "srmr"))
> fitMeasures(fit_metric, c("cfi", "rmsea", "srmr"))
> fitMeasures(fit_scalar, c("cfi", "rmsea", "srmr"))
> fitMeasures(fit_strict, c("cfi", "rmsea", "srmr"))
> ```

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 在《[[Research Literacy Scale for Teachers|教师研究素养量表]]》的实证检验中，对男性（$n=77$）与女性（$n=181$）教师执行跨性别 MG-CFA，形态等值（$\text{CFI}=.907$）、弱等值（$\Delta\text{CFI}=-.001$）、强等值（$\Delta\text{CFI}=+.003$）与严格等值（$\Delta\text{CFI}=.000$）全部完全满足 $|\Delta\text{CFI}| \le .010$ 标准，实证确立了跨性别严格测量不变性，为男女教师研究素养均值无偏比较提供了基石。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Scale Development]] | 宏观方法 | 测量等值性是量表编制第三阶段确立工具[[External Validity\|可推广性]]与跨组可比性的核心程序。 |
> | [[Confirmatory Factor Analysis]] | 基础方法 | 多组 CFA 是执行测量等值性参数估计与约束对比的底层建模工具。 |
> | [[Model Fit Indices in SEM and CFA]] | 评价指标 | 提供 $\Delta\text{CFI}$ 与 $\Delta\text{RMSEA}$ 等核心判定参数。 |
> | [[Construct Validity]] | 理论概念 | 跨组不变性是构念效度在多群体环境下的延伸与必要验证。 |
> | [[Cross-cultural Validity]] | 效度类型 | 跨文化比较研究中确立跨国测量等同性的必要前提。 |
> | [[Multivariate Analysis of Variance]] | 后续分析 | 只有在满足强等值（Scalar）后，多变量方差分析的均值比较才具有合法解释力。 |
> | [[Research Literacy Scale for Teachers]] | 测量工具 | 完整通过跨性别四阶测量等值性检验的量表编制典范。 |
