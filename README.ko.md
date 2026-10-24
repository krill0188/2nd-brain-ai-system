# 2nd Brain AI 시스템

[Stage 0-R 후속 검증](docs/STAGE_0R_FOLLOWUP.md)

> **Stage 0-R 최신 정정 (2026-09-14):** 원본은 `~/2nd`, 공개 snapshot은 `drone-wiki-web/data/wiki`입니다. sync는 검증 전용이며, 기존 해시는 기존 bytes 보존에만 사용합니다. GraphRAG는 canonical 전용 `drone-knowledge-graph.json`과 미검증 `discovery-knowledge-graph.json`을 함께 읽습니다. Production은 현재 Python 실행환경이 없는 배포 구성상 keyword fallback이며 live 호출 로그는 UNKNOWN입니다. 예약 self-update는 `--apply`로 canonical을 직접 씁니다. Discovery는 여전히 OpenRouter를 사용하고 kinetic의 레거시 알림은 Hermes를 호출할 수 있습니다. [최신 검증·제한](docs/STAGE_0R_REBASELINE.md).

[English](README.md) | **한국어**

> Markdown과 Git 기반 드론 도메인 지식 관리 시스템 — **launchd + `claude -p` 자동화 + 5종 AI 도구 스택 + AI 연구 루프(인간 승인형)** 탑재.

## 기획 · 의도 · 구조 (한눈에)

### 기획 — 무엇을 만드는가
드론 기술(비행제어·통신·하드웨어·SW·AI·군집·법규) 지식을 **수집 → 컴파일 → 발견 → 인간 결정**으로 쌓고,
검증된 지식만 공개 위키 [DroneWiki](https://github.com/krill0188/drone-wiki-web)로 발행하는 **개인 지식 운영 시스템**이다.
논문·제조사 문서·뉴스·영상·특허·정부 공고를 매일 자동 수집하고, AI가 정리·연결하되 **확정은 증거와 승인 규칙으로만** 한다.

### 의도 — 왜 이렇게 만드는가
1. **증거 우선**: 원문은 `raw/`에 불변 보존, 지식은 출처가 추적되는 Markdown으로만 컴파일한다. 환각을 쌓지 않는다.
2. **원본은 한 곳, 공개는 선별**: 이 저장소가 source of truth이고, 공개 snapshot은 정책·해시 게이트를 통과한 문서만 `drone-wiki-web`으로 나간다.
3. **도구는 교체 가능, 자산은 영속**: Markdown·출처 메타데이터·Git 이력이 자산이고, AI 도구·자동화 엔진은 바꿔 끼울 수 있는 레이어다.
4. **AI는 제안, 사람은 결정**: 일상 컴파일은 자동이지만, AI 연구 루프의 가설·통찰과 미검증 발견 그래프는 사람이 승인해야 canonical이 된다.
5. **구조화된 지식**: 문서 검색을 넘어 온톨로지(클래스 74개, 관계, 추론 규칙)로 부품 호환·임무 요구·분야 간 연쇄를 **계산**할 수 있게 한다.

### 구조 — 4개 지식 계층과 연계 시스템

```text
[수집]  RSS · arXiv 8도메인 · Crossref · KCI · 특허 · FAA/관보 · YouTube 27채널 · 나라장터 · HW 제조사/SW 레지스트리
   ▼  inbox/ ──(daily-ingest, claude -p)──► canonical (concepts · entities · comparisons · queries)
   │                                         ▲  원문 증거 raw/ (불변)
   ▼                                         │
[발견]  discovery graph (AI 추출·미검증)  ──► 사람 검토(/discovery-review) ──► canonical 승격
[연구]  research/ (Planner→Retriever→Hypothesis→Critic→Verifier→Report) ──► 마스터 승인 ──► 개별 클레임 승격
   ▼
[발행]  publication gate(정책·해시) ──► auto-publish(매일 10:30) ──► drone-wiki-web/data/wiki ──► Vercel
```

| 구분 | 위치 | 규모(2026-10-24 실측) |
|---|---|---|
| canonical 개념/개체/비교/질의 | `concepts/` `entities/` `comparisons/` `queries/` | 3,199 / 56 / 4 / 2 (이 중 2,366쪽은 자동 승격된 미검토 문서) |
| 원문 증거 | `raw/` (papers, articles, youtube, transcripts, web …) | 532개 파일 |
| 수집 대기/처리 | `inbox/` | 1,786개 파일 |
| 연구 루프 산출 | `research/` | 73개 파일 |
| 온톨로지 | `ontology/class-hierarchy.json` · `docs/ONTOLOGY_SPEC.md` | 클래스 74개(주제 클래스 10개, NewsDigest·VendorRegistry 포함), 추론 규칙은 drone-wiki-web에서 구동 |
| 자동화 | `scripts/` + launchd `ai.2nd.*` | 스크립트 161개, 로드된 `ai.2nd.*` 잡 10개(1개는 별개 프로젝트) |
| 발행 정책 | `publication/policy.json` | 문서 해시 승인, `ontology/`는 review |

### GitHub 기준 현황
- 저장소: 공개, 2026-07-26 생성. 언어 비중 Python ≈ 415KB · Shell ≈ 180KB · HTML ≈ 31KB (자동화 스크립트 중심 저장소).
- 릴리즈 이력: **v3.2.2**(08-19 학술수집 대확장: arXiv 8도메인+KCI+Zotero) → **v3.3.0**(08-20 팔란티어식 온톨로지 Link+Action) → **v3.4.0**(09-02 hermes cron → Claude Pro 구독 전환) → **v3.5.0**(09-03 로컬 AI 드론빌더) → **v3.6.0**(10-09 auto-publish 안정화, 발행중단 4일치 복구) → **v3.7.0**(10-17 HW 수집 확장, 아래).
- 연계 저장소: [`drone-wiki-web`](https://github.com/krill0188/drone-wiki-web) — 공개 snapshot을 서비스하는 Next.js 앱(AI Q&A·GraphRAG·온톨로지 추론·드론 빌더).

### 최근 업데이트 (v3.8.0, 2026-10-24)
- **discovery 일괄 승격**: 대기 중이던 discovery 개념 1,791건을 **모델 호출 없이**(이름·분류·출처·그래프 이웃만) 한 번에 승격했다. 각 문서에는 `confidence: low`와 `unreviewed` 태그를 달았고, 생성된 분류·출처 허브 11개(`concepts/auto-hub-*.md`)에 연결해 관계를 지어내지 않고도 위키링크 린트 규칙을 충족했다. 마스터가 화면에서 직접 승격한 문서를 합쳐 canonical 문서는 909 → 3,275쪽(임베딩 3,934, canonical 그래프 노드 3,275 · 엣지 14,072)이 됐다.
- **사실 근거 아님**: 이 문서들은 claim이 없다. 사실은 원문 인용이 검증된 claim(`claims.json`, `paper-claims.json`)과 `^[출처]` 문장에서만 나온다. 다음 단계는 LLM이 제안하고 코드가 원문과 글자 단위로 대조해 확인하는 claim 추출이다.
- **온톨로지**: `NewsDigest`·`VendorRegistry` 클래스 추가(부모 `DataArtifact`), 제품·뉴스 문서 52건 분류(`ontology/class-approvals-20261024b.json`, `scripts/revert-class-approvals.py`로 되돌릴 수 있음).
- **파이프라인 보강**: PyYAML이 없으면 `.venv`로 자동 재실행, 문서 추출 일부 실패가 야간 파이프라인 전체를 멈추지 않도록 수정(`PARTIAL_EXTRACTION_CONTINUE`).
- **웹(drone-wiki-web)**: NIM·OpenRouter 키 풀 폴백, 빌더 배선도·단계별 이미지, 4조건 안내 카드, GitHub Actions 클라우드 점검. 해당 저장소 `docs/RELEASES.md` 참고.

### 이전 업데이트 (v3.7.0, 2026-10-17)
- **HW 세분화 수집**: arXiv 5종(모터/ESC·프로펠러·전원·프레임·페이로드) + 온톨로지 클래스 5개(Propeller/Battery/Frame/Datalink/Payload) 추가.
- **HW 자료 61건 컴파일**: 제품 카탈로그 7 · 연구 6 · 사례 4 · 개체 2 신규(제조사 공식 사양 기반).
- **발행 파이프라인**: 새 정규문서 19개 자동 승인·매니페스트 등록, 재기준선 고정(매일 10:30 자동 발행 대기).
- **수집 확장 설계(승인 대기)**: 드론+α 기본구조 16종·이기종 통신/프로토콜/주파수·공학 8개 분야를 위한 신규 도메인 12개 제안, 제조사 레지스트리(15개 카테고리)·SW 레지스트리(12개 카테고리) 수집은 `~/projectm/hw-collection`에 보관 중(위키 미반영, 승인 후 이관).

### 한계
- 일부 서브시스템은 구독 전용이 아니다(discovery 추출은 OpenRouter, kinetic 알림은 레거시 Hermes 경로). 상세는 위 Stage 0-R 정정 참고.
- 공개 snapshot의 production 검색은 현재 keyword fallback이 기대 동작이다(live 호출 로그는 UNKNOWN).
- 신규 수집 레지스트리의 라이선스·연동 칸은 표본 검증 전이며, 접근 차단 사이트(ROS 공식 문서 등)는 비어 있다.

---

## 프로젝트 개요

이 프로젝트는 **드론 기술** (8개 주제 영역: drone / datalink / swarm / voice-control / drone-hw / drone-sw / drone-ai / ai-agent) 에 특화된 개인 지식 관리 시스템입니다. Obsidian, VS Code, GitHub 등 어떤 Markdown 도구와도 호환되는 일반 Markdown 파일을 사용해 **캡처 → 컴파일 → 발견 → 인간 결정**의 지속적 워크플로우를 구현합니다.

[ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template) 기반으로 커스텀 AI 도구 레이어, launchd + `claude -p` 자동화, AI 연구 루프(`research/`)를 추가 구성한 시스템입니다.

### 아키텍처

시스템은 4개 지식 계층으로 구성됩니다: **증거 → 정식 메모리 → 발견 → 인간 결정**. 원본 소스 자료는 `raw/`에 불변 증거로 보존되며, 재사용 가능한 지식은 추적 가능한 출처와 함께 정식 Markdown으로 컴파일됩니다.

**자동화 제어 플레인** (macOS `launchd`, 라벨 접두사 `ai.2nd.*`, Claude Pro/Max 구독으로 `claude -p` 직접 호출)이 예약된 수집·컴파일·린트를 자동 처리합니다 — 전체 체인은 아래 "자동화 제어 플레인" 참고. **일상적인 daily-ingest 컴파일에는 사전 승인 절차가 없습니다** — llm-wiki 스킬이 조건을 만족하면 즉시 canonical 페이지를 생성하고, `log.md`에 기록하며, 매일 아침 텔레그램 리포트로 신규 생성 목록을 마스터에게 사후 통지합니다(가시성 확보 목적, 확정을 막는 게이트는 아님). **인간 승인이 실제로 확정을 가로막는 지점은 `research/` AI 연구 루프뿐입니다** — AI가 생성한 가설·통찰은 마스터가 `research-run.sh approve`로 명시 승인하고, `research-promote.py`로 개별 클레임을 지정해야만 canonical로 반영됩니다(§ AI 연구 루프 참조).

![마스터 2nd Brain AI 시스템 아키텍처](docs/architecture/master-ai-architecture.png)

### 운영 워크플로우

두 개의 별도 경로가 있습니다.

1. **일상 컴파일 경로(사전 승인 없음)**: 캡처 → `ai.2nd.daily-fetch`(launchd, `fetch-inbox.sh`) → `ai.2nd.daily-ingest`(`claude -p`) 자동 컴파일 → `log.md` 기록 → 매일 11:30 텔레그램 사후 통지(신규 페이지 목록, `ai.2nd.morning-report`). 주기적으로 `scripts/gate-c-analyze.sh`(그래프 구조 공백 분석)가 별도 실행됩니다.
2. **AI 연구 루프(사전 승인 있음)**: 연구 목표 입력 → Planner→Retriever→Hypothesis→Critic→Verifier→Report(5단계 LLM) → 마스터 승인(`approve`/`reject`) → 개별 클레임 선택 승격(`research-promote.py`). 이 경로만 승인 전 canonical 반영을 실제로 차단합니다.

![마스터 2nd Brain 운영 워크플로우](docs/workflow/master-workflow.png)

### 기술 스택

스택은 launchd + `claude -p` 자동화와 각각 고유한 역할을 가진 5종 AI 도구를 결합합니다. 오픈 형식 Markdown, 출처 메타데이터, Git 히스토리가 내구성 있는 자산이며 AI 도구와 자동화 엔진은 교체 가능한 레이어입니다.

![마스터 2nd Brain 기술 스택](docs/tech-stack/master-tech-stack.png)

---

## 자동화 제어 플레인 — launchd + `claude -p`

> 실제 스케줄러는 native launchd입니다. Ingest와 주간 Claude jobs는 `claude -p`를 쓰지만,
> discovery 추출은 OpenRouter와 선택적 Neo4j를 사용합니다. 레거시 Hermes 경로가 남아 있고
> kinetic 알림은 Hermes를 호출할 수 있습니다. `hermes-wrap.sh`는 기존 notify 스크립트로 알림을 전달합니다.

아래는 독립 jobs의 예약 시각이며, 앞 단계의 성공·완료를 보장하는 순차 체인이 아닙니다.

| 순서 | launchd 라벨 | 시각 | 스크립트 | 역할 |
| --- | --- | --- | --- | --- |
| 1 | `ai.2nd.daily-fetch` | 07:30 | `hermes-wrap.sh` → `scripts/fetch-inbox.sh` | 8개+ 소스(RSS, arXiv 8도메인, Crossref, KCI, USPTO, 미 연방관보/FAA, YouTube 27채널, 나라장터) 수집 → `inbox/` |
| 2 | `ai.2nd.daily-ingest` | 08:00 | `scripts/daily-ingest-claude.sh`(`claude -p`) | `summarize-note`/`publish-entry` 스킬로 `inbox/`를 canonical `concepts/`/`entities/`/`comparisons/`/`queries/`로 컴파일, 처리 완료 파일은 `inbox/processed/`로 이동 |
| 3 | `ai.2nd.lint-knowledge` | 08:12 | `scripts/lint-knowledge.py --recent-hours 2 --quiet` | 직전 실행에서 수집된 것에 대한 스키마 게이트 — canonical 9필드 계약 강제 |
| 4 | `ai.2nd.dronewiki-self-update` | 08:20 | `.hermes/scripts/dronewiki-self-update.sh --apply` | 기존 자동 실행이 canonical 뉴스 섹션을 직접 수정. 제안 전용 아님. 완료 의존성은 미해결. |
| 5 | `ai.2nd.sync-dronewiki` | 08:30 | compatibility wrapper → repository `sync-wiki.sh` → `publication-preflight.py` | Stage 0-R 검증 전용: lint·kinetic·임베딩 최신성·발행 정책 검사. snapshot 변경/push/배포 없음 |
| 6 | `ai.2nd.extract-knowledge-graph` | 08:45 | `scripts/extract-knowledge-graph.sh --limit 15` | raw 원문에서 미검증 discovery 그래프 추출(canonical 그래프와 절대 섞이지 않음) |
| 7 | `ai.2nd.update-knowledge-graph` | 08:47 | `scripts/update-graph.sh` | canonical 4개 디렉터리로부터 그래프 갱신(레거시 잔존 노드 가능) |
| 8 | `ai.2nd.apply-kinetic-rules` | 08:50 | `scripts/apply-kinetic-rules.py` | 구현된 SWRL 규칙 2개 실행(규칙4: SLM/LLM 판별, 규칙6: 미승인 가설 감사) |
| 9 | `ai.2nd.morning-report` | 11:30 | `scripts/morning-report-send.sh` | 기존 아침 리포트 발송. 새 발행 파이프라인의 성공 증명은 아님 |

주간(일일 체인과 독립):

| launchd 라벨 | 시각 | 스크립트 | 역할 |
| --- | --- | --- | --- |
| `ai.2nd.weekly-lint` | 월 05:00 | `scripts/weekly-lint-claude.sh`(`claude -p`) | 고아 페이지, 끊긴 wikilink, SHA-256 드리프트 |
| `ai.2nd.weekly-summary` | 월 05:30 | `scripts/weekly-summary-claude.sh`(`claude -p`) | 주간 지식 다이제스트 텔레그램 발송 |

같은 `ai.2nd.*` launchd 네임스페이스에 스케줄되어 있지만 **완전히 별개인 프로젝트**도 하나
있습니다: `ai.2nd.medic-wiki-fetch`는 `~/medic-wiki/scripts/fetch-inbox.sh`(자체 Supabase
백엔드, 이 저장소 콘텐츠와 무관)를 실행합니다. 스케줄러만 공유할 뿐 데이터는 공유하지
않습니다.

### 스케줄 확인/변경

```bash
launchctl list | grep ai.2nd                              # 로드됐는지, 마지막 종료코드는?
plutil -p ~/Library/LaunchAgents/ai.2nd.daily-ingest.plist # 특정 잡의 스케줄/경로 확인
# plist 수정 후:
launchctl unload ~/Library/LaunchAgents/ai.2nd.<name>.plist
launchctl load   ~/Library/LaunchAgents/ai.2nd.<name>.plist
```

모든 일일 잡은 **의도적으로 한국시간 오전 7시 이후**로 잡혀 있습니다 — Claude 구독의 주간
사용한도가 리셋되는 시각이기 때문입니다. 예전엔 03:30~04:50 사이에 돌다가 리셋 직전까지
"사용한도 초과"로 종종 실패했습니다(사고 기록: `docs/incident-reports/2026-09-11-briefing-outage/`).
다음에 다시 시각을 옮길 일이 있으면, 하나만 따로 옮기지 말고 체인 전체의 **상대 간격**을
그대로 유지하세요(fetch → +30분 ingest → +12분 lint → ...) — 두 잡이 같은 시각에 겹치는 건
에러 로그도 안 남는 조용한 실패 유형입니다.

### 텔레그램 — 승인 게이트 아님, 통지·조회 채널

```
[입력]      마스터 → 텔레그램 → (수동 캡처, "빠른 시작" 참고) → inbox/
[사후 통지] ai.2nd.morning-report(11:30) → 텔레그램: 오늘 신규 canonical 페이지 + 드론 뉴스 다이제스트
[쿼리]      마스터 → 텔레그램(dronewikibot) → wiki 검색 → 답변
```

> 텔레그램은 **확정을 가로막는 승인 게이트가 아니라 사후 통지·조회 채널**입니다.
> daily-ingest는 텔레그램 응답을 기다리지 않고 즉시 `index.md`/`log.md`를 갱신합니다.
> 실제로 승인이 확정을 가로막는 지점은 아래 "AI 연구 루프"의 `research-run.sh approve`/
> `research-promote.py`(CLI 기반, 텔레그램 아님), 그리고 drone-wiki-web의 `/self-update-review`·
> `/discovery-review` 페이지(인간 승인 게이트, 로컬 전용)뿐입니다.

---

## AI 도구 역할

이 시스템에는 6종 도구가 구성되어 있으며, 각각의 책임은 [AGENTS.md](AGENTS.md)에 정의되어 있습니다.

| 도구 | 인터페이스 | 주요 역할 |
| --- | --- | --- |
| **launchd + `claude -p`** | macOS 스케줄러 / CLI | 자동 수집·컴파일·린트(사전 승인 없이 즉시 확정), 완료 후 텔레그램 통지 |
| **OpenCode + Kimi K2** | 터미널 (`opencode`) | 수동 컴파일 지원, 문서 초안 작성, 대량 편집 |
| **Claude Code** | 터미널 (`claude`) | 아키텍처 분석, 모순 검토, AI 연구 루프(Planner~Report) 실행 |
| **Codex** | 터미널 (`codex`) | 드론 펌웨어 탐색 (PX4/ArduPilot/ROS2), 코드→raw 파이프라인 |
| **GitHub Copilot Chat** | VS Code 사이드바 (`@workspace`) | 교차 검증, 대안 관점, 워크스페이스 파일 직접 읽어 요약·질의응답 |
| **GitHub Copilot 인라인** | VS Code 인라인 | Markdown 또는 코드 작성 중 자동완성 |
| **Understand Anything** | `scripts/gate-c-analyze.sh` / Claude Code | Gate C — 지식그래프 생성, 공백 분석, 구조적 관측 |

> **비용 원칙**: 일일/주간 자동화는 이미 Claude Pro/Max 구독(`claude -p`)으로 도는 만큼 호출당 별도 비용 관리가 필요 없습니다. 임시 대량 수동 컴파일은 Kimi K2로 라우팅. 대화형 Claude 세션은 아키텍처 결정과 모순 해소에 예약. GitHub Copilot(인라인 + Chat)은 무료 — 편집 중 및 교차 검증에 자유롭게 사용.

---

## 드론 도메인 커버리지

주요 지식 도메인은 8개 등록 태그 카테고리에 걸친 **드론 기술**입니다 ([SCHEMA.md](SCHEMA.md) 및 [docs/domain/drone-domain-guide.md](docs/domain/drone-domain-guide.md) 참조).

| 태그 | 범위 |
| --- | --- |
| `drone` | 일반 시스템 — 기체, 비행 역학, 규제, 임무 계획 |
| `datalink` | RF, LTE, MAVLink 텔레메트리, C2 링크, 암호화 |
| `swarm` | 멀티드론 조정, 편대 비행, 합의 알고리즘 |
| `voice-control` | 드론 운용을 위한 자연어/음성 명령 인터페이스 |
| `drone-hw` | 하드웨어 — FC, ESC, 모터, 배터리, LiDAR, 카메라, 페이로드 |
| `drone-sw` | PX4, ArduPilot, GCS, MAVSDK, ROS/ROS2, MAVROS/MAVROS2, uORB |
| `drone-ai` | 컴퓨터 비전, 자율 비행, SLAM, 객체 감지, 세그멘테이션 |
| `ai-agent` | AI 에이전트 아키텍처, 자율 의사결정, 멀티에이전트 시스템 |

수집 우선순위: `drone-sw` → `datalink` → `drone-ai` → `swarm` → 기타.

---

## 주요 기능

| 기능 | 설명 |
| --- | --- |
| **자동화 수집 파이프라인** | `ai.2nd.daily-fetch`(launchd, 07:30)가 `inbox/`를 채우고, `ai.2nd.daily-ingest`(08:00, `claude -p`)가 canonical 페이지를 **사전 승인 없이 즉시** 컴파일·확정합니다. 매일 11:30 아침 리포트가 그날 생성분을 텔레그램으로 사후 통지합니다. |
| **AI 연구 루프 — 실제 인간 승인 게이트** | `research/` 경로에서만 승인이 확정을 가로막습니다: 연구 세션(Planner~Report)이 draft를 만들면 `research-run.sh approve`로 마스터가 명시 승인해야 하고, `research-promote.py --items`로 클레임을 개별 지정해야 canonical에 반영됩니다. `fact` 클레임(기존 출처 재진술)은 승격 자체가 거부됩니다. |
| **소스와 출처 보존** | Zotero와 Obsidian Web Clipper로 논문과 웹 자료를 캡처한 후 소스, 메타데이터, SHA-256 다이제스트를 `raw/` 아래에 보존해 모든 주장을 증거까지 추적할 수 있습니다. |
| **검증된 지식 컴파일** | `ai.2nd.daily-ingest`(`claude -p`)와 OpenCode + Kimi K2가 소스 자료를 출처, 신뢰도 평가, 모순 추적을 포함한 엔티티, 개념, 비교, 쿼리 문서로 구조화합니다. |
| **연결된 Markdown 편집** | Obsidian에서 wikilinks와 역방향 링크를 사용해 지속적 지식을 읽고 편집하며, GitHub Copilot 인라인이 편집 중 자동완성을 지원합니다. |
| **멀티 AI 교차 검증** | Claude Code와 GitHub Copilot Chat(`@workspace`)이 동일 증거에 대해 독립적 분석을 제공할 수 있습니다 — 다만 이는 daily-ingest 자동 컴파일 전에 강제로 실행되는 게이트가 아니라, 필요 시 사람이 선택적으로 사용하는 수동 검증 도구입니다. |
| **드론 코드 탐색** | Codex가 PX4, ArduPilot, ROS2/MAVROS2, MAVSDK 소스 코드를 탐색하며, 결과는 `inbox/`에 저장되어 `ai.2nd.daily-ingest`가 컴파일 시 수집합니다. |
| **지식그래프 (Gate C)** | Understand Anything `understand-knowledge` 스킬이 위키를 분석해 인터랙티브 지식그래프(`.ua/knowledge-graph.json`)를 생성 — 클러스터, 공백, 구조적 약한 연결을 자동으로 표면화합니다. 로컬 뷰어는 `open .ua/graph.html`로 실행 (지식 도메인 노드 전용·포스-다이렉티드·오프라인 동작). |
| **Gate C v2 — AI 공백 분석** | `scripts/gate-c-analyze.sh`가 지식그래프를 읽어 구조 통계(레이어 밀도·고립 노드·과부하 허브·단절 레이어 쌍)를 전처리한 후 `claude -p`로 AI 해석을 수행합니다. 결과는 `.ua/gap-report.md`에 저장되며 텔레그램 형식으로 출력됩니다. `--deliver` 옵션으로 `scripts/hermes-wrap.sh`(게이트웨이 없이 텔레그램 Bot API 직접 호출)를 통해 즉시 전송 가능합니다. |

---

## 사전 준비 사항

### 캡처 도구

| 분류 | 도구 | 목적 |
| --- | --- | --- |
| 필수 | [Obsidian](https://obsidian.md/download) | 이 저장소를 로컬 볼트로 열어 Markdown을 탐색하고 편집합니다. |
| 논문 캡처 | [Zotero + Zotero Connector](https://www.zotero.org/download/) | Connector로 브라우저에서 스크랩 → Zotero 라이브러리 → `python3 scripts/zotero-ingest.py` → `raw/papers/<topic>/` Markdown 레코드 + `raw/papers/files/<topic>/` PDF 원문 사본 자동 생성(`attachment_path`/`attachment_sha256` frontmatter 페어링). PDF는 git 미추적(로컬 전용, Zotero가 원본 보관). Zotero Settings → Advanced → "Allow other applications" 활성화 필수. 이미 인제스트된 레코드에 첨부만 소급 반영하려면 `--backfill-attachments`. |
| 웹 캡처 | [Obsidian Web Clipper](https://obsidian.md/clipper) | 웹 페이지를 `raw/web/` Markdown 파일로 변환합니다. |

### 자동화 및 메시징

| 도구 | 목적 | 설정 |
| --- | --- | --- |
| macOS `launchd` | 자동화 제어 플레인 — 모든 `ai.2nd.*` 예약 잡(위 "자동화 제어 플레인" 참고) | plist는 `~/Library/LaunchAgents/ai.2nd.*.plist`에 있음; 각각 `launchctl load` |
| Claude Pro/Max 구독 | 자동화 체인의 모든 `claude -p` 호출이 여기로 감, API 키 아님 | `claude` — 브라우저로 한 번 로그인; `ANTHROPIC_API_KEY` 불필요·미사용 |
| 텔레그램 봇 | 캡처 명령 수신 + 사후 통지·조회 채널(승인 게이트 아님) | [@BotFather](https://t.me/BotFather)로 생성, 토큰을 `claudeclaw/.env`에 `DRONEWIKI_BOT_TOKEN`/`ALLOWED_CHAT_ID`로 설정(`notify.sh`/`notify-dronewiki.sh`가 읽음) |

### AI 도구

| 도구 | 인증 방법 | 설정 |
| --- | --- | --- |
| [OpenCode](https://opencode.ai) + Kimi K2 | OpenRouter API 키 | 터미널에서 `opencode providers login openrouter` |
| [Claude Code](https://claude.ai/code) | Claude Max 구독 | `claude` — 첫 실행 시 브라우저로 로그인 |
| [Codex](https://github.com/openai/codex) | ChatGPT Plus 구독 | `codex` — 첫 실행 시 브라우저로 로그인 |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub 계정 (기본 제공) | VS Code 1.130+에 내장됨; GitHub로 로그인. 인라인 자동완성 + Chat(`@workspace`) 교차 검증 모두 제공 |

### 권장 설정 순서

1. 이 저장소를 클론하고 Obsidian에서 볼트로 열기.
2. Zotero, Zotero Connector(Chrome), Obsidian Web Clipper 설치. Zotero 로컬 API 활성화: Settings → Advanced → "Allow other applications on this computer to communicate with Zotero". zotero-mcp 설치: `pipx install zotero-mcp-server`.
3. npm으로 OpenCode, Claude Code CLI, Codex CLI 설치.
4. VS Code에서 GitHub Copilot 로그인(v1.130+ 내장); Copilot Chat(`@workspace`)으로 교차 검증 사용.
5. 자동화 plist 로드: `for p in ~/Library/LaunchAgents/ai.2nd.*.plist; do launchctl load "$p"; done`
6. 텔레그램 발송용으로 `claudeclaw/.env`에 `DRONEWIKI_BOT_TOKEN`, `ALLOWED_CHAT_ID` 설정.
7. `launchctl list | grep ai.2nd`로 확인 — 모든 잡의 마지막 종료코드가 `0`이면 정상(PID가 `-`인 건 예약 실행 사이 대기 상태라 정상).

---

## 디렉토리 구조

```text
.
├── inbox/                    # 임시 수집함 — ai.2nd.daily-fetch(07:30)가 채우고 ai.2nd.daily-ingest(08:00)가 비움
├── raw/                      # 불변 소스 증거
│   ├── articles/             # 아티클 및 웹 클리핑 소스 텍스트
│   ├── notebooklm/           # NotebookLM 소스 레코드
│   ├── papers/files/         # 논문 첨부파일 (플레이스홀더 전용)
│   ├── transcripts/          # 오디오, 비디오, 미팅 트랜스크립트
│   ├── web/                  # 웹 캡처 (임포터 보존 경로)
│   ├── youtube/              # YouTube 메타데이터 및 트랜스크립트
│   └── assets/               # 소스 레코드가 참조하는 이미지
├── entities/                 # 정식 지식 — 사람, 조직, 도구
├── concepts/                 # 정식 지식 — 개념, 원칙
├── comparisons/              # 정식 병렬 분석
├── queries/                  # 소스 기반 질문과 답변
├── docs/
│   ├── architecture/         # 시스템 아키텍처 다이어그램 및 사양
│   ├── domain/               # 드론 도메인 수집 가이드
│   ├── tech-stack/           # 기술 스택 다이어그램
│   └── workflow/             # 운영 워크플로우 다이어그램
├── templates/                # 프론트매터 템플릿 (raw-article / entity / concept / comparison / query)
├── _archive/                 # 대체된 정식 페이지
├── AGENTS.md                 # AI 도구 역할 정의 및 도메인 포커스
├── CLAUDE.md                 # Claude Code 전용 지침
├── SCHEMA.md                 # 권위 있는 데이터 계약
├── index.md                  # 활성 정식 지식 카탈로그
└── log.md                    # 추가 전용 운영 이력
```

---

## 빠른 시작

### 1. 저장소 클론

```bash
git clone https://github.com/krill0188/2nd-brain-ai-system.git
cd 2nd-brain-ai-system
```

### 2. 에디터에서 열기

- **Obsidian**: `폴더를 볼트로 열기` → 저장소 디렉토리 선택.
- **VS Code**: `code .` 또는 `code ~/2nd` (~/2nd에 클론한 경우).

### 3. 지식 세션 시작

```bash
# 자동화 파이프라인 — launchd가 일일 수집 처리("자동화 제어 플레인" 참고)
launchctl list | grep ai.2nd

# 수동 컴파일 지원 — Kimi K2
cd ~/2nd && opencode

# 아키텍처 / 모순 분석 — Claude
cd ~/2nd && claude

# 드론 코드 탐색 — Codex (결과는 inbox/로)
cd ~/2nd && codex
```

### 4. 텔레그램으로 캡처 명령 전송

```
[텔레그램 → @dronewikibot]
"이 링크를 수집해서 inbox/에 저장해줘: https://docs.px4.io/..."
```

캡처된 콘텐츠는 `inbox/`에 저장되고, 다음 `ai.2nd.daily-ingest` 실행(08:00)에서 컴파일됩니다.

### 5. 지식그래프 뷰어 열기

```bash
# Gate C 인터랙티브 뷰어 실행 (오프라인, 독립 실행형)
open .ua/graph.html
```

Concepts / Comparisons / Queries / Entities 등 정식 지식 도메인 노드만 포스-다이렉티드 레이아웃으로 시각화합니다 (docs·templates 제외). 노드 클릭 시 요약·파일 경로·연결 목록을 확인할 수 있으며, 도메인 필터와 이름 검색을 지원합니다.

### 6. 운영 계약 읽기

지식을 추가하기 전에 [SCHEMA.md](SCHEMA.md)를 읽고, [index.md](index.md)에서 이미 다루어진 주제를 확인하고, [log.md](log.md)의 최신 항목을 검토하세요.

---

## 기본 워크플로우

1. **캡처**: 텔레그램에 링크를 전송하거나 Obsidian Web Clipper로 웹 페이지를 `raw/web/`에 저장. 논문은 Zotero Connector → Zotero 라이브러리 → `python3 scripts/zotero-ingest.py` → `raw/papers/<topic>/`.
2. **자동 컴파일(사전 승인 없음)**: `ai.2nd.daily-ingest`(launchd, 매일 08:00, `claude -p`)이 `inbox/`를 스캔하고, canonical 페이지를 **즉시 생성·확정**한다. 대기 상태 없이 바로 `index.md`/`log.md`에 반영됨.
3. **사후 통지**: 매일 07:30 `morning-report.sh`가 그날 자동 생성된 페이지 목록을 텔레그램으로 통지(승인 요청 아님 — 이미 확정된 것을 알리는 것).
4. **(선택) 교차 검증**: 필요하다고 판단되면 GitHub Copilot Chat(`@workspace`) 또는 Claude에게 이미 생성된 페이지를 검토해 모순이나 누락을 찾도록 사람이 직접 요청 — 자동 실행 아님.
5. **AI 연구 루프(실제 승인 게이트)**: 더 깊은 탐구가 필요한 질문은 `scripts/research-run.sh new "<질문>"`으로 연구 세션을 만든다. Planner→Retriever→Hypothesis→Critic→Verifier→Report를 거쳐 draft가 나오면, `research-run.sh approve <id>`로 마스터가 승인하고 `research-promote.py <id> --items C1,C3`로 클레임을 개별 지정해야만 canonical에 반영된다 — **이 경로만 승인 전 확정을 실제로 차단한다.**
6. **쿼리**: 텔레그램 봇에 직접 질문 — `"PX4 비행 모드에 대해 무엇을 수집했나요?"` — dronewikibot이 wiki를 검색해 답변.
7. **아카이브**: 완전히 대체된 페이지를 `_archive/`로 이동, 링크 수정, 운영을 `log.md`에 기록.

---

## 데이터 관리 원칙

> [!IMPORTANT]
> `README.ko.md`는 사용 가이드입니다; [SCHEMA.md](SCHEMA.md)가 권위 있는 데이터 계약입니다. 둘이 다르게 보일 때는 `SCHEMA.md`를 따르세요.

- **소스 본문은 불변입니다.** 초기 캡처 후 `raw/` 콘텐츠를 수정하지 않습니다.
- **소스 경로는 존재해야 합니다.** 정식 `sources`는 등록된 `raw/` 디렉토리 아래의 실제 Markdown 파일만 포함할 수 있습니다.
- **정식 지식은 선택적입니다.** 주제가 하나의 소스에서 핵심이거나 최소 두 소스에 걸쳐 반복될 때만 승격합니다.
- **정식 지식은 연결되어 있습니다.** 모든 활성 정식 페이지는 `[[wikilinks]]`를 통해 최소 두 개의 다른 활성 정식 페이지와 링크되어야 합니다.
- **변경은 원자적입니다.** 정식 생성/업데이트/아카이브는 `index.md` 업데이트와 `log.md` 추가가 함께 완료되어야 완성입니다.
- **Git에 비밀정보 없음.** API 키, 봇 토큰, 로그인 세션을 이 저장소에 커밋하지 않습니다. `~/.hermes/.env`는 로컬 전용으로 유지합니다.

---

## 동기화

```bash
git add .
git commit -m "feat: add drone-sw canonical pages (PX4 architecture)"
git push
```

히스토리를 위해 Git을 사용합니다. API 키, 토큰, 로그인 세션은 절대 저장소에 저장하지 않습니다.

---

## 라이선스

[ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template) 기반. launchd + `claude -p` 자동화 및 인간 승인형 AI 연구 루프(`research/`)를 포함한 드론 도메인 AI 지식 관리를 위해 조정 및 확장됨.
