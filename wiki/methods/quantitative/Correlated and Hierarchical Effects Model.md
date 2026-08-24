---
title: Correlated and Hierarchical Effects Model
aliases:
  - 相关与层级效应模型
  - CHE
  - CHE model
  - Correlated and Hierarchical Effects
summary: "用于同时处理元分析中多重测量相关的效应量（相关效应）与嵌套于不同研究/元分析中的效应量（层级效应）的三水平统计工作模型"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 17
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/meta-analysis
  - method/che
  - statistics/multilevel-modeling
related_concepts:
  - "[[Effect Size]]"
  - "[[Heterogeneity]]"
  - "[[Sampling Error]]"
  - "[[Presence]]"
  - "[[Hypothesis]]"
  - "[[Creativity]]"
  - "[[Construct]]"
  - "[[Sample Size Determination]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Standard Error]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Accounts]]"
  - "[[Robust Variance Estimation]]"
  - "[[Random Sampling]]"
  - "[[Multilevel Egger's Test]]"
related_arguments:
  - "[[Argument_Runco_2026_CRJ]]"
confidence: high
status: draft
created: 2026-08-24
updated: 2026-08-24
---

# Correlated and Hierarchical Effects Model

---

## 定义

> [!def] 方法定义
> [[Correlated and Hierarchical Effects Model|相关与层级效应模型]]（Correlated and Hierarchical Effects Model, CHE 模型）是一种专门用于在[[Meta-analysis|元分析]]（Meta-Analysis）与[[Meta-meta-analysis|二阶元分析]]中同时处理**相关效应（Correlated Effects，同一项研究或同一被试报告的多个相关测量）**与**层级效应（Hierarchical Effects，[[Effect Size|效应量]]嵌套于不同原始研究或一阶元分析集群中）**的三水平统计工作模型（Working Model）（Pustejovsky & Tipton, 2022; [[Argument_Runco_2026_CRJ|Runco et al., 2026, p. 5]]）。CHE 通过构建块对角协方差工作矩阵并分解三层方差分量，为加权估计提供最优化统计效率。

> [!method-scope] 方法范围
> - **研究对象** 包含多重测量指标、多亚组比较、纵向追踪或跨元分析嵌套依赖的一阶与二阶元分析数据矩阵。
> - **问题类型** 同时存在元分析内效应量相关与元分析间效应[[Heterogeneity|异质性]]时的多水平方差分解与加权最小二乘拟合。
> - **分析单位** Level 1 [[Sampling Error|抽样误差]]、Level 2 研究内变异、Level 3 集群/元分析间真实效应变异。
> - **输出形式** 层级方差分量估计值（$\tau_3^2, \tau_2^2$）、异质性比率（$I_{(3)}^2, I_{(2)}^2$）及加权逆方差协方差工作矩阵 $\mathbf{V}$。

> [!citation-card]- 关键定义
> CHE 模型结合了相关效应与层级效应的优点，通过指定近似的相关结构构建工作协方差矩阵，使得效应量多水平加权更为精准。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 5)]]
>
> *We employed a correlated and hierarchical effects (CHE) working model to [[Accounts|account]] for the simultaneous [[Presence]] of correlated outcomes within studies and hierarchical nesting across meta-analyses...*

---

## 方法定位：解决的核心问题

> [!contrast-table] 传统模型 vs 独立多水平模型 vs CHE 工作模型
> | 维度 | 传统两水平[[Meta-analysis\|元分析]]模型 | 纯层级效应模型（Hierarchical） | 相关与层级效应工作模型（CHE） |
> |---|---|---|---|
> | **依赖性[[Hypothesis\|假设]]** | 假设所有[[Effect Size\|效应量]]完全独立 | 仅假设效应量嵌套于研究中，假设研究内无额外相关 | **同时建模研究内测量相关（$\rho$）与多层嵌套（$\tau_3^2, \tau_2^2$）** |
> | **协方差结构** | 对角矩阵（非对角线恒为 0） | 块对角矩阵（仅靠随机截距吸收） | **显示定义块对角已知抽样协方差矩阵 $\mathbf{V}$（包含 $\rho$ 结构）** |
> | **方差分解能力** | 单一残差方差 $\tau^2 + v_i$ | 两级[[Heterogeneity\|异质性]]方差（研究间 vs 抽样） | **三级方差分解（元分析间 $\tau_3^2$ + 元分析内 $\tau_2^2$ + 抽样 $V_{ij}$）** |
> | **与 [[Robust Variance Estimation\|RVE]] 的配合** | 加权效率低下 | 权重可能欠佳 | **提供最优 GLS 权重，极大提升 RVE 统计估计效率** |

> [!concept-lens] CHE 模型解决的核心痛点
> 1. **现实数据的双重依赖** 实证研究往往既包含“同一被试测了多种[[Creativity|创造力]]指标”（相关效应），又包含“多篇论文来自同一个实验室或同一个一阶元分析”（层级效应）。单纯使用层级模型会低估研究内相关，单纯使用相关模型则无法区分跨研究异质性。
> 2. **优化广义最小二乘（GLS）加权效率** 尽管稳健方差估计（RVE）能对错误的工作模型提供保护，但越接近真实依赖结构的工作模型，GLS 点估计的统计功效（Power）与估计精度越高。CHE 提供了最贴近真实数据生成过程的工作矩阵。

---

## 核心统计模型与数学公式

> [!formula-set] CHE 模型三水平方差分解与建模流程
> ```mermaid
> flowchart LR
>   A["步骤 1：提取一阶效应量<br/>(第 j 个元分析中的第 i 个效应量)"] --> B["步骤 2：设定三水平随机效应方程<br/>(分解集群间、集群内与抽样变异)"]
>   B --> C["步骤 3：构建抽样协方差矩阵<br/>(插补先验相关系数 ρ = 0.8)"]
>   C --> D["步骤 4：REML 限制极大似然估计<br/>(联合估计 τ₃² 与 τ₂²)"]
>   D --> E["步骤 5：输出最优加权权重矩阵<br/>(用于后续 GLS 逆方差拟合)"]
> ```

---

### 1. 三水平方差分解公式

> [!formula-step] 公式步骤　CHE 三水平数学模型
> $$z_{ij} = \beta_0 + \sum_{p=1}^P \beta_p X_{p,ij} + \zeta_{(3)j} + \zeta_{(2)ij} + \epsilon_{ij}$$
> $$\operatorname{Var}(\zeta_{(3)j}) = \tau_3^2, \quad \operatorname{Var}(\zeta_{(2)ij}) = \tau_2^2, \quad \operatorname{Var}(\epsilon_{ij}) = V_{ij}$$
>
> **这个公式在做什么** 将第 $j$ 个一阶[[Meta-analysis|元分析]]内第 $i$ 个[[Effect Size|效应量]] $z_{ij}$ 的总方差分解为三层变异：
> 1. **Level 3（集群/元分析间变异 $\tau_3^2$）** 反映不同一阶元分析之间真实总体效应的离散程度；
> 2. **Level 2（集群/元分析内变异 $\tau_2^2$）** 反映同一元分析内部不同效应量[[Construct|构念]]间的真实变异；
> 3. **Level 1（[[Sampling Error|抽样误差]]变异 $V_{ij}$）** 反映主要研究因有限[[Sample Size Determination|样本量]]带来的[[Random Sampling|随机抽样]]噪声（如 Fisher's $z$ 下 $V_{ij} = \frac{1}{n_{ij}-3}$）。
>
> **结果怎么读** 
> - 集群间[[Heterogeneity|异质性]]比例：$I_{(3)}^2 = \frac{\tau_3^2}{\tau_3^2 + \tau_2^2 + \bar{V}}$
> - 集群内异质性比例：$I_{(2)}^2 = \frac{\tau_2^2}{\tau_3^2 + \tau_2^2 + \bar{V}}$
> 两者之和即为全领域总真实异质性比例 $I_{\text{total}}^2$。

---

### 2. 抽样协方差矩阵的插补构造

> [!formula-step] 公式步骤　块对角协方差工作矩阵构建
> $$\mathbf{V}_j = \begin{pmatrix} 
> V_{1j} & \rho \sqrt{V_{1j} V_{2j}} & \cdots & \rho \sqrt{V_{1j} V_{k_j j}} \\
> \rho \sqrt{V_{2j} V_{1j}} & V_{2j} & \cdots & \rho \sqrt{V_{2j} V_{k_j j}} \\
> \vdots & \vdots & \ddots & \vdots \\
> \rho \sqrt{V_{k_j j} V_{1j}} & \rho \sqrt{V_{k_j j} V_{2j}} & \cdots & V_{k_j j}
> \end{pmatrix}$$
>
> **这个公式在做什么** 在[[Primary and Secondary Documents|原始文献]]未完整报告测量间相关系数时，设定合理的先验集群内相关常数 $\rho$（在敏感性分析中通常设定 $\rho = 0.8$，并检验 $\rho \in [0.0, 0.9]$ 范围内的稳定性），插补构造块对角抽样协方差矩阵。

---

## 软件实现与代码规程

> [!software-impl] R 语言环境（metafor）拟合 CHE 模型
> ```R
> library(metafor)
> 
> # 1. 计算效应量与已知抽样方差（Fisher's z）
> dat <- escalc(measure = "ZCOR", ri = r_obs, ni = n_sample, data = raw_data)
> 
> # 2. 构建 CHE 协方差工作矩阵（设定先验相关系数 rho = 0.8）
> V_mat <- impute_covariance_matrix(vi = dat$vi, cluster = dat$cluster_id, r = 0.8)
> 
> # 3. 拟合三水平 CHE 随机效应模型（REML 估计）
> fit_che <- rma.mv(yi, V_mat, random = ~ 1 | cluster_id / effect_id, 
>                   data = dat, sparse = TRUE)
> 
> # 4. 提取方差分量与计算异质性比率
> total_var <- fit_che$sigma2[1] + fit_che$sigma2[2] + mean(dat$vi)
> I2_level3 <- fit_che$sigma2[1] / total_var
> I2_level2 <- fit_che$sigma2[2] / total_var
> ```

---

## 适用场景与局限性

> [!method-fit] 适用判断
> - **强烈推荐** [[Meta-analysis|元分析]]中存在多重结果测量、亚组对比，或[[Meta-meta-analysis|二阶元分析]]中[[Effect Size|效应量]]嵌套于多个一阶元分析中。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 5)]]
> - **配合使用** 强烈建议将 CHE 模型作为加权工作模型，配合 [[Robust Variance Estimation|稳健方差估计]]（RVE） 进行[[Hypothesis|假设]]检验与[[Standard Error|标准误]]校正。

> [!method-limits] 方法局限
> - **工作模型假定依赖** 先验相关系数 $\rho$ 是人为指定的固定常数，必须进行敏感性检验（如在 0.0 到 0.9 间变动）以确认估计结论对 $\rho$ 的取值不敏感。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联方向 | 说明 |
> |:-----|:-----|:---------|:-----|
> | [[Meta-meta-analysis]] | 综合方法 | 核心技术 | 二阶[[Meta-analysis\|元分析]]运用 CHE 模型分解一阶元分析间与元分析内的双重方差。 |
> | [[Robust Variance Estimation]] | 推断方法 | 黄金搭档 | CHE 提供最优加权工作矩阵，RVE 基于该矩阵提供稳健[[Hypothesis\|假设]]检验与[[Standard Error\|标准误]]。 |
> | [[Multilevel Egger's Test]] | 偏倚方法 | 扩展应用 | 将 CHE 模型扩展用于控制聚类依赖下的小研究偏倚检验与截距校正。 |
> | [[Argument_Runco_2026_CRJ\|Runco et al. (2026)]] | 论证 | 典范应用 | 在 52 项[[Creativity\|创造力]]一阶元分析中运用 CHE 模型实现了高精度的[[Effect Size\|效应量]]建模。 |
