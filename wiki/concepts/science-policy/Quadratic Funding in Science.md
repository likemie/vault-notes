---
title: Quadratic Funding in Science
aliases:
  - 科学二次方资助
  - 二次方配比资助
  - 二次方配比资助机制
  - 二次方资助
  - Quadratic Funding
  - Quadratic Research Funding
summary: "指基于机制设计理论将公共配比资金池按赞助人数平方根之和的平方进行分配的算法资助模式，旨在通过放大基层小额支持广度以打破学术权威把关偏倚。"
type: concept
domain: "science-policy"
related_count: 7
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - science-policy
  - metascience
  - mechanism-design
  - public-funding
related_concepts:
  - "[[Metascience]]"
  - "[[Big Science]]"
  - "[[Gatekeepers]]"
  - "[[Seniority Barrier in Academia]]"
related_theories: []
related_methods:
  - "[[Matching]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Kratsios_2026_OSTP]]"
confidence: medium
status: draft
created: 2026-10-07
updated: 2026-10-07
---

# Quadratic Funding in Science

---

## 定义

> [!def] 核心定义
> **科学领域的二次方配比资助机制（Quadratic Funding in Science / Quadratic Research Funding）**是指源自机制设计（Mechanism Design）与公共品融资理论的一种算法化科研经费配置模式。该机制设立中央匹配资金池，项目的最终获资助总额不仅取决于收到的捐助总金额，更与“赞助人数的平方根之和的平方”（即 $(\sum_{i} \sqrt{c_i})^2$）成正比，从而赋予获得大量基层研究人员、青年学者及跨学科探索者小额背书的课题极高的配比乘数，系统性纠正少数权威评审专家垄断经费把关权所导致的风险规避偏倚。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, pp. 30, 87)]]

> [!concept-lens] 概念透镜
> - **含义** 指向科研资助中“支持人数广度”优先于“单一大额资金偏好”的去中心化算法配置规则。
> - **用途** 帮助[[Metascience|元科学]]与政策研究者设计能够识别被传统共识评审边缘化的非主流假说、跨界冷门探索及基础开源科研工具的资助工具。
> - **边界** 适用于具有公共品属性、广泛外部性且在学术社群中存在真实需求的探索性课题，不适用于必须由国家统筹的单一重资产巨额[[Big Science|大科学工程]]。

> [!citation-card] 二次方配比资助与去中心化科学配置
> 二次方配比资助试验强调基层共同体背书广度而非单一资助方额度，通过机制设计探索降低把关者偏倚的新型配置模式，促进科学资源的民主化与多样化分配。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, p. 30)]]
>
> *Quadratic funding experiments emphasize the breadth of community support over the size of individual contributions, mathematically expanding the multiplier for projects with widespread grassroots backing.*

> [!boundary]- 概念边界
> - 不等于 普通的科研众筹（Crowdfunding） — 普通众筹仅由个体捐款线性累加（无匹配乘数），而二次方资助依托中央资金池以二次方算法对广度支持提供超额放大。
> - 不等于 基于同行评议分数的传统排名分配。

---

## 概念辨析

> [!contrast-table] 概念辨析
> | 维度 | 二次方配比资助（Quadratic Funding） | 传统同行评审拨款（Traditional Peer Review） | 纯民间科学众筹（Pure Scientific Crowdfunding） |
> |---|---|---|---|
> | **决策权分配** | 分散化：由大量社群成员的独立微额资助综合决定 | 集中化：由 3–5 名指定同行专家打分共识决定 | 完全去中心化：仅由公众个体散户自愿出资决定 |
> | **对共识的偏好** | 奖励“多人看好”但单笔小额的异端/创新选题 | 奖励“无明显硬伤”的折衷渐进式主流选题 | 依赖公众情绪公关与大众科普话题度 |
> | **抗合谋与防刷量** | 通过数学根号抑制单一金主刷量，但需防女巫攻击 | 易滋生学术派系互保、圈子利益交换 | 无匹配池，刷量成本由出资人自负 |

---

## 核心要素

> [!feature] 核心要素
> - **中央匹配资金池（[[Matching]] Pool）** 由政府科学基金、慈善机构或大学联合出资设立的专项配比基金。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, p. 30)]]
> - **二次方非线性放大算法** 匹配资金量 $M = (\sum \sqrt{c_i})^2 - \sum c_i$；当 100 人各捐 1 美元时，其获得的匹配额远高于 1 人捐 100 美元。
> - **学术身份真实性核验（Sybil Resistance）** 建立严格的学者身份链上认证或学术凭证，防止恶意拆分账户刷取配比资金。

> [!logic-map]- 要素关系
> ```mermaid
> flowchart TD
>     A["政府/慈善设立中央匹配池"] --> D["二次方配比算法计算"]
>     B["基层学者群体小额捐助 A (广度大)"] --> D
>     C["单一机构大额捐助 B (广度小)"] --> D
>     D --> E["项目 A 获得极高匹配乘数与总资助"]
>     D --> F["项目 B 获得较低匹配额"]
> ```

---

## 围绕概念形成的命题

---

### 命题一　基于社群广度支持的二次方算法能够有效降低科研把关人偏倚并激活小众颠覆性探索

> [!concept-lens] 机制设计与同行评审矫正
> 探讨算法驱动的去中心化配置如何打破传统资助评审的垄断与避险倾向。

> [!claim] [[Argument_Kratsios_2026_OSTP|Kratsios (2026)]]
> **算法配比与探索多样性** 传统同行评议在识别非常规颠覆性假说时往往因评审人的既得利益与共识妥协而失灵；引入二次方资助机制，利用数学算法放大基层学者广泛看好的小额背书课题，能够为缺乏权威背书但具备真实社群需求的青年学者与开源工具开发者提供全新资金通道，有效拓展国家科研组合的多样性边界。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, pp. 30, 87)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **算法配比与探索多样性** | 数学二次方放大机制能有效打破权威[[Gatekeepers\|把关人]]垄断，赋能小众高风险探索 | 基础科学微额探索、开源科研软件工具开发、青年跨学科基金配置 | [[Argument_Kratsios_2026_OSTP\|Kratsios (2026)]] |

---

## 概念演变

> [!dev-timeline] 概念演变
> - **2018 — 二次方融资数学模型提出** 格伦·韦尔（Glen Weyl）、维塔利克·布特林（Vitalik Buterin）与佐伊·希茨格（Zoë Hitzig）提出 Liberal Radicalism 理论框架。
> - **2019–2024 — 开源软件与去中心化科学（DeSci）试验** Gitcoin 与多个去中心化科学平台将 QF 用于资助数千个公共开源基础设施。
> - **2026 — 进入联邦国家科学政策与预算备忘录** 《科学：新黄金时代》正式将二次方资助纳入联邦资助机构多元选拔与机制设计试验序列。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, pp. 30, 87)]]

---

## 争议与批评

> [!tension] 民主化共识评估与专业科学门槛把关的张力
> - **去中心化与反垄断视角（蓝方）** 认为[[Seniority Barrier in Academia|资历垄断]]是科学停滞主因，算法民主化配置能激发最具活力的前沿突破。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, p. 30)]]
> - **科学精英把关视角（红方）** 担忧纯粹依赖社群支持会导致“学术民粹化”，且防范虚假账户的女巫攻击（Sybil Attack）在学术界需付出额外合规成本。

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Kratsios_2026_OSTP|Kratsios (2026)]] — 将二次方资助纳入美国联邦 2028 财年研发预算优先事项与[[Metascience|元科学]]试点机制。
