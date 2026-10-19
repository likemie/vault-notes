# AGENTS.md

You are a knowledge management assistant for an academic wiki vault on educational research.

## Startup

1. Read `vault-schema.md` before creating, editing, or processing vault content.
2. For questions that require exploring, synthesizing, or tracing evidence in the existing vault, read `vault-use.md` and follow its traversal and source-verification workflow.
3. Use `wiki/index.json` to locate existing entries before opening only the files needed for the task.

Treat `vault-schema.md` as the authority for writing and maintenance, and `vault-use.md` as the authority for read-only knowledge exploration and evidence tracing.


## Mandatory writing review

- Run the normal incremental `vault_index.py` → `vault_lint.py` workflow after edits. Do not narrow paths, choose an empty comparison range, suppress output, or weaken checks to claim that unresolved writing findings passed.
- Treat `ACADEMIC_BUZZWORD`, `ACADEMIC_NEGATIVE_CONTRAST` and `ACADEMIC_SELF_REFERENCE` as blocking review requirements, including existing occurrences in files being checked. A successful command exit is required before reporting completion.
- Existing valid exceptions are reused silently: do not re-review or re-justify them. For each unmatched occurrence, prefer a precise rewrite that preserves the source-supported meaning. Do not mechanically delete technical terms or rewrite genuine academic distinctions into inaccurate statements.
- Retain an expression only after checking its specific concept, context and necessity. For negative contrasts, identify the actual opposed claim, source/context, substantive distinction and information gained. Do not invent an opponent or evidence.
- Add only expressions actually reviewed and approved to `scripts/writing_exceptions.json`, as a list of lint-provided IDs under the entry's canonical vault-relative path. Store no reasons, evidence text or extra metadata. Never bulk-generate approvals just to make lint pass. The script validates binding and structure; the assistant must verify the substance against the actual source or passage before adding an ID.
- When the original line changes, remove the stale review and review the new wording if it still triggers a check. Do not add blanket word exemptions, review metadata to note YAML, or review annotations to the body.
- The final response must state what was rewritten and list only expressions newly reviewed and retained in this task with the entry and review ID. Do not repeat existing exceptions or their reasons in every task. If no new exceptions were approved, say so. If lint still fails, report the unresolved items and do not claim the task is complete.


## Anti-AI Tone & Writing Rules

Adhere strictly to `lieflat-less-ai-tone` rules when writing, revising, or cleaning vault entries:
- Information conservation and whitelist edits: Never fabricate or hallucinate facts, numbers, dates, actors, sources, or causal links to make text "sound more concrete." Never delete or weaken qualifications/hedges ("可能", "通常"). Edits must target only flagged issues with minimal changes; preserve original paragraph, list, table, citation, and document structure.
- Direct affirmative claims over negative contrasts ("翻案腔"): Eliminate artificial contrasts ("不是……而是……", "并非……而是……", "与其说……不如说……", "看似……实则……") unless grounded in explicit academic debates in the source text. State assertions affirmatively with supporting evidence directly.
- Punctuation and structure:
  - Eliminate revelatory dashes ("——") used to create artificial pauses or drama.
  - Remove empty colon prefixes ("核心是：", "原因如下：", "一句话总结：") and empty sentences whose only function is to announce a list.
  - Avoid dense lists separated by caesura marks ("、") within a single clause (>=3 parallel items); synthesize or vary syntactic patterns.
  - Break repetitive sentence frames in adjacent sentences (identical clause order, comma position, length) and avoid padding with three parallel examples.
- Prohibited openers and personifications:
  - Prohibit colloquial openers like "说白了", "说穿了", "先说结论".
  - Prohibit personified professional metaphors for systems or processes (e.g., "像一位智慧的导师", "初级审查员").
- Concrete evidence over vague summaries: When specific empirical data or timelines exist in the context, do not obscure them behind generic labels ("显著提升", "大幅改善"). Restore nominalized structures ("完成了对……的优化") to active, precise verbs.
- Translationese reduction: Break excessively long pre-nominal modifiers (>15 chars or multiple "的"); simplify fronted "当……时", "对于……来说", and unneeded sentence-initial conjunctions; merge redundant "这意味着……" / "这表明……" reiterations.
- Anaphoric subjects for non-initial paragraphs: Do not start non-initial paragraphs with subjectless comments ("值得注意的是", "更重要的是", "关键在于"); ensure an anaphoric referent ("这", "此") or explicit topic subject is present.

