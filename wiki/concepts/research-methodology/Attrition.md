---
title: Attrition
aliases:
  - 流失
  - 实验流失
  - 样本流失
  - experimental mortality
  - attrition bias
  - 流失偏差
  - 实验死亡率
  - 差异流失
  - differential attrition
  - overall attrition
summary: "实验或追踪研究中参与者因各种原因中途脱落导致初始随机等价性被破坏的内部效度威胁，WWC通过整体流失与差异流失二维边界模型度量其潜在因果偏误。"
type: concept
domain: "research-methodology"
related_count: 35
related_level: 3
related_stars: "⭐⭐⭐"
related_color: "#fde68a"
tags:
  - subject/research-methodology
  - experiment
  - bias-control
  - internal-validity
  - causal-inference
related_concepts:
  - "[[Internal Validity]]"
  - "[[Sample Size Determination]]"
  - "[[External Validity]]"
  - "[[Effect Size]]"
  - "[[Causality]]"
  - "[[Pre-test and Post-test]]"
  - "[[Variable]]"
  - "[[Complier Average Causal Effect]]"
  - "[[Paradigm]]"
  - "[[Sampling Error]]"
  - "[[Questionnaire]]"
  - "[[Response Bias]]"
  - "[[Hypothesis]]"
  - "[[Threats to Internal Validity]]"
related_theories:
  - "[[Campbellian Validity Framework]]"
related_methods:
  - "[[Cohort Study]]"
  - "[[Random Assignment]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Intent-to-Treat Analysis]]"
  - "[[Imputation Methods]]"
  - "[[Covariate Adjustment]]"
  - "[[Cross-sectional Study]]"
  - "[[Pilot Testing]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[What Works Clearinghouse]]"
  - "[[Blueprints for Healthy Youth Development]]"
  - "[[Social Programs That Work]]"
  - "[[Clearinghouse for Military Family Readiness Continuum of Evidence]]"
  - "[[National Dropout Prevention Center]]"
  - "[[Success for All]]"
  - "[[Communities in Schools]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge]]"
confidence: high
status: active
created: 2026-07-12
updated: 2026-08-22
---

# Attrition

---

## 定义

> [!def] 概念定义
> **实验流失（Attrition / Experimental Mortality）**，亦称**样本流失**或**受试脱落**，是指在教育实验或纵向[[Cohort Study|追踪研究]]进行期间，部分参与者因转学、缺勤、失去动机、主动放弃或行政失联等原因中途退出，导致最终进入数据分析的样本（Analytic Sample）不再等同于初始[[Random Assignment|随机分配]]样本的现象([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, pp. 333–334]]; [[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p. 1327]])。
>
> 流失的核心破坏力在于：**退出极少是随机发生的**。脱落者与留守者通常在学业基础、家庭支持与动机水平上存在系统性差异，从而破坏了随机分配（Random Assignment）所建立的组间同质性，使原本严密的[[Randomised Controlled Trials|随机对照试验]]（RCT）退化为带有自选择偏误的[[Quasi-Experimental Designs|准实验设计]]。在美国教育部 [[What Works Clearinghouse|WWC]] 审查体系中，流失通过**整体流失率（Overall Attrition）**与**差异流失率（Differential Attrition）**构建二维边界模型进行刚性因果门控审查([[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, p. 8]])。

> [!concept-lens] 效度视角与方法学定位
> - **[[Internal Validity|内部效度]]的核心威胁** 流失不仅使[[Sample Size Determination|样本量]]缩小，更直接动摇了内部效度（Internal Validity）。两组在实验结束后的表现差异，可能完全源于“谁留下来了”而非“干预是否有效”。
> - **与[[External Validity|外部效度]]的张力** 即使采用统计手段维持了内部效度，严重的流失也意味着干预结论只能外推至“有能力坚持完成干预的特定子群体”，从而损害了生态推广的外部效度（External Validity）。
> - **真实验向准实验的滑坡点** 一旦 RCT 发生高流失，该研究即刻丧失“无保留达标（Meets Standards Without Reservations）”的顶级资格，必须强制通过基线等值性重新核查方能获得降级达标。

> [!citation-card]- 关键定义
> 实验死亡率（Experimental Mortality）不仅是样本量的缩减，它从根本上重构了组别成分。如果退出者与保留者存在系统性特征差异，仅分析留守样本（Completers-Only）将产生灾难性的流失偏差，完全扭曲真实的因果[[Effect Size|效应量]]。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, p. 333)]]
>
> *Attrition threatens internal validity because individuals who drop out are often systematically different from those who remain. When dropout rates differ between treatment and control groups, randomization is compromised, requiring rigorous attrition modeling or intention-to-treat adjustments.*

---

## 核心机制与理论模型

> [!mechanism] 流失破坏[[Causality|因果推断]]的三大微观机制
> 1. **脱落者的系统性非随机特征（Non-Random Dropout）** 脱落者通常具有特定的人口学与学业特征（如低收入家庭搬迁频率更高、学业困难生更容易产生挫败感而退出）。排除这部分学生会直接人工拔高留守组的平均成绩。
> 2. **组间非对称/差异流失（Differential Attrition）** 干预组因任务繁重、教学进度快或体验不佳导致高流失，而对照组维持常规照常教学（BAU）流失率极低；两组在[[Pre-test and Post-test|后测]]时的背景失衡直接伪造了虚假[[Effect Size|效应量]]。
> 3. **完工者分析（Completers-Only）的效应量扭曲** 若直接剔除脱落者仅分析坚持到底的学生（Per-Protocol 分析），当脱落者为学困生时效应量被**系统性高估**；当干预过于有效导致轻症学生提前“康复/脱落”时效应量被**系统性低估**。

---

### WWC 流失边界模型与潜在偏误度量

> [!formula-step] [[What Works Clearinghouse|WWC]] 整体与差异流失二维判定模型
> WWC 建立了基于最大潜在因果偏误不超过 **$0.05\text{ SD}$** 的数学边界模型：
>
> 1. **整体流失率（Overall Attrition Rate, $A_{\text{overall}}$）**
>    $$A_{\text{overall}} = \frac{N_{\text{initial\_total}} - N_{\text{analytic\_total}}}{N_{\text{initial\_total}}}$$
>
> 2. **差异流失率（Differential Attrition Rate, $A_{\text{diff}}$）**
>    $$A_{\text{diff}} = |A_{\text{treatment}} - A_{\text{control}}| = \left| \frac{N_{T0} - N_{T1}}{N_{T0}} - \frac{N_{C0} - N_{C1}}{N_{C0}} 
ight|$$
>
> 3. **宽容边界（Liberal Boundary）vs 保守边界（Conservative Boundary）**
>    - **宽容边界（Liberal Curve）** 假定流失主要由与干预内容无关的外生因素（如学区自然家庭搬迁）引起；允许较高的临界差异流失率；
>    - **保守边界（Conservative Curve）** 假定流失可能直接由干预本身的不良体验、繁重负担或学生抵触引起；对差异流失率设定极其严苛的上限。
>    - **裁定分流规则** 处于边界之下的研究被判定为**低流失 [[Randomised Controlled Trials|RCT]]（Low Attrition）**直接维持一级无保留达标；跨越边界的研究被判定为**高流失 RCT（High Attrition）**，必须重新核验分析样本在基线前测上的等值性（Baseline Equivalence）。

---

### 循证清算中心对样本流失的审查门槛对比

> [!contrast-table] 四大清算中心对样本流失的审查门槛对比（基于 Wadhwa et al., 2024）
> | 清算中心 | 流失审查技术模型 | 对高流失研究的补救与降级要求 | 审查严苛度定性 |
> |:---|:---|:---|:---|
> | **[[What Works Clearinghouse\|WWC]] (联邦官方)** | **整体 vs 差异二维连续曲线模型**<br>(严格控制潜在偏误 $\le 0.05\text{ SD}$) | 高流失 RCT 降级为准实验规程；强制要求前测基线差异 $\le 0.25\text{ SD}$ 且控制协变量。 | **极高（数理精细模型）** |
> | **[[Blueprints for Healthy Youth Development\|Blueprints]]** | **脱落者与留守者双重平衡性检验** | 必须在实验组与对照组内部分别对脱落者与保留者实施 $\chi^2$ 或 $t$ 检验，证明无选择偏差。 | **极高（双重平衡检验）** |
> | **[[Social Programs That Work\|SPTW]] / [[Clearinghouse for Military Family Readiness Continuum of Evidence\|CMFR]]** | **单一固定百分比阈值**<br>(通常设定整体流失率 $\le 20\%$ 上限) | 仅粗筛总流失率，未建立精细的差异流失与基线联动补偿模型。 | **中等（粗线条过滤）** |
> | **[[National Dropout Prevention Center\|NDPC]]** | **未设量化流失门槛** | 宽容采纳具备正向实践效果的实证，不因样本流失做制度性降级。 | **包容（实践导向）** |

---

## 统计纠偏与补偿策略

> [!framework-table] 应对流失偏差的四大统计纠偏工具
> | 统计纠偏技术 | 核心操作原理 | 适用场景与优劣势 |
> |:---|:---|:---|
> | **[[Intent-to-Treat Analysis\|意向治疗分析]] (ITT)** | **“一旦随机，永远分析”**；将所有最初[[Random Assignment\|随机分配]]的学生（无论是否中途脱落或未完整接受干预）全部纳入最终分析。 | 彻底捍卫随机化基线等价性，防止虚假高估；缺点是可能稀释干预在足额完成者中的真实潜在功效。 |
> | **基线等值性重新核查 (Baseline Equivalence)** | 丢弃初始样本基线，仅针对最终留在[[Pre-test and Post-test\|后测]]中的分析样本（Analytic Sample）重新检验前测均值与协[[Variable\|变量]]平衡。 | 高流失 RCT 挽救因果资格的唯一通道；若前测差值在 $0.05–0.25\text{ SD}$ 间必须纳入回归协变量调整。 |
> | **多重插补 (Multiple [[Imputation Methods\|imputation]], MI) / FIML** | 依据受试者基线成绩、人口学变量与过程数据，通过统计算法多重填补缺失的后测结果。 | 假定数据为**随机缺失（MAR）**；若属于非随机缺失（MNAR，如最差的学生故意缺考），插补结果仍有偏倚。 |
> | **工具变量法与 [[Complier Average Causal Effect\|CACE]] 估计 (Complier Average Effect)** | 以初始随机分组作为工具变量（IV），剥离脱落与不顺从行为，估计**顺从者平均因果效应（CACE）**。 | 精准识别真正坚持完成干预者的净效应，是现代因果计量经济学纠偏标准[[Paradigm\|范式]]。 |

---

## 概念边界与常见误区

> [!boundary] 概念辨析与适用边界
> - **流失（Attrition） vs 排除偏差（Exclusion Bias）** 流失是指参与者已经入组并启动实验，但在中途退出或[[Pre-test and Post-test|后测]]失联；排除偏差是指研究者在[[Random Assignment|随机化]]分配前依据既定准入标准（如智商低于特定值）系统排除特定对象。
> - **流失偏差 vs 小样本[[Sampling Error|抽样误差]]（Sampling Error）** 小样本导致的偶然不平衡可通过事后[[Covariate Adjustment|协变量控制]]缓解，且样本属性未变；流失是在时间维度上动态改变了受试者总体的概率分布结构。
> - **[[Cross-sectional Study|横截面调查]]（Cross-sectional）不存在实验流失** 流失是纵向时间序列[[Cohort Study|追踪研究]]和干[[Pilot Testing|预实验]]特有的威胁；单次横截面[[Questionnaire|问卷]]中只存在**无[[Response Bias|应答偏差]]（Non-response Bias）**。

---

## 典型应用与反思案例

> [!case] 周六早间数学加强班的自选择流失（[[Argument_Cohen_Manion_Morrison_2011_Routledge|Cohen et al., 2011]]; Torgerson, 2003）
> 一项针对初中数学困难生的自愿周六补习 [[Randomised Controlled Trials|RCT]] 实验中：
> - **初始设计** 200 名学生[[Random Assignment|随机分配]]至补习组（100 人）与对照组（100 人），基线成绩完全等价。
> - **流失过程** 补习组因要求周六早起上课，数周内 30 名学习动机最低、家庭支持最弱的学生相继脱落；对照组学生因无需额外付出，仅自然流失 2 人。
> - **偏差结果** 若仅分析补习组剩余 70 名“勤奋好学”的留守学生，[[Pre-test and Post-test|后测]]平均分显著超越对照组；但这一显著优势完全是由差异流失造成的自选择伪效应，采用 [[Intent-to-Treat Analysis|ITT]] 分析后[[Effect Size|效应量]]即刻归零。

> [!case] 宏观综合学生支持中的人口流动 vs 政策倦怠脱落
> 在全美大型防辍干预项目（如 [[Success for All]]、[[Communities in Schools]]）的多年期评估中：
> - 贫困学区每年面临高达 20%–40% 的自然家庭搬迁流动（符合 [[What Works Clearinghouse|WWC]] 宽容边界[[Hypothesis|假设]]）；
> - 若某一实验校因实施过严导致学生主动转学逃避（符合保守边界假设），研究者必须区分两类流失的微观机理，否则无法向清算中心合理解释[[Internal Validity|内部效度]]。

---

## 相关概念与方法网络

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Internal Validity]] | 核心概念 | 流失是 Campbellian 效度体系中最致命的[[Threats to Internal Validity\|内部效度威胁]]之一。 |
> | [[Intent-to-Treat Analysis]] | 纠偏方法 | 防范流失偏差、保全初始[[Random Assignment\|随机化]]等价性的标准分析方法。 |
> | [[Randomised Controlled Trials]] | 实验方法 | 流失能够直接击穿 RCT 的因果识别前提，使其降级为准实验。 |
> | [[What Works Clearinghouse]] | 评价机构 | 制定了国际最权威的“整体-差异流失”二维数学边界模型。 |
> | [[Campbellian Validity Framework]] | 理论基础 | 将实验死亡率（Experimental Mortality）列为[[Causality\|因果推断]]八大威胁之一。 |

---
