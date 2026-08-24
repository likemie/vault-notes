---
title: Causality
aliases:
  - 因果性
  - 因果关系
  - 因果推断
  - causal inference
  - causation
summary: "教育与社会科学中建立原因与效果之间关系的推理体系，涵盖概率因果、反事实潜在结果模型、因果识别设计层级（RCT/QED/RDD/SCD）以及生成性因果机制与筛选隔离逻辑。"
type: concept
domain: "research-methodology"
related_count: 57
related_level: 5
related_stars: "⭐⭐⭐⭐⭐"
related_color: "#fecdd3"
tags:
  - causality
  - causal-inference
  - counterfactual
  - experimental-design
  - research-methodology
  - probabilistic-causation
related_concepts:
  - "[[Variable]]"
  - "[[Probabilistic Causation]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Counterfactual]]"
  - "[[Hypothesis]]"
  - "[[Internal Validity]]"
  - "[[Necessary and Sufficient Conditions]]"
  - "[[Causal Over-determination]]"
  - "[[Homework]]"
  - "[[Multiplicity]]"
  - "[[Rashomon Effect]]"
  - "[[Action Narratives]]"
  - "[[Screening Off]]"
  - "[[Pre-test and Post-test]]"
  - "[[Compound Causes]]"
  - "[[Interaction Effect]]"
  - "[[Threats to Internal Validity]]"
  - "[[Effect Size]]"
  - "[[Operationalization]]"
  - "[[Construct Validity]]"
  - "[[Evaluator Independence]]"
  - "[[Fade-out Effect]]"
  - "[[Iatrogenic Effects in Education]]"
  - "[[Attrition]]"
  - "[[Implementation Fidelity]]"
  - "[[Emergence]]"
  - "[[Heterogeneity]]"
  - "[[Causal Processes]]"
  - "[[Transfer Translation Transformation]]"
related_theories:
  - "[[Realist Evaluation]]"
  - "[[Potential Outcomes Framework]]"
related_methods:
  - "[[Multiple Regression]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Random Assignment]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Regression Discontinuity Design]]"
  - "[[Pretest-Posttest Control Group Design]]"
  - "[[Factorial Design]]"
  - "[[Qualitative Research]]"
  - "[[Ethnography]]"
  - "[[Mixed Methods Research]]"
  - "[[Gating Procedure]]"
  - "[[Single-Case Design]]"
  - "[[Intent-to-Treat Analysis]]"
  - "[[Single-Subject Design]]"
  - "[[ABAB Design]]"
  - "[[Causal Modeling]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[What Works Clearinghouse]]"
  - "[[Blueprints for Healthy Youth Development]]"
  - "[[Home Visiting Evidence of Effectiveness]]"
  - "[[Top Institute for Evidence-Based Education Research]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]"
  - "[[Argument_Hitchcock_2015_JBE]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
confidence: high
status: active
created: 2026-05-31
updated: 2026-08-21
---

# Causality

---

## 定义

> [!def] 核心定义
> **因果关系（Causality / Causal Inference）** 指实证研究中通过严密的研究设计与统计分析，确立原因 $X$ 导致结果 $Y$ 发生的推理过程([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p. 56]])。在科学研究中，建立有效因果推断必须同时满足三大基石要件：(1) **统计关联性（[[Variable|变量]]间存在稳定的协变证据）**；(2) **时间先后序**（原因在时间上严格先于结果发生）；(3) **排除替代解释**（系统排除潜在混杂变量与虚假关联）([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, pp. 56–57]])。
>
> 在社会科学与教育研究中，因果关系通常体现为**[[Probabilistic Causation|概率因果性]]（即[[Independent Variable|自变量]] $X$ 提高了[[Dependent Variable|因变量]] $Y$ 发生的概率）**，其经验识别的底层逻辑依赖于**[[Counterfactual|反事实]]比较（Counterfactual Comparison）**——即对比干预实际发生的世界与[[Hypothesis|假设]]该干预未发生的反事实世界之间的状态差异([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 54–59]])。

> [!concept-lens] 概念透镜
> - **含义** 因果推断追问并回答“什么有效（What Works）”、“对谁有效（For Whom）”、“在什么情境下有效（Under What Conditions）”以及“通过何种机制产生效果（How/Why）”。
> - **用途** 为教育政策制定、教学方案选择与公共资源配置提供无偏的净收益信号，避免将偶然相关或虚假趋势误判为政策红利。
> - **边界** 因果推断不等于相关（相关可能由第三变量驱动）、不等于预测（基于错误因果识别的气压计仍可预测风暴）、不等于事后合理化解释；社会科学中的因果推断始终是概率性的证据累积，而非绝对的逻辑证明([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 58–59]])。

> [!citation-card]- 关键表述
> 因果性意味着我们预期变量 X 会导致变量 Y。[[Internal Validity|内部效度]]，即干预与结果之间因果关系的有效程度，是实验设计的[[Necessary and Sufficient Conditions|必要条件]]。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, p. 56)]]; [[Argument_Hitchcock_2015_JBE|(Hitchcock et al., 2015, p. 461)]]
>
> *Causality means that we would expect variable X to cause variable Y. Establishing causal evidence requires demonstrating empirical association, temporal precedence, and the elimination of plausible rival explanations.*

> [!boundary]- 概念边界
> - 不等于 **经验相关（Correlation / Association）** — 关联是因果成立的必要非充分条件；红酒消费与心脏病发病率降低相关，但二者可能共同由更高的社会经济地位（SES）驱动([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p. 57]])。
> - 不等于 **统计预测（Prediction）** — 气压计指针骤降能准确预测暴风雨来临，但拨动气压计指针绝不会产生暴风雨。
> - 不等于 **[[Causal Over-determination|因果过度决定]]（Causal Over-determination）** — 当多个原因中每一个都足以单独产生结果时（如学生成绩提升同时受到[[Homework|家庭作业]]、家长重压和高额辅导刺激），单一归因存在逻辑缺陷([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 63–64]])。

---

## 概念辨析

> [!contrast-table] 因果关系四重刻画取向对比
> | 比较维度 | 决定论因果 (Deterministic) | 概率因果 (Probabilistic) | [[Counterfactual\|反事实]]潜在结果模型 (Counterfactual) | 机制生成论因果 (Generative) |
> |:---|:---|:---|:---|:---|
> | **核心本体主张** | 若 $X$ 发生，则 $Y$ 必然发生（$100\%$ 必然性） | $X$ 的出现系统性提高 $Y$ 发生的概率 | 因果效应为个体接受处理与未接受处理的潜在结果之差 | 因果是行动者在特定情境脉络下通过能动性转化的动态过程 |
> | **代表传统与学者** | 经典物理学、休谟恒常联结 | Suppes (1970), Mellor (1995) | Neyman (1923), Rubin (1974), Holland (1986) | Salmon (1998), Pawson & Tilley (1997), Morrison (2009) |
> | **核心推断挑战** | 无法容纳社会系统的随机扰动与复杂互动 | 统计关联可能受隐性混杂[[Variable\|变量]]污染 | 因果推断基本问题（单一个体反事实不可直接观测） | 质性叙事的[[Multiplicity\|多重性]]（[[Rashomon Effect\|罗生门效应]]）与主观意图黑箱 |
> | **主要应对方法** | 封闭实验室极限控制 | [[Multiple Regression\|多元回归]]、倾向得分匹配（PSM） | [[Randomised Controlled Trials\|随机对照试验]]（RCT）、工具变量（IV）、断点回归（RDD） | 质性过程追踪、[[Realist Evaluation\|现实主义评估]]、[[Action Narratives\|行动叙事]] |

---

## 核心要素

> [!feature] 因果推断的五大核心要素
> - **时间优先序（Temporal Precedence）** [[Independent Variable|自变量]] $X$ 的施加必须在时间轴上严格先于[[Dependent Variable|因变量]] $Y$ 的变动，防范反向因果（Reverse Causality）([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p. 57]])。
> - **[[Counterfactual|反事实]]基准构建（Counterfactual Benchmark）** 解决“因果推断基本问题（Holland, 1986）”——通过[[Random Assignment|随机化]]（[[Randomised Controlled Trials|RCT]]）或[[Quasi-Experimental Designs|准实验设计]]（QED/[[Regression Discontinuity Design|RDD]]）构建出在期望上完全可比的反事实控制组。
> - **[[Screening Off|筛选隔离]]与混杂控制（Screening Off & Confounder Control）** 基于 Reichenbach-Salmon 原理，通过实验物理隔离或统计控制（偏相关、结构方程模型），切断共同原因导致的伪相关([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 59–60]])。
> - **因果识别设计层级（Causal Design Hierarchy）** 依据[[Internal Validity|内部效度]]控制强度，将实证设计划分为 0–3 级严密阶梯（RCT/RDD 为 3 级，严谨 QED 为 2–3 级，单组前[[Pre-test and Post-test|后测]]为 0 级）([[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, p. 8]])。
> - **因果机制与情境条件（Mechanisms & Contextual Conditions）** 识别[[Compound Causes|复合原因]]（Compound Causes）与[[Interaction Effect|交互效应]]，解释干预在特定生态情境中赖以起效的中介机制。

> [!framework-table] 循证政策中的因果识别设计分级（基于 Wadhwa et al., 2024; WWC Standards v5.0）
> | 因果推断强度等级 | 典型研究设计类型 | [[Threats to Internal Validity\|内部效度威胁]]控制机制 | 清算中心准入待遇（[[What Works Clearinghouse\|WWC]] / [[Blueprints for Healthy Youth Development\|Blueprints]] / [[Home Visiting Evidence of Effectiveness\|HomVEE]]） |
> |:---|:---|:---|:---|
> | **3 级（强因果推断）** | **随机对照试验（RCT）**<br>**断点回归（RDD）** | 随机分配使两组在可测与不可测[[Variable\|变量]]上均等价；断点局域随机化控制连续混杂 | 无保留达标（Meets Standards Without Reservations）；可作为最高评级（Model / [[Top Institute for Evidence-Based Education Research\|TIER]] 1）证据 |
> | **2 级（中度因果推断）** | **严谨准实验设计（QED）**<br>**间断时间序列（ITS）** | 建立基线等值性（Baseline Equivalence，差值 $< 0.05\text{ SD}$）；多时间点追踪排除历史与成熟威胁 | 有保留达标（Meets Standards With Reservations）；满足联邦 Tier 2 标准 |
> | **1 级（弱因果推断）** | **匹配不良的比较组研究**<br>**事后回溯相关研究** | 仅控制部分可观察协变量，存在严重的不可测选择偏倚（Selection Bias） | 通常判定为不达标（Does Not Meet Standards）；仅能作为初步探索线索 |
> | **0 级（无效因果推断）** | **单组前后测设计（Pre-Post）**<br>**事后单次调查** | 无法分离自变量与自然成熟、历史事件、均值回归的混杂 | 完全被所有权威清算中心排除，不承认为因果证据 |

> [!formula-step] 前后测控制组真实验的平均因果[[Effect Size|效应量]]化
> 在[[Pretest-Posttest Control Group Design|前后测控制组设计]]（Pretest-Posttest Control Group Design）中，平均因果效应量化模型为([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch. 16, p. 314]])：
>
> $$\text{平均因果效应（ATE）} = (E_1 - E_2) - (C_1 - C_2)$$
>
> - **数学含义** $E_1, E_2$ 分别为实验组后测与前测分值；$C_1, C_2$ 分别为控制组后测与前测分值。$(E_1 - E_2)$ 包含“干预净效应 + 自然成熟 + 历史变动”，$(C_1 - C_2)$ 包含“纯自然成熟 + 历史变动”；二者双重差分相减，剥离出纯净的因果效应。
> - **成立前提** 依赖于**其他条件不变假定（Ceteris Paribus）**；随机分配（Random Assignment）通过大数定律保证了两组在期望上的完全等价性。

> [!logic-map]- 从相关到因果识别的逻辑判定流
> ```mermaid
> flowchart TD
>     A["观察到变量 X 与 Y 存在统计相关"] --> B{"时间先后顺序检验"}
>     B -->|X 不先于 Y| C["排除因果关系与反向因果"]
>     B -->|X 先于 Y| D{"混杂变量排除检验 Screening Off"}
>     D -->|存在未控制共同原因| E["伪相关 Spurious Correlation"]
>     D -->|成功排除混杂| F{"反事实控制设计"}
>     F -->|随机分配 RCT| G["强因果推断·内部效度最高"]
>     F -->|准实验基线等值 QED| H["中度因果推断·条件内部效度"]
>     F -->|无对照单组前后测| I["因果推断失败·混入成熟与历史"]
> ```

---

## 围绕概念形成的命题

---

### 命题一　因果推断的底层基石是不可直接观测的反事实比较

> [!concept-lens] [[Counterfactual|反事实]]潜在结果模型
> 因果推断的核心任务在于回答“如果干预未发生，结果会怎样”。

> [!claim] [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen, Manion, & Morrison (2011)]]
> **因果推断基本问题与实验[[Operationalization|操作化]]回答** 依据 Holland (1986) 确立的“因果推断基本问题”，同一个体无法同时处于接受干预与未接受干预的状态，因此个体反事实永远无法直接观测。实验设计通过[[Random Assignment|随机化]]构建控制组，用控制组的平均潜在结果作为实验组反事实的无偏替代，从而在群体均值层面实现平均因果效应（ATE）的无偏估计。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|(Cohen et al., 2011, pp. 55–56)]]; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch. 16, p. 314)]]

---

### 命题二　社会科学中的因果关系呈现为概率性、条件性与复合因果组合

> [!concept-lens] [[Compound Causes|复合原因]]与[[Interaction Effect|交互效应]]
> 单纯断言“X 导致 Y”在社会复杂系统中往往是不充分的，因果效力高度依赖必要与[[Necessary and Sufficient Conditions|充分条件]]的特定组合。

> [!claim] [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al. (2011)]]
> **复合原因与[[Causal Over-determination|因果过度决定]]** 单一原因很少能够单独产生社会效应。原因通常需要组合在一起形成**复合原因（Compound Causes）**并发生交互作用（Interaction Effects）。在因果过度决定（Causal Over-determination）情境下，多个原因中每一个都可能单独产生效果，研究者必须通过[[Factorial Design|析因设计]]与机制追踪防范过度简化的单一归因。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|(Cohen et al., 2011, pp. 56–57, 63–64)]]

---

### 命题三　前向干预实验与后向机制追溯构成因果识别的互补双翼

> [!concept-lens] 两种因果研究策略
> 量化实验回答“原因之效果”，质性过程追踪回答“效果之原因”。

> [!claim] [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022)]]; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al. (2011)]]
> **前向操纵与后向追溯的互补性** 量化实验通过前向施加干预来估计原因的平均效果大小；[[Qualitative Research|质性研究]]（[[Ethnography|民族志]]、[[Action Narratives|行动叙事]]）则通过后向追溯深入行动者头脑，揭示因果链条中的动机、理解与情境互动机制。两者的结合能同时回答因果关系的“发生与否（Whether）”与“如何发生（How）”。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, pp. 56–58)]]; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|(Cohen et al., 2011, pp. 74–92)]]

---

### 命题四　单项研究内部因果确证不能自动等同于跨情境稳健的因果效能

> [!concept-lens] 循证清算与因果综合门槛
> 从微观单项实验的因果识别到宏观政策采纳，必须跨越证据综合与[[Construct Validity|构念效度]]的双重门槛。

> [!claim] [[Argument_Hitchcock_2015_JBE|Hitchcock et al. (2015)]]; [[Argument_Wadhwa_2024_RER|Wadhwa, Zheng, & Cook (2024)]]
> **因果有效性的综合门槛割裂** [[Internal Validity|内部效度]]达标是因果推断成立的必要条件，但并非宏观认证的充分条件。Wadhwa 等人揭示，由于不同清算机构在**[[Evaluator Independence|独立评估者]]复制**、**12 个月[[Fade-out Effect|持续效果]]**及**[[Iatrogenic Effects in Education|医源性伤害]]排除**等综合门槛上的分歧，单项高质量 [[Randomised Controlled Trials|RCT]] 的因果结论在跨机构综合评级中表现出高达 35.4% 的极端冲突，要求政策制定者穿透评级标签审视底层因果证据。[[Argument_Hitchcock_2015_JBE|(Hitchcock et al., 2015, pp. 461–462)]]; [[Argument_Wadhwa_2024_RER|(Wadhwa et al., 2024, pp. 4, 26)]]

---

### 命题总览

> [!contrast-table] 因果推断核心命题总览
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |:---|:---|:---|:---|
> | **反事实基准命题** | 因果效应本质是潜在结果差，依赖构建反事实控制组 | RCT、[[Quasi-Experimental Designs\|QED]]、RDD 因果评估 | Holland (1986); [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04\|Cohen et al. (2011)]] |
> | **概率复合因果命题** | 社会因果呈现概率性，依赖复合条件与交互作用 | 复杂干预评估、析因实验设计 | Mellor (1995); 复合因果研究组 |
> | **双向互补推断命题** | 前向实验（测效果）与后向追溯（明机制）深度融合 | [[Mixed Methods Research\|混合方法研究]]、[[Realist Evaluation\|现实主义评估]] | [[Argument_Creswell_2022_SAGE\|Creswell & Creswell (2022)]]; Morrison (2009) |
> | **效能综合门槛命题** | 单项因果识别不等于跨平台稳健，需经受复制门槛检验 | 循证清算中心、政策认证决策 | [[Argument_Hitchcock_2015_JBE\|Hitchcock et al. (2015)]]; [[Argument_Wadhwa_2024_RER\|Wadhwa et al. (2024)]] |

---

## 概念演变

> [!dev-timeline] 因果关系与因果推断理论演进
> - **18 世纪 — 休谟归纳因果四准则** 大卫·休谟提出时空邻近、时间优先、恒常联结与必然联系，指出因果关系源于人类的经验归纳而非绝对先验演绎。
> - **1956 — [[Screening Off|筛选隔离]]原理提出** Hans Reichenbach 提出筛选隔离（Screening Off）概念，为用统计控制排除共同原因混杂奠定理论基础。
> - **1974–1986 — 潜在结果模型与[[Counterfactual|反事实]]革命** Donald Rubin 与 Paul Holland 建立[[Potential Outcomes Framework|潜在结果框架]]，提出“因果推断基本问题”，奠定当代计量经济学与实验因果推断的数理基石。
> - **1990 年代 — 因果图模型与有向无环图** Judea Pearl 创立因果图（DAGs）与 do-calculus 演算体系，形式化了因果识别中的混杂路径切断规则。
> - **2002–2015 — 联邦循证门控标准确立** Shadish et al. (2002) 体系化[[Internal Validity|内部效度]]；IES/[[What Works Clearinghouse|WWC]] 正式建立以内部效度为先导的因果审查门控程序（[[Gating Procedure]]）([[Argument_Hitchcock_2015_JBE|Hitchcock et al., 2015, pp. 461–467]])。
> - **2024 — 清算体系因果综合反思** Wadhwa, Zheng & Cook 全景检验 10 所清算中心 1,359 个项目，实证揭示各机构在单项因果识别与跨研究综合门槛上的割裂，推动因果推断从“微观实验识别”走向“宏观证据生态审思”([[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, pp. 3–5, 26–30]])。

---

## 在研究与评估中的操作

> [!proc] 建立严谨因果推断的六步规程
> 1. **明确界定因果识别问题** 清晰界定干预[[Variable|变量]] $X$ 的具体成分与目标[[Dependent Variable|结果变量]] $Y$，锁定目标推断人群。
> 2. **选择高等级因果设计** 优先选用[[Randomised Controlled Trials|随机对照试验]]（RCT）或严谨准实验（[[Regression Discontinuity Design|RDD]]/[[Quasi-Experimental Designs|QED]]/[[Single-Case Design|SCD]]），在设计阶段阻断选择偏倚。
> 3. **核查基线等值性与[[Attrition|流失]]边界** 严格检验对照组基线等值性（差值 $< 0.05\text{ SD}$），套用 WWC 流失模型排查样本流失偏倚风险([[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, p. 8]])。
> 4. **规范实施[[Intent-to-Treat Analysis|意向治疗分析]]（ITT）** 保留所有[[Random Assignment|随机化]]入组样本，防范处理依从性（Compliance）选择偏倚对因果识别的破坏。
> 5. **开展敏感性与多重[[Hypothesis|假设]]校正** 针对多重比较实施 Benjamini-Hochberg 校正，开展混杂敏感性分析检验因果结论的稳健性。
> 6. **结合质性过程追踪** 嵌入[[Action Narratives|行动叙事]]与[[Implementation Fidelity|实施忠实度]]监控，打开因果起效的微观机制黑箱([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 71–74]])。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 纯净因果控制 vs 现实生态复杂性
> > 争论过于追求封闭环境中的高[[Internal Validity|内部效度]]控制，是否会牺牲干预在常规学校与复杂课堂中的真实生命力。
> >
> > - **实验方法学派** 坚守内部效度优先原则，强调因果关系不清的研究无法提供任何有效实践指导([[Argument_Hitchcock_2015_JBE|Hitchcock et al., 2015, p. 461]])。
> > - **复杂系统学派** 批评社会系统具有开放性与[[Emergence|涌现]]性（Emergence），过度隔离混杂可能脱离真实情境脉络([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch. 16, p. 319]])。
>
> > [!axis] 平均处理效应（ATE） vs [[Heterogeneity|异质性]]因果效应（HTE）
> > 争论宏观平均[[Effect Size|效应量]]是否会掩盖弱势群体中的差异化因果反应（如高能力与低能力学生的完全相反表现）。

> [!critique] 常见因果推断误用
> - **把相关性直接解读为因果结论** 在回归模型中控制若干[[Variable|变量]]后便轻率得出“政策导致提分”的结论。
> - **以单组前[[Pre-test and Post-test|后测]]声称因果成效** 忽略时间推移带来的自然成熟与均值回归假象。
> - **混淆局部处理效应（LATE）与全局平均效应（ATE）** 将[[Regression Discontinuity Design|断点回归]]或工具变量识别出的局域因果效应盲目推广至全样本。

---

## 实证数据

> [!ref-table]- 因果推断核心实证与方法学案例
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究与案例 | 案例情境与对象 | 因果设计类型 | 核心因果机制与[[Variable\|变量]] | 关键结论与启示 | 解释边界 |
> |:---|:---|:---|:---|:---|:---|
> | [[Argument_Wadhwa_2024_RER\|Wadhwa et al. (2024)]] | 10 个清算中心审查的 1,359 个去重教育项目 | 因果设计分级与跨平台综合评级 | 因果识别设计（[[Randomised Controlled Trials\|RCT]]/[[Quasi-Experimental Designs\|QED]]/RDD）与综合门槛 | 证明单项研究的因果识别（[[Internal Validity\|内部效度]]）不等于宏观评级收敛；35.4% 的极端评级冲突源于独立复制与随访门槛差异 | 宏观清算体系元评估 |
> | [[Argument_Hitchcock_2015_JBE\|Hitchcock et al. (2015)]] | [[What Works Clearinghouse\|WWC]] [[Single-Subject Design\|单一被试设计]]（[[Single-Case Design\|SCD]]）审查标准 | [[ABAB Design\|ABAB 设计]]与多基线设计 (SCD) | 阶段撤回与多基线阶梯式介入 | 证明 SCD 凭借密集的阶段内重复测量与阶段间对比，与组间 RCT 共享相同的排除成熟/历史替代解释逻辑 | 单一个案因果推断 |
> | [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04\|Cohen et al. (2011)]] | 阅读时间增加与阅读能力提升案例 | 机制展开与过程追踪 | 阅读动机、专注度、文本难度、教师支架 | 证明单一输入变量并非简单因果，背后包含至少 18 个微观维度的动态交互与能动性转化过程 | 复杂[[Causal Processes\|因果过程]]模型 |
> | [[Compound Causes\|复合原因]]哲学案例 (Morrison, 2009) | 冰面摔倒骨折经典案例 | [[Necessary and Sufficient Conditions\|必要条件]]与充分条件析因 | 冰面、视力不佳、鞋底光滑、平衡感差、骨质疏松 | 证明冰面仅为贡献原因之一，需与其他条件结合构成充分条件组合，揭示复合原因本质 | 哲学因果分析 |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen, Manion, & Morrison (2011)]] — 系统构建教育研究因果推断全景，详述概率因果、[[Counterfactual|反事实]]、[[Screening Off|筛选隔离]]、[[Causal Over-determination|因果过度决定]]及真实验前[[Pre-test and Post-test|后测]]双重差分效应模型（Ch. 4 / Ch. 16）。
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022)]] — 明确量化因果推断三要件（关联证据、时间顺序、排除替代解释）及[[Causal Modeling|因果建模]]路径。
> - [[Argument_Hitchcock_2015_JBE|Hitchcock et al. (2015)]] — 论证单一被试实验（[[Single-Case Design|SCD]]）与组间实验的因果推断同构性及[[Internal Validity|内部效度]]门控机制。
> - [[Argument_Wadhwa_2024_RER|Wadhwa, Zheng, & Cook (2024)]] — 建立清算中心 0–3 级因果识别设计分级标准，揭示微观因果证据向宏观政策[[Transfer Translation Transformation|转译]]时的综合门槛割裂。
