---
title: Process Design Kit
aliases:
  - 工艺设计套件
  - PDK
  - 工艺设计包
summary: "晶圆代工厂向芯片设计团队与电子设计自动化（EDA）软件提供的底层模型、物理规则与标准单元库文件集合，构成了集成电路代码与逻辑设计转化为物理可制造硅片的法定工程界面。在微电子创新生态中，专有 PDK 附加的高昂授权费用与严苛保密协议构成了大学实验室与初创团队开展硬件创新的关键制度壁垒；推动成熟节点开源 PDK 许可与跨代工厂标准化接口，是现代产业政策降低芯片原型验证门槛的核心共性支撑举措。"
type: concept
domain: "university-industry-collaboration"
related_count: 10
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/semiconductor
  - theme/university-industry-collaboration
  - theme/open-source-hardware
  - theme/innovation-policy
related_concepts:
  - "[[Translational Research]]"
  - "[[Innovation Ecosystem]]"
  - "[[Modern Industrial Policy]]"
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts:
  - "[[Taiwan Semiconductor Manufacturing Corporation]]"
  - "[[MOSIS]]"
  - "[[National Semiconductor Technology Center]]"
  - "[[Engineering Research Centers]]"
  - "[[National Science and Technology Council]]"
  - "[[DARPA]]"
related_arguments:
  - "[[Argument_NIST_2023_NSTC]]"
confidence: high
status: active
created: 2026-10-10
updated: 2026-10-10
---

# Process Design Kit

---

## 定义

> [!def] 核心定义
> **工艺设计套件（Process Design Kit, PDK）**是晶圆代工厂（Foundry）针对特定半导体制造工艺节点，向集成电路设计团队与电子设计自动化（Electronic Design Automation, EDA）工具软件提供的底层数据文件、物理设计规则、器件物理模型与标准单元库的集合，是连接前端抽象电路设计与后端物理硅片制造的基石工程契约。[[Argument_NIST_2023_NSTC|(NIST, 2023, pp. 5, 11, 16)]]

> [!concept-lens] 概念透镜
> - **含义** PDK 规定了特定制造产线能够稳定加工的物理几何极限、材料电学特性、晶体管电气行为模型与互连寄生参数，使设计人员在未接触物理晶圆厂的情况下即可进行精确仿真与物理版图绘制。
> - **用途** 在产学研转化与微电子创新链中，PDK 是消除从实验室原理突破到代工厂量产（[[Translational Research|lab-to-fab]]）工艺不匹配、保障流片一次成功率的核心技术中介。
> - **边界** PDK 本身不包含具体的芯片功能电路或逻辑算法代码，也不等同于通用的 EDA 设计软件，而是特定半导体制造产线专属的工艺参数与模型集合。

> [!citation-card] 工艺设计套件在微电子[[Innovation Ecosystem|创新生态]]中的公共品属性
> 申请联邦激励资金的晶圆制造厂商可通过向公众和产业界扩大成熟节点工艺设计套件的开放访问权限（如通过开源许可证），以促进知识产权开发并提升不同晶圆代工厂之间的设计互操作性。[[Argument_NIST_2023_NSTC|(NIST, 2023, p. 11)]]
>
> *Applicants could increase public and industry access to mature-node process design kits, such as through open-source licenses, to foster IP development and improve foundry interoperability.*

> [!boundary]- 概念边界
> - **不等于 EDA 软件** EDA（如 Synopsys、Cadence、Siemens）是用于芯片设计与仿真的通用软件平台；PDK 是运行在 EDA 平台之上、由具体晶圆代工厂针对特定产线定制的工艺参数数据包。
> - **不等于知识产权核（IP Core）** IP 核是具有特定逻辑功能的可复用电路模块（如 ARM CPU 核心、PCIe 控制器）；PDK 是实现这些 IP 核物理布局与电气仿真所依赖的底层基础工艺规程。

---

## 概念辨析

> [!contrast-table] 芯片设计与制造核心要素辨析
> | 维度 | 工艺设计套件（PDK） | 电子设计自动化（EDA） | 多项目晶圆（MPW） |
> |---|---|---|---|
> | **功能定位** | 制造工艺与物理特性的数据契约 | 芯片逻辑综合、仿真与版图设计软件 | 物理晶圆拼版流片与低成本验证通道 |
> | **提供主体** | 晶圆代工厂（[[Taiwan Semiconductor Manufacturing Corporation\|TSMC]]、GlobalFoundries 等） | EDA 独立软件供应商与开源社区 | 晶圆代工厂与中试协调代理（[[MOSIS]]、[[National Semiconductor Technology Center\|NSTC]]） |
> | **生态壁垒** | 高度专有、保密协议（NDA）限制严格 | 昂贵的商业软件许可费 | 实体机台光罩与洁净室高昂运行成本 |
> | **政策解法** | 推动成熟节点开源 PDK 与统一数据格式 | 联邦谈判集中采购与云端设计网关共享 | 联邦资助聚合拼版需求与预留流片班次 |

---

## 核心构件与文件组成

> [!feature] PDK 核心文件体系与技术构件
> - **器件仿真模型（SPICE Models）** 包含晶体管、电阻、电容、二极管等基础元器件在不同温度、电压和工艺偏差（PVT Corner）下的精确非线性紧凑物理模型（如 BSIM-CMOS），用于前端电路仿真。
> - **物理设计规则（DRC / LVS / [[Engineering Research Centers|ERC]] Rules）** 规定导线最小宽度、层间最小间距、通孔包覆等几何规则（Design Rule Check, DRC），以及电路原理图与物理版图一致性比对规则（Layout Versus Schematic, LVS）。
> - **标准单元库与符号库（Standard Cell Libraries & Symbols）** 提供经过硅验证的基础逻辑门（与、或、非、触发器）的版图、时序文件（Liberty .lib）与原理图符号，供数字逻辑自动布局布线（APR）使用。
> - **寄生参数提取文件（PEX / RC Extraction Decks）** 定义金属互连层间介电常数、三维拓扑电容与寄生电阻计算模型，用于后仿真阶段准确评估信号延迟与串扰。

---

## 运作流程与流片验证机制

> [!proc] 基于 PDK 的芯片设计到硅片制造转化流程
> 1. **PDK 载入与设计环境配置** 设计团队将晶圆厂提供的 PDK 导入 EDA 环境，配置目标工艺节点的物理参数与标准单元库。
> 2. **电路原理图设计与前仿真** 依据 PDK 提供的 SPICE 物理模型进行电路仿真与功能验证，确保逻辑与时序在理论极限内达标。
> 3. **物理版图绘制与自动布局布线** 借助 PDK 内嵌的设计规则，完成晶体管与金属走线的物理布局。
> 4. **物理验证与寄生参数后仿真（DRC / LVS / PEX）** 调用 PDK 验证规则脚本，自动排查版图中的短路、断路与几何违规，并提取物理寄生参数执行高精度后仿真。
> 5. **生成光刻版图数据交付制造（Tape-out）** 生成符合晶圆代工厂标准的 GDSII / OASIS 版图数据，交付代工厂制作光罩并投入物理晶圆加工。

---

## 政策意义与生态演进

> [!pathways] [[Modern Industrial Policy|现代产业政策]]推动 PDK 开放与标准化的核心路径
> - **破除实验室到代工厂（[[Translational Research|lab-to-fab]]）的准入壁垒** 传统商业代工厂对先进制程 PDK 施加严苛的非公开商业审查与法律保密壁垒，将中小微初创公司与高校研究者阻隔在先进硬件创新之外。[[Argument_NIST_2023_NSTC|(NIST, 2023, pp. 5, 11)]]; [[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 23–24)]]
> - **建设国家级云端设计网关与标准参考流程** [[National Semiconductor Technology Center|NSTC]] 与 [[DARPA]] 通过搭建集中托管的设计网关，预集成多晶圆厂 PDK、装配设计套件（Assembly Design Kit, ADK）与端到端参考设计流程，使研究人员无需重复签署繁琐法务协议即可调用硅验证工具链。[[Argument_NIST_2023_NSTC|(NIST, 2023, pp. 16–17)]]; [[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 15, 23–24)]]
> - **推动开源 PDK/ADK 革命与跨代工厂互操作性** 鼓励代工厂开放成熟制程与先进封装模型，繁荣开源 EDA 与封装装配设计工具链，大幅提升芯片与芯粒设计在不同代工与封装产线之间的可移植性。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 17, 23–24)]]

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_NSTC_2024_MicroelectronicsResearch|NSTC (2024)]] — 提出构建集成 PDK/ADK 与多项目晶圆流片的国家级开放设计基础设施，打破设计工具与先进制造资源准入壁垒。
> - [[Argument_NIST_2023_NSTC|NIST (2023)]] — 系统阐明通过国家半导体技术中心云端设计网关集中托管商业 PDK 与开源模型，降低芯片前端设计与流片验证门槛。

