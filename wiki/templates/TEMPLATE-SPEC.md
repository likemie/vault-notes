# Template Spec

本文件是 `wiki/templates/` 的主规范入口。AI 新建或重写条目时最多读取三类文件：

1. `wiki/templates/TEMPLATE-SPEC.md`
2. `wiki/templates/CALLOUTS.md`
3. 对应的 `wiki/templates/template-*.md`

模板文件只决定可插入的页面骨架；本文件决定字段、写作、来源和类型结构规则。若模板与本文件冲突，以本文件为准。

---

## Universal Rules

- 正文使用简体中文；文件名、文件夹名、`title`、`tags` 使用英文。
- 正文先按主题、概念层级或论证功能组织，再在主题内部按时间、发展阶段或论证顺序排列。
- 修改已有条目时，先判断归属章节、子主题和插入位置，再精确替换相关段落，不重写整个文件。
- 分点少于 8 条时按模板逻辑或论证顺序排列；分点达到 8 条或以上时建立 `###` 子主题，组内再按时间或论证顺序排列。
- 有内容才保留章节；没有材料支持的空章节可以删除。
- 正式条目正文不要保留模板里的说明注释。
- 不使用来源以外的知识；资料不足时写“待核”或不写该判断。

---

## Language Rules

- 句子主体使用中文表达。除专名、引文、公式、代码、APA citation 和无法翻译的固定术语外，避免中英混合。
- 人名第一次出现必须使用全名；中文正文优先写成中文全名（英文全名），后文可按语境使用中文名、姓氏或代称。
- 缩写第一次出现必须写成中文（英文全称，缩写）；后文才可单独使用缩写。
- 术语首次出现使用中文（English）格式；如果该术语有缩写，使用中文（English Full Name，ABBR）格式。
- 少用破折号和冒号，优先用短句、逗号或句号。
- 少用“不是/并非……而是……”句式。只有纠正常见误解时才使用；普通说明直接写正面判断。
- 删除没有信息量的元话语，保留具体判断、机制、证据或例子。
- 理论或哲学内容不能只堆定义；抽象主张后应有例子或说明。

---

## Frontmatter Rules

- `summary` 只用于索引说明，不是摘要。
- `summary` 外层必须使用双引号包裹。
- `summary` 内部避开英文冒号 `:`、双引号 `"`、单引号 `'`；需要断句时优先使用中文标点。
- `tags` 用方括号列表，内容使用英文小写连字符。
- `related_*` 由 `scripts/wiki_relations.py` 自动维护，AI 不手动填写。
- `related_*` 若引用条目，必须写成带引号的 wikilink，例如 `"[[Cultural Capital]]"`。
- 新建 Concept / Theory / Method / Fact / Person 默认不写 YAML `sources`，也不写正文 `## 来源`。
- Argument YAML `sources` 由脚本维护；正文 `## 来源` 只列 source record wikilink。
- Argument 不使用 `aliases`；Concept / Theory / Method / Fact / Person 使用 `aliases` 作为检索和自动补链白名单。
- `related_*`、Argument YAML `sources`、source record 的 `extracted_to` 都是生成字段，不手动维护。
- `part_of` 若引用条目，必须写成带引号的 wikilink。

---

## Source and Citation Rules

- 来源性陈述优先链接到已处理 Argument，而不是直接链接 source record。
- 非 Argument 条目引用来源时使用 APA 短引用链接到 Argument，例如 `[[Argument_Thomas_2000_RER|(Thomas, 2000, p. 4)]]`。
- 叙述式引用写作 `[[Argument_Thomas_2000_RER|Thomas (2000, p. 4)]]`。
- Argument 条目引用当前对应文献时只写页码，例如（p.147）或（pp.147–148）。
- Argument 条目引用当前文献之外的已处理文献时，使用 APA 短引用。
- Argument frontmatter 的 `authors` 必须写成 YAML 列表，每位作者单独一项。
- 英文个人作者若使用 Person wikilink，链接显示名必须是 APA 倒置姓名，例如 `"[[Louis Cohen|Cohen, L.]]"` 或 `"[[Cohen, L.]]"`。
- `year` 写出版年份。
- `doi` 可留空；著作、教材或论文集章节若能确认 ISBN，可写入 `isbn`。
- `citation_aliases` 由 `scripts/citation_index.py` 自动生成，AI 不手动维护。
- `citation_aliases` 只保留基本作者年份形式：`Author, Year` 与 `Author (Year)`。
- 不把页码形式写进 `citation_aliases`；页码由 `scripts/citation_linker.py` 在正文补链时动态识别。
- 英文文献按 APA 生成英文 alias：双作者用 `&`，三位及以上用 `et al.`。
- 中文论文或著作若 `citation` 字段含中文作者名，`scripts/citation_index.py` 会额外生成中文 alias，例如 `郑雅君, 2023` 与 `郑雅君 (2023)`；中文双作者用“和”，三位及以上用“等”。
- 同一作者同一年多篇文献时，`scripts/citation_index.py` 自动追加 `a`、`b`、`c` 后缀。
- 正文 APA 短引用补链由 `scripts/citation_linker.py` 完成。
- 处理完成后只自动运行基础索引：`.venv/bin/python3 scripts/vault_index.py`。补链、关系同步和 lint 需要先询问用户。

---

## Editing Rules

- 确定新内容属于哪个 `##` 章节。
- 先判断新内容属于哪个主题、子主题或论证步骤，再判断该主题内部的时间位置或推理位置。
- 写入前声明“归属章节 > 子主题 > 插入位置”，再精确替换相关段落。
- 插入位置优先级：同主题已有段落或列表 → 对应章节末尾 → 新增 `###` 子主题 → 新增模板允许的章节。
- 不要把新内容按出现顺序直接堆到文件末尾。
- 正式条目正文不要写任何模板说明注释。

---

## Type Rules

### Argument

Argument 页写某篇论文、章节、报告、政策文件或书籍的论证结构。`title` 与文件名保持稳定技术命名，不写 APA 短引用；APA 信息写入 `citation` 字段。

推荐结构：

- `## 研究问题`
- `## 理论框架`
- `## 研究方法`
- `## 论证结构`
- `## 主要发现`
- `## 关键引用`
- `## 自述局限`
- `## 来源`

规则：

- `summary` 用一句话说明文献核心论证，写法为“研究对象/问题 + 理论视角/方法 + 核心论证或发现”。
- `summary` 好例子：`从统计学角度审查 Hattie 以效应量排序教学干预的前提，指出 d=0.40 依赖样本量且排名缺少置信区间。`
- 直接陈述论证思路，不让摘要围绕论文、研究或作者展开；无法概括时留空：`summary: ""`。
- `## 论证结构` 中每个步骤独立成段，步骤之间使用 `---`。
- 逐步拆解论证，不跳过中间环节直接给结论。
- 抽象理论必须配例子；例子优先来自原文，原文没有时可用简短教育情境说明。
- `## 论证结构` 顶部可用 Mermaid 图呈现核心逻辑链；图后必须跟 `---` 分割线。
- `## 论证结构` 内根据论文实际论证方式综合运用多种 callout，例如 `[!argument-map]`、`[!claim]`、`[!chain-link]`、`[!warrant]`、`[!line-a]`、`[!contrast-table]`、`[!evidence-grid]`、`[!logic-map]`。
- 需要并列线索时使用 `[!line-a]`；需要对比或结构化展示数据时，使用 `[!contrast-table]`、`[!evidence-grid]`、`[!ref-table]`、`[!meta-table]` 或普通 Markdown 表格。
- `## 主要发现` 不超过四点；三点时按两短一长编排，更多细节放入数据卡、证据卡或正文小节。
- `## 自述局限` 只写原文明确自述的局限、边界条件或未来研究方向，不补写外部批评。
- Argument 主要任务是如实记录论文内容，不默认设置外部评价性的“讨论与批评”章节。
- `## 来源` 只列 source record wikilink；按来源年份从早到晚排序，同一年按作者或机构字母顺序。
- 期刊论文文件名格式：`Argument_作者姓_年份_期刊缩写.md`。
- 论文集章节文件名格式：`Argument_章节作者姓_年份_关键词.md`。
- 报告或政策文件文件名格式：`Argument_机构_年份_Report.md`。

### Edited Volume Overview

Edited volume overview 是论文集或编著的结构入口，不是主要可引用单元。可引用文献以各章 Argument 为主。

推荐结构：

- `## 编者论点`
- `## 全书结构`
- `## 理论框架`
- `## 各章概览`
- `## 来源`

规则：

- 使用 `template-argument-edited-volume.md`。
- `subtype` 使用 `edited-volume-overview`，`publication_type` 使用 `edited-volume`。
- overview 不填写 `citation_aliases`，不进入 citation 索引。
- `summary` 说明论文集的组织问题、编者立场和全书结构，不写成图书简介。
- `## 全书结构` 和 `## 理论框架` 优先使用 `[!framework-table]`。
- `## 各章概览` 只记录章节 Argument 链接和核心贡献。
- `## 来源` 只列 overview source record wikilink。

### Monograph Argument

Monograph Argument 是整本专著的论证入口。章节处理阶段先累积材料，整合阶段再提炼全书论证。

推荐结构：

- `## 研究问题`
- `## 理论框架`
- `## 研究方法`
- `## 论证结构`
- `## 主要发现`
- `## 各章概览`
- `## 关键引用`
- `## 自述局限`
- `## 来源`

规则：

- 使用 `template-argument-monograph.md`。
- `subtype` 使用 `monograph`，`publication_type` 使用 `book`。
- 每章处理结果追加到 `## 各章概览`，不写成完整小型笔记。
- `## 理论框架` 优先使用 `[!framework-table]`；`## 研究方法` 优先使用 `[!method-panel]`；`## 论证结构` 可用 `[!argument-map]` 承载全书论证路径。
- 关键引用持续补充到 `## 关键引用`，标注章节与页码；没有页码时只标注章节，不编造页码。
- 整本书 source record 创建前，可以暂时省略 `## 来源` 的 source wikilink；source record 创建后再补入。
- `summary` 说明全书核心论证，写法为“研究对象/核心问题 + 理论视角/材料 + 全书论证或发现”。

### Textbook Argument

Textbook Argument 记录教材的知识推进结构。具体定义、分类、争议、例子、方法步骤和理论说明优先沉淀到对应 wiki 条目。

固定结构：

- `## 章节结构`
- `## 章节概览`
- `## 重要摘录`
- `## 来源`

规则：

- 使用 `template-argument-textbook.md`。
- `subtype` 使用 `textbook`，`publication_type` 使用 `book`。
- `## 章节结构` 只保留三列：章节、内容概要、主要关联条目。
- `## 章节结构` 优先使用 `[!ref-table]`；`## 章节概览` 每章可用 `[!chapter-question]` 标出本章位置。
- 主要关联条目只列 3–5 个最核心的 Concept / Theory / Method / Fact / Person。
- `## 章节概览` 跟随教材自身知识推进逻辑，记录概念、理论、证据、案例、表格、图片和结论如何展开。
- 已建条目只简单提及，详细内容写入具体条目。
- `## 重要摘录` 只保留有启发或表述精炼的观点，标注章节与页码；没有页码时只标注章节，不编造页码。
- 整本教材 source record 创建前，可以暂时省略 `## 来源` 的 source wikilink；source record 创建后再补入。

### Concept

Concept 页写一个概念、术语、机制、分类或分析对象。它不是某篇论文的摘要，而是跨来源沉淀的知识条目。

推荐结构：

- `## 定义`
- `## 概念辨析`
- `## 核心要素`
- `## 围绕概念形成的命题`
- `## 概念演变`
- `## 实证发现`
- `## 争议与批评`
- `## 应用案例`

规则：

- `summary` 说明概念对象、核心含义和教育研究中的意义。
- `summary` 写法为“对象类型 + 核心含义/贡献 + 教育研究中的意义”。
- 不围绕某一篇论文写摘要，不堆材料细节；无法概括时留空：`summary: ""`。
- `## 定义` 先说明核心含义、适用范围和边界。
- `## 定义` 推荐使用 `[!def]` + `[!concept-lens]` + `[!boundary]`：先给定义，再说明含义、用途和边界。
- `## 概念辨析` 用于区分相近概念；没有相近概念时可省略。
- `## 核心要素` 是 Concept 条目的重点，用于拆解概念包含的构成要素、判断标准、条件和边界。
- `## 核心要素` 可综合使用 `[!feature]`、`[!logic-map]`、`[!taxonomy]`、`[!frames-ref]`、`[!contrast-table]`、`[!ref-table]` 等 callout。
- `## 围绕概念形成的命题` 写可争辩命题，组织机制、条件、结果或分类体系。
- `## 围绕概念形成的命题` 可综合使用 `[!claim]`、`[!warrant]`、`[!implication]`、`[!line-a]`、`[!finding-cards]` 和 `[!logic-map]`。
- `## 概念演变` 写接受史、扩展史、领域迁移或概念转向。
- 概念或框架本身写入 `## 围绕概念形成的命题`、`## 核心框架` 或对应功能章节。
- 特定国家接受史、研究者再诠释写入 `## 概念演变`，不放在核心框架或实施章节。
- 学术体制批评、期刊事件、争议立场写入 `## 争议与批评`，不放在概念发展时间线内。
- 内容少于 3 点时优先用散文；内容足够丰富时再使用 callout，不要为了排版稀释内容。
- 动笔前先识别要素之间的逻辑关系，再决定是否使用 `[!logic-map]`、`[!line-a]` 或 `[!finding-cards]`。
- `## 争议与批评` 根据实际材料选用 callout；没有充分材料时可删除本节。
- `## 实证发现` 和 `## 应用案例` 默认用 callout 承载一句话索引，不展开成完整小节；详细内容回到对应 Argument。
- `[!citation-card]` 或关键逐字引文优先集中到页面后部，不散落在各节。

### Theory

Theory 页写可作为理论框架、解释机制或分析视角的理论、模型或框架。

推荐结构：

- `## 核心主张`
- `## 核心命题`
- `## 发展脉络`
- `## 认识论立场`
- `## 分析框架`
- `## 争议与批评`
- `## 相关研究`
- `## 应用领域`

规则：

- 区分理论的基本立场、解释机制、适用对象和方法论含义。
- `## 核心主张` 使用 `[!claim]`；`## 核心命题` 使用 `[!finding-cards]`、`[!claim]`、`[!warrant]` 或 `[!logic-map]`。
- `## 分析框架` 适合使用 `[!framework-table]`、`[!logic-map]` 或 `[!frames-ref]`；不要把框架写成散乱列表。
- 发展脉络按时间排列，争议与批评按立场或问题分组。
- 相关研究链接到使用该理论的 Argument。

### Method

Method 页写研究方法、研究设计、资料收集方法、分析方法或项目评价方法。

推荐结构：

- `## 定义`
- `## 认识论立场`
- `## 研究程序`
- `## 资料与分析`
- `## 适用场景`
- `## 局限性`
- `## 相关理论`
- `## 使用此方法的研究`

规则：

- 课堂教学法不放 Method，通常放 Concept。
- `method_type` 使用 `qualitative`、`quantitative` 或 `mixed`。
- `## 研究程序` 写可执行步骤；`## 适用场景` 写适合回答的问题类型。
- `## 研究程序` 优先用 `[!proc]`；`## 资料与分析` 优先用 `[!method-panel]`；`## 使用此方法的研究` 默认作为一句话索引。
- 非思辨或评论性文章，至少把一个核心方法案例记录到 `## 使用此方法的研究`，只写一句话索引并链接对应 Argument。

### Fact

Fact 页写事件、政策、项目、组织、制度安排或可核查事实。

推荐结构按 subtype 调整：

- Event：背景、经过、关键文件或声明、影响、争议、相关条目。
- Policy：背景、政策文本、实施机制、效果、争议、相关条目。

规则：

- `region` 必须尽量具体；全球性事实用 `global`，多国比较用 `multi`。
- Event 必须有明确时间、地点和主体；Policy 必须说明出台时间、发布主体、适用地区和制度对象。
- 经过、实施和演变类内容按时间顺序排列。
- 经过和时间线优先使用 `[!timeline]` 或 `[!phase]`；影响、效果和评价优先使用 `[!finding-cards]`、`[!stat-cards]` 或 `[!lessons]`。
- Event 的 `## 争议与评论` 按评论视角和争议焦点组织；不同人或机构的评论可先用 `[!actor-grid]` 区分视角，再用 `[!tension]`、`[!voice]` 或 `[!critique-*]` 展开。
- 相关概念、政策和理论默认使用 `[!ref-table]` 做一句话关系索引。
- 不把理论解释写成事实本身；解释放到对应 Concept / Theory 或 Argument 中。

### Person

Person 页写学者、政策人物或关键行动者的生平、思想、著作和影响。

推荐结构：

- `## 简介`
- `## 生平与职涯`
- `## 主要著作`
- `## 核心思想`
- `## 思想发展`
- `## 影响`
- `## 格言／关键表述`
- `## 争议与批评`

规则：

- `nationality` 按国籍或主要学术归属填写；不明或跨国身份放 `global` 文件夹。
- `aliases` 写中文名、英文全名变体、常见缩写或不同拼写。
- 只有人物有独立理论、概念、框架、学派或持续影响时才建 Person；只是论文作者、顺带引用一次或普通受访者时不建。
- Person 文件名和 `title` 使用常用英文全名；`aliases` 可写 APA 作者名、英文全名变体、中文全称和必要中文简称，不写单独英文姓氏。
- `## 主要著作` 默认使用 `[!ref-table]`；`## 生平与职涯` 和 `## 思想发展` 优先使用 `[!timeline]` 或 `[!phase]`。
- `## 核心思想` 使用 `[!claim]`、`[!concept-lens]` 或 `[!citation-card]`，不与著作列表重复。
- 相关研究链接到讨论此人物或使用其思想的 Argument。
