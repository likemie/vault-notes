---
title: Ex Post Facto Research
aliases:
  - 事后回溯研究
  - Ex Post Facto Design
summary: "一种回溯性非实验研究设计，通过观察已发生的因变量并逆向搜索可能的自变量来探索因果关系，属于准实验的一种形式"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 28
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/ex-post-facto
  - research-design
  - causal-inference
  - quasi-experiment
  - subject/research-methodology
related_concepts:
  - "[[Variable]]"
  - "[[Independent Variable]]"
  - "[[Hypothesis]]"
  - "[[Causality]]"
  - "[[Dependent Variable]]"
  - "[[Epistemology]]"
  - "[[Internal Validity]]"
  - "[[External Validity]]"
  - "[[Post Hoc Ergo Propter Hoc Fallacy]]"
  - "[[Questionnaire]]"
  - "[[Alternative Hypothesis]]"
  - "[[Co-relational Study]]"
  - "[[Criterion Group Study]]"
  - "[[Effective Teaching]]"
  - "[[Document]]"
  - "[[Falsification]]"
  - "[[Interaction Effect]]"
  - "[[Counterfactual]]"
  - "[[Causal Over-determination]]"
related_methods:
  - "[[Random Assignment]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Experimental Research]]"
  - "[[t-test]]"
  - "[[Analysis of Variance]]"
  - "[[Matching]]"
  - "[[Observational and Correlational Research]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]"
confidence: medium
status: draft
created: 2026-07-12
updated: 2026-07-13
---
# Ex Post Facto Research

---

## 定义

> [!def] 事后回溯研究的定义
> 事后回溯研究（ex post facto research）字面意为"事后"，指通过观察已存在的条件或状态，并回溯搜索可能的因果因素来探索因果-效应关系的研究方法（p.304）。研究者从因[[Variable|变量]]（DV）出发，逆向搜索已经发生、无法被操纵或控制的可能[[Independent Variable|自变量]]（IV），然后通过[[Hypothesis|假设]]、检验、控制样本和匹配等方式试图建立因果联系（pp.304–305）。由于自变量已发生且无法被研究者操纵，[[Causality|因果推断]]属于概率性因果关系的范畴（p.304）。

> [!method-scope] 方法范围
> - **研究对象** 已发生的自然事件、条件或处理对后续结果的影响，如家庭暴力对学生成绩的影响、教师培训质量对教学效能的影响。
> - **问题类型** 探索因果关系或关联关系，适合[[Dependent Variable|因变量]]已发生、自变量无法操纵的情境；回答"什么因素与某结果有关"以及"可能的原因是什么"。
> - **分析单位** 个体、群体、组织；通常以组别（处理组/对照组，或按因变量高低分组）为比较单位。
> - **输出形式** 组间差异比较、相关关系、可能的因果推断（试探性而非确定性）。

> [!citation-card]- Kerlinger（1970）的定义
> 事后回溯研究被定义为自变量已经发生、研究者从因变量的观察出发、回溯研究自变量与因变量可能关系的方法。研究者从已发生的结果逆向推断可能的原因，通过逐一检验和排除来锁定最可能的因果因素（p. 305）。
>
> *Ex post facto research is that in which the independent variable or variables have already occurred and in which the researcher starts with the observation of a dependent variable or variables. She then studies the independent variable or variables in retrospect for their possible relationship to, and effects on, the dependent variable or variables.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 事后回溯研究属于概率性[[Causality|因果推断]]传统，承认无法确定性地证明因果关系；因果推断是试探性而非结论性的（p.304）。
> - **研究者角色** 研究者是回溯性侦探：从已发生的结果出发，[[Hypothesis|假设]]可能原因，通过控制、匹配和比较来逐一检验这些假设（p.304）。
> - **有效性标准** [[Internal Validity|内部效度]]较弱——缺乏对自[[Variable|变量]]的操纵和[[Random Assignment|随机分配]]；[[External Validity|外部效度]]可接受——研究发生在自然情境中；核心威胁包括反向因果、第三变量和[[Post Hoc Ergo Propter Hoc Fallacy|事后归因谬误]]（pp.307–308）。
> - **不声称回答的问题** 无法确定性地证明因果关系；无法区分因果方向；无法排除所有替代解释。

> [!method-stack] 方法层级
> - **研究设计** [[Quasi-Experimental Designs|准实验设计]]（quasi-experiment），属于非[[Experimental Research|实验研究]]设计的一种伪实验形式（Spector, 1993, p. 42）。
> - **数据收集** 回溯性数据（档案、记录、[[Questionnaire|问卷]]、现有数据库）与当前数据（[[Dependent Variable|因变量]]测量）相结合。
> - **分析方法** 组间比较（[[t-test|t检验]]、[[Analysis of Variance|ANOVA]]）、相关分析、列联表分析。
> - **辅助技术** 匹配、将额外[[Independent Variable|自变量]]纳入设计、同质性抽样、[[Alternative Hypothesis|替代假设]]检验。

---

## 研究程序

### 两种基本设计

事后回溯研究包含两种基本设计类型（pp. 306–307）：

> [!contrast-table] [[Co-relational Study|共变关系研究]]与[[Criterion Group Study|标准组研究]]的对比
> | 维度 | 共变关系研究（co-relational / causal study） | 标准组研究（criterion group / causal-comparative study） |
> |---|---|---|
> | 设计符号 | X → O | E (X → O₁) vs C (O₂) |
> | 逻辑 | 收集两组数据（一组回溯），确定自[[Variable|变量]]与因变量的关系 | 比较[[Dependent Variable|因变量]]存在与不存在的两组被试，逆向搜索可能原因 |
> | 目的 | 识别当前条件的先行因素 | 发现导致组别差异的可能原因 |
> | 示例 | Borkowsky（1970）：音乐教师本科培训质量（X）与后续教学效能（O）的关系 | Morrison（2009）：通过比较有无同事课程规划的教师，推断同事规划是否是[[Effective Teaching|有效教学]]的原因 |
> | 核心局限 | 无法确定[[Causality|因果]]方向（X→O、O→X 或第三变量→二者） | 最多是相关研究，因果不等于相关；第三变量可能同时解释原因与结果 |

> [!contrast-table] 前瞻性与回溯性设计（Ary et al., 2009, p. 335）
> | 维度 | 前瞻性设计（proactive） | 回溯性设计（retroactive） |
> |---|---|---|
> | 分组依据 | 按[[Independent Variable|自变量]]（IV）存在与否分组 | 因变量（DV）固定，按结果高低分组 |
> | 比较内容 | 比较两组在因变量（DV）上的差异 | 比较两组在多个可能的自变量（IV）上的差异 |
> | 推理方向 | 从原因到结果 | 从结果到原因 |
> | 与实验的相似性 | 接近实验逻辑（控制组与"实验组"比较） | 更接近探索性回溯 |

### 操作程序

Lord（1973, p. 6）提出了事后回溯研究的八个阶段（pp. 315–316）：

> [!proc] Lord（1973, p. 6）的八阶段程序
> 1. **界定问题并回顾[[Document|文献]]** 明确研究领域，通过文献了解前人研究的问题、障碍和发现。
> 2. **陈述[[Hypothesis|假设]]与前提** 明确待检验的假设以及假设和研究程序所基于的前提假设。
> 3. **选择被试与数据收集方法** 确定抽样策略和数据收集工具。
> 4. **建立分类标准与类别** 建立尽可能无歧义的数据分类标准，使关系和相似性能被发现。
> 5. **收集"结果出现时"始终存在的因素数据** 收集在给定结果出现时始终在场的因素数据，舍弃这些因素不一致存在时的数据。
> 6. **收集"结果不出现时"始终存在的因素数据** 收集在给定结果未出现时始终在场的因素数据。
> 7. **比较两组数据** 将第5步数据从第6步数据中减去，以推断导致结果出现或不出现的原因。
> 8. **分析、解释并报告发现** 呈现分析结果，注意证据是说明（illustrate）假设而非检验（test）假设。

> [!warning] 证据说明而非检验假设
> Lord（1973, p. 7）提醒：在事后回溯研究中，证据说明假设而非检验假设，因为假设是从同一数据中生成的，无法在同一数据上被[[Falsification|证伪]]（p. 316）。

### 引入控制的手段

事后回溯研究的核心弱点是缺乏对自变量的控制和[[Random Assignment|随机化]]。但研究者仍可采用四种手段引入一定程度的控制（pp. 316–317）：

> [!feature] 四种控制手段
> - **匹配（[[Matching]]）** 在因果-比较设计中，将实验组和对照组的被试在重要相关特征上进行匹配（Ary et al., 2009）。困难在于研究者未必知道哪些因素是相关的，且无法匹配的被试会被舍弃，导致样本缩减。Lewis-Beck（1993, p. 43）报告了一个从 1,194 缩减到 46 的匹配后样本缩减实例。
> - **将额外自变量纳入设计** 将无法控制的外部自变量作为一个额外的自变量纳入设计，使用[[Analysis of Variance|方差分析]]揭示其对因变量的主效应和[[Interaction Effect|交互效应]]（Ary et al., 2009）。例如将智力水平作为额外自变量纳入，以分离其对因变量的影响。
> - **选择同质性样本** 在某一特定变量上选择尽可能同质的样本，使该变量的效应被排除（Ary et al., 2009）。例如只纳入一个智力水平的学生，以排除智力差异的其他可能解释。
> - **陈述并检验[[Alternative Hypothesis|替代假设]]** 明确陈述并检验能解释研究结果的其他可能假设（p. 317）。例如吸烟与肺癌的关系——烟草公司提出替代假设：吸烟和肺癌都可能是某个未指明的第三因素的结果。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 更严格的实验方法不可行时：自[[Variable|变量]]超出研究者控制时；实验室控制不切实际、成本过高或不符合伦理时；特别是在社会、教育和心理情境中[[Independent Variable|自变量]]通常无法被操纵时（p. 310）。
> - **谨慎使用** 简单因果-效应关系探索；变量之间的相关较强且替代解释可被排除时；拥有大型公共数据库可供分析时（Ayres, 2008）；作为[[Experimental Research|实验研究]]的预备探索阶段生成[[Hypothesis|假设]]时。
> - **不适合使用** 需要确定性[[Causality|因果推断]]的情境；自变量可以被直接操纵时；需要[[Random Assignment|随机分配]]以控制所有混淆变量时；可能存在反向因果或强的第三变量解释时。

> [!example] 典型应用示例
> - 吸烟与肺癌的关系研究
> - 教师特征与教学效能的关系
> - 政治/宗教归属与态度的关系
> - 学校成就与社会阶层、种族、性别、智力等自变量的关系
> - Stables（1990）大样本研究混合与单性别学校学生差异
> - Arnold & Atkins（1991）小样本研究听障学生的社会与情感适应

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 缺乏对自[[Variable|变量]]的控制（核心弱点）；无法[[Random Assignment|随机分配]]；回溯数据受历史证据的弱点和偏差影响；[[Hypothesis|假设]]可以从同一数据中获得多个甚至相互矛盾的支持（p. 308）；[[Post Hoc Ergo Propter Hoc Fallacy|事后归因谬误]]（post hoc, ergo propter hoc）——仅因一个变量在时间上先于另一个，不意味着前者引发了后者（Cohen & Nagel, 1961）（p. 309）。
> - **适用边界** 最多只能展示变量间的相关或关联关系；[[Causality|因果推断]]是试探性的，不应被解读为确定性的（p. 308）；因果关系方向无法确定——A 可能引发 B，B 可能引发 A，或第三变量可能同时引发二者（p. 309）。
> - **误用风险** 将相关误解为因果；忽略可能的反向因果；忽略未测量的第三变量；将来自数据的假设当作已被数据检验过的假设（Lord, 1973, p. 7）（p. 316）；分类为二分组的困难（p. 313）；匹配导致的样本大幅缩减（Lewis-Beck, 1993, p. 43）（pp. 316–317）。
> - **补救方式** 通过匹配、同质性抽样、纳入额外[[Independent Variable|自变量]]、检验[[Alternative Hypothesis|替代假设]]引入控制（pp. 316–317）；谨慎地将事后回溯研究定位为探索性工具和假设来源，而非确定性检验（p. 310）。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Causality]] | 概念 | 事后回溯研究在概率性因果框架下运作，关注"结果的原因"而非"原因的结果"（p. 304）。 |
> | [[Matching]] | 方法 | 匹配是事后回溯研究中引入控制的主要手段之一，用于提高比较组的可比性（pp. 316–317）。 |
> | [[Observational and Correlational Research]] | 方法 | 事后回溯研究的因果-比较设计被视为桥梁，连接描述性研究方法和真正[[Experimental Research|实验研究]]（p. 308）。 |
> | [[Experimental Research]] | 方法 | 事后回溯研究是准实验的一种形式，介于描述性研究与真正实验之间（Spector, 1993, p. 42）（p. 305）。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15]] — 本章以事后回溯研究本身为对象，系统论述其定义、设计类型、特征、适用时机、优势和局限，并以 Morrison（2009）的[[Effective Teaching|有效教学]]因果-比较研究为示例。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]] — 第4章系统阐述了事后回溯研究所依赖的概率性[[Causality|因果关系]]、[[Counterfactual|反事实推理]]和[[Causal Over-determination|因果过度决定]]等概念基础。
