---
title: Hardware Security
aliases:
  - 硬件安全
  - 硬件完整性与安全
  - Hardware Integrity and Security
  - 硬件信任根
  - Hardware Root of Trust
summary: "贯穿微电子系统从底层材料、电路设计、晶圆制造、异构封装到现场部署全生命周期的安全防护学科与工程实践，旨在防范硬件木马、物理侧信道攻击、逆向工程、供应链伪造与篡改，并在架构根基处建立可度量验证的零信任硬件信任根。"
type: concept
domain: "science-policy"
related_count: 16
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - theme/semiconductor
  - theme/science-policy
  - theme/national-security
  - theme/cybersecurity
related_concepts:
  - "[[Trustworthiness]]"
  - "[[Co-Design]]"
  - "[[Reliability]]"
  - "[[Paradigm]]"
  - "[[Screening Off]]"
  - "[[Hypothesis]]"
  - "[[Document]]"
  - "[[Competitiveness]]"
  - "[[Variable]]"
related_theories: []
related_methods:
  - "[[Power Analysis]]"
  - "[[Effect Size]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[National Science and Technology Council]]"
  - "[[DARPA]]"
  - "[[National Strategy on Microelectronics Research]]"
related_arguments:
  - "[[Argument_NSTC_2024_MicroelectronicsResearch]]"
confidence: high
status: active
created: 2026-10-10
updated: 2026-10-10
---

# Hardware Security

---

## 定义

> [!def] 核心定义
> **硬件安全（Hardware Security / Hardware Integrity and Security）** 指涵盖微电子器件与集成电路全生命周期（涵盖材料选型、逻辑综合、物理版图、晶圆流片、先进封装、测试筛选直至终端部署与废弃）的系统性安全防御技术、架构规范与工程方法。其核心目标在于防范外部敌对势力或非可信供应链引入的恶意硬件木马、物理侧信道攻击（Side-Channel Attacks）、故障注入攻击、逆向工程与假冒伪劣芯片，并在芯片内部构建硬件信任根（Hardware Root of Trust）、零信任物理认证机制以及抗物理探测的加密防线，确保国家关键基础设施与国防微电子系统的[[Trustworthiness|可信赖性]]（Trust and Assurance）。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 10, 13, 18–19)]]

> [!concept-lens] 概念透镜
> - **含义** 硬件安全将计算信任锚点确立在最底层的物理微电子结构中，认定软件安全防御的有效性最终取决于底层承载硬件的物理完整性与不可篡改性。
> - **用途** 为防范全球化代工供应链中的技术截获、非授权后门植入以及关键基础设施芯片失效提供制度规范、自动化检测工具与物理防御架构。
> - **边界** 硬件安全不等于单纯的密码学软件算法实现，它重点解决物理层面的微观电磁泄漏、热辐射、探针物理接触、掺杂层篡改与异构芯粒互连认证等实体物理威胁。

> [!citation-card] 全生命周期硬件安全与可信验证
> 在日益复杂的分布式全球供应链环境下，硬件完整性与安全性已成为国家安全与经济韧性的核心支柱。必须将安全考量作为首要内生要素贯穿于设计到封装的全栈协同流程中，开发覆盖设计工具、制造流程与现场运行的自动化硬件验证与形式化检验技术，以抵御先进物理探测与供应链攻击。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 18–19)]]
>
> *Prioritize hardware integrity and security as an element in [[Co-Design]] strategies across the stack... Hardware security and integrity are vital for national and economic security, ensuring that microelectronic devices operate reliably and as intended, without vulnerabilities that could be exploited by adversaries throughout the lifecycle of design, fabrication, assembly, test, and deployment.*

> [!boundary]- 概念边界
> - 不等于 软件网络安全（Software / Cyber Security）— 软件网络安全主要通过防火墙、操作系统权限控制与杀毒软件防范逻辑层漏洞；若底层物理硬件本身存在后门或硬件木马，所有上层软件安全机制将被彻底绕过与瓦解。
> - 不等于 基础硬件[[Reliability|可靠性]]（Hardware Reliability）— 硬件可靠性关注芯片在特定工作环境与时间跨度下的物理老化、介质击穿或随机物理故障（如宇宙射线单粒子翻转）；硬件安全则专门应对有组织、有目的的主动敌对攻击、恶意植入与逆向窃密。

---

## 概念辨析

> [!contrast-table] 安全防护[[Paradigm|范式]]对比
> | 维度 | 硬件安全（Hardware Security） | 软件网络安全（Software Security） | 传统器件[[Reliability\|可靠性]]（Device Reliability） |
> |---|---|---|---|
> | **防护层级** | 物理硅片、纳米晶体管、封装基板与微架构 | 操作系统、中间件、网络协议与应用程序 | 材料物理性质、金属迁移与栅极氧化层寿命 |
> | **威胁来源** | 恶意代工厂、硬件木马、物理探针、侧信道窃听 | 恶意代码、黑客网络渗透、逻辑越权漏洞 | 自然物理退化、高温高湿环境、热应力疲劳 |
> | **修复成本** | 芯片流片后几乎无法物理修补，需前置根植设计 | 可通过在线发布软件补丁与固件升级低成本修复 | 依赖冗余备份电路或器件降频妥协运行 |
> | **核心防御机制** | 物理不可克隆函数（PUF）、防篡改网格、差分功耗混淆 | 访问控制列表、数据加密传输、内存安全沙箱 | 降额设计、纠错码（ECC）、抗辐照物理加固 |

---

## 核心要素

> [!feature] 硬件安全的关键技术支柱
> - **硬件信任根（Hardware Root of Trust, RoT）** 在芯片内部嵌入不可篡改的加密密钥存储单元、真随机数发生器与物理不可克隆函数（Physical Unclonable Function, PUF），为上层系统提供唯一的物理身份凭证。（p. 18）
> - **零信任硬件架构（Zero-Trust Hardware Architecture）** 假定制造、封装与分销供应链环节均存在被渗透风险，在片上网络与芯粒接口间强制推行互操作鉴权与动态加密通信。（p. 18）
> - **抗侧信道与防物理探测技术（Side-Channel & Anti-Tamper Defense）** 采用差分功耗平衡电路、片上噪声注入、主动[[Screening Off|屏蔽]]网格与光/热传感器，阻止外部攻击者通过物理探针或功耗电磁辐射分析破解密钥。（p. 19）
> - **自动化安全形式化验证工具（Automated Security Verification Tools）** 在电子设计自动化（EDA）工具链中嵌入硬件木马扫描器与脆弱性形式化验证算法，在流片前自动检出潜在安全漏洞。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 15, 18–19)]]

> [!logic-map]- 硬件安全全生命周期防御框架
> ```mermaid
> flowchart TD
>     A["安全协同设计\n(EDA安全验证 / 硬件信任根)"] --> B["安全晶圆制造\n(防掺杂篡改 / 分割制造)"]
>     B --> C["安全封装与测试\n(PUF指纹注册 / 芯粒互信鉴权)"]
>     C --> D["安全分销与供应链\n(防伪溯源 / 防翻新篡改)"]
>     D --> E["现场安全运行\n(实时侧信道防御 / 自毁与锁定)"]
> ```

---

## 围绕概念形成的命题

---

### 命题一　硬件安全是构建主权可信计算底座与国家安全系统的基石

> [!concept-lens] 信任根基与国家安全保障
> 围绕现代关键基础设施对微电子器件的深度依赖，探讨物理层安全对国防、能源与通信系统的决定性作用。

> [!claim] [[National Science and Technology Council|NSTC]]
> **硬件信任作为不可替代的安全锚点** 现代信息系统的信任链条自底向上层层建立，任何上层软件加密与协议防御都建立在底层硬件真实可靠的[[Hypothesis|假设]]之上。如果微电子硬件本身被植入恶意逻辑或存在物理漏洞，敌对势力便可在毫无软件日志痕迹的情况下窃取核心机密或瘫痪整个系统。因此，必须将硬件安全确立为最高优先级的国家战略技术基石。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 3, 10, 18–19)]]

---

### 命题二　全生命周期安全协同设计是破解非可信全球供应链风险的必然选择

> [!concept-lens] 供应链全球化与非可信制造环境
> 围绕半导体代工与封装环节高度离岸化的现实，探讨如何在不可信制造环境下保证终端芯片的绝对安全。

> [!claim] NSTC
> **设计端内生免疫化解制造端外部风险** 面对全球化代工与复杂外包分工带来的潜在供应链安全风险，单纯依靠事后抽样破坏性检测无法实现全面防御。必须依托全栈[[Co-Design|协同设计]]（Co-Design）思想，在前端设计中嵌入轻量级自鉴权模块、混淆逻辑与零信任验证协议，使芯片即使在不受信任的海外代工厂生产，也能在最终封装与激活阶段抵御篡改与木马激活。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 13, 18–19)]]

---

### 命题总览

> [!contrast-table] 硬件安全核心命题概览
> | 命题方向 | 核心论断 | 技术与政策意涵 | 代表[[Document\|文献]] |
> |---|---|---|---|
> | **国家可信计算根基** | 硬件完整性是整个计算栈信任链条的物理支点 | 驱动国防与关键基础设施专用可信微电子研发计划 | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024, pp. 3, 10)]] |
> | **供应链安全防御** | 前置全栈协同安全设计能够免疫非可信代工环节风险 | 指导开发新一代安全EDA工具与零信任硬件标准 | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024, pp. 13, 18–19)]] |

---

## 概念演变

> [!dev-timeline] 概念演变
> - **1980s–1990s — 独立加密协处理器与物理防拆封装** 早期硬件安全主要依赖物理隔离的安全芯片（如智能卡与加密协处理器），通过环氧树脂封装与防拆网格传感器防止攻击者磨削芯片直连总线。
> - **2000s — 侧信道分析与微观物理泄露防御** 科赫尔（Paul Kocher）等学者提出差分功耗分析（Differential [[Power Analysis]], DPA）与电磁辐射探测，硬件安全研究转向防范利用芯片计算过程中的物理副产物反推密钥。
> - **2010s — 物理不可克隆函数（PUF）与硬件信任根（RoT）** 利用硅晶圆制造中不可控的纳米级物理工艺偏差，生成芯片唯一且不可复制的硬件“数字指纹”（PUF），奠定了现代芯片物理防伪与密钥生成的基石。
> - **2020s — 零信任硬件架构与自动化安全形式化验证** 针对全球代工供应链中的硬件木马与非授权篡改风险，[[DARPA|国防高级研究计划局]]（DARPA）与电子设计自动化（EDA）厂商合作开发前置安全扫描工具，在流片前自动检出硬件脆弱性。
> - **2024 — 国家战略确立硬件完整性与安全性为内生[[Co-Design|协同设计]]支柱** [[National Science and Technology Council|白宫国家科学技术委员会]]（NSTC）在《微电子研究国家战略》中将硬件安全与保证（Trust and Assurance）确立为全栈协同设计的核心内生要素，依托跨部门机制保障国防与关键基础设施微电子系统的绝对可信。[[Argument_NSTC_2024_MicroelectronicsResearch|(NSTC, 2024, pp. 10, 18–19)]]

---

## 争议与批评

> [!debates] 硬件安全学术争议与工程张力
>
> > [!axis] 安全防护开销：内生安全防御 vs 商业算力与面积能效损耗
> > 争论芯片架构设计应不计代价最大化硬件防护，还是在可接受的安全等级下优先保障算力与成本[[Competitiveness|竞争力]]。
> >
> > - **[[Argument_NSTC_2024_MicroelectronicsResearch|NSTC (2024)]]** 强调国家安全关键领域的微电子系统必须推行零信任硬件信任根与全流程形式化验证，安全开销是保障主权可信的必要代价。
> > - **商业消费级芯片阵营** 认为过度的物理混淆网格、功耗均衡电路与重度加密鉴权会造成 15%–30% 以上的芯片面积与能耗惩罚，降低产品商业竞争力，主张分级适度防护。
>
> > [!axis] 供应链安全验证：事后破坏性抽样检测 vs 前端设计端零信任免疫
> > 围绕非可信全球化制造环境下，保障芯片真实可信的主导防御路径展开的争论。
> >
> > - **前置内生安全[[Co-Design|协同设计]]学派** 论证指出单纯依赖流片后抽样破坏性物理扫描与 X 射线检测覆盖率极低且成本高昂，必须通过前端安全[[Co-Design|协同设计]]实现“设计端内生免疫”。（pp. 18–19）
> > - **传统军规可信代工（Trusted Foundry）支持者** 坚持认为唯有完全由本国受控的封闭专用可信晶圆厂才能保证硬件的绝对纯净，设计端算法防御无法完全阻断恶意代工厂在底层掺杂层施加的隐蔽物理篡改。

---

## 实证数据

> [!ref-table]- 其他实证结果（无[[Effect Size|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024)]] | 美国关键基础设施与国防微电子全生命周期供应链安全（涵盖材料、设计、流片、先进封装与现场部署） | 跨部门国家安全战略评估与供应链脆弱性审查 | 硬件完整性与安全性（T&AM）要素、零信任硬件架构、抗侧信道防御与 EDA 安全验证工具 | ① 确立硬件信任根（RoT）与物理不可克隆函数（PUF）为底层信任支点；② 规划自动化安全 EDA 验证工具以实现流片前硬件木马 **100% 形式化覆盖**；③ 提出跨部门微电子可信与保证框架 | 跨部门国家战略政策文件与安全规划（原文报告） | 确立硬件安全作为全生命周期内生要素抵御非可信代工风险与物理侧信道攻击的核心战略地位 |

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关联维度与贡献 |
> |:---|:---|:---|
> | [[Trustworthiness]] | Concept | 硬件安全构成了整个信息与计算系统自底向上可信赖性的物理锚点。 |
> | [[Co-Design]] | Concept | 协同设计将硬件安全从外部补丁转化为贯穿全技术栈的前置内生属性。 |
> | [[Reliability]] | Concept | 硬件安全防范主动敌对攻击，与防范物理退化失效的硬件可靠性形成互补。 |
> | [[National Science and Technology Council]] | Fact (Organization) | 制定《微电子研究国家战略》并统筹全美硬件安全科技攻坚的白宫协调机构。 |
> | [[Argument_NSTC_2024_MicroelectronicsResearch\|NSTC (2024)]] | Argument | 白宫[[National Strategy on Microelectronics Research\|国家微电子研究战略]]，确立硬件完整性与安全性为协同设计的核心支柱。 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_NSTC_2024_MicroelectronicsResearch|NSTC (2024)]] — 将硬件完整性与安全性确立为国家安全基石，提出基于零信任硬件信任根与全生命周期安全[[Co-Design|协同设计]]的防御体系。

