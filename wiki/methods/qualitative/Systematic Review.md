---
title: Systematic Review
aliases:
  - 系统综述
  - 系统性综述
summary: "通过明确的纳入标准和系统搜索策略识别、筛选与评估研究文献的综述方法，旨在减少选择偏差并为元分析提供可重复的输入"
type: method
method_type: qualitative
method_family: "qualitative"
method_related_count: 37
method_related_level: 4
method_related_stars: "⭐⭐⭐⭐"
method_related_color: "#dbeafe"
tags:
- systematic-review
- research-synthesis
- evidence-based-education
- methodology
- literature-review
related_concepts:
  - "[[Effect Size]]"
  - "[[Document]]"
  - "[[Publication Bias]]"
  - "[[Statistical Significance]]"
  - "[[Epistemology]]"
  - "[[Positivism]]"
  - "[[Intercoder Agreement]]"
  - "[[Inter-Rater Reliability]]"
  - "[[Reliability]]"
  - "[[Causality]]"
  - "[[External Validity]]"
  - "[[Literature Search]]"
  - "[[Research Question]]"
  - "[[Variable]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Heterogeneity]]"
  - "[[Hypothesis]]"
  - "[[Evaluation Research]]"
  - "[[Evidence-Based Education]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Quantitative Research]]"
  - "[[Qualitative Research]]"
  - "[[Mixed Methods Research]]"
  - "[[Ethnography]]"
  - "[[Grounded Theory]]"
  - "[[Content Analysis]]"
  - "[[Case Study]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Meta-meta-analysis]]"
related_persons: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
  - "[[Argument_Higgins_2016_RE]]"
  - "[[Argument_Li_2025_HSSC]]"
related_facts:
  - "[[EPPI-Centre]]"
  - "[[EEF Teaching and Learning Toolkit]]"
  - "[[PISA]]"
confidence: medium
status: draft
created: '2026-06-08'
updated: 2026-07-17
---
# Systematic Review

---

## 定义

> [!def] 方法定义
> 系统综述（Systematic Review）是研究综合（Research Synthesis）的一种严格形式：要求使用最小化偏差的技术、遵循搜索相关原始研究（通常为实证研究）的协议和标准、明确纳入排除标准、规定可接受的方法论严谨性标准、界定纳入研究的范围、采用团队方法减少偏差、采用一致且明确的方法综合来自不同研究的信息，并得出谨慎的结论和建议（Evans & Benefield, 2001, p. 529; Hemsley-Brown & Sharp, 2003）。正是这些标准使系统综述区别于传统叙事综述——后者更宽泛且选择标准更不明确（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, pp.384–385]]）。
>
> 系统综述通常作为[[Meta-analysis|元分析]]的前置步骤：先通过系统综述识别符合条件的研究，再对这些研究的[[Effect Size|效应量]]进行统计综合。但系统综述本身也可以独立于元分析存在——当纳入研究的结果无法量化合并时，系统综述仍可提供结构化的证据总结。
>
> 研究综合追求两个并行目标：发现表面上相似的主要研究之间的**一致性**，同时**解释研究之间的变异性（Cooper & Hedges, 1994, p. 4）**，从而在所用研究的限度和情境内得出推广性结论（Davies, 2000, p. 366）。

> [!method-scope] 方法范围
> - **研究对象** 已发表的实证研究[[Document|文献]]，包括[[Quantitative Research|定量研究]]、[[Qualitative Research|质性研究]]和[[Mixed Methods Research|混合方法研究]]；也可纳入灰色文献和未发表研究以减少[[Publication Bias|发表偏倚]]。
> - **问题类型** 适合回答评价性问题——"什么有效？""对谁有效？""在什么条件下有效？"——也可处理描述性和比较性问题。
> - **分析单位** 单项研究（study-level）为基本分析单位；也可按干预类型、人群特征或研究设计进行亚组分析。
> - **输出形式** 系统综述报告——包含纳入研究清单、质量评估、综合结论和政策建议；定量综合时输出[[Effect Size|效应量]]汇总。

> [!citation-card]- Evans & Benefield (2001) 的系统综述定义
> 系统综述要求使用最小化偏差的技术、遵循搜索相关原始研究（通常为实证研究）的协议和标准、明确纳入排除标准、规定可接受的方法论严谨性标准、界定纳入研究的范围、采用团队方法减少偏差、采用一致且明确的方法综合来自不同研究的信息，并得出谨慎的结论和建议。（Evans & Benefield, 2001, p. 529; Hemsley-Brown & Sharp, 2003）
>
> *Systematic reviews require the use of techniques to minimize bias, they follow protocols and criteria for searching for relevant primary, usually empirical, studies, their inclusion and exclusion, the standards for acceptable methodological rigour, their relevance to the topic in question, the scope of the studies included, team approaches to reviewing in order to reduce bias, the adoption of a consistent and clearly stated approach to combining information from across different studies, and the careful, relevant conclusions and recommendations drawn.*

---

### 研究综合的类型

研究综合（Research Synthesis）是一个更广泛的伞式术语，涵盖将多篇研究和综述汇集为单一专家报告的一系列方法，可结合定性和定量研究（Davies, 2000; Dixon-Woods et al., 2005）（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, pp.385–386]]）。系统综述是其中更严格、更少"叙事"色彩的形式。

> [!taxonomy] 研究综合的常见形式
> | 方法 | 描述 | 来源 |
> |---|---|---|
> | **叙事综述与总结** | 对研究发现进行叙述性总结 | — |
> | **投票计数综述** | 计数有多少结果在一个方向上有[[Statistical Significance\|统计显著性]]，多少无效应 | Davies, 2000, p. 367 |
> | **最佳证据综合** | 基于明确标准和方法论选择研究 | Slavin, 1986 |
> | **元[[Ethnography\|民族志]]** | 总结和综合来自民族志和解释性质性研究的证据 | — |
> | **主题分析** | 基于主题的综合 | — |
> | **[[Grounded Theory\|扎根理论]]** | 使用扎根理论方法综合 | — |
> | **元研究** | 对研究的研究进行综合 | — |
> | **实在论综合** | 关注干预"为什么有效、对谁有效、在什么条件下有效" | — |
> | **质性数据分析技术** | 基于 Miles & Huberman（1984）的跨案例和案例内分析 | — |
> | **[[Content Analysis\|内容分析]]** | 对研究内容的系统分析 | — |
> | **案例调查** | 对多个[[Case Study\|案例研究]]的调查综合 | — |
> | **质性比较分析** | 跨案例的质性比较 | — |

关于定性研究综合的进一步介绍，教材指引读者参阅 Howell Major & Savin-Baden（2010）（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, p.385]]）。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** [[Positivism|实证主义]]倾向——通过系统、透明、可重复的程序减少研究者主观偏差，追求可累积的证据基础。但同时承认纳入标准的设定和[[Coding in Qualitative Research|编码]]分类涉及研究者的概念判断。
> - **研究者角色** 中立的证据收集与评估者。团队方法（多个研究者独立筛选和编码）是减少个体偏差的核心手段。
> - **有效性标准** 方法透明度、可复制性、可更新性；搜索穷尽性；[[Intercoder Agreement|编码者间信度]]（[[Inter-Rater Reliability]]，即[[Reliability|信度]]的一种形式）；纳入研究的质量评估。
> - **不声称回答的问题** 不能替代一手研究产生新数据；不能直接解决因果方向问题（除非纳入的研究本身已通过[[Randomised Controlled Trials|随机对照试验]]等方法建立了[[Causality|因果关系]]）；结论的[[External Validity|可推广性]]受纳入研究的范围和质量的限制。

> [!method-stack] 方法层级
> - **研究设计** 系统综述设计，遵循预设协议——如 PRISMA（Preferred Reporting Items for Systematic Reviews and Meta-Analyses）、[[EPPI-Centre]] 框架、Cochrane 手册（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, pp.386–397]]）。
> - **数据收集** 数据库检索（如 ERIC、SSCI、Scopus）、参考[[Document|文献]]追踪、灰色[[Literature Search|文献搜索]]、专家咨询、手工检索关键期刊。
> - **分析方法** [[Coding in Qualitative Research|编码]]与主题分析（定性综合）；[[Effect Size|效应量]]汇总（定量[[Meta-analysis|元分析]]）；投票计数；叙事综合；质性比较分析。
> - **辅助技术** 双重筛选（dual screening）、偏倚风险评估工具、PRISMA 流程图（记录检索→筛选→纳入的流程）、编码者间信度检验。

---

## 研究程序

> [!proc] 通用程序
>
> > [!step] 步骤一：制定[[Research Question|研究问题]]与纳入标准
> > 明确界定要回答的[[Research Question|研究问题]]，并预先确定哪些研究符合纳入条件。纳入标准通常涉及研究设计（如是否为[[Randomised Controlled Trials|随机对照试验]]）、参与者特征（如学龄儿童）、干预类型（如语音教学）和结果测量（如阅读理解测试分数）（[[Argument_Higgins_2016_RE|Higgins, 2016, p.32]]）。
>
> > [!step] 步骤二：系统搜索
> > 使用多种数据库和搜索策略尽可能全面地识别符合条件的研究。搜索策略需要透明记录，以便他人重复。Sipe & Curlette（1997）的[[Meta-meta-analysis|元综合]]从 427 项研究中通过严格纳入标准筛选出 103 项（[[Argument_Higgins_2016_RE|Higgins, 2016, p.43]]）。
>
> > [!step] 步骤三：筛选与质量评估
> > 对检索到的[[Document|文献]]进行双重筛选（至少两位研究者独立判断），并评估每项纳入研究的方法论质量。这一步骤直接影响后续[[Meta-analysis|元分析]]的[[Reliability|可靠性]]（[[Argument_Higgins_2016_RE|Higgins, 2016, p.38]]）。
>
> > [!step] 步骤四：数据提取与综合
> > 从纳入研究中提取相关数据，进行定性综合或定量[[Meta-analysis|元分析]]。提取的[[Variable|变量]]通常包括[[Independent Variable|自变量]]、[[Dependent Variable|因变量]]、[[Effect Size|效应量]]、研究设计和样本特征等。

三个主要操作框架在阶段划分上有差异，但核心逻辑一致：

> [!contrast-table] 操作框架的阶段对应
> | 核心任务 | 通用程序 | [[EPPI-Centre]] | Evans & Benefield | Cooper |
> |---------|---------|------------|-------------------|-------|
> | **设定问题与范围** | 制定问题与纳入标准 | 综述方法 → 启动 | 1 明确研究问题 | 1 形成问题 |
> | **系统搜索文献** | 系统搜索 | 收集与描述研究（前半） | 2 系统、全面、穷尽搜索 | 2 搜索文献 |
> | **筛选与质量评估** | 筛选与质量评估 | 收集（后半）→ 评估（前半） | 3 纳入排除标准 + 4 评估方法论质量 | 3 收集信息 + 4 评估质量 |
> | **综合、报告与传播** | 数据提取与综合 | 评估（后半）→ 使用综述 | 5 减少偏差策略 + 6 方法论透明度 | 5 整合 + 6 解释 + 7 呈现 |

其中 Evans & Benefield 的纳入排除标准最为详尽，明确了数据提取应包括：发表状态、引用细节、语言、关键词、资助来源、研究类型、干预性质、样本特征、研究规划和过程、结果评估，以及研究的描述性数据——资助来源、干预内容、人群与抽样、干预和研究的设计规划（Evans & Benefield, 2001, p. 537）。

EPPI-Centre 在上述阶段模型之外，还提出了七项独立于操作步骤的**质量标准**（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, pp.386–389]]）：

> [!feature] EPPI-Centre 的系统综述七项质量标准
> - **明确、严格和透明的方法** 必须系统性地应用
> - **基于明确标准综合研究** 以避免偏差
> - **遵循标准阶段** 一套既定的操作阶段
> - **可问责、可复制、可更新**
> - **对用户具有相关性和实用性**
> - **旨在回答特定研究问题**
> - **以证据为基础**

**英国教育研究协会（British Educational Research Association，BERA）** 也发布了系统综述操作指南，涵盖系统综述问题的制定、概念框架与纳入/排除标准，并提供进一步阅读资源（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, pp.392–393]]）。

> [!warning] Davies (2000, p. 373) 的警示
> Davies 警告研究者确保系统综述不要选择性地使用证据来制造"大多数教育干预的正面效应"的印象——即这些结论可能是综述本身方法论的产物——并确保[[Statistical Significance|统计显著性]]不凌驾于教育显著性之上。这一警示对元分析和研究综合同样适用（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, pp.397–398]]）。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 当某一研究领域已积累大量原始研究，需要结构化地识别和总结证据时；当需要为[[Meta-analysis|元分析]]提供可重复的输入时；当政策或实践决策需要基于尽可能全面的证据而非选择性引用时。[[EEF Teaching and Learning Toolkit]] 的编制就依赖系统综述来识别各领域的元分析证据（[[Argument_Higgins_2016_RE|Higgins, 2016, p.47]]）。
> - **谨慎使用** 当研究领域内研究[[Heterogeneity|异质性]]极高、测量工具和研究设计差异过大时——纳入标准可能难以在全面性和可比性之间取得平衡；当原始研究普遍存在方法论缺陷时——系统综述的质量取决于底层研究的质量。
> - **不适合使用** 当研究领域[[Document|文献]]量极小（如新兴领域只有寥寥数篇研究）——不足以构成"系统综述"的必要规模；当需要产生新数据或探索全新[[Hypothesis|假设]]时——系统综述只能综合已有证据，不能替代一手研究。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 搜索策略的完整性直接影响结论的[[Reliability|可靠性]]——即使系统搜索也可能遗漏未发表的研究，导致[[Publication Bias|发表偏倚]]（[[Argument_Higgins_2016_RE|Higgins, 2016, p.35]]）。纳入标准的设定涉及主观判断——标准过严可能排除有价值的数据，标准过宽可能引入低质量研究。Eysenck 的"垃圾进，垃圾出"批评和 Glass 的回应反映了这一两难（[[Argument_Higgins_2016_RE|Higgins, 2016, p.38]]）。
> - **适用边界** 系统综述的质量取决于底层研究的质量。即使搜索和筛选过程完全透明，如果原始研究本身存在设计缺陷或报告偏差，综述结论仍可能误导。
> - **误用风险** 选择性使用证据以制造"正面效应"印象（见上文 Davies 警示）；将[[Statistical Significance|统计显著性]]凌驾于教育显著性之上；未经充分[[Evaluation Research|评估研究]]质量即纳入综合。
> - **补救方式** 使用未发表研究和灰色[[Document|文献]]补充数据库检索；采用双重筛选和[[Intercoder Agreement|编码者间信度]]检验；使用偏倚风险评估工具；遵循 PRISMA 或 [[EPPI-Centre]] 等标准化报告框架。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Meta-analysis]] | 后续方法 | 系统综述识别和筛选研究后，元分析对[[Effect Size\|效应量]]进行统计综合；系统综述是元分析的前置步骤，但也可独立使用 |
> | [[Meta-meta-analysis]] | 扩展方法 | 对多项元分析进行再综合，是系统综述在更高层级的应用 |
> | [[Coding in Qualitative Research]] | 分析技术 | 系统综述中纳入研究的特征编码（如研究设计、样本、效应量）依赖编码技术 |
> | [[Randomised Controlled Trials]] | 主要输入 | 系统综述（尤其是[[Evidence-Based Education\|循证教育]]中的系统综述）最常纳入的研究类型 |
> | [[Qualitative Research]] | 输入类型 | 系统综述可综合质性研究，使用元民族志、主题分析等方法 |
> | [[Quantitative Research]] | 输入类型 | 系统综述最常综合的研究类型，提供效应量等可量化指标 |
> | [[Grounded Theory]] | 综合方法 | 作为研究综合的一种质性方法，可用于对多项研究进行扎根理论综合 |
> | [[Ethnography]] | 综合对象 | 元民族志（meta-ethnography）专门综合民族志和解释性质性研究 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - **[[Argument_Higgins_2016_RE|Higgins (2016)]]** 系统综述的方法论教材，涵盖[[Research Question|研究问题]]制定、纳入标准、系统搜索、质量评估和数据综合的完整操作框架。
> - **[[Argument_Li_2025_HSSC|Li et al. (2025)]]** 按照 PRISMA 框架从 SSCI and Scopus 数据库系统检索并筛选 85 篇 [[PISA]] 政策影响实证研究，使用[[Coding in Qualitative Research|编码]]分析和序列分析方法探讨 PISA 对全球基础教育改革的影响。
> - **[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al. (2011, Ch17)]]** 教材第 17 章节系统介绍了系统综述与研究综合的定义、类型、操作标准（[[EPPI-Centre]]、BERA、Evans & Benefield、Cooper 等框架）与方法论警示。
