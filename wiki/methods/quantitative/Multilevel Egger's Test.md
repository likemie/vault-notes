---
title: Multilevel Egger's Test
aliases:
  - 多水平艾格检验
  - 多水平艾格回归
  - Multilevel Egger's Regression
  - 多水平发表偏倚检验
  - Multilevel Egger test
summary: "在多水平与聚类依赖元分析数据中检验小研究效应与发表偏倚，并通过回归截距估计剔除样本量偏倚后的真实效应量的统计检验方法"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 19
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/meta-analysis
  - method/publication-bias
  - statistics/multilevel-modeling
related_concepts:
  - "[[Small Study Effects]]"
  - "[[Publication Bias]]"
  - "[[Standard Error]]"
  - "[[Variable]]"
  - "[[Effect Size]]"
  - "[[Confidence Interval]]"
  - "[[Hypothesis]]"
  - "[[Research Contribution]]"
  - "[[Sample Size Determination]]"
  - "[[Sampling Error]]"
  - "[[Heterogeneity]]"
related_methods:
  - "[[Meta-meta-analysis]]"
  - "[[Meta-analysis]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Trim and Fill Method]]"
  - "[[Robust Variance Estimation]]"
  - "[[Meta-regression]]"
  - "[[Correlated and Hierarchical Effects Model]]"
related_arguments:
  - "[[Argument_Runco_2026_CRJ]]"
confidence: high
status: draft
created: 2026-08-24
updated: 2026-08-24
---

# Multilevel Egger's Test

---

## 定义

> [!def] 方法定义
> [[Multilevel Egger's Test|多水平艾格检验]]（Multilevel Egger's Test，亦称多水平艾格回归 Multilevel Egger's Regression）是一种在包含聚类依赖、多重结果测量或多层嵌套结构（如[[Meta-meta-analysis|二阶元分析]]）的[[Meta-analysis|元分析]]中检验**[[Small Study Effects|小研究效应]]（Small-Study Effects）**与[[Publication Bias|发表偏倚]]（Publication Bias）的定量诊断与校正方法（Rodgers & Pustejovsky, 2021; [[Argument_Runco_2026_CRJ|Runco et al., 2026, p. 6]]）。该方法将抽样[[Standard Error|标准误]]作为调节[[Variable|变量]]纳入三水平[[Fixed-Effect and Random-Effects Models|随机效应模型]]，通过斜率检验偏倚是否存在，并利用回归截距估计理论无限大样本下的无偏[[Effect Size|效应量]]。

> [!method-scope] 方法范围
> - **研究对象** 存在多重效应量嵌套依赖的一阶元分析或二阶元分析证据库。
> - **问题类型** 检验效应量大小是否与抽样精度系统性相关（发表偏倚诊断），并校正小样本膨胀效应。
> - **分析单位** 包含抽样标准误 $\text{SE}_{ij}$ 与效应量 $z_{ij}$ 的多水平观测矩阵。
> - **输出形式** 偏倚斜率检验统计量（$\beta_{\text{SE}}$ 与 $p$ 值）、偏倚校正后的二阶效应量点估计（$\beta_0$ / 转换后的 $r$ 或 $g$）及其 95% [[Confidence Interval|置信区间]]。

> [!citation-card]- 关键定义
> 多水平艾格回归模型通过在层级随机效应结构中将效应量对标准误进行回归，能够在控制聚类依赖的同时准确检验发表偏倚并给出校正后的效应量估计。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 6)]]
>
> *We evaluated potential publication bias using a multilevel extension of Egger's regression test... The intercept provides an estimate of the overall effect size adjusted for small-study effects.*

---

## 方法定位：解决的核心问题

> [!contrast-table] 传统单水平 Egger 检验 vs 漏斗图[[Trim and Fill Method|剪补法]] vs 多水平 Egger 检验
> | 比较维度 | 传统 Egger 检验（1997） | 漏斗图剪补法（Trim and Fill） | 多水平 Egger 检验（Rodgers & Pustejovsky, 2021） |
> |---|---|---|---|
> | **独立性[[Hypothesis\|假设]]** | 假定每项[[Research Contribution\|研究贡献]]单一独立[[Effect Size\|效应量]] | 假定漏斗图基于独立样本 | **允许效应量嵌套于研究/[[Meta-analysis\|元分析]]中（聚类依赖）** |
> | **依赖数据下的表现** | [[Standard Error\|标准误]]严重低估，假阳性率急剧上升（把聚类相关误判为偏倚） | 插补伪造研究，在多水平数据下失效 | **结合 CHE/[[Robust Variance Estimation\|RVE]] 正确控制多层误差结构** |
> | **核心产出** | 仅给出偏倚显著性检验 $p$ 值 | 填补虚拟研究后的粗糙估计 | **同时输出偏倚显著性 $p$ 值与偏倚校正后的无偏截距 $\beta_0$** |

> [!concept-lens] 多水平 Egger 检验解决的核心痛点
> 1. **破解依赖数据下的假阳性偏倚警报** 传统 Egger 回归忽略了同一研究或一阶元分析内部的效应量相关性，会将“同一高质量综述内部效应量的集中性”错误诊断为“严重的[[Publication Bias|发表偏倚]]”。多水平模型通过 Level 2 和 Level 3 随机效应吸收了这些集群内变异。
> 2. **实现“偏倚诊断”与“无偏效应量校正”的一体化** 经典方法通常只能做偏倚检验或粗糙剪补；多水平 Egger 回归通过数学截距项 $\beta_0$（当抽样标准误 $\text{SE} \to 0$ 时的理论效应量），直接给出了剔除小样本膨胀效应后的“纯净效应量基准”。

---

## 核心统计模型与数学公式

> [!formula-set] 多水平艾格检验与截距校正流程
> ```mermaid
> flowchart LR
>   A["步骤 1：输入效应量与标准误<br/>(作为唯一连续调节变量)"] --> B["步骤 2：拟合三水平艾格元回归<br/>(分解集群间与集群内变异)"]
>   B --> C["步骤 3：检验斜率显著性<br/>(诊断是否存在小研究发表偏倚)"]
>   C --> D["步骤 4：提取模型截距项<br/>(获取极限样本下的无偏效应量)"]
>   D --> E["步骤 5：RVE 稳健方差校正<br/>(应用 CR2 调整输出置信区间)"]
>   E --> F["步骤 6：逆双曲正切反变换<br/>(输出校正后皮尔逊 r 基准值)"]
> ```

---

### 1. 多水平艾格回归模型公式

> [!formula-step] 公式步骤　多水平艾格回归方程
> $$z_{ij} = \beta_0 + \beta_{\text{SE}} \sqrt{V_{ij}} + \zeta_{(3)j} + \zeta_{(2)ij} + \epsilon_{ij}$$
>
> **这个公式在做什么** 在三水平方差分解架构下，将[[Effect Size|效应量]] $z_{ij}$ 对已知抽样[[Standard Error|标准误]] $\text{SE}_{ij} = \sqrt{V_{ij}}$ 进行多水平[[Meta-regression|元回归]]分析。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 6)]]
>
> **符号说明**
> - $z_{ij}$：第 $j$ 个[[Meta-analysis|元分析]]集群中第 $i$ 个效应量（Fisher's $z$ 转换值）；
> - $\sqrt{V_{ij}}$：该效应量的抽样标准误（$\text{SE}_{ij} = \frac{1}{\sqrt{n_{ij}-3}}$）；
> - $\beta_{\text{SE}}$：[[Small Study Effects|小研究效应]]斜率系数；
> - $\beta_0$：回归截距项（当[[Sample Size Determination|样本量]]趋于无穷大、$\text{SE} \to 0$ 时的理论效应量）；
> - $\zeta_{(3)j} \sim \mathcal{N}(0, \tau_3^2)$：元分析间随机效应（Level 3）；
> - $\zeta_{(2)ij} \sim \mathcal{N}(0, \tau_2^2)$：元分析内效应量间随机效应（Level 2）；
> - $\epsilon_{ij} \sim \mathcal{N}(0, V_{ij})$：已知[[Sampling Error|抽样误差]]（Level 1）。

---

### 2. 假设检验与偏倚校正判定

> [!formula-step] 公式步骤　偏倚判定与截距还原
> $$\text{偏倚检验：} H_0: \beta_{\text{SE}} = 0 \quad \text{vs} \quad H_1: \beta_{\text{SE}} \neq 0$$
> $$\text{校正后效应量：} r_{\text{adjusted}} = \tanh(\hat{\beta}_0) = \frac{\exp(2\hat{\beta}_0) - 1}{\exp(2\hat{\beta}_0) + 1}$$
>
> **数学原理与读法**
> 1. **偏倚诊断** 若斜率 $\beta_{\text{SE}} > 0$ 且统计显著（如 Runco et al., 2026 报告 $F(1, 10.9) = 15.7, p = .002$），表明小样本研究系统性报告了偏大的效应量，证实全领域存在显著的[[Publication Bias|发表偏倚]]/小研究效应；
> 2. **效应量校正** 截距 $\hat{\beta}_0$ 代表消除了抽样标准误影响后的渐近总体效应；通过逆双曲正切函数 $\tanh(\hat{\beta}_0)$ 还原为相关系数 $r_{\text{adjusted}}$（例如原始加权平均为 $r = 0.22$，偏倚校正后为 $r = 0.17$，95% CI $[0.11, 0.22]$）。

---

## 软件实现与代码规程

> [!software-impl] R 语言环境（metafor 与 clubSandwich）实现多水平艾格检验
> ```R
> library(metafor)
> library(clubSandwich)
> 
> # 1. 计算抽样标准误 SE
> dat$sei <- sqrt(dat$vi)
> 
> # 2. 构建 CHE 协方差工作矩阵
> V_mat <- impute_covariance_matrix(vi = dat$vi, cluster = dat$cluster_id, r = 0.8)
> 
> # 3. 拟合多水平艾格回归模型（以 SE 为自变量）
> egger_model <- rma.mv(yi ~ sei, V_mat, 
>                       random = ~ 1 | cluster_id / effect_id, 
>                       data = dat, sparse = TRUE)
> 
> # 4. 应用 RVE 计算稳健标准误与小样本检验
> egger_robust <- coef_test(egger_model, vcov = "CR2", cluster = dat$cluster_id)
> print(egger_robust)
> 
> # 5. 提取偏倚校正后的截距并转换为相关系数 r
> b0 <- egger_model$b[1]
> r_adj <- tanh(b0)
> ci_lower <- tanh(egger_robust$beta[1] - 1.96 * egger_robust$SE[1])
> ci_upper <- tanh(egger_robust$beta[1] + 1.96 * egger_robust$SE[1])
> cat("偏倚校正后效应量 r =", round(r_adj, 3), 
>     "95% CI [", round(ci_lower, 3), ",", round(ci_upper, 3), "]\n")
> ```

---

## 适用场景与局限性

> [!method-fit] 适用判断
> - **强烈推荐** 包含嵌套结构（多重结果测量、多亚组比较）的一阶[[Meta-analysis|元分析]]，以及所有包含多个一阶元分析的[[Meta-meta-analysis|二阶元分析]]项目。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 6)]]
> - **输出优势** 能够同时提供统计检验 $p$ 值与经实证校正后的真实[[Effect Size|效应量]]点估计与[[Confidence Interval|置信区间]]。

> [!method-limits] 方法局限
> - **低功效风险** 当集群数量过少（$<10$）时，多水平元回归的斜率检验功效较低，可能遗漏微弱的发表偏倚；
> - **[[Heterogeneity|异质性]]混淆** [[Small Study Effects|小研究效应]]除了[[Publication Bias|发表偏倚]]外，也可能是由于小样本研究采用了更高强度的定制干预（实质异质性）所致，需要结合亚组分析综合研判。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联方向 | 说明 |
> |:-----|:-----|:---------|:-----|
> | [[Meta-meta-analysis]] | 综合方法 | 偏倚控制 | 二阶[[Meta-analysis\|元分析]]运用多水平艾格检验输出全领域校正后真实[[Effect Size\|效应量]]。 |
> | [[Correlated and Hierarchical Effects Model]] | 基础模型 | 建模底层 | 多水平艾格回归建立在 CHE 三水平随机效应方差分解之上。 |
> | [[Robust Variance Estimation]] | 推断方法 | 统计保障 | 运用 RVE 确保多水平艾格回归截距与斜率的[[Standard Error\|标准误]]保持稳健。 |
> | [[Argument_Runco_2026_CRJ\|Runco et al. (2026)]] | 论证 | 典范应用 | 检验发现显著小研究效应（$p = .002$），并将创造力总体效应量校正为 $r = 0.17$。 |
