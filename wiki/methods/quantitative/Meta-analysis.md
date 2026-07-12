---
title: Meta-analysis
aliases:
  - 元分析
summary: "通过汇总多项原始研究的效应量来综合证据的统计方法，常用于比较干预强度、估计平均效果和检验结果一致性"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 61
method_related_level: 6
method_related_stars: "⭐⭐⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
- meta-analysis
- effect-size
- evidence-based-education
- statistical-synthesis
- methodology
related_concepts:
  - "[[Effect Size]]"
  - "[[Evidence-Based Education]]"
  - "[[Forest Plot]]"
  - "[[Sample Size Determination]]"
  - "[[Epistemology]]"
  - "[[Hypothesis]]"
  - "[[Ontology]]"
  - "[[Visible Learning]]"
  - "[[Variable]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Sampling Error]]"
  - "[[Fitness for Purpose]]"
  - "[[Reliability]]"
  - "[[Statistical Significance]]"
  - "[[Research Utilization]]"
  - "[[Class Size]]"
  - "[[Publication Bias]]"
  - "[[Critique of Meta-analysis]]"
  - "[[Document]]"
  - "[[Whole Language]]"
  - "[[Homework]]"
  - "[[External Validity]]"
  - "[[Heterogeneity]]"
  - "[[Research Question]]"
  - "[[Feedback]]"
  - "[[Research Purpose]]"
  - "[[Sociology of Valuation and Evaluation]]"
  - "[[Literature Review]]"
related_theories:
  - "[[Critical Realism]]"
related_methods:
  - "[[Randomised Controlled Trials]]"
  - "[[Moderator Analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Analysis of Variance]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Systematic Review]]"
  - "[[Quantitative Research]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Experimental Research]]"
  - "[[Observation Method]]"
  - "[[Random Assignment]]"
related_persons:
  - "[[Gene Glass]]"
  - "[[Karl Pearson]]"
related_arguments:
  - "[[Argument_Wrigley_2019_ERE]]"
  - "[[Argument_Higgins_2016_RE]]"
  - "[[Argument_Wiliam_2019_ERE]]"
  - "[[Argument_Qvortrup_2015_Paideia]]"
  - "[[Argument_Qvortrup_2019_NordSTEP]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
  - "[[Argument_Snook_2009_NZJES]]"
  - "[[Argument_Snook_2010_NZJES]]"
  - "[[Argument_Berk_2011_ER]]"
  - "[[Argument_Simpson_2017_JEP]]"
  - "[[Argument_Terhart_2011_JCS]]"
  - "[[Argument_OConnor_2020_AJLL]]"
  - "[[Argument_ONeill_2012_NZJES]]"
  - "[[Argument_Hattie_2015_Paideia]]"
  - "[[Argument_Hattie_2015_SOTLP]]"
  - "[[Argument_Wrigley_2018_BERJ]]"
related_facts:
  - "[[EEF Teaching and Learning Toolkit]]"
  - "[[Education Endowment Foundation]]"
confidence: medium
status: draft
created: '2026-05-01'
updated: 2026-07-08
---

## 定义

> [!info] 定义
> 元分析是一种统计方法，通过计算多项原始研究的平均[[Effect Size|效应量]]来综合研究证据。它由 [[Gene Glass]] 于 1976 年提出，最初旨在系统性地总结某一主题的研究发现。在[[Evidence-Based Education|证据本位教育]]中，元分析被用作综合[[Randomised Controlled Trials|随机对照试验]]证据的核心工具，其结论（平均效应量）被视为"什么有效"的主要证据来源([[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, p. 118]])。
>
> 元分析有两个核心目标：判断某一干预或方法总体上是否有效，以及通过[[Moderator Analysis|调节变量分析]]解释研究间效果的变异([[Argument_Higgins_2016_RE|Higgins, 2016, p.32]])。
>
> [[Argument_Wiliam_2019_ERE|Wiliam (2019, p.11)]] 在定义上增加了关键的层级区分：元分析综合原始研究的效应量；而[[Meta-meta-analysis|元-元分析]]是通过效应量的加权合并综合多个元分析的结果，是另一回事。Wiliam 断言后者在教育政策制定中绝对没有任何角色。

## 历史发展

> [!note]- 历史发展
> **思想先驱：Pearson（1904）**
>
> [[Karl Pearson|Karl Pearson]] 在 1904 年《英国医学杂志》上发表了最早的跨研究合并分析——合并英国军队在印度和南非的伤寒疫苗接种数据。他同时追求两个目标：合并多项小研究的发现以获得更可靠结论，以及探索研究间效果变异的原因（如志愿者自我选择偏差）。这两个目标构成了[[Meta-analysis|元分析]]的核心概念。他将每项研究结果以独立行呈现并给出平均相关系数的呈现方式，预示了后来[[Forest Plot|森林图]]（forest plot）的标准形式([[Argument_Higgins_2016_RE|Higgins, 2016, p.33]])。
>
> **Fisher 的统计基础（1930s–1950s）**
>
> Ronald Fisher 在[[Analysis of Variance|方差分析]]等技术上的发展为跨研究比较奠定了统计基础。Fisher 鼓励研究者清晰严格地报告发现，使跨研究的比较和聚合变得更容易([[Argument_Higgins_2016_RE|Higgins, 2016, p.34]])。
>
> **命名与确立：Glass（1976）**
>
> [[Gene Glass|Gene Glass]] 于 1976 年在美国教育研究协会主席演说中首次提出"元分析"一词。他与 Mary Lee Smith 合作的心理治疗效果元分析（Smith & Glass, 1977）发现平均[[Effect Size|效应量]]为 0.6 个标准差，直接挑战了 Eysenck 的"心理治疗无效"共识。Glass 将[[Effect Size|效应量]]（标准差单位）确立为跨研究比较的通用尺度，并承认 Robert Rosenthal 发展了效应量的基础度量([[Argument_Higgins_2016_RE|Higgins, 2016, pp.36–37]])。
>
> **医学领域的发展（1970s–1980s）**
>
> Peter Elwood 和 Archie Cochrane 等人通过阿司匹林预防心脏病发作的随机试验，展示了[[Meta-analysis|元分析]]在医学证据综合中的力量。Richard Peto 推广了[[Fixed-Effect and Random-Effects Models|固定效应模型]]（按精度加权）。Larry Hedges（1983）倡导随机效应模型，DerSimonian & Laird（1986）提供了简化的计算公式([[Argument_Higgins_2016_RE|Higgins, 2016, pp.38–39]])。
>
> **"苹果和橙子"争论（1980s）**
>
> Eysenck 称元分析为"超级愚蠢"，批评其将不可比的研究混为一谈。Slavin（1984）同样提出"苹果和橙子"问题。Glass 的回应是："当然它混合苹果和橙子；在研究水果时没有别的合理做法"——任何推论都直接取决于元分析所包含的内容([[Argument_Higgins_2016_RE|Higgins, 2016, p.37]])。
>
> **[[Systematic Review|系统综述]]的制度化（1990s–2000s）**
>
> 1993 年 Cochrane 协作网成立，将系统综述和元分析制度化为医学证据综合的标准方法。Chalmers & Altman（1995）主张"元分析"一词应仅用于定量综合。2009 年，PRISMA（系统综述和元分析优先报告条目）声明发布，为系统综述的透明报告提供了标准化框架（Moher et al., 2009, cited in [[Argument_Higgins_2016_RE|Higgins, 2016, p.38]]）。
>
> **在教育领域的扩展（1990s–2010s）**
>
> 元分析在教育研究中的应用从 1990 年代起迅速扩展。Hattie（1992）综合了 134 项元分析，2008 年扩展至 800 多项。[[EEF Teaching and Learning Toolkit]]（2011）将元分析结果转化为面向实践者的政策工具。然而，[[Sample Size Determination|样本量]]与效应量之间的系统性相关（相关系数 –0.28）表明该领域仍面临方法论挑战（Cheung & Slavin, 2015, cited in [[Argument_Higgins_2016_RE|Higgins, 2016, p.48]]）。

---

## 认识论立场

> [!abstract] [[Epistemology|认识论]]立场
> 元分析隐含经验主义认识论：[[Hypothesis|假设]]通过对多个研究的[[Effect Size|效应量]]进行统计平均，可以产生关于干预有效性的可靠知识。[[Critical Realism|批判实在论]]从三层[[Ontology|本体论]]（实在/实际/经验）角度批评这一假设——元分析停留在"经验"层面（观察到的效应量），未能深入"实在"层面（产生效应的因果机制及其激活条件）([[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, pp. 116–117]])。

## 操作步骤

> [!example] 操作步骤
> 1. **选择源研究** 基于技术标准（如是否为 [[Randomised Controlled Trials|RCT]]）筛选相关研究
> 2. **提取[[Effect Size|效应量]]** 从每项源研究中提取或计算标准化效应量
> 3. **加权与平均** 对效应量进行加权（通常按[[Sample Size Determination|样本量]]），计算平均效应量
> 4. **报告** 以平均效应量（有时转换为更直观的单位，如 [[Education Endowment Foundation|EEF]] Toolkit 的"额外学习月数"）呈现结果
>
> [[Meta-meta-analysis|元-元分析]]（Meta-meta-analysis）是在元分析基础上进一步聚合——综合多个元分析的效应量产生更高层次的排名或估计。Wecker, Vogel & Hetmanek（2016）从[[Fixed-Effect and Random-Effects Models|固定效应模型]]推导了该方法必须满足的 6 项方法论要求（包括公式 1-9 的完整数学推导和等价性证明），并论证 Hattie 的 *[[Visible Learning]]* 在六个分析步骤中均存在方法论不足。完整技术细节见 [[Meta-meta-analysis]]。

### 详细操作流程

Glass et al.（1981）和 Hunter et al.（1982）提出了八步程序（pp.105–118）：

1. 确定关注的[[Variable|变量]]（[[Independent Variable|自变量]]和[[Dependent Variable|因变量]]）
2. 识别所有涉及这些变[[Quantitative Research|量的研究]]
3. 对每项研究[[Coding in Qualitative Research|编码]]可能预测结果和效应量的特征（如参与者年龄、性别、种族、干预持续时间）
4. 计算每对变量（因变量和自变量）的效应量（见 Glass, 1977），按样本量加权
5. 计算跨研究效应量的均值和标准差（跨研究方差）
6. 确定[[Sampling Error|抽样误差]]、测量误差和范围限制的影响
7. 如果方差的大部分可归因于步骤 6 的问题，平均效应量可被视为变量间关系的准确估计
8. 如果方差的大部分不可归因于步骤 6，则审查与效应量相关的特征

Cook et al.（1992: 7–12）提出了四阶段整合性综述模型（pp.120–132）：

1. **问题形成** 高质量元分析必须在综述的设计、执行和分析上保持严谨
2. **数据收集** 纳入研究的抽样必须展示[[Fitness for Purpose|目的适配性]]
3. **数据检索与分析** 处理非[[Experimental Research|实验研究]]（整合性综述即属此类）中的效度威胁——效度必须展示目的适配性、编码[[Reliability|信度]]，并关注原始研究的方法论严谨性
4. **分析与解释** 多项研究的累积发现应被视为复杂数据点，需要通过细致的统计分析来解释

Fitz-Gibbon（1984: 141–142）的四步法（pp.134–142）：

1. 寻找可计算效应量的研究（已发表和未发表）
2. 编码研究特征（日期、发表状态、设计特征、设计质量、研究者身份）
3. 测量效应量（将实验组定位为控制组分布中的 z 分数），使结果可在共同尺度上测量，控制"块状数据"（大数据集中的非独立数据）
4. 将效应量与情境变量相关（如区分控制良好和控制不佳的研究）

Gorard（2001b: 72–73）的四步模型（pp.194–202）：

1. 收集所有适合纳入的研究
2. 按规模和质素对每项研究加权
3. 列出使用的结果测量
4. 根据收集的数据性质选择聚合方法（如计数出现效应的研究和不出现效应的研究，或计算跨研究的平均效应量）

### 效应量计算

效应量是元分析中优先于[[Statistical Significance|统计显著性]]的统计量。Wood（1995: 393）建议效应量可通过将显著性水平除以样本量来计算。Glass et al.（1981: 29, 102）计算效应量为（pp.144–150）：

$$\Delta = \frac{M_{\text{实验组}} - M_{\text{对照组}}}{SD_{\text{控制组}}}$$

Hedges（1981）和 Hunter et al.（1982）提出了考虑样本量差异的不同权重的替代公式。Lipsey（1992: 93–100）列出处理效应量、效应量均值和同质性的系列统计检验。最常用的效应量指标是标准化均值差和相关系数（Glass et al., 1981: 373），尽管非参数统计量（如中位数）也可使用（pp.150–151）。

---

## 适用场景

> [!success] 作为效果总体估计的工具
> - 当有大量使用可比较设计和结果测[[Quantitative Research|量的研究]]时，元分析可以提供效果的总体估计
> - 在医学领域（其起源领域），元分析在已有充分理论理解治疗机制的前提下可以补充回答"效果平均多大"
> - 元分析对教育研究尤其重要，因为许多小型研究具有中等或较低的效果，可能无法达到[[Statistical Significance|统计显著性]]。Cooper & Rosenthal（1980）的实证检验表明，元分析比传统叙事综述更不容易低估证据。Gorard（2014）同样指出，合并小型研究可以提供答案，而不必过度依赖与[[Sample Size Determination|样本量]]直接相关的统计显著性([[Argument_Higgins_2016_RE|Higgins, 2016, p.32]])
> - 教育领域中使用元分析的倡导者认为它适合为实践者和政策制定者提供关于"什么有效"的总结性指导([[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, pp. 110–111]])

> [!success] 作为追问变异和调节[[Variable|变量]]的工具
> - Hattie（2015）从支持者立场强调，元分析最有价值的用法不是把平均效应当成最后答案，而是迫使教育者追问调节[[Variable|变量]]和竞争解释：哪些年龄、学段、文化、先前成绩和结果测量类型会改变效果，平均值背后的变异说明了什么（Hattie, 2015, pp.10–11, 14–15）
> - [[Argument_Qvortrup_2015_Paideia|Qvortrup (2015, pp.25–27)]]从支持者立场认为，教育元分析不需要等待所有[[Research Utilization|研究使用]]完全相同的学习结果定义才可比较；[[Effect Size|效应量]]提供的是干预组与控制组或干预前后之间的相对效果，因此可以跨研究比较"相对学习结果"。但这种比较的代价是学习结果变得抽象，研究者难以说明测量的是表层知识、深层理解、社会能力还是概念性学习([[Argument_Qvortrup_2015_Paideia|Qvortrup, 2015, p.27]])
> - [[Argument_Qvortrup_2019_NordSTEP|Qvortrup (2019, p.5)]]从支持者立场提出"观察透镜"论证：元分析是系统观察的一种形式，所有观察都从特定位置和特定透镜进行，元分析透镜产生的图像与定性[[Observation Method|观察研究]]的图像不同但互补——前提是两者均遵循高效度标准
> - [[Argument_Wiliam_2019_ERE|Wiliam (2019, p.11)]]的谨慎立场：如果且仅当满足 11 项条件，元分析才可能值得严肃对待

> [!example]- 案例：[[Class Size|班级规模]]与学习成就（Glass & Smith, 1978）
> Glass & Smith（1978）和 Glass et al.（1981: 35–44）识别了 77 项关于班级规模与学生学习的实证研究。这些研究产生了 725 项关于较小班级和较大班级成就的比较，数据累积来自近 90 万名各年龄段和能力的学生，学习各学科。使用回归分析，725 项比较被整合为一条显示班级规模与成就关系的单一曲线。该曲线揭示了班级规模与学生学习之间存在明确的负相关。当研究者为不同情境（如年级水平、学科、学生能力等）推导类似曲线时，几乎没有任何特殊情境改变了这一基本关系。只有一个因素显著影响了曲线——原始研究是否在将学生和教师分配到大小班级时进行了充分的实验控制。控制充分和不充分的曲线见图 17.1。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|(Cohen et al., 2011, Ch17, pp.237–244)]]

---

## 局限性

> [!warning] 批判总览
> 元分析面临来自方法论前提、操作程序、统计推断和政策用途等多层面的系统批判，涵盖研究可比性（苹果和橙子问题）、输入质量（垃圾进垃圾出）、[[Publication Bias|发表偏倚]]、非独立数据、过度简化、伪精确性、抽样与伦理问题等。详细的批判维度与回应见 [[Critique of Meta-analysis]]。以下聚焦已被其他[[Document|文献]]深入讨论的关键局限。
> **Eysenck (1978) — 垃圾进，垃圾出**
>
> Eysenck（1978, p.517）对元分析提出了著名的早期批评，指出元分析的不加区分性质——每个与选定领域相关的研究都被用于计算[[Effect Size|效应量]]，而不论不同研究的质量或严谨性：
>
> > "大量报告——好的、坏的和平庸的——被输入计算机，希望人们不再关心结论所基于的材料的质量。……'垃圾进——垃圾出'是计算机专家熟知的格言；它在这里同样有力。"（引自 O'Connor, 2020, p.143）
>
> 这一批评奠定了后续所有元分析方法论批评的基础命题：**聚合的质量取决于输入的质量**。
>
> **[[Argument_Snook_2009_NZJES|Snook et al. (2009)]] — 元分析在教育领域的五项方法论问题**
>
> [[Argument_Snook_2009_NZJES|Snook et al. (2009, pp.96–98)]]在《[[Visible Learning|可见的学习]]》出版同年识别了元分析在教育中应用的五项特有局限：
>
> 1. **偏差不受控** 设计不良研究的元分析（无论设计多好）不可避免地导致不可靠结论（p.96–97）
> 2. **[[Publication Bias|发表偏差]]** 支持有利结论的研究更可能被发表——在药物公司资助的研究和利润丰厚的教育时尚（如学习风格）中尤其严重（p.97）
> 3. **教育[[Variable|变量]]难以清晰界定** 与医学中"药物 A vs 药物 B"不同，"以儿童为中心 vs 以教师为中心"等教育变量通常处于连续谱上，主观判断不可或缺。Hattie 本人承认[[Whole Language|全语言]]的两项元分析因分类差异导致结论矛盾（p.97）
> 4. **平均化消除复杂性** 以[[Homework|家庭作业]]为例，总体 d=0.29 掩盖了小学 d=0.15、中学 d=0.64 以及数学、科学、社会研究之间的巨大差异（p.97）
> 5. **[[External Validity|可推广性]]有限** 大多数研究来自美国等英语发达国家，不可直接推广至非英语或发展中国家——在发展中国家学校效应（相对于教师效应）远更大（p.97–98）
>
> **"苹果和橙子"问题（1980s–）**
>
> 根本不同的研究（不同学生年龄、课程领域、先前成就水平、干预时长、结果测量类型）被聚合产生单一的平均效应量。[[Gene Glass]]——元分析的创始人——本人警告："元分析的结果永远不应该是平均值；它应该是一张图"（Robinson, 2004, p. 29, cited in [[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, p. 119]]）。
>
> Hattie (2015) 对这一问题的回应不是否认[[Heterogeneity|异质性]]，而是要求把异质性转化为[[Research Question|研究问题]]：平均效应必须继续追问调节变量。例如 [[Feedback]] 的平均效应很强，但 Hattie 自己也承认反馈类型、反馈方向和学生接收方式会使效果差异很大，不能用”反馈有效”替代对具体机制的判断（Hattie, 2015, p.11）。

> [!warning] 看似客观的数字背后
> 元分析产出一个精确的效应量数字，给人以客观的印象。但同一主题的不同元分析可能得出不同的汇总效应量，差异来自研究者在研究问题、纳入标准和分析程序上的选择。以语音教学为例([[Argument_Higgins_2016_RE|Higgins, 2016, p.32]])：
>
> | 元分析 | 汇总效应量 | 各自的调节变量结论 |
> |--------|-----------|------------------|
> | Ehri et al. (2001) | 0.41 | 较早开始语音教学更有价值 |
> | Jeynes (2008) | 0.27 | 发现在不同质[[Quantitative Research\|量的研究]]中具有稳健性 |
> | Torgerson et al. (2006) | 0.30 | 没有证据表明综合语音优于分析语音 |
>
> 三项元分析研究的是同一个干预，但汇总效应量从 0.27 到 0.41 不等，对调节变量的结论也各不相同。差异不是来自随机误差，而是来自研究者对”什么算语音教学””纳入哪些研究””如何处理质量差异”等问题的不同判断。元分析的数字看起来比叙事综述更客观，但数字背后仍然嵌入了研究者的分类选择和纳入决定。

> [!warning] 可比性问题的具体案例
> **家庭作业的分类困境([[Argument_Higgins_2016_RE|Higgins, 2016, pp.37–38]])**
>
> 教育中使用的许多一般术语看似明确，实则模糊。以”家庭作业”为例，以下是否都是同一回事？
> - 五岁儿童带书回家与父母共读
> - 在家背单词
> - 在”作业俱乐部”中做作业（实际在学校而非家中）
> - 为课堂做预习阅读
> - 为考试背乘法表
> - 在家完成考试课程作业
>
> 如果合并所有这些研究得出”作业有效”，这并不意味着作业总是有效的。它表明当人们试验作业是否有效时，大体答案是肯定的。要做出实践判断，还需要知道包含的是哪类作业研究、学生年龄、频率和规律性等信息。
>
> **三种效果量不可混为一谈([[Argument_Higgins_2016_RE|Higgins, 2016, p.44]])**
>
> 干预效果（相对于比较组的改善）应区别于成熟差异（单组设计）。相关效果（如作业与学业表现之间的关系）与干预效果（有作业与无作业的比较）本质不同。这些研究中教育成就的底部分布可能不同，使比较失去意义。

> [!warning] 嵌套数据结构与[[Sample Size Determination|样本量]]偏差
> **聚类效应([[Argument_Higgins_2016_RE|Higgins, 2016, p.40]])**
>
> 学校中学生的嵌套或聚类结构常未被考虑。学生在班级中，班级在学校中，两者都可能影响不同方法的效果。不考虑这一点可能导致效果被高估（Campbell et al., 2012; Raudenbush, 1997）。
>
> **样本量与效应量的系统性相关([[Argument_Higgins_2016_RE|Higgins, 2016, p.48]])**
>
> 较大型研究报告较小的效果，样本量与效应量之间的相关系数为 –0.28（Cheung & Slavin, 2015; Slavin & Smith, 2009）。这种变异究竟来自[[Publication Bias|发表偏差]]、试验类型和阶段的影响（试点研究往往报告更高的效应量），还是超级实现偏差（Cronbach et al., 1980）的其他方面，尚不清楚。
>
> **源研究选择的纯技术标准**
>
> 元分析通常基于技术质量（如 [[Randomised Controlled Trials|RCT]] 设计）而非理论相关性选择源研究，且讨论部分的理论内容在最终报告中往往消失([[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, pp. 119, 123]])。
>
> **发表偏倚**
>
> 学术发表对[[Statistical Significance|统计显著性]]的偏好可能筛选掉"效应量可观但统计不显著"的结果，使元分析平均值系统性地高估真实效应。详见 [[Publication Bias]]。
>
> **源研究不充分问题**
>
> [[Education Endowment Foundation|EEF]] Toolkit 的体育参与条目仅基于三个元分析中的四个效应量([[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, pp. 121–122]])。
>
> **[[Argument_Snook_2010_NZJES|Snook et al. (2010)]] — 元分析从医学到教育的移植问题**
>
> [[Argument_Snook_2010_NZJES|Snook et al. (2010, p.96)]]在回应 Hattie（2010）时，提出了一个常被忽略的更深层问题：元分析技术起源于医学科学——医学有经过仔细界定的概念和严谨的（通常为实验性）研究设计。然而在教育领域，"被研究的变量往往概念化差，研究也经常不够严格"：
>
> > "如何为[[Research Purpose|研究目的]]清晰区分一个'以教师为中心'和一个'以学生为中心'的课堂？在比较它们时，如何在一个嘈杂繁忙、可能有 30 多个参与者的课堂中控制所有变量？"
>
> 经过四十年课堂细粒度研究，Graham Nuthall（2007, p.16）得出结论：虽然有大量已发表的教育研究报告，但"在识别那些对课堂教学有值得信赖的内容的研究时，你需要非常有选择性"([[Argument_Snook_2010_NZJES|Snook et al., 2010, p.97]])。Snook et al. 以 Nuthall 的 The Hidden Lives of Learners（基于数十年新西兰课堂研究）与 Hattie 的《可见的学习》（基于国际元分析）的书名对比，暗示两者在[[Epistemology|认识论]]取向上存在本质差异。
>
> 这一批评的核心在于：元分析在医学中成功运作的条件（概念清晰、设计标准化、机制可分离）在教育领域经常不成立——这不是方法论执行缺陷的问题，而是方法本身与研究对象之间的基础性不匹配。


> [!warning] 平均效应的误导性与因果信息的丧失
> **Kluger & DeNisi (1996) — 反馈元分析：平均效应的误导性案例**
>
> [[Argument_Wiliam_2019_ERE|Wiliam (2019, pp.10–11)]]以 Kluger & DeNisi的反馈元分析为例展示平均效应量的误导性：
>
> - 131 项研究、607 个效应量，平均效应量约 0.4 个标准差——这使 Hattie（1999）提出"改善教育的最简单处方必须是大量的反馈"
> - 然而效应量的标准差约为 **1**（即效应量分布极为分散），约 **38% 的效应量为负**——在超过三分之一的案例中，给予反馈反而比不给予反馈更差
> - Wiliam 指出：不了解干预如何产生效果，在特定情境中应用干预可能产生持续负效果——对[[Evidence-Based Education|证据本位教育]]倡导者而言"反馈可能适得其反"不是相关的替代状态；对教师而言高度相关
>
> > "在他们考察的案例中，超过三分之一的情况下，不给予反馈反而更好。"([[Argument_Wiliam_2019_ERE|Wiliam, 2019, p.10]])
>
> **Pawson (2006) — 因果信息的系统性消除**
>
> Pawson（2006, pp.42-43, 72）论证在元分析综述的每一阶段，解释干预如何起作用的关键特征被系统性地从考虑中消除：
>
> > "[[Hypothesis|假设]]被删节、研究被丢弃、项目细节被过滤、情境信息被消除、选定发现被利用、平均值被计算、估计被做出……这种简化、标准化和聚合的过程不产生任何持久的真理。它产生的描述性总结很可能令人失望、误导或需要进一步澄清。"（引自 O'Connor, 2020, p.143; 另见 Wrigley & McCusker, 2019, p. 122）


> [!warning] 效应量与统计推断的方法论缺陷
> **[[Argument_Berk_2011_ER|Berk (2011)]] — 不可比研究、有偏估计与统计推断的三重批判**
>
> [[Argument_Berk_2011_ER|Berk (2011, pp.198–199)]] 基于 35 年编辑经验，对元分析在因果效应估计中的使用提出了三重批判：
>
> **1. 研究不可比导致平均效应无政策意义**
>
> "当被合并的研究不是可比较的随机实验时，元分析开始脱轨"([[Argument_Berk_2011_ER|Berk, 2011, p.198]])。Berk 给出具体例证：如果合并职业培训研究和职业咨询研究，发现平均而言"效果有益"——这对政策意味着什么？应该增加培训项目、咨询项目，还是两者都增加？"在跨处理的平均值中，没有证据表明任何一种干预单独有效，也没有证据表明两者一起引入时都有效"([[Argument_Berk_2011_ER|Berk, 2011, p.199]])。标准化效应量的常规做法只是掩盖了这个问题。
>
> **2. 有偏估计不会相互抵消**
>
> "当研究不是随机实验时，极有可能正在合并一组有偏的处理效应估计。这如何使人更好？有偏估计不是随机误差，不会相互抵消。结果可能只是一个更精确的因果估计，但符号错误且系统性地过大或过小"。
>
> **3. 统计推断的基本假设几乎从未被满足**
>
> 在缺乏[[Random Assignment|随机分配]]的情况下，元分析的统计推断"变得非常难以辩护"（Berk, 2007）。必须假设被合并的研究是"所有可能（或已完成）研究的一个概率样本，且研究之间彼此独立实现"。Berk 指出："随便做一下项目[[Sociology of Valuation and Evaluation|评估社会学]]就会发现，综述的研究不是任何真实事物的概率样本。而独立性的通常要求意味着研究者不阅读彼此的工作、不在学术会议上讨论这些工作、从不合作、也不雇佣彼此的学生"。
>
> > "简言之，元分析在因果效应估计中的重要性被严重高估了。传统的[[Literature Review|文献综述]]往往做得更好。至少，读者不会被伪装成统计花招的统计不当操作所迷惑。"
>
> **[[Argument_Simpson_2017_JEP|Simpson (2017)]] — 元分析两项核心假设的系统性违背**
>
> [[Argument_Simpson_2017_JEP|Simpson (2017, pp.4–5)]]论证教育元分析依赖两项核心假设，两者均被系统性地违背：
>
> 1. **可比较性假设** 效应量更大的干预通常与更大的教育显著性相关联——即效应量可以跨不同研究进行比较
> 2. **可合并性假设** 不同研究的效应量可被合并产生有意义的估计
>
> 三个系统性偏差来源（详细论证见 [[Effect Size#Simpson (2017) 的三大系统性偏差：原始论证]]）：
> - **比较组的不对等性** 不同[[Research Utilization|研究使用]]不同比较基线（无干预 vs 替代处理 vs 照常教学），使效应量不可比——"一个分析的实验组是另一个分析的控制组"([[Argument_Simpson_2017_JEP|Simpson, 2017, p.7]])；Camilli et al. (2010) 发现比较"无干预"的效应量是"替代处理"的 3 倍以上
> - **范围限制** 选择窄化样本减小方差→放大效应量，10,000 次模拟显示中等能力组效应量膨胀 40%([[Argument_Simpson_2017_JEP|Simpson, 2017, pp.8–9]])；Elbaum et al. (2000) 故意选择阅读失败风险学生的元分析在 EEF Toolkit 中与未限制范围的元分析合并且未调整
> - **测量设计（聚焦度+精确度）** 研究者自编测试效应量比标准化测试平均高约 40%([[Argument_Simpson_2017_JEP|Simpson, 2017, p.12]])；测试长度翻倍可膨胀效应量 ~20%–100%+（Figure 3）——Kluger & DeNisi (1996) 中测试从 6 任务到 300 算术题，未调整
>
> **关键洞察** 这些偏差不是随机噪声。偏差随研究领域系统性变化：反馈研究容易使用无反馈比较、限制样本范围、设计聚焦测试；而延长学校日或校服研究无法做到这些。元分析合并效应量时，实际合并的是不同领域中不同程度的研究设计操纵自由度([[Argument_Simpson_2017_JEP|Simpson, 2017, pp.5–14]])。详见 [[Effect Size]]、[[Argument_Simpson_2017_JEP]]。


> [!warning] [[Meta-meta-analysis|元-元分析]]（二级聚合）的特有局限
> **[[Argument_Terhart_2011_JCS|Terhart (2011)]] — 稳定性/变异性双重困境**
>
> Terhart识别了元-元分析的特有问题：信息在聚合层级间系统性损失、稳定性/变异性双重困境、纳入标准不透明、数据库质量异质。详见 [[Meta-meta-analysis]]。
>
> **LeLorier et al. (1997) — 偏倚在聚合层级间传播**
>
> LeLorier et al.在医学[[Document|文献]]中已警告偏倚在聚合层级间传播——一级聚合的偏倚在二级聚合中被进一步放大。
>
> **[[Argument_OConnor_2020_AJLL|O'Connor (2020)]] — 全语言案例的方法论审查**
>
> O'Connor通过 Hattie 对全语言效应量（d=0.06）处理的详细案例审查，揭示了元-元分析中分类错误、不对称审查（接受 -0.65 / 修正 +0.65）、选择性修正和不加权平均等具体问题。详见 [[Meta-meta-analysis]]。
>
> **[[Argument_ONeill_2012_NZJES|O'Neill (2012)]] — 跨教育阶段混合综合与排名扭曲**
>
> [[Argument_ONeill_2012_NZJES|O'Neill (2012, pp.155–156)]]识别了《可见的学习》元-元分析的一个具体方法论问题：Hattie 的综合涵盖早教、学校教育和高等教育所有阶段，非学校阶段的研究对学校教育政策无已证明的相关性，但其纳入扭曲了特定主题的平均效应量和排名位置。典型例证是"教学质量"的元分析证据全部来自大学生评教研究，却被用于论证增加中小学[[Class Size|班级规模]]的政策合理性——暴露了跨阶段混合综合在政策应用中可能产生的具体误导。


> [!warning] 评估清单
> **[[Argument_Wiliam_2019_ERE|Wiliam (2019)]] — 11 点评估清单**
>
> [[Argument_Wiliam_2019_ERE|Wiliam (2019, p.11)]]提出以下检查清单用于评估元分析是否值得严肃对待：
>
> 1. 包含的研究是否**相关**？
> 2. 效应量是**干预**的结果还是仅仅是**关联**？
> 3. 效应量比较的是**相同的事物**（如与替代干预比较或"照常教学"比较，而非仅前后比较）？
> 4. 效应量在**同一层面（如个体层面 vs. 群体层面）**？
> 5. 是否检查了**发表偏倚**（如漏斗图）？
> 6. 被比较的干预在**持续时间**上是否相似？
> 7. 被比较的干预在**强度**上是否相似？
> 8. 使用的所有**结果测量**是否测量**同一事物**？
> 9. 测量属性的**离散度**在被比较的研究中是否相似？
> 10. 使用的**结果测量**对被调查的处理是否**同等敏感**？
> 11. 研究参与者在被调查的处理上是否具有**同等的资质（aptitude）**？
>
> > "如果所有这些问题的答案都是肯定的，或者至少元分析检验了这些问题（例如将这些问题作为效应的调节变量），那么元分析可能值得认真对待。然而，如果任何一个问题的答案是否定的，那么元分析不太可能与真实的教育情境有多大关联。"

---

## 相关理论

> [!info] 相关理论
> - [[Critical Realism]] — 为元分析的经验主义[[Hypothesis|假设]]提供了系统的哲学批判：因果机制而非[[Effect Size|效应量]]平均值才是科学知识的真正对象

---

## 使用此方法的研究

> [!example] 使用此方法的研究
> - [[Argument_Hattie_2015_Paideia]] — Hattie 回应《[[Visible Learning|可见的学习]]》批评时把元分析解释为寻找调节[[Variable|变量]]和竞争解释的证据地图，而不是直接替教师做决策的排名表
> - [[Argument_Hattie_2015_SOTLP]] — Hattie 将 1200 项元分析（65,000 多项研究）综合应用于高等教育，提出六项关键发现和八项思维框架
> - [[Argument_Wrigley_2019_ERE]] — 通过 [[Education Endowment Foundation|EEF]] Toolkit 体育参与案例的深度追踪揭示[[Meta-meta-analysis|元-元分析]]的程序缺陷
> - [[Argument_Wrigley_2018_BERJ]] — 对元分析和元-元分析（Hattie / EEF Toolkit）的系统方法论批判

---

## 替代方案


Pawson (2006) 提出**实在论综合（Realist Synthesis）**作为替代：研究综述应基于因果理论（干预"为什么有效、对谁有效、在什么条件下有效"），基于理论和相关性而非纯技术标准选择源研究，并以揭示效应变异性的分散图景（而非单一平均值）为输出形式([[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, pp. 119, 123]])。

---

