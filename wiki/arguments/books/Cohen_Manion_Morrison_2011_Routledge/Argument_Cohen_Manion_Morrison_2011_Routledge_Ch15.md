---
authors:
  - "[[Louis Cohen|Cohen, L.]]"
  - "[[Lawrence Manion|Manion, L.]]"
  - "[[Keith Morrison|Morrison, K.]]"
source_language: en
summary: "系统介绍事后回溯研究的字面含义与回溯性因果探索逻辑，详述共变关系研究（X→O）与标准组研究（E vs C）两种设计类型、前瞻性与回溯性两种研究路径、与真正实验在操纵控制与随机化上的五维对比、六项适用场景与公共数据库清单、六项优势与十三项劣势，以及Lord八阶段操作程序与四种引入控制的手段"
type: argument
subtype: textbook
publication_type: book-chapter
title: "Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15"
argument_key: "Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15"
argument_display_title: "Research Methods in Education · Ch15"
argument_kind: "book-chapter"
argument_related_count: 29
argument_related_level: 1
argument_related_stars: "⭐"
argument_related_color: "#fef3c7"
book_title: "Research Methods in Education"
publication_place: "London"
publisher: "Routledge"
year: 2011
doi: ""
citation_aliases: []
isbn: "978-0-415-58336-7"
citation: ""
tags:
  - source/textbook
  - method/ex-post-facto
  - research-design
  - paradigm/quantitative
  - causal-inference
related_concepts:
  - "[[Causality]]"
  - "[[Hypothesis]]"
  - "[[Variable]]"
  - "[[Dependent Variable]]"
  - "[[Independent Variable]]"
  - "[[Homework]]"
  - "[[Co-relational Study]]"
  - "[[Criterion Group Study]]"
  - "[[Sample Size Determination]]"
  - "[[Effective Teaching]]"
  - "[[Document]]"
  - "[[Post Hoc Ergo Propter Hoc Fallacy]]"
  - "[[Research Purpose]]"
  - "[[Evidence-Based Education]]"
  - "[[Falsification]]"
  - "[[Literature Review]]"
  - "[[Interaction Effect]]"
  - "[[Alternative Hypothesis]]"
  - "[[Probabilistic Causation]]"
related_methods:
  - "[[Ex Post Facto Research]]"
  - "[[Experimental Research]]"
  - "[[Random Assignment]]"
  - "[[t-test]]"
  - "[[Analysis of Variance]]"
  - "[[Matching]]"
  - "[[Matched Pairs Design]]"
related_facts:
  - "[[OECD]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
status: draft
created: 2026-07-12
updated: 2026-07-13
part_of: "[[Argument_Cohen_Manion_Morrison_2011_Routledge]]"
sources:
  - "[[books/Cohen_Manion_Morrison_2011_Routledge/Cohen_Manion_Morrison_2011_Routledge|Cohen_Manion_Morrison_2011_Routledge]]"
---
# Argument_Cohen_Manion_Morrison_2011_Routledge_Ch15

## 概念地图

> [!knowledge-map]- 第15章 概念地图
> ![](https://img.mylikemie.icu/books/Cohen_Manion_Morrison_2011_Routledge/figures/Chapter_15_Concept_Map.jpg)

## 章节内容

> [!logic-map] [[Ex Post Facto Research|事后回溯研究]]方法的核心知识结构
> ```mermaid
> flowchart LR
>     A["事后回溯研究<br/>Ex Post Facto Research"]
>     A --> B["定义与逻辑<br/>回溯性因果探索 · 自变量不可操纵<br/>概率性因果推断 · 反向实验"]
>     A --> C["两种设计<br/>共变关系研究 X→O<br/>标准组研究 E vs C"]
>     A --> D["两种路径<br/>前瞻性 proactive<br/>回溯性 retroactive"]
>     A --> E["与实验的对比<br/>操纵控制 · 随机化<br/>假设灵活性 · 事后归因谬误"]
>     A --> F["控制手段<br/>匹配 · 纳入额外变量<br/>同质性样本 · 替代假设"]
>     C --> G["Figure 15.1<br/>四种事后回溯研究类型"]
>     C --> H["Figure 15.2<br/>两个原因与两个效果"]
> ```

事后回溯研究对新手研究者可能较为陌生，其关键特征及实施方法如下（p. 304）。作为[[Experimental Research|实验研究]]的引言，本章展示如何利用已有数据构建实验形式并探索因果与效应关系，阅读时可结合[[Causality|因果关系]]（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|第4章]]）、抽样（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|第8章]]）和实验研究（第16章）。

---

### 15.1 引言：什么是事后回溯研究？

事后回溯研究的字面翻译是事后（after the fact），含义包括事后所做（from what is done afterwards）、事件之后（from after the event）或从已发生的事情推演（from what has happened）。在社会和教育研究中，指回溯性地（retrospectively）探索可能的因果-效应关系，即通过观察已存在的条件或状态，逆时间搜索可能的因果因素（p. 304）。

在因果关系的框架中（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|第4章]]），事后回溯研究关注研究结果的原因（causes of effects），区别于研究原因的结果（effects of causes）。核心追问是：哪些因素似乎与特定事件、条件或行为方面有关联？这些都已发生，因此必须[[Hypothesis|假设]]可能的原因，然后对照证据逐一检验，例如通过将因素保持不变、控制样本并进行匹配（p. 304）。

> [!def] 事后回溯研究的正式定义
> 事后回溯研究是一种梳理已发生事件的先行因素的方法，这些事件已发生因此无法被控制、设计或操纵（Cooper & Schindler, 2001, p. 136）。只能报告已发生或正在发生的事情，通过谨慎关注抽样来设法将因素保持不变。自[[Variable|变量]]无法像在真正实验中那样被操纵，因为它们已经发生。因此整个推断在概率性因果关系的领域内进行：试探性地推断原因（inferring causes tentatively），无法确定性地展示因果关系（p. 304）。

事后回溯研究可用于研究相似但仅在一个条件上不同的群体，评估那个不同条件对[[Dependent Variable|因变量]]的效应。它因此是一种实验形式，但没有真正实验的严格控制：存在控制组和实验组（后者指某一特定条件被应用的组）。由于几乎没有或完全没有对[[Independent Variable|自变量]]或条件的严格操纵，也没有对被试的[[Random Assignment|随机分配]]，任何因果推断都是试探性的（p. 304）。

> [!case] 交通事故调查
> 假设某地区致命交通事故急剧增加。一位专家被召来进行调查。她无法研究已发生的实际事故，它们已经发生了；无法调用技术手段回放事故录像；更无法要求参与者跑到公交车或卡车前面，或站在飞驰摩托车的前方以发现效果。
>
> 她可以做的事情包括：(1) 研究医院记录，看哪些群体遭受了最大创伤，是公交车、卡车还是摩托车冲击受害者；(2) 通过分析统计数据、勘验事故地点、收集受害者和目击者的陈述来重建事件。通过这种方式，可以识别可能的事故决定因素：超速、路况不佳、疏忽驾驶、挫折感、车辆故障、药物或酒精影响等。
>
> 在她的勘验基础上，她可以就可能的原因形成[[Hypothesis|假设]]，并以建议的形式提交给相关权威机构。这些建议可能包括改善路况、降低限速或加强警察巡逻。关键在于：她在回溯性识别原因的过程中，采用的正是事后回溯视角（p. 304）。

---

事后回溯研究也可用于替代实验，在不可能、不切实际或不道德地控制或操纵因变量（乃至自变量）的情境中，检验关于因果与效应的假设（p. 305）。

> [!case] 家庭暴力与学业表现
> 假设要检验家庭暴力导致学业表现不佳这一假设。从伦理上讲，不应让学生暴露于家庭暴力，也无法将情绪稳定的儿童置于受控的创伤环境中来研究效应（Lord, 1973, p. 2）。
>
> 但可以将学生分为两组，在一系列因素上仔细匹配：一组有家庭暴力经历，另一组家庭环境更可接受。如果假设可成立，在其他变量被匹配或尽可能保持不变的情况下，两组之间应能发现学业表现的差异（p. 305）。

---

#### Kerlinger 的定义与反向实验逻辑

Kerlinger（1970）将事后回溯研究定义为：自变量（IV）已经发生，从因变量（DV）的观察出发，回溯研究自变量与因变量可能关系的方法。由此回溯性地检查一个自然发生的事件对后续结果的影响，以建立二者之间的因果联系。建立原因的关键在于：谨慎识别可能的原因，逐一对照证据进行检验，淘汰无法通过检验的原因，同时确保关注谨慎抽样和控制，即将某些变量固定不变（p. 305）。

> [!contrast-table] 真正实验与事后回溯的逻辑对比
> | 维度 | 真正实验 | 事后回溯研究 |
> |---|---|---|
> | 起点 | 取等效组 | 从已经存在差异的组出发 |
> | 操作 | 施加不同处理 | 回溯搜索导致差异的因素 |
> | 终点 | 产生因变量差异 → 测量差异 | 试图建立因果联系 |

> [!conclusion] Spector（1993, p. 42）的定性
> 事后回溯研究是一种试图将非实验研究设计转化为**伪实验形式（pseudo-experimental form）**的程序，因此事后回溯实验是准实验（quasi-experiment）的一种形式（pp. 305–306）。

---

#### 两种研究路径

可以识别两种事后回溯研究路径（p. 306）：

> [!contrast-table] 两种事后回溯研究路径
> | 维度 | 路径一：从自变量出发 | 路径二：从因变量出发 |
> |---|---|---|
> | 起点 | 在某自变量（IV）上不同的被试（如数学学习年限） | 在某因变量（DV）上不同的被试（如数学考试成绩） |
> | 比较内容 | 他们在因变量上的差异（如数学考试成绩） | 他们在一系列自变量上的差异（如学习年限、学科喜好、[[Homework\|作业]]量） |
> | 推理方向 | 从原因到结果 | 从结果逆向搜索原因 |
> | 分析逻辑 | 比较 IV 高低两组在 DV 上的差异 | 在自变量已发生后，比较结果高的学生（如数学高分）与结果低的学生（如数学低分）在各 IV 上的差异，以此探索特定结果的原因 |

路径二的本质是在自变量已经发生之后，通过结果的高低来反向区分组别，再回溯比较两组在多个可能的自变量上是否存在差异。

Ary et al.（2009, p. 335）进一步将这两种路径分别命名为前瞻性（proactive）和回溯性（retroactive）设计（p. 306）：

> [!contrast-table] 前瞻性设计与回溯性设计（Ary et al., 2009, p. 335）
> | 维度 | 前瞻性设计（proactive） | 回溯性设计（retroactive） |
> |---|---|---|
> | 分组依据 | 按自变量存在与否分组 | 因变量恒定，按结果高低分组 |
> | 比较内容 | 比较两组在因变量（结果）上的差异 | 比较两组在可能的自变量上的差异 |
> | 核心逻辑 | 假设自变量 → 检验因变量差异 | 观察因变量差异 → 假设并检验各自变量 |
> | 与实验的相似性 | 接近实验逻辑：有处理组和对照组 | 更接近探索性的逆向推理 |

> [!example]- 图15.1 四种事后回溯研究类型
> ![](https://img.mylikemie.icu/books/Cohen_Manion_Morrison_2011_Routledge/figures/Figure_15-1_Four_Types_of_Ex_Post_Facto_Research.jpg)
>
> 该图以前瞻性/回溯性和[[Co-relational Study|共变关系研究]]/[[Criterion Group Study|标准组研究]]两个维度，划分出四种事后回溯研究设计类型（p. 306）。

---

#### 示例三：教师缺勤与困难班级

> [!case] 教师缺勤与困难班级的教学日
> 观察到一所大规模中学的教职工在教授困难班级的日子缺勤。研究者进行事后回溯研究以尝试建立原因。首先记录教职工在教授困难班级日子里的缺勤情况（pp. 306–307）。

> [!ref-table]- 表1：教授困难班级与教职工缺勤
> | | 教授困难班级的日子 |
> |---|---|
> | **缺勤情况** | 是 | 否 |
> | 高缺勤 | 26 | 30 |
> | 低缺勤 | 22 | 50 |
> | **合计** | 48 | 80 |

总[[Sample Size Determination|样本量]]：128

> 此处时间因素很重要：教职工是**只在**教授困难班级的日子缺勤，还是在其他日子也缺勤？是否有其他变量可以纳入研究，例如年龄组？因此研究被进一步细化，收集了更多数据（pp. 306–307）。

> [!dual-header]- 表2：年龄、班级类型与缺勤交叉分析
> | | 教授困难班级的日子 | | 不教授困难班级的日子 | |
> |---|---|---|---|---|
> | **年龄** | 高缺勤 | 低缺勤 | 高缺勤 | 低缺勤 |
> | < 30 岁 | 30 | 6 | 16 | 10 |
> | 30–50 岁 | 4 | 4 | 4 | 20 |
> | > 50 岁 | 2 | 2 | 2 | 28 |
> | **合计** | 36 | 12 | 22 | 58 |

总样本量：128

> 细化数据显示：年龄也是一个因素，与教授困难班级的天数共同作用。年轻教师更可能缺勤，大多数缺勤教师年龄在 30 岁以下。在各年龄组内部，也能清晰看到：年轻教师在教授困难班级时的高缺勤率远高于同年龄组不教授困难班级时的缺勤率。
>
> 更进一步的检验是比较同一教师教与不教困难班级时的缺勤率，并进行差异检验（[[t-test|t检验]]、[[Analysis of Variance|ANOVA]]；见第36章），以检验两组分数（教授困难班级的日子 vs 不教困难班级的日子；各年龄组在教授困难班级与不教困难班级日子上的差异）（pp. 306–307）。

---

### 15.2 共变关系研究与标准组研究

事后回溯研究中可识别两种基本设计：

> [!contrast-table] 共变关系研究与标准组研究的对比
> | 维度 | 共变关系研究（causal research） | 标准组研究（causal-comparative research） |
> |---|---|---|
> | 设计符号 | X → O | E (X → O₁) vs C (O₂) |
> | 核心逻辑 | 收集两组数据（一组回溯），确定自变量与因变量的关联 | 比较因变量存在与不存在的两组被试，逆向搜索可能原因 |
> | 分析目的 | 识别当前条件的先行因素 | 发现导致组别差异的可能原因 |
> | 典型示例 | Borkowsky（1970）：音乐教师培训质量 → 教学效能 | Morrison（2009）：有无同事课程规划 → 教学效能差异 |
> | 核心局限 | 无法确定因果方向；三种竞争性解释（X→O、O→X、第三变量→二者） | 最多是相关研究；第三变量可能同时解释分组差异与结果差异 |
> | 价值定位 | 探索性工具：产出关联度量，作为因果探索的有用第一步 | 桥梁：连接描述性研究方法与真正实验研究 |

---
#### [[Co-relational Study|共变关系研究]]（X → O）

共变关系（或因果）研究旨在识别当前条件的先行因素。顾名思义，它涉及收集两组数据，其中一组是回溯性的，以确定二者之间的关系。基本设计可表示为（使用 Campbell & Stanley, 1963 的符号：X = 自变量；O = 因变量）：

> [!case] Borkowsky（1970）：音乐教师培训与教学效能
> 基于这种设计尝试展示音乐教师本科培训质量（X）与后续教学效能（O）之间的关系。培训质量的测量可包括：具体课程成绩、平均绩点、自评等。教学效能可通过学生表现指标、学生知识、学生态度和专家判断等评估。所有测量之间的相关被计算以确定关系。
>
> 这项研究最多能显示培训质量与教学效能之间存在事后关系（p. 307）。

当自变量与因变量之间存在强相关时，三种可能的解释对研究者开放（p. 307）：

> [!dimension] 强关系下对 X 与 O 关系的三种解读视角
> - **解释一：变量 X 引发了 O**
>   因果正方向：自变量是原因，因变量是结果。
> - **解释二：变量 O 引发了 X**
>   反向因果（reverse causation）：因果方向可能是反过来的。
> - **解释三：第三变量同时引发了 X 和 O**
>   某个尚未识别、因此未被测量的第三变量是共同原因，同时影响了看似有因果关系的两个变量。

> [!warning] 因果方向无法确定
> 通常无法确定三种解释中哪种是正确的。这引出了因果方向的核心问题：在事后回溯实验中，很难确定什么引发了什么，是 A 引发 B，还是 B 引发 A（p. 307）。

共变关系或因果研究的价值主要在于其探索性或启发性特征：虽然它们自身通常不足以建立变量间的因果关系，但由于能产出关联度量，它们是在这一方向上的有用第一步（p. 307）。

---

#### [[Criterion Group Study|标准组研究]]（E vs C）

在标准组（或因果-比较）方法中，通过比较变量存在的被试与变量不存在的相似被试，即注意给定效应在何种情境下出现与不出现，来发现所研究现象的可能原因（Lord, 1973, p. 3）（p. 307）。

基本设计可表示为：

> [!example]- 图15.2 两个原因与两个效果
> ![](https://img.mylikemie.icu/books/Cohen_Manion_Morrison_2011_Routledge/figures/Figure_15-2_Two_Causes_and_Two_Effects.jpg)
>
> 该图呈现 Morrison（2009, p. 181）的[[Effective Teaching|有效教学]]因果-比较研究设计（见下文）（p. 308）。

如果选择这种设计来研究影响教师效能的因素，先通过测量两组教师对班级学生的差异效应来识别标准组 O₁（有效教师）及其对照组 O₂（不表现标准组特征的教师组）。然后检查 X，即某变量或事件，如背景、培训、技能和人格，以发现什么可能使只有部分教师有效（p. 307）。

> [!case] Morrison（2009, p. 181）：有效教学的因果-比较研究
> Morrison 给出一个标准组事后回溯研究示例。假设要建立有效教学的原因，并假设一个原因是与部门同事进行课程规划（collegial curriculum planning）。
>
> 研究设计包含两个标准组：(a) 存在同事课程规划；(b) 不存在同事课程规划。通过检查两组教师在教学效能上的差异（无论怎样测量），可以推断一个可能的因果差异。
>
> 但必须谨慎：这最多是一项相关研究（correlational study），因果不等于相关。第三因素（如教职工社交性 staff sociability）可能同时影响有效/无效教学和有无同事课程规划，即两条因果路径可能共享一个共同原因，而不是一条路径中的 X 导致了 O（pp. 307–308）。

---

#### 与历史设计的区别和桥梁定位

> [!contrast-table] 因果-比较设计与历史设计的对比（Lord, 1973, p. 4）
> | 维度 | 因果-比较设计 | 历史设计 |
> |---|---|---|
> | 时间焦点 | 关注当前事件 | 追溯过去事件的历史 |
> | 数据性质 | 可直接观察和访谈当前参与者 | 依赖档案、[[Document\|文献]]和二手记录 |
> | 与研究对象的关系 | 研究者可接触活着的当事人 | 研究者与研究对象之间存在时间距离 |
> | 核心任务 | 比较当前组别差异，逆向搜索原因 | 基于史料重建过去情境和因果脉络 |

> [!conclusion] 标准组研究的桥梁定位
> 标准组或因果-比较研究可被视为**桥梁**，连接一端是描述性研究方法，另一端是真正实验研究（p. 308）。

---

### 15.3 事后回溯研究的特征

事后回溯研究中，研究者取效应（或因变量）并回溯检查数据以建立原因、关系或关联及其含义（p. 308）。

事后回溯研究的特征在与真正实验研究对比时最为清晰。Kerlinger（1970）描述了实验研究者的操作模式（modus operandi）（pp. 308–309）：

> [!contrast-table] 真正实验 vs 事后回溯研究的系统对比
> | 维度 | 真正实验研究 | 事后回溯研究 |
> |---|---|---|
> | 推理方向 | 如果 X，则 O（if frustration, then aggression）；从受控 X 预测 O | 观察 O → 回溯搜索 X；从 O 出发寻找与假设一致的 X |
> | 对 X 的操作 | 使用某种方法主动操纵 X | X 已发生，无法操纵 |
> | 控制手段 | 至少拥有操纵控制；至少有一个主动变量；可通过[[Random Assignment\|随机化]]分配被试或处理到各组 | 对 X 的控制不可能；随机化同样不可能；必须接受事物的既有状态并尝试理清 |
> | 对 O 的观察 | 观察 O 是否出现伴随变异（concomitant variation），即与 X 的变化相应的预期变异；假定其他条件相等，O 的变化是 X 被操纵的结果 | O 已被观察 → 回溯寻找合理的 X；无法以实验研究者的信心断言假设关系的真实性 |
> | 假设的角色 | 预测：从特定解释出发，确定是否与外部获取的数据一致；假设先行，数据检验 | 解释：从某些数据出发，寻找与数据一致的解释；同一数据可支持多项甚至相互矛盾的解释；假设是从数据中生成的，同一数据不能检验自身 |
> | 根本弱点 | 人工性 | 缺乏对自变量的控制（内置弱点，built-in weakness）；如 Spector（1993, p. 43）所言，不可能隔离和控制每一个可能的变量，也不可能绝对确定哪些是最关键的变量 |

尽管有上述限制，事后回溯研究仍可采用若干选择性的程序引入一定程度的控制（见 15.7 节）。

---

#### 事后归因谬误（post hoc, ergo propter hoc）

> [!warning] [[Post Hoc Ergo Propter Hoc Fallacy|事后归因谬误]]（post hoc, ergo propter hoc fallacy）
> 因果关系常常建立在脆弱的基础上：仅因某变量先于所研究的现象发生，就假定它是原因（在此之后，因此因为此，after this, therefore because of this）。仅因一个变量在时间上先于另一个，并不意味前者引发了后者（p. 309）。

> [!case] 咖啡与失眠
> 喝咖啡然后失眠，并不意味咖啡导致了失眠，可能有其他原因（Cohen & Nagel, 1961）。即使发现两个变量之间存在关系，也必须认识到二者可能都是某个共同第三因素的个别结果，而不是第一个必然是第二个的原因（p. 309）。

---

#### 反向因果与第三变量

> [!chain-link] 两种替代解释的逻辑链
> - **反向因果（reverse causation）** 心脏状况促进肥胖，反过来也可能成立，或二者相互促进。关键点：证据只是说明（illustrate）假设，不能检验（test）假设，因为假设不能在与推导出假设的同一数据上进行检验（p. 309）
> - **第三变量（third variable）** 看电视与学业表现差相关：(1) 看电视 → 学业差？(2) 学业差 → 看电视多？(3) 第三变量（能力或动机）→ 看电视多 + 学业差？注意第三种解释中，是第三变量（IV）同时引发了两个结果（DV）

---

#### 重新定位为调查

不能因此认为事后回溯研究价值不大，教育和心理学中许多重要研究都是事后回溯设计。通常别无选择：无法使一组人成为失败者、犯罪者、自杀者、脑损伤者或辍学者，研究必须依赖已有群体。

> [!conclusion] 事后回溯研究应被理解为调查
> 事后回溯设计无法融入基本的控制需求（通过操纵或[[Random Assignment|随机化]]），使其从科学角度易受攻击，产生误导的可能性应被明确承认。事后回溯设计更适合被更谨慎地理解为**调查（surveys）**，作为需由更常规实验方法在日后检验的假设的有用来源，而不是具有更大确定性的实验（p. 310）。

---

### 15.4 适用时机

事后回溯设计适用于更严格的实验方法不可行的情境（p. 310）：

> [!method-fit] 六类适用情境
> - **自变量无法被操纵时** 无法选择、控制和操纵直接研究因果-效应关系所必需的因素
> - **控制单一自变量不切实际** 控制除一个自变量外的所有变量可能不切实际和人为化，阻碍与其他影响变量的正常交互
> - **实验室控制不可行** 实验室控制在许多[[Research Purpose|研究目的]]上不切实际、成本过高或伦理上不可取
> - **社会、教育和心理情境** 自变量通常超出研究者控制：吸烟与肺癌研究、教师特征研究、政治/宗教归属与态度关系、学校成就与社会阶层/种族/性别/智力等自变量的关系
> - **大样本研究和小样本研究均可** Stables（1990）的大规模混合/单性别学校学生差异研究；Arnold & Atkins（1991）的小样本听障学生社会与情感适应研究
> - **大型公共数据库分析** Ayres（2008）展示了事后回溯设计中大样本和子样本数据集的概率和规律性力量，特别是分析考虑了标准差时（两倍标准差覆盖 95% 总体）。这些在[[Evidence-Based Education|循证教育]]中可能比人类直觉更可靠（Ayres, 2008, chapter 10）（p. 311）

---

#### 可用于事后回溯研究的公共数据库

> [!ref-table] 教育研究可用的公共领域数据库与数据集（pp. 311–312）
> | 类别 | 来源 |
> |---|---|
> | 政府数据库 | [英国政府开放数据（data.gov.uk）](https://data.gov.uk)、[教育部（DfE）](https://www.gov.uk/dfe)、[高等教育统计局（HESA）](https://www.hesa.ac.uk)、[政府社会研究（GSR）](https://www.gsr.gov.uk) |
> | 研究机构 | [英国数据服务（UK Data Service）](https://www.data-archive.ac.uk) |
> | 研究联盟 | [校际政治与社会研究联盟（ICPSR）](https://www.icpsr.umich.edu) |
> | 国际组织 | [欧盟教育信息网络（Eurydice）](https://eurydice.eacea.ec.europa.eu)、[[OECD]]、[国际学生评估（PISA）](https://www.oecd.org/pisa/)、[教科文组织统计所（UNESCO）](https://www.uis.unesco.org)、[世界银行（World Bank）](https://data.worldbank.org)、[国际数学与科学趋势（TIMSS）](https://nces.ed.gov/timss/) |
> | 个别数据集 | [英国教育研究协会（BERA）](https://www.bera.ac.uk) |
> | 高校数据集 | [英国队列研究（CLS）](https://www.cls.ioe.ac.uk)

---

### 15.5 事后回溯研究的优势与劣势

#### 六项优势

> [!strength] 事后回溯研究的六项优势（pp. 311–312）
> - **在更严格实验方法不可行时满足重要需求** 例如吸烟与肺癌的所谓关系无法通过实验检验（至少对人类而言）。当研究者无法操纵因变量和自变量时，事后回溯设计提供替代路径
> - **产出关于现象本质的有用信息** 展示什么与什么相伴、在什么条件下相伴。以此方式是宝贵的探索工具（exploratory tool）
> - **统计技术和一般方法论的改进** 使事后回溯设计更具可辩护性（more defensible）
> - **在某些情境中比实验方法更有用** 特别是在设置实验会引入人工性（artificiality）的情境中
> - **特别适合探索简单因果-效应关系（simple cause-and-effect relationships）**
> - **提供方向感与丰富的假设来源** 可供后续更严格实验方法检验

---

#### 十三项劣势与局限

> [!weakness] 事后回溯设计的十三项局限（pp. 312–313）
> - 无法操纵自变量或随机化被试，即**缺乏控制**的根本问题
> - 无法确定因果因素是否被纳入甚至被识别（cannot know whether the causative factor has been included or even identified）
> - 可能没有单一因素是原因，即**多因性（multiple causes）**的挑战
> - 某一特定结果在不同情境中可能源自**不同原因（different causes on different occasions）**
> - 发现关系后，难以判断何为因、何为果，必须考虑**反向因果（reverse causation）**
> - 两个因素的关系**不能确立**因果关系（does not establish cause and effect）
> - 事后回溯假设生成于数据收集**之后**，因此无法被[[Falsification|证伪]]（Babbie, 2010, p. 462），即缺乏**可证伪性（nullifiability）**和确认性
> - 分类为**二分组的困难（problematic dichotomous classification）**
> - 解释困难与**事后归因谬误**的危险，即相信因为 X 先于 O，所以 X 引发 O
> - 匹配关键变量的尝试导致**样本缩减（shrinkage of sample）** Spector（1993, p. 43）指出这一风险；Lewis-Beck（1993, p. 43）报告了从 1,194 缩减到 46 的实例
> - 结论常基于过于**有限的样本或发生次数**
> - 经常未能挑选出**真正显著**的单一因素，且未能认识到事件有多个原因，不限于单一原因
> - 作为一种方法被认为**过于灵活（too flexible）**，缺乏可证伪性和确认性

---

### 15.6 设计一项事后回溯研究

#### 共变关系模型（X → O）

共变关系模型试图识别当前条件的先行因素，可表示为：

```
自变量 X  ──→  因变量 O
```

尽管事后回溯研究中的一个变量不能像真正实验研究中那样被确信为依赖于另一个变量，但仍通常将一个变量指定为自变量（X），另一个为因变量（O）。从左到右的维度指示时间顺序，但即使建立了时间顺序，也不可忽视反向因果的可能（pp. 313–314）。

在典型的共变关系研究中，收集与自变量（X）和因变量（O）分别相关的两组数据。关于自变量（X）的数据具有回溯性特征，因此容易受到所有历史证据所具有的弱点、局限和扭曲的影响。

> [!case] 学校士气低落：共变关系模型的应用
> 假设一所中学教职工士气低落（O），据推测是大约两年前一次重组的直接结果。可以识别若干区分新旧组织的关键因素，这些因素集体代表或包含了自变量 X，其数据可回溯性收集。这些因素可能包括：混合能力分班与团队教学的引入、课程创新、教师身份丧失、学生动机下降、学校招生区域变化或新校长的任命。
>
> 然后将这些因素对照当前教师态度测量（O），为研究者提供至少一些关于当前不满可能原因的线索（p. 314）。

---

#### 因果-比较模型（E vs C）

因果-比较模型可示意如下（pp. 314–315）：

> [!ref-table]- 因果-比较模型示意
> | | 自变量 | 因变量 |
> |---|---|---|
> | 实验组 E | X | O₁ |
> | 控制组 C | — | O₂ |

（虚线表示比较组 E 和 C 不是通过随机分配来等价的。）

使用这一模型时，假设自变量 X，然后比较两组：暴露于自变量 X 的实验组（E）和未暴露的控制组（C）。或检查两个在某些方面不同的组，然后通过调查可能的先行因素来解释差异。

这两种做法反映了因果-比较研究的两种路径（p. 315）：

> [!contrast-table] "从原因到效果" vs "从效果到原因"
> | 维度 | 从原因到效果（cause-to-effect） | 从效果到原因（effect-to-cause） |
> |---|---|---|
> | 起点 | 假设自变量 X | 已有两个在某方面不同的组 |
> | 分组 | 按暴露于 X 与否分为 E 组和 C 组 | 组已存在（自然分组） |
> | 操作 | 比较两组在因变量上的差异 | 调查可能的先行因素来解释差异 |
> | 与实验相似性 | 类似实验设计，只是 X 不可操纵 | 更接近探索性回溯 |

> [!contrast-table] 因果-比较设计 vs 真正实验设计的核心区别
> | 维度 | 真正实验 | 因果-比较研究（以及共变关系研究） |
> |---|---|---|
> | 自变量的性质 | **可操纵的（manipulable）**，在研究者控制之下 | **不可操纵的（non-manipulable）**，已发生，超出研究者控制 |
> | 由此导致的后果 | 可以确定因果方向，推断具有较高信心 | 因果方向不确定，推断是试探性的 |

---

### 15.7 事后回溯研究的操作程序

事后回溯研究关注发现数据中变量之间的关系，可通过因果模型或因果-比较模型来实现。

> [!proc] Lord（1973, p. 6）的八阶段程序
> 1. **界定问题并回顾[[Document|文献]]** 明确研究领域。通过[[Literature Review|文献回顾]]了解前人研究的议题、问题、障碍和发现（pp. 315–316）。
> 2. **陈述假设与前提假设** 明确待检验的假设以及研究程序所基于的前提或假设。
> 3. **选择被试与数据收集方法** 确定抽样策略（sampling）和数据收集工具。
> 4. **建立数据分类标准与类别** 建立尽可能无歧义、能发现关系和相似性的分类标准，使数据适合研究目的。
> 5. **收集"结果出现时"始终存在的因素数据** 收集在给定结果出现时始终在场的因素数据，舍弃这些因素不一致存在时的数据。
> 6. **收集"结果不出现时"始终存在的因素数据** 收集在给定结果未出现时始终在场的因素数据。
> 7. **比较两组数据** 将第 5 步数据从第 6 步数据中减去（即比较），以推断导致结果出现或不出现的原因。
> 8. **分析、解释并报告发现** 呈现分析结果。

> [!warning] 关键提醒
> Lord（1973, p. 7）强调：证据**说明（illustrate）**假设，不能**检验（test）**假设。事后回溯研究的核心弱点是缺乏对自变量影响因变量（因果设计）或影响组间因变量差异（因果-比较设计）的控制（p. 316）。

---

#### 引入控制的四种手段

尽管事后回溯研究被剥夺了变量控制和随机化原则，研究者仍可采用若干程序引入一定程度的控制（pp. 316–317）：

> [!feature] 四种控制手段
> - **匹配被试（[[Matching]]）** 在因果-比较设计中，将实验组和对照组的被试在重要且相关的特征上进行匹配，这是最常用的引入控制的手段。Ary et al.（2009）指出[[Matched Pairs Design|配对设计]]（matched pair designs；见第16章）需仔细匹配可能影响研究的相关特征（示例见 Leow, 2009）。困难在于：(1) 未必知道哪些因素是相关的，即哪些因素可能与因变量有关；(2) 无法匹配的被试将被淘汰，导致样本缩减。Lewis-Beck（1993, p. 43）报告了一个从 1,194 缩减到 46 的匹配后样本缩减实例（p. 316）。
> - **将额外自变量纳入设计并使用[[Analysis of Variance|方差分析]]** 作为匹配的替代程序，建议将外部自变量纳入设计然后使用方差分析。例如智力是相关的外部变量，但又无法通过匹配等方式控制时，可将其作为另一个自变量纳入研究，按智力水平对被试分类。通过方差分析揭示智力的主效应和[[Interaction Effect|交互效应]]，即使智力与因变量之间不能假设因果关系，也可显示组间在因变量上是否存在统计显著差异，以及智力对该差异的贡献（pp. 316–317）。
> - **选择同质性样本** 建议在某一给定变量上选择尽可能同质的样本。例如智力是相关外部变量时，可通过只纳入一个智力水平的被试来控制其效应。这将自变量与其他常见关联的变量分离开（disentangle），使任何发现的效应可被合理地归因于自变量（p. 317）。
> - **陈述并检验[[Alternative Hypothesis|替代假设]]** 明确陈述并检验能合理解释研究经验结果的其他可能假设。必须警惕，不要把事后回溯研究中第一个看起来合理的解释接受为必然唯一或最终的解释。经典案例：吸烟与肺癌的关系。卫生官员迅速接受"吸烟引发肺癌"的解释，而烟草公司提出替代假设：吸烟和肺癌可能都是某个尚未指明的第三因素的结果，即自变量和因变量都可能是单一共同原因的分别结果，这一可能性不可忽视。

---

## 关键引用

> [!citation-card]- 从结果逆向搜索原因
> [[Ex Post Facto Research|事后回溯研究]]字面意为事后（after the fact）；在社会和教育研究中，指回溯性地研究可能的因果-效应关系，通过观察已存在的条件或状态，逆时间搜索可能的因果因素。（第15章，p. 304）
>
> *Ex post facto means 'after the fact' ... In the context of social and educational research the phrase means 'retrospectively' and refers to those studies which investigate possible cause-and-effect relationships by observing an existing condition or state of affairs and searching back in time for plausible causal factors.*

> [!citation-card]- 概率性因果：试探性推断，无法确定性展示
> 只能报告已发生或正在发生的事情，通过谨慎关注抽样来设法将因素保持不变。自[[Variable|变量]]无法像在真正实验中那样被操纵，因为它们已经发生。因此推断在概率性[[Causality|因果关系]]的领域内进行：试探性地推断原因，无法确定性地展示因果关系。（第15章，p. 304）
>
> *Researchers can only report what has happened or what is happening, by trying to hold factors constant by careful attention to the sampling. [[Independent Variable|independent variables]] cannot be manipulated as in true experiments, as they have already happened. Hence the researcher is in the realms of [[Probabilistic Causation]], inferring causes tentatively rather than being able to demonstrate causality unequivocally.*

> [!citation-card]- 反向实验：事后回溯是实验的逻辑镜像
> 事后回溯设计在某种程度上相当于反向进行的[[Experimental Research|实验研究]]：从已经在某些方面存在差异的组出发，回溯搜索导致差异的因素，而不是取等效组并施加不同处理以产生[[Dependent Variable|因变量]]差异。Spector（1993, p. 42）认为事后回溯研究是一种试图将非实验研究设计转化为伪实验形式的程序。（第15章，pp. 305–306）
>
> *Some instances of ex post facto designs correspond to experimental research in reverse, for instead of taking groups that are equivalent and subjecting them to different treatments so as to bring about differences in the dependent variables to be measured, an ex post facto experiment begins with groups that are already different in some respect and searches in retrospect for the factor that brought about the difference.*

> [!citation-card]- [[Post Hoc Ergo Propter Hoc Fallacy|事后归因谬误]]与反向因果
> 因果关系的建立常常仅仅基于这样的前提：任何先于所研究现象发生的相关事件都被假定为其原因，即经典的事后归因谬误（post hoc, ergo propter hoc fallacy）。仅因一个变量在时间上先于另一个，不意味着前者引发后者。即使发现两个变量之间的关系，也必须认识到二者可能都是某个共同的第三因素的结果。还有反向因果的真实可能性，如心脏状况促进肥胖，反过来也可能成立。（第15章，pp. 309–310）
>
> *Frequently, causal relationships seem to be established on nothing more substantial than the premise that any related event occurring prior to the phenomenon under study is assumed to be its cause – the classical post hoc, ergo propter hoc fallacy. Even when we do find a relationship between two variables, we must recognize the possibility that both are individual results of a common third factor rather than the first being necessarily the cause of the second. There is also the real possibility of reverse causation.*

> [!citation-card]- 证据只能说明[[Hypothesis|假设]]，不能检验假设
> 事后回溯假设生成于数据收集之后，因此无法被[[Falsification|证伪]]（Babbie, 2010, p. 462）。正如 Lord（1973, p. 7）所强调的，证据说明假设，不能检验假设：假设不能在与推导出假设的同一数据上进行检验。（第15章，pp. 313, 316）
>
> *The ex post facto hypothesis is generated after the data have been collected, so it is not possible to disconfirm it (Babbie, 2010: 462). The evidence illustrates rather than tests the hypothesis here (Lord, 1973: 7).*

> [!citation-card]- 将事后回溯研究重新定位为调查
> 事后回溯设计更适合被理解为调查（surveys），作为需由更常规实验方法在日后检验的假设的有用来源。尽管有诸多局限，教育和心理学中许多重要研究都是事后回溯设计：通常别无选择，无法使一组人成为失败者、犯罪者、自杀者或脑损伤者，研究必须依赖已有群体。（第15章，p. 310）
>
> *Ex post facto designs are probably better conceived more circumspectly, not as experiments with the greater certainty that these denote, but more as surveys, useful as sources of hypotheses to be tested by more conventional experimental means at a later date. Many of our important investigations in education and psychology are ex post facto designs. There is often no choice in the matter: an investigator cannot cause one group to become failures, delinquent, suicidal, brain-damaged or dropouts.*

## 来源

- [[books/Cohen_Manion_Morrison_2011_Routledge/Cohen_Manion_Morrison_2011_Routledge|Cohen_Manion_Morrison_2011_Routledge]]
