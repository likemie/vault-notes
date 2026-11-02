---
title: Matching
aliases:
  - 匹配法
  - 样本匹配
  - Matching Methods
summary: "在非随机或观察性研究中通过使处理组与对照组在可观测前置协变量分布上达成均衡以消除选择偏误、逼近反事实因果估计的准实验统计方法"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 25
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - matching
  - observational-studies
  - causal-inference
  - subject/research-methodology
  - method/quantitative
related_concepts:
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Counterfactual]]"
  - "[[Dependent Variable]]"
  - "[[Independent Variable]]"
  - "[[Stable Unit Treatment Value Assumption]]"
  - "[[Interaction Effect]]"
  - "[[Internal Validity]]"
  - "[[External Validity]]"
related_theories:
  - "[[Potential Outcomes Framework]]"
related_methods:
  - "[[Experimental Research]]"
  - "[[Matched Pairs Design]]"
  - "[[Random Assignment]]"
  - "[[Causal Modeling]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Propensity Score Matching]]"
  - "[[Covariate Adjustment]]"
  - "[[Non-intervention Research]]"
  - "[[Ex Post Facto Research]]"
  - "[[Difference-in-Differences]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge]]"
  - "[[Argument_Berk_2011_EvalRev]]"
  - "[[Argument_Liu_2023_NHB]]"
confidence: high
status: completed
created: 2026-05-03
updated: 2026-11-02
---

---

> [!def] Matching
> **匹配法（Matching）** 是观察性研究与准实验因果推断中用于消除可观测选择偏误的基础统计方法。其核心逻辑在于：在缺乏人为[[Random Assignment|随机分配]]的情境下，依据个体在接受干预前已具备的多维可观测协[[Variable|变量]]特征，在未受干预的对照候选池中为处理组寻找特征相似的匹配对象，使两组在基线特征分布上达成统计均衡，进而逼近[[Potential Outcomes Framework|潜在结果框架]]下的[[Counterfactual|反事实]]比较([[Argument_Berk_2011_EvalRev|Berk, 2011, pp. 195–198]])。
> 
> 在实验设计中，匹配亦表现为[[Matched Pairs Design|配对设计]]的前置技术，即先在关键变量上完成受试者两两配对，再在配对层级实施随机指派([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch. 16]])。在科学学与政策评估中，精确匹配、粗化精确匹配与倾向得分匹配被广泛用于剥离资助模式与学者声誉等内生混杂特征([[Argument_Liu_2023_NHB|Liu et al., 2023, pp. 341–350]])。

> [!method-scope] 方法范围
> - **研究对象** 大规模教育调查、公共政策试点、科研基金申请记录与学术合作网络中的非实验观测样本。
> - **问题类型** 在无法实施随机实验的前提下，识别干预措施对实际参与者的平均处理效应（ATT）或总体平均处理效应（ATE）。
> - **[[Unit of Analysis|分析单位]]** 学生个体、教师、学校、学者或科研团队。
> - **输出形式** 匹配前后协变量标准化均值差（SMD）平衡检验图表、配对权重矩阵、处理效应点估计值及对未观测偏误的敏感性界限。

> [!citation-card] 匹配作为受实证诊断约束的因果识别进路
> 匹配方法通过协变量平衡逼近条件随机化，其匹配变量的选择必须在不参考结果变量的情况下独立确立；相比依赖不可检验模型假设的传统因果建模，匹配更多受到客观样本平衡性诊断的实证约束。[[Argument_Berk_2011_EvalRev|(Berk, 2011, p. 198)]]
>
> *Matching methods determine the set of matching variables without reference to the response variable. The goal is to achieve sample balance, for which the response variables can be locked in a safe, relying more on empirical diagnostic constraints than on untestable structural assumptions.*

---

> [!method-position] 认识论与方法定位
> - **知识观** 根植于反事实因果推理。假定只要处理分配机制在给定一组可观测前置协变量的条件下独立于潜在产出（条件独立性假定），两组观测产出的差异即可确认为因果效应。
> - **研究者角色** 在隔离结果变量的前提下负责匹配维度的筛选、算法设定与平衡性诊断，杜绝依据处理效应大小反复调配变量的循环论证。
> - **有效性标准** 匹配后样本在各维度的标准化均值差绝对值（SMD $< 0.10$）与方差比接近 1；估计结果对未观测遗漏变量具备充分的统计耐受度。
> - **不声称回答的问题** 匹配仅对纳入模型的命名可观测特征产生平衡，无法自动排除不可测动机、未记录历史冲击或动态时变混杂的干扰。

> [!method-stack] 方法层级
> - **研究设计** [[Quasi-Experimental Designs|准实验设计]]、[[Ex Post Facto Research|事后回溯研究]]、观察性比较研究与实验配对设计。
> - **数据收集** 行政普查记录、追踪问卷、学业基线测验与科研成果发表历史档案。
> - **分析方法** 精确匹配（Exact Matching）、粗化精确匹配（Coarsened Exact Matching, CEM）、[[Propensity Score Matching|倾向得分匹配]]（PSM）与马氏距离匹配。
> - **辅助技术** 共同支撑集核查、卡尺设定、标准化偏差诊断与 Rosenbaum 边界敏感性分析。

---

> [!proc] 观察性匹配分析标准流程
> 1. **协变量挑选与隔离** 提取干预前已固化的基线人口学、历史表现与组织背景特征；严禁参考结果变量，防止中介变量污染。
> 2. **匹配算法选择与配对** 依据变量维度与连续性，选用精确匹配、分箱粗化匹配或概率距离匹配，建立处理与对照样本的一对一或一对多映射。
> 3. **核查样本平衡性与共同支撑集** 计算各协变量匹配前后的标准化均值差，绘制重叠密度图，剔除缺乏对等支撑的极端边缘观测。
> 4. **效应估计与模型协同** 在配对平衡样本上计算平均处理效应；若存在时间序列数据，可进一步结合[[Difference-in-Differences|双重差分法]]消除时间恒定的不可测个体异质性。
> 5. **敏感性分析与稳健性报告** 运用 Rosenbaum Bounds 评估遗漏混杂对结论稳健性的潜在破坏临界点，明确结论的适用边界。

> [!contrast-table] 匹配法 vs 结构方程因果建模（SEM）特征对比
> | 比较维度 | 样本匹配法（Matching） | 结构方程因果建模（[[Causal Modeling|SEM]]） |
> |:---|:---|:---|
> | **变量选择准则** | 匹配变量在完全不参考结果变量的情况下独立确定 | 变量选择往往与因变量回归拟合度深度交织 |
> | **模型假定依赖** | 较少依赖不可检验的函数形式假定，受客观平衡指标约束 | 高度依赖线性因果图、正态分布与误差无关等强假设 |
> | **诊断透明度** | 通过协变量平衡表与重叠分布直接验证，直观清晰 | 依赖整体拟合指数，难以直接观测微观个体间反事实可比性 |
> | **统计推断风险** | 匹配规避了模型搜索带来的推断失真风险 | 复杂的模型调试极易引发严重的事后推断偏差 |

> [!method-stack] 数据与变量
> - **数据结构** 包含明确二值处理指示变量、前置基线协变量矩阵及追踪产出指标的观察截面或面板数据。
> - **样本与单位** 独立受试个体、学术院系或项目资助申请者。
> - **核心假设** 满足条件独立性假定、共同支撑集假定以及[[Stable Unit Treatment Value Assumption|稳定单元处理值假定]]（SUTVA）。

---

> [!method-fit] 适用判断
> - **适合使用** 无法人为实施随机分配但积累了详实微观基线档案的实证研究（如长周期学生行政大数据库或科研学者完整发表轨迹）。[[Argument_Berk_2011_EvalRev|(Berk, 2011, p. 195)]]; [[Argument_Liu_2023_NHB|(Liu et al., 2023, pp. 341–350)]]
> - **谨慎使用** 候选对照池规模有限或处理组与对照组基线特征差异悬殊时，匹配可能引发严重的共同支撑集脱落，导致大量样本被剔除。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15|(Cohen et al., 2011, Ch. 15)]]
> - **不适合使用** 关键选择机制受制于无法观测的隐性动机或瞬时随机偶发因素的情境。

---

> [!method-limits] 方法局限
> - **偏误来源** 匹配仅对已测量的命名变量建立平衡，对遗漏混杂与未观测异质性缺乏天然免疫力，因果有效性弱于真实随机实验。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch. 16, p. 323)]]
> - **样本损耗与外部效度收缩** 严苛的匹配条件可能迫使研究者放弃大量无对应配对的样本（如 Lewis-Beck 案例中有效样本由 1194 例骤降至 46 例），削弱总体代表性。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15|(Cohen et al., 2011, Ch. 15)]]
> - **误用风险** 将匹配平衡后的样本简单等同于随机实验，夸大因果推断结论的绝对确定性。
> - **补救方式** 采用匹配双重差分法（Matching-DID）吸收固定效应，并常规报告 Rosenbaum 边界敏感性分析指标。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Potential Outcomes Framework]] | 理论 | 为匹配方法提供潜在结果与反事实因果推断的形式化数学基石。 |
> | [[Random Assignment]] | 黄金参照 | 随机化在全部已知与未知变量上均达成等价，匹配仅在命名变量上产生平衡。 |
> | [[Propensity Score Matching]] | 子类方法 | 通过概率标量降维解决多维协变量维数灾难的最主流匹配实现进路。 |
> | [[Matched Pairs Design]] | 实验形态 | 匹配在真实验设计中的具体落地形式，先按特征配对再执行组内随机化。 |
> | [[Causal Modeling]] | 对照路径 | 匹配被视作结构方程模型的经验替代方案，更少依赖不可检验的参数结构假设。 |
> | [[Difference-in-Differences]] | 协同方法 | 匹配与双重差分组合构成匹配 DID，在平衡横截面特征的同时消除时不变未观测混杂。 |
> | [[Covariate Adjustment]] | 对照方法 | 回归协变量控制通过模型方程调整混杂，匹配则通过样本重构实现直接平衡。 |
> | [[Non-intervention Research]] | 母类范畴 | 匹配属于非干预观察性研究中改善因果推断可信度的标准策略。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Berk_2011_EvalRev|Berk (2011)]] — 论证匹配法作为因果建模替代方案的认识论优越性，强调匹配变量的选择必须在隔离结果变量的前提下进行，由客观样本诊断约束推断过程。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge|Cohen et al. (2011)]] — 系统梳理实验配对设计与准实验匹配的技术细节，辨析匹配在控制未测变量上弱于随机分配的方法学局限（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Ch. 16]]）；并阐释事后回溯研究中匹配提升可比性的规程，指出严苛配对可能引发有效样本规模的剧烈缩减（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15|Ch. 15]]）。
> - [[Argument_Liu_2023_NHB|Liu et al. (2023)]] — 将精确匹配与倾向得分匹配确立为科学学因果推断的基础进路，评述其在控制学者学术年龄与入选前产出基线、评估高风险科研资助对原始创新因果促进中的实证应用（pp. 341–350）。
