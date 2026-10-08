---
title: Five Whys
aliases:
  - 五问法
  - 5个为什么
  - 五个为什么
  - 5 Whys
  - 根本原因分析法
  - 5-Why Analysis
summary: "由大野耐一在丰田生产方式中创立、后被帕兰提尔拓展至软件工程与人际系统诊断的根本原因分析（RCA）质性方法；通过连续五层递进追问“为什么”，由表层故障穿透至深层物理机理、流程设计、考核激励与高层博弈根源，倡导以宽容免责的工程文化排查系统缺陷。"
type: method
method_type: qualitative
method_family: "qualitative"
method_related_count: 22
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dbeafe"
tags:
  - method/qualitative
  - theme/root-cause-analysis
  - theme/engineering-mindset
  - theme/organizational-diagnosis
  - theme/lean-production
related_concepts:
  - "[[Lean Production]]"
  - "[[Totally Pedagogised Society]]"
  - "[[Unit of Analysis]]"
  - "[[Assemblage]]"
  - "[[Epistemology]]"
  - "[[Epoché]]"
  - "[[Causality]]"
  - "[[Technological Republic]]"
  - "[[Chain of Evidence]]"
  - "[[Bureaucracy]]"
  - "[[Hypothesis]]"
  - "[[Engineering Mindset]]"
  - "[[Constructive Disobedience]]"
  - "[[Determinism]]"
related_theories:
  - "[[Hedgehog and Fox Model]]"
related_methods:
  - "[[Sample Size Determination]]"
  - "[[Case Study]]"
  - "[[In-depth Interview]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons:
  - "[[Taiichi Ohno]]"
related_facts:
  - "[[Palantir Technologies]]"
related_arguments:
  - "[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14]]"
confidence: high
status: draft
created: 2026-10-08
updated: 2026-10-08
---

# Five Whys

---

## 定义

> [!def] 方法定义
> **五问法（Five Whys）** 是一种用于探究复杂物理系统故障、软件工程交付延误以及组织跨部门协作障碍深层机理的递进式质性因果诊断方法。该方法由丰田汽车前生产副社长[[Taiichi Ohno|大野耐一]]在创立[[Lean Production|丰田生产方式]]（[[Totally Pedagogised Society|TPS]]）时系统化，后被[[Palantir Technologies|帕兰提尔科技]]等前沿软件企业拓展至“人际与制度系统”诊断；其核心准则在于：当系统出现任何偏差或故障时，坚决抵制将责任归咎于具体个人的懒惰倾向，而是通过连续追问至少五次“为什么”，顺着因果线索一追到底，直至穿透表象锁定导致系统失灵的根本设计缺陷、资源配置失衡、激励机制扭曲或高层人际博弈根源。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14|(Karp & Zamiska, 2025, pp. 164–166)]]

> [!method-scope] 方法范围
> - **研究对象** 工业制造生产线停机、大型软件系统延期或崩溃、跨部门协同梗阻、政策执行偏差及高层决策扭曲。
> - **问题类型** 因果机制解释、深层根本原因诊断（Root Cause Analysis, RCA）、组织流程优化与制度漏洞排查。
> - **[[Unit of Analysis|分析单位]]** 具体的故障事件、延期项目、工作流断裂点或组织人际博弈案例。
> - **输出形式** 多层递进因果链条诊断流程图、不指责具体个人的免责式系统审查报告与结构性纠错行动方案。

> [!citation-card]- 关键定义
> 排查任何复杂系统故障的原因，无论是企业级软件平台还是内燃机[[Assemblage|装配]]线，都必然要求将焦点放在系统内部的运行机制上。在帕兰提尔，我们将这一探究方法扩展到对作为软件前置条件的人际系统的剖析中……通过追踪因果链条，往往能够解开阻碍组织发展的核心死结。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14|(Karp & Zamiska, 2025, pp. 164–166)]]
>
> *Identifying the reasons for the failure of a system, whether it be an enterprise software platform or an assembly line for internal combustion engines, necessarily requires a focus on the inner workings and mechanics of the system at issue. At Palantir, we build on this method of inquiry to incorporate an analysis and indeed acknowledgment of the human systems that are precursors to the software that we are building.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为组织与工程系统的故障具有深层的非线性多层因果嵌套性；表面看到的失误往往只是底层制度、流程或人际结构扭曲的末端病征（企业蝴蝶效应）。
> - **研究者角色** 诊断者必须秉持客观求实、[[Epoché|悬置]]道德批判且完全免责（Blameless）的中立态度，营造心理安全环境以促使真实信息浮现。
> - **有效性标准** 因果链条逻辑自洽性、每一步推论的证据可验证性与整改措施对同类故障的彻底阻断力。
> - **不声称回答的问题** 不能自动替代大[[Sample Size Determination|样本量]]化[[Causality|因果推断]]；不能通过主观臆测跳跃关键环节。

> [!method-stack] 方法层级
> - **研究设计** 质性回溯性[[Case Study|案例研究]]与事故复盘诊断。
> - **数据收集** 机器运行日志、代码提交版本库、财务与预算审批记录、当事人[[In-depth Interview|深度访谈]]与现场勘验。
> - **分析方法** 五层因果递进追溯、因果链条逆向回溯、组织激励机制结构性穿透。
> - **辅助技术** 因果流程图（Mermaid）、免责复盘报告模板、行动纠错跟踪表。

---

## 研究程序

> [!proc] 通用程序
> 1. **界定初始问题** 清晰客观地陈述所发生的故障或偏差事件，记录精确的时间、地点、涉及部门与可观察的物理事实。
> 2. **开展第一层追问** 询问“为什么该具体现象会发生”，基于现场直观证据确认直接的技术、操作或时间瓶颈。
> 3. **递进多层追因** 针对上一层的回答连续追问“为什么”，由表及里穿透技术参数、执行流程、资源配置与考核激励机制。
> 4. **排除个人指责** 严格抑制将原因归结为“某某粗心或能力不足”的懒惰倾向，将追问重心锁定在促使该错误必然发生的制度环境或结构漏洞上。
> 5. **形成结构对策** 当追问触及根本原因（Root Cause）后，制定针对性的结构性防范与系统修复措施，并撰写正式的免责复盘报告。

---

### 经典物理制造程序：大野耐一的丰田五问法（Toyota 5 Whys）

[[Taiichi Ohno|大野耐一]]在《[[Lean Production|丰田生产方式]]》（[[Totally Pedagogised Society|TPS]]）中阐述的机械故障标准排查链条，通过连续五次追问，将表层电气停机穿透至底层设计过滤缺陷：

> [!proc] 丰田生产方式中五问法排查机械故障的经典五步
> 1. **第一问：为什么机器停机了？**
>    - **直接原因** 因为保险丝因过载而发生熔断。
> 2. **第二问：为什么保险丝会过载？**
>    - **运行诱因** 因为轴承润滑不足，导致摩擦阻力激增引发电机过载。
> 3. **第三问：为什么润滑不足？**
>    - **机械瓶颈** 因为润滑油泵供油量不足，未能持续加压。
> 4. **第四问：为什么润滑油泵供油不足？**
>    - **部件损伤** 因为油泵的泵轴严重磨损，产生了晃动与气蚀。
> 5. **第五问：为什么泵轴会磨损？**
>    - **根本原因（Root Cause）** 因为进油口未加装过滤网，导致金属碎屑进入泵体磨损泵轴。（**根本对策** 在进油口加装滤网）（pp. 164–165）。

---

### 组织与人际系统程序：帕兰提尔的企业级软件五问法（Palantir 5 Whys）

卡普与扎米斯卡在《[[Technological Republic|技术共和国]]》中将五问法拓展至软件工程背后的“人际与制度系统”，揭示出软件交付延期往往源于高层人际博弈与考核导向扭曲引发的“企业蝴蝶效应”：

> [!proc] [[Palantir Technologies|帕兰提尔]]软件交付延期与组织人际系统排查的经典五步
> 1. **第一问：为什么企业级软件更新未能在周五截止期前发布？**
>    - **直接诱因** 因为工程审查团队仅有两天时间来审查代码草案。
> 2. **第二问：为什么团队只有两天时间审查代码？**
>    - **资源瓶颈** 因为该团队在去年底的预算审查周期中失去了 6 名核心软件工程师。
> 3. **第三问：为什么该团队的预算会被削减？**
>    - **部门调度** 因为该业务部门主管应另一位业务负责人的要求，将研发优先级转移到了其他领域。
> 4. **第四问：为什么会提出转移优先级的要求？**
>    - **制度激励** 因为公司推行了全新的薪酬考核模式，过度激励特定领域的增长而牺牲了其他方向。
> 5. **第五问：为什么某些领域会被优先选择而牺牲其他领域？**
>    - **根本原因（Root Cause）** 因为公司最高管理层的两位高管之间存在长期的个人争端与博弈。（**根本对策** 理顺高层权力结构，重构薪酬激励方案）（pp. 165–166）。

> [!logic-map]- 软件延期的企业蝴蝶效应因果链条
> ```mermaid
> flowchart LR
>   Q1["<b>第一问：表层现象</b><br>软件更新未能按时交付<br><i>直接诱因：审查仅剩2天</i>"] --> Q2["<b>第二问：执行瓶颈</b><br>代码草案积压无法消化<br><i>资源瓶颈：损失6名工程师</i>"]
>   Q2 --> Q3["<b>第三问：资源分配</b><br>部门预算与编制被削减<br><i>部门调度：转移研发重心</i>"]
>   Q3 --> Q4["<b>第四问：制度设计</b><br>研发优先级被强制调配<br><i>制度激励：新考核模型扭曲</i>"]
>   Q4 --> Q5["<b>第五问：深层根因</b><br>考核导向倾斜与部门偏袒<br><i>核心根源：高管人际博弈</i>"]
> ```

---

### 物理系统与人际系统诊断范式对比

> [!contrast-table] 物理制造系统 vs. 软件与人际系统的五问法诊断对比
> | 诊断维度 | 丰田物理制造五问法（TPS） | 帕兰提尔软件与人际五问法 |
> |:---|:---|:---|
> | **排查对象** | 物理机械装置、[[Assemblage\|装配]]线设备、工件物理损伤 | 软件代码架构、跨部门研发协同、高管决策动态 |
> | **追问终点** | 机械零件磨损、物理过滤与润滑设计缺陷 | 薪酬考核导向、资源分配机制与高层人际博弈 |
> | **根本对策** | 加装进油滤网、改进润滑泵机械防护设计 | 理顺高层权力结构、重构组织考核与激励模型 |
> | **文化前提** | 现场现物（Genba）、尊重一线工人操作反馈 | 彻底免责保护（Blameless）、打破对失业与问责的恐惧 |

---

## 质性诊断程序与现场证据链

> [!sample-panel] 现场诊断与证据收集规范
> | 维度 | 具体规范与操作要求 |
> |---|---|
> | **材料来源** | 系统监控日志、Git 代码提交与审查记录、财务预算与编制调整单、考核制度文件、当事人[[In-depth Interview\|深度访谈]]记录。 |
> | **调查文化原则** | **免责保护（Blameless）** 坚决禁止将技术与流程故障归咎于一线员工，消除惩罚恐惧。 |
> | **[[Chain of Evidence\|证据链]]要求** | 每一步追问必须有确凿可查验的客观记录支撑，严禁凭主观臆想推断因果联系。 |
> | **报告输出** | 形成正式书面复盘报告，完整记录因果链条，明确流程与制度修复责任人。 |

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 大型企业级软件交付故障复盘、跨职能研发团队协作受阻诊断、制造业质量与安全隐患排查、组织流程再造。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14|(Karp & Zamiska, 2025, pp. 164–166)]]
> - **谨慎使用** 缺乏组织心理安全感、员工普遍因恐惧问责而隐瞒真相的[[Bureaucracy|科层制]]机构（必须首先建立制度化免责保护机制）。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14|(Karp & Zamiska, 2025, p. 166)]]
> - **不适合使用** 纯粹由不可抗力自然灾害引起的单次偶发破坏（无需过度穿透人际博弈）。

---

## 局限性

> [!method-limits] 方法局限
> - **停顿过早风险** 调查团队常常在追问两到三次后便止步于“某人粗心”或“某部门执行不力”等浅层原因，未能彻底触及结构与激励根源。
> - **主观偏见引导** 若调查主持者预设立场，容易在追问过程中选择性采纳线索，强行将原因引导至特定部门。
> - **文化依赖性** 极度依赖开放宽容、鼓励主动暴露问题的工程文化；在恐惧掩盖文化的组织中容易退化为形式主义应付。
> - **线性[[Hypothesis|假设]]局限** 真实世界常存在网状因果与多元反馈回路，单一链条追问可能简化复杂的非线性系统交互。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Engineering Mindset]] | 概念 | 支撑理念：五问法构成了工程思维在组织微观管理中求真务实、直面运行反馈的核心诊断工具。 |
> | [[Lean Production]] | 概念 | 起源传统：[[Taiichi Ohno\|大野耐一]]在丰田生产方式中开创了以消除浪费和追溯质量根因为目标的五问法体系。 |
> | [[Constructive Disobedience]] | 概念 | 文化保障：为一线工程师在五问法复盘中如实指出上层决策与制度漏洞提供心理抗体。 |
> | [[Hedgehog and Fox Model]] | 理论 | [[Epistemology\|认识论]]基础：反对机械[[Determinism\|决定论]]，以狐狸型经验探索视角耐心解开组织制度与人际关系的复杂死结。 |
> | [[Case Study]] | 质性方法 | 研究形式：五问法本质上是一种深度事故与偏差案例的质性机制解构方法。 |

---

## 使用此方法的研究

> [!evidence-grid-a]- [[Correlational Research|相关研究]]索引
> - [[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14]] — 详述[[Taiichi Ohno|大野耐一]]丰田机械排查案例与[[Palantir Technologies|帕兰提尔]]二十年间开展数千次五问法复盘以穿透软件交付延期至高层人际博弈的实战案例。
