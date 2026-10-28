本次只处理下列一批，完成后停止；未经用户再次指示，不获取或处理下一批。
遵守 AGENTS.md、vault-schema.md；用 wiki/index.json 定位。首先完整读取现有目标条目、下列必读规范及本批模板，判断模板符合性：结构、内容归位或 Callout 不符，必须列入“重构”，不以有无新增信息为前提。不能凭记忆或沿用旧格式；规范优先于模板，不建无证据的空章节，不复制模板说明。
完整阅读指定 Argument、经 source record 定位的原文，核对链接语境与概念含义，并回查已有引用。误链、同名异义、普通词误配专业概念、仅提及而无实质讨论/应用/证据，不据此补入内容；原条目符合模板时记“不变”，否则仍按模板重构。无法核验、原文未读全或证据不足则停止，不得以“不变”冒充完成。
重构标准：原条目不符合对应模板，必须整体“重构”；模板符合时，若新材料能够深化或改变现有认识，且已有信息足以形成更合理的论述结构，则进行整体“重构”；若主要增加事实、证据、解释或细节，则在现有结构下“补充”；无新增有效信息则“不变”。
重构必须充分整合新旧内容，保留已有的有效信息、重要细节和论证深度，避免因结构调整造成信息损失或过度概括。对新旧材料中的差异与矛盾，应先核实其来源、证据及适用条件。确有学术分歧的，保留不同观点并纳入“争议”部分；已经证实的事实性错误则直接纠正。
无论重构还是补充，都应检查新旧内容的衔接，消除重复论述，保留页码与引用；完成后逐节对照模板检查结构、内容归位及 Callout。
确认误链时运行 .venv/bin/python3 scripts/wiki_linker.py exclude <所在条目路径> --sentence '<完整可见句子>' --target '<目标路径>' --record-only 登记，普通补链时去除，保留本任务 Argument 快照；仅提及不记例外。只改本批非 Argument 条目正文及必要例外记录。
按目标顺序将等量状态写入指定 result.json 的 items 数组，每项只能为“不变／重构／补充”之一，不写其他字段。运行下方 accept，由其执行正常增量 vault_index→vault_lint 并登记本批完成，无须重复手动检查；随后停止，失败也停止。无需计划、进度或逐条报告，受阻说明原因。

Argument：wiki/arguments/journal-articles/European Educational Research Journal/Argument_Grek_2024_EERJ.md
本批类型：concept；统一模板：wiki/templates/template-concept.md
目标（按序）：
1. wiki/concepts/comparative-education/European Education Space.md
2. wiki/concepts/university-industry-collaboration/Knowledge Production.md
3. wiki/concepts/political-economy-geopolitics/Governing by Numbers.md
4. wiki/concepts/sociology-of-education/Data Infrastructure.md
5. wiki/concepts/comparative-education/Subsidiarity Principle.md

必读规范：wiki/templates/TEMPLATE-SPEC.md、wiki/templates/CALLOUTS.md

结果：/Users/shaoyangwu/Documents/MyNotes/output/related-updates/Argument_Grek_2024_EERJ-a075f690/batch-002/result.json
