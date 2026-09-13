# 00_CURRENT_SYSTEM.md

> **Project:** 2nd Brain × DroneWiki  
> **Document Type:** Current Architecture Baseline  
> **Status:** VERIFIED BASELINE — READ ONLY AUDIT  
> **Baseline Date:** 2026-09-13  
> **Repositories:**  
> - `krill0188/2nd-brain-ai-system` → local target `~/2nd`
> - `krill0188/drone-wiki-web` → local target `~/projectm/drone-wiki-web`
>
> **Important:** This document records the currently verified state only.  
> It does **not** authorize code, data, deployment, schema, or automation changes.

---

# 1. Purpose

This file is the baseline for all future development.

Before adding new Drone Builder, Engineering Ontology, Simulation, Research, or Paper Workbench features, the project must first agree on what is actually implemented today.

The governing rule is:

```text
Code / executable configuration / generated artifacts
        >
outdated plans
        >
assumptions
```

A document that says a feature is planned is not proof that it is unimplemented.
A document that says a feature is complete is not proof that it currently works.

Every important capability should ultimately have:

```text
Status
Purpose
Implementation
Evidence files
Runtime
Dependencies
Known limitations
Last verified
```

---

# 2. Status Vocabulary

This baseline uses only the following states.

| Status | Meaning |
|---|---|
| `IMPLEMENTED` | Code or data structure exists and its intended path is directly verifiable from the repository. |
| `PARTIAL` | Core implementation exists, but an important runtime path, environment, integration, or guarantee is incomplete. |
| `EXPERIMENTAL` | Code exists but is isolated/manual/research-oriented and not part of the normal production path. |
| `PLANNED` | Design or roadmap exists, but implementation was not confirmed. |
| `DEPRECATED` | Historical path retained only for compatibility/reference. |
| `UNKNOWN` | Evidence is insufficient. Do not infer. |

---

# 3. High-Level Architecture

The current verified architecture is best described as two cooperating systems.

```text
External Sources
    │
    ▼
┌─────────────────────────────────────────────┐
│ ~/2nd                                      │
│ 2nd Brain AI System                        │
│                                             │
│ raw evidence                                │
│   ↓                                         │
│ canonical knowledge                         │
│   ↓                                         │
│ ontology / graph / embeddings / research    │
│                                             │
│ Role: Knowledge Source of Truth             │
└────────────────────┬────────────────────────┘
                     │
                     │ sync / snapshot
                     ▼
┌─────────────────────────────────────────────┐
│ ~/projectm/drone-wiki-web                   │
│ DroneWiki                                   │
│                                             │
│ data/wiki snapshot                          │
│ RAG / GraphRAG / Ontology query             │
│ AI Chat / Drone Builder / Review UI         │
│                                             │
│ Role: AI Application & Presentation Layer   │
└────────────────────┬────────────────────────┘
                     │
                     ▼
                Git / Vercel
```

The long-term architecture should continue to preserve this separation unless a future ADR explicitly changes it.

---

# 4. 2nd Brain — Verified Responsibilities

## 4.1 Raw evidence

**Status: `IMPLEMENTED`**

`SCHEMA.md` defines `raw/` as immutable source evidence.

Confirmed source areas include:

- `raw/articles/`
- `raw/notebooklm/`
- `raw/papers/<topic>/`
- `raw/transcripts/`
- `raw/web/`
- `raw/youtube/`
- `raw/career-quiz/`

Raw bodies are protected from ordinary rewriting.

### Important rule

```text
Raw Evidence ≠ Canonical Knowledge
```

Corrections and interpretations belong in canonical pages.

**Evidence**
- `2nd-brain-ai-system/SCHEMA.md`
- `2nd-brain-ai-system/AGENTS.md`

---

## 4.2 Canonical knowledge

**Status: `IMPLEMENTED`**

Canonical knowledge is restricted to:

```text
entities/
concepts/
comparisons/
queries/
```

Each canonical page is required to carry:

```text
title
created
updated
type
tags
sources
confidence
contested
contradictions
```

`claim_type` is an optional additional field for research-promoted content.

Canonical changes must also maintain:

```text
index.md
log.md
```

**Evidence**
- `SCHEMA.md`
- `AGENTS.md`

---

## 4.3 Daily ingestion / automatic compilation

**Status: `IMPLEMENTED` at repository design level; runtime schedule not independently executed during this audit**

The current README describes a daily path in which Hermes + llm-wiki compiles qualifying material into canonical knowledge without a pre-approval gate.

Human review is therefore **not** a universal gate for ordinary ingestion.

The documented path is:

```text
capture
→ Hermes
→ llm-wiki compile
→ canonical
→ log
→ later notification
```

This distinction must remain explicit in all architecture documents.

**Evidence**
- `README.ko.md`
- `AGENTS.md`

---

# 5. Research Loop

## 5.1 Research staging

**Status: `IMPLEMENTED`**

`research/` is explicitly separated from raw and canonical knowledge.

Typical state flow:

```text
planned
→ retrieving
→ hypothesis_generated
→ under_critique
→ evidence_checked
→ awaiting_approval
→ approved / rejected / failed
```

Research output itself is not automatically canonical.

---

## 5.2 Human-approved research promotion

**Status: `IMPLEMENTED`**

This is an important correction to older documentation.

Current `scripts/research-promote.py` performs actual promotion checks, including:

- session must already be approved
- `fact` claims are rejected as new canonical promotion candidates
- `inference` / `hypothesis` are eligible categories
- `verification_status` must be `grounded`
- at least one raw source must exist
- unresolved sources are rejected
- non-primary reconstructed evidence alone is insufficient
- at least two canonical wikilinks are required
- validation is all-or-nothing for the requested promotion set

It then creates canonical concept content with provenance and `claim_type`.

### Documentation drift

`AGENTS.md` still contains an older statement that promotion tooling exists but is not wired into the phase pipeline.

That statement no longer accurately describes the current `research-promote.py` implementation.

**Required action:** documentation correction only, after Stage 0 review.

**Evidence**
- `scripts/research-promote.py`
- `AGENTS.md`

---

# 6. Knowledge Graph

## 6.1 Canonical Drone Knowledge Graph

**Status: `IMPLEMENTED`**

`scripts/update-graph.sh` scans:

```text
concepts
entities
comparisons
queries
```

and writes:

```text
.ua/drone-knowledge-graph.json
```

Node metadata includes:

```text
id
name
layer
domain
tags
updated
confidence
status
ontologyClass
```

Relations include at least:

```text
wikilink
related
evidences
contradicts
```

depending on document context and frontmatter.

### Important architectural decision

The dedicated drone graph is separated from the legacy:

```text
.ua/knowledge-graph.json
```

because the `understand-anything` tool also used the legacy file for a different graph model.

This separation is correct and should later be captured in an ADR.

**Evidence**
- `scripts/update-graph.sh`

---

## 6.2 Discovery Graph

**Status: `IMPLEMENTED`**

The system maintains a separate AI-extracted graph:

```text
.ua/discovery-knowledge-graph.json
```

Its relationships are treated as unverified discovery information rather than canonical knowledge.

DroneWiki GraphRAG can combine canonical and discovery relationships.

**Evidence**
- `drone-wiki-web/lib/graphrag.ts`
- `data/wiki/.ua/discovery-knowledge-graph.json`

---

# 7. Ontology

## 7.1 Class hierarchy

**Status: `IMPLEMENTED`**

A machine-readable class hierarchy exists under:

```text
ontology/class-hierarchy.json
```

It includes high-level branches such as:

```text
Thing
├─ PhysicalEntity
├─ SoftwareSystem
├─ AbstractProcess
├─ DataArtifact
└─ Agent
```

and drone-specific subclasses.

---

## 7.2 Ontology class assignment

**Status: `IMPLEMENTED`**

`update-graph.sh` assigns `ontologyClass` from:

1. explicit frontmatter `ontology_class`, when valid
2. otherwise a domain-to-class mapping

Invalid or unsupported classifications are not forced.

---

## 7.3 Ancestor / descendant reasoning

**Status: `IMPLEMENTED`**

DroneWiki has TypeScript logic for:

- ancestor traversal
- descendant traversal
- class-based query expansion
- subsumption strings such as:

```text
ComputeUnit ⊑ PhysicalEntity ⊑ Thing
```

These results can be injected into RAG context.

**Evidence**
- `drone-wiki-web/lib/ontology.ts`
- `drone-wiki-web/lib/rag.ts`

---

## 7.4 OWL build

**Status: `EXPERIMENTAL`**

`build-owl.py` can produce an OWL representation and optionally invoke reasoning.

It is deliberately not part of the normal production pipeline.

A key design decision is preserved:

```text
Wiki document ≠ real-world drone/software instance
```

Canonical documents are represented as documentation objects rather than pretending that a Markdown page itself is a physical or runtime entity.

**Evidence**
- `scripts/build-owl.py`

---

## 7.5 Kinetic rules

**Status: `EXPERIMENTAL`**

`apply-kinetic-rules.py` implements only rules that can be evaluated from static knowledge metadata.

Confirmed examples include:

- SLM / LLM classification
- audit of unapproved hypothesis use

It does not constitute a complete Palantir-style operational ontology.

**Evidence**
- `scripts/apply-kinetic-rules.py`

---

## 7.6 Runtime Drone Ontology / Digital Twin

**Status: `PLANNED`**

Not confirmed as implemented.

Missing runtime objects include concepts such as actual live instances of:

```text
DroneInstance
MissionExecution
TaskExecution
BatteryState
SensorState
DatalinkState
```

and real operational Action/Function execution against such objects.

This remains a later phase and should not be mixed into the current 2nd Brain responsibility.

---

# 8. DroneWiki Runtime

## 8.1 Application stack

**Status: `IMPLEMENTED`**

Current `package.json` confirms a Next.js full-stack application using:

- Next.js 16
- React 19
- TypeScript
- Vercel AI SDK
- OpenRouter provider
- Anthropic SDK
- react-force-graph-2d
- Markdown parsing/rendering tools

DroneWiki is therefore **not just a frontend**.

**Evidence**
- `drone-wiki-web/package.json`

---

## 8.2 Wiki root resolution

**Status: `IMPLEMENTED`**

The code resolves knowledge in this order:

```text
1. WIKI_PATH environment variable
2. ~/2nd
3. data/wiki
```

This creates two different operational modes:

```text
Local:
DroneWiki → ~/2nd

Deployment:
DroneWiki → data/wiki snapshot
```

This distinction must be maintained explicitly in architecture documentation.

---

# 9. RAG

## 9.1 Canonical RAG

**Status: `IMPLEMENTED`**

The RAG loader reads canonical content from:

```text
concepts
entities
comparisons
queries
```

---

## 9.2 Raw RAG

**Status: `IMPLEMENTED`**

Current `lib/rag.ts` also searches selected raw evidence directories:

```text
raw/papers
raw/articles
raw/youtube
raw/videos
raw/releases
```

Raw sources are explicitly marked as:

```text
origin: raw
```

and are intended to be labeled as unverified in AI context.

This is useful, but trust separation must remain visible to both model and user.

---

## 9.3 Hybrid vector search — local

**Status: `IMPLEMENTED`**

The local hybrid path uses:

```text
keyword score
+
vector cosine similarity
```

with configured weighting.

Query embeddings are generated through a local Python virtual environment.

---

## 9.4 Hybrid vector search — production

**Status: `PARTIAL`**

Current `lib/rag.ts` explicitly returns no query vector when the local venv Python executable is unavailable.

This means the deployed application is designed to fall back to keyword-only search when that environment is absent.

At the same time, the deployment snapshot currently contains:

```text
data/wiki/.ua/embeddings.json
```

with an observed size of approximately 3.8 MB.

Therefore the conservative conclusion is:

```text
Document vectors may be deployed,
but production vector retrieval is not proven active
because query embedding depends on local Python.
```

Do not document production Hybrid RAG as fully operational until this is runtime-tested.

---

# 10. GraphRAG

**Status: `IMPLEMENTED`**

The current chat and Drone Builder paths use:

```text
RAG seed results
→ canonical graph
→ discovery graph
→ multi-hop graph expansion
→ model context
```

Discovery-derived relations are marked as unverified.

This is a real application path, not just a roadmap item.

**Evidence**
- `lib/graphrag.ts`
- `app/api/chat/route.ts`
- `app/api/drone-builder/route.ts`

---

# 11. AI Chat

**Status: `IMPLEMENTED`**

The API path currently combines:

```text
question
+ current document
+ recent viewed documents
+ RAG
+ news
+ GraphRAG
+ agent manifest
→ OpenRouter model
→ streamed answer
```

The currently configured model in the verified route is:

```text
anthropic/claude-haiku-4.5
```

**Evidence**
- `app/api/chat/route.ts`

---

# 12. AI Drone Builder

**Status: `IMPLEMENTED`, but not yet an engineering-grade design system**

Current implementation is a three-stage LLM orchestration:

```text
1. proposal
2. technical specification
3. architecture / code skeleton
```

Each stage re-queries the knowledge base with RAG + GraphRAG.

This is useful and real.

However, it is still fundamentally an LLM planning workflow rather than a verified engineering design engine.

Not yet confirmed as implemented:

- formal MissionProfile object
- EnvironmentProfile object
- Requirement IDs
- deterministic mass/power/endurance calculators
- component compatibility engine
- trade-study engine
- requirement verification matrix
- simulation result linkage
- physical test evidence linkage

Therefore this feature must not yet be described as:

```text
"AI that can design and verify a new drone"
```

A conservative description is:

```text
"knowledge-grounded drone concept, specification,
and architecture drafting assistant"
```

**Evidence**
- `app/api/drone-builder/route.ts`

---

# 13. AI Write / Review Safety

## 13.1 Discovery promotion

**Status: `IMPLEMENTED` with environment gate**

Write operations for discovery promotion are blocked on deployed Vercel environments and are intended for local development.

---

## 13.2 Self-update

**Status: `IMPLEMENTED` with local write gate**

News-to-wiki update suggestions can be generated, while write/apply operations are intended for local usage.

This is a good safety boundary and should be preserved.

---

# 14. Snapshot Synchronization

## 14.1 Confirmed sync script

**Status: `IMPLEMENTED` — corrected 2026-09-13, see architecture audit**

> **Correction**: this section previously audited `scripts/sync-wiki.sh`, which **does not exist
> in this repository** (deleted/moved before this audit). The actual script that `launchd`
> (`ai.2nd.sync-dronewiki`, daily 08:30) runs is **`~/.hermes/scripts/dronewiki-sync.sh`** (125
> lines). Full detail: [`docs/2026-09-13-architecture-audit.md`](docs/2026-09-13-architecture-audit.md).

`~/.hermes/scripts/dronewiki-sync.sh` explicitly copies:

```text
concepts
entities
comparisons
queries
ontology
raw/                (rsync -a --delete, career-quiz/papers-files excluded — added 2026-09-04)

news-feed.json
daily-briefing.json

drone-knowledge-graph.json
discovery-knowledge-graph.json
embeddings.json
```

Then, if `data/wiki` changed, it:

```text
git add
git commit
git push
npx vercel --prod --yes
```

Real run observed 2026-09-13 17:48: "584docs" pushed as commit `67328a9`, "raw: 207개 동기화",
Vercel production deploy confirmed in the job's own log
(`~/2nd/.ua/logs/2nd-sync-dronewiki.log`).

---

## 14.2 raw snapshot path — RESOLVED (was P0)

**Status: `RESOLVED` (previously `UNKNOWN / INVESTIGATE BEFORE CHANGE`)**

`drone-wiki-web/data/wiki/raw/` is populated by `dronewiki-sync.sh` itself via an explicit
`rsync -a --delete` step (added 2026-09-04, see 14.1). The earlier "P0 investigation item" was
caused by auditing the wrong file (`scripts/sync-wiki.sh`, which never had this logic and no
longer exists) instead of the real runtime script. No further investigation needed — do not
reopen this as unknown; if `raw/` sync ever looks wrong, the first place to check is
`~/.hermes/scripts/dronewiki-sync.sh`, not this repository's `scripts/` directory.

---

# 15. Latest Observed Deployment Snapshot

At audit time, the latest accessible DroneWiki Git commit observed was:

```text
67328a9
```

Commit message:

```text
sync: 2nd Brain → DroneWiki 2026-09-13 17:48 [584docs]
```

**Update 2026-09-13**: this was a manual catch-up run (the Mac was asleep through the original
07:30/08:00/08:30 schedule that morning — see incident write-up in the architecture audit), not
the scheduled automatic run. The catch-up was verified end-to-end: git push succeeded, and the
job's own log confirms `"완료 — Vercel 프로덕션 배포 성공 (584docs)"`. Going forward, `launchctl
list | grep ai.2nd.sync-dronewiki` plus `~/2nd/.ua/logs/2nd-sync-dronewiki.log` are the fastest way
to confirm a given day's scheduled run actually happened — don't infer success or failure from
repository history alone.

---

# 16. Public / Private Boundary

**Status: `PARTIAL / HIGH PRIORITY REVIEW`**

Both verified GitHub repositories are currently public.

The DroneWiki repository contains knowledge snapshots and derived artifacts.

Therefore the system currently needs a formally documented publication boundary:

```text
~/2nd
Private / master knowledge
        ↓
Publication Gate
        ↓
data/wiki
Public deployment snapshot
```

No new private, restricted, operationally sensitive, personal, or licensing-constrained material should be assumed safe for deployment merely because it exists in `~/2nd`.

A future publication policy should explicitly classify content as, for example:

```text
PUBLIC
INTERNAL
PRIVATE
RESTRICTED
```

No schema change is authorized by this baseline document.

---

# 17. Document Drift — Confirmed

The following documentation drift is already confirmed.

## Drift A — research promotion

`AGENTS.md` describes promotion tooling as not wired into the research phase.

Current `research-promote.py` is an active implementation with validation and canonical page generation logic.

**Action:** documentation correction candidate.

---

## Drift B — Ontology planning documents vs actual implementation

Older ontology documents include statements such as "design only" or "not implemented."

Current code includes:

```text
ontology/class-hierarchy.json
scripts/update-graph.sh ontologyClass support
scripts/build-owl.py
scripts/apply-kinetic-rules.py
drone-wiki-web/lib/ontology.ts
RAG ontology context
```

Therefore old plan documents must not be treated as current-state documents.

**Action:** do not delete them; classify them as SPEC / HISTORICAL PLAN and add current status headers.

---

## Drift C — RAG production explanation

The repository snapshot contains `embeddings.json`, while production query embedding still depends on local Python venv availability.

Any document saying either:

```text
"Vercel has no embeddings"
```

or:

```text
"Production Hybrid RAG is fully active"
```

would be too strong without runtime verification.

**Action:** document actual distinction between document-vector presence and query-vector generation.

---

# 18. Risk Register

| ID | Risk | Severity | Current Action |
|---|---|---:|---|
| R-001 | Private/master knowledge can cross into public snapshot without a formal publication policy | HIGH | Audit only |
| R-002 | Unknown writer/path for `data/wiki/raw/` | HIGH | Trace pipeline before modifying sync |
| R-003 | Documentation can mislead AI development agents about implemented vs planned features | HIGH | Build current-state baseline |
| R-004 | Production vector search status can be misunderstood | MEDIUM-HIGH | Runtime verification required |
| R-005 | Sync, commit, push, and production deploy are tightly coupled | MEDIUM | Document first; redesign later |
| R-006 | Raw evidence used in RAG may be mistaken for canonical fact | MEDIUM | Preserve explicit origin/trust labels |
| R-007 | Discovery-to-canonical graph matching relies partly on normalized names | MEDIUM | Stable identity design later |
| R-008 | AI Drone Builder may appear more engineering-verified than it really is | MEDIUM | Rename/document capability precisely |
| R-009 | Ontology logic is split across Python, JSON, and TypeScript | MEDIUM | Create ontology current-state spec |
| R-010 | Runtime state / digital twin scope could leak into 2nd Brain responsibility | MEDIUM | Keep Track A / Track B separation |

---

# 19. What Must NOT Be Changed Yet

Until Stage 0 is complete, do not:

- replace Markdown with a database
- introduce Neo4j merely because the repository description mentions it
- rewrite the ontology
- move canonical directories
- change raw immutability rules
- automatically expose more raw data to DroneWiki
- enable autonomous canonical writes
- merge 2nd Brain and DroneWiki into one repository
- make Production RAG architecture changes
- integrate real flight-control actions
- introduce a runtime digital twin
- refactor `sync-wiki.sh`
- change research approval semantics

The first task is understanding and documentation, not optimization.

---

# 20. Stage 0 Work Plan

## S0-01 — Current Capability Matrix

Create one authoritative matrix covering:

```text
Ingestion
Canonical
Research
Promotion
Graph
Discovery Graph
Ontology
OWL
Kinetic Rules
Embedding
RAG
GraphRAG
AI Chat
Drone Builder
Self Update
Discovery Review
Sync
Deployment
Session
Security
```

**Done when:** every row has status + evidence file + known limitation.

---

## S0-02 — C4 System Context

Document only major systems:

```text
User
2nd Brain
Hermes
DroneWiki
GitHub
Vercel
OpenRouter
External Sources
```

**Done when:** no module-level details are mixed into this diagram.

---

## S0-03 — C4 Container View

Separate:

```text
2nd Brain Markdown store
automation/scripts
derived graph/embedding artifacts
DroneWiki Next.js app
RAG/GraphRAG layer
deployment snapshot
external model provider
```

---

## S0-04 — Actual Data Flow

Trace one source from capture to answer:

```text
Source
→ raw file
→ canonical page
→ graph / embedding
→ sync
→ data/wiki
→ RAG / GraphRAG
→ AI response
```

Every arrow must identify its actual script/function.

No inferred arrow is allowed.

---

## S0-05 — Sync Writer Audit

Find exactly what writes:

```text
data/wiki/raw/
```

This must be completed before any sync refactor.

---

## S0-06 — Runtime Verification

Read-only verification targets:

```text
Hermes cron list
latest ingest log
latest graph build
latest embedding generation
latest sync
latest Vercel deployment
```

Repository evidence alone is not enough for runtime status.

---

## S0-07 — Documentation Classification

Every architecture/roadmap document receives one category:

```text
CURRENT
SPEC
ADR
ROADMAP
HISTORICAL
```

No deletion yet.

---

## S0-08 — ADR Index

Prepare ADR candidates, but do not rewrite architecture yet.

Minimum candidates:

```text
ADR-001 Markdown as Knowledge Source of Truth
ADR-002 Raw / Canonical Separation
ADR-003 Dedicated Drone Knowledge Graph
ADR-004 Local ~/2nd vs Deployment Snapshot
ADR-005 Knowledge Ontology vs Runtime Ontology
ADR-006 Research Human Approval
ADR-007 File-based Graph vs Graph Database
ADR-008 Public Knowledge Snapshot Boundary
```

---

# 21. Exit Criteria for Stage 0

Do not enter Engineering Ontology development until all of the following are true.

- [ ] Current Capability Matrix completed
- [ ] Current system context diagram completed
- [ ] Container architecture completed
- [ ] End-to-end data flow verified
- [ ] Writer of `data/wiki/raw/` identified
- [ ] Production RAG runtime behavior verified
- [ ] Ontology implementation status reclassified
- [ ] Public/private boundary documented
- [ ] Key documentation drift recorded
- [ ] ADR index created
- [ ] No unresolved P0 architecture ambiguity remains

---

# 22. Current PM Decision

**Decision: HOLD feature expansion.**

Do not begin:

```text
MissionProfile
EnvironmentProfile
Requirement Engine
Engineering Calculator
Component Compatibility
Simulation Adapter
Paper Workbench
Digital Twin
```

yet.

The current codebase has enough capability that adding another feature layer before freezing the architecture baseline would increase technical and documentation debt.

The next safe milestone is:

```text
STAGE 0 COMPLETE
```

Only after that should the project move to:

```text
Knowledge OS
→ Engineering Ontology
→ Design Engine
→ Verification
→ Research
→ Publication
```

---

# 23. Evidence Used for This Baseline

## 2nd Brain

Verified repository:

```text
krill0188/2nd-brain-ai-system
default branch: master
visibility: public
```

Primary evidence files:

```text
README.ko.md
SCHEMA.md
AGENTS.md
scripts/research-promote.py
scripts/update-graph.sh
scripts/build-owl.py
scripts/apply-kinetic-rules.py
ontology/class-hierarchy.json
docs/ONTOLOGY_SPEC.md
docs/ONTOLOGY_IMPLEMENTATION_ROADMAP.md
docs/ONTOLOGY_GUIDED_GRAPHRAG_PLAN.md
```

## DroneWiki

Verified repository:

```text
krill0188/drone-wiki-web
default branch: main
visibility: public
```

Primary evidence files:

```text
package.json
lib/rag.ts
lib/graphrag.ts
lib/ontology.ts
app/api/chat/route.ts
app/api/drone-builder/route.ts
scripts/sync-wiki.sh
data/wiki/.ua/*
```

Latest observed sync commit during this audit:

```text
4b7dbec472e5f647a0fc9cf4e37630291761c3ae
sync: 2nd Brain → DroneWiki 2026-09-12 04:30 [581docs]
```

---

# 24. Baseline Conclusion

The system is already beyond a basic LLM Wiki.

The conservative current classification is:

```text
2nd Brain
= mature evidence-based knowledge system
  + automated ingestion
  + research workflow
  + graph
  + partial ontology reasoning

DroneWiki
= full-stack knowledge application
  + RAG
  + GraphRAG
  + ontology-aware AI
  + knowledge-grounded drone concept builder
```

But it is **not yet** a verified autonomous drone engineering and research platform.

The safe sequence remains:

```text
Document reality
→ close architecture ambiguity
→ secure publication boundary
→ stabilize retrieval
→ formalize Engineering Ontology
→ build deterministic engineering tools
→ add verification/simulation
→ extend research workflow
→ build publication workflow
```

That sequence is the current approved conservative direction.
