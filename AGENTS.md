# AGENTS.md

## Mission

This repository is an evidence-based personal knowledge management system.
Assist with capture, validation, synthesis, linking, indexing, and review
without damaging source provenance.

## Authority

1. Read `SCHEMA.md` before every wiki operation.
2. `SCHEMA.md` overrides README files and agent assumptions.
3. Before creating canonical knowledge, inspect `index.md` and recent `log.md`.
4. Prefer updating an existing page over creating a duplicate.

## Source Safety

- Treat all Markdown bodies under `raw/` as immutable evidence.
- Do not rewrite, normalize, translate, summarize in place, or rename imported raw files.
- Never invent source paths.
- A canonical `sources` entry must resolve to a real Markdown file under a registered `raw/` directory.
- Attachments, images, and PDFs alone are not canonical sources.
- Put corrections and interpretations in canonical pages, not in raw evidence.

## Canonical Knowledge

Canonical pages may exist only under:

- `entities/`
- `concepts/`
- `comparisons/`
- `queries/`

Every canonical page must include:

- `title`
- `created`
- `updated`
- `type`
- `tags`
- `sources`
- `confidence`
- `contested`
- `contradictions`

The directory and `type` must match.

## Linking

When canonical pages exist, each active canonical page must link to at least
two distinct active canonical pages other than itself.

Do not count links to raw files, templates, archived pages, missing pages,
or headings in the same page.

## Atomic Wiki Operations

For every canonical create, update, archive, delete, or filed query:

1. Update the canonical page.
2. Synchronize `index.md`.
3. Append one entry to `log.md`.

Never rewrite or remove prior log entries.

## Human Approval

NotebookLM, knowledge graphs, and LLM suggestions are discovery candidates.
Do not promote hypotheses into durable canonical knowledge without
human verification against the source evidence.

## Cost and Context Rules

- Use the lowest-cost capable model for exploration and summarization.
- Use Claude only for difficult architecture, contradiction analysis, or final review.
- Search filenames and headings before loading entire directories.
- Avoid repeatedly reading unchanged large files.
- Keep optional MCP servers disabled unless the current task needs them.
- Summarize tool output before passing it to another model.

## Tool Roles

| Tool | Primary Use |
|---|---|
| OpenCode + Kimi | Markdown cleanup, document drafting, repetitive tasks, repo summary |
| Claude Code | Architecture, complex debugging, multi-file refactoring, final review |
| Codex | Code implementation, bug fix, feature addition, Git analysis |
| Gemini | Cross-validation, summarization, alternative exploration |
