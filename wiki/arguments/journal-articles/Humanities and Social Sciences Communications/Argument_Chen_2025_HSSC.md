---
summary: "基于微软学术图谱 21,271 位经济学家的长周期生涯数据，结合折损累积增益算法（DCG）测度爆发期前后与内部的颠覆度差异，发现学者学术爆发期内的成果颠覆度显著高于其他时期；最具颠覆性成果的出现时机服从随机规律，且颠覆度峰值平均领先引文影响力峰值数年；更高的发文量能显著提高进入爆发期并产出颠覆性成果的概率。"
type: argument
authors:
  - "Chen, H."
  - "Bornmann, L."
  - "Bu, Y."
source_language: en
citation: "Chen, H., Bornmann, L., & Bu, Y. (2025). Hot streaks and disruptiveness in the career of scientists: is there an association between both phenomena? Humanities and Social Sciences Communications, 12, Article 1424. https://doi.org/10.1057/s41599-025-05701-2"
year: 2025
doi: "10.1057/s41599-025-05701-2"
citation_aliases:
  - "Chen et al., 2025"
  - "Chen et al. (2025)"
isbn: ""
tags:
  - theme/science-of-science
  - theme/scientific-career
  - theme/scientometrics
  - method/quantitative
related_concepts:
  - "[[Hot Streak]]"
  - "[[Scientific Productivity]]"
  - "[[Variable]]"
  - "[[Construct]]"
  - "[[Paradigm]]"
  - "[[Sleeping Beauty in Science]]"
related_theories:
  - "[[Constant-Probability-of-Success Model]]"
  - "[[Random Impact Rule]]"
related_methods:
  - "[[Disruption Index]]"
related_instruments: []
related_persons:
  - "[[Dean Keith Simonton]]"
  - "[[Lu Liu]]"
  - "[[Dashun Wang]]"
related_facts: []
related_arguments: []
sources:
  - "[[sources/Chen_2025_HSSC/Chen_2025_HSSC|Chen_2025_HSSC]]"
part_of:
status: draft
created: 2026-11-03
updated: 2026-11-03
subtype: journal-article
publication_type: journal-article
title: "Argument_Chen_2025_HSSC"
argument_key: "Argument_Chen_2025_HSSC"
argument_display_title: "Hot streaks and disruptiveness in the career of scientists: is there an association between both phenomena? Humanities and Social Sciences Communications, 12, Article 1424"
argument_kind: "journal-article"
argument_related_count: 12
argument_related_level: 1
argument_related_stars: "⭐"
argument_related_color: "#dbeafe"
journal: "Humanities and Social Sciences Communications"
book_title: ""
publication_place: ""
publisher: ""
issuing_organization: ""
---

---

> [!question]
> 科研人员在其学术生涯中产出的成果具有异质性，既有颠覆既有知识基础的开创性工作，也有巩固已有传统的渐进性工作，还有潜在价值滞后显现的[[Sleeping Beauty in Science|睡美人文献]]。既往科学学研究多聚焦于单篇成果层面的引文影响力与颠覆度关联，尚未解答学者生涯中的高影响力时期（即[[Hot Streak|学术爆发期]]）是否与成果的高颠覆度存在系统性关联。本研究旨在回答：学者在爆发期内发表的论著是否比生涯其他阶段展现出更高的颠覆度；颠覆性产出的发生时序是否与爆发期一样遵循随机规律；学者最具颠覆性成果与最高被引成果在生涯时序上如何演进；以及发文数量与合著团队特征如何调节爆发期内外的颠覆度变化。

> [!claim] 核心主张
> 学者在[[Hot Streak|学术爆发期]]内产出成果的颠覆度显著高于爆发期之前与之后的生涯阶段；顶尖颠覆性成果在学术生涯中的涌现服从[[Random Impact Rule|随机分布规律]]，但个体颠覆度峰值年份系统性领先于最高被引年份；更高的[[Scientific Productivity|科研生产力]]（发文量）能够显著提高进入爆发期并产生颠覆性成果的概率，而爆发期内单纯累积高被引成果反而伴随更低的颠覆度增量。

> [!concept-lens] 阅读透镜
> - **对象** 微软学术图谱（Microsoft Academic Graph, MAG）中 21,271 位拥有 20 年以上研究生涯、发表论著不少于 15 篇的经济学学者全生命周期产出记录，兼顾计算机科学、地质学与生物学领域的对照验证。
> - **张力** 直觉上学者最具影响力的代表作往往被视同为最具颠覆性的成果，然而经验文献显示高引成果常偏向巩固既有范式的发展型研究；本研究检验高被引聚集的爆发期究竟是强化了[[Paradigm|范式]]颠覆，还是仅仅表现为常规科学的规模扩张。
> - **贡献** 首次在学者长周期生涯尺度上证实高引爆发期伴随更高的颠覆性；揭示颠覆峰值早于引文峰值的时序错位规律；通过折损累积增益算法（Discounted Cumulative Gain, DCG）有效解决了学者多篇成果颠覆度聚合测度的技术瓶颈，为优化中青年科技人才资助节奏提供了实证证据。

---

> [!framework-table] 理论工具箱
> | 理论工具 | 解释功能 |
> |----------|----------|
> | **学术爆发期理论**<br>[[Hot Streak]] | 界定创造性职业生涯中表现显著优于个人历史基线的暂时性卓越时期，为划分学者生涯阶段（爆发期前、爆发期内、爆发期后）提供分析框架。 |
> | **机会构型理论 / 成功恒定概率模型**<br>[[Constant-Probability-of-Success Model]] | [[Dean Keith Simonton|迪恩·凯斯·西蒙顿]]（Dean Keith Simonton）提出的创造力认知模型，指出重大突破源于海量随机尝试中的机遇配置；本研究以此解释颠覆性产出的时序随机性及发文规模对进入爆发期的正向预测作用。 |
> | **随机影响规律**<br>[[Random Impact Rule]] | 表明重大代表作在学者全生涯发表时序中均匀随机出现，本研究检验颠覆性极值成果是否同样契合该统计无偏基准。 |
> | **科学革命与常规科学理论**<br>[[Paradigm]] | 托马斯·库恩（Thomas S. Kuhn）关于常规科学解谜与科学革命范式更替的理论，为颠覆型研究（开启新方向）与巩固型研究（深化旧传统）提供认识论区隔。 |

> [!warrant]- 理论如何支撑论证
> 库恩的范式理论将科学成果区分为开辟新路径的革命性工作与巩固旧框架的常规工作，[[Disruption Index|颠覆性指数]]从引文拓扑结构上将这一区隔操作化。西蒙顿的机会构型理论与成功恒定概率模型假定重大创新的涌现依赖持续尝试与盲目变异，由此推导出提高探索总量有助于触碰突破边界。研究者通过结合学术爆发期理论与机会构型假说，将颠覆度测度置于学者生命周期演化视角下，构建了“发文尝试驱动机遇获取—爆发期迎来颠覆突破—后继工作走向常规巩固与引文扩散”的解释链条。

### 核心变量与操作化编码表（仅量化研究填写）

> [!index-table] 核心变量操作化定义与编码规程
> | [[Variable\|变量]]维度与分类 | [[Construct\|理论构念]]与操作化定义 | 核心教学规程、典型测量工具与纳入案例 |
> |---|---|---|
> | **颠覆度差异（因变量）**<br>（D_diff） | 学者在爆发期内的学术颠覆度相对爆发期之前的净增量，表征爆发期激发的创造性范式转换强度。 | 采用折损累积增益算法分别计算爆发期内与爆发期前 2 年窗口的成果颠覆度总分：$D_{diff} = DCG(D_{during}) - DCG(D_{before})$。主模型基于去除自引与噪声的 $D_5$ 指数，稳健性检验采用无参考分母的 $D_{noR}^5$、百分位排序颠覆度以及求和加总法。 |
> | **爆发期时空特征（自变量）**<br>（length_hot, start_hot_period, start_year_hot） | 学者经历学术爆发期的持续时长与在生涯序列中开启的时间节点。 | `length_hot` 为爆发期持续年数（样本均值 3.67 年）；`start_hot_period` 为从学者首次发表到爆发期起始之间的年份跨度（样本均值 13.09 年）；`start_year_hot` 为爆发期起始年份相对学者平均生涯跨度的相对偏移量。 |
> | **科研产出与生产力（自变量）**<br>（#pub_before, #pub_during, cits_num_*, D_num_*） | 学者在各阶段的发文总量、获得引用的文献数以及具有正向颠覆度成果的规模。 | `#pub_before` 与 `#pub_during` 分别记录对应时期的发文总数；`cits_num_before` 与 `cits_num_during` 为获得至少 1 次引用的论著数量；`D_num_before` 与 `D_num_during` 为颠覆度大于 0 的论著数量。 |
> | **团队协作规模（控制变量）**<br>（team_size_before, team_size_during） | 学者在爆发期前后发表成果的平均署名规模。 | 计算对应时期内单篇论著合作人数的算术平均值，控制大团队倾向于巩固、小团队倾向于颠覆对个体成果指标的影响。 |
>
> **图表解读** 本表系统界定了回归分析中的因变量、核心预测变量与控制变量。通过将引文网络衍生的单篇颠覆度通过 DCG 聚合为学者阶段指标，研究者量化了爆发期对学者创造性产出的动态影响。

---

> [!method-panel] 研究设计
> | 模块 | 材料与处理方式 |
> |------|----------------|
> | **全量引文网络清洗**<br>Bibliometric Network Filtering | 基于微软学术图谱提取学者成果的自引网络与施引拓扑，设定 $I = 5$ 阈值（即施引文献必须引用焦点成果参考文献中至少 5 篇先驱成果才计入共引集合 $N_B^5$），有效剔除引文膨胀与偶然共引噪声，生成 $D_5$ 与 $D_{noR}^5$ 指标。 |
> | **阶段产出聚合算法**<br>Discounted Cumulative Gain (DCG) | 借鉴信息检索领域的折损累积增益算法，按成果颠覆度或被引频次降序排列后施加对数位置折损权重：$DCG(D) = \sum_{i=1}^{p'} \frac{D_i}{\log_2(i+1)}$。克服算术平均数受大量低值成果稀释、直接求和偏袒单纯堆砌边缘成果的缺陷，突显顶尖成果的权重。 |
> | **时序配对与计量回归**<br>Fixed-Effects Regression Analysis | 以爆发期前 2 年作为基准窗口，运用配对样本 t 检验比较爆发期前、中、后的 DCG 颠覆度分布差异；进而构建包含领域固定效应的多变量回归模型，识别爆发期长度、起始时机、产出规模与团队结构对颠覆度增量的影响机制。 |

> [!sample-panel]- 样本与材料快照
> | 样本层面 | 构成 |
> |----------|------|
> | **文本样本** | 微软学术图谱（MAG）中 1800 至 2019 年间的跨学科文献库，主分析纳入 241,158 篇被引不少于 5 次且参考文献不少于 5 篇的经济学学术论著。 |
> | **学者样本** | 21,271 位生涯年限不低于 20 年、发文量不低于 15 篇的成熟经济学家。主回归排除爆发期与职业生涯起点（6.4%）或终点（3.1%）重叠而缺乏 2 年前置窗口的学者，最终进入计量回归的分析样本为 19,152 位学者。 |
> | **跨学科对照** | 补充纳入计算机科学、地质学与生物学三个学科的科研人员数据，用于检验经济学主要发现的跨领域稳健性与外部有效性。 |

---

> [!logic-map]- 核心论证逻辑链
> ```mermaid
> flowchart LR
>     A["研究问题：学术爆发期是否伴随成果颠覆度的提升？"] --> B["方法建构：引入 D5 指数与 DCG 阶段折损加总算法"]
>     B --> C["实证发现一：爆发期内 DCG 颠覆度显著超越爆发期前与后"]
>     B --> D["实证发现二：颠覆极值时序服从随机规律，但峰值年份领先引文峰值"]
>     B --> E["实证发现三：发文规模正向预测爆发期进入与颠覆度提升"]
>     C & D & E --> F["政策推论：科研资助应加大对中年探索期学者的容错支持"]
> ```

---

> [!claim|step] 论证步骤一　学者在学术爆发期内的成果颠覆度显著超越生涯其他时期
> 学者在经历学术爆发期期间，其发表论著的整体颠覆度显著提高，突破了高引爆发期仅代表常规科学数量扩张的传统质疑。

> [!sub-claim] 1. 爆发期内的 DCG 颠覆度系统性高于爆发期前与爆发期后
> 采用配对样本 t 检验对 19,152 位经济学家的生涯数据进行测算表明，学者在爆发期内的 DCG 颠覆度显著高于爆发期前 2 年窗口及爆发期后 2 年窗口（$p < .001$）。而在爆发期之前与爆发期之后的两个非爆发期阶段之间，成果颠覆度不存在统计学显著差异。这表明学术爆发期是学者全生命周期中兼具高学术关注度与高知识开创性的非平稳激发窗口。

> [!figure]- 图5：爆发期前后与爆发期内 DCG 颠覆度分布对比
> ![](https://img.mylikemie.icu/sources/Chen_2025_HSSC/figures/Chen_2025_HSSC_Fig5_DCG_Disruption_Comparison.jpg)

> [!sub-claim] 2. 爆发期持续时长与颠覆度增量呈现稳健正向关联
> 样本中学者的爆发期平均持续时长为 3.67 年（标准差 3.33 年），主要集中在 1 至 7 年区间。回归分析表明，爆发期持续时间（`length_hot`）对颠覆度增量（$D_{diff}$）具有高度统计显著的正向促进作用（在 $D_{noR}^5$ 模型中，$\beta = 0.227, p < .001$；在百分位模型中，$\beta = 18.428, p < .001$）。较长的爆发期为学者深化探索并拓展前沿问题提供了充裕的时间窗口，促使其产出颠覆性更强的代表作。

---

> [!claim|step] 论证步骤二　顶尖颠覆性产出在时序上展现出随机性规律，且颠覆度峰值年份系统性先于引文峰值年份
> 学者产出最具颠覆性成果的时间节点服从跨生涯时序的随机分布，然而颠覆度的黄金探索窗口在学术年龄上明显早于其引文影响力的巅峰时期。

> [!sub-claim] 1. 颠覆性作品的出现时机支持机会构型理论的随机规律
> 分析显示，学者爆发期的起始时间（`start_hot_period`）平均处于入行后第 13.09 年（标准差 8.34 年），跨度从第 1 年延续至第 82 年。检验爆发期起始占比（`start_time_hot`）和结束占比（`end_time_hot`）与颠覆度增量的关系未发现统计学显著规律。这一实证证据表明，颠覆性突破在全生涯时序上的降临并不依附于特定生理年龄，支持了[[Constant-Probability-of-Success Model|成功恒定概率模型]]与[[Random Impact Rule|随机影响规律]]在颠覆性研究中的适用性。

> [!figure]- 图6：学者前 i 篇最具颠覆性成果与最高被引成果出现的平均学术生涯年份
> ![](https://img.mylikemie.icu/sources/Chen_2025_HSSC/figures/Chen_2025_HSSC_Fig6_Disruptive_vs_Cited_Years.jpg)

> [!sub-claim] 2. 学者顶尖颠覆作发表年份平均领先最高被引作发表年份数年
> 追踪学者生涯中前 $i$ 篇最具颠覆性成果与前 $i$ 篇最高被引成果的发表年份发现，学者颠覆度最高的年份普遍集中在入行后第 14 至 16 年之间；而其最高被引成果发表的年份则滞后出现于更成熟的学术阶段。科研人员往往在职业生涯中早期通过开辟新假说与新路径实现认知突破，随后随着学术界对新范式的接纳吸收与跟进拓展，相关工作才逐步迎来大规模引文爆发。

---

> [!claim|step] 论证步骤三　发文规模正向驱动爆发期进入概率与颠覆度提升，但高被引产出对总体颠覆度产生竞争性负向抑制
> 产出总量的扩张是科研人员触碰颠覆性创新边界的关键路径，然而在爆发期内部过度追求高引成果反而与高颠覆度产出形成替代关系。

> [!sub-claim] 1. 爆发期内的发文生产力显著提升颠覆度净增量
> 计量模型显示，学者在爆发期内的发文总量（`#pub_during`）对颠覆度增量具有高度显著的正向影响（在模型 4 中，$\beta = 0.029, p < .001$；模型 3 中，$\beta = 2.026, p < .001$）。高产出为学者提供了更广泛的概念重组与试验空间，印证了西蒙顿关于创造性杰作依托海量试错规模的达尔文主义变异机制。

> [!sub-claim] 2. 高被引论著规模对总体颠覆度增长施加负向影响
> 回归结果表明，爆发期内获得引用的论著数量（`cits_num_during`）对颠覆度增量呈现出负向系数（模型 4 中，$\beta = -0.126, p < .001$；模型 2 中，$\beta = -0.008, p < .001$）。高引论著往往致力于解决既有范式内部公认的重要难题，后人倾向于将其与先驱文献共同引用以确立渊源，因而在算法上表现为发展型而非颠覆型。这一发现揭示了文献被引规模与引文颠覆度之间存在的内在张力。

---

> [!finding-cards] 核心发现
> 1. **爆发期颠覆度显著更高** 经济学家在学术爆发期内的成果颠覆度显著超越爆发期前与爆发期后，证实学术爆发期兼具质量卓越与范式革新特征。
> 2. **颠覆峰值早于引文峰值** 学者最具颠覆性成果的发表时机集中于入行后 14 至 16 年的中前期，系统性早于其职业生涯中引文累积达到极值的时期。
> 3. **发文规模驱动创新边界** 爆发期内发文数量的提升显著正向预测颠覆度增量，支持通过高频探索与概念试错促成重大范式突破的机制。
> 4. **高引成果对颠覆度的抑制效应** 爆发期内被引成果数量的增多对整体颠覆度增量产生负向影响，印证了高引累积与知识颠覆在引文网络拓扑结构上的功能分化。

> [!stat-cards]- 核心数据
> - **21,271 位** 纳入全样本追踪的资深经济学家总数。
> - **19,152 位** 满足前后 2 年窗口对比要求并纳入计量回归分析的学者样本规模。
> - **3.67 年** 样本中学者学术爆发期的平均持续时长（标准差 3.33 年）。
> - **13.09 年** 学者从入行到迎来首个学术爆发期的平均时间跨度（标准差 8.34 年）。
> - **14–16 年** 学者发表前若干篇顶尖颠覆性论著的平均职业学术年龄。
> - **0.03** 学者在爆发期内相比爆发期前的 DCG 颠覆度净增量均值（标准差 0.08）。

---

> [!citation-card] 资助机构应当优化对中年探索期科研人员的容错资助
> 颠覆性产出（生涯中前期）与引文认可（生涯中后期）之间的时序脱节表明，科技资助机构应当在不同生涯阶段持续维持高容错度的探索性资助，而非将资源过度集中于初入行青年学者或晚期成熟团队。处于入行 14 至 16 年的中年学者正迎来其最具颠覆性的阶段，为其提供灵活的资助机制有助于激发重大的开拓性发现。此外，发文生产力与颠覆度之间的正向联系进一步强化了资助计划应当包容探索试错、鼓励科研人员积极推进发表的政策价值。
>
> *First, the temporal gap between disruptive output (early-mid career) and citation recognition (mid-late career) suggests that funding agencies could optimize support by sustaining risk-tolerant grants across career stages rather than concentrating resources on early-career researchers. For example, mid-career scientists—who our analysis shows are often entering their most disruptive phases—may benefit from flexible funding schemes that allow them to build on exploratory work initiated earlier... Second, the link between productivity and disruptiveness underscores the value of funding programs that support prolific output and iterative experimentation without penalizing incremental or failed explorations.*

---

> [!warning] 自述局限
> - **数据库收录范围限制** 研究主要依赖微软学术图谱，对未被完全索引的书籍、工作底稿（Working Papers）或小众期刊论著可能存在覆盖不全问题。
> - **学科特异性与泛化边界** 主样本聚焦于经济学领域（成果署名普遍按姓氏字母排序且团队规模相对较小），尽管在计算机科学、地质学与生物学中得到了相似的结论，但在数千人跨国协作的大科学物理实验等领域的适用性仍需谨慎检验。
> - **聚合算法参数敏感性** DCG 聚合算法引入了对数衰减权重，虽然克服了均值与求和法的缺陷，但权重的阶梯设定对特定极端成果的敏感度仍依赖规范判断。
> - **颠覆性指标本身的结构演化** 现代科技文献参考文献列表整体膨胀，可能对跨年代的原始颠覆度产生系统性挤压漂移。

---

## 来源

- [[sources/Chen_2025_HSSC/Chen_2025_HSSC|Chen_2025_HSSC]]
