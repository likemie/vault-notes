---
title: Publication Bias
aliases:
  - 发表偏差
  - 发表偏倚
  - 文件抽屉效应
  - File Drawer Effect
summary: "正面或显著结果比零结果或负面结果更可能被发表或传播的系统性倾向，导致已发表文献库系统性高估干预的真实有效性；元分析中常结合漏斗图、Egger检验、剪补法与失安全数进行综合诊断与稳健性校正"
type: concept
domain: "research-methodology"
related_count: 32
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - publication-bias
  - file-drawer-effect
  - meta-analysis
  - research-methodology
  - evidence-based-education
related_concepts:
  - "[[Document]]"
  - "[[Critique of Meta-analysis]]"
  - "[[Developer Effect]]"
  - "[[Hypothesis]]"
  - "[[Evaluator Independence]]"
  - "[[Cumulative Knowledge Base]]"
  - "[[Categorical Funding]]"
  - "[[Knowledge Mobilisation]]"
  - "[[Researcher Degrees of Freedom]]"
  - "[[Visible Learning]]"
  - "[[Preregistration]]"
  - "[[Higher-Order Thinking Skills]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Meta-analysis]]"
  - "[[Systematic Review]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Quantitative Research]]"
  - "[[Experimental Research]]"
  - "[[Funnel Plot]]"
  - "[[Trim and Fill Method]]"
  - "[[Fail-Safe N]]"
related_persons: []
related_facts:
  - "[[What Works Clearinghouse]]"
  - "[[Creation of REES]]"
  - "[[Every Student Succeeds Act]]"
related_arguments:
  - "[[Argument_Wolf_2020_JREE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
  - "[[Argument_Revai_2022_ChangingLandscape]]"
  - "[[Argument_Higgins_2016_ROE]]"
  - "[[Argument_Kraft_2023_ER]]"
  - "[[Argument_Wecker_2016_ZfE]]"
  - "[[Argument_Zhao_2025_JIntell]]"
  - "[[Argument_Cartiff_2021_JEP]]"
confidence: high
status: active
created: 2026-05-02
updated: 2026-09-21
---

# Publication Bias

## 定义

> [!def] 核心定义
> 发表偏倚（Publication Bias），也称文件抽屉效应（File Drawer Effect），指具有统计显著性或正向结论的研究比零效应或负面结果的研究更有可能被学术期刊接收、发表或传播的系统性倾向。在教育实证与教学干预评估中，发表偏倚意味着公开学术[[Document|文献]]库中的加权平均[[Effect Size|效应量]]往往系统性高估了干预措施的真实有效性（Rosenthal, 1991; [[Argument_Wolf_2020_JREE|Wolf et al., 2020, p. 429]]）。

在现代循证教育评价中，发表偏倚被视为威胁实证合成内部效度的关键偏倚源。元分析研究者通常通过漏斗图（[[Funnel Plot]]）、Egger 线性回归、剪补法（[[Trim and Fill Method]]）以及失安全数（[[Fail-Safe N]]）等多重统计工具对发表偏倚进行系统性审计与效应量下调校正。

> [!concept-lens] 概念透镜
> - **含义** 学术出版与资助体系对显著和正面结果的选择性偏好，使公开证据池系统性右偏并脱离真实因果分布。
> - **用途** 帮助[[Meta-analysis|元分析]]研究者识别和校正证据库的不完整性，为政策制定者提供“公开证据本身可能已被筛选”的警惕与审慎依据。
> - **边界** 发表偏倚不等于有意学术造假，它往往源于学术期刊的出版偏好、研究者的发表激励或资助方的经济利益驱动。

> [!citation-card] 认识论元分析中的发表偏倚稳健性检验
> 绘制标准误与 Fisher's Z 漏斗图并结合剪补法虚拟填补 6 项缺失研究后，效应量从 $d = 0.509$ 下调为 $d = 0.342$，依然高度显著；失安全数检验表明需要 2,593 项未发表的零效应研究才能推翻结论，确立了因果促学效应经受住了发表偏倚的稳健性考验。[[Argument_Cartiff_2021_JEP|(Cartiff et al., 2021, pp. 484–485)]]
>
> *Visual inspection of the funnel plot suggested possible publication bias. Duval and Tweedie’s trim and fill procedure imputed six studies, adjusting the overall effect to d = 0.342 (95% CI [0.155, 0.528]), which remained statistically significant. Rosenthal’s fail-safe N indicated that 2,593 null-effect studies would be needed to reduce the effect size to non-significance.*

> [!boundary]- 概念边界
> - 不等于选择性报告偏倚（Selective Outcome Reporting） 发表偏倚指整篇研究由于非显著而被锁在“文件抽屉”中（研究级 Study-level）；选择性报告偏倚指同一篇研究内部研究者选择性报告达到显著的结果指标而隐瞒不显著指标（发现级 Finding-level）。[[Argument_Wolf_2020_JREE|(Wolf et al., 2020, p. 441)]]
> - 不等于[[Developer Effect|开发者效应（Developer Effect）]] 发表偏倚是开发者效应的一个子机制（约贡献 66%），但开发者效应还涵盖干预实施保真度高、测量工具过度对齐等其他实质机制。
> - 不等于[[Researcher Degrees of Freedom|研究者自由度（Researcher Degrees of Freedom）]] 研究者自由度发生在数据收集与分析阶段（如灵活调整协变量或离群值剔除标准），而发表偏倚发生在论文投稿与同行评审的传播环节。

---

## 概念辨析

> [!contrast-table] 偏倚类型与方法学属性辨析
> | 偏倚类型 | 发生阶段 | 作用层级 | 核心机制 | 典型校正与防范方案 |
> |---|---|---|---|---|
> | **[[Publication Bias\|发表偏倚]]（Publication Bias）** | 成果投稿与出版传播 | 研究级（整篇论文未面世） | 期刊偏好正面“好故事”、资助方压制零结果 | 剪补法、失安全数、[[Preregistration\|研究预注册]]、注册报告 |
> | **选择性报告偏倚（Selective Reporting）** | 数据整理与手稿撰写 | 指标级（单篇内隐瞒部分指标） | 仅汇报 $p < .05$ 的结局变量，隐藏不显著测量 | 方案预注册、多结局指标全量核对表 |
> | **[[Researcher Degrees of Freedom\|研究者自由度]]（Researcher Degrees of Freedom）** | 数据分析与模型建构 | 过程级（模型与样本调试） | p-hacking、事后合理化假设（HARKing）、反复调整缩尾阈值 | 盲态分析、多分析团队验证、预注册分析计划 |
> | **[[Developer Effect\|开发者效应]]（Developer Effect）** | 干预研发、实施与评估全周期 | 方案级（研发者亲自主导实验） | 开发者额外支持提高保真度、自编测验过度对齐、对负面结果选择性发表 | 强制[[Evaluator Independence\|第三方独立评估]]、采用标准化统考测验 |

---

## 核心要素

### 1. 诱发机制与知识生态危害

> [!feature] 发表偏倚的多重诱因与生态后果
> [[Argument_Wolf_2020_JREE|Wolf et al. (2020, p. 429)]] 与 [[Argument_Revai_2022_ChangingLandscape|Révai (2022, p. 22)]] 揭示了教育研究中发表偏倚的多重动因及其系统性危害：
> - **学术发表压力与期刊偏好** 研究者面临晋升与学术考评压力，商业学术期刊系统性偏爱“引人注目、反常识、显著”的理论证实性研究，零效应与复现研究往往被拒稿。
> - **资助者与开发者的利益驱动** 商业教学产品提供方与项目方有极强动机压制负面评估；即使是受雇的评估团队，也容易因顾及委托方关系而弱化不利结论。
> - **阻滞累积性知识库建构** 出版生态对显著正向结果的偏爱导致实证证据碎片化，排斥了零结果与情境复现研究，阻碍了教学改进所需[[Cumulative Knowledge Base|累积性知识库]]（Cumulative Knowledge Base）的生成，使循证决策者难以辨识真实可靠的有效实践（Burkhardt & Schoenfeld, 2003）。

### 2. 诊断与统计校正方法族

在现代元分析报告规范中，发表偏倚的诊断与校正已形成严密的多工具互证规程：

> [!tools] 发表偏倚核心诊断与校正方法族
> - **漏斗图（Funnel Plot）目视诊断** 以效应量为横轴、样本量或标准误为纵轴绘制散点图；在无偏倚情境下散点呈对称倒漏斗状；若左下角（小样本零结果/负结果）出现明显缺失，提示存在偏倚。
> - **Egger 线性回归检验** 对漏斗图的不对称性进行定量参数检验，以标准化效应量对测量精度进行回归，通过截距项显著性判定漏斗图是否存在统计学不对称。
> - **剪补法（Duval & Tweedie Trim and Fill）** 非参数迭代算法，首先“剪除”导致不对称的极端研究以估计对称中心，随后沿中心对称轴“虚拟填补”缺失的对侧研究，重新计算校正后的合并效应量与置信区间。[[Argument_Cartiff_2021_JEP|(Cartiff et al., 2021, p. 484)]]
> - **Rosenthal 经典失安全数（Fail-Safe N）** 计算需要多少项效应为零的未发表研究，才能将当前元分析的合并显著性水平压低至临界值（$\alpha = .05$）；失安全数远超 $5k + 10$ 时，表明结论抗偏倚性强。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|(Cohen et al., 2011, Ch17, p. 355)]]
> - **Orwin 失安全数** 针对效应量大小而非单纯 p 值的指标，计算需要多少项零效应研究才能将加权平均效应量降低至具有实质教学意义的阈值以下（如 $d = 0.20$）。[[Argument_Cartiff_2021_JEP|(Cartiff et al., 2021, p. 485)]]
> - **极端离群值缩尾（Winsorization）** 在开展偏倚检验前，对 Grubbs' 检验检出的极端离群效应量进行缩尾处理（如将 $d = 3.2$ 缩尾至次大值 $d = 2.6$），防止单项极端值扭曲漏斗图基线。

---

## 围绕概念形成的命题

---

### 命题一　学术发表系统的正向偏好通过压制零效应导致元分析平均效应量系统性虚高

> [!concept-lens] 证据池扭曲与效应虚增机制
> 探讨学术期刊与资助生态对显著结果的偏爱如何系统性抬高公开文献库中的平均效应量，导致教育实践的有效性被普遍高估。

> [!claim] Kraft, M. A.
> **实证效应分布右偏与干预失败率低估** 基于全美随机对照试验（RCT）大样本经验分布指出，已发表文献中的效应量分布已被发表偏倚整体推向较大的正向数值；文献中显示的“36% 效应量低于 0.05”实质上严重低估了教育干预的实际失败率。小样本研究若只发现微弱效应，往往因统计功效不足与结果非显著而被埋没于文件抽屉中。[[Argument_Kraft_2023_ER|(Kraft, 2023, p. 186)]]

> [!claim] Wolf, R., et al.
> **发表偏倚对开发者效应的实质驱动** 运用权重函数模型检验 WWC 实证库证实，发表偏倚解释了约 66% 的开发者效应。商业出版生态对显著正面结果的选择性接收，使得独立评估的零效应更难见刊，在未经严密校正的情况下，单纯依赖公开文献综合得出的教育干预决策潜藏巨大的虚假有效性风险。[[Argument_Wolf_2020_JREE|(Wolf et al., 2020, p. 442)]]

---

### 命题二　多重统计校正与剪补模型可有效检验结论稳健性并还原真实因果边界

> [!concept-lens] 稳健性诊断与剪补下调
> 探讨如何通过漏斗图、剪补法与失安全数等多重统计手段穿透发表偏倚的迷雾，判定核心因果结论是否具有超越发表偏倚的稳健性。

> [!claim] Cartiff, B. M., et al.
> **多重诊断与剪补下调确立因果效应抗偏倚稳健性** 在关于认识论认知干预的一阶元分析中，漏斗图目视不对称性与 Egger 线性回归检验显著提示文献库中存在潜在的抽屉效应；研究者进而调用 Duval & Tweedie 剪补法虚拟填补了 6 项缺失研究，使总体效应量从 $d = 0.509$ 保守下调为 $d = 0.342$（$95\% \text{ CI } [0.155, 0.528]$），下调后的效应量依然高度显著且处于稳健的中等促进区间；同时 Rosenthal 经典失安全数高达 2,593，Orwin 失安全数表明需要 46 项零效应研究才能将平均效应压低至 $0.20$ 基准以下。这一多重互证规程确立了即使在存在显著发表偏倚的情况下，认识论认知干预的核心因果价值依然具有坚实的统计稳健性。[[Argument_Cartiff_2021_JEP|(Cartiff et al., 2021, pp. 484–485)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **证据扭曲命题** | 出版与资助生态对显著正面结果的偏好导致文献库效应量系统性虚夸，掩盖真实失败率 | 元分析效应量解释、循证政策审查 | [[Argument_Wolf_2020_JREE\|Wolf et al. (2020)]]; [[Argument_Kraft_2023_ER\|Kraft (2023)]] |
> | **稳健性检验命题** | 结合剪补法、失安全数与回归检验可量化偏倚下调幅度，确立核心因果推论的稳健性边界 | 元分析偏倚审计、敏感性分析与稳健性报告 | [[Argument_Cartiff_2021_JEP\|Cartiff et al. (2021)]]; [[Argument_Zhao_2025_JIntell\|Zhao et al. (2025)]] |

---

## 概念演变

> [!dev-timeline] 发表偏倚的概念演变
> - **1940 — Pratt and Rhine 最早检测** 在对 145 项超感知觉实验的系统性综述中首次估计未发表论文对汇总效果的影响，开启了对抽屉效应的方法学关注。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 35)]]
> - **1991 — Rosenthal 经典失安全数** 提出量化文件抽屉效应的经典方法，通过计算推翻显著结论所需零效应研究数量评估证据稳健性。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|(Cohen et al., 2011, Ch17, p. 355)]]
> - **1995 — Vevea & Hedges 权重函数模型** 提出针对元分析中不同 p 值区间赋予权重的参数化统计校正模型。
> - **2000 — Duval & Tweedie 剪补法普及** 提出基于对称性的非参数剪除与虚拟填补算法，成为国际元分析审计发表偏倚的标准配置。
> - **2020 — Wolf et al. 解构开发者效应** 将权重函数模型应用于开发者与独立评估效应量比较，证实发表偏倚贡献了开发者效应的 66%。[[Argument_Wolf_2020_JREE|(Wolf et al., 2020, p. 442)]]
> - **2021 — Cartiff et al. 多方法严密诊断范式** 在《教育心理学杂志》（JEP）元分析中建立包含离群值缩尾、漏斗图、Egger 回归、剪补法、Rosenthal 及 Orwin 双失安全数的多工具互证规范。[[Argument_Cartiff_2021_JEP|(Cartiff et al., 2021, pp. 484–485)]]
> - **2022 — Révai 知识动员系统批评** 将发表偏倚从统计学技术问题提升至知识动员生态危机高度，揭示出版商偏好对累积性知识库的阻滞。[[Argument_Revai_2022_ChangingLandscape|(Révai, 2022, p. 22)]]
> - **2023 — Kraft 教育 RCT 经验基准** 基于大规模试验实证分布，指出发表偏倚导致教育实证文献中的项目有效率被严重虚夸。[[Argument_Kraft_2023_ER|(Kraft, 2023, p. 186)]]

---

## 争议与批评

> [!warning] 统计校正模型的前提假设与适用局限
> - **权重函数模型与剪补法的模型假设** Vevea-Hedges 权重模型高度依赖发表概率与 p 值区间的先验假设；剪补法假定漏斗图不对称完全源于发表偏倚，但在真实研究中，小样本研究质量较差、干预强度更高或研究间实质异质性同样会导致漏斗图不对称，机械剪补可能过度下调真实效应。[[Argument_Wolf_2020_JREE|(Wolf et al., 2020, p. 442)]]
> - **官方清算机构（WWC）数据的特殊性** 由于美国联邦项目资助合同强制要求提交结题评估报告，美国强效清算中心（WWC）库容中包含了大量独立评估的零效应报告；因此一般商业期刊文献库中的发表偏倚通常远比 WWC 数据严重。

> [!critique] 基础设施层面的系统性治理方案：中央证据数据库
> [[Argument_Wecker_2016_ZfE|Wecker et al. (2016, pp. 34–36)]] 在对 Hattie 可见学习的方法学批判中，指出仅靠事后统计校正无法彻底解决发表偏倚，必须从科研基础设施层面建立中央证据数据库：
> - **不分发表状态的全量归档** 强制无条件收集所有经资助的实证研究的方法、原始数据与结果，直接在中央数据库中以标准化格式开放，从根本上阻断文件抽屉效应。
> - **统一效应量标准与透明数据表** 统一采用 Hedges' g 规范无偏估计，要求每个元分析必须附带主要研究的完整元数据表，终结 Hattie 式的不透明数据综合。

---

## 实证数据

> [!ref-table]- 元分析发表偏倚诊断与校正实证结果
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | 偏倚检验工具与指标 | 关键校正结果 | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Cartiff_2021_JEP\|Cartiff et al. (2021)]] | 认识论认知干预文献库，26 项实验与准实验（28 个独立样本、$N = 4,373$） | 随机效应元分析多重偏倚诊断 | 漏斗图、Egger 检验、Duval & Tweedie 剪补法、Rosenthal 与 Orwin 失安全数 | 漏斗图呈现不对称且 Egger 检验显著；剪补法虚拟填补 6 项研究后效应量从 $d = 0.509$ 下调为 $d = 0.342$；失安全数 $N_{fs} = 2{,}593$；Orwin $N_{fs} = 46$（目标 $d = 0.20$） | 剪补后 $95\% \text{ CI } [0.155, 0.528], p < .001$，仍高度显著 | 严谨的多工具互证证实认识论干预即使扣除潜在发表偏倚后，依然保持稳健的中等因果促进效应（pp. 484–485） |
> | [[Argument_Zhao_2025_JIntell\|Zhao et al. (2025)]] | 生成式 AI 促进高阶思维的 29 项实验与准实验研究（59 个效应量） | 一阶元分析偏倚审计 | 漏斗图目视诊断结合 Egger 线性回归截距检验 | 漏斗图散点大体围绕均值对称分布；Egger 回归截距检验统计量 $t = 1.871, p = 0.066$ | $p > 0.05$ 未达统计显著水平 | 参数检验排除了严重发表偏倚对合并促学效应（$g = 0.609$）的实质性扭曲（pp. 9–10） |
> | [[Argument_Wolf_2020_JREE\|Wolf et al. (2020)]] | WWC 收录的中小学数学与阅读干预 RCT/QED 研究库 | 权重函数模型校正 | Vevea-Hedges 权重函数模型、亚组效应对比 | 开发者研究原始 $ES = +0.292$，校正后 $+0.276$；独立研究原始 $ES = +0.177$，校正后 $+0.200$；组间差异由 0.115 降为 0.076 | 独立研究校正前后差异达显著（$p < .05$） | 证实发表偏倚约解释 66% 的开发者效应，且独立评估更容易受制于期刊选择性发表（p. 442） |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Cartiff_2021_JEP|Cartiff et al. (2021)]] — 在认识论认知元分析中建立漏斗图、Egger 检验、Duval & Tweedie 剪补法及双失安全数的多重诊断范式，确立效应量经剪补下调（$d = 0.509 \to 0.342$）后依然稳健的实证典范。
> - [[Argument_Wolf_2020_JREE|Wolf et al. (2020)]] — 运用 Vevea-Hedges 权重函数模型检验发表偏倚对开发者效应的贡献（解释约 66%），揭示独立评估在出版生态中遭遇的选择性发表风险。
> - [[Argument_Zhao_2025_JIntell|Zhao et al. (2025)]] — 结合漏斗图与 Egger 线性回归检验（$t = 1.871, p = 0.066$）对生成式 AI 高阶思维促学效应展开稳健性核查。
> - [[Argument_Kraft_2023_ER|Kraft (2023)]] — 基于全美教育 RCT 大规模经验分布，指出发表偏倚导致文献库中干预“失败率”被系统性低估。
> - [[Argument_Revai_2022_ChangingLandscape|Révai (2022, p. 22)]] — 从知识动员复杂系统维度剖析学术出版偏好对教育累积性知识库建构的结构性阻滞。
> - [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] — 对 Hattie 元分析展开方法学批判，提出建立无条件全量归档的“中央证据数据库”作为从源头治理发表偏倚的基础设施方案。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al. (2011, Ch17)]] — 教育研究方法经典教材，系统阐述 Rosenthal 文件抽屉方法与元分析偏倚争议。
> - [[Creation of REES]] — 实证教育研究预注册（REES）制度，旨在通过研究设计前置公开防范发表偏倚与选择性报告。
