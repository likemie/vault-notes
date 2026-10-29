---
title: Sampling Error
aliases:
  - 抽样误差
  - sampling distribution
  - 抽样分布
summary: "从同一总体中多次随机抽样时样本统计量围绕总体真实参数的理论波动；度量从样本推断总体的随机不确定性，在元分析中作为研究内抽样方差与研究间真实异质性相对立，其准确估计依赖于样本独立性假设与逆方差加权机制"
type: concept
domain: "research-methodology"
related_count: 42
related_level: 4
related_stars: "💎⭐"
related_color: "#fdba74"
tags:
  - method/sampling
  - quantitative-research
  - statistics
  - meta-analysis
  - evidence-synthesis
related_concepts:
  - "[[Study Population and Sample]]"
  - "[[Scientific Method]]"
  - "[[Publication Bias]]"
  - "[[Reliability]]"
  - "[[Artefact]]"
  - "[[Heterogeneity]]"
  - "[[Floor and Ceiling Effects]]"
  - "[[Variable]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Type I and Type II Errors]]"
  - "[[Visible Learning]]"
  - "[[Document]]"
  - "[[Problem-Based Learning]]"
  - "[[Direct Instruction]]"
related_theories:
  - "[[Central Limit Theorem]]"
related_methods:
  - "[[Effect Size]]"
  - "[[Standard Error]]"
  - "[[Research Synthesis]]"
  - "[[Meta-analysis]]"
  - "[[Between-Study Variance]]"
  - "[[Random Sampling]]"
  - "[[Confidence Interval]]"
  - "[[Sample Size Determination]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Meta-meta-analysis]]"
  - "[[Sampling Frame]]"
  - "[[Fixed-Effect Model]]"
  - "[[Descriptive Analysis]]"
  - "[[Theoretical Sampling]]"
  - "[[Funnel Plot]]"
  - "[[Fail-Safe N]]"
  - "[[Multilevel Egger's Test]]"
  - "[[Causal Modeling]]"
  - "[[Random-Effects Model]]"
  - "[[Small Study Effects]]"
related_persons:
  - "[[Christof Wecker]]"
  - "[[John Hattie]]"
  - "[[Gene Glass]]"
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
  - "[[Argument_Wecker_2016_ZfE]]"
  - "[[Argument_Higgins_2016_ROE]]"
  - "[[Argument_Johnson_2023_CritEduc]]"
confidence: high
status: completed
created: 2026-06-21
updated: 2026-10-29
---

---

> [!def] Sampling Error
> **抽样误差（Sampling Error）** 指从同一[[Study Population and Sample|目标总体]]中反复抽取样本时，样本统计量（如均值、比例、回归系数或标准化均数差[[Effect Size|效应量]]）围绕总体真实参数所产生的理论随机波动与离散程度。抽样误差并非操作疏失或实验失误的产物，而是由有限经验样本推断广义总体时固有的概率不确定性所致；其离散程度以[[Standard Error|标准误]]（Standard Error, SE）度量，受制于总体的变异性（$\sigma$ 或 $SD_{pop}$）与样本容量（$N$）。在现代[[Research Synthesis|证据综合]]与[[Meta-analysis|元分析]]中，抽样误差被形式化界定为 **“研究内抽样方差”（Within-study sampling variance, $v_i$）**，与反映真实情境变异的 **“[[Between-Study Variance|研究间真实方差]]”（Between-study variance, $\tau^2$）** 共同构成元分析双层方差分解的核心基石。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, pp. 149–151)]]; [[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 24–25)]]

> [!concept-lens] 概念透镜
> - **含义** 抽样误差度量的是无偏[[Random Sampling|随机抽样]]所产生的不可避免的偶然涨落，体现了[[Scientific Method|经验科学]]对客观规律渐近逼近的概率特征。
> - **用途** 为单项实证研究构建参数[[Confidence Interval|置信区间]]（$CI = \text{点估计} \pm Z \times SE$）、执行假设检验以及规划目标[[Sample Size Determination|样本量]]；在证据综合中充当[[Inverse-Variance Weighting|逆方差加权]]（$w_i = 1/v_i$）的精度基准。
> - **边界** 抽样误差严格局限于随机抽样引起的随机波动，既不包含测量工具的不精确性（测量误差），也不涵盖非随机性系统扭曲（抽样偏差与[[Publication Bias|发表偏倚]]）；在[[Meta-meta-analysis|二级元分析]]中，抽样误差公式的成立高度依赖于主要研究样本相互独立的充要条件。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25, 29–30)]]

> [!boundary]- 概念边界
> - **不等于 抽样偏差（Sampling Bias）** 抽样偏差由抽样程序缺陷、[[Sampling Frame|抽样框]]覆盖不足或非随机选择导致，产生系统性的固定倾斜，即使无限扩大样本量也无法消除；抽样误差是随机波动的幅度，随样本量扩大以反比例 $1/\sqrt{N}$ 持续收敛至 0。
> - **不等于 测量误差（Measurement Error）** 测量误差源于量表[[Reliability|信度]]不足、仪[[Artefact|器物]]理故障或受试者作答偶然失误；抽样误差源于被试样本对总体代表性的随机概率离散。
> - **不等于 研究间真实[[Heterogeneity|异质性]]（Between-Study Heterogeneity, $\tau^2$）** 抽样误差是每个研究内部因抽样偶然性带来的误差方差（$v_i$）；异质性是不同研究因教学情境、干预时长、人群特质不同而具有的真实总体效应分布方差（$\tau^2$）。[[Fixed-Effect Model|固定效应模型]]假定 $\tau^2=0$、所有离散纯属抽样误差，在教育多情境下极易违背现实。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 39)]]
> - **严禁将抽样误差度量（SE）与总体标准差（SD）混为一谈** 标准差描述个体数据点在样本内部的离散度，标准误[[Descriptive Analysis|描述统计]]量在[[Theoretical Sampling|理论抽样]]分布上的离散度；在标准化均数差计算中误将标准误代入分母除数，会导致效应量虚增 $\sqrt{N}$ 倍的灾难性计量事故。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 27)]]

> [!citation-card] 抽样误差的客观随机本质
> 抽样误差不一定是抽样程序错误的结果。更确切地说，变异源于对不同个体的随机选择。若我们从总体中抽取大量等规模样本并测量均值，这些样本均值不会完全相同，其围绕总体均值的变异程度直接度量了抽样误差。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, p. 149)]]
>
> *Sampling error is not necessarily the result of mistakes made in sampling procedures. Rather, variations may occur due to the chance selection of different individuals... The standard deviation of the theoretical distribution of sample means is a measure of sampling error.*

---

> [!contrast-table] 抽样误差与相邻统计学概念多维辨析
> | 比较维度 | 抽样误差（Sampling Error） | 抽样偏差（Sampling Bias） | 测量误差（Measurement Error） | 研究间异质性（Heterogeneity, $\tau^2$） |
> |:---|:---|:---|:---|:---|
> | **误差性质** | 随机性理论波动（Random fluctuation） | 系统性偏差（Systematic distortion） | 工具或反应偶然/系统变异 | 跨情境真实分布离散（Real dispersion） |
> | **产生根源** | 有限经验样本对无限总体的随机代表性限制 | [[Sampling Frame\|抽样框]]缺陷、自选样本、有偏排除 | 量表[[Reliability\|信度]]不足、记录失真、[[Floor and Ceiling Effects\|天花板效应]] | 教学干预强度、受试学段、组织生态[[Heterogeneity\|异质性]] |
> | **度量形式** | 标准误（$\text{SE} = \text{SD}/\sqrt{N}$，抽样方差 $v_i$） | 偏差偏移量（$\text{Bias} = E(\hat{\theta}) - \theta$） | 测量标准误（$\text{SEM}_{\text{meas}} = s\sqrt{1-r_{xx}}$） | 研究间方差 $\tau^2$ 与异质性比率 $I^2$ |
> | **增大样本量 $N$ 的效应** | 以 $1/\sqrt{N}$ 速率收敛衰减，有效抵消随机误差 | **无法消除**，仅使有偏估计更加狭窄地偏离真值 | 无法通过单纯增加[[Sample Size Determination\|样本量]]消除 | 不随单项[[Study Population and Sample\|研究样本]]量增大而改变，反映客观多样性 |
> | **[[Research Synthesis\|证据综合]]中的应对方案** | 按逆方差赋权（$w_i = 1/v_i$）实现最佳线性无偏估计 | [[Funnel Plot\|漏斗图]]检验、[[Fail-Safe N\|失安全数]]、[[Multilevel Egger's Test\|多水平艾格回归]]剪补 | 潜[[Variable\|变量]]结构方程模型（[[Causal Modeling\|SEM]]）、测量误差校正 | 采用[[Random-Effects Model\|随机效应模型]]并将 $\tau^2$ 纳入加权分母 |

---

> [!feature] 抽样误差的数理支柱与运作要素
> - **[[Central Limit Theorem|中心极限定理]]（Central Limit Theorem）** 若从任何总体中反复抽取等大规模的大样本，样本均值的理论分布趋向于正态分布，其均值等于总体真实均值，标准差即为均值[[Standard Error|标准误]]（Rose & Sullivan, 1993, p. 144）。即便总体本身呈偏态，25 例以上的样本通常即可生成满足渐近正态性的均值抽样分布（Hopkins et al., 1996, p. 159）。
> - **均值标准误（Standard Error of the Mean, [[Causal Modeling|SEM]]）** 样本均值抽样分布的理论标准差，基本公式为 $\text{SEM} = \frac{SD_{pop}}{\sqrt{N}} \approx \frac{SD_s}{\sqrt{N}}$。分母中的开方运算确立了抽样误差对[[Sample Size Determination|样本量]]的非线性敏感性：将抽样误差减半需要样本量扩大 4 倍，将抽样误差缩小至十分之一需要样本量扩大 100 倍。
> - **分类比例标准误（Standard Error of Proportions）** 针对分类或百分比数据，抽样误差公式表达为 $\text{SE}_p = \sqrt{\frac{P(100 - P)}{N}}$；在非置换有限总体中引入有限总体校正系数（Finite Population Correction, FPC）：$fpc = \sqrt{1 - \frac{N}{N_{pop}}}$，样本占总体比例越高，抽样误差衰减越显著。
> - **两级[[Meta-analysis|元分析]]中的抽样方差传递** 在一级元分析中，单项研究[[Effect Size|效应量]]抽样方差按独立双组标准误计算；在[[Meta-meta-analysis|二级元分析]]中，汇总抽样误差为各元分析方差倒数和的开方（$\text{SE}_D = \sqrt{1/\sum W_j}$）。该公式在代数上成立的根本公理在于主要[[Study Population and Sample|研究样本]]互不重叠。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25, 37)]]

> [!logic-map]- 抽样误差产生、测量收敛与两级元分析加权逻辑链
> ```mermaid
> flowchart LR
>     A["总体真实参数分布<br/>存在客观方差与均值"] --> B["有限样本随机抽取<br/>引发样本间理论均值涨落"]
>     B --> C["样本量扩大与方差收敛<br/>标准误以 1/sqrt(N) 速率递减"]
>     C --> D["单级逆方差最优加权<br/>以研究抽样精度为权重合并效应"]
>     D --> E["两级跨层加权等价定理<br/>充要条件：原始研究完全独立无重叠"]
>     E --> F["文献重叠与协方差污染<br/>抽样误差被严重低估致假阳性膨胀"]
> ```

---

## 围绕概念形成的命题

---

> [!concept-proposition] 命题一｜[[Sample Size Determination|样本量]]对抽样误差的抑制呈现显著的边际收益递减规律
> **探讨维度　[[Sample Size Determination|样本量]]规划与统计功效边界** 探讨样本规模与抽样误差衰减之间的非线性关系，辨析小样本风险与大样本资源配置的平衡点。

> [!claim] Cohen, Manion & Morrison; Gorard
> **样本规模门槛与边际递减规律** 样本量与抽样误差之间存在确定的反比开方关系，少于 30 例的样本处于统计高危区间，允许过大的抽样误差存在并导致极低的统计功效；当样本量超过约 80 例后，单纯依靠增加样本量对压缩抽样误差的边际贡献急剧放缓。若总体中某[[Variable|变量]]本身的变异性（$\sigma$）极大（例如智商测验或复杂教育成就），控制抽样误差所需的样本量远大于低变异变量。大样本的核心意义在于建立足够的统计检验功效，将实质性[[Effect Size|效应量]]从[[Random Sampling|随机抽样]]变异中清晰分离出来。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, pp. 145, 151–152)]]

---

> [!concept-proposition] 命题二｜[[Fixed-Effect Model|固定效应模型]]将所有研究间变异机械归因于抽样误差，违背教育干预的生态现实
> **探讨维度　双层方差分解与同质性破产** 探讨[[Meta-analysis|元分析]]中将真实情境[[Heterogeneity|异质性]]降格为抽样误差所引发的推断失真。

> [!claim] Higgins; Wecker et al.
> **[[Fixed-Effect Model|固定效应]]同质性假设与异质性降格批判** [[Fixed-Effect Model|固定效应模型]]假定所有纳入研究均在估计同一个永恒不变的真实参数，所有研究间观察到的离散纯粹是由有限样本的抽样误差（$v_i$）引起的。然而[[Christof Wecker|克里斯托夫·韦克尔]]（Christof Wecker）等人指出，在复杂教育研究中，受试学生学段、教师素养、教学时长与组织情境千差万别，必然存在显著的[[Between-Study Variance|研究间真实方差]]（$\tau^2 > 0$）。强行假定所有变异皆属抽样误差，会导致合并估计量的[[Confidence Interval|置信区间]]严重虚假收窄，向外推论的超总体效度彻底破产。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 24–25)]]; [[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 39)]]

---

> [!concept-proposition] 命题三｜[[Primary and Secondary Documents|原始文献]]重叠违背独立性假设，致使两级元分析的抽样误差被严重低估
> **探讨维度　独立性破产与[[Type I and Type II Errors|第一类错误]]率膨胀** 探讨主要研究重复纳入如何破坏抽样分布方差的计算基石，制造出虚假精确的统计幻觉。

> [!claim] Wecker et al.; Johnson & Janzen
> **协方差未校正导致的假性精确与假阳性灾难** [[Meta-meta-analysis|二级元分析]]经典方差公式 $\text{Var}(D) = 1/\sum W_j$ 的严格数理前提是各一阶元分析收录的主要研究互不重叠、协方差为 0。韦克尔等人审计证实，[[John Hattie|哈蒂]]《[[Visible Learning|可见的学习]]》容忍不同一阶元分析之间高达 93% 的主要研究相互重叠。由于重叠研究引入了高度正相关的协方差项（$\text{Cov} > 0$），若仍按独立抽样误差公式相加，会导致分母被虚假人为放大，从而使合并效应量的真实抽样误差（[[Standard Error|标准误]]）被大幅低估，计算出的 $z$ 值虚高，造成第一类错误率（伪阳性）严重失控。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25, 29–30)]]; [[Argument_Johnson_2023_CritEduc|(Johnson & Janzen, 2023, pp. 25–26)]]

---

> [!concept-proposition] 命题四｜混淆抽样误差（SE）与样本标准差（SD）会导致效应量虚增数倍的灾难性计量事故
> **探讨维度　计量审计中的除数混淆事故** 探讨一阶[[Document|文献]]数据提取中将抽样分布统计量与原始样本分布参数混淆带来的倍增放大效应。

> [!claim] Wecker et al.
> **标准误作为效应量除数引发的虚假暴增** 在初级研究与元分析数据提取规程中，计算标准化均数差（Cohen's $d$）的分母必须是样本原始数据的联合标准差（SD）。韦克尔等人在对哈蒂引用的 Eisenstaedt et al.（1990）关于“[[Problem-Based Learning|基于问题的学习]]”元分析进行微观数据审计时发现，原作者在提取主要研究数据时，错误地将报告的均值标准误（[[Causal Modeling|SEM]]）当作样本标准差（SD）作为除数代入公式。由于 $\text{SEM} = \text{SD}/\sqrt{N}$，以标准误为除数直接导致效应量被虚假放大了 $\sqrt{N}$ 倍——原本仅为 $d = 0.08$ 的微弱真实效应，被严重误算为 $d = 0.79$ 的显著高效应，暴增近十倍。此类抽样统计量概念混淆若未被严格审计，会彻底污染整座循证证据大厦。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 27)]]

---

> [!contrast-table] 围绕抽样误差形成的理论命题总览
> | 命题类型 | 核心主张 | 统计与方法论机制 | 代表学者 |
> |:---|:---|:---|:---|
> | **样本量边际收益递减** | 样本量以 $1/\sqrt{N}$ 压缩抽样误差，存在 30 例警戒线与 80 例递减拐点 | 均值抽样分布方差衰减、[[Central Limit Theorem\|中心极限定理]]、统计功效保障 | [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|Cohen et al. (2011)]]; Gorard (2003) |
> | **模型假定与误差二元分解** | 区分研究内抽样误差与研究间真实异质性，固定效应模型在此存在根本盲区 | 方差分解模型（$v_i$ vs $\tau^2$）、同质性假设检验 | [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]]; [[Argument_Higgins_2016_ROE\|Higgins (2016)]] |
> | **独立性破坏与误差低估** | 文献重叠引入正协方差，未加校正使抽样误差严重低估并诱发假阳性失控 | 协方差交叉项缺失、[[Inverse-Variance Weighting\|逆方差加权]]膨胀、伪精确诊断 | [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]]; [[Argument_Johnson_2023_CritEduc\|Johnson and Janzen (2023)]] |
> | **除数混淆与效应量虚增** | 误将标准误（SE）当标准差（SD）计算效应量，导致数值虚假放大 $\sqrt{N}$ 倍 | 标准化均数差分母混淆、数据逆向还原取证 | [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]] |

---

> [!dev-timeline] 抽样误差理论与方法演进
> - **1733–1812 — 抽样分布与[[Central Limit Theorem|中心极限定理]]发端** 棣莫弗（De Moivre）与拉普拉斯（Laplace）推导正态近似，高斯确立最小二乘与高斯-马尔可夫方差最优理论，为抽样分布离散度提供数学工具。
> - **1908 — 小样本抽样理论突破** 戈塞特（“Student”）发表 $t$ 分布，明确区分总体标准差 $\sigma$ 与小样本估算的[[Standard Error|标准误]]，确立小样本抽样误差的精准推断边界。
> - **1976 — [[Meta-analysis|元分析]]中的抽样误差[[Inverse-Variance Weighting|逆方差加权]]** 罗森塔尔（Rosenthal）与格拉斯（[[Gene Glass]]）将抽样误差形式化为单项研究方差（$v_i$），并引入以逆方差（$w_i = 1/v_i$）赋权的最优加权方案，奠定现代证据合成基石。
> - **2011 — 教育研究抽样误差体系的系统梳理** Cohen, Manion and Morrison（2011, Ch. 8）系统规范了教育调查中均值标准误、分类比例标准误、有限总体校正及 30/80 例样本规模边际收益递减法则。
> - **2016 — 二级[[Research Synthesis|证据综合]]中抽样误差失效与除数事故的法医式审计** [[Christof Wecker|克里斯托夫·韦克尔]]（[[Argument_Wecker_2016_ZfE|Wecker et al., 2016]]）系统证明两级元分析成立依赖于原始研究独立的充要条件；揭露 93% 文献重叠导致抽样误差被严重低估的假性精确机制，并实证诊断出将标准误代替标准差计算[[Effect Size|效应量]]导致数值暴增近十倍的重大计量事故。

---

> [!debates] 学术争议
>
> > [!axis] 单一抽样误差建模 vs 真实[[Heterogeneity|异质性]]多层吸收
> > 探讨证据合成中应当把[[Effect Size|效应量]]变异主要归结为抽样误差，还是必须纳入研究间真实异质性。
> >
> > - **[[Fixed-Effect Model|固定效应]]教条** 坚持所有研究间离散纯属抽样误差（$v_i$），以最大化统计检验力和追求单一普适平均值。
> > - **[[Random-Effects Model|随机效应]]与现实主义反思** 坚持教育实践的复杂性与情境多样性使真实异质性（$\tau^2$）必然存在，忽视真实方差会将真正的教学机制差异误当作抽样噪声强行抹杀。[[Argument_Higgins_2016_ROE|(Higgins, 2016, p. 39)]]; [[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 24–25)]]
>
> > [!axis] 二阶算术平均 vs [[Inverse-Variance Weighting|逆方差加权]]
> > 探讨在二级综合中是否允许跨过抽样误差悬殊的现实直接进行简单平均。
> >
> > - **算术平均操作主义（Hattie, 2009）** 对各一级[[Meta-analysis|元分析]]进行无权简单算术平均，声称宏观效应足够大时微观抽样差异可以忽略。
> > - **数理加权规范（[[Argument_Wecker_2016_ZfE|Wecker et al., 2016]]; [[Argument_Johnson_2023_CritEduc|Johnson & Janzen, 2023]]）** 指出只有严格以一级元分析抽样误差倒数（$W_j = 1/v_{d_j}$）赋权，二级汇总才具有代数合法性；无权简单平均彻底剥夺了大样本抵消抽样误差的基本统计功能。

> [!warning] 抽样误差掩蔽下的系统性[[Publication Bias|发表偏倚]]
> 统计学家长期警示，抽样误差是无方向的随机正负波动，而现实发表生态充斥着对微弱或负向效应量的系统性过滤。小样本由于抽样误差极大，极易因偶然波动产生极大的伪阳性效应量；若这些异常值因跨过显著性门槛而获得优先发表，便会形成经典的“[[Small Study Effects|小研究效应]]”（Small-Study Effects），将原本对称的抽样误差异化为极度右偏的学术偏倚。

---

> [!index-table] 抽样误差度量、计算实例与计量事故审计表
> | 案例 / 审计项目 | 样本规模与情境参数 | 计算公式与输入维度 | [[Theoretical Sampling\|理论抽样]]误差 / 输出数值 | 方法论定性与现实后果 |
> |---|---|---|---|---|
> | **学校午休政策民意调查（小样本）** | 随机抽取 $N = 25$ 名学生，赞成率 $P = 66\%$（$Q = 34\%$） | $\text{SE}_p = \sqrt{\frac{66 \times 34}{25}}$ | $\text{SE} = 9.4\%$（赞成率区间：$56.6\% \sim 75.4\%$） | 抽样误差极大，无法提供确凿的决策支持。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|(Cohen et al., 2011, p. 151)]] |
> | **学校午休政策民意调查（中样本）** | 随机抽取 $N = 100$ 名学生，赞成率 $P = 66\%$ | $\text{SE}_p = \sqrt{\frac{66 \times 34}{100}}$ | $\text{SE} = 4.5\%$（赞成率区间：$61.5\% \sim 70.5\%$） | 样本量扩大 4 倍，抽样误差精确减半。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|(Cohen et al., 2011, p. 151)]] |
> | **学校午休政策民意调查（全校普查级）** | 随机抽取 $N = 1,000$ 名学生，赞成率 $P = 66\%$ | $\text{SE}_p = \sqrt{\frac{66 \times 34}{1,000}}$ | $\text{SE} = 1.5\%$（赞成率区间：$64.5\% \sim 67.5\%$） | 抽样误差显著收窄，解释了全国性民调多采集 1,000–1,500 例样本的原因。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08\|(Cohen et al., 2011, p. 151)]] |
> | **PBL 教学法数据审计：Eisenstaedt et al. (1990)** | 基于问题的学习初级研究，主要样本 $N$ 约数十人 | 误用 $\text{SEM}$ 作为除数计算标准化均数差 $d$ | 报告效应量 $d = 0.79$，经审计校正后真实效应量仅为 $d = 0.08$ | 误将标准误代入标准差，导致效应量虚增近 **10 倍**，直接污染宏观排行榜。[[Argument_Wecker_2016_ZfE\|(Wecker et al., 2016, p. 27)]] |
> | **[[Direct Instruction\|直接教学]]法数据审计：Haas (2005)** | 纳入 36 项初级研究，其中高达 20 项完全未报告原始均值与标准差 | 缺少主要研究抽样方差数据，无法按逆方差准确加权 | 有效研究量从 36 篇断崖式塌陷至 16 篇，[[John Hattie\|哈蒂]]仍直接采用未加权汇总 | 原始数据缺失破坏了抽样误差推算基础，导致二级合成完全丧失数理精度。[[Argument_Wecker_2016_ZfE\|(Wecker et al., 2016, pp. 27–28)]] |
> | **[[Meta-meta-analysis\|二阶元分析]] 93% 文献重叠模拟** | 哈蒂《[[Visible Learning\|可见的学习]]》网络学习主题所收录的[[Meta-analysis\|元分析]]集合 | 未建模正相关协方差 $\text{Cov}_{ji} > 0$ 直接按独立方差公式相加 | 二级合并[[Standard Error\|标准误]]被低估逾 **40%**，假阳性概率成倍膨胀 | 违背独立性假设制造了虚假统计精确性，使大量无效干预被包装为高效干预。[[Argument_Wecker_2016_ZfE\|(Wecker et al., 2016, pp. 29–30)]] |

---

> [!citation-card] 均值[[Standard Error|标准误]]的抽样变异性
> 抽样分布的标准差是抽样误差的度量，称为均值的标准误（[[Causal Modeling|SEM]]）。抽样误差取决于总体的变异性和[[Sample Size Determination|样本量]]：总体变异性越小，抽样误差越小；样本量越大，抽样误差越小。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|(Cohen et al., 2011, Ch. 8, pp. 150–151)]]
>
> *The standard deviation of the theoretical distribution of sample means is a measure of sampling error and is called the standard error of the mean (SEM).*

> [!citation-card] 审查中的标准误混淆诊断
> 在对主要研究的重新分析中，我们发现原本报告为高成效的干预实际上几乎没有效果。显然，原作者在计算标准化均数差时使用了标准误而不是标准差作为除数，从而将[[Effect Size|效应量]]放大了数倍。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, p. 27)]]
>
> *Offenbar wurde hier der Standardfehler statt der Standardabweichung verwendet... was zu einer massiven künstlichen Vergrößerung der Effektstärke führte.*

> [!citation-card] 文献重叠对抽样独立性的瓦解
> 当不同[[Meta-analysis|元分析]]收录相同的原始研究时，各元分析之间的抽样独立性彻底破产。如果忽视非零协方差的存在，常规方差公式计算出的标准误会被大幅低估，使研究者误以为掌握了高度精确的证据。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 25, 29)]]
>
> *Wenn sich Metaanalysen in den Primärstudien überschneiden, liegt keine stochastische Unabhängigkeit mehr vor... Der resultierende Standardfehler wird systematisch unterschätzt.*

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 系统阐明教育研究中抽样误差、均值[[Standard Error|标准误]]、分类比例标准误、[[Central Limit Theorem|中心极限定理]]及样本容量边际递减法则，提供比例标准误的递进计算数值实例。
> - [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] — 系统推导两级[[Meta-analysis|元分析]]成立的代数等价性定理；法医式揭露文献重叠导致抽样误差低估的假阳性膨胀机制，以及误将标准误当标准差计算导致[[Effect Size|效应量]]虚增近十倍的重大计量事故。
> - [[Argument_Higgins_2016_ROE|Higgins (2016)]] — 阐明元分析中抽样误差（研究内方差）与研究间真实[[Heterogeneity|异质性]]的二元方差分解，辨析[[Fixed-Effect Model|固定效应]]与[[Random-Effects Model|随机效应模型]]在处理抽样波动时的根本分歧。
> - [[Argument_Johnson_2023_CritEduc|Johnson and Janzen (2023)]] — 解构[[Meta-meta-analysis|二阶元分析]]中忽视抽样误差差异的无权简单算术平均弊端，论证[[Sample Size Determination|样本量]]加权对于消除[[Random Sampling|随机抽样]]偏差的必要性。

---

> [!entry-map] 领域应用
>
> | 条目 | 类型 | 关联与贡献 |
> |:-----|:-----|:-----|
> | [[Standard Error\|标准误]] | 方法 | 标准误是抽样误差在[[Theoretical Sampling\|理论抽样]]分布上的具体统计量度形式。 |
> | [[Central Limit Theorem\|中心极限定理]] | 理论 | 为抽样误差的大样本渐近正态分布特征提供核心数学证明。 |
> | [[Sample Size Determination\|样本量确定]] | 方法 | 样本量规划旨在以最优投入将抽样误差压制在预定[[Confidence Interval\|置信区间]]之内。 |
> | [[Meta-analysis\|元分析]] | 方法 | 元分析以抽样误差的倒数（逆方差）进行加权合成，实现最优线性无偏估计。 |
> | [[Fixed-Effect Model\|固定效应模型]] | 方法 | 固定效应模型预设[[Between-Study Variance\|研究间方差]]为 0，假定所有观察变异纯属抽样误差。 |
> | [[Random-Effects Model\|随机效应模型]] | 方法 | 随机效应模型将总变异显式分解为研究内抽样误差与研究间真实方差。 |
> | [[Inverse-Variance Weighting\|逆方差加权]] | 方法 | 依据单项研究抽样方差的倒数分配权重，确保抽样误差小的研究获得主导权重。 |
> | [[Visible Learning\|可见的学习]] | 概念 | [[John Hattie\|哈蒂]]因容忍 93% 文献重叠导致抽样误差严重低估，成为反思抽样独立性的经典反面教材。 |
