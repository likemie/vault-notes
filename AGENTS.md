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
