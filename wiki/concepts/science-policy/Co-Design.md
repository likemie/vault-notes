---
title: Co-Design
aliases:
  - 协同设计
  - 协同优化
  - Design-Technology Co-Optimization
  - DTCO
  - System-Technology Co-Optimization
  - STCO
summary: "打破传统自上而下单向或离散工程壁垒，在微电子系统全生命周期中将底层物理材料、器件物理、制造工艺、高级封装、电路架构、算法软件直至终端应用需求进行全栈双向信息互通与联合优化的工程研发范式。"
type: concept
domain: "science-policy"
related_count: 0
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - theme/semiconductor
  - theme/science-policy
  - theme/innovation
  - theme/research-methodology
related_concepts:
  - "[[Paradigm]]"
  - "[[Hardware Security]]"
  - "[[Reliability]]"
  - "[[Flow]]"
  - "[[Variable]]"
  - "[[Computer Simulation]]"
  - "[[Document]]"
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts:
  - "[[International Schools Association]]"
  - "[[National Science and Technology Council]]"
related_arguments:
  - "[[Argument_NSTC_2024_MicroelectronicsResearch]]"
confidence: high
status: active
created: 2026-10-10
updated: 2026-10-10
---

# Co-Design

---

## 定义

> [!def] 核心定义
> **协同设计（Co-Design）** 指在微电子及复杂工程系统的研发全生命周期中，打破传统层级隔离与单向传递的设计流水线，将材料特性、物理模型、器件结构、制造工艺、异构封装、电路拓扑、算法体系及终端应用需求进行全栈双向贯通与同步联合优化的研发[[Paradigm|范式]]。在半导体技术领域，协同设计具体涵盖设计—技术协同优化（Design-Technology Co-Optimization, DTCO）与系统—技术协同优化（System-Technology Co-Optimization, STCO），通过在设计初期同步考量可制造性、热耗散极限、辐射耐受性、物理安全性与全生命周期能效，实现系统级指标的最优权衡。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 10, 13–16, 18–20)]]

> [!concept-lens] 概念透镜
> - **含义** 协同设计将传统自顶向下（Top-down）或自底向上（Bottom-up）的单向线性研发流程，重塑为多层级之间持续双向反馈、参数互锁与同步迭代的网状工程机制。
> - **用途** 解决先进节点下物理效应（热、电磁干扰、量子隧穿、寄生电容）与系统架构之间日益严重的耦合矛盾，使[[Hardware Security|硬件安全]]性与[[Reliability|可靠性]]成为前置内生属性而非后验补丁。
> - **边界** 协同设计不等于简单的跨部门例行协调会议，它依赖于统一的跨层次仿真建模工具链、标准化数据交换接口与共同约束求解算法。

> [!citation-card] 全栈双向协同设计的体系架构
> 协同设计要求在全技术栈之间建立持续的双向信息流，由终端应用需求逆向驱动底层材料与器件研发，同时由底层物理突破正向重塑上层算法与计算架构。这种全栈贯通机制是将安全性、可靠性与抗辐射性能从最初阶段内生嵌入系统的唯一有效路径。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, p. 13)]]
>
> *Integrated design refers to a constant bidirectional [[Flow]] of information from the top to the bottom of the stack driven by applications. Linking end-user needs to R&D is essential for rapid, focused technological development and deployment of research and development to the market... Such an integrated approach is the only way to guarantee that critical system attributes such as security, reliability, and radiation-hardness are designed in from the start and considered throughout the development cycle.*

> [!boundary]- 概念边界
> - 不等于 顺序线性设计（Sequential Waterfall Design）— 顺序设计中，材料与器件工程师完成物理工艺开发并冻结设计规则后，才交由电路设计人员进行逻辑综合与物理版图布局，容易在后期暴露严重热功耗或制造良率瓶颈且无法逆向修改底层参数。
> - 不等于 简单软件硬件协同设计（Narrow HW/SW Co-Design）— 早期软硬件协同设计仅局限于指令集架构（[[International Schools Association|ISA]]）与编译器层面的互补调整；现代半导体协同设计（DTCO/STCO）进一步向下贯穿至原子级材料晶格、量子传输物理与纳米封装界面。

---

## 概念辨析

> [!contrast-table] 芯片设计研发[[Paradigm|范式]]对比
> | 维度 | 协同设计（Co-Design / DTCO / STCO） | 经典抽象分层设计（Layered Modular Design） | 逆向定制设计（Post-Hoc Customization） |
> |---|---|---|---|
> | **信息流动模式** | 全栈多层级持续双向反馈与动态迭代 | 严格自顶向下或自底向上单向抽象传递 | 先行制造标准通用硬件，后期通过软件适配 |
> | **约束边界处理** | 将制造、热学与安全约束作为前置优化[[Variable\|变量]] | 上下层通过固定设计规则（Design Rules）刚性隔离 | 在既有固定物理硬件约束下被动妥协 |
> | **优化目标维度** | 算力、面积、能效、良率、安全与全生命周期成本 | 局部电路功能实现与标准单元面积压缩 | 快速推向市场与前期工程成本压缩 |
> | **主要工具支撑** | 跨尺度物理模型、云端数字孪生与多物理场仿真 | 标准电子设计自动化（EDA）静态综合与验证工具 | 硬件仿真器与后仿真微调补丁 |

---

## 核心要素

> [!feature] 协同设计的关键构成支柱
> - **多层级双向信息流（Bidirectional Stack Communication）** 实现从材料晶格—物理器件—异构封装—逻辑电路—算法软件—网络应用的连续双向参数传递。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 13, 20)]]
> - **跨尺度物理建模与仿真工具（Cross-Scale Modeling & [[Computer Simulation|simulation]]）** 支持从量子力学第一性原理计算、原子级缺陷演化，向上跨越至连续介质热力学、电路瞬态响应与系统级通信负载仿真的统一数字孪生工具。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 15, 25)]]
> - **前置内生安全与[[Reliability|可靠性]]验证（Design-in Security & Resilience）** 在架构与电路设计初始阶段即嵌入抗侧信道攻击、防物理篡改、零信任硬件根与抗辐射加固机制。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 13, 18–19)]]
> - **全生命周期能效与可持续性评估（Lifecycle Sustainability Metrics）** 将芯片制造耗能、化学品用量、运行动态功耗与器件退役回收机制纳入协同设计的目标函数。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 13, 19–20)]]

> [!logic-map]- 协同设计信息流模型
> ```mermaid
> flowchart TD
>     App["终端应用与系统需求\n(AI/通信/航天/边缘计算)"] <--> SW["算法与软件体系\n(编译优化 / 算子映射)"]
>     SW <--> Arch["计算架构与电路拓扑\n(近存计算 / 领域专用加速)"]
>     Arch <--> Pkg["异构集成与先进封装\n(3DHI / 芯片微互连 / 热管理)"]
>     Pkg <--> Dev["器件物理与微观结构\n(晶体管构型 / 寄生效应)"]
>     Dev <--> Mat["半导体材料与制造工艺\n(宽禁带/二维材料/制造工艺基线)"]
> ```

---

## 围绕概念形成的命题

---

### 命题一　协同设计是突破先进工艺节点物理限制与跨尺度瓶颈的核心路径

> [!concept-lens] 物理极限与系统级优化
> 围绕半导体物理微缩带来的互连延迟剧增、暗硅效应与热耗散危机，探讨跨层次联合优化如何释放系统级算力潜力。

> [!claim] [[National Science and Technology Council|NSTC]]
> **设计与工艺联合优化化解物理孤岛效应** 在先进制程下，微观物理效应已无法通过抽象黑箱进行有效隔离。单纯改进单一器件结构或单纯优化上层算法均无法获得性能突破。协同设计（DTCO/STCO）通过将工艺物理特性前置导入电路架构与编译器优化，能够在不依赖极限物理微缩的前提下，实现能效比与运算速度的成倍提升。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 10, 13–16)]]

---

### 命题二　协同设计将安全性与可持续性从外生补丁重塑为内生结构要素

> [!concept-lens] 安全性与全生命周期环境约束
> 围绕传统[[Hardware Security|硬件安全]]后期修补的脆弱性以及半导体制造能耗扩张，探讨全栈协同如何构建内生可信与低碳体系。

> [!claim] NSTC
> **全生命周期安全与绿色设计前置化** 面对日益复杂的硬件木马、侧信道物理攻击以及高昂的环境碳足迹，事后追加防护或工艺补救措施成本极高且效果有限。通过在材料选择、电路拓扑与系统级协议之间实施协同设计，研究团队能够在架构根基处构建零信任硬件信任根与低功耗绿色制造参数，从源头上保障国家安全关键基础设施的韧性。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 13, 18–20)]]

---

### 命题总览

> [!contrast-table] 协同设计核心命题概览
> | 命题方向 | 核心论断 | 技术与政策意涵 | 代表[[Document\|文献]] |
> |---|---|---|---|
> | **物理与架构效能** | 跨尺度全栈双向反馈突破传统单片物理微缩收益递减瓶颈 | 推动先进电子设计自动化（EDA）与跨尺度仿真工具研发 | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024, pp. 10–16)]] |
> | **安全与系统可持续性** | 硬件信任根与全生命周期低碳参数必须在前置阶段内生嵌入 | 指导国防关键芯片与绿色半导体制造重大研发计划布局 | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024, pp. 18–20)]] |
