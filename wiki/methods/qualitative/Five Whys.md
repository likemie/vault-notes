---
title: Five Whys
aliases:
  - 五问法
  - 5个为什么
  - 五个为什么
  - 5 Whys
  - 根本原因分析法
  - 5-Why Analysis
summary: "由日本工业工程师大野耐一在丰田生产方式中确立的根本原因分析（RCA）质性诊断方法；通过对故障或失误现象进行至少五层递进式因果追问，穿透表面偶然现象与个人失误，系统排查组织结构、激励机制与工程设计深层隐患。"
type: method
method_type: qualitative
method_family: "qualitative"
method_related_count: 10
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dbeafe"
tags:
  - method/qualitative
  - theme/root-cause-analysis
  - theme/engineering-mindset
  - theme/organizational-diagnosis
related_concepts:
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Chain of Evidence]]"
  - "[[Bureaucracy]]"
related_theories: []
related_methods:
  - "[[In-depth Interview]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons:
  - "[[Taiichi Ohno]]"
  - "[[Alexander Karp]]"
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
> **五问法（Five Whys）** 是一种用于探究复杂工程故障、产品缺陷或组织执行障碍深层机理的递进式质性诊断方法。该方法要求在问题出现时，不满足于最直接的表层解释或将责任简单归咎于当事人的疏忽，而是通过连续追问至少五次“为什么”，沿着因果链条逆向追踪，直至锁定导致系统失灵的根本设计缺陷、流程断裂或制度激励扭曲。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14|(Karp & Zamiska, 2025, pp. 164–166)]]

> [!method-scope] 方法范围
> - **研究对象** 工业制造故障、大型软件系统延期或崩溃、组织跨部门协同梗阻、公共政策执行偏差。
> - **问题类型** 因果机制解释、系统性根因诊断、流程优化与制度漏洞排查。
> - **[[Unit of Analysis|分析单位]]** 具体的故障事件、延期项目、工作流断裂点或组织事故案例。
> - **输出形式** 多层递进因果链条诊断图、不指责个人的系统性根因审查报告与纠错行动方案。

> [!citation-card] [[Taiichi Ohno|大野耐一]]与卡普论五问法的系统性因果追踪
> 在工业制造中，大野耐一列举了一台机器因保险丝过载停机的例子，通过进一步追问发现是由泵破损引起，最终深层原因是金属零件磨损。在软件企业中，[[Alexander Karp|亚历山大·卡普]]将这种方法扩展至对人类系统与人际激励动态的剖析，指出排查系统故障必须追踪错综复杂的因果链条。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14|(Karp & Zamiska, 2025, pp. 164–166)]]
>
> *Ohno provided an example of a machine that stopped working because of an overloaded fuse, which upon further inquiry had been caused by a broken pump and ultimately worn metal parts... At [[Palantir Technologies|Palantir]], we build on this method of inquiry to incorporate an analysis and indeed acknowledgment of the human systems that are precursors to the software that we are building.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为组织与工程系统的故障具有多层因果嵌套性；表面看到的失误往往只是深层制度或物理结构缺陷的末端病征。
> - **研究者角色** 诊断者需秉持中立、非指责（Blameless）的调查态度，引导团队直面真实事实而非掩盖问题。
> - **有效性标准** 解释连贯性、因果链条证据充分性与整改方案的根治性。
> - **不声称回答的问题** 不能自动替代大样本统计推断；不能单纯依靠主观猜测跳过事实求证。

---

## 研究程序

> [!proc] 通用诊断程序
> 1. **界定初始问题** 清晰客观地陈述所发生的故障或偏差事件，记录精确的时间、地点与可观察物理表现。
> 2. **开展第一层追问** 询问“为什么该具体现象会发生”，基于现场直观证据确认直接技术或操作诱因。
> 3. **递进多层追因** 针对上一层的回答连续追问“为什么”，由表及里穿透技术参数、执行流程、资源配置与上层激励机制。
> 4. **排除个人指责** 严格抑制将原因归结为“某某粗心或能力不足”的懒惰倾向，将追问重心锁定在促使该错误必然发生的制度环境或结构漏洞上。
> 5. **形成闭环整改** 当追问触及根本原因（Root Cause）后，制定针对性的结构性防范与修复措施，并撰写正式的免责复盘报告。

### 质性分析程序

> [!sample-panel] 现场诊断与证据收集
> | 维度 | 信息 |
> |---|---|
> | 材料来源 | 系统运行日志、代码提交记录、预算与会议纪要、当事人[[In-depth Interview\|深度访谈]]与现场观察。 |
> | 调查原则 | 心理安全优先、禁止秋后算账、坚持现场现物。 |
> | [[Chain of Evidence\|证据链]]要求 | 每一步“为什么”的推论都必须具备可验证的文字、代码或流程证据支持。 |

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 复杂技术系统运维事故复盘、跨职能研发团队协作受阻诊断、制造生产线质量缺陷排查。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14|(Karp & Zamiska, 2025, pp. 164–166)]]
> - **谨慎使用** 缺乏组织心理安全感、员工普遍因恐惧问责而隐瞒真相的[[Bureaucracy|科层制]]机构（需先建立免责保护机制）。[[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14|(Karp & Zamiska, 2025, p. 166)]]
> - **不适合使用** 纯粹由不可抗力自然灾害引起的单次偶发破坏（无需过度追溯人际系统）。

---

## 局限性

> [!method-limits] 方法局限
> - **调查者偏误** 若调查者预设立场，容易在追问过程中强行引导至特定部门或个人。
> - **停顿过早风险** 调查团队常常在追问两到三次后便止步于浅层管理原因，未能彻底触及结构根源。
> - **文化依赖性** 极度依赖开放宽容、鼓励暴露问题的工程文化；在恐惧掩盖文化的组织中容易沦为形式主义。

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Karp_Zamiska_2025_Technological_Republic_Ch14]] — 记录[[Taiichi Ohno|大野耐一]]在丰田创立五问法及[[Palantir Technologies|帕兰提尔]]两十年间开展数千次五问法复盘以诊断大型企业软件延期深层人际系统根因的实践案例。
