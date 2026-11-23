---
title: Intervention Research
aliases:
  - 干预研究
  - 干预性研究
summary: "通过操纵教育处理、项目或实践条件来检验效果及因果影响的研究设计，常用于评估干预是否带来可观察变化"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 24
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - intervention-research
  - educational-psychology
  - causal-inference
  - research-methodology
related_concepts:
  - "[[Variable]]"
  - "[[Independent Variable]]"
  - "[[Epistemology]]"
  - "[[Causality]]"
  - "[[Recommendations for Practice]]"
  - "[[Homework]]"
  - "[[Academic Achievement]]"
  - "[[Experiential Learning]]"
  - "[[Reproducibility Crisis]]"
  - "[[Evidence-Based Education]]"
  - "[[Chain of Evidence]]"
  - "[[Epistemic Cognition]]"
  - "[[Inquiry-Based Learning]]"
  - "[[Source Evaluation]]"
  - "[[Heterogeneity]]"
  - "[[Reliability]]"
related_theories: []
related_methods:
  - "[[Experimental Research]]"
  - "[[Random Assignment]]"
  - "[[Correlational Research]]"
  - "[[Non-intervention Research]]"
  - "[[Meta-analysis]]"
  - "[[Pre-test and Post-test]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Questionnaire]]"
related_persons: []
related_arguments:
  - "[[Argument_Brady_2023_EPR]]"
  - "[[Argument_Cartiff_2021_JEP]]"
  - "[[Argument_Higgins_2016_ROE]]"
  - "[[Argument_Terhart_2014_HolyGrail]]"
confidence: medium
status: active
created: 2026-05-05
updated: 2026-11-23
---

---

> [!def] Intervention Research
> 干预研究（Intervention Research）指研究者通过主动操纵[[Independent Variable|自变量]]（引入特定教育处理、教学方案、政策干预或实践项目），检验其是否对因变量产生系统影响及因果效应的研究设计。它处于从观察探索走向实证因果检验的验证阶段，为教育改进与实践建议提供因果证据支撑。[[Argument_Brady_2023_EPR|(Brady et al., 2023, pp. 2–4)]]

> [!method-scope] 方法范围
> - **研究对象** 教学干预方案、学习策略训练、课程改革措施、教育心理学实验处理或学校改进项目。
> - **问题类型** 因果效应识别、教学处理的净效应测度、方案有效性评估与干预机制检验。
> - **分析单位** 学生个体、课堂班级、教师群体或参与试点的学校机构。
> - **输出形式** 前后测平均分差、均值比较统计量（t 检验与方差分析）、标准化效应量（Cohen's $d$）、协方差分析调整效应。

> [!citation-card] Brady et al. 论干预研究对因果识别的必要性
> 任何未建立在能识别因果关系的严谨方法论基础上的实践建议，都是值得怀疑的。如果目标是指导实践，真正的干预假设必须通过干预研究和随机实验进行正式检验。[[Argument_Brady_2023_EPR|(Brady et al., 2023, pp. 2, 9)]]
>
> *The underlying assumption of this study is that any RFP [recommendation for practice] that is not based on sound methodology that can identify causal relations is suspect.*

---

> [!method-position] 认识论与方法定位
> - **知识观** 实证主义与后实证主义因果解释取向；强调仅凭观察性相关数据无法断言教育措施的必然效果，必须通过主动控制与实验干预分离时序因果。
> - **研究者角色** 教学处理的设计者与实验条件的控制者，负责维持处理保真度并隔离非干预混杂因素。
> - **有效性标准** 内部效度（控制成熟偏差、历史事件与选择偏倚）、构念效度（处理操作化与测量的一致性）、统计结论效度与生态效度。
> - **不声称回答的问题** 单一干预研究不能保证跨异质情境的普遍推广性，且在缺乏随机分配时难以完全排除不可观测的基线选择偏误。

> [!method-stack] 方法层级
> - **研究设计** 前后测对照组设计、准实验设计、时间序列设计与随机对照试验（RCT）。
> - **数据收集** 学业测验、标准化量表、行为观察记录、课堂任务表现评估。
> - **分析方法** 独立样本与配对样本 t 检验、方差分析（ANOVA）、协方差分析（ANCOVA）、重复测量方差分析与多层线性模型（HLM）。
> - **辅助技术** 匹配技术（倾向得分匹配 PSM）、基线平衡性检验、处理保真度监测、失联流失分析。

---

> [!proc] 通用程序
> 1. **明确干预假设与因果边界** 梳理前期观察与相关性研究线索，明确拟操纵自变量与目标因变量之间的因果机制假设（[[Argument_Brady_2023_EPR|Brady et al., 2023, p. 2]]）。
> 2. **设计干预处理与选择对照条件** 界定实验组所接受的具体教学处理，明确对照组采用既有常规教学或对照条件，制定标准化干预手册。
> 3. **抽样分组与基线测量** 确定研究对象并实施分组（准实验配对或随机分配），施测基线前测以检验组间同质性与可比性。
> 4. **实施干预与保真度监控** 在预定周期内执行教学处理，记录实施过程中的偏差、依从度及流失情况，确保干预条件的纯粹性。
> 5. **后测评估与效应建模** 开展后测或延时追踪测验，采用协方差分析等模型估计净效应量，检验统计显著性并评估实践价值。

> [!method-stack] 数据与变量
> - **数据结构** 纵向前测—后测面板数据、实验组—对照组配对数据或课堂嵌套分层数据。
> - **样本与单位** 处理组与对照组样本量、抽样方式（整班抽样或个体抽样）、分析单位（学生个体或班级）。
> - **变量或测量** 操纵自变量（特定干预方案的有无与强度）、结果因变量（学业成就或认知指标）、控制变量（前测基线得分、家庭背景）。

---

> [!method-fit] 适用判断
> - **适合使用** 评估具体教学法、认知策略训练或技术介入对学生学习成效的直接因果影响，为教育决策提供坚实的因果依据。[[Argument_Brady_2023_EPR|(Brady et al., 2023, pp. 2–3)]]; [[Argument_Cartiff_2021_JEP|(Cartiff et al., 2021, p. 509)]]
> - **谨慎使用** 涉及伦理争议的剥夺性对照（如长时间剥夺对照组正常学习资源）；处于急剧震荡或高流失率的教育现场。
> - **不适合使用** 仅用于初步摸底特定教育现象的宏观社会分布，或探索未有明确理论构想的深层质性生活史。

---

> [!method-limits] 方法局限
> - **偏误来源与效应混淆** 在元分析中，若混淆干预效果、成熟自然增长与横截面相关效应，会导致合成效应失去比较意义（[[Argument_Higgins_2016_ROE|Higgins, 2016, p. 44]]）。
> - **准入质控门槛缺失引发的方法学异质性** 若元分析缺乏严密的文献准入与质量评价门槛，将实验控制严谨的干预研究与宽泛粗疏的问卷调查在计算中一视同仁，会使底层证据库的质量异质性极高，损害结论的可靠性（[[Argument_Terhart_2014_HolyGrail|Terhart, 2014, p. 14]]）。
> - **现场合作与实施成本约束** 课堂干预需要耗费大量时间、经费与学校深度配合，问责压力与教师流失常常阻碍严格干预研究的落地（[[Argument_Brady_2023_EPR|Brady et al., 2023, p. 8]]）。
> - **补救方式** 采用预注册方案明确干预规程；通过意向性治疗分析（ITT）控制流失偏误；在元分析中设立严格的文献方法学准入标准并开展亚组异质性检验。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Evidence-Based Education]] | 理论 | 证据知情教育将干预研究与随机实验视为确立实践因果推荐的证据链基石。 |
> | [[Experimental Research]] | 上位方法 | 实验研究在干预研究操纵自变量的基础上进一步要求随机分配。[[Argument_Brady_2023_EPR|(Brady et al., 2023, p. 4)]] |
> | [[Random Assignment]] | 核心技术 | 随机分配是消除不可观测混杂、将准实验干预提升为真实验的关键程序。 |
> | [[Non-intervention Research]] | 替代方法 | 非干预研究不操纵自变量，适合情境探索但不宜直接导出强因果实践建议。[[Argument_Brady_2023_EPR|(Brady et al., 2023, pp. 2–4)]] |
> | [[Correlational Research]] | 前置方法 | 观察与相关研究识别潜在关联，为设计针对性干预处理提供假说来源。 |
> | [[Meta-analysis]] | 综合方法 | 元分析聚合多项干预研究以评估综合效应，需警惕与非干预数据的混合偏倚。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 44)]]; [[Argument_Terhart_2014_HolyGrail|(Terhart, 2014, p. 14)]] |
> | [[Questionnaire]] | 数据收集 | 问卷常用于收集自陈数据，其实验控制强度与干预研究存在实质差异。[[Argument_Terhart_2014_HolyGrail|(Terhart, 2014, p. 14)]] |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Brady_2023_EPR|Brady et al. (2023)]] — 对 2020 年五大权威教育心理学期刊开展方法趋势编码，揭示干预研究占比从 2000 年的 40% 降至 25% 并长期停滞，指出非干预研究过度跨越因果界限提出实践建议的方法学风险（pp. 2–9）。
> - [[Argument_Cartiff_2021_JEP|Cartiff et al. (2021)]] — 针对 26 项旨在促进认识论认知的实验与准实验干预研究开展元分析，证实教学干预对学业成就具有显著因果促进作用（$d = 0.509$）（p. 509）。
> - [[Argument_Higgins_2016_ROE|Higgins (2016)]] — 指出在元分析中混淆干预效果、成熟效应与横截面相关效果会导致效应量失去内在可比性（p. 44）。
> - [[Argument_Terhart_2014_HolyGrail|Terhart (2014)]] — 批评哈蒂在元分析合成中缺乏质量准入门槛，将控制严谨的干预研究与宽泛的问卷调查等同对待，引发底层证据库的严重异质性（p. 14）。
