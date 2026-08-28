---
title: Three-Level Meta-Analysis
aliases:
  - 三层元分析
  - 多层元分析
  - Multilevel Meta-analysis
  - 3层元分析
  - 三水平元分析
summary: "处理同一原始研究内报告多个相关效应量所致统计依赖性的多层模型，将总方差分解为抽样误差、研究内方差与研究间方差"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 34
method_related_level: 4
method_related_stars: "⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - meta-analysis
  - multilevel-modeling
  - effect-size
  - statistical-dependence
  - quantitative-methods
related_concepts:
  - "[[Effect Size]]"
  - "[[Sampling Error]]"
  - "[[Between-Study Variance]]"
  - "[[Document]]"
  - "[[Dependent Variable]]"
  - "[[Construct]]"
  - "[[Heterogeneity]]"
  - "[[Confidence Interval]]"
  - "[[Variable]]"
  - "[[Interaction Effect]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Hypothesis]]"
  - "[[Epistemology]]"
  - "[[Funnel Plot]]"
  - "[[Qualitative Codebook]]"
  - "[[Research Question]]"
  - "[[Literature Search]]"
  - "[[Sample Size Determination]]"
  - "[[Statistical Significance]]"
  - "[[Publication Bias]]"
  - "[[Measurement Alignment]]"
  - "[[Standard Error]]"
  - "[[Reliability]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-regression]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Robust Variance Estimation]]"
  - "[[Systematic Review]]"
  - "[[PRISMA]]"
  - "[[Effect Size Conversion]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Moderator Analysis]]"
related_arguments:
  - "[[Argument_Song_Choi_2026_FPSYG]]"
  - "[[Argument_Park_2026_TSC]]"
confidence: high
status: draft
created: 2026-08-20
updated: 2026-08-25
---

# Three-Level Meta-Analysis

---

## 定义

> [!def] 方法定义
> 三层[[Meta-analysis|元分析]]（Three-Level Meta-Analysis）是将多层线性模型（Multilevel Linear Modeling）扩展应用于元分析的量化合成方法，专门用于解决单项原始研究报告多个相关[[Effect Size|效应量]]时产生的统计依赖性（Statistical Dependence）问题。该方法将观察到的总变异解构为三个层级：第一层为效应量层面的[[Sampling Error|抽样误差]]方差（Sampling Variance），第二层为同一研究内部不同效应量之间的研究内方差（Within-Study Variance），第三层为不同研究之间的[[Between-Study Variance|研究间方差]]（Between-Study Variance）。[[Argument_Song_Choi_2026_FPSYG|(Song & Choi, 2026, pp. 4–5)]]

> [!method-scope] 方法范围
> - **研究对象** 包含多个非独立效应量的实证研究[[Document|文献]]集（如同一研究报告多个[[Dependent Variable|结果变量]]、子样本、[[Construct|构念]]维度或测量时间点）。
> - **问题类型** 适合回答跨研究综合效应估计、真实[[Heterogeneity|异质性]]分解、研究内与研究间特征对效应量的调节作用检验等问题。
> - **分析单位** 包含三层嵌套结构：第一层为具体效应量（Effect Size），第二层为原始研究（Study），第三层为更高层级的聚类单位或跨研究总体。
> - **输出形式** 汇总加权效应量估计值、95% [[Confidence Interval|置信区间]]（Confidence Interval, CI）、各层方差分量（$\tau_{(2)}^2$ 与 $\tau_{(3)}^2$）、异质性比例指标（$I_{(1)}^2$、$I_{(2)}^2$、$I_{(3)}^2$）、多[[Variable|变量]][[Meta-regression|元回归]][[Interaction Effect|调节效应]]检验统计量（$F$ 或 $\chi^2$）。

> [!citation-card]- 关键定义
> 三层元分析模型通过建立分层随机效应结构，使得研究者能够纳入[[Primary and Secondary Documents|原始文献]]中报告的所有相关效应量，既避免了人为平均或强制舍弃效应量导致的信息损失与偏倚，又严格遵守了统计独立性[[Hypothesis|假设]]。[[Argument_Song_Choi_2026_FPSYG|(Song & Choi, 2026, pp. 4–5)]]
>
> *Adopting this hierarchical structure enables all relevant effect sizes to be used in the meta-analysis without violating the independence assumption.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 视实证[[Document|文献]]中的测量结果为包含多源误差与多层[[Heterogeneity|异质性]]的抽样观察值，主张通过分层方差分解捕捉真实效应的结构性分布。
> - **研究者角色** 在[[Effect Size|效应量]][[Coding in Qualitative Research|编码]]、[[Construct|构念]]分类、调节[[Variable|变量]]识别和协方差结构假定中行使理论与统计判断。
> - **有效性标准** 依靠受限最大似然法（Restricted Maximum Likelihood, REML）估计、对数似然比检验（Log-Likelihood Ratio Test, LRT）对比模型拟合优度、[[Robust Variance Estimation|稳健方差估计]]（Robust Variance Estimation, RVE）以及[[Funnel Plot|漏斗图]]与三层 Egger 回归检验。
> - **不声称回答的问题** 不能仅凭观察性效应量的[[Meta-analysis|元分析]]关联直接推断因果机制，也不能自动纠正原始研究内在的方法学偏倚。

> [!method-stack] 方法层级
> - **研究设计** [[Systematic Review|系统综述]]（Systematic Review）与量化证据综合设计。
> - **数据收集** 基于电子数据库检索、[[PRISMA]] 流程筛选以及标准化[[Qualitative Codebook|编码手册]]提取相关系数、标准化均数差或回归系数。
> - **分析方法** 多层随机效应建模、受限最大似然估计（REML）、多变量[[Meta-regression|元回归]]调节分析、逐一剔除敏感性分析。
> - **辅助技术** [[Effect Size Conversion|效应量转换]]（如将回归系数 $\beta$ 转换为相关系数 $r$、Fisher\'s $z$ 变换）、三层 Egger 回归检验、标准化残差异常值诊断。

---

## 研究程序

> [!proc] 通用程序
> 1. 确立[[Research Question|研究问题]]与纳入排除标准，完成系统[[Literature Search|文献检索]]与[[Document|文献]]质量评价。
> 2. 提取所有合格[[Effect Size|效应量]]及[[Sample Size Determination|样本量]]，将其统一转换为标准尺度（如 Pearson 相关系数 $r$ 进而转换为 Fisher\'s $z$ 值）。
> 3. 构建无协[[Variable|变量]]的三层空模型（Intercept-Only Model），估计总效应量，并通过对数似然比检验（LRT）检验第二层与第三层方差的[[Statistical Significance|统计显著性]]。
> 4. 计算各层方差分量与[[Heterogeneity|异质性]]比例指标（$I_{(1)}^2, I_{(2)}^2, I_{(3)}^2$），评估异质性来源。
> 5. 引入类别或连续型调节变量构建混合效应多变量[[Meta-regression|元回归]]模型，评估背景特征、测量工具与学段等因素的[[Interaction Effect|调节效应]]。
> 6. 执行[[Publication Bias|发表偏倚]]检验（三层 Egger 检验与[[Funnel Plot|漏斗图]]）与敏感性分析（逐一排除与异常值诊断），最后将 Fisher\'s $z$ 转换回原始指标进行解释与呈现。

### 量化方法模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 嵌套数据结构（Nested Data），多个效应量 $i$ 嵌套于独立研究 $j$ 中。
> - **样本与单位** 纳入研究数 $k$、效应量总数 $m$ 以及总受试者人数 $N$。
> - **变量或指标** 效应量 $y_{ij}$（如 Fisher\'s $z$）、已知抽样方差 $v_{ij}$、各层调节变量 $X_{ij}$（如学段、[[Construct|构念]]类型、[[Measurement Alignment|测量对齐]]度）。
> - **模型或统计量** 三层随机效应多层线性模型、固定效应回归系数、限制性最大似然方差分量 $\tau_{(2)}^2$ 与 $\tau_{(3)}^2$。
> - **诊断与检验** $Q$ 统计量检验总异质性、似然比检验（LRT）对比二层与三层模型拟合、标准化残差 $|z| > 3.29$ 异常值检验。

> [!formula-step] 公式步骤　三层[[Fixed-Effect and Random-Effects Models|随机效应模型]]
> $$y_{ij} = \gamma_{00} + u_{(3)j} + u_{(2)ij} + e_{ij}$$
>
> **这个公式在做什么** 将研究 $j$ 中第 $i$ 个观察效应量 $y_{ij}$ 分解为全域真实均值 $\gamma_{00}$、研究间随机效应 $u_{(3)j}$、研究内效应量间随机效应 $u_{(2)ij}$ 以及已知[[Sampling Error|抽样误差]] $e_{ij}$。
>
> **符号说明** $y_{ij}$ 为观察到的第 $i$ 个效应量；$\gamma_{00}$ 为所有研究与效应量的总体平均真实效应；$u_{(3)j} \sim \mathcal{N}(0, \tau_{(3)}^2)$ 为第 $j$ 项研究偏离总均值的效应（Level 3 方差）；$u_{(2)ij} \sim \mathcal{N}(0, \tau_{(2)}^2)$ 为第 $j$ 项研究内第 $i$ 个效应量偏离该研究均值的效应（Level 2 方差）；$e_{ij} \sim \mathcal{N}(0, v_{ij})$ 为抽样误差（Level 1 方差，通常根据样本量预先计算固定）。
>
> **数学直觉** 传统[[Meta-analysis|元分析]][[Hypothesis|假设]]每个研究只提供一个独立效应量，若同一研究提供多个效应量，这些效应量共享相同的受试者和研究环境，具有相关性。三层模型引入两级随机截距，将研究内相关性分离到 Level 2，从而提供无偏的[[Standard Error|标准误]]估计与[[Confidence Interval|置信区间]]。
>
> **结果怎么读** $\gamma_{00}$ 显著大于 0 表明总体正向关联；$\tau_{(3)}^2$ 显著说明研究间存在真实异质性；$\tau_{(2)}^2$ 显著说明同一研究内部不同测量或子构念间存在实质性变异。
>
> **注意事项** Level 1 抽样方差 $v_{ij}$ 视为已知固定值；模型通常使用受限最大似然估计（REML）。[[Argument_Song_Choi_2026_FPSYG|(Song & Choi, 2026, pp. 4–5)]]

> [!formula-step] 公式步骤　三层方差比例分解
> $$I_{(1)}^2 = \frac{\tilde{v}}{\tilde{v} + \tau_{(2)}^2 + \tau_{(3)}^2} \times 100\%, \quad I_{(2)}^2 = \frac{\tau_{(2)}^2}{\tilde{v} + \tau_{(2)}^2 + \tau_{(3)}^2} \times 100\%, \quad I_{(3)}^2 = \frac{\tau_{(3)}^2}{\tilde{v} + \tau_{(2)}^2 + \tau_{(3)}^2} \times 100\%$$
>
> **这个公式在做什么** 计算抽样误差（Level 1）、研究内变异（Level 2）与研究间变异（Level 3）在总变异中所占的相对百分比。
>
> **符号说明** $\tilde{v}$ 为典型抽样方差；$\tau_{(2)}^2$ 为 Level 2 研究内真实方差；$\tau_{(3)}^2$ 为 Level 3 [[Between-Study Variance|研究间真实方差]]。
>
> **数学直觉** 将经典的 $I^2$ 统计量推广至三层架构，使研究者能够明确异质性主要来自于研究内不同测量维度的差异（$I_{(2)}^2$）还是跨研究背景与样本的宏观差异（$I_{(3)}^2$）。
>
> **结果怎么读** $I_{(2)}^2 + I_{(3)}^2$ 反映真实异质性占总变异的比例；若 $I_{(3)}^2 > I_{(2)}^2$，说明跨研究情境差异大于研究内构念测量差异。
>
> **注意事项** 三个比例之和恒等于 100%。[[Argument_Song_Choi_2026_FPSYG|(Song & Choi, 2026, p. 5)]]

> [!software-impl] 软件实现
> - **数据处理** R 语言环境，清洗数据并计算效应量与已知抽样方差。
> - **推荐软件** R（v4.0 以上）。
> - **核心包或命令** `metafor` 包中的 `rma.mv()` 函数。
> - **实现流程** 设定模型公式 `rma.mv(yi = z, V = v, random = ~ 1 | study_id / es_id, data = dat, method = "REML")`；加入调节变量使用 `mods = ~ factor(moderator)`；使用 `anova()` 或似然比检验比较不同嵌套模型。
> - **报告标准** 完整报告各层方差分量（$\tau_{(2)}^2, \tau_{(3)}^2$）、$I^2$ 比例、似然比检验 $\chi^2$ 值、固定效应估计值、95% 置信区间以及元回归 $F$ 检验。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 原始研究频繁报告多个相关结果指标、多个分量表[[Construct|构念]]、不同时间点追踪数据或多个子样本时的量化[[Systematic Review|系统综述]]。[[Argument_Song_Choi_2026_FPSYG|(Song & Choi, 2026, pp. 4–5)]]
> - **谨慎使用** 纳入研究数量较少（如 $k < 10$）时，Level 3 真实方差的估计可能缺乏统计功效或不稳定。
> - **不适合使用** 每项研究仅报告严格单一独立[[Effect Size|效应量]]的情形（此时退化为传统二层[[Fixed-Effect and Random-Effects Models|随机效应模型]]）。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 原始研究层面的选择性报告偏倚、测量工具[[Reliability|信度]]缺陷以及未观测到的混杂因素。
> - **适用边界** 依赖于足够的样本研究数与[[Effect Size|效应量]]数量以保证受限最大似然估计的收敛性与功效。
> - **误用风险** 容易将调节分析中的生态学关联（Ecological Association）误认为个体层面的因果机制。
> - **补救方式** 结合[[Robust Variance Estimation|稳健方差估计]]（RVE）、三层 Egger 检验、逐一剔除敏感性分析及离群值残差诊断。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Meta-analysis]] | 基础方法 | 三层元分析是传统二层元分析在多层数据结构下的拓展。 |
> | [[Fixed-Effect and Random-Effects Models]] | 统计模型 | 提供了三层模型中随机效应设定的理论基础。 |
> | [[Moderator Analysis]] | 分析策略 | 在三层架构下通过多元[[Meta-regression|元回归]]检验研究内与研究间协[[Variable|变量]]的[[Interaction Effect|调节效应]]。 |
> | [[Meta-regression]] | 分析方法 | 三层混合效应模型通过元回归整合固定效应协变量。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Song_Choi_2026_FPSYG|Song & Choi (2026)]] — 采用三层[[Meta-analysis|元分析]]模型分析了嵌套在 18 项研究中的 512 个[[Effect Size|效应量]]，妥善处理了单个研究同时报告多个[[Epistemology|认识论]][[Construct|构念]]与学习成果指标所造成的统计依赖性。
> - [[Argument_Park_2026_TSC|Park et al. (2026)]] — 对嵌套在 29 项研究中的 51 个相关系数采用三层随机效应[[Meta-analysis|元分析]]，将方差分解为[[Sampling Error|抽样误差]]、研究内与研究间三层，处理同一研究报告多个测量组合[[Effect Size|效应量]]造成的统计依赖性。
