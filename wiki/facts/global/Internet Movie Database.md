---
title: Internet Movie Database
aliases:
  - IMDb
  - 互联网电影资料库
summary: "由科尔·尼达姆于1990年创立、现为亚马逊旗下的全球最具权威性的电影、电视与创意视听作品综合数据库；收录跨越一个多世纪的千万级作品元数据、演员导演完整演职年表以及数以亿计的大众与专业用户评分；其单片评分服从均值为7.1的标准正态分布，在计算文化学、创意产业经济学与科学学跨界实证中，被确立为度量影视导演职业生涯产出质量与艺术连胜的基准量化数据源（Liu et al., 2018; Wasserman et al., 2015）。"
type: fact
subtype: program
region: "global"
fact_region: "global"
fact_kind: "program"
fact_related_count: 9
fact_related_level: 0
fact_related_stars: "☆"
fact_related_color: "#ede9fe"
period: "1990–至今"
initiator_organization: "Amazon"
official_website: "https://www.imdb.com"
tags:
  - fact/program
  - theme/cultural-analytics
  - theme/creative-career
  - theme/database
  - theme/science-of-science
related_concepts:
  - "[[Creativity]]"
  - "[[Hot Streak]]"
  - "[[Data Infrastructure]]"
  - "[[Collective Intelligence]]"
  - "[[Homophily]]"
related_theories: []
related_methods:
  - "[[Sample Size Determination]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[National Academy of Sciences]]"
  - "[[Web of Science]]"
related_arguments:
  - "[[Argument_Liu_2018_Nature]]"
confidence: high
status: active
created: 2026-11-03
updated: 2026-11-11
---

---

> [!claim] 项目定位
> 互联网电影资料库（Internet Movie Database，IMDb）是由英国计算机程序员科尔·尼达姆（Col Needham）于 1990 年创立、1998 年被亚马逊公司收购运营的全球规模最大、历史最悠久的影视视听作品与演职人员在线数据库。该数据库系统收录了自电影诞生以来全球数百万部影视作品的演职人员名录、剧情制作档案以及基于贝叶斯算法的大众与影评人综合评分。在计算文化学、创意经济学与宏观科学学跨界实证中，IMDb 被确立为评估电影导演职业生涯作品时序质量、检验[[Creativity|创造力]]生命周期与成团连胜动力学（[[Hot Streak]]）的标准实证[[Data Infrastructure|数据基础设施]]。[[Argument_Liu_2018_Nature|(Liu et al., 2018, p. 396)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 1990 年 10 月起源于 Usenet 新闻组网络脚本集合；1993 年建立万维网网站，1998 年由亚马逊收购商业化运作，常态化持续运营至今。
> - **发起方与资助机制** 由科尔·尼达姆及其志愿者团队创立，现由亚马逊公司（Amazon.com）通过在线广告、会员订阅（IMDbPro）与行业数据授权模式持续资助与运营。
> - **覆盖范围与对象** 截至 2020 年代收录超过 1,000 万部影视与娱乐作品、逾 1,100 万名演职从业人员记录，拥有数以亿计的注册用户评分。
> - **核心问题导向** 攻克早期电影史料与演职信息碎片化、视听艺术成果质量缺乏公认客观标尺的困境，通过大众智慧聚合与算法平滑，构建兼具专业深度与大众口碑的统一量化评价体系。

---

> [!claim] 核心机制假说
> 影视作品评分在经过贝叶斯加权平滑后服从标准正态分布，能够克服商业票房的短期通胀与院线排片扭曲，作为衡量导演个体创造力输出质量的稳健量化代理。[[Argument_Liu_2018_Nature|(Liu et al., 2018, p. 396)]]

> [!policy-design] 方案设计
> - **项目目标** 建立全人类影视艺术创作的百科全书式档案库，提供公允可比的作品影响力与艺术水准度量。
> - **覆盖对象** 全球自 1890 年代无声电影至今的所有院线电影、电视长剧、纪录片、短片及网络流媒体视听作品。
> - **核心干预措施** 建立标准演职人员编号与作品编号系统，记录导演终身完整执导时序；引入加权贝叶斯评分公式计算 1 至 10 分的综合 IMDb 评分（IMDb Rating），过滤刷分噪声。
> - **实施控制机制** 实施严格的用户身份验证与极端评分惩罚权重，结合 IMDbPro 为电影工业界提供权威的星级与行业指数（STARmeter / MOVIEmeter）。

> [!citation-card] IMDb 评分作为影视创造力质量的量化代理
> 在对人类创造力展开的大规模跨界实证中，研究团队采集了 IMDb 数据库收录的 6,233 位电影导演的职业生涯档案，以单部影片的 IMDb 评分作为作品优异程度的标准度量。实证检验显示，该评分服从均值为 7.1、标准差为 1.2 的标准正态分布，并与各类行业获奖与票房指标高度正相关。[[Argument_Liu_2018_Nature|(Liu et al., 2018, p. 396, Extended Data Fig. 2b)]]
>
> *D2 contains profiles of 6,233 film directors recorded in the IMDB database, each career being represented by the sequence of films directed by the individual. As metrics that quantify the impact of a film correlate closely with each other, here we use the IMDB rating to measure the goodness of a film.*

---

> [!dev-timeline] 项目推进历程
> - **1990 — Usenet 爱好者数据库起步** 科尔·尼达姆发布可检索的电影演职人员列表脚本。
> - **1993 — 万维网先驱上线** 成为互联网历史上最早的视听作品超文本数据库之一。
> - **1998 — 亚马逊并购与工业化** 亚马逊收购 IMDb，推动其向影视产业基础设施与商业数据中心转型升级。
> - **2015 — 跨指标有效性确证** 瓦瑟曼等在《[[National Academy of Sciences|美国国家科学院]]院刊》（PNAS）证实 IMDb 评分与影评人专业评分、奥斯卡奖项及长期文化影响力高度相关（Wasserman et al., 2015）。
> - **2018 — 艺术文化爆发期实证基座** 在《自然》研究中作为 D2 数据集，支撑 6,233 位导演长周期职业连胜规律的发现（[[Argument_Liu_2018_Nature|Liu et al., 2018]]）。

---

> [!contrast-table] 创造力产出质量量化数据源对比辨析
> | 维度 | 互联网电影资料库（[[Internet Movie Database\|IMDb]]） | 艺术拍卖落槌价（Artprice） | 科学文献十年被引（$C_{10}$ / [[Web of Science\|WoS]]） |
> |---|---|---|---|
> | **对应创意领域** | 影视编导与视听文化艺术 | 纯美术绘画与造型雕塑艺术 | 自然科学与跨学科前沿科学研究 |
> | **核心评价标尺** | 1 至 10 分用户加权评分（IMDb Rating） | 公开拍卖市场落槌成交价（$\ln(\text{price})$） | 发表 10 年后的累积被引频次（$\ln(C_{10})$） |
> | **经验统计分布** | 标准正态分布（$\mu = 7.1, \sigma = 1.2$） | 重尾对数正态分布（$\mu = 7.9, \sigma = 1.5$） | 重尾对数正态分布（$\mu = 2.3, \sigma = 1.3$） |
> | **评价机制特征** | 大众影迷与专业受众的综合审美口碑 | 艺术市场二级交易的资本与学术双重认证 | 科学共同体同行后继引证与知识继承拓扑 |

---

> [!debates] 学术争议
>
> > [!axis] 大众智慧集体评分 vs 粉丝刷分与极端评价偏倚
> > 开放用户评分是否能够代表电影作品的真实艺术水准？
> >
> > - **[[Collective Intelligence|集体智慧]]支持论** 大样本用户评分通过贝叶斯加权有效抹平了个别影评人的个人偏好，其长程评分已被证实高度吻合经典电影的留存度。
> > - **文化批评质疑论** 商业大片、流行流行文化衍生品极易引发粉丝控评或黑粉互踩，导致初期评分存在显著的极化失真。

> [!warning] 数据局限
> 早期无声电影由于历史胶片遗失与当代观众观影较少，评分[[Sample Size Determination|样本量]]相对稀疏；个别小众艺术电影由于受众群体[[Homophily|同质性]]高，评分均值可能存在向上选择性偏倚。

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Liu_2018_Nature|Liu et al. (2018)]] — 利用 IMDb 数据库追踪 6,233 位导演的职业时序，证实影视创作领域存在平均持续 5.2 年的爆发期，且最强与次强影片紧密相连。
