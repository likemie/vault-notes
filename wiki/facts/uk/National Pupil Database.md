---
title: National Pupil Database
aliases:
  - 国家学生数据库
  - 英国国家学生数据库
  - NPD Database
summary: "英格兰教育部编纂并维护的国家级微观行政纵向人口数据库，记录所有公立学校学生的学业统考、人口特征与升学轨迹，是英国教育实证研究、大规模RCT独立结局测量与数据归档的核心基础设施。"
type: fact
subtype: program
region: uk
fact_region: "uk"
fact_kind: "program"
fact_related_count: 25
fact_related_level: 3
fact_related_stars: "⭐⭐⭐"
fact_related_color: "#ede9fe"
tags:
  - region/uk
  - policy/data-infrastructure
  - theme/administrative-data
  - theme/evidence-based-education
  - method/database
related_concepts:
  - "[[Data Infrastructure]]"
  - "[[Variable]]"
  - "[[Class Size]]"
  - "[[Causality]]"
  - "[[Heterogeneity]]"
  - "[[External Validity]]"
  - "[[Attrition]]"
  - "[[Academic Achievement]]"
  - "[[Model Dependency]]"
  - "[[Preregistration]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Ordinary Least Squares]]"
  - "[[Covariate Adjustment]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Generalized Estimating Equations]]"
  - "[[Correlational Research]]"
  - "[[Propensity Score Matching]]"
  - "[[Difference-in-Differences]]"
related_instruments:
  - "[[EEF Padlock Security Rating]]"
related_persons: []
related_facts:
  - "[[Pupil Premium]]"
  - "[[Education Endowment Foundation]]"
  - "[[What Works Network]]"
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
  - "[[Argument_Gough_2022_EvidenceOnEIPP]]"
confidence: high
status: draft
created: 2026-09-14
updated: 2026-09-18
---

# National Pupil Database

---

## 基础设施定位与宗旨

> [!claim] 核心定位
> 英格兰国家学生数据库（National Pupil Database，NPD）是由英国教育部（Department for Education，DfE）设立并统筹运营的国家级全样本行政微观人口数据库。该数据库整合了英格兰所有受公共财政资助的学校中 3 至 19 岁儿童与青少年的标准化统考成绩、出勤表现、人口统计特征及升学轨迹，构成了英国教育因果评估、循证改革研究及教育公平问责不可或缺的核心[[Data Infrastructure|数据基础设施]]（FFT Education Datalab, 2018；[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, pp. 52–54]]）。

> [!org-context] 数据库背景与技术规格
> - **建设发起方 / 主管部门** 英国教育部。受《教育法》及国家人口普查法例授权，享有对全英公立学校在读学童行政数据的法定汇交权。
> - **覆盖规模与广度** 覆盖英格兰逾 20,000 所公立中小学、800 余万在校学生的微观全样本面板数据，时间跨度覆盖从学前教育直至 18 岁高中毕业全过程。
> - **核心技术标识** 依托每个学生入校时生成的法定“唯一学生编号”（Unique Pupil Number，UPN），实现学生跨年级、跨学校、跨学区乃至跨行政区域变动时的终身精准追踪。
> - **数据安全与伦理准入** 运行在最高级别的脱敏与安全沙箱环境之下，受严格的数据保护法律（GDPR）约束，仅面向经国家安全审查合格的大学研究团队与独立评估机构开放受限学术访问。

---

## 数据架构与核心模块

> [!ref-table] NPD 核心数据模块与[[Variable|变量]]构成
> | 模块名称 | 英文名称 | 涵盖主要指标 | 在实证评估中的关键作用 |
> |:---|:---|:---|:---|
> | **学校普查模块** | School Census | 学生性别、族裔、母语、学籍状态、缺勤率、转学记录及[[Class Size\|班级规模]]。 | 充当[[Causality\|因果推断]]模型中的人口学协变量，检验处理组与对照组的基线等值性。 |
> | **关键阶段国家统考成绩** | Key Stage Assessments | 关键阶段 1/2（小学统考 SATs）、关键阶段 4（普通中等教育证书 GCSE）及 KS5（A-Level）客观统考原始分与等级分。 | 作为完全独立于干预研发者的标准化终期学业结局测量（Primary Outcome）。 |
> | **弱势与特教支持标记** | Disadvantage & SEND | 免费校餐资格（Free School Meals, FSM）、[[Pupil Premium\|学生津贴]]（Pupil Premium）标记及特殊教育需求与残障分类。 | 开展处境不利群体的[[Heterogeneity\|异质性]]子群体分析（Subgroup Analysis），评估学业差距缩窄幅度。 |

---

## 在循证教育试验中的方法论支柱功能

> [!feature] NPD 驱动的方法学革新
> - **根治自编测验偏倚，确立坚实的[[External Validity|外部效度]]** 传统教育试验常使用研发者自行编制的测验，因过度贴合干预内容而导致[[Effect Size|效应量]]被虚假放大数倍（Cheung & Slavin, 2016）。英国[[Education Endowment Foundation|教育捐赠基金会]]强制要求以 NPD 全国统考客观成绩作为主要结局指标，彻底剥离研发者自制量表的狭隘偏向，确保了试验结论的客观性与[[External Validity|外部效度]]（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, p. 54]]）。
> - **彻底对冲[[Attrition|样本流失]]，实现超长周期追踪** 传统现场测试往往因学生毕业离校、转学导致高达 20%–40% 的严重被试流失（[[Attrition|流失]]）。利用 UPN 编号在 NPD 中直接匹配，评估者无需重返校园施测即可零接触捕获学生在小学毕业（KS2）或初中毕业（KS4）的客观[[Academic Achievement|学业表现]]，使试验的长期追踪成为可能。
> - **支撑开放数据归档与[[Model Dependency|模型敏感性]]检验** EEF 将资助完成的 105 项大规模 [[Randomised Controlled Trials|RCT]] 微观数据与 NPD 全面链接，建立了全球首个教育试验开放归档库（EEF Data Archive）。杜伦大学研究者利用该归档对 17 项早期试验进行复算，揭示出统计模型选择（[[Ordinary Least Squares|OLS]] [[Covariate Adjustment|协变量调整]] vs [[Hierarchical Linear Model|多层线性模型]] vs [[Generalized Estimating Equations|GEE]]）会导致效应量剧烈波动（Xiao et al., 2016），直接推动出台了国家级《EEF 评估统计分析指南》（*Statistical Analysis Guidance for EEF Evaluations*; The EEF, 2018）。
> - **[[EEF Padlock Security Rating|挂锁安全评级]]的硬性衡量标准** 在英国[[EEF Padlock Security Rating|挂锁安全评级]]规范中，若主要结局指标未采用与 NPD 相关的全国标准化统考，而是采用研发者自定制测验，将被强制扣减 1 把锁，凸显了 NPD 作为国家证据黄金标准的制度约束力。

---

## 衍生影响与相关事实

> [!entry-map]
> 
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Education Endowment Foundation]] | 核心用户 | EEF 建立的试验评估、协议[[Preregistration\|预注册]]与数据归档体系完全依托 NPD 作为国家测量基础设施。 |
> | [[EEF Padlock Security Rating]] | 评价准则 | 试验主要结局指标是否挂钩 NPD 全国统考，是评定挂锁安全评级的重要指标。 |
> | [[Randomised Controlled Trials]] | 方法应用 | NPD 为大规模学校聚类随机对照试验提供了全样本基线匹配与低[[Attrition\|流失]]结局追踪手段。 |
> | [[Academic Achievement]] | 测量对象 | NPD 记录的国家关键阶段考试分数，构成了英国教育评价中最核心的学业成就指标。 |
> | [[What Works Network]] | 宏观生态 | NPD 为跨部门循证决策支持提供了最权威的公立教育行政微观面板数据。 |

---

## 相关研究索引

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 详述国家学生数据库在避免自编测验偏倚、对冲[[Attrition|样本流失]]及支撑 [[Education Endowment Foundation|EEF]] 试验数据开放归档中的核心支柱角色。
> - [[Argument_Gough_2022_EvidenceOnEIPP|Gough et al. (2022)]] — 记录英国财政研究所如何依托 NPD 微观数据开展大样本[[Propensity Score Matching|倾向得分匹配]]与[[Difference-in-Differences|双重差分]]因果评估。
