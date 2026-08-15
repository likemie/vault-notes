---
title: Confirmatory Factor Analysis
aliases:
  - "验证性因子分析"
  - "CFA"
summary: "一种用于检验观测变量（如问卷题项）与潜在结构（如潜变量/因子）之间假设关系的多元统计方法。常用于量表开发、结构效度检验和测量模型确证。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 12
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags: []
related_concepts:
  - "[[Variable]]"
  - "[[Construct Validity]]"
  - "[[Construct]]"
  - "[[Epistemology]]"
  - "[[Epistemological Beliefs]]"
  - "[[Hypothesis]]"
  - "[[Sample Size Determination]]"
  - "[[Questionnaire]]"
  - "[[Confidence Interval]]"
  - "[[Standard Error]]"
related_theories: []
related_methods:
  - "[[Causal Modeling]]"
  - "[[Chi-Squared Test]]"
related_instruments:
  - "[[Epistemic and Ontological Cognition Questionnaire]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Greene_2010_JEP]]"
confidence: medium
status: draft
created: 2026-08-15
updated: 2026-08-15
---

# Confirmatory Factor Analysis

---

## 定义

> [!def] 方法定义
> 验证性因子分析（Confirmatory Factor Analysis, CFA）是一种用来测试研究者预先设定的潜[[Variable|变量]]（因子）结构是否与实际收集到的数据相契合的统计方法。与探索性因子分析（EFA）不同，CFA 要求研究者在分析前就明确指定哪些外显指标（观测变量）对应哪些潜在因子。

> [!method-scope] 方法范围
> - **研究对象** 多维度的量表测量数据、外显指标体系。
> - **问题类型** 回答预设的测量模型是否具有良好的[[Construct Validity|结构效度]]（[[Construct]] Validity）。
> - **分析单位** 个体。
> - **输出形式** 因子载荷估计值、模型整体拟合指数（如 $\chi^2$, RMSEA, CFI, SRMR 等）。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为心理与教育测量中的诸多概念（如智力、动机、[[Epistemological Beliefs|认识论信念]]）是无法直接观测的潜[[Variable|变量]]，必须通过一组可观测的指标来推断。
> - **研究者角色** 研究者基于先验理论或前期探索研究提出结构[[Hypothesis|假设]]，主观决定模型的设定。
> - **有效性标准** 各种绝对拟合指数和相对拟合指数（如 RMSEA < .08, CFI > .90 等）。

> [!method-stack] 方法层级
> - **分析方法** 验证性因子分析（CFA）。
> - **辅助技术** 最大似然估计（ML）、加权最小二乘法（WLSMV，适用于类别变量）。

---

## 研究程序

> [!proc] 通用程序
> 1. 根据理论或前期研究，构建测量模型（指明题项与因子的对应关系，以及因子间的协方差）。
> 2. 收集足够规模的样本数据（通常要求 N > 200）。
> 3. 运行模型并进行参数估计。
> 4. 评价模型拟合度。如果不佳，可参考修正指数（Modification Indices, MI）谨慎修改模型。
> 5. 报告因子载荷、测量误差与整体拟合指数。

### 量化方法模块

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** 横截面数据为主，追踪数据可用于做测量等值性（Measurement Invariance）检验。
> - **变量或指标** 观测变量（题项分数）、潜变量（因子）、测量误差。
> - **模型或统计量** 结构方程模型（[[Causal Modeling|SEM]]）的测量模型部分。
> - **诊断与检验** $\chi^2$ 检验（易受大[[Sample Size Determination|样本量]]影响）、RMSEA、SRMR、CFI、TLI 等拟合指标。

> [!formula-step] 公式步骤　CFA 基础测量方程
> $$ y_i = \Lambda \eta_i + \epsilon_i $$
>
> **这个公式在做什么** 描述观测变量的得分是如何由潜在因子的真实水平与测量误差共同决定的。
>
> **符号说明** $y_i$ 是观测变量向量；$\Lambda$ 是因子载荷矩阵（Factor Loadings）；$\eta_i$ 是潜因子向量；$\epsilon_i$ 是特定测量误差向量。
>
> **数学直觉** 把复杂的卷面分数降维剥离出纯净的“潜在特质”得分，同时把杂乱的误差隔离出来。
>
> **结果怎么读** $\Lambda$ 越大且显著，说明该题项越能有效代表其背后的潜变量（通常要求标准载荷 > 0.4 或 0.5）。

> [!formula-step] 公式步骤　近似误差均方根（RMSEA）
> $$ RMSEA = \sqrt{\frac{\max(\chi^2 - df, 0)}{df(N - 1)}} $$
>
> **这个公式在做什么** 测量模型隐含的协方差矩阵与真实总体协方差矩阵之间的差异（误差），并对复杂模型施加惩罚。
>
> **符号说明** $\chi^2$ 是模型的卡方值；$df$ 是模型的自由度；$N$ 是样本量。
>
> **数学直觉** 传统的[[Chi-Squared Test|卡方检验]]（$\chi^2$）对大样本量极为敏感，样本一多就容易拒绝模型（即认为拟合不好）。RMSEA 通过除以样本量 $N$ 和自由度 $df$ 进行了除颤修正。它评估的是“近似拟合”：允许模型有微小瑕疵，看它每个自由度上的平均误差有多大。
>
> **结果怎么读** 误差**越小越好**。业界公认：< .05 代表拟合极好，< .08 代表拟合可接受，> .10 则说明模型存在严重缺陷。

> [!formula-step] 公式步骤　比较拟合指数（CFI）
> $$ CFI = 1 - \frac{\max(\chi^2_M - df_M, 0)}{\max(\chi^2_M - df_M, \chi^2_B - df_B, 0)} $$
>
> **这个公式在做什么** 将你设定的模型（目标模型 $M$）与一个最烂的“基线模型”（Baseline model $B$，假定所有变量互不相关）进行打分对比。
>
> **数学直觉** 这是一种“相对评优”的思路：看看你的模型比最差的随机情况进步了多少。如果你的模型解释力远超基线模型，那么右侧的分数项就会趋近于 0，从而使 CFI 趋近于满分 1。
>
> **结果怎么读** 范围在 0 到 1 之间，**越大越好**。通常以 > .90 作为及格线，> .95 视为拟合极佳。

> [!formula-step] 公式步骤　标准化残差均方根（SRMR）
> $$ SRMR = \sqrt{ \frac{\sum_{i \le j} (r_{ij} - \hat{r}_{ij})^2}{p(p+1)/2} } $$
>
> **这个公式在做什么** 简单粗暴地计算真实数据的相关矩阵（$r_{ij}$）与模型预测的相关矩阵（$\hat{r}_{ij}$）之间的平均差异。
>
> **数学直觉** 就是看“模型推算出来的题项相关性”跟“实际[[Questionnaire|问卷]]收集到的题项相关性”在标准化之后，平均每对变量相差多少。
>
> **结果怎么读** 作为残差指标，当然**越小越好**。通常以 < .08 为拟合可接受的黄金法则。

> [!software-impl] 软件实现
> - **推荐软件** Mplus、R（lavaan 包）、Amos。
> - **报告标准** 需报告 $\chi^2$ 及其自由度和 $p$ 值，RMSEA 及其 90% [[Confidence Interval|置信区间]]，CFI，SRMR，以及各个题项的标准化因子载荷。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 验证成熟量表在不同人群中的[[Construct Validity|结构效度]]，或在进行复杂的[[Causal Modeling|结构方程建模]]前验证测量模型。

---

## 局限性

> [!method-limits] 方法局限
> - **误用风险** 为了追求好的拟合指数，无视理论依据盲目释放误差协方差（ correlated errors）。
> - **适用边界** [[Sample Size Determination|样本量]]过小时估计不稳定；当观测指标不是连续[[Variable|变量]]而是 Likert 等级评分时，使用传统 ML 估计可能导致[[Standard Error|标准误]]偏误。

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Greene_2010_JEP|Greene et al. (2010)]] —  使用验证性因子分析（CFA）评估了《[[Epistemic and Ontological Cognition Questionnaire|认识论与本体论认知问卷]]》（EOCQ）在数学和历史领域的维度结构及其数据拟合度。
