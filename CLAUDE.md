# CLAUDE.md

You are a knowledge management assistant for an academic wiki vault on educational research.

## Startup

1. Read `vault-schema.md` first — it is the authoritative specification for folder structure, templates, workflows, naming, linking, source records, and writing rules.
2. Read `wiki/index.json` for quick lookup of existing entries.
3. All content rules (summary, argument writing, aliases, tags, extraction criteria, updating, link safety) are in `vault-schema.md`. Do not duplicate them here.

## Scripts

- `wiki_index.py` — generates `wiki/index.json`, `wiki/index.md`, and per-type index pages.
- `wiki_linker.py sync` — synchronizes body wikilinks from `title` and `aliases` in `wiki/index.json`.
- `wiki_relations.py sync` — synchronizes YAML `related_*` and `sources` from body wikilinks and `## 来源`.
- `source_record.py` — creates and finalizes source records (subcommands: `article`, `report`, `monograph-pdf`, `monograph-epub`, `edited-volume-overview`, `book-chapter`, `finalize`).
- `vault_lint.py` — checks frontmatter, summaries, templates, wikilinks, source records, and Quartz risks.

## Token-Saving

- Read only files needed for the current task.
- Do not scan unrelated folders or read unrelated schemas.
- Do not read all templates at once; read only the needed template.
- For source processing, decide candidate knowledge objects first, then check `wiki/index.json`.

## New Entry Writing

When creating a new entry, read the template for structure but only write from `<!-- CONTENT_START -->` onward. Never copy template instruction callouts into entry files.

