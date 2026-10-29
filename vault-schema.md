# Vault Schema

本文件只保留 AI / Claude Code 处理 Obsidian vault 时必须遵守的规则。模板规范以 `wiki/templates/TEMPLATE-SPEC.md` 与 `wiki/templates/CALLOUTS.md` 为入口；具体页面骨架以 `wiki/templates/` 中对应模板为准；脚本实现细节以 `scripts/` 为准。

---

## 1. Core Principles

- 只读取当前任务需要的文件，避免扫描无关文件夹。
- 先根据材料判断需要建立或更新哪些知识对象，再读 `wiki/index.json` 检索候选条目是否已存在。
- `wiki/index.json`、`wiki/index.md` 和各类型索引页由 `scripts/wiki_index.py` 自动生成，不手动维护。不手动维护生成字段：`related_*`、Argument YAML `sources`、source record 的 `extracted_to`。Source 记录与阅读页面由 `scripts/source_record.py` 生成。
- 修改已有条目必须先读取文件，判断目标章节、子主题与插入位置，再使用 `str_replace` 精确替换相关段落，不重写整个文件。
- 期刊 Argument 不记录本篇自引，不写作者与年份，也不写指向本篇的页码。书籍、教材、论文集章节和报告引用当前文献时只写页码，如（pp.147–148）。其他条目按 APA 格式引用。非 Argument 条目不写 YAML `sources` 和正文 `## 来源`；
- “相关研究索引”中，只有同一本专著或教材的分章节 Argument 合并为一个顶层来源条目；论文集章节按各章作者与独立论证分别列出，不合并，也不用论文集 overview 替代章节证据。每个顶层索引条目只写一句话，可见文字不超过 150 个字符；脚本只提醒超限，不自动压缩正文。
- 不使用来源以外的知识；

- 普通论文 / 报告 source record 使用最终 `<论文命名>` 创建；完整 citation 在 Argument 页完成后由 `source_record.py finalize` 回填。若文献包含需要保留占位的 figure，`finalize` 时使用 `--with-figures` 生成 `sources/<论文命名>/figures/`。
- 新建、移动、删除、重命名条目后，自动运行基础索引：`vault_index.py`（先刷新引用索引，再修复格式与引用链接、维护书籍 overview 章节表格、更新日期与关联派生字段，最后刷新 wiki 索引）。是否继续运行 citation 补链、普通 wiki 补链、关系同步与 Concept 派生字段同步，由用户确认。
- 任何修改了 vault 文件的任务，结束前必须依次运行 `vault_index.py` 与 `vault_lint.py`（增量）。`vault_index.py` 会先对改动过的文件自动完成机械性修复（见第 5 节），lint 只报告需要判断的问题。必须解决全部 ERROR，以及本次改动新引入的全部 WARN（增量 lint 隐藏 HEAD 已有的普通警告；未审查的写作用词与句式命中始终列出）；确属合理保留的警告须在回复中说明理由。lint 报告 0 error 且无未处理的新警告才算完成。本地不设 pre-commit 钩子，lint 是唯一的本地门禁。
- 非必要不要运行 `--full`。优先使用 git 增量或路径限定；只有批量重命名/移动/删除、批量 title/alias/citation 字段变更、增量结果异常、发布/备份/重要提交前，才使用 full sync 或 full lint。

---

## 2. Workflow

### 普通论文／报告

1. 读取 `vault-schema.md`；若用户明确说明是专著、论文集或教材，转入 `Specialized Schemas`；若用户未说明类型，按普通论文／期刊论文流程处理。
2. 读取原始文件并提取可读文本。
3. 扫描文献，同时判断二类事项：需要建立或更新哪些知识对象，是否包含需要占位的 figure。
4. 在创建 Argument 页之前确定最终 Argument 文件名，并由此确定最终 `<论文命名>`；期刊论文先读取 `citation/journals.json`，按期刊全名取唯一代码，不自行猜缩写。新期刊先用 `citation_index.py --register-journal "<期刊全名>" <代码>` 登记。Argument 页正文 `## 来源` 可先写 `[[<论文命名>]]`。
5. 为每个候选知识对象记录暂定英文标题、中文术语或别名、类型、目标二级文件夹和独立成条理由。
6. 读取 `wiki/index.json`，用标题、中文术语、英文变体和缩写检索是否已有。
7. 将候选分为待更新和待新建。
8. 更新已有条目：读取文件 → 判断目标章节、子主题与插入位置 → 先按主题归组，再在主题内按时间或论证顺序整合 → 用 `str_replace` 精确替换相关段落。
9. 新建条目：读取 `wiki/templates/TEMPLATE-SPEC.md`、`wiki/templates/CALLOUTS.md` 和对应 `wiki/templates/template-*.md` → 按模板逻辑组织内容，先主题后时间；同时记录该条目应回链到当前 Argument 的哪个论证段落。
10. 判断研究方法，除非是思辨类或评论文章，更新或新建至少一个 Method 条目，在 `## 使用此方法的研究` 加入一条方法案例，并链接当前 Argument。
11. 创建或更新 Argument 页，frontmatter 按 `template-argument.md` 写入必要字段，正文 `## 来源` 使用相对于 vault 根目录的完整路径列出 `[[sources/<论文命名>|<论文命名>]]`；书籍来源使用 `[[books/<书籍目录>/<来源记录>|<来源记录>]]`。若有 figure，在对应论证位置写图片占位，图片路径使用第 4 步确定的最终 `<论文命名>`。本任务新建的每个 Concept / Theory / Method / Instrument / Fact / Person 都必须在 Argument 正文的相关论证段落中至少出现一次 wikilink。
12. 用最终 `<论文命名>` 创建 source record：期刊论文用 `source_record.py article --record-name <论文命名> --journal "<期刊全名>"`；政策、报告、白皮书用 `source_record.py report --record-name <论文命名>`。
13. 运行 `source_record.py finalize --argument <Argument路径> --rename`，回填 citation；若第 3 步判断有图片占位，则加 `--with-figures`，生成 `sources/<论文命名>/`、`sources/<论文命名>/<论文命名>.md`、`sources/<论文命名>/<论文命名>.pdf` 和 `sources/<论文命名>/figures/`。
14. 自动运行基础索引：`.venv/bin/python3 scripts/vault_index.py`。
15. 询问用户是否继续运行标准脚本流程。



### Specialized Schemas

AI 不主动判断书籍材料属于专著、论文集还是教材；按用户指令选择对应 schema。若用户未说明类型，按普通论文／期刊论文流程处理。

| 用户指令 | 读取文件 |
|---|---|
| 用户说明「专著」/「著作」 | `schema/schema-monograph.md` |
| 用户说明「论文集」/「编著」 | `schema/schema-edited-volume.md` |
| 用户说明「教材」/「教科书」/「课程用书」/「入门读本」 | `schema/schema-textbook.md` |

书籍任务每次只处理一章或用户当前指定章节，处理完停止。专著和教材的 Argument 粒度按用户指定：整本书一个 Argument，或全书 overview + 分章节 Argument。专著处理流程不区分 PDF 与 EPUB，但最后创建 source 记录和阅读页面时按文件格式分支；EPUB 阅读页使用已配置的 epub.js 静态脚本。教材仍放在 `books/` 和 `wiki/arguments/books/<book-folder>/`。

### Figure 和 Table 处理

适用于普通论文、报告、专著、论文集和教材。

- Figure 指图、模型图、流程图、照片、示意图等非表格图像。figure 写图片占位。
- Table 指作者标为 table 的材料，也包括截图表格和扫描表格。table 只要可读，就必须复刻为 Markdown 表格；只有完全无法读取时才写图片占位。
  - **表格内双链转义**：表格表头与单元格内的别名双链必须对竖线进行转义，写作 `[[Target\|Alias]]`，严禁写成 `[[Target|Alias]]`；未转义的 `|` 会被 Markdown 解析器识别为列分隔符，导致单元格被截断、多出空列或列数错位，破坏表格排版。无需别名时直接写 `[[Target]]`。
  - **表格 Callout 匹配**：必须根据表格结构选用 `CALLOUTS.md` 对应的专用 callout（如文献横向多行对比选用 `[!row-contrast]`，变量操作化选用 `[!coding-frame]`，元分析合并效应选用 `[!effect-summary]`，调节效应选用 `[!moderator-summary]` 等）；严禁将多列对比表套入通常仅 2 列且在 CSS 中默认隐藏表头的 `[!framework-table]`，以免表头丢失。
- 占位跟随正文叙述放在最相关段落之后，不堆在开头；使用 Markdown 嵌入 `![](...jpg)`，不要包在任何注释中；可见标题使用图号和图名。
- Figure 或无法读取的 table 主要服务于文献整体论证时，放在当前 Argument 的对应位置；主要服务于具体 Concept / Theory / Method / Instrument / Fact / Person 时，放在对应条目中，并在 Argument 页简要提及或链接该条目。
- 普通论文／报告若需要图片占位或后续补图，最终 source record、本地 PDF 和 figures 目录应放入 `sources/<论文命名>/`；无图时仍可保持 `sources/<论文命名>.md` 和 `sources/<论文命名>.pdf` 的扁平结构。PDF 本地副本不进 git，发布页使用 NAS URL。

普通论文／报告 figure 占位：

```markdown
> [!figure]- 图X：名称
> ![](https://img.mylikemie.icu/sources/<论文命名>/figures/<论文命名>_FigX_Descriptive_Name.jpg)
```

说明：`<论文命名>` 由 AI 在创建 Argument 文件名前确定，通常等于最终 Argument 文件名去掉 `Argument_` 后的部分，如 `Argument_Simpson_2019_ERE.md` 对应 `Simpson_2019_ERE`。命名前要先判断是否有需要保留占位的 figure 或无法读取的 table；需要占位时使用 `source_record.py finalize --rename --with-figures`，让 source record、本地 PDF 和 `figures/` 落入 `sources/<论文命名>/`，并在 source record 中生成对应 NAS iframe。

书籍 figure 占位：

```markdown
> [!figure]- 图X-X：名称
> ![](https://img.mylikemie.icu/books/<book-folder>/figures/Figure_X-X_Descriptive_Name.jpg)
```

### Sync Decision

脚本流程统一见第 5 节。普通任务完成后运行基础索引与增量 lint 并清零 ERROR；是否继续补链、同步关系由用户确认。

---

## 3. Folder Structure and Entry Types

```text
raw/                         待处理原始文献，不编辑
sources/                     已处理论文／报告 source 记录、PDF 与可选配套文件夹
books/                       书籍工作区
schema/                      专项工作流 schema，按任务触发读取
  schema-edited-volume.md
  schema-monograph.md
  schema-textbook.md
scripts/
  vault_index.py              基础维护统一入口
  vaultlib.py                 各脚本共用的基础函数（frontmatter、YAML 引号、wikilink、git、JSON）；公共逻辑只写在这里
  wiki_index.py               wiki 索引与机构登记表 wiki/organizations.json
  citation_index.py           Argument 引用索引与库外短引用索引
  wiki_linker.py
  wiki_relations.py
  vault_lint.py
  effect_table.py             vault_lint 使用的效应量表格解析
  source_record.py
  related_update.py           相关研究分批更新任务
  metax_sync.py
  eef_sync.py
citation/
  journals.json              AI 命名用期刊全名到唯一代码的最小注册表
  citation_full.json          可引用 Argument 的全量索引
  citation_ambiguous.json     同作者同年歧义组（含 APA 7 区分建议）与库外作者年份撞车
  external_identities.json    条目正文中的库外短引用，可手填 doi、isbn 或篇名
  citation_external.json      库外短引用生成索引；同一作者同一年多篇时分配 a/b/c
datasets/                    外部证据数据集（不进 wiki、不补链）；原始导出放 raw/<数据集>/
  metax/                      Visible Learning MetaX（同步：scripts/metax_sync.py；原始：raw/MetaX/）
    metax.json                studies（书目与匹配状态）+ influences（总览、明细行、挂载条目）
    zh.json                   因素名、领域、子领域、影响判定的中文译名与评级
    mapping.json              因素到条目的映射（人工审定）
    errata.json               单篇／整合勘误，须有来源
    reports/                  审核与诊断输出：MetaX 映射审核.md、audit.json（疑似数据错误线索，不是勘误）
  eef/                        EEF 教与学工具包与早期教育工具包（同步：scripts/eef_sync.py；原始：raw/EEF/）
    eef.json                  strands（评级、合并结果、研究列表、挂载条目）
    errata.json               勘误，须有来源
wiki/
  index.json                  AI / Claude Code 检索用极简机器索引
  index.md                    Quartz 4 / Obsidian / GitHub 可读静态索引
  templates/                  AI / Claude Code 与 Obsidian Templater 共用条目模板
    TEMPLATE-SPEC.md          模板字段、写作、来源和类型结构主规范
    CALLOUTS.md               callout 语义和 CSS contract
  concepts/<field>/
  theories/<field>/
  methods/qualitative/
  methods/quantitative/
  methods/mixed/
  instruments/tests/
  instruments/scales/
  instruments/questionnaires/
  instruments/inventories/
  instruments/rubrics/
  instruments/checklists/
  instruments/observation-tools/
  instruments/interview-tools/
  persons/<nationality-or-region>/
  facts/<region>/
  arguments/journal-articles/<journal-name>/
  arguments/books/<book-folder>/
  arguments/reports-policy-documents/
```

| 条目类型 | 路径 | 归类规则 |
|---|---|---|
| Concept | `wiki/concepts/<field>/` | 按领域，如 `comparative-education`、`curriculum`、`educational-philosophy`、`educational-leadership-administration` |
| Theory | `wiki/theories/<field>/` | 只放可作为理论框架、解释机制或分析视角的理论／框架／模型 |
| Method | `wiki/methods/qualitative/`、`quantitative/`、`mixed/` | 放研究方法、研究设计、资料收集／分析方法、项目评价方法，以及测度指标与指数、统计量、统计与计量模型、综合评价模型；课堂教学法放 Concept；判断规则见下方“条目类型判断” |
| Instrument | `wiki/instruments/<instrument-type>/` | 放命名量表、问卷、测验、清单、评分规程、观察工具和访谈工具。标准子目录为 `tests/`（最高表现测验）、`scales/`（典型表现量表）、`questionnaires/`（事实与经历问卷）、`inventories/`（倾向清单/存表）、`rubrics/`（表现评价量规）、`checklists/`（方法学质评核查表）、`observation-tools/`（观察编码规程）、`interview-tools/`（访谈与焦点小组指南）；构念放 Concept，通用程序放 Method |
| Person | `wiki/persons/<nationality-or-region>/`、`wiki/persons/schools/` | 按国籍／地区；不明或跨国身份放 `global`；学术流派／学派放 `schools`（使用学派模板） |
| Fact | `wiki/facts/<region>/` | 按地区；全球性放 `global`；多国比较放 `multi`；`subtype` 固定为 `policy`（政策法案）、`event`（历史事件）、`organization`（组织机构）、`program`（重大项目）四大标准类别 |
| Argument | `wiki/arguments/journal-articles/<journal-name>/`、`wiki/arguments/books/<book-folder>/`、`wiki/arguments/reports-policy-documents/` | 按文献类型；期刊论文 Argument 按 `journal` 字段对应的期刊名称分组；书籍 Argument 再按具体书籍文件夹分组 |


### 条目类型判断

先看条目要回答的核心问题，再定类型。名称像不像术语、是否出现在政策争论中、有没有公式，都不能单独决定类型。

| 核心问题 | 类型 | 库内例子 |
|---|---|---|
| 这是什么现象、构念或分类？ | Concept | Scientific Productivity、Research Impact |
| 怎样获得、测量、计算或分析数据？ | Method | h-Index、I-squared Statistic、Cronbach's Alpha、Difference-in-Differences、Coupling Coordination Model |
| 为什么会这样，用什么机制解释？ | Theory | Shockley's Multiplicative Hurdle Model |
| 用哪个具体工具施测？ | Instrument | 命名量表、问卷、测验 |

量化对象按以下顺序判断，命中即停：

1. 有明确的计算或估计规则（输入数据，经公式或算法，输出数值、等级或估计量），读者需要知道怎么算、怎么读、何时失效：建 Method，使用 `template-method-quant.md`。包括测度指标与指数（h 指数、g 指数、期刊影响因子）、统计量（$I^2$、Cronbach's α、效应量）、统计与计量模型（回归、双重差分、多层线性模型）、综合评价模型（耦合协调模型、熵权法）。
2. 数学模型用来解释现象为何如此分布或变化，输出的是机制判断，不是对某个样本的测量值：建 Theory。例如 Shockley 跨栏连乘模型、Lotka 定律。
3. 指标或模型所测量的对象本身：建 Concept。h 指数测的是学者的累积学术影响，这一构念归入 Scientific Productivity、Research Impact 等 Concept；h-Index 页在 `[!method-scope]` 中链接它们。
4. 可施测、有版本和题项的具体工具：建 Instrument。

常见误判：

- 指标常以“X 指数”“X index”命名，读起来像术语，容易归入 Concept。判断看页面主体：主体是定义式、计算步骤、数据口径、效度和变体，就是 Method。
- 指标在科研评价或政策争论中被频繁讨论，不改变其类型。对该指标使用方式的争议写入 Method 的 `[!method-fit]` 和 `[!method-limits]`；关于量化评价科研这一更大议题的讨论，写入相应 Concept。
- 同一文献同时讨论指标和它测量的构念时，分别建条目并互链，不合成一页。
- Method 页内服务于指标解读的子模型（如 h 指数的线性增长式 $h(t)\approx mt$）作为 `[!formula-step]` 留在该页；子模型被独立用来解释现象时，另建 Theory。
- Concept 页中如需列出定义式以外的计算步骤、数据口径或软件实现，说明该对象应建为 Method。

文件名、文件夹名、`title`、`tags` 使用英文；正文使用简体中文。

- 正文中的加粗小标题后不加中文或英文冒号：写 `**标题** 内容`，不要写 `**标题**：内容` 或 `**标题**: 内容`。
- 加粗小标题如带英文注释，英文必须放进同一组粗体标记：写 `**中文（English）**`，不要写 `**中文**（English）`。

期刊论文 Argument 的二级归档规则：

- 目标路径为 `wiki/arguments/journal-articles/<journal-name>/Argument_<Author>_<Year>_<JournalAbbrev>.md`。
- `<journal-name>` 使用条目 frontmatter 的 `journal` 全称；若期刊名称含 `/` 或 `:` 等不适合作为路径的字符，用空格替换并压缩连续空格。
- 对应 source record 的最终文件名为 `<Author>_<Year>_<JournalAbbrev>.md`，即去掉 Argument 文件名前缀 `Argument_`。

`<JournalAbbrev>` 以 `citation/journals.json` 为唯一命名依据。该文件只存 `{期刊全名: 库内唯一代码}`，无期刊介绍、数量、条目路径、历史缩写或人类可读页面；代码按不区分大小写全库唯一，可使用较长代码消歧。AI 先查表，未登记时用 `.venv/bin/python3 scripts/citation_index.py --register-journal "<期刊全名>" <代码>` 显式登记，脚本不根据新论文文件名自动生成代码，也不覆盖已登记代码。

旧文件名默认保留，不因新增注册表自动批量改名；用户要求统一旧名称时，按注册表迁移 Argument、source record、本地 PDF 和配套目录，更新正文引用，再由脚本重建索引与关系。新建或改名的期刊 Argument 必须使用登记代码；已有文件只在 `journal` 全名保持原值时兼容旧名称，修改期刊归属后重新校验。日常以 HEAD 判断旧文件，CI 以 PR 基线或推送前提交判断，防止错误名称随提交后被当作旧名放行。

基础索引先运行 `citation_index.py --journals-check`；lint 报告 `JOURNAL_NAMING` / `JOURNAL_REGISTRY_INVALID`，同一规则已接入 CI。`source_record.py article` 新建期刊来源时传入 `--journal "<期刊全名>"`，在移动 PDF 前校验最终 `--record-name`；`finalize` 也校验对应 Argument。书籍与报告不受期刊代码表约束。

---

## 4. Naming, Aliases and Tags

### File Names and Titles

`wiki/` 条目的文件名应尽量与 frontmatter `title` 一致，使用可读英文标题，不使用全小写 slug 作为条目文件名。

- 正确：`Piaget's Theory of Cognitive Development.md`

命名规则：

- `title` 是知识对象的正式名称；文件名通常等于 `title`。
- 文件名和 `title` 不使用 tag 风格 slug。
- 标题表达归属关系时，优先使用自然英文结构，如 `Van Leeuwen's Legitimation Theory`、`Teaching Theory of Gruschka`。
- Concept / Theory / Method / Instrument / Fact 的标题和文件名默认不得带括号、冒号、引号；缩写放入 `aliases` 或正文说明。
- Person 命名细则按 `template-person.md` 执行。
- Argument 文件名和 `title` 通常保持一致。
- 缩写、中文译名、常见变体放入 `aliases`。


### Source Record Names

普通论文 / 报告 source record 的最终命名规则：

```text
<Author>_<Year>_<JournalOrPublisherAbbrev>
```

例如：

```text
Simpson_2019_ERE
Marginson_2024_CE
Zhu_2023_BJSE
OECD_2018_GlobalCompetence
```

规则：

- 期刊论文优先使用 `Author_Year_JournalAbbrev`。
- 报告、政策文件、白皮书可使用 `Organization_Year_ShortTitle` 或 `Organization_Year_PublisherAbbrev`。
- source record 文件名和 PDF 文件名保持一致。
- 与 Argument 文件名去掉 `Argument_` 前缀后的部分保持一致。

### aliases

`aliases` 同时用于 Obsidian 检索和 `wiki_linker.py` 自动补链，因此必须精确。alias 本身不准确时，从对应条目删除后重新同步；仅在某句话中误配时，登记句子级链接例外，保留其他语境中的有效 alias。

- Argument 不使用 `aliases`。
- Concept / Theory / Method / Instrument / Fact 的 `aliases` 写中文译名、常见英文变体和缩写。
- Person 的 `aliases` 按 `template-person.md` 执行。
- 页面中某个人名第一次出现时尽可能使用全名，中文正文采用中文（英文）格式；后续再次出现可自由使用英文原文（如英文姓氏或全名）或中文名/姓氏，无需机械重复添加双语括号。APA 引用中的人名保留英文原样。
- 中文译名、英文变体和缩写分成不同 alias；不要把“中文（English）”这类双语括注整体写进一个 alias。人名或缩写与中文术语组合的常用写法（如“Pearson相关”“PISA素养”“IB文凭项目”）可以作为 alias。
- 英文 alias 默认不区分大小写；不要同时写只差大小写的重复 alias。
- 不要写过短、过宽或 tag 风格 slug alias，如“资本”“文化”“教育”“政策”“课程”“能力”“国家”“公平”。
- alias 不得与其他条目同名。`vault_lint.py` 以 ERROR 拦截三种情况：两个条目使用完全相同的 alias 或 alias 等于另一条目标题（`ALIAS_DUPLICATE_CROSS_ENTRY`）；alias 是另一条目以括号声明的缩写，如“Education for All (EFA)”之于 EFA（`ALIAS_HOMONYM`）；Person 的中文姓氏 alias 与另一 Person 中文全名的姓氏相同，如“卡尔·皮尔逊”之于“皮尔逊”（`ALIAS_HOMONYM`）。出现以上任一同名必须修正：删除该 alias 或改为更长、更具体的写法。
- 短 alias（如中文 1–2 字、英文缩写）只要不与其他条目同名即可保留；嵌在其他词语中的偶发误匹配可以容忍，误匹配频繁时再删除或改为更长的写法。
- 不要轻易写单个汉字 alias；只有该字作为独立术语有强识别度时才保留。

### Citation Index Rules

`citation/` 存放可引用 Argument 的引用索引，由 `scripts/citation_index.py` 生成。`external_identities.json` 可以由人补 `doi`、`isbn` 或篇名，脚本不覆盖这些已填字段。

```text
citation/
  citation_full.json          可引用 Argument 的全量索引
  citation_ambiguous.json     同一作者同一年多篇可引用文献的歧义索引
  external_identities.json    条目正文中的库外短引用，可手填 doi、isbn 或篇名
  citation_external.json      库外短引用生成索引；同一作者同一年多篇时分配 a/b/c
```

Citation 字段按 `wiki/templates/TEMPLATE-SPEC.md` 和对应 Argument 模板执行。Argument 保留 `source_language`、`year`、`doi`、可选 `isbn`、`citation_aliases` 与完整 `citation`。`citation_aliases` 由 `scripts/citation_index.py` 根据原始出版语言、`authors`、`year` 和完整 `citation` 自动生成。英文原始文献生成英文 APA author-year 形式。中文原始文献的 `authors` 使用中英双语显示，但完整 `citation` 和 `citation_aliases` 只使用中文；`wiki_linker.py` 也只按这些中文 aliases 匹配该文献。中文期刊论文使用 `source_language: zh`，citation 采用中文作者、中文篇名和中文期刊名，`argument_display_title` 保留中文原题；英文作者转写只存在于 `authors`，不进入 citation 索引。英文文献的作者无论在中文正文还是括注中，三位及以上一律写 `et al.`，不写“等”或“等人”（如 `Hopkins et al., 1996`、`Cai et al.（2025）`、`Hattie et al. 指出`）。基础索引对改动过的条目自动改写：拉丁字母姓氏后接年份，或姓氏属于已知人物（Person 条目与已处理文献作者）时，“等/等人”改为 `et al.`；全大写缩写与机构（`OECD、PISA 等`）、非人名（`Teach 等工具`）、并列多人（`Mignolo、Dussel 等`、`Holmes 和 King 等人`）、“等级/等同”等词与中文作者（`王等, 2025`）不改。英文基本形式为 `Author, Year` 与 `Author (Year)`：单作者用第一作者英文姓氏或机构英文简称，如 `Ball, 2008`；双作者用 `&`，如 `Lindblad & Popkewitz, 2004`；三位及以上作者用 `et al.`，如 `Wang et al., 2025`。中文基本形式只保留 `作者, 年份` 与 `作者 (年份)`；中文双作者用“和”，如 `林德布拉德和波普凯维茨, 2004`；中文三位及以上作者用“等”，如 `王等, 2025`。同一作者同一年多篇可引用文献时，`citation_index.py` 按完整 `citation`、`title`、文件路径稳定排序后自动分配 `a`、`b`、`c` 后缀。论文集章节是可引用 Argument；论文集 overview 是结构入口，不进入 citation 索引。

`doi` 用于论文、报告或有 DOI 的书籍；著作、教材、论文集或章节没有 DOI 时，`doi` 可留空，若能确认 ISBN，则写入 `isbn`。

著作、教材、论文集和论文集章节必须填写 `publisher`；`publication_place` 可选，只作元数据保存。完整 citation 按 APA 7 只写出版者、不写出版地，如 `Routledge.`、`高等教育出版社.`；团体作者同时是出版者时不重复出版者（如 `OECD. (2023). Title.`）。页码与数字范围用 en dash（`31–38`），DOI 写成 `https://doi.org/...`。这些机械格式由 `vault_lint.py` 的 `CITATION_APA7_FORMAT` 检查，`vault_lint.py --fix` 自动修正。

`citation/` 索引文件由 `scripts/citation_index.py` 生成：

- `citation_full.json`：所有 `citation_aliases` 到 Argument 的查询索引。
- `citation_ambiguous.json`：无后缀基础短引用对应的重复文献组。每篇附 `rule` 与 `apa7_aliases`：第一作者同姓不同人用名字缩写区分（`initials`，如 `J. Zhang et al.`，APA 7 8.20）；合著者不同但缩写成 et al. 后相同的，列出足以区分的作者（`authors`，如 `Kim, Lee, et al.`，APA 7 8.18）；作者完全相同才用 a/b（`suffix`）。`citation_aliases` 目前仍用 a/b，`citation_index.py --apa7` 预览、`APA7_DISAMBIGUATION = True` 启用 APA 7 形式（启用会改写全库相应显示文本）。`external` 记录库外数据集（目前为 MetaX）中与 Argument 第一作者、年份相同但篇名不同的文献，防止按作者年份误链。

正文 citation 补链由 `scripts/wiki_linker.py sync --citations-only` 完成，引用模式只读取 citation 索引，不修改 Argument frontmatter。基础索引自动执行增量引用补链；标准流程通过同一补链入口统一执行引用与普通双链维护。

正文引用当前 Argument 之外的已处理文献时，优先沿用原始文献的 author-year 格式。英文文献使用英文 APA，叙述式如 `Lindblad and Popkewitz (2004)`，括号式如 `(Lindblad & Popkewitz, 2004)`；中文文献可以使用中文作者年，如 `郑雅君 (2023)`、双作者 `作者甲和作者乙 (2023)`、三位及以上 `作者甲等 (2023)`。如果原文采用 APA 引用格式，优先保留原文中的短引用，再由 `wiki_linker.py` 自动补链。

原文已有 `Author (YearSuffix: page)` 或 `Author, YearSuffix: page` 这类内部参考文献编号时，清除原文后缀，只保留作者、年份和页码，例如将 `Tandon (2005c: 30)` 写作 `Tandon (2005: 30)`。这类原文编号不写入 `citation_aliases`，不放入 `citation_ambiguous.json`，也不自动补链；只有该文献被独立处理为 Argument 后，才由本库 citation 流程重新决定是否需要 `a/b/c` 后缀。

条目正文里尚未链到 Argument 的 APA 短引用，由 `scripts/citation_index.py` 收集进 `citation/external_identities.json`。每条保留作者和年份。能确定文献时优先写 `doi`；书籍没有 DOI 时写 `isbn`；两者都没有时写篇名。写了 `doi` 或 `isbn` 之后，篇名可以留着便于辨认。期刊名和出版社不作为必填，也不用来区分同年文献。脚本只刷新 `seen_in`，已填写的 `doi`、`isbn` 和篇名保持原样。

同一作者同一年在库外只对应一篇时，`citation_external.json` 里的短引用不加 `a`/`b`/`c`。`doi`、`isbn` 或篇名显示为不同文献，或原文同时写出不同的年份字母时，按篇名、`doi`、`isbn` 和身份键稳定排序后分配 `a`、`b`、`c`，规则与库内相同。生成索引里的字母按这次排序决定，不必与原文里的字母相同。原文年份字母留在 `external_identities.json` 的身份键上，不写入 Argument 的 `citation_aliases`。单独一个带字母的短引用仍生成不带字母的规范形式。

文献入库后，下一次 `citation_index.py` 删除对应库外记录。对上的方式是：`doi` 或 `isbn` 与 Argument 相同；或者身份键已经是该 Argument 的 `citation_aliases`；或者篇名出现在同一作者年份的 Argument 完整 `citation` 里。只含作者和年份的记录继续保留，直到补上能与某篇 Argument 对上的 `doi`、`isbn`、篇名或完整短引用。

`vault_lint.py` 用 INFO `EXTERNAL_CITATION_IDENTITY` 提示还没有 `doi`、`isbn` 或篇名的库外短引用。这条提示不计入必须处理的 WARN，不阻挡已有条目同步。增量检查只列出相对基线新出现的短引用；`--full` 把存量收成一行，工作清单在 `citation/external_identities.json`。补记时看来源原文的参考文献。`citation_ambiguous.json` 的 `external` 仍只记录 MetaX 里作者年份相同、篇名不同的撞车，不存放这套库外短引用。

正文引用当前 Argument 之外的已处理文献时，统一使用 APA 短引用：

- 括号式：`(Ball, 2008a)`、`(Ball, 2008a, p. 12)`、`(Ball, 2008a, pp. 12–15)`。
- 叙述式：`Ball (2008a)`、`Ball (2008a, p. 12)`、`Ball (2008a, pp. 12–15)`。

期刊 Argument 不记录本篇自引。判定只认本篇 `citation_aliases` 的完整括注形式，保留 `a`/`b`/`c` 后缀；同一作者同一年的另一篇文章，以及不带后缀的作者年份，都不是本篇自引，按原引用保留并照常索引。本篇自引整段删除，不收成页码。只含页码、表号、图号或脚注号的括注，`vault_lint.py` 以 `JOURNAL_SELF_PAGE` 提示删除。书籍、教材、论文集章节和报告引用当前文献时只写页码，如（p.147）或（pp.147–148）；正文以裸文本括注写出本文献（含 `part_of` 继承的全书）完整 `citation_aliases` 的，`vault_lint.py` 以 `ARGUMENT_RAW_SELF_ALIAS` 收成纯页码，不把另一篇同年文献收成页码。`vault_lint.py` 检查 citation 字段、`a/b/c` 冲突、正文 APA 短引用格式和歧义引用核验。可引用 Argument 的完整 `citation` 不得缺失或为空；专著和教材的章节 Argument 可继承全书引用，论文集 overview 不作为可引用单元。`citation_index.py --check` 同样检查完整引用是否为空。

非 Argument 条目（Concept、Theory、Method、Instrument、Person、Fact）引用 Argument 时，wikilink 显示文本必须包含作者与年份，可继续附页码或章节，例如 `[[Argument_Author_Year_Journal|Author, Year, p. 12]]` 或 `[[Argument_Author_Year_Journal|Author (Year, Ch. 1)]]`；不得只写 `p. 12`、`pp. 12–15`、`Ch. 1` 或裸 `[[Argument_...]]`。

### Visible Learning MetaX Module

MetaX 数据只存在 `datasets/metax/`，条目中的 MetaX 模块（一组 `[!metax]` callout）由 `scripts/metax_sync.py` 生成，不手写、不手改。

- 位置：模块不设标题（避免全库出现同名标题），作为实证数据组的第一项，放在第一张实证表格 callout（`[!effect-table]` / `[!ma-table]` / `[!ref-table]`，以表内 marker 识别）正前方；没有实证表格时放在 `[!evidence-grid-a] 相关研究索引` 之前，否则放在正文末尾。不依赖任何章节标题。挂载模块的条目自动加 tag `metax`，卸载时自动移除。
- 结构：`[!metax]` 总览（标题为“中文名 · 英文名”的 MetaX 原页链接，兼作模块标识；下一行为领域 › 子领域）→ `[!metax-ma]-` 元分析列表（默认折叠）→ 仅在 `errata.json` 有该因素条目时出现 `[!metax-errata]`。
- 卡片只写 APA 短引用、变量与数字；篇名、期刊、完整作者只存 `metax.json`。眉标与表头中文由 CSS 生成，Markdown 表头只写代号（`rate ma k n m d du rob` / `ref var k n m d e`；`d` 为按研究数加权的平均效应量，即 MetaX 总览值；`du` 为未加权平均，即 MetaX 明细合计行的值）。因素名、领域、子领域与影响判定按 `datasets/metax/zh.json` 译为中文；影响判定显示为评级星（★★★★ 显著加速 … ▼ 负向影响），稳健性显示为 ●○ 五点。
- `[!metax*]` 整块不参与普通补链和 APA 引用补链。块内引用链接只由 `metax_sync.py` 写入：年份、第一作者姓氏与篇名（或 DOI）一致才链接；作者年份相同但篇名不同记为 `collision`，永不链接，并写入 `citation_ambiguous.json` 的 `external`。新入库的元分析 Argument 在下一次 `vault_index.py` 后自动链接到所有收录它的模块。
- 挂载：`metax_sync.py map <influence_id> <条目路径>`；卸载：`unmap`；候选：`suggest`（因素名与条目 title/alias 完全一致）。一个条目可挂多个因素，按因素名排序叠放。
- 勘误写入 `datasets/metax/errata.json`：`level` 为 `study`（单篇，明细行 e 列标 ①②…）或 `influence`（整合，总览对应数值旁标 ⚑）；字段 `influence`、`study`（S 编号）、`field`、`metax`、`corrected`、`type`、`source`（Argument 文件名）、`pages`、`note`。勘误须有来源；`audit` 的输出只是待核线索。
- 自动核算：每次同步按列表重算并比对，只报告真实不一致：研究数、学生数、效应数的单项相加是否等于总览与 MetaX 合计行；按研究数加权的平均效应量（Σkd/Σk，即 MetaX 总览值）与未加权平均效应量（即合计行）是否算对；元分析数是否等于列表项数；研究数、效应数与效应量完全相同的疑似重复行。不一致时在勘误框以 `∑ 自动核算` 列出，重复行在 e 列标 ∑。直接相加、NA 不计入、重叠研究重复计数等对所有因素普遍成立的口径问题，统一在 [[Visible Learning Meta-X]] 条目“因素汇总口径与核算”一节说明，不逐卡报告。自动核算不写入 `errata.json`，数据改正后自动消失。
- `vault_lint.py` 以 `METAX_STALE` 检查模块与匹配状态是否最新。
- 关系字段例外：`[!metax*]` 块内的链接（MetaX 模块里的元分析引用、Meta-X 条目中的领域汇总与 440 个因素索引）由 `wiki_relations.py` 跳过，不写入 `related_*`，避免 frontmatter 膨胀。
- 映射与存根：440 个因素按 `datasets/metax/mapping.json`（审核表 `datasets/metax/reports/MetaX 映射审核.md`）挂载到已有条目，或由 `metax_sync.py apply-mapping` 新建存根条目。存根只含 frontmatter（`status: draft`、tag `metax`）、H1 与 MetaX 模块，不按完整模板撰写；带 `metax` tag 的新条目免于“须在 Argument 正文中链接”检查，由 [[Visible Learning Meta-X]] 的因素索引承担入口。新建标题避免过短或泛化的词，中文别名不用两字泛词，以减少误链。

### EEF Teaching and Learning Toolkit Module

EEF 数据存于 `datasets/eef/`（`eef.json` 由 `scripts/eef_sync.py import --toolkit tlt|ey` 从浏览器导出整理；`tlt` 为教与学工具包，`ey` 为早期教育工具包，后者的策略键带 `ey:` 前缀，卡片写作 `[!eef|ey]`，两套工具包共用一条 `[!eef-divider]`，同一条目内教与学工具包在前），条目中的 EEF 模块（`[!eef]` 总览、`[!eef-studies]-` 研究列表、`[!eef-errata]` 勘误）由 `eef_sync.py` 生成，不手写。

- 分割线：条目自有实证表格（原始研究、一阶／二阶元分析、亚组、其他结果）之前有 `[!empirical-divider]`，已写入 concept 模板；新建含实证表格的条目照此保留。MetaX 与 EEF 卡片组排在它之前。
- 分割线：MetaX 与 EEF 卡片组前各有一条带标签的分割线（`[!metax-divider]` / `[!eef-divider]`，空 callout，线与标签由 CSS 绘制），由脚本随模块增删。
- 位置：同属实证数据组，紧跟 MetaX 模块之后；无 MetaX 时放在第一张实证表之前，规则与 MetaX 相同。两个脚本只删改各自的 callout，互不覆盖；挂载条目加 tag `eef`。30 个策略的对应条目见 `eef_sync.py` 的 `MAPPING`，无对应条目时建存根。
- 总览：影响（月）、成本与证据强度（EEF 五级）、页面报告的研究数、合并效应量、95% 置信区间、异质性 I²。研究列表一行一个效应量，同一研究的多个效应以小标签区分；标题同时给出效应量条数与去重后的研究数。
- 链接：研究按 DOI，或篇名加年份与库内 Argument 一致时才链接。
- 勘误：自动核算报告页面研究数与参考文献列表不一致、权重不闭合、合并结果疑为占位；来源勘误写入 `datasets/eef/errata.json`，`level` 为 `strand`（总览数值旁标 ⚑）或 `study`（列表 e 列标 ①②，`study` 填效应量 id），须附来源。EEF 的合并模型无法用常规随机效应法复现，τ² 与合并值的差异不作为错误报告。
- `[!eef*]` 块与 `[!metax*]` 块同样不参与补链、不写入 `related_*`，也不做写作审查；`vault_lint.py` 以 `EEF_STALE` 检查是否最新。
- 外部文献：`eef_sync.py register-external` 把 EEF 与 MetaX 中尚未入库的研究登记到 `citation/external_identities.json`，有 DOI 写 DOI，否则写篇名，并以 `datasets`（如 `eef:feedback`、`metax:S0412`）注明来源；不改动已有行，同一作者同年的不同文献加年份字母，与库内 Argument 同作者同年时也加字母。入库为 Argument 后由 `citation_index.py` 自动移除。

EEF 具名项目使用 `datasets/eef/programmes.json` 和 `template-fact-eef-programme.md`，归入 `Fact / program`。`eef_sync.py import-programmes --raw <JSON> --slug <项目键>` 仅刷新指定项目并保留其他项目；`entries` 显式映射项目页，`render-programmes` 生成 `[!eef-programme|v3]` 及内嵌的试验折叠块（`[!eef-trial]-`）与待核实事项（`[!eef-errata]-`）；样板在 `template-fact-eef-programme.md` 的成效段（该模板与 `template-fact-program.md` 结构对齐）。基础索引和 EEF 门禁维护已映射模块，不自动新建项目条目。成本保留估算条件，样本逐试验列出，结果评级逐行保留；表头与 CSS contract 见 `wiki/templates/CALLOUTS.md`。

### tags

- tags 全部英文、小写连字符。
- 常用前缀：`region/`、`level/`、`subject/`、`paradigm/`、`theme/`、`method/`、`theory/`、`policy/`、`source/`。

---

## 5. Script Rules and Sync Commands

脚本用于维护索引、citation 索引、补链、关系字段、source 记录和 lint 检查。`vault_index.py` 是基础索引统一入口，内部维护书籍 overview 章节表格和研究地图统计，先刷新引用索引，最后刷新 wiki 索引；用户确认后可用 `vault_index.py --standard-workflow` 运行补链、关系同步、索引刷新和 lint；研究地图统计可用 `vault_index.py --research-map-only` 单独同步；Concept 的 `domain`、`related_count`、`related_level`、`related_stars`、`related_color` 可用 `vault_index.py --concept-fields-only` 显式同步；Instrument 的 `instrument_related_count`、`instrument_related_level`、`instrument_related_stars`、`instrument_related_color` 可用 `vault_index.py --instrument-fields-only` 显式同步；`wiki_index.py` 只维护普通 wiki 索引；`citation_index.py` 维护 Argument 的 `citation_aliases`、引用索引与期刊代码注册表；`wiki_linker.py` 统一维护正文 APA 引用和普通知识链接，并可继续在 YAML `authors` / `editors` 中把 APA 人名补成 Person wikilink，在 YAML `issuing_organization` 中按 `wiki/organizations.json`（机构登记表，`wiki_index.py` 生成，`variants` 可手动编辑）把机构名补成 organization Fact wikilink（规则见 `wiki/templates/TEMPLATE-SPEC.md`）。日常使用增量模式，非必要不使用 `--full-workflow`。

### Python Environment

所有 vault 脚本默认使用仓库本地虚拟环境运行，不用系统 Python 判断依赖是否缺失。推荐命令统一写成 `.venv/bin/python3 scripts/<script>.py`。若直接运行 `python3 scripts/vault_lint.py`，脚本会尝试自动切换到 `.venv`；如果仍出现 `PyYAML is not installed` 等依赖错误，先用 `.venv/bin/python3 -c "import yaml"` 检查虚拟环境，再判断是否需要安装依赖。

### Automatic Step

每次处理完条目、书籍章节、source 记录、模板或 schema 后，AI 只自动运行基础索引：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
.venv/bin/python3 scripts/vault_index.py
```

不要自动运行 `--standard-workflow`。完成基础索引后，询问用户是否运行标准脚本流程。

### Standard Script Flow

用户确认后，再运行：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
.venv/bin/python3 scripts/vault_index.py --standard-workflow
```

标准流程按依赖顺序执行：刷新引用索引 → 机械修复与书籍 overview 维护 → 刷新 wiki 检索索引 → 统一补链（先 APA 引用与显示修正，再普通 wiki 双链） → 关系同步 → 更新日期、关联数量和星钻 → 刷新最终 wiki / 引用索引 → lint。关系同步后必须清除旧缓存并重算派生字段，确保一轮运行即得到最新星钻。

基础索引保留现有的增量 APA 自动补链；普通 wiki 补链与关系同步只在显式标准 / 全量流程中运行。

独立补链入口为 `.venv/bin/python3 scripts/wiki_linker.py sync`，默认先处理 APA 引用，再处理普通双链；`--citations-only` 仅处理引用，`--wiki-only` 仅处理普通双链与 YAML 人名。`--dry-run` 预览统一处理后的结果，不写文件。

### 句子级误链例外

审查确认某句话中的普通双链为误链时，用 `wiki/index.json` 确定所在条目及目标的完整路径，再登记：

```bash
.venv/bin/python3 scripts/wiki_linker.py exclude 'wiki/arguments/.../Argument_Example.md' --sentence '这一假设尚需进一步检验。' --target 'wiki/concepts/.../Research Hypothesis.md'
```

命令只登记例外并将该句中指向该目标的现有链接还原为显示文字，不执行其他补链、关系同步或修改生成字段。仅提及、没有新增信息、不值得更新条目均不自动构成误链；核实概念含义与语境后才能排除。

独立 `related_update.py` 批次审查使用同一命令加 `--record-only`，仅登记，保留任务锁定的 Argument 快照；已有误链在后续显式普通补链中去除。登记命令默认立即去掉对应误链。

关联更新按类型和对应模板分批，默认每批最多五个；每次只执行当前一批。首次用 `related_update.py start <Argument>` 获取本批，保存结果后用 `accept <任务目录>` 完成正常增量检查并停止。仅在用户再次明确指示后，用 `next <任务目录>` 或重复 `start <Argument>` 获取下一批；不得连续自动处理。旧 `advance` 命令仅作为 `accept` 的兼容入口，不再输出下一批；可选 CLI 执行器也每次只运行一批。

`scripts/link_exceptions.json` 只记录所在条目路径、完整可见句子和排除目标路径，不存理由、时间或报告，不向正文或 YAML 加标记：

```json
{
  "wiki/arguments/.../Argument_Example.md": [
    {
      "sentence": "这一假设尚需进一步检验。",
      "target": "wiki/concepts/.../Research Hypothesis.md"
    }
  ]
}
```

普通补链在原有规则外先屏蔽该句中的该目标词及链接，处理后恢复显示文字，避免再次补回，也避免占用每节首次链接名额；同句其他目标、其他句子的有效链接仍按原规则处理。例外不用于 APA 引用、YAML 人名或 source 链接，`--citations-only`、`--tables-only` 不应用例外。

匹配使用完整可见句子，忽略 wikilink 标记、Unicode NFC 差异及连续空白，不绑定行号，不模糊匹配；以中文句末标点、英文句点后空白、换行或表格单元格为分界。重复句拒绝自动定位，需先改写区分；代码等非普通正文中的内容不登记。

基础 `vault_index.py` 和普通补链会自动删除失效记录：句子删除或改写、所在文件删除、目标文件删除时清除，对应列表为空时删除路径键；不保留失效历史。改写后的句子重新按正常规则补链；文件移动或改名应同步例外路径，否则按旧路径失效处理。读取失败或 JSON 损坏时停止并保留文件，不当作删除清空。可单独运行 `.venv/bin/python3 scripts/wiki_linker.py exceptions-clean` 清理，不修改知识条目。普通补链的 `--dry-run` 不改例外表或正文；例外表新增、修改或删除的记录会将对应文件纳入默认增量补链。

`vault_lint.py` 始终校验例外表的路径、结构、句子唯一性与目标类型；无效记录报 `LINK_EXCEPTION_INVALID`，不得靠扩大匹配范围或批量登记绕过审查。

例外处理与回归测试均内置于 `wiki_linker.py`，不另设 Python 脚本。运行 `.venv/bin/python3 scripts/wiki_linker.py self-test` 在临时 vault 中检查登记、排除、清理及增量行为，不修改真实知识条目。

### Full Sync

非必要不要运行 full。只有在以下情况才全量同步与检查：

- 批量修改 `title`、`aliases`、Person APA aliases 或 Argument citation 字段。
- 批量移动、删除、重命名 wiki 条目。
- 使用 `source_record.py finalize --rename` 批量重命名 source record 和 PDF 后。
- 怀疑 wikilink、`related_*`、YAML `sources` 或 source record 的 `extracted_to` 状态不同步。
- 增量同步或增量检查结果异常。
- 发布、备份或重要提交前。

全量流程：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
.venv/bin/python3 scripts/vault_index.py --full-workflow
```

严格检查只在发布、备份或重要提交前运行：

Frontmatter 中同一 YAML 映射内不得重复声明键，包括嵌套映射和行内映射。`vault_lint.py` 以 `YAML_DUPLICATE_KEY` 错误报告重复位置及首次声明行号，阻止提交和发布；不同映射中的同名字段不视为重复。不要通过保留最后一个值自动修复，须先判断应保留或合并的内容。

```bash
.venv/bin/python3 scripts/vault_lint.py --full --strict
```

机械格式错误（加粗小标题冒号、英文注释在粗体外、英文双作者 and、summary 引号、`[!axis]` 层级及同级分隔）可自动修复：

```bash
.venv/bin/python3 scripts/vault_lint.py --fix          # 增量
.venv/bin/python3 scripts/vault_lint.py --full --fix   # 全库
```

引用显示文本的 a/b/c 后缀漂移（新增同作者同年文献后旧链接显示未更新）可自动改写：

```bash
.venv/bin/python3 scripts/wiki_linker.py sync --citations-only --fix-display --full
```

本地不使用 git pre-commit 钩子：Obsidian Git 每 10 分钟自动提交备份，钩子会让含未完成内容的备份静默失败。门禁分两层：

1. 本地：`vault_lint.py` 即提交门禁。除内容检查外，它并行检查 wiki 索引是否最新（`INDEX_STALE`）、引用索引是否一致（`CITATION_INDEX_STALE`），本地与 CI 共用这一入口。结束任务前先运行 `vault_index.py` 再运行 lint，任何 ERROR 和新引入的 WARN 都必须解决。`EXTERNAL_CITATION_IDENTITY` 是 INFO，不在此列：它提示新出现的库外短引用补 DOI、ISBN 或篇名，不阻挡已有条目同步。增量模式与 `--path` 隐藏基线已有的普通警告（按检查项与提示内容比对，行号变化不影响），未审查的写作用词与句式命中始终列出；`--all-warnings` 显示全部，`--full` 始终显示全部，用于盘点存量。`--no-gate` 只用于调试。

`vault_index.py` 在刷新引用索引后，对 git 中有改动的文件自动执行机械性修复，不需要手动处理，也不再出现在 lint 中：英文双作者引用连接词（叙述用 and、括号内用 &）、加粗边界、summary 引号、`[!axis]` 分隔符、引用链接缺失的 a/b/c 年份后缀、非 Argument 条目中裸 `[[Argument_…]]` 链接补作者年份、与标题重复的 alias、同一段落或 callout 内重复的括号式引用链接、英文作者引用中的“等/等人”（改为 et al.）；随后把正文有改动的条目 `updated` 设为当天。手动执行同样的修复可用 `vault_lint.py --fix`。
2. 发布：GitHub Actions 运行 `scripts/vault_lint.py`（期刊注册表、只读 wiki 索引检查、完整引用检查和增量 lint），未通过则不发布。CI 使用 `--base` 模式时，写作审查只拦截相对推送基准新增或改写的命中（按条目路径、检查项与去链接后的可见语境比对）；基准中已存在的未审查命中不阻断发布，仍由本地 lint 列出，按本地门禁要求处理。

手动执行与 CI 相同的检查使用 `.venv/bin/python3 scripts/vault_lint.py`。依赖在 `requirements.txt` 中固定，CI 据此安装，不得删除。`scripts/hooks/pre-commit` 保留备用；如需临时恢复钩子：`git config --local core.hooksPath scripts/hooks`。

GitHub Actions 在 pull request 和 main 分支 push 时执行同一检查入口，通过只读选项 `--base <SHA>` 检查相对于 PR 基线或 push 前提交新增、修改和重命名后的 Markdown 文件，避免干净检出时增量 lint 为空。仅 main 的 push 且检查全部通过后，才触发 Quartz 发布。此日常门禁不替代重要发布前的全量严格检查。

移动 wiki 条目时：

- 只移动文件本身，不手动编辑 `wiki/index.json`、`wiki/index.md`、各类型索引页或 generated fields。
- 批量移动 journal article Argument 时，按 `journal` 字段创建或复用 `wiki/arguments/journal-articles/<journal-name>/`，移动后立即运行 `vault_index.py`。
- 若移动涉及正文中的 vault-root 图片路径、source record 的反向关系，或移动后索引 / 链接检查异常，再运行标准 full sync。

### Wikilink and Relation Rules

- wikilink 由 `wiki_linker.py` 自动维护，依据是 `title` 和 `aliases`。
- 页面中某个人名第一次出现时尽可能使用全名，中文正文采用中文（英文）格式；后续再次出现可自由使用英文原文（如英文姓氏或全名）或中文名/姓氏，无需机械重复添加双语括号。APA 引用中的人名保留英文原样。
- 只有 Argument 页使用 `## 来源` / `## Sources` 章节，且只放 source wikilink。来源链接必须包含相对于 vault 根目录的完整路径和简短显示名，不得只写文件名，以免 Quartz 将同名文件夹笔记解析到错误的根路径。
- Argument 页的 YAML `sources` 由 `wiki_relations.py` 从 `## 来源` 章节同步。
- source record 的 YAML `extracted_to` 由 `wiki_relations.py` 从 Argument 页的 `## 来源` 章节反向同步。
- Concept / Theory / Method / Instrument / Person / Fact 不写 YAML `sources` 和正文 `## 来源`；正文中的 Argument 链接同步到 `related_arguments`。

---

## 6. Source Records and Source Files

Source record 不是完整文献数据库条目，而是来源入口页。

- source record frontmatter 只保留 `citation`、`extracted_to`、`processed_date`；书籍任务可按专项 schema 额外保留必要的 `part_of`。
- source record 正文只保留一级标题、本地 PDF / EPUB 阅读入口和 NAS 在线阅读入口；不要写摘要、关键词、研究问题、作者信息、期刊信息等。
- `citation` 初始可为空；完整 citation 应在 Argument 页完成后由 `source_record.py finalize` 从 Argument frontmatter 回填。
- `extracted_to` 始终由 `wiki_relations.py` 反向同步，AI 和 `source_record.py finalize` 不手动维护。
- source record 文件名、一级标题、PDF / EPUB 文件名应保持一致；本地文件保留给 Obsidian 阅读，但不进入 git。
- NAS 在线地址统一按 vault 相对路径映射到 `https://img.mylikemie.icu/`：例如 `sources/A.pdf` → `https://img.mylikemie.icu/sources/A.pdf`，`books/B/Book.pdf` → `https://img.mylikemie.icu/books/B/Book.pdf`。
- 仅迁移本地文件名而未迁移 NAS 时，允许保留已发布的 PDF / 图片 URL。使用 `source_record.py finalize --rename --preserve-remote-url` 保留原 PDF iframe 地址；正文图片 URL 同样保留。后续仅回填 citation、未再次改本地 PDF 名称时，finalize 会继续保留来源页中的显式在线地址。不要把在线地址改为尚未发布的新路径，也不新增重复的来源字段。
- source record 不是普通 wiki 条目，不写 `type`、`subtype`、`tags`、`status`、`related_*`。

### Source Record Commands

Source 记录与阅读页面优先由 `scripts/source_record.py` 生成。AI 先判断来源类型，再调用对应子命令；脚本不负责自动猜类型。

| 来源类型 | 子命令 | 输出位置 |
|---|---|---|
| 期刊论文 | `article` | `sources/`，有图时 finalize 后为 `sources/<论文命名>/` |
| 报告／政策文件／白皮书 | `report` | `sources/`，有图时 finalize 后为 `sources/<论文命名>/` |
| 专著整本书 PDF source | `monograph-pdf` | `books/<book-folder>/` |
| 专著整本书 EPUB source | `monograph-epub` | `books/<book-folder>/` |
| 论文集／编著整体 overview | `edited-volume-overview` | `books/<book-folder>/` |
| 论文集章节 source | `book-chapter` | `books/<book-folder>/` |
| 从 Argument 页回填 source record | `finalize` | `sources/` 或 `books/<book-folder>/` |

常用命令形态：

```bash
.venv/bin/python3 scripts/source_record.py article --file raw/FILENAME.pdf --record-name <论文命名> --journal "<期刊全名>"
.venv/bin/python3 scripts/source_record.py report --file raw/FILENAME.pdf --record-name <论文命名>
.venv/bin/python3 scripts/source_record.py finalize --argument "wiki/arguments/.../Argument_<Author>_<Year>_<JournalAbbrev>.md" --rename

# 若创建 Argument 前判断该论文／报告需要图片占位或后续补图：
.venv/bin/python3 scripts/source_record.py finalize --argument "wiki/arguments/.../Argument_<Author>_<Year>_<JournalAbbrev>.md" --rename --with-figures
```

`finalize` 只负责从 Argument 页回填 citation、按需重命名 source record/PDF，并同步 Argument 页中的 source wikilink；`--with-figures` 会将普通论文／报告 source 移入 `sources/<论文命名>/` 并创建 `figures/`；不维护 `extracted_to`。

### Source Files

- `raw/` 只放原始 PDF，不加 frontmatter，不编辑。
- `sources/**/*.pdf`、`books/**/*.pdf`、`books/**/*.epub` 是本地阅读副本；它们应由 `.gitignore` 排除，并同步到 NAS 后由 source record 中的 `https://img.mylikemie.icu/...` 地址发布。
- 在线 EPUB 阅读器使用 `epub.js` 从 NAS 拉取 `.epub`；NAS/CDN 必须对 `.epub` 返回 `Access-Control-Allow-Origin: *`（或至少允许站点域名），否则浏览器会因 CORS 拦截而无法内嵌显示。PDF iframe 不需要这个头。
- 普通论文或报告先确定最终 `<论文命名>`，Argument 的 `## 来源` 可先写 `[[<论文命名>]]`；source record 在 Argument 页写好后用 `source_record.py article` 或 `source_record.py report` 生成。
- 普通论文或报告处理完成并写好 Argument 页后，再用 `source_record.py finalize --rename` 回填 citation。
- 若普通论文或报告有 figure 或无法读取的 table，使用 `source_record.py finalize --rename --with-figures`，并按「Figure 和 Table 处理」写图片占位；可读 table 必须复刻为 Markdown 表格。
- 书籍来源记录按对应专项 schema 执行。
- `sources/` 与 `books/` 下的 source record 不进入 `related_*` 自动维护逻辑；`extracted_to` 只从 Argument 页反向同步。

---

## 7. Entry Perspective and Writing Style

### Knowledge-base perspective

除 Argument 外，所有条目都以知识对象本身为中心，论文只是证据来源。

- Concept：写概念本身。
- Theory：写理论本身。
- Method：写方法本身。
- Person：写人物本身。
- Fact：写现实中的政策、事件、制度或历史节点。
- Argument：写某篇论文、章节、报告或专著的论证结构。

非 Argument 条目不得以文献、文章、章节或作者作为常规主语，应改为知识库陈述：

> 通识教育科于 2009 年在香港正式推行……  
> 该政策的主要影响包括……  
> 学界对此存在争议……

### Argument style

Argument 可以围绕文献本身，但正文应直接陈述论证思路，不以“论文 / 本文 / 本章 / 文章 / 研究 / 作者 / 研究者 / 本研究 / 论证”等作为常规句子主语。直接阐述研究问题、证据、机制或结论。

Argument 论证结构三要素：
- **步骤标题主张化**：各级标题（`### 论证步骤` 与 `#### 子论点`）必须体现明确的学术主张与判断，严禁使用中立、模糊或纯描述性短语（如禁止单纯写“论证步骤一”或“历史背景”，必须直接亮明判断）。
- **内容围绕核心主张展开**：论证步骤下所有内容必须高度聚焦核心主张，系统展示充分扎实的证据支撑（一手文献、法案条款、实证数据等）与严密的论证推导过程（思想史考证、因果机制推演、对质反驳等），杜绝机械直译或清单式平铺直叙。
- **不写过渡语**：标题与 callout 之间、callout 与 callout 之间不硬加过渡句。只有承载实质内容（论断、机制、证据、条件）且不重复标题或下一个 callout 标题的文字，才作为正文保留；没有这样的内容时，callout 直接相接。禁止“下面从……展开”“学界形成了……”“……如下”“……揭示了……的局限性”这类只预告或复述结构的句子。仍应避免数百字未加结构化的大段裸文字。

Argument 必须详细拆解论证关系：问题来源、概念或理论、前提、证据如何支持前提、中间推论如何连接到结论，以及可能存在的跳跃、弱证据或过度推论。这里的“拆解论证关系”不等于必须使用 `[!chain-link]`；该 callout 只保留给 3–5 个链节、逐层依赖、不可换序且共同指向一个结论的深层论证链。超过 5 项必须合并相邻链节，无法压缩时改用逻辑图和分段散文。单层证据支持、并列发现和时间顺序分别使用 warrant/evidence、finding 或 timeline/phase 等更准确的结构。

Argument 的 `## 论证结构` 中，每一个论证步骤都应独立成段，步骤之间使用 `---` 分割线。

语言要易懂。抽象理论必须配例子；例子优先来自原文，原文没有时可用简短教育情境说明。

Argument 引用规则：

- 期刊 Argument 不记录本篇自引，不写作者与年份，也不写指向本篇的页码、表号、图号或脚注号。本篇引用其他文献时，按该文原有 APA 短引用写下，被引文献自带的页码保留。同一作者同一年的另一篇文章按原引用保留。
- 书籍、教材、论文集章节和报告引用当前文献时，只写页码，如（p.147）或（pp.147–148），不写作者与年份。
- 当前文献引用其他文献时，按原引用内容直接记录，不额外添加二手引文标记，使用 APA 引用。
- 书籍、教材、论文集章节和报告只有引用当前文献之外的独立来源时，才写作者、年份与页码。

全库引用格式（APA 规范）：

- 无论是论证页（Argument）还是其他知识库条目，在正文中提及或引用多作者文献时，必须严格遵循 APA 格式。
- **严禁**使用中文的“等人”或“等学者”来代替英文多作者（例如：不得写成 `Machamer 等人指出` 或 `Sandoval 等学者发现`，必须规范写作 `Machamer et al. (2000) 指出` 或 `Sandoval et al. (2016) 发现`）。
- 两名作者的文献在叙述时，严禁使用中文的“和”或“与”（例如：严禁写 `Hofer 和 Pintrich (1997)`）。叙述性引用必须使用英文 `and`（如 `Hofer and Pintrich (1997)`），括号内引用必须使用 `&`（如 `(Hofer & Pintrich, 1997)`）；三人及以上作者首引或续引均统一使用 `et al.`，彻底剔除口语化的“等人”与“和”，保持严格的 APA 原文引用语态。

- **公式归属** 公式的完整说明（`[!formula-step]` 中的符号、数学直觉、手算示例、结果读法、GeoGebra 模拟）写在对应的 Method 或 Theory 条目。条目已完整收录某个公式后，Argument 删除该 `[!formula-step]`，改为一两句话说明作者用公式得出的结论，可保留行内主公式，并链接条目。条目尚未建立或尚未收录时，Argument 可暂留 `[!formula-step]`，迁移完成后再删除；迁移前先核对条目已包含原卡片的全部信息与出处。

### Writing and Template Rules

- 新建或重写条目必须读取三个文件：`wiki/templates/TEMPLATE-SPEC.md`、`wiki/templates/CALLOUTS.md`、对应 `wiki/templates/template-*.md`。
- `TEMPLATE-SPEC.md` 规定字段、写作、来源和类型结构规则。
- `CALLOUTS.md` 规定 callout 语义和 CSS contract。
- `template-*.md` 只提供具体页面骨架；有内容才写，没有内容可省略空章节。
- 模板与规范冲突时，以 `TEMPLATE-SPEC.md` 和 `CALLOUTS.md` 为准。
- 正式条目正文不要复制模板中的说明注释。
- **术语与缩写规范**：任何专业术语、带缩写的机构、项目或量表名称（包括在 Argument 论证页与各类型 Wiki 条目中），首次出现时必须完整写出格式为：`中文名（英文全称，缩写）`，例如：`随机对照试验（Randomised Controlled Trial, RCT）`、`教育捐赠基金会（Education Endowment Foundation, EEF）`、`认识论问卷（Epistemological Questionnaire, EQ）`。只有在完整定义过一次后，后续行文才能单独使用缩写（如 `RCT`、`EEF`、`EQ`），绝不能默认读者已知缩写含义而直接抛出。
- **命题去数据化规范**：概念条目的“命题”章节（`## 围绕概念形成的命题`）专注于理论机制、因果推导与观点辩护，严禁在命题陈述或 `[!claim]` 中堆砌具体实证统计数据（如效应量数值 $g/d$、样本量 $k/N$、$p$ 值与检验统计量等）。所有具体实证统计必须严格收拢在 实证数据表格中，彻底杜绝概念条目内部的内容冗余。
- **人名与语言规范**：页面中某个人名第一次出现时，中文正文采用“中文（英文）”格式，且尽可能使用全名（例如：`哈罗德·诺亚（Harold Noah）`）；后续再次出现时可自由处理，可以直接使用英文原文（如直接使用 `Noah`、`Harold Noah` 等），也可以使用中文名、姓氏或代称，无需重复标注英文或机械添加双语括号。APA citation 中的学者姓名保留英文原样，严禁汉化翻译。正文叙述减少使用破折号和不必要的引号。
- **AI 常见网红词汇与互联网黑话**：对“跃迁、闭环、沉淀、托举、内核、跃升、底座、破局、颗粒度、耦合、统摄、统合、链路、蜕变、坍塌、杠杆、闭合、靶向、解耦、归约、收敛、规约、收束”等词，除非具有明确的概念内涵、切合具体语境且确有表达必要，否则避免使用此类互联网黑话和泛化的抽象词汇，优先采用准确、具体、自然的学术表达。`vault_lint.py` 以 `ACADEMIC_BUZZWORD` 要求核对概念、语境和表达必要性，不自动改写。
- **否定转折句式**：检测“不是、并非、绝非、不在于、而是、而在于”。使用否定转折句式前，必须检查所否定的观点是否真实存在、前后概念是否构成实质性对立、是否涉及真实的学术争论，以及转折是否带来明确的信息增量；若存在虚构论争对象、制造虚假对立或缺乏实质性论证的情况，应改用直接的肯定式表述。 `vault_lint.py` 以 `ACADEMIC_NEGATIVE_CONTRAST` 要求逐项审查，不自动改写。写作检查覆盖正式 wiki 条目的正文和 summary；未审查命中显示 WARN，并使普通 / 严格 lint 返回失败，不受基线隐藏影响。代码、注释、链接地址、来源列表与规则文档不参与此项检查。


- **自我说明性文字**：检测“论文、本文、本章、作者、原文”，以 `ACADEMIC_SELF_REFERENCE` 要求审查。去掉自我说明性文字，避免以这些词作为常规叙述主语，直接陈述具体判断、知识对象、机制、证据或结论，必要出处放在引用中。实质讨论研究文献、章节或作者的必要表达须结合语境审查，不机械删除。沿用写作审查门禁及句子级例外机制。

### 写作审查门禁

有效例外由脚本自动匹配并直接跳过，AI 不再重复审查或逐次报告。只有未匹配例外的命中才须修改表达，或在核对概念、语境、来源和保留必要性后批准为例外。不得凭空补写来源、未经审查批量放行或修改 lint 规避检查。脚本核验记录结构和原句绑定关系；AI 在添加 ID 前完成实质审查，并在最终回复列出本次改写及新批准的条目与 ID。

例外表 `scripts/writing_exceptions.json` 仅保存条目的 vault 相对路径（NFC）及已批准的审查 ID 列表，不保存解释、理由、证据文字或其他元数据；不写入条目的 YAML 或正文：

```json
{
  "wiki/concepts/<field>/<Title>.md": ["0123456789abcdef"]
}
```

ID 必须为不重复的 16 位小写十六进制字符串。例外绑定条目路径、规则类别、正文 / summary 位置及完整原始行，不绑定行号。已批准例外持续生效；原句改动、规则类别变化或移到其他条目后，须删除失效 ID，并重新审查仍需保留的新表述。无效记录报 `ACADEMIC_REVIEW_INVALID`，失效记录报 `ACADEMIC_REVIEW_STALE`，均为 ERROR。JSON 格式错误、重复键以及对应条目被删除或移动，也会阻断检查；即使条目不在本次增量范围内，已有记录仍会检查是否有效。有效例外静默跳过，不触发 AI 重复审查。未通过审查的表达不进入例外表；不使用全词白名单。

例外表有变动时，增量 lint 同时检查变动前后表中涉及的条目，删除例外后对应表达重新进入待审查范围。未处理项即使已被自动提交、曾出现在 HEAD 中，也不会在所选文件内被忽略。`--all-warnings` 用于显示其他存量问题，不是绕过写作审查的开关；标准与全量流程入口保持不变。

---

## 8. Extraction Criteria

提取标准只决定“是否值得建条目”。一旦新建 Concept / Theory / Method / Instrument / Fact / Person，必须同步更新当前 Argument 页，在相关论证段落中用一句话提及并链接该条目；如果无法在 Argument 正文中自然提及，就不要新建，改为在 Argument 中保留纯文字说明。

### Concept

只要研究对某个 Concept 报告了样本、测量、频数、比例、均值、相关、回归、组间差异、显著性、置信区间、效应量或元分析结果，就必须更新该 Concept 的实证数据表格，并至少填写一张与数据类型相符的表格。通用结果填写 `[!ref-table]-`，可比较效应量的一级研究同时填写 `[!effect-table]-`，元分析同时填写 `[!ma-table]-`。每行链接对应 Argument；原文未报告的指标写 `—`，不得自行推算，也不得只在“相关研究”中概述结论来替代表格。

### Fact

有明确时间 + 地点 + 主体的政策、事件、组织机构、重大项目或制度安排，应建 Fact 条目。`subtype` 固定分为四类：
1. `policy`：法律法案、政策文本、国家战略、课程纲要、官方白皮书、行政规程；
2. `event`：重大历史事件、危机、教育运动、历史性访问、国际论战；
3. `organization`：政府机构、国际组织、学术学会、大学、科研清算中心、智库、基金会；
4. `program`：重大国家/国际科研工程、评价项目（如 PISA）、实验试点项目、卓越资助计划。

不要把具体政策、事件、机构或项目只当作概念例子一笔带过。

### Theory

论文提供以下任一信息时，可建 Theory 条目：明确作为理论框架；用于解释现象或论证立场；有专门章节介绍核心主张、起源、代表人物或应用方式。只被点名但无介绍时，不单独建条目，只在相关条目中链接。

### Method

论文提供以下任一信息时，可建 Method 条目：研究设计、数据收集或分析方式、方法选择的理由、认识论立场、操作步骤、适用场景或局限。文献给出指标、统计量或模型的计算规则时，也按 Method 建条目，类型判断见第 3 节“条目类型判断”。方法只被命名但无介绍时，不因其定义新建或扩写 Method 条目，但实证研究仍需按下面规则记录方法案例。

除思辨类、评论类、理论建构类和概念辨析类文献外，所有实证研究都必须至少记录一条方法案例。量化、质性和混合方法研究都适用。

处理实证研究时，AI 必须识别至少一种核心研究方法，并更新对应 Method 条目的 `## 使用此方法的研究` 章节。若对应 Method 条目不存在，则新建 Method 条目。方法案例只写一句话，并链接到当前 Argument 页。

方法案例只说明该研究如何使用方法，不展开文献摘要。若文献只命名方法但没有提供方法论说明，仍可作为案例记录；但不据此扩展方法定义、研究程序或局限性。

### Instrument

文献使用或讨论可以明确识别的命名量表、问卷、测验、清单、评分规程、观察工具或访谈工具时，应创建或更新 Instrument。只写“使用问卷调查”而没有工具名称、版本、题项结构或计分信息时，不建 Instrument。

处理使用命名工具的实证研究时，必须在对应 Instrument 的 `## 使用该工具的研究` 中增加一句话案例，并链接当前 Argument。研究报告的版本、语言、人群、维度、计分、信度、效度、阈值或测量不变性信息，应分别写入对应章节，不能把不同版本或样本的结果混写。

抽象测量对象写入 Concept。一般性的问卷法、量表开发、因子分析、信效度检验或测量模型写入 Method。只有可以作为具体施测对象识别和复用的工具写入 Instrument。

### Person

不是每个作者都建 Person。只有符合以下之一才建：有独立理论、概念或框架贡献；在领域内有持续影响力；文献专门讨论其思想。只是论文作者、顺带引用一次、受访者，不建 Person 条目。

---

## 9. Updating Existing Entries

整合新内容时：

- 保留原有内容。
- 新信息补充到最相关章节。
- 先判断新信息属于哪个主题、子主题或模板章节，再判断该主题内部的时间位置；不要只按出现时间把内容插到文件末尾。
- 相似内容要融合，不堆砌重复条目。
- 有分歧时放入“争议与批评”，不要覆盖原观点。
- 新旧内容之间加过渡句，保持段落自然。
- 插入位置优先级：同主题已有段落或列表 → 对应章节末尾 → 新增 `###` 子主题 → 新增模板允许的章节。
- 期刊 Argument 的新增信息不附本篇页码。书籍、教材、论文集章节和报告的新增信息附来源页码。
- `updated` 由 `vault_index.py` 自动维护：正文相对上次提交有改动的条目会被设为当天日期，不需要手动修改；需要时更新 `confidence`。
- 不手动更新 `related_*`、Argument `sources`、source record `extracted_to`，交由脚本同步。
- 所有七类条目的关联亮度使用同一规则：每 10 个关联计 1 星，每 3 星显示为 1 枚钻石，余数继续计星，不足 10 个显示 ☆；数值 level 保留总星数，不封顶。由 `vault_index.py` 统一重算。
- 在正文中自然使用 wikilink，脚本会自动维护 frontmatter 关系。
- 只有 Argument 页更新正文 `## 来源` 章节；非 Argument 条目用 Argument 短引用承载来源关系。

章节组织：默认先按主题或模板逻辑分组，再在组内按时间或论证顺序排列；分点少于 8 条时可直接按逻辑顺序排列；分点达到 8 条或以上时按 `###` 子主题分组，组内按时间排列；争议章节按立场分组；发展脉络按时间顺序；来源列表只按时间排序，不分主题。

---

## 10. Link, Duplication and Markdown Safety

### Link and Duplication Rules

核心原则：用链接减少重复，具体补链交给脚本。

- 详细内容只写在最相关的主条目中。
- 其他条目只写一句关系说明。
- 条目尚未建立时先写纯文字。

### Quartz / Markdown Safety

写入 Markdown 时注意：

- 加粗标记须遵守 CommonMark 边界规则。加粗内容以括号、引号等标点结尾且后接正文时，在结束 `**` 后加空格，如 `**等值性（reliability as equivalence）** 的核心形式`；以标点开头且前接正文时，在开始 `**` 前加空格。`vault_lint.py` 以 `BOLD_DELIMITER_BOUNDARY` 提醒简单加粗片段的边界风险，`--fix` 仅在必要的外侧边界补空格，保留文字与加粗范围。

- HTML 颜色不要写 `#ccc`，改用 `rgb(204,204,204)`。
- DOI / URL 若含特殊字符，优先放 frontmatter，或用反引号包裹。
- 不在正文写内联 JS；脚本逻辑放外部文件。
- 数学公式：行内公式写 `$d = 0.40$`；独立公式写：

```markdown
$$d = ...$$
```

- 正式条目正文不要写任何注释。模板中的 HTML 注释或 Obsidian 注释只用于说明结构，生成或更新条目时不得复制进正式条目。
- **表格内双链竖线转义**：Markdown 表格中 `|` 为列分隔符。表格表头与单元格内带有别名的双链必须使用反斜杠转义竖线：`[[Target\|Alias]]`，严禁写成未转义的 `[[Target|Alias]]`；未转义的 `|` 会导致单元格被截断、多出空列或列数错位，破坏表格排版。无需别名时可直接写 `[[Target]]`。
