---
title: Average Variance Extracted
aliases:
  - 平均方差抽取量
  - 平均方差提取量
  - AVE
  - 平均方差变异抽取量
summary: "在结构方程模型与验证性因子分析中评估潜变量对观测指标平均解释方差比例的统计指标，是判定收敛效度（AVE ≥ .50）与区分效度（Fornell-Larcker 准则）的核心心理测量学标准。"
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
  - "[[Convergent and Discriminant Validity]]"
related_theories: []
related_methods:
  - "[[Confirmatory Factor Analysis]]"
  - "[[Scale Development]]"
  - "[[Composite Reliability]]"
related_instruments:
  - "[[Research Literacy Scale for Teachers]]"
related_arguments:
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
confidence: high
status: draft
created: 2026-08-28
updated: 2026-08-28
---

# Average Variance Extracted

---

## 定义

> [!def] 方法定义
> **平均方差抽取量（Average Variance Extracted, AVE）** 是由 Claes Fornell 与 David F. Larcker 于 1981 年提出的量化心理测量学指标，用于在[[Confirmatory Factor Analysis|验证性因子分析]]（CFA）与结构方程模型（SEM）中衡量[[Construct|潜变量]]所解释的观测指标方差相对于测量误差方差的平均比例。AVE 是确立测量工具[[Convergent and Discriminant Validity|收敛效度]]（Convergent Validity）与区分效度（Discriminant Validity）的黄金判定标准。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, pp. 6–7)]]

> [!method-scope] 方法范围
> - **研究对象** 验证性因子分析（CFA）模型中潜变量与其所属各观测题项之间的标准化因子载荷矩阵与残差方差。
> - **问题类型** 评估多题项测量量表的构念收敛效度强度、检验不同潜变量因子之间的区分有效性。
> - **分析单位** 潜变量（Latent Factor）构念层级。
> - **输出形式** 介于 0 到 1 之间的变异抽取比例系数（通常以两位小数报告，如 $\text{AVE} = .54$）。

> [!citation-card]- 关键定义
> 平均方差抽取量反映了潜变量对其测度指标所能解释的平均方差大小。当 AVE 达到或超过 0.50 时，表明潜变量所解释的指标方差大于测量误差方差，构念的收敛效度获得实证支持。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 6)]]
>
> *Average Variance Extracted (AVE) measures the average percentage of variation that the latent construct explains among its indicators. An AVE of 0.50 or higher demonstrates adequate convergent validity, meaning the construct explains more variance than measurement error.*

---

## 方法定位

> [!method-position] 认识论与方法定位
> - **知识观** 假定可观测题项的变异由潜变量的“真变异”（共同性）与“测量误差”（特异变异与随机误差）共同构成，效度高低取决于真变异在总变异中的相对份额。
> - **研究者角色** 在估计 CFA 模型后，提取标准化因子载荷进行严谨的数学方差分解，而非依赖主观内容判断。
> - **有效性标准** 
>   1. **收敛效度基准** $\text{AVE} \ge .50$（Fornell & Larcker, 1981）；
>   2. **区分效度基准（Fornell-Larcker 准则）** 潜变量的 $\text{AVE}$ 必须大于该潜变量与模型中任何其他潜变量之间的相关系数平方（决定系数 $r^2$），即 $\text{AVE}_j > r_{jk}^2$（或 $\sqrt{\text{AVE}_j} > |r_{jk}|$）。
> - **不声称回答的问题** AVE 仅反映指标对构念的变异捕获程度，不能替代专家对题项语义和内容维度的定性审查。

> [!method-stack] 方法层级
> - **研究设计** [[Scale Development|量表编制]]与结构确证设计。
> - **数据收集** 大规模标准化问卷调查。
> - **分析方法** 验证性因子分析（CFA）、协方差结构分析。
> - **辅助技术** 极大似然估计（ML）、稳健极大似然估计（MLR）、`semTools` 自动化可靠性矩阵提取。

---

## 数学原理与计算公式

> [!formula-step] 公式步骤　平均方差抽取量（AVE）计算公式
> $$\text{AVE} = \frac{\sum_{i=1}^{k} \lambda_i^2}{\sum_{i=1}^{k} \lambda_i^2 + \sum_{i=1}^{k} \theta_i}$$
>
> **这个公式在做什么** 输入某一潜变量下所有 $k$ 个观测题项的标准化因子载荷 $\lambda_i$，计算各载荷平方和（解释方差）占总方差（载荷平方和加上各题项残差方差 $\theta_i$ 之和）的比例。
>
> **符号说明**
> - $\lambda_i$：第 $i$ 个题项在该潜变量上的标准化因子载荷（Standardized Factor Loading）。
> - $\theta_i$：第 $i$ 个题项的标准化测量误差方差（Error Variance）。在完全标准化解中，$\theta_i = 1 - \lambda_i^2$。
> - $k$：属于该潜变量的题项总数。
>
> **完全标准化简化形式** 当模型完全标准化（指标总方差为 1）且无误差协方差时，公式可直接简化为标准化载荷平方的算术平均值：
> $$\text{AVE} = \frac{1}{k} \sum_{i=1}^{k} \lambda_i^2$$
>
> **数学直觉** 因子载荷 $\lambda_i$ 是潜变量与题项之间的相关系数，$\lambda_i^2$ 代表潜变量对该题项方差的解释比例（决定系数）。AVE 就是该潜变量对这组题项解释力的平均值。
>
> > [!result-reading]- 结果怎么读
> > - **$\text{AVE} \ge .50$** 达到理想门槛，表明潜变量能解释题项方差的 $50\%$ 以上，收敛效度优良。
> > - **$.40 \le \text{AVE} < .50$** 处于可接受边缘。根据 Fornell & Larcker (1981)，若组合信度 $\text{CR} \ge .70$，即使 AVE 略低于 .50，构念的收敛效度在实际研究中仍可勉强接受。
> > - **$\text{AVE} < .40$** 表明测量误差占主导地位，存在较多低载荷或含混题项，需删题或重构维度。

---

## 区分效度检验：Fornell-Larcker 准则

> [!formula-step] 公式步骤　Fornell-Larcker 区分效度判定
> $$\text{AVE}_j > r_{jk}^2 \quad \Longleftrightarrow \quad \sqrt{\text{AVE}_j} > |r_{jk}| \quad (\forall k \neq j)$$
>
> **这个公式在做什么** 比较目标潜变量 $j$ 的平均方差抽取量 $\text{AVE}_j$ 与它和另一潜变量 $k$ 之间的共享方差（决定系数 $r_{jk}^2$）。
>
> **数学直觉** 目标构念解释自身题项的方差（内部收敛力）必须大于它与其他构念共享的方差（外部重叠度）。如果两个构念之间的相关系数平方超过了各自的 AVE，说明这两个构念在统计上无法有效区分，实际上测量的是同一概念。
>
> > [!result-reading]- 结果怎么读
> > 将各潜变量的 $\sqrt{\text{AVE}}$ 填入相关矩阵的对角线上：
> > - 如果对角线上的数值均**严格大于**该行和该列的所有非对角线相关系数（$r$），则区分效度完全确立；
> > - 若对角线数值小于某一同行/同列的相关系数，表明两维度存在严重概念重叠，需考虑合并因子或重构量表。

---

## 软件实现与代码规程

> [!software-impl] R 语言计算 AVE 与 CR 实现代码
> ```R
> library(lavaan)
> library(semTools)
> 
> # 1. 定义验证性因子分析模型
> cfa_model <- '
>   Awareness =~ R1 + R2 + R3 + R4
>   Attitude  =~ R5 + R6 + R7
>   Skills    =~ R8 + R9 + R10 + R11 + R12 + R13
>   Usage     =~ R14 + R15 + R16 + R17 + R18 + R19 + R20
> '
> 
> # 2. 拟合 CFA 模型
> fit <- cfa(cfa_model, data = sample_data, estimator = "MLR")
> 
> # 3. 提取 AVE、CR 与 Cronbach's Alpha 矩阵
> rel_matrix <- reliability(fit)
> print(rel_matrix)
> # 输出包含: alpha, omega (CR), ave
> 
> # 4. Fornell-Larcker 区分效度检验
> ave_vals <- rel_matrix["ave", ]
> sqrt_ave <- sqrt(ave_vals)
> corr_matrix <- lavInspect(fit, "cor.lv")
> 
> # 对角线替换为 sqrt(AVE) 进行对比
> diag(corr_matrix) <- sqrt_ave
> print(round(corr_matrix, 3))
> ```

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 在《[[Research Literacy Scale for Teachers|教师研究素养量表]]》CFA 验证中，计算 4 个维度的 AVE 分别为：研究意识（$.56$）、研究态度（$.50$）、研究技能（$.54$）、研究使用（$.56$），全部达到 $\ge .50$ 标准，且均高于各因子间的决定系数（$r^2$ 为 $.31\sim.59$），确立了优良的收敛与区分效度。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Scale Development]] | 宏观方法 | AVE 是量表编制第三阶段确立构念效度的核心标准。 |
> | [[Confirmatory Factor Analysis]] | 前置方法 | 提供计算 AVE 所需的标准化因子载荷与残差方差。 |
> | [[Composite Reliability]] | 配套方法 | 常与 AVE 同步计算并报告，共同构成潜变量效信度评估电池。 |
> | [[Convergent and Discriminant Validity]] | 理论概念 | AVE 提供收敛效度与 Fornell-Larcker 区分效度的量化判定依据。 |
> | [[Research Literacy Scale for Teachers]] | 测量工具 | 严格报告 4 维度 AVE 并通过区分效度检验的测量学典范。 |
