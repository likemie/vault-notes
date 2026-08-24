---
title: Meta-meta-analysis
aliases:
  - 元-元分析
  - 元元分析
  - mega-analysis
  - meta-synthesis
  - 元综合
  - super-analysis
  - super-synthesis
  - Second-Order Meta-Analysis
  - 二阶元分析
  - 二级元分析
  - SOMA
summary: "在更高层级汇总多个已发表元分析结果的统计综合方法，运用多水平层级效应与稳健方差估计处理大型证据库并探索全领域异质性来源"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 77
method_related_level: 6
method_related_stars: "⭐⭐⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/meta-analysis
  - theme/meta-meta-analysis
  - field/research-methodology
related_concepts:
  - "[[Document]]"
  - "[[Effect Size]]"
  - "[[Sampling Error]]"
  - "[[Construct]]"
  - "[[Heterogeneity]]"
  - "[[Interaction Effect]]"
  - "[[Small Study Effects]]"
  - "[[Confidence Interval]]"
  - "[[Prediction Interval]]"
  - "[[External Validity]]"
  - "[[Research Purpose]]"
  - "[[Publication Bias]]"
  - "[[Literature Search]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Variable]]"
  - "[[Visible Learning]]"
  - "[[Paradigm]]"
  - "[[Cooperative Learning]]"
  - "[[Creativity]]"
  - "[[Hypothesis]]"
  - "[[Standard Error]]"
  - "[[Student-Teacher Relationship]]"
  - "[[Direct Instruction]]"
  - "[[Metacognition]]"
  - "[[Class Size]]"
  - "[[Tracking]]"
  - "[[School Leadership]]"
  - "[[Growth]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Sample Size Determination]]"
  - "[[Transcription in Qualitative Research]]"
  - "[[Predictive Validity]]"
  - "[[Academic Achievement]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Affective Outcomes]]"
  - "[[Problem-Based Learning]]"
  - "[[Critical Thinking]]"
  - "[[Epistemology]]"
  - "[[Critique of Meta-meta-analysis]]"
related_theories:
  - "[[Walberg's Educational Productivity Model]]"
  - "[[Dynamic Knowledge and Learning Model]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-regression]]"
  - "[[Robust Variance Estimation]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Inverse-Variance Weighting]]"
  - "[[Correlated and Hierarchical Effects Model]]"
  - "[[Trim and Fill Method]]"
  - "[[Multilevel Egger's Test]]"
  - "[[Umbrella Review]]"
  - "[[Second-Order Meta-Regression]]"
  - "[[Fail-Safe N]]"
  - "[[Begg and Mazumdar Rank Correlation]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Pearson Product-Moment Correlation]]"
  - "[[Random Sampling]]"
  - "[[Comparative Meta-synthesis]]"
  - "[[Effect Size Conversion]]"
related_instruments:
  - "[[AMSTAR]]"
related_facts:
  - "[[EEF Teaching and Learning Toolkit]]"
  - "[[Education Endowment Foundation]]"
related_arguments:
  - "[[Argument_Terhart_2011_JCS]]"
  - "[[Argument_Runco_2026_CRJ]]"
  - "[[Argument_Higgins_2016_RE]]"
  - "[[Argument_Wecker_2016_ZfE]]"
  - "[[Argument_Gungor_2026_CP]]"
  - "[[Argument_Qvortrup_2015_Paideia]]"
  - "[[Argument_Wrigley_2019_ERE]]"
  - "[[Argument_Erdem_2026_SHE]]"
  - "[[Argument_Simpson_2017_JEP]]"
  - "[[Argument_Allerup_2015_Paideia]]"
  - "[[Argument_Bergeron_2017_MJE]]"
  - "[[Argument_Johnson_2023_CE]]"
  - "[[Argument_OConnor_2020_AJLL]]"
  - "[[Argument_Snook_2009_NZJES]]"
  - "[[Argument_Wiliam_2019_ERE]]"
confidence: high
status: draft
created: 2026-05-03
updated: 2026-08-24
---

# Meta-meta-analysis

---

## 定义

> [!def] 方法定义
> [[Meta-meta-analysis|元-元分析]]（Meta-[[Meta-analysis]]，在现代统计学中亦称二阶元分析 Second-Order Meta-Analysis, SOMA，早期[[Document|文献]]称 Mega-analysis 或 Meta-synthesis）指在更高统计层级上对多个已发表[[Meta-analysis|元分析]]（Meta-analysis）结果进行系统检索、方法学质控与定量合成的方法体系。与一阶元分析综合原始主要研究不同，二阶元分析以一阶元分析提取的汇总[[Effect Size|效应量]]（及其背后的[[Sampling Error|抽样误差]]结构）为分析单位，旨在估计宏观领域效应量基准、比较不同[[Construct|理论构念]]与干预维度的相对有效性，并识别全领域效应[[Heterogeneity|异质性]]的深层来源。[[Argument_Terhart_2011_JCS|(Terhart, 2011, p. 436)]]; [[Argument_Runco_2026_CRJ|(Runco et al., 2026, p. 2)]]

> [!method-scope] 方法范围
> - **研究对象** 已发表或灰色文献中关于特定主题的系统评价与一阶元分析汇总效应量矩阵。
> - **问题类型** 评估跨领域宏观效应量强度、检验不同理论构念或干预模式的相对差异、探索出版偏倚与方法学质量的[[Interaction Effect|调节效应]]。
> - **分析单位** 纳入的一阶元分析或其报告的独立一阶效应量集群（Clusters）。
> - **输出形式** 经[[Small Study Effects|小研究效应]]偏倚校正后的二阶总体效应量点估计值（$r$ 或 $g$）、95% [[Confidence Interval|置信区间]]（CI）、95% [[Prediction Interval|预测区间]]（PI）及多水平二阶[[Meta-regression|元回归]]调节系数。

> [!citation-card]- 关键定义
> 二阶元分析在大样本水平上整合多重一阶元分析，采用[[AMSTAR|系统评价质量评估工具]]与多水平[[Robust Variance Estimation|稳健方差估计]]，能够克服单一研究局限，提供高度稳健且具备[[External Validity|可推广性]]的效应量基准。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 2–5)]]
>
> *Second-order meta-analyses synthesize the findings of previous meta-analyses to provide a higher-order summary of evidence... controlling for dependencies through cluster-robust variance estimation.*

---

## 术语演变与方法定位

> [!ref-table]- 术语演变对照表
> | 术语 | 提出者 / 使用者 | 含义侧重与历史定位 |
> |---|---|---|
> | **Meta-[[Meta-analysis]]** | Kazrin et al. (1979) | 强调对元分析进行再分析与统计聚合。 |
> | **Mega-analysis** | Smith (1982) | 强调在样本与[[Document\|文献]]规模上的超级扩展。 |
> | **Super-analysis** | Dillon (1982) | 强调统计抽象层级上的超越。 |
> | **Super-synthesis** | Sipe & Curlette (1996) | 强调跨元分析的系统综合过程。 |
> | **Meta-synthesis** | Sipe & Curlette (1997); [[Argument_Higgins_2016_RE\|Higgins (2016)]] | 质性与量化综合的通用统称。 |
> | **Second-Order Meta-Analysis (SOMA)** | Schmidt & Oh (2013); [[Argument_Runco_2026_CRJ\|Runco et al. (2026)]] | 强调估计一阶[[Sampling Error\|抽样误差]]并采用多水平稳健方差模型进行精确校正的现代统计学标准术语。 |

> [!concept-lens] [[Argument_Higgins_2016_RE|Higgins (2016)]] 的两种用法区分
> [[Argument_Higgins_2016_RE|Higgins (2016, p. 41)]] 区分了二阶综合的两种截然不同的[[Research Purpose|研究目的]]：
> 1. **方法学过程研究** 将元分析作为分析单位来研究元分析过程本身的统计特征、[[Publication Bias|发表偏倚]]与报告质量（如 Ioannidis & Trikalinos, 2007; Lipsey & Wilson, 1993）；
> 2. **实质性主题综合** 试图将不同元分析合并为关于更广泛教育或心理主题的单一信息结论（如 Hattie, 1992; Marzano, 1998; [[Argument_Runco_2026_CRJ|Runco et al., 2026]]）。后者必须解决深刻的[[Construct|构念]]可比性与[[Heterogeneity|异质性]]挑战。

> [!contrast-table] 二阶元分析三代方法谱系多维对比
> | 比较维度 | 第一代：粗放元综合<br>（Naive Meta-Synthesis） | 第二代：标准伞状二阶元分析<br>（Standard Umbrella / SOMA） | 第三代：现代多水平稳健二阶元分析<br>（Modern Multilevel & Robust SOMA） |
> |---|---|---|---|
> | **代表学者与文献** | Fraser, Walberg & Hattie (1987); Hattie (1992, 2008, 2009); Marzano (1998) | Cooper & Koenka (2012); Cafri et al. (2010); [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]]; [[Argument_Gungor_2026_CP\|Güngör et al. (2026)]] | Schmidt & Oh (2013); Cheung (2014); Pustejovsky & Tipton (2022); [[Argument_Runco_2026_CRJ\|Runco et al. (2026)]] |
> | **分析单位** | 一阶元分析报告的算术平均值 $d$ | 一阶元分析提取的汇总效应量（$k$ 个独立观测项） | 一阶元分析[[Effect Size\|效应量]]及其多水平依赖集群（Clusters） |
> | **[[Literature Search\|文献检索]]与质控** | 粗放纳入、无统一质量准入门槛 | 遵循 PRISMA 指南、采用 [[AMSTAR]] / R-AMSTAR 进行严格方法学质量评级 | 遵循 PRISMA 2020、严格 AMSTAR-2 质控并建立初级研究全量引用矩阵 |
> | **效应量尺度处理** | 混用 $d, g, r, \Delta$ 等不同测度而不转换 | 将 OR、$r$、Hedges' $g$ 规范转换为统一 Cohen's $d$ 或 Fisher's $z$ | 统一进行效应量标准化、Fisher's $z$ 变换并保留完整协方差结构 |
> | **初级研究重叠处理** | 完全忽略（容忍 90%+ 的初级研究重叠） | 宏观经验门槛控制（Cooper & Koenka $\le 25\%$ 重叠率门槛，或计算校正覆盖面积 CCA） | 微观[[Primary and Secondary Documents\|初级文献]]完全矩阵去重，或构建跨元分析重叠协方差矩阵进行统计校正 |
> | **加权与统计模型** | 简单未加权算术平均、违规套用单级[[Fixed-Effect and Random-Effects Models\|固定效应模型]] | 单水平经典[[Inverse-Variance Weighting\|逆方差加权法]]（$w_i^* = \frac{1}{v_i + \tau^2}$）与[[Fixed-Effect and Random-Effects Models\|随机效应模型]]（Borenstein et al., 2021） | 三水平[[Correlated and Hierarchical Effects Model\|相关与层级效应模型]]（CHE）+ [[Robust Variance Estimation\|稳健方差估计]]（RVE / 三明治估计量） |
> | **发表偏倚检验** | 无偏倚检验与校正 | 经典漏斗图、Egger 回归截距检验与[[Trim and Fill Method\|剪补法]]（DTTF） | 多水平改进艾格检验（[[Multilevel Egger's Test]]）截距校正与二阶元回归 |
> | **核心目的与产出** | 建立宏观全景排行榜（League Table）与气压计 | 评估特定领域宏观平均效应、检验亚组调节[[Variable\|变量]]并评估发表偏倚 | 估计无偏宏观效应基准、精确分解全领域多层级异质性、检验理论调节模型 |

---

## 历史演变与三代方法谱系演进

> [!phase] 二阶[[Meta-analysis|元分析]]的三代方法谱系演进
>
> - **第一代：早期探索与粗放元综合（1980s–2000s）**
>
>   Glass 提出元分析 10 年后，Fraser, Walberg & Hattie（1987）首次综合 226 项元分析以检验 Walberg 的[[Walberg's Educational Productivity Model|教育生产力模型]]。Hattie（1992, 2008, 2009）在《[[Visible Learning|可见的学习]]》中将其扩展至 800 多项元分析（涵盖 52,649 项研究、8300 万学生），建立 $d = 0.40$ 的影响气压计。然而第一代综合在统计上存在严重缺陷：采用简单算术平均而非[[Inverse-Variance Weighting|逆方差加权]]、混用不同[[Effect Size|效应量]]测度、强行套用[[Fixed-Effect and Random-Effects Models|固定效应模型]]、完全忽略初级研究高达 90% 以上的重叠率，且不报告[[Confidence Interval|置信区间]]与显著性检验。[[Argument_Terhart_2011_JCS|(Terhart, 2011)]]; [[Argument_Wecker_2016_ZfE|(Wecker et al., 2016)]]
>
> - **第二代：标准伞状综述与经典规范二阶元分析（2010s）**
>
>   针对第一代的统计乱象，Cooper & Koenka（2012）在《Research Synthesis Methods》系统提出了综述之综述（Overview of Reviews / [[Umbrella Review]]）的方法学标准；Cafri et al.（2010）在《JEBS》奠定了二阶元分析的基础统计框架；Sipe & Curlette（1996, 1997）与 Pieper et al.（2014）规范了重叠控制标准；Wecker, Vogel & Hetmanek（2016）从数学基础推导出六项方法论规范；[[Argument_Gungor_2026_CP|Güngör et al. (2026)]]则将该[[Paradigm|范式]]应用于[[Cooperative Learning|合作学习]]领域。第二代二阶元分析建立了 PRISMA 与 [[AMSTAR]] 质量筛选流程，严格执行效应量测度转换，普遍采用**经典逆方差加权法（$w_i^* = \frac{1}{v_i + \tau^2}$）**与**随机效应模型**（Borenstein et al., 2021），并采用 Cooper & Koenka $\le 25\%$ 重叠率或校正覆盖面积（CCA）控制[[Document|文献]]重叠，全面报告置信区间与[[Publication Bias|发表偏倚]]检验。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016)]]; [[Argument_Gungor_2026_CP|(Güngör et al., 2026)]]
>
> - **第三代：现代多水平与集群稳健二阶元分析（2013–至今）**
>
>   Schmidt & Oh（2013）在《HRMR》奠定了二阶[[Sampling Error|抽样误差]]与全领域推广理论；Cheung（2014）与 Pustejovsky & Tipton（2022）建立了多水平元分析与集群[[Robust Variance Estimation|稳健方差估计]]（RVE）体系；[[Argument_Runco_2026_CRJ|Runco et al. (2026)]]在[[Creativity|创造力]]全领域综合中确立了第三代范式标杆。第三代方法彻底放弃单水平[[Hypothesis|假设]]，对初级研究进行微观完全去重，采用**[[Correlated and Hierarchical Effects Model|相关与层级效应模型]]（CHE）**进行三水平方差分解（Level 1 抽样误差、Level 2 一阶元分析内依赖、Level 3 跨元分析变异），结合**[[Robust Variance Estimation|稳健方差估计]]（RVE / 三明治估计量）**提供渐近无偏的[[Standard Error|标准误]]与小样本 $T^2 / F$ 校正，并运用多水平改进艾格检验（[[Multilevel Egger's Test]]）和[[Second-Order Meta-Regression|二阶元回归]]，在无需严苛独立性假定下实现了高度稳健的宏观证据推断。[[Argument_Runco_2026_CRJ|(Runco et al., 2026, pp. 2–6)]]

---

## 经典二阶综合操作案例：Hattie 的六大领域与影响气压计

> [!ref-table]- Hattie (2009) 六大影响因素领域与气压计分区
> | 领域分组 | 涵盖维度与特征 | 一阶[[Meta-analysis\|元分析]]数量 | 平均效应量（Cohen's $d$） |
> |---|---|---|---|
> | **教师（Teacher）** | 教师期望、[[Student-Teacher Relationship\|师生关系]]、清晰度、微格教学 | 约 36 项元分析 | **$d = 0.49$** |
> | **课程（Curricula）** | 阅读干预、数学方案、整合课程、户外项目 | 约 147 项元分析 | **$d = 0.45$** |
> | **教学方法（Teaching）** | 反馈、[[Direct Instruction\|直接教学]]、合作学习、[[Metacognition\|元认知]]策略 | 约 332 项元分析 | **$d = 0.42$** |
> | **学生（Student）** | 先前成就、动机倾向、自我概念、认知能力 | 约 141 项元分析 | **$d = 0.40$** |
> | **家庭（Home）** | 社会经济地位、家庭环境、父母参与 | 约 33 项元分析 | **$d = 0.31$** |
> | **学校（School）** | [[Class Size\|班级规模]]、校舍设施、[[Tracking\|分轨制]]、[[School Leadership\|学校领导]] | 约 127 项元分析 | **$d = 0.23$** |

> [!tip] 影响气压计的四个判定区间
> 1. **负面效应区（$d < 0$）** 对学业产生阻碍或倒退（如留级 $d = -0.16$、暑期滑坡）；
> 2. **发展效应区（$0.0 \le d \le 0.15$）** 学生不接受干预仅随生理成熟与自然[[Growth|生长]]产生的基线进步；
> 3. **教师效应区（$0.15 < d \le 0.40$）** 普通教师常规教学能够达到的平均年度进步幅度；
> 4. **期望效应区（$d > 0.40$）** 超越常规教学效果的卓越干预门槛（即 Hattie 设定的“关节点” Hinge Point）。

---

## 现代二阶元分析核心统计支柱与分析方法矩阵

> [!contrast-table] 现代二阶[[Meta-analysis|元分析]]核心统计支柱与分析方法
> | 统计方法条目 | 方法定位与角色 | 解决的核心统计问题与方法论痛点 | 深度条目索引 |
> |:---|:---|:---|:---|
> | **[[Inverse-Variance Weighting\|逆方差加权法（Inverse-Variance Weighting）]]** | **精度加权基础算法** | 解决简单算术平均扭曲估计精度的问题，依据抽样方差与研究间异质性方差的倒数（$w_i^* = \frac{1}{v_i + \tau^2}$）分配权重，实现合成效应量方差最小化。 | 🔗 [[Inverse-Variance Weighting]] |
> | **[[Correlated and Hierarchical Effects Model\|相关与层级效应模型（CHE）]]** | **方差分解与加权工作模型** | 解决同一研究内多重测量相关（相关效应）与跨元分析嵌套（层级效应）的**双重依赖问题**，通过三水平方差分解提供最优逆方差权重矩阵 $\mathbf{W}$，最大化统计估计效率。 | 🔗 [[Correlated and Hierarchical Effects Model]] |
> | **[[Robust Variance Estimation\|稳健方差估计（RVE / 三明治估计量）]]** | **稳健统计推断与[[Standard Error\|标准误]]校正** | 解决文献重叠与聚类依赖导致传统理论方差严重低估（标准误虚假缩水、假阳性率急剧膨胀）的**推断失真问题**，在无需严苛独立性假定下提供渐近无偏的标准误与霍特林 $T^2$ 小样本调整。 | 🔗 [[Robust Variance Estimation]] |
> | **[[Multilevel Egger's Test\|多水平艾格检验（Multilevel Egger's Test）]]** | **[[Small Study Effects\|小研究效应]]诊断与截距偏倚校正** | 解决传统单水平[[Publication Bias\|发表偏倚]]检验在聚类依赖数据下假阳性率高的问题，并同时实现<strong>“小研究偏倚定量诊断”与“截距校正真实效应量”</strong>的一体化输出（参见[[Effect Size\|效应量]]）。 | 🔗 [[Multilevel Egger's Test]] |
> | **[[Fail-Safe N\|失安全系数（Fail-Safe N）]]** | **发表偏倚极端敏感性测试** | 解决抽屉文件效应（File Drawer Problem）潜在威胁的判断问题，通过计算将当前显著合并效应拉低至不显著所需零效应隐藏研究篇数，设定 $5k + 10$ 安全判定门槛。 | 🔗 [[Fail-Safe N]] |
> | **[[Trim and Fill Method\|剪补法（Trim and Fill Method）]]** | **非参数漏斗图偏倚诊断与填补校正** | 解决单侧发表偏倚导致漏斗图不对称与效应量高估的问题，通过迭代剪除极端不对称研究锁定对称中心，并对侧镜像填补虚拟研究以重新估计偏倚校正后的真实效应量。 | 🔗 [[Trim and Fill Method]] |
> | **[[Begg and Mazumdar Rank Correlation\|Begg 秩相关检验（Begg & Mazumdar）]]** | **非参数等级相关偏倚检验** | 解决小样本研究与效应量大小单调关联的诊断问题，通过计算标准化效应量与方差的 Kendall's $\tau$ 秩相关，提供不受正态性假定约束的偏倚检验。 | 🔗 [[Begg and Mazumdar Rank Correlation]] |
> | **[[Second-Order Meta-Regression\|二阶元回归（Second-Order Meta-Regression）]]** | **全领域[[Heterogeneity\|异质性]]来源分解与调节检验** | 解决宏观二阶效应量高度离散、单一平均值掩盖因果机制的问题，在控制[[Document\|文献]]重叠下系统检验[[Construct\|构念]]分类、[[Variable\|变量]]角色与研究特征的[[Interaction Effect\|调节效应]]。 | 🔗 [[Second-Order Meta-Regression]] |

---

## 现代二阶元分析研究程序与步骤

> [!proc] 现代二阶[[Meta-analysis|元分析]]六步标准操作规程
> 1. **多数据库系统检索与灰色[[Document|文献]]扩展** 检索主流学术数据库与博硕士论文库，遵循 PRISMA 声明进行四阶段筛选，严格排除缺乏定量合并矩阵的质性综述与无关系[[Effect Size|效应量]]的坐标元分析。
> 2. **[[AMSTAR]] 12 项方法学质量评估** 采用改编的 AMSTAR 准则进行双人独立[[Coding in Qualitative Research|编码]]（一致率 $\ge 95\%$），设定得分阈值（如 $\ge 0.75$）作为高质量指示[[Variable|变量]]。
> 3. **效应量标准化转换与正态化** 将不同一阶指标统一转换为[[Pearson Product-Moment Correlation|皮尔逊相关]]系数 $r$ 或标准化均值差 $g$，运用 Fisher's $z$ 变换实现方差稳定化。
> 4. **多水平 [[Correlated and Hierarchical Effects Model|CHE]] 与 [[Robust Variance Estimation|RVE]] 稳健方差建模** 设定集群内相关系数（$\rho = 0.8$），运用经验残差构造三明治估计量，计算稳健[[Standard Error|标准误]]与小样本 $F$ 检验。
> 5. **多水平改进艾格回归偏倚检验与校正** 检验[[Small Study Effects|小研究效应]]并根据回归模型截距输出偏倚校正后的二阶效应量点估计值与[[Confidence Interval|置信区间]]。
> 6. **二阶[[Meta-regression|元回归]]与亚组调节变量检验** 纳入[[Construct|理论构念]]类型、[[Independent Variable|自变量]]/[[Dependent Variable|结果变量]]角色、研究设计等调节变量，全面分解效应[[Heterogeneity|异质性]]来源。

---

## 统计建模核心步骤与方法学原理

```mermaid
flowchart LR
  A["步骤 1：效应量转换与正态化<br/>统一测度尺度 (r 或 g) 并稳定抽样方差"] --> B["步骤 2：CHE 三水平方差分解<br/>区分集群间、集群内与抽样三层变异"]
  B --> C["步骤 3：RVE 三明治稳健推断<br/>经验残差外积吸收文献重叠与聚类相关"]
  C --> D["步骤 4：多水平艾格回归偏倚校正<br/>检验小研究效应并由截距提取无偏基准"]
  D --> E["步骤 5：二阶元回归全模型调节分析<br/>纳入宏观协变量检验全领域异质性来源"]
```

---

### 步骤一：固定效应二级汇总的经典等价性原理与独立性约束

> [!formula-step] 公式步骤　固定效应二级汇总等价性定理
> $$d_{\text{second}} = \frac{\sum_{j=1}^{m} w_j d_j}{\sum_{j=1}^{m} w_j} = \frac{\sum_{j=1}^{m} \left(\sum_{i=1}^{k_j} w_{ji}\right) d_j}{\sum_{j=1}^{m} \left(\sum_{i=1}^{k_j} w_{ji}\right)} = \frac{\sum_{\text{all } i} w_i d_i}{\sum_{\text{all } i} w_i}$$
>
> **这个公式在做什么** 证明当且仅当所有一阶[[Meta-analysis|元分析]]纳入的主要研究**互不重叠**且严格按精度反比（$w_j = 1/v_{d_j}$）加权时，二级固定效应元分析才在数学上等价于对所有原始研究直接进行的一级元分析。[[Argument_Wecker_2016_ZfE|(Wecker et al., 2016, pp. 24–28)]]
>
> **关键前提与崩溃条件**
> 该数学等价性成立的**充要条件是纳入的一阶元分析所包含的原始实证研究互不重叠**（抽样独立性假定）。一旦不同元分析重复纳入了相同的经典[[Document|文献]]，该研究的数据就会被重复计算，人为压缩了联合[[Standard Error|标准误]]，造成[[Confidence Interval|置信区间]]虚假过窄与假阳性检验结果膨胀。
>
> 🔗 完整数学证明与理论推导参见：[[Fixed-Effect and Random-Effects Models]] 与 Wecker 等人的论证。

> [!ref-table] [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] 二阶元分析 6 项方法论要求及其违背后果
> | 要求编号 | 方法论准则与规范要求 | 违背类型 | 对效应量 $d$ 与标准误 $SE_d$ 的影响后果 |
> |---|---|---|---|
> | **要求 1** | 统一效应量测度（推荐 Hedges' $g$），正确计算合并标准差，严格区分 SE 与 SD，执行 Fisher's $z$ 转换。 | 测度混合 / SE 与 SD 混淆 | 效应量可放大或缩小十倍（如 Eisenstaedt 1990 中 SE=2.74 被当 SD，导致 $d$ 从 $-0.80$ 膨胀至 $-8.29$），极端值严重扭曲总体平均。 |
> | **要求 2** | 一级元分析必须按精度反比加权（$w_{ji} = 1/v_{ji}$），严禁使用简单算术平均。 | 一级未加权平均 | 估计非最优；$p$ 值与置信区间失真，系统性低估标准误。 |
> | **要求 3** | 纳入的一阶元分析必须基于**互不重叠的主要研究集**，确保抽样独立性。 | 主要研究重复计数 | 重复数据被赋予不成比例的过大权重，置信区间虚假变窄，显著性检验假阳性膨胀。 |
> | **要求 4** | 每个一级元分析必须完整报告联合效应量 $d_j$ 及其方差/标准误/置信区间。 | 方差与精度信息缺失 | 无法确定真实权重与精度边界。 |
> | **要求 5** | 二级汇总必须使用精度反比（$w_j = 1/v_{d_j}$）加权，严禁使用简单算术平均。 | 二级未加权平均 | 估计出现两级复合偏差，排名发生严重对调（如正确加权后 $d = 0.59 \to 0.23$，排名从 #26 骤跌至 #98）。 |
> | **要求 6** | 正确计算联合标准误（$SE_d = \sqrt{1/\sum w_j}$）与 95% 置信区间，执行严格统计显著性检验。 | 标准误人为武断设定 | 人为设置 0.05 下限导致置信区间不可靠，显著性不可解释。 |

---

### 步骤二：三水平方差分解原理（相关效应与层级效应的解耦）

> [!concept-lens] [[Correlated and Hierarchical Effects Model|CHE]] 工作模型的方差分解逻辑
> 传统两水平模型只能处理单一维度的变异，无法应对二阶元分析面临的复杂数据结构。相关与层级效应模型（CHE 模型）通过三水平随机效应架构将总方差剥离为三层：
> 1. **Level 3（元分析集群间变异 $\tau_3^2$）** 捕捉不同一阶元分析在领域主题、时代背景与检索标准上的宏观真实效应差异；
> 2. **Level 2（元分析集群内变异 $\tau_2^2$）** 捕捉同一元分析内部不同测量工具或理论子维度的真实[[Construct|构念]]变异；
> 3. **Level 1（[[Sampling Error|抽样误差]]变异 $V_{ij}$）** 根据已知[[Sample Size Determination|样本量]]计算的[[Random Sampling|随机抽样]]噪声。
>
> **协方差工作矩阵的插补机制**
> 通过设定合理的先验集群内相关常数（如 $\rho = 0.8$），CHE 模型构建块对角抽样协方差矩阵，使得广义最小二乘（GLS）加权估计能够紧密贴合数据的真实多层依赖结构，大幅提高点估计的精度。
>
> 🔗 完整三水平方差分解公式与协方差矩阵插补参见：相关与层级效应模型（CHE）。

---

### 步骤三：聚类稳健三明治方差估计原理（破除文献重叠依赖）

> [!concept-lens] 从“理论模型[[Hypothesis|假设]]”到“经验残差修复”
> [[Robust Variance Estimation|稳健方差估计]]（RVE）是现代二阶元分析破解 Wecker 等人指出的“文献重叠致命软肋”的标准解法。其核心在于经典的**“面包夹肉”三明治结构**
>
> - **两片面包（Bread）** 由 Wecker 经典[[Inverse-Variance Weighting|逆方差加权]]矩阵构成；
> - **中间的夹心肉（Meat）** 由基于实际数据波动计算出的**经验残差外积矩阵**构成。
>
> **破局机理**
> 即使纳入的一阶元分析之间存在不可避免的主要研究重复引用，或者研究者设定的工作模型相关系数（$\rho$）不完全准确，经验残差外积也能自动捕获数据中的真实相关性与超额波动，**自动将虚假缩小的标准误修正回真实水平**。配合 Hotelling $T^2$ 小样本调整，确保在集群数量有限时检验的假阳性率被严格控制在名义水平（如 0.05）。
>
> 🔗 完整三明治矩阵公式与小样本校正算法参见：稳健方差估计（RVE）。

---

### 步骤四：多水平小研究效应检验与截距偏倚校正原理

> [!concept-lens] 截距校正真实[[Effect Size|效应量]]原理
> 经典艾格回归将元分析内不同效应量视为独立点，容易将“同一综述内部效应量的聚集性”误判为[[Publication Bias|发表偏倚]]。[[Multilevel Egger's Test|多水平艾格检验]]在三水平随机效应架构下，将抽样标准误（$\text{SE}$）作为[[Independent Variable|自变量]]纳入回归模型：
>
> 1. **偏倚诊断原理** 若回归斜率系数显著大于零，表明小样本研究系统性报告了偏大的效应量，证实全领域存在[[Small Study Effects|小研究效应]]或发表偏倚；
> 2. **截距校正原理** 回归方程的截距项在数学上对应抽样标准误趋近于零（$\text{SE} \to 0$，即理论无限大样本研究）时的渐近效应量。通过逆双曲正切函数（$\tanh$）将截距还原，即可直接提取出**剔除小样本膨胀效应后的无偏真实效应量基准**。
>
> 🔗 完整多水平回归模型与偏倚校正公式参见：[[Multilevel Egger's Test|多水平艾格检验]]。

---

### 步骤五：二阶元回归调节分析原理（全领域异质性来源分解）

> [!concept-lens] 二阶[[Heterogeneity|异质性]]来源识别
> 二阶元分析的最终目的不仅在于获得单一平均值，更在于分解全领域的异质性来源。通过在 CHE-RVE 框架下纳入宏观协[[Variable|变量]]（如变量角色：自变量 vs [[Dependent Variable|结果变量]]；研究设计：横断面 vs 纵向 vs 实验；方法学质量等级：[[AMSTAR]] 高 vs 低），采用稳健 Wald $F$ 检验系统识别哪些特征显著改变综合效应量，从而在宏观理论层面阐明干预有效性的边界条件。
>
> 🔗 完整三水平[[Meta-regression|元回归]]方程与多参数 Wald 检验公式参见：[[Second-Order Meta-Regression|二阶元回归]]。

---

## 认识论辩护与推论层级约束

> [!concept-lens] [[Argument_Qvortrup_2015_Paideia|Qvortrup (2015)]] 的辩护与动态知识学习模型
> [[Argument_Qvortrup_2015_Paideia|Qvortrup (2015, pp. 27–33)]] 从支持者角度为二阶综合的合理性辩护：元-[[Meta-analysis|元分析]]通过[[Effect Size|效应量]]将不同的具体测量转换为“共同表达式”，使跨研究比较相对学习结果成为可能。但他同时指出，共同表达式的代价是结果高度抽象化，难以判断总体效应究竟来自表层记忆、深层理解还是概念性学习；因此主张引入[[Dynamic Knowledge and Learning Model|动态知识与学习模型]]，按知识类型对学习结果进行多维细化分解。

> [!boundary] [[Argument_Higgins_2016_RE|Higgins (2016)]] 的比较推论层级与苹果橙子类比
> [[Argument_Higgins_2016_RE|Higgins (2016, pp. 40–41)]] 指出，**[[Comparative Meta-synthesis|比较性元分析]]**（在单一元分析内比较多种干预）回答的是“X 是否比 Y 更有效”；而**比较性元综合**（跨元分析比较）面临更高层级的“苹果与橙子”难题。以 Graham et al. (2012) 写作教学元分析为例，虽然可以识别策略教学、自我调节、文本结构、[[Creativity|创造力]]与[[Transcription in Qualitative Research|转录]]等共同有益特征，但这类似于讨论水果的共同繁殖特征（种子），无法推断橙子特有的内部组织结构。

---

## 软件实现与代码规程

> [!software-impl] R 语言多水平二阶[[Meta-analysis|元分析]]实现代码
> ```R
> library(metafor)
> library(clubSandwich)
> 
> # 1. 效应量转换与计算抽样方差（Fisher's z）
> dat <- escalc(measure = "ZCOR", ri = r_val, ni = n_sample, data = raw_data)
> 
> # 2. 构建 CHE 协方差工作矩阵（设定集群内相关系数 rho = 0.8）
> V_mat <- impute_covariance_matrix(vi = dat$vi, cluster = dat$meta_id, r = 0.8)
> 
> # 3. 拟合三水平 CHE 随机效应模型
> model_che <- rma.mv(yi, V_mat, random = ~ 1 | meta_id / effect_id, 
>                     data = dat, sparse = TRUE)
> 
> # 4. 应用 RVE 稳健方差估计（CR2 小样本校正）
> robust_res <- coef_test(model_che, vcov = "CR2", cluster = dat$meta_id)
> 
> # 5. 多水平二阶元回归调节检验
> model_reg <- rma.mv(yi ~ predictor_type + study_design + amstar_high, 
>                     V_mat, random = ~ 1 | meta_id / effect_id, data = dat)
> robust_reg <- Wald_test(model_reg, constraints = constrain_predictors(model_reg), 
>                         vcov = "CR2", cluster = dat$meta_id)
> ```

---

## 使用此方法的核心代表研究

> [!evidence-grid] 使用此方法的核心代表研究
> - **[[Visible Learning]]** Hattie (2009) 综合 800 多项[[Meta-analysis|元分析]]的开创性巨型综合项目。[[Argument_Terhart_2011_JCS|(Terhart, 2011)]]
> - **[[EEF Teaching and Learning Toolkit]]** 英国[[Education Endowment Foundation|教育捐赠基金会]]以[[Effect Size|效应量]]与额外学习月数排名 30+ 类教育干预的循证政策工具。[[Argument_Wrigley_2019_ERE|(Wrigley & McCusker, 2019)]]
> - **[[Creativity|创造力]]全领域二阶元分析** [[Argument_Runco_2026_CRJ|Runco et al. (2026)]] 综合 52 项一阶元分析（2,609 项原始研究、124 万被试），运用 [[Correlated and Hierarchical Effects Model|CHE]] 与 [[Robust Variance Estimation|RVE]] 确立创造力[[Predictive Validity|预测效度]]与教育干预效应。
> - **[[Cooperative Learning|合作学习]]全领域二阶元分析** [[Argument_Gungor_2026_CP|Güngör et al. (2026)]] 综合 15 项一阶元分析（403 项原始实证研究），在[[Umbrella Review|伞状综述]]框架下采用单水平经典[[Inverse-Variance Weighting|逆方差加权]][[Fixed-Effect and Random-Effects Models|随机效应模型]]（Cooper & Koenka $\le 25\%$ 重叠率准则）评估合作学习对[[Academic Achievement|学业成就]]、[[Higher-Order Thinking Skills|高阶思维]]与[[Affective Outcomes|情感行为]]的综合促进效应（$ES = 0.71$），并检验教学技术、学科领域与研究设计的[[Interaction Effect|调节效应]]。
> - **[[Problem-Based Learning|问题本位学习]]高等教育二阶元分析** [[Argument_Erdem_2026_SHE|Erdem et al. (2026)]] 综合 20 项一阶元分析（469 项原始实证研究、47 个独立[[Effect Size|效应量]]），在[[Fixed-Effect and Random-Effects Models|随机效应模型]]下采用经典[[Inverse-Variance Weighting|逆方差加权法]]，依据 Cooper & Koenka $\le 25\%$ 重叠率准则与 R-[[AMSTAR]] 质量评级控制[[Document|文献]]重叠与质量偏倚，报告问题本位学习对学生理论性知识、临床技能、[[Critical Thinking|批判性思维]]、态度与满意度的总体效应（调整后 $ES = 0.60$），并检验结果类型、地域、抽样方法、质量、报告类型与年份的[[Interaction Effect|调节效应]]。
> - **固定效应等价性与方法论批判** [[Argument_Wecker_2016_ZfE|Wecker et al. (2016)]] 从固定效应数学模型推导 6 项要求并系统审查《可见的学习》。

---

## 方法学局限与学术争议总览

> [!warning] 方法学局限与争议提示
> 二阶[[Meta-analysis|元分析]]虽然在统计技术上通过[[Robust Variance Estimation|三明治估计量]]实现了多水平稳健化，但在[[Epistemology|认识论]]和证据应用层面仍面临多重系统性挑战：
> 1. **试验灵敏度混淆** [[Effect Size|效应量]]大小可能反映研究者操纵试验灵敏度的难易程度而非干预本身有效性（[[Argument_Simpson_2017_JEP|Simpson, 2017]], 2019）；
> 2. **偏倚逐级复合** 一阶元分析中的未加权、SE/SD 混淆与公式不可比性无法在二阶统计中被自动消除（[[Argument_Allerup_2015_Paideia|Allerup, 2015]]; [[Argument_Bergeron_2017_MJE|Bergeron & Rivard, 2017]]; [[Argument_Wecker_2016_ZfE|Wecker et al., 2016]]）；
> 3. **透明度与数据重构危机** 粗放元综合常存在数据提取不透明与证实偏差（[[Argument_Johnson_2023_CE|Johnson & Janzen, 2023]]; [[Argument_OConnor_2020_AJLL|O'Connor, 2020]]）；
> 4. **因果机制距离与政策角色争议** 宏观抽象聚合远离了实在层面的因果机制，知识的局部性与临时性使其难以直接指导政策决策（[[Argument_Snook_2009_NZJES|Snook et al., 2009]]; [[Argument_Terhart_2011_JCS|Terhart, 2011]]; [[Argument_Wiliam_2019_ERE|Wiliam, 2019]]; [[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019]]）。
>
> 完整详尽的批判脉络、数学反例、透明度重构与案例剖析详见专门理论条目：
> 🔗 **[[Critique of Meta-meta-analysis|元-元分析批判]]（Critique of Meta-meta-analysis）**。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联方向 | 说明 |
> |:-----|:-----|:---------|:-----|
> | [[Critique of Meta-meta-analysis]] | 概念 | 方法学反思 | 系统阐释元-[[Meta-analysis\|元分析]]在[[Epistemology\|认识论]]、测量错位与政策误用层面的理论批判。 |
> | [[Effect Size Conversion]] | 方法 | 计算前置 | 二阶元分析依赖[[Effect Size\|效应量]]转换统一不同一阶研究的量规尺度。 |
> | [[Correlated and Hierarchical Effects Model]] | 方法 | 建模工作模型 | CHE 三水平方差分解为二阶合成提供最优逆方差权重矩阵。 |
> | [[Robust Variance Estimation]] | 方法 | 稳健推断方法 | RVE 三明治估计量是解决二阶[[Document\|文献]]重叠与聚类依赖的支柱技术。 |
> | [[Multilevel Egger's Test]] | 方法 | 偏倚控制方法 | 在控制聚类依赖下定量诊断[[Publication Bias\|发表偏倚]]并输出校正后真实效应量。 |
> | [[Second-Order Meta-Regression]] | 方法 | 调节分析方法 | 运用多水平稳健[[Meta-regression\|元回归]]系统检验全领域[[Construct\|理论构念]]与研究特征的[[Interaction Effect\|调节效应]]。 |
> | [[AMSTAR]] | 工具 | 质量控制 | 用于二阶元分析中对一阶元分析规范度进行量化评级的方法学工具。 |
> | [[Argument_Runco_2026_CRJ\|Runco et al. (2026)]] | 论证 | 典范应用 | [[Creativity\|创造力]]领域二阶元分析代表作，确立了现代六步建模与偏倚校正规程。 |
> | [[Argument_Wecker_2016_ZfE\|Wecker et al. (2016)]] | 论证 | 诊断先驱 | 严格证明二级固定效应等价性与文献重叠时经典方差失效的机制。 |
