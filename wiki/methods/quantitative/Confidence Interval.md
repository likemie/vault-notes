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
method_related_count: 34
method_related_level: 3
method_related_stars: "💎"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - confidence-interval
  - standard-error
  - statistical-inference
  - effect-size
  - research-methodology
related_concepts:
  - "[[Null Hypothesis]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Sampling Error]]"
  - "[[Variable]]"
  - "[[Construct]]"
  - "[[Reliability]]"
  - "[[International Large-Scale Assessments]]"
  - "[[Educational Brokerage Agency]]"
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
  - "[[Fixed-Effect Model]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Random Sampling]]"
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
confidence: high
status: completed
created: 2026-05-05
updated: 2026-10-29
---

---

> [!def] Confidence Interval
> 置信区间（Confidence Interval, CI）是统计推断中围绕参数点估计值所构建的可能取值区间，用于表征估计精度的统计不确定性。一个 $100(1-\alpha)\%$（通常为 95%）的置信区间意味着：若在相同条件下从同一总体中进行无限次独立重复抽样并依照相同数学程序构建区间，理论上将有 $100(1-\alpha)\%$ 的区间包含真实的总体未明参数。置信区间由估计值、临界值（如 $Z$ 或 $t$ 分位数，由置信水平决定）与[[Standard Error|标准误]]三者共同确定。在抽样设计中，CI 作为边际误差（Margin of Error）约束所需[[Sample Size Determination|样本量]]；在实验报告与[[Meta-analysis|元分析]]中，CI 呈现[[Effect Size|效应量]]的不确定性边界，并作为防范假阳性与点估计虚假排名的核心工具。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 147–148)]]; [[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 29–30)]]

> [!method-scope] 方法范围
> - **研究对象** 单均值、均值差、比率、相关系数、标准化效应量（Cohen's $d$、Hedges' $g$）以及定量[[Meta-analysis|元分析]]或[[Meta-meta-analysis|二阶元分析]]的合成效应量。
> - **问题类型** 用于解答参数估计的精度范围、是否能拒绝特定[[Null Hypothesis|零假设]]值（如零效应）、抽样规划中满足目标精度所需的样本容量，以及相邻排序或亚组比较是否具有统计可区分性。
> - **[[Unit of Analysis|分析单位]]** 抽样个体、独立干预群体、原始实证研究（一阶元分析）或一阶元分析池（二阶综合）。
> - **输出形式** 下限与上限构成的连续区间 $[L, U]$、边际误差半宽 $e$、点估计与区间[[Forest Plot|森林图]]（Forest Plot）。

> [!citation-card] 置信区间的变异度表征与常规策略
> 置信区间是希望确保的变异程度或变异范围。例如民调中 $\pm 3\%$ 意味着若某党获 52% 选票，实际可能在 49%–55% 之间。常规抽样策略使用 95% 置信水平和 3% 置信区间。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 147–148)]]
>
> *The confidence interval is that degree of variation or variation range that one wishes to ensure. A conventional sampling strategy will be to use a 95 per cent confidence level and a 3 per cent confidence interval.* ([[Argument_Cohen_Manion_Morrison_2011_Routledge|Cohen et al., 2011, p. 148]])

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 视单次实证观察所得的点估计为包含[[Sampling Error|抽样误差]]的随机[[Variable|变量]]，任何不报告不确定性边界的孤立点估计均具有认识论上的误导性（False Precision）；科学知识的客观性体现于估计精度的收敛与对不确定性的透明呈现。
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

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **输入数据** 点估计值（$\bar{x}$、$p$ 或[[Effect Size|效应量]] $d$）、样本容量（$n$）、抽样方差（$v = SE^2$）或跨研究权重（$W_j$）。
> - **核心变量** 置[[Reliability|信度]] $1-\alpha$、正态临界值 $Z_{1-\alpha/2}$ 或 Student's $t$ 分位数、边际误差半宽 $e$。
> - **推断模型** 渐近大样本正态模型、学生 $t$ 分布小样本修正模型、两级[[Fixed-Effect Model|固定效应]]跨层[[Inverse-Variance Weighting|逆方差加权]]模型。

> [!formula-set]- 置信区间计算与推断推导流程
> ```mermaid
> flowchart LR
>   A["步骤 1：确定置信水平与分布临界值<br/>设定 95% CL 导出 Z 或 t 分位数"] --> B["步骤 2：抽样设计阶段边际误差约束<br/>基于公式反推所需最小样本容量"]
>   B --> C["步骤 3：单项实证研究效应量区间构建<br/>点估计叠加边际误差形成置信带"]
>   C --> D["步骤 4：多级证据综合联合置信区间<br/>依据逆方差精度累加法则计算总体 CI"]
>   D --> E["步骤 5：统计可区分性与区间重叠检验<br/>防范点估计排名的虚假精确性"]
> ```

---

### 公式步骤一　抽样设计中的样本量确定与边际误差（Cohen et al., 2011）

> [!formula-step] 抽样[[Sample Size Determination|样本量]]反推公式
> $$e = Z_{\alpha/2} \cdot SE = Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$
> 变换得到目标精度下的所需[[Sample Size Determination|样本量]]公式：
> $$n = \left( \frac{Z_{\alpha/2} \cdot \sigma}{e} \right)^2$$
>
> **这个公式在做什么** 抽样设计阶段，研究者根据容许的置信水平（决定 $Z$）与希望确保的变异范围（置信区间半宽 $e$），反推获得该精度所需的最小样本量。
>
> **384 例天花板的数理机制** Krejcie and Morgan (1970) 广为人知的 384 例大总体样本量天花板，基于 95% 置信水平（$Z = 1.96$）、$\pm 5\%$ 置信区间（$e = 0.05$）与最大方差假设（$p = 0.5$）：
> $$n = \frac{1.96^2 \cdot 0.5 \cdot 0.5}{0.05^2} = 384.16 \approx 384$$
> 若研究者将置信区间精度收紧至常规民意调查所追求的 $\pm 3\%$（$e = 0.03$），样本量将骤增至：
> $$n = \frac{1.96^2 \cdot 0.25}{0.03^2} \approx 1067$$
> 这从数理上解释了为何民意调查普遍要求 1,000–1,500 人而非 384 人的样本量。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, pp. 146–148)]]

---

### 公式步骤二　单项研究效应量标准化置信区间

> [!formula-step] Cohen's $d$ 与 Hedges' $g$ 的 95% 置信区间
> $$CI_{95\%} = [d - 1.96 \cdot SE_d, \; d + 1.96 \cdot SE_d]$$
> 其中独立双样本实验设计的效应量[[Standard Error|标准误]]为：
> $$SE_d = \sqrt{\frac{n_E + n_C}{n_E \cdot n_C} + \frac{d^2}{2(n_E + n_C)}}$$
>
> **区间重叠法则（Overlap Rule）** 当两项干预措施的点估计分别为 $d_1 = 0.72$ 与 $d_2 = 0.71$ 时，若二者的 95% 置信区间发生重叠且互含点估计值，在统计学上无法拒绝二者无差异的[[Null Hypothesis|零假设]]，点估计的细微数值差属于[[Random Sampling|随机抽样]]噪声，不能作为干预优劣的依据。[[Argument_Allerup_2015_Paideia|(Allerup, 2015, pp. 47–48)]]

---

### 公式步骤三　两级证据综合中的联合置信区间与精度累加（Wecker et al., 2016）

> [!formula-step] 二级固定效应[[Meta-analysis|元分析]]联合置信区间公式
> 在[[Meta-meta-analysis|二级元分析]]中，宏观综合效应量 $D$ 的 95% 置信区间严格依据各一级元分析的[[Inverse-Variance Weighting|逆方差加权]]精度累加法则计算：
> $$CI_D = [D - 1.96 \cdot SE_D, \; D + 1.96 \cdot SE_D]$$
> 其中总体标准误 $SE_D$ 为：
> $$SE_D = \sqrt{v_D} = \sqrt{\frac{1}{\sum_{j=1}^m W_j}} = \sqrt{\frac{1}{\sum_{j=1}^m \frac{1}{v_{d_j}}}}$$
>
> **协方差失效与伪造置信区间机理** 公式成立的充要条件为各元分析包含的主要研究完全独立。若元分析间存在文献重叠（如网络学习中 93.3% 重叠），重叠主要研究诱发正协方差项：
> $$\text{Var}(D) = \frac{\sum W_j^2 v_{d_j} + 2 \sum_{j < k} W_j W_k \text{Cov}(d_j, d_k)}{(\sum W_j)^2} > \frac{1}{\sum W_j}$$
> 此时直接套用无协方差公式计算出的 $SE_D$ 被严重人为低估，导致构建出的 95% 置信区间虚假狭窄，产生伪造的超高精度与统计检验假阳性。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25, 29–30, 37–38)]]

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
>   - 存在严重集群依赖或文献重叠却未做方差校正的数据集（计算出的经典 CI 属于虚假置信区间）。

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
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011)]] — 系统阐释置信区间与置信水平在[[Random Sampling|概率抽样]][[Sample Size Determination|样本量]]设计中的数理逻辑，剖析 384 例天花板与民调 1067 例样本容量的置信半宽推导（Ch. 8, pp. 146–148）。
> - [[Argument_Allerup_2015_Paideia|Allerup (2015)]] — 借助置信区间分析批判点估计排名的虚假精确性，对比 [[PISA]] 误差区间论证无 CI 的干预排序在统计上不可区分（pp. 47–48）。
> - [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] — 在[[Meta-meta-analysis|二级元分析]]规范中推导跨层[[Inverse-Variance Weighting|逆方差加权]]下的联合置信区间公式，系统批判 Hattie 隐匿置信区间与文献重叠导致虚假狭窄区间的致命统计缺陷（pp. 25, 29–30）。
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald and Nevill (2021)]] — 探讨英美 141 项大规模教育现场 [[Randomised Controlled Trials|RCT]] 中置信区间过宽的争议，深入反思证据中介在技术报告严谨 CI 呈现与前端工具包直观转化之间的制度张力（pp. 56–58）。
