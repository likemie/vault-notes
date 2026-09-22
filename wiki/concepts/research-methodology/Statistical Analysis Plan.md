---
title: Statistical Analysis Plan
aliases:
  - 统计分析计划
  - SAP
  - 预先统计分析计划
  - prespecified SAP
summary: "在试验数据收集或解盲前由独立评估团队预先制定并公开发布的详尽技术法典，硬性锁定主要模型、协变量、集群校正与敏感性分析规则，是根除数据钓鱼与消解模型依赖性的制度基石"
type: concept
domain: "research-methodology"
related_count: 38
related_level: 3
related_stars: "⭐⭐⭐"
related_color: "#fde68a"
tags:
  - statistical-analysis-plan
  - research-methodology
  - preregistration
  - open-science
  - statistics
  - causal-inference
related_concepts:
  - "[[Variable]]"
  - "[[Initial Teacher Training]]"
  - "[[Causality]]"
  - "[[Evaluator Independence]]"
  - "[[Model Dependency]]"
  - "[[Publication Bias]]"
  - "[[Dependent Variable]]"
  - "[[Attrition]]"
  - "[[Hypothesis]]"
  - "[[Paradigm]]"
  - "[[Preregistration]]"
  - "[[Document]]"
  - "[[Clinical Trial]]"
  - "[[Heterogeneity]]"
related_theories:
  - "[[Theory of Change]]"
related_methods:
  - "[[Standard Error]]"
  - "[[Complier Average Causal Effect]]"
  - "[[Sample Size Determination]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Pre-test and Post-test]]"
  - "[[Stratified Sampling]]"
  - "[[Meta-meta-analysis]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Qualitative Research]]"
  - "[[Ethnography]]"
  - "[[Effect Size]]"
  - "[[Correlational Research]]"
related_instruments:
  - "[[EEF Padlock Security Rating]]"
  - "[[CONSORT-SPI]]"
related_persons: []
related_facts:
  - "[[Education Endowment Foundation]]"
  - "[[ISRCTN]]"
  - "[[What Works Clearinghouse]]"
  - "[[Institute of Education Sciences]]"
  - "[[National Center for Education Evaluation and Regional Assistance]]"
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
  - "[[Argument_Higgins_2016_ROE]]"
confidence: high
status: completed
created: 2026-09-15
updated: 2026-09-17
---

# Statistical Analysis Plan

---

## 定义

> [!def] 核心定义
> 统计分析计划（Statistical Analysis Plan，简称 SAP）指在实证试验实施、数据采集或双盲解密之前，由独立评估团队预先起草、经同行评审并公开发布的技术性刚性规范文件（[[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill, 2021, pp. 51–52]]）。它详尽规定了主要因果结局的精确数学模型、协[[Variable\|变量]]纳入标准、多层集群[[Standard Error\|标准误]]校正规程、缺失数据处理算法、依从性分析（意向性治疗分析 [[Initial Teacher Training\|ITT]] 与[[Complier Average Causal Effect\|依从者平均因果效应]] CACE）以及辅助性敏感性检验范围。SAP 是将开放科学规范落到实处的关键法典，旨在彻底杜绝研究者在看到数据后挑选显著结果的数据钓鱼（Data Dredging）行为。

> [!concept-lens] 概念透镜
> - **含义** 指向量化[[Causality\|因果推断]]中的“技术契约”，将分析自由度在前置阶段予以制度化剥离。
> - **用途** 为独立评估报告提供刚性核查底线，防止研究团队因外部商业利益或学术发表压力而更改统计模型。
> - **边界** 超越宽泛的试验方案概述（Protocol），专注文数转化过程中的每一个参数设定与代码级算法逻辑。

> [!citation-card] 统计分析计划的强制公开与防偏倚机制（[[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill, 2021]]）
> 为最大程度降低选择性报告（即排除负面或不利结果所产生的偏倚），英国[[Education Endowment Foundation\|教育捐赠基金会]]（EEF）强制要求每项受资助试验的评估方案与预先制定的统计分析计划（SAP）必须在官方网站公开发布，并在 [[ISRCTN]] 等一级临床与社会试验注册库完成登记。所有试验报告无论成效显著与否均无条件全量公开……这种将 SAP 前置备案的做法，成为防范研发者暗中施加影响、根除利益冲突的根本制度防火墙。[[Argument_Edovald_Nevill_2021_ECNUROE\|(Edovald & Nevill, 2021, p. 52)]]
>
> *“The EEF requires a prespecified protocol and statistical analysis plan for every trial to be published on its website and the trial registered on ISRCTN registry... All EEF’s findings are published, whatever the result.”*

> [!boundary] 概念边界
> - **不等于 试验总体研究方案（Trial Protocol）** Protocol 涵盖干预背景、受试者招募、实施伦理与田野后勤；而 SAP 专门聚焦数据清洗、统计建模、标准误估计与统计推断规则的技术细则。
> - **不等于 试验注册摘要（Registry Summary, 如 ISRCTN 登记项）** 注册平台通常仅记录简要的结局指标名称与[[Sample Size Determination\|样本量]]；SAP 是长达数十页的完整数学建模白皮书。
> - **不等于 事后数据分析脚本（Post-hoc Analysis Script）** 数据分析脚本是事后执行的代码；SAP 是在接触最终结局数据之前确立的先验规则。

---

## 概念辨析

> [!contrast-table] 试验设计与透明度规范层级对比
> | 规范层次 | 试验研究方案 (Trial Protocol) | 统计分析计划 (SAP) | 临床与社会试验注册 (Registry Record) |
> |---|---|---|---|
> | **编制核心主体** | 研发者与[[Evaluator Independence\|独立评估者]]协同起草 | 独立评估团队计量学家独立拟定 | 课题负责人向公共平台（如 [[ISRCTN]]）提交 |
> | **核心涵盖内容** | 干预[[Theory of Change\|变革理论]]、招募路径、伦理审批、现场田野日程 | 主效应模型公式、协[[Variable\|变量]]字典、[[Intraclass Correlation Coefficient\|ICC]] 校正、缺失插补算法 | 试验名称、目标[[Sample Size Determination\|样本量]]、主要/次要结局测量工具名称 |
> | **发布时间节点** | 试验招募与基线测试启动之前 | 试验实施期内、终结性数据收集或解盲之前 | 首次招募受试者入组之前完成时间戳备案 |
> | **质控防范功能** | 防范现场实施脱靶与伦理风险 | 彻底消解[[Model Dependency\|模型依赖性]]与事后数据钓鱼（p-hacking） | 确立优先权，防范隐匿整个试验的[[Publication Bias\|发表偏倚]] |

---

## 核心要素

> [!feature] 核心要素
> - **主效应回归模型形式化（Primary Model Equation）** 用明确的数学公式锁定因果估计方程（例如：指定两级[[Hierarchical Linear Model\|分层线性模型]]、固定斜率与随机截距、[[Dependent Variable\|因变量]]标准化方式及 Hedges' $g$ 计算分母）。
> - **协[[Variable\|变量]]前置刚性列表（Pre-specified Covariates）** 逐一明确纳入主模型的控制变量名称与测量来源（如强制纳入英国 NPD 统考基线[[Pre-test and Post-test\|前测]]成绩），严禁在看到回归结果后随意增删控制变量。[[Argument_Edovald_Nevill_2021_ECNUROE\|(Edovald & Nevill, 2021, p. 52)]]
> - **层级群聚与[[Standard Error\|标准误]]估计准则（Clustering Standard Errors）** 明确设定如何校正学校或班级层级的[[Intraclass Correlation Coefficient\|组内相关系数]]（ICC），指定采用 Huber-White 聚类稳健标准误还是全贝叶斯[[Stratified Sampling\|分层抽样]]。
> - **缺失数据诊断与敏感性规程（Missing Data Protocols）** 预先规定当[[Attrition\|样本流失]]率超过特定阈值时，采取何种缺失机制[[Hypothesis\|假设]]（MCAR, MAR, MNAR）并执行多重插补或界限分析（Bounds Analysis）。
> - **偏离记录与备案透明度（Protocol Deviation Reporting）** 明确若在实际分析中因不可抗力必须偏离 SAP 时，必须在最终报告中设立专门章节详述偏离理由，并同时报告原 SAP 模型的基准结果。

> [!logic-map] 统计分析计划（SAP）在证据生产全周期的防护机制
> ```mermaid
> flowchart TD
>     A["试验立项与方案设计"] --> B["编制并公开发布详尽 SAP"]
>     B --> C["公共注册平台时间戳锁定 (ISRCTN)"]
>     C --> D["现场田野干预实施与数据收集"]
>     D --> E["数据清洗与盲态锁定"]
>     E --> F{"是否严格执行 SAP 预设模型?"}
>     F -- "是" --> G["生成高安全级别评估结果 (3-5把挂锁)"]
>     F -- "否/暗中变更" --> H["评级降级惩罚、扣减挂锁、公开质疑"]
>     G --> I["彻底阻断研究者自由度与模型依赖性漂移"]
> ```

---

## 围绕概念形成的命题

---

### 命题一　统计分析计划（SAP）将预注册从宽泛的意向声明升格为具有约束力的技术契约

> [!concept-lens] 探讨维度：开放科学从宏观倡导向微观技术规范的[[Paradigm\|范式]]演进
> 科学社会学与量化方法学研究表明：仅在网站上简略登记研究假说，依然为研究者保留了巨大的操纵空间；唯有代码级的先验 SAP 才能真正终结假阳性危机。

> [!claim] [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021, pp. 51–53)]]
> **技术锁定根除选择性报告** 传统社会科学研究中，正向显著结果的发表几率比零结果高出 40%（Franco et al., 2014）。许多研究者即使[[Preregistration\|预注册]]了假说，仍会在后端通过“更换协[[Variable\|变量]]”或“删除不显著亚组”实现显著。[[Education Endowment Foundation\|EEF]] 的实践表明，强制评估团队在接触数据前独立提交长篇 SAP，并将具体分析模型、协变量定义和聚类校正方法固定在公开服务器上，使得任何事后迎合资助方或学术期刊审稿人的暗室操作在技术上彻底失去空间。

---

### 命题二　SAP 构成了循证中介机构实施证据质量评级与跨试验横向比较的制度红线

> [!concept-lens] 探讨维度：证据清算机构的标准化治理基础设施
> 证据生态学研究揭示：缺乏预注册 SAP 的因果证据无法在[[Meta-meta-analysis\|二阶元分析]]工具包中获得高公信力的横向排位。

> [!claim] [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021, pp. 51–53, 57)]]; The EEF (2018, 2019c)
> **[[EEF Padlock Security Rating\|挂锁安全评级]]的准入刚性** EEF 在《挂锁安全评级体系》（Padlock Rating）中将“是否严格遵循预注册 SAP”作为评定证据安全性的核心扣分指标。若某项试验未能在数据收集前发布 SAP，或最终报告严重违背 SAP 且未作充分方法学解释，该研究将被直接扣减 1 把挂锁甚至判定为证据不可靠。正是得益于 SAP 的全面制度化推行，EEF 资助的已发表试验中高达 85% 获得了 3 把锁及以上的极高安全评级，为全球教育证据清算树立了标杆。

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者与[[Document\|文献]] |
> |---|---|---|---|
> | **技术契约命题** | 阐明 SAP 如何通过算法级预先规约剥夺事后分析自由度，根除选择性报告 | 开放科学、试验方案审查、统计推断防偏倚 | [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]]; Franco et al. (2014) |
> | **制度红线命题** | 论证 SAP 作为证据等级评定与跨项目可比性制度门槛的刚性治理功能 | 证据中介机构运营、[[What Works Clearinghouse\|WWC]]/EEF 清算标准 | The EEF (2018, 2019c); Boulay et al. (2018) |

---

## 概念演变

> [!dev-timeline] 概念演变与学术脉络
> - **1990s — 国际人用药品技术要求协调会（ICH E9）确立规范** 国际医药监管机构发布 ICH E9《[[Clinical Trial\|临床试验]]的统计原则》，首次在法规层面上确立了必须在试验双盲揭开前锁定 SAP 的法定要求。
> - **2000s — 医学向社会科学扩散受阻** 尽管流行病学与医学试验普及了 SAP，但社会科学与教育学界长期认为社会情境干预过于复杂，抗拒采用机械的先验计划，导致教育试验深陷“抽屉问题”与假阳性危机。
> - **2013 — [[Education Endowment Foundation\|EEF]] 首创教育评估 SAP 制度化模板** 英国 EEF 基于 CONSORT 标准（Shulz et al., 2010），编制了全球首个专用于教育现场试验的方案与 SAP 模板，开辟了教育实证治理先河。[[Argument_Edovald_Nevill_2021_ECNUROE\|(Edovald & Nevill, 2021, p. 52)]]
> - **2018 — 跨领域国际标准 [[CONSORT-SPI]] 与行业指南集成** 伴随 CONSORT-SPI（Montgomery et al., 2018）与《EEF 评估统计分析指南》（*Statistical Analysis Guidance for EEF Evaluations*; The EEF, 2018）的发布，SAP 正式从个别机构探索演化为全球复杂社会干预报告的黄金行业基准。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] [[Preregistration\|预注册]]刚性契约 vs 意外科学发现的探索自由
> > 争论焦点在于严格锁定 SAP 是否会扼杀研究者在数据探索中捕捉非预期因果机制的学术敏锐度。
> >
> > - **严格规范立场（[[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill, 2021]]）** 坚称主要验证性因果结论必须严格受制于 SAP；未在计划中的分析只能被明确标记为“探索性附录”，决不能与主要结论混为一谈。
> > - **科学探索立场** 指出教育现实充满动态变异，现场常出现意料之外的阻碍或[[Heterogeneity\|异质性]]群体，机械绑定预注册方案可能导致研究者不敢深入挖掘真实机制。

> [!critique] 外部批评
> - **评估者形式化应对风险** 部分学者指出，某些评估团队为了规避责任，在制定 SAP 时倾向于写下宽泛模棱两可的模型描述，使得事后的所谓“严格按 SAP 执行”流于形式。

> [!warning] 适用局限
> 统计分析计划专用于以因果[[Hypothesis\|假设]]检验为核心目的的定量实证研究（如 [[Randomised Controlled Trials\|RCT]] 与严谨 [[Quasi-Experimental Designs\|QED]]）。在以理论生成为目的的[[Qualitative Research\|质性研究]]、质性[[Ethnography\|民族志]]或探索性先导试验（Pilots）中不适用。

---

## 实证数据

> [!ref-table]- 其他实证结果（无[[Effect Size\|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]] | 英国 [[Education Endowment Foundation\|EEF]] 资助开展的 95 项已完成评估报告 | 独立评估全流程审计与[[EEF Padlock Security Rating\|挂锁安全评级]]统计 | 方案[[Preregistration\|预注册]]与 SAP 发布率、3 锁以上达成比例 | 89% 的评估基于 RCT，85% 的已发表报告达成 3 把锁及以上评级（整体流失率 $< 30\%$）；强制公开预注册 SAP 与方案使得发表偏倚得到有效控制 | 85% 达成高质量安全评级 | 证明基于 SAP 的制度化规约能够在大规模国家级资助中系统性提升因果推断可信度 |
> | Boulay et al. (2018) | 美国[[Institute of Education Sciences\|教育科学研究院]]（IES）[[National Center for Education Evaluation and Regional Assistance\|NCEE]] 资助的 65 项 i3 独立评估 | 跨国评估治理模式横向比较 | 自聘评估机构 vs 独立委托机构的 SAP 约束与 [[What Works Clearinghouse\|WWC]] 达标率 | 仅有刚刚超过三分之二（68%）的 i3 试验无保留达到 WWC 最高标准；与 EEF 相比，美方模式缺乏对评估者冲突与先验建模的强硬独立约束 | 显著低于 EEF 85% 的高安全比例 | 凸显了独立三方委托与强制 SAP 预注册在防范评估偏倚上的制度优越性 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research\|相关研究]]索引
> - [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]] — 详细阐明 [[Education Endowment Foundation\|EEF]] 如何通过将 SAP 前置备案、[[ISRCTN]] 试验注册与 NPD 数据库归档深度咬合，打造全链条透明与可复现性治理体系。
> - [[Argument_Higgins_2016_ROE\|Higgins (2016)]] — 反思[[Meta-meta-analysis\|元综合]]中纳入研究在分析方法学上的质量门槛，强调先验协议对控制二阶综合偏差的关键价值。
