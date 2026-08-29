---
title: Model Fit Indices in SEM and CFA
aliases:
  - 结构方程模型拟合指数
  - 验证性因子分析拟合指数
  - 模型拟合度指数
  - 模型拟合指数
  - Goodness-of-Fit Indices
  - RMSEA
  - CFI
  - TLI
  - NNFI
  - SRMR
summary: "验证性因子分析与结构方程模型中评估理论假设模型与样本协方差矩阵匹配程度的综合量化指标体系，涵盖绝对拟合指数（χ²/df、RMSEA、SRMR）、增量拟合指数（CFI、TLI/NNFI）与信息准则（AIC、BIC），构成结构确证与竞争模型选择的判定支柱。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 11
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/sem
  - statistics/psychometrics
  - scale-development/validation
related_concepts:
  - "[[Hypothesis]]"
  - "[[Variable]]"
  - "[[Construct Validity]]"
  - "[[Confidence Interval]]"
  - "[[Sample Size Determination]]"
  - "[[Research Literacy]]"
related_theories: []
related_methods:
  - "[[Confirmatory Factor Analysis]]"
  - "[[Causal Modeling]]"
  - "[[Measurement Invariance]]"
  - "[[Scale Development]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
confidence: high
status: draft
created: 2026-08-29
updated: 2026-08-29
---

# Model Fit Indices in SEM and CFA

---

## 定义

> [!def] 方法定义
> **结构方程模型与[[Confirmatory Factor Analysis|验证性因子分析]]拟合指数（Model Fit Indices in [[Causal Modeling|SEM]] and CFA）** 是一套用于检验理论[[Hypothesis|假设]]模型所蕴含的协方差矩阵 $\boldsymbol{\Sigma}(\boldsymbol{\theta})$ 与样本实际观测协方差矩阵 $\mathbf{S}$ 之间吻合程度（Goodness of Fit）的多维度量化评价体系。它弥补了传统卡方拟合优度检验（$\chi^2$）对大样本过度敏感而必然拒绝正确模型的缺陷，为评估测量模型（CFA）与结构路径模型（SEM）的经验合法性提供客观决策标准。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 9)]]

> [!method-scope] 方法范围
> - **研究对象** 验证性因子分析模型（一阶、高阶或双因子结构）、路径分析模型及完全潜[[Variable|变量]]结构方程模型。
> - **问题类型** 测量模型[[Construct Validity|构念效度]]确证、备择竞争模型优选、[[Measurement Invariance|多组测量等值性]]阶梯检验。
> - **分析单位** 协方差矩阵残差与模型自由度。
> - **输出指标族群**
>   1. **绝对拟合指数（Absolute Fit）** 卡方自由度比（$\chi^2/df$）、渐进残差均方和平方根（$\text{RMSEA}$）、标准化残差均方根（$\text{SRMR}$）、拟合优度指数（$\text{GFI}$）；
>   2. **增量/相对拟合指数（Incremental / Relative Fit）** 比较拟合指数（$\text{CFI}$）、Tucker-Lewis 指数（$\text{TLI}$，亦称非规范拟合指数 $\text{NNFI}$）、规范拟合指数（$\text{NFI}$）；
>   3. **简约与信息准则（Parsimony & Information Criteria）** 赤池信息准则（$\text{AIC}$）、贝叶斯信息准则（$\text{BIC}$）。

---

## 核心指标矩阵与判定阈值

> [!contrast-table] 核心拟合指数全景对比与判定阈值
> | 指标族群 | 指标名称（缩写） | 数学公式 / 核心定义 | 优秀标准 | 可接受标准 | 指标特征与核心注意事项 |
> |:---|:---|:---|:---:|:---:|:---|
> | **绝对拟合** | **卡方自由度比**<br>$\chi^2/df$ | $\frac{\chi^2}{df}$ | $< 2.0$ | $< 3.0$（宽松 $< 5.0$） | 消除样本量对卡方的部分线性膨胀，但 $N > 1000$ 时仍易虚警。 |
> | **绝对拟合** | **渐进残差均方和平方根**<br>$\text{RMSEA}$ | $\sqrt{\max\left(0, \frac{\chi^2 - df}{(N-1)df}\right)}$ | $< 0.06$ | $< 0.08$（$> 0.10$ 拒绝） | 度量模型设定误差大小；惩罚复杂模型；应同时报告 90% [[Confidence Interval\|置信区间]]。 |
> | **绝对拟合** | **标准化残差均方根**<br>$\text{SRMR}$ | $\sqrt{\frac{2 \sum \sum (s_{ij} - \hat{\sigma}_{ij})^2}{p(p+1)}}$ | $< 0.05$ | $< 0.08$ | 基于标准化残差协方差矩阵平均偏差，不受模型复杂度惩罚。 |
> | **增量拟合** | **比较拟合指数**<br>$\text{CFI}$ | $1 - \frac{\max(\chi_T^2 - df_T, 0)}{\max(\chi_B^2 - df_B, 0)}$ | $\ge 0.95$ | $\ge 0.90$ | 对比目标模型与独立虚无基线模型；对[[Sample Size Determination\|样本量]]变化高度稳健。 |
> | **增量拟合** | **Tucker-Lewis 指数**<br>$\text{TLI / NNFI}$ | $\frac{\chi_B^2/df_B - \chi_T^2/df_T}{\chi_B^2/df_B - 1}$ | $\ge 0.95$ | $\ge 0.90$ | 包含对模型自由度的显式惩罚；取值可略微突破 1.0。 |
> | **信息准则** | **赤池 / 贝叶斯准则**<br>$\text{AIC / BIC}$ | $-2\ln L + 2k \ / \ -2\ln L + k\ln N$ | — | 越小越好 | 用于**非嵌套模型（Non-nested Models）**之间的相对优劣选拔。 |

---

## 经典公式与数学原理

> [!formula-step] 公式步骤一　RMSEA 渐进残差均方和平方根
> $$\text{RMSEA} = \sqrt{\max\left(0, \frac{\chi^2 - df}{(N - 1)df}\right)}$$
>
> **这个公式在做什么** 计算全人口中目标模型与真实数据协方差矩阵之间的非中心参数误差平方根，并按模型自由度（$df$）进行加权平摊。
>
> **符号说明**
> - $\chi^2$：极大似然估计下的模型拟合卡方值。
> - $df$：模型自由度（$df = \frac{p(p+1)}{2} - q$，$q$ 为估计参数个数）。
> - $N$：[[Sample Size Determination|样本量]]。
>
> **数学直觉** 当自由度 $df$ 很大而卡方接近 $df$ 时（$\chi^2 - df \le 0$），$\text{RMSEA} = 0$，表示完美拟合；当模型引入大量无用自由参数时，自由度 $df$ 下降，分母变小，导致 RMSEA 惩罚性上升。

> [!formula-step] 公式步骤二　CFI 比较拟合指数
> $$\text{CFI} = 1 - \frac{\max(\chi_{\text{target}}^2 - df_{\text{target}}, 0)}{\max(\chi_{\text{null}}^2 - df_{\text{null}}, \chi_{\text{target}}^2 - df_{\text{target}}, 0)}$$
>
> **这个公式在做什么** 度量目标[[Hypothesis|假设]]模型相比于“所有[[Variable|变量]]完全独立”的虚无基线模型（Null Model），改善了多少比例的不拟合度。
>
> **结果怎么读** $\text{CFI} \in [0, 1]$。$\text{CFI} \ge 0.95$ 表明模型解释了基线模型中 $95\%$ 以上的非独立协方差变异，拟合优异。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 9)]]

---

## 判定准则与报告规范

> [!method-position] Hu & Bentler (1999) 双指标组合判定规则
> 传统仅依据单一指数（如 CFI $> .90$）容易导致过高的 II 类错误（接受错误模型）。Hu & Bentler (1999) 蒙特卡洛模拟推荐采用**双指标联合判定策略**
> 1. **组合策略 A** $\text{SRMR} \le 0.08$ 且 $\text{RMSEA} \le 0.06$；
> 2. **组合策略 B** $\text{SRMR} \le 0.08$ 且 $\text{CFI} \ge 0.95$（或 $\text{TLI} \ge 0.95$）。

> [!software-impl] 软件报告规范
> - **R 语言 (`lavaan`)**
>   ```R
>   library(lavaan)
>   fit <- cfa(my_cfa_syntax, data = my_data)
>   fitMeasures(fit, c("chisq", "df", "pvalue", "cfi", "tli", "rmsea", "rmsea.ci.lower", "rmsea.ci.upper", "srmr"))
>   ```
> - **规范报告范例**
>   *“[[Confirmatory Factor Analysis|验证性因子分析]]表明修正后的一阶四因子模型拟合优异：$\chi^2(163) = 316.25, \chi^2/df = 1.94, \text{RMSEA} = 0.060 \ [90\%\text{ CI: } .050, .070], \text{SRMR} = 0.068, \text{CFI} = 0.94, \text{TLI} = 0.93$。”*

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Confirmatory Factor Analysis]] | 核心应用方法 | 运用拟合指数评估测量模型与竞争[[Hypothesis\|假设]]结构的最核心方法载体。 |
> | [[Measurement Invariance]] | 扩展应用 | 依据 $|\Delta\text{CFI}| \le .010$ 与 $\Delta\text{RMSEA} \le .015$ 判定形态、弱、强与严格等值阶梯。 |
> | [[Scale Development]] | 宏观流程 | 在量表编制阶段三中作为确证因子模型与评价题项质量的把关指标。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 在独立样本 2（$N=258$）中对比单因子、一阶四因子与二阶因子模型的拟合指数（$\chi^2/df = 1.94, \text{RMSEA} = 0.060, \text{CFI} = 0.94$），确立教师[[Research Literacy|研究素养]]的二阶高阶因子结构。
