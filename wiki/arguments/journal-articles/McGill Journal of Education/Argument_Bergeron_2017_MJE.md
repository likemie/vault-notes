---
summary: "从数理统计学视角系统审查 John Hattie 可见学习方法论，揭示二阶元分析存在初等概率计算错误（普通语言效应量产出负概率）、基线比较主观任意性、三类有效公式导致完全相反排名以及相关换算极值爆炸与因果混淆，确立教育实证研究必须在全流程引入独立专业统计咨询"
type: argument
authors:
  - "[[Pierre-Jérôme Bergeron|Bergeron, P.-J.]]"
  - "Rivard, L."
source_language: en
citation: "Bergeron, P.-J. & Rivard, L. (2017). How to engage in pseudoscience with real data: A criticism of John Hattie's arguments in Visible Learning from the perspective of a statistician. McGill Journal of Education, 52(1), 237–246. https://doi.org/10.7202/1040816ar"
year: 2017
doi: "10.7202/1040816ar"
citation_aliases:
  - "Bergeron & Rivard, 2017"
  - "Bergeron and Rivard (2017)"
isbn: ""
tags:
  - visible-learning
  - effect-size
  - meta-analysis
  - pseudoscience
  - methodology-critique
  - statistics
  - subject/research-methodology
related_concepts:
  - "[[Visible Learning]]"
  - "[[Scientific Method]]"
  - "[[Commensuration]]"
  - "[[Causality]]"
  - "[[Epistemology]]"
  - "[[Falsification]]"
  - "[[Document]]"
  - "[[Creativity]]"
  - "[[Variable]]"
  - "[[Study Population and Sample]]"
  - "[[Class Size]]"
  - "[[Socioeconomic Status]]"
  - "[[Academic Achievement]]"
  - "[[Incommensurability]]"
  - "[[Zone of Desired Effects]]"
  - "[[Self-reported Grades]]"
  - "[[Creativity Training]]"
  - "[[Critical Thinking]]"
  - "[[Blind Spot in Observation]]"
  - "[[Heterogeneity]]"
related_theories: []
related_methods:
  - "[[Meta-meta-analysis]]"
  - "[[Meta-analysis]]"
  - "[[Effect Size]]"
  - "[[Inappropriate Baseline Comparisons]]"
  - "[[Common Language Effect Size]]"
  - "[[Random Assignment]]"
  - "[[Experimental Research]]"
  - "[[Pre-test and Post-test]]"
  - "[[Correlational Research]]"
  - "[[Pearson Product-Moment Correlation]]"
related_instruments: []
related_persons:
  - "[[John Hattie]]"
  - "[[Pierre-Jérôme Bergeron]]"
related_facts: []
related_arguments: []
sources:
  - "[[sources/Bergeron_2017_MJE/Bergeron_2017_MJE|Bergeron_2017_MJE]]"
part_of: ""
status: completed
created: 2026-05-03
updated: 2026-10-29
subtype: journal-article
publication_type: journal-article
title: "Argument_Bergeron_2017_MJE"
argument_key: "Argument_Bergeron_2017_MJE"
argument_display_title: "How to engage in pseudoscience with real data: A criticism of John Hattie's arguments in Visible Learning from the perspective of a statistician"
argument_kind: "journal-article"
argument_related_count: 32
argument_related_level: 3
argument_related_stars: "💎"
argument_related_color: "#dbeafe"
journal: McGill Journal of Education
---
---

> [!question]
> 从专业数理统计学视角系统审查 [[John Hattie|约翰·哈蒂]]（John Hattie） 在《[[Visible Learning|可见的学习]]》（*Visible Learning*, 2008）中构建的[[Meta-meta-analysis|二阶元分析]]方法论是否符合科学有效性的基本统计准则。面对汇总 800 余项[[Meta-analysis|元分析]]、50,000 余项研究和数百万学生的庞大数据库，该综合究竟属于严谨的[[Scientific Method|经验科学]]，还是以真实数据编造故事的伪科学？

> [!claim] 核心主张
> 哈蒂的《可见的学习》在方法论上存在多重致命缺陷：不仅包含初等计算错误（在常见语言[[Effect Size|效应量]]中算出负概率与超过 100% 的不可能概率），且对效应量的基线比较完全缺乏自省；受控数值模拟证实三种在技术上均合法的计算公式对同一数据得出完全颠倒的排名，相关向均值差的换算更带来数学爆炸与因果混淆。这一所谓教育学圣杯实质上是一座以真实数据构建却迅速崩解的脆弱纸牌屋，属于典型的伪科学。

> [!concept-lens] 阅读透镜
> - **对象** 哈蒂在《可见的学习》及其衍生著作中汇总的 800 余项元分析数据库、统计合成程序及影响因素排名榜单。
> - **张力** 海量实证数据规模带来的科学严谨性假象，与基础计算崩溃、度量尺度不可[[Commensuration|通约]]、基线主观任意及[[Causality|因果推断]]失范之间的尖锐对立。
> - **贡献** 证实 Cohen's $d$ 无法充当跨研究设计的普适度量标尺，证明效应量排名完全取决于公式选择与基线方向，确立了教育实证研究必须在全流程引入专业统计咨询的制度规范。

---

> [!framework-table] 理论工具箱
> | 理论工具 | 解释功能 |
> |----------|----------|
> | **科学研究三大主要错误分类**<br>Allison et al. (2016) | 在《自然》（*Nature*）中归纳的科学研究核心错误体系，为审查[[John Hattie\|哈蒂]]在[[Meta-analysis\|元分析]]中的计算错误与[[Inappropriate Baseline Comparisons\|不当基线比较]]提供权威准绳。 |
> | **普通语言效应量概率映射理论**<br>McGraw and Wong (1992) | 将连续分布标准化均值差转化为二项超越概率的数学模型，确立概率值域严格落于 $(0\%, 100\%)$ 的数学公理边界。 |
> | **元分析度量空间与转换准则**<br>Borenstein et al. (2009) | 规范统计指标跨尺度转换的前提条件与数学假设，提供审查相关系数向 Cohen's $d$ 转换合法性的度量空间依据。 |
> | **全程统计咨询介入原则**<br>Fisher (1938) | 强调实验设计前介入而非事后尸检的统计[[Epistemology\|认识论]]，作为重构教育实证研究方法论防线的基本原则。 |

> [!warrant]- 理论如何支撑论证
> 上述统计学理论工具共同构建了评判教育证据合成的方法论支架：Allison et al. (2016) 的分类直接锁定了哈蒂工作中最严重的计算错误与基线比较问题；McGraw & Wong 的数学公理直接[[Falsification|证伪]]了哈蒂报告的不可能概率；Borenstein et al. (2009) 的尺度要求揭示了公式混用与相关系数转换中的维度丢失；最后，Fisher 的统计哲学指明了教育学界单凭直觉处理海量数据所必然引发的认识论灾难，推导出全周期专业统计咨询的必要性。

---

> [!method-panel] 研究设计
> | 模块 | 材料与处理方式 |
> |------|----------------|
> | **统计学审计与方法学批判** | 从数理统计学家视角审查已有[[Meta-meta-analysis\|二阶元分析]]程序，重点核验计算公式、基线设定、符号界定及聚合逻辑。 |
> | **受控数值模拟反证** | 构造具有确定正态分布参数（$\mu=75, \sigma=5$）的四个平行实验组，分别代入三种标准效应量计算公式，检验其对教学干预排名的稳定性。 |
> | **极值与边界数学分析** | 针对相关系数转换公式 $d = \frac{2r}{\sqrt{1-r^2}}$ 与普通语言效应量开展极限分析，检验其在 $r \to 1$ 及方差为零条件下的数学收敛性。 |

> [!sample-panel]- 样本与材料快照
> | 样本层面 | 构成 |
> |----------|------|
> | **分析对象** | [[John Hattie\|约翰·哈蒂]] 2008 年专著《[[Visible Learning\|可见的学习]]》及其后续更新文献中涉及的统计合成方法、附录换算表与核心排序。 |
> | **关联[[Document\|文献]]** | 包含 Allison et al. (2016) 关于科学错误的《自然》评论、Topphol (2012) 挪威方法学批评、Legewie and DiPrete (2012) 性别成就实证及 Kim (2005) [[Creativity\|创造力]][[Meta-analysis\|元分析]]等。 |
> | **文本情境** | 《麦吉尔教育学刊》（McGill Journal of Education, MJE）论坛发表，因学术反响强烈由法文原版翻译为英文版发表。 |

---

> [!logic-map]- 核心论证逻辑链
> ```mermaid
> flowchart TD
>     A["问题起点：Visible Learning 庞大数据库的科学严谨性假象"]
>     B["初等计算失范：普通语言效应量产出负概率与超 100% 荒谬值"]
>     C["比较基线任意性：正负符号取决于主观选择，解释完全被动反转"]
>     D["度量标尺失效：受控实验证实三种有效公式产出完全矛盾排名"]
>     E["相关转换爆炸：极值发散且因果关系混淆，解释方差仅 3.85%"]
>     F["结论裁定：违背基本数理统计规范，整体体系沦为伪科学纸牌屋"]
>
>     A --> B
>     A --> C
>     B --> D
>     C --> D
>     D --> E
>     E --> F
> ```

---

### 论证步骤一　普通语言效应量计算违反初等概率公理

由 皮埃尔-热罗姆·伯杰龙（[[Pierre-Jérôme Bergeron]]） 与利桑·里瓦尔（Lysanne Rivard）开展的数理审计表明，《[[Visible Learning|可见的学习]]》表面上呈现由海量数字构筑的宏大结构，底层计算却存在严重数学缺陷。

> [!claim|lead] 步骤一核心主张
> [[John Hattie|哈蒂]]的方法论仅停留在平均值与未真正利用的标准差计算层面；其[[Meta-meta-analysis|二阶元分析]]包含初等计算错误，在普通语言[[Effect Size|效应量]]中算出了负概率与超过 100% 的荒谬数值。

> [!sub-claim] 1. 负概率与超额概率暴露基础数理失范

任何接受过基础统计训练的研究者均应知晓概率的严格数学边界，而哈蒂的二阶合成结果却汇报了负概率。

> [!ref-table] Cohen's d 与[[Common Language Effect Size|普通语言效应量]]（[[Common Language Effect Size]], CLES）规范对照
> | Cohen's $d$ | 0.00 | 0.20 | 0.40 | 0.60 | 0.80 | 1.00 | 1.20 | 1.40 | 2.00 | 3.00 |
> |---|---|---|---|---|---|---|---|---|---|---|
> | **普通语言效应量（CLES）** | 50% | 56% | 61% | 66% | 71% | 76% | 80% | 84% | 92% | 98% |
>
> **图表解读** 普通语言效应量（CLES）反映从实验组随机抽取一人得分高于对照组个体的概率。理论值域严格受限于 $(0\%, 100\%)$，当 $d=0$ 时为 50%。编制此基础对照表即可轻易识别附录中出现的负百分比与超 100% 概率等严重失误。

这一初等计算错误的长期存在，反映出研究团队在数理逻辑与质控上的严重缺失。

> [!critique-method] 统计咨询缺失引发的事后尸检困境
> - **事后尸检隐喻** 援引统计学家罗纳德·费希尔（Ronald Fisher）的经典论断：在实验结束后才去咨询统计学家，往往只是请他来做一场尸检，至多只能诊断出实验究竟死于什么原因。
> - **全流程缺失后果** 在研究方案设计、数据清洗与分析阶段缺乏经验丰富的专业统计学家介入，导致基础运算失误演变为教育决策依据。

> [!sub-claim] 2. 组间与组内公式混用破坏测度可比性

二阶[[Meta-analysis|元分析]]并置了两套数学逻辑完全不同的效应量公式，误认为二者因缺乏量纲即可直接对比。

> [!formula-set] 二阶元分析混同并置的两类效应量计算公式
> - **组间比较效应量**
>   $$\text{ES}_{\text{组间}} = \frac{\text{Mean}_{\text{实验组}} - \text{Mean}_{\text{对照组}}}{\text{标准差}}$$
>   度量不同被试组间的净差异，分母消除组间变异。
> - **前后比较效应量**
>   $$\text{ES}_{\text{前后}} = \frac{\text{Mean}_{\text{干预后}} - \text{Mean}_{\text{干预前}}}{\text{标准差}}$$
>   度量同一群被试的时间序列增长，分母消除个体成长变异。

两类公式在统计学上度量空间与假设完全不可[[Commensuration|通约]]，但在二阶元分析中却被直接混合取平均，导致跨研究排名的可比性彻底破产。

---

### 论证步骤二　效应量正负与优劣受制于主观基线设定

在初等计算失准之外，二阶元分析更深层的[[Epistemology|认识论]]危机在于对效应量相对性本质的完全无知。

> [!claim|lead] 步骤二核心主张
> 每一个效应量都是相对于特定基线总体的相对测量，哈蒂对基线选择的任意性毫无察觉，使得效应量的正负符号与优劣定性完全受制于主观设定的比对方向。

> [!sub-claim] 1. 比较基线反转彻底颠覆干预优劣定性

面对实证数据集，统计推断必须依循核心问题、测量[[Variable|变量]]、[[Study Population and Sample|目标总体]]、抽样方式以及分配机制进行情境化界定。

> [!case] 变量测量脱离情境的灾难性后果（挑战者号航天飞机案例）
> - **情境剥离风险** 脱离具体情境与测量层级（个体、学校、学区、国家）解释数据容易诱发严重误判。
> - **挑战者号历史教训** 1986 年挑战者号航天飞机发射决策所依据的数据分析，表面上显示环境温度与事故风险之间不存在显著关联；然而这一结论的根源在于分析人员在数据集中人为排除了所有未发生故障的正常发射批次（Kennet & Thyregod, 2006）。将不同学段、不同持续时间及不同测量工具的研究合并为单一均值，重蹈了剥离背景条件的覆辙。

哈蒂将负效应量断定为有害的逆向效应，然而在方法论上构成了典型的[[Inappropriate Baseline Comparisons|不当基线比较]]（Inappropriate Baseline Comparisons）：效应量的正负符号取决于对照基线的设定。

> [!tension-table] 基线反转引发的解释颠覆：[[Class Size|班级规模]]与[[Socioeconomic Status|社会经济地位]]案例
> | 考量因素与案例 | 正向设定（以常规或劣势组为基线） | 反向设定（以干预或优势组为基线） |
> |---|---|---|
> | **[[Class Size\|班级规模]]** | **小班比大班** $d \approx +0.20$<br>因低于 0.40 门槛，被武断判定为影响微弱、缺乏干预价值。 | **大班比小班** $d = -0.20$<br>依哈蒂负效应即有害的标准，结论转变为大班教学具有显著损害性。 |
> | **[[Socioeconomic Status\|社会经济地位]]（SES）** | **富裕比贫困** $d = +0.59$<br>被归因为学者无法改变的既定家庭背景，未能转化为政策行动焦点。 | **贫困比富裕** $d = -0.59$<br>逆转为全书负面冲击最大的要素，突显通过补偿性制度干预不平等的紧迫性。 |

> [!sub-claim] 2. 混淆影响因素与文献数量制造虚假均值

汇总异质研究时混淆总体的做法导致计算出的平均值缺乏现实统计解释力。

> [!critique-logic] 总体范畴混淆与虚假均值批判
> - **总体范畴混淆** 二阶元分析混淆了两个截然不同的总体：影响学业成功的现实因素总体，以及学术界针对这些因素所发表的研究数量总体。
> - **杂货店物价加权隐喻** 缺乏权重的算术平均如同走进杂货店根据商品标价罗列清单，因鱼子酱价格高昂就得出海鲜对家庭账单影响最大的推论；现实决策必须依据普通消费者的实际购买频率进行加权。
> - **疾病大杂烩聚合失范** 将癌症、糖尿病、镰刀型贫血症与消化系统疾病等发生率悬殊的健康问题合并为单一疾病效应，忽视了各疾病在学生总体中的实际患病率差异。
> - **性别差异实证脱节** 将所有性别差异研究生硬揉合，得出男孩学业成功优于女孩（$d=0.12$）的结论；然而绝大多数工业化国家的实证数据均表明女孩在[[Academic Achievement|学业表现]]上平均领先男孩，印证算术均值与经验现实严重脱节。

---

### 论证步骤三　三类合法公式对相同数据得出完全相反排名

受控数值模拟实验为二阶元分析的[[Incommensurability|不可通约性]]提供了确凿数理检验。

> [!claim|lead] 步骤三核心主张
> 受控数值模拟证实，跨研究设计的效应量缺乏普适通用标尺，三种在数学上完全合法的效应量计算公式对同一组数据得出了完全相反的排名，证明排行榜反映的是公式选择而非教学干预的真实效能。

> [!sub-claim] 1. 受控模拟证实干预排名取决于公式选择

在受控模拟环境中，四个独立学生组具有相同的初始成绩正态分布（$\mu=75, \sigma=5$），通过[[Random Assignment|随机分配]]实施不同教学法，组 0 为标准对照组（成绩增量为 0，$\sigma=0$），方法 1、2、3 平均分别增加 1、2、3 分，增加值的标准差分别为 1、2、3。

> [!design-notation] 四组受控随机教学[[Experimental Research|实验设计]]
> 参与者随机分配至三个实验组与一个对照组，施测[[Pre-test and Post-test|前测与后测]]：
>
> - **对照组（方法 0）** *R₀* ==O₁== `X₀` ==O₂==
> - **实验组 1（方法 1）** *R₁* ==O₁== `X₁` ==O₂==
> - **实验组 2（方法 2）** *R₂* ==O₁== `X₂` ==O₂==
> - **实验组 3（方法 3）** *R₃* ==O₁== `X₃` ==O₂==

针对完全相同的模拟数据，分别套用三类标准公式进行效应量计算与排名。

> [!row-contrast] 三类技术有效公式对同一受控实验数据的计算结果比对
> | 教学方法组别 | 公式 (a) 与对照组比较（组间） | 公式 (b) 前后比较（组内） | 公式 (c) 相关系数转换为 $d$ |
> |---|---|---|---|
> | **标准对照组（方法 0）** | 0.00 | N/A | $\infty$（无穷大） |
> | **教学方法 1** | 0.14 | 1.00 | 10.00 |
> | **教学方法 2** | 0.27 | 1.00 | 5.00 |
> | **教学方法 3** | 0.39 | 1.00 | 3.33 |
> | **方法优劣排名** | **$3 > 2 > 1 > 0$** | **$1 = 2 = 3$** | **$0 > 1 > 2 > 3$** |
>
> **图表解读** 公式 (a) 组间比较反映真实效果梯度（方法 3 最优）；公式 (b) 因分子增量与分母离散度同步扩大得出三者完全等价的误导性结论；公式 (c) 转化后判定未做改变的对照组无穷优于实验组，且增量最大的方法 3 排名最末。三类公式得出了彻底冲突的排名。

四组期末成绩与前后差值的分布形态揭示了公式背后的度量机制差异。

> [!figure]- 图 1　四组期末成绩分布曲线
> ![](https://img.mylikemie.icu/sources/Bergeron_2017_MJE/figures/Bergeron_2017_MJE_Fig1_Grade_Distribution.jpg)

> [!figure]- 图 2　四组前后成绩差值分布曲线
> ![](https://img.mylikemie.icu/sources/Bergeron_2017_MJE/figures/Bergeron_2017_MJE_Fig2_Distribution_Differences.jpg)

> [!sub-claim] 2. 相对离散度消除与一致性测量导致维度流失

不同计算公式所依据的统计假设造成了度量维度的系统性流失。

> [!critique-method] 维度流失与度量对象变质的数理机理
> - **公式 (a) 的组间噪声纳入** 测量新教学法相对于标准方法的组间增量，分母为跨组总变异，因而能够准确反映实际干预效果梯度。
> - **公式 (b) 的维度丢失** 仅测量组内成绩变化与其自身离散度的相对比值。当教学干预在提升平均分的同时成比例放大学生间变异时，相除操作直接消除了关键度量维度，导致异质干预被抹平为相同数值。
> - **公式 (c) 的噪声逆向度量** 相关系数转化实质上测量变化轨迹的线性一致性，脱离了均值增长本身；对照组成绩完全未变（变异为 0），其自相关为 1.0，转换后直接导致 $d \to \infty$；成绩提升越显著但变异越大的干预，相关性反而越弱，换算后效应量垫底。
> - **排行榜破产判定** 三种公式各自具有合理的数学基础，但在二阶元分析合成中未经区分地直接混合取均值，表明排行榜仅反映文献作者碰巧采纳的特定计算公式，无法代表教学方法的真实有效性。

---

### 论证步骤四　相关向均值差换算混淆因果并引发极值爆炸

借助公式将[[Correlational Research|相关性研究]]硬性转化为 Cohen's $d$，构成了二阶元分析中最具欺骗性的因果混淆环节。

> [!claim|lead] 步骤四核心主张
> 相关系数向 Cohen's $d$ 的换算公式在 $r \to 1$ 时呈爆炸性发散，且微弱相关即可虚增至[[Zone of Desired Effects|期望效应区]]；将相关性研究包装为因果干预效应量的做法彻底混淆了相关与因果，使整个理论体系滑入伪科学。

> [!sub-claim] 1. 换算公式导致弱关联虚增为高效应量

依据 Borenstein et al. (2009) 记录的跨尺度度量转换模型，相关系数向 Cohen's $d$ 的换算在数学上极其敏感，对数据度量空间有着严苛的先决假设。

> [!formula-step] 公式步骤　相关系数向 Cohen's d 换算的极值发散机制
> $$d = \frac{2r}{\sqrt{1 - r^2}}, \quad \lim_{r \to 1^-} d = +\infty$$
>
> **这个公式在做什么** 接收两变量间的[[Pearson Product-Moment Correlation|皮尔逊相关]]系数 $r$，尝试映射为标准化均值差 $d$。
>
> **数学直觉与边界** 当相关系数 $r$ 趋向于 1.0 时，分母迅速收敛至零，促使 $d$ 值产生爆炸性膨胀。更为危险的是，该公式对弱相关赋予了不成比例的高效应量。

这一公式缺陷直接导致了期望效应区的虚假建构。

> [!critique-method] 相关因果混淆实证案例：[[Creativity|创造力]]与[[Self-reported Grades|自我报告成绩]]
> - **弱相关跨入期望效应区** 仅仅需要 $r = 0.196$ 的微弱关联，代入公式即可产出 $d = 0.40$，从而跨入哈蒂所谓的[[Zone of Desired Effects|期望效应区]]。然而在一元线性回归模型中，$r = 0.196$ 对应的决定系数仅为 $R^2 = 0.0385$，意味着仅能解释 3.85% 的变异，剩余 96.15% 属于完全未解释的随机噪声。
> - **创造力横向相关假象** 金（Kim, 2005）的元分析被归结为[[Creativity|创造力]]对学业成就的显著影响，实际上该研究所依据的仅是智商（Intelligence Quotient, IQ）测验与创造力测验得分之间的横向相关，从未测量[[Creativity Training|创造力干预]]带来的因果增益。
> - **自我报告成绩榜首失范** 效应量雄居榜首的学生自我报告成绩，实质上只是一组学生预估分数与期末真实成绩之间的自相关，根本没有测量实施自我预估组与常规组之间的因果差异，却被包装为最强大的教学干预手段。

> [!sub-claim] 2. 伪科学体系呼唤全流程独立专业统计咨询

初等计算崩溃、基线任意性、公式矛盾与相关因果混淆，共同确立了二阶元分析的伪科学性质。

> [!critique-fatal] 违背数理统计规范的伪科学判定
> 约翰·哈蒂及其研究团队缺乏开展有效统计分析所必需的专业知识与核心技能。以真实数据编造脱离数理事实的故事，并在严肃批评提出后继续坚持辩护，构成了学术盲目与对伪科学的兜售；任何研究者均不应沿袭此种方法。

为避免海量实证数据沦为误导教育决策的伪证据，统计治理必须建立根本性的制度防线。

> [!pathways] 全流程独立专业统计咨询规程
> - **设计前介入** 在研究方案设计与数据收集前常态化引入资深统计学家，审定测量工具、抽样设计与基线比较逻辑，杜绝事后尸检困境。
> - **过程中核验** 在数据清洗与分析阶段严格审查度量空间假设，杜绝跨设计公式混用与相关系数无条件转换。
> - **发布前审计** 面对宏观证据库，必须依靠现代统计学与数据科学提供的严密工具开展独立复核，彻底终结单纯依靠数字规模堆砌的伪实证。

---

> [!finding-cards] 核心发现
> 1. **初等概率计算崩溃** 常见语言[[Effect Size|效应量]]计算出现严重失误，汇报了不可能出现的负概率与超过 100% 的概率数值，暴露其缺乏基本的数理审查。
> 2. **基线比较主观任意** 效应量的正负符号与量级完全受制于基线总体的选取，基线反转直接将[[Class Size|班级规模]]微弱正面效应逆转为有害效应、将贫困差距转化为全书最严重的负面损害。
> 3. **三类有效公式排名彻底颠倒** 针对完全相同的受控实验数据，组间比较、前后变化与相关转换三种技术有效公式得出了互不相容的排名，证明排行榜仅反映公式选择而非干预优劣。
> 4. **相关转换数学爆炸** $r \to d$ 换算公式在强相关下急剧发散，且仅需 $r=0.196$（仅解释 3.85% 方差）即可虚构出达到[[Zone of Desired Effects|期望效应区]]（$d=0.40$）的假象。
> 5. **相关因果混淆与伪科学定性** 将智商与[[Creativity|创造力]]相关、预期与真实成绩相关硬性包装为干预效应量，确证其整体二阶方法论属于用真实数据构建的伪科学纸牌屋。

> [!stat-cards]- 核心数据
> - **800+** 纳入综合的[[Meta-analysis|元分析]]总数量。
> - **50,000+** 二阶数据库涵盖的原始实证研究总数。
> - **$r=0.196 \to d=0.40$** 仅需 0.196 的微弱相关即可换算为期望效应区临界值。
> - **$R^2 = 3.85\%$** 达到期望效应区门槛的线性回归模型所能解释的方差比例，剩余 96.15% 为随机噪声。
> - **$d = 0.59 \to -0.59$** [[Socioeconomic Status|社会经济地位]]在基线反转前后的极端效应量落差。
> - **$d \to \infty$** 对照组在零方差自相关条件下代入公式 (c) 产生的极限发散值。

---

> [!citation-card] 审视[[Visible Learning|可见的学习]]的纸牌屋本质
> 当以专业专家的眼光对《可见的学习》展开必要的深入审视时，所见全无坚固城堡的结构，唯有一座迅速崩塌的脆弱纸牌屋。
>
> *When taking the necessary in-depth look at Visible Learning with the eye of an expert, we find not a mighty castle but a fragile house of cards that quickly falls apart.*

> [!citation-card] 辩护伪科学构成蓄意盲目
> 轻信[[John Hattie|哈蒂]]意味着在评估科学严谨性时存在[[Critical Thinking|批判性思维]]的盲点；推崇其工作不幸陷入了对伪科学的宣介；而在获知对其方法论的严肃批评后仍坚持为其辩护，则构成了蓄意的学术盲目。
>
> *To believe Hattie is to have a [[Blind Spot in Observation|blind spot]] in one's critical thinking when assessing scientific rigor. To promote his work is to unfortunately fall into the promotion of pseudoscience. Finally, to persist in defending Hattie after becoming aware of the serious critique of his methodology constitutes willful blindness.*

> [!citation-card] [[Effect Size|效应量]]基线比较的武断性
> 哈蒂所作的基线比较完全出于主观臆断，而其自身对此毫无察觉。
>
> *Hattie's comparisons are arbitrary and he is completely unaware of it.*

> [!citation-card] 算术平均掩盖极端方差与无意义均值
> 归根结底，哈蒂计算出的平均值缺乏实质统计学意义。
>
> *Basically, Hattie computes averages that do not make any sense.*

> [!citation-card] 拒绝伪科学与全流程统计咨询原则
> 显而易见，约翰·哈蒂及其团队既不具备也不掌握开展有效统计分析所必需的专业知识与核心技能。任何研究者都不应沿袭此种方法，学术界绝不能接纳伪科学。这一局面令人深感遗憾，因为依靠数百项[[Meta-analysis|元分析]]的数据完全能够开展真正的科学研究。
>
> *It is clear that John Hattie and his team have neither the knowledge nor the competencies required to conduct valid statistical analyses. No one should replicate this methodology because we must never accept pseudoscience. This is most unfortunate, since it is possible to do real science with data from hundreds of meta-analyses.*

---

> [!warning] 自述局限
> - **专栏篇幅限制** 受限于期刊专栏篇幅，未对二阶数据库涵盖的 800 余项一阶[[Meta-analysis|元分析]]逐一进行详尽的统计勘误与分类。
> - **复杂建模细节省略** 多水平建模涉及剂量反应曲线、空间[[Heterogeneity|异质性]]与时滞效应，未展开具体数理推导细节。
> - **未展开替代推断方案** 分析重心在于解构现有指标与换算程序的统计缺陷，未提供基于数百项元分析提取真实科学结论的完整统计推断替代框架。

---

## 来源

- [[sources/Bergeron_2017_MJE/Bergeron_2017_MJE|Bergeron_2017_MJE]]
