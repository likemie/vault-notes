---
title: Dual In-Line Package
aliases:
  - 双列直插封装
  - 双列直插式封装
  - DIP
summary: "1960年代中期由仙童半导体从系统装配与印刷电路板布线视角研发的标准集成电路封装架构，通过双列平行引脚与100密耳间距设计，极大降低布线难度并适配自动插件机，成为商用集成电路大规模扩散的关键物理接口。"
type: concept
domain: "economics"
related_count: 7
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - theme/manufacturing-innovation
  - theme/packaging-technology
  - theme/modular-design
  - theme/electronics-industry
related_concepts:
  - "[[Assemblage]]"
  - "[[Variable]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Fairchild Semiconductor]]"
  - "[[VLSI Project]]"
related_arguments:
  - "[[Argument_Lecuyer_1999_HT]]"
confidence: high
status: draft
created: 2026-10-03
updated: 2026-10-05
---

# Dual In-Line Package

---

## 定义

> [!def] 核心定义
> 双列直插封装（Dual In-Line Package, DIP）是一种具有长方形外壳以及两排平行垂直向下金属引脚的集成电路芯片封装标准架构。该封装于1964至1965年间由[[Fairchild Semiconductor|仙童半导体]]的力克斯·赖斯（Rex Rice）及研发团队针对商用计算机和工业用户的系统级[[Assemblage|装配]]瓶颈研发而成。其核心设计特征在于采用100密耳（mil，即0.1英寸）的标准引脚间距与双列直插布局，既简化了印刷电路板（Printed Circuit Board, PCB）的双层布线拓扑，又能无缝兼容下游计算机制造商广泛采用的自动化插件机，从而彻底打破了军用封装对商业化扩散的成本与工艺制约。[[Argument_Lecuyer_1999_HT|(Lécuyer, 1999, pp. 204–207)]]

> [!concept-lens] 概念透镜
> - **含义** 指向连接微观半导体芯片与宏观系统印刷电路板的标准化物理机械与电气互联界面。
> - **用途** 帮助产业史学者与技术经济学家分析物理封装设计如何作为跨系统协同创新的关键纽带，消解上游先进器件与下游工业组装之间的工艺断层。
> - **边界** 属于通孔插装（Through-Hole Technology）时代的标准封装，不适用于后期超大规模集成电路（[[VLSI Project|VLSI]]）对超高引脚密度的表面贴装技术（Surface-Mount Technology, SMT）需求。

> [!citation-card] 双列直插封装的系统设计视角
> 赖斯与器件开发部的封装团队合作，设计出一种不仅能简化印刷电路板布局、而且能使整机组装更具经济性的封装方案。……他们最终确立了具备双列引脚的双列直插设计。
>
> *Based on these findings, Rice, in collaboration with a packaging group in the device development section, designed a package that would not only simplify the layout of printed circuit boards but make their assembly more economic. ... they transformed the in-line package into the dual in-line package.* [[Argument_Lecuyer_1999_HT|(Lécuyer, 1999, pp. 206–207)]]

> [!boundary]- 概念边界
> - 不等于金属罐封装（TO-5 Metal Can）——TO-5 引脚呈圆形排列，引脚数量有限且难以实现多层密集布线与自动化插件。
> - 不等于军用扁平封装（Flatpack, TO-84）——扁平封装引脚间距过窄（50密耳），要求昂贵的高密度窄迹线 PCB，且必须人工显微焊接，无法适应民用大批量自动化装配。

---

## 概念辨析

> [!contrast-table] 早期微电子封装形式对比
> | 封装类型 | 物理形态与引脚特征 | 制造与[[Assemblage\|装配]]特性 | 目标市场与局限性 |
> |---|---|---|---|
> | **双列直插封装（DIP）** | 矩形塑料或陶瓷外壳，两侧对称平行排列两排直下引脚，100密耳间距 | 极易手工快速插装，完全兼容工业自动化插件机；PCB 布线极为简便 | 面向商用计算机与工业控制系统；成为全球数十年的工业标准 |
> | **扁平封装（Flatpack / TO-84）** | 微型扁平矩形金属/玻璃外壳，引脚从四侧或两侧水平延伸，50密耳微间距 | 必须人工使用显微镜逐脚手工焊接；对 PCB 走线精度要求极高且成本高昂 | 面向航空航天与导弹机载设备（如民兵导弹）；商业整机组装成本过高 |
> | **金属罐封装（TO-5 Can）** | 圆柱形金属晶体管外壳，底盘呈圆形引脚排列（8–10 引脚） | 沿用早期晶体管组装设备，引脚弯折困难，占用纵向空间过大 | 早期过渡形态；引脚扩展受限，布线交叉重叠严重 |

---

## 核心要素

> [!feature] 双列直插封装（DIP）的核心工程要素
> - **100密耳标准化引脚间距（100-mil Pitch）** 相较于军用扁平封装的50密耳间距，100密耳间距允许低成本印刷电路板在引脚之间轻松穿行导线，无需制造昂贵的多层微细走线板。[[Argument_Lecuyer_1999_HT|(Lécuyer, 1999, pp. 205–206)]]
> - **双列平行直插构型（Dual-Row Layout）** 引脚垂直向下插入 PCB 安装通孔，机械刚性强，既支持快速手工定位，又可直接输入波峰焊与自动化插件流水线。[[Argument_Lecuyer_1999_HT|(Lécuyer, 1999, pp. 205–207)]]
> - **塑料模塑成型与低成本材质（Molded Plastic / Ceramic）** 摆脱了金属外壳的高昂成本，能够与低成本环氧树脂模压封装工艺结合，在离岸[[Assemblage|组装]]厂实现大批量低成本产出。[[Argument_Lecuyer_1999_HT|(Lécuyer, 1999, pp. 203–204)]]

---

## 围绕概念形成的命题

---

### 命题一　元器件封装创新必须从下游系统装配与布线经济学视角进行协同重塑

> [!concept-lens] 系统级架构视角与模块化设计
> 探讨电子元器件物理界面如何超越单一芯片物理保护功能，转而作为系统工程中降低下游整机制造总成本的关键杠杆。

> [!claim] Lécuyer, C.
> **整机系统[[Assemblage|装配]]视角主导的物理封装重构** 莱屈耶论述道，在[[Fairchild Semiconductor|仙童半导体]]数字系统实验室负责人力克斯·赖斯的主导下，集成电路封装的研发脱离了传统仅关注芯片密封与散热的狭隘器件视角，转向考量整机印刷电路板布线密度与系统装配经济学的系统视角。实验表明扁平封装在 PCB 上需要大量水平跨线并耗费冗长布线时间，而 DIP 封装大幅削减了布线设计周期与电路板层数，并与控制数据公司（Control Data Corporation, CDC）及通用电气（General Electric, GE）等下游整机客户共同验证，最终通过市场互动将单列直插方案修正为双列直插方案，实现了全行业通用标准的建立。[[Argument_Lecuyer_1999_HT|(Lécuyer, 1999, pp. 205–207)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **系统级装配协同** | 封装设计必须匹配下游 PCB 布线成本与自动化组装流水线要求 | 上游芯片向下游整机系统的大规模扩散阶段 | Lécuyer |

---

## 概念演变

> [!dev-timeline] 概念演变
> - **1960–1963 — 军工主导的金属罐与扁平封装时期** 仙童与德州仪器等主要提供 TO-5 金属罐封装与 TO-84 扁平封装，主要满足机载导航对极端紧凑与耐震动要求。
> - **1964–1965 — 仙童研发与双列直插封装确立** 力克斯·赖斯带领系统与器件团队研发 DIP 架构，在征询控制数据公司等整机客户后定型为 14 引脚与 16 引脚双列直插规格。[[Argument_Lecuyer_1999_HT|(Lécuyer, 1999, pp. 205–207)]]
> - **1966–1980年代 — 成为全球微电子产业标准** 德州仪器、摩托罗拉、英特尔等全行业芯片厂商全面采纳 DIP 标准，主导了个人电脑与家电产业数十年。

---

## 实证数据

> [!ref-table]- 仙童双列直插封装与早期封装形态的工程性能考证数据
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无[[Effect Size\|效应量]]） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Lecuyer_1999_HT\|Lécuyer (1999, p. 206)]] | 1965年仙童数字系统实验室关于扁平封装与直插封装 PCB 布线对比实验 | 实验室工程对比实验与系统布线分析 | PCB布线横向跨线数量与面积占用 | 8引脚扁平封装平均需要5条额外水平走线，且二维板面占用更大；而8引脚直插封装仅需2条额外水平走线 | 实验室系统工程测试报告 | 证实直插架构显著降低电路板布线难度与制造成本 |
> | [[Argument_Lecuyer_1999_HT\|Lécuyer (1999, p. 204)]] | 1966年仙童集成电路封装产品系列（TO-5、Epoxy、Flatpack、DIP） | 产品目录与技术规程考证 | 引脚间距与物理标准 | 扁平封装引脚间距为50密耳（0.05英寸）；DIP封装采用100密耳（0.10英寸）标准化间距与14/16引脚规范 | 官方技术规格书记录 | 说明引脚间距放宽至100密耳是实现自动化插件机兼容性的关键工程阈值 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Lecuyer_1999_HT|Lécuyer (1999)]] — 系统考证了[[Fairchild Semiconductor|仙童半导体]]如何从计算机整机[[Assemblage|装配]]与印刷电路板布线经济学出发，打破军用扁平封装局限，发明并推广双列直插封装（DIP）成为商用半导体行业标准的过程。
