---
title: Von Neumann Architecture
aliases:
  - 冯·诺依曼体系结构
  - 冯·诺依曼架构
  - 冯诺依曼架构
  - 存储程序计算机体系结构
  - 存储程序计算机
  - 存储程序架构
  - Stored-program architecture
  - Von Neumann computer architecture
summary: "约翰·冯·诺依曼于1945年提出的经典通用数字计算机体系结构范式。以存储程序控制与运算器、控制器、存储器及输入输出五大部件为核心，实现软硬件解耦。后摩尔时代正向类脑神经形态与存内计算等非冯架构演进。"
type: concept
domain: "science-policy"
related_count: 23
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - concept/science-policy
  - theme/computer-hardware
  - theme/technology-innovation
  - theme/information-technology
  - region/us
related_concepts:
  - "[[Variable]]"
  - "[[Paradigm]]"
  - "[[General Purpose Technology]]"
  - "[[Corporate University]]"
  - "[[Co-invention]]"
  - "[[Sage]]"
  - "[[Co-Design]]"
  - "[[Heterogeneous Integration]]"
  - "[[Hardware Security]]"
  - "[[Curiosity-Driven Research]]"
related_theories:
  - "[[Path Dependence]]"
related_methods:
  - "[[Coding in Qualitative Research]]"
  - "[[Perpetual Inventory Method]]"
  - "[[Effect Size]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons:
  - "[[David C. Mowery]]"
related_facts:
  - "[[Institute for Advanced Study]]"
  - "[[Office of Naval Research]]"
  - "[[National Science and Technology Council]]"
  - "[[National Strategy on Microelectronics Research]]"
  - "[[Semi-Automatic Ground Environment]]"
related_arguments:
  - "[[Argument_Mowery_2011_NBER]]"
  - "[[Argument_NSTC_2024_MicroelectronicsResearch]]"
confidence: high
status: active
created: 2026-10-03
updated: 2026-10-10
---

# Von Neumann Architecture

---

## 定义

> [!def] 核心定义
> 冯·诺依曼架构（Von Neumann Architecture），又称存储程序计算机体系结构（Stored-Program Computer Architecture），是数学家约翰·冯·诺依曼（John von Neumann）于 1945 年在《离散[[Variable|变量]]自动电子计算机报告书的第一份草案》（*First Draft of a Report on the EDVAC*）中系统阐述的通用电子数字计算机体系结构[[Paradigm|范式]]。其核心原则为“存储程序与程序控制”——将预先编制的计算程序指令与运算数据同等以二进制代码形式存放在统一的随机存取内部存储器中，由中央处理器顺序提取指令并自动译码执行；该架构在物理与逻辑上由运算器、控制器、存储器、输入设备和输出设备五大基本部件构成。[[Argument_Mowery_2011_NBER|(Mowery, 2011, pp. 171–174)]]

> [!concept-lens] 概念透镜
> - **含义** 指向一种将物理硬件执行逻辑与逻辑程序指令彻底解耦的通用计算体系结构设计。
> - **用途** 帮助科技政策学者与技术史学家理解，二战后早期基础计算知识的非专有公开扩散如何打破了军事保密壁垒，将计算机从专用的“硬线连线计算机器”转变为支撑全社会千行百业的[[General Purpose Technology|通用目的技术]]（GPT）。
> - **边界** 传统冯·诺依曼架构强调指令与数据共享同一总线与内存空间的串行处理；在当代大规模并行神经网络计算与超高吞吐场景下，易面临总线带宽与内存延迟瓶颈。

> [!citation-card] Mowery 论冯·诺依曼架构与早期战后计算资助的非专有扩散
> 战后早期美国联邦政府对计算机开发的资助坚持了非专有和学术公开的根本原则。[[Institute for Advanced Study|普林斯顿高等研究院]]的冯·诺依曼计算机项目不仅确立了存储程序通用计算的技术基石，更通过完全公开出版其设计报告与工程图纸，直接催生了全美大学和商业企业中数十种计算机的研制，避免了单一技术垄断或国家军事保密对新兴产业的扼杀。[[Argument_Mowery_2011_NBER|(Mowery, 2011, pp. 173–174)]]
>
> *Postwar federal funding of early computer development emphasized open publication and nonproprietary dissemination... The von Neumann architecture developed at the Institute for Advanced Study served as the blueprint for numerous university and commercial computers across the United States.*

> [!boundary]- 概念边界
> - 不等于 ENIAC 早期硬连线架构 — 1945 年交付的 ENIAC 在改变计算任务时必须由操作员耗费数小时乃至数天重新插拔物理跳线与开关旋钮，缺乏将程序存入内存并自动调用的能力。
> - 不等于哈佛架构（Harvard Architecture） — 哈佛架构在物理上为指令存储器与数据存储器设置了完全分离的独立寻址空间与独立传输总线，二者在软硬件灵活性与微控制器特种设计上存在结构性差异。

---

## 概念辨析

> [!contrast-table] 经典计算机硬件体系结构[[Paradigm|范式]]对比
> | 比较维度 | 冯·诺依曼架构（Von Neumann Architecture） | 哈佛架构（Harvard Architecture） | 专用硬线连线架构（Hardwired Architecture, 如 ENIAC 初版） |
> |---|---|---|---|
> | **程序与数据存储方式** | 指令与数据共享同一物理存储器空间 | 指令和数据物理完全分离，分属不同存储器 | 无内部程序存储器，程序体现为物理跳线排布 |
> | **传输总线结构** | 指令与数据共用同一套数据与地址总线 | 拥有独立的程序总线与数据总线，可同时读写 | 无通用总线，依靠物理电缆与步进开关传输脉冲 |
> | **硬件设计与通用性** | 控制器与总线结构简洁，具备极高通用性与灵活性 | 总线与硬件结构较为复杂，主要用于特种嵌入式/DSP | 无通用可重构性，切换算法需人工重新连线排线 |
> | **核心局限与瓶颈** | 存在总线争用与数据吞吐的“冯·诺依曼瓶颈” | 内存利用效率受限于预先固化的指令/数据比例 | 编程极其繁琐耗时，无法实现在线动态跳转与自修改 |

---

## 核心要素

> [!feature] 冯·诺依曼架构的五大硬件基石与运行机制
> - **算术逻辑单元（Arithmetic Logic Unit, ALU）** 负责执行算术四则运算与布尔逻辑运算的核心部件。
> - **控制单元（Control Unit, [[Corporate University|CU]]）** 负责从存储器中顺序读取指令、解释指令含义并向全局协调发送控制时钟信号的指挥中枢。
> - **内部存储器（Memory）** 按统一编址的存储单元序列，同等存放程序指令代码与运算原始/中间数据。
> - **输入设备（Input Devices）** 将外部信息（纸带、穿孔卡片、键盘或数字信号）[[Coding in Qualitative Research|编码]]为计算机内部二进制电平的接口。
> - **输出设备（Output Devices）** 将计算机计算结果转换为人类可读形式（打印机、显示器）或机器控制信号的终端。
> - **存储程序与顺序控制流（Stored-Program Control）** 程序指令按内存地址自动顺序递增执行，同时支持基于条件判断的无条件或条件跳转控制。[[Argument_Mowery_2011_NBER|(Mowery, 2011, pp. 171–174)]]

> [!logic-map]- 冯·诺依曼计算机五大部件协同数据与控制流
> ```mermaid
> flowchart LR
>     In["输入设备<br>（Input Devices）"] --> Mem["内部存储器<br>（Memory: 指令与数据同存）"]
>     Mem --> Out["输出设备<br>（Output Devices）"]
>     
>     subgraph CPU["中央处理器（Central Processing Unit, CPU）"]
>         direction LR
>         CU["控制单元（CU）<br>指令译码与时钟调度"] <--> ALU["算术逻辑单元（ALU）<br>算术与逻辑运算"]
>     end
>     
>     Mem <-->|数据总线 / 算术操作数| ALU
>     Mem <-->|指令总线 / 控制信号| CU
> ```

---

## 围绕概念形成的命题

---

### 命题一　非专有原则与技术蓝图公开出版避免了计算产业技术锁定并催生了全球工业群

> [!concept-lens] 知识产权政策与技术扩散动力学
> 探讨早期国防资助为何坚持将前沿架构公开发行，以及这一举措如何塑造战后产业格局。

> [!claim] [[David C. Mowery|Mowery, D. C.]]
> **学术公开原则打破军事垄断并奠定通用计算知识公地** 莫厄里系统论证指出，二战后由陆军、[[Office of Naval Research|海军研究办公室]]（Office of Naval Research, ONR）与原子能委员会（Atomic Energy Commission, AEC）资助的[[Institute for Advanced Study|普林斯顿高等研究院]]（Institute for Advanced Study, IAS）计算机项目，从一开始就拒绝将冯·诺依曼架构据为军方独占的机密技术。冯·诺依曼及其团队编写的理论报告与工程设计蓝图向全美乃至全球学术界与产业界无偿分发。这种极其罕见的非专有政策使得伊利诺伊大学（ILLIAC）、洛斯阿拉莫斯国家实验室（MANIAC）、兰德公司（JOHNNIAC）、阿贡国家实验室（AVIDAC）乃至商业巨头 IBM（基于 IAS 架构开发其首款商用科学计算机 IBM 701）能够迅速消化并并行研制出各自的存储程序计算机。这一政策有效避免了新兴计算机技术被单一军种或单一垄断巨头锁定的风险，为美国培育了多元化、去中心化的计算机硬件产业生态。[[Argument_Mowery_2011_NBER|(Mowery, 2011, pp. 171–174)]]

---

### 命题二　软硬件彻底解耦为通用目的技术收敛与下游用户端的大规模共同发明创造了物理载体

> [!concept-lens] 模块化分工与[[General Purpose Technology|通用目的技术]]收敛
> 探讨存储程序架构如何实现算法与硬件的分离，从而支撑全社会范围的流程再造。

> [!claim] Mowery, D. C.
> **统一硬件标准赋能软件独立性与用户端[[Co-invention|共同发明]]** 莫厄里指出，在冯·诺依曼架构确立之前，每一套计算逻辑都意味着定制的物理硬件搭建；而存储程序原则将“通用的硬件物理平台”与“动态可变的应用软件程序”彻底解耦。这一模块化分离使得计算机硬件能够收敛于标准化的冯·诺依曼通用逻辑，进而为下游企业（如美洲航空公司在 [[Sage]] 基础上的 SABRE 订票系统开发）提供了无需重新设计硬件即可开展海量业务流程创新的统一载体。标准化硬件平台激发了广泛的用户端[[Co-invention|共同发明]]，使信息技术最终完成了向全社会[[General Purpose Technology|通用目的技术]]的跃迁。[[Argument_Mowery_2011_NBER|(Mowery, 2011, pp. 178–180, 185)]]

---

### 命题三　超越冯·诺依曼架构是非冯计算范式变革与后摩尔微电子战略的核心突破口

> [!concept-lens] 后摩尔架构重塑与稳健处理[[Paradigm|范式]]
> 探讨面对“内存墙”与能耗极限，国家科技战略如何引导学术界与工业界向非冯·诺依曼计算架构跃迁。

> [!claim] [[Argument_NSTC_2024_MicroelectronicsResearch|NSTC (2024)]]
> **新型稳健非冯架构与全栈软硬件[[Co-Design|协同设计]]** [[National Science and Technology Council|国家科学技术委员会]]（National Science and Technology Council, NSTC）在《[[National Strategy on Microelectronics Research|国家微电子研究战略]]》中明确指出，随着传统晶体管微缩逼近物理极限，基于传统冯·诺依曼架构的处理器面临严重的数据传输带宽与能耗瓶颈（即“内存墙”），多达 80% 的系统能耗消耗在中央处理器（CPU）/图形处理器（GPU）与离散存储器之间的高频数据搬运上。战略将“新型稳健处理架构”（Processing Architectures, 1.3）列为第一重大突破目标，全面部署向“超越冯·诺依曼”（Beyond von Neumann）范式演进：通过支持类脑神经形态计算（Neuromorphic Computing）、存内计算（In-Memory Computing, IMC）、模拟与光子计算（Photonic Computing）以及专用硬件加速器，在物理层将计算单元直接嵌入存储阵列内部；同时要求将新型微架构与软硬件[[Co-Design|协同设计]]、[[Heterogeneous Integration|异构集成]]（[[Heterogeneous Integration]]）及[[Hardware Security|硬件安全]]从底层全面绑定，重构自下而上的编译器、运行时环境与算法堆栈。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 16–17)]]

---

### 命题总览

> [!contrast-table] 冯·诺依曼架构核心命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 / 机构 |
> |---|---|---|---|
> | **知识公地与技术扩散** | 联邦资助的非专有技术图纸公开打破军事垄断，催生 IAS 派生计算机家族 | 战后计算科学建制化与早期国防资助 | [[Argument_Mowery_2011_NBER\|Mowery (2011, pp. 171–174)]] |
> | **软硬件解耦与通用化** | 存储程序架构确立通用计算基座，支撑下游海量软件共同发明 | 通用目的技术（GPT）演化与产业组织分工 | [[Argument_Mowery_2011_NBER\|Mowery (2011, pp. 178–180, 185)]]; Bresnahan & Trajtenberg (1995) |
> | **超越传统架构与非冯范式** | 破解内存墙与能耗瓶颈，部署存内计算、类脑神经形态与软硬件协同设计 | 后摩尔时代微电子战略与先导计算研究 | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024, pp. 16–17)]] |

---

## 概念演变

> [!dev-timeline] 概念演变历程
> - **1945 — 《EDVAC 报告草案》确立理论模型** 冯·诺依曼在宾夕法尼亚大学摩尔电机工程学院总结 ENIAC 经验，系统提出存储程序与二进制五大部件架构。[[Argument_Mowery_2011_NBER|(Mowery, 2011, p. 171)]]
> - **1946–1951 — 普林斯顿 [[Institute for Advanced Study|IAS]] 计算机工程与全球派生** 陆军与 [[Office of Naval Research|ONR]] 资助普林斯顿高等研究院研制实体样机，公开分发蓝图，催生全美高校与工业界（IBM 701、MANIAC、ILLIAC 等）的克隆制造浪潮。[[Argument_Mowery_2011_NBER|(Mowery, 2011, pp. 172–174)]]
> - **1960s–1980s — 商业化主导与指令集架构繁荣** 成为大型主机（IBM System/360）、小型机（DEC PDP）及个人微机（x86、ARM）的支配性事实标准。
> - **1990s–2010s — 冯·诺依曼瓶颈审思与存算一体萌芽** 随处理器频率增长远超内存带宽，内存墙问题日益尖锐；学术界提出存算一体（Processing-in-Memory, [[Perpetual Inventory Method|PIM]]）与专用加速架构。
> - **2024 年至今 — “超越冯·诺依曼”的国家战略化推进** 美国[[National Science and Technology Council|国家科学技术委员会]]（[[National Science and Technology Council|NSTC]]）在《[[National Strategy on Microelectronics Research|国家微电子研究战略]]》中将类脑神经形态、存内计算、光子计算等非冯架构确立为国家战略级攻关重点，依托软硬件[[Co-Design|协同设计]]实现全栈重构。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 16–17)]]

---

## 争议与批评

> [!debates] 学术与技术争议
>
> > [!axis] 发明权归属争议：冯·诺依曼 vs. 埃克特与莫奇利
> > 探讨《EDVAC 报告》以冯·诺依曼单一署名公开发表所引发的优先权历史纷争。
> >
> > - **埃克特与莫奇利阵营（反方）** ENIAC 的主要发明人 J. 普雷斯珀·埃克特（J. Presper Eckert）与约翰·莫奇利（John Mauchly）指出，存储程序的核心概念在摩尔学院团队内部讨论时已萌芽；报告以冯·诺依曼单人署名公开出版，不仅掩盖了工程团队的原创贡献，更导致法院以“已进入公有领域”为由判决该架构专利无效。
> > - **科技政策与演化派辩护（正方）** Mowery 等学者指出，正是由于该报告未被申请为排他性专利、而是作为无偿公共品公开发行，才避免了战后微电子硬件技术被初创公司或单一巨头垄断封锁，构成了美国计算工业高速扩散的制度前提。[[Argument_Mowery_2011_NBER|(Mowery, 2011, pp. 173–174)]]
>
> > [!axis] 冯·诺依曼瓶颈（Von Neumann Bottleneck）与内存墙
> > 探讨传统架构在现代极高算力吞吐场景下的物理与能耗极限。
> >
> > - **技术架构局限** 计算机科学家约翰·巴克斯（John Backus, 1977）指出，CPU 与存储器之间共享的狭窄通信总线构成了严重的吞吐量瓶颈；在深度学习与海量数据搬运中，高达 80% 的能耗与延迟消耗在总线数据传输而非实际计算上。
> > - **架构超越方案（NSTC 2024）** 推动计算与存储在物理空间与材料层面的深度融合，通过类脑脉冲阵列、阻变存储器（RRAM）及三维[[Heterogeneous Integration|异构集成]]，使运算直接在数据所在地发生。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 16–17)]]

> [!warning] 适用局限
> 冯·诺依曼架构适用于以确定性逻辑判断、精确控制流和串行离散算法为特征的通用计算任务；对于大规模低精度并行矩阵运算、生物脉冲神经网络模拟及非确定性量子概率解算，传统冯·诺依曼架构面临显著的能效比与吞吐量约束。

---

## 实证数据

> [!ref-table]- 1945–1955年战后联邦资助早期计算机开发工程统计
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 早期计算机项目 | 单台成本估算 | 主要联邦资助机构 | 架构技术特征（无[[Effect Size\|效应量]]） | 解释边界 |
> |---|---|---|---|---|---|
> | [[Argument_Mowery_2011_NBER\|Mowery (2011, p. 172)]] | Princeton IAS Computer (1951) | \$650,000 | 陆军 / 海军 / RCA / 原子能委员会 | 奠定存储程序与并行二进制冯·诺依曼架构基石，图纸完全公开出版。 | 反映战后首个十年联邦多渠道去中心化资助特征（Table 5.2）。 |
> | 同上 (p. 173) | MIT Whirlwind (1951) | \$4,000,000–\$5,000,000 | 海军（[[Office of Naval Research\|ONR]]） / 空军 | 率先应用磁芯内存与实时在线处理架构，后发展为 [[Semi-Automatic Ground Environment\|SAGE]] 防空系统。 | 聚焦于实时防空工程应用场景。 |
> | 同上 (p. 173) | IBM NORC (1955) | \$2,500,000 | 海军（Navy） | 海军军械局资助的超高性能冯·诺依曼科学计算主机。 | 军工高性能计算特种采购。 |

---

## 条目关联

> [!entry-map]
> | 条目 | 类型 | 关联与贡献 |
> |:-----|:-----|:-----------|
> | [[General Purpose Technology]] | Concept | 冯·诺依曼架构通过解耦软硬件奠定了信息技术作为通用目的技术的硬件标准。 |
> | [[Co-Design]] | Concept | 超越冯·诺依曼架构的关键方法论，要求算法、编译器与底层非冯微架构同步协同开发。 |
> | [[Heterogeneous Integration]] | Concept | 异构集成先进封装技术为非冯存算一体芯片提供三维高密度互连物理支撑。 |
> | [[Curiosity-Driven Research]] | Concept | 类脑神经形态材料与自旋电子学等非冯物理机理来源于前沿好奇心探索。 |
> | [[National Science and Technology Council]] | Fact (Organization) | 白宫国家科技委员会，主导制定《[[National Strategy on Microelectronics Research\|国家微电子研究战略]]》并部署非冯架构突破。 |
> | [[Argument_Mowery_2011_NBER\|Mowery, 2011]] | Argument | 详尽考据二战后美国军政机构公开扩散 [[Institute for Advanced Study\|IAS]] 蓝图与奠定通用计算工业生态的经典论著。 |
> | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC, 2024]] | Argument | 战略报告，确立超越冯·诺依曼架构、类脑计算与存算一体为后摩尔时代第一突破方向。 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Mowery_2011_NBER|Mowery (2011)]] — 详尽考据二战后美国陆海空三军与民政科研机构资助普林斯顿 [[Institute for Advanced Study|IAS]] 计算机工程的历史，论证冯·诺依曼架构的非专有公开出版如何避免了[[Path Dependence|技术锁定]]并奠定现代计算机产业生态。
> - [[Argument_NSTC_2024_MicroelectronicsResearch|NSTC (2024)]] — 白宫国家科技委员会[[National Strategy on Microelectronics Research|国家微电子研究战略]]，系统规划新型稳健处理架构（1.3），推动存内计算、类脑神经形态与光子计算等“超越冯·诺依曼”[[Paradigm|范式]]与软硬件[[Co-Design|协同设计]]变革。

