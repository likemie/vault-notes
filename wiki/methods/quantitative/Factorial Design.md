---
title: Factorial Design
aliases:
  - 因子设计
  - 析因设计
  - factorial experiment
  - 2x2 factorial design
  - 析因实验
  - factorial trial
summary: "同时操纵两个或多个自变量以检验主效应与交互效应的实验设计；在第二代循证试验中用于解构复杂干预组件并检验条件性因果关系。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 39
method_related_level: 4
method_related_stars: "⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental
  - quantitative-research
  - design-type
related_concepts:
  - "[[Independent Variable]]"
  - "[[Variable]]"
  - "[[Interaction Effect]]"
  - "[[Causality]]"
  - "[[Evidence-Based Education]]"
  - "[[Unit of Analysis]]"
  - "[[Hypothesis]]"
  - "[[Implementation Fidelity]]"
  - "[[Dependent Variable]]"
  - "[[Business as Usual]]"
  - "[[Type I and Type II Errors]]"
  - "[[Learner Autonomy]]"
  - "[[Paradigm]]"
  - "[[Realism in International Relations]]"
related_theories:
  - "[[Realist Evaluation]]"
  - "[[Theory of Change]]"
related_methods:
  - "[[Experimental Research]]"
  - "[[Multi-Arm Trial]]"
  - "[[Random Assignment]]"
  - "[[Effect Size]]"
  - "[[Confidence Interval]]"
  - "[[Cluster Randomized Trials]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Pre-test and Post-test]]"
  - "[[Analysis of Variance]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Implementation and Process Evaluation]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Standard Error]]"
  - "[[Sample Size Determination]]"
  - "[[True Experimental Design]]"
  - "[[Solomon Four-Group Design]]"
  - "[[Correlational Research]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
related_facts:
  - "[[Literacy Octopus]]"
  - "[[Education Endowment Foundation]]"
  - "[[Research Schools Network]]"
confidence: high
status: active
created: 2026-05-31
updated: 2026-09-17
---
# Factorial Design

## 定义

> [!def] 因子设计
> **因子设计（Factorial Design，亦称析因设计）**是[[Experimental Research|实验研究]]中同时操纵两个或多个[[Independent Variable|自变量]]（因子），以检验每个自[[Variable|变量]]的独立主效应（Main Effects）以及自变量之间[[Interaction Effect|交互效应]]（Interaction Effects）的高级实验设计类型（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。其命名基于因子数量与水平数——例如 $2 \times 2$ 因子设计表示两个自变量各包含两个水平，形成 4 种正交的处理组合。
>
> 因子设计在组织结构上通常表现为一种特化的[[Multi-Arm Trial|多臂试验]]（Multi-Arm Trial），但其核心方法学本质在于揭示**条件性[[Causality|因果关系]]**——即某一自变量的干预效应是否依赖于另一自变量（或环境背景）的特定水平（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 323–324]]）。在第二代[[Evidence-Based Education|循证教育]]与[[Realist Evaluation|现实主义试验]]中，析因设计与多臂试验构成了打破复杂干预“因果黑箱”的核心方法学利器，使得研究者能够系统解构多组分方案，分别及组合检验干预组件的离散效能与协同机制（Bonell et al., 2012；[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, pp. 53–54]]）。

> [!method-scope] 方法范围
> - **研究对象** 被[[Random Assignment|随机分配]]至各因子水平组合的个体受试者或集群单位（如学校、班级）。
> - **核心问题** 复合干预中各个独立组分的主效应为何？各组分间是否存在协同增益或相互抵消的交互效应？
> - **[[Unit of Analysis|分析单位]]** 个体参与者或集群学校/班级。
> - **输出形式** 各因子主效应检验、交互效应检验、多水平回归系数估计及[[Effect Size|效应量]][[Confidence Interval|置信区间]]。

---

## 方法定位

> [!method-position] 在实验设计中的独特位置
> - **超越单因子黑箱实验** 单因子实验只能回答“复合方案 X 是否有效”，无法辨析究竟是哪一个关键组件在起效；因子设计通过同时操纵多个独立组分，能在单一试验中同时检验多个因果[[Hypothesis|假设]]，具有极高的方法学经济性与诊断力。
> - **[[Realist Evaluation|现实主义试验]]的方法学载体** 现实主义评估强调情境与机制的[[Interaction Effect|交互作用]]；因子设计通过构建因子与微观情境的正交组合，成为验证“何种组件在何种条件下有效”的定量实验金标准。
> - **高阶交互的解释边界** 当因子数量达到三个或以上时（如 $2 \times 2 \times 2$），三向及更高阶交互效应的统计功效急剧下降，且在教育实践中往往难以赋予清晰的理论诠释。

> [!method-stack] 方法层级
> - **研究设计** 真实验或[[Cluster Randomized Trials|集群随机对照试验]]（Cluster [[Randomised Controlled Trials|RCT]]）——多因子正交交叉，[[Random Assignment|随机分配]]至各实验臂。
> - **数据收集** 独立基线与多阶段[[Pre-test and Post-test|后测]]数据，同步采集次要结局指标与过程[[Variable|变量]]。
> - **分析方法** 析因[[Analysis of Variance|方差分析]]（ANOVA）、多水平线性模型（[[Hierarchical Linear Model|HLM]]）及中介调节效应建模。
> - **辅助工具** 正交试验生成表、交互效应图（Interaction Plots）及[[Implementation Fidelity|实施保真度]]监测规程。

---

## 研究程序

> [!ref-table] 3 × 3 因子设计的[[Independent Variable|自变量]]与水平配置矩阵
> | 自[[Variable\|变量]] | 水平 1 | 水平 2 | 水平 3 |
> |---|---|---|---|
> | **资源可用性** | 有限（1） | 中等（2） | 高（3） |
> | **学习动机** | 低（4） | 中等（5） | 高（6） |

九种组合为两个自变量各水平的全交叉：1+4, 1+5, 1+6, 2+4, 2+5, 2+6, 3+4, 3+5, 3+6，共 9 个实验组。例如，可能发现有限资源+低动机对考试成绩有显著负面影响，而中等+高资源没有——因子设计的价值正在于揭示这类条件性效应（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 323–324]]）。

> [!proc] 实验室与基础实验的关键步骤
> 1. **确定自变量与水平数** 明确至少两个自变量，界定每个因子的具体水平与变量类型（被试间 vs 被试内）。
> 2. **实施[[Random Assignment|随机化]]分组** 运用随机数序列将受试者正交分配到各个实验条件组合中。
> 3. **采集[[Dependent Variable|因变量]]指标** 对经历不同处理组合的参与者统一实施标准化测量。
> 4. **检验主效应与[[Interaction Effect|交互效应]]** 运行[[Analysis of Variance|方差分析]]检验各因子独立效应及其交互项。
> 5. **绘制交互图示与[[Effect Size|效应量]]评估** 绘制边际均值走向图，报告各效应量及[[Confidence Interval|置信区间]]（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。

> [!proc] 复杂教育干预的多臂析因现场试验实施流程
> 1. **[[Theory of Change|变革理论]]要素解构** 基于因果理论模型，将复合教育干预拆解为独立的[[Hypothesis|假设]]驱动因子（如因子 A：技术软件自学；因子 B：教师面对面主导辅导）。
> 2. **构建正交多臂分配矩阵** 设立 $2 \times 2$ 实验臂（A处理、B处理、A+B组合处理、[[Business as Usual|常态教学]]对照组），在[[Cluster Randomized Trials|集群随机对照试验]]中分配学校或班级。
> 3. **嵌入[[Implementation and Process Evaluation|实施与过程评估]]（IPE）** 对各实验臂的[[Implementation Fidelity|实施保真度]]（Fidelity）、师生顺应度与常态对照基线活动进行同步定性追踪，严防组间交叉污染。
> 4. **主效应与交互效应多水平建模** 采用[[Hierarchical Linear Model|分层线性模型]]（HLM）控制学校集群效应，分别估计离散组件的净效应与组合交互效应。
> 5. **中介路径与机制验证** 引入中间机制度量，量化验证特定要素如何通过路径变量向终极学业产出传导（Bonell et al., 2012；[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, pp. 53–54]]）。

> [!def] [[Interaction Effect|交互效应]]
> 当两个或多个自变量同时作用于因变量时，一个自变量的效应**依赖于**另一个自变量的水平。以性别 × 年龄对数学学习动机的影响为例：男女之间的动机差异不是恒定的，而是随年龄发生非线性变化。因子设计特别适合检验此类条件依存性，这是其区别于单因子实验的决定性优势（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 324]]）。

---

## 资料与分析

> [!info] 方差分解与多水平析因建模
> 因子设计的统计分析核心是总方差的正交分解——总变异被分解为各因子主效应平方和、因子间[[Interaction Effect|交互效应]]平方和以及组内误差平方和。
> - **交互效应的图示诊断** 边际均值图中的线条不平行是存在交互效应的重要视觉指征。若交叉项显著，主效应的解释必须进行条件限制——不能断言“干预 A 有效”，而应准确表述为“干预 A 的成效取决于干预 B 是否同步实施”。
> - **现场试验的多水平校正** 在以学校为单位开展的多臂现场试验中，个体嵌套于班级和学校，必须采用[[Hierarchical Linear Model|多水平模型]]（HLM）校正[[Intraclass Correlation Coefficient|群内相关系数]]（ICC），避免[[Standard Error|标准误]]低估造成[[Type I and Type II Errors|第一类错误]]（伪显著）。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 理论上预期干预组件之间存在协同或拮抗作用时；需要拆解多组分复合政策以评估各模块真实贡献时；希望在单一试验中检验因果机制随微观生态情境的变异时。
> - **谨慎使用** 因子超过 3 个或单因子水平超过 4 个时——处理组合数与集群[[Sample Size Determination|样本量]]需求呈指数级增长；高阶交互在实践中难以解释。
> - **不适合使用** 仅关注单一干预策略的总体宏观效果，或试验资源与样本规模无法支持多臂正交分配时。

---

## 局限性

> [!method-limits] 局限与方法学挑战
> - **[[Sample Size Determination|样本量]]需求的指数增长** 因子数量与水平的增加导致实验组数成倍扩散（$2 \times 2 = 4$ 组；$3 \times 3 = 9$ 组；$2 \times 3 \times 4 = 24$ 组），维持足够的统计功效需要招募极为庞大的学校集群，实地后勤协调与财务成本高昂。
> - **现场交叉污染风险加剧** 在常态学校环境中，设置多个不同处理臂容易导致相邻班级或教师之间的非正式经验交流与材料借阅，削弱各实验臂之间的独立性对比。
> - **高阶交互的解释困局** 统计上显著的三向或四向[[Interaction Effect|交互效应]]，在复杂的教育与心理实践中往往难以赋予逻辑自洽的教育学解释。

---

## 典型案例

> [!case] 复杂干预组件剥离：从单维度黑箱走向多臂析因现场试验（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, pp. 53–54]]）
> - **案例一：“[[Literacy Octopus|识字八爪鱼]]”[[Multi-Arm Trial|多臂试验]]（Literacy Octopus Trial）** 英国[[Education Endowment Foundation|教育捐赠基金会]]（EEF）动员全英 800 余所小学开展多臂试验（Lord et al., 2017），设置多个正交实验臂系统比对了 4 种证据传播与教学支持策略（涵盖被动邮件与资料寄送、主动研讨会培训以及专家入校深度辅导）。试验最终证实，单向被动寄送循证材料对学生成绩的净效应完全为零，有力推翻了“只要把研究报告寄到学校就能改善教学”的经验[[Hypothesis|假设]]，倒逼英格兰重构基于人际互动与校际协作的[[Research Schools Network|研究学校网络]]。
> - **案例二：ABRA 在线阅读支持多臂析因试验** 在 ABRA 数字化阅读干预试验中（McNally et al., 2018），评估团队采用析因逻辑系统剥离了“教育软件[[Learner Autonomy|自主学习]]”与“教师面对面辅导”两个核心要素，分别检验了单一软件处理、单一教师辅导以及两者结合的离散成效，精准揭示了技术工具必须与教师专业支架深度协同方能释放因果效能的交互机制。

---

## 相关理论与方法

> [!entry-map]
> 
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[True Experimental Design]] | 方法体系 | 因子设计是真实验与集群 [[Randomised Controlled Trials\|RCT]] 的高级变体。 |
> | [[Multi-Arm Trial]] | 组织形式 | 因子设计在实验臂架构上所属的广义多臂试验大类，因子设计为其特化的正交交叉形态。 |
> | [[Interaction Effect]] | 核心概念 | 因子设计的最核心检验对象就是因子间的条件性交互效应。 |
> | [[Realist Evaluation]] | 理论[[Paradigm\|范式]] | [[Realism in International Relations\|现实主义]]试验的核心操作工具，通过析因设计检验组件独立效应与情境交互。 |
> | [[Implementation and Process Evaluation]] | 互补方法 | 过程评估用于监测析因各实验臂的现场[[Implementation Fidelity\|实施保真度]]，防止组间交叉污染。 |
> | [[Solomon Four-Group Design]] | 特殊案例 | 所罗门四组设计本质上是处理因素 × 前测因素的 $2 \times 2$ 因子设计。 |
> | [[Analysis of Variance]] | 统计工具 | 方差分析与方差分解是因子设计标准的数据分析与[[Hypothesis\|假设]]检验方法。 |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 探讨多臂与析因设计在全英大规模复杂教育干预评估中的机制剥离价值，援引“[[Literacy Octopus|识字八爪鱼]]”[[Multi-Arm Trial|多臂试验]]与 ABRA 在线阅读试验。
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022, Ch8)]] — 以 $2 \times 4$ 混合因子设计为例，系统示范因子间主效应与[[Interaction Effect|交互效应]]的统计检验程序。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011, Ch16)]] — 系统阐释 $3 \times 3$ 因子设计的正交组合逻辑，并结合交互效应图示示范条件性[[Causality|因果推断]]。

