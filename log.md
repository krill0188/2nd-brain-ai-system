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

## [2026-07-30] ingest | RSS 뉴스 및 YOLO 릴리스 인제스트

- Source files from `inbox/`:
  - `fetch-2026-07-29-rss-dronedj.md`
  - `fetch-2026-07-29-rss-dronelife.md`
  - `fetch-2026-07-29-rss-oscarliang-fpv.md`
  - `fetch-2026-07-29-rss-suasnews-regulation.md`
  - `fetch-2026-07-29-rss-suasnews.md`
  - `fetch-2026-07-30-rss-dronedj.md`
  - `fetch-2026-07-30-rss-dronelife.md`
  - `fetch-2026-07-30-rss-suasnews.md`
  - `fetch-2026-07-30-yolo.md`
- Created entities:
  - `entities/doordash-air.md` — DoorDash Air FAA Part 135 인증
  - `entities/droneshield.md` — DroneShield RfAI-3 AI 엔진
  - `entities/perceptual-robotics.md` — 영국 풍력 터빈 검사 드론 기업
  - `entities/terra-drone.md` — 일본 드론 배터리 사업
  - `entities/xtend-ai-robotics.md` — XTEND-JFB $15억 합병
- Created concepts:
  - `concepts/dji-everest-mapping.md` — 에베레스트 매핑 프로젝트
  - `concepts/dji-terra.md` — DJI Terra AI 매핑 소프트웨어
  - `concepts/fcc-drone-regulations.md` — FCC 외국 드론 규제 정책
  - `concepts/lockheed-martin-morfius.md` — 드론 스웜 대응 시스템
  - `concepts/yolo-v8-4-112.md` — YOLO v8.4.112 릴리스 정보
- Updated: `index.md` (67 pages), `log.md`
- Moved sources to: `inbox/processed/` (9 files)

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

## [2026-07-28] ingest | inbox 배치 — PX4, ArduPilot, MAVLink, 스웜 소스 처리

- 수집: `inbox/*.md` 20개 파일 → `inbox/processed/`로 이동 완료
- Canonical 생성:
  - `concepts/recon-swarm-project.md` — 지능형 자율 군집정찰 프로젝트
  - `concepts/swarm-modes.md` — Formation, Follow-Leader, Area Search 모드
  - `concepts/mavlink-protocol-deep.md` — 패킷 구조, XML 스키마, 마이크로서비스
  - `concepts/dronecan-deep.md` — CAN 버스 프로토콜 상세
  - `concepts/px4-architecture-deep.md` — uORB, Tasks, Work Queue 분석
  - `concepts/ros2-drone-deep.md` — ROS2 연동과 Offboard 제어
- 업데이트:
  - `index.md` — 6개 새 항목 추가 (total pages: 39)
  - `log.md` — this entry
- Cross-links: 새 6개 페이지는 기존 canonical 페이지와 상호 연결
- Tags: `swarm`, `drone-ai`, `datalink`, `drone-hw`, `drone-sw`, `ai-agent`

## [2026-07-28] ingest | inbox 드론 엔티티 4종 canonical 승격

- 수집: `inbox/entity-*.md` 4개 파일
- 원본 이동: `inbox/entity-*.md` → `raw/articles/` 4개 파일
- Canonical 생성:
  - `entities/pixhawk.md` — Pixhawk 하드웨어 플랫폼 엔티티
  - `entities/ardupilot.md` — ArduPilot 비행 스택 엔티티  
  - `entities/mavlink-protocol.md` — MAVLink 통신 프로토콜 엔티티
  - `entities/px4-flight-stack.md` — PX4 비행 스택 엔티티
- 업데이트:
  - `index.md` — 4개 Entities 항목 추가, total pages 39 → 43
  - `log.md` — this entry
- 이동: 원본 4개 파일 `inbox/processed/`로 이동 완료
- Cross-links: 4개 엔티티 페이지는 PX4/ArduPilot/MAVLink/DroneCAN/GCS 등 기존 개념 페이지와 상호 연결
- Tags: `drone-hw`, `drone-sw`, `datalink`, `drone`

## [2026-07-29] ingest | inbox RSS 및 GitHub 릴리스 소스 15개 canonical 컴파일

- 수집된 raw sources:
  - `inbox/fetch-2026-07-29-rss-suasnews-regulation.md`
  - `inbox/fetch-2026-07-29-rss-dronelife.md`
  - `inbox/fetch-2026-07-29-rss-suasnews.md`
  - `inbox/fetch-2026-07-29-rss-dronedj.md`
  - `inbox/fetch-2026-07-29-rss-oscarliang-fpv.md`
  - `inbox/fetch-2026-07-29-opencv.md`
  - `inbox/fetch-2026-07-29-yolo.md`
  - `inbox/fetch-2026-07-29-ros2.md`
  - `inbox/fetch-2026-07-29-missionplanner.md`
  - `inbox/fetch-2026-07-29-qgroundcontrol.md`
  - `inbox/fetch-2026-07-29-pymavlink.md`
  - `inbox/fetch-2026-07-29-mavsdk.md`
  - `inbox/fetch-2026-07-29-betaflight.md`
  - `inbox/fetch-2026-07-29-ardupilot.md`
  - `inbox/fetch-2026-07-29-px4.md`

- 생성된 canonical pages (concepts/):
  - `concepts/betaflight.md` — domain: flight-control
  - `concepts/opencv.md` — domain: ai-autonomy
  - `concepts/yolo.md` — domain: ai-autonomy
  - `concepts/ros2-lyrical.md` — domain: gcs-software
  - `concepts/mission-planner.md` — domain: gcs-software
  - `concepts/qgroundcontrol.md` — domain: gcs-software
  - `concepts/pymavlink.md` — domain: comms-protocol
  - `concepts/mavsdk-release.md` — domain: comms-protocol
  - `concepts/ardupilot-plane-4-7.md` — domain: flight-control
  - `concepts/px4-v1-17.md` — domain: flight-control
  - `concepts/fpv-hardware.md` — domain: hardware
  - `concepts/drone-news-regulations.md` — domain: regulations
  - `concepts/drone-news-ops.md` — domain: ops-mission
  - `concepts/drone-news-hardware.md` — domain: hardware

- 업데이트된 navigation:
  - `index.md` — 페이지 수 43 → 58, 새 항목 알파벳 순 추가
  
- 이동된 raw sources:
  - 모두 `inbox/processed/`로 이동

## [2026-07-27] ingest | arXiv 논문 3개 수집

- **voice-control**: `raw/papers/voice-control/lim2025-taking-flight-with-dialogue.md`
  - Title: Taking Flight with Dialogue: Enabling Natural Language Control for PX4-based Drone Agent
  - Topics: PX4, ROS2, LLM, VLM, voice control
  - Source: arXiv:2506.07509 [cs.RO]

- **swarm**: `raw/papers/swarm/cai2026-progress-aware-docking.md`
  - Title: A Progress-Aware Leader-Follower Midair Docking System for Dual-Drone Aerial Manipulation  
  - Topics: Leader-Follower, dual-drone docking, PX4, ROS2
  - Source: arXiv:2605.29410 [cs.RO], IEEE CASE 2026

- **drone-sw**: `raw/papers/drone-sw/jacinto2024-pegasus-simulator.md`
  - Title: Pegasus Simulator: An Isaac Sim Framework for Multiple Aerial Vehicles Simulation
  - Topics: PX4, ROS2, NVIDIA Isaac Sim, multi-drone simulation
  - Source: arXiv:2307.05263 [cs.RO], IEEE ICUAS 2024

## [2026-07-27] ingest | 추가 arXiv 논문 6개 수집

- **datalink**: 
  - `koubaa2019-mavlink-survey.md` — MAVLink 종합 서베이 (IEEE Access 2019)
  - `allouch2019-mavsec.md` — MAVLink 보안 프로토콜 (IWCMC 2019)

- **swarm**: 
  - `li2025-airswarm.md` — COTS 드론 멀티-UAV 플랫폼 (arXiv 2025)

- **drone-ai**: 
  - `shapira2025-icdnet.md` — Visual-Inertial SLAM 딥러닝 (arXiv 2025)
  - `radwan2024-uav-slam-gpsdenied.md` — GPS 없는 환경 3D SLAM (IEEE ICUAS 2024)

## [2026-07-30] ingest | arXiv 논문 및 RSS 뉴스 인제스트

- Source files from `inbox/`:
  - `fetch-2026-07-30-arxiv-chained-attacks-on-drone-based-federated-learning-from-netwo.md`
  - `fetch-2026-07-30-arxiv-distributed-continuous-aerial-surveillance-by-uas-swarms-und.md`
  - `fetch-2026-07-30-arxiv-electromagnetic-neural-network-for-direction-of-arrival-esti.md`
  - `fetch-2026-07-30-arxiv-federated-lightweight-intrusion-detection-in-drone-swarms-wi.md`
  - `fetch-2026-07-30-arxiv-flight-ready-lidar-inertial-odometry-for-embedded-drone-plat.md`
  - `fetch-2026-07-30-arxiv-high-level-spatial-dubins-airplane-based-reference-smoothing.md`
  - `fetch-2026-07-30-arxiv-linear-stability-analysis-of-an-indi-pitch-rate-controller-u.md`
  - `fetch-2026-07-30-arxiv-stacked-intelligent-metasurfaces-assisted-uav-communications.md`
  - `fetch-2026-07-30-arxiv-vertical-pinching-antenna-systems-v-pas-aided-uav-communicat.md`
  - `fetch-2026-07-30-rss-dronedj.md`
  - `fetch-2026-07-30-rss-suasnews.md`

- Created concepts:
  - `concepts/chained-attacks-drone-fl.md` — 드론 FL 체인 공격 (DoS + 사칭)
  - `concepts/distributed-aerial-surveillance-swarm.md` — LTL 기반 분산 공중 감시
  - `concepts/emnn-doa-estimation.md` — 전자기 신경망 DOA 추정
  - `concepts/federated-lightweight-intrusion-detection.md` — FL+KD 경량 IDS
  - `concepts/flight-ready-lidar-inertial-odometry.md` — 임베디드 LIO 시스템
  - `concepts/spatial-dubins-quadrotor-control.md` — Dubins 기반 쿼드로터 제어
  - `concepts/indi-stability-tilt-rotor-vtol.md` — INDI VTOL 안정성 분석
  - `concepts/stacked-intelligent-metasurfaces.md` — SIM 기반 UAV 통신
  - `concepts/vertical-pinching-antenna-systems.md` — V-PAS 수직 안테나 시스템
  - `concepts/dji-easa-sail-bvlos.md` — DJI EASA BVLOS 승인
  - `concepts/wing-nhs-medical-delivery.md` — Wing NHS 의료 배달
  - `concepts/zipline-us-expansion.md` — Zipline 미국 확대
  - `concepts/montis-avalanche-faa-approval.md` — MONTIS FAA 승인
  - `concepts/brinc-emergency-drone-funding.md` — BRINC $125M 자금 조달
  - `concepts/amazon-mk30-safety-incident.md` — Amazon MK30 안전 사고

- Updated: `index.md` (80 pages), `log.md`
- Moved sources to: `inbox/processed/` (11 files)

## [2026-07-30] ingest | arXiv 및 기타 소스 인제스트

- Source files from `inbox/`:
  - `fetch-2026-07-30-arxiv-a-cross-layered-multi-drone-coordination-for-medical-supply-.md`
  - `fetch-2026-07-30-arxiv-a-heuristic-approach-for-performance-tuning-in-rl-based-quad.md`
  - `fetch-2026-07-30-arxiv-a-model-for-mediating-multi-modal-human-intent-into-safe-man.md`
  - `fetch-2026-07-30-arxiv-active-sensing-assisted-uav-communications-with-jittering-fr.md`
  - `fetch-2026-07-30-arxiv-aerial-inspection-behaviors-via-rl-based-quadrotor-control-f.md`
  - `fetch-2026-07-30-arxiv-decentralized-uav-swarms-for-ground-target-protection-in-gps.md`
  - `fetch-2026-07-30-arxiv-e2e-fly-an-integrated-training-to-deployment-system-for-end-.md`
  - `fetch-2026-07-30-arxiv-inverse-reinforcement-learning-enabled-digital-twin-for-inte.md`
  - `fetch-2026-07-30-arxiv-lightweight-safe-reinforcement-learning-for-end-to-end-uav-n.md`
  - `fetch-2026-07-30-arxiv-mars-dragonfly-agile-and-robust-flight-control-of-modular-ae.md`
  - `fetch-2026-07-30-arxiv-neurosymland-neuro-symbolic-landing-site-assessment-for-robu.md`
  - `fetch-2026-07-30-arxiv-skyjepa-learning-long-horizon-world-models-for-zero-shot-sim.md`
  - (and 38 additional files: crossref papers, youtube videos, etc.)

- Created concepts:
  - `concepts/cross-layered-medical-drone-coordination.md` — CTDE 기반 의료 배달 다중 드론 협업
  - `concepts/rl-quadrotor-tunable-control.md` — RL 보상 설계 기반 쿼드로터 성능 튜닝
  - `concepts/multi-modal-human-intent-uav.md` — 다중 모달리티 인간 의도 중재
  - `concepts/decentralized-swarm-gps-denied.md` — GPS/통신 차단 환경 분산 군집
  - `concepts/active-sensing-uav-communication.md` — 감지 지원 UAV 통신 (AoA)
  - `concepts/mars-dragonfly-modular-aerial.md` — 모듈형 항공 로봇 시스템(MARS)
  - `concepts/neurosymland-landing-assessment.md` — 신경-기호적 착륙 장소 평가
  - `concepts/e2e-fly-end-to-end-quadrotor.md` — 종단간 쿼드로터 자율 시스템
  - `concepts/skyjepa-world-models.md` — JEPA 스타일 장기 예측 세계 모델
  - `concepts/lightweight-safe-rl-uav.md` — 밀집 환경 경량 안전 RL 내비게이션
  - `concepts/digital-twin-intent-drone-networks.md` — 의도 기반 드론 네트워크 디지털 트윈

- Updated: `index.md` (92 pages), `log.md`
- Moved sources to: `inbox/processed/` (58 files)

- **drone-hw**: 
  - `danial2025-microdrone-slam.md` — Micro 드론 단안 SLAM (arXiv 2025)

## [2026-07-30] ingest | 오늘의 새 자료 수집

### 논문 (arXiv)
- **swarm**: `x... [truncated]
## [2026-07-30] manual | FC 파라미터 설정 시리즈 6편 작성

- 생성: fc-vendor-param-guide(hardware) / px4-params-by-version, ardupilot-params-by-version(flight-control) / pixhawk-setup-params, cuav-setup-params, holybro-setup-params(hardware)
- 배경: 제조사별 FC·펌웨어 버전별 파라미터 자료 공백 (마스터 지적 — 사용자 수요 최상위)
- Cross-links: sensor-calibration, pid-tuning-control 연결

## [2026-07-30] auto | 파라미터 diff 자동생성 시스템 (2단계)

- scripts/param-diff.py: PX4 펌웨어 내장 parameter_xml + ArduPilot 버전별 공식 문서 자동 비교
- 초기 생성: param-diff-px4-1-16-0-1-17-0 / param-diff-copter-4-6-0-4-7-0
- fetch-inbox.sh --auto 훅: 신규 릴리즈 감지 시 직전 버전 대비 diff 페이지 자동 생성

## [2026-07-31] ingest | Inbox daily ingest

- Source files from `inbox/`:
  - `fetch-2026-07-30-crossref-learning-heuristics-with-vision-transformers-for-risk-aware-.md`
  - `fetch-2026-07-30-crossref-optimising-360-panoramic-imaging-fisheye-image-stitching-for.md`
  - `fetch-2026-07-30-crossref-path-planning-for-urban-transmission-tower-inspection-using-.md`
  - `fetch-2026-07-30-crossref-s2anet-semantic-spatial-driven-alignment-salient-object-dete.md`
  - `fetch-2026-07-30-yt-32ish-questions-with-an-mit-robotics-researcher-and-actor.md`
  - `fetch-2026-07-30-yt-3d-printing-additive-manufacturing-full-course.md`
  - `fetch-2026-07-30-yt-aeon-ul16-aurora2305-2500kv-5x43x3-v1s-hqprop-kiss-esc-4in1-.md`
  - `fetch-2026-07-30-yt-behind-the-popular-ai-tools-lies-a-crucial-bit-of-tech-calle.md`
  - `fetch-2026-07-30-yt-bitcraze-at-icra-2026-crazyflie-swarm-highlights-from-vienna.md`
  - `fetch-2026-07-30-yt-capture-every-detail4-august-2026-12-pm-gmt.md`
  - `fetch-2026-07-30-yt-depth-anything-v2-pytorch-code-generation-with-matlab-coder.md`
  - `fetch-2026-07-30-yt-dji-mavic-4-pro-unboxing.md`
  - `fetch-2026-07-30-yt-fcc-investigates-dji-linked-tech.md`
  - `fetch-2026-07-30-yt-kiss-esc-prototype-test-flying-back-in-2017.md`
  - `fetch-2026-07-30-yt-learning-agile-quadrotor-flight-in-the-real-world-rss-2026.md`
  - `fetch-2026-07-30-yt-many-of-us-want-home-robots-whats-the-holdup.md`
  - `fetch-2026-07-30-yt-marine-corps-fiber-optic-live-fire-strike-at-camp-pendleton-.md`
  - `fetch-2026-07-30-yt-motion-aware-event-suppression-for-event-cameras-rss-2026.md`
  - `fetch-2026-07-30-yt-nemyx-drone-swarm-demo-with-british-army-auterion.md`
  - `fetch-2026-07-30-yt-qa-livestream---august-17-2026.md`
  - `fetch-2026-07-30-yt-ratefpv-f4-40a-aio-flight-controller-a-first-look.md`
  - `fetch-2026-07-30-yt-stop-leaking-construction-profit-with-the-right-gnss-tools.md`
  - `fetch-2026-07-30-yt-yolov11-litert-code-generation-with-matlab-coder.md`
  - `fetch-2026-07-31-arxiv-uav-swarming-for-air-ground-isac-via-cross-region-cooperatio.md`
  - `fetch-2026-07-31-crossref-a-two-layer-multi-objective-planner-for-heterogeneous-uav-as.md`
  - `fetch-2026-07-31-crossref-multi-objective-electric-vehicle-drone-routing-problem-incor.md`
  - `fetch-2026-07-31-crossref-multiscale-cross-layer-interaction-and-coordinated-symmetric.md`
  - `fetch-2026-07-31-rss-dronedj.md`
  - `fetch-2026-07-31-rss-dronelife.md`
  - `fetch-2026-07-31-rss-suasnews.md`
  - `fetch-2026-07-31-yt-agentic-ai-complete-course-for-beginners.md`
  - `fetch-2026-07-31-yt-auterionos-powering-autonomous-mass-across-air-land-sea-aute.md`
  - `fetch-2026-07-31-yt-darpa-offers-65mm-for-impossible-heavy-lift-challenge.md`
  - `fetch-2026-07-31-yt-dji-osmo-pocket-4p-is-herethe-dual-lens-cinematic-pocket-gim.md`
  - `fetch-2026-07-31-yt-high-speed-drone-los-flying-in-2020-5s-264kmh.md`
  - `fetch-2026-07-31-yt-rc-news-kite-gcs-goes-into-release-candidate-a-brand-new-mod.md`
  - `fetch-2026-07-31-yt-tiny-fpv-whoop-racespec-v2-flying---edit.md`
- Created entities:
  - `entities/auterion.md` — PX4 기반 드론 소프트웨어 플랫폼 기업
  - `entities/bitcraze.md` — Crazyflie 나노 드론 플랫폼
  - `entities/kite-gcs.md` — ArduPilot/INAV/PX4 지원 현대적 GCS
  - `entities/ratefpv.md` — FPV 드론 AIO FC 제조업체
- Created concepts:
  - `concepts/agile-quadrotor-learning.md` — 실제 환경 민첩 쿼드로터 학습
  - `concepts/event-camera-drone.md` — 이벤트 카메라 드론 비전
  - `concepts/drone-news-2026-07-31.md` — 2026-07-31 드론 업계 뉴스
  - `concepts/uav-isac-cross-region.md` — UAV ISAC 교차 지역 협력
- Updated: `index.md` (106 pages), `log.md`
- Moved sources to: `inbox/processed/` (37 files)

## [2026-08-01] ingest | 2026-08-01 인제스트 — MAVLink-M, QGC v5.1.0, DJI 하드웨어, AI 연구

- Source files from `inbox/` (17 files):
  - `fetch-2026-08-01-yt-this-drone-can-chase-f1-cars.md`
  - `fetch-2026-08-01-yt-a-new-era-of-interoperable-payloads-begins-at-the-dronecode-.md`
  - `fetch-2026-08-01-yt-radial-impeller-drone-fly-by-drone-fpv-diy-rc-fpvdrone-quadm.md`
  - `fetch-2026-08-01-yt-unbox-slip-it-into-your-pocket-start-rolling-osmo-pocket-4.md`
  - `fetch-2026-08-01-yt-three-moves-one-gimbal-all-in-dji-rs-5.md`
  - `fetch-2026-08-01-rss-oscarliang-fpv.md`
  - `fetch-2026-08-01-rss-dronelife.md`
  - `fetch-2026-08-01-rss-dronedj.md`
  - `fetch-2026-08-01-qgroundcontrol.md`
  - `fetch-2026-08-01-yolo.md`
  - `fetch-2026-08-01-crossref-graph-neural-network-driven-anomaly-detection-framework-for-.md`
  - `fetch-2026-08-01-crossref-detection-aided-enhanced-reweighted-atomic-norm-minimization.md`
  - `fetch-2026-08-01-yt-중고등학생을-위한-피지컬-ai-로봇팔자율주행ai-로봇-체험-프로그램-소개.md`
  - `fetch-2026-08-01-yt-윈도우-python-개발환경-visual-studio-code-miniconda-claude-code-설치-.md`
  - `fetch-2026-08-01-yt-kubernetes-operator-best-practices-kubebuilder-deep-dive.md`
  - `fetch-2026-08-01-yt-how-to-verify-generated-code-using-pil-support-package-for-r.md`
  - `fetch-2026-08-01-yt-installation-and-hardware-setup-support-package-for-renesas-.md`
- Created concepts:
  - `concepts/high-speed-drone-tracking.md` — 고속 추적 드론 기술
  - `concepts/mavlink-m-interoperability.md` — MAVLink-M 상호운용성
  - `concepts/radial-impeller-drone.md` — 방사형 임펠러 드론
  - `concepts/hglrc-talon-cinewhoop.md` — HGLRC Talon 시네후프 리뷰
  - `concepts/gnn-uav-anomaly-detection.md` — GNN 기반 UAV 이상 탐지
  - `concepts/uav-swarm-target-localization.md` — UAV 스웜 표적 위치 추정
  - `concepts/drone-news-2026-08-01.md` — 2026-08-01 드론 뉴스
  - `concepts/drone-delivery-news.md` — 드론 배달 뉴스
- Created entities:
  - `entities/qgroundcontrol.md` — QGroundControl v5.1.0
  - `entities/dji-osmo-pocket-4.md` — DJI Osmo Pocket 4P
  - `entities/dji-rs-5.md` — DJI RS 5
  - `entities/yolo-v8-4-114.md` — YOLO v8.4.114
- Updated: `index.md` (114 pages), `log.md`
- Moved sources to: `inbox/processed/` (17 files)


## [2026-08-01] research-promote | 지식베이스에 축적된 마이크로드론 온보드 SLAM 관련 문서들을 종합했을 때 공통적인 기술 트렌드는 무엇인가?

- Source: `research/drafts/20260801-research-1785543589.md` (마스터 승인)
- Created pages:
  - `concepts/micro-drone-slam-imu-vio-lidar-uav-livox-mid-360-pixhawk-4-m.md` — 검색 결과에서 "micro drone"으로 명시된 SLAM 사례는 카메라+IMU(VIO) 조합을 사용한 반면, LiDAR-관성 오도메트리 사례는 더 큰 임베디드 UAV 플랫폼(Li
  - `concepts/gps-uav-imu.md` — GPS 미수신 환경에 특화된 마이크로드론/UAV 위치추정 기법들은 공통적으로 외부 위치 인프라(GPS) 없이 온보드 카메라·IMU·옵티컬 플로우 등 상대적/자기완결적 센싱에만 의존
- Updated: `index.md`

## [2026-08-02] ingest | Inbox 배치 인제스트 (10 sources)

- Source files from `inbox/`:
  - `fetch-2026-08-02-crossref-etfnet-an-efficient-transformer-based-rgbir-fusion-network-f.md`
  - `fetch-2026-08-02-rss-dronelife.md`
  - `fetch-2026-08-02-yolo.md`
  - `fetch-2026-08-02-yt-flying-over-people-with-a-drone-whats-actually-legal.md`
  - `fetch-2026-08-02-yt-how-to-configure-dios-as-inputs-support-package-for-renesas-.md`
  - `fetch-2026-08-02-yt-how-to-work-with-tsg3-support-package-for-renesas-rh850-mcus.md`
  - `fetch-2026-08-02-yt-passion-mission-all-for-padel-dji-avata-360.md`
  - `fetch-2026-08-02-yt-rules-for-flying-a-drone-over-people.md`
  - `fetch-2026-08-02-yt-wallefpv-lightening3-hd-quad-a-real-hoot-and-only-53g-with-w.md`
  - `fetch-2026-08-02-yt-whats-waiting-on-the-other-side-of-the-lake-osmo-pocket-4p.md`
- Created entities:
  - `entities/geocomm.md` — 위치 정보 및 DFR Routing 기술 기업
  - `entities/skyfireai.md` — 공익안전 자율 드론 플랫폼 기업
  - `entities/wallefpv.md` — FPV 드론 하드웨어 제조업체
- Created concepts:
  - `concepts/rgb-ir-fusion-uav-detection.md` — Transformer 기반 RGB-IR 퓨전 UAV 객체 검출
  - `concepts/yolo-v8-4-115.md` — YOLO v8.4.115 릴리스 (HUB→Platform 전환)
  - `concepts/drone-first-responder-dfr.md` — 응급 대응 드론 활용 프로그램
- Updated: `index.md` (127 pages), `log.md`
- Moved sources to: `inbox/processed/` (10 files)

## [2026-08-03] ingest | FAA 규제 및 드론 하드웨어 뉴스 인제스트

- Source files from `inbox/`:
  - `fetch-2026-08-03-yt-how-to-configure-dios-as-outputs-support-package-for-renesas.md`
  - `fetch-2026-08-03-yt-it-was-never-the-moment-that-was-missing-osmo-pocket-4p.md`
  - `fetch-2026-08-03-yt-f28-at-night-the-stars-come-through-dji-osmo-action-6.md`
  - `fetch-2026-08-03-yt-qa-livestream---august-2-2026.md`
  - `fetch-2026-08-03-yt-installing-the-pixhawk-into-the-frame-and-testing-motors-ard.md`
  - `fetch-2026-08-03-fedreg-faa-2026-06297.md`
  - `fetch-2026-08-03-fedreg-faa-2026-07585.md`
  - `fetch-2026-08-03-fedreg-faa-2026-08943.md`
  - `fetch-2026-08-03-fedreg-faa-2026-13126.md`
  - `fetch-2026-08-03-fedreg-faa-2026-15417.md`
  - `fetch-2026-08-03-rss-parrot.md`
  - `fetch-2026-08-03-rss-skydio.md`
  - `fetch-2026-08-03-rss-dji-enterprise.md`
  - `fetch-2026-08-03-rss-oscarliang-fpv.md`
  - `fetch-2026-08-03-betaflight.md`
  - `fetch-2026-07-30-rss-suasnews.md`
- Created entities:
  - `entities/parrot.md` — 프랑스 4G 연결 드론 기업
  - `entities/skydio.md` — 미국 AI 자율 드론 기업
- Created concepts:
  - `concepts/dji-osmo-action-6.md` — DJI 액션 카메라 6세대
  - `concepts/faa-section-927-waiver.md` — FAA Section 927 면제 프로세스
  - `concepts/faa-deter-program.md` — FAA DETER UAS 집행 프로그램
  - `concepts/faa-section-2209-uafr.md` — FAA Section 2209 UAFR 제한
  - `concepts/faa-uas-environmental-assessment.md` — FAA UAS 환경평가
  - `concepts/uk-caa-airspace-architecture.md` — 영국 CAA Airspace Architecture
  - `concepts/edgetx-custom-audio.md` — EdgeTX 커스텀 오디오 설정
- Updated:
  - `concepts/betaflight.md` — 2026.6.1 릴리스 정보 추가
  - `index.md` (135 pages), `log.md`
- Moved sources to: `inbox/processed/` (16 files)

## [2026-08-04] ingest | Inbox batch — RSS/YouTube/arXiv/crossref sources

- Source files from `inbox/`:
  - `fetch-2026-08-04-arxiv-mrope-a-multi-robot-safe-cooperative-strategy-via-combined-p.md`
  - `fetch-2026-08-04-crossref-dronuum-a-smart-and-energy-efficient-drone-application-withi.md`
  - `fetch-2026-08-04-crossref-one-size-doesnt-fit-all-divide-and-conquer-detector-for-uav-.md`
  - `fetch-2026-08-04-rss-dji-enterprise.md`
  - `fetch-2026-08-04-rss-dronedj.md`
  - `fetch-2026-08-04-rss-dronelife.md`
  - `fetch-2026-08-04-rss-oscarliang-fpv.md`
  - `fetch-2026-08-04-rss-parrot.md`
  - `fetch-2026-08-04-rss-skydio.md`
  - `fetch-2026-08-04-rss-suasnews.md`
  - `fetch-2026-08-04-yt-6g-isac-implementation-with-matlab-and-usrp.md`
  - `fetch-2026-08-04-yt-elrs-41-makes-binding-easier-than-ever.md`
  - `fetch-2026-08-04-yt-from-tricky-lighting-to-fleeting-details-camera-keeps-your-v.md`
  - `fetch-2026-08-04-yt-low-level-graphics-in-c-pixel-manipulation-and-frame-buffers.md`
  - `fetch-2026-08-04-yt-pov-flying-through-a-waterfall-dji-osmo-nano.md`
- Created concepts:
  - `concepts/6g-isac-matlab-usrp.md` — 6G ISAC MATLAB/USRP 구현
  - `concepts/dji-matrice-5-rumor.md` — DJI Matrice 5 루머 및 O4 Ground Station
  - `concepts/dji-osmo-nano.md` — DJI Osmo Nano 52g 카메라
  - `concepts/dji-osmo-pocket-4p-dlog2.md` — DJI Osmo Pocket 4P D-Log 2
  - `concepts/divide-conquer-uav-detector.md` — UAV 분할-정복 탐지기
  - `concepts/dronuum-computing-continuum.md` — Computing Continuum 드론 앱
  - `concepts/elrs-41-release.md` — ELRS 4.1 릴리스
  - `concepts/eve-air-mobility-transition.md` — Eve Air Mobility 전환 비행
  - `concepts/event38-tb2-drops-integration.md` — Event38-TB2 DROPS 통합
  - `concepts/fpv-antenna-guide.md` — FPV 안테나 가이드
  - `concepts/hoverair-versa.md` — HoverAir Versa 하이브리드 카메라
  - `concepts/ideaforge-yeti-heavy-lift.md` — ideaForge YETI 헤비리프트
  - `concepts/mrope-multi-robot-safety.md` — MROPE 다중 로봇 안전 전략
  - `concepts/skydio-centralsquare-dfr-integration.md` — Skydio-CentralSquare DFR 통합
  - `concepts/uk-caa-bvlos-scale.md` — UK CAA BVLOS 상용화 로드맵
- Updated: `index.md` (149 pages), `log.md`
- Moved sources to: `inbox/processed/` (15 files)

## [2026-08-05] ingest | Emlid RTK, DJI Mic, C-UAS 기업, 의료 드론 배달 인제스트

- Source files from `inbox/`:
  - `fetch-2026-08-05-yt-emlid-corrections-get-centimeter-accuracy-with-your-reach-in.md`
  - `fetch-2026-08-05-yt-how-to-get-an-rtk-fix-with-emlid-corrections.md`
  - `fetch-2026-08-05-yt-meet-dji-mic-mini-2s---capture-every-detail.md`
  - `fetch-2026-08-05-yt-edgetx-trainer-setup-using-a-cable-super-simple.md`
  - `fetch-2026-08-05-rss-dronelife.md`
  - `fetch-2026-08-05-rss-suasnews.md`
  - `fetch-2026-08-05-rss-parrot.md`
  - `fetch-2026-08-05-rss-skydio.md`
  - `fetch-2026-08-05-rss-dji-enterprise.md`
  - `fetch-2026-08-05-rss-dronedj.md`
- Created entities:
  - `entities/fortem-technologies.md` — DHS C-UAS IDIQ 주계약자
  - `entities/monava.md` — 스웨덴-핀란드 C-UAS 기업
  - `entities/sol-one.md` — 벨기에 자율 드론 시스템 기업
  - `entities/tekever.md` — 유럽 AI 기반 자율 시스템 기업, 영국 육군 CORVUS 계약
- Created concepts:
  - `concepts/emlid-corrections.md` — Emlid RTK 보정 서비스
  - `concepts/dji-mic-mini-2s.md` — DJI 무선 마이크 시스템
  - `concepts/cleveland-clinic-drone-delivery.md` — 미국 최초 장기 의료 드론 배달
  - `concepts/us-dod-cuas-marketplace.md` — 미국 국방부 C-UAS 마켓플레이스
- Updated:
  - `concepts/edgetx-custom-audio.md` — 트레이너 모드 추가
  - `entities/terra-drone.md` — Terra Xross 1 실내 검사 드론 정보 추가
- Updated: `index.md` (153 pages), `log.md`
- Moved sources to: `inbox/processed/` (10 files)

## [2026-08-06] lint-fix | 그래프 단절(broken wikilink + orphan) 진단 및 broken link 해소

마스터 지적: Obsidian 그래프에서 관계형 데이터 일부 미연결 확인 → 실측 진단.

- 진단 결과: canonical 171페이지 중 76개 인바운드 링크 0(고아), 13개 링크 타겟이 페이지 자체가 없어 40건 참조가 깨져 있음(SCHEMA 위반). 원인은 도메인 분류 실패가 아니라 (1) 여러 페이지가 `[[drone-hw]]`/`[[drone-sw]]`/`[[drone-ai]]`/`[[ops-mission]]` 등 SCHEMA 태그명을 실제 존재하지 않는 허브 페이지처럼 링크한 것, (2) `[[ai-agent]]`→`drone-ai-agents`, `[[swarm]]`→`swarm-coordination` 슬러그 오기(typo).
- Created (broken link 40건 해소, 신규 허브/개체 13개):
  - `concepts/drone-hw.md`, `concepts/drone-sw.md`, `concepts/drone-ai.md`, `concepts/ops-mission.md` — 도메인 개요 허브
  - `concepts/companion-computer.md`, `concepts/mavros.md`, `concepts/utm-system.md`, `concepts/px4-simulation.md`
  - `entities/dji.md`, `entities/dji-enterprise.md`, `entities/matternet.md`
- Fixed slug typo (3 files): `entities/droneshield.md`, `entities/xtend-ai-robotics.md` (`[[ai-agent]]`→`[[drone-ai-agents]]`), `concepts/lockheed-martin-morfius.md` (`[[swarm]]`→`[[swarm-coordination]]`)
- 잔여 이슈(미해결, 대량 갱신이라 마스터 확인 필요): 인바운드 링크 0인 고아 페이지 76개는 그대로 남음 — 기존 페이지에 역링크 추가는 10개 이상 문서 일괄 갱신에 해당해 SCHEMA 규칙상 사전 승인 필요.
- `mavlink-protocol`(index.md 2회 언급) 등 index.md에는 있으나 실제 파일이 없는 항목 별도 발견 — 이번 세션 범위 밖, 별도 lint 보고 필요.

## [2026-08-06] ingest | drone wiki 스케줄 실행 + inbox 미처리 13건(Hermes 2nd-daily-ingest 402 에러로 미처리) 처리

- 원인: Hermes `2nd-daily-ingest`(04:00) cron이 OpenRouter 크레딧 부족(HTTP 402)으로 실패 → `inbox/fetch-2026-08-06-*.md` 13건 미인제스트 상태로 잔류.
- drone-wiki-web 자가갱신(`scripts/self-update-pipeline.ts`) dry-run 실행: 뉴스↔위키 교차참조 후보 40건 발견. 상당수가 저점수(≤4) 키워드 우연일치(MATLAB 튜토리얼↔SLAM 페이지, Claude Code 강좌↔UAV 탐지기 등 도메인 무관) → `--apply` 보류, 유효 매칭은 아래 수동 반영으로 대체.
- Source files from `inbox/` (13개, 전부 검토):
  - `fetch-2026-08-06-rss-dji-enterprise.md`, `fetch-2026-08-06-rss-dronedj.md`, `fetch-2026-08-06-rss-dronelife.md`, `fetch-2026-08-06-rss-oscarliang-fpv.md`, `fetch-2026-08-06-rss-parrot.md`, `fetch-2026-08-06-rss-skydio.md`, `fetch-2026-08-06-yt-a-water-ring-slowed-all-the-way-down-osmo-action-6.md`, `fetch-2026-08-06-yt-claude-code-full-course-autonomous-goals-mcp-and-vs-code-set.md`, `fetch-2026-08-06-yt-for-the-moments-you-planned-and-the-ones-you-never-saw-comin.md`, `fetch-2026-08-06-yt-how-to-get-an-rtk-fix-in-seconds.md`, `fetch-2026-08-06-yt-inside-ais-hidden-supply-chain.md`, `fetch-2026-08-06-yt-spline-fitting-explained-how-to-smooth-noisy-data-in-matlab.md`, `fetch-2026-08-06-yt-why-did-divimath-release-a-4w-analog-vtx.md`
- Created concepts:
  - `concepts/china-drone-export-controls.md` — 중국 대미 드론·부품 수출 통제
  - `concepts/divimath-4w-analog-vtx.md` — Divimath 4W 아날로그 VTX
- Updated:
  - `entities/skydio.md` — $1.1억 펀딩/$44억 밸류에이션 추가
  - `concepts/emlid-corrections.md` — 3번째 소스(RTK Fix in seconds) 추가
  - `concepts/dji-osmo-action-6.md` — 슬로우모션 데모 소스 추가
- Skipped(사유): DJI Enterprise RSS 4건(구형/일반 펌웨어 소식, 개별 문서화 가치 낮음), FIFA 드론 압수(단발성 이벤트), 프랑스 드론 제조 이전·인적요인 시리즈(단일소스, 임계값 미달), HelloRadio 리뷰(단일 제품 리뷰), Parrot RSS 4건(2018~2024 구기사, 기존 `parrot.md`와 중복), Skydio DFR 기사(기존 `skydio-centralsquare-dfr-integration.md`와 동일 사안 중복), Skydio $3.5B 투자(동일 문서에 이미 반영된 사실과 중복), Minneapolis 항의(기존 `skydio.md` 서술과 동일 사안 연속보도), DJI Osmo Pocket 4P 영상(기존 페이지 대비 신규 정보 없음), Claude Code 강좌·MIT AI 공급망·MATLAB 스플라인(드론 도메인과 무관, out-of-domain)
- Updated: `index.md` (185 pages), `log.md`
- Moved sources to: `inbox/processed/` (13 files)

## [2026-08-06] lint-fix | 고아 페이지(인바운드 0) 76개 전량 역링크 백필

마스터 승인 후 진행(대량 갱신이라 사전 확인 필요했던 항목). 주제별 클러스터로 묶어 기존/신규 허브 문서에 역링크 추가하는 방식으로 처리 — 개별 페이지에 억지 연결을 만들지 않고 실제 주제가 일치하는 허브에서만 링크.

- `entities/mavlink.md` → MAVLink 심화 8건(advanced-mavlink, mavlink-advanced, mavlink-advanced-features, mavlink2-security, mavlink-m-interoperability, mavsdk-release, dronecan-deep, digital-twin-intent-drone-networks)
- `concepts/px4-tuning-control.md` → PX4 튜닝/버전 6건
- `concepts/ros2-drone-integration.md` → ROS2 심화 5건
- `concepts/drone-news-{2026-07-31,2026-08-01,hardware,ops,regulations}.md` → 5개 뉴스 아카이브 상호 교차링크
- `concepts/drone-regulations.md` → 규제 사례 5건
- `concepts/swarm-coordination.md` → 스웜 연구 5건
- `concepts/drone-ai.md` → AI 연구/기업 12건
- `concepts/drone-hw.md` → 제품/부품 15건
- `concepts/ops-mission.md` → 운용 사례 8건
- `concepts/ardupilot-architecture.md` → 제어 연구 4건
- 부수 발견: `param-diff-copter-4-6-0-4-7-0`, `param-diff-px4-1-16-0-1-17-0`, `px4-params-by-version`, `ardupilot-params-by-version` 4개 페이지가 아웃바운드 링크 1개뿐(SCHEMA 최소 2개 위반) — 각각 상위 개념(`ardupilot-architecture`/`px4-tuning-control`) 링크 1개씩 추가해 해소.
- **검증 결과**: 총 184페이지 / 고아(인바운드 0) 0개 / 아웃바운드<2 위반 0개 / 깨진 wikilink 0개 — 전부 0으로 확인.
- `scripts/update-graph.sh` 재실행: drone-knowledge-graph.json 184노드 / 1094엣지(전회 1002 대비 +92), 고립 노드 0.

## [2026-08-07] ingest | inbox 10건 처리 (Hermes 2nd-daily-ingest 연속 2일째 402 에러)

- 원인: 2026-08-07 04:00 `2nd-daily-ingest` cron도 어제와 동일하게 OpenRouter HTTP 402(크레딧 부족)로 실패 — 반복되는 근본 원인이므로 마스터의 크레딧 충전 또는 모델 설정 변경이 필요함을 재차 보고.
- Source files (10개, 전부 검토):
  - `fetch-2026-08-07-crossref-deep-learning-based-collision-avoidance-techniques-in-multi-.md`, `fetch-2026-08-07-rss-dji-enterprise.md`, `fetch-2026-08-07-rss-dronedj.md`, `fetch-2026-08-07-rss-parrot.md`, `fetch-2026-08-07-rss-skydio.md`, `fetch-2026-08-07-rss-suasnews.md`, `fetch-2026-08-07-yt-a-pool-from-above-looks-like-art-dji-mavic-4-pro.md`, `fetch-2026-08-07-yt-is-this-drone-flight-legal.md`, `fetch-2026-08-07-yt-whats-under-the-moss-dji-osmo-nano.md`, `fetch-2026-08-07-yt-피지컬ai-체험-로봇팔자율주행반려로봇.md`
- Created concepts:
  - `concepts/multi-uav-collision-avoidance-survey.md` — Crossref 저널 서베이 논문(다중 UAV 딥러닝 충돌회피)
  - `concepts/dfend-counter-drone-worldcup.md` — 2026 FIFA 월드컵 DFEND 대드론 작전(어제 스킵했던 700대 압수 사건과 연계)
- Updated:
  - `concepts/drone-first-responder-dfr.md` — 호놀룰루 경찰 DFR 2개 관할구 가동
  - `entities/skydio.md` — JTF-SB 국경 임무 드론 운용 추가
  - `concepts/dji-osmo-nano.md` — 방수 침수 촬영 데모 소스 추가
  - `concepts/fcc-drone-regulations.md` — 외국 제조사 미국 시장 진입 절차 가이드 추가
  - `concepts/drone-ai.md`, `concepts/us-dod-cuas-marketplace.md` — 신규 페이지 2건 역링크(고아 방지)
- Skipped(사유): DJI Enterprise RSS 3건(제품 수명주기/일반 발표, 개별 문서화 가치 낮음), Parrot RSS 4건(2023~2025 구기사 재탕, 기존 페이지와 중복), DJI Mavic 4 Pro·"Is This Drone Flight Legal?" 영상(마케팅/컨텐츠 없음), 피지컬AI 체험 영상(로봇팔·자율주행·반려로봇 — 드론 무관 out-of-domain), Skydio Minneapolis 표결·펀딩 목록(기존 `skydio.md` 서술과 중복)
- **검증**: 총 186페이지 / 고아 0 / 아웃바운드<2 위반 0 / 깨진 링크 0
- Updated: `index.md` (186 pages), `log.md`
- Moved sources to: `inbox/processed/` (10 files)

## [2026-08-09] ingest | inbox 23건 처리 (Hermes 2nd-daily-ingest 4일 연속 402 에러)

- 원인: 2026-08-08, 08-09 04:00 `2nd-daily-ingest` cron 모두 OpenRouter HTTP 402(크레딧 부족)로 실패 — 4일 연속(08-06~09) 반복. 근본 조치(크레딧 충전/모델 재설정) 필요.
- 병렬 그래프 무결성 감사(fork, 진단 전용): 08-07 정리 이후 상태 재확인 — 고아 0 / 깨진 링크 0 / SCHEMA 위반 0 / index 유령 항목 0, 전부 유지되고 있음을 확인. 자동 self-update-pipeline의 "📰 최근 관련 소식" 섹션은 순수 텍스트+URL이라 wikilink 그래프에 영향 없음.
- Source files (23개, 2026-08-08 12건 + 2026-08-09 11건, 전부 검토):
  - 08-08: `rss-dronedj`, `rss-dronelife`, `rss-parrot`, `rss-skydio`, `rss-suasnews`, `yolo`, `yt-70-more-video-range...`, `yt-embedded-intelligence...`, `yt-pinklab-pinky-zero`, `yt-the-249-gram-drone-trap-explained`, `yt-the-hardest-screenshot-challenge...`, `yt-the-wilderness-has-a-sound...`
  - 08-09: `ros2`, `rss-dji-enterprise`, `rss-dronelife`, `rss-oscarliang-fpv`, `rss-skydio`, `rss-suasnews`, `yolo`(08-08과 동일 릴리스, 중복), `yt-faroe-islands...`, `yt-inspired-by-the-odyssey...`, `yt-my-rc-kit-picks...`, `yt-the-249-gram-drone-trap`(explained판과 중복 주제)
- Created:
  - `concepts/yolo-v8-4-116.md` — YOLO v8.4.116 릴리스(08-08/09 중복 파일 통합 인용)
  - `entities/ondas.md` — 미 방산 드론 기업(Mistral 전술 LUS, Sentrycs 대드론)
  - `concepts/faa-249-gram-registration-rule.md` — FAA 249g 드론 등록 규정(중복 영상 2건 통합)
  - `comparisons/fc-firmware-comparison.md` — Betaflight vs INAV vs ArduPilot 비교
  - `concepts/dji-mavic-4-pro.md` — DJI Mavic 4 Pro(08-07/09 마케팅 영상 2건 통합)
- Updated:
  - `concepts/dfend-counter-drone-worldcup.md` — D-Fend 공식 확인(EnforceAir, 20+ 기관), Ondas 백링크
  - `concepts/fcc-drone-regulations.md` — FCC DJI 접근차단 검토 + Gorge Drones $289,215 민사제재금 사례
  - `entities/skydio.md` — Blue UAS 인증, SFPD 6개월 라이브스트림 유출, EVERYWHERE 단독근무자 파트너십
  - `concepts/dji-mic-mini-2s.md` — 야외 녹음 데모 소스 추가
  - `concepts/betaflight.md`, `entities/dji.md`, `concepts/drone-regulations.md`, `concepts/us-dod-cuas-marketplace.md`, `concepts/yolo-v8-4-115.md` — 신규 페이지 5건 역링크(고아 방지)
- Skipped(사유): L&T 산업화 전망·ACSL 팬데믹 회고 op-ed·Robinson Unmanned Drone Dominance(단일언급, 임계값 미달), Parrot RSS 3건(2020~2023 구기사, 기존 페이지 중복), Skydio Minneapolis 표결·Spokane 400회 비행·A3 인사이트·$52M 육군계약(구식/중복/일반론), suasnews Tiltan HIL·SYPAQ·KLM Vantrel(단발 기업 홍보성, 임계값 미달), Skydio-CentralSquare DFR 재보도(기존 `skydio-centralsquare-dfr-integration.md`와 동일 사안), Inzpire RPAS 훈련(단일언급), ros2 lyrical patch2 릴리스노트(설치안내뿐 실질 체인지로그 없음), RushFPV VTX·MATLAB 임베디드AI·PinkLab Pinky Zero·DJI Neo2 챌린지·DJI RS5·Painless360 RC픽(마케팅/제휴링크 위주 또는 도메인 무관, 콘텐츠 실질 없음)
- **검증**: 총 191페이지 / 고아 0 / 아웃바운드<2 위반 0 / 깨진 링크 0
- Updated: `index.md` (191 pages), `log.md`
- Moved sources to: `inbox/processed/` (23 files)
