---
title: Homophily
aliases:
  - 同质偏好
  - 同质性
  - 族裔同质偏好
  - 学术同质偏好
  - Homophily in Science
summary: "在社会网络分析与科学计量学中，指行动者倾向于与在人口统计学特征、学术资历、文化背景或机构隶属上高度相似的个体建立联系与合作的自发倾向。在科研团队组建中，同质偏好虽然降低了前期的沟通与磨合成本，但会导致研究视角的同质化回音室，实证上伴随着期刊影响因子与长期引文表现的系统性偏低。"
type: concept
domain: "science-policy"
related_count: 8
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - concept/science-policy
  - theme/social-networks
  - theme/team-science
  - theme/sociology-of-science
related_concepts:
  - "[[Team Diversity]]"
  - "[[Coauthorship Network]]"
  - "[[Super Ties in Science]]"
related_theories:
  - "[[Team Assembly Model]]"
related_methods:
  - "[[Bibliometric Analysis]]"
related_instruments: []
related_persons:
  - "[[Brian Uzzi]]"
  - "[[Roger Guimera]]"
related_facts: []
related_arguments:
  - "[[Argument_Wang_Barabasi_2021_Cambridge_Unit05]]"
confidence: medium
status: draft
created: 2026-10-30
updated: 2026-10-30
---

---

> [!def] Homophily
> 在社会网络理论与科研合作研究中，指个体更倾向于与自身具有相似人口统计学特征（如族裔、性别、国别）、组织隶属或学科背景的同伴建立联结并组建合作团队的社会心理与结构倾向。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 114–115)]]

> [!concept-lens|notitle] 概念透镜
> - **含义** 指向行动者在社会网络联结中对“与我相似者”的内生吸引与优先选择机制。
> - **用途** 用于解释科研团队组装过程中的自发抱团现象，以及阻碍多样性团队形成的网络结构壁垒。
> - **边界** 解释合作初期的微观伙伴挑选偏好，不直接等同于团队合作过程中的内耗或冲突水平。

> [!citation-card|notitle] 科研合作中的族裔同质偏好与引文代价
> 总体而言，拥有英文姓氏的学者不成比例地更倾向于与其他英文姓氏同行合著，而华裔学者也更有可能与其他华裔科学家合作。由这种同质偏好所产生的成果，往往只能发表在影响力较低的期刊上，并且获得的引用也更少。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, p. 114)]]
>
> *In general, authors with English surnames were disproportionately likely to coauthor papers with other authors with English surnames and those with Chinese names were more likely to collaborate with other Chinese scientists. The papers that result from such homophily, however, tend to land in lower impact journals and garner fewer citations.*

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 同质偏好（Homophily） | [[Team Diversity|团队多样性]]（Team Diversity） | [[Super Ties in Science|超级合作联结]]（Super Ties） |
> |------|---------------------|-----------------------------------|-----------------------------------|
> | 概念取向 | 趋同选择倾向（网络形成机制） | 异质构成状态（结构属性） | 极少数长期绑定的高产互补伙伴（深度关系） |
> | 驱动因素 | 沟通舒适感、共享文化代码与低信任门槛 | 复杂攻关任务对多元互补技能的需求 | 高度不可替代的技能互补与共同学术理想 |
> | 创新后果 | 容易陷入认知回音室，影响力受限 | 拓展创新假说空间，产出高被引成果 | 带来超额产出速率与深厚学术突破 |

---

> [!feature] 核心表现
> - **文化与族裔趋同** 学者优先寻找母语相同或文化习惯相似的同行结为合著者，形成圈层内部高密度合署。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, p. 114)]]
> - **熟人圈子自我复制** 在任老手倾向于反复挑选已有合作经历的旧搭档（对应团队组装模型中的高参数 $q$），导致知识储备同质化。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 119–120)]]
> - **学术影响力折价** 规避异质摩擦的同时错失了跨界思想的交叉碰撞，导致成果在期刊层次与引用率上处于劣势。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 114–115)]]

> [!logic-map]- 同质偏好的形成与后果
> ```mermaid
> flowchart LR
>     A["相似文化与背景特征"] --> B["沟通便利与即时信任"]
>     B --> C["同质偏好合作网络形成"]
>     C --> D["降低前期组队协调成本"]
>     C --> E["认知回音室与思维定势"]
>     E --> F["期刊影响因子与被引率系统性偏低"]
> ```

---

> [!concept-proposition] 命题一｜科研合作中的同质偏好降低了前期磨合阻力，但抑制了学术突破的新颖度
> **探讨维度　团队组建中的心理舒适与创新潜力的张力** 该命题探讨同质偏好对科研绩效的双刃剑机制。同质合作虽然提供了畅通的内部交流氛围，但同质化知识结构难以激发创造性思想碰撞。
>
> [!claim] Freeman, R. B.
> **同质偏好造成学术影响力与期刊层级的系统性折价** 对全美 250 万篇论著的大数据分析表明，科研人员表现出显著的族裔同质合作倾向；全同质团队产出成果的引文表现比吸纳异质背景的团队低 5% 至 10%，证实舒适同质倾向对学术产出质量存在潜在损害。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 114–115)]]

---

> [!concept-proposition] 命题二｜熟人搭档的过度封闭抱团与期刊学术水准呈负相关
> **探讨维度　既往联结重复率对学术水准的约束机制** 该命题聚焦合作演化中的网络封闭性。在任老手如果过度依赖熟悉旧搭档，将削弱团队吸纳新颖知识的能力。
>
> [!claim] Guimerà, R.
> **重复合作偏好参数与顶刊发表表现呈现负向关联** 在跨经济学、生态学、天文学与社会心理学的实证拟合中，团队组装模型中表征与既往搭档重复合作倾向的参数 $q$ 与期刊影响因子始终保持稳健的负相关关系，证明过度抱团会阻碍团队提出开创性思想。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 119–120)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **影响力折价命题** | 族裔与背景同质偏好导致成果发表层级与引用率偏低 | 跨机构与跨文化科研合作决策 | Freeman and Huang (2014); [[Argument_Wang_Barabasi_2021_Cambridge\|Wang and Barabási (2021)]] |
> | **网络封闭抑制命题** | 资深学者过度重复合署旧伙伴会固化思维范式并降低期刊水准 | 科学合作网络组装与学术梯队建设 | Guimerà et al. (2005); Uzzi and Spiro (2005) |

---

> [!dev-timeline] 概念演变
> - **1954 年 — 经典社会学发轫** 保罗·拉扎斯菲尔德（Paul Lazarsfeld）与罗伯特·默顿（Robert K. Merton）在研究友谊网络时正式提出“同质偏好（Homophily）”概念。
> - **2001 年 — 社会网络综述奠基** 麦克弗森（Miller McPherson）等人在《Annual Review of Sociology》发表里程碑文献，系统总结同质偏好在种族、性别、年龄等维度的普遍规律。
> - **2014 年 — 科学学实证测度** 理查德·弗里曼（Richard Freeman）与黄炜（Wei Huang）利用海量论著大数据量化科研领域的族裔同质偏好，确证其对学术引用的负向影响。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 114–115)]]

---

> [!warning|limits] 适用局限
> 同质偏好是社会网络形成的普遍基础机制，在科研早期阶段有助于青年学者快速建立心理安全感、确立共同语言并降低沟通成本；只有当团队长期处于封闭自洽状态、拒绝外部异质视角介入时，同质偏好才会演化为抑制创新的认知屏障。不能将其简单等同于科研恶意或狭隘主义。[[Argument_Wang_Barabasi_2021_Cambridge_Unit05|(Wang & Barabási, 2021, pp. 114–115, 118)]]

---

> [!empirical-divider]

> [!ref-table]- 其他实证结果（无效应量）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | 变量或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Wang_Barabasi_2021_Cambridge_Unit05\|Freeman & Huang (2014)]] | 1985–2008 年美国发表的 250 万篇学术论著 | 姓名学算法与计量经济学分析 | 族裔合著同质偏好及其对引文与期刊层级之影响 | 英文姓氏学者偏好与同姓氏同行合署，华裔学者偏好与华裔合作；同质合署成果在期刊影响因子与引用率上系统性低于异质团队 5%–10% | $p < 0.01$ | 揭示舒适心理带来的同质合作会遭受学术影响力惩罚 |

---

> [!evidence-grid-a|notitle] 相关研究索引
> - [[Argument_Wang_Barabasi_2021_Cambridge_Unit05|Wang & Barabási (2021)]] — 结合全美 250 万篇论著与四大基础学科网络拟合，揭示族裔与既往搭档维度的同质偏好对成果期刊层级与长期引文的制约机制。
