# Callouts

本文件定义 `wiki/templates/` 使用的 callout 语义和 CSS contract。具体视觉样式由 `.obsidian/snippets/argument-callouts.css` 提供；本文件只规定"什么时候用哪一种"。

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

---

## Core Callouts

通用 callout，所有页面类型均可使用。

| Callout | 用途 |
|---|---|
| `[!info]` | 定义、背景、方法说明、前提条件 |
| `[!abstract]` | 核心主张摘要、理论框架、政策摘要、章节结构 |
| `[!question]` | 研究问题、经验谜题、核心关切 |
| `[!claim]` | 核心主张、局部命题、论证步骤中的可争辩判断；必须写可争辩判断，不写材料描述 |
| `[!warrant]` | 证据与主张之间的推理桥梁；必须解释"为什么证据能支持主张"，不重复证据 |
| `[!implication]` | 发现、命题或论证的理论、方法和实践后果；用于收束意义 |
| `[!concept-lens]` | 概念的含义、用途和边界三联透镜 |
| `[!success]` | 主要发现、影响、效果 |
| `[!warning]` | 局限、风险、重要例外；只写原文明确自述的内容 |
| `[!tip]` | 理论提示、相关理论、可迁移经验 |
| `[!quote]` | 原文引用或双语关键引用 |
| `[!example]` | 案例、教育情境例子、图表占位 |
| `[!note]-` | 可折叠补充说明 |
| `[!tension]` | 理论张力、对立立场、规范冲突、争议焦点 |
| `[!citation-card]-` | 关键引用，中文译文 + 原文；每节最多 1–2 个，优先集中到页面后部 |
| `[!entry-map]` | 条目关联表，三列：条目 / 类型 / 关系；只写有真实关联的行 |

---

## Argument Callouts

用于 Argument 页面的论证结构和数据展示。

| Callout | 用途 |
|---|---|
| `[!stat-cards]` | 样本量、比例、效应量、关键数字 |
| `[!effect-table]-` | 效应量汇总表，8 列：研究 / 样本 / 前测 / 后测 / d / SE / CI / 结论；适合量化综述 |
| `[!ma-table]-` | 元分析汇总表，7 列：研究 / N / d / SE / 95%CI / Q / 结论 |
| `[!finding-cards]` | 不超过四条核心发现；超过 4 条时改用小节或证据网格 |
| `[!framework-table]` | 理论镜头、概念工具箱；通常 2 列：工具 / 用法 |
| `[!method-panel]` | 研究设计、材料处理、分析策略；通常 2 列：环节 / 说明 |
| `[!sample-panel]` | 样本构成、材料快照、访谈信息；通常 2 列：维度 / 信息 |
| `[!logic-map]` | Mermaid 论证图、机制图、因果链；节点标签不使用 `\n` |
| `[!line-a]` | 蓝色自动编号线索框（A → B → C…），连续使用时序号自动递增；适合并列证据链或递进命题 |
| `[!line-b]` | 红色对照线索框，紧接 `[!line-a]` 使用，两者上下拼合形成对比结构；不单独出现 |
| `[!chain-link]` | 独立"证据到分析结论"链节，各块内容应自足；可用 2–3 列拆"证据 / 推理 / 结论" |
| `[!evidence-grid]` | 多点并列证据；列表或表格均可 |
| `[!evidence-grid-a]` | 第一组主题证据，常与 `[!evidence-grid-b]` 对照 |
| `[!evidence-grid-b]` | 第二组主题证据，常与 `[!evidence-grid-a]` 对照 |
| `[!contrast-table]` | 概念辨析、案例对比、理论路径对比；2–4 列，多维比较；必须有明确比较维度 |
| `[!ref-table]` | 参考速查表；通常 3 列：对象 / 说明 / 来源；用于查阅，不承担论证推进 |
| `[!meta-table]` | 元分析或研究综述表；固定 5 列：研究 / 纳入 / N / d / 结论；不要挪作普通参考表 |
| `[!pathways]` | 行动路径、实践建议、操作化方案 |
| `[!conclusion]` | 论证结论或批评裁定 |
| `[!voice]` | 边缘声音、访谈引述、立场陈述 |
| `[!case]` | 独立政策或实证案例 |
| `[!event-context]` | Event 背景档案，2 列卡片网格；固定写时间地点、关键主体、制度背景、触发条件 |
| `[!policy-context]` | Policy 背景档案，2 列卡片网格；固定写发布主体、适用对象、政策问题、制度位置 |
| `[!policy-design]` | Policy 设计 2×2 格；固定为目标、对象、工具、约束方式 |
| `[!prop-table]-` | 行动者属性表；列：行动者 / 资源类型 / 核心利益 / 立场 / 策略 |

---

## Concept and Theory Callouts

| Callout | 用途 |
|---|---|
| `[!def]` | 概念定义，适合突出核心定义和边界 |
| `[!term]` | 术语说明，适合短定义或名称辨析 |
| `[!boundary]` | 概念边界、适用范围、排除条件 |
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
| `[!frames-ref]` | 固定数量的框架、原则或要点，适合 6–12 项；最后一项奇数时自动满行 |
| `[!quad-grid]` | 恰好 4 项且权重相当的类型、案例或框架 |
| `[!actor-grid]` | 行动者或利益相关者 2×2 网格 |
| `[!col-l]` + `[!col-r]` | 父 callout 内两个并列子主题 |
| `[!theory-position]` | 理论定位四格，固定写解释对象、理论问题、理论类型和知识位置 |
| `[!proposition-chain]` | 核心命题链，按前提 → 机制 → 条件 → 结果组织；命题之间应有推理方向 |
| `[!mechanism-map]` | 理论机制图，优先放 Mermaid；图后仍要用 `[!proposition-chain]` 或散文解释 |
| `[!theory-components]` | 理论构件，说明关键概念、分类、机制或方法在理论中的功能 |
| `[!theory-stance]` | 认识论与方法含义；必须写"不能直接推出的东西" |
| `[!theory-use]` | 理论使用方式，说明如何作为框架、工具、批判视角和报告逻辑 |
| `[!theory-boundary]` | 理论适用边界，固定写适合、谨慎、不适合和常见误用 |

---

## Method Callouts

| Callout | 用途 |
|---|---|
| `[!proc]` | 标准操作程序、研究步骤链、方法执行流程 |
| `[!method-scope]` | Method 范围四格，固定为研究对象、问题类型、分析单位、输出形式 |
| `[!method-position]` | Method 的认识论定位、研究者角色、有效性标准和不能回答的问题 |
| `[!method-stack]` | Method 层级结构，适合研究设计、数据收集、分析方法和辅助技术 |
| `[!method-fit]` | Method 适用判断三格，固定为适合、谨慎、不适合 |
| `[!formula]` | 单个核心公式展示框；内容用等宽字体，变量用 `**bold**` 标注 |
| `[!formula-step]` | 一个公式步骤，固定写公式、数学解释、结果解读和注意事项 |
| `[!formula-set]` | 多公式链总览，优先放 Mermaid 流程图，不放大公式表 |
| `[!math-principle]` | 公式的数学直觉、关键性质和隐含假设；不重复变量定义 |
| `[!result-reading]` | 量化结果的正确解读、报告方式和常见误读；必须区分"能说明什么"和"不能说明什么" |
| `[!software-impl]` | 软件实现、核心包/命令、复现步骤和报告标准 |
| `[!method-limits]` | 方法局限、参数边界、权重敏感性、阈值风险和误用提醒 |
| `[!critique]` | 通用学术批评 |
| `[!critique-method]` | 方法论或统计错误（钢蓝） |
| `[!critique-logic]` | 逻辑或概念矛盾（紫） |
| `[!critique-data]` | 实证或数据反例（琥珀） |
| `[!critique-fatal]` | 根本性缺陷（深红，左边框加宽） |

注意：

- `[!formula-step]` 固定顺序：公式 → 这个公式在做什么 → 数学直觉 → 嵌套 `[!result-reading]` → 嵌套 `[!method-limits]` 或 `[!warning]`。
- `[!formula]` 适合一个独立核心公式；`[!formula-set]` 只作总览，不替代逐个 `[!formula-step]`。
- `[!result-reading]` 描述性指数、分类结果、空间相关和预测结果不得直接写成因果效果。

---

## Person Callouts

| Callout | 用途 |
|---|---|
| `[!person-profile]` | 人物档案三格，固定写身份位置、核心角色、代表贡献（末格满行） |
| `[!work-line]` | 主要著作线，按年份说明著作的问题意识、核心贡献和思想转向 |
| `[!thought-timeline]` | 思想发展时间线，按阶段说明代表著作、关键概念／方法和阶段转向 |
| `[!influence-path]` | 影响路径，区分理论、方法、政策和跨国／跨领域传播 |
| `[!person-network]` | 关系网络，记录师承、合作、继承、批评、机构或运动关系 |

注意：

- `[!work-line]` 与 `[!thought-timeline]` 二选一；资料不足时降级为 `[!work-line]`，不强行分期。
- `[!person-network]` 只收录能解释思想、影响或争议的关系。

---

## Book Callouts

### Textbook

| Callout | 用途 |
|---|---|
| `[!textbook-overview]` | 教材章节总览表，列出章节链接、内容概要和主要关联条目 |
| `[!knowledge-map]` | 教材总览知识地图或章节概念地图；通常先放图片占位 |

### Monograph

| Callout | 用途 |
|---|---|
| `[!monograph-profile]` | 专著档案，固定写核心对象、论证类型、处理粒度和材料边界 |
| `[!monograph-thesis]` | 全书核心主张，区分问题起点、核心解释和最终贡献 |
| `[!monograph-tools]` | 专著理论与概念工具，只写贯穿全书的工具 |
| `[!monograph-method]` | 专著研究方法与材料，必须写方法边界 |
| `[!book-argument-map]` | 全书论证图，优先放 Mermaid |
| `[!argument-steps]` | 全书论证步骤，按问题 → 工具 → 前提 → 证据 → 推论 → 结论 → 谨慎处组织 |
| `[!chapter-arc]` | 章节推进线，强调各章如何推进全书论证，不重复目录 |
| `[!chapter-index]` | 章节索引卡片网格，只写一句话导航 |
| `[!book-synthesis]` | 跨章综合，只写跨章节才成立的判断 |
| `[!book-limits]` | 专著自述局限与使用边界 |

### Edited Volume

| Callout | 用途 |
|---|---|
| `[!volume-profile]` | 编著档案，固定写核心议题、材料边界、章节关系和使用方式 |
| `[!volume-argument]` | 编者组织主张，区分共同问题、组织逻辑和整体贡献 |
| `[!volume-structure]` | 全书结构，按部分或章节组说明推进关系 |
| `[!volume-map]` | 编著结构图，优先放图片占位；无扫描图时改用 Mermaid |
| `[!volume-tools]` | 编著理论、方法与关键词工具箱 |
| `[!cross-chapter]` | 跨章主题线索，每条线索说明哪些章节应放在一起读及原因 |
| `[!chapter-roadmap]` | 章节处理路线，说明已处理、优先处理、可暂缓和缺口 |
| `[!volume-contribution]` | 编著整体贡献，说明研究议题、理论方法和资料价值 |
| `[!volume-limits]` | 编著使用边界，提醒 overview 不能替代单章论证或系统综述 |

---

## Evaluation Callouts

| Callout | 用途 |
|---|---|
| `[!strength]` | SWOT 优势（绿） |
| `[!weakness]` | SWOT 劣势（红） |
| `[!opportunity]` | SWOT 机会（蓝） |
| `[!threat]` | SWOT 威胁（琥珀） |
| `[!indicators]` | 评价指标体系，三层：投入 / 过程 / 结果 |
| `[!lessons]` | 案例分析后的经验、启示或教训；自动编号 |

四个 SWOT callout 拼合时自动对齐为 2×2 网格（每个 callout 内部各自是 2×2 li 网格）。

---

## Citation Cards

关键引用优先使用 `[!citation-card]-`（可折叠）。

外文材料：

```markdown
> [!citation-card]- 引用主题
> 中文译文。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
>
> *Original text.*
```

中文材料：

```markdown
> [!citation-card]- 引用主题
> 中文原文。[[Argument_Author_Year_Journal|(作者, 年份, p. X)]]
>
> *English translation.*
```

不要只写中文意译；重要逐字引用必须保留原文。英文原文使用斜体。
