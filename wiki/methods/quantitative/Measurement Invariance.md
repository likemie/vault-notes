---
title: Measurement Invariance
aliases:
  - 测量等值性
  - 测量不变性
  - 多组测量等值性
  - 测量等同性
  - 跨组测量不变性
summary: "在多组验证性因子分析（MG-CFA）中检验测量工具在不同群体或时间点是否具有相同测量特性的系统统计方法，按形态等值、弱等值（负荷等值）、强等值（截距等值）和严格等值（残差等值）四个层级递进检验，以确保潜变量跨组均值与关系的有效比较。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 5
method_related_level: 0
method_related_stars: ""
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/psychometrics
  - statistics/sem
  - theme/scale-development
related_concepts:
  - "[[Construct Validity]]"
related_theories: []
related_methods:
  - "[[Confirmatory Factor Analysis]]"
  - "[[Scale Development]]"
related_instruments:
  - "[[Research Literacy Scale for Teachers]]"
related_arguments:
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
confidence: high
status: draft
created: 2026-08-28
updated: 2026-08-28
---

# Measurement Invariance

---

## 定义

> [!def] 方法定义
> **测量等值性（Measurement Invariance, MI）**（亦称测量不变性或测量等同性）是指在多组[[Confirmatory Factor Analysis|验证性因子分析]]（Multigroup CFA, MG-CFA）中，通过对不同群体（如性别、年龄、文化、地域）或不同时间点的测量模型施加阶梯式参数等值约束，系统检验测量工具是否在所有被试子群体中衡量了完全相同心理构念与测量尺度的统计方法。它是开展跨群体均值比较、结构方程路径对比与跨文化研究的前提性方法论门槛。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, pp. 6–8)]]

> [!method-scope] 方法范围
> - **研究对象** 嵌套在不同人口学、文化或时间分组之下的多组协方差与均值结构矩阵。
> - **问题类型** 检验测量工具是否跨群体存在测量偏差（Measurement Bias）或项目功能差异（Differential Item Functioning, DIF）、确立跨组比较合法性。
> - **分析单位** 多组独立样本的观测变量与潜变量参数结构。
> - **输出形式** 形态、弱、强、严格四阶段嵌套模型的拟合指数矩阵（$\chi^2$、$df$、RMSEA、SRMR、CFI）及其改变量（$\Delta\text{CFI}$、$\Delta\text{RMSEA}$）。

> [!citation-card]- 关键定义
> 测量等值性确立了量表在不同子群体中具有相同的测量意义与单位。只有当强等值（截距等值）成立时，跨组潜变量均值比较才具有实质解释力；否则观测到的群体均值差异可能仅仅源于题项反应偏差而非真实的特质水平差异。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, pp. 6–7)]]
>
> *Measurement invariance evaluates whether an instrument measures the same construct across different groups. Establishing scalar invariance is a necessary prerequisite for meaningful latent mean comparisons.*

---

## 四阶段等值阶梯与推论权限

> [!contrast-table] 测量等值性的四阶递进模型与推论权限
> | 等值阶梯 | 模型约束条件 | 心理测量学含义 | 解锁的统计推论权限 |
> |---|---|---|---|
> | **1. 形态等值<br>（Configural Invariance）** | 无跨组参数约束；各组仅保持**相同的因子构型与题项归属**。 | 基线结构等值：不同群体使用相同的概念框架理解构念维度。 | 确认量表的维度划分在各组中普遍适用，但不允许跨组进行任何数值比较。 |
> | **2. 弱等值 / 负荷等值<br>（Metric / Weak Invariance）** | 约束各组对应题项的因子载荷跨组相等（$\boldsymbol{\Lambda}^{(1)} = \boldsymbol{\Lambda}^{(2)}$）。 | 测量单位等值：潜变量每变动一个单位，各组题项观测分的变动幅度完全一致。 | 允许跨组比较潜变量方差、协方差、相关系数及结构方程回归系数。 |
> | **3. 强等值 / 截距等值<br>（Scalar / Strong Invariance）** | 在弱等值基础上，进一步约束各题项的测量截距跨组相等（$\boldsymbol{\tau}^{(1)} = \boldsymbol{\tau}^{(2)}$）。 | 测量零点/原点等值：在潜变量水平相同时，不同群体的题项期望观测得分完全相同（无系统偏倚）。 | 允许跨组比较潜变量的均值差异（Latent Mean Comparisons / ANOVA）。 |
> | **4. 严格等值 / 残差等值<br>（Strict Invariance）** | 在强等值基础上，进一步约束各题项的测量残差与误差方差跨组相等（$\boldsymbol{\Theta}^{(1)} = \boldsymbol{\Theta}^{(2)}$）。 | 测量精度完全等值：测量误差在各组中完全均等。 | 允许直接使用量表简易加总分/均分进行跨群体 $t$ 检验或方差分析。 |

---

## 判定标准与评价公式

> [!formula-step] 公式步骤　多组嵌套模型拟合改变量（Cheung & Rensvold 与 Chen 标准）
> $$\Delta\text{CFI} = \text{CFI}_{\text{restricted}} - \text{CFI}_{\text{base}}, \quad \Delta\text{RMSEA} = \text{RMSEA}_{\text{restricted}} - \text{RMSEA}_{\text{base}}$$
>
> **这个公式在做什么** 计算在施加更严格等值约束（受限模型）相对于前一阶段等值模型（基准模型）时，比较拟合指数（CFI）与近似误差均方根（RMSEA）的变化幅度。
>
> **为什么不用传统卡方差（$\Delta\chi^2$）检验** 
> 传统卡方差异检验对样本量极度敏感。在大样本（$N > 200$）下，哪怕参数仅存在微不足道的微弱差异，$\Delta\chi^2$ 也会呈统计学显著（$p < .05$），从而导致严重的过度拒绝（Type I 错误膨胀）。因此，现代心理测量学全面采用实际拟合指数的改变量作为稳健决策标准。
>
> > [!result-reading]- 结果判定门槛
> > - **Cheung & Rensvold 准则** 满足 $|\Delta\text{CFI}| \le .010$ 且 $|\Delta\text{NNFI}| \le .010$ 时，约束模型成立，等值性获得实证支持。
> > - **Chen 综合样本量准则** 当样本量 $N > 300$ 时：
> >   - 弱等值检验：$|\Delta\text{CFI}| \le .010$ 且 $\Delta\text{RMSEA} \le .015$（$\Delta\text{SRMR} \le .030$）；
> >   - 强等值与严格等值检验：$|\Delta\text{CFI}| \le .010$ 且 $\Delta\text{RMSEA} \le .015$（$\Delta\text{SRMR} \le .015$）。

---

## 软件实现与代码规程

> [!software-impl] R 语言多组验证性因子分析测量等值性代码
> ```R
> library(lavaan)
> library(semTools)
> 
> # 1. 定义多维度测量模型
> model <- '
>   Awareness =~ R1 + R2 + R3 + R4
>   Attitude  =~ R5 + R6 + R7
>   Skills    =~ R8 + R9 + R10 + R11 + R12 + R13
>   Usage     =~ R14 + R15 + R16 + R17 + R18 + R19 + R20
> '
> 
> # 2. 使用 semTools 执行自动化四阶段阶梯检验
> inv_res <- measurementInvariance(model = model, data = sample_data, 
>                                  group = "gender", estimator = "MLR")
> 
> # 3. 提取嵌套比较拟合指数表格
> print(inv_res)
> ```

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 在《[[Research Literacy Scale for Teachers|教师研究素养量表]]》的实证检验中，对男性（$n=70$）与女性（$n=188$）教师执行跨性别 MG-CFA，形态等值（$\text{CFI}=.907$）、弱等值（$\Delta\text{CFI}=.001$）、强等值（$\Delta\text{CFI}=-.003$）与严格等值（$\Delta\text{CFI}=.000$）全部完全满足 $|\Delta\text{CFI}| \le .010$ 标准，实证确立了跨性别严格测量不变性。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Scale Development]] | 宏观方法 | 测量等值性是量表编制第三阶段确立工具可推广性与跨组可比性的核心程序。 |
> | [[Confirmatory Factor Analysis]] | 基础方法 | 多组 CFA 是执行测量等值性参数估计与约束对比的底层建模工具。 |
> | [[Construct Validity]] | 理论概念 | 跨组不变性是构念效度在多群体环境下的延伸与必要验证。 |
> | [[Research Literacy Scale for Teachers]] | 测量工具 | 完整通过跨性别四阶测量等值性检验的量表编制典范。 |
