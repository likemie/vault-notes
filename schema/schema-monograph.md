# Schema：专著（Monograph）

触发标识：用户说明材料为专著、著作或整本书研究。

---

## 核心原则

- 每次只处理用户当前发送的一章。
- 处理开始时确定 `<book-folder>`，并使用 `books/<book-folder>/` 与 `wiki/arguments/books/<book-folder>/`。
- 整本书处理完成前，不创建 source 记录，不创建阅读页面。
- 章节处理结果累积到全书 Argument 的「各章概览」和「关键引用」。
- 全书 Argument 使用 `wiki/templates/template-argument-monograph.md`。
- Concept / Theory / Method / Fact / Person 条目不写 YAML `sources` 和正文 `## 来源`；来源性陈述通过 Argument 链接进入 `related_arguments`。
- 图片、表格、新建条目提及规则和脚本运行规则按 `vault-schema.md` 执行。

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
```

`<book-folder>` 使用 `Author_Year_Publisher` 或稳定的英文书籍短名。

---

## 单章记录

「各章概览」只记录章节在全书论证中的位置，不写成完整小型笔记。

```markdown
### 第X章 章节标题

#### 章节问题

说明该章要回答的问题，或它在全书论证中的位置。

#### 论证链条

按前提、证据、中间推论、结论拆解章节论证。每一个论证步骤独立成段，步骤之间使用分割线。
```

关键引用写入「关键引用」章节，使用双语无外层引号格式，标注章节与页码。没有页码时只标注章节，不编造页码。

---

## 单章处理流程

1. 读取 `vault-schema.md` 和 `schema/schema-monograph.md`。
2. 只处理当前章节文本。
3. 扫描可提取或更新的 Concept / Theory / Method / Person / Fact / Argument。
4. 读取 `wiki/index.json` 判断候选条目是否已存在。
5. 更新已有条目或按模板新建条目。
6. 更新或新建 `wiki/arguments/books/<book-folder>/Argument_<book-folder>.md`。
7. 将当前章节整合进「各章概览」，将代表性引用整合进「关键引用」。
8. 在 `## 来源` 列出 source wikilink。
9. 执行 `vault-schema.md` 的脚本运行规则。
10. 当前章节处理完成后停止。

---

## Source 记录和阅读页面

用户提供整合后的 PDF / EPUB 并要求建立 source 记录时，文件放在：

```text
books/<book-folder>/<book-folder>.<ext>
```

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

EPUB source record 使用已配置的 epub.js 阅读器容器：

```html
<div id="epub-viewer" style="width:100%;height:560px;border:1px solid rgb(204,204,204);" data-epub="/books/<book-folder>/<book-folder>.epub"></div>
```

---

## 整合全书 Argument

1. 读取全书 Argument 的「各章概览」。
2. 读取 `wiki/templates/template-argument-monograph.md`。
3. 提炼全书研究问题、理论框架、研究方法、论证结构、主要发现、关键引用和自述局限。
4. 从各章概览筛选代表性发现与引用，不机械搬运全部章节记录。
5. 保留「各章概览」作为章节处理记录。
6. 执行 `vault-schema.md` 的脚本运行规则。
