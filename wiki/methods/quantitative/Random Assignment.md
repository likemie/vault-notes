---
title: Random Assignment
aliases:
  - 随机分配
  - 随机分组
  - randomisation
  - randomized assignment
  - 随机化
  - randomization
summary: "将受试对象按概率均等原则分派至不同实验处理条件中的核心技术，通过消除组间系统性偏差确立因果推断的内部效度；在当代教育与社会科学中面临开放系统与能动性反思，在现代科学学（Metascience）中进一步被拓展为评估科研资助机制与实施部分抽签资助的制度实验工具。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 49
method_related_level: 5
method_related_stars: "⭐⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental
  - quantitative-research
  - causal-inference
  - theme/metascience
related_concepts:
  - "[[Causality]]"
  - "[[Internal Validity]]"
  - "[[Counterfactual]]"
  - "[[Unit of Analysis]]"
  - "[[Fundamental Problem of Causal Inference]]"
  - "[[Metascience]]"
  - "[[Epistemology]]"
  - "[[Positivism]]"
  - "[[Empiricism]]"
  - "[[Variable]]"
  - "[[Reliability]]"
  - "[[External Validity]]"
  - "[[Independent Variable]]"
  - "[[Business as Usual]]"
  - "[[Attrition]]"
  - "[[Study Population and Sample]]"
  - "[[Research Ethics]]"
  - "[[Open-Mindedness]]"
  - "[[Comparative Education as a Cross-Sectional Area]]"
related_theories:
  - "[[Critical Realism]]"
related_methods:
  - "[[Experimental Research]]"
  - "[[Effect Size]]"
  - "[[Quantitative Research]]"
  - "[[True Experimental Design]]"
  - "[[Pre-test and Post-test]]"
  - "[[Posttest-Only Control Group Design]]"
  - "[[Questionnaire]]"
  - "[[Analysis of Variance]]"
  - "[[Analysis of Covariance]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Blinding]]"
  - "[[Baseline Standardized Mean Difference]]"
  - "[[Confidence Interval]]"
  - "[[Random Sampling]]"
  - "[[Propensity Score Matching]]"
  - "[[Matching]]"
  - "[[Sample Size Determination]]"
  - "[[Case Study]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Mechanism Experiments]]"
related_persons:
  - "[[Michael Kratsios]]"
related_facts:
  - "[[United Kingdom Metascience Unit]]"
  - "[[Office of Science and Technology Policy]]"
  - "[[Education Endowment Foundation]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Kratsios_2026_OSTP]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10]]"
  - "[[Argument_Wrigley_2018_BERJ]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge]]"
confidence: high
status: active
created: '2026-05-31'
updated: 2026-10-07
---

# Random Assignment

---

## 定义

> [!def] 方法定义
> 随机分配（Random Assignment，亦称随机分组或随机化）是[[Experimental Research|实验研究]]中将受试对象按已知且非零的概率均等原则分派至不同实验处理条件（如干预组与对照组）的核心技术。其核心功能在于使各组受试对象在所有已知与未知的基线特征上达到期望等价，从而消除选择偏误（Selection Bias），为确立[[Causality|因果推断]]（Causal Inference）与估计干预净效应奠定最强[[Internal Validity|内部效度]]基石。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch. 8)]]; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch. 16, p. 313)]]

> [!method-scope] 方法范围
> - **研究对象** 被随机分派到不同实验处理条件中的受试者个体（如学生、患者）、集群单位（如学校、班级）以及科研资助项目提案（在科学学中）。
> - **问题类型** 因果识别、[[Counterfactual|反事实]]净效应估计以及资助分配机制的噪声控制。
> - **[[Unit of Analysis|分析单位]]** 个体、组织集群、科研基金申请书。
> - **输出形式** 组间基线平衡性检验统计量、干预后标准化[[Effect Size|效应量]]（Effect Size, ES）及无偏因果推断结论。

> [!citation-card] 真实验的核心判准与反事实等价
> 当个体被随机分配到组别中时，该程序被称为真实验。随机化是对因果推断基本问题的统计解决方案——一个人不能同时处于实验组和控制组，但随机化使两组在期望上等价，从而用控制组平均结果替代实验组的[[Counterfactual|反事实]]结果。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch. 8)]]; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch. 16, p. 313)]]
>
> *When individuals are randomly assigned to groups, the procedure is called a true experiment... Randomization provides a statistical solution to the [[Fundamental Problem of Causal Inference]] by creating counterfactual equivalence.*

> [!citation-card] 科学学中资助分配的部分随机化实验
> 在科学资助领域，随机分配正演化为克服同行评议偏误的新型治理工具。[[United Kingdom Metascience Unit|英国元科学单元]]（UK [[Metascience]] Unit）与白宫科技政策办公室（[[Office of Science and Technology Policy|OSTP]]）推动在达到基本资助门槛的提案中实施‘部分随机化（Partial Randomization / Lotteries）’，以科学实验检验抽签分配能否有效打破共识评审对非共识、高风险颠覆性创新的系统性歧视。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, p. 32)]]
>
> *In metascience, partial randomization is tested as an empirical funding mechanism to overcome reviewer noise and support high-variance, non-consensus breakthroughs.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 基于[[Positivism|实证主义]]与[[Empiricism|经验主义]]因果观。假定通过控制和消除混杂[[Variable|变量]]，可以直接从因果事件的恒常规则性推导出[[Causality|因果关系]]。Cohen 等（2011）将样本随机化列为[[Quantitative Research|量化研究]]效度的实证主义前提之一。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, pp. 158–159)]]
> - **在因果推断中的角色** 随机分配使两组在期望上等价，将组间任何后续差异无偏归因于干预操作（*ceteris paribus* 假定）。
> - **研究者角色** 客观中立的实验操控者与观察者，依托算法生成序列排除主观选择偏好。
> - **有效性标准** [[Internal Validity|内部效度]]优先。高[[Reliability|信度]]的随机分配能最大限度排除选择偏误，但不能自动保证在复杂开放系统中的[[External Validity|外部效度]]。
> - **不声称观察的问题** 无法直接揭示干预“为什么”起作用的深层微观机制，亦无法消除受试者能动性（Agency）在非双盲情境下的交互干扰。[[Argument_Wrigley_2018_BERJ|(Wrigley, 2018, pp. 6, 8)]]

> [!method-stack] 方法层级
> - **研究设计** [[True Experimental Design|真实验设计]]（如[[Pre-test and Post-test|前测]]-后测对照组设计、[[Posttest-Only Control Group Design|仅后测对照组设计]]、集群随机化设计 CRT）。
> - **数据收集** 前后测标准化测验、[[Questionnaire|问卷]]量表、行政数据、基金评审得分记录。
> - **分析方法** 组间独立样本 t 检验、[[Analysis of Variance|方差分析]]（ANOVA）、[[Analysis of Covariance|协方差分析]]（ANCOVA）、[[Hierarchical Linear Model|多水平模型]]（HLM）及 Hedges' g [[Effect Size|效应量]]计算。
> - **辅助技术** 伪随机数发生器、分层随机化（Stratified Randomisation）、区组随机化（Block Randomisation）、最小化法（Minimisation）。

---

## 研究程序

> [!proc] 通用操作程序
> 1. **确定实验处理条件** 界定[[Independent Variable|自变量]]的各个水平（如干预组 vs [[Business as Usual|常规对照组]]；或传统同行评议组 vs 随机化抽签资助组）。
> 2. **生成随机分配序列** 使用计算机算法或随机数表，为每个进入实验的受试单位生成概率均等的分配序列并做好分配隐蔽（Allocation Concealment）。
> 3. **隐蔽分配与实施入组** 确保分配序列对执行人员隐蔽（必要时实施[[Blinding|盲法]]），将受试对象依次分派入组。
> 4. **基线平衡检验（[[Baseline Standardized Mean Difference|Baseline Equivalence]] Test）** 在干预前比对处理组与对照组的[[Pre-test and Post-test|前测]]得分及核心协[[Variable|变量]]，检验随机化是否成功消除组间系统性偏差。
> 5. **后测与因果净效应估计** 收集后测结果数据，严格核查[[Attrition|样本流失]]率，计算并报告[[Effect Size|效应量]]（ES）与[[Confidence Interval|置信区间]]。

> [!stat-cards] 随机分配的概率等价演示（改编自 Pilliner, 1973）
> - **纸牌模拟实验** 从一副牌中选 20 张（10 红 10 黑），洗牌后随机分成两堆各 10 张，记录红黑牌分布。
> - **理论概率分布**
>   - 最可能的结果：每堆各 5 红 5 黑；
>   - 出现“一堆全红、一堆全黑”极端失衡的概率仅为 **1/92,378**；
>   - 获得“每堆不超过 6 张同色”良好混合结果的概率约为 **82%**。
> - **科学推论** 仅凭机会法则，随机分配几乎总能在两组间实现未知特征的近似等价混合，这正是其排除混杂的统计力量。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch. 16, pp. 318–319)]]

---

## 辨析与对比

> [!contrast-table] 随机分配 vs [[Random Sampling|随机抽样]] vs [[Propensity Score Matching|倾向得分匹配]]
> | 维度 | 随机分配（Random Assignment） | 随机抽样（Random Sampling） | 匹配（[[Matching]]） |
> |---|---|---|---|
> | **核心目的** | 消除组间系统偏差，确立[[Causality\|因果推断]] | 提升样本对母体总体的代表性 | 在少数可观测[[Variable\|变量]]上实现组间平衡 |
> | **保障的效度** | [[Internal Validity\|内部效度]]（Internal Validity） | [[External Validity\|外部效度]]（External Validity） | 有限的内部效度（受遗漏变量威胁） |
> | **操作时机** | 样本选定后分派至实验条件时 | 从[[Study Population and Sample\|目标总体]]中抽取受试样本时 | 非随机样本选定后进行配对控制 |
> | **等价性范围** | **全部变量**（已知与未知、已测与未测） | 样本与总体在关键特征上的同构 | 仅限于**少数显性命名变量** |
> | **来源** | [[Argument_Creswell_2022_SAGE\|Creswell & Creswell (2022)]]; [[Argument_Cohen_Manion_Morrison_2011_Routledge\|Cohen et al. (2011)]] | 同上 | Smith (1991); [[Argument_Cohen_Manion_Morrison_2011_Routledge\|Cohen et al. (2011)]] |

---

## 适用场景与局限性

> [!method-fit] 适用判断
> - **适合使用** 评估标准化教学干预、数字工具、药物疗效或科研资助机制（如部分抽签）的纯粹因果效应；当[[Research Ethics|研究伦理]]允许且[[Sample Size Determination|样本量]]足以保障统计功效时。
> - **谨慎使用** 复杂社会与教育生态中，当受试者具有强烈能动性且无法实施双盲时，教师态度与代偿性努力极易污染对照组。[[Argument_Wrigley_2018_BERJ|(Wrigley, 2018, p. 6)]]
> - **不适合使用** 涉及剥夺基础受教育权或已知救济措施的伦理禁区，宏观历史变迁、制度演变或情境依赖性极高的质性[[Case Study|个案研究]]。

> [!method-limits] 方法局限与治理警惕
> - **小样本失衡与“糟糕随机化”** 当样本量较小时，随机分配可能偶然导致严重的基线不平衡；若直接计算均值差将产生严重的数据包装偏误。[[Argument_Wrigley_2018_BERJ|(Wrigley, 2018, p. 5)]]
> - **颠覆偏差（Subversion Bias）** 执行人员可能因偏好而人为操纵受试者入组，必须通过中心化分配与[[Blinding|盲法]]防范。
> - **黑箱化与因果机制遮蔽** 仅能输出平均[[Effect Size|效应量]]，无法解释干预为何在特定情境下生效，过滤了微观实践主体的推理与情境脉络。

> [!critique-method] 随机化失败的技术解构案例：Fresh Start 拼读实验
> 英国[[Education Endowment Foundation|教育捐赠基金会]]（EEF）曾对中一学生阅读干预项目（Fresh Start）开展 [[Randomised Controlled Trials|RCT]] 评估，报告宣称获得 $+0.24$ SD 的显著增益。然而深入解构技术报告发现：
> 1. **[[Pre-test and Post-test|前测]]严重失衡** 由于分配失控，干预组前测成绩远低于控制组，其后测成绩仅略高于控制组前测；
> 2. **匹配子集拆解的幻灭** 当研究者筛选出前测分数完全相同的同质学生子集重新比对时，两组净效应量骤降为 $+0.00$ SD。
> 这一案例实证表明：不经严格基线细分核验的随机分配极易沦为统计伪像，凸显了对随机化质量进行全流程审计的必要性。[[Argument_Wrigley_2018_BERJ|(Wrigley, 2018, p. 5)]]

---

## 相关条目网络

> [!entry-map]
> 
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Critical Realism]] | 理论 | 批判实在论强调社会系统的分层[[Open-Mindedness\|开放性]]与深层机制，对随机分配的封闭系统假定提出哲学解构。 |
> | [[Randomised Controlled Trials]] | 方法 | 随机分配是构建真实验与随机对照试验的最核心设计要素。 |
> | [[Random Sampling]] | 方法 | 随机抽样服务于样本代表性，与服务于因果隔离的随机分配构成互补。 |
> | [[United Kingdom Metascience Unit]] | Fact (Org) | 将随机分配方法创新应用于科研资助抽签实验的国家级专门机构。 |
> | [[Metascience]] | Concept | 运用随机化分配与因果[[Experimental Research\|实验研究]]科研体制本身的[[Comparative Education as a Cross-Sectional Area\|交叉学科]]前沿。 |
> | [[Michael Kratsios]] | Person | 在白宫 [[Office of Science and Technology Policy\|OSTP]] 报告中倡导运用部分随机化资助实验破除同行评议避险偏误。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 研究索引
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022)]] — 系统阐述在混合实验设计中使用随机数生成器进行真实验随机分配的标准操作规程。
> - [[Argument_Wrigley_2018_BERJ|Wrigley (2018)]] — 对 [[Education Endowment Foundation|EEF]] Fresh Start 实验报告进行深度方法学解构，提供“随机分配失衡导致[[Effect Size|效应量]]虚假膨胀”的经典批判案例。
> - [[Argument_Kratsios_2026_OSTP|Kratsios (2026)]] — 系统评述[[United Kingdom Metascience Unit|英国元科学单元]]（UK [[Metascience]] Unit）将部分随机分配（Partial Randomization / Lotteries）应用于政府科研基金资助的[[Mechanism Experiments|机制实验]]，推动因果实验向科学治理自身的延伸。
