---
title: Heterogeneity
aliases:
  - 异质性
  - 研究间异质性
summary: "元分析中各研究效应量之间超出抽样误差的变异，是判断能否合理合并研究 and 探索调节变量的核心概念"
type: concept
domain: "research-methodology"
related_count: 31
related_level: 3
related_stars: "⭐⭐⭐"
related_color: "#fde68a"
tags:
- heterogeneity
- meta-analysis
- effect-size
- statistical-synthesis
- methodology
related_concepts:
  - "[[Effect Size]]"
  - "[[Sampling Error]]"
  - "[[Causality]]"
  - "[[Sample Size Determination]]"
  - "[[Forest Plot]]"
  - "[[Hypothesis]]"
  - "[[Variable]]"
  - "[[Epistemology]]"
  - "[[Praxis]]"
  - "[[Student-Teacher Relationship]]"
  - "[[Visible Learning]]"
  - "[[Positivism]]"
  - "[[Paradigm]]"
  - "[[Tracking]]"
related_theories:
  - "[[Critical Realism]]"
  - "[[Realist Evaluation]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Random Sampling]]"
  - "[[Moderator Analysis]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Meta-meta-analysis]]"
related_persons:
  - "[[Karl Pearson]]"
  - "[[Gene Glass]]"
  - "[[John Hattie]]"
related_arguments:
  - "[[Argument_Higgins_2016_RE]]"
  - "[[Argument_Wrigley_2018_BERJ]]"
  - "[[Argument_Wrigley_2019_ERE]]"
  - "[[Argument_Simpson_2017_JEP]]"
  - "[[Argument_Terhart_2011_JCS]]"
related_facts:
  - "[[Education Endowment Foundation]]"
confidence: medium
status: draft
created: '2026-06-08'
updated: 2026-07-08
---

# Heterogeneity

---

## 定义

> [!def] 核心定义
> 异质性（Heterogeneity）在[[Meta-analysis|元分析]]中指各研究的[[Effect Size|效应量]]之间超出[[Sampling Error|抽样误差]]预期的变异。当研究间效果的差异大于仅由抽样误差（即样本随机变异）所能解释的程度时，即存在异质性，表明研究在干预实施、参与者特征、结果测量或研究设计等方面存在系统性变异([[Argument_Higgins_2016_RE|Higgins, 2016, p. 32]])。

> [!concept-lens] 概念透镜
> - **含义** 该概念指向多项一级实证研究在特征（设计、情境、样本）与测量结果（效应量）上的系统性多样性与不一致性。
> - **用途** 帮助研究者评估合并研究的合理性，判断平均效应是否具有误导性，并指导通过探索变异来源来识别干预在“什么情境下更有效”。
> - **边界** 不应仅被视为统计学上的“干扰噪声”或测量误差，而应被视为深入探索因果机制和边界条件的关键线索([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 13]])。

> [!boundary]- 概念边界
> - **不等于 统计变异（Statistical Variance）** — 统计变异是指由于抽样造成的随机误差，而异质性特指超出随机误差之外、由研究系统性差异（如干预强度、人群特征）引起的变异。
> - **不适用于 封闭确定性系统** — 在[[Causality|因果关系]]固定且不受环境干扰的物理学封闭实验中，异质性不是核心概念；但教育属于开放的社会系统，因果力量受到意志与环境的符号交互影响，这使得异质性不可避免([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 14]])。

---

## 概念辨析

> [!contrast-table] 概念辨析
> | 维度 | 统计异质性 (Statistical Heterogeneity) | 情境/教学异质性 (Contextual Heterogeneity) | [[Random Sampling\|随机抽样]]误差 (Sampling Error) |
> |------|--------|----------------|----------------|
> | **表现形式** | 效应量之间的数学分布差异（通过 Q 检验、$I^2$ 等检测） | 实证研究在干预定义、学科领域、人群和实施强度上的实际差异 | 单一研究的测量均值围绕总体真值的偶然偏离 |
> | **处理原则** | 选择合适的加权统计模型，并运行统计学[[Moderator Analysis\|调节变量分析]] | 诉诸[[Causality\|因果]]理论，进行实在论综合，探寻 CMO 配置 | 通过增大[[Sample Size Determination\|样本量]]予以稀释和抵消 |
> | **研究价值** | 指示数据合成是否面临“苹果与橙子”合并的风险 | 提供因果机制 and 边界条件的实质解释资源([[Argument_Wrigley_2018_BERJ\|Wrigley, 2018, p. 13]]) | 作为统计精度（[[Sampling Error\|标准误]]）的计算基础 |

---

## 核心要素

> [!feature] 核心要素
> - **异质性检测与量化** 通过 Q 检验判断研究间变异是否超出随机误差；通过 $I^2$ 统计量描述异质性占总观测变异的比例。此外，[[Forest Plot|森林图]]是直观展示变异性的重要可视化工具。
> - **统计模型选择**[[Fixed-Effect and Random-Effects Models|固定效应模型]][[Hypothesis|假设]]所有研究估计同一个真实[[Effect Size|效应量]]，观测差异仅来自[[Sampling Error|抽样误差]]；随机效应模型则承认每项研究有其随机变异，同时考虑研究内和研究间变异([[Argument_Higgins_2016_RE|Higgins, 2016, p. 39]])。
> - **调节[[Variable|变量]]探索** 通过调节[[Variable|变量]]分析（[[Moderator Analysis]]）识别与较大或较小效应相关的特征（如学生年龄、干预时长等），使研究从“有没有效”转向“对谁、在什么情境下有效”([[Argument_Higgins_2016_RE|Higgins, 2016, p. 32]])。

---

## 围绕概念形成的命题

> [!claim] 命题总览
> 围绕异质性的学术讨论揭示了统计合成的深层[[Epistemology|认识论]]危机：是将异质性视为需要“清洗掉”以计算平均值的技术噪声，还是将其视为揭示教育复杂因果机制的科学信号。

---

> [!claim] 命题一：异质性是教育改进的因果机制信号，而非待抹除的噪声
> 在高度情境化的教育[[Praxis|实践]]中，平均[[Effect Size|效应量]]往往会抹杀具有实质意义的效果差异，因此探索异质性（什么条件下效果更好）比单纯计算平均效应更具有实践价值。([[Argument_Higgins_2016_RE|Higgins, 2016, p. 37]])
> 
> [!warrant]- 命题一的支撑理由
> 教育是一个符号与递归（semiotic and recursive）的开放系统，人类意志和信念在其中具有因果效应。干预的效果高度依赖于特定情境（如学生先前水平、[[Student-Teacher Relationship|师生关系]]、学校文化等）与底层机制的交互，这些因素的变异直接在统计上表现为强烈的异质性([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 14]])。
> 
> [!exegesis]- 教育研究例子
> 用一个具体教育情境说明这条命题如何工作。Kluger & DeNisi (1996) 对反馈研究的[[Meta-analysis|元分析]]显示，尽管“反馈”的平均效应量达到 $+0.40$ 标准差，但由于极高的异质性（效应量标准差为 1），有超过三分之一（38%）的研究中反馈反而带来了负面效果([[Argument_Wiliam_2019|Wiliam, 2019, p. 10]])。这说明反馈在任何教学交互中都是不可避免的，粗暴地给出一个“反馈最有效”的均值数字，根本无法告诉教师在具体课堂情境中“什么样”的反馈才是有效的。

---

> [!claim] 命题二：统计聚合通过剥离情境强行抹除异质性，导致“统计炼金术”与语义空洞
> 当研究者在缺乏因果理论支撑的情况下，强行合并性质迥异的研究以计算单一平均效应时，异质性在多级聚合中被系统性清洗，导致结论空洞化并引发错误的政策决策。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, pp. 9–10]])
> 
> [!implication]- 命题后果
> - **解释后果** 当详细的项目评估报告被逐级简化为一个效应量数字时，所有解释该项目为什么成功的因果情境信息（如一对一辅导、地位提升等）都被消除，导致研究只看到相关性而看不到机制([[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, p. 122]])。
> - **政策后果** 这种去情境化的扁平化排名（如《教学与学习工具包》）极易误导学校决策。例如，将教学助理（TA）类目贴上“低影响、高成本”的标签，直接遮蔽了“TA 因为缺乏与教师沟通的备课时间而被结构性使用不当”的底层异质性情境，从而可能为政府在预算缩减时作出裁减 TA 的错误决定提供依据([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 12]])。

---

## 概念演变

> [!dev-timeline] 概念演变
> - **1904 — 起源阶段**[[Karl Pearson]] 在跨研究合并分析中首次同时关注“合并数据能否给出可靠答案”以及“效果变异（即异质性）的原因”这两个基本维度([[Argument_Higgins_2016_RE|Higgins, 2016, p. 33]])。
> - **1970s–1980s — [[Meta-analysis|元分析]]倡导** [[Gene Glass]] 创立“元分析”概念，并明确警告：元分析 the 最终结果“绝对不应该是一个平均数，而应该是一张显示变异性（异质性）的图表”([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 9]])。
> - **1995 — 方法论解构与批评**医学统计学家 Alvan Feinstein (1995) 批评元分析是“21世纪的统计炼金术”，指出它将不同病理状态的研究强行合流，从而将重要的异质性埋入统计泥浆之中。
> - **2002 — 教育研究的测量批评**Robert Coe (2002) 警告，在测量工具、干预实施强度和目标人群大相径庭 of 教育研究中，将这些[[Effect Size|效应量]]进行平均在数学上是完全没有意义的。
> - **2010s — 多级聚合失真与实在论转向**Ray Pawson (2006) 和 [[Argument_Wrigley_2018_BERJ|Wrigley (2018)]] 解构了从第一级 [[Randomised Controlled Trials|RCT]] 到第二级元分析再到第三级[[Meta-meta-analysis|元-元分析]]（如[[John Hattie|哈蒂]]的《[[Visible Learning|可见的学习]]》（Visible Learning，VL） and [[Education Endowment Foundation|EEF]] 工具包）的逐级消洗过程，指出“洗涤”使得因果解释性信息完全消失，主张转向探求“背景-机制-结果”的实在论综合([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 13]])。

---

## 争议与批评

> [!tension] 核心争议
> 围绕异质性处理的核心分歧在于：
> - **[[Positivism|实证主义]]技术[[Paradigm|范式]]** 认为通过统计技术（如[[Moderator Analysis|调节变量分析]]或[[Fixed-Effect and Random-Effects Models|随机效应模型]]）足以在数字层面平差 and 修正异质性，以计算可供决策参考 of 平均效应。
> - **[[Critical Realism|批判实在论]]与[[Realist Evaluation|实在论评估]]范式** 主张在开放系统中，异质性无法通过数学加权来解决。当合并的研究具有异质性时，计算平均效应是数学上的错误。必须转向对个案进行质性、深层的理论还原，寻找底层因果机制([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 13]])。

> [!warning] 方法论批评与适用局限
> - **测量学系统偏误（Simpson 2017）** [[Argument_Simpson_2017_JEP|Simpson (2017)]] 进一步指出，在 [[Education Endowment Foundation|EEF]] 工具包等平台中，所谓的异质性变异并不一定反映了实际教育成效的多样性，而往往是由测量学的系统性偏差所致，包括对照组效应、范围限制（标准差分母收窄）以及测试设计偏误([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 12]])。

---

## 实证数据

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Higgins_2016_RE|Higgins (2016)]] — 系统介绍了异质性检验的统计学机制（Q、I²、固定/随机模型） and [[Moderator Analysis|调节变量分析]]的价值。
> - [[Argument_Terhart_2011_JCS|Terhart (2011)]] — 警示[[Meta-meta-analysis|元-元分析]]（如[[John Hattie|约翰·哈蒂]]的研究）存在变异性与稳定性困境，在累积中导致了原始经验信息的丢失。
> - [[Argument_Wrigley_2018_BERJ|Wrigley (2018)]] — 对比分析了 [[Education Endowment Foundation|EEF]] 工具包中的“反馈”和“教学助理”等类目，揭示了多级统计聚合抹除教学异质性所带来的[[Praxis|实践]]与政策风险。
> - [[Argument_Wiliam_2019|Wiliam (2019)]] — 以反馈研究的变异和[[Tracking|能力分组]]研究的教师变异为例，论证了去情境化平均[[Effect Size|效应量]]的误导性。
