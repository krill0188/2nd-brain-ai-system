# 2nd Brain AI System

**English** | [한국어](README.ko.md)

> A drone-domain knowledge management system built on Markdown and Git — powered by **Hermes Agent automation + 5-AI tool stack + Telegram HITL**.

## Project Overview

This project is a personal knowledge management system specialized in **drone technology** (8 subject areas: drone / datalink / swarm / voice-control / drone-hw / drone-sw / drone-ai / ai-agent). It implements a continuous **capture → compile → discovery → human decision** workflow using plain Markdown files — compatible with Obsidian, VS Code, GitHub, and any Markdown-compatible tool.

Built on [ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template) with a custom AI tool layer, Hermes Agent automation, and Telegram HITL integration.

### Architecture

The system consists of four knowledge layers: **Evidence → Canonical Memory → Discovery → Human Decision**. Raw source material is preserved as immutable evidence under `raw/`; reusable knowledge is compiled into canonical Markdown with traceable provenance.

An **Automation Control Plane** (Hermes Agent + llm-wiki skill) handles scheduled ingestion, compilation, and lint automatically. A **Telegram HITL gateway** delivers diff reports to the master and gates canonical promotion on explicit approval — no AI hypothesis enters canonical memory without human sign-off.

![Master 2nd Brain AI System Architecture](docs/architecture/master-ai-architecture.png)

### Operating Workflow

The operating workflow follows **Capture → Hermes Cron → Gate A/B/C → Telegram Approval → Canonical**. Three integrity gates (Gate A: raw integrity / Gate B: lint + frontmatter / Gate C: graph freshness) run automatically. Gate B results are delivered to Telegram for human review before any canonical change is finalized.

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
| **Telegram gateway** | Hermes gateway (launchd, PID auto-restart) | Always-on — receives capture commands, delivers Gate B diffs for approval | ✅ Running |

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

### Telegram HITL — 4-Point Integration

```
[Point 1: Input]      Master → Telegram → Hermes → raw/inbox/
[Point 2: Cron log]   Hermes Cron → Telegram: "3 raw added, 2 canonical candidates"
[Point 3: Gate]       Gate B diff → Telegram → Master: approve / reject / revise
[Point 4: Query]      Master → Telegram → Hermes → wiki search → answer
```

Point 3 is the critical gate: Hermes sends the canonical diff to Telegram, and the master's reply (`approve` / `reject`) determines whether `index.md` and `log.md` are updated.

---

## AI Tool Roles

Five tools are configured for this system — each with a distinct responsibility defined in [AGENTS.md](AGENTS.md).

| Tool | Interface | Primary Role |
| --- | --- | --- |
| **Hermes + llm-wiki** | Gateway / Cron | Automated ingestion, compilation, lint, Telegram delivery |
| **OpenCode + Kimi K2** | Terminal (`opencode`) | Manual compile assist, document drafting, large-batch editing |
| **Claude Code** | Terminal (`claude`) | Architecture analysis, contradiction review, Gate B deep judgment |
| **Codex** | Terminal (`codex`) | Drone firmware exploration (PX4/ArduPilot/ROS2), code-to-raw pipeline |
| **Gemini Code Assist** | VS Code sidebar | Cross-validation, alternative perspective, summarization while editing |
| **GitHub Copilot** | VS Code inline | Autocomplete while writing Markdown or code |
| **Understand Anything** | Hermes skill / Claude Code | Gate C — knowledge graph generation, gap analysis, structural observation |

> **Cost principle**: Route repetitive compile tasks to Hermes/Kimi K2. Reserve Claude for architecture decisions and contradiction resolution. Gemini and Copilot are free — use freely during editing.

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
| **Automated ingestion pipeline** | Hermes Agent cron scans `raw/inbox/` daily at 04:00, runs llm-wiki skill to compile canonical candidates, and delivers results to Telegram. |
| **Telegram HITL gate** | Gate B diffs are delivered to Telegram for master approval. No canonical change is finalized without an explicit `approve` reply. |
| **Source and provenance preservation** | Capture papers and web material with Zotero and Obsidian Web Clipper, then preserve the source, metadata, and SHA-256 digest under `raw/` so every claim can be traced to evidence. |
| **Verified knowledge compilation** | Hermes llm-wiki skill and OpenCode + Kimi K2 structure source material into entity, concept, comparison, and query documents with provenance, confidence ratings, and contradiction tracking. |
| **Connected Markdown editing** | Read and edit durable knowledge in Obsidian using wikilinks and backlinks; GitHub Copilot and Gemini Code Assist assist inline while editing. |
| **Multi-AI cross-validation** | Claude Code and Gemini provide independent analysis of the same evidence — contradictions surface before knowledge is promoted to canonical. |
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
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Automation control plane — llm-wiki, cron, Telegram gateway | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| Telegram Bot | HITL notification and approval gateway | Create via [@BotFather](https://t.me/BotFather), set token in `~/.hermes/.env` |

### AI Tools

| Tool | Auth Method | Setup |
| --- | --- | --- |
| [OpenCode](https://opencode.ai) + Kimi K2 | OpenRouter API key | `opencode providers login openrouter` in terminal |
| [Claude Code](https://claude.ai/code) | Claude Max subscription | `claude` — login via browser on first run |
| [Codex](https://github.com/openai/codex) | ChatGPT Plus subscription | `codex` — login via browser on first run |
| [Gemini Code Assist](https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist) | Google account (free) | Install VS Code extension, sign in with Google |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub account (built-in) | Built into VS Code 1.130+; sign in with GitHub |

### Recommended Setup Order

1. Clone this repository and open it in Obsidian as a vault.
2. Install Zotero, Zotero Connector (Chrome), and Obsidian Web Clipper. Enable Zotero local API: Settings → Advanced → "Allow other applications on this computer to communicate with Zotero". Install zotero-mcp: `pipx install zotero-mcp-server`.
3. Install OpenCode, Claude Code CLI, and Codex CLI via npm.
4. Install Gemini Code Assist extension in VS Code; sign in with GitHub for Copilot.
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
2. **Auto-ingest**: Hermes Cron (04:00 daily) scans `raw/inbox/`, compiles canonical candidates using llm-wiki, and sends a Telegram report.
3. **Gate B approval**: Hermes delivers the canonical diff to Telegram. Reply `approve` to finalize or `reject` to discard.
4. **Cross-validate**: Ask Gemini or Claude to review drafts for contradictions or missing coverage.
5. **Explore**: Treat knowledge-graph suggestions as hypotheses. Promote only human-verified findings to canonical.
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

Based on [ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template). Adapted and extended for drone-domain AI knowledge management with Hermes Agent automation and Telegram HITL.
