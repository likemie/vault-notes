---
title: KMO and Bartlett's Test of Sphericity
aliases:
  - 巴特利特球形度检验
  - 巴特利特球形检验
  - 抽样适宜性系数
  - Kaiser-Meyer-Olkin
  - "KMO and Bartlett's Test"
  - "Bartlett's Test of Sphericity"
summary: "探索性因子分析与主成分分析前置诊断观测变量相关矩阵是否适宜进行因子降维分解的标准检验体系，KMO通过简单相关与偏相关比率度量样本充分度，Bartlett检验则基于似然比判定相关矩阵是否显著偏离独立单位矩阵。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 12
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/psychometrics
  - statistics/multivariate
  - scale-development/validation
related_concepts:
  - "[[Variable]]"
  - "[[Sample Size Determination]]"
  - "[[Null Hypothesis]]"
  - "[[Epistemological Beliefs]]"
  - "[[Questionnaire]]"
  - "[[Epistemology]]"
related_theories: []
related_methods:
  - "[[Exploratory Factor Analysis]]"
  - "[[Pearson Product-Moment Correlation]]"
  - "[[Scale Development]]"
related_instruments:
  - "[[Schommer's Modified Epistemological Questionnaire]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
  - "[[Argument_Lodewyk_2007_EP]]"
confidence: high
status: draft
created: 2026-08-29
updated: 2026-08-29
---

# KMO and Bartlett's Test of Sphericity

---

## 定义

> [!def] 方法定义
> **KMO 抽样适宜性度量与巴特利特球形度检验（KMO and Bartlett's Test of Sphericity）** 是在执行[[Exploratory Factor Analysis|探索性因子分析]]（EFA）或主成分分析（PCA）之前，用于检验多[[Variable|变量]]相关矩阵是否具备可因子化性（Factorability）的标准前置诊断规程。KMO 度量观测变量之间的偏相关程度是否足够低，以确保存在紧密的公共因子结构；Bartlett 球形度检验则从全局推断样本相关矩阵是否显著异于变量互不相关的单位矩阵（Identity Matrix）。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 5)]]

> [!method-scope] 方法范围
> - **研究对象** 包含 3 个及以上连续或有序分类题项的相关矩阵（Correlation Matrix $\mathbf{R}$）。
> - **问题类型** 数据降维前置合法性检验、公因子提取前提诊断。
> - **分析单位** 测验题项系统与变量相关矩阵。
> - **输出形式** KMO 全局系数与单题 MSA 系数（Measure of Sampling Adequacy，取值 0 到 1）、Bartlett 检验近似卡方值 $\chi^2$、自由度 $df$ 与 $p$ 显著性水平。

---

## 核心指标与数学原理

### 量化分析与公式推导

> [!formula-step] 公式步骤一　KMO 抽样适宜性系数（Kaiser-Meyer-Olkin Measure）
> $$\text{KMO} = \frac{\sum_{i \ne j} r_{ij}^2}{\sum_{i \ne j} r_{ij}^2 + \sum_{i \ne j} a_{ij}^2}$$
>
> **这个公式在做什么** 对比所有[[Variable|变量]]对之间的**简单相关系数平方和（$\sum r_{ij}^2$）**与**简单相关平方和加上偏相关系数平方和（$\sum a_{ij}^2$）**的比值。
>
> **符号说明**
> - $r_{ij}$：变量 $i$ 与变量 $j$ 之间的零阶皮尔逊[[Pearson Product-Moment Correlation|积差相关]]系数。
> - $a_{ij}$：在控制了数据集中所有其余所有变量后，变量 $i$ 与变量 $j$ 之间的偏相关系数（Partial Correlation / Anti-image Correlation）。
>
> **数学直觉** 如果变量之间由少数强有力的公共因子驱动，则在剔除公因子影响后，变量间的偏相关 $a_{ij}$ 应当接近 0，此时分母接近分子，$\text{KMO} \to 1.0$；反之，若变量间充斥着独特的非共享变异，偏相关很大，$\text{KMO} \to 0$。
>
> **判定准则（Kaiser 1974 标准）**
> - $\text{KMO} \ge .90$：极佳（Marvelous）；
> - $.80 \le \text{KMO} < .90$：良好（Meritorious）；[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 5)]]
> - $.70 \le \text{KMO} < .80$：中等（Middling）；
> - $.60 \le \text{KMO} < .70$：勉强可接受（Mediocre）；
> - $\text{KMO} < .50$：不可接受（Unacceptable，禁止开展因子分析）。

> [!formula-step] 公式步骤二　巴特利特球形度检验（Bartlett's Test of Sphericity）
> $$\chi^2 = -\left(N - 1 - \frac{2p + 5}{6}\right) \ln |\mathbf{R}|, \quad df = \frac{p(p-1)}{2}$$
>
> **这个公式在做什么** 检验总体相关矩阵 $\mathbf{R}$ 是否为一个对角线全为 1、非对角线全为 0 的单位阵（$\mathbf{I}$），即检验各变量在总体中是否完全独立无关。
>
> **符号说明**
> - $N$：[[Sample Size Determination|样本量]]。
> - $p$：分析的变量/题项总数。
> - $|\mathbf{R}|$：相关矩阵的行列式（Determinant）。
>
> **结果怎么读** 若 $p < .001$，拒绝[[Null Hypothesis|虚无假设]]（$H_0: \mathbf{R} = \mathbf{I}$），证实变量间存在显著相关性，允许提取公因子。

---

## 软件实现

> [!software-impl] 软件实现
> - **R 语言 (`psych`)**
>   ```R
>   library(psych)
>   # KMO 检验（包含全局与单题 MSA）
>   kmo_res <- KMO(mydata)
>   print(kmo_res)
>   # Bartlett 球形检验
>   bartlett_res <- cortest.bartlett(cor(mydata), n = nrow(mydata))
>   print(bartlett_res)
>   ```
> - **SPSS**
>   在 `Analyze -> Dimension Reduction -> Factor` 中，点击 `Descriptives`，勾选 `KMO and Bartlett's test of sphericity` 与 `Anti-image`。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Exploratory Factor Analysis]] | 后续核心方法 | KMO 与 Bartlett 检验达标后所执行的潜在维度提取与旋转分析。 |
> | [[Scale Development]] | 宏观流程 | 在量表编制阶段二（结构探索）中作为首道准入检验门槛。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 在样本 1（$N=310$）执行 [[Exploratory Factor Analysis|EFA]] 前，检验并报告 KMO $= .92$ 且 Bartlett 球形检验达到极显著水平（$\chi^2 = 3450.21, p < .001$），确立因子分析的充分合法性。
> - [[Argument_Lodewyk_2007_EP|Lodewyk (2007)]] — 在中学生科学[[Epistemological Beliefs|认识论信念]][[Questionnaire|问卷]]（[[Schommer's Modified Epistemological Questionnaire|SMEQ]]）因子分析前，通过 KMO 与 Bartlett 检验确立[[Epistemology|认识论]] 3 维度的提取前提。
