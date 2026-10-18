这是关联条目更新任务。请直接执行下述审读和更新要求，无须分析或修改 related_update.py。

你正在维护一个教育研究学术知识库。本任务是更新关联条目正文，不是手动刷新 related_* 字段。
本指令适用于当前会话中的任何 AI，不限定产品、模型或命令行工具。由当前 AI 使用本地文件与终端工具直接完成任务；不需要安装或调用 Codex CLI，也不需要为脚本配置模型 API。
仅更新 Concept、Theory、Method、Instrument、Person、Fact。排除 related_arguments 及正文中的所有 Argument 目标；Argument 只作为阅读、引用和证据追溯材料，不修改其正文。

先读取 AGENTS.md、vault-schema.md、vault-use.md；用 wiki/index.json 定位条目。读取 wiki/templates/TEMPLATE-SPEC.md、wiki/templates/CALLOUTS.md 和每个目标类型的最新模板。

完整阅读指定 Argument 和它对应的原文（通过 Argument 的来源章节、sources 和 source record 定位 PDF / EPUB，不把 Argument 当原文）。完整阅读本批每个现有知识条目，先执行下述关联性核验；通过后，再沿其引用回查已有 Argument 和支持相关主张的原文上下文。只读到提炼或摘要时不得声称核验了原文。原文缺失、无法完整阅读或关键证据不足时停止，简报阻碍并保持本批未完成，不用常识补齐，也不能填“不变”冒充完成。

更新前先核验关联是否成立：

- 在指定 Argument 中定位指向目标的链接及其上下文，对照原文和目标条目的定义、对象与适用范围，核实是否指向同一个知识对象。related_* 或双链只能提供候选，不能证明需要更新。
- 若为误链、同名异义或普通词义被错误映射到专业概念，只记“不变”；跳过该条目的内容、格式和 Callout 更新，不另写理由。
- 若原文只是使用、列举或顺带提到某个词，没有实质讨论对应知识对象，也没有可用于该条目的定义、论证、证据、实际方法应用或案例，只记“不变”，跳过更新。例如，“假设某种情况”中的普通用词，不足以更新“研究假设”条目。
- 不以出现频率、链接数量或词形匹配代替关联判断；实质讨论也不要求单设章节。原文确实说明了该知识对象，或提供了可核验的实际应用与证据时，才继续判断是否补充或重构。
- 对已确认的误链，本任务不改写 Argument，也不手工删除或改写 related_*。已核实的跳过项属于正常完成；关联含义仍无法核实时停止，保持本批未完成。

对于本批的每个目标，执行以下要求：

请完整阅读原文及现有知识库条目，判断当前积累的信息是否足以支持结构性重构，还是仅需补充完善。若新材料能够深化或改变现有认识，且已有信息足以形成更合理的论述结构，则进行整体重构；若主要增加事实、证据、解释或细节，则在现有结构下补充。
重构必须充分整合新旧内容，保留已有的有效信息、重要细节和论证深度，避免因结构调整造成信息损失或过度概括。对新旧材料中的差异与矛盾，确有学术分歧的，保留不同观点并纳入“争议”部分；已经证实的事实性错误则直接纠正。
无论重构还是补充，都应检查新旧内容的衔接，消除重复论述。按照wiki/templates里对应的模板统一排版及 Callout 格式，确保条目的信息完整性、逻辑连贯性和学术准确性。

具体执行边界：

- 本批逐项审读，误链和仅提及项记“不变”；关联成立但没有新增有效信息的条目也记“不变”，不强行增补或仅为统一格式修改被跳过的条目。
- 重构前在内部核对现有有效内容及其来源，完成后核对保留情况；不另写内容清单或论证报告。按规范精确修改已有文件。
- 正文保留页码和完整的文献引用关系；临时记录不重复抄写来源、原文范围、改写细节或分析过程。
- 仅修改本批列出的目标正文及必要的写作例外记录。不要改写指定 Argument、无关条目或本任务的 state.json；生成字段由规范脚本维护。不要提交、推送、启动其他 AI 会话或子代理。当前聊天执行时，允许按照输出的命令调用 related_update.py 的 accept 和 next 推进本任务；不要调用 run-codex 或其他 AI 命令行启动另一个 AI，也不要递归创建新任务。
- 不手工维护 related_*、Argument sources、source record extracted_to，不自动运行标准补链/关系同步流程。
- 有效写作例外静默复用；未匹配的写作用词和否定转折须逐项实质审查，优先准确改写。禁止批量批准 ID 或弱化检查。
- 结束前依次运行 .venv/bin/python3 scripts/vault_index.py 和 .venv/bin/python3 scripts/vault_lint.py，使用正常增量范围，不限定路径、不压制输出。失败时报告全部未解决项，不声称完成，也不修改无关的并行工作来清零检查。
- result.json 只填写三种状态，严格按下方目标顺序逐项对应，例如 {"items":["不变","重构","补充"]}。不写路径、理由、来源、核验标记、修改说明或其他字段；不遗漏目标。只有本批全部完成实际阅读和处理后才保存完整结果并运行 accept，受阻时不填写完成状态。
- 临时文件和聊天都不另写逐条长报告，不复述提示词、schema 或已写入正文的内容。每批完成后简报进度；最终仅简报重构、补充、跳过数量及未解决项，并按 AGENTS.md 报告本次新增写作例外或明确无新增。


指定 Argument：wiki/arguments/journal-articles/Educational Philosophy and Theory/Argument_Rømer_2018_EPT.md

本批目标（逐项完成）：
1. wiki/concepts/research-methodology/Reflexivity.md（concept；Reflexivity）
2. wiki/concepts/educational-philosophy/Disciplina and Doctrina.md（concept；Disciplina and Doctrina）
3. wiki/concepts/educational-philosophy/Falsification.md（concept；Falsification）

本批结果 schema：/Users/shaoyangwu/Documents/MyNotes/output/related-updates/Argument_Rømer_2018_EPT-20261018-101735/batch-010/batch-result.schema.json
手动在聊天中执行时，将符合 schema 的最终 JSON 保存到：/Users/shaoyangwu/Documents/MyNotes/output/related-updates/Argument_Rømer_2018_EPT-20261018-101735/batch-010/result.json
