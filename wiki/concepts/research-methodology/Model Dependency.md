---
title: Model Dependency
aliases:
  - 模型依赖性
  - model sensitivity
  - 模型敏感性
  - specification dependence
summary: "同一经验数据集因统计分析者选用的建模假定不同而导致效应量估计与统计推断发生大幅漂移的现象，揭示了实证证据高度脆弱的主观模型设定根源，催生了强制性预注册与统计分析计划"
type: concept
domain: "research-methodology"
related_count: 13
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - model-dependency
  - research-methodology
  - statistics
  - quantitative-methods
  - causal-inference
  - effect-size
related_concepts:
  - "[[Researcher Degrees of Freedom]]"
  - "[[Sampling Error]]"
  - "[[Scientific Uncertainty]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Confidence Interval]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ROE]]"
  - "[[Argument_Higgins_2016_RE]]"
confidence: high
status: completed
created: 2026-09-15
updated: 2026-09-15
---

# Model Dependency

---

## 定义

> [!def] 核心定义
> 模型依赖性（Model Dependency，亦称模型敏感性或形式设定依赖）指在同一批经验观测数据上，由于统计分析者所选取的底层数学建模假定（如协变量纳入规则、群聚结构校正方式、固定效应与随机效应设定）不同，导致干预因果[[Effect Size|效应量]]的点估计值、[[Confidence Interval|置信区间]]宽度及统计学显著性（$p$ 值）发生大幅漂移乃至定性翻转的现象（[[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill, 2021, p. 52]]）。该概念揭示了即便数据采集真实无欺，实证结论仍高度脆弱地依附于分析者主观模型设定的方法学困境（Xiao, Higgins, & Kasim, 2016）。

> [!concept-lens] 概念透镜
> - **含义** 指向因果推断中由模型技术参数与底层假定所诱发的推断不确定性，打破了“客观数据必然导出单一客观结论”的技术迷思。
> - **用途** 用于诊断量化试验的稳健性边界，倒逼研究机构建立分析标准（如预先拟定统计分析计划 SAP）以阻断事后“数据钓鱼”。
> - **边界** 区别于纯粹的测量误差或抽样随机涨落；特指数据集固定不变条件下，分析模型选择本身带来的推断变异。

> [!citation-card] 17 项教育试验复算揭示模型依赖性（Xiao, Higgins, & Kasim, 2016; Edovald & Nevill, 2021）
> 得益于英国教育捐赠基金会（EEF）依托英格兰国家学生数据库（NPD）建立的微观试验档案库，杜伦大学学者齐·肖（ZhiMin Xiao）、史蒂夫·希金斯（Steve Higgins）与阿迪特·卡西姆（Adetayo Kasim）获得了对 17 项早期完成的 RCT 试验微观原始数据进行二次审计的机会。复算揭示了惊人的敏感性：在 17 项试验中，多达 12 项试验的点估计效应量或其统计显著性在不同统计模型间发生了漂移与突变。某些干预在简单模型中达到 $p < .05$ 显著，而在分层随机截距模型中置信区间跨越了零点……这一发现证实了即使数据真实无欺，效应量结果仍高度依赖分析者的模型设定。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021, p. 52)]]
>
> *“Twelve of the 17 evaluations were sensitive to the model used... this powerful data set demonstrated that even when data are completely authentic, findings remain vulnerable to analytical model dependency unless rigorously pre-specified.”*

> [!boundary] 概念边界
> - **不等于 [[Researcher Degrees of Freedom|研究者自由度（p-hacking）]]** 研究者自由度强调研究者主观恶意或下意识地“试错直到显著”；而模型依赖性是客观存在的技术特征，即便极其严谨正直的研究者在面临不同合法模型时，同样会遭遇结论分歧。
> - **不等于 [[Sampling Error|抽样误差（Sampling Error）]]** 抽样误差随样本量增大而趋近于零，由随机抽样波动决定；模型依赖性在样本量极大时依然存在，甚至可能因大样本过度敏感而放大模型误设的偏差。
> - **不等于 测验测量偏倚（Measurement Bias）** 测量偏倚源于测验工具本身的信效度缺陷；模型依赖性发生在测验分数已完成采集之后的统计建模阶段。

---

## 概念辨析

> [!contrast-table] 实证推断偏倚与不确定性来源对比
> | 比较维度 | 模型依赖性 (Model Dependency) | 研究者自由度 (Researcher Degrees of Freedom) | 抽样误差 (Sampling Error) |
> |---|---|---|---|
> | **根源所在** | 统计模型底层假定（协变量/集群/方差结构）的数学差异 | 分析者在多重假设检验中未公开的主观选择与挑拣 | 从总体中随机抽取有限样本带来的自然随机涨落 |
> | **数据表现** | 相同固定数据集，切换模型即导致 $p$ 值与效应量漂移 | 数据清洗、剔除极端值或切换指标以达成 $p < .05$ | 样本统计量围绕总体真实参数呈现正态或 $t$ 分布分散 |
> | **防范与治理手段** | 制定统一建模指南（如 SAP）、多模型稳健性敏感性检验 | 严格方案预注册（Preregistration）、盲法数据分析 | 扩大有效样本量、采用两阶段分层整群最优抽样设计 |
> | **典型实证案例** | EEF 17 项试验四模型并行复算中 12 项结果漂移（Xiao et al., 2016） | 社会科学实验中显著结果发表率虚高 40%（Franco et al., 2014） | 早期教育试验由于群内相关（ICC）导致有效样本量骤降 |

---

## 核心要素

> [!feature] 核心要素
> - **协变量调整设定（Covariate Adjustment）** 模型是否纳入基线前测考分或受试者背景特征作为控制变量。纳入高预测力前测可大幅吸收残差方差、提高估计精度，但若基线存在不平衡则可能扭曲估计斜率。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021, p. 52)]]
> - **集群结构校正（Clustering Architecture）** 数据嵌套于班级或学校时，是否引入组内相关系数（ICC）校正。忽略层级嵌套的 OLS 模型会严重低估标准误，导致虚假的统计显著性；而多层模型（MLM/HLM）或广义估计方程（GEE）则会拉宽置信区间。
> - **效应结构假定（Fixed vs Random Effects）** 究竟将群聚单元视为固定效应（仅推论至参试学校）还是随机截距/随机斜率（推论至总体分布），直接决定了误差方差的分解方式。
> - **缺失数据处理规程（Missing Data Mechanisms）** 是采用完全案例分析（Listwise Deletion）、均值填补、多重插补（Multiple Imputation）还是全信息极大似然法（FIML），会显著改变最终样本权重与效应估计。

> [!logic-map] 模型依赖性的生成机制与应对路径
> ```mermaid
> flowchart TD
>     A["同一批微观试验数据 (如 NPD 数据集)"] --> B["分析模型选择分歧"]
>     B --> C["单层模型 (OLS / 均值差异)"]
>     B --> D["协方差分析 (ANCOVA 控前测)"]
>     B --> E["分层多层模型 (MLM / HLM 随机截距)"]
>     B --> F["聚类稳健方程 (GEE 模型)"]
>     C --> G["标准误低估，易假阳性显著"]
>     D --> H["残差方差缩小，点估计调整"]
>     E --> I["置信区间展宽，部分显著性消失"]
>     F --> J["经验方差替代，点估计漂移"]
>     G & H & I & J --> K["模型依赖性爆发 (12/17 试验结论分歧)"]
>     K --> L["制度化防范：出台刚性《统计分析指南》"]
>     L --> M["前置锁定预注册统计分析计划 (SAP)"]
> ```

---

## 围绕概念形成的命题

---

### 命题一　统计模型的微小假定差异足以颠覆大规模现场试验的政策定性与证据等级

> [!concept-lens] 探讨维度：因果推断在数学模型层面的高度脆弱性
> 计量方法学研究揭示：教育干预的有效性判定绝非仅仅取决于教学方案本身，而是高度受制于后端统计分析师选用的回归公式结构。

> [!claim] [[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill (2021, p. 52)]]; Xiao, Higgins, & Kasim (2016)
> **多模型复算下的显著性漂移** 杜伦大学团队对英国 17 项大规模教育 RCT 原始数据进行的四模型复算显示：超过三分之二的干预项目，其是否具有统计显著性完全取决于使用的是简单均值对比、OLS 回归、MLM 还是 GEE 模型。某些干预在研究者自选的模型中呈现耀眼的 $p < .05$，一旦放入严格校正学校两级嵌套的随机截距模型中，置信区间便直接跨越零点。这意味着如果没有统一的模型规范，政策制定者可能基于统计模型的偶然选择，错误资助无效方案或扼杀有潜力的实践。

---

### 命题二　单纯依靠数据透明无法解决推断危机，必须通过前置统计分析计划（SAP）构建方法学制度防火墙

> [!concept-lens] 探讨维度：从开放数据到流程规程化的治理转向
> 开放科学研究指出：公开原始微观数据虽然保障了可复现性（Reproducibility），但无法自主解决可比性（Comparability）；唯有剥夺事后自由挑选模型的裁量权，才能维护循证科学的公信力。

> [!claim] [[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill (2021, pp. 52–53)]]
> **统计分析指南的制度化诞生** 面对 17 项试验复算揭示的模型依赖性危机，EEF 迅速将学术危机转化为治理法典，于 2018 年出台了行业里程碑《统计分析指南》（The EEF, 2018）。该指南硬性确立三条基准：
> 1. 主效应模型必须强制纳入基线前测成绩作为主要协变量；
> 2. 强制采用校正组内相关系数的聚类稳健标准误模型；
> 3. 必须在试验数据解盲前完成统计分析计划（SAP）的公开备案，主分析必须严格执行备案模型，并将其他模型降格为补充敏感性检验。

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者与文献 |
> |---|---|---|---|
> | **推断脆弱性命题** | 揭示同一数据集在不同建模假定下效应量与显著性的质变漂移 | 量化研究方法论、二阶复算审计、Meta分析 | Xiao, Higgins, & Kasim (2016); [[Argument_Edovald_Nevill_2021_ROE\|Edovald & Nevill (2021)]] |
> | **制度防范治理命题** | 论证前置预注册与强制统计分析计划（SAP）是消解模型依赖性唯一可靠路径 | 循证清算标准、科研治理、开放科学规范 | Demack (2019); The EEF (2018) |

---

## 概念演变

> [!dev-timeline] 概念演变与学术脉络
> - **1980s — 勒默尔的极端界限分析（Extreme Bounds Analysis）** 经济学家爱德华·勒默尔（Edward Leamer, 1983）发表著名论文《让我们从计量经济学中除去欺瞒》（Let's Take the Con Out of Econometrics），首次系统形式化了“设定依赖性”（Specification Dependence），指出回归模型结果因控制变量的微调而剧烈变动。
> - **2000s — 多水平模型普及带来的分析分裂** 伴随分层线性模型（HLM）在教育学普及，传统 OLS 与多层模型之间的结果冲突频发，学界开始意识到忽视嵌套结构会导致严重的假阳性。
> - **2012–2016 — 试验微观数据库支撑下的全量复算** 依托英国 NPD 建立的 105 项 RCT 档案库，杜伦大学方法学团队（Xiao et al., 2016）系统复算 17 项试验，首次在实证上量化了教育现场试验中模型依赖性的发生概率（高达 70%）。
> - **2018–至今 — 统计分析指南（SAP）时代确立** EEF《统计分析指南（2018）》与 CONSORT-SPI 报告标准的全面融合，标志着国际教育实证科学从允许自由探索模型，正式步入前置锁定分析模型的规约化时代。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021)]]

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 机械统一模型 vs 依据数据特征灵活选模
> > 争论焦点在于循证机构是否应当强制规定唯一的标准模型（如统一 ANCOVA 加稳健标准误），还是应赋予分析师根据数据分布选择最佳拟合模型的自由。
> >
> > - **标准化规约立场（EEF, 2018; [[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill, 2021]]）** 认为如果不剥夺模型选择自由，模型依赖性必然演变为暗中迎合 $p < .05$ 的选择性操作；统一标准能最大限度保障不同试验效应量的横向可比性。
> > - **统计学灵活性立场** 认为不存在放之四海而皆准的万能模型；当数据呈现严重非正态、零膨胀或异方差时，机械套用预注册模型可能导致估计偏误，应当鼓励多模型并呈与敏感性边界汇报。

> [!critique] 外部批评
> - **置信区间掩盖问题** 批评者指出，即便统一了主要模型，如果未能充分正视模型设定的[[Scientific Uncertainty|不确定性]]，仅报告单一模型的点估计与置信区间，依然可能向公众传达虚假的精确度。

> [!warning] 适用局限
> 模型依赖性分析主要针对复杂的嵌套数据与现场准实验/随机试验。在单水平纯随机且基线完全平衡的简单物理或实验室实验中，模型设定的敏感性相对较低。

---

## 实证数据

> [!ref-table]- 其他实证结果（无效应量）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | 变量或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | Xiao, Higgins, & Kasim (2016); [[Argument_Edovald_Nevill_2021_ROE\|Edovald & Nevill (2021)]] | 英国 EEF 资助并归档于 NPD 的 17 项早期完成学校 RCT 试验 | 原始微观数据四模型（OLS、ANCOVA、HLM、GEE）全量并行复算审计 | 各模型下的干预效应量点估计值、标准误与 $p$ 值 | 17 项试验中多达 12 项试验对分析模型表现出高度敏感性；多项干预在简单模型中显著而在分层模型中跨越零点 | $12/17$ 试验跨模型结论不一致 | 证明大规模教育实证推断存在普遍而严峻的模型依赖性风险 |
> | Demack (2019) | 英国中小学教育试验班级与学校两级嵌套数据 | 蒙特卡洛模拟与 NPD 归档数据实证检验 | 班级层级组内相关系数（Classroom ICC）对标准误的影响 | 忽略班级层级聚集效应会导致第一类错误率（假阳性）剧增，模型对是否校正班级效应高度敏感 | 统计功效与标准误发生显著扭曲 | 倒逼 EEF 规范在两级分层线性模型中将班级效应纳入敏感性检验 |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill (2021)]] — 系统记录杜伦大学利用 NPD 微观数据复算 17 项试验揭示模型依赖性的全过程，阐述其如何直接催生 EEF 官方《统计分析指南》。
> - [[Argument_Higgins_2016_RE|Higgins (2016)]] — 从二阶元综合的方法学高度，反思原始研究在模型假定上的异质性如何加剧跨干预比较的偏差风险。
