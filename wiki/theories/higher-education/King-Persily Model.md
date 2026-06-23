---
title: King-Persily Model
aliases:
  - 金-珀斯利模型
  - King Persily model
  - King-Persily 模型
summary: "King 与 Persily（2019）提出的产学合作数据治理模型，通过引入第三方委员会来解耦研究者对产业数据和专有信息的完全访问，最初针对社会科学与社交媒体大数据场景，Swick 与 Jones（2025）讨论了其在生物医学创新中的适用性"
type: theory
theory_field: "higher-education"
theory_related_count: 7
theory_related_level: 0
theory_related_stars: ""
theory_related_color: "#e5e7eb"
tags:
  - "theory/data-governance"
  - "theme/university-industry-collaboration"
  - "theme/data-ethics"
  - "level/higher-education"
related_concepts:
  - "[[University-Industry Collaboration]]"
  - "[[Clinical Trial]]"
  - "[[Academic Health System]]"
  - "[[Informed Consent]]"
related_theories: []
related_methods: []
related_persons: []
related_facts:
  - "[[Social Science One]]"
related_arguments:
  - "[[Argument_Swick_Jones_2025_AcademicHealthSystems]]"
  - "[[Argument_OxfordUIDP_2019_UIPartnerships]]"
confidence: medium
status: draft
created: 2026-06-02
updated: 2026-06-10
---

# King-Persily Model

## 核心主张

> [!tip]-
> King-Persily 模型（King & Persily, 2019）提出了一种解决大学与产业在数据治理和专有信息问题上矛盾的合作框架。其核心思路是：引入一个独立的第三方委员会，将研究者与产业数据、政策和专有信息之间的完全接触解耦（decouple），从而使研究者可以在不掌握产业专有数据的前提下完成独立学术研究([[Argument_Swick_Jones_2025_AcademicHealthSystems|Swick & Jones, 2025, p.188]])。

该模型最初为解决社会科学领域和社交媒体大数据场景下的[[University-Industry Collaboration|产学合作]]困境而设计——产业伙伴担心敏感数据被公开或滥用，而学术研究者需要数据来开展独立研究。第三方委员会在两者之间充当缓冲层和治理中介。

## 核心命题

> [!abstract]
> King-Persily 模型的核心命题包含两个维度（[[Argument_Swick_Jones_2025_AcademicHealthSystems|Swick & Jones, 2025, pp.188–189]]）：
> - **数据访问与学术独立的平衡**：第三方委员会负责审查数据访问请求，确保研究者在获得必要数据的同时，产业伙伴的专有信息不被泄露。这既保护了学术研究的独立性，也回应了产业对数据安全的关切。
> - **适用于数据密集型合作场景**：该模型尤其适用于那些分析对象本身就是产业持有的数据（如社交媒体平台数据、患者数据、[[Clinical Trial|临床试验]]数据）的[[University-Industry Collaboration|产学合作]]项目。

## 运作结构

> [!abstract]
> King-Persily 模型的具体运作结构包括以下核心组件（[[Argument_OxfordUIDP_2019_UIPartnerships|Oxford & UIDP, 2019, pp.13–14]]）：

- **公司端（Company）**：提供数据和信息，但不直接接触研究者；公司与委员会共同商定研究项目的范围，并发布研究提案征集
- **委员会（The Commission — 可信第三方）**：由资深学者组成，与公司签署保密协议并放弃基于数据的发表权。委员会独立评审研究提案的学术和社会价值，排除侵犯隐私、违反现有法律协议/义务、干扰正在进行的调查或使公司处于竞争劣势的提案
- **非营利基金会（Nonprofit Foundations）**：提供资助，不参与数据访问决策
- **独立学术专家（Independent Academic Experts）**：来自大学的独立研究者，申请资助和（经过隐私保护的）数据访问；研究成果发表**无需公司预先批准**
- **同行评审过程（Peer Review Process）**：确保研究质量和独立性

> 这一结构的关键设计原则是：公司放弃对研究提案选择和研究结果发表的事前控制，换取一个受信任的委员会机制来确保数据安全和专有利益保护。研究者获得数据访问的渠道但不需要直接接触原始隐私数据。基金会提供中立的资金来源，进一步保障了研究的独立性。

该模型已在 [[Social Science One]] 实施，并在哈佛大学定量社会科学研究所内部孵化。

## 在生物医学创新中的适用性

> [!note]-
> 在生物医学研究创新空间中，King-Persily 模型具有一定的适用性，但需要两项重要调整（pp.188–189）：
> 1. **发表权保留**：[[Academic Health System|学术健康系统]]倾向于保留发表研究结果的权利，但同意给予产业伙伴一个时间窗口来审阅和删节专有信息。
> 2. **患者数据去标识化**：所有患者数据在使用前必须去标识化，以保护患者和受试者隐私。此外，患者数据不应被货币化出售——学术健康系统对患者负有信托责任，其使用必须符合[[Informed Consent|知情同意]]所授权的目的。

## 争议与批评

> [!warning]
> 患者数据在[[University-Industry Collaboration|产学合作]]中面临特殊的伦理困境，独立于任何具体合作框架：患者数据是 [[Academic Health System|AHS]] 在产学合作中的核心价值之一，但不能简单地提供给合作伙伴——即使已去标识化。缺乏医学背景的人可能从中得出错误结论，而错误的结论可能导致生命代价。这构成了对该模型在医疗场景中应用的额外约束（pp.188–189）。

