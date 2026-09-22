---
title: Omega-Squared
aliases:
  - 欧米茄平方
  - Omega Squared
summary: "方差分析中用于估计自变量解释总体方差比例的无偏效应量统计量，通过扣除均方误差校正样本高估偏差"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 26
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/effect-size
  - method/anova
  - method/quantitative
related_concepts:
  - "[[Independent Variable]]"
  - "[[Variable]]"
  - "[[Dependent Variable]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Causality]]"
  - "[[Paradigm]]"
  - "[[Hypothesis]]"
  - "[[Document]]"
  - "[[Effective Sample Size]]"
  - "[[Interaction Effect]]"
related_theories: []
related_methods:
  - "[[Analysis of Variance]]"
  - "[[Effect Size]]"
  - "[[Experimental Research]]"
  - "[[Questionnaire]]"
  - "[[Sample Size Determination]]"
  - "[[Statistical Significance]]"
  - "[[Factorial Design]]"
  - "[[Repeated Measures Design]]"
  - "[[Meta-analysis]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Likert Scale]]"
  - "[[Confidence Interval]]"
  - "[[Cluster Analysis]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Altrichter_2019_ZfB]]"
confidence: high
status: draft
created: 2026-09-18
updated: 2026-09-18
---

# Omega-Squared

---

## 定义

> [!def] 方法定义
> **欧米茄平方（Omega-Squared, $\omega^2$）** 是在单因素或多因素[[Analysis of Variance\|方差分析]]（Analysis of Variance, ANOVA）中用于度量分类[[Independent Variable\|自变量]]（自[[Variable\|变量]]处理或分组）解释连续[[Dependent Variable\|因变量]]总变异比例的总体[[Effect Size\|效应量]]估计量。由统计学家威廉·海斯（William L. Hays, 1963）系统提出，它通过从组间平方和中扣除由随机误差引起的变异，有效克服了传统样本决定系数 Eta-Squared（$\eta^2$）在小样本或多组设计中系统性高估总体效应的样本偏倚。[[Argument_Altrichter_2019_ZfB\|(Altrichter et al., 2019, p. 27)]]

> [!method-scope] 方法范围
> - **研究对象** 实验设计、准[[Experimental Research\|实验研究]]或[[Questionnaire\|问卷调查]]中的组间均值比较数据（方差分析模型）。
> - **问题类型** 因果效应强度估计、组间差异实际重要性评估、总体方差贡献率测度。
> - **[[Unit of Analysis\|分析单位]]** 包含分类自变量分组标签与连续因变量得分的观测个体（如学生、教师、学校）。
> - **输出形式** 介于 $0$ 到 $1$ 之间的无量纲连续比例统计量（若计算值为负则通常约定截断为 $0$），表示因变量总体方差中可归因于自变量处理的净百分比。

> [!citation-card] 效应量判定阈值与稳健估计
> 为了评估组间差异的实际效应大小，方差分析中报告了效应量 Omega-Squared（$\omega^2$），并采用事后 $t$ 检验的两两比较效应量 Cohen's $d$；判定阈值遵循统计学经典准则：$\omega^2 > 0.01$ 为弱效应，$0.06$ 为中等效应，$0.14$ 为强效应。[[Argument_Altrichter_2019_ZfB\|(Altrichter et al., 2019, p. 27)]]
>
> *Um die praktische Bedeutsamkeit der Unterschiede abzusichern, werden Effektmaße berichtet: Omega-Squared ( $\omega^2$ ) für Varianzanalysen und Cohen's d für Post-hoc-Vergleiche... $\omega^2 > 0{,}01$ wird als kleiner, $0{,}06$ als mittlerer und $0{,}14$ als großer Effekt interpretiert.*

---

## 方法定位

> [!method-position] [[Epistemology\|认识论]]与方法定位
> - **知识观** 属于频率学派参数统计与[[Causality\|因果推断]][[Paradigm\|范式]]，主张不能仅依靠依赖于[[Sample Size Determination\|样本量]]的[[Statistical Significance\|统计显著性]]检验（$p$ 值），必须通过报告对总体效应的无偏点估计来界定经验差异的实质科学价值。
> - **研究者角色** 研究者需检验[[Analysis of Variance\|方差分析]]的基本[[Hypothesis\|假设]]（正态性、方差齐性），在完全随机单因素、[[Factorial Design\|析因设计]]或[[Repeated Measures Design\|重复测量设计]]中选取对应形态的 $\omega^2$ 计算公式，并合理解释[[Effect Size\|效应量]]的理论与实践内涵。
> - **有效性标准** 统计结论效度（消除小样本正向偏倚）、跨研究可比性与[[Meta-analysis\|元分析]]效应量汇总适切性。
> - **不声称回答的问题** $\omega^2$ 仅度量方差解释比例与关联强度，其数值高低本身不能证明[[Independent Variable\|自变量]]与[[Dependent Variable\|因变量]]之间必然存在因果关系（需依赖严格的研究设计排查混杂偏误）。

> [!method-stack] 方法层级
> - **研究设计** [[Randomised Controlled Trials\|随机对照试验]]（RCT）、准实验组间比较、横截面分类调查设计。
> - **数据收集** 标准化测验成绩、[[Likert Scale\|李克特量表]][[Questionnaire\|问卷调查]]、行为时间记录。
> - **分析方法** 单因素方差分析（One-way ANOVA）、多因素方差分析（Factorial ANOVA）。
> - **辅助技术** 
>   - Levene 方差齐性检验
>   - 事后多重比较（Post-hoc tests with Cohen's $d$ / Hedges' $g$）
>   - 效应量[[Confidence Interval\|置信区间]] Bootstrap 自助抽样法

---

## 统计原理与数学推导

> [!formula-step] 公式推导一　单因素[[Analysis of Variance\|方差分析]]中的 $\omega^2$ 解析式
> 在经典的单因素完全随机方差分析中，样本平方和分解为：
> $$SS_{\text{total}} = SS_{\text{between}} + SS_{\text{within}}$$
> 样本统计量 $\eta^2 = \frac{SS_{\text{between}}}{SS_{\text{total}}}$ 直接计算样本变异比值，但数学期望存在向上偏倚：$E(\eta^2) > \omega_{\text{pop}}^2$。
> 
> 总体方差分量可表示为：
> $$\omega^2 = \frac{\sigma_{\alpha}^2}{\sigma_{\alpha}^2 + \sigma_{\epsilon}^2}$$
> 利用均方期望（$E(MS_{\text{between}}) = \sigma_{\epsilon}^2 + n'\sigma_{\alpha}^2$ 与 $E(MS_{\text{within}}) = \sigma_{\epsilon}^2$），代换可得无偏点估计公式：
> $$\omega^2 = \frac{SS_{\text{between}} - (k - 1)MS_{\text{within}}}{SS_{\text{total}} + MS_{\text{within}}}$$
> 其中：
> - $SS_{\text{between}}$ 为组间平方和，$df_{\text{between}} = k - 1$；
> - $MS_{\text{within}}$ 为组内均方（均方误差 $MS_{\text{error}}$）；
> - $SS_{\text{total}}$ 为总平方和；
> - $k$ 为[[Independent Variable\|自变量]]水平数（组别数）。

> [!formula-step] 公式推导二　基于 $F$ 检验统计量与自由度的等价表达
> 在发表[[Document\|文献]]中，若仅报告了方差分析检验统计量 $F$ 值与自由度，可直接通过下式换算 $\omega^2$：
> $$\omega^2 = \frac{df_{\text{between}}(F - 1)}{df_{\text{between}}(F - 1) + N}$$
> 其中 $N$ 为全样本总[[Effective Sample Size\|有效样本量]]。
> 当 $F < 1$ 时，分子为负数，代数计算结果为负值，在实证报告中通常截断记录为 $\omega^2 = .00$。

> [!formula-step] 公式推导三　偏欧米茄平方（Partial Omega-Squared, $\omega_p^2$）
> 在多因素析因方差分析设计中，为了控制其他主效应与[[Interaction Effect\|交互效应]]的变异干扰，通常计算偏欧米茄平方：
> $$\omega_p^2 = \frac{SS_{\text{effect}} - df_{\text{effect}} \cdot MS_{\text{error}}}{SS_{\text{effect}} + (N - df_{\text{effect}})MS_{\text{error}}} = \frac{df_{\text{effect}}(F - 1)}{df_{\text{effect}}(F - 1) + N}$$

---

## 启发式规则与决策标准

> [!method-heuristics] [[Effect Size\|效应量]]大小判定标准与指标选取规则
> - **科恩基准经验阈值（Jacob Cohen, 1988）**
>   - $\omega^2 < 0.01$：微弱或可忽略效应（Trivial / Negligible）；
>   - $0.01 \le \omega^2 < 0.06$：小效应（Small Effect）；
>   - $0.06 \le \omega^2 < 0.14$：中等效应（Medium Effect）；
>   - $\omega^2 \ge 0.14$：大效应（Large Effect）。
> - **与 $\eta^2$ 及偏 $\eta_p^2$ 的选用规则**
>   - 当[[Sample Size Determination\|样本量]]较大（$N > 500$）时，$\omega^2$ 与 $\eta^2$ 差异微小；
>   - 当样本量较小（$N < 100$）或组别较多（$k \ge 4$）时，$\eta^2$ 会严重高估效应（高估幅度可达 $30\% \sim 50\%$），必须强制报告 $\omega^2$ 或 Epsilon-Squared（$\epsilon^2$）；
>   - 跨研究做[[Meta-analysis\|元分析]]汇总时，推荐使用 $\omega^2$，因其点估计具备更优的无偏性。

---

## 软件实现与代码规程

> [!software-code]- R 语言与 Python 统计计算实现规程
> ```R
> # R 语言实现：基于 effectsize 包直接提取方差分析模型对象的 omega_squared
> library(effectsize)
> 
> # 拟合单因素方差分析模型
> fit <- aov(work_time ~ cluster_group, data = principal_data)
> 
> # 提取无偏效应量 Omega-Squared 及其置信区间
> omega_res <- omega_squared(fit, ci = 0.95, alternative = "two.sided")
> print(omega_res)
> # 输出: Omega2 | 95% CI [LL, UL]
> ```
> 
> ```python
> # Python 实现：基于 pingouin 统计库计算方差分析与 omega-squared
> import pingouin as pg
> 
> aov = pg.anova(data=principal_data, dv='work_time', between='cluster_group', detailed=True)
> # pingouin 自动输出 np2 (partial eta-squared) 与 omega_squared
> print(aov'Source', 'SS', 'DF', 'MS', 'F', 'p-unc', 'np2')
> ```

---

## 典型案例

> [!ref-table]- 教育治理实证研究中的 $\omega^2$ 应用标本
>
> | 研究[[Document\|文献]] | 分析模型与[[Variable\|变量]] | $F$ 检验与样本量 | $\omega^2$ 统计结果 | 效应等级与实证解释 |
> |---|---|---|---|---|
> | [[Argument_Altrichter_2019_ZfB\|Altrichter et al. (2019, p. 29, 教学活动)]] | 校长治理态度聚类（3组）对**校本教学发展活动**的影响 | $F(2, 301) = 7.99, p < .001, N = 304$ | $\omega^2 = 0.04$ | 小到中等效应；证实循证治理态度能实质解释约 4% 的教学发展活动变异。 |
> | [[Argument_Altrichter_2019_ZfB\|Altrichter et al. (2019, p. 29, 协同发展)]] | 校长治理态度聚类（3组）对**教师协同发展能力**的影响 | $F(2, 291) = 9.66, p < .001, N = 294$ | $\omega^2 = 0.06$ | **标准中等效应**；证实治理理念差异对学校教研共同体建设具有稳健的塑造作用。 |
> | [[Argument_Altrichter_2019_ZfB\|Altrichter et al. (2019, p. 30)]] | 校长治理态度聚类（3组）对**课堂直接授课工时占比**的影响 | $F(2, 299) = 10.51, p < .001, N = 302$ | $\omega^2 = 0.06$ | **标准中等效应**；证实治理态度可解释校长直接授课比例 6% 的总体方差变异，驱动其向管理角色转型。 |

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Analysis of Variance]] | Method | 计算 $\omega^2$ 的底层统计模型与变异来源分解框架。 |
> | [[Effect Size]] | Method | $\omega^2$ 所属的宏观统计方法学上位范畴。 |
> | Eta-Squared | Method | $\omega^2$ 所旨在修正并替代的样本有偏对应统计量。 |
> | [[Cluster Analysis]] | Method | 在聚类分组后检验簇间分离度与下游[[Variable\|变量]]差异时的标准效应量配套工具。 |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research\|相关研究]]索引
> - [[Argument_Altrichter_2019_ZfB\|Altrichter et al. (2019)]] — 在单因素[[Analysis of Variance\|方差分析]]中报告 $\omega^2$ 作为无偏[[Effect Size\|效应量]]，检验三类治理态度聚类校长在学校发展活动与日常工时分配上的组间差异。
