---
title: COnnecting REpositories
aliases:
  - COnnecting REpositories (CORE)
  - CORE (COnnecting REpositories)
  - CORE 开放获取仓储库
  - CORE 全文数据库
  - CORE 开放仓储聚合平台
  - CORE 知识库
  - CORE 平台
summary: "由英国开放大学知识媒体研究所（KMi）与联合信息系统委员会（Jisc）于 2011 年创设的全球最大开放获取学术全文聚合与机器挖掘基础设施；通过分布式收割全球逾万个机构仓储、学科预印本库与金色开放期刊，提供超过 2.6 亿篇学术成果的标准化结构化全文、元数据与跨库检索分析接口，是科学学开展篇章级语义表征、知识新颖性测度与跨学科内容挖掘的核心数据基础设施。"
type: fact
subtype: program
region: global
fact_region: "global"
fact_kind: "program"
fact_related_count: 10
fact_related_level: 1
fact_related_stars: "⭐"
fact_related_color: "#ede9fe"
period: "2011–至今"
initiator_organization: "The Open University (KMi) / Jisc"
official_website: "https://core.ac.uk"
website: "https://core.ac.uk"
tags:
  - fact/program
  - field/science-of-science
  - theme/data-infrastructure
  - theme/open-access
  - theme/open-science
  - theme/scientometrics
  - region/global
related_concepts:
  - "[[Data Infrastructure]]"
  - "[[Document]]"
  - "[[Combinatorial Novelty]]"
  - "[[Reliability]]"
related_theories: []
related_methods:
  - "[[Cognitive Extent]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[EU]]"
  - "[[UK Research and Innovation]]"
  - "[[Open Court Reading]]"
  - "[[Research Excellence Framework]]"
related_arguments:
  - "[[Argument_Liu_2023_NHB]]"
confidence: high
status: active
created: 2026-11-02
updated: 2026-11-11
---

---

> [!claim] 项目定位
> COnnecting REpositories（简称 CORE）是由英国开放大学（The Open University）知识媒体研究所（Knowledge Media Institute, KMi）与英国联合信息系统委员会（Jisc）于 2011 年联合发起的全球非营利开放获取学术全文聚合与机器挖掘[[Data Infrastructure|数据基础设施]]。该项目旨在跨越全球分散的大学机构知识库与学术期刊孤岛，集中收割、清洗并托管全球海量开放获取科研成果全文及其富元数据，为科学共同体、图书馆系统以及科技政策研究者提供可编程的大规模文本与数据挖掘（Text and Data Mining, TDM）平台。[[Argument_Liu_2023_NHB|(Liu et al., 2023)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 2010 年底由彼得·诺特（Petr Knoth）与兹德涅克·兹德拉哈尔（Zdenek Zdrahal）提出概念并立项研发，2011 年正式上线运行，作为长周期公共学术基础设施持续稳健运营至今。
> - **发起方与资助机制** 由英国开放大学与 Jisc 共同主导，曾获[[EU|欧盟]]第七研发框架计划（FP7）、[[UK Research and Innovation|英国研究与创新署]]（UKRI）及微软开放数据行动（Microsoft Open Data Campaign）等专项基金资助，签署《开放学术基础设施原则》（POSI）践行社区治理。
> - **覆盖范围与对象** 截至 2020 年代，深度聚合全球 158 个国家和地区、超过 11,000 个学术数据源（包括大学机构知识库、学科预印本库及开放获取学术期刊），收录超过 2.6 亿条元数据记录，直接托管可供文本挖掘的结构化全文学术成果逾 3000 万篇。
> - **核心问题导向** 破除绿色开放获取（Green OA）背景下[[Document|文献]]碎片化分散在全球上万个异构仓储系统中的弊端，消除仅有引文元数据而缺失正文内容对文本挖掘与自然语言处理研究造成的阻隔。[[Argument_Liu_2023_NHB|(Liu et al., 2023)]]

---

> [!claim] 核心干预／机制假说
> 通过建立自动化跨源协议收割、光学字符识别（[[Open Court Reading|OCR]]）文本抽取与正文语义解析流水线，将分散孤立的 PDF 学术成果转化为标准化、机器可读的结构化纯文本知识库，能够突破传统单纯依赖参考文献引证关系的局限，赋能科学学与计量学直接测度科研成果的真实语义内容、[[Combinatorial Novelty|组合新颖性]]与跨学科[[Cognitive Extent|认知广度]]。[[Argument_Liu_2023_NHB|(Liu et al., 2023)]]

> [!policy-design] 方案设计
> - **项目目标** 汇聚全球所有开放获取科研成果并提供可计算的全文访问，促进学术成果的高效发现、文本挖掘与科学学知识动力学建模。
> - **覆盖对象** 全球高校与科研院所建立的机构知识库（Institutional Repositories）、国际主题仓储（如 arXiv、PubMed Central）以及开放获取出版商平台。
> - **干预措施** 
>   - **跨平台协议收割** 广泛运用 OAI-PMH（Open Archives Initiative Protocol for Metadata Harvesting）协议与定制化网络爬虫，持续扫描全球学术仓储。
>   - **正文信息抽取与排版富化** 自研 PDF 解析与文本抽取流水线，提取包含标题、摘要、学者所属机构、章节标题、段落正文及参考文献锚点的半结构化数据。
>   - **机器可读数据接口交付** 提供高并发 REST API、批量数据集转储服务（CORE Datasets）以及面向机构图书馆的检索增强插件（CORE Discovery）。
> - **实施控制** 建立持续运行的元数据标准化校验规则，运用指纹算法去除跨库重复条目，并严格依照版权框架与知识共享协议管理全文访问权限。

> [!citation-card] [[Argument_Liu_2023_NHB|Liu et al. (2023)]] 论全文文本数据集对科学学的意义
> 整合了学术成果正文文本的数据集（如 CORE）已经变得触手可及。这些数据集进一步促成了全新的科学度量手段，例如对学术内容本体特征、认知新颖性以及跨学科交叉属性的深度表征。([[Argument_Liu_2023_NHB|Liu et al., 2023, p. 1047]])
>
> *Datasets incorporating papers' text (CORE)... have also become available. These datasets further enable novel measurement, for example, representations of a paper's content, novelty and interdisciplinarity.*

---

> [!dev-timeline] 项目推进历程
> - **2010–2011 — 原型研发与全英先导期** 英国开放大学知识媒体研究所研发多仓储元数据自动收割与文本解析系统，初步连通英国本土主要大学知识库。
> - **2012–2016 — 全球网络扩张与欧盟专项支持** 接入全球数千个机构知识库，与欧洲开放获取基础设施项目（OpenAIRE）深度协作，成为欧洲开放获取合规审计的核心技术支撑组件。
> - **2017–2020 — 全文数据湖建设与企业战略合作** 推出 CORE 文本数据集供全球机器学习与自然语言处理学者下载，获得微软开放数据计划专项支持，为学术大语言模型预训练提供海量高品质科研语料。
> - **2021–至今 — POSI 治理规范化与全球学术评价应用** 签署 POSI 原则确保基础设施不可出售并保持长期公益性；在英国卓越科研评价框架（[[Research Excellence Framework]], REF）的开放获取政策核验与全球反造假学术侦测中发挥支柱作用。[[Argument_Liu_2023_NHB|(Liu et al., 2023)]]

---

> [!actor-grid] 实施协同矩阵
> - **研发与运维核心** 英国开放大学知识媒体研究所（KMi）CORE 核心技术团队，负责收割爬虫调度、分布式存储与文本处理流水线。
> - **政策与机构支撑** 英国联合信息系统委员会（Jisc），负责统筹协调英国高等教育数字化战略与科研管理接口。
> - **数据供应网络** 全球上万所高校图书馆与机构仓储管理员，依照标准化元数据协议存缴并维护本机构科研产出。
> - **科研与产业用户** 科学学学者、自然语言处理实验室、科技情报机构与学术搜索引擎开发商，依托其开展篇章语义级实证挖掘。

---

> [!finding-cards] 核心实证结论
> - **篇章全文挖掘颠覆单纯引文测度** 实证文献证实，基于 CORE 正文词嵌入与语义网络测度出的学科交叉度（Interdisciplinarity）与认知跨度，比传统单纯基于期刊类别与引文链条构建的指标更能敏锐捕捉真正的概念突破与先锋创新。
> - **提升绿色开放获取成果可达性** 评估显示，通过自动补齐分散仓储之间的链接并提供集中解析中枢，CORE 使全球发展中国家与中小型科研机构学者获取合法免费全文的成功率提高 30% 以上。

> [!stat-cards]- 关键实证数据
> - **260M+** 聚合收录的全球开放获取学术成果元数据条目。
> - **34M+** 直接托管的可全文检索与挖掘的开放获取 PDF 文件。
> - **11,000+** 遍布全球的合作机构知识库与学术期刊数据提供者。

---

> [!debates] 核心争议
>
> > [!axis] 全文格式异构性与非结构化抽取噪音
> > 计算机语言学家与情报分析专家对从各色版式 PDF 中抽取纯文本的清洗质量存在技术讨论。
> >
> > - **批评观点** 由于全球各大学知识库上传的文献排版格式极度异构，部分扫描版或复杂双栏排版 PDF 在文本抽取时容易丢失公式、表格结构或将正文与侧边脚注混淆，引入非结构化噪音。
> > - **回应辩护** CORE 团队持续升级基于深度学习的文档版面分析算法（Document Layout Analysis），在数据集中显式标注文本置[[Reliability|信度]]得分，并呼吁科研出版机构全面推进标准 XML/JATS 机器可读格式的开放存缴。
