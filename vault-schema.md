# Vault Schema

本文件只保留 AI / Claude Code 处理 Obsidian vault 时必须遵守的规则。模板规范以 `wiki/templates/TEMPLATE-SPEC.md` 与 `wiki/templates/CALLOUTS.md` 为入口；具体页面骨架以 `wiki/templates/` 中对应模板为准；脚本实现细节以 `scripts/` 为准。

---

## 1. Core Principles

- 只读取当前任务需要的文件，避免扫描无关文件夹。
- 先根据材料判断需要建立或更新哪些知识对象，再读 `wiki/index.json` 检索候选条目是否已存在。
- `wiki/index.json`、`wiki/index.md` 和各类型索引页由 `scripts/wiki_index.py` 自动生成，不手动维护。不手动维护生成字段：`related_*`、Argument YAML `sources`、source record 的 `extracted_to`。Source 记录与阅读页面由 `scripts/source_record.py` 生成。
- 修改已有条目必须先读取文件，判断目标章节、子主题与插入位置，再使用 `str_replace` 精确替换相关段落，不重写整个文件。
- Argument 条目引用当前对应文献时只写页码，如（pp.147–148）。其他条目需按照APA格式严格引用。非 Argument 条目不写 YAML `sources` 和正文 `## 来源`；
- 不使用来源以外的知识；

- 普通论文 / 报告 source record 使用最终 `<论文命名>` 创建；完整 citation 在 Argument 页完成后由 `source_record.py finalize` 回填。若文献包含需要保留占位的 figure，`finalize` 时使用 `--with-figures` 生成 `sources/<论文命名>/figures/`。
- 新建、移动、删除、重命名条目后，只自动运行基础索引：`vault_index.py`（内部维护书籍 overview 章节表格，并依次运行 `wiki_index.py` 与 `citation_index.py`）；是否继续运行 citation 补链、普通 wiki 补链、关系同步、Concept 派生字段同步与 lint，由用户确认。
- 非必要不要运行 `--full`。优先使用 git 增量或路径限定；只有批量重命名/移动/删除、批量 title/alias/citation 字段变更、增量结果异常、发布/备份/重要提交前，才使用 full sync 或 full lint。

---

## 2. Workflow

### 普通论文／报告

1. 读取 `vault-schema.md`；若用户明确说明是专著、论文集或教材，转入 `Specialized Schemas`；若用户未说明类型，按普通论文／期刊论文流程处理。
2. 读取原始文件并提取可读文本。
3. 扫描文献，同时判断二类事项：需要建立或更新哪些知识对象，是否包含需要占位的 figure。
4. 在创建 Argument 页之前确定最终 Argument 文件名，并由此确定最终 `<论文命名>`；Argument 页正文 `## 来源` 可先写 `[[<论文命名>]]`。
5. 为每个候选知识对象记录暂定英文标题、中文术语或别名、类型、目标二级文件夹和独立成条理由。
6. 读取 `wiki/index.json`，用标题、中文术语、英文变体和缩写检索是否已有。
7. 将候选分为待更新和待新建。
8. 更新已有条目：读取文件 → 判断目标章节、子主题与插入位置 → 先按主题归组，再在主题内按时间或论证顺序整合 → 用 `str_replace` 精确替换相关段落。
9. 新建条目：读取 `wiki/templates/TEMPLATE-SPEC.md`、`wiki/templates/CALLOUTS.md` 和对应 `wiki/templates/template-*.md` → 按模板逻辑组织内容，先主题后时间；同时记录该条目应回链到当前 Argument 的哪个论证段落。
10. 判断研究方法，除非是思辨类或评论文章，更新或新建至少一个 Method 条目，在 `## 使用此方法的研究` 加入一条方法案例，并链接当前 Argument。
11. 创建或更新 Argument 页，frontmatter 按 `template-argument.md` 写入必要字段，正文 `## 来源` 列出 `[[<论文命名>]]`；若有 figure，在对应论证位置写图片占位，图片路径使用第 4 步确定的最终 `<论文命名>`。本任务新建的每个 Concept / Theory / Method / Fact / Person 都必须在 Argument 正文的相关论证段落中至少出现一次 wikilink。
12. 用最终 `<论文命名>` 创建 source record：期刊论文用 `source_record.py article --record-name <论文命名>`；政策、报告、白皮书用 `source_record.py report --record-name <论文命名>`。
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
- 占位跟随正文叙述放在最相关段落之后，不堆在开头；使用 Markdown 嵌入 `![](...jpg)`，不要包在任何注释中；可见标题使用图号和图名。
- Figure 或无法读取的 table 主要服务于文献整体论证时，放在当前 Argument 的对应位置；主要服务于具体 Concept / Theory / Method / Fact / Person 时，放在对应条目中，并在 Argument 页简要提及或链接该条目。
- 普通论文／报告若需要图片占位或后续补图，最终 source record 和 PDF 应放入 `sources/<论文命名>/`，并创建 `sources/<论文命名>/figures/`；无图时仍可保持 `sources/<论文命名>.md` 和 `sources/<论文命名>.pdf` 的扁平结构。

普通论文／报告 figure 占位：

```markdown
> [!example]- 图X：名称
> ![](https://img.mylikemie.icu/sources/<论文命名>/figures/<论文命名>_FigX_Descriptive_Name.jpg)
```

说明：`<论文命名>` 由 AI 在创建 Argument 文件名前确定，通常等于最终 Argument 文件名去掉 `Argument_` 后的部分，如 `Argument_Simpson_2019_ERE.md` 对应 `Simpson_2019_ERE`。命名前要先判断是否有需要保留占位的 figure 或无法读取的 table；需要占位时使用 `source_record.py finalize --rename --with-figures`，让 source record、PDF 和 `figures/` 落入 `sources/<论文命名>/`。

书籍 figure 占位：

```markdown
> [!example]- 图X-X：名称
> ![](https://img.mylikemie.icu/books/<book-folder>/figures/Figure_X-X_Descriptive_Name.jpg)
```

### Sync Decision

脚本流程统一见第 5 节。普通任务完成后只运行基础索引，是否继续补链、同步关系和 lint 由用户确认。

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
  vault_index.py
  wiki_index.py
  citation_index.py
  citation_linker.py
  wiki_linker.py
  wiki_relations.py
  vault_lint.py
  source_record.py
citation/
  citation_full.json          可引用 Argument 的全量索引
  citation_ambiguous.json     同一作者同一年多篇可引用文献的歧义索引
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
| Method | `wiki/methods/qualitative/`、`quantitative/`、`mixed/` | 只放研究方法、研究设计、资料收集／分析方法、项目评价方法；课堂教学法放 Concept |
| Person | `wiki/persons/<nationality-or-region>/` | 按国籍／地区；不明或跨国身份放 `global` |
| Fact | `wiki/facts/<region>/` | 按地区；全球性放 `global`；多国比较放 `multi` |
| Argument | `wiki/arguments/journal-articles/<journal-name>/`、`wiki/arguments/books/<book-folder>/`、`wiki/arguments/reports-policy-documents/` | 按文献类型；期刊论文 Argument 按 `journal` 字段对应的期刊名称分组；书籍 Argument 再按具体书籍文件夹分组 |

文件名、文件夹名、`title`、`tags` 使用英文；正文使用简体中文。

期刊论文 Argument 的二级归档规则：

- 目标路径为 `wiki/arguments/journal-articles/<journal-name>/Argument_<Author>_<Year>_<JournalAbbrev>.md`。
- `<journal-name>` 使用条目 frontmatter 的 `journal` 全称；若期刊名称含 `/` 或 `:` 等不适合作为路径的字符，用空格替换并压缩连续空格。
- 对应 source record 的最终文件名为 `<Author>_<Year>_<JournalAbbrev>.md`，即去掉 Argument 文件名前缀 `Argument_`。

---

## 4. Naming, Aliases and Tags

### File Names and Titles

`wiki/` 条目的文件名应尽量与 frontmatter `title` 一致，使用可读英文标题，不使用全小写 slug 作为条目文件名。

- 正确：`Piaget's Theory of Cognitive Development.md`

命名规则：

- `title` 是知识对象的正式名称；文件名通常等于 `title`。
- 文件名和 `title` 不使用 tag 风格 slug。
- 标题表达归属关系时，优先使用自然英文结构，如 `Van Leeuwen's Legitimation Theory`、`Teaching Theory of Gruschka`。
- Concept / Theory / Method / Fact 的标题和文件名默认不得带括号、冒号、引号；缩写放入 `aliases` 或正文说明。
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

`aliases` 同时用于 Obsidian 检索和 `wiki_linker.py` 自动补链，因此必须精确。若 alias 产生错误链接，直接从对应条目删除后重新同步。

- Argument 不使用 `aliases`。
- Concept / Theory / Method / Fact 的 `aliases` 写中文译名、常见英文变体和缩写。
- Person 的 `aliases` 按 `template-person.md` 执行。
- 页面中某个人名第一次出现时必须使用全名；中文正文优先采用中文全名（英文全名）格式，后续再出现可按语境使用中文名、姓氏或代称。
- 单个 alias 不要中英混合；中文译名、英文变体和缩写分成不同 alias。
- 英文 alias 默认不区分大小写；不要同时写只差大小写的重复 alias。
- 不要写过短、过宽或 tag 风格 slug alias，如“资本”“文化”“教育”“政策”“课程”“能力”“国家”“公平”。
- 不要轻易写单个汉字 alias；只有该字作为独立术语有强识别度时才保留。

### Citation Index Rules

`citation/` 存放可引用 Argument 的引用索引，由 `scripts/citation_index.py` 生成。

```text
citation/
  citation_full.json          可引用 Argument 的全量索引
  citation_ambiguous.json     同一作者同一年多篇可引用文献的歧义索引
```

Citation 字段按 `wiki/templates/TEMPLATE-SPEC.md` 和对应 Argument 模板执行。Argument 保留 `year`、`doi`、可选 `isbn`、`citation_aliases` 与完整 `citation`。`citation_aliases` 由 `scripts/citation_index.py` 根据 `authors`、`year` 和完整 `citation` 自动生成。英文原始文献生成英文 APA author-year 形式；中文原始文献同时生成英文 APA 版本和中文作者年版本。英文基本形式为 `Author, Year` 与 `Author (Year)`：单作者用第一作者英文姓氏或机构英文简称，如 `Ball, 2008`；双作者用 `&`，如 `Lindblad & Popkewitz, 2004`；三位及以上作者用 `et al.`，如 `Wang et al., 2025`。中文基本形式同样只保留 `作者, 年份` 与 `作者 (年份)`；中文双作者用“和”，如 `林德布拉德和波普凯维茨, 2004`；中文三位及以上作者用“等”，如 `王等, 2025`。同一作者同一年多篇可引用文献时，`citation_index.py` 按完整 `citation`、`title`、文件路径稳定排序后自动分配 `a`、`b`、`c` 后缀。论文集章节是可引用 Argument；论文集 overview 是结构入口，不进入 citation 索引。

`doi` 用于论文、报告或有 DOI 的书籍；著作、教材、论文集或章节没有 DOI 时，`doi` 可留空，若能确认 ISBN，则写入 `isbn`。

`citation/` 索引文件由 `scripts/citation_index.py` 生成：

- `citation_full.json`：所有 `citation_aliases` 到 Argument 的查询索引。
- `citation_ambiguous.json`：无后缀基础短引用对应的重复文献组。

正文 citation 补链由 `scripts/citation_linker.py` 完成，只读取 `citation_full.json` 与 `citation_ambiguous.json`，不扫描或修改 Argument frontmatter；日常通过 `scripts/vault_index.py --standard-workflow` 统一触发。

正文引用当前 Argument 之外的已处理文献时，优先沿用原始文献的 author-year 格式。英文文献使用英文 APA，如 `Lindblad & Popkewitz (2004)`；中文文献可以使用中文作者年，如 `郑雅君 (2023)`、双作者 `作者甲和作者乙 (2023)`、三位及以上 `作者甲等 (2023)`。如果原文采用 APA 引用格式，优先保留原文中的短引用，再由 `citation_linker.py` 自动补链。

原文已有 `Author (YearSuffix: page)` 或 `Author, YearSuffix: page` 这类内部参考文献编号时，清除原文后缀，只保留作者、年份和页码，例如将 `Tandon (2005c: 30)` 写作 `Tandon (2005: 30)`。这类原文编号不写入 `citation_aliases`，不放入 `citation_ambiguous.json`，也不自动补链；只有该文献被独立处理为 Argument 后，才由本库 citation 流程重新决定是否需要 `a/b/c` 后缀。

正文引用当前 Argument 之外的已处理文献时，统一使用 APA 短引用：

- 括号式：`(Ball, 2008a)`、`(Ball, 2008a, p. 12)`、`(Ball, 2008a, pp. 12–15)`。
- 叙述式：`Ball (2008a)`、`Ball (2008a, p. 12)`、`Ball (2008a, pp. 12–15)`。

Argument 页引用当前对应文献时，只写页码，如（p.147）或（pp.147–148）。`vault_lint.py` 检查 citation 字段、`a/b/c` 冲突、正文 APA 短引用格式和歧义引用核验。

非 Argument 条目（Concept、Theory、Method、Person、Fact）引用 Argument 时，wikilink 显示文本必须包含作者与年份，可继续附页码或章节，例如 `[[Argument_Author_Year_Journal|Author, Year, p. 12]]` 或 `[[Argument_Author_Year_Journal|Author (Year, Ch. 1)]]`；不得只写 `p. 12`、`pp. 12–15`、`Ch. 1` 或裸 `[[Argument_...]]`。

### tags

- tags 全部英文、小写连字符。
- 常用前缀：`region/`、`level/`、`subject/`、`paradigm/`、`theme/`、`method/`、`theory/`、`policy/`、`source/`。

---

## 5. Script Rules and Sync Commands

脚本用于维护索引、citation 索引、补链、关系字段、source 记录和 lint 检查。`vault_index.py` 是基础索引统一入口，内部维护书籍 overview 章节表格，并依次运行 `wiki_index.py` 与 `citation_index.py`；用户确认后可用 `vault_index.py --standard-workflow` 运行补链、关系同步、索引刷新和 lint；Concept 的 `domain`、`related_count`、`related_level`、`related_stars`、`related_color` 可用 `vault_index.py --concept-fields-only` 显式同步；`wiki_index.py` 只维护普通 wiki 索引；`citation_index.py` 只维护 Argument 的 `citation_aliases` 与 `citation/` JSON；`citation_linker.py` 只维护正文 APA 短引用到 Argument 的链接；`wiki_linker.py` 只维护普通知识链接，并可继续在 YAML `authors` / `editors` 中把 APA 人名补成 Person wikilink。日常使用增量模式，非必要不使用 `--full-workflow`。

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

```bash
.venv/bin/python3 scripts/vault_lint.py --full --strict
```

移动 wiki 条目时：

- 只移动文件本身，不手动编辑 `wiki/index.json`、`wiki/index.md`、各类型索引页或 generated fields。
- 批量移动 journal article Argument 时，按 `journal` 字段创建或复用 `wiki/arguments/journal-articles/<journal-name>/`，移动后立即运行 `vault_index.py`。
- 若移动涉及正文中的 vault-root 图片路径、source record 的反向关系，或移动后索引 / 链接检查异常，再运行标准 full sync。

### Wikilink and Relation Rules

- wikilink 由 `wiki_linker.py` 自动维护，依据是 `title` 和 `aliases`。
- 页面中某个人名第一次出现时必须使用全名；中文正文优先采用中文全名（英文全名）格式，后续再出现可按语境使用中文名、姓氏或代称。
- 只有 Argument 页使用 `## 来源` / `## Sources` 章节，且只放 source wikilink。
- Argument 页的 YAML `sources` 由 `wiki_relations.py` 从 `## 来源` 章节同步。
- source record 的 YAML `extracted_to` 由 `wiki_relations.py` 从 Argument 页的 `## 来源` 章节反向同步。
- Concept / Theory / Method / Person / Fact 不写 YAML `sources` 和正文 `## 来源`；正文中的 Argument 链接同步到 `related_arguments`。

---

## 6. Source Records and Source Files

Source record 不是完整文献数据库条目，而是来源入口页。

- source record frontmatter 只保留 `citation`、`extracted_to`、`processed_date`；书籍任务可按专项 schema 额外保留必要的 `part_of`。
- source record 正文只保留一级标题和 PDF / EPUB 嵌入；不要写摘要、关键词、研究问题、作者信息、期刊信息等。
- `citation` 初始可为空；完整 citation 应在 Argument 页完成后由 `source_record.py finalize` 从 Argument frontmatter 回填。
- `extracted_to` 始终由 `wiki_relations.py` 反向同步，AI 和 `source_record.py finalize` 不手动维护。
- source record 文件名、一级标题、PDF 文件名应保持一致。
- source record 不是普通 wiki 条目，不写 `type`、`subtype`、`tags`、`status`、`related_*`。

### Source Record Commands

Source 记录与阅读页面优先由 `scripts/source_record.py` 生成。AI 先判断来源类型，再调用对应子命令；脚本不负责自动猜类型。

| 来源类型 | 子命令 | 输出位置 |
|---|---|---|
| 期刊论文 | `article` | `sources/`，有图时 finalize 后为 `sources/<论文命名>/` |
| 报告／政策文件／白皮书 | `report` | `sources/`，有图时 finalize 后为 `sources/<论文命名>/` |
| 专著整本书 source | `monograph` | `books/<book-folder>/` |
| 论文集／编著整体 overview | `edited-volume-overview` | `books/<book-folder>/` |
| 论文集章节 source | `book-chapter` | `books/<book-folder>/` |
| 从 Argument 页回填 source record | `finalize` | `sources/` 或 `books/<book-folder>/` |

常用命令形态：

```bash
.venv/bin/python3 scripts/source_record.py article --file raw/FILENAME.pdf --record-name <论文命名>
.venv/bin/python3 scripts/source_record.py report --file raw/FILENAME.pdf --record-name <论文命名>
.venv/bin/python3 scripts/source_record.py finalize --argument "wiki/arguments/.../Argument_<Author>_<Year>_<JournalAbbrev>.md" --rename

# 若创建 Argument 前判断该论文／报告需要图片占位或后续补图：
.venv/bin/python3 scripts/source_record.py finalize --argument "wiki/arguments/.../Argument_<Author>_<Year>_<JournalAbbrev>.md" --rename --with-figures
```

`finalize` 只负责从 Argument 页回填 citation、按需重命名 source record/PDF，并同步 Argument 页中的 source wikilink；`--with-figures` 会将普通论文／报告 source 移入 `sources/<论文命名>/` 并创建 `figures/`；不维护 `extracted_to`。

### Source Files

- `raw/` 只放原始 PDF，不加 frontmatter，不编辑。
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

Argument 必须详细拆解论证链：问题来源、概念或理论、前提、证据如何支持前提、中间推论如何连接到结论，以及可能存在的跳跃、弱证据或过度推论。

Argument 的 `## 论证结构` 中，每一个论证步骤都应独立成段，步骤之间使用 `---` 分割线。

语言要易懂。抽象理论必须配例子；例子优先来自原文，原文没有时可用简短教育情境说明。

Argument 引用规则：

- 引用当前 Argument 对应文献时，只写页码，如（p.147）或（pp.147–148），不写作者与年份。
- 当前文献引用其他文献时，按原引用内容直接记录，不额外添加二手引文标记，使用APA引用
- 只有引用当前 Argument 对应文献之外的独立来源时，才写作者、年份与页码。

### Writing and Template Rules

- 新建或重写条目必须读取三个文件：`wiki/templates/TEMPLATE-SPEC.md`、`wiki/templates/CALLOUTS.md`、对应 `wiki/templates/template-*.md`。
- `TEMPLATE-SPEC.md` 规定字段、写作、来源和类型结构规则。
- `CALLOUTS.md` 规定 callout 语义和 CSS contract。
- `template-*.md` 只提供具体页面骨架；有内容才写，没有内容可省略空章节。
- 模板与规范冲突时，以 `TEMPLATE-SPEC.md` 和 `CALLOUTS.md` 为准。
- 正式条目正文不要复制模板中的说明注释。

---

## 8. Extraction Criteria

提取标准只决定“是否值得建条目”。一旦新建 Concept / Theory / Method / Fact / Person，必须同步更新当前 Argument 页，在相关论证段落中用一句话提及并链接该条目；如果无法在 Argument 正文中自然提及，就不要新建，改为在 Argument 中保留纯文字说明。

### Fact

有明确时间 + 地点 + 主体的政策、事件、制度安排，应建 Fact 条目。包括政策、法案、课程纲要、白皮书、历史事件、课程改革节点、教育制度、考试制度、督学制度、分流制度。不要把具体政策或事件只当作概念例子一笔带过。

### Theory

论文提供以下任一信息时，可建 Theory 条目：明确作为理论框架；用于解释现象或论证立场；有专门章节介绍核心主张、起源、代表人物或应用方式。只被点名但无介绍时，不单独建条目，只在相关条目中链接。

### Method

论文提供以下任一信息时，可建 Method 条目：研究设计、数据收集或分析方式、方法选择的理由、认识论立场、操作步骤、适用场景或局限。方法只被命名但无介绍时，不因其定义新建或扩写 Method 条目，但实证研究仍需按下面规则记录方法案例。

除思辨类、评论类、理论建构类和概念辨析类文献外，所有实证研究都必须至少记录一条方法案例。量化、质性和混合方法研究都适用。

处理实证研究时，AI 必须识别至少一种核心研究方法，并更新对应 Method 条目的 `## 使用此方法的研究` 章节。若对应 Method 条目不存在，则新建 Method 条目。方法案例只写一句话，并链接到当前 Argument 页。

方法案例只说明该研究如何使用方法，不展开文献摘要。若文献只命名方法但没有提供方法论说明，仍可作为案例记录；但不据此扩展方法定义、研究程序或局限性。

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
- 每条新增信息附来源页码。
- 更新 frontmatter 的 `updated`，需要时更新 `confidence`。
- 不手动更新 `related_*`、Argument `sources`、source record `extracted_to`，交由脚本同步。
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

- HTML 颜色不要写 `#ccc`，改用 `rgb(204,204,204)`。
- DOI / URL 若含特殊字符，优先放 frontmatter，或用反引号包裹。
- 不在正文写内联 JS；脚本逻辑放外部文件。
- 数学公式：行内公式写 `$d = 0.40$`；独立公式写：

```markdown
$$d = ...$$
```

- 正式条目正文不要写任何注释。模板中的 HTML 注释或 Obsidian 注释只用于说明结构，生成或更新条目时不得复制进正式条目。
