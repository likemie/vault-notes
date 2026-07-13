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
  - "[[Argument_Berk_2011_ER]]"
  - "[[Argument_Simpson_2017_JEP]]"
  - "[[Argument_Snook_2010_NZJES]]"
  - "[[Argument_Hattie_2015_Paideia]]"
  - "[[Argument_Hattie_2015_SOTLP]]"
  - "[[Argument_Wrigley_2018_BERJ]]"
related_facts:
  - "[[EEF Teaching and Learning Toolkit]]"
  - "[[Education Endowment Foundation]]"
confidence: medium
status: draft
created: '2026-05-01'
updated: 2026-07-13
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
> 元分析面临来自方法论前提、操作程序、统计推断和政策用途等多层面的系统批判，涵盖研究可比性（苹果和橙子问题）、输入质量（垃圾进垃圾出）、[[Publication Bias|发表偏倚]]、非独立数据与过度简化、伪精确性、统计推断[[Hypothesis|假设]]违背、抽样与伦理问题、领域迁移不匹配、平均效应误导以及[[Meta-meta-analysis|元-元分析]]的偏倚传播。[[Argument_Wiliam_2019_ERE|Wiliam (2019)]]提出了 11 点评估清单作为元分析可[[Reliability|信度]]的检验框架。详细的批判维度、学者论证与回应见 [[Critique of Meta-analysis]]。

> [!warning] 操作层面的关键提醒
> - **可比性** 根本不同的研究被聚合时，平均[[Effect Size|效应量]]的解释力有限。[[Gene Glass]]——元分析的创始人——本人警告：”元分析的结果永远不应该是平均值；它应该是一张图”（Robinson, 2004, p. 29, cited in [[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, p. 119]]）。
> - **输入质量** Eysenck（1978）的”垃圾进，垃圾出”奠定了所有方法论批评的基础命题：聚合的质量取决于输入的质量。
> - **统计推断** [[Argument_Berk_2011_ER|Berk (2011)]]和 [[Argument_Simpson_2017_JEP|Simpson（2017）]]论证元分析的统计推断假设在教育研究中几乎从未被满足。
> - **领域差异** [[Argument_Snook_2010_NZJES|Snook et al.（2010）]]指出元分析在医学中成功运作的条件（概念清晰、设计标准化、机制可分离）在教育领域经常不成立。
> - **平均效应** Kluger & DeNisi（1996）的反馈元分析显示，平均 d ≈ 0.4 掩盖了约 38% 的效应量为负的事实（[[Argument_Wiliam_2019_ERE|Wiliam, 2019, pp.10–11]]）。
> - **二级聚合** [[Meta-meta-analysis|元-元分析]]在聚合层级间传播和放大偏倚。详见 [[Critique of Meta-analysis]]。

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

