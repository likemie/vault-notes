---
title: Quasi-Experimental Designs
aliases:
  - 准实验设计
  - quasi-experimental design
  - QED
  - counterfactual viability
  - counterfactual strength
  - 反事实可行性
summary: "在无法实现随机分配的真实教育情境中通过非等对控制组、时间序列或断点规则构建反事实比较的量化研究设计，对应ESSA中等证据与WWC有保留达标标准。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 48
method_related_level: 5
method_related_stars: "⭐⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quasi-experimental-design
  - method/quantitative
  - evidence-based-education
  - causal-inference
  - counterfactual
related_concepts:
  - "[[Independent Variable]]"
  - "[[Hypothesis]]"
  - "[[Evidence-Based Education]]"
  - "[[Effect Size]]"
  - "[[Variable]]"
  - "[[Pre-test and Post-test]]"
  - "[[Counterfactual]]"
  - "[[Causality]]"
  - "[[Epistemology]]"
  - "[[Postpositivism]]"
  - "[[Pragmatic Paradigm]]"
  - "[[Ecological Validity]]"
  - "[[Intelligent Tutoring Systems]]"
  - "[[Implementation Fidelity]]"
  - "[[Academic Achievement]]"
  - "[[Attrition]]"
  - "[[Interaction Effect]]"
  - "[[Falsification]]"
  - "[[Heterogeneity]]"
  - "[[Order Effects]]"
  - "[[Evaluator Independence]]"
  - "[[Fade-out Effect]]"
  - "[[Logic Model]]"
  - "[[Growth]]"
  - "[[Bildung]]"
  - "[[Threats to External Validity]]"
related_theories:
  - "[[Campbellian Validity Framework]]"
related_methods:
  - "[[Random Assignment]]"
  - "[[Time Series Design]]"
  - "[[Regression Discontinuity Design]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Baseline Standardized Mean Difference]]"
  - "[[Analysis of Covariance]]"
  - "[[Experimental Research]]"
  - "[[Meta-analysis]]"
  - "[[Single-Case Design]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Single-Subject Design]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Top Institute for Evidence-Based Education Research]]"
  - "[[What Works Clearinghouse]]"
  - "[[Gaokao]]"
  - "[[Parliamentary Office of Science and Technology]]"
  - "[[ESSA 2015 Evidence Standards]]"
  - "[[Best Evidence Encyclopedia]]"
  - "[[Blueprints for Healthy Youth Development]]"
  - "[[National Dropout Prevention Center]]"
  - "[[Home Visiting Evidence of Effectiveness]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Ross_Morrison_2021_ROE]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Hitchcock_2015_JBE]]"
confidence: high
status: active
created: 2026-05-23
updated: 2026-08-21
---

# Quasi-Experimental Designs

---

## 定义

> [!def] 方法定义
> **准实验设计（Quasi-Experimental Designs, QED）** 是指在无法实施完全[[Random Assignment|随机分配]]（Random Assignment）的真实教育与社会情境中，通过选用非等对自然组别（Non-equivalent Groups）、构建间断时间序列（[[Time Series Design|interrupted time series]]）或设定断点赋值规则（[[Regression Discontinuity Design|regression discontinuity]]），系统操纵[[Independent Variable|自变量]]以检验因果[[Hypothesis|假设]]的量化实验设计方法([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, pp. 317–318]])。
>
> 在当代[[Evidence-Based Education|循证教育]]体系中，QED 构成了连接完全[[Randomised Controlled Trials|随机对照试验]]（RCT）与纯观察性研究的关键方法桥梁；在 2015 年《每个学生都成功法案》（ESSA）中对应**中等证据（Moderate Evidence / [[Top Institute for Evidence-Based Education Research|TIER]] 2）**法定层级，在[[What Works Clearinghouse|WWC]] 中对应**有保留达标（Meets Standards With Reservations）**标准([[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021, p. 109]]; [[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, pp. 8–10]])。

> [!method-scope] 方法范围
> - **研究对象** 嵌入在自然班级、完整学校或行政行政区划中的具名教育干预方案、教学模式与政策改革。
> - **问题类型** 因果效应估计（Causal Effect Estimation）、政策试点成效评估、比较有效性研究（Comparative Effectiveness）。
> - **分析单位** 学生个体、自然班级、学校集群或时间观测点。
> - **输出形式** 调整后[[Effect Size|效应量]]（Adjusted Effect Size）、双重差分（DID）估计值、基线等值性检验参数、间断斜率变化统计量。

> [!citation-card]- 关键定义
> 准实验设计涉及在无法进行随机分配的情境中对自[[Variable|变量]]进行操纵。虽然缺乏随机化带来的理论等价性保证，但通过严密的控制组选择、[[Pre-test and Post-test|前测]]基线调整与替代解释排除，准实验能够建立高度可信的因果证据。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, pp. 317–320)]]
>
> *Quasi-experimental designs encompass situations where the researcher can manipulate the independent variable but cannot randomly assign participants to groups. Establishing [[Counterfactual]] viability through robust pretesting and [[Baseline Standardized Mean Difference|Baseline Equivalence]] is the cornerstone of [[Causality|causal inference]] in quasi-experiments.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **认识论取向** 秉承[[Postpositivism|后实证主义]]与[[Pragmatic Paradigm|实用主义]]哲学取向，承认社会与学校系统具有开放性与情境嵌套性，在坚持[[Causality|因果推断]]逻辑的同时，以妥协性控制技术换取更高的[[Ecological Validity|生态效度]]（Ecological Validity）。
> - **因果识别定位** 采用[[Counterfactual|反事实]]潜在结果逻辑，但因果识别依赖于**条件独立性[[Hypothesis|假设]]（Conditional Independence Assumption）**——即假定在控制了基线[[Pre-test and Post-test|前测]]和关键可观察协[[Variable|变量]]后，组别分配与潜在结果无关。
> - **与 [[Randomised Controlled Trials|RCT]] 的互补关系** 当出于伦理考量（如不能剥夺弱势学生的必要辅导）、行政限制（学校拒绝打破现有班级建制）或政治可行性而无法实施 RCT 时，QED 提供唯一合法的因果证据替代路径([[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021, p. 109]])。

> [!method-stack] 方法层级
> - **设计形态** 非等对控制组前后测设计、[[Time Series Design|间断时间序列设计]]（[[Intelligent Tutoring Systems|ITS]]）、[[Regression Discontinuity Design|断点回归设计]]（RDD）、轮换/对等材料设计。
> - **数据采集** 标准化基线前测、多时间点追踪观测、过程[[Implementation Fidelity|实施忠实度]]记录、终结性后测。
> - **统计控制工具** 倾向得分匹配（PSM）、双重差分模型（DID）、[[Analysis of Covariance|协方差分析]]（ANCOVA）、多层线性模型（HLM）。

---

## 研究程序

> [!proc] 准[[Experimental Research|实验研究]]标准实施六步规程
> 1. **选择非等对比较组** 依据地理、学业背景与人口学特征，匹配选择最接近干预组的自然对照学校或班级。
> 2. **实施全面基线测量** 采集详尽的[[Pre-test and Post-test|前测]][[Academic Achievement|学业成绩]]与背景协[[Variable|变量]]，严密检验两组基线等值性（[[Baseline Standardized Mean Difference|Baseline Equivalence]]）。
> 3. **常态化现场干预实施** 干预组落实新教学方案，对照组维持**常规照常教学（Business-As-Usual, BAU）**，同步监控[[Implementation Fidelity|实施忠实度]]。
> 4. **终结性后测数据采集** 采用完全相同的标准化工具进行干预后评估，排查[[Attrition|差异流失]]（Differential Attrition）。
> 5. **构建统计纠偏模型** 运用双重差分法（DID）或 [[Analysis of Covariance|ANCOVA]] 剥离基线初始差异与自然时间趋势。
> 6. **开展替代解释敏感性分析** 针对历史事件、测验敏感化及选择-成熟[[Interaction Effect|交互作用]]进行[[Falsification|证伪]]检验。

---

### 准实验五大经典亚型

> [!framework-table] 准实验五大经典设计亚型对比（基于 Cohen et al., 2011, Ch. 16）
> | 设计亚型 | 经典符号模型 | 核心机制与控制优势 | 主要效度威胁与防范 | 典型应用情境 |
> |:---|:---:|:---|:---|:---|
> | **非等对控制组前后测设计<br>(Non-equivalent Control Group)** | $\frac{O_1 \quad X \quad O_2}{O_3 \quad\quad\quad O_4}$ | 教育中最广泛使用；通过前测 $O_1, O_3$ 建立基线，控制历史与成熟主效应 | 威胁：**选择-成熟交互（Selection $\times$ Maturation）**；防范：协变量调整与倾向匹配 | 班级或学校整体采纳新课程的教学对比 |
> | **间断时间序列设计<br>(Interrupted Time Series, ITS)** | $O_1 O_2 O_3 \ X \ O_4 O_5 O_6$ | 干预前后多时间点连续观测，通过前测趋势线外推建立动态[[Counterfactual\|反事实]] | 威胁：与干预同时发生的历史事件；防范：引入非等对对照时间序列 | 区域性中[[Gaokao\|高考]]改革、全校行为管理系统实施 |
> | **断点回归设计<br>(Regression Discontinuity, RDD)** | $\frac{C \quad X \quad O_1}{C \quad\quad\quad O_2}$ | 依据连续变量阈值（Cut-off）分组，断点局域近似[[Random Assignment\|随机分配]]（因果效力最高） | 威胁：阈值操纵（Manipulation）；防范：断点密度检验与带宽敏感性分析 | 依据成绩达线入选的资优生项目或补救辅导 |
> | **轮换对等设计<br>(Counterbalanced Design)** | $\frac{X_A O_1 X_B O_2}{X_B O_3 X_A O_4}$ | 两组交叉接受不同干预，所有被试兼任自身对照，控制组间不可测[[Heterogeneity\|异质性]] | 威胁：**处理滞留污染（[[Order Effects\|carry-over effect]]）**；防范：设置充足的清洗期（Washout Period） | 两种短期互补教学策略或数字软件轮换测试 |
> | **仅后测非等对组设计<br>(Posttest-Only Non-equivalent)** | $\frac{X \quad O_1}{\quad\quad O_2}$ | 无法获取前测时的妥协设计；依赖事后统计匹配尝试控制已知背景变量 | 威胁：严重的初始选择偏倚；属于弱因果设计 | 突发教育事件评估或历史档案回溯研究 |

---

### 统计模型与基线等值性规范

> [!formula-step] 双重差分模型（DID）与 [[What Works Clearinghouse|WWC]] 基线等值分级判定
> 
> 1. **双重差分因果效应估计模型（Difference-in-Differences）**
>    $$Y_{it} = \beta_0 + \beta_1 \cdot \text{Treat}_i + \beta_2 \cdot \text{[[Parliamentary Office of Science and Technology|POST]]}_t + \mathbf{\delta} \cdot (\text{Treat}_i \times \text{Post}_t) + \mathbf{\gamma}' \mathbf{X}_{it} + \varepsilon_{it}$$
>    - **$\delta$** 核心因果效应参数（净处理效应），代表干预组在干预前后的变化量减去控制组的变化量；
>    - **$\mathbf{X}_{it}$** 控制的可观察协变量向量（如家庭经济背景、先前基线成绩）。
>
> 2. **WWC 对 QED 的基线等值性（Baseline Equivalence）三级判定准则**
>    - **基线差异 $\le 0.05\text{ SD}$** 判定为基线完全等价，统计模型无需额外控制即满足“有保留达标”；
>    - **$0.05\text{ SD} < \text{基线差异} \le 0.25\text{ SD}$** 判定为中度失衡，**必须**在回归模型中纳入前测协变量进行统计调整；
>    - **基线差异 $> 0.25\text{ SD}$** 判定为严重不等价，直接裁定为“未达标（Does Not Meet Standards）”，否定其[[Causality|因果推断]]资格([[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, p. 8]])。

---

## 政策与清算体系中的审查标准

> [!framework-table] 循证清算中心对 QED 的准入门槛与评级待遇对比（基于 Wadhwa et al., 2024）
> | 清算中心 / 政策法规 | 对 QED 因果设计的描述强度 | 允许获得的最高评级待遇 | 关键限制条件与特殊要求 |
> |:---|:---:|:---|:---|
> | **[[What Works Clearinghouse\|WWC]] (美国联邦)** | 2 级 (明确规程) | **Meets Standards With Reservations**<br>(封顶于二等，不得作为单项一等证据) | 必须满足严苛的基线等值性要求（$\le 0.25\text{ SD}$）及整体/差异流失模型。 |
> | **[[ESSA 2015 Evidence Standards\|ESSA 2015]] (联邦立法)** | 法定分级 | **Tier 2 (Moderate Evidence)**<br>(中等证据法定上限) | 要求具备良好的统计控制与广泛代表性，作为学区申请联邦资助的合法依据。 |
> | **[[Best Evidence Encyclopedia\|BEE]] (JHU/Slavin)** | 1 级 ([[Meta-analysis\|元分析]]纳入) | **Moderate / Strong** (需与 [[Randomised Controlled Trials\|RCT]] 结合) | 允许高质量 QED 纳入元分析；最高 Strong 证据允许“1 项大型多中心 RCT + 1 项高质量 QED”组合。 |
> | **[[Blueprints for Healthy Youth Development\|Blueprints]]** | 3 级 (严苛规程) | **Promising** (封顶于二等) | 排除单独 QED 参评 Model / Model Plus 顶级认证；强制要求[[Evaluator Independence\|独立评估者]]报告与[[Fade-out Effect\|持续效果]]。 |
> | **[[National Dropout Prevention Center\|NDPC]]** | 1 级 (宽松包容) | **Strong Evidence** (允许 QED 获评最高级) | 准入门槛包容，仅要求存在显著正向 QED 证据且方案在学校现场实际运行满 3 年。 |

> [!abstract] [[Counterfactual|反事实]]可行性与比较组强度（Counterfactual Viability）
> [[Argument_Ross_Morrison_2021_ROE|Ross & Morrison (2021, p. 112)]] 指出，QED 的有效性高度依赖于反事实可行性（Counterfactual Viability）：
> - **比较条件的真实强度** 对照组若为“低质量、低强度或缺乏支持的弱条件”，干预容易呈现虚大[[Effect Size|效应量]]；若对照组为“成熟优质的常规教学”，效应量虽小但代表真实的政策净附加值。
> - **透明报告对照组生态** 证据审查不仅要审查干预组，更必须详尽报告对照组的教学时间、支持资源与课程[[Logic Model|逻辑模型]]，否则无法在真实学校间迁移。

---

## 适用场景

> [!fit-grid] 适用判断
> - **适合使用** 自然班级和完整学校建制不可随意打散拆分时；政策试点推广前的阶段性因果检验；评估既有历史性教育改革方案；弱势群体补偿性项目（伦理上不允许设立无支持对照组）。
> - **谨慎使用** 候选对照组与干预组在学区财政、生源背景上存在显著系统鸿沟时；[[Attrition|样本流失]]率极高且无法追踪流失原因时。
> - **不适合使用** 完全缺乏基线[[Pre-test and Post-test|前测]]数据、且无法通过历史档案构建可信对照的单组事后研究。

---

## 局限性

> [!method-limits] 效度威胁、偏误来源与误用风险
> - **选择-成熟交互威胁（Selection-Maturation Interaction）** 即使基线分数完全一致，来自高社会经济地位（SES）学校的对照组学生其自然[[Growth|成长]]斜率可能远快于薄弱校干预组，导致因果估计发生系统偏差。
> - **不可测混杂与遗漏[[Variable|变量]]偏倚（Omitted Variable Bias）** 倾向得分匹配只能平衡已测量协变量，无法控制动机、家庭[[Bildung|教养]]风格等不可测潜变量。
> - **均值回归现象（Regression to the Mean）** 当依据极端低分挑选干预组时，[[Pre-test and Post-test|后测]]分数的提高可能仅仅是统计回归假象，而非干预真实功效。
> - **实践维度的信息遮蔽** QED 同 [[Randomised Controlled Trials|RCT]] 一样，若仅报告平均[[Effect Size|效应量]]，会系统性遗漏学校采纳最急需的**实施成本**、**用户满意度**与**本地适配指南**([[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021, pp. 120–122]])。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Randomised Controlled Trials]] | 量化方法 | 真实实验母方法，QED 在无法[[Random Assignment\|随机化]]时的主要替代与对照基准。 |
> | [[Campbellian Validity Framework]] | 核心理论 | 提供 QED 内[[Threats to External Validity\|外部效度威胁]]分类体系与[[Causality\|因果推断]]逻辑框架。 |
> | [[Causality]] | 核心概念 | QED 的[[Epistemology\|认识论]]归宿，通过[[Counterfactual\|反事实]]控制建立概率性因果关系。 |
> | [[Single-Case Design]] | 替代方法 | 针对单一个案通过密集重复测量建立因果证据的非组间替代设计。 |
> | [[ESSA 2015 Evidence Standards]] | 政策依据 | 确立 QED 对应 [[Top Institute for Evidence-Based Education Research\|TIER]] 2 Moderate Evidence 的联邦法定资助地位。 |
> | [[What Works Clearinghouse]] | 评价机构 | 制定了最具代表性的 QED 基线等值性与[[Attrition\|流失]]纠偏审查技术规程。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011)]] — 体系化梳理准实验五大经典设计（非等对控制组、时间序列、[[Regression Discontinuity Design|断点回归]]、轮换对等），详析选择-成熟交互与均值回归等效度威胁(Ch. 16, pp. 317–324)。
> - [[Argument_Wadhwa_2024_RER|Wadhwa et al. (2024)]] — 全景比较 12 所清算中心对 QED 的因果审查规程（0–3 级[[Coding in Qualitative Research|编码]]），揭示 [[What Works Clearinghouse|WWC]]/[[Home Visiting Evidence of Effectiveness|HomVEE]] 的 0.05–0.25 SD 基线等值模型及 QED 在最高证据层级中的制度性分歧(pp. 8–11)。
> - [[Argument_Ross_Morrison_2021_ROE|Ross & Morrison (2021)]] — 深入探讨 QED 在 ESSA [[Top Institute for Evidence-Based Education Research|TIER]] 2 政策证据层级中的应用，提出[[Counterfactual|反事实]]可行性（Counterfactual Viability）与对照组生态报告的必要性(pp. 109–112)。
> - [[Argument_Hitchcock_2015_JBE|Hitchcock et al. (2015)]] — 论证准实验、[[Single-Subject Design|单一被试设计]]与组间 [[Randomised Controlled Trials|RCT]] 在排除历史与成熟威胁上的同构逻辑与效度门控机制(pp. 461–464)。
