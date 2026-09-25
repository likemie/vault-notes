---
summary: "Jansen 等人（2026）基于约翰·哈蒂可见的学习数据库中的 156 项一阶教育元分析，通过两阶段专家仲裁校准确立金标准，证实大语言模型数据提取准确性（ICC = 0.96–0.97）达到人类专家水平，提出双模型初筛结合专家仲裁的人机混合验证范式。"
type: argument
authors:
  - "Jansen, T."
  - "Liebenow, L. W."
  - "Schaller, N.-J."
  - "[[John Hattie|Hattie, J.]]"
  - "Möller, J."
source_language: en
citation: "Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J. (2026). Automated data extraction by large language models: Assessing accuracy in comparison to human experts using the example of Visible Learning. Educational Psychology Review, 38, Article 38. https://doi.org/10.1007/s10648-026-10136-5"
year: 2026
doi: "https://doi.org/10.1007/s10648-026-10136-5"
citation_aliases:
  - "Jansen et al., 2026"
  - "Jansen et al. (2026)"
isbn: ""
tags:
  - method/meta-analysis
  - theme/artificial-intelligence
  - theme/visible-learning
  - field/educational-psychology
related_concepts:
  - "[[Visible Learning]]"
  - "[[Document]]"
  - "[[Evaluation Research]]"
  - "[[Automated Data Extraction]]"
  - "[[Paradigm]]"
  - "[[Meaningful Human Control]]"
  - "[[Academic Achievement]]"
  - "[[Homework]]"
  - "[[Reliability]]"
  - "[[Tracking]]"
  - "[[AI Hallucination]]"
  - "[[Variable]]"
  - "[[Operationalization]]"
  - "[[Construct]]"
  - "[[Literature Search]]"
  - "[[Research Question]]"
  - "[[Primary and Secondary Documents]]"
related_theories: []
related_methods:
  - "[[Meta-meta-analysis]]"
  - "[[Meta-analysis]]"
  - "[[Effect Size]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Sample Size Determination]]"
  - "[[Violin Plot]]"
  - "[[UpSet Plot]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
related_instruments: []
related_persons:
  - "[[John Hattie]]"
related_facts:
  - "[[Visible Learning Meta-X]]"
  - "[[Achieve]]"
related_arguments: []
sources:
  - "[[sources/Jansen_2026_EPR/Jansen_2026_EPR|Jansen_2026_EPR]]"
part_of:
status: draft
created: 2026-09-18
updated: 2026-09-18
subtype: journal-article
publication_type: journal-article
title: "Argument_Jansen_2026_EPR"
argument_key: "Argument_Jansen_2026_EPR"
argument_display_title: "Automated data extraction by large language models: Assessing accuracy in comparison to human experts using the example of Visible Learning"
argument_kind: "journal-article"
argument_related_count: 29
argument_related_level: 1
argument_related_stars: "⭐"
argument_related_color: "#dbeafe"
journal: "Educational Psychology Review"
book_title: ""
publication_place: ""
publisher: ""
issuing_organization: ""
---
# Argument_Jansen_2026_EPR

---

## 研究问题

> [!question]
> 在教育心理学与实证教育研究中，[[Meta-meta-analysis\|二阶元分析]]（Second-Order Meta-Analyses, SOMAs）通过定量汇总大量一阶[[Meta-analysis\|元分析]]结果，能够系统评估宏观干预效能、比较跨领域影响要素并确立[[Effect Size\|效应量]]基准（如[[John Hattie\|约翰·哈蒂]]（John Hattie）的《[[Visible Learning\|可见的学习]]》项目）。然而，二阶元分析面临沉重的时间与人力成本壁垒：系统性从学术[[Document\|文献]]全文中提取统计结果单篇耗时达 125–172 分钟（中等综述需 44–66 小时，大型综述超 300 小时）。前沿大语言模型（Large Language Models, LLMs）能否胜任二阶元分析中复杂的统计数据提取并达到人类专家水平？以往[[Evaluation Research\|评估研究]]简单将单一人类提取预设为无误差真值的做法存在何种方法论缺陷？如何建立专家仲裁校准的金标准基准以解构机器与人类的真实误差形态？

> [!claim] 核心主张
> 前沿大语言模型在规范提示词引导下，对复杂教育元分析文献进行[[Automated Data Extraction\|自动化数据提取]]的统计准确性全面达到甚至部分超越人类专家水平（与仲裁金标准的[[Intraclass Correlation Coefficient\|组内相关系数]] $\text{ICC} = 0.96–0.97$ vs 专家 $\text{ICC} = 0.81–0.95$；一致率达 77%–81% vs 专家 80%–86%）；模型之间表现出高达 87%–90% 的高度收敛一致性。事实性AI 幻觉在规范抽取中发生率极低（3–4 例，与专家持平），主要误差源于跨表格加总学生总数与原文报告模糊性。研究据此构建了双模型独立初筛结合专家分歧仲裁的人机混合验证[[Paradigm\|范式]]，在恪守[[Meaningful Human Control\|有意义的人类控制]]（Meaningful Human Control, MHC）的前提下消减 80% 人工劳动，实现证据综合效率与精度的帕累托最优。

> [!concept-lens] 阅读透镜
> - **对象** 从《[[Visible Learning\|可见的学习]]》数据库（[[Visible Learning Meta-X]]）中随机抽取的 156 项调查学生[[Academic Achievement\|学业成就]]的一阶元分析全文文献（涵盖综合效应量 $d$、纳入研究数 $k$ 与学生样本总量 $N$ 共 468 个目标数据点）。
> - **张力** 传统证据综合对繁重双人人工[[Homework\|作业]]的高昂成本依赖 vs 大模型全自动提取的不[[Reliability\|可靠性]]与幻觉担忧；单一人类提取被预设为无偏真值 vs 真实科研中人类单方[[Coding in Qualitative Research\|编码]]普遍存在的疲劳漂移与疏漏偏差。
> - **贡献** 首次在二阶元分析情境下建立多专家两阶段仲裁校准的金标准基准；系统评测三大前沿大语言模型（Gemini 2.5 Pro、GPT-4.1、GPT-o3）与人类专家的准确性矩阵；提出兼顾伦理规范与生产力跃升的有意义人类控制证据综合实操框架。

---

## 理论框架

> [!framework-table] 理论工具箱
> | 理论工具 | 解释功能 |
> |----------|----------|
> | **[[Meaningful Human Control\|有意义的人类控制]]**<br>[[Meaningful Human Control]] | 源自人工智能伦理学（Santoni de Sio & van den Hoven, 2018）与负责任证据综合指南，确立人类在自动化决策全流程中的追踪条件（[[Tracking]] Condition）与响应条件（Responsiveness Condition），防止人类退化为被动盖章者。 |
> | **[[Automated Data Extraction\|自动化数据提取]]**<br>[[Automated Data Extraction]] | 解构大模型在长文本中识别、抽取并结构化呈现统计量与研究特征的自动化规程，突破传统任务专用算法需要定制编程与泛化脆弱的局限。 |
> | **[[AI Hallucination\|AI 幻觉]]与误差分类学**<br>[[AI Hallucination]] | 建立涵盖事实虚构、信息遗漏、跨表计算偏差与报告模糊性选择偏误的四维诊断体系。 |

> [!warrant]- 理论如何支撑论证
> 负责任证据综合中人工智能使用（Responsible use of AI in evidence SynthEsis）指南为本研究确立了评价基线：任何人工智能系统的引入都不能直接假定其可[[Reliability\|信度]]，而必须通过严密的实证评测确定其在特定任务情境下的准确性基准；同时，人类专家必须保持对系统的因果追踪能力。通过解构模型与人类在不同误差类型上的认知表现，研究得以将统计一致性指标转化为人机协同分工的理论依据。（pp. 3, 6, 20, 24）

### 核心变量与操作化编码表（仅量化研究填写）

> [!index-table] 核心[[Variable\|变量]][[Operationalization\|操作化]]定义与[[Coding in Qualitative Research\|编码]]规程
> | [[Automated Data Extraction\|变量维度与分类]] | [[Construct\|理论构念]]与操作化定义 | 核心教学规程、典型测量工具与纳入案例 |
> |---|---|---|
> | **综合效应量**<br>（Effect Size, $d$） | 一阶元分析报告的主要总体综合效应量（Cohen's $d$ 或 Hedges' $g$）。 | 优先提取与学生[[Academic Achievement\|学业成就]]最相关的全域总体加权汇总值；若[[Document\|文献]]同时汇报固定与随机效应，优先提取主分析模型数值；若只报告亚组效应则依据代码簿优先级提取。 |
> | **纳入研究篇数**<br>（Number of Studies, $k$） | 贡献于上述综合[[Effect Size\|效应量]]的一阶原始实证研究总篇数或独立样本数。 | 严格区分[[Literature Search\|文献检索]]获取的总篇数与最终纳入定量合成的研究篇数；若文献仅报告效应量个数而明确缺失独立研究数，则严格编码为缺失值（Not Applicable, NA）。 |
> | **参与者样本总量**<br>（Number of Participants, $N$） | 包含在定量合并分析中的学生/被试总人数。 | 提取文献明确汇报的总[[Sample Size Determination\|样本量]]；若总被试数未直接汇总而是分散在各分表或各亚组中，需执行跨表精确累加；若全文均未报告被试规模则编码为缺失值（NA）。 |
>
> **图表解读** 本表严格定义了从一阶[[Meta-analysis\|元分析]]中提取的三大核心连续变量及其边界规则，构成了大语言模型提示词构建、独立作者编码与专家金标准仲裁的统一操作化基准。（pp. 7–8）

---

## 研究方法

> [!method-panel] 研究设计
> | 模块 | 材料与处理方式 |
> |------|----------------|
> | **[[Document\|文献]]抽样与数据准备** | 从[[John Hattie\|约翰·哈蒂（John Hattie）]]教授维护的[[Visible Learning Meta-X]]数据库（包含 2,100+ 项元分析）中，随机抽取 156 项聚焦学生学业成就的一阶元分析全文文献（PDF 格式）。（pp. 7–8） |
> | **提示词工程与模型推断** | 构建包含角色定义、[[Variable\|变量]]代码簿、优先级层级与 3 个少样本示例的提示词架构。在独立的 10 篇[[Meta-analysis\|元分析]]子集上完成预试调优后，通过应用程序编程接口（Application Programming Interface, API）运行三大专有前沿模型：Gemini 2.5 Pro、GPT-4.1 与 GPT-o3。（pp. 8–9） |
> | **两阶段基准仲裁体系** | 针对 101 项存在分歧的元分析，首先由一位作者独立复核建立银标准；对剩余 67 项高度存疑或与原数据库严重背离的文献，由专家作者组联合研讨仲裁建立无偏金标准基准。（pp. 9–10） |
> | **多维准确性评估方法** | 采用双向随机效应绝对一致性单评分者[[Intraclass Correlation Coefficient\|组内相关系数]]（Intraclass Correlation Coefficient, ICC）模型 $\text{ICC}(2,1)$、直接百分比一致率、皮尔逊相关系数（$r$）、平均绝对误差（Mean Absolute Error, MAE）、[[Violin Plot\|小提琴图]]（Violin Plot）与集合交集图（[[UpSet Plot]]）展开全景评测。（pp. 10–14） |

> [!sample-panel]- 样本与材料快照
> | 样本层面 | 构成 |
> |----------|------|
> | **文献样本** | 156 篇发表于 1980 至 2023 年间的教育一阶元分析全文 PDF，篇幅介于 5 至 50+ 页，涵盖广泛的排版布局与统计汇报体例。（p. 7） |
> | **[[Coding in Qualitative Research\|编码]]主体** | 人类编码员 2 组（独立作者专家编码、[[Visible Learning]] 既有数据库录入）；大语言模型 3 组（Gemini 2.5 Pro、GPT-4.1、GPT-o3）。（pp. 8–10） |
> | **评估数据点** | 156 篇文献 × 3 个核心变量（$d, k, N$）= 全样本共计 468 个独立比对数据点。（p. 10） |

---

## 论证结构

> [!logic-map]- 核心论证逻辑链
> ```mermaid
> flowchart LR
>     A["起点：SOMA 面临巨大耗时壁垒<br/>且单一人类基准存在固有偏误假定"] --> B["第一阶段：提示词校准与多主体提取<br/>Gemini 2.5 Pro / GPT-4.1 / GPT-o3"]
>     B --> C["第二阶段：专家双轮仲裁确立金标准<br/>解决 101 项分歧并纠正 57 处历史偏离"]
>     C --> D["第三阶段：准确性与收敛性评测<br/>LLM ICC 0.96-0.97 匹敌人类单专家"]
>     D --> E["第四阶段：误差谱系与认知归因剖析<br/>幻觉极低 (~5%) / 遗漏与多表计算居多"]
>     E --> F["结论：构建基于 MHC 的人机混合验证范式<br/>双模型初筛 + 专家仲裁消减 80% 耗时"]
>     
>     A --> B
>     B --> C
>     C --> D
>     D --> E
>     E --> F
> ```

---

### 论证步骤一　传统单一人类提取基准存在系统性偏误，需通过专家双轮仲裁确立无偏金标准

> [!claim] 步骤一核心主张
> 以往人工智能[[Evaluation Research\|评估研究]]简单将单一人类提取作为无误差的基准真值，掩盖了人类单方[[Coding in Qualitative Research\|编码]]中的固有失误；必须通过专家交叉复核与两阶段仲裁建立客观金标准。（pp. 3, 9–10）

#### 1. 研究全流程设计与三阶段实施路径

> [!goal] 研究设计目标
> - **核心动机** 在开展[[Meta-meta-analysis\|二阶元分析]]时，数据提取是决定证据质量的生命线环节。以往研究直接将单一人工录入作为无偏基准，掩盖了人类编码的固有疏漏；本研究设计严密的三阶段程序，建立客观金标准以解构机器与人类的真实误差形态。

> [!example]- 图1：研究程序示意图
> ![](https://img.mylikemie.icu/sources/Jansen_2026_EPR/figures/Jansen_2026_EPR_Fig1_Study_Procedure.jpg)

该流程图系统展示了从数据准备、模型推断到专家仲裁的完整复现闭环。研究团队在提取提示词中固化了精确的代码簿规则与优先级，并在独立的 10 篇试点[[Document|文献]]上完成了提示词优化，确保推断过程与测试样本完全隔离。（pp. 8–10）

#### 2. 差异识别与两阶段专家仲裁规程

在提取的 156 项[[Meta-analysis|元分析]]（共 468 个数据点）中，各编码主体之间并非天然一致——多达 101 项元分析在至少一个[[Variable|变量]]上存在分歧，必须通过严谨的仲裁程序确定真值。

> [!proc] 专家仲裁确立金标准的两阶段操作规程
> 1. **第一阶段：银标准独立复核** 一位资深作者独立重新审阅全部 101 项存在分歧的元分析原文，严格对照统一代码簿判定基准值。（p. 9）
> 2. **第二阶段：金标准专家研讨仲裁** 针对首轮复核后仍存在多重解释模糊性、或判读值与原数据库严重背离的 67 篇文献（占全样本 42.9%），由专家作者组联合开展研讨质证，逐一排查多表格累加口径与亚组定义，最终达成全员共识真值。（p. 10）

> [!implication]- 仲裁的方法论意义
> 这一仲裁流程揭示出关键事实：既有数据库中存在 57 处独有的人工单方偏离；若未进行仲裁校准，这些人工失误将被错误归因于大模型的提取错误，导致 AI 表现系统性低估。（pp. 16–17）

---

### 论证步骤二　大语言模型在统计量提取上达到人类专家水平且各模型间高度收敛

> [!claim] 步骤二核心主张
> 大语言模型在[[Effect Size\|效应量]]、研究数与[[Sample Size Determination\|样本量]]提取上的统计分布与仲裁金标准高度重合，[[Intraclass Correlation Coefficient\|组内相关系数]]与一致率全面达到甚至部分超越人类专家水平。（pp. 16–19）

#### 1. 总体统计分布对齐性检验

实证分析首先通过[[Violin Plot|小提琴图]]检验各编码主体提取数据的宏观分布特征。

> [!example]- 图2：效应量、研究数与参与者人数分布小提琴图
> ![](https://img.mylikemie.icu/sources/Jansen_2026_EPR/figures/Jansen_2026_EPR_Fig2_Violin_Plots.jpg)

> [!warrant]- 图2 支持分布对齐主张的推理
> 小提琴图显示，大语言模型（绿色）、人类专家（蓝色）以及银标准与金标准（银灰色/金色）在三大变量的概率密度分布上几乎完全重合。综合效应量 $d$ 的均值高度收敛（$M = 0.50–0.51, SD = 0.33–0.35$），研究篇数 $k$ 均值介于 41.54–46.68 之间，参与者总数 $N$ 展现出相似的偏态分布，证明大模型没有产生系统性的尺度偏移或截断——这直接支持了大模型与金标准在统计分布层面的根本性等值判断。（pp. 15–16）

#### 2. 全矩阵准确性指标对比与模型间收敛

通过计算百分比一致率与双向随机效应组内相关系数 $\text{ICC}(2,1)$，研究构建了完整的准确性矩阵。

> [!contrast-table] 编码员与参考标准准确性矩阵（上三角：一致率；下三角：$\text{ICC}(2,1)$）
> | 评估对象 | 金标准（Gold） | 银标准（Silver） | 独立作者编码 | [[Visible Learning]] | Gemini 2.5 Pro | GPT-4.1 | GPT-o3 |
> |---|---|---|---|---|---|---|---|
> | **金标准（Gold）** | — | **93%** | **86%** | **80%** | **81%** | **78%** | **77%** |
> | **银标准（Silver）** | 0.98 | — | 91% | 79% | 84% | 80% | 78% |
> | **独立作者编码** | 0.95 | 0.98 | — | 76% | 82% | 78% | 77% |
> | **Visible Learning** | 0.81 | 0.78 | 0.75 | — | 79% | 77% | 76% |
> | **Gemini 2.5 Pro** | 0.96 | 0.94 | 0.95 | 0.82 | — | **90%** | **87%** |
> | **GPT-4.1** | 0.97 | 0.95 | 0.97 | 0.82 | 0.97 | — | **87%** |
> | **GPT-o3** | 0.96 | 0.96 | 0.96 | 0.81 | 0.95 | 0.97 | — |

> [!conclusion] 矩阵数据的核心结论
> 三大前沿大语言模型与金标准的组内相关系数均处于卓越区间（$\text{ICC} = 0.96–0.97$），百分比一致率介于 77%–81%，表现完全媲美人类独立作者（$\text{ICC} = 0.95$，一致率 86%），且显著优于 Visible Learning 既有数据库（$\text{ICC} = 0.81$，一致率 80%）。更关键的是，模型之间的一致率高达 87%–90%（$\text{ICC} = 0.95–0.97$），证实模型的准确性源自对文献语义的稳定理解而非偶然命中。（pp. 18–19）

#### 3. 编码主体交集结构与共识模式

为了进一步厘清多方一致性的深层结构，研究采用[[UpSet Plot|集合交集图]]剖析了 468 个数据点的组合重叠分布。

> [!example]- 图3：人类编码员、LLMs与金银标准之间一致性交集的 UpSet 图
> ![](https://img.mylikemie.icu/sources/Jansen_2026_EPR/figures/Jansen_2026_EPR_Fig3_UpSet_Plot.jpg)

> [!warrant]- 图3 支持共识模式主张的推理
> 集合交集图（UpSet Plot）分析显示，在 280 个数据点上（占 59.8%），所有人类与机器编码员及两项参考标准达成完全一致；排在第二位的频次是 Visible Learning 数据库的单方偏离（57 例，占 12.2%）；在 27 例中（占 5.8%），所有模型与独立作者一致判定，仅既有数据库存在偏差。仅有 16 例（占 3.4%）属于人类双重一致而所有模型均未能正确提取的情形——这表明大模型的失准边界极窄，且与既有人类数据库的误差分布呈现截然不同的结构。（pp. 17–18）

---

### 论证步骤三　提取误差主要由复杂计算与报告模糊性驱动，人机协同工作流实现效率与精度的帕累托最优

> [!claim] 步骤三核心主张
> 大模型的错误并非源于事实捏造，而是受限于分散数据累加与原文报告模糊性；建立多模型共识结合专家仲裁的混合架构能够兼顾效率飞跃与质量问责。（pp. 18, 20–25）

#### 1. 错误形态解构：幻觉罕见而遗漏与多表计算居多

> [!concept-lens] 误差画像的三重透镜
> - **[[Research Question\|研究问题]]** 细粒度的错误分类分析区分人类专家与大语言模型截然不同的误差画像：错误来自何种认知机制？频率如何分布？
> - **关键区分** 事实性幻觉（凭空虚构）vs 信息遗漏（有据可查却标记为缺失）vs 计算偏差（数值存在但累加错误）
> - **实践边界** 识别误差结构是精准设计提示词与人工介入策略的前提

> [!feature] 数据提取误差四维谱系
> - **事实性幻觉** 指原文明确缺失某项数据但编码主体凭空虚构数值。在 55 项缺失特定统计量的元分析中，三大模型仅出现 3–4 例幻觉，与人类专家的 3–4 例完全持平，表明模型在提示词约束下极少无中生有。（p. 18）
> - **信息遗漏** 指原文包含数据但被误标为缺失值（NA）。独立人类作者遗漏最少（12 例），Gemini 2.5 Pro（21 例）与 GPT-4.1（22 例）表现良好，优于原数据库的 31 例遗漏；GPT-o3 遗漏较多（36 例）；所有遗漏均集中于需要深度跨表定位的被试总数 $N$。
> - **跨表格加总计算偏差** 当被试规模分散在多个亚组或分表中时，大模型在长上下文中执行多步心算累加容易产生微小差错。（p. 16）
> - **报告模糊性选择偏误** 当原文摘要与正文表格数值冲突，或同时呈现固定效应与[[Fixed-Effect and Random-Effects Models\|随机效应模型]]时，模型偶尔捕获了局部亚组值而非全局汇总值。（p. 17）

#### 2. 基于有意义人类控制的四步混合验证范式

> [!goal] 混合验证规程的设计目标
> - **核心目标** 将大模型的提取潜能转化为严谨的学术生产力，结合RAiSE 负责任证据综合指南，在恪守[[Meaningful Human Control\|有意义的人类控制]]原则的前提下，最大化节约专家劳动。

> [!proc] 证据综合中有意义人类控制的四步混合验证规程
> 1. **提示词开发与预试校准** 编制涵盖变量代码簿、提取优先级与少样本示例的标准化提示词，在独立先导文献集上完成参数调优。（p. 8）
> 2. **异构双模型背对背独立推断** 部署两个不同技术路线的前沿模型（如 Gemini 2.5 Pro 与 GPT-4.1）分别独立提取全文数据。（p. 24）
> 3. **自动化交集比对与分流** 脚本自动比对双模型输出：完全一致的数据点（约占 80%–84%）直接归入高置[[Reliability\|信度]]数据库，无需人工逐字审验。
> 4. **专家介入分歧争议仲裁** 针对双模型输出不一致或标记为高复杂度跨表加总的数据点（约占 16%–20%），触发领域专家深度查阅原文并作出最终裁决。（p. 25）

> [!warrant]- 混合工作流如何实现帕累托最优
> 单一人类提取不仅耗时高昂（156 篇需约 390 小时），且存在约 14%–20% 的认知疲劳与单方失误。双模型初筛结合专家异常仲裁，将专家精力高度聚焦于 20% 的争议盲区（人工耗时缩减至约 60–80 小时），同时通过人机交叉互证彻底排除了单一人工失误，使最终证据库质量无限逼近 100% 金标准真值，实现了科研效率与严谨性的双重突破。（pp. 23–25）

---

## 主要发现

> [!finding-cards] 核心发现
> 1. **前沿大语言模型提取准确性达到人类专家水准** Gemini 2.5 Pro、GPT-4.1 与 GPT-o3 在 156 项教育[[Meta-analysis\|元分析]]中的提取表现（[[Intraclass Correlation Coefficient\|组内相关系数]] ICC = 0.96–0.97，一致率 77%–81%）全面匹敌单一人类专家（ICC = 0.81–0.95，一致率 80%–86%）。（pp. 18–19）
> 2. **事实性幻觉在规范抽取中极为罕见** 在缺失数据的[[Document\|文献]]中，大模型虚构数值的幻觉率仅为 5%–7%（3–4 例），与人类专家的幻觉率完全持平。（p. 18）
> 3. **提取瓶颈聚焦于多表加总与报告模糊性** 机器与人类的分歧主要源于跨分表被试总数 $N$ 的累加疏漏，以及[[Primary and Secondary Documents\|原始文献]]在摘要与正文中汇报冲突数据时的选择偏好。（pp. 16–18）
> 4. **确立人机混合验证的帕累托最优[[Paradigm\|范式]]** 双模型初筛结合专家分歧仲裁，在节约 80% 人工劳动的同时，能够有效消除单人提取疏漏并保障[[Meaningful Human Control\|有意义的人类控制]]。（pp. 24–25）

> [!stat-cards]- 核心数据
> - **0.96–0.97** 三大前沿大语言模型与金标准的组内相关系数 ICC(2,1)。
> - **87%–90%** 大语言模型之间的两两一致率（ICC = 0.95–0.97）。
> - **≈ 80%** 采用双模型初筛后可直接免除人工逐字复核的高置[[Reliability\|信度]]数据比例。（p. 24）
> - **≈ 390** 传统单人提取 156 篇文献所需的专家工时（小时，混合范式仅需约 60–80 小时）。（pp. 2, 24）
>
> 以上 ICC 与一致率数据均来自 p. 18 主要结果表格。

---

## 关键引用

> [!citation-card] 大模型提取精度逼近人类专家基准
> 研究结果表明，大语言模型在数据提取准确性上达到了与人类专家相当的水平。我们在 156 项调查学生[[Academic Achievement\|学业成就]]的教育[[Meta-analysis\|元分析]]中比较了三种大语言模型与人类专家的准确性。大模型与金标准的[[Intraclass Correlation Coefficient\|组内相关系数]]达到 0.96–0.97，一致率达到 77%–81%。（p. 1）
>
> *The results demonstrate that LLMs [[Achieve]] data extraction accuracy comparable to that of human experts. We compare the accuracy of three LLMs with that of human experts extracting data from 156 educational meta-analyses investigating students' achievement... Accuracy reached ICCs of 0.95/0.81 for the two human experts, and 0.96/0.97/0.96 for LLMs, with percentage agreement of 86%/80% (humans) and 81%/78%/77% (LLMs).*

> [!citation-card] 证据综合中有意义人类控制与验证条件
> 证据综合中负责任使用人工智能指南明确要求，必须通过[[Evaluation Research\|评估研究]]确定 AI 在特定语境下是否表现充分。我们的研究为大语言模型负责任地用于数据提取提供了实证基础，并阐明了在何种条件下人类、模型或人机混合提取的数据可被视为经过有效验证。（pp. 3, 24）
>
> *The RAiSE guidance states that evaluation studies should determine whether an AI performs adequately in a given context. Our study provides an empirical foundation for responsible use of LLMs for data extraction. We discuss the conditions under which data extracted by LLMs, humans, or a hybrid of both can be considered validated for use in educational SOMAs.*

---

## 自述局限

> [!warning]
> 1. **专有闭源黑盒模型依赖** 研究选用了处于技术前沿的专有商业模型（GPT-4.1、Gemini 2.5 Pro 等），模型更新不透明且成本可能变动，研究结论无法直接无缝推广至参数较小的开源本地模型。（pp. 25–26）
> 2. **训练集数据污染潜在风险** 《[[Visible Learning\|可见的学习]]》部分公开[[Meta-analysis\|元分析]]数据可能存在于大模型的预训练语料中；尽管模型在金标准与原数据库背离时仍能准确提取原文数值证明其具备真实阅读理解能力，但未来仍需在全新的非公开人类共识数据集上进行前瞻性验证。（p. 26）
> 3. **计算能耗与环境成本考量** 运行 156 篇[[Document\|文献]]的大模型推断约消耗 1.3–2.0 kWh 电力与 5.3 L 淡水蒸发；但相比人工完成相同任务所需的 390 小时工作站能耗与个人用水需求，机器提取的综合环境足迹仍显著更低。
> 4. **提示词工程对领域专长的依存性** 提示词架构经过教育元分析专家的深度优化与校准，迁移至其他学科（如临床医学）或截然不同的[[Coding in Qualitative Research\|编码]]任务时需要重新标定。（pp. 24–25）

---

## 来源

- [[sources/Jansen_2026_EPR/Jansen_2026_EPR|Jansen_2026_EPR]]
