---
title: Propensity Score Matching
aliases:
  - 倾向得分匹配
  - PSM
  - 倾向评分匹配
  - 倾向得分匹配法
  - Propensity Score Matching Method
summary: "一种基于可观测协变量将多维特征压缩为单一参与概率（倾向得分），进而对处理组与对照组进行配对平衡以模拟随机分配的非实验因果推断方法。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 27
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/propensity-score-matching
  - method/quantitative
  - method/causal-inference
  - method/quasi-experiment
related_concepts:
  - "[[Causality]]"
  - "[[Variable]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Counterfactual]]"
  - "[[Internal Validity]]"
  - "[[Academic Achievement]]"
  - "[[Dependent Variable]]"
  - "[[Effective Sample Size]]"
  - "[[Heterogeneity]]"
  - "[[Paradigm]]"
related_theories: []
related_methods:
  - "[[Matching]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Random Assignment]]"
  - "[[Difference-in-Differences]]"
  - "[[Regression Discontinuity Design]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Sample Size Determination]]"
  - "[[Pre-test and Post-test]]"
  - "[[Questionnaire]]"
  - "[[Confidence Interval]]"
  - "[[Standard Error]]"
  - "[[Observation Method]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[National Pupil Database]]"
  - "[[Education Endowment Foundation]]"
  - "[[Researching School Choices]]"
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
confidence: high
status: active
created: 2026-09-15
updated: 2026-09-15
---

# Propensity Score Matching

---

## 定义

> [!def] 方法定义
> **倾向得分匹配（Propensity Score [[Matching]]，简称 PSM）**是由保罗·罗森鲍姆与唐纳德·鲁宾（Rosenbaum & Rubin, 1983）奠定的经典准实验[[Causality|因果推断]]方法。其核心思想是：利用处理前丰富且关键的可观测基线协[[Variable|变量]]向量 $\mathbf{X}_i$，通过概率回归模型将个体面临的多维混杂特征压缩为一维的条件参与概率标量——**倾向得分（Propensity Score）** $e(\mathbf{X}_i) = \Pr(Z_i = 1 \mid \mathbf{X}_i)$；进而在处理组与对照组之间寻找倾向得分高度相近的个体进行配对（Matching），以此模拟[[Randomised Controlled Trials|随机对照试验]]中两组基线特征期望相等的无偏状态，有效校正由于非随机选择产生的可观测选择偏误（Selection on Observables）。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 55–56)]]

> [!method-scope] 方法范围
> - **研究对象** 大规模教育行政调查截面数据、学生追踪档案（如英国[[National Pupil Database|国家学生数据库]]）中自愿或按规则采纳某项政策、课程模式或办学机制的非实验样本。
> - **问题类型** 因果效应评估问题（回答“当控制所有可观测背景差异后，加入某种办学模式相比未加入模式的学校平均带来了多少学业增益”）。
> - **[[Unit of Analysis|分析单位]]** 学生个体、班级或整所学校。
> - **输出形式** 处理组平均处理效应（Average Treatment Effect on the Treated, ATT）、总体平均处理效应（ATE）、配对权重、协变量标准化偏差均衡图。

> [!citation-card] 准实验匹配在学校体制抉择评估中的机制应用（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）
> 面对学校宏观办学机制转型等无法强行人为[[Random Assignment|随机化]]的现实难题，英国 [[Education Endowment Foundation|EEF]] 设立了“[[Researching School Choices|研究学校选择]]”（Researching School Choices）专属资助流。该资助流不再依赖传统 RCT，而是依托国家学生数据库（NPD）详实的纵向普查大数据，采用[[Difference-in-Differences|双重差分法]]（DID）、倾向得分匹配（PSM）与回归断点设计（[[Regression Discontinuity Design|RDD]]）等严密的准实验架构，科学评估真实教育生态下的宏观治理决策。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 55–56)]]
>
> *“In 2019, the EEF opened the 'Researching School Choices' funding stream... exploiting naturally occurring policy changes and variations using longitudinal data from the National Pupil Database (NPD). [[Quasi-Experimental Designs]], including difference-in-differences and propensity score matching, enable rigorous evaluation where randomisation is not feasible.”*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与因果识别定位
> - **知识观** 根植于[[Counterfactual|反事实推理]]与鲁宾因果模型（Rubin Causal Model）。假定只要控制了影响处理选择与潜在线性产出的全部共同前置[[Variable|变量]]，非实验组别间的因果反事实即可通过概率加权或相近距离配对加以重构。
> - **核心识别假定**
>   1. **条件独立性假定（Conditional Independence / Unconfoundedness）** 给定协变量 $\mathbf{X}$，潜在产出 $(Y(1), Y(0))$ 与处理指派状态 $Z$ 统计独立，即 $(Y(1), Y(0)) \perp Z \mid \mathbf{X}$；
>   2. **共同支撑集假定（Common Support / Overlap）** 对于任意协变量取值，个体进入处理组与对照组的概率均处于开区间内，即 $0 < \Pr(Z=1 \mid \mathbf{X}) < 1$。
> - **有效性标准** [[Internal Validity|内部效度]]取决于协变量的完备性与匹配后各维度标准化均值差（SMD $< 0.10$）；统计推断必须考虑配对依赖性。
> - **不声称回答的问题** PSM 绝对无法消除未被观测到的混杂因素（如学生天赋动机、校长未公开领导力风格或校内隐性文化）。

> [!contrast-table] 匹配方法横向对比：PSM vs 粗化精确匹配 vs 协变量精确匹配 vs 逆概率加权
> | 匹配策略 | 空间压缩维度 | 维数灾难敏感度 | 协变量平衡机制 | 适用数据场景与主要瓶颈 |
> |---|---|---|---|---|
> | **倾向得分匹配（PSM）** | 压缩为单一概率标量 $[0, 1]$ | **极低**（彻底规避维数灾难） | 基于倾向得分绝对距离配对 | 协变量丰富、[[Sample Size Determination\|样本量]]充裕；但可能存在模型设定偏误。 |
> | **粗化精确匹配（CEM）** | 离散化分箱匹配 | 中等（取决于分箱细度） | 分箱内完全精确相同 | 样本量大、变量以分类为主；易导致共同支撑集外大量样本脱落。 |
> | **协变量精确匹配（Exact）** | 保持高维多变量全集 | **极高**（维数灾难严重） | 多维空间完全重合点 | 仅限少量离散控制变量；变量多时几乎无法找到任何匹配对。 |
> | **逆概率加权（IPW）** | 构造加权伪总体 | 较低（依赖概率模型） | 全样本基于概率倒数赋权 | 避免样本剔除损失；但在概率接近 0 或 1 时产生极端权重漂移。 |

> [!method-stack] 方法层级
> - **研究设计** 观察性比较研究、非等价对照组设计、政策事后评价。
> - **数据收集** 行政普查数据库（英国[[National Pupil Database|国家学生数据库]]）、学业前[[Pre-test and Post-test|后测]]档案、[[Questionnaire|问卷调查]]多维背景数据。
> - **分析方法** Logistic 回归估计得分、近邻匹配（Nearest-Neighbour）、卡尺匹配（Caliper/Radius）、核匹配（Kernel [[Matching]]）、局部线性匹配。
> - **辅助技术** 平衡性检验（Balance Diagnostics）、共同支撑集密度重叠图、罗森鲍姆边界（Rosenbaum Bounds）敏感性分析。

---

## 研究程序

> [!proc] 通用程序
> 1. **协[[Variable|变量]]挑选与外生性审查** 广泛搜集在政策干预发生前已确定的基线变量（[[Pre-test and Post-test|前测]]成绩、家庭经济背景、生源流动性等），严禁纳入受到干预结果反向污染的中介变量。
> 2. **拟合倾向得分模型** 采用 Logit 或 Probit 回归估计个体参与政策的条件概率，输出每位个体的倾向得分 $\hat{e}(\mathbf{X}_i)$。
> 3. **核查共同支撑集并实施配对** 绘制处理组与对照组的倾向得分概率密度分布图，剔除无重叠区域样本；依据研究目标选取合适匹配算法（如 1:1 无放回卡尺近邻匹配）。
> 4. **匹配后协变量平衡性诊断** 逐项检验所有协变量在匹配前后的标准化均值差（Standardised Mean Difference, SMD）与方差比，确保所有协变量的绝对偏差降至 0.10（或 0.05）阈值以下。
> 5. **估计平均处理效应并开展隐性偏误敏感性分析** 在配对样本集上计算平均处理效应（ATT）；利用 Rosenbaum Bounds 评估结果对潜在未观测混杂因素的抵御韧性。

### 量化分析模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 包含处理组与大量未受干预候选池个体的横截面或基线面板数据。
> - **核心变量**
>   - 处理状态变量 $Z_i$：1 = 处于处理组，0 = 处于对照池。
>   - 协变量向量 $\mathbf{X}_i$：个人人口学特征、先前[[Academic Achievement|学业成就]]、家庭社会经济地位、学校组织规模等。
>   - [[Dependent Variable|结果变量]] $Y_i$：后测成绩或学业增值。
> - **匹配参数设置** 卡尺通常设定为倾向得分标准差的 0.2 倍（$0.2 \times \sigma_{\text{logit}(e)}$）。

> [!formula-step] 公式步骤　倾向得分估计模型
> $$e(\mathbf{X}_i) \equiv \Pr(Z_i = 1 \mid \mathbf{X}_i) = \frac{\exp(\mathbf{X}_i' \boldsymbol{\beta})}{1 + \exp(\mathbf{X}_i' \boldsymbol{\beta})}$$
>
> **这个公式在做什么** 利用多维基线特征向量 $\mathbf{X}_i$ 与待估计参数 $\boldsymbol{\beta}$，通过 Logistic 链接函数计算个体进入处理组的预测条件概率标量 $e(\mathbf{X}_i) \in (0, 1)$。
>
> **符号说明**
> - $Z_i$：二值处理分配变量。
> - $\mathbf{X}_i$：影响选择与产出的多维混杂协变量向量。
> - $e(\mathbf{X}_i)$：倾向得分标量。
>
> **数学直觉** 罗森鲍姆与鲁宾证明：倾向得分是一个“平衡得分（Balancing Score）”。只要在控制全部协变量时条件独立性成立，那么仅仅控制一维标量 $e(\mathbf{X})$ 时，条件独立性亦同样成立，从而将 $K$ 维特征匹配的高维难题转化为一维实轴上的距离寻找。
>
> **注意事项** 模型目标是实现组间协变量的均衡，而非单纯追求最高的分类准确率或拟合度。

> [!formula-step] 公式步骤　处理组平均处理效应（ATT）估计
> $$\tau_{\text{ATT}} = \frac{1}{N_T} \sum_{i \in T} \left[ Y_i - \sum_{j \in C} w(i, j) Y_j \right]$$
>
> **这个公式在做什么** 计算处理组个体的实际产出 $Y_i$ 与其所配对的对照组加权[[Counterfactual|反事实]]产出 $\sum_j w(i, j) Y_j$ 之间的差值，并在全体处理组样本上取平均，得到干预对实际参与者的净效应。
>
> **符号说明**
> - $N_T$：处于共同支撑集内的处理组[[Effective Sample Size|有效样本量]]。
> - $T, C$：处理组与对照组配对样本集。
> - $w(i, j)$：对照个体 $j$ 赋予处理个体 $i$ 的匹配权重（在 1:1 近邻匹配中为 1，在核匹配中为核权重）。
>
> **结果怎么读** $\tau_{\text{ATT}} > 0$ 且[[Confidence Interval|置信区间]]不包含 0，表明接受政策干预的学校或学生在匹配后显著优于具有同等入选概率的对照群体。
>
> **注意事项** 估计值的有效性完全依赖于“无不可观测混杂”假定。在英国 [[Education Endowment Foundation|EEF]] 的实证应用中，PSM 常被与[[Difference-in-Differences|双重差分法]]串联为匹配双重差分（PSM-DID），利用 DID 消除不随时间变化的未观测[[Heterogeneity|异质性]]（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）。

> [!software-impl] 软件实现
> - **推荐软件** R (`MatchIt`, `optmatch`, `cobalt`), Stata (`psmatch2`, `teffects psmatch`), Python (`DoWhy`, `causalinference`).
> - **实现流程**
>   1. 估计倾向得分并实施 1:1 卡尺匹配：
>      - Stata: `psmatch2 treat covars, outcome(score) n(1) caliper(0.05) common`
>      - R: `matchit(treat ~ covars, data = df, method = "nearest", caliper = 0.05)`
>   2. 协变量平衡性核查与绘图：
>      - R: `summary(m_out); plot(summary(m_out))`
>   3. 敏感性分析：
>      - Stata: `rbounds score, gamma(1(0.1)2)`
> - **报告标准** 完整报告匹配前后各变量标准化偏差（SMD）、匹配丢弃[[Sample Size Determination|样本量]]、共同支撑集重合比例及 ATT 点估计与稳健[[Standard Error|标准误]]。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - 拥有海量行政普查数据库，且能够采集到极丰富基线学生与学校特征的大规模评估项目（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）；
>   - 处理组[[Sample Size Determination|样本量]]较小但存在庞大的未受干预“候选对照池”的情形；
>   - 评估自愿报名或按既有政策选择开展特定教改项目的真实成效。
> - **谨慎使用**
>   - 缺乏关键前置特征（如缺少历史成绩[[Pre-test and Post-test|前测]]、家庭背景信息极度匮乏）；
>   - 处理组与对照池特征极其悬殊，导致共同支撑集范围极窄、匹配后丢弃绝大多数样本的研究。
> - **不适合使用**
>   - 处理分配高度由隐藏动机（如强烈进取心、未公开人际关系）决定的情境，此类隐性偏误无法被可观测[[Variable|变量]]捕捉。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源**
>   - **不可观测混杂偏差（Hidden Bias）** PSM 最大的方法学软肋：它仅能平衡纳入模型的“可观测”[[Variable|变量]]，完全无法抵御未观测变量带来的内生选择性偏误。
>   - **样本代表性损耗（Support Dropping）** 为了追求严格匹配，处于共同支撑集外的极端样本往往被直接剔除，导致最终结论无法外推至整个目标人群。
> - **适用边界** 结论仅限于具有共同支撑重叠的局部样本（ATT）。
> - **误用风险** 以为“经过 PSM 匹配就等于做了真正随机试验”，盲目夸大因果推论力度，忽视对未观测偏误的稳健性敏感检验。
> - **补救方式** 采用匹配[[Difference-in-Differences|双重差分法]]（PSM-DID），将横向可观测匹配与纵向时间差分双重结合；运用 Rosenbaum Bounds 计算隐藏偏误临界值 $\Gamma$。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 可观测[[Variable|变量]]控制充分性 vs 隐性动机选择
> > [[Observation Method|观察研究]]中能否通过增加控制变量彻底解决选择偏差。
> >
> > - **乐观派主张** 随着大数据与国家级行政数据库的发展，只要纳入了细致的微观历史学业、社区与家庭指标，绝大部分选择机制已被成功代理。
> > - **怀疑派批评** 学校管理层的改革远见、教师的团队凝聚力与进取文化属于典型的不可观测因素，自愿采纳某种办学机制的学校本身就是“不同质的”，PSM 极易给出虚假的因果信心。
>
> > [!axis] 倾向得分标量压缩 vs 粗化精确匹配（CEM）争鸣
> > 统计学界关于是否应该将多维数据压缩为概率标量的争论（King & Nielsen, 2019）。
> >
> > - **CEM 主张** 批评 PSM 盲目压缩变量维数可能导致在具体某个关键变量上的反向失衡，主张直接在关键维度上进行分箱粗化精确匹配。
> > - **PSM 辩护** 指出在微观连续变量极多的复杂教育真实数据中，CEM 极易因空箱问题遭遇严重的样本脱落，而 PSM 依然是可行性最强且经过充分实证检验的基准[[Paradigm|范式]]。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Quasi-Experimental Designs]] | 上位分类 | PSM 所属的核心准实验因果识别方法族。 |
> | [[Difference-in-Differences]] | 协同方法 | 两者结合构成 PSM-DID，纵横双向同时克服可观测与时间不变未观测偏误。 |
> | [[Matching]] | 基础概念 | PSM 是匹配方法家族中基于概率距离压缩的最主流实现分支。 |
> | [[Regression Discontinuity Design]] | 替代方法 | 存在刚性分数准入切分点时的优先准实验替代工具。 |
> | [[Randomised Controlled Trials]] | 对标黄金标准 | PSM 通过在观察数据中构造平衡性以逼近 RCT 的[[Counterfactual\|反事实]]对照机制。 |
> | [[National Pupil Database]] | 数据基础 | 英国支撑学校与学生层面 PSM 协[[Variable\|变量]]精准匹配的国家级微观纵向大数据库。 |
> | [[Researching School Choices]] | 实践载体 | [[Education Endowment Foundation\|EEF]] 设立的依托 PSM 等准实验评估宏观学校办学选择的重大资助流。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 详述了英国 [[Education Endowment Foundation|EEF]] 突破对单一 [[Randomised Controlled Trials|RCT]] 的教条依赖，设立“[[Researching School Choices|研究学校选择]]”资助流，依托[[National Pupil Database|国家学生数据库]]运用[[Difference-in-Differences|双重差分法]]与倾向得分匹配评估学校宏观体制选择的因果成效。
