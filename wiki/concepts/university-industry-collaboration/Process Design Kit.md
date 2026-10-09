---
title: Process Design Kit
aliases:
  - 工艺设计套件
  - PDK
  - 工艺设计包
  - Assembly Design Kit
  - 装配设计套件
  - ADK
summary: "晶圆代工厂向芯片设计团队与电子设计自动化（EDA）工具提供的底层模型、物理规则与标准单元库集合，构成了电路设计转化为物理硅片的法定工程界面；随着先进封装发展进一步演进出装配设计套件（ADK）。在创新生态中，专有套件的高昂授权与保密协议构成了硬件创新的关键壁垒；依托国家设计网关集中托管并推动开源 PDK 与标准化接口，是打通从实验室到代工厂中试断层的核心举措。"
type: concept
domain: "university-industry-collaboration"
related_count: 22
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - theme/semiconductor
  - theme/university-industry-collaboration
  - theme/open-source-hardware
  - theme/innovation-policy
  - theme/heterogeneous-integration
  - theme/hardware-security
related_concepts:
  - "[[Heterogeneous Integration]]"
  - "[[Assemblage]]"
  - "[[Translational Research]]"
  - "[[Innovation Ecosystem]]"
  - "[[Pilot Scale Platform]]"
  - "[[Hardware Security]]"
  - "[[Modern Industrial Policy]]"
  - "[[Master Agreement]]"
  - "[[Co-Design]]"
  - "[[Market Failure]]"
related_theories: []
related_methods:
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Taiwan Semiconductor Manufacturing Corporation]]"
  - "[[MOSIS]]"
  - "[[National Semiconductor Technology Center]]"
  - "[[Engineering Research Centers]]"
  - "[[National Science and Technology Council]]"
  - "[[Natcast]]"
  - "[[National Advanced Packaging Manufacturing Program]]"
  - "[[DARPA]]"
related_arguments:
  - "[[Argument_NIST_2023_NSTC]]"
  - "[[Argument_NSTC_2024_MicroelectronicsResearch]]"
  - "[[Argument_Zhuo_2026_ICE]]"
confidence: high
status: active
created: 2026-10-10
updated: 2026-10-10
---

# Process Design Kit

---

## 定义

> [!def] 核心定义
> **工艺设计套件（Process Design Kit, PDK）**是晶圆代工厂（Foundry）针对特定半导体制造工艺节点，向集成电路设计团队与电子设计自动化（Electronic Design Automation, EDA）工具软件提供的底层模型、物理设计规则、器件紧凑物理模型与标准单元库的结构化数据集合，是连接前端抽象电路代码设计与后端物理硅片制造的基石工程契约。随着 2.5D/3D [[Heterogeneous Integration|异构集成]]与芯粒（Chiplet）技术发展，该体系进一步衍生出**[[Assemblage|装配]]设计套件（Assembly Design Kit, ADK）**，用于界定多芯片封装层级的中介层布线、微凸点键合与多物理场仿真规则。[[Argument_NIST_2023_NSTC|(NIST, 2023, pp. 5, 11, 16)]]; [[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 15, 23–24)]]

> [!concept-lens] 概念透镜
> - **含义** PDK 规定了特定晶圆产线能够稳定加工的物理几何极限、材料电学特性、晶体管电气行为模型与互连寄生参数，使设计人员在未接触物理机台的情况下即可进行高保真仿真与物理版图绘制；ADK 则进一步界定多芯粒物理堆叠与热力学装配边界。
> - **用途** 在产学研转化与微电子创新链中，PDK 与 ADK 是消除从实验室原理突破到代工厂量产（[[Translational Research|lab-to-fab]]）工艺失配、保障流片与封装一次成功率的核心技术中介与通用工程语言。
> - **边界** PDK 本身不包含具体的芯片功能电路代码或逻辑算法 IP，也不等同于通用的 EDA 软件平台，而是特定半导体制造产线专属的工艺参数与物理验证规则库。

> [!citation-card] 工艺设计套件在微电子[[Innovation Ecosystem|创新生态]]中的公共品属性
> 申请联邦激励资金的晶圆制造厂商可通过向公众和产业界扩大成熟节点工艺设计套件的开放访问权限（如通过开源许可证），以促进知识产权开发并提升不同晶圆代工厂之间的设计互操作性。此外，国家级云端设计网关将集中托管多晶圆厂 PDK、装配设计套件（ADK）与端到端参考设计流程，彻底打破初创企业与学术团队的准入壁垒。[[Argument_NIST_2023_NSTC|(NIST, 2023, p. 11)]]; [[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 23–24)]]
>
> *Applicants could increase public and industry access to mature-node process design kits, such as through open-source licenses, to foster IP development and improve foundry interoperability... The Design Gateway will provide streamlined access to commercial and specialized PDKs, assembly design kits (ADKs), and shared MPW runs.*

> [!boundary]- 概念边界与扩展范畴
> - **不等于 EDA 软件** EDA（如 Synopsys、Cadence、Siemens）是用于芯片设计、综合与仿真的通用软件平台工具；PDK/ADK 是运行在 EDA 平台之上、由具体晶圆代工厂或封装厂针对特定产线定制的工艺参数数据包。
> - **不等于知识产权核（IP Core）** IP 核是具有特定逻辑功能的可复用硬件电路模块（如 RISC-V 处理器核、PCIe 控制器）；PDK/ADK 是实现这些 IP 核物理布局、多物理场仿真与电气验证所依赖的底层工艺规程。
> - **PDK 与 ADK 的层级协同** PDK 聚焦于“单颗裸片（Die）内部”的微观半导体器件与互连制造；ADK 聚焦于“多芯片组装系统（Multi-Die System）”的中介层（Interposer）、硅通孔（TSV）、微凸点（Micro-bump）与三维立体封装堆叠。

---

## 概念辨析

> [!contrast-table] 芯片前端设计与后端制造封装核心要素辨析
> | 维度 | 工艺设计套件（PDK） | [[Assemblage\|装配]]设计套件（ADK） | 电子设计自动化（EDA） | 多项目晶圆（MPW） |
> |:---|:---|:---|:---|:---|
> | **功能定位** | 单芯片制造工艺与物理特性的数据契约 | 2.5D/3D 异构封装与芯粒装配规则包 | 芯片逻辑综合、仿真与版图设计软件工具 | 物理晶圆拼版流片与低成本验证通道 |
> | **技术关注点** | 晶体管模型、层间规则、寄生参数 | 芯粒间距、微凸点对准、热应力与电磁串扰 | 算法综合、静态时序分析、自动布局布线 | 掩模版光罩空间共享与分摊制造费用 |
> | **提供主体** | 晶圆代工厂（[[Taiwan Semiconductor Manufacturing Corporation\|台积电]]、格芯、英特尔等） | 封装测试厂（OSAT）与先进封装[[Pilot Scale Platform\|中试平台]] | EDA 独立软件供应商与开源开源社区 | 晶圆代工厂与中试中介（[[MOSIS]]、[[National Semiconductor Technology Center\|NSTC]]） |
> | **生态壁垒** | 高度专有、保密协议（NDA）限制严格 | 封装接口不统一、多物理场协同仿真复杂 | 商业许可证昂贵、多租户云端部署受限 | 实体机台光罩与洁净室高昂运行成本 |
> | **政策解法** | 推动成熟节点开源 PDK 与集中云端授权 | 建立统一标准 ADK 与 UCIe 互联规范 | 联邦集中采购授权与支持开源工具链 | 联邦资助聚合拼版需求与预留流片班次 |

---

## 核心构件与文件组成

> [!feature] PDK 与 ADK 核心文件体系与技术构件
> - **器件仿真紧凑模型（SPICE Models）** 包含晶体管、电阻、电容、二极管等基础元器件在不同温度、电压和工艺偏差（PVT Corner）下的精确非线性紧凑物理模型（如 BSIM-CMOS），用于前端电路逻辑与模拟信号高精度仿真。
> - **物理设计规则检查文件（DRC / LVS / [[Engineering Research Centers|ERC]] Rules）** 规定导线最小宽度、层间最小间距、通孔包覆等几何规则（Design Rule Check, DRC），电路原理图与物理版图一致性比对规则（Layout Versus Schematic, LVS），以及电气规则检查脚本（Electrical Rule Check, ERC）。
> - **标准单元库与原理图符号（Standard Cell Libraries & Symbols）** 提供经过硅验证的基础逻辑门（与、或、非、触发器、加法器）的物理版图、时序功耗描述文件（Liberty .lib）与原理图符号，供数字逻辑自动布局布线（APR）工具调用。
> - **寄生参数提取文件（PEX / RC Extraction Decks）** 定义金属互连层间介电常数、三维拓扑电容与寄生电阻计算模型，用于后仿真阶段准确评估高频信号延迟、红外压降（IR-drop）与时钟抖动。
> - **[[Assemblage|装配]]设计规则与多物理场模型（ADK Decks）** 涵盖 2.5D/3D [[Heterogeneous Integration|异构集成]]中的微凸点阵列间距、硅通孔（TSV）禁布区、重布线层（RDL）规则，以及热膨胀失配（CTE）热力学与电磁协同仿真模型。
> - **[[Hardware Security|硬件安全]]与信任根检测规则（Hardware Security Rules）** 现代安全增强型 PDK 内嵌硬件木马排查准则、侧信道功耗泄露评估模型与物理不可克隆函数（PUF）单元模型，保障全生命周期硬件安全。

---

## 运作流程与流片验证机制

> [!proc] 基于 PDK/ADK 的芯片设计到硅片制造转化流程
> 1. **设计环境配置与套件导入** 设计团队通过国家设计网关或代工厂安全通道导入目标工艺节点的 PDK 与封装 ADK，配置工艺参数库与标准单元时序模型。
> 2. **电路原理图设计与前仿真** 依据 PDK 提供的 SPICE 物理紧凑模型进行电路功能仿真与电气参数优化，确保逻辑与时序在极端工况下满足设计指标。
> 3. **物理版图绘制与自动布局布线（APR）** 借助 PDK 约束与 EDA 工具，完成晶体管几何图形生成、标准单元布局与多层金属走线拓扑布通。
> 4. **物理验证与寄生参数后仿真（DRC / LVS / PEX）** 运行 PDK 验证脚本，自动排查版图短路、断路与制造几何违规，提取三维互连寄生参数执行高保真带载后仿真。
> 5. **芯粒间[[Assemblage|装配]]与多物理场协同验证（ADK 流程）** 针对[[Heterogeneous Integration|异构集成]]系统，利用 ADK 进行芯粒间微凸点对准、中介层走线时序、散热流体与机械热应力仿真。
> 6. **生成光刻版图数据交付制造（Tape-out）** 生成符合晶圆代工厂标准的 GDSII / OASIS 版图文件，接入多项目晶圆（MPW）拼版，交付代工厂制作光罩并投入晶圆制造与封装测试。

---

## 政策意义与生态演进

> [!pathways] [[Modern Industrial Policy|现代产业政策]]推动 PDK/ADK 开放与标准化的核心路径
> - **破除实验室到代工厂（[[Translational Research|lab-to-fab]]）的制度壁垒** 传统商业代工厂对先进制程 PDK 施加严苛的非公开商业审查与法律保密协议（NDA），法务谈判动辄耗时数月甚至数年，将中小微初创公司与高校科研团队阻隔在先进硬件创新门槛之外。[[Argument_NIST_2023_NSTC|(NIST, 2023, pp. 5, 11)]]; [[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 23–24)]]
> - **建设国家级云端设计网关（Design Gateway）与统一 NDA 框架** 由[[National Semiconductor Technology Center|国家半导体技术中心]]（[[National Science and Technology Council|NSTC]]）依托非营利实体 [[Natcast]] 建立集中托管的设计网关，预集成多晶圆厂 PDK、[[Assemblage|装配]]套件 ADK 与端到端参考设计流程；研发团队签署单一[[Master Agreement|主协议]]即可调用全美主流代工厂与中试设施的工艺资源。[[Argument_NIST_2023_NSTC|(NIST, 2023, pp. 16–17)]]; [[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 15, 23–24)]]
> - **推动开源 PDK 革命与跨代工厂设计可移植性** 鼓励晶圆制造厂商开源成熟制程（如 130nm、90nm）PDK 与先进封装 ADK，繁荣开源 EDA 与开源硬件知识产权生态，大幅降低芯片与芯粒在不同代工产线之间的迁移与重构成本。[[Argument_NIST_2023_NSTC|(NIST, 2023, p. 11)]]; [[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 17, 23–24)]]
> - **全栈[[Hardware Security|硬件安全]]与内生信任根支撑** 在国家战略框架下，推动将密码学安全原语、硬件抗侧信道攻击指标与漏洞扫描规则直接集成至 PDK/ADK 标准规则库中，实现从底层物理版图阶段杜绝硬件木马与供应链篡改隐患。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 16, 24)]]

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Translational Research]] | Concept | PDK/ADK 是解决实验室原理突破向代工规模量产转化的核心工程接口。 |
> | [[Heterogeneous Integration]] | Concept | [[Assemblage\|装配]]设计套件（ADK）是实现 2.5D/3D 多芯粒系统级异构集成的规则基石。 |
> | [[Co-Design]] | Concept | PDK 提供贯穿材料、器件、电路到算法的全栈协同设计物理参数基础。 |
> | [[Hardware Security]] | Concept | 现代安全增强型 PDK 将硬件信任根与漏洞检测内嵌于物理规则库中。 |
> | [[Pilot Scale Platform]] | Concept | 中试平台通过统一部署 PDK/ADK 与 MPW 拼版通道，为学术界与初创企业提供低成本验证。 |
> | [[Modern Industrial Policy]] | Concept | 联邦政府资助国家设计网关与开源 PDK 是通过公共投入纠正微电子[[Market Failure\|市场失灵]]的关键工具。 |
> | [[National Semiconductor Technology Center]] | Fact (Organization) | 建立国家级设计赋能网关（DEG），集中托管商业与开源 PDK/ADK。 |
> | [[National Advanced Packaging Manufacturing Program]] | Fact (Program) | 领导制定全美统一的先进封装装配套件（ADK）标准与异构集成规范。 |
> | [[MOSIS]] | Fact (Organization) | 历史开创多项目晶圆拼版流片与大学 PDK 共享模式的先驱机构。 |
> | [[Natcast]] | Fact (Organization) | 运营国家设计网关并维护通用 PDK/ADK 访问协议的受托非营利实体。 |
> | [[Taiwan Semiconductor Manufacturing Corporation]] | Fact (Organization) | 全球先进制程 PDK 的主要制定者与工艺标准引领者。 |
> | [[DARPA]] | Fact (Organization) | 资助 POSH、IDEA 与 Toolbox 计划，推动开源 PDK 与自动化电路生成。 |
> | [[Argument_NIST_2023_NSTC\|NIST (2023)]] | Argument | 阐明国家半导体技术中心云端设计网关集中托管商业与开源 PDK 的制度构想。 |
> | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024)]] | Argument | 确立国家微电子顶层战略，将开放 PDK/ADK 与国家设计网关列为打通转化断层的共性支柱。 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_NSTC_2024_MicroelectronicsResearch|NSTC (2024)]] — 提出构建集成 PDK/ADK 与多项目晶圆流片的国家级开放设计基础设施，打破设计工具与先进制造资源准入壁垒，支撑全栈[[Hardware Security|硬件安全]]与[[Co-Design|协同设计]]。
> - [[Argument_NIST_2023_NSTC|NIST (2023)]] — 系统阐明通过[[National Semiconductor Technology Center|国家半导体技术中心]]云端设计网关集中托管商业 PDK 与开源模型，降低芯片前端设计、封装[[Assemblage|装配]]与流片验证门槛。
> - [[Argument_Zhuo_2026_ICE|卓泽林 (2026)]] — 分析美国高校与科研机构依托开源指令集、开放 PDK 与共享流片平台参与国家半导体创新网络建设的实践模式。


