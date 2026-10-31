---
title: Disruption Index
aliases:
  - 颠覆性指数
  - 颠覆度指数
  - 破缺指数
  - CD 指数
  - CD Index
  - Consolidated Disruption Index
summary: "一种用于量化科研成果或发明专利是开拓新方向还是巩固既有范式的文献计量指标；通过测算后继文献在引用焦点成果时是否同时共引其前期参考文献，输出取值在 -1 到 1 之间的指数，从而区分发展型工作与颠覆型工作。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 14
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/indicator
  - theme/science-of-science
  - theme/bibliometrics
related_concepts:
  - "[[Document]]"
  - "[[Paradigm]]"
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
  - "[[Value Neutrality]]"
  - "[[Knowledge Production]]"
  - "[[Comparative Education as a Cross-Sectional Area]]"
related_theories:
  - "[[Technological Trajectories]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Network Analysis]]"
related_instruments: []
related_persons:
  - "[[Lingfei Wu]]"
  - "[[Dashun Wang]]"
  - "[[James A. Evans]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit05]]"
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit11]]"
confidence: high
status: active
created: 2026-10-30
updated: 2026-10-31
---

---

> [!def] Disruption Index
> 颠覆性指数（Disruption Index，记作 $D$ 或 $CD$ 指数）是量化一项学术论著、专利或技术发明在知识网络中具有开拓颠覆性抑或巩固发展性的[[Document|文献]]计量测度指标。该指标输入焦点成果的前向施引网络与后向引文网络，统计仅引用焦点成果（$n_i$）、同时共引焦点成果及其参考文献（$n_j$）以及仅引用其参考文献（$n_k$）的三类文献规模，经归一化差分算式输出 $[-1, 1]$ 区间内的连续数值：数值趋近于 1 表明该成果开启全新问题并遮蔽了前期知识（颠覆型）；数值趋近于 -1 表明该成果巩固并推进了既有研究传统（发展型）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 128–131)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 测度科技成果对既有知识基础的演进导向与[[Paradigm|范式]]转换程度，评估成果是“开辟新方向（颠覆）”还是“深化已有框架（巩固）”。
> - **问题类型** 测度、描述、比较与分类。
> - **[[Unit of Analysis|分析单位]]** 单篇学术论著、发明专利、开源软件代码仓库，亦可聚合为学者个体、科研团队、学术期刊或学科领域的平均颠覆度。
> - **输入数据** 焦点成果的后向引文列表（参考文献）以及引用焦点成果或其参考文献的全部后向施引网络拓扑数据。
> - **输出形式** $[-1, 1]$ 区间内的标准化实数，亦可转换为领域与年代校准后的百分位秩次（Disruption Percentile）。

> [!citation-card] 颠覆与发展之区分
> 科学文献在引用网络中呈现两种截然不同的贡献方式。发展型项目在前期研究基础上推进既有问题的认知，因而往往与前期文献被后人共同引用；颠覆型项目则开辟崭新的探究前沿，呈现出与既往知识传统的决裂，因而后继研究倾向于单独引用该工作而不提及先驱文献。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 129–130)]]
>
> *“Developmental” projects, those that build upon earlier research, seek to advance understanding of an existing problem, hence they tend to be cited along with earlier work... “Disruptive” projects, on the other hand, tend to establish a brand new frontier of inquiry, hence they are more likely to be cited without the predecessors, since they represent a departure from previous knowledge.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 传统被引频次仅反映成果所受关注总量，无法区分技术巩固与[[Paradigm|范式]]更替；颠覆性指数通过引入共引结构捕捉知识流动方向，有效弥补了引文数量指标的结构性盲区。
> - **研究者判断** 需确定施引文献的统计时间窗口（如发表后 5 年或 10 年）、学科引文归一化基准以及对参考文献极少或无引文作品的处理规则。
> - **有效性标准** 在物理学、生物医学、软件工程与专利发明等不同语境中，颠覆性高值成果系统对应于诺贝尔奖原创新概念或改变行业技术路线的开创性专利。
> - **不声称回答的问题** 颠覆性指数不直接等同于科学质量或社会经济价值；高发展型成果同样具备重大价值（例如实验证实重要理论预言的诺奖级成果常表现为高度发展型）。

> [!method-stack] 方法层级
> - **上位方法** [[Bibliometric Analysis|文献计量分析]]、复杂网络引文[[Network Analysis|网络分析]]。
> - **前置步骤** 成果参考文献消歧与引文网络图谱构建。
> - **变体与扩展** CD5 指数（发表后 5 年窗口）、去除自引后的修正颠覆度、按期刊与年代加权的相对颠覆百分位。

> [!dev-timeline] 方法演变
> - **2017 — 基础定义提出** Russell J. Funk 与 Jason Owen-Smith 在创新研究中首次形式化 CD 指数算法，用于评估医学发明专利的[[Technological Trajectories|技术轨道]]路线变革。
> - **2019 — 大数据扩展与规律发现** [[Lingfei Wu|吴令飞]]、[[Dashun Wang|王大顺]]与[[James A. Evans|詹姆斯·埃文斯]]（Wu, Wang, & Evans, 2019）将该指标推广至 6,000 万篇论著、专利与软件项目，揭示小团队倾向于颠覆科学而大团队倾向于发展科学的组织规模分化规律。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 128–132)]]
> - **2021 — 多维影响力度量体系整合** 王大顺与巴拉巴西在《科学学》中将颠覆性指数确立为深挖引文网络拓扑结构、超越狭隘引文计数的关键方法，与替代计量学和产业专利转化共同构成多维评价体系。[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|(Wang & Barabási, 2021, pp. 245–248)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["提取焦点成果引文网络<br>（焦点篇 p，参考文献集 R_p）"] --> B["分类统计后继施引文献<br>n_i：独引 p<br>n_j：共引 p 与 R_p<br>n_k：独引 R_p 忽略 p"]
>   B --> C["代入归一化差分算式<br>D = (n_i - n_j) / (n_i + n_j + n_k)"]
>   C --> D["输出 D 值 [-1, 1]<br>判别颠覆性或发展性"]
> ```

> [!formula-step] 步骤一　归一化引文差分计算
> $$D_p = \frac{n_i - n_j}{n_i + n_j + n_k}$$
>
> **这个公式在做什么** 输入焦点文献及其参考文献的后向引文拓扑，统计三类施引文献数量，输出 $[-1, 1]$ 区间内的颠覆性指数。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 129–130)]]
>
> **符号说明** $n_i$ 为仅引用焦点文献的成果数；$n_j$ 为同时共引焦点文献与其参考文献的成果数；$n_k$ 为仅引用其参考文献而未引焦点文献的成果数。
>
> **数学直觉** 公式通过独引与共引的差分比率衡量注意力转移：后继研究若绕过前期文献而单引焦点工作，表明焦点工作颠覆了前人；后继研究若持续共引前期文献，表明焦点工作是在前人框架内的累积推进；$n_k$ 充当分母控制相关领域的总体学术活跃度规模。
>
> > [!example]- 手算示例
> > 假设施引网络中，仅引用焦点成果的篇数 $n_i = 80$，同时共引焦点成果与参考文献的篇数 $n_j = 20$，仅引用参考文献的篇数 $n_k = 100$。代入算式：
> > $$D = \frac{80 - 20}{80 + 20 + 100} = \frac{60}{200} = 0.30$$
> > 所得 $D = 0.30 > 0$，表明该成果偏向颠覆型工作。
>
> > [!geogebra] 动态参数模拟
> > - **左侧三条滑块** 分别控制 $n_i$（绿，独引焦点篇）、$n_j$（橙，共引焦点与参考篇）、$n_k$（灰，独引参考篇），取值范围均为 $0$–$100$。
> > - **D 值刻度轴** （$[-1, 1]$）：拖动滑块后，绿色正向段与橙色负向段实时延伸，黑色指针锁定当前 $D$ 值位置。
> > - **动态文字输出** 实时显示 $D$ 的数值及类型判定（高颠覆型 / 轻度颠覆型 / 均势 / 轻度发展型 / 高发展型）。
> > - **右侧引用拓扑图** 固定展示焦点篇 $F$（蓝色）、参考文献节点 $R_{1-3}$（深灰）以及三类施引文献节点（绿色 $n_i$、橙色 $n_j$、灰色 $n_k$）的拓扑示意。
> > - **参考基准** 模拟器预载经典案例默认值（$n_i = 80, n_j = 20, n_k = 100$，$D = 0.30$）；可手动输入 BTW 模型近似参数验证 $D \approx 0.86$。
> >
> > ![[wiki/assets/geogebra/disruption_index.ggb]]
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 正值倾向 | $D > 0$（趋近 1）表明成果开辟新方向，后继研究倾向于绕过先驱文献直接引用该工作。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05\|(Wang & Barabási, 2021, p. 129)]] |
> > | 读法 | 负值倾向 | $D < 0$（趋近 -1）表明成果巩固既有范式，后继研究倾向于将其与先驱文献共同引用。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05\|(Wang & Barabási, 2021, p. 129)]] |
> > | 读法 | 零值均势 | $D = 0$（或 $n_i = n_j$）表明成果在颠覆开拓与累积巩固之间达成均势。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05\|(Wang & Barabási, 2021, p. 130)]] |
> > | 注意 | [[Value Neutrality\|价值中立]] | 指数仅区分工作类型而非科学质量的高低，实验验证理论的重大突破常表现为高度负值。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05\|(Wang & Barabási, 2021, p. 130)]] |
> > | 注意 | 时滞效应 | 原创新概念常经历较长的承认延迟，短期引文窗口内的 $D$ 值波动较大。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05\|(Wang & Barabási, 2021, p. 131)]] |

---

> [!contrast-table] 颠覆型成果与发展型成果特征对比
> | 维度 | 颠覆型成果（$D \to 1$） | 发展型成果（$D \to -1$） |
> |:---|:---|:---|
> | **典型代表案例** | Bak 等关于自组织临界性的 BTW 模型（$D = 0.86$） | Davis 等关于玻色－爱因斯坦凝聚态的实验观测（$D = -0.58$） |
> | **后继引用模式** | 后人只引用该成果本身，不再提及该成果所引的前辈成果 | 后人几乎始终将该成果与其引用的前期先驱著述一并共引 |
> | **[[Knowledge Production\|知识生产]]功能** | 开辟全新探究疆域，提出非常规假说与问题 | 攻克既有公认科学难题，推进精细化设计与测量 |
> | **引文时滞特征** | 短期内引文积累缓慢，但半衰期长，具备持久远期影响 | 发表后迅速获得同领域密集引用，但生命周期衰减较快 |
> | **典型生产团队** | 独立研究者或 2–4 人的敏捷小团队 | 跨学科、大规模甚至成百上千人的大科研团队 |

---

> [!method-fit] 适用判断
> - **适合使用** 科技创新政策评估、科研资助资助组合优化、学科范式演化计量、团队规模与结构绩效比较。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 128–132)]]
> - **谨慎使用** 新兴[[Comparative Education as a Cross-Sectional Area|交叉学科]]或小众冷门领域，由于施引文献基数过小（分母接近 0），$D$ 值波动极易受单篇偶然引用的干扰。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, p. 130)]]
> - **不适合使用** 不适合用于直接替代科研质量同行评议，亦不适合在未做年代与学科基准校准的情况下跨学科直接比对绝对数值。

---

> [!method-limits] 方法局限
> - **偏误来源** 现代学术成果参考文献列表平均篇幅持续膨胀，客观上推高了偶然共引的发生概率，导致各领域原始 $D$ 值随年份出现机械下移漂移。
> - **适用边界** 严重依赖完整透明的引文索引网络，无法有效测度书籍、非公开发表报告或引文网络稀疏的人文学科成果。
> - **误用风险** 将 $D$ 指数简单等同于成果学术水平或资助优先权，诱发对发展型重要工作的忽视或引发研究者刻意操纵参考文献规避共引。
> - **补救方式** 采用年代与期刊领域百分位标准化（Disruption Percentile）消除时间通胀；去除自引网络；延长引文统计时间窗至 5–10 年。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Technological Trajectories]] | 理论 | 技术轨道理论为颠覆型开辟与发展型深化提供技术演进理论支撑。 |
> | [[Bibliometric Analysis]] | 上位方法 | 文献计量分析为颠覆性指数提供底层数据结构与引文分析基础。 |
> | [[Network Analysis]] | 前置方法 | 复杂网络分析为引文拓扑构建与节点度量提供算法支持。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge|Wang and Barabási (2021)]] — 运用颠覆性指数证实小团队颠覆既有范式、大团队发展成熟传统的组织分工规律（[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|Unit 05]]，pp. 128–132）；并将其确立为深挖网络拓扑、超越引文计数的关键指标（[[Argument_Wang_Barabasi_2021_Cambridge_Unit11|Unit 11]]，pp. 245–248）。
