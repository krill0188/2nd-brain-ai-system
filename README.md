# 2nd Brain AI System

**English** | [한국어](README.ko.md)

> A drone-domain knowledge management system built on Markdown and Git — powered by **Hermes Agent automation + 5-AI tool stack + a human-approved AI research loop**.

## Project Overview

This project is a personal knowledge management system specialized in **drone technology** (8 subject areas: drone / datalink / swarm / voice-control / drone-hw / drone-sw / drone-ai / ai-agent). It implements a continuous **capture → compile → discovery → human decision** workflow using plain Markdown files — compatible with Obsidian, VS Code, GitHub, and any Markdown-compatible tool.

Built on [ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template) with a custom AI tool layer, Hermes Agent automation, and an AI research loop (`research/`).

### Architecture

The system consists of four knowledge layers: **Evidence → Canonical Memory → Discovery → Human Decision**. Raw source material is preserved as immutable evidence under `raw/`; reusable knowledge is compiled into canonical Markdown with traceable provenance.

An **Automation Control Plane** (Hermes Agent + llm-wiki skill) handles scheduled ingestion, compilation, and lint automatically. **Routine daily-ingest compilation has no pre-approval step** — the llm-wiki skill compiles canonical pages immediately once its own conditions are met, logs the change to `log.md`, and a daily Telegram report notifies the master of what was created (visibility, not a blocking gate). **The only place human approval actually blocks finalization is the `research/` AI research loop** — AI-generated hypotheses/insights require the master to explicitly `approve` via `research-run.sh` and to name specific claims via `research-promote.py` before anything reaches canonical (see "AI Research Loop" below).

![Master 2nd Brain AI System Architecture](docs/architecture/master-ai-architecture.png)

### Operating Workflow

There are two separate paths.

1. **Routine compilation path (no pre-approval)**: Capture → Hermes Cron (`fetch-inbox.sh`) → llm-wiki auto-compiles → logged to `log.md` → daily 07:30 Telegram post-hoc notification (list of new pages). `scripts/gate-c-analyze.sh` (graph structural gap analysis) runs separately and periodically.
2. **AI research loop (pre-approval enforced)**: research goal → Planner→Retriever→Hypothesis→Critic→Verifier→Report (5 LLM calls) → master approval (`approve`/`reject`) → individually-selected claim promotion (`research-promote.py`). Only this path actually blocks canonical writes pending approval.

![Master 2nd Brain Operating Workflow](docs/workflow/master-workflow.png)

### Technology Stack

The stack combines Hermes Agent automation with five AI tools, each assigned to a distinct role. Open-format Markdown, provenance metadata, and Git history are the durable assets; AI tools and automation engines are the replaceable layer.

![Master 2nd Brain Technology Stack](docs/tech-stack/master-tech-stack.png)

---

## Automation Control Plane — Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) (v0.19.0) serves as the automation backbone, replacing the manual compilation loop with a scheduled pipeline.

| Role | Tool | Trigger | Status |
| --- | --- | --- | --- |
| **Daily ingestion** | Hermes + llm-wiki skill (`b1a360fce35d`) | Cron `0 4 * * *` — scans `inbox/`, compiles canonical candidates | ✅ Active |
| **Weekly lint** | Hermes + wiki audit (`91acb1c73884`) | Cron `0 5 * * 1` — checks orphans, broken links, stale pages, SHA-256 drift | ✅ Active |
| **Weekly summary** | Hermes gateway (`bd81d81bca5f`) | Cron `0 9 * * 1` — delivers weekly knowledge digest to Telegram | ✅ Active |
| **Morning check + new-page notice** | `scripts/morning-report.sh` (`8fad48c5176d`) | Cron `30 7 * * *` — chain health check + list of canonical pages created that day (tagged auto-generated vs. research-loop-approved), sent via Telegram | ✅ Running |

### Registering Cron Jobs

Set up the skill symlink then register all three jobs via CLI:

```bash
# Skill symlink (displays as custom/llm-wiki-ains in Hermes UI)
mkdir -p ~/.hermes/skills/custom
ln -s ~/.hermes/skills/research/llm-wiki ~/.hermes/skills/custom/llm-wiki-ains

# Daily ingestion — 04:00 every day
hermes cron create "0 4 * * *" \
  "raw/inbox/ scan → llm-wiki compile → canonical candidate. Move processed to raw/inbox/processed/. Summary: N collected, N compiled, N failed. If empty: exit silently." \
  --name "2nd-daily-ingest" --skill "custom/llm-wiki-ains" \
  --workdir "$(pwd)" --deliver telegram

# Weekly lint — Monday 05:00
hermes cron create "0 5 * * 1" \
  "Audit all canonical docs in ~/2nd. Check: orphan pages, broken wikilinks, missing frontmatter fields, stale updated dates. Output violations as filename + reason list per SCHEMA.md. No auto-fix. If clean: 'lint passed — N pages checked'." \
  --name "2nd-weekly-lint" --skill "custom/llm-wiki-ains" \
  --workdir "$(pwd)" --deliver telegram

# Weekly summary — Monday 09:00
hermes cron create "0 9 * * 1" \
  "Read ~/2nd/log.md for this week's changes. Format: new docs N / updated N / lint result one line. Top 3 topics. Next week collection priority: drone-sw → datalink → drone-ai." \
  --name "2nd-weekly-summary" \
  --workdir "$(pwd)" --deliver telegram
```

Verify registration: `hermes cron list`

### Telegram Integration — 3 Points (not an approval gate — a notification/query channel)

```
[Point 1: Input]         Master → Telegram → Hermes → raw/inbox/
[Point 2: Post-hoc]      Hermes Cron → Telegram (07:30): "8 new canonical pages auto-created today"
[Point 3: Query]         Master → Telegram → Hermes → wiki search → answer
```

> ⚠️ Telegram here is a **post-hoc notification/query channel, not a blocking approval gate**.
> Daily-ingest does not wait for a Telegram reply — it updates `index.md`/`log.md` immediately.
> The only point where approval actually blocks finalization is `research-run.sh approve` /
> `research-promote.py` in the AI research loop below (CLI-based, not Telegram).

---

## AI Tool Roles

Five tools are configured for this system — each with a distinct responsibility defined in [AGENTS.md](AGENTS.md).

| Tool | Interface | Primary Role |
| --- | --- | --- |
| **Hermes + llm-wiki** | Gateway / Cron | Automated ingestion, compilation, lint (finalized immediately, no pre-approval), Telegram notice afterward |
| **OpenCode + Kimi K2** | Terminal (`opencode`) | Manual compile assist, document drafting, large-batch editing |
| **Claude Code** | Terminal (`claude`) | Architecture analysis, contradiction review, running the AI research loop (Planner–Report) |
| **Codex** | Terminal (`codex`) | Drone firmware exploration (PX4/ArduPilot/ROS2), code-to-raw pipeline |
| **GitHub Copilot Chat** | VS Code sidebar (`@workspace`) | Cross-validation, alternative perspective, summarization — reads workspace files directly |
| **GitHub Copilot Inline** | VS Code inline | Autocomplete while writing Markdown or code |
| **Understand Anything** | Hermes skill / Claude Code | Gate C — knowledge graph generation, gap analysis, structural observation |

> **Cost principle**: Route repetitive compile tasks to Hermes/Kimi K2. Reserve Claude for architecture decisions and contradiction resolution. GitHub Copilot (inline + Chat) is free — use freely during editing and cross-validation.

---

## Drone Domain Coverage

The primary knowledge domain is **drone technology** across 8 registered tag categories (see [SCHEMA.md](SCHEMA.md) and [docs/domain/drone-domain-guide.md](docs/domain/drone-domain-guide.md)).

| Tag | Scope |
| --- | --- |
| `drone` | General systems — airframes, flight mechanics, regulations, mission planning |
| `datalink` | RF, LTE, MAVLink telemetry, C2 link, encryption |
| `swarm` | Multi-drone coordination, formation flight, consensus algorithms |
| `voice-control` | Natural language / voice command interfaces for drone operation |
| `drone-hw` | Hardware — FC, ESC, motors, batteries, LiDAR, cameras, payloads |
| `drone-sw` | PX4, ArduPilot, GCS, MAVSDK, ROS/ROS2, MAVROS/MAVROS2, uORB |
| `drone-ai` | Computer vision, autonomous flight, SLAM, object detection, segmentation |
| `ai-agent` | AI agent architectures, autonomous decision-making, multi-agent systems |

Collection priority: `drone-sw` → `datalink` → `drone-ai` → `swarm` → others.

---

## Key Features

| Feature | Description |
| --- | --- |
| **Automated ingestion pipeline** | Hermes Agent cron scans `raw/inbox/` daily at 04:00 and runs the llm-wiki skill, which compiles and **finalizes canonical pages immediately, with no pre-approval step**. A 07:30 morning report notifies the master via Telegram of what was created that day, after the fact. |
| **AI research loop — the actual human approval gate** | Approval only blocks finalization in `research/`: a research session (Planner–Report) produces a draft, the master must explicitly `approve` it via `research-run.sh`, and must name specific claims via `research-promote.py --items` for them to reach canonical. `fact`-type claims (restating an existing source) are refused outright. |
| **Source and provenance preservation** | Capture papers and web material with Zotero and Obsidian Web Clipper, then preserve the source, metadata, and SHA-256 digest under `raw/` so every claim can be traced to evidence. |
| **Verified knowledge compilation** | Hermes llm-wiki skill and OpenCode + Kimi K2 structure source material into entity, concept, comparison, and query documents with provenance, confidence ratings, and contradiction tracking. |
| **Connected Markdown editing** | Read and edit durable knowledge in Obsidian using wikilinks and backlinks; GitHub Copilot inline assists while editing. |
| **Multi-AI cross-validation** | Claude Code and GitHub Copilot Chat (`@workspace`) can provide independent analysis of the same evidence — but this is a manual check a human runs when warranted, not an automatic gate that runs before daily-ingest compilation. |
| **Drone code exploration** | Codex navigates PX4, ArduPilot, ROS2/MAVROS2, and MAVSDK source code; results are saved to `raw/inbox/` and picked up by Hermes for compilation. |
| **Knowledge graph (Gate C)** | Understand Anything `understand-knowledge` skill analyzes the wiki and produces an interactive knowledge graph (`.ua/knowledge-graph.json`) — clusters, gaps, and structural weak links surfaced automatically. Open the local viewer with `open .ua/graph.html` (force-directed, interactive, works offline). |
| **Gate C v2 — AI gap analysis** | `scripts/gate-c-analyze.sh` reads the knowledge graph, pre-processes structure stats (layer density, isolated nodes, high-degree hubs, disconnected layer pairs), and pipes them to `claude -p` for AI interpretation. Output is a Telegram-formatted gap report saved to `.ua/gap-report.md`. Run with `--deliver` to push via Hermes. |

---

## Prerequisites

### Capture Tools

| Category | Tool | Purpose |
| --- | --- | --- |
| Required | [Obsidian](https://obsidian.md/download) | Open this repository as a local vault to browse and edit Markdown. |
| Paper capture | [Zotero + Zotero Connector](https://www.zotero.org/download/) | Scrape papers from the browser → Zotero library → `python3 scripts/zotero-ingest.py` → `raw/papers/<topic>/`. Requires Zotero Settings → Advanced → "Allow other applications" enabled. |
| Web capture | [Obsidian Web Clipper](https://obsidian.md/clipper) | Convert web pages into `raw/web/` Markdown files. |

### Automation & Messaging

| Tool | Purpose | Setup |
| --- | --- | --- |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Automation control plane — llm-wiki, cron, Telegram notification channel | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| Telegram Bot | Capture-command intake + post-hoc notification/query channel (not an approval gate) | Create via [@BotFather](https://t.me/BotFather), set token in `~/.hermes/.env` |

### AI Tools

| Tool | Auth Method | Setup |
| --- | --- | --- |
| [OpenCode](https://opencode.ai) + Kimi K2 | OpenRouter API key | `opencode providers login openrouter` in terminal |
| [Claude Code](https://claude.ai/code) | Claude Max subscription | `claude` — login via browser on first run |
| [Codex](https://github.com/openai/codex) | ChatGPT Plus subscription | `codex` — login via browser on first run |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub account (built-in) | Built into VS Code 1.130+; sign in with GitHub. Provides both inline completions and Chat (`@workspace`) |

### Recommended Setup Order

1. Clone this repository and open it in Obsidian as a vault.
2. Install Zotero, Zotero Connector (Chrome), and Obsidian Web Clipper. Enable Zotero local API: Settings → Advanced → "Allow other applications on this computer to communicate with Zotero". Install zotero-mcp: `pipx install zotero-mcp-server`.
3. Install OpenCode, Claude Code CLI, and Codex CLI via npm.
4. Sign in to GitHub Copilot in VS Code (built-in from v1.130+); use Copilot Chat (`@workspace`) for cross-validation.
5. Install Hermes Agent: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
6. Set `WIKI_PATH`, `OPENROUTER_API_KEY`, and `TELEGRAM_BOT_TOKEN` in `~/.hermes/.env`.
7. Start the gateway: `hermes gateway install --start-now --start-on-login`
8. Configure cron jobs via the Hermes Telegram bot or CLI.

---

## Directory Structure

```text
.
├── inbox/                    # Temporary intake — Hermes picks up daily at 04:00
├── raw/                      # Immutable source evidence
│   ├── articles/             # Article and web-clipping source text
│   ├── notebooklm/           # NotebookLM source records
│   ├── papers/files/         # Paper attachments (placeholder only)
│   ├── transcripts/          # Audio, video, and meeting transcripts
│   ├── web/                  # Web captures (importer-preserved paths)
│   ├── youtube/              # YouTube metadata and transcripts
│   └── assets/               # Images referenced by source records
├── entities/                 # Canonical knowledge — people, orgs, tools
├── concepts/                 # Canonical knowledge — concepts, principles
├── comparisons/              # Canonical side-by-side analysis
├── queries/                  # Source-grounded questions and answers
├── docs/
│   ├── architecture/         # System architecture diagram and spec
│   ├── domain/               # Drone domain collection guide
│   ├── tech-stack/           # Technology stack diagram
│   └── workflow/             # Operating workflow diagram
├── templates/                # Frontmatter templates (raw-article / entity / concept / comparison / query)
├── _archive/                 # Superseded canonical pages
├── AGENTS.md                 # AI tool role definitions and domain focus
├── CLAUDE.md                 # Claude Code specific instructions
├── SCHEMA.md                 # Authoritative data contract
├── index.md                  # Active canonical knowledge catalog
└── log.md                    # Append-only operation history
```

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/krill0188/2nd-brain-ai-system.git
cd 2nd-brain-ai-system
```

### 2. Open in Your Editor

- **Obsidian**: `Open folder as vault` → select the repository directory.
- **VS Code**: `code .` or `code ~/2nd` (if cloned to `~/2nd`).

### 3. Start a Knowledge Session

```bash
# Automated pipeline — Hermes handles daily ingestion
hermes gateway status

# Manual compile assist — Kimi K2
cd ~/2nd && opencode

# Architecture / contradiction analysis — Claude
cd ~/2nd && claude

# Drone code exploration — Codex (results go to raw/inbox/)
cd ~/2nd && codex
```

### 4. Send a Capture Command via Telegram

```
[Telegram → @dronewikibot]
"Collect this link and save to raw/inbox/: https://docs.px4.io/..."
```

Hermes saves the content to `raw/inbox/`, and the next cron run compiles it.

### 5. View the Knowledge Graph

```bash
# Open the interactive Gate C graph viewer (offline, self-contained)
open .ua/graph.html
```

The viewer shows only canonical knowledge domain nodes (Concepts / Comparisons / Queries / Entities) with a force-directed layout — docs, templates, and scaffolding are intentionally excluded. Click any node to see its summary, file path, and connections. Filter by domain or search by name.

### 6. Read the Operating Contract

Before adding knowledge, read [SCHEMA.md](SCHEMA.md), check [index.md](index.md) for subjects already covered, and review the latest entries in [log.md](log.md).

---

## Basic Workflow

1. **Capture**: Drop links into Telegram or save web pages via Obsidian Web Clipper → `raw/web/`. Papers go via Zotero Connector → Zotero library → `python3 scripts/zotero-ingest.py` → `raw/papers/<topic>/`.
2. **Auto-compile (no pre-approval)**: Hermes Cron (04:00 daily) scans `raw/inbox/` and llm-wiki compiles and **finalizes** canonical pages immediately — no waiting state, `index.md`/`log.md` are updated right away.
3. **Post-hoc notice**: `morning-report.sh` at 07:30 sends that day's newly-created pages to Telegram (a notice, not an approval request — the pages are already final).
4. **(Optional) Cross-validate**: If warranted, ask GitHub Copilot Chat (`@workspace`) or Claude to review already-created pages for contradictions or missing coverage — a manual, human-initiated check, not an automatic step.
5. **AI research loop (the real approval gate)**: For deeper questions, start a session with `scripts/research-run.sh new "<question>"`. It runs Planner→Retriever→Hypothesis→Critic→Verifier→Report to produce a draft; the master must `research-run.sh approve <id>` and then name specific claims via `research-promote.py <id> --items C1,C3` before anything reaches canonical — **only this path actually blocks finalization pending approval.**
6. **Query**: Ask the Telegram bot directly — `"What did we collect on PX4 flight modes?"` — Hermes searches the wiki and replies.
7. **Archive**: Move fully superseded pages to `_archive/`, repair links, and record the operation in `log.md`.

---

## Data Management Principles

> [!IMPORTANT]
> `README.md` is a usage guide; [SCHEMA.md](SCHEMA.md) is the authoritative data contract. Follow `SCHEMA.md` whenever the two appear to differ.

- **Source bodies are immutable.** Do not modify `raw/` content after initial capture.
- **Source paths must exist.** Canonical `sources` may contain only real Markdown files under registered `raw/` directories.
- **Canonical knowledge is selective.** Promote a subject only when it is central to one source or repeated across at least two sources.
- **Canonical knowledge is connected.** Every active canonical page must link to at least two other active canonical pages via `[[wikilinks]]`.
- **Changes are atomic.** Canonical create/update/archive is complete only after updating `index.md` and appending to `log.md` together.
- **No secrets in Git.** Never commit API keys, bot tokens, or login sessions to this repository. Keep `~/.hermes/.env` local-only.

---

## Synchronization

```bash
git add .
git commit -m "feat: add drone-sw canonical pages (PX4 architecture)"
git push
```

Use Git for history. Never store API keys, tokens, or login sessions in the repository.

---

## License

Based on [ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template). Adapted and extended for drone-domain AI knowledge management with Hermes Agent automation and a human-approved AI research loop (`research/`).
