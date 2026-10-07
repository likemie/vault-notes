---
title: ARPANET
aliases:
  - 阿帕网
  - 高级研究计划局网络
  - Advanced Research Projects Agency Network
summary: "由美国国防高级研究计划局（DARPA）于1960年代末资助建立的全球首个基于分布式分组交换技术的计算机通信网络，是现代互联网的技术原型与制度先驱；其非专利公共协议政策与跨高校科研部署奠定了全球互联网开放架构。"
type: fact
subtype: program
region: us
fact_region: "us"
fact_kind: "program"
fact_related_count: 13
fact_related_level: 1
fact_related_stars: "⭐"
fact_related_color: "#ede9fe"
initiator_organization: "DARPA"
period: "1969–1990"
tags:
  - fact/program
  - fact/us
  - computer-networking
  - internet
  - packet-switching
  - darpa
related_concepts:
  - "[[Research Universities]]"
  - "[[Reliability]]"
  - "[[Innovation Ecosystem]]"
  - "[[Competitiveness]]"
  - "[[General Purpose Technology]]"
  - "[[Cold War University]]"
  - "[[Technology Transfer]]"
related_theories: []
related_methods:
  - "[[Internet-Based Experiments]]"
  - "[[Network Analysis]]"
related_instruments: []
related_persons:
  - "[[David C. Mowery]]"
related_facts:
  - "[[DARPA]]"
  - "[[National Science Foundation]]"
related_arguments:
  - "[[Argument_Fabrizio_Mowery_2005_REI]]"
confidence: high
status: active
created: 2026-10-05
updated: 2026-10-07
---

# ARPANET

---

## 项目背景与立项契机

> [!claim] 项目定位
> 阿帕网（Advanced Research Projects Agency Network, ARPANET）是由[[DARPA|美国国防高级研究计划局]]（Defense Advanced Research Projects Agency, [[DARPA]]）于 1960 年代末出资建立的全球首个分布式分组交换计算机广域网络，被公认为现代互联网的直接制度与技术先驱。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 38)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 1968 年底正式由 DARPA 签发主研制合同，1969 年 10 月实现首批节点连通，1975 年移交国防通信局（Defense Communications Agency, DCA）运营，1990 年正式退役并由 NSFNET 及商业互联网骨干网全面接替。
> - **发起方与资助机制** 由美国国防部高级研究计划局（DARPA）全额注资，采取大学基础研究资助与私营工程先导采购合同协同推进的模式。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, pp. 38–39)]]
> - **覆盖范围与对象** 早期连接加州大学洛杉矶分校（UCLA）、斯坦福研究所（SRI）、加州大学圣巴巴拉分校（UCSB）与犹他大学，至 1975 年迅速扩展连接超过 100 处顶尖[[Research Universities|研究型大学]]与国防科研基地。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 39)]]
> - **核心问题导向** 解决冷战核威胁与战时通信脆弱性，实现跨地域异构大型主机之间的计算资源共享与鲁棒的分布式容灾通信。

---

## 方案设计与运行机制

> [!claim] 核心机制假说
> 通过摆脱传统电信垄断机构的专有线路交换模式，采用基于无中心分布式分组交换（Packet Switching）与异构网关互联的技术路线，并将核心通信协议置于公共领域（Public Domain），以零许可壁垒的大规模先导网络催生高度竞争的软硬件生态。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, pp. 38–40)]]

> [!policy-design]- 方案设计
> - **项目目标** 验证分布式分组交换在恶劣网络环境与异构计算节点间传输数据的高[[Reliability|可靠性]]，建立跨高校与实验室的协同计算基础设施。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 38)]]
> - **覆盖对象** 遍布全美的顶尖[[Research Universities|研究型大学]]计算机科学系、国家实验室及国防外包科研机构的主机群与终端。
> - **干预措施** 资助理论学者进行分组交换协议设计；采购专用接口信息处理机（Interface Message Processor, IMP）作为通信网关；全资铺设 50 kbps 租用数字通信干线。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, pp. 38–39)]]
> - **实施控制** 采取开放的征求意见稿（Request for Comments, RFC）同行评议机制，鼓励各节点青年研究生与工程师民主参与协议草案拟定与迭代测试。

> [!citation-card] ARPANET 的先导地位与公共协议效应
> 1968 年 12 月，[[DARPA]] 向位于马萨诸塞州剑桥的小型工程公司博尔特-贝拉内克-纽曼（Bolt, Beranek and Newman, BBN）授予合同，制造连接各大顶尖科研计算设施的节点交换机。由此诞生的阿帕网被广泛公认为互联网的最早先驱。到 1975 年，随着大学与其他核心国防科研基地相继接入，阿帕网已发展壮大至 100 多个节点。（[[Argument_Fabrizio_Mowery_2005_REI|Fabrizio & Mowery, 2005, p. 39]]）
>
> *In December 1968, DARPA granted a contract to the Cambridge Massachusetts-based engineering firm of Bolt, Beranek and Newman (BBN) to build the packet switches that linked computers at several major research computing facilities. The resulting ARPANET is widely recognized as the earliest forerunner of the Internet... By 1975, as universities and other major defense research sites were linked to the network, ARPANET had grown to more than 100 nodes.* [[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 39)]]

---

## 推进历程与阶段演进

> [!dev-timeline] 项目推进历程
> - **1960年代初–1968年 — 理论奠基与先导发包** 麻省理工学院的伦纳德·克兰罗克（Leonard Kleinrock）与兰德公司的保罗·巴兰（Paul Baran）分别提出分组交换理论；1968 年底 [[DARPA]] 将首批接口信息处理机研制合同授予由麻省理工学院教授创立的新创小企业博尔特-贝拉内克-纽曼（Bolt, Beranek and Newman, BBN）。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, pp. 38–39)]]
> - **1969年–1975年 — 原型联网与网络跨域扩散** 1969 年秋实现 UCLA 与 SRI 之间的首次数据包传输；随后网络以指数级速度接入斯坦福、哈佛、MIT 等名校与军工实验室，至 1975 年实现超过 100 处异构学术节点联网。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 39)]]
> - **1974年–1983年 — 协议标准化与向互联网跃迁** 1974 年由 DARPA 资助的罗伯特·卡恩（Robert Kahn）与文顿·瑟夫（Vinton Cerf）发表传输控制协议与网际协议（TCP/IP）规范，并将该技术无偿公开在公共领域；1983 年 1 月 1 日阿帕网全面将底层网络控制协议（NCP）切换为 TCP/IP，标志着现代多网络互联互联网的正式诞生。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 39)]]
> - **1983年–1990年 — 军民分轨与退役解耦** 1983 年阿帕网军用节点正式剥离为独立的国防数据网（MILNET），剩余民用学术节点于 1986 年由[[National Science Foundation|美国国家科学基金会]]网络（NSFNET）接管扩展，ARPANET 于 1990 年功成身退完成历史性解散。

---

## 实施架构与角色分工

> [!actor-grid] 实施协同矩阵
> - **发起与资助方** [[DARPA|国防高级研究计划局]]（DARPA），负责整体战略立项、研发经费全额注资与去中心化管理协调。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 38)]]
> - **核心硬件与节点网络总承包商** 博尔特-贝拉内克-纽曼公司（BBN），负责研制专用接口信息处理机硬件与底层包交换路由软件。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 39)]]
> - **高校与学术研究网络** 麻省理工学院、斯坦福大学、加州大学伯克利分校等，负责高层主机协议（NCP、TCP/IP）开发、应用层软件（Telnet、FTP、电子邮件）发明与实验验证。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, pp. 38–40)]]
> - **电信基础设施供应商** 美国电话电报公司（AT&T），按商业规程为网络提供物理租用专线支持。

> [!contrast-table] 阿帕网与英法同期[[Internet-Based Experiments|网络实验]]跨国制度对比
> | 比较维度 | 美国 ARPANET 模式 | 英国与法国原型网络模式（如 CYCLADES） |
> |---|---|---|
> | **部署网络规模** | 依托国防巨额预算，迅速部署覆盖全美 100 多个顶尖大学与研究节点的超大规模实体网络 | 局限于少数高校实验室的小规模试验网络，缺乏广泛互联节点 |
> | **采购对象偏好** | 敢于将关键研制合同发包给 BBN 等麻省理工学院衍生新兴高科技小企业 | 普遍依赖传统国家邮政电信（PTT）垄断机构与老牌官办实验室 |
> | **知识产权规制** | 将核心 TCP/IP 协议完全置于公共领域（Public Domain），杜绝专利私有化 | 试图确立专有技术壁垒或受限于国际电信联盟（ITU）繁重官僚标准 |
> | **[[Innovation Ecosystem\|创新生态]]塑造** | 零许可壁垒促进软硬件厂商自由进入，催生全球性通用基础设施 | 难以在商业市场上形成具有全球[[Competitiveness\|竞争力]]的独立软件与网络产业集群 |

---

## 成效评估与实证发现

> [!finding-cards] 核心实证结论
> - **确立互联网非专利开放架构底座** 卡恩与瑟夫在 [[DARPA]] 资助下将 TCP/IP 规范公开且不申请专利，使这一开放标准成功击败了 IBM 的系统网络架构（[[Network Analysis|SNA]]）及数字设备公司（DEC）的 DECNET 等商业专有协议，确立了全球互联网开放标准基座。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 39)]]
> - **先导采购培育出独立网络企业生态** DARPA 将数额巨大的开发与采购合同直接授予初创企业 BBN，大幅降低了新兴网络厂商的进入壁垒，有力刺激了战后美国在网络硬件、系统软件与信息服务领域的密集创新。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 40)]]
> - **规模化网络部署带来强正向网络外部性** 跨全美 100 多个节点的异构部署模式，加速了电子邮件（E-mail）、文件传输（FTP）及远程登录等关键应用协议的原型落地，为 1990 年代万维网（World Wide Web）在全美爆发式扩散构筑了坚实的物理与人才基座。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, pp. 39–40)]]

> [!stat-cards]- 关键实证数据
> - **1968 年 12 月** DARPA 向初创工程企业 BBN 正式签发接口信息处理机研制合同。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 39)]]
> - **> 100 个节点** 截至 1975 年已接入阿帕网的全美顶尖大学与科研机构节点总数。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 39)]]
> - **3,416 倍** 依托阿帕网奠定的全美开放互联网基础设施，1993 年 Mosaic 浏览器问世后首年超文本传输协议（HTTP）流量激增倍数。[[Argument_Fabrizio_Mowery_2005_REI|(Fabrizio & Mowery, 2005, p. 41)]]

---

## 相关条目网络

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[DARPA]] | Fact | 发起、全额注资并领导阿帕网研制与网络协议演进的核心国防研发机构。 |
> | [[General Purpose Technology]] | Concept | 阿帕网所孕育的互联网作为战后最具渗透性的通用目的技术的典型实证。 |
> | [[Cold War University]] | Concept | 深度接入阿帕网节点并参与底层通信协议研发的战后顶尖研究型高校。 |
> | [[Technology Transfer]] | Concept | DARPA 将阿帕网协议完全置于公共领域的非专利技术开放扩散机制。 |
> | [[David C. Mowery]] | Person | 深入研究 ARPANET 采购制度与开放网络架构演进的著名科技政策学者。 |
