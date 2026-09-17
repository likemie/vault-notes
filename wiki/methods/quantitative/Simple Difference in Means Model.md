---
title: Simple Difference in Means Model
aliases:
  - 简单均值差异模型
  - 简单均值差
  - 均值差异模型
  - Difference in Means
  - Simple Difference in Means
summary: "RCT 与组间比较中最直观的基础统计模型，直接以处理组与对照组后测样本均值之差估计平均处理效应，虽在随机分配下期望无偏，但未控制基线变异导致残差方差大且统计功效较低。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 38
method_related_level: 4
method_related_stars: "⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/statistical
  - method/rct
  - method/causal-inference
related_concepts:
  - "[[Counterfactual]]"
  - "[[Study Population and Sample]]"
  - "[[Variable]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Researcher Degrees of Freedom]]"
  - "[[Internal Validity]]"
  - "[[Heterogeneity]]"
  - "[[Hypothesis]]"
  - "[[Attrition]]"
  - "[[Null Hypothesis]]"
  - "[[Dependent Variable]]"
  - "[[Preregistration]]"
  - "[[Statistical Analysis Plan]]"
  - "[[Causality]]"
  - "[[Model Dependency]]"
related_theories:
  - "[[Central Limit Theorem]]"
related_methods:
  - "[[Randomised Controlled Trials]]"
  - "[[Random Assignment]]"
  - "[[Pre-test and Post-test]]"
  - "[[Standard Error]]"
  - "[[Confidence Interval]]"
  - "[[Covariate Adjustment]]"
  - "[[Ordinary Least Squares]]"
  - "[[Effect Size]]"
  - "[[Sample Size Determination]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Questionnaire]]"
  - "[[Analysis of Variance]]"
  - "[[Descriptive Analysis]]"
  - "[[Effect Size Conversion]]"
  - "[[Experimental Research]]"
  - "[[Analysis of Covariance]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Education Endowment Foundation]]"
  - "[[National Pupil Database]]"
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
confidence: high
status: active
created: 2026-09-15
updated: 2026-09-17
---

# Simple Difference in Means Model

---

## 定义

> [!def] 方法定义
> **简单均值差异模型（Simple Difference in Means Model）**是[[Randomised Controlled Trials|随机对照试验]]（RCT）与两组比较实验中最直观、最基础的[[Counterfactual|反事实]]因果估计模型。在完全[[Random Assignment|随机分配]]的前提下，该模型直接以处理组（Treatment Group）[[Pre-test and Post-test|后测]]结果的样本均值减去对照组（Control Group）后测结果的样本均值，作为干预对[[Study Population and Sample|目标总体]]的平均处理效应（Average Treatment Effect, ATE）的无偏点估计。模型不纳入任何基线协[[Variable|变量]]（如学生前测成绩或家庭背景特征），完全依赖随机化机制在期望上抹平两组基线差异。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 52–53)]]

> [!method-scope] 方法范围
> - **研究对象** 经过随机分配的处理组与对照组在干预实施后的单一截面后测产出指标。
> - **问题类型** 均值差异检验与平均因果效应点估计（回答“接受干预组与未接受干预组在后测表现上平均相差多少”）。
> - **[[Unit of Analysis|分析单位]]** 学生个体、实验受试者（在整群试验中亦可为集群平均值）。
> - **输出形式** 均值差估计值 $\hat{\tau}_{\text{SDM}} = \bar{Y}_T - \bar{Y}_C$、独立样本 $t$ 检验统计量、[[Standard Error|标准误]]及[[Confidence Interval|置信区间]]。

> [!citation-card] 简单均值比较在试验审计中的效应漂移与功效缺陷（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]; Xiao et al., 2016）
> 杜伦大学学者对英国 [[Education Endowment Foundation|EEF]] 早期 17 项已完成 RCT 试验微观考分数据进行四模型平行复算时发现，简单均值差异模型因完全放弃基线前测[[Covariate Adjustment|协变量控制]]，使得残差方差完全暴露于学生个体的基线能力变异之中。在多个边缘试验中，简单均值模型的标准误显著偏大、置信区间宽泛，导致真实微弱的干预增益被淹没在抽样噪音中（表现为 $p > .05$），与引入基线协变量的回归模型产生惊人的效应漂移与显著性翻转。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 52–53)]]
>
> *“Using archived data from the [[National Pupil Database]] (NPD), Xiao et al. (2016) reanalysed 17 completed EEF trials using four alternative models: simple difference in means, [[Ordinary Least Squares]] with pre-test, multilevel linear models, and generalised estimating equations. The choice of model had profound impacts on [[Effect Size]] estimates and confidence intervals, demonstrating that simple mean comparisons without covariate adjustment suffer from substantial loss of statistical power.”*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 依托内曼-鲁宾因果模型（Neyman-Rubin Causal Model）。认为在理想[[Random Assignment|随机分配]]下，处理分配指标独立于潜在结果（$T_i \perp (Y_i(1), Y_i(0))$），两组[[Pre-test and Post-test|后测]]可观测均值之差在数学期望上严格等于总体平均因果效应。
> - **研究者角色** 极简非参数或极简参数设定，不依赖研究者对函数形式（协[[Variable|变量]]线性关系）的主观设定，具有纯粹的客观透明性，避免了通过挑选协变量操纵 $p$ 值的[[Researcher Degrees of Freedom|研究者自由度]]（Researcher Degrees of Freedom）。
> - **有效性标准** [[Internal Validity|内部效度]]完全由随机化质量保障；统计推断效度依赖[[Sample Size Determination|样本量]]与误差方差；在有限样本下易受偶然基线不平衡（Chance Imbalance）的干扰。
> - **不声称回答的问题** 不能控制有限样本下的基线随机不平衡；不能解释干预的[[Heterogeneity|异质性]]效应；无法直接校正学校和班级层面的集群相关性。

> [!contrast-table] 均值差异模型 vs [[Ordinary Least Squares|OLS]] [[Covariate Adjustment|协变量调整]] vs [[Hierarchical Linear Model|多层线性模型]]（HLM）
> | 比较维度 | 简单均值差异模型 | OLS 协变量调整模型 | 多层线性模型（HLM） |
> |---|---|---|---|
> | **协变量控制** | 完全不控制（仅后测） | 线性控制基线前测与背景特征 | 多层级控制个体与集群协变量 |
> | **残差方差** | 最大（包含全部个体基线变异） | 显著收缩（被前测吸收 50%–70%） | 结构化分解（分为层内与层间残差） |
> | **检验功效** | 较低（需更大样本量才能检出） | 显著提高（[[Standard Error\|标准误]]明显收窄） | 高（且能准确反映集群真实功效） |
> | **集群相关处理** | 无法处理（违背独立性假定） | 需外挂聚类稳健标准误（CRSE） | 模型内直接建模组间随机效应与 [[Intraclass Correlation Coefficient\|ICC]] |
> | **模型[[Hypothesis\|假设]]** | 极少（仅依赖随机化无偏性） | 线性假定、无遗漏变量、同方差 | 正态随机效应分布、层级嵌套假定 |

> [!method-stack] 方法层级
> - **研究设计** 简单[[Randomised Controlled Trials|随机对照试验]]（Individual RCT）、实验室双组实验、AB 测试。
> - **数据收集** 实验终结性标准化测验、学业考分、量表[[Questionnaire|问卷]]后测总分。
> - **分析方法** 独立双样本 $t$ 检验（Student's $t$ / Welch's $t$）、单因素无协变量[[Analysis of Variance|方差分析]]（ANOVA）、双变量哑变量 OLS 回归。
> - **辅助技术** 随机化基线平衡性检验、置换检验（Permutation Test / Fisher's Exact Test）、Bootstrap 重抽样标准误。

---

## 研究程序

> [!proc] 通用程序
> 1. **检验[[Random Assignment|随机分配]]质量与基线平衡性** 比较处理组与对照组在基线人口统计学特征上的分布，评估是否存在严重的偶然基线偏差。
> 2. **计算两组[[Pre-test and Post-test|后测]][[Descriptive Analysis|描述统计]]量** 分别计算处理组（$N_T$）与对照组（$N_C$）的[[Sample Size Determination|样本量]]、后测算术均值（$\bar{Y}_T, \bar{Y}_C$）与样本方差（$s_T^2, s_C^2$）。
> 3. **计算简单均值差点估计量** 直接两组相减计算 $\hat{\tau}_{\text{SDM}} = \bar{Y}_T - \bar{Y}_C$。
> 4. **执行[[Hypothesis|假设]]检验与推断** 检验两组方差齐性（Levene 检验）；若方差不齐采用韦尔奇 $t$ 检验（Welch's $t$），构建[[Confidence Interval|置信区间]]与确定 $p$ 值。
> 5. **换算标准化[[Effect Size|效应量]]** 结合全样本对照组标准差换算为 Cohen's $d$ 或小样本校正的 Hedges' $g$。

### 量化分析模块

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** 单期后测横截面两组数据，包含 $N_T$ 个处理组受试与 $N_C$ 个对照组受试（总样本量 $N = N_T + N_C$）。
> - **核心变量**
>   - 后测产出变量 $Y_i$：个体终结性测验成绩或行为量表得分。
>   - 处理状态哑变量 $T_i$：分配至处理组取值为 1，对照组取值为 0。
> - **诊断与检验** 正态性检验（Shapiro-Wilk）、方差齐性检验（Levene）、选择性[[Attrition|流失]]检验（Attrition Bias Check）。

> [!formula-step] 公式步骤　简单均值差异估计量与抽样方差
> $$\hat{\tau}_{\text{SDM}} = \bar{Y}_T - \bar{Y}_C = \frac{1}{N_T}\sum_{i \in T} Y_i - \frac{1}{N_C}\sum_{j \in C} Y_j$$
>
> $$\text{SE}(\hat{\tau}_{\text{SDM}}) = \sqrt{\frac{s_T^2}{N_T} + \frac{s_C^2}{N_C}}$$
>
> **这个公式在做什么** 计算处理组与对照组样本平均得分之差，并基于两组各自的样本方差计算该差异估计量的[[Standard Error|标准误]]。
>
> **符号说明**
> - $\bar{Y}_T, \bar{Y}_C$：处理组与对照组后测结果的算术平均值。
> - $N_T, N_C$：处理组与对照组的有效观测样本量。
> - $s_T^2, s_C^2$：处理组与对照组后测得分的无偏样本方差。
> - $\text{SE}(\hat{\tau}_{\text{SDM}})$：异方差稳健（韦尔奇）均值差标准误。
>
> **数学直觉** 根据大数定律与[[Central Limit Theorem|中心极限定理]]，当样本量充足时，样本均值收敛于总体期望。若随机分配成立，两组潜在结果的期望基线完全对称，后测均值差直接揭示外加干预引发的期望位移。
>
> **结果怎么读** $\hat{\tau}_{\text{SDM}} > 0$ 表明处理组表现优于对照组；$t = \hat{\tau}_{\text{SDM}} / \text{SE}$ 绝对值若大于临界值（如 $1.96$），则在 $\alpha = .05$ 水平拒绝两组无差异的[[Null Hypothesis|零假设]]。
>
> **注意事项** 若未控制高相关的基线前测，公式中的残差方差 $s^2$ 包含了受试者个体间所有的先天天赋与初始学业差异，导致 $\text{SE}$ 偏大，置信区间较宽。

> [!formula-step] 公式步骤　无协变量双变量回归等价模型
> $$Y_i = \alpha + \beta_1 T_i + \varepsilon_i$$
>
> **这个公式在做什么** 将两组均值比较转化为最简形式的一元线性回归模型。
>
> **符号说明**
> - $\alpha$：截距项，数值上恒等于对照组样本均值 $\bar{Y}_C$。
> - $\beta_1$：斜率项，数值上恒等于均值差估计量 $\hat{\tau}_{\text{SDM}} = \bar{Y}_T - \bar{Y}_C$。
> - $\varepsilon_i$：个体未观测残差项。
>
> **数学直觉** 在仅包含单一分组二元虚拟变量的 [[Ordinary Least Squares|OLS]] 回归中，正交投影求解的参数解与算术均值差完全重合。这种等价性表明，简单均值比较在本质上就是零协变量的 OLS 回归。
>
> **结果怎么读** 斜率项 $\hat{\beta}_1$ 的点估计值即为干预效应量，其 $t$ 检验结果与等方差假设下的双样本学生氏 $t$ 检验完全等价。
>
> **注意事项** 该模型假定残差项 $\varepsilon_i$ 服从独立同分布；若受试者来自不同学校或班级，由于群聚误差相关性，此等价回归报告的常规标准误将被严重低估。

> [!software-impl] 软件实现
> - **推荐软件** R, Stata, Python.
> - **核心命令**
>   - R: `t.test(post_score ~ treat, data = df, var.equal = FALSE)` 或 `lm(post_score ~ treat, data = df)`
>   - Stata: `ttest post_score, by(treat) unequal` 或 `reg post_score treat`
>   - Python: `scipy.stats.ttest_ind(y_treatment, y_control, equal_var=False)`
> - **实现流程**
>   1. 数据清洗：核查组别变量取值（0/1）及后测变量缺失值；
>   2. 描述统计：输出两组均值、标准差及样本量；
>   3. 均值比较：执行双样本检验并输出均值差、标准误与 95% 置信区间；
>   4. [[Effect Size Conversion|效应量换算]]：提取对照组标准差计算标准化效应量 Hedges' $g$。
> - **报告标准** 完整呈现处理组与对照组样本量、后测原始均值与标准差、非标准化均值差、标准误、95% 置信区间以及标准化效应量。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - 样本规模极大、且由于评估成本限制未收集基线[[Pre-test and Post-test|前测]]数据的探索性大规模个体随机实验；
>   - 作为复杂多层或[[Covariate Adjustment|协变量调整]]回归分析前的基准探索与透明度对照（Benchmark）；
>   - 实验室控制环境下的极简双组行为学测试。
> - **谨慎使用**
>   - 小样本[[Randomised Controlled Trials|随机对照试验]]（极易发生偶然基线失衡，导致点估计出现实质偏倚）；
>   - 实施于学校或班级场景的整群试验（直接应用会由于忽略群聚相关性而犯严重的 I 型错误）。
> - **不适合使用**
>   - 任何非[[Random Assignment|随机分配]]的观察性研究或准[[Experimental Research|实验研究]]（两组初始存在严重选择偏误，均值差完全被混杂[[Variable|变量]]污染）；
>   - 预期效应微弱、必须依赖协变量压缩残差方差以确保统计功效的边际干预评估。

---

## 局限性

> [!method-limits] 方法局限
> - **统计功效显著受损** 由于未利用基线[[Pre-test and Post-test|前测]]成绩对后测成绩进行解释，[[Dependent Variable|因变量]]的总变异全部沦为残差方差。实证审计表明，在同等[[Effect Size|效应量]]下，简单均值差异模型通常需要比引入基线前测的模型多出 2 至 4 倍的[[Sample Size Determination|样本量]]才能达到 80% 的统计功效（Xiao et al., 2016）。
> - **偶然不平衡易致偏误** 在样本量有限的真实试验中，[[Random Assignment|随机化]]只能确保无偏的数学期望，无法保证特定样本中两组基线完全对等。若处理组偶然分入较多高学力学生，简单均值差异模型会将基线优势全盘误判为干预效果。
> - **误用风险** 在教育场景中直接将学生个体考分套入简单均值差异模型，严重忽略了班级和学校的集群效应，导致[[Confidence Interval|置信区间]]过窄、$p$ 值虚假显著。
> - **补救方式** 在试验设计阶段采集基线前测数据，并在分析阶段升级为引入基线协[[Variable|变量]]的 [[Ordinary Least Squares|OLS]] 模型（[[Analysis of Covariance|ANCOVA]]）或校正集群效应的[[Hierarchical Linear Model|多层线性模型]]（HLM）。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 模型自由度滥用防范 vs 估计精度最大化
> > 证据学界围绕试验分析是否应坚持最简均值比较的争论。
> >
> > - **极简无参派观点** 坚持认为简单均值比较完全不依赖任何线性函数形式[[Hypothesis|假设]]，彻底杜绝了分析师通过挑选协[[Variable|变量]]（$p$-hacking）操纵显著性的可能，是保持试验绝对客观公信力的防线。
> > - **现代计量与循证派抗辩** 认为在具备[[Preregistration|预注册]][[Statistical Analysis Plan|统计分析计划]]（SAP）的前提下，[[Researcher Degrees of Freedom|研究者自由度]]已被有效封死；强行采用简单均值比较会白白丢弃基线[[Pre-test and Post-test|前测]]的巨大解释力，导致大量真正有效的微弱教育创新因统计功效不足而被误杀。肖等学者（Xiao et al., 2016）利用 NPD 微观数据的复算无可辩驳地证明了这一点，推动了英国《[[Education Endowment Foundation|EEF]] 评估统计分析指南》（*Statistical Analysis Guidance for EEF Evaluations*; The EEF, 2018）对[[Covariate Adjustment|协变量调整]]的强制要求（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Randomised Controlled Trials]] | 适用场景 | 简单均值差异模型作为[[Causality\|因果推断]]基准的最核心实验设计载体。 |
> | [[Ordinary Least Squares]] | 扩展方法 | 引入基线[[Pre-test and Post-test\|前测]]与控制[[Variable\|变量]]的参数化回归模型，大幅压缩残差方差。 |
> | [[Hierarchical Linear Model]] | 替代方法 | 显式处理学校与班级嵌套结构、校正集群相关性的高级层级模型。 |
> | [[Covariate Adjustment]] | 互补技术 | 改善简单均值模型功效缺陷、控制基线偶然不平衡的核心统计技术。 |
> | [[Analysis of Covariance]] | 对应模型 | 结合[[Analysis of Variance\|方差分析]]与协变量控制的等价均值比较方法。 |
> | [[Model Dependency]] | 风险现象 | 简单均值模型与其他模型在[[Effect Size\|效应量]]估计与显著性上的差异揭示的核心方法学挑战。 |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 综述了齐·肖（ZhiMin Xiao）等杜伦大学学者利用英格兰[[National Pupil Database|国家学生数据库]]（NPD）对 17 项早期完成的 [[Education Endowment Foundation|EEF]] 试验开展的四模型并行复算，揭示出简单均值差异模型相比[[Covariate Adjustment|协变量调整]]模型和多层模型存在严重的功效损失与效应漂移，促成了英国国家级试验统计分析标准的建立。
