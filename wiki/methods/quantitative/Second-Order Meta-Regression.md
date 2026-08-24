---
title: Second-Order Meta-Regression
aliases:
  - 二阶元回归
  - 二级元回归
  - 二阶调节分析
  - Second-Order Meta-Regression Analysis
  - SOMA Meta-Regression
  - 二阶元分析元回归
summary: "在二阶元分析框架下，通过三水平CHE工作模型与RVE三明治估计量，检验宏观理论构念、研究特征与方法学质量对二阶效应量异质性的解释力的统计回归方法"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 24
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/meta-analysis
  - method/meta-regression
  - statistics/multilevel-modeling
related_concepts:
  - "[[Construct]]"
  - "[[Variable]]"
  - "[[Effect Size]]"
  - "[[Document]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Sampling Error]]"
  - "[[Standard Error]]"
  - "[[Confidence Interval]]"
  - "[[Interaction Effect]]"
  - "[[Heterogeneity]]"
  - "[[Hypothesis]]"
  - "[[Ecological Fallacy]]"
  - "[[Creativity]]"
related_methods:
  - "[[Meta-regression]]"
  - "[[Meta-meta-analysis]]"
  - "[[Meta-analysis]]"
  - "[[Correlated and Hierarchical Effects Model]]"
  - "[[Robust Variance Estimation]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Random Sampling]]"
  - "[[Multilevel Egger's Test]]"
related_instruments:
  - "[[AMSTAR]]"
related_arguments:
  - "[[Argument_Runco_2026_CRJ]]"
confidence: high
status: draft
created: 2026-08-24
updated: 2026-08-24
---

# Second-Order Meta-Regression

---

## 定义

> [!def] 方法定义
> [[Second-Order Meta-Regression|二阶元回归]]（Second-Order [[Meta-regression]]，亦称二阶调节分析或 [[Meta-meta-analysis|SOMA]] Meta-Regression）是在[[Meta-meta-analysis|二阶元分析]]（Second-Order [[Meta-analysis]]）框架下，通过将宏观理论[[Construct|构念]]属性、研究设计类型、方法学质量及抽样精度等特征作为调节[[Variable|变量]]（Moderators），系统检验其对跨元分析汇总[[Effect Size|效应量]]变异解释力的多水平统计建模方法（Schmidt & Oh, 2013; [[Argument_Runco_2026_CRJ|Runco et al., 2026, pp. 5–6]]）。与一阶[[Meta-regression|元回归]]不同，二阶元回归必须在[[Correlated and Hierarchical Effects Model|相关与层级效应模型]]（CHE）与[[Robust Variance Estimation|稳健方差估计]]（RVE）三明治估计量之上运行，以克服跨元分析[[Document|文献]]重叠与多层集群依赖导致的自由度虚假膨胀与假阳性偏差。

> [!method-scope] 方法范围
> - **研究对象** 嵌套于多个一阶元分析集群中的效应量矩阵及其关联的宏观[[Coding in Qualitative Research|编码]]协变量。
> - **问题类型** 检验理论构念差异（如变量角色：[[Independent Variable|自变量]] vs [[Dependent Variable|结果变量]]）、研究设计特征（横断面 vs 纵向 vs 实验）、方法学质量等级（[[AMSTAR]] 高 vs 低）及小研究效应。
> - **分析单位** Level 1 [[Sampling Error|抽样误差]]、Level 2 一阶元分析内效应量构念、Level 3 一阶元分析集群。
> - **输出形式** 经 RVE 稳健调整后的回归系数点估计 $\hat{\beta}_p$、稳健[[Standard Error|标准误]]、95% [[Confidence Interval|置信区间]]及基于 Hotelling $T^2$ 近似的宏观[[Interaction Effect|调节效应]] Wald $F$ 检验统计量与 $p$ 值。

> [!citation-card]- 关键定义
> 二阶元回归通过在多水平 CHE 与 RVE 框架下纳入多重调节变量，系统分解了全领域效应量的[[Heterogeneity|异质性]]来源，评估了构念类型、变量角色与研究设计对效应强度的调节作用。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 5–7)]]
>
> *Second-order meta-regressions were conducted using correlated and hierarchical effects models combined with robust variance estimation to examine the moderating roles of theoretical constructs, study design, and methodological quality...*

---

## 数学原理：一阶元回归 vs 二阶元回归

> [!concept-lens] 底层数学同构：广义加权最小二乘法（GLS）
> 一阶[[Meta-regression|元回归]]与二阶元回归在底层参数点估计上具有完全相同的数学形式，均属于广义加权最小二乘线性模型：
> $$\hat{\boldsymbol{\beta}} = \left( \mathbf{X}^T \mathbf{W} \mathbf{X} \right)^{-1} \mathbf{X}^T \mathbf{W} \mathbf{y}$$
> 两者的共同目标都是通过特征设计矩阵 $\mathbf{X}$ 解释[[Effect Size|效应量]]向量 $\mathbf{y}$ 的离散变异，并通过逆方差权重矩阵 $\mathbf{W}$ 赋予高精度观测点更大的统计权重。

> [!contrast-table] 一阶元回归与二阶元回归的数学原理深度对比
> | 比较维度 | 经典一阶元回归（[[Meta-regression]]） | 现代二阶元回归（[[Second-Order Meta-Regression]]） |
> |:---|:---|:---|
> | **观测单元 $\mathbf{y}$** | 原始实证研究的独立效应量 $y_i$<br>（Primary Study Effect Size） | 嵌套于第 $j$ 个元分析集群中的一阶汇总效应量 $z_{ij}$<br>（Cluster-Nested Effect Size） |
> | **误差方程与方差分解** | 两水平方差分解<br>$$y_i = \mathbf{x}_i \boldsymbol{\beta} + u_i + \epsilon_i$$<br>$\operatorname{Var}(u_i) = \tau^2$（研究间真实异质性）<br>$\operatorname{Var}(\epsilon_i) = v_i$（抽样方差） | 三水平方差分解与协方差插补（[[Correlated and Hierarchical Effects Model\|CHE 模型]]）<br>$$z_{ij} = \mathbf{x}_{ij} \boldsymbol{\beta} + \zeta_{(3)j} + \zeta_{(2)ij} + \epsilon_{ij}$$<br>$\operatorname{Var}(\zeta_{(3)j}) = \tau_3^2$（Level 3 集群间变异）<br>$\operatorname{Var}(\zeta_{(2)ij}) = \tau_2^2$（Level 2 集群内变异）<br>$\operatorname{Cov}(\epsilon_{aj}, \epsilon_{bj}) = \rho \sqrt{V_{aj} V_{bj}}$（集群内测量相关） |
> | **加权矩阵 $\mathbf{W}$ 结构** | 对角矩阵（Diagonal Matrix）<br>$$\mathbf{W} = \operatorname{diag}\left( \frac{1}{\tau^2 + v_1}, \dots, \frac{1}{\tau^2 + v_k} \right)$$<br>假定所有纳入研究完全独立，非对角协方差恒为 0 | 块对角矩阵（Block-Diagonal Matrix）<br>$$\mathbf{W}_j = \left( \tau_3^2 \mathbf{I} + \tau_2^2 \mathbf{J} + \mathbf{V}_j \right)^{-1}$$<br>显式包含由先验相关系数（$\rho = 0.8$）构建的群内已知抽样协方差矩阵 $\mathbf{V}_j$ |
> | **[[Standard Error\|标准误]]与协方差估计** | 基于模型假定的理论方差<br>$$\operatorname{Var}(\hat{\boldsymbol{\beta}}) = \left( \mathbf{X}^T \mathbf{W} \mathbf{X} \right)^{-1}$$<br>严格依赖模型设定正确且研究间无数据重叠 | 非参数经验三明治估计量（[[Robust Variance Estimation\|RVE]]）<br>$$\mathbf{V}_{\text{RVE}} = (\mathbf{X}^T \mathbf{W} \mathbf{X})^{-1} \left[ \sum_{j=1}^J \mathbf{X}_j^T \mathbf{W}_j \mathbf{e}_j \mathbf{e}_j^T \mathbf{W}_j \mathbf{X}_j \right] (\mathbf{X}^T \mathbf{W} \mathbf{X})^{-1}$$<br>利用经验残差外积自动吸收未知的跨综述文献重叠 |
> | **小样本调节[[Hypothesis\|假设]]检验** | Knapp-Hartung 调整 $t$ 检验或标准 Wald $\chi^2$ 检验<br>（自由度直接基于研究总数 $k - p - 1$） | CR2 杠杆调整残差与 Hotelling $T^2$ 调整 $F$ 检验<br>$$\tilde{\mathbf{e}}_j = (\mathbf{I} - \mathbf{H}_j)^{-1/2} \mathbf{e}_j$$<br>基于 Satterthwaite 近似估计有效集群自由度 $\nu$ |

> [!warning] 一阶元回归处理二阶数据时的“数学失效”机理
> 若直接将一阶元回归套用于[[Meta-meta-analysis|二阶元分析]]数据，会触发两大致命的数学偏差：
> 1. **独立性假设被[[Document|文献]]重叠撕裂** 真实协方差包含跨[[Meta-analysis|元分析]]重复引用引起的正协方差 $\sigma_{jk} > 0$。一阶理论方差 $(\mathbf{X}^T \mathbf{W} \mathbf{X})^{-1}$ 强行忽略正协方差交叉项，相当于把重复样本误当成全新的独立证据，导致计算出的标准误被人为大幅压缩，造成严重的假阳性偏差（把随机噪声误判为显著[[Interaction Effect|调节效应]]）；
> 2. **多层变异维度的混淆** 一阶模型单一的 $\tau^2$ 无法解耦宏观元分析间[[Heterogeneity|异质性]]（$\tau_3^2$）与微观[[Construct|构念]]间异质性（$\tau_2^2$），导致调节[[Variable|变量]]的解释力归因不清。

---

## 核心统计模型与数学公式

> [!formula-set] 二阶[[Meta-regression|元回归]]统计建模与[[Hypothesis|假设]]检验流程
> ```mermaid
> flowchart LR
>   A["输入效应量 z_ij 与调节变量矩阵 X_ij<br/>(第 j 个元分析中的第 i 个效应量)"] --> B["构建三水平元回归模型<br/>z_ij = β_0 + ∑ β_p X_p,ij + ζ_(3)j + ζ_(2)ij + ε_ij"]
>   B --> C["基于 CHE 工作矩阵进行 GLS 拟合<br/>β̂ = (X'WX)⁻¹ X'Wy"]
>   C --> D["计算 RVE 三明治协方差矩阵 V_RVE<br/>应用 CR2 小样本杠杆校正"]
>   D --> E["多参数联合 Wald F 检验<br/>基于 Hotelling T² 近似输出稳健 p 值"]
>   E --> F["计算二阶伪判定系数 R²<br/>评估宏观调节变量对全领域异质性的解释率"]
> ```

---

### 1. 三水平二阶元回归方程

> [!formula-step] 公式步骤　三水平二阶元回归数学模型
> $$z_{ij} = \beta_0 + \sum_{p=1}^P \beta_p X_{p,ij} + \zeta_{(3)j} + \zeta_{(2)ij} + \epsilon_{ij}$$
> $$\zeta_{(3)j} \sim \mathcal{N}(0, \tau_3^2), \quad \zeta_{(2)ij} \sim \mathcal{N}(0, \tau_2^2), \quad \epsilon_{ij} \sim \mathcal{N}(0, V_{ij})$$
>
> **这个公式在做什么** 在三水平方差分解框架下，将第 $j$ 个一阶[[Meta-analysis|元分析]]中第 $i$ 个[[Effect Size|效应量]] $z_{ij}$ 对一组宏观特征调节[[Variable|变量]] $X_{1,ij}, \dots, X_{P,ij}$ 进行多水平加权回归分析。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 5–6)]]
>
> **符号说明**
> - $z_{ij}$：经过 Fisher's $z$ 变换的正态化一阶效应量；
> - $\beta_0$：回归截距项（所有调节变量取基准值时的总体基准效应量）；
> - $\beta_p$：第 $p$ 个调节变量的二阶元回归斜率系数；
> - $X_{p,ij}$：第 $j$ 个元分析内第 $i$ 个效应量的第 $p$ 个[[Coding in Qualitative Research|编码]]特征（如[[Construct|构念]]分类哑变量、研究设计类型、质量达标指标）；
> - $\zeta_{(3)j}$：一阶元分析集群间随机截距残差（Level 3）；
> - $\zeta_{(2)ij}$：元分析集群内部效应量构念间随机截距残差（Level 2）；
> - $\epsilon_{ij}$：已知的主要研究[[Random Sampling|随机抽样]]误差（Level 1）。

---

### 2. 稳健方差估计与参数检验

> [!formula-step] 公式步骤　GLS 估计与 [[Robust Variance Estimation|RVE]] 协方差矩阵
> $$\hat{\boldsymbol{\beta}} = \left( \mathbf{X}^T \mathbf{W} \mathbf{X} \right)^{-1} \mathbf{X}^T \mathbf{W} \mathbf{y}$$
> $$\mathbf{V}_{\text{RVE}} = \left( \mathbf{X}^T \mathbf{W} \mathbf{X} \right)^{-1} \left( \sum_{j=1}^J \mathbf{X}_j^T \mathbf{W}_j \mathbf{e}_j \mathbf{e}_j^T \mathbf{W}_j \mathbf{X}_j \right) \left( \mathbf{X}^T \mathbf{W} \mathbf{X} \right)^{-1}$$
>
> **数学原理与推导**
> 1. **GLS 点估计** 权重矩阵 $\mathbf{W}$ 为根据 [[Correlated and Hierarchical Effects Model|CHE]] 模型分解方差（$\tau_3^2, \tau_2^2$）与设定的先验相关常数（$\rho = 0.8$）构建的块对角矩阵；
> 2. **三明治协方差校正** 通过集群经验残差外积 $\sum \mathbf{X}_j^T \mathbf{W}_j \mathbf{e}_j \mathbf{e}_j^T \mathbf{W}_j \mathbf{X}_j$，RVE 自动修正了一阶元分析间因[[Document|文献]]重叠或工作模型设定误差带来的方差畸变，确保回归系数 $\hat{\beta}_p$ 的[[Standard Error|标准误]]渐近无偏。

---

### 3. 多参数调节效应联合检验（Wald $F$ 检验）

> [!formula-step] 公式步骤　Hotelling $T^2$ 调整的多参数 Wald 检验
> $$H_0: \mathbf{L} \boldsymbol{\beta} = \mathbf{0} \quad \text{vs} \quad H_1: \mathbf{L} \boldsymbol{\beta} \neq \mathbf{0}$$
> $$T^2 = \left( \mathbf{L} \hat{\boldsymbol{\beta}} \right)^T \left( \mathbf{L} \mathbf{V}_{\text{RVE}} \mathbf{L}^T \right)^{-1} \left( \mathbf{L} \hat{\boldsymbol{\beta}} \right)$$
> $$F = \frac{\nu - q + 1}{\nu q} T^2 \sim F(q, \nu - q + 1)$$
>
> **数学原理与读法**
> - $\mathbf{L}$：用于检验多分类调节变量（如 4 种研究设计或 6 类干预模式）各水平间是否存在显著整体差异的假设约束矩阵（秩为 $q$）；
> - $\nu$：基于 Satterthwaite 近似估计的有效小样本自由度；
> - 若检验统计量 $F$ 显著（$p < 0.05$），表明该宏观调节维度对效应量强度存在显著的系统性调制效应（例如 Runco et al., 2026 检验变量角色差异：$F(1, 10.9) = 15.7, p = .002$）。

---

## 软件实现与代码规程

> [!software-impl] R 语言环境（metafor 与 clubSandwich）实现二阶[[Meta-regression|元回归]]
> ```R
> library(metafor)
> library(clubSandwich)
> 
> # 1. 效应量转换与抽样方差计算
> dat <- escalc(measure = "ZCOR", ri = r_val, ni = n_sample, data = raw_data)
> 
> # 2. 构建 CHE 协方差工作矩阵
> V_mat <- impute_covariance_matrix(vi = dat$vi, cluster = dat$meta_id, r = 0.8)
> 
> # 3. 拟合多变量二阶元回归模型
> # 纳入调节变量：变量角色(predictor_role)、研究设计(study_design)、质量达标(amstar_high)
> model_meta_reg <- rma.mv(yi ~ predictor_role + study_design + amstar_high, 
>                          V_mat, random = ~ 1 | meta_id / effect_id, 
>                          data = dat, sparse = TRUE)
> 
> # 4. 应用 RVE 进行单个回归系数稳健检验（CR2 小样本调整）
> coef_results <- coef_test(model_meta_reg, vcov = "CR2", cluster = dat$meta_id)
> print(coef_results)
> 
> # 5. 针对多分类调节变量进行整体 Wald F 检验
> wald_design <- Wald_test(model_meta_reg, constraints = constrain_predictors(model_meta_reg, 
>                                                                            pattern = "study_design"), 
>                          vcov = "CR2", cluster = dat$meta_id)
> print(wald_design)
> ```

---

## 适用场景与局限性

> [!method-fit] 适用判断
> - **强烈推荐** [[Meta-meta-analysis|二阶元分析]]项目中存在显著[[Heterogeneity|异质性]]（$I^2 > 50\%$），需要系统比较不同[[Construct|构念]]流派、研究设计或方法学质量的[[Interaction Effect|调节效应]]时；
> - **偏倚控制** 强烈建议将抽样[[Standard Error|标准误]] $\text{SE}$ 作为协[[Variable|变量]]纳入模型，以实现控制小研究偏倚下的条件[[Effect Size|效应量]]估计。

> [!method-limits] 方法局限
> - **[[Ecological Fallacy|生态谬误]]风险（Ecological Fallacy）** 二阶[[Meta-regression|元回归]]分析的是一阶[[Meta-analysis|元分析]]水平的汇总特征，不能直接推断微观个体层面的心理或教学因果机制；
> - **多重共线性与自由度受限** 当纳入的一阶元分析数量有限（$<30$）且调节变量较多时，有效自由度较低可能削弱统计检验功效。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联方向 | 说明 |
> |:-----|:-----|:---------|:-----|
> | [[Meta-meta-analysis]] | 综合方法 | 核心模块 | 二阶[[Meta-regression\|元回归]]是现代二阶[[Meta-analysis\|元分析]]用于解释全领域[[Heterogeneity\|异质性]]来源的标准分析工具。 |
> | [[Correlated and Hierarchical Effects Model]] | 基础模型 | 建模底层 | 二阶元回归基于 CHE 三水平随机效应方程与协方差工作矩阵构建。 |
> | [[Robust Variance Estimation]] | 推断方法 | 统计引擎 | RVE 三明治估计量为二阶元回归各系数及 Wald 检验提供稳健[[Standard Error\|标准误]]。 |
> | [[Multilevel Egger's Test]] | 偏倚方法 | 特殊形式 | 多水平艾格检验本质上是以抽样标准误为唯一调节[[Variable\|变量]]的单变量二阶元回归。 |
> | [[Meta-regression]] | 基础方法 | 概念源流 | 经典一阶元回归在多水平二阶元分析领域的理论与技术延伸。 |
> | [[Argument_Runco_2026_CRJ\|Runco et al. (2026)]] | 论证 | 典范应用 | 运用二阶元回归系统检验了[[Independent Variable\|自变量]]角色、横断面设计与干预模式对[[Creativity\|创造力]]效应的调节机制。 |
