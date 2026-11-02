---
title: Algorithmic Bias
aliases:
  - 算法偏倚
  - 算法偏见
  - 算法偏差
  - 算法歧视
  - Algorithmic Fairness
  - Bias in AI
summary: "算法系统基于历史数据进行训练与参数拟合时，系统性学习、放大并在制度层面固化人类社会既有偏倚、歧视与结构不平等的现象；在人员招聘、司法量刑、信贷审批及同行评审与科研资助分配中展现出显著的放大效应与黑箱治理风险。"
type: concept
domain: "ethics-of-technology"
related_count: 12
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - concept/ethics-of-technology
  - theme/artificial-intelligence
  - theme/ai-ethics
  - theme/algorithmic-governance
  - theme/metascience
related_concepts:
  - "[[Automation Bias]]"
  - "[[Status Bias in Peer Review]]"
  - "[[Novelty Bias in Peer Review]]"
  - "[[Publication Bias]]"
  - "[[Predictive Policing]]"
  - "[[Meaningful Human Control]]"
  - "[[Causality]]"
  - "[[Scientific Productivity]]"
  - "[[Metascience]]"
related_theories: []
related_methods:
  - "[[Audit Trail]]"
  - "[[Network Analysis]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit10]]"
confidence: high
status: draft
created: 2026-11-02
updated: 2026-11-02
---

---

> [!def] Algorithmic Bias
> 算法偏倚（Algorithmic Bias）指计算算法系统基于历史经验数据展开训练与参数拟合时，系统性学习、提炼并级联放大人类既有的社会偏见、认知偏离与结构性不平等的现象。这一机制将数据源中潜藏的统计偏斜固化为制度化的自动化歧视性决策规则。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 239–240)]]

> [!concept-lens] 概念透镜
> - **含义** 数据驱动算法对历史社会偏见的高维拟合与自激放大，导致自动化决策系统重现或加剧既有不平等。
> - **用途** 用于诊断和防范人员招聘、司法量刑、信贷审批以及科学计量与学术治理等领域的自动化决策失衡。
> - **边界** 适用于目标函数与训练数据拟合历史社会偏倚所致的系统性偏差，不适用于因样本容量有限引发的随机采样误差，亦不同于底层软件编写引发的机械程序故障。

> [!citation-card] 历史偏见的级联放大
> 随着分析工具在精度与复杂度上的持续提升，算法将忠实地放大并长久固化人类既有的各类偏倚。在科学学纵深演进的进程中，学界必须深入探究所构建工具与评价指标底层的偏倚结构与因果机制。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 240)]]
>
> *What Amazon’s debacle illustrates is that, as our tools grow in accuracy and sophistication, they’ll amplify and help perpetuate whatever biases we humans already have. Which means that as the science of science advances, there will be an increased need to understand biases and causal relationships in the tools and metrics our community builds.*

> [!boundary]- 概念边界
> - 不等于 [[Automation Bias|自动化偏差]]：自动化偏差探讨人类决策者过度信赖机器判断的认知心理失衡；算法偏倚关注算法系统自身决策输出对历史偏见的统计放大与歧视性固化。
> - 不等于机械编程错误：算法偏倚发生时系统严格按照既定优化目标运作，问题根源在于训练语料内嵌的历史不平等与目标函数对社会正义约束的缺位。
> - 不适用于纯粹物理测量噪声或无标签监督的理论解析模型。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 算法偏倚（Algorithmic Bias） | [[Automation Bias|自动化偏差（Automation Bias）]] | [[Status Bias in Peer Review|声望偏倚（Status Bias）]] |
> |---|---|---|---|
> | **分析对象** | 数据驱动算法系统与目标函数 | 实际运用人员与决策者的认知心理 | 评审专家与学术编辑的评价行为 |
> | **核心机制** | 高维拟合历史语料并级联放大统计偏斜 | 盲从自动化提示并放弃独立验证 | 受外生头衔与机构光环扭曲质量判断 |
> | **典型表现** | 招聘模型自动扣减女性履历评分 | 驾驶员忽视前方障碍报警任由系统接管 | 顶级名校稿件录用率达普通机构 1.76 倍 |
> | **治理路径** | 样本再平衡、算法审计与因果校准 | 认知摩擦介入与意义控制保持 | 双盲评审机制与多维度同行评议改革 |

---

> [!feature] 核心要素
> - **历史数据内嵌性** 训练数据忠实反映既有社会格局，过往的歧视模式与资源垄断通过标签分布注入模型底层。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 239–240)]]
> - **统计放大效应** 监督学习以最小化总体经验损失为导向，促使算法强化主导类别的特征权重并压低非主流群体特征得分。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 240)]]
> - **黑箱隐蔽性** 深层非线性表征切断了特征输入与决策输出之间的可解释[[Causality|因果]]关联，使得系统性歧视隐藏于高维参数权重之中。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 239)]]
> - **制度反馈循环** 算法决策反向塑造现实资源分配，受到算法排斥群体的现实境遇进一步受限并持续污染未来的训练样本。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 240)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart LR
>     A["历史社会偏见与数据失衡"] --> B["高维参数拟合与统计放大"]
>     B --> C["黑箱算法歧视性输出"]
>     C --> D["资源分配与制度固化"]
>     D --> A
> ```

---

> [!concept-proposition] 命题一｜监督学习与历史数据拟合通过统计放大效应将潜隐社会偏倚转化为刚性制度排斥
> **探讨维度　数据驱动模型的偏差放大机制** 探讨机器学习算法以经验风险最小化为导向拟合历史语料时，如何将人类社会既有的非正式歧视提炼为确定性的自动化决策壁垒。

> [!claim] Wang, D. & Barabási, A.-L.
> **历史数据拟合诱发系统性歧视放大** 汪大胜（Dashun Wang）与阿尔伯特-拉斯洛·巴拉巴西（Albert-László Barabási）通过剖析亚马逊实验性人工智能招聘系统指出，算法工具的精密度提升并未消除偏见，反而成为放大既有社会不平等的加速器。该系统以科技行业过去十年间男性占据压倒性多数的履历库为训练源，系统自主提炼出了男性候选人更符合技术岗位的隐性规律，导致模型自动惩罚包含特定女性词汇的简历并降级女子学院毕业生。算法完全忠实地执行了人类历史数据暗含的优化目标，将统计关联误用为甄选规则，证明了缺乏因果约束的数据驱动模型必然在制度层面复制并固化历史偏见。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 239–240)]]

---

> [!concept-proposition] 命题二｜算法客观性表象与黑箱机制掩盖因果机制缺位导致科学治理指标的二次极化与马太效应
> **探讨维度　科学学评价与学术治理的黑箱风险** 剖析学术界盲目引入人工智能计量工具与自动化评审分配时，缺乏可解释因果结构所引发的声誉垄断与评价失真。

> [!claim] Wang, D. & Barabási, A.-L.
> **科学计量工具黑箱化加剧学术资源分配失衡** 汪大胜与巴拉巴西论证指出，随着人工智能与计量算法深度嵌入期刊审稿指派、前沿态势感知与科研资助分配，学界必须高度警惕黑箱工具的假客观性。算法系统能够极为高效地给出排序与预测评分，但决策过程完全处于不可解释的黑箱状态。若决策者不深入厘清评价指标底层的因果关联机理，直接将复杂预测模型转化为刚性评价标准，算法将忠实地把学界历史形成的地域特权、机构声望壁垒与学科垄断固化为看似中立的数字化指标，在学术生态内制造更为严苛的马太效应与创新阻滞。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 240)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **数据放大机制** | 算法拟合历史经验数据将潜隐偏见放大为刚性制度排斥 | 人力资源招聘、信贷评分、司法风控 | Wang, D.; Barabási, A.-L. |
> | **学术治理风险** | 黑箱模型掩盖因果缺位并将学术特权固化为量化评价指标 | 期刊审稿匹配、科研项目资助分配、学者学术影响力计量 | Wang, D.; Barabási, A.-L. |

---

> [!dev-timeline] 概念演变
> - **2016 — 算法正义问题凸显** 调查报告揭露司法风险评估算法对特定族裔被告的系统性偏见，引发全社会对算法公平性的广泛关注。
> - **2018 — 工业界黑箱招聘折戟** 亚马逊废止基于十年历史数据训练的人工智能招聘系统，确证深度学习算法自动惩罚女性履历，使算法偏倚成为人工智能伦理审查的核心议题。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 239–240)]]
> - **2021 — 科学学评价因果转向** 汪大胜与巴拉巴西在科学学体系中系统阐明算法偏倚机制，警告同行评审与科研资助自动化必须警惕指标黑箱化，确立了科学治理工具因果检验与伦理校准的研究方向。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 240)]]

---

> [!tension|notitle] 核心张力
> - **技术中立论（蓝方）** 算法是客观反映数据分布的数学工具，预测误差源于现实社会本身存在的信息不对称，持续扩充数据与优化参数即可逐步减少偏差。
> - **结构性正义论（红方）** 算法承载特定价值预设，以历史经验损失最小化为优化目标必然在统计上级联放大既有歧视，必须引入法律规范、因果校准与[[Meaningful Human Control|意义控制]]。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 240)]]

> [!warning|limits] 适用局限
> - **去偏技术与精度损失的权衡边界** 强制实施人口统计平等约束通常会折损算法在特定无偏子任务上的纯粹预测精度，政策制定者需要在公平价值与统计效率之间进行价值权衡。
> - **算法透明度与商业保密壁垒** 商业算法与科研资助评价系统受商业秘密或机构保护，外部独立审计常面临数据壁垒与代码不可见困境。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, pp. 239–240)]]

---

> [!evidence-grid-a|notitle] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit10|Wang & Barabási (2021)]] — 结合亚马逊人工智能招聘案例，阐明算法对人类历史偏见的级联放大机制，并系统论述科学学评价工具必须坚持因果分析与伦理校准。
