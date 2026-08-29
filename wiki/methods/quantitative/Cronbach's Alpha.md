---
title: Cronbach's Alpha
aliases:
  - 克隆巴赫系数
  - 克隆巴赫阿尔法系数
  - 克隆巴赫α系数
  - 内部一致性信度系数
  - Cronbach alpha
  - "Cronbach's α"
  - Alpha reliability
summary: "经典测量理论下评估多题项量表内部一致性信度的基石指标，通过解构题项方差之和与总分方差的比率反映测验项目的同质性与测量误差，其数学有效性严格依赖于单维性与本质τ-等值模型假设。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 22
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/psychometrics
  - measurement/reliability
  - scale-development/validation
related_concepts:
  - "[[Internal Consistency]]"
  - "[[Reliability]]"
  - "[[Construct]]"
  - "[[Likert Scale]]"
  - "[[Semantic Differential]]"
  - "[[Questionnaire]]"
  - "[[Variable]]"
  - "[[Epistemology]]"
  - "[[Hypothesis]]"
  - "[[Item Analysis]]"
  - "[[Split-Half Reliability]]"
  - "[[Sample Size Determination]]"
related_theories:
  - "[[Classical Test Theory]]"
related_methods:
  - "[[Composite Reliability]]"
  - "[[Survey Research]]"
  - "[[Scale Development]]"
  - "[[Pearson Product-Moment Correlation]]"
  - "[[Confirmatory Factor Analysis]]"
  - "[[McDonald's Omega]]"
related_instruments:
  - "[[Research Literacy Scale for Teachers]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
confidence: high
status: draft
created: 2026-08-29
updated: 2026-08-29
---

# Cronbach's Alpha

---

## 定义

> [!def] 方法定义
> **克隆巴赫 $\alpha$ 系数（Cronbach's Alpha）** 是[[Classical Test Theory|经典测量理论]]（CTT）框架下评估多题项复合测量工具[[Internal Consistency|内部一致性]][[Reliability|信度]]（Internal Consistency Reliability）最通用的量化指标。它通过计算测验中所有可能折半[[Composite Reliability|组合信度]]的均值，度量同一量表（或分量表）内各个题项在多大程度上共同测量同一个潜在[[Construct|构念]]，从而估计由题项抽样变异所引起的测量误差比例。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, pp. 310–312)]]

> [!method-scope] 方法范围
> - **研究对象** 采用李克特多级计分（[[Likert Scale]]）、[[Semantic Differential|语义差异量表]]或连续评分的多题项[[Questionnaire|问卷]]与心理测验。
> - **问题类型** 测量工具内部一致性检验、量表纯化过程中的题项筛选、潜[[Variable|变量]]测量误差估计。
> - **分析单位** 测验题项（Items）与被试作答反应向量。
> - **输出形式** $\alpha$ 信度系数值（介于 0 到 1 之间）、标准化 $\alpha$ 值、删除某题项后的 $\alpha$ 变化值（$\alpha$ if item deleted）及矫正题总相关（Corrected Item-Total Correlation, CITC）。

> [!citation-card]- 关键定义
> 内部一致性检验反映了量表内部题项反应的一致程度。如果量表中的所有题项都在测量相同的构念，被试对这些题项的反应应当高度关联。克隆巴赫 $\alpha$ 系数是这一内部一致性检验的行业标准统计量。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, p. 311)]]
>
> *Internal consistency relates to the degree of consistency between item responses within a single instrument. If the items all measure the same underlying construct, responses across items should be correlated. Cronbach's alpha is the industry-standard statistic for reporting internal consistency.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 建立在[[Classical Test Theory|经典测量理论]]的真分数模型（$X = T + E$）之上，假定观测分数的方差由真实方差与随机误差方差加和构成，[[Internal Consistency|内部一致性]]反映真分数方差占总方差的比例。
> - **研究者角色** 研究者需在计算 $\alpha$ 之前验证量表的单维性（Unidimensionality），并审慎评估题项数量对 $\alpha$ 值的机械膨胀效应。
> - **有效性标准** 遵循统计结论效度与测量[[Reliability|信度]]标准：探索性量表要求 $\alpha \ge .70$；成熟应用与诊断量表要求 $\alpha \ge .80$（优选 $\ge .90$）；若 $\alpha > .95$ 则提示题项可能存在高度语义冗余。
> - **不声称回答的问题** $\alpha$ 系数**不能证明量表具有单维性（高 $\alpha$ 并不代表单因子结构）**；在违反本质 $\tau$-等值[[Hypothesis|假设]]（即各题项因子载荷不等）时，$\alpha$ 会成为真实信度的**下界保守估计**。

> [!method-stack] 方法层级
> - **研究设计** [[Survey Research|调查研究]]、[[Scale Development|量表编制]]、横断面心理测量。
> - **数据收集** [[Likert Scale|李克特量表]][[Questionnaire|问卷]]作答数据。
> - **分析方法** 方差-协方差矩阵分解、[[Item Analysis|项目分析]]（CITC 筛选）。
> - **辅助技术** McDonald's $\omega$ 对比验证、[[Split-Half Reliability|折半信度]]对比、删除题项后的 $\alpha$ 诊断。

---

## 研究程序与数学原理

### 量化分析与公式推导

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** $N$ 名被试在 $k$ 个题项上的作答矩阵（$N \times k$），总分 $X = \sum_{i=1}^k Y_i$。
> - **[[Sample Size Determination|样本量]]要求** 建议 $N \ge 100$ 且被试与题项比 $\ge 5:1$ 以获得稳定的方差估计。
> - **前置核心[[Hypothesis|假设]]**
>   1. **单维性（Unidimensionality）** 所有题项仅测量单一潜变量；
>   2. **本质 $\tau$-等值（Essential $\tau$-equivalence）** 各题项在潜变量上的因子载荷完全相等（$\lambda_1 = \lambda_2 = \dots = \lambda_k$）；
>   3. **误差不相关（Uncorrelated Errors）** 题项测量残差之间互不相关。

> [!formula-step] 公式步骤一　克隆巴赫 $\alpha$ 经典方差分解公式
> $$\alpha = \frac{k}{k-1} \left(1 - \frac{\sum_{i=1}^{k} \sigma_i^2}{\sigma_X^2}\right)$$
>
> **这个公式在做什么** 通过对比各个独立题项方差之和（$\sum \sigma_i^2$）与量表总分方差（$\sigma_X^2$），计算题项间共享协方差占总变异的比例。
>
> **符号说明**
> - $k$：测验中的题项总数（Number of items）。
> - $\sigma_i^2$：第 $i$ 个题项的作答方差。
> - $\sigma_X^2$：所有题项加总所得总分的方差（$\sigma_X^2 = \sum \sigma_i^2 + 2\sum_{i < j} \sigma_{ij}$）。
>
> **数学直觉** 当题项之间完全没有协变关系（$\sigma_{ij} = 0$）时，总方差等于各题方差之和，括号内为 $1 - 1 = 0$，$\alpha = 0$；当题项间高度正相关时，协方差使得总方差 $\sigma_X^2 \gg \sum \sigma_i^2$，分式接近 0，$\alpha \to 1$。
>
> **结果怎么读** $\alpha \in [0, 1]$。$\alpha < .60$ 不可接受；$.70 \le \alpha < .80$ 可接受；$.80 \le \alpha < .90$ 良好；$\alpha \ge .90$ 卓越。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 11)]]

> [!formula-step] 公式步骤二　标准化克隆巴赫 $\alpha$ 公式（Standardized Alpha / Spearman-Brown 形式）
> $$\alpha_{\text{standardized}} = \frac{k \bar{r}}{1 + (k - 1) \bar{r}}$$
>
> **这个公式在做什么** 当各题项方差不一致或数据已经过标准化处理时，基于题项间平均[[Pearson Product-Moment Correlation|皮尔逊相关]]系数（$\bar{r}$）计算[[Reliability|信度]]。
>
> **符号说明**
> - $\bar{r}$：题项间相关矩阵非对角线元素的算术平均值。
> - $k$：题项数量。
>
> **注意事项** 该公式揭示了 $\alpha$ 的**题项数量依赖性** 即使题间平均相关 $\bar{r}$ 较低，只要不断增加题项数 $k$，$\alpha$ 也会机械膨胀。因此不可盲目追求高 $\alpha$ 而增加冗余题项。

---

## 分析流程与应用

> [!proc] 量表[[Reliability|信度]]检验标准流程
> ```mermaid
> flowchart LR
>   A["采集样本作答数据"] --> B["反向计分题项转换与缺失值处理"]
>   B --> C["因子分析检验单维性（EFA / CFA）"]
>   C --> D["计算 CITC 题总相关与 α if item deleted"]
>   D --> E{"是否存在 CITC < .30 或删除后 α 显著上升题？"}
>   E --"是"--> F["剔除瑕疵题项并重新评估"]
>   E --"否"--> G["计算全量表与各分维度 α 系数"]
>   G --> H["同步计算 McDonald's ω 检验载荷异质性"]
>   H --> I["报告信度系数与置信区间"]
> ```

> [!software-impl] 软件实现
> - **R 语言 (`psych`)**
>   ```R
>   library(psych)
>   # 计算 alpha 并输出题项删除诊断
>   alpha_res <- psych::alpha(mydata[, c("Q1", "Q2", "Q3", "Q4")])
>   summary(alpha_res)
>   print(alpha_res$item.stats)
>   ```
> - **SPSS**
>   `Analyze -> Scale -> Reliability Analysis`，Model 选择 `Alpha`，在 `Statistics` 中勾选 `Scale if item deleted`。

---

## 局限性与现代替代

> [!method-limits] 方法局限与现代心理测量学批判
> - **本质 $\tau$-等值[[Hypothesis|假设]]过于苛刻** 现实教育测评中，各题项在潜[[Variable|变量]]上的因子载荷几乎不可能完全相等。当载荷不等（Congeneric Model）时，$\alpha$ 会**系统性低估真实[[Reliability|信度]]（Underestimation）**。
> - **题项数量膨胀虚假信度** $\alpha$ 对题项数 $k$ 极其敏感。一份包含 50 题的粗糙[[Questionnaire|问卷]]可能因为题数众多而呈现 $\alpha > .90$，掩盖个别题项相关微弱的事实。
> - **首选现代替代** 现代心理测量学一致推荐使用基于 [[Confirmatory Factor Analysis|CFA]] 因子载荷的 **McDonald's $\omega$** 与 **[[Composite Reliability|组合信度]]（CR）** 作为更准确的无偏信度估计。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[McDonald's Omega]] | 现代替代 | 突破等载荷假设限制，提供总信度（$\omega_t$）与分层信度（$\omega_h$）的无偏估计。 |
> | [[Composite Reliability]] | 结构方程对应物 | 基于 [[Confirmatory Factor Analysis\|CFA]] 完全标准化解直接计算潜[[Variable\|变量]]合成[[Reliability\|信度]]。 |
> | [[Split-Half Reliability]] | 经典前置方法 | 将测验分为两半计算相关后修正，$\alpha$ 在数学上等于所有可能折半信度的均值。 |
> | [[Classical Test Theory]] | 理论基础 | 提供真分数、误差方差与信度比率的数理公理体系。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 在[[Research Literacy Scale for Teachers|教师研究素养量表]]开发中，报告 20 题 RLS 总量表 Cronbach's $\alpha = .94$，4 个分维度 $\alpha$ 介于 $.83 \sim .90$，矫正题总相关介于 $.48 \sim .72$。
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022, Ch. 11)]] — 详述量化调查与[[Scale Development|量表编制]]中[[Internal Consistency|内部一致性]] Cronbach's $\alpha$ 的评估基准与题项净化规程。
