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
