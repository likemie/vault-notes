---
title: Literature-Based Discovery
aliases:
  - 基于文献的发现
  - LBD
  - Swanson Hypothesis
  - 斯旺森假说
  - Undiscovered Public Knowledge
  - 未被发现的公开知识
summary: "通过计算文本挖掘、共现网络与语义关联算法从互不相通的独立文献语料库中挖掘隐含科学联系的假设生成方法；以唐·斯旺森提出的 ABC 推理模型为基石，通过中间实体桥接促成潜在新假设的生成，曾成功预测鱼油缓解雷诺氏综合征以及镁缺乏与偏头痛的生理关联。"
type: method
method_type: mixed
method_family: "mixed"
method_related_count: 0
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#fef3c7"
cssclasses:
  - method-manual
tags:
  - method/mixed
  - method/discovery
  - theme/science-of-science
  - theme/scientometrics
  - theme/artificial-intelligence
confidence: high
status: active
created: "2026-10-31"
updated: 2026-10-31
---

---

> [!def] Literature-Based Discovery
> 基于文献的发现（Literature-Based Discovery, LBD）指利用计算语言学、实体抽取与网络分析技术，在相互分割、缺乏直接互引的独立文献集合之间，自动化挖掘潜在逻辑关联与新科学假说的研究方法。其理论基础为唐·斯旺森（Don Swanson）提出的“未被发现的公开知识”（Undiscovered Public Knowledge）原理与 ABC 模型：假定文献集甲探讨了概念 A 与概念 B 的关联，文献集乙探讨了概念 B 与概念 C 的关联，若两个文献群从未产生直接交集，则概念 A 与概念 C 之间蕴含极具价值且待实证检验的新科研假说。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 227)]]

> [!method-scope] 方法范围
> - **研究对象** 大规模学术文献全文本或摘要集合中的概念、生物化学实体、病理机制、药物靶标或交叉学科理论命题。
> - **问题类型** 假设生成、潜在机制推断、跨学科概念穿透、前沿空白识别。
> - **分析单位** 概念实体三元组（A-B-C 路径）与共现关联强度。
> - **输出形式** 经拓扑排序与语义过滤后的高优先级候选科学假说列表。

> [!citation-card] 斯旺森假说与潜在知识挖掘逻辑
> 单纯增加概念库容量及其关联通常会导致产生海量低质量假说，因此筛选过程需要具备敏锐的鉴别力。定位高价值发现的经典范式是斯旺森假说：若概念 A 与 B 在特定文献群体中被共同研究，而 B 与 C 在另一独立文献群体中被探讨，则 A 与 C 之间的潜在联系便具有探索价值。斯旺森依托这一方法推导出鱼油能减轻雷诺氏血液病症状，并指出镁缺乏与偏头痛存在生理关联，两项假说均在后续研究中获得实证支持。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 227)]]
>
> *One example of how to home in on valuable discoveries is the Swanson hypothesis. Swanson posits that if concepts A and B are studied in one literature, and B and C in another, then the link between A and C may be worth exploring. Using this approach, Swanson hypothesized that fish oil could lessen the symptoms of Raynaud’s blood disorder and that magnesium deficits are linked to migraine headaches, both of which were later validated.*

---

> [!method-position] 方法定位
> - **认识论前提** 现代科学的高度专业化与学科壁垒导致知识碎片化，大量客观存在且在逻辑上相互吻合的公开数据散落在孤立子领域中，形成了未被发现的隐性真理库。
> - **构念效度** 依赖实体识别的精准度与中间桥梁概念 B 的语义特异性；泛化度过高的高频停用词会诱发组合爆炸与假阳性关联。
> - **推断边界** 该方法输出的是具有高度探索价值的理论假设或关联线索，其因果真实性与有效性必须经过受控实体实验或临床观察的独立检验。

> [!method-stack] 方法层级
> - **上位方法** 科学计量学（Scientometrics）与计算知识发现（Knowledge Discovery in Databases, KDD）。
> - **前置步骤** 生物医学实体识别（Named Entity Recognition, NER）、文本分词与概念消歧。
> - **分支形态** 开放式发现（Open Discovery，给定 A，寻找未知 C）与封闭式检验（Closed Discovery，给定 A 与 C，检索潜在中介 B）。

---

> [!proc] 通用分析流程
> 1. **语料构建与实体抽取** 针对特定科学领域检索海量文献摘要或全文，运用自然语言处理工具标定关键构念与实体节点。[[Argument_Wang_Barabasi_2021_Cambridge_Unit10|(Wang & Barabási, 2021, p. 227)]]
> 2. **子图划分与共现关联映射** 建立概念共现二值网络或加权图谱，依据学科领域标签识别相互隔绝的孤立文献子集。
> 3. **中介路径遍历与评分** 针对孤立实体 A 遍历跨文献集的中介节点 B，计算 A-B 与 B-C 的综合拓扑权重，生成候选关联 A-C。
> 4. **先验约束与语义过滤** 引入领域本体论图谱与关联度阈值剔除平凡无用连接，压缩假说空间以规避组合爆炸。
> 5. **专家评估与实体实验验证** 领域专家对排名前列的高置信度假说展开机理解释评估，并移交实验室开展实体干预实证。

---

> [!contrast-table] 发现模式与适用特征
> | 维度 | 开放式发现（Open Discovery） | 封闭式检验（Closed Discovery） |
> |---|---|---|
> | **初始输入** | 单一关注概念 A（如某种罕见病理现象） | 两个已知具有潜在关联但机制未明的概念 A 与 C |
> | **推断目标** | 自动发现全新的潜在干预物质或靶标 C | 自动搜寻解释 A 与 C 相互作用的潜在生理中介 B |
> | **典型输出** | 探索性候选治疗方案或新型材料假说 | 解释性因果链条假设与机制说明路径 |
> | **代表案例** | 斯旺森由雷诺氏症出发搜寻到鱼油（EPA） | 斯旺森在偏头痛与镁缺乏之间寻找中介血管痉挛机制 |

---

> [!method-limits] 方法局限
> - **组合爆炸风险** 随着文献语料规模激增，二阶邻域路径数量呈指数级膨胀，若缺乏结构化领域先验引导，系统将输出大量信噪比极低的平庸假说。
> - **文件抽屉造成的盲目重复** 若此前已有学者尝试过 A 与 C 的关联但因负结果未予发表，单纯依赖正向公开文献的算法将重复推荐已在物理实验室宣告失败的死胡同。
> - **语义多义与语境脱落** 实体抽取算法在剥离复杂学术修辞后可能误解原始语篇中的否定语气或限定条件，导致假说推导脱离真实的生物化学或物理约束。

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit10|Wang & Barabási (2021)]] — 将斯旺森假说作为算法加速科学发现的基准方法，说明知识图谱与文本挖掘在识别高价值前沿中的演进应用。
