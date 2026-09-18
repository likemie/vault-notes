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
method_related_count: 76
method_related_level: 6
method_related_stars: "⭐⭐⭐⭐⭐⭐"
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
  - "[[Educational Evidence Clearinghouses]]"
  - "[[Unit of Analysis]]"
  - "[[Counterfactual]]"
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Epistemology]]"
  - "[[Postpositivism]]"
  - "[[Pragmatic Paradigm]]"
  - "[[Ecological Validity]]"
  - "[[Tracking]]"
  - "[[Scientifically Based Research]]"
  - "[[Evidence Standards]]"
  - "[[Intelligent Tutoring Systems]]"
  - "[[Academic Achievement]]"
  - "[[Business as Usual]]"
  - "[[Implementation Fidelity]]"
  - "[[Attrition]]"
  - "[[Interaction Effect]]"
  - "[[Falsification]]"
  - "[[Heterogeneity]]"
  - "[[Order Effects]]"
  - "[[Dependent Variable]]"
  - "[[Evaluator Independence]]"
  - "[[Fade-out Effect]]"
  - "[[Paradigm]]"
  - "[[Champ]]"
  - "[[School Choice]]"
  - "[[Preregistration]]"
  - "[[Logic Model]]"
  - "[[Growth]]"
  - "[[Bildung]]"
  - "[[Internal Validity]]"
  - "[[External Validity]]"
  - "[[Construct Validity]]"
related_theories:
  - "[[Campbellian Validity Framework]]"
related_methods:
  - "[[Random Assignment]]"
  - "[[Time Series Design]]"
  - "[[Regression Discontinuity Design]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Correlational Research]]"
  - "[[Effect Size]]"
  - "[[Difference-in-Differences]]"
  - "[[Pre-test and Post-test]]"
  - "[[Baseline Standardized Mean Difference]]"
  - "[[Propensity Score Matching]]"
  - "[[Matching]]"
  - "[[Analysis of Covariance]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Experimental Research]]"
  - "[[Standard Error]]"
  - "[[Meta-analysis]]"
  - "[[Qualitative Research]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Single-Subject Design]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Every Student Succeeds Act]]"
  - "[[What Works Clearinghouse]]"
  - "[[No Child Left Behind Act 2001]]"
  - "[[Gaokao]]"
  - "[[Best Evidence Encyclopedia]]"
  - "[[Blueprints for Healthy Youth Development]]"
  - "[[National Dropout Prevention Center]]"
  - "[[Title I of the Elementary and Secondary Education Act]]"
  - "[[Evidence for ESSA]]"
  - "[[Education Endowment Foundation]]"
  - "[[Education Resources Information Center]]"
  - "[[Researching School Choices]]"
  - "[[Home Visiting Evidence of Effectiveness]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Ross_Morrison_2021_ECNUROE]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Ginsberg_2024_EP]]"
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
  - "[[Argument_Hitchcock_2015_JBE]]"
confidence: high
status: active
created: 2026-05-23
updated: 2026-09-18
---

# Quasi-Experimental Designs

---

## 定义

> [!def] 方法定义
> **准实验设计（Quasi-Experimental Designs, QED）** 是指在无法实施完全[[Random Assignment|随机分配]]（Random Assignment）的真实教育与社会情境中，通过选用非等对自然组别（Non-equivalent Groups）、构建间断时间序列（[[Time Series Design|interrupted time series]]）或设定断点赋值规则（[[Regression Discontinuity Design|regression discontinuity]]），系统操纵[[Independent Variable|自变量]]以检验因果[[Hypothesis|假设]]的量化实验设计方法（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, pp. 317–318]]）。
>
> 在当代[[Evidence-Based Education|循证教育]]体系中，QED 构成了连接完全[[Randomised Controlled Trials|随机对照试验]]（Randomised Controlled Trial, RCT）与纯[[Correlational Research|相关性研究]]的关键方法桥梁；在 2015 年《每个学生都成功法案》（[[Every Student Succeeds Act]], ESSA）中对应**中等证据（Moderate Evidence / Tier II）**法定层级，在[[What Works Clearinghouse|有效干预清算中心]]（What Works [[Educational Evidence Clearinghouses|Clearinghouse]], WWC）中对应**有保留达标（Meets Standards With Reservations）**标准（[[Argument_Ross_Morrison_2021_ECNUROE|Ross & Morrison, 2021, p. 109]]；[[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, pp. 8–10]]；[[Argument_Ginsberg_2024_EP|Ginsberg et al., 2024, pp. 162–163]]）。

> [!method-scope] 方法范围
> - **研究对象** 嵌入在自然班级、完整学校或行政区划中的具名教育干预方案、教学模式、课程改革与教育政策。
> - **问题类型** 因果效应估计（Causal Effect Estimation）、政策试点成效评估、比较有效性研究（Comparative Effectiveness）。
> - **[[Unit of Analysis|分析单位]]** 学生个体、自然班级、学校集群、学区或时间观测点。
> - **输出形式** 调整后[[Effect Size|效应量]]（Adjusted Effect Size）、[[Difference-in-Differences|双重差分法]]（Difference-in-Differences, DID）因果估计值、基线等值性检验参数、断点局域平均处理效应（Local Average Treatment Effect, LATE）、时间序列间断斜率变化统计量。

> [!citation-card] 科恩等论准实验设计与[[Counterfactual|反事实]]可行性
> 准实验设计涉及在无法进行随机分配的情境中对自[[Variable|变量]]进行操纵。虽然缺乏随机化带来的理论等价性保证，但通过严密的控制组选择、[[Pre-test and Post-test|前测]]基线调整与替代解释排除，准实验能够建立高度可信的因果证据。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, pp. 317–320)]]
>
> *Quasi-experimental designs encompass situations where the researcher can manipulate the independent variable but cannot randomly assign participants to groups. Establishing counterfactual viability through robust pretesting and [[Baseline Standardized Mean Difference|Baseline Equivalence]] is the cornerstone of [[Causality|causal inference]] in quasi-experiments.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **认识论取向** 秉承[[Postpositivism|后实证主义]]与[[Pragmatic Paradigm|实用主义]]哲学取向，承认学校系统具有开放性、社会关系复杂性与情境嵌套性，在坚持[[Causality|因果推断]]逻辑的同时，以妥协性控制技术换取更高的[[Ecological Validity|生态效度]]（Ecological Validity）。
> - **因果识别定位** 采用[[Counterfactual|反事实]]潜在结果逻辑，但因果识别依赖于**条件独立性[[Hypothesis|假设]]（Conditional Independence Assumption, CIA）**——即假定在控制了基线[[Pre-test and Post-test|前测]]和关键可观察协[[Variable|变量]]后，组别分配与潜在结果在统计上条件独立。
> - **与[[Randomised Controlled Trials|随机对照试验]]的互补关系** 当出于伦理考量（如不能剥夺弱势学生的必要辅导）、行政限制（学校拒绝打破现有班级建制）、政策可行性，或学校拒绝被[[Random Assignment|随机分配]]宏观组织决策（如混合[[Tracking|能力分组]]分流、作息时间变革）而无法实施 RCT 时，QED 提供唯一合法的因果证据替代路径（[[Argument_Ross_Morrison_2021_ECNUROE|Ross & Morrison, 2021, p. 109]]；[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, pp. 55–56]]）。
> - **法定证据体系的演进定位** 相较于 2001 年《[[No Child Left Behind Act 2001|不让一个孩子掉队法案]]》（No Child Left Behind Act, NCLB）笼统要求的“[[Scientifically Based Research|基于科学的研究]]”（scientifically based research），[[Every Student Succeeds Act|ESSA]] 将 QED 正式制度化为 Tier II 中等[[Evidence Standards|证据标准]]，要求试验方案具备严密的前测基线控制与统计调整模型（[[Argument_Ginsberg_2024_EP|Ginsberg et al., 2024, pp. 162–163]]）。

> [!method-stack] 数据、变量与方法层级
> - **数据结构** 重复截面数据、面板数据（Panel Data）、多时间点追踪序列、多层嵌套行政数据（学生-班级-学校）。
> - **设计形态** 非等对控制组前后测设计、[[Time Series Design|间断时间序列设计]]（Interrupted Time Series, [[Intelligent Tutoring Systems|ITS]]）、[[Regression Discontinuity Design|断点回归设计]]（Regression Discontinuity Design, RDD）、轮换对等设计。
> - **统计控制工具** [[Propensity Score Matching|倾向得分匹配]]（Propensity Score [[Matching]], PSM）、[[Difference-in-Differences|双重差分]]模型（DID）、[[Analysis of Covariance|协方差分析]]（Analysis of Covariance, ANCOVA）、[[Hierarchical Linear Model|多层线性模型]]（Hierarchical Linear Model, HLM）。
> - **辅助技术** 熵平衡（Entropy Balancing）、合成控制法（Synthetic Control）、断点局域多项式平滑、安慰剂检验（Placebo Tests）。

---

## 研究程序

> [!proc] 准[[Experimental Research|实验研究]]标准实施六步规程
> 1. **选择非等对比较组** 依据地理区位、历史[[Academic Achievement|学业成绩]]与生源特征，匹配选择与干预组最相似的自然对照学校或行政班级。
> 2. **实施全面基线测量** 采集详尽的[[Pre-test and Post-test|前测]][[Academic Achievement|学业成绩]]与背景协[[Variable|变量]]，严密核验两组基线等值性（[[Baseline Standardized Mean Difference|Baseline Equivalence]]）。
> 3. **常态化现场干预实施** 干预组落实新教学方案，对照组维持**常规[[Business as Usual|照常教学]]（Business-As-Usual, BAU）**，同步监控[[Implementation Fidelity|实施忠实度]]（Implementation Fidelity）。
> 4. **终结性后测数据采集** 采用完全相同的独立标准化测验开展后测，系统排查差异性[[Attrition|样本流失]]（Differential Attrition）。
> 5. **构建统计因果纠偏模型** 运用[[Difference-in-Differences|双重差分法]]（DID）、逆概率加权（Inverse Probability Weighting, IPW）或[[Analysis of Covariance|协方差分析]]（ANCOVA）剥离基线初始差异与自然时间趋势。
> 6. **开展替代解释敏感性分析** 针对历史事件、测验敏感化、选择-成熟[[Interaction Effect|交互作用]]及对照组代偿性努力开展[[Falsification|证伪]]与安慰剂检验。

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

### 量化分析与估计模型

> [!formula-step] 公式步骤　双重差分基准估计模型（Difference-in-Differences）
> $$Y_{it} = \beta_0 + \beta_1 Treat_i + \beta_2 Post_t + \beta_3 (Treat_i \times Post_t) + \sum_{k} \gamma_k X_{kit} + \varepsilon_{it}$$
>
> **这个公式在做什么** 通过双向固定差分消除干预组与对照组不随时间变化的时间不变偏误（Time-Invariant Confounders）以及两组共同经历的时间自然成熟趋势，从而提炼出干预方案的净因果效应（$\beta_3$）。
>
> **符号说明**
> - $Treat_i$：组别哑变量（1 = 干预组，0 = 对照组）；
> - $Post_t$：时间哑变量（1 = 干预实施后，0 = 基线前测期）；
> - $Treat_i \times Post_t$：交互项，其系数 $\beta_3$ 即为双重差分因果估计值（DID Estimator）；
> - $X_{kit}$：随时间变化的个体或学校协变量矩阵。
>
> **数学直觉** 计算“干预组前后变化量”减去“对照组前后变化量”的差中之差：$\beta_3 = (\bar{Y}_{T,1} - \bar{Y}_{T,0}) - (\bar{Y}_{C,1} - \bar{Y}_{C,0})$。
>
> **结果怎么读** 若 $\beta_3 > 0$ 且统计学显著（$p < 0.05$），表明排除自然成熟趋势后，干预措施带来了实质性学业增益。
>
> **注意事项** DID 的因果识别依赖于**平行趋势假定（Parallel Trends Assumption）**——即若无干预发生，两组[[Dependent Variable|结果变量]]随时间的变动趋势应当完全平行。

> [!formula-step] 公式步骤　基线标准化均值差与 [[What Works Clearinghouse|WWC]] 等值分级判定
> $$\text{SMD}_{\text{baseline}} = \frac{\bar{X}_{T,0} - \bar{X}_{C,0}}{S_p}$$
>
> **这个公式在做什么** 计算干预实施前干预组与非等对对照组在前测学业成就或关键协变量上的基线标准化均值差（Baseline Standardised Mean Difference, SMD），作为准实验因果效度达标与否的门槛依据。
>
> **符号说明**
> - $\bar{X}_{T,0}, \bar{X}_{C,0}$：处理组与对照组的前测样本均值；
> - $S_p$：两组合并前测标准差（Pooled Baseline Standard Deviation）。
>
> **结果怎么读（WWC 对 QED 的基线等值性三级判定准则）**
> - **基线差异 $\le 0.05$ 个标准差（Standard Deviation, SD）** 判定为基线高度等价，统计模型无需额外控制即满足 WWC“有保留达标”；
> - **$0.05\text{ SD} < \text{基线差异} \le 0.25\text{ SD}$** 判定为中度失衡，**必须**在回归模型中纳入前测协变量进行统计调整；
> - **基线差异 $> 0.25\text{ SD}$** 判定为严重不等价，直接裁定为“未达标（Does Not Meet Standards）”，彻底否定其[[Causality|因果推断]]资格（[[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, p. 8]]）。

> [!software-impl] 软件实现
> - **推荐软件** R、Stata、Python。
> - **核心扩展包**
>   - R：`fixest`（高维固定效应与双重差分）、`MatchIt`（倾向得分与匹配分析）、`rdrobust`（[[Regression Discontinuity Design|断点回归]]稳健估计）。
>   - Stata：`diff`（双重差分估计）、`teffects`（处理效应与逆概率加权）、`rdrobust`（断点估计）。
>   - Python：`linearmodels`（面板与双重差分）、`causalinference`（因果匹配与平衡性检验）。
> - **标准流程**
>   1. 数据清洗并检查基线前测平衡性（计算 $\text{SMD}_{\text{baseline}}$ 并绘制平衡性图）；
>   2. 检验平行趋势[[Hypothesis|假设]]（绘制事件研究法 Event-Study 动态滞后与超前系数图）；
>   3. 估计核心处理效应并引入聚类稳健[[Standard Error|标准误]]（Cluster-Robust Standard Errors at school/class level）；
>   4. 开展安慰剂检验（伪断点检验、提前干预检验）与协变量替换敏感性测试。

---

## 政策与清算体系中的审查标准

> [!framework-table] 循证清算中心对 QED 的准入门槛与评级待遇对比（基于 Wadhwa et al., 2024）
> | 清算中心 / 政策法规 | 对 QED 因果设计的描述强度 | 允许获得的最高评级待遇 | 关键限制条件与特殊要求 |
> |:---|:---:|:---|:---|
> | **[[What Works Clearinghouse\|WWC]] (美国联邦)** | 2 级 (明确规程) | **Meets Standards With Reservations**<br>(封顶于二等，不得作为单项一等证据) | 必须满足严苛的基线等值性要求（$\le 0.25\text{ SD}$）及整体/差异流失模型。 |
> | **[[Every Student Succeeds Act\|ESSA 2015 证据标准]] (联邦立法)** | 法定分级 | **Tier 2 (Moderate Evidence)**<br>(中等证据法定上限) | 要求具备良好的统计控制与广泛代表性，作为学区申请联邦资助的合法依据。 |
> | **[[Best Evidence Encyclopedia\|最佳证据百科全书（Best Evidence Encyclopedia, BEE）]]** | 1 级 ([[Meta-analysis\|元分析]]纳入) | **Moderate / Strong** (需与 [[Randomised Controlled Trials\|RCT]] 结合) | 约翰斯·霍普金斯大学（Johns Hopkins University, JHU）团队允许高质量 QED 纳入元分析；最高 Strong 证据允许“1 项大型多中心 RCT + 1 项高质量 QED”组合。 |
> | **[[Blueprints for Healthy Youth Development\|Blueprints]]** | 3 级 (严苛规程) | **Promising** (封顶于二等) | 排除单独 QED 参评 Model / Model Plus 顶级认证；强制要求[[Evaluator Independence\|独立评估者]]报告与[[Fade-out Effect\|持续效果]]。 |
> | **[[National Dropout Prevention Center\|国家预防辍学中心（National Dropout Prevention Center, NDPC）]]** | 1 级 (宽松包容) | **Strong Evidence** (允许 QED 获评最高级) | 准入门槛包容，仅要求存在显著正向 QED 证据且方案在学校现场实际运行满 3 年。 |

> [!critique] 单项 QED 法定门槛下的合规假象与科研供给断层（基于 Ginsberg et al., 2024）
> 约娜·金斯伯格（Yona Ginsberg）等学者对全美大型城市学区三年总计 2.88 亿美元联邦 [[Title I of the Elementary and Secondary Education Act|Title I]] 支出流水与四大公共证据库（WWC、[[Evidence for ESSA]]、[[Education Endowment Foundation|教育捐赠基金会]]（Education Endowment Foundation, EEF）、[[Education Resources Information Center|教育资源信息中心]]（Education Resources Information Center, ERIC））的实证审计，揭示了 QED 在当代证据治理中的制度困境（[[Argument_Ginsberg_2024_EP|Ginsberg et al., 2024, pp. 162–165, 174–178]]）：
> 1. **法定单项 QED 门槛下的形式化合规偏差** 《每个学生都成功法案》（[[Every Student Succeeds Act|ESSA]]）法定规则允许“仅凭单项设计良好的实验（Tier I）或准实验（Tier II）研究呈现显著正向效应”，即可认定整笔教育采购合法合规。实证发现，基于单项合格研究门槛，学区超过 95%（直接按全校项目计达 99%）的资金均符合法定标准；然而，一旦引入“全量证据体综合评价[[Paradigm|范式]]”（Full Body of Evidence Paradigm），全面审视同一实践在各数据库中的所有 QED 与 RCT 结果，获稳定积极实证支持的资金比重降至 49%–58%，表明单项 QED 门槛极易被学区用作挑选樱桃（cherry-picking）的合规工具。
> 2. **目标学段 QED 实证研究供给不足** 基础教育科研界在大规模 QED 生产上存在明显的学段断层。实证发现，样本学校采购的教育实践中，有多达 26 项实践在相关目标学段（如高中国语或特定小学学段）根本不存在任何 QED 或 RCT 因果证据；学区被迫在缺乏目标学段因果支持的情况下进行跨学段推论。
> 3. **微观复合实践的因果识别局限** 现有 QED 研究大多针对宏观打包课程方案（如全校性数学项目或青少年综合发展计划），而极少对学区实际采购的微观交付构件（如面对面微课辅导、驻校咨询、实地考察 [[Champ|field]] trips）进行独立的准实验因果识别，导致大量财政资金投入到未经因果检验的细分环节之中。

> [!case] 英国[[Education Endowment Foundation|教育捐赠基金会]]（EEF）“研究[[School Choice|学校选择]]”资助序列的准实验转向（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, pp. 55–56]]）
> 切斯特·埃多瓦尔德（Chester Edovald）与克莱尔·内维尔（Claire Nevill）系统记录了循证因果评估在真实学校系统中的重大方法学调适：
> - **学校对[[Random Assignment|随机分配]]的抵制困境** 教育捐赠基金会（Education Endowment Foundation, EEF）长期以大规模学校级随机对照试验（Randomised Controlled Trials, RCT）为黄金标准，已招募超过半数英格兰学校参与试验；然而，当评估涉及学校内生性宏观组织政策而非外购干预项目时，学校强烈抵制被随机分配（如混合能力分组 vs 基于能力的分轨分流 RCT 因学校拒绝被随机分组而招募失败，Roy et al., 2014；中学调整上学时间试验同样遭遇招募流产，Robinson, 2016）。
> - **设立“[[Researching School Choices|研究学校选择]]”专门资助序列** 为解答学校内生决策对教育产出的真实影响，EEF 于 2019 年正式增设“研究学校选择（Researching school choices）”专门资助序列，确立了利用教育系统内部客观存在的**自然变异（natural variation）**、结合准实验设计（QEDs）评估宏观学校政策的制度合法性。
> - **制度化因果质控准则** EEF 对此类 QED 研究设立了与 RCT 同等严苛的方法学门槛，强制要求评估团队坚持行业最佳实践（如[[Pre-test and Post-test|前测]]基线等值性严格控制、透明[[Preregistration|预注册]]制度，以及评估者独立性与无利益冲突审查）。

> [!abstract] [[Counterfactual|反事实]]可行性与比较组强度（Counterfactual Viability）
> [[Argument_Ross_Morrison_2021_ECNUROE|Ross & Morrison (2021, p. 112)]] 指出，QED 的有效性高度依赖于反事实可行性（Counterfactual Viability）：
> - **比较条件的真实强度** 对照组若为“低质量、低强度或缺乏支持的弱条件”，干预容易呈现虚大[[Effect Size|效应量]]；若对照组为“成熟优质的常规教学”，效应量虽小但代表真实的政策净附加值。
> - **透明报告对照组生态** 证据审查不仅要审查干预组，更必须详尽报告对照组的教学时间、支持资源与课程[[Logic Model|逻辑模型]]，否则无法在真实学校间迁移。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 自然班级和完整学校建制不可随意打散拆分时；学校强烈抵制被[[Random Assignment|随机分配]]宏观组织决策（如[[Tracking|能力分组]]分流、作息制度变革、校历调整）时；利用行政区划、政策试点边界或考试录取分数线开展回溯性因果评估时；弱势群体补偿性项目（伦理上不允许设立无支持的空白对照组）（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, pp. 55–56]]；[[Argument_Ross_Morrison_2021_ECNUROE|Ross & Morrison, 2021, p. 109]]）。
> - **谨慎使用** 候选对照组与干预组在学区财政、生源社会经济地位上存在系统性鸿沟且无法通过统计匹配消除时；[[Attrition|样本流失]]率极高且存在严重差异性流失时；需要向目标学段之外进行跨学段外推时（[[Argument_Ginsberg_2024_EP|Ginsberg et al., 2024, pp. 177–178]]）。
> - **不适合使用** 完全缺乏基线[[Pre-test and Post-test|前测]]数据、无法通过历史档案构建可信对照的单组事后研究；旨在推断复杂教育系统内深层主观体验、文化生态或哲学意义的[[Qualitative Research|质性研究]]。

---

## 局限性

> [!method-limits] 方法局限与偏误控制
> - **选择-成熟交互威胁（Selection-Maturation Interaction）** 即使基线[[Pre-test and Post-test|前测]]分数完全平衡，来自优势社区学校的对照组学生其自然认知[[Growth|成长]]斜率可能显著快于薄弱校干预组，导致因果估计产生系统性正向或负向偏倚（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, pp. 318–320]]）。
> - **不可测混杂与遗漏[[Variable|变量]]偏倚（Omitted Variable Bias）** [[Propensity Score Matching|倾向得分匹配]]（PSM）与回归控制仅能平衡已观测到的协变量，无法控制教师教学热情、学生求知动机与家庭[[Bildung|教养]]风格等不可测潜变量。
> - **均值回归假象（Regression to the Mean）** 当依据前测极端低分筛选补救干预对象时，后测成绩的提高往往部分源于极端测验误差的统计回归，而非干预方案的纯因果实效。
> - **法定单项合规掩盖全量证据赤字** 在证据治理中，单项 QED 易被异化为合规工具，掩盖同一实践在全量证据库中高达 42%–51% 的无支持或负效应现实（[[Argument_Ginsberg_2024_EP|Ginsberg et al., 2024, p. 177]]）。
> - **实践维度的信息遮蔽** QED 同 [[Randomised Controlled Trials|RCT]] 一样，若仅报告平均[[Effect Size|效应量]]，会系统性遗漏学校采纳最急需的微观实施成本、师生满意度与本地适配指南（[[Argument_Ross_Morrison_2021_ECNUROE|Ross & Morrison, 2021, pp. 120–122]]）。

---

## 相关理论与方法

> [!entry-map]
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Campbellian Validity Framework]] | 理论 | 为准实验设计提供四大效度体系（[[Internal Validity\|内部效度]]、[[External Validity\|外部效度]]、[[Construct Validity\|构念效度]]、统计结论效度）及效度威胁排除逻辑。 |
> | [[Postpositivism]] | 理论 | 为准实验在开放真实社会情境中通过不完美控制逼近客观因果规律提供[[Epistemology\|认识论]]哲学支撑。 |
> | [[Evidence Standards]] | 政策规程 | 规定 QED 对应 Tier II 中等证据（Moderate Evidence）法定资质，作为学区申请联邦资助的合法依据。 |
> | [[Every Student Succeeds Act]] | 政策法规 | 联邦立法确立分级证据体系，将 QED 制度化为指导学区教育采购与改进干预的核心方法标尺。 |
> | [[What Works Clearinghouse]] | 评估机构 | 制定形式化因果审查规程，确立 QED 基线等值性（$\le 0.25$ SD）及“有保留达标”评级门槛。 |
> | [[Education Endowment Foundation]] | 实践机构 | 设立“[[Researching School Choices\|研究学校选择]]”资助序列，利用自然变异通过严密 QED 评估学校宏观组织决策。 |
> | [[Randomised Controlled Trials]] | 参照方法 | 真实实验基准，QED 在因[[Random Assignment\|随机化]]受阻而面临伦理或组织阻力时的首要因果替代方案。 |
> | [[Difference-in-Differences]] | 统计工具 | QED 剥离组别初始差异与宏观时间趋势的核心计量因果估计模型。 |
> | [[Propensity Score Matching]] | 统计工具 | 依据多维可观察协[[Variable\|变量]]测算倾向得分，为干预组匹配最相似自然对照样本以削弱选择偏倚。 |
> | [[Regression Discontinuity Design]] | 准实验变体 | 依据连续变量阈值实施断点分组，在阈值局部近似随机分配的最强准实验因果识别设计。 |
> | [[Time Series Design]] | 准实验变体 | 跨越干预前后多时间点连续观测以建立动态[[Counterfactual\|反事实]]趋势线的无对照或有对照序列设计。 |
> | [[Baseline Standardized Mean Difference]] | 质控指标 | 测度干预组与对照组基线失衡程度的标准量，作为 WWC 裁定 QED 是否达标的核心门槛。 |
> | [[Tracking]] | 核心应用 | 因学校抵制随机分配导致 RCT 招募失败的典型学校内生组织政策，转由 QED 实施因果评估。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011)]] — 体系化梳理准实验五大经典设计（非等对控制组、时间序列、[[Regression Discontinuity Design|断点回归]]、轮换对等），详析选择-成熟交互与均值回归等效度威胁（Ch. 16, pp. 317–324）。
> - [[Argument_Wadhwa_2024_RER|Wadhwa et al. (2024)]] — 全景比较 12 所清算中心对 QED 的因果审查规程（0–3 级[[Coding in Qualitative Research|编码]]），揭示 [[What Works Clearinghouse|WWC]] 与 [[Home Visiting Evidence of Effectiveness|HomVEE]] 的 0.05–0.25 SD 基线等值模型及 QED 在最高证据层级中的制度性分歧（pp. 8–11）。
> - [[Argument_Ross_Morrison_2021_ECNUROE|Ross & Morrison (2021)]] — 深入探讨 QED 在 [[Every Student Succeeds Act|ESSA]] Tier 2 政策证据层级中的应用，提出[[Counterfactual|反事实]]可行性（Counterfactual Viability）与对照组生态报告的必要性（pp. 109–112）。
> - [[Argument_Hitchcock_2015_JBE|Hitchcock et al. (2015)]] — 论证准实验、[[Single-Subject Design|单一被试设计]]与组间 [[Randomised Controlled Trials|RCT]] 在排除历史与成熟威胁上的同构逻辑与效度门控机制（pp. 461–464）。
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 总结英国[[Education Endowment Foundation|教育捐赠基金会]]（EEF）在学校拒绝[[Random Assignment|随机分配]]宏观政策背景下，设立“[[Researching School Choices|研究学校选择]]”资助序列、利用系统自然变异推进准实验因果评估的方法学制度演进（pp. 55–56）。
> - [[Argument_Ginsberg_2024_EP|Ginsberg et al. (2024)]] — 审计大型城市学区 2.88 亿美元支出流水，实证揭示单项 QED 法定中等证据门槛下超过 95% 的名义合规假象、学段科研供给断层及微观复合实践归因局限（pp. 162–165, 174–178）。
