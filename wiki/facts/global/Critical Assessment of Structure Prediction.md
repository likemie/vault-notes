---
title: Critical Assessment of Structure Prediction
aliases:
  - 蛋白质结构预测关键评估
  - CASP
  - 国际蛋白质结构预测竞赛
  - 蛋白质结构盲测评估
summary: "自1994年起每两年举办一次的全球蛋白质三维结构预测盲测评估竞赛与基准检验平台；由约翰·莫尔特（John Moult）等发起，采用预测者在结构未公开前提下进行纯盲测的严密黄金标准，通过刚性客观指标衡量算法进步，成功打破了各学术团队自卖自夸的评估陷阱，并成为检验与见证AlphaFold实现革命性蛋白质折叠突破的决定性竞技场。"
type: fact
subtype: program
region: global
fact_region: "global"
fact_kind: "program"
fact_related_count: 11
fact_related_level: 1
fact_related_stars: "⭐"
fact_related_color: "#ede9fe"
period: "1994至今"
initiator_organization: "University of Maryland / CASP Organizing Committee"
tags:
  - org/consortium
  - theme/technology-innovation
  - theme/science-policy
  - field/metascience
  - region/global
related_concepts:
  - "[[Paradigm]]"
  - "[[Big Science]]"
  - "[[Focused Research Organization]]"
  - "[[Data Infrastructure]]"
  - "[[Industrial Commons]]"
  - "[[Metascience]]"
related_theories: []
related_methods: []
related_instruments: []
related_persons:
  - "[[Michael Kratsios]]"
related_facts:
  - "[[National Institutes of Health]]"
  - "[[National Science Foundation]]"
  - "[[Protein Data Bank]]"
related_arguments:
  - "[[Argument_Kratsios_2026_OSTP]]"
confidence: high
status: active
created: 2026-10-07
updated: 2026-10-07
---

# Critical Assessment of Structure Prediction

---

## 项目背景与立项契机

> [!claim] 项目定位
> **蛋白质结构预测关键评估（Critical Assessment of Protein Structure Prediction, CASP）** 是全球结构生物学与计算生物学领域最具公信力的两年一度盲测评估项目与基准检验平台，于 1994 年由马里兰大学约翰·莫尔特（John Moult）与克日什托夫·菲德利斯（Krzysztof Fidelis）等学者正式创设。CASP 通过纯盲测实验设计与严密的量化打分标准，客观裁决全球各研究团队从一维氨基酸序列预测三维空间构型的计算精度，彻底终结了计算生物学界长期存在的“自测自夸”自娱自乐困境。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, p. 22)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 1994 年启动首届（CASP1），每两年举办一届，迄今已连续举办十余届（包括 CASP13/14/15/16 等关键里程碑）。
> - **发起方与资助机制** 由国际 CASP 组织委员会独立运营，主要依托[[National Institutes of Health|美国国立卫生研究院]]（NIH/NIGMS）及[[National Science Foundation|美国国家科学基金会]]（NSF）持续学术资助支持。
> - **覆盖范围与对象** 汇聚全球所有顶尖计算生物学课题组、跨国科技巨头前沿实验室（如 Google DeepMind、Meta AI）及结构生物学实验团队。
> - **核心问题导向** 破除各团队在各自私有数据集上宣称高精度的学术泡沫，建立面向未解结构的统一、无偏见且具有刚性物理约束的全球基准竞技场。

---

## 方案设计与运行机制

> [!claim] 核心机制假说
> **刚性盲测竞赛打破学术避险与指标造假假说** 唯有剥离预测者对已公开答案的事后拟合（Overfitting），在结构生物学家即将实验测出但尚未公开发布的真实验证靶点上进行前瞻性盲测，才能逼出真实算法极限，吸引颠覆性工程团队入场并在短周期内促成[[Paradigm|范式]]级质的突破。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, p. 22)]]

> [!policy-design]- 严密的双盲测试方案与规程
> - **实验团队协同靶点征集** 实验晶体学与冷冻电镜实验室在解析出全新蛋白质三维结构后、公开或提交 [[Protein Data Bank|PDB]] 数据库之前，将氨基酸序列作为“未知盲测靶点（Targets）”交由 CASP 组委会。
> - **限期前瞻性盲测提交** 全球参赛团队在几周的封闭时间窗口内，仅凭氨基酸序列自主运行计算模型，提交预测的原子空间坐标文件。
> - **独立评估专家组与 GDT-TS 打分** 盲测截止后，实验实验室公开真实结构，独立评估委员会采用全局距离检验总分（Global Distance Test - Total Score, GDT-TS，满分 100）等严苛几何指标对所有参赛模型进行机器全自动打分排名。

> [!citation-card] CASP 盲测科学哲学宣言
> CASP 证明了在科学中确立客观、不容妥协的真实测试标准所蕴含的巨大变革力量。当我们消除了事后修饰与主观辩解的空间，真正的颠覆性突破便会在客观度量面前无可辩驳地显现。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, p. 22)]]
>
> *CASP provides a rigorous, blind testing mechanism for assessing the state of the art in protein structure modeling, establishing gold-standard benchmarks that drive the entire computational biology community forward.*

---

## 推进历程与阶段演进

> [!dev-timeline] CASP 关键里程碑历程
> - **1994 — CASP1 创设与盲测[[Paradigm|范式]]确立** 首次证明计算生物学界宣称的算法在盲测面前误差巨大，奠定了“无盲测不采信”的严密科学基准。
> - **1996–2016 — 缓慢爬坡期与自由建模瓶颈** 二十年间全球团队在同源建模上稳步进步，但在缺乏已知模板的从头预测（*ab initio* / Free Modeling）中 GDT-TS 分数长期停滞在 30–40 分的低效区间。
> - **2018 — CASP13 与 AlphaFold 首度惊艳亮相** DeepMind 团队携初代 AlphaFold 参赛，在自由建模类别中以显著优势碾压传统物理化学方法，引发全球关注。
> - **2020 — CASP14 与蛋白质折叠半世纪难题的历史性攻克** AlphaFold 2 在绝大多数靶点上取得了中位数超过 90 分的 GDT-TS 成绩，达到与 X 射线晶体衍射和冷冻电镜实验误差相当的原子级精度，宣告蛋白质折叠空间预测问题基本解决。
> - **2025–2026 — 白宫国家科技战略总结其为中等规模工程科学典范** [[Michael Kratsios|迈克尔·克拉齐奥斯]]（[[Argument_Kratsios_2026_OSTP|Kratsios, 2026]]）报告第二章将 CASP 盲测竞赛与 [[Protein Data Bank|PDB]] 数据公地共同确立为中等规模工程科学与跨学科颠覆性突破的制度范本。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, p. 22)]]

---

## 实施架构与治理网络

> [!actor-grid] 全球盲测协同网络
> - **CASP 国际组织委员会** 负责整体规划、靶点分类规则研制、会议组织及评估委员会遴选。
> - **实验结构提供实验室网络** 遍布全球的同步辐射光源、冷冻电镜中心与大学晶体学实验室，自愿延后论文发布以配合盲测周期。
> - **独立评估专家组（Independent Assessors）** 由未参与预测竞赛的资深资历结构生物学家组成，主持匿名盲审与分类评分。
> - **全球跨界参赛阵营** 包括学术计算生物学组、计算物理学家、AI 初创团队与大型工业科技实验室。

---

## 影响与体系成效

> [!indicators]- 影响力与机制成效维度
> - **终结半世纪重[[Big Science|大科学]]挑战** 为长达 50 年的安芬森假说（Anfinsen's Dogma）计算实现提供了无可争议的历史性裁判席。
> - **跨学科人才与资本虹吸** 客观可度量的明确黄金标准，吸引了顶级计算机科学家与风险资本将资源集中投向结构生物学与 AI for Science 赛道。
> - **重塑科学竞赛标准[[Paradigm|范式]]** 为 RNA 结构预测（RNA-Puzzles）、蛋白质-配体对接（D3R Grand Challenge）等其他前沿领域树立了标准的盲测评估模板。

> [!stat-cards]- 核心规模数据
> - **历史评估靶点数** 超 1,500 个真实前沿未知蛋白质靶点。
> - **全球参赛队伍规模** 每届吸引来自数十个国家的 100–200 支顶尖专业团队。
> - **突破性历史精度** 将盲测预测中位数精度从早期的不足 40 分提升至 AlphaFold 2 的 90+ 分（实验原子级精度）。

---

## 争议、批评与反思

> [!debates] 盲测竞赛机制学术争鸣
>
> > [!axis] 工业工程巨头资源碾压 vs 大学小课题组生存空间
> > 探讨在 CASP 演进为高度工程化、算力密集型竞技场后，传统大学单 PI 课题组是否丧失了竞争公平性。
> >
> > - **工程密集优势派（[[Argument_Kratsios_2026_OSTP|Kratsios, 2026]]）** 指出科学已从个人手工作坊迈向高度集成的中等规模工程，必须承认企业跨学科工程团队在解决结构性大问题上的组织优势，并通过 [[Focused Research Organization|FRO]] 等新[[Paradigm|范式]]赋能公共学术界。[[Argument_Kratsios_2026_OSTP|(Kratsios, 2026, p. 22)]]
> > - **传统学术多元批评** 担忧单一盲测排名导向可能压制对微观物理机理的深入探讨，导致科研资源过度向追求分数的单一算法堆叠倾斜。

---

## 条目关联网络

> [!entry-map]
>
> | 条目 | 类型 | 关联维度与贡献 |
> |:---|:---|:---|
> | [[Protein Data Bank]] | Fact | CASP 盲测靶点实验结构最终收录的国际公共[[Data Infrastructure\|数据基础设施]]。 |
> | [[Focused Research Organization]] | Concept | 旨在复刻 CASP 与 DeepMind 攻关模式、填补大学工程科学空白的新型组织。 |
> | [[Industrial Commons]] | Concept | CASP 与 PDB 共同构成的生物信息学公共基准公地。 |
> | [[Metascience]] | Concept | 将盲测基准竞赛作为克服学术自测偏差的元科学机制研究。 |
> | [[Argument_Kratsios_2026_OSTP\|Kratsios (2026)]] | Argument | 白宫 2026 年科技报告对 CASP 作为中等规模工程科学突破典范的系统论述。 |

---

