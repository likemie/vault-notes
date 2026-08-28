---
title: Composite Reliability
aliases:
  - 组合信度
  - 复合信度
  - 构念信度
  - construct reliability
  - Raykov rho
  - Dillon-Goldstein rho
summary: "在结构方程模型与验证性因子分析中评估潜变量多指标内部一致性的现代心理测量学指标，基于标准化因子载荷与误差方差精确估计合成信度，克服了 Cronbach alpha 的同质性等权假设局限。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 7
method_related_level: 0
method_related_stars: ""
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/psychometrics
  - statistics/sem
  - theme/scale-development
related_concepts:
  - "[[Construct]]"
  - "[[Internal Consistency]]"
related_theories: []
related_methods:
  - "[[Confirmatory Factor Analysis]]"
  - "[[Scale Development]]"
  - "[[Average Variance Extracted]]"
related_instruments:
  - "[[Research Literacy Scale for Teachers]]"
related_arguments:
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
confidence: high
status: draft
created: 2026-08-28
updated: 2026-08-28
---

# Composite Reliability

---

## 定义

> [!def] 方法定义
> **组合信度（Composite Reliability, CR）**（在结构方程模型中亦称构念信度）是由 Werts, Linn & Jöreskog（1974）以及 Raykov（1997）系统发展的现代心理测量学指标。它基于[[Confirmatory Factor Analysis|验证性因子分析]]（CFA）中各题项的标准化因子载荷与误差方差，精确计算由一组观测指标线性组合而成的[[Construct|潜变量]]的[[Internal Consistency|内部一致性]]信度。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, pp. 6–7)]]

> [!method-scope] 方法范围
> - **研究对象** 潜变量与其测量题项之间的因子载荷（$\lambda_i$）与题项误差方差（$\theta_i$）。
> - **问题类型** 评估不可直接观测潜变量的测量信度、检验多题项合成测度的内在稳定性。
> - **分析单位** 潜变量（Latent Factor）构念层级。
> - **输出形式** 介于 0 到 1 之间的信度系数值（通常保留两位或三位小数，如 $\text{CR} = .87$）。

> [!citation-card]- 关键定义
> 组合信度衡量了潜变量内部所有测度指标的一致性水平。与传统的 Cronbach's $\alpha$ 相比，组合信度不强求各题项具有相等的因子负荷，因而能更准确地反映构念的真实测量信度；通常以 0.70 作为判定信度优良的临界值。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 6)]]
>
> *Composite reliability reflects the shared variance among the observed indicators of a latent construct. Unlike Cronbach's alpha, it does not assume tau-equivalence, providing a more precise and unbiased estimate of internal consistency.*

---

## 方法定位与理论优势

> [!method-position] 认识论与方法定位
> - **知识观** 承认不同测量题项对潜在构念的贡献权重是**异质且不均等**的，高载荷题项对信度的贡献显著大于低载荷题项。
> - **有效性标准** 
>   1. **基本门槛** $\text{CR} \ge .70$（Hair et al., 2010; Bagozzi & Yi, 1988），表明具备优良的内部一致性；
>   2. **探索性研究可接受线** $\text{CR} \ge .60$（Nunnally & Bernstein, 1994）；
>   3. **高精度标准** $\text{CR} \ge .80$，适合用于个体选拔与关键实践决策。
> - **不声称回答的问题** CR 仅评估同维指标内部的一致性，不能代替跨时点重测稳定性（Test-Retest Reliability）或评分者一致性（Inter-rater Reliability）。

> [!contrast-table] 组合信度（CR）vs 传统克隆巴赫系数（Cronbach's $\alpha$）
> | 比较维度 | 传统克隆巴赫系数（Cronbach's $\alpha$） | 现代组合信度（Composite Reliability, CR） |
> |---|---|---|
> | **核心统计假设** | 假定**本质 $\tau$ 等值（Essential Tau-Equivalence）**，即所有题项在潜变量上的真实载荷完全相同（$\lambda_1 = \lambda_2 = \dots = \lambda_k$）。 | 采用**同质性非等权模型（Congeneric Model）**，允许各题项拥有差异化的自由估计载荷（$\lambda_i$）。 |
> | **假设违背的后果** | 当题项因子载荷不相等时，Cronbach's $\alpha$ 会**严重系统性低估**潜变量的真实信度。 | 无偏估计，准确反映由异质载荷题项组合而成的真实构念信度。 |
> | **题项数量敏感性** | 对题项数量极度敏感；即使单题质量很差，只要题项数足够多，$\alpha$ 也会机械膨胀。 | 依赖载荷强度而非机械堆砌题项数，抗数量膨胀能力更强。 |
> | **误差协方差处理** | 假定所有题项误差严格互不相关。 | 在扩展形式中可显式纳入误差协方差项进行精确计算。 |

---

## 数学原理与计算公式

> [!formula-step] 公式步骤　组合信度（CR）标准计算公式
> $$\text{CR} = \frac{\left(\sum_{i=1}^{k} \lambda_i\right)^2}{\left(\sum_{i=1}^{k} \lambda_i\right)^2 + \sum_{i=1}^{k} \theta_i}$$
>
> **这个公式在做什么** 输入潜变量下各题项的标准化因子载荷 $\lambda_i$ 与误差方差 $\theta_i = 1 - \lambda_i^2$，先将所有载荷求和后取平方（代表合成真分数方差），再除以该平方和与各题项误差方差之和的总和（代表总方差）。
>
> **符号说明**
> - $\lambda_i$：第 $i$ 个测度题项的标准化因子载荷（Standardized Factor Loading）。
> - $\theta_i$：第 $i$ 个测度题项的标准化误差方差（Error Variance），在完全标准化解中 $\theta_i = 1 - \lambda_i^2$。
> - $k$：属于该潜变量的题项总数。
>
> **数学直觉** 
> 观测分数的总方差可分解为由潜变量解释的公共方差和未解释的误差方差。当指标线性加总时，真分数方差随载荷和的平方 $(\sum \lambda_i)^2$ 增长，而随机误差方差仅随误差方差之和 $\sum \theta_i$ 线性累加。CR 正是真分数方差占合成总方差的精准比率。
>
> > [!result-reading]- 结果怎么读
> > - **$\text{CR} \ge .80$** 表现卓越，指标合成具备极高的一致性与测量稳定性。
> > - **$.70 \le \text{CR} < .80$** 达到公认的优良水平，支持构念作为独立分析变量。
> > - **$\text{CR} < .60$** 表明指标间分歧过大，测量误差占据主导，需精简或剔除低负荷题项。

---

## 软件实现与代码规程

> [!software-impl] R 语言计算组合信度（CR）代码
> ```R
> library(lavaan)
> library(semTools)
> 
> # 1. 拟合 CFA 模型
> fit <- cfa(cfa_model, data = sample_data, estimator = "MLR")
> 
> # 2. 提取可靠性电池（包含 Alpha、CR/Omega、AVE）
> rel_res <- reliability(fit)
> 
> # 3. 查看组合信度 (semTools 中输出为 omega 或 omega.tot)
> cr_values <- rel_res["omega", ]
> print(round(cr_values, 3))
> ```

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 在《[[Research Literacy Scale for Teachers|教师研究素养量表]]》的 CFA 心理计量检验中，计算各分维度的组合信度分别为：研究意识（$\text{CR} = .83$）、研究态度（$\text{CR} = .75$）、研究技能（$\text{CR} = .87$）、研究使用（$\text{CR} = .90$），全部显著超过 $.70$ 门槛，证实了量表各维度卓越的内部一致性。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Scale Development]] | 宏观方法 | 组合信度是量表编制第三阶段替代传统 Alpha 的核心信度指标。 |
> | [[Confirmatory Factor Analysis]] | 前置方法 | 提供计算 CR 所需的因子载荷矩阵与残差方差。 |
> | [[Average Variance Extracted]] | 配套方法 | 与 CR 共同构成衡量潜变量效度与信度的一体化指标。 |
> | [[Internal Consistency]] | 理论概念 | CR 是现代内部一致性信度估计的理论金标准。 |
> | [[Research Literacy Scale for Teachers]] | 测量工具 | 运用 CR 确立四维度内部一致性的实证代表量表。 |
