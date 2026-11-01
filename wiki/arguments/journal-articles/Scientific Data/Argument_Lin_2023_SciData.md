---
summary: "论证构建覆盖 1.34 亿篇文献的大规模开放科学学数据湖 SciSciNet，通过规范化清洗、论文家族聚合与概率记录链接串联上游科研资助与下游专利及临床应用，并预计算颠覆性指数等核心指标，有效降低实证门槛并保障研究可复现性。"
type: argument
authors:
  - Zihang Lin
  - Yian Yin
  - Lu Liu
  - Dashun Wang
source_language: en
citation: "Lin, Z., Yin, Y., Liu, L., & Wang, D. (2023). SciSciNet: A large-scale open data lake for the science of science research. Scientific Data, 10, Article 315. https://doi.org/10.1038/s41597-023-02198-9"
year: 2023
doi: "https://doi.org/10.1038/s41597-023-02198-9"
citation_aliases:
  - "Zihang Lin et al., 2023"
  - "Zihang Lin et al. (2023)"
tags:
  - field/science-of-science
  - theme/data-infrastructure
  - theme/scientometrics
  - theme/open-science
  - theme/record-linkage
  - method/quantitative
related_concepts:
  - "[[Variable]]"
  - "[[Construct]]"
  - "[[Metascience]]"
  - "[[Data Infrastructure]]"
  - "[[Sleeping Beauty in Science]]"
  - "[[Combinatorial Novelty]]"
related_theories:
  - "[[WSB Model]]"
related_methods:
  - "[[Bibliometric Analysis]]"
  - "[[Author Name Disambiguation]]"
  - "[[Disruption Index]]"
  - "[[Combinatorial Novelty Measurement]]"
  - "[[Record Linkage]]"
related_instruments: []
related_persons:
  - "[[Dashun Wang]]"
related_facts:
  - "[[Microsoft Academic Graph]]"
  - "[[SciSciNet]]"
related_arguments: []
sources:
  - "[[sources/Lin_2023_SciData|Lin_2023_SciData]]"
status: active
subtype: journal-article
publication_type: journal-article
title: "Argument_Lin_2023_SciData"
argument_key: "Argument_Lin_2023_SciData"
argument_display_title: "SciSciNet: A large-scale open data lake for the science of science research"
argument_kind: "journal-article"
argument_related_count: 15
argument_related_level: 1
argument_related_stars: "⭐"
argument_related_color: "#dbeafe"
journal: Scientific Data
---

---

> [!question]
> 科学学（Science of Science）与[[Metascience|元科学]]的实证研究长期面临多源异构大数据分割孤立、预处理与清洗步骤极其繁复且缺乏公开透明标准、前沿测度指标计算成本高昂且重复劳动严重等结构性障碍。这使得学者难以全面追踪学科间知识网络扩散、难以建立学术产出与社会经济价值之间的完整关联，亦加剧了实证结论的可复现性危机。

> [!claim] 核心主张
> 构建大规模开放学术数据湖 [[SciSciNet]]，以规范化清洗与家族去重后的 1.34 亿篇核心论著为支柱，依托多源[[Record Linkage|记录链接]]打通上游科研资助与下游专利、临床及媒体应用网络，并全量预计算经典科学学测度指标，能够显著降低实证研究进入壁垒，消除群体性重复预处理损耗，为科学学研究提供兼具高复现性与高拓展性的公共实证数据基础设施。

> [!concept-lens] 阅读透镜
> - **对象** 全球跨学科多源科研大数据，涵盖 134,129,188 篇学术出版物、4.14 亿条学者-机构关系、15.89 亿条引文网络、上游资助与下游社会经济应用关联。
> - **张力** 商业数据库高昂使用成本及黑箱清洗规则与开源共同体对透明、可复现公共[[Data Infrastructure|数据基础设施]]迫切需求之间的张力。
> - **贡献** 开源发布包含 22 张规范化数据表的完整科学学数据湖，公布全套预处理与模糊记录匹配算法，并预计算颠覆性、新颖性、引文动力学等多维指标。

---

> [!framework-table] 理论工具箱
> | 理论工具 | 解释功能 |
> |---|---|
> | **元科学知识网络理论**<br>[[Metascience]] | 将科学发展理解为由学者、出版物、资助机制与技术应用交织而成的演化网络，为跨源数据湖实体的关系抽取与指标设计提供本体论支撑。 |
> | **WSB 引文动力学模型**<br>[[WSB Model]] | 整合指数增长、优先连接、适应度与对数正态衰老四大机制，预测单篇文献终极被引量并提供跨学科通用动力学参数。 |

> [!warrant]- 理论如何支撑论证
> 元科学知识网络视角将科学成果的生命历程扩展至“输入资助—学术生产—知识网络扩散—社会经济转化”的完整链条，要求实证数据基础设施必须突破传统期刊引文数据库的单一封闭边界；借助 WSB 模型、颠覆性指数等经同行检验的经典量化机制，数据湖的指标预计算能够直接对接科学学核心理论命题，并在宏观尺度验证数据湖清洗质量与统计有效性。

### 核心变量与操作化编码表（仅量化研究填写）

> [!index-table] 核心变量操作化定义与编码规程
> | [[Variable\|变量]]维度与分类 | [[Construct\|理论构念]]与操作化定义 | 核心教学规程、典型测量工具与纳入案例 |
> |---|---|---|
> | **学术影响力与知识扩散**<br>（Citation Impact & Diffusion） | 衡量成果在科学共同体内部的累积传播广度与长期持久度。 | 5 年引文数（C5）、10 年引文数（C10）、总被引频次，以及基于 [[WSB Model\|WSB 模型]] 拟合的即时性参数 $\mu$、衰老参数 $\sigma$ 与终极影响力预测值 $c_\infty$。 |
> | **范式革新与知识组合特征**<br>（Disruption & Combinatorial Novelty） | 衡量成果开辟全新研究轨道或实现罕见跨学科知识融合的拓扑性质。 | [[Disruption Index\|颠覆性指数]] $D \in [-1, 1]$（Wu et al., 2019）；基于 [[Combinatorial Novelty Measurement\|期刊共引对非典型度分析]] 计算的中位数 Z 分数（常规性基底）与第 10 百分位数 Z 分数（尾部新颖性）（Uzzi et al., 2013）。 |
> | **长周期延迟认可**<br>（Delayed Recognition） | 衡量成果在经历长期休眠后爆发被引的非典型演化轨迹。 | [[Sleeping Beauty in Science\|睡美人现象]] 系数 $B$ 与唤醒时间 $T$（Ke et al., 2015），结合学科外施引比例刻画知识的跨领域延迟激活。 |
> | **多源跨界应用转化**<br>（Socioeconomic Linkage） | 衡量基础科学向上游公共资金与下游产业、医疗及公共舆论的渗透程度。 | 美国国家科学基金会（National Science Foundation, NSF）与美国国立卫生研究院（National Institutes of Health, NIH）资助项目关联；USPTO/EPO 专利引用；ClinicalTrials.gov 临床试验引用；Crossref 媒体与社交媒体提及。 |
>
> **图表解读** 本表系统界定了 SciSciNet 核心数据表覆盖的理论构念、操作化指标与计算规程，为宏观科学学计算实验提供统一基准。

---

> [!method-panel] 研究设计
> | 模块 | 材料与处理方式 |
> |---|---|
> | **原始图谱过滤与家族整合**<br>[[Bibliometric Analysis]] | 以微软学术图谱（Microsoft Academic Graph, MAG）2021 年 12 月 6 日终版（2.7 亿条记录）为底库，剔除专利与无 DOI/类别记录，按预印本-正式出版等成果家族聚合主论著，重算 134,129,188 篇文献的引文分布。 |
> | **跨源多模态记录链接**<br>[[Record Linkage]] | 采用模糊字符串匹配、作者姓名与发表年份时间窗约束，将 NSF 项目报告的参考引文字符串解析并链接至 MAG 论著；通过 PMID、NCT 编号与事件 API 串接 NIH、专利、临床试验与社交媒体。 |
> | **指标规模化工程计算**<br>High-throughput Metric Computation | 依托分布式计算管道全量解算近 5000 万篇论著的颠覆性得分、共引非典型性 Z 分数、睡美人指数与引文动力学拟合参数。 |
> | **双盲交叉实证检验**<br>Benchmark Cross-Validation | 以商业数据库 Dimensions 为外部基准，从文献重合率、引文相关性、资助匹配度等维度建立混淆矩阵与相关分析，检验数据完整性与可靠性。 |

> [!sample-panel]- 样本与材料快照
> | 样本层面 | 构成 |
> |---|---|
> | **核心出版物样本** | 134,129,188 篇独立主论著（期刊论文 90,764,813 篇，图书 4,629,342 部，图书章节 3,932,366 篇，会议论文 5,123,597 篇，学位论文 5,998,509 篇，其他带 DOI 成果 20,451,018 篇）。 |
> | **实体关系网络** | 413,869,501 条学者-机构-论著关系；1,588,739,703 条论著间引文对；134,197,162 名学者（附带性别推断指标）；311 个学科领域（19 个顶级领域与 292 个子领域）。 |
> | **外部应用链接样本** | 1,309,518 条 NSF 资助关联；6,013,187 条 NIH 资助关联；38,740,313 条专利引文关联；438,220 条临床试验引用；56,441,791 条新闻与推特社交提及。 |

---

> [!logic-map]- 核心论证逻辑链
> ```mermaid
> flowchart LR
>     A["科学学数据壁垒与复现困境"] --> B["数据湖本体设计与数据清洗"]
>     B --> C["规范化 1.34 亿篇核心出版物图谱"]
>     C --> D["跨源概率记录链接打通上下游应用"]
>     C --> E["规模化预计算颠覆性与动力学指标"]
>     D --> F["外部商业基准双盲交叉验证"]
>     E --> G["稳健复现科学学里程碑规律"]
>     F --> H["确立开放低门槛高可靠实证数据基座"]
>     G --> H
> ```

---

> [!claim|step] 论证步骤一　规范化清洗与论文家族聚合确立 1.34 亿篇核心出版物高纯度图谱
> 从原始海量学术元数据中提取高保真度的分析底库，必须通过严格的出版物类别过滤、论文家族合并与全量引文网络重新赋权，消除多版本重复统计与脏数据干扰。

> [!sub-claim] 1. 过滤非学术产出并以论著家族聚合多重版本
> 微软学术图谱（MAG）原始版本包含逾 2.7 亿条记录，混杂大量未授权专利、缺少类别标识或无数字对象标识符（Digital Object Identifier, DOI）的碎片化记录。首先将文档类型标注为专利的条目剔除，同时清除缺失 DOI 且无文档类别的无效行；其次，针对学术产出普遍存在的预印本、工作论文、会议录与期刊正式发表等“论文家族（paper family）”现象，将同属于一个家族的多重记录聚合为唯一的“主论著（primary paper）”，并将撤稿论文及附属版本分流归档至详细信息表，最终提炼出包含 134,129,188 条高质量独立主论著的核心出版物库。

> [!sub-claim] 2. 闭环引文重算消除家族聚合引起的网络失真
> 在压缩和聚拢主论著后，原始引文对与被引频次会出现严重统计失真。在 1.34 亿篇核心出版物集合内部，对全部前向施引与后向引用网络实施闭合重新计算，剔除因版本合并产生的重复引文对，构建出包含 1,588,739,703 条严格位于核心文献集内部的真实引文关系对。重算前后的斯皮尔曼等级相关系数在被引频次上达到 0.991，在参考文献数上达到 0.994，既保障了对原始引文分布的忠实继承，又肃清了空引用与多版本冗余膨胀。

> [!figure]- 图 1：SciSciNet 实体关系图
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig1_Entity_Relationship_Diagram.jpg)

> [!figure]- 图 3：SciSciNet 科学出版物汇总统计分布
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig3_Summary_Statistics_Publications.jpg)

---

> [!claim|step] 论证步骤二　多源概率记录链接打通资助端到应用端的全链条证据网络
> 科学学研究需要突破文献象牙塔边界，通过开发高精度的[[Record Linkage|记录链接]]算法，能够可靠贯通基础科研向上游资金源头与向下游技术转化的外部映射。

> [!sub-claim] 1. 模糊引文字符串解析解决非结构化资助对齐瓶颈
> 针对美国国家科学基金会（National Science Foundation, NSF）资助成果长期缺乏标准 DOI 结构化记录的现实难题，开发了由“字段解析—模糊字符串比对—时间窗与作者多重硬约束”构成的记录链接管道。该方法利用正则表达式从非结构化成果描述中提取论文标题，计算候选标题与 MAG 论著标题之间的 Levenshtein 距离及比率得分，并施加论著发表年份位于资助批准年份前一年至后五年（$t-1 \le t_{\text{pub}} \le t+5$）的强时间约束，同时交叉校验第一作者姓氏与合著者匹配度。由此打通 1,309,518 条高置信度的 NSF 资助-成果链接，填补了公共开放资助匹配的空白。

> [!sub-claim] 2. 多通道串联下游专利转化、临床应用与公众舆论
> 通过利用经清洗的 PubMed 唯一标识符（PubMed Identifier, PMID）桥梁，精准绑定美国国立卫生研究院（National Institutes of Health, NIH）RePORTER 系统的 6,013,187 条项目资助记录；下游端借助 Marx & Fuegi 专利引用数据集打通美国专利商标局（USPTO）与欧洲专利局（EPO）的 38,740,313 条专利对科学文献的引用网络；同时整合 ClinicalTrials.gov 的 438,220 条临床试验应用链接，以及来自 Crossref Event API 的 5584 万条推特讨论与 59.5 万条新闻报道提及，构建起跨越基础科学、应用技术与公共领域的知识生态网络。

> [!figure]- 图 2：NSF 资助参考引文字符串与 MAG 记录匹配流程
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig2_Matching_NSF_Reference_Strings.jpg)

> [!figure]- 图 4：科学出版物与社会经济制度机构关联分布
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig4_Linking_Publications_Socioeconomic_Institutions.jpg)

---

> [!claim|step] 论证步骤三　全量预计算经典测度指标并在宏观尺度稳健复现科学学里程碑定律
> 预先解算高算力门槛的核心前沿指标不仅能够免除共同体的重复算力开销，更能通过在亿级数据规模上严谨复现文献经典实证规律，确立数据湖作为科学研究基准的信度。

> [!sub-claim] 1. 团队尺度与范式颠覆性规律的亿级全量重现
> 针对核心库中 48,581,274 篇具有完整出引与入引记录的出版物全量计算了[[Disruption Index|颠覆性指数]]（$D$）。针对团队规模与颠覆性关系的复现分析表明：随着论文合著团队规模由单人递增至数十人，论文的颠覆性百分位单调持续下降，而平均被引频次则稳步攀升；处于顶尖 5% 的高颠覆性成果在小团队中占比极高，而大团队成果进入高被引序列的概率显著更高。这在亿级规模上稳健确证了 Wu et al. (2019) 发现的“小团队开拓颠覆、大团队巩固发展”的经典结论。

> [!sub-claim] 2. 知识常规性与非典型新颖性兼备驱动科学突破
> 针对 44,143,650 篇期刊论文全量测算了基于置换引文网络的期刊共引对 $z$ 分数，提取常规性中位数与尾部新颖性（第 10 百分位数）。针对 1950 年至 2000 年间论著的四象限分析证实：同时兼具高常规性中位数与高尾部新颖性的成果，跻身同期同领域前 5% 高被引顶尖成果的概率高达 7.32%，显著超越随机基线（5%）；而双低成果的顶尖命中率仅为 3.55%，低常规高新颖成果与高常规低新颖成果的命中率分别为 6.48% 与 4.18%，在全量跨学科样本中精准再现了 Uzzi et al. (2013) 的非典型知识组合平衡法则。

> [!sub-claim] 3. 引文动力学主曲线坍缩与睡美人延迟唤醒机制
> 基于 [[WSB Model|WSB 模型]] 对物理学等长周期期刊论著进行引文动力学拟合，经验引文轨迹在经无量纲重标度后高度坍缩至标准正态累积分布主曲线上，15 年窗口的外推预测在未来 10 年与 20 年的平均绝对百分比误差（MAPE）分别稳定保持在 0.10 与 0.15 以下；针对 52,699,363 篇论文测算[[Sleeping Beauty in Science|睡美人现象]]系数，幂律拟合指数为 $\alpha = 2.40$（最小系数 $B_m = 23.59$），且高 $B$ 值成果显著依赖于跨学科外部引用的唤醒输入，在超大规模实证上呼应了 Ke et al. (2015) 的动力学发现。

> [!figure]- 图 5：SciSciNet 常用测度指标宏观分布
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig5_Commonly_Used_Metrics.jpg)

> [!figure]- 图 7：科学学经典实证规律复现验证
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig7_Validation_Measurements_Literature.jpg)

---

> [!claim|step] 论证步骤四　多维交叉验证确立开放数据湖超越商业基准的高保真覆盖质量
> 将开放数据湖与主流商业引文及资助数据库实施全方位的双盲比对，能够证实开源数据工程的稳健性，打破学术界对开源基础设施质量劣于商业专有数据库的成见。

> [!sub-claim] 1. 文献体量与引文测量高度一致且略显广阔
> 将 SciSciNet 核心文献集与顶尖商业学术数据库 Dimensions（收录 106,517,016 篇带 DOI 论文）进行 DOI 级精确对齐，结果显示 SciSciNet 收录 98,795,857 篇带 DOI 文献，二者共享多达 84,936,278 篇共同文献，占 Dimensions 总量的 79.74% 与 SciSciNet 的 85.97%；在共同匹配的 8490 万篇文献中，SciSciNet 篇均记录 16.75 次被引，略高于 Dimensions 的 14.64 次，两者篇级被引计数斯皮尔曼相关系数达到 0.946，一致性系数（Lin's concordance coefficient）高达 0.940，证明其文献覆盖广度与引文完整度处于业界第一梯队。

> [!sub-claim] 2. 基金资助项目级混淆矩阵验证外部对齐可信度
> 在 2000 年至 2020 年窗口内，比对两数据库在 NSF 与 NIH 项目-成果对上的收录情况。对于 NIH 资助，两数据库展现出近乎完全重合的收录特征，Dimensions 中 95.3% 的资助-论文对（5,356,652 对）以及 SciSciNet 中 99.7% 的记录均能在对方库中找到，项目级篇数斯皮尔曼相关系数达 0.973；对于匹配难度更高的 NSF 模糊记录链接，两库共同拥有 529,382 对资助关系，重合率达 78.9%（Dimensions）与 83.7%（SciSciNet），项目级篇数相关系数达 0.714，并且 SciSciNet 独立挖掘出 103,186 条商业数据库未收录的有效资助关联对。

> [!figure]- 图 6：SciSciNet 与 Dimensions 数据库关联交叉验证
> ![](https://img.mylikemie.icu/sources/Lin_2023_SciData/figures/Lin_2023_SciData_Fig6_Validation_Data_Linkages_Dimensions.jpg)

---

> [!finding-cards] 核心发现
> 1. **核心学术版图清洗提炼** 经过规范化过滤与家族聚合，从 MAG 2.7 亿条原始记录中提炼出包含 134,129,188 篇主论著与 15.89 亿条真实引文对的高纯度学术网络，彻底消除预印本与多版本引起的虚假引文膨胀。
> 2. **上游资助与下游应用贯通** 借助多源模糊记录链接，成功匹配 131 万条 NSF 资助关联、601 万条 NIH 资助关联、3874 万条专利引用与 43.8 万条临床试验链接，确立了基础科学向社会经济转化的立体数据网络。
> 3. **核心测度指标规模化预解算** 完成近 5000 万篇文献的颠覆性得分、非典型性 Z 分数、WSB 动力学参数与睡美人系数解算，高保真复现了小团队颠覆性优势、常规与新颖组合红利及引文普适坍缩等里程碑科学学规律。
> 4. **对标商业基准的高保真品质** 与 Dimensions 商业数据库的比对证实，两者在 8490 万篇共同文献上的引文斯皮尔曼相关系数达 0.946，NIH 资助关联重合率达 95.3% 以上，确立了开源数据湖不逊于专有商业库的基准可信度。

> [!stat-cards]- 核心数据
> - **134,129,188 篇** SciSciNet 核心主出版物数量（包含 9076 万篇期刊论文与 463 万部图书）。
> - **1,588,739,703 条** 核心文献集内部闭合引文关系对。
> - **48,581,274 篇** 全量解算颠覆性指数（Disruption score）的文献规模。
> - **44,143,650 篇** 全量解算期刊共引非典型性（Atypicality Z-scores）的期刊论文规模。
> - **0.946** SciSciNet 与 Dimensions 在 8490 万篇共有文献上的篇级引文斯皮尔曼相关系数。
> - **7.32%** 高常规性与高尾部新颖性兼备成果跻身前 5% 高被引顶尖行列的命中率（对照双低组 3.55%）。

---

> [!citation-card] 开放科研数据湖的核心使能价值
> 科学学界将科学方法应用于科学自身，帮助人们以量化方式理解科学进步的核心机制。然而，随着数据集体量日益膨胀，追踪分散来源与跨数据源关联变得极其艰难。构建跨领域开放数据湖不仅能降低新进入者的科研壁垒、减少共同体在数据预处理与基础测量上的重复损耗，更能显著提升实证论断的稳健性与可复现性，进而拓宽学术界新思想的多元性与代表性。
>
> *Overall, this data lake serves as an initial but useful resource for the field, by lowering the barrier to entry, reducing duplication of efforts in data processing and measurements, improving the robustness and replicability of empirical claims, and broadening the diversity and representation of ideas in the field.*

> [!citation-card] 论文家族聚合与引文重新配赋准则
> 数据库中每项科学出版物可能以不同实体形式呈现（例如预印本与会议论文），在微软学术图谱中表现为论文家族。为避免重复计算，所有归属于同一家族的论文均被聚合为单一主论著。撤稿论文与家族附属成果被分流记录至明细表。为维持统计口径严格一致，引文与参考文献计数在 1.34 亿篇核心主论著子集中重新计算，确保每项施引与被引关系均可在此闭合子集中溯源。
>
> *Each scientific publication in the database may be represented by different entities (e.g., preprint and conference), indicated as a paper 'family' in MAG. To avoid duplication, we aggregate all papers in the same family into one primary paper... For consistency, we recalculate the citation and reference counts within the subset of 134 M primary papers, such that each citation or reference record is also included in this subset and can be found in 'SciSciNet_PaperReferences'.*

---

> [!warning] 自述局限
> 资助-成果链接当前主要聚焦于美国的 NSF 与 NIH 项目，未完全覆盖其他国家资助体系；专利引用主要局限于 USPTO 与 EPO 专利数据库；临床试验引用主要来自 ClinicalTrials.gov，存在国家间入组与注册申报的地理异质性；基于作者姓名的性别推断模型具有内在算法局限与统计误差，在细分领域分析时须审慎校准；数据湖当前指标集聚焦于经典测度，尚待共同体进一步拓展更丰富的分析维度。

---

## 来源

- [[sources/Lin_2023_SciData|Lin_2023_SciData]]
