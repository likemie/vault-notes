---
title: Pre-test and Post-test
aliases:
  - 前测与后测
  - pretest and posttest
  - 前测
  - 后测
  - pretest
  - posttest
summary: "实验与评估中在干预前后分别实施的基准确立与效应测量技术，用于检验组间等价性、隔离外部成熟与历史偏误并精确测度能力净增值。"
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
  - method/quantitative
  - quantitative-research
  - research-design
  - experiment
related_concepts:
  - "[[Dependent Variable]]"
  - "[[Unit of Analysis]]"
  - "[[Interaction Effect]]"
  - "[[Causality]]"
  - "[[Epistemology]]"
  - "[[Pre-test Sensitisation]]"
  - "[[Construct]]"
  - "[[Reliability]]"
  - "[[Placement, Formative, Diagnostic, and Summative Testing]]"
  - "[[Achievement and Aptitude Tests]]"
  - "[[Variable]]"
  - "[[Floor and Ceiling Effects]]"
  - "[[Operationalization]]"
  - "[[Independent Variable]]"
  - "[[Order Effects]]"
  - "[[Internal Validity]]"
  - "[[Formative Assessment]]"
  - "[[External Validity]]"
  - "[[Chain of Evidence]]"
related_theories: []
related_methods:
  - "[[Pretest-Posttest Control Group Design]]"
  - "[[Difference-in-Differences]]"
  - "[[Solomon Four-Group Design]]"
  - "[[Time Series Design]]"
  - "[[Rating Scale]]"
  - "[[Analysis of Covariance]]"
  - "[[Analysis of Variance]]"
  - "[[Repeated Measures Design]]"
  - "[[Item Response Theory]]"
  - "[[Random Assignment]]"
  - "[[Effect Size]]"
  - "[[Experimental Research]]"
related_persons:
  - "[[Olaf Köller]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Koller_2014_WhatWorks]]"
related_facts: []
confidence: high
status: active
created: 2026-07-13
updated: 2026-11-24
---

> [!def] Pre-test and Post-test
> 前测与后测（Pre-test and Post-test）指在实验干预或教学改进实施前后分别开展的两次（或多阶段）标准化测量规程。**前测（Pre-test）** 在干预开始前执行，核心功能在于建立个体或群体的认知基线、评估被试先验知识并检验实验组与对照组间的初始等价性；**后测（Post-test）** 在干预结束或关键里程碑处实施，用于评估[[Dependent Variable|因变量]]状态变化并剥离外部干扰以量化干预带来的净增值效应。在[[Pretest-Posttest Control Group Design|前后测控制组设计]]中，因果净效应通常表达为[[Difference-in-Differences|双重差分]] $(E_2 - E_1) - (C_2 - C_1)$。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch. 16, pp. 314, 334–335)]]; [[Argument_Koller_2014_WhatWorks|(Köller, 2014, p. 35)]]

> [!method-scope] 方法范围
> - **研究对象** 实验组与对照组被试在干预前后特定认知、态度或能力维度的表现水平变化。
> - **问题类型** 检验基线等价性、评估干预前后能力增长幅度、识别时间流逝自然成熟与实际处理效应的差异。
> - **[[Unit of Analysis|分析单位]]** 学生个体得分、班级平均表现或学校整体绩效增值指标。
> - **输出形式** 基线等价性统计量（如基线标准化均值差）、前后测增值分（Gain Score）、双重差分净效应、时滞[[Interaction Effect|交互效应]]图表。

> [!citation-card] 关键定义
> 前测回答“两组在干预前是否等价并提供初始认知锚点”，后测回答“干预后两组是否存在显著能力增量”。在前后测控制组设计中，前后两次测量与对照组的结合构成了[[Causality|因果推断]]的核心支柱。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch. 16, pp. 314, 334–335)]]
>
> *“In the pretest-posttest control group design... the effect of the experimental treatment is calculated as (E2 - E1) - (C2 - C1)... Pretests establish initial equivalence and baselines, while posttests measure subsequent performance.”*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 实证因果对比与动态增量视角；认为单次静态后测无法区分干预真实效果与被试先验差异，唯有通过前后历时对比方能隔离增值变化。
> - **研究者角色** 测量工具标准化的维护者与施测时机控制者；需严格控制前测对被试心理的[[Pre-test Sensitisation|预试敏感化]]，并审慎选择后测时间窗口以防范即时近因效应与延迟消退效应。
> - **有效性标准** 前后测工具的[[Construct|构念]]等值性与[[Reliability|信度]]、基线等价性标准（如 $d < 0.05 \sim 0.25$）、自然成熟与历史事件干扰的有效排除。
> - **不声称回答的问题** 单纯前后测本身不等于因果推断；若缺乏无干预对照组，前后得分差异不能排除自然身心发展、环境事件或回归均数等竞争性假设。

> [!method-stack] 方法层级
> - **研究设计** 前后测控制组设计（Pretest-Posttest Control Group）、单组前后测设计（Pre-experimental）、[[Solomon Four-Group Design|所罗门四组设计]]（Solomon Four-Group Design）、[[Time Series Design|间断时间序列设计]]（Interrupted Time Series）。
> - **数据收集** 诊断性[[Placement, Formative, Diagnostic, and Summative Testing|形成性测验]]、标准化纸笔与机考[[Achievement and Aptitude Tests|成就测验]]、行为量规评定、心理[[Rating Scale|态度量表]]。
> - **分析方法** [[Analysis of Covariance|协方差分析]]（ANCOVA，控制前测分）、重复测量[[Analysis of Variance|方差分析]]（[[Repeated Measures Design|Repeated Measures]] ANOVA）、差分中的差分（DID）、潜[[Variable|变量]]潜增长模型（LGM）。
> - **辅助技术** 前测敏感化排查、等值试卷编制与锚题链接（[[Item Response Theory]] Equating）、[[Floor and Ceiling Effects|天花板与地板效应]]诊断。

---

> [!proc] 通用程序
> 1. **明确测量目标与构念[[Operationalization|操作化]]** 依据干预内容界定前后测考查的核心概念与技能标准，编制具备构念等值性的平行测验工具。
> 2. **实施前测并确立基线等价性** 在干预启动前贴近执行前测，评估被试先验知识分布，检验组间基线均值与方差差异。
> 3. **展开教学或实验干预** 在严格控制外部混淆因素的前提下落实干预方案，并记录执行过程保真度。
> 4. **合理选择时机施测后测** 权衡即时近因效应与长期延迟效应，确定适宜的后测时点（必要时增设延时追踪后测）。
> 5. **统计建模分离净效应** 运用协方差分析或双重差分模型剥离前测基线差异与自然发展趋势，准确估计干预带来的能力净增长。

> [!method-stack] 数据与变量
> - **数据结构** 重复测量宽格式或长格式面板数据，包含被试标识、测量时点、处理分组及测验分值。
> - **样本与单位** 参与干预与对照的个体被试、班级集群。
> - **变量或测量** [[Independent Variable|自变量]]为实验组与对照组分类标签；因变量为前后测各轮次的测验连续分值；协变量包含前测基线分与背景人口统计特征。

---

> [!contrast-table] 前测 vs 后测 vs 多次测量的时间序列
> | 维度 | 前测 | 后测 | 多次前后测（[[Time Series Design\|时间序列]]） |
> |---|---|---|---|
> | **目的** | 建立基线、验证等价 | 测量干预效应 | 观察趋势变化，区分即时/延迟/无效应 |
> | **时机** | 干预前 | 干预后 | 干预前后各多次 |
> | **主要威胁** | [[Pre-test Sensitisation\|前测敏感化]] | 时机选择（太早/太晚） | [[Order Effects\|练习效应]]、历史事件 |
> | **缺失时的代价** | 无法验证等价、无法测量个体变化 | 无法评估干预效应 | 无法区分干预效应与已有趋势 |

---

> [!method-fit] 适用判断
> - **适合使用**
>   - 课堂教学与实验干预中准确评估学生的能力净增量。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, p. 334)]]
>   - 在以学生为中心的循证教学改进规程中，作为把脉认知起点（前测）与核验实际增值（后测）的专业反思依据。[[Argument_Koller_2014_WhatWorks|(Köller, 2014, p. 35)]]
>   - 检验[[Random Assignment|随机化]]分组在关键目标变量上的平衡性。
> - **谨慎使用**
>   - 测验内容容易产生明显练习效应或前测敏感化（使受试者提前获知考点）的研究情境。
> - **不适合使用**
>   - 无对照组且干预周期长达数月乃至数年的长期发展研究（无法区分成熟效应与干预效应）。

---

> [!method-limits] 方法局限
> - **前测敏感化威胁[[Internal Validity|内部效度]]** 前测可能改变受试者对干预材料的关注重点（Good, 1963），导致处理组与前测发生交互效应；此时可借助所罗门四组设计进行剥离。
> - **后测时机的两难困境** 立即后测易混淆短时练习排练效应与真实高阶掌握；延后后测虽能观察持久效果，却极易被干预后介入的外部历史事件污染（Morrison, 2009）。
> - **回归均数偏误** 若依据前测极端低分筛选受试者入组，后测得分往往因统计测量误差自发向均值回归，易被误判为干预奇效。
> - **测验天花板与地板效应** 若前测太难或后测太容易，将压制实际能力增量的离散度，掩盖真实干预差异。
> - **补救方式** 采用等值平行试卷降低练习效应；增设无前测对照组排查敏感化；运用协方差分析（ANCOVA）控制基线不平衡。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Pretest-Posttest Control Group Design]] | 核心设计 | 前后测控制组设计是运用前后测分离因果净效应的经典准实验框架。 |
> | [[Solomon Four-Group Design]] | 扩展设计 | 通过增设无前测对照组，专门用于检验与剥离前测敏感化效应。 |
> | [[Formative Assessment]] | 实践应用 | 教学实践中前测常作为形成性评价工具，用于诊断先备知识与概念起点。 |
> | [[Effect Size]] | 结果指标 | 描述前后测变化量与组间净效应标准差位移的核心统计指标。 |
> | [[Pre-test Sensitisation]] | 偏误来源 | 揭示前测对被试行为产生意外催化并威胁[[External Validity\|外部效度]]的典型方法学偏误。 |
> | [[Olaf Köller]] | 人物 | 将形成性前测诊断与后测增值测量整合进以学生为中心循证改进链条的德国学者。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011)]] — 详述前后测在[[Experimental Research|实验设计]]中的双重差分计算逻辑、前测敏感化局限以及后测时机选择带来的因果解释困境（Ch. 16, pp. 314, 334–336）。
> - [[Argument_Koller_2014_WhatWorks|Köller (2014)]] — 在以学生为中心的循证教学改进规程中，将形成性前测把脉起点（第 3 步）与标准化测验评估增值（第 5 步）确立为专业教学反思的[[Chain of Evidence|证据链]]条（p. 35）。
