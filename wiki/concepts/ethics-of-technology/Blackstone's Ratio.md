---
title: Blackstone's Ratio
aliases:
  - 布莱克斯通比率
  - 布莱克斯通公式
  - Blackstone's formulation
  - 疑罪从无原则
summary: "英国法学家威廉·布莱克斯通在《英国法释义》中确立的刑事司法经典认识论原则（宁可放过十个罪犯，不可冤枉一个无辜）；体现了刑法对误判无辜的极端零容忍态度，并构成当代在执法中应用人工智能与监控技术时权衡误伤风险与公共安全效能的基准伦理框架。"
type: concept
domain: "ethics-of-technology"
related_count: 7
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - concept/jurisprudence
  - theme/criminal-justice
  - theme/legal-epistemology
  - theme/ai-ethics
related_concepts:
  - "[[Type I and Type II Errors]]"
  - "[[Evidence Standards]]"
  - "[[Predictive Policing]]"
  - "[[Pragmatic Paradigm]]"
  - "[[Epistemology]]"
related_theories: []
related_methods:
  - "[[Correlational Research]]"
related_instruments: []
related_persons:
  - "[[William Blackstone]]"
  - "[[Alexander Karp]]"
  - "[[Nicholas Zamiska]]"
related_facts: []
related_arguments:
  - "[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch15]]"
confidence: high
status: draft
created: 2026-10-08
updated: 2026-10-08
---

# Blackstone's Ratio

---

## 定义

> [!def] 核心定义
> [[William Blackstone|布莱克斯通]]比率（Blackstone's Ratio）指 18 世纪英国法学家威廉·[[William Blackstone|布莱克斯通]]在《英国法释义》中提出的经典刑事法理准则——“宁可让十个有罪之人逃脱法网，也不可使一个无辜者遭受冤狱”（It is better that ten guilty persons escape than that one innocent suffer）；该原则确立了刑事司法对一类错误（[[Type I and Type II Errors|false positive]]，冤枉无辜）相比于二类错误（False Negative，漏网之鱼）的绝对不对称容忍阈值，构成了现代正当程序与疑罪从无理念的核心法理支柱。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch15|(Karp & Zamiska, 2025, p. 174)]]

> [!concept-lens] 概念透镜
> - **含义** 确立国家公权力在剥夺公民人身自由时必须承受的极端审慎证据要求。
> - **用途** 衡量司法审判[[Evidence Standards|证据标准]]（超越合理怀疑）、审查新兴侦查技术（人脸识别、算法警务、DNA 鉴定）的假阳性误判风险。
> - **边界** 适用于刑事司法的定罪与人身自由剥夺，不直接等同于行政调查、风险预防或公共基础设施的容错机制。

> [!citation-card] 布莱克斯通论宁纵十罪不枉一无辜
> 司法审理宁可让十个有罪的人逃脱，也绝不能让一个无辜的人蒙受冤屈；这一比例深刻塑造了法治传统中关于司法误判容忍度的核心讨论框架。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch15|(Karp & Zamiska, 2025, p. 174)]]; (Blackstone, 1893, p. 587)
>
> *In the eighteenth century, William Blackstone, one of England's greatest legal minds, went further, writing that it would be better to allow "ten guilty persons escape than that one innocent suffer"—a ratio that would come to structure debate about errors, permissible or otherwise, in criminal justice.*

---

## 概念演变与思想谱系

> [!dev-timeline] 刑事司法错误容忍思想谱系
> - **1749 — 伏尔泰（Voltaire）** 在哲学小说《查第格》（*Zadig*）中提出：放走两个有罪之人，远好过惩罚一个清白无辜之人（比例 2:1）。
> - **1760年代 — [[William Blackstone|威廉·布莱克斯通]]（[[William Blackstone]]）** 在《英国法释义》中正式确立 10:1 的经典比率，成为普通法宪政传统的基石。
> - **1826 — 托马斯·斯塔基（Thomas Starkie）** 在证据法专著中将比率极端推高至 99:1，主张宁纵九十九罪犯，不枉一无辜。
> - **当代 — 科技警务与算法治理时代** 成为评估[[Predictive Policing|预测性警务]]、自动化监控与面部识别系统错误容忍度的法理标尺。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch15|(Karp & Zamiska, 2025, p. 174)]]

---

## 核心要素

> [!feature] 核心要素
> - **价值不对称性（Normative Asymmetry）** 冤枉无辜造成的国家伦理损害被判定为远大于放纵犯罪的实际损害。
> - **对[[Pragmatic Paradigm|实用主义]]妥协的排斥（Rejection of Pragmatic Error Tolerance）** 刑事司法不同于一般工程或商业决策，绝非容忍“可接受故障率”的实用主义试验场。
> - **技术合规设计的根本约束（Design Constraint for Tech）** 要求在研发和部署执法类软件时，必须以哪怕防范一次潜在滥用为导向构建系统。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch15|(Karp & Zamiska, 2025, p. 174)]]

---

## 围绕概念形成的命题

---

### 命题一　刑事司法的极端审慎原则要求执法软件的设计必须将防范误判无辜置于最高优先级

> [!concept-lens] 法律[[Epistemology|认识论]]与技术伦理
> 探讨法治国原则对算法工程研发与权限设计的根本规范约束。

> [!claim] [[William Blackstone|Blackstone, W.]]
> **刑事司法绝非[[Pragmatic Paradigm|实用主义]]容错的试验场** 威廉·布莱克斯通及启蒙思想家确立的法理传统强调，刑事司法的权威建立在对无辜者不可侵害的绝对承诺之上；任何旨在辅助执法的信息技术或软件，在架构设计与实战部署时都必须以“哪怕只有一次误用或侵害无辜的可能”作为警示，确保严格的程序正义不可动摇。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch15|(Karp & Zamiska, 2025, p. 174)]]

---

### 命题二　对技术误用风险的合理审慎不应演化为彻底放弃运用技术打击犯罪的逃避借口

> [!concept-lens] 公共治理与风险决策
> 阐明在恪守布莱克斯通原则与积极运用技术拯救生命之间的动态平衡。

> [!claim] [[Alexander Karp|Karp, A. C.]], & [[Nicholas Zamiska|Zamiska, N. W.]]
> **克服未知恐惧与承担治理复杂性** 亚历山大·卡普与尼古拉斯·扎米斯卡指出，布莱克斯通比率强调的是司法语境下的道德审慎，而非推卸公共治理责任的借口。当前部分机构因害怕面对新技术的潜在不确定性与复杂性，索性对严重暴力犯罪采取彻底不作为的冷漠态度；真正的法治与工程精神要求在严格贯彻防范误判机制的同时，积极运用先进软件化解城市枪患与暴力威胁。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch15|(Karp & Zamiska, 2025, p. 174)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |:---|:---|:---|:---|
> | **法理底线确立** | 宁纵十罪不枉一无辜构成了刑事证据与司法的最高道德律令 | 刑事审判、[[Evidence Standards\|证据标准]]、程序法治 | [[William Blackstone]] (1893); Voltaire (1749) |
> | **治理责任平衡** | 审慎防范技术误用必须与运用科技积极遏制暴力犯罪有机结合 | [[Predictive Policing\|预测警务]]政策、科技伦理、公共安全 | [[Alexander Karp]] & [[Nicholas Zamiska]] (2025) |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Karp_Zamiska_2025_Technological_Republic_Ch15|Karp & Zamiska (2025)]] — 引述伏尔泰、[[William Blackstone|布莱克斯通]]与斯塔基的法律[[Epistemology|认识论]]传统，剖析前沿算法警务中的误判风险与公共安全平衡问题。
