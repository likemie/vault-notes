---
title: Heterogeneous Integration
aliases:
  - 异构集成
  - 3D Heterogeneous Integration
  - 3DHI
  - 三维异构集成
  - Chiplet
  - 芯粒技术
summary: "将采用不同半导体材料、制造工艺节点与特定功能特性的独立制造单元（如数字CMOS、射频、光子、高带宽存储器、微机电系统与模拟器件）在高阶微互连基板或三维堆叠结构中紧密集成的工程范式与制造技术，旨在突破单芯片单片集成物理极限，实现后摩尔时代的系统级算力与能耗效能扩展。"
type: concept
domain: "science-policy"
related_count: 17
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/semiconductor
  - theme/science-policy
  - theme/innovation
  - theme/industrial-policy
related_concepts:
  - "[[Paradigm]]"
  - "[[Assemblage]]"
  - "[[Process Design Kit]]"
  - "[[Commercial Off-The-Shelf]]"
  - "[[Innovation Ecosystem]]"
  - "[[Document]]"
  - "[[Pilot Scale Platform]]"
  - "[[Variable]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[National Science and Technology Council]]"
  - "[[National Advanced Packaging Manufacturing Program]]"
  - "[[Taiwan Semiconductor Manufacturing Corporation]]"
  - "[[DARPA]]"
  - "[[CHIPS and Science Act]]"
  - "[[National Strategy on Microelectronics Research]]"
related_arguments:
  - "[[Argument_NSTC_2024_MicroelectronicsResearch]]"
confidence: high
status: active
created: 2026-10-10
updated: 2026-10-10
---

# Heterogeneous Integration

---

## 定义

> [!def] 核心定义
> **异构集成（Heterogeneous Integration, HI）** 指将由不同半导体材料、不同制造工艺节点以及不同功能特质分别加工制造而成的独立单元（如先进互补金属氧化物半导体（Complementary Metal-Oxide-Semiconductor, CMOS）逻辑核心、射频前端、硅光子光互连模块、高带宽存储器及模拟器件），通过先进高密度封装基板、微凸点互连、硅通孔（Through-Silicon Via, TSV）或无凸点混合键合等三维堆叠技术（3D Heterogeneous Integration, 3DHI），整合为单个系统级封装或微系统的工程技术与制造[[Paradigm|范式]]。该技术摆脱了对传统单片二维晶体管物理尺寸微缩（摩尔定律）的单一依赖，通过模块化芯粒（Chiplets）协同实现系统层面的算力密度跃升、互连延迟压缩与能效最优化。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 2–3, 10, 17–18)]]

> [!concept-lens] 概念透镜
> - **含义** 异构集成将芯片性能演进的重心从单一硅基晶圆表面二维特征尺寸的物理微缩，转向多维空间内异质材料、异构工艺节点与功能专用模块的物理堆叠与紧密耦合。
> - **用途** 为后摩尔时代的超算、人工智能边缘加速、空间辐射防护与高频通信系统提供突破物理极限的实现路径，同时大幅降低尖端芯片全掩膜流片的设计与试错成本。
> - **边界** 异构集成不等于传统的印刷电路板（Printed Circuit Board, PCB）板级[[Assemblage|组装]]，它在微米甚至亚微米尺度实现微互连与键合；也不等同于单一硅基晶圆上的单片系统级芯片（System-on-Chip, SoC）制造。

> [!citation-card] 异构集成的战略功能定位
> 随着微电子应用场景从超级计算机延伸至边缘传感和高辐射航天载荷，芯片性能需求呈现高度分化，迫使半导体技术偏离单纯依赖晶体管特征尺寸微缩的传统路径。通过异构集成与三维芯粒堆叠，研究人员能够将差异化半导体材料与专用架构无缝组合，驱动后摩尔时代微电子性能的持续拓展。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 3, 12, 17)]]
>
> *As microelectronic devices have become pervasive, their key performance requirements have become increasingly varied, necessitating a divergence from the traditional scaling in feature size exemplified by Moore’s Law... These application-specific requirements are driving an increased diversification of microelectronics, which will be enabled and advanced by approaches such as heterogeneous integration and chiplets.*

> [!boundary]- 概念边界
> - 不等于 单片系统级芯片（System-on-Chip, SoC）— 单片 SoC 必须在同一块硅晶圆上采用同一制造节点加工所有数字、模拟与射频电路，受制于掩膜面积上限、良率断崖式下降及不同工艺兼容性矛盾；异构集成允许不同功能单元各自选用最成熟高效的材料与工艺节点分别制造后再行封装。
> - 不等于 传统多芯片模块（Multi-Chip Module, MCM）— 传统多芯片模块依赖毫米尺度的引线键合或低密度封装基板，互连线长、寄生电容大且带宽受限；现代三维异构集成采用微米/亚微米级微凸点、硅中介层与直接混合键合，提供与单芯片相当的高带宽高密度互连。

---

## 概念辨析

> [!contrast-table] 芯片集成[[Paradigm|范式]]对比
> | 维度 | 异构集成（Heterogeneous Integration） | 单片系统级芯片（Monolithic SoC） | 板级系统集成（System-on-Board） |
> |---|---|---|---|
> | **材料与工艺** | 允许多种异质材料（Si、SiGe、GaN、InP等）与不同节点混合 | 必须统一于单一晶圆及单一制造工艺基线 | 离散元器件焊装于 PCB 基板 |
> | **互连密度与延迟** | 极高（微米级间距、硅通孔与直接键合），纳秒级低延迟 | 最高（单芯片内部金属层互连），极低延迟 | 较低（毫米级走线），寄生效应与延迟显著 |
> | **研发成本与试错** | 模块化芯粒可独立迭代复用，试错成本与良率风险较低 | 尖端节点全掩膜开发成本极高，单点缺陷导致整片报废 | 开发成本低，但体积与功耗无法满足前沿计算需求 |
> | **主要技术挑战** | 多物理场热管理、异质界面应力、多芯片协同测试与封装规程 | 掩膜物理尺寸极限、暗硅效应、异质功能集成工艺不兼容 | 互连带宽瓶颈、功耗过高、外形尺寸庞大 |

---

## 核心要素

> [!feature] 异构集成的关键支撑要素
> - **模块化芯粒架构（Modular Chiplet Architecture）** 将庞大复杂的单芯片解构为具有独立功能的标准化小芯片（Chiplets），支持跨厂商、跨工艺节点的即插即用与灵活配置。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 10, 17)]]
> - **微尺度高密度互连技术（Micro-Scale Interconnects）** 包含微凸点（Micro-bumps）、硅中介层（Silicon Interposer）、硅通孔（TSV）与晶圆级直接混合键合（Direct Hybrid Bonding），提供超高互连线密度与超低信号传输损耗。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 17–18)]]
> - **多物理场表征与计量（Multi-Physics Metrology）** 跨越微米到纳米尺度的无损缺陷检测、界面应力分析、三维热分布感知与高频电磁兼容测量规程。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 17–18, 28)]]
> - **[[Assemblage|装配]]设计套件（Assembly Design Kit, ADK）** 与[[Process Design Kit|工艺设计套件]]（PDK）相配套，为跨芯片装配、热机械应力模拟与信号完整性仿真提供标准化的数字模型与设计规则。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 17, 24)]]

> [!logic-map]- 异构集成技术体系
> ```mermaid
> flowchart TD
>     A["应用需求多元化\n(算力/功耗/极端环境/高频)"] --> B["异质材料与工艺解耦\n(CMOS / RF / 光子 / 存储)"]
>     B --> C["模块化芯粒设计\n(Chiplet IP & ADK)"]
>     C --> D["三维高密度互连与堆叠\n(3DHI / TSV / Hybrid Bonding)"]
>     D --> E["多物理场协同测试与封装\n(热管理 / 机械应力 / 计量)"]
>     E --> F["系统级性能与能效突破\n(超越摩尔定律)"]
> ```

---

## 围绕概念形成的命题

---

### 命题一　异构集成打破物理微缩单维限制重构半导体系统性能扩展范式

> [!concept-lens] 物理极限与系统算力扩展
> 围绕二维晶体管特征尺寸逼近原子极限导致的物理收益递减，探讨如何通过多维多材料空间集成重塑系统算力曲线。

> [!claim] [[National Science and Technology Council|NSTC]]
> **后摩尔时代性能演进重心转移** 随着半导体特征尺寸微缩至 3 纳米及以下节点，量子隧穿效应与热耗散瓶颈显著加剧，单纯依赖二维微缩所获得的算力收益已无法满足下一代人工智能与高性能计算需求。异构集成通过在垂直维度紧密集成专用逻辑、近存计算模块与光学互连器件，将性能提升的主引擎从器件微观尺寸转移到系统级微互连架构，确立了微电子演进的全新技术路线。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 3, 10–12, 17–18)]]

---

### 命题二　异构集成推动设计与制造解耦并重塑微电子创新门槛

> [!concept-lens] 产业分工与中试准入门槛
> 围绕尖端制程高昂全掩膜成本对大学与初创企业的排斥，探讨芯粒复用与先进封装如何降低硬件创新试验成本。

> [!claim] NSTC
> **硬件敏捷迭代与创新去中心化** 传统单片先进制程流片动辄数千万美元的掩膜成本，使得学术界与初创企业被阻隔在硬件创新前沿之外。异构集成允许科研人员将创新的专用功能单元与商业现货（[[Commercial Off-The-Shelf]], COTS）成熟芯粒通过标准化[[Assemblage|装配]]设计套件（Assembly Design Kit, ADK）进行封装级集成，在显著压缩研发周期与流片资本开支的同时，为跨学科原型验证与硬件[[Innovation Ecosystem|创新生态]]的繁荣提供了制度与技术支撑。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 14, 17–18, 28)]]

---

### 命题总览

> [!contrast-table] 异构集成核心命题概览
> | 命题方向 | 核心论断 | 技术与政策意涵 | 代表[[Document\|文献]] |
> |---|---|---|---|
> | **物理与系统演进** | 性能跃升重心由单片晶体管微缩转向三维多材料系统耦合 | 确立三维异构集成（3DHI）作为国家战略技术主攻方向 | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024, pp. 3, 10–18)]] |
> | **产业生态与创新准入** | 芯粒复用与封装解耦大幅降低尖端硬件原型验证门槛 | 支撑[[National Advanced Packaging Manufacturing Program\|国家先进封装制造计划]]（NAPMP）与[[Pilot Scale Platform\|中试平台]]建设 | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024, pp. 14, 17–28)]] |

---

## 概念演变

> [!dev-timeline] 概念演变
> - **1980s — 多芯片模块（MCM）起源** 早期多芯片模块（Multi-Chip Module, MCM）采用引线键合与厚膜/薄膜陶瓷基板，首次将多个未封装裸片集成于同一封装体内，用于大型机与高端航空航天电子系统，但受制于互连间距大与信号延迟高。
> - **2000s — 系统级封装（SiP）与消费电子普及** 随着智能手机对微型化与多功能集成的爆发式需求，系统级封装（System-in-Package, SiP）兴起，在有机基板上将基带芯片、射频收发器与存储器堆叠封装，开启多器件板级向封装级整合的过渡阶段。
> - **2010s — 2.5D/3D TSV 先进微互连技术突破** 硅通孔（Through-Silicon Via, TSV）与硅中介层（Silicon Interposer）实现商业化量产，[[Taiwan Semiconductor Manufacturing Corporation|台积电]] CoWoS 与英特尔 EMIB 等先进封装平台将逻辑芯片与高带宽存储器（High Bandwidth Memory, HBM）紧密相连，大幅突破单芯片互连带宽瓶颈。
> - **2020s — 芯粒（Chiplets）架构与 UCIe 标准化** 芯粒互连通用标准（Universal Chiplet Interconnect Express, UCIe）等开放行业规范确立，模块化芯粒生态形成，[[DARPA|美国国防高级研究计划局]]（Defense Advanced Research Projects Agency, DARPA）启动三维异构集成（3D Heterogeneous Integration, 3DHI）重大攻关计划。
> - **2024 — 国家战略确立三维异构集成为后摩尔核心[[Paradigm|范式]]** [[National Science and Technology Council|白宫国家科学技术委员会]]（NSTC）在《微电子研究国家战略》中将先进封装与异构集成确立为全美四大战略科技目标之一，依托[[National Advanced Packaging Manufacturing Program|国家先进封装制造计划]]（NAPMP）系统推进[[Assemblage|装配]]设计套件（ADK）与跨材料 3DHI 平台。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 10, 17–18)]]

---

## 争议与批评

> [!debates] 异构集成学术争议与工程张力
>
> > [!axis] 技术演进路线：单片微缩优先 vs 三维异构集成主导
> > 争论微电子算力提升应继续依托晶体管特征尺寸向埃米（Angstrom）节点极限微缩，还是全面转向异构集成与三维堆叠。
> >
> > - **[[Argument_NSTC_2024_MicroelectronicsResearch|NSTC (2024)]]** 认为单纯依赖二维物理尺寸微缩已遭遇热耗散与制造成本收益递减瓶颈，多材料三维异构集成是后摩尔时代算力跃升的根本方向。
> > - **单片集成物理学派** 强调单片集成在超高频互连与信号完整性上仍具不可替代的物理优势，三维异构堆叠面临严重的热集中、机械热应力失配与整体良率多芯片乘积风险（Yield Compounding）。
>
> > [!axis] 生态治理规范：专有私有互连协议 vs 开放跨厂商[[Assemblage|装配]]标准
> > 围绕芯粒间互连协议应由芯片巨头主导私有架构还是推行开放通用标准展开的分歧。
> >
> > - **开放架构与国家计划倡导者** 强调必须建立统一的开放装配设计套件（ADK）与物理测试标准，以破除行业龙头专利壁垒，允许中小企业与大学原型公平接入先进封装生态。（pp. 17–18）
> > - **行业先发寡头企业** 倾向于维护私有专有接口以最大化垂直整合性能与构筑技术护城河，认为过度标准化会拖慢前沿定制化算力创新的迭代节奏。

---

## 实证数据

> [!ref-table]- 其他实证结果（无[[Effect Size|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024)]] | 美国半导体技术演进与先进封装国家战略需求（涵盖高性能计算、AI 边缘加速、射频与极端环境航天载荷） | 跨部门战略评估与微电子技术路线图综述 | 晶体管物理极限瓶颈、异构微互连密度、[[Assemblage\|装配]]设计套件（ADK）规范与 [[National Advanced Packaging Manufacturing Program\|NAPMP]] 投资目标 | ① 先进逻辑晶体管特征尺寸逼近 **亚 2 纳米原子物理极限**，单片光刻掩膜开发成本激增；② 异构集成与先进封装获《[[CHIPS and Science Act\|芯片法案]]》**30 亿美元** 专项资金支持；③ 确立微凸点间距、硅通孔（TSV）与混合键合等 **亚微米级微互连** 计量规程 | 跨部门国家战略政策文件与路线图规划（原文报告） | 确立异构集成作为突破单片物理微缩瓶颈、支撑国家先进封装与算力扩展的核心战略路径 |

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联维度与贡献 |
> |:---|:---|:---|
> | [[Paradigm]] | Concept | 异构集成代表了从单片晶体管物理微缩向多维多材料系统级集成的范式转型。 |
> | [[Assemblage]] | Concept | 模块化芯粒在先进基板与垂直三维空间中的微尺度物理与功能组合。 |
> | [[Process Design Kit]] | Concept | 与工艺设计套件相对应，装配设计套件（ADK）构成了异构集成设计的核心标准工具。 |
> | [[Innovation Ecosystem]] | Concept | 芯粒复用与先进封装中试共享平台为微电子初创企业提供了低门槛创新生态。 |
> | [[National Advanced Packaging Manufacturing Program]] | Fact (Program) | 美国依据《[[CHIPS and Science Act\|芯片法案]]》设立的推进先进封装与异构集成技术研发与中试的重大国家工程。 |
> | [[National Science and Technology Council]] | Fact (Organization) | 制定《微电子研究国家战略》并统筹全美异构集成科技布局的白宫战略协调机构。 |
> | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024)]] | Argument | 白宫[[National Strategy on Microelectronics Research\|国家微电子研究战略]]，确立三维异构集成与先进封装为四大核心战略科技目标之一。 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_NSTC_2024_MicroelectronicsResearch|NSTC (2024)]] — 提出将三维异构集成（3DHI）确立为突破单片晶体管物理微缩极限的核心战略路径，系统规划模块化芯粒（Chiplets）与开放[[Assemblage|装配]]设计套件（ADK）标准体系。

