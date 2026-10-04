---
title: Cost of Ownership
aliases:
  - 所有权成本
  - 所有权成本模型
  - COO
summary: "所有权成本（Cost of Ownership, COO）是评估制造装备与研发设施全生命周期单位产出综合成本的标准模型。该模型综合纳入初始资本折旧、日常运维、停机损失及良率损失，确立了单位合格品成本测算标准，是产学研协同与技术验证的核心基准。"
type: concept
domain: "university-industry-collaboration"
related_count: 20
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - university-industry-collaboration
  - technology-transfer
  - manufacturing-economics
  - sematech
related_concepts:
  - "[[Reliability]]"
  - "[[Return on Investment]]"
  - "[[Research Translation]]"
  - "[[Valley of Death]]"
  - "[[Pilot Scale Platform]]"
  - "[[University Spin-Out]]"
  - "[[Megascience Installations]]"
  - "[[Hypothesis]]"
  - "[[Paradigm]]"
  - "[[Variable]]"
  - "[[Assemblage]]"
related_theories: []
related_methods:
  - "[[Statistical Process Control]]"
  - "[[Sample Size Determination]]"
  - "[[Effect Size]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons:
  - "[[David C. Mowery]]"
related_facts:
  - "[[Sematech]]"
  - "[[Competitive Semiconductor Manufacturing Program]]"
related_arguments:
  - "[[Argument_Grindley_1994_JPAM]]"
  - "[[Argument_Macher_1998_CMR]]"
confidence: high
status: active
created: 2026-10-04
updated: 2026-10-04
---

# Cost of Ownership

---

## 定义

> [!def] 核心定义
> **所有权成本（Cost of Ownership, COO）**是指在装备或技术系统的整个生命周期内，为获得、运营、维护该设备并生产单位合格产出物所分摊的全部直接与间接经济成本之和。与仅关注购置标价的传统核算不同，COO 模型将初始固定投资、可变运行维护费用、设备[[Reliability|可靠性]]/利用率损失以及材料与良率缺陷损失统一转化为“单位合格产出成本”（Cost per Good Unit），成为衡量先进制造装备生命周期真实经济价值与产业竞争力的权威基准。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, pp. 735, 746)]]

> [!concept-lens] 概念透镜
> - **含义** 指向设备全生命周期内资本投入、物料消耗、停机维护与良率损失的综合经济度量机制。
> - **用途** 帮助采购方与研发方摆脱“低单价购置但高故障返修”的劣质锁定，为产学研协作与供应链技术研发提供统一的经济评价语言。
> - **边界** 聚焦于已知工艺与生产环节的生命周期成本核算，不直接评估颠覆性技术创新的战略期权价值或技术溢出效应。

> [!citation-card] 关键表述
> 广泛推行所有权成本（Cost of Ownership, COO）模型与[[Statistical Process Control|统计过程控制]]（SPC），能够系统性识别设备生命周期内的关键耗损环节，帮助中小设备商建立规范的工程化标准，进而大幅缩短新设备入厂调试周期并降低运行总成本。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, p. 735)]]
>
> *Widespread adoption of the Cost of Ownership (COO) model and statistical process control techniques enabled suppliers and buyers to evaluate equipment based on lifetime operating economics and reliability rather than initial purchase price alone.*

> [!boundary]- 概念边界
> - 不等于 **设备采购价格（Purchase Price）** — 采购价格仅为初始资本开支，在高端复杂装备中往往仅占全生命周期总成本的 20%–40%，忽视维护、良率与停机损失会导致严重的决策扭曲。
> - 不等于 **通用总拥有成本（Total Cost of Ownership, TCO）** — IT 领域的 TCO 多侧重软件授权与人力维护，而半导体与先进制造的 COO 模型（如 SEMI E35 标准）深度整合了材料损耗、物理吞吐率（Throughput）与微观晶圆缺陷复合良率（Composite Yield）。

---

## 概念辨析

> [!contrast-table] 概念辨析
> | 维度 | 所有权成本（COO） | 设备购置价格（Purchase Price） | 通用总拥有成本（TCO） | [[Return on Investment\|投资回报率]]（ROI） |
> |---|---|---|---|---|
> | **分析对象** | 单位合格产出物的全生命周期成本 | 购买设备时的初始交易契约金额 | 组织拥有特定资产的信息技术与管理总开销 | 资本投入所产生的净收益与投入之比 |
> | **核心机制** | 整合固定成本、运营维护与良率损失分摊 | 供应商报价与市场买卖博弈定价 | 统计直接软硬件支出与间接人力运维负担 | 比较贴现现金流收益与全额资本开支 |
> | **核心输出** | 单个合格晶圆/零件的综合成本（\$/Good Die） | 单台设备总售价（\$） | 周期内总支出绝对额（\$） | 收益率百分比或回收年限 |
> | **适用情境** | 高端制造中试验证、设备选型与工艺路线优化 | 简单标准品采购与初次资产核算 | 企事业单位 IT 基础设施规划与运维预算 | 重大研发项目投资决策与商业化论证 |

---

## 核心要素

> [!feature] 核心要素
> - **固定资本成本（Fixed Capital Costs）** 包含设备采购标价、厂房洁净室空间占用折旧、安装调试工程费及配套辅助设施投入。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, p. 735)]]
> - **可变运营与维护成本（Recurring Operating Costs）** 包含工艺消耗品（靶材、化学气体、去离子水）、电力与气体能耗、预防性维护备件及现场工程师人力成本。
> - **[[Reliability|可靠性]]与停机损失（Reliability and Downtime Costs）** 包含非计划故障停机造成的产能闲置损失、平均无故障工作时间（MTBF）及平均修复时间（MTTR）对应的机会成本。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, p. 746)]]
> - **良率与材料报废损失（Yield Loss and Scrap Costs）** 包含设备缺陷引入导致的晶圆破损、边缘失真及缺陷密度增加造成的未合格品分摊成本。
> - **有效综合吞吐量（Composite Good Throughput）** 设备在生命周期内实际生产的总晶圆数与复合工艺良率的乘积，是所有成本的分摊分母。

> [!logic-map]- 要素关系
> ```mermaid
> flowchart TD
>     A["固定资本支出<br>(购置费 + 厂房设施 + 安装调试)"] --> D["总生命周期支出"]
>     B["可变运营维护<br>(化学消耗品 + 备件 + 能源 + 人力)"] --> D
>     C["停机与良率损失<br>(故障停机 + 缺陷报废 + 调试延误)"] --> D
>     D --> E["所有权成本 (COO)<br>单位合格产出成本 ($/Good Wafer)"]
>     F["有效产能基数<br>(运行工时 × 吞吐速率 × 复合良率)"] --> E
> ```

---

## 围绕概念形成的命题

---

### 命题一　基于所有权成本的全生命周期核算打破了低价劣质采购与高额停机调试的负向锁定循环

> [!concept-lens] 供应链激励与技术升级机制
> 传统设备采购中买方常利用买方垄断地位压低供应商设备标价，导致设备商缩减工程设计与[[Reliability|可靠性]]测试预算，最终在晶圆厂运行中因频繁故障和良率损失导致巨额隐形成本。

> [!claim] Grindley, P. C., [[David C. Mowery|Mowery, D. C.]], & Silverman, B. S.; Macher, J. T., Mowery, D. C., & Hodges, D. A.
> **采购激励机制重构** 在 [[Sematech]] 的推动下，全行业建立起统一的 COO 模型（后上升为 SEMI 行业标准）。芯片制造商不再单纯依据采购单价压榨上游供应商，而是根据设备在 5 年生命周期内的单位产出综合成本进行竞标，促使设备商将研发重点由“拼低价”转向“提升平均无故障工作时间（MTBF）与工艺良率”，使关键设备运行成本降低高达 50%。Macher 等人进一步指出，COO 模型的确立是联盟最持久的制度遗产之一，它将零和对抗的买卖关系转化为基于全生命周期经济学的长期战略契约。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, pp. 735, 746)]]; [[Argument_Macher_1998_CMR|(Macher et al., 1998, pp. 121–122)]]

---

### 命题二　标准化 COO 模型构成了产学研跨界协同中降低信息不对称与技术验证风险的通用语言

> [!concept-lens] 产学研协同度量与标准沉淀
> 高校与中试机构研发的新型工艺装备若无法提供工业界认可的经济学可信数据，难以跨越[[Research Translation|技术转化]]过程中的“[[Valley of Death|死亡之谷]]”。

> [!claim] Grindley, P. C., Mowery, D. C., & Silverman, B. S.
> **中试验证与通用评价语言** 在奥斯汀建立的[[Pilot Scale Platform|中试验证平台]]中，COO 模型与[[Statistical Process Control|统计过程控制]]（SPC）共同作为设备准入与交付验收的法定工具。通过在真实生产工况下模拟连续运行，平台精确测算并验证了新型原型机的 COO 指标，消除了制造厂对中小创新企业设备可靠性的顾虑，大幅加速了前沿技术的商业化落地。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, pp. 734–735)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **供应链升级与激励重构** | 以生命周期单位成本替代采购单价，驱动供应商聚焦可靠性与良率提升 | 复杂高端制造装备供应链与技术采购 | Grindley, Mowery, & Silverman; Macher, Mowery, & Hodges |
> | **产学研协同与中试验证** | 提供可量化的经济效能度量标准，降低新技术跨越死亡之谷的验证成本 | 中试平台、[[University Spin-Out\|大学衍生企业]]与共性技术联盟 | Grindley, Mowery, & Silverman |

---

## 概念演变

> [!dev-timeline] 概念演变
> - **1980 年代初 — 传统单价采购阶段** 半导体及重型装备采购主要依赖单台设备购置价格谈判，忽视隐性停机成本与缺陷损失。
> - **1989–1992 年 — [[Sematech]] 与 SEMI 标准化阶段** SEMATECH 联合国际半导体设备与材料协会（SEMI）开发出标准 COO 数学模型与专用计算软件，随后确立为 SEMI E35 标准，成为全球半导体行业的通用准则。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, pp. 735, 746)]]; [[Argument_Macher_1998_CMR|(Macher et al., 1998, pp. 121–122)]]
> - **2000 年代至今 — 跨行业与重大科研基础设施拓展** COO 模型从微电子制造广泛拓展至光伏新能源、大型生物制药反应器、国家实验室[[Megascience Installations|大科学装置]]及高校共享实验平台的运行效能评估。

---

## 争议与批评

> [!critique] 外部批评
> - **参数高度敏感性与主观[[Hypothesis|假设]]偏差** COO 计算对设备稼动率（Utilization Rate）与微小良率波动的假设极为敏感，微小的参数设定偏差可能导致不同设备之间的单位成本估算产生数倍颠倒。
> - **忽略战略颠覆性技术价值** COO 模型本质上是针对渐进性技术改良与已知工艺路线的优化工具；当面临全新[[Paradigm|范式]]革新（如全新光刻物理架构）时，初期极高的 COO 可能会扼杀具有远期战略潜力的颠覆性技术。

> [!warning] 适用局限
> COO 模型高度依赖真实连续生产环境下的精确工时与缺陷数据收集，在缺乏中试验证环境或[[Sample Size Determination|样本量]]极小的实验室研发初期，难以开展高置[[Reliability|信度]]的模型测算。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, p. 735)]]

---

## 实证数据

> [!ref-table]- 其他实证结果（无[[Effect Size|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Grindley_1994_JPAM\|Grindley et al. (1994)]] | 1988–1992 年美国半导体制造与设备产业（[[Sematech]] 合作项目及 11 项工程案例） | 产业追踪与多案例定性/定量分析 | 设备运行成本、MTBF、[[Assemblage\|装配]]调试周期 | 推广 COO 与 [[Statistical Process Control\|SPC]] 后，设备生命周期运行成本削减最高达 50%，在役设备 MTBF 显著倍增，新设备调试周期由数月缩短至数周 | 描述性产业案例统计，无推断性统计检验 | 结果反映纵向协同与工程工具推广的综合成效，不可单独归因于单一财务模型 |
> | [[Argument_Macher_1998_CMR\|Macher et al. (1998)]] | 1980–1997 年美日半导体制造装备与材料产业（SME 供应商与晶圆厂数据） | 宏观产业追踪与微观标杆案例分析 | 设备[[Reliability\|可靠性]]、买卖双方合作研发密度、全球装备市场份额 | COO 模型标准化消除了买卖双方信息不对称，驱动美国装备商在 1992 年以 51% 份额重夺全球第一，奠定了设备供应链长期竞争壁垒 | 描述性统计与产业案例，结合伯克利 [[Competitive Semiconductor Manufacturing Program\|CSM]] 现场调研 | 份额回升兼受宏观日元升值与日本投资紧缩影响，COO 提供了微观工程能力支撑 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Grindley_1994_JPAM|Grindley et al. (1994)]] — 详述 [[Sematech]] 如何通过开发与推广 COO 标准模型，重塑半导体设备买卖双方长期信任并降低装备生命周期运行成本。
> - [[Argument_Macher_1998_CMR|Macher et al. (1998)]] — 论证 COO 标准化与技术路线图如何作为制度基础设施，支撑美国半导体装备产业实现制造能力重构与全球份额逆转。
