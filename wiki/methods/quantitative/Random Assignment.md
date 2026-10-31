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
method_related_count: 63
method_related_level: 6
method_related_stars: "💎💎"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
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
  - "[[Academic Achievement]]"
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
  - "[[Class Size]]"
  - "[[Open-Mindedness]]"
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
  - "[[Effect Size Conversion]]"
  - "[[Meta-analysis]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Meta-meta-analysis]]"
  - "[[Research Synthesis]]"
  - "[[Mechanism Experiments]]"
related_persons:
  - "[[John Hattie]]"
  - "[[Ivan Snook]]"
related_facts:
  - "[[United Kingdom Metascience Unit]]"
  - "[[Office of Science and Technology Policy]]"
  - "[[Tennessee STAR Project 1985-1989]]"
  - "[[Education Endowment Foundation]]"
  - "[[MDRC]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Kratsios_2026_OSTP]]"
  - "[[Argument_Snook_2009_NZJES]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10]]"
  - "[[Argument_Wrigley_2018_BERJ]]"
  - "[[Argument_Bergeron_2017_MJE]]"
  - "[[Argument_Hattie_2010_NZJES]]"
  - "[[Argument_Legrand_2012_PolStud]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit11]]"
confidence: high
status: active
created: '2026-05-31'
updated: 2026-10-31
---

---

> [!def] Random Assignment
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

> [!citation-card] 田纳西 STAR 项目的双重随机分配基准
> 田纳西州师生[[Academic Achievement|学业成就]]比率研究（STAR）覆盖全州 76 所公立小学，对 6,750 名儿童和教师实行了真正的双重随机分配，将学生与教师同时随机指派至小班（13–17 人）或常规班（22–25 人）。芬恩与阿基里斯（Finn & Achilles, 1990）证实，这一严格消除选择偏误的随机分配设计在幼儿园至小学三年级（K–3）取得了 $d = 0.62$ 至 $0.66$ 的显著因果效应量。[[Argument_Snook_2009_NZJES|(Snook et al., 2009, p. 100)]]
>
> *The [[Tennessee STAR Project 1985-1989|Project STAR]] experiment involved true random assignment of both teachers and children to classes... producing substantial achievement effect sizes of 0.62 to 0.66.*

> [!citation-card] 哈佛医学院研讨会面对面交流的随机分组试验
> 在哈佛医学院内部科研研讨会中，研究者从 400 名参会科学家中随机抽取结对进行 90 分钟面对面研讨。随机分配机制彻底平衡了科学家既往的友谊、共同研究偏好等潜在混杂特征；评估证实，经随机指派获得面对面研讨机会的配对，后续形成真实科研合作的概率较对照组显著提升 75%，严格确立了降低物理搜寻成本对促进跨界科研合作的因果效应。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, pp. 249–250)]]
>
> *At a Harvard Medical School symposium, scientists were randomly paired for 90 minutes of face-to-face interaction, which increased their probability of subsequent collaboration by 75% compared to controls, cleanly isolating the causal effect of physical search costs.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 基于[[Positivism|实证主义]]与[[Empiricism|经验主义]]因果观。假定通过控制和消除混杂[[Variable|变量]]，可以直接从因果事件的恒常规则性推导出[[Causality|因果关系]]。[[Argument_Cohen_Manion_Morrison_2011_Routledge|Cohen et al. (2011)]]将样本随机化列为[[Quantitative Research|量化研究]]效度的实证主义前提之一。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|(Cohen et al., 2011, Ch. 10, pp. 158–159)]]
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

> [!proc] 通用操作程序
> 1. **确定实验处理条件** 界定[[Independent Variable|自变量]]的各个水平（如干预组 vs [[Business as Usual|常规对照组]]；或传统同行评议组 vs 随机化抽签资助组）。
> 2. **生成随机分配序列** 使用计算机算法或随机数表，为每个进入实验的受试单位生成概率均等的分配序列并做好分配隐蔽（Allocation Concealment）。
> 3. **隐蔽分配与实施入组** 确保分配序列对执行人员隐蔽（必要时实施[[Blinding|盲法]]），将受试对象依次分派入组。
> 4. **基线平衡检验（[[Baseline Standardized Mean Difference|Baseline Equivalence]] Test）** 在干预前比对处理组与对照组的[[Pre-test and Post-test|前测]]得分及核心协[[Variable|变量]]，检验随机化是否成功消除组间系统性偏差。
> 5. **后测与因果净效应估计** 收集后测结果数据，严格核查[[Attrition|样本流失]]率，计算并报告[[Effect Size|效应量]]（ES）与[[Confidence Interval|置信区间]]。

> [!stat-cards]- 随机分配的概率等价演示（改编自 Pilliner, 1973）
> - **20** （纸牌模拟实验） 从一副牌中选 20 张（10 红 10 黑），洗牌后随机分成两堆各 10 张，记录红黑牌分布。
> - **1/92,378 / ≈82%** （理论概率分布）
>   - 最可能的结果：每堆各 5 红 5 黑；
>   - 出现“一堆全红、一堆全黑”极端失衡的概率仅为 **1/92,378**；
>   - 获得“每堆不超过 6 张同色”良好混合结果的概率约为 **82%**。


---

> [!contrast-table] 随机分配 vs [[Random Sampling|随机抽样]] vs [[Propensity Score Matching|倾向得分匹配]]
> | 维度 | 随机分配（Random Assignment） | 随机抽样（Random Sampling） | 匹配（[[Matching]]） |
> |---|---|---|---|
> | **核心目的** | 消除组间系统偏差，确立[[Causality\|因果推断]] | 提升样本对母体总体的代表性 | 在少数可观测[[Variable\|变量]]上实现组间平衡 |
> | **保障的效度** | [[Internal Validity\|内部效度]]（Internal Validity） | [[External Validity\|外部效度]]（External Validity） | 有限的内部效度（受遗漏变量威胁） |
> | **操作时机** | 样本选定后分派至实验条件时 | 从[[Study Population and Sample\|目标总体]]中抽取受试样本时 | 非随机样本选定后进行配对控制 |
> | **等价性范围** | **全部变量**（已知与未知、已测与未测） | 样本与总体在关键特征上的同构 | 仅限于**少数显性命名变量** |
> | **来源** | [[Argument_Creswell_2022_SAGE\|Creswell and Creswell (2022)]]; [[Argument_Cohen_Manion_Morrison_2011_Routledge\|Cohen et al. (2011)]] | 抽样统计学标准规范 | Smith (1991); Rosenbaum and Rubin (1983) |

---

> [!method-fit] 适用判断
> - **适合使用** 评估标准化教学干预、数字工具、药物疗效或科研资助机制（如部分抽签）的纯粹因果效应；当[[Research Ethics|研究伦理]]允许且[[Sample Size Determination|样本量]]足以保障统计功效时。
> - **谨慎使用** 复杂社会与教育生态中，当受试者具有强烈能动性且无法实施双盲时，教师态度与代偿性努力极易污染对照组。[[Argument_Wrigley_2018_BERJ|(Wrigley, 2018, p. 6)]]
> - **不适合使用** 涉及剥夺基础受教育权或已知救济措施的伦理禁区，宏观历史变迁、制度演变或情境依赖性极高的质性[[Case Study|个案研究]]。

---

> [!method-limits] 方法局限与治理警惕
> - **小样本失衡与“糟糕随机化”** 当[[Sample Size Determination|样本量]]较小时，随机分配可能偶然导致严重的基线不平衡；若直接计算均值差将产生严重的数据包装偏误。[[Argument_Wrigley_2018_BERJ|(Wrigley, 2018, p. 5)]]
> - **颠覆偏差（Subversion Bias）** 执行人员可能因偏好而人为操纵受试者入组，必须通过中心化分配与[[Blinding|盲法]]防范。
> - **黑箱化与因果机制遮蔽** 仅能输出平均[[Effect Size|效应量]]，无法解释干预为何在特定情境下生效，过滤了微观实践主体的推理与情境脉络。

> [!critique-method] 受控随机分配下的公式依赖与因果排名反转（基于 Bergeron & Rivard, 2017）
> 随机分配通常被视为消除混杂[[Variable|变量]]的终极统计保障，但在宏观二阶综合中，即使受试者被严格随机指派，**[[Effect Size Conversion|效应量换算]]公式的选择偏倚依然能够彻底推翻因果结论**。
> - **受控数值实验设计** 伯杰龙与里瓦尔设定四个独立学生组，具有完全同质的初始学业正态分布（$\mu = 75, \sigma = 5$），通过真随机分配接受对照方法 0（零增量）与实验方法 1、2、3（均值增量分别为 1、2、3 分）。
> - **完全相悖的效能排名** 针对这一完美排除选择偏误的随机化数据，采用三种在统计学上合法的计算公式：
>   1. 公式 (a)（组间[[Pre-test and Post-test|后测]]均值差）：得出方法 3 > 方法 2 > 方法 1 > 方法 0（$d=0.55 > 0.37 > 0.19 > 0$）；
>   2. 公式 (b)（各组前后测增量标准化）：得出方法 1 = 方法 2 = 方法 3（$d=1.00 = 1.00 = 1.00$）；
>   3. 公式 (c)（相关系数反推均值差）：得出方法 0 > 方法 1 > 方法 2 > 方法 3（$d = +\infty > 2.00 > 1.41 > 1.15$）。
> - **方法学推论** 严格的随机分配保障了初级研究的[[Internal Validity|内部效度]]，但若[[Meta-analysis|元分析]]研究者未经检验地混用不同效应量换算公式，得出的干预排行榜反映的将是公式选择而非教学干预的真实效能。[[Argument_Bergeron_2017_MJE|(Bergeron & Rivard, 2017, pp. 243–245)]]

> [!critique-method] 随机化失败的技术解构案例：Fresh Start 拼读实验
> 英国[[Education Endowment Foundation|教育捐赠基金会]]（EEF）曾对中一学生阅读干预项目（Fresh Start）开展 [[Randomised Controlled Trials|RCT]] 评估，报告宣称获得 $+0.24$ SD 的显著增益。然而深入解构技术报告发现：
> 1. **[[Pre-test and Post-test|前测]]严重失衡** 由于分配失控，干预组前测成绩远低于控制组，其后测成绩仅略高于控制组前测；
> 2. **匹配子集拆解的幻灭** 当研究者筛选出前测分数完全相同的同质学生子集重新比对时，两组净效应量骤降为 $+0.00$ SD。
> 这一案例实证表明：不经严格基线细分核验的随机分配极易沦为统计伪像，凸显了对随机化质量进行全流程审计的必要性。[[Argument_Wrigley_2018_BERJ|(Wrigley, 2018, p. 5)]]

> [!case] 黄金标准随机分配的二阶稀释困境：田纳西 STAR 与[[Meta-analysis|元分析]]均值的张力
> 随机分配作为确立[[Causality|因果推断]][[Internal Validity|内部效度]]的黄金标准，在宏观教育政策应用中面临显著的二阶稀释困境：
> 1. **双重随机分配确立的强因果效应** 田纳西州 STAR 项目（Finn & Achilles, 1990）作为教育史上极少数对数千名师生同时实现真随机分配的标志性实验，确证了在关键早期学段（K–3）大幅压缩[[Class Size|班级规模]]（13–17 人）具有高达 $d = 0.62 \sim 0.66$ 的因果增益，且该增益在随后的求学阶段展现出长期保持性。
> 2. **[[Meta-meta-analysis|二阶元分析]]的无差别均值抹平** 然而在宏观[[Research Synthesis|证据综合]]中，[[John Hattie|约翰·哈蒂]]（John Hattie, 2009）将此类严谨落实双重随机分配的黄金标准研究，与大量非随机化、微小降班（如 25 人降至 23 人）以及不敏感高年级学段的研究机械合并，得出班级规模效应量仅为 $d \approx 0.20$ 的微弱平均数，并据此得出缩减班级规模性价比极低的政策结论。
> 3. **因果纯度与宏观概括的[[Epistemology|认识论]]分裂** [[Ivan Snook|伊万·斯努克]]（Ivan Snook）等学者（2009）指出，这种将高质量随机分配试验与弱设计混杂合并的二阶元分析做法，实质上架空并稀释了初级实验通过严格随机化所辛苦建立的纯净因果结论；哈蒂（[[Argument_Hattie_2010_NZJES|Hattie, 2010]]）则回应辩称，即便随机分配改变了物理班额，若教师未能相应调整教学行为，大规模财政投入依然效率低下。这揭示出微观严格随机分配实验与宏观二阶政策指引之间的深刻张力。[[Argument_Snook_2009_NZJES|(Snook et al., 2009, pp. 100–101)]]; [[Argument_Hattie_2010_NZJES|(Hattie, 2010, pp. 90–91)]]

> [!case] 公共福利政策中随机分配的伦理张力与制度突破：英国残障新政与 ERA 示范项目
> 随机分配要求设立不享受补贴或服务的对照组，在公共社会政策领域极易引发深层的[[Research Ethics|研究伦理]]争议与公众政治反弹：
> 1. **弱势群体对照组设置受阻** 2002 年英国就业与养老金部（DWP）尝试在残障人士新政中实施美式随机对照实验，但因将部分弱势受助群体随机划入无法获得额外支持的对照组，遭到社会倡导团体与公众的强烈抗议，被指责违背社会正义并剥夺困难群体基本权益，导致实验一度搁浅。
> 2. **循证刚性需求驱动更大规模制度实验** 面对伦理争议，决策层对严格因果检验的认识论诉求推动了制度设计创新。英国政府随后在英国就业保留与晋升示范项目中，成套引入美国成熟的双重激励设计，由美国专业智库 [[MDRC]] 跨境承接分组规程设计与现场运行审计，使随机分配规程在包含留职现金奖励的复合设计中突破了单一剥夺性对照的伦理困局，成为英国社会政策史上最大规模的随机对照实验。[[Argument_Legrand_2012_PolStud|(Legrand, 2012, p. 343)]]

---

> [!entry-map] 相关理论与方法
> 
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Critical Realism]] | 理论 | 批判实在论强调社会系统的分层[[Open-Mindedness\|开放性]]与深层机制，对随机分配的封闭系统假定提出哲学解构。 |
> | [[Randomised Controlled Trials]] | 进阶设计 | 随机分配是构建真实验与随机对照试验的最核心技术操作。 |
> | [[Random Sampling]] | 互补方法 | 随机抽样服务于样本代表性与[[External Validity\|外部效度]]，与服务于组间等价和[[Internal Validity\|内部效度]]的随机分配构成互补。 |
> | [[Propensity Score Matching]] | 替代方法 | 观测研究中在可测协[[Variable\|变量]]上平衡组间特征的准实验替代手段，但无法平衡未测遗漏变量。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Bergeron_2017_MJE|Bergeron and Rivard (2017)]] — 在四组完全随机分配的受控模拟实验中，证实三种合法[[Effect Size|效应量]]公式导致因果排名完全颠倒，揭示出宏观综合对公式选择的虚假依赖（pp. 243–245）。
> - [[Argument_Creswell_2022_SAGE|Creswell and Creswell (2022)]] — 系统阐述在混合实验设计中使用随机数生成器进行真实验随机分配的标准操作规程。
> - [[Argument_Wrigley_2018_BERJ|Wrigley (2018)]] — 对 [[Education Endowment Foundation|EEF]] Fresh Start 实验报告进行深度方法学解构，提供“随机分配失衡导致[[Effect Size|效应量]]虚假膨胀”的经典批判案例。
> - [[Argument_Kratsios_2026_OSTP|Kratsios (2026)]] — 系统评述[[United Kingdom Metascience Unit|英国元科学单元]]（UK [[Metascience]] Unit）将部分随机分配（Partial Randomization / Lotteries）应用于政府科研基金资助的[[Mechanism Experiments|机制实验]]，推动因果实验向科学治理自身的延伸。
> - [[Argument_Snook_2009_NZJES|Snook et al. (2009)]] — 详尽剖析田纳西州 STAR 实验中师生双重真随机分配确立的强因果效应（$d = 0.62 \sim 0.66$），批评[[Meta-meta-analysis|二阶元分析]]将高质量随机实验与低质量研究无差别平均从而掩盖因果真相的方法论缺陷。
> - [[Argument_Hattie_2010_NZJES|Hattie (2010)]] — 回应[[Class Size|班级规模]]随机分配实验的政策争议，论证仅靠随机化调整物理班额而不变革教学方法无法带来理想的教育产出比。
> - [[Argument_Legrand_2012_PolStud|Legrand (2012)]] — 详尽剖析英国就业与养老金部（DWP）如何跨国引入美国 [[MDRC]] 研发的随机分配技术，并开展英国社会政策史上最大规模的就业保留与晋升（ERA）随机对照评估（pp. 342–343）。
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Wang & Barabási (2021)]] — 评述哈佛医学院研讨会利用随机分组分配面对面研讨，严格平衡科学家未观测混杂特征并证实合作概率相对净增 75% 的实地实验设计（pp. 249–250）。

