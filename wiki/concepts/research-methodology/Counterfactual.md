---
title: Counterfactual
aliases:
  - 反事实
  - 反事实推理
  - counterfactuals
  - counterfactual reasoning
  - counterfactual comparison
  - 反事实对照
summary: "因果推断中通过构建与设想原因不存在时的潜在结果以识别真实因果效应的核心推理机制，在实证研究中依托控制组与随机分配构建无偏反事实代理"
type: concept
domain: "research-methodology"
related_count: 44
related_level: 4
related_stars: "⭐⭐⭐⭐"
related_color: "#fdba74"
tags:
  - subject/research-methodology
  - topic/causation
  - topic/experimental-design
  - evidence-based-reform
related_concepts:
  - "[[Causality]]"
  - "[[Hypothesis]]"
  - "[[Variable]]"
  - "[[Order Effects]]"
  - "[[Internal Validity]]"
  - "[[Independent Variable]]"
  - "[[Operationalization]]"
  - "[[Business as Usual]]"
  - "[[Epistemology]]"
  - "[[Necessary and Sufficient Conditions]]"
  - "[[Fundamental Problem of Causal Inference]]"
  - "[[Attrition]]"
  - "[[Preregistration]]"
  - "[[Clinical Trial]]"
  - "[[Evidence-Based Education]]"
  - "[[Evidence Standards]]"
  - "[[Heterogeneity]]"
  - "[[Realism in International Relations]]"
  - "[[Ontology]]"
  - "[[Hawthorne Effect]]"
  - "[[Paradigm]]"
  - "[[Cooperative Integrated Reading and Composition]]"
  - "[[Statistical Analysis Plan]]"
  - "[[Measurement Alignment]]"
related_theories:
  - "[[Potential Outcomes Framework]]"
related_methods:
  - "[[Random Assignment]]"
  - "[[Experimental Research]]"
  - "[[Pre-test and Post-test]]"
  - "[[Covariate Adjustment]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Sample Size Determination]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Cluster Randomized Trials]]"
  - "[[Effect Size]]"
related_persons:
  - "[[Robert Slavin]]"
related_facts:
  - "[[What Works Clearinghouse]]"
  - "[[Education Endowment Foundation]]"
  - "[[Success for All]]"
  - "[[ISRCTN]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]"
  - "[[Argument_Slavin_2019_EP]]"
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
related_instruments:
  - "[[EEF Padlock Security Rating]]"
confidence: high
status: draft
created: 2026-06-17
updated: 2026-09-17
---

# Counterfactual

---

## 定义

> [!def] 核心定义
> 反事实（Counterfactual）是[[Causality|因果推断]]中通过设想与构建“若[[Hypothesis|假设]]的原因不存在，效果是否还会发生或呈现何种状态”来判定因果效应的核心推理机制：如果假设原因 $X$ 发生时产生结果 $Y(1)$，而在 $X$ 不发生的替代可能世界中结果为 $Y(0)$，则因果效应即定义为 $Y(1) - Y(0)$。由此提出的检验问题是：“如果那个假设的原因不存在，效果还会发生或还是原来的样子吗？”如果答案是否定的，方可确证 $X$ 对 $Y$ 具有实质促成作用（Mackie, 1993; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 55–56]]）。在实证教育研究中，反事实主要依托[[Random Assignment|随机分配]]设立的控制组来构建无偏的反事实代理（[[Argument_Slavin_2019_EP|Slavin, 2019, pp. 22–23]]）。

> [!concept-lens] 概念透镜
> - **含义** 反事实是对“如果情境不同，替代结果会怎样”的严密潜在结果（Potential Outcomes）界定，追问干预缺失状态下的真实基线。
> - **用途** 帮助研究者区分真正的因果增益与单纯的时间先后伴随、自然成熟效应或历史混淆[[Variable|变量]]。
> - **边界** 反事实推理无法在个体层面被直接观察（因同一个人无法在同一时点既接受又不接受干预）；在多重因果交织的复杂教育生态中，反事实必须通过大样本群组平均效应与严格实验控制方能近似逼近。

> [!citation-card] 反事实与因果关系的确证基石
> 判定因果关系是否存在的关键标志在于反事实的成立：即明确如果假设的原因不存在，所观察到的效果就不会发生。在教育实验中，控制组正是作为反事实的代理而存在的——它假定反映了实验组在没有接受该项教学干预时本应呈现的发展状态。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|(Cohen et al., 2011, p. 56)]]
>
> *A marker of whether causation is operating is the counterfactual: if the supposed cause X did not occur then the effect Y would not occur... in [[Experimental Research]], a control group acts as a counterfactual, standing in for what would have happened to the experimental group without the intervention.*

> [!boundary]- 概念边界
> - 不等于 单纯前[[Pre-test and Post-test|后测]]对比（Pre-post Comparison） — 前后测只记录了干预组自身随时间推移的变化，混杂了学生生理心理自然成熟、测试[[Order Effects|练习效应]]与外部环境干扰，缺乏真正的无干预反事实对照。
> - 不等于 观察性统计相关与[[Covariate Adjustment|协变量调整]] — 统计回归控制虽然能在数学上调整已知可测混淆因素，但无法排除未观测混淆变量（Unobserved Confounders）与选择偏差，不能等同于实验诱导的反事实状态。
> - 不等于 纯思辨性哲学思想实验 — 现代实证科学中的反事实要求通过大样本[[Randomised Controlled Trials|随机对照试验]]（Randomised Controlled Trial, RCT）或高质量准实验，在真实世界中构建可度量、可复现的实体对照组代理。

---

## 概念辨析

> [!contrast-table] 反事实对照与相邻推论方式的辨析
> | 维度 | 实验反事实对照（[[Randomised Controlled Trials\|RCTs]]） | 单组前[[Pre-test and Post-test\|后测]]对比（Pre-Post） | 观察性[[Covariate Adjustment\|协变量调整]]回归 | 思辨哲学思想实验 |
> |---|---|---|---|---|
> | **反事实构建方式** | 依托[[Random Assignment\|随机分配]]建立同质控制组作为实体反事实代理 | 将受试者干预前的历史状态假定为反事实基线 | 通过统计模型在数学上剥离已知协[[Variable\|变量]] | 在脑海中逻辑设想“若无原因”的可能世界 |
> | **混淆控制能力** | 同时平衡已测与未测混淆[[Variable\|变量]]，达成 ceteris paribus（其他条件相同） | 完全无法控制自然成熟、历史事件与测试回归效应 | 仅能控制已观测纳入模型的变量，面临遗漏变量偏倚 | 依赖理论演绎与直觉[[Hypothesis\|假设]]，无法接受经验数据检验 |
> | **[[Causality\|因果推断]]效度** | [[Internal Validity\|内部效度]]极高，公认为因果识别的黄金标准 | 因果效度极低，极易将时间伴随误判为干预效应 | 因果效度中等，依赖强无混淆假设（Unconfoundedness） | 属于假说生成工具，不具备直接经验证据效力 |
> | **教育政策适用性** | 为循证采购提供强因果依据（如 [[What Works Clearinghouse\|WWC]] 与 EEF） | 常见于教师日常叙事，但严禁作为法定循证依据 | 用于无法实施随机化的大规模普查与政策评估 | 用于构建概念模型与因果机制理论推导 |

---

## 核心要素

> [!feature] 反事实[[Causality|因果推断]]的核心要素
> - **[[Hypothesis|假设]]原因识别（Hypothesized Cause）** 明确待检验的[[Independent Variable|自变量]]或教学干预措施，界定干预的边界与[[Operationalization|操作化]]内涵。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|(Cohen et al., 2011, p. 55)]]
> - **潜在结果界定（Potential Outcomes）** 设定研究对象在接受干预下的潜在结果 $Y(1)$ 与在未接受干预下的潜在结果 $Y(0)$。
> - **反事实观测困境（Unobservability）** 承认任何个体在特定时空只能处于一种现实状态，反事实状态在个体层面上具有不可直接观测性。
> - **实体代理对照构建（Counterfactual Proxy）** 通过[[Random Assignment|随机分配]]设立控制组，以控制组的群体平均结局作为实验组反事实状态的无偏估计。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|(Cohen et al., 2011, p. 56)]]
> - **真实生态常态对照（Business-as-Usual Contrast）** 在教育实地实验中，反事实不仅指“零干预”，更指控制组学校所接受的常规标准教学（[[Business as Usual]], BAU），反映真实实践反差。[[Argument_Slavin_2019_EP|(Slavin, 2019, pp. 22–23)]]

> [!logic-map]- 反事实因果推断与代理构建逻辑
> ```mermaid
> flowchart LR
>     subgraph CausalProblem["因果推断基本问题"]
>         T["处理对象（接受干预 X）"] --> Y1["观测到现实结果 Y(1)"]
>         T -.->|"无法直接观测"| Y0_missing["反事实潜在状态 Y(0)"]
>     end
> 
>     subgraph ExperimentalSolution["随机试验与反事实代理"]
>         Pop["总体样本池"] -->|"随机分配 (Random Assignment)"| Exp["实验组 (Treatment)"]
>         Pop -->|"随机分配 (Random Assignment)"| Ctrl["控制组 (Control / BAU)"]
>         Exp --> Y_exp["实验组现实均值 E[Y(1)]"]
>         Ctrl --> Y_ctrl["控制组现实均值 E[Y(0)]<br>(反事实无偏代理)"]
>     end
> 
>     subgraph CausalInference["因果效应判定"]
>         Y_exp & Y_ctrl --> Tau["平均处理效应 ATE = E[Y(1)] - E[Y(0)]"]
>     end
> 
>     CausalProblem --> ExperimentalSolution
>     ExperimentalSolution --> CausalInference
> ```

---

## 围绕概念形成的命题

---

### 命题一　反事实对照是区分真实因果推断与单纯时间伴随的核心标志

> [!concept-lens] 因果识别的[[Epistemology|认识论]]判准
> 探讨如何超越休谟的经典时间先后性，以“无原因则无结果”的逆向反事实检验确立因果必然性与因果权重。

> [!claim] Mackie, J. L.
> **反事实作为因果存在的决定性标志** 区分[[Causality|因果关系]]是否发生的本质标志是反事实的存在——即确定[[Hypothesis|假设]]原因 $X$ 的缺失会导致效果 $Y$ 的缺失。单纯的时间先后发生（休谟的优先性原则）仅仅是因果关系的[[Necessary and Sufficient Conditions|必要条件]]而非充分条件；只有当通过理性设想或实证对照排除了“即使没有 $X$，$Y$ 仍会发生”的可能性时，才能判定 $X$ 是引发 $Y$ 的实质原因。（Mackie, 1993）

> [!claim] Cohen, Manion & Morrison
> **多重因果情境下的反事实解释边界** 在现实复杂的社会与教育情境中，单一因素很少构成效果的充分条件。反事实推理能够有效检验某个因素是否属于促成原因之一（即 INUS 条件），但无法决定全部因果权重；研究者必须清醒认识到，即使某一特定原因缺席，其他并存的替代机制仍可能引发相似效果。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|(Cohen et al., 2011, pp. 55–56)]]

---

### 命题二　随机分配通过构建可比对照组克服因果推断基本问题并提供无偏反事实代理

> [!concept-lens] [[Potential Outcomes Framework|潜在结果框架]]与实验反事实代理构建
> 探讨面对个体反事实不可观测的认识论困境，[[Random Assignment|随机分配]]如何在大样本群体层面上实现其他条件相同（ceteris paribus）并生成合法的反事实基线。

> [!claim] Holland, P. W.
> **[[Fundamental Problem of Causal Inference|因果推断的基本问题]]与群体反事实替代** 因果分析的根本障碍在于“因果推断的基本问题”（Fundamental Problem of Causal Inference）：研究者永远无法在同一时间点对同一个体同时观测到接受处理 $Y(1)$ 与未接受处理 $Y(0)$ 的状态。因此，科学因果推断必须从个体层面的因果效应转向群体层面的平均处理效应（Average Treatment Effect, ATE）；通过随机分配，使得实验组与控制组在处理前的所有特征期望完全相同，从而使控制组的现实表现合法地充当实验组未受干预时的反事实代理。（Holland, 1986, pp. 945–947）

> [!claim] Edovald & Nevill
> **大样本随机试验对反事实有效性的制度保障** 在大规模教育试验中，反事实代理的有效性高度取决于[[Sample Size Determination|样本量]]规模与数据损耗控制。微弱样本或高[[Attrition|流失]]率会破坏随机分配建立的初始同质性，引入选择性偏倚，导致控制组偏离真实的反事实基准；高标准循证机构（如英国 [[Education Endowment Foundation|EEF]]）通过大样本多中心设计与严格方案[[Preregistration|预注册]]，确保反事实估计免受研究者操作偏倚的侵蚀。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 50–53)]]

---

### 命题三　整群随机分配与多层线性模型在真实学校生态中保障宏观反事实的外部概化力

> [!concept-lens] 学校组织生态下的宏观反事实与多层统计结构
> 探讨教育改革如何突破微观个体反事实的局限，在学校与班级整群层面构建具有政策意义的常态对照基准。

> [!claim] [[Robert Slavin|Slavin, R.]] E.
> **整群试验中常规教学对照（BAU）的反事实实质与多层嵌套校正** 教育政策改革中的因果验证不能依赖抽象教学原则，而必须依托整校层面的整群[[Randomised Controlled Trials|随机对照试验]]。在整校改革中，控制组所代表的反事实并非虚无真空，而是各校正在实施的真实常规教学（[[Business as Usual]], BAU）。由于学生嵌套于班级、班级嵌套于学校，反事实比较必须采用[[Hierarchical Linear Model|多层线性模型]]（Hierarchical Linear Modeling, HLM）进行方差分解，纠正群聚效应导致的自由度虚高；只有在全校生态中经受住与 BAU 的反事实对照检验，干预措施才具备真正向全美学校规模化推广的有效性。[[Argument_Slavin_2019_EP|(Slavin, 2019, pp. 22–23, 26–27)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **因果识别判准命题** | 反事实是超越时间先后、确证真正因果关系的必要识别标志 | 哲学因果分析、教育质性与量化因果推论 | 约翰·麦基（John L. Mackie）; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04\|Cohen et al. (2011)]] |
> | **实验代理构建命题** | 随机分配通过群体平衡克服不可观测性，构建无偏反事实代理 | [[Clinical Trial\|临床试验]]、心理与教育随机对照试验（RCTs） | 保罗·霍兰德（Paul Holland）; [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]] |
> | **生态常态与多层校正命题** | 学校整群试验中反事实体现为常规教学（BAU），需依托 HLM 确保宏观推论效度 | 全校性教育改革、政府循证政策评估与规模化推广 | [[Robert Slavin\|罗伯特·斯莱文]]（Robert Slavin）; [[Argument_Slavin_2019_EP\|Slavin (2019)]] |

---

## 概念演变

> [!dev-timeline] 概念演变
> - **1748 — 休谟哲学反事实雏形** 大卫·休谟（David Hume）在《人类理解研究》中首次提出反事实定义：“若第一个对象不存在，则第二个对象从未存在”，开启了[[Causality|因果推断]]的反事实思考传统。
> - **1923–1974 — 内曼-鲁宾潜在结果模型** 耶日·内曼（Jerzy Neyman, 1923）与唐纳德·鲁宾（Donald Rubin, 1974）形式化建立了潜在结果模型（Rubin Causal Model），用数学符号严密界定个体接受与未接受处理的潜在状态。
> - **1986 — 霍兰德提出因果推断基本问题** 保罗·霍兰德（Paul Holland, 1986）发表里程碑论文《统计学与因果推断》，明确断定因果推断的本质困难在于反事实不可直接观测，确立[[Random Assignment|随机化]]实验作为群体反事实代理的基准地位。
> - **1993 — 麦基系统化因果条件与反事实** 约翰·麦基（John L. Mackie, 1993）在《世界的隐秘结构》中深入阐述 INUS 条件与反事实检验，为社会科学因果分析提供[[Epistemology|认识论]]工具。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|(Cohen et al., 2011, p. 55)]]
> - **2002–2015 — [[Evidence-Based Education|循证教育]]改革确立反事实实证标准** 美国成立[[What Works Clearinghouse|有效干预清算中心]]（WWC），出台严格因果[[Evidence Standards|证据标准]]，要求有效性主张必须基于具备同质反事实对照组的高质量 [[Randomised Controlled Trials|RCT]] 或 [[Quasi-Experimental Designs|QED]]。
> - **2019 — 斯莱文推进整群生态反事实与规模化标准** [[Robert Slavin|罗伯特·斯莱文]]（Robert Slavin, 2019）总结三十年循证改革经验，强调全校改革必须在真实学校生态中进行[[Cluster Randomized Trials|整群随机试验]]，以常规教学（BAU）为反事实基准，并结合 [[Hierarchical Linear Model|HLM]] 纠正层级嵌套偏倚。[[Argument_Slavin_2019_EP|(Slavin, 2019, pp. 22–27)]]

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 方法论纯洁性 vs 真实生态常态对照的[[Heterogeneity|异质性]]
> > 争论聚焦于教育实验中的反事实对照应当追求高度受控的人工“安慰剂”状态，还是采纳学校日常真实发生的教学常态。
> >
> > - **人工严格受控派（传统实验心理学）** 坚持反事实控制组必须剔除所有非特异性干预成分，追求因果解释的纯洁性与高[[Internal Validity|内部效度]]。
> > - **生态常态对照派（[[Argument_Slavin_2019_EP|Slavin, 2019, pp. 22–23]]）** 指出教育并非医学给药，控制组教师绝不可能处于“零教学”真空；教育反事实必须定义为常规教学对照（BAU），唯有超越现存真实实践的干预才具备推广价值。
>
> > [!axis] 平均处理效应（ATE）的反事实充分性 vs 异质性机制黑箱
> > 争论围绕量化反事实推导出的群体平均效应是否足以指导复杂的教育决策。
> >
> > - **实验因果派（Holland, 1986; WWC）** 强调群体平均反事实是排除偏倚、达成科学因果推论的唯一可靠途径。
> > - **批判[[Realism in International Relations|现实主义]]派（Biesta, 2007; Pawson, 2006）** 批评单纯的量化反事实比较只呈现“黑箱”输入与输出，无法揭示“在何种情境下、对谁、通过何种机制起作用”，容易掩盖处境不利亚群体的异质性反应。

> [!warning] 适用局限
> - **[[Causality|因果推断]]基本问题的[[Ontology|本体论]]限制** 任何个体层面的反事实状态均无法被直接观测，所有实证估计本质上都是基于群体可比性[[Hypothesis|假设]]的统计近似（Holland, 1986）。
> - **对照组污染与[[Hawthorne Effect|霍桑效应]]** 在学校实地研究中，控制组教师可能通过非正式交流模仿实验组做法（对照污染），或因意识到处于对照状态而改变日常行为（霍桑效应/补偿性均等），从而扭曲真实的反事实基准。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 54–55)]]
> - **非实验情境下的混淆假设风险** 在缺乏[[Random Assignment|随机分配]]的观察性研究中，反事实推论极度依赖“可忽略性假设”（Ignorability），若遗漏关键未测[[Variable|变量]]，反事实估计将产生严重系统性偏倚。

---

## 典型案例

> [!case] 冰面摔倒与反事实的多重因果边界
> 如果人行道上没有结冰，我就不会滑倒摔断手臂——因此冰的存在是骨折的促成原因之一（通过了反事实检验）。然而，冰并不是导致骨折的充分原因：即使路面结冰，若当事人具备出色的平衡能力、视力良好、光线充足、穿着高抓地力防滑鞋且骨质健康，骨折也不会发生。该案例生动说明了反事实推理在多重因果交织网络中识别促成因素的有效性及其解释边界。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|(Cohen et al., 2011, pp. 55–56)]]

> [!case] 全员成功（[[Success for All|SFA]]）与常规教学（BAU）的整群反事实检验
> 在全员成功（Success for All, SFA）全校综合改革项目的大规模实证评估中，研究团队将数十所处境不利小学整群[[Random Assignment|随机分配]]为 SFA 实验组与 BAU 控制组。控制组学校继续沿用学区原有常规阅读教材与教法（作为真实的政策反事实）。在持续多年的追踪测试中，SFA 学校在独立标准化阅读测验上显著超越了 BAU 控制组，从而确证了结构化全校改革相对于日常分散教学的因果净增益。[[Argument_Slavin_2019_EP|(Slavin, 2019, pp. 22–24)]]

---

## 实证数据

> [!ref-table]- 其他实证结果（无[[Effect Size|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04\|Cohen et al. (2011)]] | 教育研究方法论[[Causality\|因果推断]][[Paradigm\|范式]]与逻辑分析 | [[Epistemology\|认识论]]与方法论概念梳理 | 因果条件识别、反事实存在性检验与实验控制 | 系统辨析休谟时间先后性、麦基反事实判准与控制组代理机制 | — | 确立反事实推理在教育实验与[[Quasi-Experimental Designs\|准实验设计]]中的方法学基石地位（pp. 55–56） |
> | [[Argument_Slavin_2019_EP\|Slavin (2019)]] | 全美教育循证改革三十年经验与多项大型整校改革评估（如 [[Success for All\|SFA]]、[[Cooperative Integrated Reading and Composition\|CIRC]]、DI） | 宏观政策综述与整群 [[Randomised Controlled Trials\|RCT]] 方法学评析 | 整校改革干预 vs 常规教学（BAU）反事实对照；标准化独立测验与 [[Hierarchical Linear Model\|HLM]] 方差校正 | 证实缺乏严格 BAU 反事实对照的非实验项目极易高估成效；严格整群 RCT 确立了可复制全校模式的真实因果效度 | — | 说明反事实在真实学校生态中必须依托整群[[Random Assignment\|随机化]]与多层模型方能保障政策外推效度（pp. 22–27） |
> | [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]] | 英国 [[Education Endowment Foundation\|EEF]] 前 8 年资助的 190+ 项大规模学校实地试验（涉及万所学校） | 大规模教育随机对照试验（RCT）元评估 | 试验[[Preregistration\|预注册]]（[[ISRCTN]]）、方案锁定（[[Statistical Analysis Plan\|SAP]]）、国家统考（NPD）对照与[[EEF Padlock Security Rating\|挂锁安全评级]] | 严格大样本随机化有效保障了控制组反事实基线同质性；强调[[Measurement Alignment\|测量对齐]]偏差（自编测验）会人为扭曲反事实反差 50%–100% | — | 实证揭示教育实地试验中维护反事实纯洁性所面临的实施[[Attrition\|流失]]与测量工具硬约束（pp. 50–55） |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al. (2011)]] — 阐述教育研究中[[Causality|因果推断]]的[[Epistemology|认识论]]演进，系统辨析休谟时间先后性与麦基反事实判准，界定实验控制组作为反事实代理的操作逻辑。
> - [[Argument_Slavin_2019_EP|Slavin (2019)]] — 论证全校教育改革在真实学校生态中以常规教学（BAU）为反事实基准的重要性，确立整群[[Randomised Controlled Trials|随机对照试验]]与[[Hierarchical Linear Model|多层线性模型]]在循证改革中的方法学支柱地位。
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 解构英国[[Education Endowment Foundation|教育捐赠基金会]]（EEF）大规模学校实地试验中的反事实构建与质量规约，实证分析自编测验扭曲反事实反差的风险及独立标准化测量的治理价值。

