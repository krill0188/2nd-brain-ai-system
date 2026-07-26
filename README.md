# 2nd Brain AI System

**English** | [한국어](README.ko.md)

> A drone-domain knowledge management system built on Markdown and Git — powered by a 5-AI tool stack (OpenCode + Kimi K2, Claude Code, Codex, Gemini Code Assist, GitHub Copilot).

## Project Overview

This project is a personal knowledge management system specialized in **drone technology** (8 subject areas: drone / datalink / swarm / voice-control / drone-hw / drone-sw / drone-ai / ai-agent). It implements a continuous **capture → compile → discovery → human decision** workflow using plain Markdown files — compatible with Obsidian, VS Code, GitHub, and any Markdown-compatible tool.

Built on [ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template) with a custom AI tool layer.

### Architecture

The system consists of four layers: **Evidence → Canonical Memory → Discovery → Human Decision**. Raw source material is preserved as immutable evidence under `raw/`; reusable knowledge is compiled into canonical Markdown with traceable provenance. A 5-AI control plane coordinates capture, compilation, cross-validation, and final judgment — each tool assigned to its role by [AGENTS.md](AGENTS.md).

![Master 2nd Brain AI System Architecture](docs/architecture/master-ai-architecture.png)

### Operating Workflow

The operating workflow follows **Capture → Compile → Discovery → Human Decision**, passing through three integrity gates (Gate A: raw integrity, Gate B: lint/frontmatter, Gate C: graph/freshness) before any canonical change is finalized. Approved changes update the canonical page, `index.md`, and `log.md` together as a single atomic operation.

![Master 2nd Brain Operating Workflow](docs/workflow/master-workflow.png)

### Technology Stack

The AI tool stack maps five tools to specific roles in the knowledge pipeline. Open-format Markdown, provenance metadata, and Git history are the durable assets; AI tools are the replaceable layer.

![Master 2nd Brain Technology Stack](docs/tech-stack/master-tech-stack.png)

## AI Tool Roles

Five tools are configured for this system — each with a distinct responsibility defined in [AGENTS.md](AGENTS.md).

| Tool | Interface | Primary Role |
| --- | --- | --- |
| **OpenCode + Kimi K2** | Terminal (`opencode`) | Markdown cleanup, document drafting, llm-wiki compile, repetitive organize tasks |
| **Claude Code** | Terminal (`claude`) | Architecture analysis, contradiction review, multi-file reasoning, final judgment |
| **Codex** | Terminal (`codex`) | Code implementation, drone firmware exploration (PX4/ArduPilot/ROS2), Git analysis |
| **Gemini Code Assist** | VS Code sidebar | Cross-validation, alternative perspective, summarization while editing |
| **GitHub Copilot** | VS Code inline | Autocomplete while writing Markdown or code |

> **Cost principle**: Route repetitive compile tasks to Kimi K2 (token cost). Reserve Claude for architecture decisions and contradiction resolution. Gemini and Copilot are free — use freely during editing.

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

## Key Features

| Feature | Description |
| --- | --- |
| **Source and provenance preservation** | Capture papers and web material with Zotero and Obsidian Web Clipper, then preserve the source, metadata, and SHA-256 digest under `raw/` so every claim can be traced to evidence. |
| **Verified knowledge compilation** | OpenCode + Kimi K2 structures source material into entity, concept, comparison, and query documents with provenance, confidence ratings, and contradiction tracking. |
| **Connected Markdown editing** | Read and edit durable knowledge in Obsidian using wikilinks and backlinks; GitHub Copilot and Gemini Code Assist assist inline while editing. |
| **Multi-AI cross-validation** | Claude Code and Gemini provide independent analysis of the same evidence — contradictions surface before knowledge is promoted to canonical. |
| **Drone code exploration** | Codex navigates PX4, ArduPilot, ROS2/MAVROS2, and MAVSDK source code and integrates findings into the wiki as `drone-sw` canonical pages. |
| **Human verification gate** | No AI hypothesis is promoted to canonical memory without human approval. The human decision layer is enforced by the Gate C check before `index.md` and `log.md` are updated. |

## Prerequisites

### Capture Tools

| Category | Tool | Purpose |
| --- | --- | --- |
| Required | [Obsidian](https://obsidian.md/download) | Open this repository as a local vault to browse and edit Markdown. |
| Paper capture | [Zotero + Zotero Connector](https://www.zotero.org/download/) | Manage drone papers and PDFs; save metadata from the browser into Zotero. |
| Web capture | [Obsidian Web Clipper](https://obsidian.md/clipper) | Convert web pages into `raw/web/` Markdown files. |

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
2. Install Zotero, Zotero Connector, and Obsidian Web Clipper.
3. Install OpenCode, Claude Code CLI, and Codex CLI via npm.
4. Install Gemini Code Assist extension in VS Code.
5. Register OpenRouter API key: `cd ~/2nd && opencode providers login openrouter`
6. Sign into Claude Max and ChatGPT Plus on first `claude` / `codex` run.
7. Sign into GitHub for Copilot in VS Code (account icon → GitHub login).

## Directory Structure

```text
.
├── inbox/                    # Temporary intake awaiting classification
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
│   ├── architecture/         # System architecture diagram
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
# Day-to-day compile tasks — Kimi K2
cd ~/2nd && opencode

# Architecture / contradiction analysis — Claude
cd ~/2nd && claude

# Drone code exploration — Codex
cd ~/2nd && codex
```

### 4. Read the Operating Contract

Before adding knowledge, read [SCHEMA.md](SCHEMA.md), check [index.md](index.md) for subjects already covered, and review the latest entries in [log.md](log.md). If the subject already exists, strengthen the existing page with new evidence instead of creating a duplicate.

## Basic Workflow

1. **Capture**: Save web pages to `raw/web/` via Obsidian Web Clipper; save papers to Zotero → export to `raw/articles/`.
2. **Classify**: Move items from `inbox/` to the correct `raw/` subdirectory and fill in frontmatter using `templates/raw-article.md`.
3. **Compile**: Ask OpenCode (Kimi K2) to draft a canonical page from 2+ raw sources using the appropriate template.
4. **Cross-validate**: Ask Gemini or Claude to review the draft for contradictions or missing coverage.
5. **Approve and record**: On approval, update `index.md` and append one entry to `log.md` in the same operation.
6. **Explore**: Treat knowledge-graph suggestions as hypotheses. Promote only human-verified findings to canonical.
7. **Archive**: Move fully superseded pages to `_archive/`, repair links, and record the operation in `log.md`.

## Data Management Principles

> [!IMPORTANT]
> `README.md` is a usage guide; [SCHEMA.md](SCHEMA.md) is the authoritative data contract. Follow `SCHEMA.md` whenever the two appear to differ.

- **Source bodies are immutable.** Do not modify `raw/` content after initial capture.
- **Source paths must exist.** Canonical `sources` may contain only real Markdown files under registered `raw/` directories.
- **Canonical knowledge is selective.** Promote a subject only when it is central to one source or repeated across at least two sources.
- **Canonical knowledge is connected.** Every active canonical page must link to at least two other active canonical pages via `[[wikilinks]]`.
- **Changes are atomic.** Canonical create/update/archive is complete only after updating `index.md` and appending to `log.md` together.
- **API keys stay out of Git.** Never commit OpenRouter, Zotero, or any other API key to this repository.

## Synchronization

```bash
git add .
git commit -m "feat: add drone-sw canonical pages (PX4 architecture)"
git push
```

Use Git for history. Never store API keys, tokens, or login sessions in the repository.

## License

Based on [ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template). Adapted and extended for drone-domain AI knowledge management.
