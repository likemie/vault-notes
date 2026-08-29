---
title: McDonald's Omega
aliases:
  - 麦克唐纳系数
  - 麦克唐纳欧米伽系数
  - 麦克唐纳ω系数
  - 组合信度系数
  - McDonald omega
  - "McDonald's ω"
  - Omega reliability
summary: "现代心理测量学中基于因子分析模型评估潜变量内部一致性的首选信度指标，突破了克隆巴赫阿尔法要求因子载荷完全相等的严苛假设，可精准提供总信度与分层信度的无偏估计。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 15
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/psychometrics
  - measurement/reliability
  - scale-development/validation
related_concepts:
  - "[[Internal Consistency]]"
  - "[[Reliability]]"
  - "[[Variable]]"
  - "[[Likert Scale]]"
  - "[[Construct]]"
  - "[[Epistemology]]"
  - "[[Paradigm]]"
  - "[[Convergent and Discriminant Validity]]"
related_theories: []
related_methods:
  - "[[Confirmatory Factor Analysis]]"
  - "[[Exploratory Factor Analysis]]"
  - "[[Average Variance Extracted]]"
  - "[[Cronbach's Alpha]]"
  - "[[Composite Reliability]]"
related_instruments:
  - "[[Research Literacy Scale for Teachers]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
confidence: high
status: draft
created: 2026-08-29
updated: 2026-08-29
---

# McDonald's Omega

---

## 定义

> [!def] 方法定义
> **麦克唐纳 $\omega$ 系数（McDonald's Omega）** 是现代心理计量学与结构方程模型中基于同类测验模型（Congeneric Test Model）估计测量工具[[Internal Consistency|内部一致性]][[Reliability|信度]]的核心统计量。由 Roderick McDonald（1999）系统提出，它通过显式纳入每个题项在潜[[Variable|变量]]上的非等同**因子载荷（Factor Loadings）**与**测量残差方差（Error Variances）**，消除了经典 Cronbach's $\alpha$ 强求本质 $\tau$-等值（等载荷）所带来的系统性信度低估偏差。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 11)]]

> [!method-scope] 方法范围
> - **研究对象** 包含连续、有序分类（[[Likert Scale|李克特量表]]）或多分题项的单维量表、多维量表及双因子模型（Bifactor Models）。
> - **问题类型** 异质载荷条件下的精确信度估计、双因子模型中全局一般因子解释比例的提炼。
> - **分析单位** 测验题项与潜在[[Construct|构念]]因子。
> - **输出形式** 
>   - **总信度 $\omega_{\text{total}}$（或 $\omega_t$）** 所有公因子（含全局因子与特定因子）解释的总变异比例。
>   - **分层信度 $\omega_{\text{hierarchical}}$（或 $\omega_h$）** 控制特定分维度因子后，全局一般因子（General Factor）单独解释的方差比例。
>   - **子维度分层信度 $\omega_{\text{subscale}}$（或 $\omega_s$）** 各子维度在剔除全局因子干扰后的净信度。

> [!citation-card]- 关键定义
> 当因子载荷在各测验题项间存在差异时（即现实中普遍存在的同类测验模型），Cronbach's $\alpha$ 仅能提供真实信度的下界估计。McDonald's $\omega$ 基于完全估计的因子载荷矩阵与误差方差直接计算真分数方差与总方差的比值，因而是当代心理测量学报告复合测量工具信度的最优基准。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 11)]]
>
> *McDonald's omega coefficient is a model-based reliability estimate derived from the factor loadings and uniquenesses of a factor model. When the assumption of essential tau-equivalence is violated, omega provides a more accurate, unbiased estimate of internal consistency than alpha.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 属于现代潜[[Variable|变量]]测量[[Paradigm|范式]]，强调[[Reliability|信度]]不仅是被试作答的样本表面统计特征，更是特定因子模型（[[Confirmatory Factor Analysis|CFA]] / [[Exploratory Factor Analysis|EFA]]）与真实数据拟合度的结构化参数。
> - **研究者角色** 研究者必须在拟合优度良好的因子模型（CFA）前提下计算 $\omega$；如果底层因子模型错误，计算出的 $\omega$ 亦无实际意义。
> - **有效性标准** 决策阈值通常与 $\alpha$ 保持一致：$\omega \ge .70$ 达到基本可接受标准；$\omega \ge .80$ 良好；$\omega \ge .90$ 卓越。双因子模型中，若 $\omega_h \ge .80$，表明量表具备强烈的单维统整属性，允许直接计算总量表总分。
> - **不声称回答的问题** $\omega$ 本身度量信度（测量精确性），不能直接替代效度检验（如 [[Average Variance Extracted|AVE]] [[Convergent and Discriminant Validity|收敛效度]]与 Fornell-Larcker 区分效度）。

---

## 研究程序与数学原理

### 量化分析与公式推导

> [!formula-step] 公式步骤一　单维/同类因子模型下的 McDonald's $\omega$
> $$\omega = \frac{\left(\sum_{i=1}^{k} \lambda_i\right)^2}{\left(\sum_{i=1}^{k} \lambda_i\right)^2 + \sum_{i=1}^{k} \theta_i}$$
>
> **这个公式在做什么** 基于标准化单因子模型，将各题项因子载荷加总平方所得的**真分数变异**，除以**真分数变异与误差方差总和（即总方差）**。
>
> **符号说明**
> - $\lambda_i$：第 $i$ 个题项在目标潜[[Variable|变量]]上的标准化因子载荷（Standardized factor loading）。
> - $\theta_i$：第 $i$ 个题项的标准化测量残差方差（$\theta_i = 1 - \lambda_i^2$）。
> - $k$：题项总数。
>
> **数学直觉** 若所有 $\lambda_i$ 严格相等（$\lambda_i = \lambda$），则 $\omega$ 在代数上严格退化为标准化 Cronbach's $\alpha$；当 $\lambda_i$ 各不相同时，$\left(\sum \lambda_i\right)^2 \ge k \sum \lambda_i^2$，因而恒有 $\omega \ge \alpha$。这证明 $\alpha$ 是 $\omega$ 的下界。

> [!formula-step] 公式步骤二　双因子/多维模型下的分层[[Reliability|信度]] $\omega_h$
> $$\omega_h = \frac{\left(\sum_{i=1}^{k} \lambda_{g,i}\right)^2}{\text{Var}(X)}$$
>
> **这个公式在做什么** 计算全局一般因子 $g$ 对总分方差 $\text{Var}(X)$ 的净解释比例，用于判定多维量表是否具备计算单一总分的合法性。
>
> **符号说明**
> - $\lambda_{g,i}$：第 $i$ 个题项在全局一般因子 $g$ 上的载荷。
> - $\text{Var}(X)$：总分方差，$\text{Var}(X) = \left(\sum \lambda_{g,i}\right)^2 + \sum_{j=1}^m \left(\sum_{i \in S_j} \lambda_{s,i}\right)^2 + \sum_{i=1}^k \theta_i$。
>
> **结果怎么读** 若 $\omega_h > .80$，说明总分变异绝大部分源于全局特质，可将量表视为“基本单维”（Essential Unidimensionality）；若 $\omega_h < .50$，说明总分主要受异质子维度驱动，不应合成总分。

---

## 软件实现

> [!software-impl] 软件实现
> - **R 语言 (`lavaan` + `semTools` 或 `psych`)**
>   ```R
>   # 方法 1：基于 psych 包的双因子分析
>   library(psych)
>   omega_res <- psych::omega(mydata, nfactors = 4)
>   print(omega_res) # 输出 omega_h, omega_t, omega_lim
>   
>   # 方法 2：基于 CFA 结构方程模型
>   library(lavaan)
>   library(semTools)
>   cfa_model <- ' Factor1 =~ Q1 + Q2 + Q3 + Q4 '
>   fit <- cfa(cfa_model, data = mydata)
>   semTools::compRelSEM(fit, tau.eq = FALSE) # 输出 McDonald's omega
>   ```

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Cronbach's Alpha]] | 经典基准 | 当且仅当所有题项因子载荷完全相等时，$\alpha = \omega$；一般情况下 $\alpha \le \omega$。 |
> | [[Composite Reliability]] | 对偶指标 | 在单维模型中，结构方程模型的组合信度（CR）与 McDonald's $\omega$ 在数学上完全等价。 |
> | [[Confirmatory Factor Analysis]] | 估计引擎 | 为 $\omega$ 提供精准的标准化因子载荷 $\lambda$ 与残差方差 $\theta$ 估计值。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 在[[Research Literacy Scale for Teachers|教师研究素养量表]]（RLS）心理测量学检验中，同步报告了总量表 McDonald's $\omega = .95$（Cronbach's $\alpha = .94$），确立了优异的潜[[Variable|变量]]合成[[Reliability|信度]]。
