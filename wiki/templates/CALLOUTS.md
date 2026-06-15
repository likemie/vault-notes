# Callouts

本文件定义 `wiki/templates/` 使用的 callout 语义和 CSS contract。具体视觉样式由 `.obsidian/snippets/argument-callouts.css` 提供；本文件只规定“什么时候用哪一种”。

---

## General Rules

- callout 服务阅读层次，用来区分定义、论证框架、数据、例子、争议、原文引用和结构导航。
- 普通说明段不要强行包进 callout。
- 同一节内 callout 不宜过密；内容少于 3 点时优先用散文或普通列表。
- 任何 callout 可加 `+` 或 `-` 控制折叠，例如 `[!stat-cards]-`。
- 嵌套不超过 2 层。
- 列表项内嵌套 callout 使用 `>    > [!type]`，即外层 `>` 加 3 个空格再加内层 `>`。
- Mermaid 节点标签保持单行简短，流程图默认使用 `flowchart LR`。
- `---` 分割线用于主要章节之间，以及 Argument 论证步骤之间；不要在同一小段内部频繁插入。
- 样式库只提供可复制的版式，不要求每篇 Argument 全部使用；优先服务论证清晰度。
- `[!logic-map]` 内节点标签不使用 `\n`，保持单行简短标签。
- `---` 的视觉语义：`##` 之前用于模块级切割；`###` 之前用于步骤间流程延续。

---

## Core Callouts

| Callout | 用途 |
|---|---|
| `[!info]` | 定义、背景、方法说明、前提条件 |
| `[!abstract]` | 核心主张摘要、理论框架、政策摘要、章节结构 |
| `[!question]` | 研究问题、经验谜题、核心关切 |
| `[!claim]` | 核心主张、局部命题、论证步骤中的可争辩判断 |
| `[!warrant]` | 证据与主张之间的推理桥梁、理论支撑理由 |
| `[!implication]` | 发现、命题或论证的理论、方法和实践后果 |
| `[!concept-lens]` | 概念的含义、用途和边界三联透镜 |
| `[!success]` | 主要发现、影响、效果 |
| `[!warning]` | 局限、风险、重要例外 |
| `[!tip]` | 理论提示、相关理论、可迁移经验 |
| `[!quote]` | 原文引用或双语关键引用 |
| `[!example]` | 案例、教育情境例子 |
| `[!note]-` | 可折叠补充说明 |
| `[!nav]` | 长节开头的阅读导览 |
| `[!reading-lens]` | 页面级阅读镜头或样式库导览，主要用于模板说明 |
| `[!argument-map]` | 页面或章节级论证地图，适合放 Mermaid 或路径表 |

---

## Argument Callouts

| Callout | 用途 |
|---|---|
| `[!stat-cards]` | 样本量、比例、效应量、关键数字 |
| `[!framework-table]` | 理论镜头、概念工具箱 |
| `[!method-panel]` | 研究设计、材料处理、分析步骤 |
| `[!sample-panel]` | 样本构成、材料快照、访谈信息 |
| `[!logic-map]` | Mermaid 论证图、机制图、因果链 |
| `[!step]` | 单个论证步骤容器 |
| `[!line-a]` | 并列趋势、证据链或命题线索，连续使用时自动 A、B、C |
| `[!line-b]` | 与前一个 `[!line-a]` 构成左右拼合或对照 |
| `[!chain-link]` | 独立“证据到分析结论”链节 |
| `[!evidence-grid]` | 多点并列证据 |
| `[!evidence-grid-a]` | 第一组主题证据，常与 `[!evidence-grid-b]` 对照 |
| `[!evidence-grid-b]` | 第二组主题证据，常与 `[!evidence-grid-a]` 对照 |
| `[!contrast-table]` | 两种或多种逻辑、框架、案例的多维对照 |
| `[!finding-cards]` | 不超过四条核心发现 |
| `[!pathways]` | 行动路径、实践建议、操作化方案 |
| `[!conclusion]` | 论证结论或批评裁定 |
| `[!voice]` | 边缘声音、访谈引述、立场陈述 |
| `[!case]` | 独立政策或实证案例 |
| `[!ref-table]` | 参考速查表，适合地区、案例或指标一览 |
| `[!meta-table]` | 5 列元分析或研究综述表，适合“研究 / 是否纳入 / N / 效应量 / 结论” |
| `[!event-context]` | Event 背景档案，适合时间、地点、主体、制度背景和触发条件 |
| `[!policy-context]` | Policy 背景档案，适合发布主体、适用对象、政策问题和制度位置 |
| `[!policy-design]` | Policy 设计四格，固定为目标、对象、工具、约束方式 |

Argument 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 研究问题 | `[!question]`、`[!stat-cards]` |
| 理论框架 | `[!framework-table]`、`[!logic-map]`、`[!frames-ref]`、`[!warrant]` |
| 研究方法 | `[!method-panel]`、`[!sample-panel]` |
| 论证结构 | 按论文实际论证综合使用 `[!argument-map]`、`[!logic-map]`、`[!claim]`、`[!chain-link]`、`[!warrant]`、`[!line-a]`、`[!contrast-table]`、`[!evidence-grid]` |
| 主要发现 | `[!finding-cards]`、`[!stat-cards]`、`[!evidence-grid]`、`[!meta-table]` |
| 自述局限 | `[!warning]` |
| 关键引用 | `[!citation-card]` |

注意：

- `[!line-a]` 连续使用时表示并列线索或证据链，序号自动递增。
- `[!line-b]` 只在需要与前一个 `[!line-a]` 构成左右拼合或对照时使用。
- `[!chain-link]` 用于完整的“证据 → 分析结论”链节，各块内容应自足。
- `[!stat-cards]` 在方法章节可写样本量；在主要发现章节应优先写结果数据，不把受访人数等样本背景混入核心发现。
- `[!finding-cards]` 适合 3–4 条核心发现；超过 4 条时改用小节或证据网格。
- `[!claim]` 必须写可争辩判断，不写材料描述。
- `[!warrant]` 必须解释“为什么证据能支持主张”，不重复证据。
- `[!implication]` 用于收束意义，避免把所有延伸讨论塞进主要发现。

---

## Table Callouts

| Callout | 适合内容 | 表格结构 |
|---|---|---|
| `[!framework-table]` | 理论镜头、概念工具箱、分析维度 | 通常 2 列：工具 / 用法 |
| `[!method-panel]` | 研究设计、材料处理、分析策略 | 通常 2 列：环节 / 说明 |
| `[!sample-panel]` | 样本构成、材料快照、访谈信息 | 通常 2 列：维度 / 信息 |
| `[!contrast-table]` | 概念辨析、案例对比、理论路径对比 | 2–4 列，多维比较 |
| `[!evidence-grid]` | 多项证据、指标或发现一览 | 列表或表格均可 |
| `[!ref-table]` | 地区、案例、指标、文献速查 | 通常 3 列：对象 / 说明 / 来源 |
| `[!meta-table]` | 元分析、系统综述、研究纳入表 | 固定 5 列：研究 / 纳入 / N / d / 结论 |
| `[!chain-link]` | 证据到结论的链节 | 可用 2–3 列拆“证据 / 推理 / 结论” |
| `[!line-a]` | 并列线索中的结构化材料 | 可用短表格承载单条线索 |

注意：

- 表格型 callout 只在“维度清楚、列名稳定”时使用；否则优先用普通列表或散文。
- `[!ref-table]` 用于查阅，不承担论证推进；`[!contrast-table]` 用于比较，必须有明确比较维度。
- `[!meta-table]` 是 5 列专用样式，不要挪作普通参考表。
- Concept 的 `## 实证发现` 和 `## 应用案例` 默认仍是一句话索引；只有需要横向比较时才升级为表格型 callout。

---

## Concept and Theory Callouts

| Callout | 用途 |
|---|---|
| `[!boundary]` | 概念边界、适用范围、排除条件 |
| `[!def]` | 概念定义，适合突出核心定义和边界 |
| `[!term]` | 术语说明，适合短定义或名称辨析 |
| `[!tension]` | 理论张力、对立立场、规范冲突 |
| `[!feature]` | 并列特征或属性卡片 |
| `[!features]` | 紧凑特征列表，常嵌套在父 callout 中 |
| `[!taxonomy]` | 分类或层级体系 |
| `[!assumptions]` | 一组层层递进的理论假设或前提 |
| `[!axioms]` | 公理化前提或不可再拆的基础命题 |
| `[!designs]` | 设计类型、研究设计或制度设计方案 |
| `[!decisions]` | 决策点、判断路径或选择标准 |
| `[!exegesis]` | 抽象概念或论证步骤的解释性补充，常配教育例子 |
| `[!timeline]` | 年代里程碑列表，每项一行 |
| `[!phase]` | 有明确起止年代的历史阶段叙事 |
| `[!dev-timeline]` | 大型分阶段时间轴，含子事件和散文详情 |
| `[!frames-ref]` | 固定数量的框架、原则或要点，适合 6–12 项 |
| `[!quad-grid]` | 恰好 4 项且权重相当的类型、案例或框架 |
| `[!actor-grid]` | 行动者或利益相关者类型网格 |
| `[!col-l]` + `[!col-r]` | 父 callout 内两个并列子主题 |
| `[!theory-position]` | 理论定位四格，固定写解释对象、理论问题、理论类型和知识位置 |
| `[!proposition-chain]` | 核心命题链，按前提、机制、条件和结果判断组织理论推理 |
| `[!mechanism-map]` | 理论机制图，优先放 Mermaid 或短机制链，不替代逐条命题解释 |
| `[!theory-components]` | 理论构件，说明关键概念、分类、机制或方法在理论中的功能 |
| `[!theory-stance]` | 认识论与方法含义，说明本体论、认识论、方法含义和不能推出的东西 |
| `[!theory-use]` | 理论使用方式，说明如何作为框架、工具、批判视角和报告逻辑 |
| `[!theory-boundary]` | 理论适用边界，固定写适合、谨慎、不适合和常见误用 |

Concept 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 定义 | `[!def]`、`[!concept-lens]`、`[!boundary]`、`[!quote]` |
| 概念辨析 | `[!contrast-table]`、`[!ref-table]` |
| 核心要素 | `[!feature]`、`[!logic-map]`、`[!taxonomy]`、`[!frames-ref]`、`[!contrast-table]`、`[!ref-table]` |
| 围绕概念形成的命题 | `[!claim]`、`[!warrant]`、`[!implication]`、`[!line-a]`、`[!logic-map]`、`[!finding-cards]` |
| 概念演变 | `[!timeline]`、`[!phase]`、`[!dev-timeline]` |
| 实证发现 | 默认用 `[!evidence-grid-a]` 承载一句话索引；材料丰富时可选 `[!stat-cards]`、`[!finding-cards]`、`[!evidence-grid-b]`、`[!meta-table]` |
| 争议与批评 | 根据实际材料选用 `[!tension]`、`[!warning]`、`[!critique]`、`[!critique-method]`、`[!critique-logic]`、`[!critique-data]`、`[!critique-fatal]` |
| 应用案例 | 默认用 `[!case]` 承载一句话索引；材料丰富时可选 `[!evidence-grid-a]`、`[!evidence-grid-b]` |
| 关键引用 | `[!citation-card]` |

注意：

- `[!line-a]` + `[!line-b]` 适合概念对或命题与延伸的层级关系；内容简短时改用 `[!finding-cards]`。
- `[!frames-ref]` 适合 6–12 个固定并列条目；有层级或需要散文延伸时改用 `[!finding-cards]`。
- `[!dev-timeline]+` 适合有丰富子事件的概念发展；内容少时降级为 `[!timeline]` 或 `[!phase]`。
- `[!citation-card]` 每节最多 1–2 个，优先集中到页面后部。
- `[!contrast-table]` 是 `## 概念辨析` 的首选样式。
- `[!concept-lens]` 适合定义章节开头，用三点快速说明“含义、用途、边界”。

---

## Method and Critique Callouts

| Callout | 用途 |
|---|---|
| `[!proc]` | 标准操作程序、研究步骤链、方法执行流程 |
| `[!method-scope]` | Method 范围四格，固定为研究对象、问题类型、分析单位、输出形式 |
| `[!method-position]` | Method 的认识论定位、研究者角色、有效性标准和不能回答的问题 |
| `[!method-stack]` | Method 层级结构，适合研究设计、数据收集、分析方法和辅助技术 |
| `[!method-fit]` | Method 适用判断三格，固定为适合、谨慎、不适合 |
| `[!formula]` | 单个核心公式、变量表和计算顺序 |
| `[!formula-step]` | 一个公式步骤，固定写公式、数学解释、结果解读和注意事项 |
| `[!formula-set]` | 多公式链总览，优先放 Mermaid 流程图或短流程，不放大公式表 |
| `[!math-principle]` | 公式的数学直觉、关键性质和隐含假设 |
| `[!result-reading]` | 量化结果的正确解读、报告方式和常见误读 |
| `[!software-impl]` | 软件实现、核心包/命令、复现步骤和报告标准 |
| `[!method-limits]` | 方法局限、参数边界、权重敏感性、阈值风险和误用提醒 |
| `[!critique]` | 通用学术批评 |
| `[!critique-method]` | 方法论或统计错误 |
| `[!critique-logic]` | 逻辑或概念矛盾 |
| `[!critique-data]` | 实证或数据反例 |
| `[!critique-fatal]` | 根本性缺陷 |

Method 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 定义 | `[!def]`、`[!method-scope]`、`[!citation-card]` |
| 认识论立场 | `[!method-position]`、`[!assumptions]`、`[!axioms]` |
| 方法层级 | `[!method-stack]`、`[!method-panel]` |
| 研究程序 | `[!proc]`、`[!formula-step]`、`[!method-panel]` |
| 资料与分析 | `[!method-stack]`、`[!method-panel]`、`[!sample-panel]`、`[!formula]`、`[!formula-set]`、`[!math-principle]`、`[!result-reading]`、`[!software-impl]` |
| 适用场景 | `[!method-fit]`、`[!decisions]`、`[!pathways]` |
| 局限性 | `[!method-limits]`、`[!critique-method]`、`[!warning]` |
| 相关理论 | `[!frames-ref]`、`[!ref-table]` |
| 使用此方法的研究 | 默认用 `[!evidence-grid-a]` 承载一句话索引 |

注意：

- Method 的 `## 定义` 优先用 `[!method-scope]` 固定四格，避免把方法对象、问题类型、分析单位和输出形式混写在同一段。
- Method 的 `## 方法定位` 优先用 `[!method-position]`，方法层级优先用 `[!method-stack]`。相关方法链接不要挤在表格单元格里，优先写成子列表。
- Method 的 `## 适用场景` 优先用 `[!method-fit]` 固定三格，分别写适合使用、谨慎使用和不适合使用。
- Method 默认少用表格。只有需要横向比较、指标清单或固定列结构时才用 `[!method-panel]`、`[!ref-table]` 或普通表格；普通说明优先用 `[!method-stack]` 或散文。
- 量化 Method 面向新手时，优先使用“流程总览 + 多个 `[!formula-step]`”的结构。每个公式步骤只解释一个核心公式，并紧接数学原理和结果读法。
- `[!formula-step]` 固定顺序为：公式 → 这个公式在做什么 → 数学直觉 → 嵌套 `[!result-reading]` → 嵌套 `[!method-limits]` 或 `[!warning]`。不要把 4 个以上公式塞进一张大表。
- `[!formula]` 适合一个独立核心公式，公式下方可放简短符号说明；`[!formula-set]` 只作为多公式链总览，优先用 Mermaid 流程图，不替代逐个公式解释。
- `[!math-principle]` 不重复变量定义，重点写平均、加权、标准化、距离、似然、惩罚、方差分解、空间邻接等数学直觉，以及公式的取值范围、边界条件和隐含假设。
- `[!result-reading]` 必须区分“能说明什么”和“不能说明什么”。描述性指数、分类结果、空间相关和预测结果不得直接写成因果效果。
- `[!software-impl]` 写实际可复现路径，优先包括数据处理、推荐软件、核心包或命令、运行顺序、诊断检查、导出和版本信息。
- `[!method-limits]` 用于集中呈现局限性，也可嵌套在 `[!formula-step]` 中说明该公式的参数、权重、阈值、分类和误用风险。

Theory 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 理论定位 | `[!theory-position]`、`[!claim]`、`[!citation-card]` |
| 核心命题与机制 | `[!proposition-chain]`、`[!mechanism-map]`、`[!warrant]`、`[!exegesis]` |
| 关键概念与理论构件 | `[!theory-components]`、`[!frames-ref]`、`[!taxonomy]` |
| 认识论与方法含义 | `[!theory-stance]`、`[!assumptions]`、`[!axioms]` |
| 分析框架与使用方式 | `[!theory-use]`、`[!logic-map]`、`[!frames-ref]` |
| 适用边界 | `[!theory-boundary]`、`[!boundary]`、`[!decisions]` |
| 发展脉络 | `[!timeline]`、`[!phase]`、`[!dev-timeline]` |
| 争议与批评 | `[!tension]`、`[!critique]`、`[!critique-method]`、`[!critique-logic]`、`[!critique-data]` |
| 相关研究 | 默认用 `[!evidence-grid-a]` 承载一句话索引 |
| 应用领域 | 默认用 `[!case]` 承载一句话索引 |

注意：

- Theory 默认少用大表格。理论构件、命题链和使用方式优先用专用 callout；只有比较多个理论、分类稳定或需要速查时才使用 `[!contrast-table]`、`[!framework-table]` 或普通表格。
- `[!theory-position]` 是入口模块，不写成文献背景；它只回答理论解释什么、回应什么问题、属于什么理论类型、站在哪个知识传统中。
- `[!proposition-chain]` 必须有推理方向，不能只是核心观点列表。命题之间应能读出“前提 → 机制 → 条件 → 结果”的关系。
- `[!mechanism-map]` 只放机制总览，优先用 Mermaid 图；图后仍要用 `[!proposition-chain]` 或散文解释关键命题。
- `[!theory-components]` 不是相关条目列表。每个链接都要说明它在理论中承担定义、分类、机制、证据或方法功能。
- `[!theory-stance]` 必须写“不能直接推出的东西”，防止把理论主张误写成因果证明、普遍规律或规范结论。
- `[!theory-boundary]` 用于集中提醒适用边界和常见误用，尤其适合学习科学、政策理论、批判理论和方法论框架。

---

## Person Callouts

| Callout | 用途 |
|---|---|
| `[!person-profile]` | 人物档案四格，固定写身份位置、建条目理由、代表贡献和阅读边界 |
| `[!contribution-map]` | 贡献地图，连接人物对概念、理论、方法和制度／政策的具体贡献 |
| `[!work-line]` | 主要著作线，按年份说明著作的问题意识、核心贡献和思想转向 |
| `[!thought-timeline]` | 思想发展时间线，按阶段说明代表著作、关键概念／方法和阶段转向 |
| `[!influence-path]` | 影响路径，区分理论、方法、政策和跨国／跨领域传播 |
| `[!person-network]` | 关系网络，记录师承、合作、继承、批评、机构或运动关系 |

Person 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 简介 | `[!person-profile]`、`[!citation-card]` |
| 贡献地图 | `[!contribution-map]` |
| 生平与职涯 | `[!timeline]`、`[!phase]` |
| 主要著作与思想发展 | `[!work-line]`、`[!thought-timeline]`、`[!phase]` |
| 核心思想 | `[!claim]`、`[!concept-lens]`、`[!citation-card]` |
| 影响路径 | `[!influence-path]`、`[!evidence-grid-a]` |
| 关系网络 | `[!person-network]` |
| 争议与批评 | `[!tension]`、`[!critique]`、`[!warning]` |

注意：

- `[!person-profile]` 是入口模块，不写成长篇传记；它只回答“此人是谁、为什么建条目、贡献在哪里、本文读哪一面”。
- `[!contribution-map]` 不是相关条目列表。每一项都必须说明此人与对应 Concept / Theory / Method / Fact 的贡献关系。
- `[!work-line]` 用于新手友好的著作线索，优先一书一条说明问题意识、贡献和转向；只有书目信息需要横向比较时才改用表格。
- `[!thought-timeline]` 用于在著作线基础上做分阶段思想发展。每个阶段必须写阶段名、代表著作、关键概念／方法和阶段转向；资料不足时不要强行分期。
- `[!influence-path]` 要区分影响类型，避免把“很有影响”写成泛泛评价。
- `[!person-network]` 只收录能解释思想、影响或争议的关系；普通共现作者和偶然引用不放入。

---

## Book and Evaluation Callouts

| Callout | 用途 |
|---|---|
| `[!chapter-question]` | 章节研究问题或章节在全书论证中的位置 |
| `[!textbook-overview]` | 教材章节总览表，列出章节链接、内容概要和主要关联条目 |
| `[!knowledge-map]` | 教材总览知识地图或章节概念地图，通常可先占位 |
| `[!monograph-profile]` | 专著档案，固定写核心对象、论证类型、处理粒度和材料边界 |
| `[!monograph-thesis]` | 全书核心主张，区分问题起点、核心解释和最终贡献 |
| `[!monograph-tools]` | 专著理论与概念工具，说明理论、概念、类型或框架如何贯穿全书 |
| `[!monograph-method]` | 专著研究方法与材料，说明研究设计、资料来源、分析策略和方法边界 |
| `[!book-argument-map]` | 全书论证图，优先放 Mermaid 论证路径 |
| `[!argument-steps]` | 全书论证步骤，按问题、工具、前提、证据、推论、结论和谨慎处组织 |
| `[!chapter-arc]` | 章节推进线，说明各章在全书连续论证中的功能 |
| `[!book-synthesis]` | 跨章综合，提炼跨章节主题、机制、案例、方法或反例关系 |
| `[!book-limits]` | 专著自述局限与使用边界 |
| `[!volume-profile]` | 编著档案，固定写核心议题、材料边界、章节关系和使用方式 |
| `[!volume-argument]` | 编者组织主张，区分共同问题、组织逻辑和整体贡献 |
| `[!volume-structure]` | 全书结构，按部分或章节组说明全书推进关系 |
| `[!volume-map]` | 编著结构图，优先放 Mermaid 流程图或短结构链 |
| `[!volume-tools]` | 编著理论、方法与关键词工具箱 |
| `[!cross-chapter]` | 跨章主题线索，记录章节之间的横向概念、案例、方法或争议关系 |
| `[!chapter-roadmap]` | 章节处理路线，说明已处理、优先处理、可暂缓和缺口 |
| `[!chapter-index]` | 章节索引，记录章节 Argument 链接、候选文件名和一句话贡献 |
| `[!volume-contribution]` | 编著整体贡献，说明研究议题、理论方法和资料价值 |
| `[!volume-limits]` | 编著使用边界，提醒 overview 不能替代单章论证或系统综述 |
| `[!strength]` | SWOT 或评价中的优势 |
| `[!weakness]` | SWOT 或评价中的劣势 |
| `[!opportunity]` | SWOT 或评价中的机会 |
| `[!threat]` | SWOT 或评价中的威胁 |
| `[!indicators]` | 评价指标体系或分层指标 |
| `[!lessons]` | 案例分析后的经验、启示或教训 |

Monograph 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 全书定位 | `[!monograph-profile]` |
| 研究问题与核心主张 | `[!question]`、`[!monograph-thesis]`、`[!citation-card]` |
| 理论、概念与方法工具 | `[!monograph-tools]`、`[!monograph-method]` |
| 全书论证地图 | `[!book-argument-map]`、`[!argument-steps]` |
| 章节推进 | `[!chapter-arc]`、`[!chapter-index]`、`[!chapter-question]` |
| 跨章综合 | `[!book-synthesis]`、`[!finding-cards]`、`[!stat-cards]` |
| 自述局限与使用边界 | `[!book-limits]`、`[!warning]` |

注意：

- Monograph Argument 是整本书的论证入口。`single-argument` 可以累积简短章节小节；`chapter-arguments` 只在本页维护章节索引和跨章综合。
- `[!monograph-profile]` 必须说明处理粒度和材料边界，避免把部分章节读法误写成全书结论。
- `[!monograph-thesis]` 不是摘要，必须区分问题起点、核心解释和最终贡献。
- `[!monograph-tools]` 只写贯穿全书的理论、概念或类型工具；单章局部工具回到章节 Argument。
- `[!monograph-method]` 必须写方法边界，尤其是质性专著、历史专著、政策分析和理论建构类专著。
- `[!book-argument-map]` 放全书路径总览，优先用 Mermaid；细节用 `[!argument-steps]` 展开。
- `[!chapter-arc]` 强调章节如何推进全书论证，不重复目录。
- `[!book-synthesis]` 只写跨章节才成立的综合判断，不机械汇总每章小结。

Textbook 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 章节总览表格 | `[!textbook-overview]` |
| 总览知识地图 | `[!knowledge-map]` |
| 章节概念地图 | `[!knowledge-map]`、`[!example]` |
| 章节内容结构 | `[!abstract]`、`[!info]`、`[!note]` |
| 图表、案例、练习 | `[!example]`、`[!tip]` |
| 易错点或限制 | `[!warning]`、`[!note]` |
| 关键引用 | `[!quote]`、`[!citation-card]` |

注意：

- Textbook Argument 是教材总览和章节整理页，不是逐段摘要。稳定定义、分类、步骤、争议和案例应沉淀到具体 wiki 条目。
- 总览页使用 `[!textbook-overview]` 章节表格和 `[!knowledge-map]` 知识地图。知识地图通常可以先占位，等章节处理较完整后再绘制。
- 如果采用分章节 Argument，总览表格第一列必须链接到章节页；表格内带别名的 wikilink 使用 `[[Argument_BookFolder_Ch01\|第1章 章节标题]]`，避免 Markdown 表格被竖线拆列。
- 每章固定按“概念地图 → 章节内容 → 关键引用”组织。概念地图通常也可以先占位。
- 章节内容按教科书自身思路整理，不强行套固定小标题；根据材料自然使用通用 callout。
- 图表、案例、练习和表格应说明“它帮助读者理解什么”，不要只粘贴材料。
- 关键引用只保留有启发、表述精炼或可作为条目定义来源的句子；没有页码时只标注章节，不编造页码。

Edited volume overview 常用位置：

| 位置 | 推荐 callout |
|---|---|
| 编著定位 | `[!volume-profile]` |
| 编者问题与组织主张 | `[!question]`、`[!volume-argument]`、`[!citation-card]` |
| 全书结构与章节路线 | `[!volume-structure]`、`[!volume-map]` |
| 理论、方法与关键词 | `[!volume-tools]`、`[!frames-ref]` |
| 跨章主题线索 | `[!cross-chapter]` |
| 章节处理路线 | `[!chapter-roadmap]` |
| 各章概览 | `[!chapter-index]`、`[!evidence-grid-a]` |
| 整体贡献与使用边界 | `[!volume-contribution]`、`[!volume-limits]` |

注意：

- Edited volume overview 是导航入口，不是单章论证替代品；完整论证、方法、发现和引用回到章节 Argument。
- `[!volume-profile]` 要说明材料边界。只读过前言、导论或部分章节时，必须让读者知道 overview 的判断依据。
- `[!volume-structure]` 优先用分部分列表说明推进关系；只有目录信息非常规则时才使用表格。
- `[!volume-map]` 只显示全书组织逻辑，优先用 Mermaid，节点保持短句。
- `[!cross-chapter]` 用于横向阅读线索，不重复目录；每条线索都要说明哪些章节应放在一起读以及为什么。
- `[!chapter-roadmap]` 是工作流模块，帮助持续拆分章节；正式成熟 overview 可以保留，也可以在章节全部处理后压缩。
- `[!chapter-index]` 只写一句话导航，不展开章节论证链。
- `[!volume-limits]` 必须提醒 overview 不能默认代表章节作者观点，也不能默认等同系统综述。

Fact 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 背景 | Event 用 `[!event-context]`；Policy 用 `[!policy-context]` |
| 经过 / 时间线 | `[!timeline]`、`[!phase]`、`[!dev-timeline]` |
| 关键文件 / 政策文本 | `[!claim]`、`[!citation-card]`、`[!quote]` |
| 实施情况 | `[!actor-grid]`、`[!pathways]`、`[!policy-design]`、`[!decisions]`、`[!ref-table]` |
| 影响 / 效果 | `[!indicators]`、`[!finding-cards]`、`[!stat-cards]`、`[!lessons]` |
| 争议与评论 | `[!actor-grid]`、`[!tension]`、`[!citation-card]`、`[!critique]`、`[!warning]` |
| 相关条目 | `[!ref-table]` |

注意：

- Event 的 `## 经过` 简单时用 `[!timeline]`；节点多、阶段差异明显或有多轮转折时，用 `[!phase]` 或 `[!dev-timeline]` 分阶段。
- Event 的 `## 背景` 优先使用 `[!event-context]`，用短列表交代时间地点、关键主体、制度背景和触发条件；不要写成泛泛历史介绍。
- Policy 的 `## 背景` 优先使用 `[!policy-context]`，用短列表交代发布时间、发布主体、适用对象、政策问题和制度位置。
- Policy 的 `## 政策文本摘要` 可用 `[!policy-design]` 拆政策目标、对象、工具和约束方式；该 callout 固定为 2×2 四格，移动端单列；`## 效果与评价` 可用 `[!indicators]` 先说明评价指标。
- Event 的 `## 争议与评论` 优先区分评论视角，而不是只写正反两方；可用 `[!actor-grid]` 记录当事方、制度、学术、公共或媒体视角。
- `[!tension]` 用于整理争议焦点；`[!citation-card]` 用于保留有代表性的评论原文或译文，视觉上与关键文件或声明保持一致；`[!critique-*]` 只在评论明确针对方法、逻辑或数据时使用。

## Citation Cards

关键引用优先使用 `[!citation-card]` 或 `[!quote]`。

外文材料：

```markdown
> [!citation-card] 引用标题
> 中文译文。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
>
> Original text.
```

中文材料：

```markdown
> [!citation-card] 引用标题
> 中文原文。[[Argument_Author_Year_Journal|(作者, 年份, p. X)]]
>
> English translation.
```

不要只写中文意译；重要逐字引用必须保留原文。
