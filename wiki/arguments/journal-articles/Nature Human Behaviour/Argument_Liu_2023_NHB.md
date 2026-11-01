---
summary: "系统梳理科学学（Science of Science）的大数据基础设施、核心测度构念与实证研究方法谱系，构建涵盖经验规律、生成机制模型、机器学习与因果推断（匹配、固定效应、准实验、随机对照试验）的方法学全景体系，为指导科技政策与理解科学系统运行规律提供方法论支撑。"
type: argument
authors:
  - "Liu, L."
  - "Jones, B. F."
  - "Uzzi, B."
  - "Wang, D."
source_language: en
citation: "Liu, L., Jones, B. F., Uzzi, B., & Wang, D. (2023). Data, measurement and empirical methods in the science of science. Nature Human Behaviour, 7(7), 1046–1058. https://doi.org/10.1038/s41562-023-01562-4"
year: 2023
doi: "https://doi.org/10.1038/s41562-023-01562-4"
citation_aliases:
  - "Liu et al., 2023"
  - "Liu et al. (2023)"
isbn: ""
tags:
  - theme/science-of-science
  - theme/science-policy
  - method/quantitative
  - method/causal-inference
  - method/machine-learning
related_concepts:
  - "[[Metascience]]"
  - "[[Construct Validity]]"
  - "[[Scientific Productivity]]"
  - "[[Citation Aging]]"
  - "[[Goodhart's Law]]"
related_theories:
  - "[[Preferential Attachment in Academia]]"
  - "[[Bianconi-Barabási Model]]"
related_methods:
  - "[[Difference-in-Differences]]"
  - "[[Regression Discontinuity Design]]"
  - "[[Matching]]"
  - "[[Propensity Score Matching]]"
  - "[[Fixed-Effect Model]]"
  - "[[Randomised Controlled Trials]]"
related_instruments: []
related_persons:
  - "[[Lu Liu]]"
  - "[[Benjamin F. Jones]]"
  - "[[Brian Uzzi]]"
  - "[[Dashun Wang]]"
related_facts:
  - "[[SciSciNet]]"
related_arguments: []
sources:
  - "[[sources/Liu_2023_NHB/Liu_2023_NHB|Liu_2023_NHB]]"
part_of:
status: active
created: 2026-11-02
updated: 2026-11-02
subtype: journal-article
publication_type: journal-article
title: "Argument_Liu_2023_NHB"
argument_key: "Argument_Liu_2023_NHB"
argument_display_title: "Data, measurement and empirical methods in the science of science"
argument_kind: "journal-article"
argument_related_count: 18
argument_related_level: 1
argument_related_stars: "⭐"
argument_related_color: "#dbeafe"
journal: "Nature Human Behaviour"
book_title: ""
publication_place: ""
publisher: "Nature Publishing Group"
issuing_organization: ""
---

---

> [!question]
> 科学学（Science of Science, SciSci）如何整合多源大数据、微观测量构念与跨学科实证方法，打破不同研究范式之间的隔阂，系统刻画科学系统的内在运行机制并为科技政策评估提供严谨证据？

> [!claim] 核心主张
> 科学学正由传统单一文献计量向整合上游研发资助与下游社会经济产出的多源大数据演进；通过系统贯通描述性规律、微观机制模型、高维机器学习表征以及因果推断框架（匹配、固定效应、准实验与随机对照试验），科学学确立了兼备模式发现、机制解释与政策因果评估效力的方法学全景体系。

> [!concept-lens] 阅读透镜
> - **对象** 跨越多个学科门类的大规模科技文献、资助拨款、科研人员生涯发展轨迹、学术团队协作网络、专利发明以及下游政策与临床转化大数据。
> - **张力** 描述统计与机器学习长于发掘关联并实现高精度预测，缺乏因果识别力与模型可解释性；计量经济学因果推断方法（如双重差分、工具变量、断点回归）长于评估政策净效应，依赖外生随机冲击且受制于局部平均处理效应的外推边界。
> - **贡献** 构建了涵盖数据源（Data）、测量构念（Measurement）与实证方法（Empirical Methods）的三维分析体系，厘清不同实证进路的适用场景与构念效度风险，为指导科技政策制定与拓展科研人员工具箱提供了系统指南。

---

> [!framework-table] 理论工具箱
> | 理论工具 | 解释功能 |
> |----------|----------|
> | **[[Preferential Attachment in Academia\|学术界优先连接理论]]**<br>[[Preferential Attachment in Academia]] | 阐释引文网络中的累积优势机制，前期获引较多的文献具有更高概率吸纳后续引文，构成科学系统马太效应的生成基底。 |
> | **[[Bianconi-Barabási Model\|比安科尼-巴拉巴西适应度模型]]**<br>[[Bianconi-Barabási Model]] | 在优先连接机制中引入内生适应度参数，解释优质创新成果如何在时间网络中突破后发劣势实现超越。 |
> | **[[Citation Aging\|引文老化构念]]**<br>[[Citation Aging]] | 刻画科学知识在发表后注意力达到峰值并随后衰减的生命周期规律，指出带有指数截断的对数正态函数能够有效捕获这一动力学历程。 |
> | **[[Construct Validity\|构念效度理论]]**<br>[[Construct Validity]] | 审视量化指标与被测理论属性之间的对应程度，防范因指标异化诱发的古德哈特定律（[[Goodhart's Law]]）与行为扭曲。 |

> [!warrant]- 理论如何支撑论证
> 优先连接理论与适应度模型揭示了科研产出分布高度偏态的生成机理，引文老化模型刻画了科研注意力的时间衰减函数，构念效度理论则为反思各类文献计量指标的局限性提供了认识论依据。这些理论工具共同架设起从宏观引文网络数据通往微观因果解释与政策评估的推论桥梁。

---

> [!method-panel] 研究设计
> | 模块 | 材料与处理方式 |
> |------|----------------|
> | **多源记录链接与基础设施整合**<br>Record Linkage and Big Data Integration | 梳理学术出版物（Web of Science、Scopus、OpenAlex）、全文语料（CORE）、资助数据库（NIH RePORTER、NSF）、专利及临床试验，评析学者姓名消歧与多源实体链接策略。 |
> | **微观构念效度评估**<br>Construct Validity Analysis | 剖析引文指标、学者个人生涯指标（如 $h$ 指数）、团队规模与多样性、机构产出等关键构念的操作化定义及其测度边界。 |
> | **生成机制建模分析**<br>Generative Mechanistic Modeling | 考察由微观互动规则推导宏观统计分布的数学模型，包括引文动力学模型、合作网络演化模型与科研失败动力学模型。 |
> | **高维机器学习预测分析**<br>Machine Learning Predictive Modeling | 评估自然语言处理（NLP）词向量嵌入（Word2vec Skip-gram）与深度神经网络在预测前沿知识发现、材料属性及研究可复现性中的应用潜力。 |
> | **准实验与实验因果推断框架**<br>Causal Inference Framework | 比较倾向得分匹配、高维固定效应、双重差分法（DID）、工具变量法（IV）、断点回归设计（RDD）以及随机对照试验（RCT）的因果识别假设与政策评估效能。 |

> [!sample-panel]- 样本与材料快照
> | 样本层面 | 构成 |
> |----------|------|
> | **数据覆盖** | 覆盖全球亿级科技文献、数十万项科研资助资助记录、跨学科数百万学者职业生涯追踪序列以及数千万项发明专利与临床试验。 |
> | **材料语境** | 重点关注主流文献数据库对非英语文献的覆盖不足、未发表负结果引发的抽屉效应，以及商业数据库对学术资源获取造成的结构性分层。 |

---

> [!logic-map]- 核心论证逻辑链
> ```mermaid
> flowchart LR
>     A["数据基础设施扩展\n(资助-出版-下游转化)"] --> B["测度构念与效度审视\n(引文/学者/团队/机构)"]
>     B --> C["实证方法谱系分流"]
>     C --> D["描述性与预测性进路\n(经验规律/机制模型/机器学习)"]
>     C --> E["因果推断进路\n(匹配/固定效应/准实验/RCT)"]
>     D --> F["揭示客观模式与预测前沿"]
>     E --> G["检验因果效应与指导科技政策"]
>     F --> H["科学学全景方法论体系"]
>     G --> H
> ```

---

> [!claim|step] 论证步骤一　科学学数据基础设施从单一出版物引文向上下游多源记录链接扩展
> 科学学研究的数据源已突破单纯依赖科技文献与学术期刊的狭窄边界，形成了向上链接公共研发资助、向下贯通专利与社会经济效益的多源立体数据基础设施。

> [!sub-claim] 1. 数据多源化打破学术出版物孤岛并延伸至资助端与应用端

早期科学学主要依赖手工统计或针对特定领域的问卷访谈，样本规模与分析维度严重受限。随着大规模数字化基础设施的确立，出版物数据库（Web of Science、Scopus、OpenAlex、PubMed、Dimensions 等）实现了对跨学科科研产出的全量覆盖。

现代科学学数据进一步向上游资助端延伸，链接美国国家科学基金会（National Science Foundation, NSF）与美国国立卫生研究院（National Institutes of Health, NIH）等机构的资助记录，系统追踪科研经费对科学产出率与公共投资回报的驱动机制。同时，数据向下游应用端扩展，链接专利数据库、药品临床试验数据、政策文本与替代计量指标（Altmetrics），为测度科学发现的实际应用价值与技术转化周期提供了量化依据。此外，结合学者的履历档案、师承渊源与大学课程教学大纲，科研人才的培养演进与社会流动网络得以清晰呈现。

> [!figure]- 图1：科学学数据与关联图谱
> ![](https://img.mylikemie.icu/sources/Liu_2023_NHB/figures/Liu_2023_NHB_Fig1_Science_of_Science_Data_and_Linkages.jpg)

> [!sub-claim] 2. 街灯效应、抽屉效应与非英语覆盖偏差构成数据层面的内在局限

尽管科学学数据规模呈指数级增长，其本身仍存在系统性选择偏差。既有数据库以正式发表文献为主，容易诱导研究者聚焦于易于发表的议题，产生“街灯效应”（Streetlight Effect）；具有探索性但得到阴性结果的研究极少发表，引发严重的“抽屉效应”（File Drawer Problem）。此外，主流文献数据库中超过 90% 的出版物为英语文献，对非英语语种期刊与区域性研究的覆盖严重不足；商业数据库的昂贵订阅费用也加剧了学术资源获取的不平等。

---

> [!claim|step] 论证步骤二　微观测度构念必须接受构念效度审视与反异化批判
> 将引文指标、学者产出、团队协作与机构表现操作化为具体量化指标时，必须严格审视构念效度，防范指标替代专家判断导致的系统性评价扭曲。

> [!sub-claim] 1. 引文测度必须区分学术影响力、负面反驳与知识流动示踪

被引频次是衡量学术影响力的常用代理指标。通过PageRank算法或特征因子（Eigenfactor）等网络指标，引文网络能够赋权不同来源引文的重要性。引文本身存在强烈的异质性，难以直接等同于知识价值：引用行为常受到学术共同体声誉结构与权力分布的调节，并包含负面批评或反驳性引用。通过结合全文自然语言处理，区分引文语境（Citation Context）与正负面情感极性，引文网络能更真实地还原跨领域、跨机构与跨国界的知识流动轨迹。

> [!sub-claim] 2. 个体与团队指标面临劳动贡献隐匿与评价机制异化挑战

在学者个人层面，由乔治·赫希（Jorge E. Hirsch）提出的 $h$ 指数（$h$-Index）综合了发文量与单篇获引率，但其衍生指标依然受制于同名学者消歧误差、学科基准差异以及对教学、同行评议与公共服务等非发表贡献的遮蔽。

在团队层面，科学研究呈现出由独著模式向大规模团队协作转变的历史趋势。虽然合作团队规模直接体现于署名名单，但名单隐藏了微观层面的分工差异；《旧金山科研评估宣言》（San Francisco Declaration on Research Assessment, DORA）与贡献者角色分类法（Contributor Roles Taxonomy, CRediT）等倡议正是为应对个体劳动被合著名单吞没而做出的制度努力。

> [!sub-claim] 3. 古德哈特定律揭示指标替代专家判断时的系统性风险

当某个评价指标被用作绩效考核与资源配置的目标时，受试对象会主动迎合指标计算规则，导致该指标丧失原有的衡量效力。这一古德哈特定律现象在学术界体现为追求引用指标、战略性互引与切分发表等异化行为。定量测度必须与定性同行评议互补结合，防范指标对学术生态的单向塑造。

---

> [!claim|step] 论证步骤三　描述规律、生成机制模型与机器学习共同构成前瞻预测工具箱
> 描述性统计规律确立了宏观经验基准，生成机制模型刻画了微观交互规则，机器学习模型则实现了跨领域高维特征表征与知识发现预测。

> [!sub-claim] 1. 经验统计规律确立宏观标度与反直觉经验事实

对海量科技文献的统计分析确立了一系列经典经验规律：学者产出与引文分布普遍呈现重尾分布；颠覆性突破在学者发表序列中遵循随机影响法则（Random Impact Rule）；大团队长于深化既有概念，小团队长于颠覆既有范式。这些经验规律为检验既有理论与构建新型数理模型奠定了坚实的经验基底。

> [!sub-claim] 2. 生成机制模型通过微观动力学方程推导宏观演化态

机制模型旨在运用极简的数学方程刻画底层数据生成过程。在引文动力学研究中，研究者将累积优势（优先连接）与个体适应度（Fitness）参数相结合，并引入刻画衰减规律的引文老化项，成功推导出与真实演化高度吻合的引文分布曲线。这类模型进一步拓展至科研团队组建、主题演化以及科研早期挫折对后续职业韧性的驱动机制模拟中。

> [!sub-claim] 3. 深度学习与高维词向量嵌入前瞻预测前沿知识突破

机器学习进路超越了传统的假设检验框架，通过在高维特征空间中优化拟合优度实现前瞻预测。利用 Word2vec Skip-gram 等深度神经网络，研究者能够从材料科学数百万篇学术摘要的无结构文本中学习词汇与语境的高维嵌入向量，仅凭文献中用词的关联模式即成功预测出数年后才被实验证实的全新热电材料物性。高维嵌入表征还在预测跨学科成果可复现性、期刊跨界影响力与机构知识重组潜力方面展现出广阔前景。

> [!figure]- 图2：基于机器学习预测知识发现的示例（Word2vec 模型）
> ![](https://img.mylikemie.icu/sources/Liu_2023_NHB/figures/Liu_2023_NHB_Fig2_Prediction_with_Machine_Learning.jpg)

---

> [!claim|step] 论证步骤四　因果推断框架通过外生变异与反事实设计支持科技政策评估
> 科技政策制定迫切需要评估各类干预手段的因果效应；匹配方法、固定效应、准实验设计与随机对照试验共同构成了克服内生性偏误的因果识别阶梯。

> [!sub-claim] 1. 匹配策略与面板固定效应有效吸收可观测与时不变混杂因素

观察性数据中的相关性往往受到未观测混杂因素的干扰。精确匹配、粗化精确匹配（Coarsened Exact Matching, CEM）以及倾向得分匹配（Propensity Score Matching, PSM）通过在可观测特征上为处理组寻找相似的对照组，部分削弱了选择偏差。

面板固定效应模型（Fixed-Effect Model）则通过引入个体虚拟变量，完全吸收了个体、机构或学科内部所有不随时间变化的时不变特征（如学者天资、家庭文化背景或机构历史声誉），有效排除了大量恒定遗漏变量的干扰。

> [!sub-claim] 2. 准实验设计借助外生冲击剥离时变内生性偏误

面对随时间动态变化的未观测混杂因素，科学学借鉴计量经济学发展出三类核心准实验方法：
1. **双重差分法（Difference-in-Differences, DID）** 利用突发外部事件（如卓越科学家意外猝逝、地缘政策突变）作为外生冲击，通过比较受冲击处理组与未受冲击对照组在事件前后的双重变化量，剥离共有时间趋势，因果识别同伴效应与学术网络溢出（[[Difference-in-Differences]]）。
2. **工具变量法（Instrumental Variables, IV）** 寻找一个仅通过影响处理变量进而作用于结果变量的外生工具，排除反向因果与遗漏变量干扰。
3. **断点回归设计（Regression Discontinuity Design, RDD）** 利用科研基金评审资助线等刚性截断门槛，比较刚好越过资助线（险胜）与刚好落入线下（惜败）的申请人。在切分阈值紧邻邻域内，两组个体的能力特征近似随机分布，阈值两侧结果变量的垂直跳跃无偏揭示了资金资助的局部平均处理效应（LATE）（[[Regression Discontinuity Design]]）。

> [!figure]- 图3：准实验因果识别方法（双重差分、工具变量与断点回归）
> ![](https://img.mylikemie.icu/sources/Liu_2023_NHB/figures/Liu_2023_NHB_Fig3_Quasi_Experiment_Methods.jpg)

> [!sub-claim] 3. 实验室实验与随机对照试验为微观机制检验与政策试点提供黄金标准

为了在真实世界中精准隔离干预效应，研究者在实验室环境中严格控制交互流程，探索期刊影响因子对学者声誉感知的心理影响以及同行评审中的性别偏见。针对现实资助政策与科研管理改革，随机对照试验（Randomised Controlled Trial, RCT）通过事前人为随机分配资助机制、盲审规则或评审流程，为检验科技政策工具的真实成效提供了最高内部效度的因果证据。

> [!row-contrast] 科学学主要实证方法范畴与目标对比（复刻表 1 方法分类体系）
> | 方法范畴 | 具体方法 | 核心目标与学科贡献 | 代表性应用场景 |
> |---|---|---|---|
> | **描述性与预测性进路**<br>（Descriptive & Predictive） | **经验规律与通则事实**<br>（Empirical Regularities） | 确立关于科学系统的宏观观察规律；证实或证伪既有假说；为构建新理论提供经验事实。 | 学者产出分布长尾特征、发文序列突破随机性、小团队与大团队创新分工。 |
> | **描述性与预测性进路**<br>（Descriptive & Predictive） | **经典回归分析**<br>（Classic Regression） | 形式化检验变量间的相关关系；估计关联系数的数值大小与统计精确度。 | 文献新颖性对后续引用表现的回归预测与控制变量敏感性检验。 |
> | **描述性与预测性进路**<br>（Descriptive & Predictive） | **生成机制模型**<br>（Mechanistic Models） | 运用微观数学方程刻画底层数据生成过程；为形式理论提供可证伪检验。 | 结合优先连接、适应度与引文老化的引文动力学模型，合作网络演化动力学。 |
> | **描述性与预测性进路**<br>（Descriptive & Predictive） | **机器学习与深度表征**<br>（Machine Learning） | 在多层抽象空间中表征复杂非结构化数据；提供优异的样本外预测精度。 | 运用自然语言处理词向量嵌入预测热电新材料物性，预测科学成果可复现性。 |
> | **因果推断进路**<br>（Causal Approaches） | **匹配与固定效应**<br>（[[Matching]] & Fixed Effects） | 削减回归估计中的选择偏误；控制驱动变量相关的可观测与时不变混杂特征。 | 性别多样性团队对成果影响力的匹配分析；学者个体固定效应排除天资差异。 |
> | **因果推断进路**<br>（Causal Approaches） | **准实验设计**<br>（[[Difference-in-Differences\|DID]] / IV / [[Regression Discontinuity Design\|RDD]]） | 利用数据情境中的外生随机性构建反事实对比，推断变量间的真实因果关系。 | 明星学者猝逝对同行产出的 DID 识别；基金资助评审分数截断处的 RDD 效应。 |
> | **因果推断进路**<br>（Causal Approaches） | **实验与随机对照试验**<br>（Lab Experiments & [[Randomised Controlled Trials\|RCT]]） | 在高度可控环境或田野试点中实施随机分配，识别具体因果机制与干预成效。 | 实验室检验双盲评审消除性别偏见；在科技资助机构中试点部分随机化资助。 |

---

> [!finding-cards] 核心发现
> 1. **全景数据基础设施成熟** 科学学研究的数据体系已由传统的学术出版物单源计量，扩展为融合研发资助输入、微观生涯发展、团队协作网络以及专利和临床转化下游效益的多源数据生态系统。
> 2. **构念效度构成度量基石** 任何基于文献计量大数据的指标均属于理论构念的近似代理；过度依赖单一量化指标容易诱发古德哈特定律式的行为扭曲，必须通过多重测度互证与同行评议机制维护构念效度。
> 3. **预测进路与因果进路形成功能互补** 机器学习与机制模型在挖掘隐性特征、刻画复杂动力学与预测知识发现前沿上具有显著优势，而计量经济学准实验与对照实验则是评估科技政策干预因果有效性不可或缺的工具。

> [!stat-cards]- 核心数据
> - **90%** 主流科学引文数据库中英语文献占比超过 90%，反映出全球文献覆盖存在结构性语种偏误。
> - **8×** 深度学习词向量模型预测未来热电新材料特性的准确率达到随机基准的 8 倍。

---

> [!citation-card] 科学学实证方法全景体系与政策使命
> 随着追踪科学运行的大规模数据资源的涌现，来自不同学科背景的研究者开始将科学方法反身应用于科学本身，孕育出蓬勃发展的科学学。新的实证研究发展为检验传统信念与理论框架、发掘科研生产力关联要素、前瞻预测科学突破并优化科技政策设计提供了坚实的实证基底。
>
> *The advent of large-scale datasets that trace the workings of science has encouraged researchers from many different disciplinary backgrounds to turn scientific methods into science itself, cultivating a rapidly expanding 'science of science'... Overall, new empirical developments provide enormous capacity to test traditional beliefs and conceptual frameworks about science, discover factors associated with scientific productivity, predict scientific outcomes and design policies that facilitate scientific progress.*

---

> [!warning] 自述局限
> 本研究作为全景综述，未展开各类方法的微观数学推导与代码实现细节；数据基础设施仍面临抽屉效应、非英语文献盲区与商业数据壁垒约束；机器学习进路在可解释性与算法公平性方面仍需健全；准实验与实验因果识别受制于自然冲击的稀缺性与局部平均处理效应的外推边界。

---

## 来源

- [[sources/Liu_2023_NHB/Liu_2023_NHB|Liu_2023_NHB]]
