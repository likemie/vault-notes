---
title: Confidence Interval
aliases:
  - 置信区间
  - confidence level
  - 置信水平
  - 边际误差
  - margin of error
summary: "围绕点估计给出的区间估计形式，由置信水平和标准误共同定义，在抽样设计中用于样本量确定与精度约束，在实证研究、国际测评与宏观证据综合中用于表征估计精度、统计不确定性与防范点估计排名的虚假精确性"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 33
method_related_level: 3
method_related_stars: "💎"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/statistical
related_concepts:
  - "[[Null Hypothesis]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Sampling Error]]"
  - "[[Variable]]"
  - "[[Construct]]"
  - "[[International Large-Scale Assessments]]"
  - "[[Educational Brokerage Agency]]"
  - "[[Document]]"
  - "[[Visible Learning]]"
  - "[[Heterogeneity]]"
  - "[[Interpretive Validity]]"
related_theories: []
related_methods:
  - "[[Standard Error]]"
  - "[[Sample Size Determination]]"
  - "[[Meta-analysis]]"
  - "[[Effect Size]]"
  - "[[Meta-meta-analysis]]"
  - "[[Forest Plot]]"
  - "[[Research Synthesis]]"
  - "[[Prediction Interval]]"
  - "[[Statistical Significance]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Rasch Measurement]]"
related_instruments:
  - "[[EEF Padlock Security Rating]]"
related_persons: []
related_facts:
  - "[[PISA]]"
  - "[[Education Endowment Foundation]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
  - "[[Argument_Wecker_2016_ZfE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge]]"
  - "[[Argument_Allerup_2015_Paideia]]"
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit05]]"
confidence: high
status: active
created: 2026-05-05
updated: 2026-10-30
---

---

> [!def] Confidence Interval
> 置信区间（Confidence Interval, CI）是统计推断中围绕参数点估计值所构建的可能取值区间，用于表征估计精度的统计不确定性。一个 $100(1-\alpha)\%$（通常为 95%）的置信区间意味着：若在相同条件下从同一总体中进行无限次独立重复抽样并依照相同数学程序构建区间，理论上将有 $100(1-\alpha)\%$ 的区间包含真实的总体未明参数。置信区间由估计值、临界值（如 $Z$ 或 $t$ 分位数，由置信水平决定）与[[Standard Error|标准误]]三者共同确定。在抽样设计中，CI 作为边际误差（Margin of Error）约束所需[[Sample Size Determination|样本量]]；在实验报告与[[Meta-analysis|元分析]]中，CI 呈现[[Effect Size|效应量]]的不确定性边界，并作为防范假阳性与点估计虚假排名的核心工具。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 147–148)]]; [[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 29–30)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 测度单均值、均值差、比率、相关系数、标准化效应量（Cohen's $d$、Hedges' $g$）以及定量[[Meta-analysis|元分析]]或[[Meta-meta-analysis|二阶元分析]]的合成效应量。
> - **问题类型** 用于解答参数估计的精度范围、是否能拒绝特定[[Null Hypothesis|零假设]]值（如零效应）、抽样规划中满足目标精度所需的样本容量，以及相邻排序或亚组比较是否具有统计可区分性。
> - **[[Unit of Analysis|分析单位]]** 抽样个体、独立干预群体、原始实证研究（一阶元分析）或一阶元分析池（二阶综合）。
> - **输入数据** 点估计值（均值、比率或效应量）、样本量、抽样标准差或已知标准误。
> - **输出形式** 下限与上限构成的连续区间 $[L, U]$、边际误差半宽 $e$、点估计与区间[[Forest Plot|森林图]]（Forest Plot）。

> [!citation-card] 置信区间的变异度表征与常规策略
> 置信区间是希望确保的变异程度或变异范围。例如民调中 $\pm 3\%$ 意味着若某党获 52% 选票，实际可能在 49%–55% 之间。常规抽样策略使用 95% 置信水平和 3% 置信区间。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 147–148)]]
>
> *The confidence interval is that degree of variation or variation range that one wishes to ensure. A conventional sampling strategy will be to use a 95 per cent confidence level and a 3 per cent confidence interval.* ([[Argument_Cohen_Manion_Morrison_2011_Routledge|Cohen et al., 2011, p. 148]])

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 视单次实证观察所得的点估计为包含[[Sampling Error|抽样误差]]的随机[[Variable|变量]]，任何不报告不确定性边界的孤立点估计均具有认识论上的误导性（False Precision）；科学知识的客观性体现于估计精度的提高与对不确定性的透明呈现。
> - **研究者角色** 在研究设计阶段依据精度目标审慎权衡置信水平与区间半宽以决定抽样规模；在数据分析与[[Research Synthesis|证据综合]]阶段严格基于理论方差计算置信区间，拒绝机械的 $p < 0.05$ 二分法，并如实汇报未被伪造或低估的区间宽度。
> - **有效性标准** 覆盖概率（Coverage Probability，名义 95% CI 应真实覆盖 95% 的真值参数）、估计精度（区间越窄信息量越高）、结论稳健性。
> - **不声称回答的问题** CI 不代表未来单一个体观测值的散布范围（该范围由[[Prediction Interval|预测区间]]定义）；CI 不能消除测量工具的系统性偏差（Systematic Bias）或混杂偏倚；CI 覆盖零值并不等同于“真实效应为零”。

> [!contrast-table] 置信水平 vs 置信区间辨析（[[Argument_Cohen_Manion_Morrison_2011_Routledge|Cohen et al., 2011, pp. 147–148]]）
> | 维度 | 置信水平（Confidence Level, CL） | 置信区间（Confidence Interval, CI） |
> |---|---|---|
> | **统计学定义** | 反复抽样构建的区间覆盖真值的长期理论概率 | 围绕点估计给出的参数可能取值范围（变异区间） |
> | **典型取值** | 90%、95%、99% | $\pm 1\%$、$\pm 3\%$、$\pm 5\%$（或特定量纲下的区间数值） |
> | **在数学模型中的角色** | 决定理论分布的临界分位数（如 95% $\to Z = 1.96$） | 决定容许的边际误差半宽 $e$（$e = Z \cdot SE$） |
> | **对[[Sample Size Determination\|样本量]]的影响** | 置信水平越高（$Z$ 越大）$\to$ 所需样本量 $n$ 越大 | 置信区间越窄（$e$ 越小）$\to$ 所需样本量 $n$ 越大 |
> | **常规折中策略** | 95% 置信水平 | $\pm 3\%$ 置信区间（民调常取）或 $\pm 5\%$（常规教育调查） |

> [!contrast-table] CI 与邻近方法学[[Construct|构念]]辨析
> | 维度 | 置信区间（CI） | [[Statistical Significance\|统计显著性]]（$p$ 值） | [[Effect Size\|效应量]]（ES） | [[Standard Error\|标准误]]（SE） | [[Prediction Interval\|预测区间]]（PI） |
> |---|---|---|---|---|---|
> | **核心回答的问题** | 总体真值大概率落在何种数值范围 | 是否有足够证据拒绝[[Null Hypothesis\|零假设]] | 现象或干预的实质大小为何 | 样本估计量的抽样离散程度 | 未来单一新实证研究/个体的可能取值 |
> | **输出形式** | 连续数值区间 $[L, U]$ | 概率标量 $p$ | 点估计标量（如 $d$、$r$、$g$） | 标准离散标量 $SE$ | 宽于 CI 的外推区间 |
> | **方法学关系** | $CI = \text{点估计} \pm Z \times SE$ | 95% CI 不包含 0 等价于 $p < 0.05$ | 点估计是 CI 的中心锚点 | $SE$ 是构建 CI 的基本原材料 | $PI = \bar{y} \pm t \sqrt{SE^2 + \tau^2}$ |

---

> [!method-stack] 方法层级
> - **上位方法** 统计推断（Statistical Inference）、参数估计理论。
> - **前置步骤** [[Standard Error|标准误]]计算、抽样分布设定（渐近正态分布、$t$ 分布）、置信水平设定。
> - **变体与扩展** Student's $t$ 小样本置信区间、非参数 Bootstrap 置信区间、效应量标准化置信区间（Cohen's $d$, Hedges' $g$）、[[Inverse-Variance Weighting|逆方差加权]]联合置信区间。

> [!formula-set]- 置信区间计算与推断推导流程
> ```mermaid
> flowchart LR
>   A["步骤 1：确定置信水平与分布临界值<br/>设定 95% CL 导出 Z 或 t 分位数"] --> B["步骤 2：抽样设计阶段边际误差约束<br/>基于公式反推所需最小样本容量"]
>   B --> C["步骤 3：单项实证研究效应量区间构建<br/>点估计叠加边际误差形成置信带"]
>   C --> D["步骤 4：多级证据综合联合置信区间<br/>依据逆方差精度累加法则计算总体 CI"]
>   D --> E["步骤 5：统计可区分性与区间重叠检验<br/>防范点估计排名的虚假精确性"]
> ```

---

> [!formula-step] 步骤一　抽样设计中的样本量确定与边际误差反推
> $$e = Z_{\alpha/2} \cdot SE = Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$
> $$n = \left( \frac{Z_{\alpha/2} \cdot \sigma}{e} \right)^2$$
>
> **这个公式在做什么** 抽样设计阶段，研究者根据容许的置信水平（确定 $Z_{\alpha/2}$）与期望保证的变异范围（置信区间半宽 $e$），反推获得该精度所需的最小样本容量。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 147–148)]]
>
> **符号说明** $e$ 为容许的边际误差半宽；$Z_{\alpha/2}$ 为正态分布双侧临界分位数；$\sigma$ 为总体标准差；$n$ 为所需样本容量。
>
> **数学直觉** 样本量 $n$ 与边际误差 $e$ 的平方成反比：若要将置信区间半宽压缩一半（精度翻倍），所需样本容量必须扩大至 4 倍。
>
> > [!example]- 手算示例
> > 在 95% 置信水平（$Z = 1.96$）与最大方差假设（$p = 0.5, \sigma^2 = 0.25$）下，容许 $\pm 5\%$ 边际误差（$e = 0.05$）时：
> > $$n = \frac{1.96^2 \cdot 0.25}{0.05^2} = \frac{3.8416 \cdot 0.25}{0.0025} \approx 384$$
> > 若将精度收紧至常规民意调查所追求的 $\pm 3\%$（$e = 0.03$）：
> > $$n = \frac{1.96^2 \cdot 0.25}{0.03^2} = \frac{0.9604}{0.0009} \approx 1067$$
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 精度折中 | 容许误差 $e$ 越小，估计精度越高，但所需样本容量呈平方级骤增。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|(Cohen et al., 2011, p. 147)]] |
> > | 读法 | 水平选择 | 置信水平由 90% 升至 99% 会扩大临界值 $Z$，相同样本量下区间必然展宽。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|(Cohen et al., 2011, p. 148)]] |
> > | 注意 | 假定独立 | 公式假定总体无限且抽样完全随机独立，有限总体需引入修正系数。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|(Cohen et al., 2011, p. 147)]] |

---

> [!formula-step] 步骤二　单项实验效应量标准化置信区间构建
> $$CI_{95\%} = [d - 1.96 \cdot SE_d, \; d + 1.96 \cdot SE_d]$$
> $$SE_d = \sqrt{\frac{n_E + n_C}{n_E \cdot n_C} + \frac{d^2}{2(n_E + n_C)}}$$
>
> **这个公式在做什么** 输入独立双样本实验的处理组与对照组样本量及效应差点估计 $d$，计算效应量抽样标准误并构建 95% 置信带。[[Argument_Allerup_2015_Paideia|(Allerup, 2015, pp. 47–48)]]
>
> **符号说明** $d$ 为 Cohen's $d$ 点估计值；$n_E$ 与 $n_C$ 分别为实验组与对照组样本量；$SE_d$ 为效应量抽样标准误。
>
> **数学直觉** 围绕点估计对称展开正负 $1.96$ 倍标准误差；样本量偏小或效应量偏大均会引起第二项方差扩张，拉宽置信区间以反映抽样不确定性。
>
> > [!example]- 手算示例
> > 设实验组 $n_E = 50$，对照组 $n_C = 50$，测得效应量点估计 $d = 0.40$。代入标准误公式：
> > $$SE_d = \sqrt{\frac{50 + 50}{50 \cdot 50} + \frac{0.40^2}{2(50 + 50)}} = \sqrt{\frac{100}{2500} + \frac{0.16}{200}} = \sqrt{0.04 + 0.0008} \approx 0.202$$
> > 计算 95% 置信区间：
> > $$CI_{95\%} = [0.40 - 1.96 \times 0.202, \; 0.40 + 1.96 \times 0.202] \approx [-0.00, \; 0.80]$$
> > 区间下限跨越 0，表明在 0.05 检验水准下该效应尚未达到统计显著。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 零值检验 | 95% 置信区间若包含 0，等价于两组差异在 $p < 0.05$ 水平下不具备统计显著性。[[Argument_Allerup_2015_Paideia\|(Allerup, 2015, p. 47)]] |
> > | 读法 | 区间重叠 | 两项干预置信区间若发生实质重叠且互含点估计，在统计上无法判定优劣次序。[[Argument_Allerup_2015_Paideia\|(Allerup, 2015, p. 48)]] |
> > | 注意 | 避免点估排序 | 严禁脱离置信区间仅凭点估计排位，细微点估计差异多属随机抽样误差。[[Argument_Allerup_2015_Paideia\|(Allerup, 2015, p. 48)]] |

---

> [!formula-step] 步骤三　多级证据综合逆方差联合置信区间
> $$CI_D = [D - 1.96 \cdot SE_D, \; D + 1.96 \cdot SE_D]$$
> $$SE_D = \sqrt{\frac{1}{\sum_{j=1}^m W_j}} = \sqrt{\frac{1}{\sum_{j=1}^m \frac{1}{v_{d_j}}}}$$
>
> **这个公式在做什么** 在证据综合或元分析中，以各分项研究方差倒数（精度）为权重，累加得到合并效应量 $D$ 的总体标准误与总体置信区间。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25, 29–30)]]
>
> **符号说明** $D$ 为加权综合效应量；$W_j = 1/v_{d_j}$ 为第 $j$ 项研究的逆方差权重；$m$ 为纳入的独立研究总数；$SE_D$ 为综合效应量标准误。
>
> **数学直觉** 独立证据累加使分母上的信息量（总精度）持续放大，使得综合估计的标准误差显著小于任一单一研究，区间大幅收窄。
>
> > [!example]- 手算示例
> > 纳入两项独立研究，方差分别为 $v_1 = 0.04$（权重 $W_1 = 25$）与 $v_2 = 0.01$（权重 $W_2 = 100$）。合并标准误为：
> > $$SE_D = \sqrt{\frac{1}{25 + 100}} = \sqrt{\frac{1}{125}} \approx 0.089$$
> > 若综合效应量 $D = 0.50$，则总体 95% 置信区间为 $[0.50 - 1.96 \times 0.089, \; 0.50 + 1.96 \times 0.089] \approx [0.33, \; 0.67]$。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 精度累加 | 纳入的高质量独立研究越多，总体标准误越小，合并效应量的估计区间越狭窄。[[Argument_Wecker_2016_ZfE\|(Wecker et al., 2016, p. 25)]] |
> > | 注意 | 独立性假定 | 公式成立的充要条件为纳入研究彼此独立，文献重叠会使标准误严重低估。[[Argument_Wecker_2016_ZfE\|(Wecker et al., 2016, p. 29)]] |
> > | 注意 | 协方差膨胀 | 底层样本重复时真实方差包含正协方差项，直接套用无协方差公式导致虚假精确。[[Argument_Wecker_2016_ZfE\|(Wecker et al., 2016, p. 30)]] |

---

> [!software-impl] 软件实现与代码范例
> - **R 语言生态（`metafor`、`esc` 包）**
>   ```R
>   library(metafor)
>   # 计算标准化均值差及其 95% 置信区间
>   dat <- escalc(measure = "SMD", m1i = m1, sd1i = sd1, n1i = n1,
>                                  m2i = m2, sd2i = sd2, n2i = n2, data = mydata)
>   # 提取 95% CI 下限与上限
>   dat$ci.lb <- dat$yi - 1.96 * sqrt(dat$vi)
>   dat$ci.ub <- dat$yi + 1.96 * sqrt(dat$vi)
>   
>   # 绘制带有 95% 置信区间的森林图 (Forest Plot)
>   res <- rma(yi, vi, data = dat, method = "REML")
>   forest(res, slab = dat$study, xlab = "Standardized Mean Difference (95% CI)")
>   ```
> - **Python 生态（`scipy.stats`、`statsmodels`）**
>   ```python
>   import numpy as np
>   from scipy import stats
>   
>   def cohen_d_ci(d, n1, n2, alpha=0.05):
>       se = np.sqrt((n1 + n2)/(n1 * n2) + (d**2)/(2 * (n1 + n2)))
>       z = stats.norm.ppf(1 - alpha / 2)
>       return d - z * se, d + z * se
>   ```
> - **规范报告要求** 汇报点估计值时必须同括号报告 95% CI 下限与上限（例如：$g = 0.42, 95\% \text{ CI } [0.18, 0.66]$），严禁仅报告 $p < 0.05$ 或孤立点估计。

---

> [!method-fit] 适用判断
> - **适合使用**
>   - **抽样方案设计** 依据预期变异度与容许误差半宽计算目标样本容量。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 147–148)]]
>   - **现场[[Randomised Controlled Trials|随机对照试验]]（RCT）** 呈现干预效应的点估计与精度范围，评估试验因果效度与统计功效。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 56–57)]]
>   - **[[International Large-Scale Assessments|国际大规模学生评估]]（[[PISA]]）** 在 Rasch 尺度上呈现各国与各子群体的能力估计区间，防止因细微点估计差异而对国别排名作过度解读。[[Argument_Allerup_2015_Paideia|(Allerup, 2015, pp. 47–48)]]
>   - **[[Meta-analysis|元分析]]与二阶[[Research Synthesis|证据综合]]** 绘制[[Forest Plot|森林图]]展示各个一阶研究的估计精度分布与综合[[Effect Size|效应量]]置信区间。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 30)]]
> - **谨慎使用**
>   - **教育证据向决策者传播转化** 实践者往往难以直观理解连续区间统计意义；英美[[Educational Brokerage Agency|证据中介机构]]（如英国 [[Education Endowment Foundation|EEF]]）常在保留底层 95% CI 的同时，在前端工具包中折叠转换为“额外学习月数”并辅以[[EEF Padlock Security Rating|挂锁安全评级]]。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 56–58)]]
> - **不适合使用**
>   - [[Sample Size Determination|样本量]]极小且严重偏离正态分布、无有效大样本近似方差的数据集（应改用 Bootstrap 置信区间或精确置信区间）。
>   - 存在严重集群依赖或[[Document|文献]]重叠却未做方差校正的数据集（计算出的经典 CI 属于虚假置信区间）。

---

> [!method-limits] 方法局限
> - **点估计排名的虚假精确性诱骗** 单纯基于点估计大小对教育干预进行单一线性排序（如《[[Visible Learning|可见的学习]]》138 项排行榜），隐去了置信区间信息，误导决策者将无统计区分度的相邻排位（如 $d = 0.72$ 与 $d = 0.71$）视作实质优劣。[[Argument_Allerup_2015_Paideia|(Allerup, 2015, pp. 47–48)]]; [[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 29–30)]]
> - **现场试验置信区间过宽的信息量困境** 现场教育试验常因学校集群效应与高[[Heterogeneity|异质性]]导致估计误差偏大。对英美 141 项现场 [[Randomised Controlled Trials|RCT]] 的重析表明其 95% CI 平均宽度达 0.30 SD（干预效应均值仅 0.06 SD），被批评为区间过宽而“无法提供有效政策信息”（uninformative）。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, p. 56)]]; (Lortie-Forgues & Inglis, 2019)
> - **文献重叠与数据伪造导致的虚假狭窄区间** 当[[Meta-meta-analysis|二阶元分析]]忽视底层主要研究重复（重叠率达 90% 以上）或直接对[[Standard Error|标准误]]求简单算术平均时，协方差失效致使计算出的置信区间被人为严重缩水，形成虚假精确性。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 29–30)]]
> - **科学严谨性与行动易读性的制度张力** 全面报告置信区间构成了专业技术门槛，[[Educational Brokerage Agency|证据中介机构]]将其简化为离散月份指标时，不可避免地隐藏了区间宽度所表征的不确定性风险。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 57–58)]]

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Sample Size Determination]] | 方法/概念 | 置信区间与置信水平是抽样设计中计算样本容量的两个决定性参数。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|(Cohen et al., 2011, pp. 147–148)]] |
> | [[Standard Error]] | 方法/概念 | 标准误是构建置信区间的基本度量单元（$CI = \text{点估计} \pm Z \times SE$）。 |
> | [[Effect Size]] | 方法/概念 | 置信区间围绕效应量点估计展开，用于界定效应量的抽样波动范围。 |
> | [[Inverse-Variance Weighting]] | 方法 | 逆方差加权合成各研究精度，导出元分析合并效应量的总体置信区间。[[Argument_Wecker_2016_ZfE\|(Wecker et al., 2016, pp. 25, 30)]] |
> | [[Meta-analysis]] 与 [[Meta-meta-analysis]] | 方法 | 证据综合中[[Forest Plot\|森林图]]必须逐项标示各研究与总体的 95% CI，缺少 CI 将使证据排行榜失去[[Interpretive Validity\|解释效度]]。 |
> | [[Randomised Controlled Trials]] | 方法 | 现场试验中用于呈现干预效果的不确定性范围，是检验因果效度的核心统计指标。 |
> | [[Rasch Measurement]] | 方法 | PISA 等国际评估中依托 Rasch 误差区间避免国别排名的过度解释。[[Argument_Allerup_2015_Paideia\|(Allerup, 2015, pp. 47–48)]] |
> | [[EEF Padlock Security Rating]] | 工具 | 充当面向一线实践者传达研究效度与不确定性的直观符号，折衷专业 CI 与行动易读性。[[Argument_Edovald_Nevill_2021_ECNUROE\|(Edovald & Nevill, 2021, p. 57)]] |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011)]] — 阐释置信区间与置信水平在抽样设计中的数理逻辑，剖析 384 例天花板与民调 1067 例样本容量推导（pp. 146–148）。
> - [[Argument_Allerup_2015_Paideia|Allerup (2015)]] — 借助置信区间分析批判点估计排名的虚假精确性，对比 PISA 误差区间论证无 CI 的干预排序在统计上不可区分（pp. 47–48）。
> - [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] — 在二级元分析中推导逆方差联合置信区间公式，批判文献重叠导致虚假狭窄区间的致命统计缺陷（pp. 25, 29–30）。
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald and Nevill (2021)]] — 探讨英美 141 项现场 RCT 中置信区间过宽的争议，反思证据中介在严谨 CI 呈现与直观转化之间的张力（pp. 56–58）。
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit05|Wang & Barabási (2021)]] — 跨学术期刊论著、专利与软件三大领域展示团队规模与颠覆性关系的 95% 置信区间带，揭示小团队颠覆度与大团队引用量的稳健分化（p. 131）。
