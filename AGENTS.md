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

## Domain Focus

This wiki's primary knowledge domain is **drone technology**. Prioritize evidence and canonical pages within these eight subject areas:

| Tag | Scope |
|---|---|
| `drone` | General drone systems — airframes, flight, regulations, mission |
| `datalink` | RF, LTE, MAVLink, C2 link, telemetry architecture |
| `swarm` | Multi-drone coordination, formation, task allocation, consensus |
| `voice-control` | Natural language / voice command interfaces for drone operation |
| `drone-hw` | Hardware — FC, ESC, motors, batteries, sensors, cameras, payloads |
| `drone-sw` | Firmware (PX4/ArduPilot), GCS, middleware, SDK, ROS/ROS2, MAVROS/MAVROS2 |
| `drone-ai` | Computer vision, autonomous flight, SLAM, detection, segmentation |
| `ai-agent` | AI agent architectures, autonomous decision-making, multi-agent |

All tags must be registered in `SCHEMA.md` before use in canonical frontmatter.

## Tool Roles

| Tool | Interface | Primary Use |
|---|---|---|
| OpenCode + Kimi K2 | Terminal (`opencode`) | Markdown cleanup, document drafting, llm-wiki compile, repetitive tasks |
| Claude Code | Terminal (`claude`) | Architecture, complex analysis, contradiction review, final judgment |
| Codex | Terminal (`codex`) | Code implementation, bug fix, Git analysis, drone code exploration |
| Gemini Code Assist | VS Code sidebar | Cross-validation, summarization, alternative perspective |
| GitHub Copilot | VS Code inline | Autocomplete while editing Markdown/code, inline writing assist |
