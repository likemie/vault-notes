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
related_count: 14
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
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
  - "[[Process Design Kit]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[International Schools Association]]"
  - "[[National Science and Technology Council]]"
  - "[[National Strategy on Microelectronics Research]]"
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

---

## 概念演变

> [!dev-timeline] 概念演变
> - **1990s — 狭义软硬件协同设计（HW/SW Co-Design）** 随着嵌入式系统与专用集成电路（ASIC）复杂化，学界与产业界开始探索在系统级规约下将功能合理划分为硬件电路与软件代码，主要聚焦指令集架构（[[International Schools Association|ISA]]）与编译器的协同权衡。
> - **2010s — 设计—技术协同优化（DTCO）进入纳米制造节点** 在 16 纳米及更先进制程中，晶体管引入鳍式场效应晶体管（FinFET）与复杂多重曝光光刻，电路设计规则与底层制造工艺强烈耦合，设计—技术协同优化（Design-Technology Co-Optimization, DTCO）成为晶圆厂与无晶圆厂设计企业缩短研发周期的标准方法。
> - **2020s — 系统—技术协同优化（STCO）与三维堆叠** 面对后摩尔时代异构芯粒堆叠与内存墙瓶颈，系统—技术协同优化（System-Technology Co-Optimization, STCO）兴起，将优化边界从单一芯片单元推进至涵盖先进封装、三维热分布、片上供电网络与系统软件的宏观系统层。
> - **2024 — 全栈双向协同设计确立为国家级工程研发[[Paradigm|范式]]** [[National Science and Technology Council|白宫国家科学技术委员会]]（NSTC）在《微电子研究国家战略》中将协同设计定义为横跨材料、器件、封装、架构、软件直至全生命周期安全与可持续性的全栈双向信息互通机制，确立其为支撑微电子创新的顶层方法论。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 10, 13–16)]]

---

## 争议与批评

> [!debates] 协同设计学术争议与治理张力
>
> > [!axis] 工程架构[[Paradigm|范式]]：跨层级全局联合优化 vs 经典抽象分层黑箱
> > 争论微电子系统研发应打破层级界限推行端到端联合优化，还是维持经典计算机体系结构的抽象分层隔离。
> >
> > - **[[Argument_NSTC_2024_MicroelectronicsResearch|NSTC (2024)]]** 认为先进节点下物理效应与系统架构深度交织，维持严格抽象层级将造成巨大能效与算力浪费，必须打通全栈双向参数反馈。
> > - **计算机抽象体系学派** 强调严格的分层抽象（如晶体管模型、标准单元库、硬件描述语言）是半导体产业实现超大规模复杂分工与软件复用的基石，过度打破层级会导致设计空间维度爆炸与验证不可收敛。
>
> > [!axis] 商业知识产权壁垒：制造工艺数据全透明共享 vs 晶圆代工厂专有商业机密
> > 围绕全栈协同设计所需的高精度底层工艺与缺陷参数共享，与代工厂知识产权保护之间的商业博弈。
> >
> > - **开放设计与国家战略视角** 呼吁构建开放[[Process Design Kit|工艺设计套件]]（PDK）与云端仿真数字孪生平台，降低设计人员获取高精度底层参数的门槛。（pp. 14–16）
> > - **头部商业代工厂** 出于保护核心制造工艺机密与客户隔离考虑，倾向于提供高度抽象化、保守放宽安全裕量的商业 PDK，限制了深度软硬件定制潜力的完全释放。

---

## 实证数据

> [!ref-table]- 其他实证结果（无[[Effect Size|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024)]] | 全美微电子技术栈跨层协同（涵盖材料、器件物理、异构封装、近存计算电路与系统软件） | 跨部门国家科技战略规划与技术路线图论证 | 全栈双向协同设计维度、跨尺度仿真工具链、[[Hardware Security\|硬件安全]]内生嵌入与可持续性指标 | ① 确立涵盖 **6 大层级**（材料/器件/封装/架构/软件/应用）的双向信息流架构；② 提出跨越量子第一性原理到系统仿真的跨尺度数字孪生目标；③ 将硬件信任根与全生命周期环境能效确立为协同设计前置约束 | 跨部门国家战略政策文件与路线图规划（原文报告） | 确立全栈双向协同设计作为化解物理孤岛效应、提升系统能效与内生安全性的核心方法论 |

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联维度与贡献 |
> |:---|:---|:---|
> | [[Paradigm]] | Concept | 协同设计标志着从传统线性单向流水线向全栈双向网状迭代的工程范式转型。 |
> | [[Hardware Security]] | Concept | 协同设计将硬件信任根与形式化安全验证作为前置约束内生嵌入芯片架构。 |
> | [[Reliability]] | Concept | 协同设计通过在初始阶段联合考量热学与物理退化机制提升系统全生命周期可靠性。 |
> | [[National Science and Technology Council]] | Fact (Organization) | 制定《微电子研究国家战略》并统筹全栈协同设计跨部门重大研发计划的白宫协调机构。 |
> | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024)]] | Argument | 白宫[[National Strategy on Microelectronics Research\|国家微电子研究战略]]，确立全栈双向协同设计为四大战略科技目标之一。 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_NSTC_2024_MicroelectronicsResearch|NSTC (2024)]] — 提出贯穿底层物理材料至终端应用的全栈双向协同设计（DTCO/STCO）[[Paradigm|范式]]，将[[Hardware Security|硬件安全]]与可持续性前置内生嵌入微电子系统架构。

