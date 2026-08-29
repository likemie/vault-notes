---
title: Cluster Randomized Trials
aliases:
  - 集群随机试验
  - 整群随机试验
  - 群组随机对照试验
  - 集群随机对照试验
  - Cluster RCT
  - CRCT
  - group-randomized trials
  - cluster-randomized trial
summary: "以自然群体（学校、班级或社区）为随机分配单位、以个体学生为测量单位的实验设计，WWC将其列为必须严格实施群内相关（ICC）与自由度校正的核心设计。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 31
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/cluster-rct
  - method/experimental-design
  - method/quantitative
  - causal-inference
  - multilevel-modeling
related_concepts:
  - "[[Standard Error]]"
  - "[[Statistical Significance]]"
  - "[[Classroom Management]]"
  - "[[Academic Achievement]]"
  - "[[Effect Size]]"
  - "[[Type I and Type II Errors]]"
  - "[[Epistemology]]"
  - "[[Peer-Supported Learning]]"
  - "[[Internal Validity]]"
  - "[[Sample Size Determination]]"
  - "[[Implementation Fidelity]]"
  - "[[Pre-test and Post-test]]"
  - "[[Attrition]]"
related_theories:
  - "[[Campbellian Validity Framework]]"
related_methods:
  - "[[Randomised Controlled Trials]]"
  - "[[Random Assignment]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Analysis of Variance]]"
  - "[[Quasi-Experimental Designs]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[What Works Clearinghouse]]"
  - "[[Success for All]]"
  - "[[Peer-Assisted Learning Strategies]]"
  - "[[Communities in Schools]]"
  - "[[Blueprints for Healthy Youth Development]]"
  - "[[California Evidence Based Clearinghouse for Child Social and Economic Welfare]]"
  - "[[National Dropout Prevention Center]]"
  - "[[Collaborative for Academic Social and Emotional Learning Guide]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Slavin_2002_ER]]"
confidence: high
status: active
created: 2026-08-22
updated: 2026-08-22
---

# Cluster Randomized Trials

---

## 定义

> [!def] 方法定义
> **集群随机试验（Cluster Randomized Trials, CRCT）**，亦称**整群随机试验**或**群组[[Randomised Controlled Trials|随机对照试验]]（Group-Randomized Trials, GRT）**，是指将完整的自然群体（如学校、班级、学区或社区）而非单个个体作为[[Random Assignment|随机分配]]（Random Assignment）的基本单位，而在群体内部的个体（如学生、教师）层面收集数据并评估干预效果的真实实验设计([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, pp. 316–318]]; [[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p. 1327]])。
>
> 在教育与社会政策研究中，CRCT 是实施全校性教学改革与课程干预最核心的量化方法。其核心统计特征在于：同属一个集群（如同一班级）的学生在背景和行为上天然存在相关性，违反了经典统计学的“独立同分布（IID）”假定；若未进行**群组内相关系数（Intraclass Correlation Coefficient, ICC）**与多层线性模型（HLM）校正，将严重低估[[Standard Error|标准误]]并制造虚假的[[Statistical Significance|统计显著性]]。在美国教育部 [[What Works Clearinghouse|WWC]] 审查规程中，未做集群校正的试验将被系统性降级([[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, pp. 8–10]])。

> [!method-scope] 方法范围
> - **研究对象** 必须以全校或全班为单位推行的教育干预（如全校读写改革 [[Success for All]]、班级同伴辅导 [[Peer-Assisted Learning Strategies]]、全校综合支持 [[Communities in Schools]]、[[Classroom Management|课堂管理]]系统 PBIS）。
> - **问题类型** 评估群体级教学策略、教育政策与组织变革对个体[[Academic Achievement|学业成就]]、心理发展及行为规范的因果净效应。
> - **分析单位** 分配单位为第二层集群（Level-2，学校/班级），测量单位为第一层微观个体（Level-1，学生）。
> - **输出形式** 多层线性模型（HLM）固定效应估计值、群组内相关系数（ICC / $\rho$）、设计效应（Design Effect）、校正后标准误与调整后[[Effect Size|效应量]]（Hedges' $g$）。

> [!citation-card]- 关键定义
> 当干预措施必须在自然组织单元（如学校或班级）整体实施，或者个体间存在严重的干预溢出污染时，集群随机化是唯一的实验选择。然而，分析单位与分配单位的错位构成了严峻的统计挑战，必须显式建模集群层级的变异。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, p. 317)]]
>
> *Cluster randomized trials assign intact social units rather than individuals to experimental conditions. While preventing treatment spillovers in classroom settings, they introduce positive intraclass correlation that inflates [[Type I and Type II Errors|Type I error]] rates if not modeled through multilevel hierarchical frameworks.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **认识论取向** 承认学校教育系统具有嵌套性（Nested Structure）与生态学特征，认为将学生个体从其所属班级与同伴生态中生硬剥离[[Random Assignment|随机分配]]是不切实际的还原主义。
> - **因果防污染优势** 彻底阻断了同一教室内学生之间的**处理扩散与污染（Treatment Spillover / Contamination）**。若在同一教室内将一半学生随机分入新教学法、另一半维持传统法，教师难以做到双轨授课且[[Peer-Supported Learning|同伴互助]]会导致干预外溢；集群分配将整个班级或学校整体归入干预组，捍卫了[[Internal Validity|内部效度]]。
> - **统计功效代价** 相同[[Sample Size Determination|样本量]]下，集群 [[Randomised Controlled Trials|RCT]] 的统计功效（Statistical Power）远低于个体级 RCT。决定检验力高低的关键在于**集群数量（Number of Clusters, $K$）**，而非集群内的学生个体数（$m$）。

> [!method-stack] 方法层级
> - **设计形态** 平行双组集群 RCT（Parallel CRCT）、阶梯楔形集群试验（Stepped-Wedge CRCT）、因子集群试验（Factorial CRCT）。
> - **数据结构** 两层或三层嵌套面板数据（学生嵌套于班级，班级嵌套于学校）。
> - **计量估计技术** 多层线性模型（HLM / [[Fixed-Effect and Random-Effects Models|随机效应模型]]）、广义估计方程（GEE）、集群稳健[[Standard Error|标准误]]（Cluster-Robust Standard Errors, CRSE）、置换检验（Permutation Test）。

---

## 研究程序

> [!proc] 集群随机试验标准实施六步规程
> 1. **集群抽样与基线评估** 招募足够数量的自然学校或班级（通常要求每组至少 15–30 个集群以上），采集学校背景及历史基线成绩。
> 2. **实施集群层级[[Random Assignment|随机分配]]** 在学校或班级层面进行完全随机化（可结合学区或生源特征进行分层块随机分配 Stratified Block Randomization）。
> 3. **全集群现场干预与保真度监控** 干预校全员落实新课程方案，对照校维持常规教学（BAU），同步监控集群层级的[[Implementation Fidelity|实施保真度]]。
> 4. **个体层级[[Pre-test and Post-test|后测]]数据收集** 跟踪全校学生采集后测指标，分别核查**集群层级[[Attrition|流失]]（Cluster Attrition）**与**个体层级流失（Sub-cluster Attrition）**。
> 5. **构建多层统计估计模型** 采用 HLM 或混合效应模型显式估计群内相关系数 $\rho$，剥离集群间方差与集群内方差。
> 6. **实施自由度校正与稳健性检验** 针对小样本集群（如学校数 $< 30$），采用 Satterthwaite 或 Kenward-Roger 自由度调整，防止过失显著性（Type I Error）。

---

### 集群效应膨胀与数理校正模型

> [!formula-step] 群内相关（ICC）与设计效应（Design Effect）计量模型
> 
> 1. **群组内相关系数（Intraclass Correlation Coefficient, ICC / $\rho$）**
>    $$\rho = \frac{\sigma_B^2}{\sigma_B^2 + \sigma_W^2}$$
>    - **$\sigma_B^2$** 集群间方差（Between-cluster Variance，反映不同学校之间的学业差异）；
>    - **$\sigma_W^2$** 集群内方差（Within-cluster Variance，反映同校内部不同学生之间的个体差异）；
>    - 在美国教育实证研究中，标准化考试的典型 ICC 通常在 **$0.10$ 至 $0.25$** 之间。
>
> 2. **设计效应（Design Effect, $\text{Deff}$）与有效[[Sample Size Determination|样本量]]（Effective Sample Size）**
>    $$\text{Deff} = 1 + (m - 1) \cdot \rho$$
>    $$N_{\text{effective}} = \frac{N_{\text{total}}}{\text{Deff}} = \frac{K \cdot m}{1 + (m - 1) \cdot \rho}$$
>    - **$m$** 每个集群的平均学生人数；**$K$** 集群总数；
>    - **效应膨胀机理** 若每班 30 名学生（$m=30$），$\rho = 0.20$，则 $\text{Deff} = 1 + 29 \times 0.20 = 6.8$。这意味着名义上收集了 680 名学生数据，其真实的统计信息量仅等价于 **100 名独立个体**！
>
> 3. **两层多层线性模型（Hierarchical Linear Model, HLM）**
>    - **个体层（Level-1）** $Y_{ij} = \beta_{0j} + \beta_{1j} X_{ij} + \varepsilon_{ij}, \quad \varepsilon_{ij} \sim N(0, \sigma_W^2)$
>    - **集群层（Level-2）** $\beta_{0j} = \gamma_{00} + \mathbf{\gamma_{01}} \cdot \text{Treat}_j + \mu_{0j}, \quad \mu_{0j} \sim N(0, \sigma_B^2)$
>    - **$\gamma_{01}$** 核心因果净处理效应（剥离了学校间差异的稳健参数）。

---

### 清算中心对集群试验的技术审查盲区

> [!contrast-table] 循证清算中心对集群处理的技术审查对比（基于 Wadhwa et al., 2024）
> | 审查维度 | [[What Works Clearinghouse\|WWC]] (联邦官方) | [[Blueprints for Healthy Youth Development\|Blueprints]] / [[California Evidence Based Clearinghouse for Child Social and Economic Welfare\|CEBC]] | [[National Dropout Prevention Center\|NDPC]] / [[Collaborative for Academic Social and Emotional Learning Guide\|CASEL]] |
> |:---|:---|:---|:---|
> | **集群效应审查技术** | **独立重算与强制纠偏**，若原作者未做 HLM，WWC 自行根据行业 ICC 常模重新膨胀标准误并重估 $p$ 值。 | 要求原作者在论文中报告适当的多层模型或集群稳健[[Standard Error\|标准误]]（CRSE）。 | **普遍缺乏集群识别能力**，直接采信未校正的单层 OLS 显著性结论。 |
> | **自由度惩罚与集群数底线** | 对集群数较少（如单组 $< 5$ 个班）的研究实施小样本惩罚，限制评级上限。 | 考察集群规模与分析单位一致性，淘汰存在严重单位错位的研究。 | 未设置集群数量底线要求。 |
> | **流失模型扩展** | 实施双重流失核验：**集群整体流失**（学校退出）与**个体流失**（学生退出）。 | 要求对脱落集群与留存集群实施平衡性检验。 | 仅考察总体表面样本变化。 |

---

## 适用场景

> [!fit-grid] 适用判断
> - **适合使用** 全校综合改革（CSR）、新教材与教学模式在整班维度的试点、班级师资培训项目、旨在重塑学校文化或校风的干预方案。
> - **谨慎使用** 能够招募的学校/班级总数极少（如总共只有 4–6 所学校），此时即使每校包含千名学生，统计功效依然极其匮乏。
> - **不适合使用** 针对个体学生的电脑自适应辅导软件（无同伴扩散风险时应优先采用个体级 [[Randomised Controlled Trials|RCT]] 以最大化统计功效）。

---

## 局限性

> [!method-limits] 效度威胁、偏误来源与误用风险
> - **单位错位分析偏误（Unit-of-Analysis Error）** 绝大多数误用源于研究者将 $N$ 记为学生总数直接套用普通 [[Analysis of Variance|ANOVA]] 或 $t$ 检验，虚假膨胀 $t$ 值导致原本不显著的结果呈现出伪显著性。
> - **招募成本极其高昂** 为达到 80% 统计功效，通常需要动员数十所学校参与，招募难度、行政协调与财政激励成本呈指数级上升([[Argument_Slavin_2002_ER|Slavin, 2002, p. 18]])。
> - **集群级[[Attrition|流失]]的致命破坏** 若干预组中有 1 所学校因校长更迭整体退出，将直接损失 10%–25% 的核心有效样本，严重摧毁组间基线平衡。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Randomised Controlled Trials]] | 母类方法 | CRCT 是 RCT 在群体组织嵌套情境下的高级拓展形态。 |
> | [[Quasi-Experimental Designs]] | 替代设计 | 当集群数量无法满足[[Random Assignment\|随机分配]]时，研究常被迫退化为非等对控制组 QED。 |
> | 多层线性模型（HLM） | 分析工具 | CRCT 正确估计[[Standard Error\|标准误]]与群间方差的核心计量分析方法。 |
> | [[Campbellian Validity Framework]] | 理论基础 | CRCT 通过组织隔离有效消除处理扩散（Diffusion of Treatments）威胁。 |
> | [[What Works Clearinghouse]] | 评价机构 | 建立了国际最严谨的 CRCT 多层集群校正与自由度审查规则。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 研究索引
> - [[Argument_Wadhwa_2024_RER|Wadhwa et al. (2024)]] — 详析集群处理在 12 所清算中心审查中的系统性分化，揭示未校正 ICC 与分析单位错位是导致虚假显著性评级的核心技术根源(pp. 8–11)。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011)]] — 阐释班级与学校层面的集群[[Random Assignment|随机分配]]操作逻辑、组织污染防范及与准实验的转化界限(Ch. 16, pp. 316–318)。
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022)]] — 规范群组随机分配在教育现场实验中的研究设计程序与多层数据收集要求(Ch. 8, p. 1327)。
