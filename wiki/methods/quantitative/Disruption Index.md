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
method_related_count: 9
method_related_level: 0
method_related_stars: "☆"
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
  - "[[Unit of Analysis]]"
  - "[[Construct Validity]]"
  - "[[Paradigm]]"
  - "[[Knowledge Production]]"
related_theories:
  - "[[Technological Trajectories]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Network Analysis]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
related_facts: []
related_arguments: []
confidence: high
status: active
created: "2026-10-30"
updated: 2026-10-30
---

---

> [!def] Disruption Index
> 颠覆性指数（Disruption Index，记作 $D$ 或 $CD$ 指数）是量化一项学术论著、专利或技术发明在知识网络中具有开拓颠覆性抑或巩固发展性的[[Document|文献]]计量测度指标。该指标输入焦点成果的前向施引文献网络与后向参考文献网络，统计仅引用焦点成果、同时共引焦点成果及其参考文献、以及仅引用其参考文献的三类文献规模，经归一化算式输出 $[-1, 1]$ 区间内的连续数值：数值趋近于 1 表明该工作完全遮蔽了前期文献并开启全新研究脉络（颠覆型）；数值趋近于 -1 表明该工作作为桥梁深化并巩固了既有知识传统（发展型）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 128–131)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 测度科技成果对既有知识基础的演进导向，即评估成果是“开辟新问题（颠覆）”还是“解决已有问题（巩固）”。
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
> - **上位方法** [[Bibliometric Analysis|文献计量学]]分析、复杂网络引文[[Network Analysis|网络分析]]。
> - **前置步骤** 论文参考文献消歧与引文网络图谱构建。
> - **变体与扩展** CD5 指数（发表后 5 年窗口）、去除自引后的修正颠覆度、按期刊与年代加权的相对颠覆百分位。

> [!dev-timeline] 方法演变
> - **2017 — 基础定义提出** Russell J. Funk 与 Jason Owen-Smith 在管理学与创新研究中首次形式化 CD 指数算法，用于评估医学发明专利的[[Technological Trajectories|技术轨道]]路线变革。
> - **2019 — 大数据扩展与规律发现** 吴令飞、[[Dashun Wang|王大顺]]与詹姆斯·埃文斯（Lingfei Wu, Dashun Wang, & James A. Evans）将该指标推广至 6,000 万篇论著、专利与软件项目，揭示小团队倾向于颠覆科学而大团队倾向于发展科学的组织规模分化规律。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 128–132)]]

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["提取焦点成果引文网络<br>（焦点篇 i，参考文献集 Ref）"] --> B["分类统计后继施引文献<br>n_i：独引 i<br>n_j：共引 i 与 Ref<br>n_k：独引 Ref 忽略 i"]
>   B --> C["代入归一化差分算式<br>D = (n_i - n_j) / (n_i + n_j + n_k)"]
>   C --> D["输出 D 值 [-1, 1]<br>判别颠覆性或发展性"]
> ```

> [!formula-step] 核心计算步骤与形式化公式
> 设给定焦点文献 $p$ 引用了参考文献集合 $R_p$。考察在 $p$ 发表之后引用了 $p$ 或引用了 $R_p$ 中至少一篇文献的后继作品集合，将其划分为三个互斥类别：
> 1. $I$ 类文献（规模为 $n_i$）：仅引用焦点文献 $p$，而未引用 $R_p$ 中任何文献；
> 2. $J$ 类文献（规模为 $n_j$）：同时引用了焦点文献 $p$ 以及 $R_p$ 中的至少一篇参考文献；
> 3. $K$ 类文献（规模为 $n_k$）：仅引用了 $R_p$ 中的文献，而完全未引用焦点文献 $p$。
> 
> 颠覆性指数 $D_p$ 定义为：
> $$D_p = \frac{n_i - n_j}{n_i + n_j + n_k}$$
> 
> 参数含义与几何意义：
> - 当 $n_j = 0$ 且 $n_k = 0$ 时，$D = 1$，表明所有后继研究均绕过前期文献而直接立足于该成果，代表绝对范式颠覆；
> - 当 $n_i = 0$ 且 $n_k = 0$ 时，$D = -1$，表明所有后继文献均将焦点工作与前期文献捆绑共引，代表典型累积巩固；
> - 当 $n_i = n_j$ 时，$D = 0$，表明成果在颠覆与发展之间达成均势。

---

> [!contrast-table] 颠覆型成果与发展型成果特征对比
> | 维度 | 颠覆型成果（$D \to 1$） | 发展型成果（$D \to -1$） |
> |:---|:---|:---|
> | **典型代表案例** | Bak 等关于自组织临界性的 BTW 模型（$D = 0.86$） | Davis 等关于玻色－爱因斯坦凝聚态的实验观测（$D = -0.58$） |
> | **后继引用模式** | 后人只引用该文本身，不再提及该文所引的前辈成果 | 后人几乎始终将该文与其引用的前期理论文献一并共引 |
> | **[[Knowledge Production\|知识生产]]功能** | 开辟全新探究疆域，提出非常规假说与问题 | 攻克既有公认科学难题，推进精细化设计与测量 |
> | **引文时滞特征** | 短期内引文积累缓慢，但半衰期长，具备持久远期影响 | 发表后迅速获得同领域密集引用，但生命周期衰减较快 |
> | **典型生产团队** | 独立研究者或 2–4 人的敏捷小团队 | 跨学科、大规模甚至成百上千人的大科研团队 |

---

> [!method-fit] 适用场景与局限
> - **适用场景** 科技创新政策评估、科研资助资助组合优化、学科范式演化计量、团队规模与结构绩效比较。
> - **主要局限**
>   1. **引文延迟效应** 新颖颠覆性成果常因超出当时同行认知而经历漫长的“睡美人”延迟承认阶段，短期计算的 $D$ 值波动较大；
>   2. **参考文献膨胀干扰** 现代学术论文参考文献列表平均长度大幅扩张，客观上增加了后继文献与焦点文献发生偶然共引的数学概率，导致近年来整体成果的原始 $D$ 均值发生系统性机械漂移。

---

## 使用此方法的研究

- [[Argument_Wang_Barabasi_2021_Cambridge_Unit05|Wang & Barabási (2021, pp. 128–132)]]：分析 1954 至 2014 年间全球 6,000 万篇期刊论文、专利与软件代码仓库，运用颠覆性指数证实团队规模与成果颠覆性呈现高度稳健的单调递减关系（团队规模从 1 增至 50 人，论文颠覆度百分位下降 70 个百分位），揭示小团队颠覆科学、大团队发展科学的本质分工。
- Wu, Wang, & Evans (2019)：在 *Nature* 发表封面论文，依托颠覆性指数全面测度跨领域科研团队组织规模对科技突破模式的决定性作用。
