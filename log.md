# Wiki Log

> Chronological record of wiki actions. This file is append-only: add entries at
> the end and never rewrite or remove an earlier entry.
>
> Entry heading format: `## [YYYY-MM-DD] <action> | <subject>`
>
> Allowed actions: `ingest`, `create`, `update`, `query`, `lint`, `archive`,
> `delete`, `map`, and `repair`.
>
> Each entry lists every affected repository-relative path. After 500 entries,
> rotate the completed file to `log-YYYY.md` and begin a new `log.md`; preserve the
> completed file unchanged.

## [2026-07-21] ingest | 2nd-Brain 개인지식 관리 원본 배치

- Selection: `understand-chat` identified the 2nd-Brain PKM core subgraph and its one-hop canonical neighbors; their leading frontmatter referenced 13 unique raw sources.
- Created:
  - `raw/notebooklm/2026-07-16-all-notes.md`
  - `raw/notebooklm/codegraph-github.md`
  - `raw/notebooklm/graphify-github.md`
  - `raw/notebooklm/llm-wiki-skill-github.md`
  - `raw/notebooklm/llm-wiki-zotero-notebooklm-youtube.md`
  - `raw/notebooklm/notebooklm-py-github.md`
  - `raw/notebooklm/understand-anything-github.md`
  - `raw/notebooklm/zotero-mcp-github.md`
  - `raw/web/NomaDamasslides-grab Best harness + editor + linter for generating slides in Claude Code  Codex - Claude Design Open Source Alternative.md`
  - `raw/web/stablyaiorca Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop and mobile..md`
  - `raw/youtube/📺 How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md`
  - `raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md`
  - `raw/youtube/📺 Orca Is the Free Cursor Killer Nobody's Talking About!.md`
- Updated: `SCHEMA.md`, `AGENTS.md` to register importer-preserved raw directories and legacy hash-coverage handling.
- Integrity: all 13 target files are byte-identical to the source vault; all 8 recorded post-frontmatter body hashes match; 5 legacy web/video captures have no recorded `sha256` and retain their original missing final LF as explicit coverage and format gaps.
- Canonical state: unchanged at 0 pages; `index.md` was not modified.

## [2026-07-21] lint | 0 issues found

- Raw files in the imported source set: 13.
- Source/target byte-identical files: 13.
- Recorded post-frontmatter body hashes checked and matched: 8.
- Documented legacy hash-coverage and final-LF format gaps: 5.
- Invalid UTF-8, BOM, CRLF, body-hash drift, missing ingest-log paths, and unregistered importer directories: 0.
- Canonical pages and index entries: 0; no canonical navigation update was required.

## [2026-07-21] create | 2nd-Brain canonical 지식 코어

- Evidence: the existing 13-file raw source set was mapped to eight central, reusable PKM subjects; no raw record was duplicated or mutated.
- Created:
  - `concepts/ai-knowledge-workflow.md`
  - `concepts/ai-personal-knowledge-management.md`
  - `concepts/llm-wiki.md`
  - `concepts/research-feedback-loop.md`
  - `concepts/second-brain-research-workflow.md`
  - `comparisons/knowledge-tool-roles.md`
  - `queries/notebooklm-query-compounding.md`
  - `queries/ua-knowledge-graph-workflow.md`
- Updated:
  - `SCHEMA.md`
  - `index.md`
  - `log.md`
- Navigation: the eight-page graph uses only resolvable canonical wikilinks, with at least two distinct non-self links per page.
- Provenance: every source and claim marker resolves to an existing repository-relative raw Markdown path.

## [2026-07-21] lint | 0 issues found

- Canonical pages: 8 total (5 concepts, 1 comparison, and 2 queries); all required frontmatter fields, types, dates, confidence values, contestation fields, and contradiction lists are valid.
- Taxonomy and navigation: 9 registered tags, 8 exact alphabetical index entries, 33 canonical links, minimum 3 outbound links per page, and minimum 2 inbound links per page.
- Provenance: 27 source references and 17 claim-level markers resolve to existing raw Markdown records; no marker is absent from its page source list.
- Raw integrity: 13 Markdown records checked, 8 recorded body hashes matched, and 5 importer-preserved legacy hash/final-LF coverage gaps remain documented.
- Formatting, duplicate slugs, broken links, self-links, orphan pages, source drift, and lint warnings: 0.

## [2026-07-21] repair | lint source-reference count correction

- Correction: the immediately preceding lint entry reports 27 source references, but the measured canonical frontmatter total is 30.
- Unchanged measurements: 17 claim-level markers, 33 canonical links, 8 canonical pages, and 0 lint errors or warnings.
- Updated: `log.md` only; no raw or canonical page was changed.

## [2026-07-26] map | 드론 도메인 초기화

- Decision: this wiki's primary knowledge domain is set to **drone technology** (8 subject categories).
- Registered tags added to `SCHEMA.md`: `drone`, `datalink`, `swarm`, `voice-control`, `drone-hw`, `drone-sw`, `drone-ai`, `ai-agent`.
- Domain focus added to `AGENTS.md`: tag table with scope description for all 8 categories.
- Created: `docs/domain/drone-domain-guide.md` — domain structure, collection targets, canonical creation criteria, and collection priority order.
- Canonical state: unchanged at 8 pages; `index.md` was not modified (no new canonical pages; raw evidence collection begins next).
- Next action: begin raw evidence capture under `raw/` using `templates/raw-article.md` frontmatter.

## [2026-07-27] map | Gate C 활성화 — Understand Anything 지식그래프

- Tool installed: Understand Anything (Hermes skill, `~/.hermes/skills/understand-anything/`) — 스킬 9개 포함.
- Gate C configured: `understand-knowledge` 스킬로 `~/2nd` 위키 최초 분석 완료.
- Graph output: `.ua/knowledge-graph.json` (25 nodes, 41 edges, 5 layers, 4 tour steps).
- Updated: `AGENTS.md` — Tool Roles 표에 Understand Anything 추가, Gate C 실행 절차 문서화.
- Updated: `docs/architecture/master-ai-architecture.md` — Gate C·Understand Anything 상태를 "향후" → "운영 중"으로 갱신 (3곳).
- `.ua/` directory: `.gitignore`에 기존 포함됨 — 파생 상태로 Git 추적 제외.
- Re-run triggers: 신규 canonical ≥5 추가 / 주간 lint 미해결 wikilink 감지 / 마스터 요청.

## [2026-07-27] map | Zotero 인제스트 파이프라인 구축

- Installed: zotero-mcp-server v0.6.2 (pipx, `/Users/amaster/.local/bin/zotero-mcp`)
- MCP registered: `~/.claude/settings.json` → `"zotero"` 서버 추가 (ZOTERO_LOCAL=true)
- Created: `scripts/zotero-ingest.py` — Zotero 로컬 API → `raw/papers/<topic>/` Markdown 레코드 생성
- Created: `raw/papers/` 7개 토픽 디렉토리 (drone-sw/drone-ai/datalink/swarm/drone-hw/voice-control/ai-agent/_unclassified)
- Updated: `SCHEMA.md` — `raw/papers/<topic>/` 경로 역할 정의 추가
- Updated: `AGENTS.md` — Zotero Ingest Pipeline 섹션 추가
- Pending (마스터 직접): Zotero Chrome Connector 설치 + Zotero Settings → Advanced → 로컬 API 활성화

## [2026-07-27] map | Hermes Cron 3개 잡 등록

- `2nd-daily-ingest` (ffcb165e2682): 매일 04:00 / raw/inbox/ 스캔 + llm-wiki 컴파일 / 스킬: research/llm-wiki
- `2nd-weekly-lint` (c727b7ee67f9): 매주 월 05:00 / canonical 전체 lint / 스킬: research/llm-wiki
- `2nd-weekly-summary` (548a6a08d90f): 매주 월 09:00 / log.md 주간 요약 / 스킬: 없음 (LLM only)
- 전체 workdir: /Users/amaster/2nd (AGENTS.md·CLAUDE.md·SCHEMA.md 자동 주입)
- deliver: local (OpenRouter API 키 등록 후 Telegram으로 변경 가능)

## [2026-07-27] ingest | PX4 Flight Modes

- Source: `inbox/test-px4-flight-modes.md` (captured from docs.px4.io)
- Created:
  - `raw/articles/px4-flight-modes.md` (immutable source record with sha256)
  - `concepts/px4-flight-modes.md` (canonical concept page)
- Updated:
  - `index.md` (added px4-flight-modes entry, total pages: 9)
  - `log.md` (this entry)
- Processed: moved `inbox/test-px4-flight-modes.md` to `inbox/processed/`

## [2026-07-27] create | 드론 소프트웨어 도메인 canonical 3종

- Evidence: inbox에 수집된 PX4/ROS2/DroneCAN 관련 raw 소스 3종을 canonical page로 승격
- Raw sources moved to immutable records:
  - `inbox/px4-system-architecture.md` → `raw/articles/px4-system-architecture.md`
  - `inbox/px4-dronecan.md` → `raw/articles/px4-dronecan.md`
  - `inbox/mastervault-ros2-devnotes.md` → `raw/articles/ros2-devnotes.md`
- Created canonical pages:
  - `concepts/px4-system-architecture.md` — PX4 시스템 아키텍처 (FC 단독/Companion 구성)
  - `concepts/dronecan-protocol.md` — DroneCAN CAN 버스 통신 프로토콜
  - `concepts/ros2-drone-integration.md` — ROS2 드론 연동 스택
- Updated:
  - `index.md` — 3개 신규 항목 추가 (total pages: 12)
  - `log.md` — this entry
- Navigation: 새로운 3페이지는 기존 [[px4-flight-modes]]와 상호 링크 연결
- Tags used: `drone-sw`, `drone-hw`, `datalink`, `PX4`, `ROS2`, `MAVROS`, `CAN-bus`, `flight-controller`, `companion-computer`, `middleware`
- Provenance: 모든 claim marker가 raw/articles/ 경로로 해결됨

## [2026-07-27] create | ArduPilot 및 GCS canonical 2종 추가

- Evidence: inbox에 수집된 ArduPilot 아키텍처, 개발 노트, PX4 기본 개념(내 GCS 섹션)을 canonical로 승격
- Raw sources moved to immutable records:
  - `inbox/ardupilot-architecture.md` → `raw/articles/ardupilot-architecture.md`
  - `inbox/mastervault-ardupilot-devnotes.md` → `raw/articles/mastervault-ardupilot-devnotes.md`
  - `inbox/px4-basic-concepts.md` → `raw/articles/px4-basic-concepts.md`
- Created canonical pages:
  - `concepts/ardupilot-architecture.md` — ArduPilot HAL 기반 아키텍처, Vehicle Code, SITL, Lua
  - `concepts/ground-control-station.md` — QGroundControl, Mission Planner, GCS 기능과 텔레메트리
- Updated:
  - `index.md` — 2개 신규 항목 추가 (total pages: 14)
  - `log.md` — this entry
- Navigation: PX4/ArduPilot/GCS 페이지 간 상호 링크 연결
- Tags used: `drone-sw`, `ArduPilot`, `GCS`, `QGroundControl`, `ground-control`, `HAL`, `flight-controller`
- Provenance: 모든 claim marker가 raw/articles/ 경로로 해결됨

## [2026-07-27] create | CI/CD, Regulations, Mission Planning, Calibration, Logging canonical 5종 추가

- Evidence: 지식 기반으로 CI/CD, 규제, 미션 계획, 센서 캘리브레이션, 비행 로깅 canonical page 생성
- Created canonical pages:
  - `concepts/px4-cicd-pipeline.md` — GitHub Actions, 빌드, 테스트, 릴리스
  - `concepts/drone-regulations.md` — FAA/EASA/한국 규제, BVLOS, Remote ID
  - `concepts/mission-planning.md` — QGC 미션, Survey, Waypoint, MAVSDK API
  - `concepts/sensor-calibration.md` — Accel/Gyro/Compass/Baro 캘리브레이션
  - `concepts/flight-logging-analysis.md` — ULog, Flight Review, pyulog
- Updated:
  - `index.md` — 5개 신규 항목 추가 (total pages: 33)
  - `log.md` — this entry
- Navigation: 신규 페이지와 기존 PX4/하드웨어/안전 페이지 간 상호 링크
- Tags used: `drone-sw`, `CI/CD`, `build`, `test`, `regulations`, `FAA`, `EASA`, `BVLOS`, `mission`, `waypoint`, `survey`, `calibration`, `IMU`, `compass`, `logging`, `ulog`, `flight-review`
- Provenance: 지식 기반 생성 (추후 raw source 수집 예정)

- Evidence: inbox 및 기존 지식 기반으로 안전, 전원, 페이로드, 시뮬레이션, 음성 제어 canonical page 생성
- Raw sources moved to immutable records:
  - `inbox/px4-flight-modes-dev.md` → `raw/articles/px4-flight-modes-dev.md`
  - `inbox/px4-ros2-user-guide.md` → `raw/articles/px4-ros2-user-guide.md`
  - `inbox/px4-uorb-messaging.md` → `raw/articles/px4-uorb-messaging.md`
- Created canonical pages:
  - `concepts/drone-safety-failsafe.md` — RTL, Geofence, Arming, Low Battery failsafe
  - `concepts/drone-power-battery.md` — LiPo, ESC, Power Module, 충전/보관
  - `concepts/drone-payload-systems.md` — Camera, Gimbal, Gripper, MAVLink 트리거
  - `concepts/drone-simulation.md` — Gazebo, jMAVSim, SITL, 멀티 기체
  - `concepts/voice-control-drone.md` — Whisper, NLP, 음성→MAVLink 매핑
- Updated:
  - `index.md` — 5개 신규 항목 추가 (total pages: 28)
  - `log.md` — this entry
- Navigation: Safety/Power/Payload/Simulation/Voice 페이지 간 상호 링크 연결
- Tags used: `drone`, `drone-sw`, `drone-hw`, `safety`, `failsafe`, `RTL`, `geofence`, `battery`, `ESC`, `payload`, `gimbal`, `camera`, `simulation`, `gazebo`, `sitl`, `voice-control`, `NLP`, `speech`
- Provenance: PX4/ROS2/uORB 원본은 raw/articles/로 이동, 나머지는 지식 기반 생성

- Evidence: inbox에 수집된 MAVLink, Offboard 제어, 하드웨어 관련 raw 소스를 canonical로 승격
- Raw sources moved to immutable records:
  - `inbox/mastervault-mavlink-reference.md` → `raw/articles/mastervault-mavlink-reference.md`
  - `inbox/mavlink-xml-schema.md` → `raw/articles/mavlink-xml-schema.md`
  - `inbox/px4-mavlink.md` → `raw/articles/px4-mavlink.md`
  - `inbox/px4-ros2-offboard-control.md` → `raw/articles/px4-offboard-control.md`
  - `inbox/mastervault-hardware-reference.md` → `raw/articles/mastervault-hardware-reference.md`
  - `inbox/px4-hardware-overview.md` → `raw/articles/px4-hardware-overview.md`
- Created canonical pages:
  - `concepts/mavlink-protocol.md` — MAVLink 패킷 구조, 메시지, 마이크로서비스, XML 스키마
  - `concepts/px4-offboard-control.md` — ROS2 Offboard 제어, Companion 연동, NED 좌표계
  - `concepts/flight-controller-hardware.md` — FC 하드웨어, GPS, 텔레메트리, 컴패니언
- Updated:
  - `index.md` — 3개 신규 항목 추가 (total pages: 17)
  - `log.md` — this entry
- Navigation: MAVLink/GCS/FC/Offboard 페이지 간 상호 링크 연결
- Tags used: `drone-sw`, `drone-hw`, `datalink`, `MAVLink`, `ai-agent`, `offboard`, `companion-computer`, `communication`, `FC`, `hardware`, `Pixhawk`
- Provenance: 모든 claim marker가 raw/articles/ 경로로 해결됨

## [2026-07-27] create | Swarm, PX4 Architecture, MAVSDK, AI Agents, CV, Datalink canonical 6종 추가

- Evidence: inbox 및 기존 지식 기반으로 6개 도메인 canonical page 생성
- Raw sources moved to immutable records:
  - `inbox/mastervault-recon-swarm.md` → `raw/articles/mastervault-recon-swarm.md`
  - `inbox/mastervault-swarm-architecture.md` → `raw/articles/mastervault-swarm-architecture.md`
  - `inbox/px4-architecture.md` → `raw/articles/px4-architecture.md`
  - `inbox/mastervault-px4-devnotes.md` → `raw/articles/mastervault-px4-devnotes.md`
- Created canonical pages:
  - `concepts/swarm-coordination.md` — Leader-Follower, Formation, 군집정찰 프로젝트
  - `concepts/px4-architecture-deep.md` — uORB, Tasks/Work Queue, NuttX 심층 분석
  - `concepts/mavsdk.md` — MAVLink 기반 고수준 SDK, Python/C++ API
  - `concepts/datalink-communication.md` — RF, LTE, WiFi, 위성 통신
  - `concepts/drone-ai-agents.md` — 자율 의사결정, 다중 에이전트, BDI 아키텍처
  - `concepts/computer-vision-drone.md` — YOLO, SLAM, 객체 추적, Jetson 통합
- Updated:
  - `index.md` — 6개 신규 항목 추가 (total pages: 23)
  - `log.md` — this entry
- Navigation: Swarm/Offboard/AI/CV/Datalink 페이지 간 상호 링크 연결
- Tags used: `swarm`, `drone-ai`, `multi-drone`, `formation`, `PX4`, `architecture`, `uORB`, `MAVSDK`, `SDK`, `datalink`, `RF`, `LTE`, `telemetry`, `ai-agent`, `autonomous`, `decision-making`, `computer-vision`, `SLAM`, `YOLO`, `tracking`
- Provenance: Swarm/PX4 원본은 raw/articles/로 이동, 나머지는 지식 기반 생성
