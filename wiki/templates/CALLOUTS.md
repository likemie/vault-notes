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
| `[!method-fit]` | Method 适用判断三格，固定为适合、谨慎、不适合 |
| `[!formula]` | 单个核心公式、变量表和计算顺序 |
| `[!formula-step]` | 一个公式步骤，固定写公式、数学解释、结果解读和注意事项 |
| `[!formula-set]` | 多公式链总览，只在需要快速索引公式体系时使用 |
| `[!math-principle]` | 公式的数学直觉、关键性质和隐含假设 |
| `[!result-reading]` | 量化结果的正确解读、报告方式和常见误读 |
| `[!software-impl]` | 软件实现、核心包/命令、复现步骤和报告标准 |
| `[!critique]` | 通用学术批评 |
| `[!critique-method]` | 方法论或统计错误 |
| `[!critique-logic]` | 逻辑或概念矛盾 |
| `[!critique-data]` | 实证或数据反例 |
| `[!critique-fatal]` | 根本性缺陷 |

Method 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 定义 | `[!def]`、`[!method-scope]`、`[!citation-card]` |
| 认识论立场 | `[!assumptions]`、`[!axioms]` |
| 研究程序 | `[!proc]`、`[!formula-step]`、`[!method-panel]` |
| 资料与分析 | `[!method-panel]`、`[!sample-panel]`、`[!formula]`、`[!formula-set]`、`[!math-principle]`、`[!result-reading]`、`[!software-impl]` |
| 适用场景 | `[!method-fit]`、`[!decisions]`、`[!pathways]` |
| 局限性 | `[!critique-method]`、`[!warning]` |
| 相关理论 | `[!frames-ref]`、`[!ref-table]` |
| 使用此方法的研究 | 默认用 `[!evidence-grid-a]` 承载一句话索引 |

注意：

- Method 的 `## 定义` 优先用 `[!method-scope]` 固定四格，避免把方法对象、问题类型、分析单位和输出形式混写在同一段。
- Method 的 `## 适用场景` 优先用 `[!method-fit]` 固定三格，分别写适合使用、谨慎使用和不适合使用。
- 量化 Method 面向新手时，优先使用“流程总览 + 多个 `[!formula-step]`”的结构。每个公式步骤只解释一个核心公式，并紧接数学原理和结果读法。
- `[!formula-step]` 固定顺序为：公式 → 这个公式在做什么 → 数学直觉 → 结果怎么读 → 常见误读或注意事项。不要把 4 个以上公式塞进一张大表。
- `[!formula]` 适合一个独立核心公式，公式下方可放简短符号说明；`[!formula-set]` 只作为多公式链总览，不替代逐个公式解释。
- `[!math-principle]` 不重复变量定义，重点写平均、加权、标准化、距离、似然、惩罚、方差分解、空间邻接等数学直觉，以及公式的取值范围、边界条件和隐含假设。
- `[!result-reading]` 必须区分“能说明什么”和“不能说明什么”。描述性指数、分类结果、空间相关和预测结果不得直接写成因果效果。
- `[!software-impl]` 写实际可复现路径，优先包括数据处理、推荐软件、核心包或命令、运行顺序、诊断检查、导出和版本信息。

Theory 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 核心主张 | `[!claim]`、`[!concept-lens]`、`[!citation-card]` |
| 核心命题 | `[!finding-cards]`、`[!claim]`、`[!warrant]`、`[!logic-map]` |
| 发展脉络 | `[!timeline]`、`[!phase]`、`[!dev-timeline]` |
| 认识论立场 | `[!assumptions]`、`[!axioms]` |
| 分析框架 | `[!framework-table]`、`[!logic-map]`、`[!frames-ref]` |
| 争议与批评 | `[!tension]`、`[!critique]`、`[!critique-method]`、`[!critique-logic]`、`[!critique-data]` |
| 相关研究 | 默认用 `[!evidence-grid-a]` 承载一句话索引 |
| 应用领域 | 默认用 `[!case]` 承载一句话索引 |

---

## Book and Evaluation Callouts

| Callout | 用途 |
|---|---|
| `[!chapter-question]` | 章节研究问题或章节在全书论证中的位置 |
| `[!strength]` | SWOT 或评价中的优势 |
| `[!weakness]` | SWOT 或评价中的劣势 |
| `[!opportunity]` | SWOT 或评价中的机会 |
| `[!threat]` | SWOT 或评价中的威胁 |
| `[!indicators]` | 评价指标体系或分层指标 |
| `[!lessons]` | 案例分析后的经验、启示或教训 |

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

Person 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 简介 | `[!abstract]`、`[!concept-lens]` |
| 生平与职涯 | `[!timeline]`、`[!phase]` |
| 主要著作 | `[!ref-table]` |
| 核心思想 | `[!claim]`、`[!concept-lens]`、`[!citation-card]` |
| 思想发展 | `[!phase]`、`[!timeline]`、`[!dev-timeline]` |
| 影响 | `[!evidence-grid-a]`、`[!case]`、`[!ref-table]` |
| 争议与批评 | `[!critique]`、`[!tension]`、`[!warning]` |

---

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
