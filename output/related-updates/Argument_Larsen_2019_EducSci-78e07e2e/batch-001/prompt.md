遵守 AGENTS.md、vault-schema.md；用 wiki/index.json 定位。首先完整读取现有目标条目、下列必读规范及本批模板，判断模板符合性：结构、内容归位或 Callout 不符，必须列入“重构”，不以有无新增信息为前提。不能凭记忆或沿用旧格式；规范优先于模板，不建无证据的空章节，不复制模板说明。
完整阅读指定 Argument、经 source record 定位的原文，核对链接语境与概念含义，并回查已有引用。误链、同名异义、普通词误配专业概念、仅提及而无实质讨论/应用/证据，不据此补入内容；原条目符合模板时记“不变”，否则仍按模板重构。无法核验、原文未读全或证据不足则停止，不得以“不变”冒充完成。
重构标准：原条目不符合对应模板，或新材料深化/改变认识且积累足以支持更合理结构。其余条目主要增加事实、证据、解释或细节则依原结构“补充”，无新增有效信息则“不变”。整合新旧信息，保留有效内容、重要细节与论证深度，核实差异；真实分歧纳入争议，已证实错误纠正。去重、衔接，保留页码与引用，完成后逐节对照模板检查结构、内容归位及 Callout。
只改本批非 Argument 条目正文及必要写作例外。
按目标顺序只存 {"items":["不变","重构","补充"]} 到指定 result.json。运行下方 advance，由其执行正常增量 vault_index→vault_lint 并取下一批，无须重复手动检查；失败立即停止。无需计划、进度或逐条报告，受阻说明原因。

Argument：wiki/arguments/journal-articles/Education Sciences/Argument_Larsen_2019_EducSci.md
本批类型：concept；统一模板：wiki/templates/template-concept.md
目标（按序）：
1. wiki/concepts/higher-education/International Education.md
2. wiki/concepts/instruction-pedagogy/Visible Learning.md
3. wiki/concepts/educational-philosophy/Paradigm.md

必读规范：wiki/templates/TEMPLATE-SPEC.md、wiki/templates/CALLOUTS.md

结果：/Users/shaoyangwu/Documents/MyNotes/output/related-updates/Argument_Larsen_2019_EducSci-78e07e2e/batch-001/result.json
