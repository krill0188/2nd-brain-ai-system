> **역사적 감사 기록:** 아래 내용은 Stage 0-R 수정 전 기준이다. 현재 sync는 audit-only이며, 예약 self-update는 canonical을 직접 쓴다. GraphRAG는 canonical+discovery를 함께 사용한다. 최신 확인·잔여 blocker는 [Stage 0-R](STAGE_0R_REBASELINE.md)을 따른다.

# 2026-09-13 아키텍처 감사 — README vs 실제 시스템

> 마스터 지시: "GitHub 문서와 실제 시스템/아키텍처/구조가 다르다, 수집·동기화 작동원리 등 레이어별 역할이 정확히 기재 안 되어있다" — 실제 launchd/스크립트 기준으로 전수 대조.
> **이 문서는 감사 결과만 담는다. 코드/README는 아직 수정하지 않았다.**

## 요약 (3줄)

1. **README.md/README.ko.md 전체가 2026-09-02 이전의 Hermes cron 체계를 기술하고 있다** — 실제로는 launchd(`ai.2nd.*`) + `claude -p` 방식으로 완전히 교체됐는데(daily-ingest/weekly-lint/weekly-summary), README는 여전히 `hermes cron create`, cron ID `b1a360fce35d` 등 존재하지 않는 것을 "✅ Active"라고 적어놓았다.
2. **같은 날(9/13) 오전에 작성된 `00_CURRENT_SYSTEM.md`("VERIFIED BASELINE") 자체도 실제 운영 스크립트를 놓쳤다** — sync 스크립트를 `scripts/sync-wiki.sh`로 감사했는데, 그 파일은 **이미 존재하지 않는다**. 실제로 launchd가 호출하는 파일은 `~/.hermes/scripts/dronewiki-sync.sh`다. 이 오독 때문에 그 문서는 "raw/ 동기화 주체 불명 — P0 조사 필요"라고 잘못 결론 냈다(§1 참고, 실제로는 명시적으로 동기화됨).
3. **launchd 자동화 레이어(12개 잡) 자체가 README와 00_CURRENT_SYSTEM.md 둘 다에 아예 등장하지 않는다** — 스케줄, 의존순서, 재시도 정책이 코드(plist)에만 있고 어떤 문서에도 정리돼 있지 않다. medic-wiki-fetch도 `~/2nd`의 launchd 네임스페이스에 얹혀있는데 두 README 어디에도 언급이 없다.

---

## 1. 동기화(sync) 레이어 — 문서 오독 정정

| 항목 | `00_CURRENT_SYSTEM.md` §14가 감사한 것 | 실제 |
|---|---|---|
| 실행 파일 | `scripts/sync-wiki.sh` | **`~/.hermes/scripts/dronewiki-sync.sh`**(존재 확인, 125줄) — `scripts/sync-wiki.sh`는 현재 저장소에 **없음**(삭제/이동됨) |
| launchd 트리거 | (언급 없음) | `ai.2nd.sync-dronewiki.plist` → `hermes-wrap.sh 2nd-sync-dronewiki "bash ~/.hermes/scripts/dronewiki-sync.sh"` |
| raw/ 동기화 | "동기화 주체 불명, P0 조사 필요"(§14.2) | **명시적으로 처리됨** — `dronewiki-sync.sh` 32~48행, `rsync -a --delete`로 `raw/` → `data/wiki/raw` 동기화(2026-09-04 추가, career-quiz/papers-files 제외). 오늘 17:48 실행 로그에도 "raw: 207개 동기화"로 실측 확인됨 |
| 정확한 매핑 | concepts/entities/comparisons/queries/ontology + news-feed.json + daily-briefing.json + 그래프 3종 | 위 항목 + **raw/**, **embeddings(465개 문서 벡터)** 누락돼 있었음 |
| 배포 확인 | "2026-09-13 스케줄 성공 여부는 런타임/크론으로 별도 검증 필요"(§15) | 오늘 세션에서 실측 완료 — git 커밋 `67328a9`, "Vercel 프로덕션 배포 성공 (584docs)" 로그 확인됨 |

**결론**: `scripts/sync-wiki.sh`는 문서에서도 코드에서도 완전히 제거하고, 앞으로 모든 문서는 `~/.hermes/scripts/dronewiki-sync.sh`를 유일한 sync 스크립트로 기술해야 한다.

---

## 2. 레이어별 표 — 실제 동작 vs 문서 기재 내용

| 레이어 | 실제 동작 | README/README.ko 기재 | 00_CURRENT_SYSTEM.md 기재 | 차이/누락 |
|---|---|---|---|---|
| **수집(fetch)** | `~/2nd/scripts/fetch-inbox.sh`(1023줄) — RSS(6+소스)/arXiv(8도메인, 오늘 sleep 3 추가)/Crossref/KCI/USPTO/Federal Register(FAA)/YouTube(27채널)/나라장터, `ai.2nd.daily-fetch` 07:30(오늘 재조정) 트리거 | Hermes cron `0 4 * * *`로 "inbox/ 스캔"이라고만 기재, 실제 8도메인 arXiv나 KCI/USPTO 등 소스 목록 전혀 없음 | §4.3에서 "runtime schedule not independently executed during audit"라 인정, 소스 목록 없음 | 소스별 목록·실패 처리 방식(429/타임아웃 시 stderr 경고 후 계속 진행) 어디에도 없음 |
| **가공/적재(ingest)** | `daily-ingest-claude.sh` → `claude -p`가 `.claude/skills/{summarize-note,publish-entry}` 절차로 canonical 작성, `ai.2nd.daily-ingest` 08:00(오늘 재조정) | Hermes+llm-wiki 스킬(`b1a360fce35d`)이라고 기재 — **완전히 다른(퇴역한) 메커니즘** | §4.3 "IMPLEMENTED at repository design level"만 언급, claude -p 전환 사실 자체가 없음 | 2026-09-02 claude -p 전환이 두 문서 어디에도 반영 안 됨(daily-ingest-claude.sh 자체 주석엔 정확히 적혀있음) |
| **거버넌스(lint/graph/kinetic)** | `lint-knowledge.py`(ai.2nd.lint-knowledge), `extract-knowledge-graph.py`+`update-graph.sh`(ai.2nd.extract/update-knowledge-graph), `apply-kinetic-rules.py`(ai.2nd.apply-kinetic-rules, SWRL 규칙4·6) | 미기재 | §6~7에서 그래프/온톨로지 구조는 상세히 기술(정확함) — 단 **어느 launchd 잡이 언제 이 스크립트들을 돌리는지는 없음** | 스크립트 존재/역할은 문서화됐지만 "언제 자동으로 도는지"가 빠짐 |
| **동기화(sync)** | 위 §1 참고 | 미기재(README는 Hermes 체계라 sync 언급 자체가 없음) | §14, 단 스크립트 경로 오류 | 위에서 정정 |
| **medic-wiki-fetch** | `ai.2nd.medic-wiki-fetch` → `~/medic-wiki/scripts/fetch-inbox.sh` 호출(완전히 별도 프로젝트, 별도 Supabase 백엔드) | **언급 전혀 없음** | **언급 전혀 없음** | 2nd Brain의 launchd 네임스페이스에 다른 프로젝트 잡이 얹혀있다는 사실 자체가 어디에도 없음 — 최소 한 줄이라도 "medic-wiki는 별도 프로젝트지만 스케줄러를 2nd Brain 것과 공유한다"는 설명 필요 |
| **hermes-wrap.sh** | 2026-09-04 신설, "Hermes Gateway 완전 대체 래퍼"(자체 주석) — gateway 프로세스 없이 직접 Telegram API 호출 | 미기재(README는 여전히 실제 Hermes gateway가 이 역할을 한다고 서술) | 미기재 | 정확히 반대로 기술되어 있음(README: gateway가 발송한다 / 실제: gateway 없이 wrap 스크립트가 직접 발송) |
| **hermes gateway 자체** | 오늘 `launchctl unload`로 완전 종료 — dronewikibot 실시간 응답 전용이었고, 2nd Brain 파이프라인과는 무관했음(확인됨) | "Hermes Agent v0.19.0이 automation backbone"이라고 기재 | 미기재 | README 기준 시스템의 "핵심"이라던 컴포넌트가 오늘부로 존재하지 않음 |

---

## 3. launchd 12개 잡 — 현재 실제 스케줄/역할 (문서 어디에도 없음)

| Label | 스케줄 | 실행 스크립트 | 역할 |
|---|---|---|---|
| `ai.2nd.daily-fetch` | 매일 07:30(오늘 03:30→07:30 재조정) | `hermes-wrap.sh` → `~/.hermes/scripts/2nd-fetch-inbox.sh` → `fetch-inbox.sh` | 8+ 소스 수집 → `inbox/` |
| `ai.2nd.daily-ingest` | 매일 08:00(오늘 04:00→08:00 재조정) | `daily-ingest-claude.sh`(`claude -p`) | inbox → canonical 컴파일 |
| `ai.2nd.sync-dronewiki` | 매일 08:30(오늘 04:30→08:30 재조정) | `hermes-wrap.sh` → `~/.hermes/scripts/dronewiki-sync.sh` | canonical/raw/그래프 → drone-wiki-web git push + Vercel 배포 |
| `ai.2nd.weekly-lint` | 월 05:00 | `weekly-lint-claude.sh`(`claude -p`) → `weekly-lint.py` | 고아 페이지/깨진 링크/SHA-256 드리프트 점검 |
| `ai.2nd.weekly-summary` | 월 05:30 | `weekly-summary-claude.sh`(`claude -p`) | 주간 지식 다이제스트 텔레그램 발송 |
| `ai.2nd.morning-report` | 매일 07:30(단, 오늘 daily-fetch도 07:30로 옮겨서 **동시 충돌 가능성 있음 — 후속 조정 필요**) | `morning-report-send.sh` | 새벽체인 검증 + 아침 브리핑 dronewikibot 발송 |
| `ai.2nd.lint-knowledge` | (plist 개별 확인 필요 — 이번 감사에서 스케줄 미확인) | `lint-knowledge.py` | canonical 스키마 게이트 |
| `ai.2nd.extract-knowledge-graph` | (동일) | `extract-knowledge-graph.py` | discovery 그래프 추출 |
| `ai.2nd.update-knowledge-graph` | (동일) | `update-graph.sh` | canonical 드론 그래프 갱신 |
| `ai.2nd.apply-kinetic-rules` | 매일 04:50 (메모리 기준) | `apply-kinetic-rules.py` | SWRL 규칙4(SLM/LLM 판별)·규칙6(미승인 가설 감사) |
| `ai.2nd.medic-wiki-fetch` | (미확인) | `hermes-wrap.sh` → `~/medic-wiki/scripts/fetch-inbox.sh` | **별도 프로젝트**(medic-wiki) 수집 — 2nd Brain 네임스페이스에 얹혀있음 |
| `ai.2nd.dronewiki-self-update` | (미확인) | (미확인) | 이번 감사에서 스크립트 미확인 — 후속 필요 |

**⚠️ 발견한 새 문제**: `daily-fetch`와 `morning-report`가 둘 다 07:30으로 겹친다(오늘 크론 재조정 때 daily-fetch만 07:30/08:00/08:30으로 옮기고 morning-report 기존 07:30은 그대로 둠). morning-report는 "새벽체인 4항목 검증"이 목적인데 daily-fetch가 아직 안 끝난 시점에 같이 돌 수 있다 — **morning-report도 09:00 이후로 재조정 필요** (다음 액션에 반영).

---

## 4. README 재작성 제안 (섹션별 초안 방향)

전면 재작성이 필요하다. 제안 구조:

1. **Automation Control Plane 섹션 전체 교체**: "Hermes Agent v0.19.0" → "**launchd(`ai.2nd.*`, 12개 잡) + `claude -p`(Claude Pro 구독)**"로 교체. `hermes cron create` 등록 커맨드 블록 삭제(더 이상 유효하지 않음). 대신 위 §3 표를 그대로 삽입.
2. **텔레그램 발송 메커니�즘 정정**: "Hermes gateway가 발송" → "`hermes-wrap.sh`가 게이트웨이 없이 직접 Telegram Bot API 호출"로 정정.
3. **Snapshot Synchronization 섹션 신설**: 현재 README에 아예 없음. §1 표 그대로 반영 + raw/ 동기화 포함.
4. **medic-wiki 관계 섹션 추가**: 최소 1문단 — "`ai.2nd.medic-wiki-fetch`는 별도 프로젝트 `~/medic-wiki`의 수집 잡을 2nd Brain 스케줄러 위에서 실행한다."
5. **README.ko.md는 README.md 확정 후 동일하게 재번역**(현재도 영문판과 구조 동일하게 유지되고 있으므로 순서만 지키면 됨).
6. `00_CURRENT_SYSTEM.md` §14는 **"sync-wiki.sh" → "dronewiki-sync.sh"로 정정 + P0 항목 해제**(더 이상 unknown 아님).

---

## 5. README와 무관한 추가 발견(코드 자체 이슈)

- **`ai.2nd.daily-fetch`와 `ai.2nd.morning-report` 스케줄 충돌**(위 §3) — 재조정 필요.
- `daily-ingest-claude.sh`는 `set -euo pipefail`로 안전하게 작성돼 있고 자체 주석도 정확함 — **이 파일은 문서화 모범 사례로 인용해도 될 정도** (다른 스크립트들도 이 수준의 자기설명 주석을 따라가면 좋겠음).
- `medic-wiki-fetch`가 2nd Brain 네임스페이스 안에 있는 것 자체가 향후 "2nd Brain 은퇴/이관" 같은 작업 시 medic-wiki 수집이 실수로 같이 꺼질 위험 — 별도 `ai.medic-wiki.*` 네임스페이스로 분리하는 게 장기적으로 안전(당장 필수는 아님, 다음 액션 후보로만 기록).
- `ai.2nd.dronewiki-self-update`, `ai.2nd.lint-knowledge`, `ai.2nd.extract/update-knowledge-graph`의 정확한 스케줄은 이번 감사에서 미확인 — README 최종 작성 전 plist 4개 추가 확인 필요.

---

## 다음 액션 (마스터 승인 대기)

1. README.md/README.ko.md 전면 재작성(§4 방향대로)
2. `00_CURRENT_SYSTEM.md` §14 정정(sync-wiki.sh→dronewiki-sync.sh, P0 해제)
3. `ai.2nd.morning-report` 스케줄을 09:00 이후로 재조정(daily-fetch와의 충돌 회피)
4. 남은 4개 plist(dronewiki-self-update/lint-knowledge/extract-graph/update-graph) 스케줄 확인 후 §3 표 보완
