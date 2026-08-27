---
title: Pairwise Wald Tests
aliases:
  - 成对瓦尔德检验
  - 两两瓦尔德检验
  - 瓦尔德卡方检验
  - Pairwise Wald Test
  - Wald Chi-Square Test
summary: "在元分析与调节效应建模中，用于检验三个或更多亚组之间两两成对效应量差异统计显著性的推断检验方法"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 24
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/statistical
  - meta-analysis
  - moderator-analysis
  - hypothesis-testing
related_concepts:
  - "[[Effect Size]]"
  - "[[Heterogeneity]]"
  - "[[Standard Error]]"
  - "[[Variable]]"
  - "[[Construct]]"
  - "[[Interaction Effect]]"
  - "[[Mind Mapping]]"
  - "[[Argument Mapping]]"
  - "[[Concept Mapping]]"
  - "[[Epistemology]]"
  - "[[Hypothesis]]"
  - "[[Sample Size Determination]]"
  - "[[Statistical Significance]]"
  - "[[Confidence Interval]]"
  - "[[Sampling Error]]"
  - "[[Graphic Organizer]]"
  - "[[Higher-Order Thinking Skills]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Moderator Analysis]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Meta-regression]]"
  - "[[Random Sampling]]"
  - "[[Cochran's Q Test]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Lei_Ding_Chiu_2026_ERR]]"
confidence: high
status: draft
created: 2026-08-25
updated: 2026-08-25
---

# Pairwise Wald Tests

---

## 定义

> [!def] 方法定义
> 成对 Wald 检验（Pairwise Wald Tests）是在[[Meta-analysis|元分析]]分类[[Moderator Analysis|调节变量分析]]中，用于检验三个或更多亚组之间两两成对[[Effect Size|效应量]]估计值是否存在统计学显著差异的参数推断方法。在基于混合效应模型或[[Fixed-Effect and Random-Effects Models|随机效应模型]]的亚组分析中，当组间[[Heterogeneity|异质性]]总检验（$Q_{between}$）表明存在实质性变异时，成对 Wald 检验通过对比成对亚组效应量差值与联合抽样[[Standard Error|标准误]]的比率，构建服从自由度为 1 的卡方分布（$\chi^2$）统计量，从而精确判定具体哪些亚组之间存在真实且显著的效能级差。[[Argument_Lei_Ding_Chiu_2026_ERR|(Lei et al., 2026, pp. 9–10)]]

> [!method-scope] 方法范围
> - **研究对象** 元分析中包含三个及以上水平的分类调节[[Variable|变量]]（如不同教学干预形态、学段划分、测量[[Construct|构念]]层级）的亚组效应量估计值与方差协方差矩阵。
> - **问题类型** 事后比较与级差推断问题：在确定整体分类[[Interaction Effect|调节效应]]显著后，具体哪两组之间存在统计学显著的优势或劣势？
> - **分析单位** 调节变量的亚组效应量估计量（Subgroup Pooled Estimates）。
> - **输出形式** 两两比较的 Wald 统计量 $W$（或 $Z$ 值）、自由度 $df$、双尾 $p$ 值以及事后多重比较校正后的显著性判定。

> [!citation-card]- 关键定义
> 亚组分析显示组织器形态间存在显著异质性；成对 Wald 检验进一步证实[[Mind Mapping|思维导图]]、[[Argument Mapping|论证图]]与[[Concept Mapping|概念图]]两两之间均存在极显著差异。[[Argument_Lei_Ding_Chiu_2026_ERR|(Lei et al., 2026, p. 10)]]
>
> *Subgroup analyses showed significant heterogeneity among organizer types; pairwise Wald tests further confirmed that mind mapping, argument mapping, and concept mapping significantly differed from one another.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 统计推断后设验证：将宏观分类维度的总体变异细化为微观亚组间的阶梯式因果比较，避免因笼统的大类合并而掩盖内在层级机制。
> - **研究者角色** 在理论指导下预设分类层级，并在拒绝总同质性[[Hypothesis|假设]]后执行严谨的事后推断检验，避免无依据的多重事后数据窥探。
> - **有效性标准** 统计结论效度（检验各亚组[[Effect Size|效应量]]方差估计的准确性与[[Sample Size Determination|样本量]]充分性）与多重假设检验的族系误差率控制（Family-Wise Error Rate, FWER）。
> - **不声称回答的问题** 不能替代连续[[Variable|变量]]的函数形态拟合（连续趋势应采用[[Meta-regression|元回归]]），亦不能脱离总模型独立解释未被控制的混杂变量。

> [!contrast-table] 成对 Wald 检验 vs 组间总[[Heterogeneity|异质性]]检验（Q_between）
> | 比较维度 | 组间总异质性检验（Cochran's $Q_{between}$） | 成对 Wald 检验（Pairwise Wald Tests） |
> |---|---|---|
> | **检验性质** | **总体泛指检验（Omnibus Test）** | **事后成对精确检验（Post-Hoc Pairwise Test）** |
> | **原假设 $H_0$** | 所有亚组的真实效应量完全相等（$\theta_1 = \theta_2 = \dots = \theta_k$） | 特定两亚组真实效应量相等（$\theta_j = \theta_k$） |
> | **统计分布** | 卡方分布 $\chi^2(k - 1)$，自由度为亚组数减 1 | 卡方分布 $\chi^2(1)$ 或渐近正态分布 $Z$ |
> | **推断能力** | 仅能判断各亚组间是否存在不全相同的变异，无法定位具体组间差异 | 精确定位两两亚组间的优劣级差与显著性边界 |
> | **典型局限** | 组数 $\ge 3$ 时无法支持两两排序推论 | 比较轮次多时需防范多重检验 I 型错误膨胀 |

---

## 研究程序

> [!proc] 通用程序
> 1. 构建[[Meta-analysis|元分析]]分类调节[[Variable|变量]]亚组模型，通过 Cochran's $Q_{between}$ 检验评估分类变量整体是否具有[[Statistical Significance|统计显著性]]。
> 2. 提取各亚组的合并[[Effect Size|效应量]]点估计值 $\hat{\theta}_j$、[[Standard Error|标准误]] $SE_j$ 及其对应的抽样方差 $\text{Var}(\hat{\theta}_j)$。
> 3. 计算目标两两亚组间的效应差值与联合方差，构造成对 Wald 统计量 $W$。
> 4. 根据卡方分布 $\chi^2(1)$ 计算双尾 $p$ 值，必要时运用 Bonferroni 或 Holm 方法执行多重比较 $p$ 值校正。
> 5. 结合效应量点估计方向与[[Confidence Interval|置信区间]]，对两两亚组的效能级差进行实质性理论阐释。

### 量化方法模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 包含亚组划分标签、各亚组效应量汇总估计值及其协方差矩阵的元分析汇总数据。
> - **样本与单位** 各亚组内纳入的独立效应量数 $k_j$ 与参与者[[Sample Size Determination|样本量]] $N_j$。
> - **变量或指标** 
>   - 效应量估计：亚组 $j$ 的合并效应量 $\hat{\theta}_j$ 与亚组 $k$ 的合并效应量 $\hat{\theta}_k$。
>   - 联合方差：独立亚组间抽样方差之和 $\text{Var}(\hat{\theta}_j) + \text{Var}(\hat{\theta}_k)$。
> - **模型或统计量** Wald $\chi^2$ 统计量（$W$）。
> - **诊断与检验** 正态性渐近[[Hypothesis|假设]]检查、各亚组样本量均衡度与多重检验校正。

> [!formula-step] 公式步骤　独立亚组成对 Wald 统计量计算
> $$W_{jk} = \frac{(\hat{\theta}_j - \hat{\theta}_k)^2}{\text{Var}(\hat{\theta}_j) + \text{Var}(\hat{\theta}_k)} \sim \chi^2(1)$$
>
> **这个公式在做什么** 计算亚组 $j$ 与亚组 $k$ 之间效应量差值的平方与其联合抽样方差的比值，用于推断两亚组真实效应量是否存在显著差异。
>
> **符号说明**
> - $W_{jk}$ 亚组 $j$ 与亚组 $k$ 之间的成对 Wald 检验统计量
> - $\hat{\theta}_j, \hat{\theta}_k$ 两亚组的加权合并效应量点估计值（如 Hedges' $g$）
> - $\text{Var}(\hat{\theta}_j), \text{Var}(\hat{\theta}_k)$ 两亚组各自合并效应量的抽样方差（即 $SE_j^2$ 与 $SE_k^2$）
>
> **数学直觉** 若原假设成立（两组真实效应无差异），两组样本估计值的差值纯粹由[[Sampling Error|抽样误差]]引起，差值除以标准误差后服从标准正态分布，其平方服从自由度为 1 的卡方分布。$W$ 越大，表明两组真实差异显著超越[[Random Sampling|随机抽样]]波动的概率越高。
>
> **结果怎么读** 当 $W > 3.84$（对应 $\alpha = .05$）或 $W > 10.83$（对应 $\alpha = .001$）时，$p < .05$ 或 $p < .001$，拒绝两组效应相等的零假设，判定两亚组成对差异具有统计学显著性。
>
> **注意事项** 上述公式假定两亚组间抽样相互独立（$\text{Cov}(\hat{\theta}_j, \hat{\theta}_k) = 0$）。若同一初级研究同时贡献了多个亚组的数据，需在多水平元分析模型下纳入协方差项进行校正。

> [!software-impl] 软件实现
> - **推荐软件** R（`metafor` 包、`multcomp` 包）、Stata（`test` 命令）、Comprehensive Meta-Analysis (CMA)。
> - **核心包或命令**
>   - R `metafor` 实现：
>     ```r
>     library(metafor)
>     # 拟合分类调节变量混合效应模型
>     res <- rma(yi, vi, mods = ~ factor(go_type) - 1, data = dat, method = "REML")
>     # 成对 Wald 检验 (检验思维导图与概念图系数差异)
>     anova(res, btt = c(1, 2))  # 或指定对比矩阵 anova(res, L = c(1, -1, 0))
>     ```
> - **实现流程** 拟合无截距亚组模型 -> 设定线性对比矩阵（Linear Contrast Matrix）-> 运行 Wald 假设检验 -> 输出 $W$ 与校正后 $p$ 值。
> - **报告标准** 完整报告各亚组的点估计值、标准误、成对比较的 Wald 统计量 $W$（或 $\chi^2$ 值）、自由度及确切 $p$ 值。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 分类调节[[Variable|变量]]包含三个或更多亚组，且总 $Q_{between}$ 检验显著，研究者需要严格确定两两亚组之间是否存在统计学显著的层级优劣时。[[Argument_Lei_Ding_Chiu_2026_ERR|(Lei et al., 2026, pp. 9–10)]]
> - **谨慎使用** 某个亚组包含的独立研究数过少（如 $k_j < 3$）导致方差估计极不稳定时；此时需报告非参数置换检验或宽置信区间。
> - **不适合使用** 调节变量本身为连续数值变量（应直接使用[[Meta-regression|元回归]]，避免人为粗暴离散化导致信息损失）。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 多重比较累积 I 型错误风险；小样本亚组方差估计不足导致 Wald 检验功效偏低。
> - **适用边界** 依赖于大样本渐近正态性[[Hypothesis|假设]]；当各组[[Effect Size|效应量]]高度相关但协方差未被建模时，可能产生有偏推断。
> - **误用风险** 在总 $Q_{between}$ 检验不显著的情况下盲目开展大量未经校正的事后成对检验，导致假阳性发现。
> - **补救方式** 结合 Bonferroni 或 FDR 校正；配合[[Confidence Interval|置信区间]]重叠度检验；在多水平框架下建模研究内相关性。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Meta-analysis]] | 前置方法 | 成对 Wald 检验依附于元分析的亚组调节检验模块，为其提供事后两两推断工具。 |
> | [[Cochran's Q Test]] | 互补检验 | $Q_{between}$ 检验提供分类变量的总体泛指检验，成对 Wald 检验提供事后两两精确检验。 |
> | [[Meta-regression]] | 替代与并列方法 | 元回归适用于连续型与多变量联合调节建模，成对 Wald 检验专注于离散亚组的事后成对级差比较。 |
> | [[Fixed-Effect and Random-Effects Models]] | 建模基础 | 各亚组的合并[[Effect Size\|效应量]]与抽样方差来源于随机或固定效应模型的加权估计。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Lei_Ding_Chiu_2026_ERR|Lei et al. (2026)]] 运用成对 Wald 检验系统验证了[[Graphic Organizer|图形组织器]]形态（[[Mind Mapping|思维导图]] $g = 1.041$ > [[Argument Mapping|论证图]] $g = 0.798$ > [[Concept Mapping|概念图]] $g = 0.548$）、学段（中学 $g = 1.113$ > 小学 $g = 0.877$ > 大学 $g = 0.659$）以及[[Higher-Order Thinking Skills|高阶思维]][[Construct|构念]]层级（倾向与过程显著强于技能结果）的两两级差显著性。
