---
title: Coauthorship Network
aliases:
  - 合著网络
  - 科学合著网络
  - 合作出版网络
  - scientific collaboration network
summary: "依据学术论著联合署名关系构建的复杂拓扑网络；具有跨学科异质性的重尾度分布、少数超级枢纽节点、平均路径约为 6 步的小世界特性以及覆盖 80%–90% 活跃学者的巨连通分支，其宏观相变与成果新颖度受资历传承与重复合作等微观组装规则深度调控。"
type: concept
domain: "science-policy"
related_count: 0
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
confidence: high
status: active
created: 2026-10-30
updated: 2026-10-30
---

---

> [!def] Coauthorship Network
> 合著网络（Coauthorship Network）指以科学研究人员为网络节点，以共同在正式学术期刊、会议文集或专利上联合署名为无向连接边的复杂社会拓扑网络。该网络是科学学中量化测度科学界社会组织形态、学术交流拓扑、微观团队组配动力学与知识协同扩散的基础结构基底。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 102–104)]]; [[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 118–123)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 刻画科学界实际发生的实质知识生产协作连线与学者社会关系图谱。
> - **用途** 帮助科学计量学与网络科学研究者识别核心学术领袖（枢纽节点）、挖掘前沿交叉派系、测算学科隔阂距离（小世界特征），并预测科研合作演化机制。
> - **边界** 合著网络仅记录正式署名层面的硬性出版记录，未能完全穷尽非署名的学术研讨、指导建议与同行审稿等非正式交往。

> [!citation-card] 合著网络的多学科异质性与拓扑特征
> 每一个分布都呈现重尾特征，表明无论在哪个学科，几乎所有科学家都只与少数合作学者共事，而极少数人积累了数量庞大的合作学者。在生物学、物理学和数学这三个学科中，合著网络的度分布遵循不同的衰减规律，生物学具有更长的长尾，而数学的衰减速度最快。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 104–105)]]
>
> *Each of these distributions is fat-tailed, indicating that, regardless of their discipline, almost all scientists work with only a few coauthors, while a rare fraction accumulates an enormous number of collaborators. But, though all three distributions shown in Fig. 10.2 are fat-tailed, the curves follow distinct patterns.*

> [!boundary]- 概念边界
> - 不等于 引文网络（Citation Network） — 引文网络是有向的文献到文献的智识继承网络；合著网络则是无向的学者与学者之间共同工作的合作关系网络。
> - 不等于 社交互联网络 — 合著网络要求有共同承担学术与法律责任的公开出版成果，连接门槛远高于一般线上互动或学术社交关注。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 学术合著网络（Coauthorship Network） | 文献引文网络（Citation Network） | 社交互联网络（Online Social Network） |
> |------|------------------------------------|---------------------------------|--------------------------------------|
> | **节点类型** | 科学家个体（唯一学者标识符） | 单篇学术成果或专利文献 | 注册用户（包含公众与机构账户） |
> | **连接性质** | 无向边（或带权边表示共同发文篇数） | 有向边（从施引文献指向被引文献） | 有向（关注）或无向（好友） |
> | **连带强度** | 极高，需要数月乃至数年的协同实质科研 | 适中，反映理论引用、方法借鉴或观点批判 | 极低至中等，轻量化点赞、评论或关注 |
> | **演进机制** | 优先连接（趋向资深知名学者）与小世界聚集 | 累积引文吸附（马太效应）与新近性偏倚 | 算法信息流推送、同质性匹配与地理邻近 |

---

> [!feature] 核心要素
> - **重尾度分布与超级枢纽节点** 绝大多数科学家的合著学者数量十分有限，而极少数像保罗·埃尔德什（Paul Erdős）这样的超级合作学者拥有数百位合著者，成为维系整个网络低阶连通的核心枢纽。生物学尾部最长，物理学次之，数学衰减最快。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 104–105)]]
> - **优先连接机制驱动网络集聚** 早期初入网络的青年学者更倾向于与导师或既有高连通度资深学者联合署名，使拥有更多学术伙伴的学者以更快速度吸纳新连线，逐步固化为网络拓扑的核心枢纽。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 105–106)]]
> - **小世界六度分隔拓扑** 尽管科学界包含数以百万计的学者，任意两位学者之间的平均最短合著路径长度通常仅为 5 至 6 步，且与核心枢纽学者的平均距离更短（如数学家到 Erdős 的平均距离仅为 4.7 步）。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 106)]]
> - **巨连通分支的普遍覆盖** 真实学科合著网络中 80% 至 90% 的学者被统一包含在同一个最大连通分支即巨连通分支（Giant Component, GCC）内部，证实科学界本质上是一个广泛连接的有机整体。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 108–109)]]
> - **微观组装规则驱动宏观结构相变** 宏观合著网络由团队微观组配概率驱动；资历参数 $p$（老手比例）跨越临界值时涌现出全局巨连通分支，而重复合作参数 $q$（熟人抱团）过高会导致网络退化为割裂的孤立小圈子。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 119–121, 254–256)]]

> [!logic-map]- 要素关系
> ```mermaid
> flowchart TD
>   A["学者微观团队组装 (p, q 参数)"] --> B["合著网络拓扑构建"]
>   B --> C["重尾度分布 P(k) (超级枢纽学者)"]
>   B --> D["密集局域社群 (知识范式聚集)"]
>   B --> E["短平均路径 (小世界拓扑 ~6 步)"]
>   B --> F["巨连通分支 (覆盖 80%-90% 学者)"]
>   C --> G["优先连接巩固枢纽中心度"]
>   A -->|高 p 低 q| F
>   A -->|高 q 熟人封闭| H["割裂的小圈子回音室"]
> ```

---

## 围绕概念形成的命题

---

> [!concept-proposition] 命题一｜合著网络展现跨学科异质性的重尾度分布与超级枢纽结构
> **探讨维度　科研合作网络的拓扑微观异质性** 探讨不同知识生产范式下合著网络连接度衰减速率的学科差异。

> [!claim] [[Albert-László Barabási|Barabási, A.-L.]]
> **学科劳动分工决定网络连接长尾** 当代生物医学湿实验的大规模分工拉长了度分布极值尾部，物理学的大科学工程团队与中等理论团队并存，而纯理论数学的合著规模分布衰减最陡峭，高度协作型个体在数学界极度稀缺。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 104–106)]]

---

> [!concept-proposition] 命题二｜适度小世界拓扑在维持群体凝聚力与吸纳异质新颖性之间取得最优平衡
> **探讨维度　网络拓扑对集体创造力与绩效的调控** 探讨合作网络松紧程度与团队创新表现之间的非线性因果机制。

> [!claim] [[Brian Uzzi|Uzzi, B.]]
> **小世界商数与团队创造力的倒 U 形关联** 百老汇百年创作网络实证表明，网络过于稀疏阻碍外部知识流动，过度紧密纠缠引发同质化认知回音室，唯有适度小世界网络兼具局域信任与外部异质思想，产出最高的商业与艺术绩效。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 107–108)]]

---

> [!concept-proposition] 命题三｜微观组配规则调控宏观合著网络拓扑相变并决定成果新颖度
> **探讨维度　在任老手经验与重复搭档封闭度的相变临界点** 阐明个体微观组队选择如何自下而上重塑全学科宏观网络连通性与学术突破质量。

> [!claim] [[Roger Guimera|Guimerà, R.]] & [[Brian Uzzi|Uzzi, B.]]
> **团队组装参数驱动全网巨连通分支相变** 罗杰·吉梅拉（Roger Guimerà）与布赖恩·乌齐（Brian Uzzi）建立的团队组装模型表明，宏观合著网络的全局贯通取决于在任老手资历参数 $p$ 与重复合作参数 $q$。只有当老手比例 $p$ 达到统计临界值时，全网才会涌现出连通绝大多数学者的巨连通分支；然而，若老手过度倾向于与旧搭档重复合署（高 $q$），网络将迅速退化为封闭孤立的小世界派系，阻碍跨界知识流动并系统性压低期刊影响因子。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 119–121, 254–256)]]

---

> [!concept-proposition] 命题四｜合著网络由高流失弱纽带支配但依赖少数终身超级联结创造代表作
> **探讨维度　合著关系生命周期与非对称产出极值** 揭示合著网络中普遍的短暂弱纽带与罕见的终身强纽带在学术生涯中的分工法则。

> [!claim] Petersen, A. M.
> **弱纽带流动与超级搭档高产并存** 亚历山大·彼得森（Alexander M. Petersen）追踪资深学者数十年发表全景，证实科学合著网络中 60% 至 80% 的合作关系仅维系 1 年；然而平均每 25 位合署学者中即存在 1 位终身超级搭档（Super Tie）。学者与超级搭档合署了半数以上的核心成果，享有 8 倍产出速率与 14 倍引文净收益，表明科学合作网络依托微观弱纽带维系广泛流动，依托宏观极少数超级强纽带筑造顶尖突破。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 121–123)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **拓扑微观异质性** | 学科分工模式决定合著网络重尾与枢纽结构 | 跨学科合著网络度分布测度 | Newman (2001); Barabási et al. (2002); [[Argument_Wang_Barabasi_2021_Cambridge_Unit04\|Wang and Barabási (2021)]] |
> | **小世界倒 U 形创造力** | 适度小世界拓扑平衡内部默契与外部异质性 | 创意团队与前沿科研网络演化 | Uzzi and Spiro (2005); [[Argument_Wang_Barabasi_2021_Cambridge_Unit04\|Wang and Barabási (2021)]] |
> | **组装参数相变调控** | 资历参数驱动巨连通分支涌现，熟人抱团诱发网络割裂 | 跨学科微观团队组配与宏观网络拓扑相变模拟 | Guimerà et al. (2005); [[Argument_Wang_Barabasi_2021_Cambridge_Unit05\|Wang and Barabási (2021)]] |
> | **强弱纽带非对称分工** | 脆弱弱纽带主导网络流动，少数终身强纽带贡献核心巅峰突破 | 科研人员全生命周期合著网络动态测度 | Petersen (2015); [[Argument_Wang_Barabasi_2021_Cambridge_Unit05\|Wang and Barabási (2021)]] |

---

> [!dev-timeline] 概念演变
> - **1990 — 六度分隔文学表达** 剧作家约翰·盖尔（John Guare）在戏剧中写下著名台词，指出全人类由平均六个人隔开。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, p. 107)]]
> - **1998 — 小世界网络数理形式化** 邓肯·瓦茨（Duncan Watts）与史蒂文·斯特罗加茨（Steven Strogatz）形式化定义高聚类与短路径并存的小世界网络模型。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 106–107)]]
> - **2001–2002 — 科学合著网络实证奠基** 马克·纽曼（Mark Newman）与巴拉巴西等将合著网络作为复杂网络真实样本，测定其无标度与小世界拓扑属性。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 104–106)]]
> - **2005 — 团队组配模型与相变机制确立** 罗杰·吉梅拉（Roger Guimerà）与布赖恩·乌齐（Brian Uzzi）提出基于老手-新秀池的团队组装生成模型，量化 $p-q$ 参数对合著网络相变的调控。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 119–121, 254–256)]]
> - **2015 — 终身超级联结动力学揭示** 亚历山大·彼得森（Alexander M. Petersen）在 PNAS 发文系统揭示合著网络中弱纽带高流失与超级强纽带超额溢价的规律。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 121–123)]]

---

> [!warning|limits] 适用局限
> 合著网络拓扑分析基于正式出版物联合署名名单，无法捕捉未署名的口头指导、同行评议与非正式学术讨论；且在高能物理等万人署名大科学工程中，署名名单更接近团队成员名录，可能弱化个体真实贡献的辨识度。[[Argument_Wang_Barabasi_2021_Cambridge_Unit04|(Wang & Barabási, 2021, pp. 103–105)]]; [[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 124–125)]]

---

> [!empirical-divider]

> [!ref-table]- 其他实证结果（无效应量）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | 变量或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit04\|Barabási et al. (2002)]] | 生物学、物理学与数学三大基础学科全量发表数据 | 复杂网络拓扑计量与度分布拟合 | 度分布幂律衰减；巨连通分支（GCC）覆盖率 | 生物学度分布重尾最长，数学衰减最陡峭；80% 至 90% 活跃学者处于同一巨连通分支中 | $P < 0.001$ | 针对自然科学与数学基础期刊全样本 |
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit04\|Uzzi & Spiro (2005)]] | 百老汇 1889 至 1989 年间上演的全部 2,258 部音乐剧创作网络 | 历史创作网络纵向计量回归模型 | 小世界商数 $W$ 与票房收益、剧评得分的关联 | 呈现高度稳健的倒 U 形关联：中等 $W$ 下作品票房与艺术声誉达到双重峰值 | $p < 0.01$ | 样本聚焦艺术创意产业团队网络 |
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit05\|Guimerà et al. (2005)]] | 经济学、生态学、天文学与社会心理学四大领域数十年发表记录 | 团队组装生成模型拟合与计量回归 | 老手资历参数 $p$、重复合作参数 $q$ 与期刊影响因子的关联 | 在所有四个学科中，$p$ 与期刊影响因子均呈高度显著正相关，$q$ 与期刊影响因子呈高度显著负相关 | $P < 0.001$ | 适用于高校与科研院所学术合署论著 |
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit05\|Petersen (2015)]] | 细胞生物学与物理学 473 位资深学者，166,000 条合著关系 | 终身合著网络生命周期生存分析 | 合作持续时间；超级合作纽带发生率；发文速率与引文溢价 | 60%–80% 合作仅存活 1 年；平均每 25 位合署学者中出现 1 位超级搭档；与超级搭档合作时发文速率提升 8 倍，引文净影响提升 14 倍 | 统计检验显著 | 针对长期高产资深学者的合署轨迹追踪 |

---

> [!evidence-grid-a|notitle] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit04|Wang and Barabási (2021)]] — 解析合著网络重尾分布与巨连通分支，并依托微观组装模型（[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|Unit 05]]）揭示强弱纽带分工规律。
