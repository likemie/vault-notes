# Schema：专著（Monograph）

触发标识：用户说明材料为专著、著作或整本书研究。

---

## 核心原则

- 模板读取顺序统一为 `wiki/templates/TEMPLATE-SPEC.md` → `wiki/templates/CALLOUTS.md` → 对应 `wiki/templates/template-*.md`。
- 每次只处理用户当前发送的一章。
- 处理开始时确定 `<book-folder>`，并使用 `books/<book-folder>/` 与 `wiki/arguments/books/<book-folder>/`。
- Argument 粒度按用户指定。
- 合法粒度：
  - `single-argument`：整本书只维护 `Argument_<book-folder>.md`，章节处理结果累积到该页。
  - `chapter-arguments`：`Argument_<book-folder>.md` 作为全书 overview，每章另建或更新独立章节 Argument。
- 采用 `single-argument` 时，章节处理结果累积到全书 Argument 的「章节推进」和「关键引用」，并在整合阶段提炼「跨章综合」。
- 采用 `chapter-arguments` 时，全书 Argument 只记录全书问题、总体论证、章节索引和跨章综合；章节细节写入章节 Argument。
- 全书 Argument 使用 `wiki/templates/template-argument-monograph.md`。
- 图片、表格、新建条目提及规则和脚本运行规则按 `vault-schema.md` 执行；基础索引统一运行 `.venv/bin/python3 scripts/vault_index.py`。

---

## 文件夹结构

```text
books/
  <book-folder>/
    <book-folder>.<ext>
    <book-folder>.md
    figures/
      Figure_X-X_Descriptive_Name.jpg

wiki/arguments/books/<book-folder>/
  Argument_<book-folder>.md
  Argument_<book-folder>_Ch01.md        # 仅在用户指定分章节 Argument 时使用
```

`<book-folder>` 使用 `Author_Year_Publisher` 或稳定的英文书籍短名。

---

## 单章记录粒度

采用 `single-argument` 时，「章节推进」只记录章节在全书论证中的位置，不写成完整小型笔记。

```markdown
### 第X章 章节标题

> [!chapter-question]
> 说明该章要回答的问题，或它在全书论证中的位置。

#### 论证链条

按前提、证据、中间推论、结论拆解章节论证。每一个论证步骤独立成段，步骤之间使用分割线。
```

关键引用写入「关键引用」章节，优先使用 `[!citation-card]`，标注章节与页码。没有页码时只标注章节，不编造页码。

采用 `chapter-arguments` 时：

- `Argument_<book-folder>.md` 是全书 overview，保留章节索引表或「各章概览」短条目，每章链接到对应章节 Argument；章节链接骨架和一致性检查由 `scripts/vault_index.py --book-only` 维护。
- 章节 Argument 文件名使用 `Argument_<book-folder>_ChXX.md`；若章节需要更强可读性，可在 `ChXX` 后追加稳定英文短标题。
- 章节 Argument 属于同一本专著，不是独立文献；章节归属和引用短名由 `scripts/citation_index.py` 自动维护。
- 章节 Argument 记录该章问题、论证链条、证据/案例、关键引用和本章创建或更新的知识条目。
- 当前章节新建的 Concept / Theory / Method / Fact / Person 必须在对应章节 Argument 正文中至少出现一次 wikilink；overview 可只链接章节 Argument 和最核心跨章条目。

---

## 单章处理流程

1. 读取 `vault-schema.md`、`wiki/templates/TEMPLATE-SPEC.md`、`wiki/templates/CALLOUTS.md` 和 `schema/schema-monograph.md`。
2. 只处理当前章节文本。
3. 确认用户指定的 Argument 粒度：`single-argument` 或 `chapter-arguments`；未指定则先询问。
4. 扫描可提取或更新的 Concept / Theory / Method / Person / Fact / Argument。
5. 读取 `wiki/index.json` 判断候选条目是否已存在。
6. 更新已有条目；新建条目时读取对应 `wiki/templates/template-*.md`。
7. 读取并使用 `wiki/templates/template-argument-monograph.md`。
8. 若采用 `single-argument`，更新或新建 `wiki/arguments/books/<book-folder>/Argument_<book-folder>.md`，将当前章节整合进「章节推进」，将代表性引用整合进「关键引用」。
9. 若采用 `chapter-arguments`，更新或新建当前章节 Argument，并在 `Argument_<book-folder>.md` 中维护章节索引、章节短摘要和跨章综合。
10. 若整本书 source record 已创建，在相关 Argument 的 `## 来源` 列出 source wikilink；尚未创建时暂不编造来源链接。
11. 执行 `vault-schema.md` 的脚本运行规则，即运行 `.venv/bin/python3 scripts/vault_index.py`。
12. 当前章节处理完成后停止。

---

## Source 记录和阅读页面

用户提供整合后的 PDF / EPUB 并要求建立 source 记录时，文件放在：

```text
books/<book-folder>/<book-folder>.<ext>
```

PDF / EPUB 是本地阅读副本，保留在 `books/<book-folder>/`，但不进入 git；同一路径的文件需要同步到 NAS，并按 `https://img.mylikemie.icu/books/<book-folder>/<文件名>` 发布。`source_record.py` 会同时生成本地阅读入口和 NAS 在线阅读入口。

PDF：

```bash
.venv/bin/python3 scripts/source_record.py monograph-pdf \
  --book-folder <book-folder> \
  --file books/<book-folder>/<book-folder>.pdf \
  --citation "Author, A. A. (Year). Book title. Publisher."
```

EPUB：

```bash
.venv/bin/python3 scripts/source_record.py monograph-epub \
  --book-folder <book-folder> \
  --file books/<book-folder>/<book-folder>.epub \
  --citation "Author, A. A. (Year). Book title. Publisher."
```

EPUB source record 使用已配置的 epub.js 阅读器容器；本地 viewer 指向 vault 内文件，在线 viewer 指向 NAS：

```html
<div id="epub-viewer" style="width:100%;height:560px;border:1px solid rgb(204,204,204);" data-epub="/books/<book-folder>/<book-folder>.epub"></div>
<div id="epub-viewer-online" style="width:100%;height:600px;border:1px solid rgb(204,204,204);" data-epub="https://img.mylikemie.icu/books/<book-folder>/<book-folder>.epub"></div>
```

---

## 整合全书 Argument

1. 读取全书 Argument 的「章节推进」；若采用 `chapter-arguments`，同时读取已处理章节 Argument。
2. 读取 `wiki/templates/TEMPLATE-SPEC.md`、`wiki/templates/CALLOUTS.md` 和 `wiki/templates/template-argument-monograph.md`。
3. 提炼全书研究问题、理论框架、研究方法、论证结构、主要发现、关键引用和自述局限。
4. 从各章概览筛选代表性发现与引用，不机械搬运全部章节记录。
5. 保留「章节推进」作为章节处理记录。
6. 执行 `vault-schema.md` 的脚本运行规则，即运行 `.venv/bin/python3 scripts/vault_index.py`。
