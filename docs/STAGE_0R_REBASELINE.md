# Stage 0-R re-baseline — 로컬 안정화 결과

검증일: **2026-09-14 KST**. 기준 HEAD: 2nd `8ff794e`, DroneWiki `ba13767`.
판정: **안전장치·로컬 복구 구현 완료 / Stage 0-R 종료 보류**.
원격 push, production deploy, 공개 snapshot 변경·삭제는 실행하지 않았다.

## 핵심 결과

| 우선순위 | 결과 | 근거/상태 |
|---|---|---|
| Publication Gate | 기본 review, 명시 allow, deny 우선. 기존 snapshot 596개 파일의 정확한 해시를 retention 기준으로 고정 | VERIFIED — audit/staging 구현·fixture 통과 |
| 운영 sync | 운영본을 repository wrapper로 통합, 현재 preflight/audit만 수행 | VERIFIED — 자동 rsync/push/deploy 경로 차단 |
| 실행 순서 | 순차 coordinator 후보와 lock·실패 중단 구현. 기존 독립 jobs가 loaded이면 실행 거부 | 구현 VERIFIED / 운영 전환 미활성 |
| Embeddings | 기존 465건 → 로컬 880건(376 canonical + 204 raw + 300 news), 768차원 | VERIFIED — fingerprint FRESH, local hybrid 점수 확인 |
| Production RAG | 배포 문서 벡터 존재. query Python 부재 시 keyword fallback | 코드 VERIFIED / production 동작 INFERRED / live log UNKNOWN |
| 문서 정합성 | Hermes·self-update 실제 쓰기·graph 파일명·GraphRAG·production RAG·예약 시각 정정 | VERIFIED |
| Control plane | 전체 ai.2nd.* 12개, plist/loaded/PID/exit/calendar/로그 mtime 표시 | VERIFIED — status에서 LLM 호출·로그 본문 제거 |
| Next.js 16 | middleware.ts → proxy.ts, export 이름만 변경 | VERIFIED — build·쿠키 smoke test 통과 |

`VERIFIED`는 이번 파일/설정/테스트/로그 확인, `INFERRED`는 코드에서 도출한 동작,
`UNKNOWN`은 확인하지 못한 상태다. 과거 배포 성공을 새 변경의 runtime 성공으로 표시하지 않는다.

## Publication 정책과 변경 영향

원본은 `~/2nd`, 공개 snapshot은 `~/projectm/drone-wiki-web/data/wiki`다.
정책 파일은 `~/2nd/publication/policy.json`이다.

- `research/`, `inbox/`, `innovations/`, `raw/career-quiz/`, `raw/papers/files/`는 발행 대상에서 제외한다.
  이는 저장소 역할/기존 sync 제외 규칙에 따른 정책이며 해당 자료가 private라는 추측이 아니다.
- 다른 디렉터리는 기본 review. 문서의 public 메타데이터, 명시 public 디렉터리, 또는 검토한 파일의 SHA-256 승인이 필요하다.
- private/internal/restricted/false/draft와 잘못되거나 중복된 관련 메타데이터는 allow보다 우선해 차단한다.
- 검사한 raw/canonical의 publication 관련 메타데이터는 **0건**. 이것만으로 비공개 자료가 존재한다거나 없다고 단정하지 않는다.
- 기존 공개 해시는 **현재 bytes 보존 허용**이며, 다음 수정본을 자동 승인하지 않는다. 기준 inventory는 자동 갱신하지 않는다.
- source에서 삭제돼도 기존 snapshot을 자동 삭제하지 않는다. 명시 deny가 기존 공개 파일에서 발견되면 자동 삭제 대신 전체 발행을 차단한다.
- 파생 graph/embeddings/news/briefing도 무조건 복사하지 않는다. 변경된 파생파일은 정확한 파일 승인과 source 검토가 필요하다.
- staging은 source/snapshot 밖의 새 디렉터리에서만 허용한다. symlink·경로 탈출·복사 중 hash 변경을 차단한다.
- `--stage`는 검토 candidate 생성 기능이다. 배포 승인이나 production 교체 기능이 아니다.

최종 audit: **593 retain / 3 hold / 24 exclude / 삭제 0**.
미승인 변경 3개는 `.ua/embeddings.json`, `.ua/drone-knowledge-graph.json`, `.ua/self-update-state.json`이다.
24개 제외 자료를 public snapshot에서 삭제한 것이 아니다. 실제 snapshot 596개 파일의 해시는 모두 기존 기준과 동일하다.
현재 gate는 파생자료를 정교하게 redaction하는 도구가 아니다. 새로운 파생 bytes를 자동 발행하지 않는 보수적 경계다.

## 실행 설정과 시간 근거

12개 ai.2nd.* jobs는 모두 loaded, 확인 시 PID는 idle이고 last exit는 0이었다.
전체 ProgramArguments/StartCalendarInterval과 로그 mtime는 `runtime-jobs.json`, `control-status.txt`에 기록했다.
환경값과 로그 본문은 기록하지 않았다.

| Job | 현재 시각 |
|---|---|
| daily-fetch | 매일 07:30 |
| daily-ingest | 매일 08:00 |
| lint-knowledge | 매일 08:12 |
| dronewiki-self-update | 매일 08:20 |
| sync-dronewiki | 매일 08:30, 현재 audit-only |
| extract-knowledge-graph | 매일 08:45 |
| update-knowledge-graph | 매일 08:47 |
| apply-kinetic-rules | 매일 08:50 |
| morning-report | 매일 11:30 |
| weekly-lint / weekly-summary | 월요일 05:00 / 05:30 |
| medic-wiki-fetch | 매일 05:00, 별도 프로젝트 |

기존 로그의 9/13 sync는 17:48:31 시작, 17:56:28 종료/배포 성공(584 Markdown)이다.
따라서 이전 대화의 “9/13 미실행”은 최신 기준으로 폐기한다. 이번 세션에서 배포한 것은 아니다.
self-update의 최근 관찰 소요는 **603초**(9/12 04:20:05~04:30:08)로, 10분 간격이 race를 막지 못한다.
Discovery는 20초, canonical graph/kinetic은 약 1초 이하로 기록됐다. Ingest 소요는 정확한 종료표식 부족으로 UNKNOWN.

기존 plist를 임의로 몇 분 미루지 않았다. 순차 후보는 중복 legacy jobs가 loaded인 동안 실행 자체를 거부한다.
활성화 전 8개 관련 daily calendar trigger를 함께 교체하고, 수동 writer와 weekly jobs까지 lock 적용 범위를 확인해야 한다.
현재 독립 생성 jobs의 순서 문제는 해결됐다고 주장하지 않는다. 다만 기존 자동 공개 경로는 audit-only로 막혀 있다.

## Embeddings와 RAG

로컬 생성시각: **2026-09-14 00:11:57 KST** (`created=2026-09-13T15:11:57Z`).
880개 벡터의 count/768차원/finite 값/입력 fingerprint 검증 통과.
같은 모델 `sentence-transformers/paraphrase-multilingual-mpnet-base-v2`를 무료 다운로드 후 로컬 계산했다.
새 유료 embedding API·상시 서버·새 production 인프라는 도입하지 않았다.
기존 465개 artifact는 `.ua/stage0r-backups/embeddings-before-20260913-234745.json`에 보존했다.

- 기본은 cached-only; 최초 다운로드는 명시 `--allow-download`에서만 허용.
- `--check`는 모델 실행 없이 freshness 확인. `--if-stale`는 입력이 같으면 모델 로드를 생략한다.
- 완성된 JSON을 atomic replace하며 생성 중 입력 변경/수치 오류/다운로드 실패 시 기존 파일을 유지한다.
- 첫 전체 생성은 약 20분이 걸렸고 높은 메모리 사용을 관찰했다. 후속 실행은 threads=2, batch_size=8로 제한했다.
  batch_size=8의 전체 생성 성능은 아직 별도 실측하지 않았다.
- 제안 cadence: 순차 ingest cycle의 변경 시에만 `--if-stale`; 고정된 별도 embedding 시각은 두지 않는다.
  향후 문서별 재사용 cache는 후속 최적화이며 이번 구현에 포함하지 않았다.
- FastEmbed 0.8.0의 기본 pooling 경고가 관찰됐다. 과거 artifact 생성 버전은 UNKNOWN.
  현재 local query와 새 문서 벡터는 같은 설치 모델로 검증했다. Production 활성화 전 버전·pooling 일치를 고정해야 한다.
- 공개 snapshot에는 기존 **465건** 임베딩을 유지했다. 로컬 복구를 production freshness 복구로 표현하지 않는다.

Production에서는 `WIKI_ROOT/.venv/bin/python`이 없으면 query vector=null → keyword fallback이다.
현재 Next.js/Vercel 설정은 Python/model을 설치하지 않는다. snapshot 경로를 강제한 로컬 RAG smoke test는 keyword 점수로 통과했다.
실제 Vercel function invocation log는 확인하지 않았으므로 production keyword-only는 코드/구성 기반 INFERRED다.
Local RAG는 새 벡터로 비정수 hybrid 점수를 반환했다.

저위험 production hybrid 활성화 경로는 아직 확정하지 않았다. 기존 모델과 다른 hosted embedding API를 붙이면
전체 문서 벡터 재생성이 필요하고 비용/지연/실패 경계가 바뀐다. 동일 모델 실행환경의 패키징·크기·cold-start 검증을
별도 수행한 뒤 결정한다. 이번에는 현재 keyword fallback을 유지한다.

## 아키텍처와 실행 체인

```text
현재 ACTIVE
External sources
  -> ~/2nd [source of truth]
      raw -> canonical -> ontology / .ua artifacts
      |      (독립 launchd 생성 jobs; ordering 미해결)
      v
launchd sync @08:30
  -> hermes-wrap.sh
  -> ~/.hermes/scripts/dronewiki-sync.sh [compatibility]
  -> drone-wiki-web/scripts/sync-wiki.sh
  -> publication-preflight.py
      lint + kinetic --check + embedding freshness + graph coverage + policy
  -> HOLD / audit 결과
      공개 snapshot 변경 없음 / Git push 없음 / Deploy 없음

기존 data/wiki [596 files; public publish snapshot]
  -> 기존 Vercel 서비스 [새 코드는 미배포]

순차 후보 (NOT ACTIVE)
Generate: fetch -> ingest -> self-update --apply -> 초기 lint
          -> embeddings --if-stale -> discovery(limit15) -> canonical graph
Validate: full lint -> kinetic --check -> freshness/coverage -> publication gate
Publish:  별도 review candidate
Deploy:   별도 승인 필요; 자동 실행 미구현
Report:   로컬 JSON 결과
```

## 변경 파일 목록과 이유

`~/2nd/`:

| 파일 | 변경 이유 |
|---|---|
| `publication/policy.json` | 문서/디렉터리 발행 정책 및 기존 공개 bytes baseline |
| `scripts/publication-gate.py` | audit/격리 staging, deny/경로/hash 경계 |
| `scripts/publication-preflight.py` | 발행 전 읽기 전용 검증 결과 집계 |
| `scripts/artifact-status.py` | canonical/discovery coverage·중복·미처리 상태 확인 |
| `scripts/knowledge-pipeline.py` | 순차 실행 후보, lock, 실패 후 단계 중단, legacy 중복 실행 거부 |
| `scripts/apply-kinetic-rules.py` | `--check`에서 지식 쓰기·알림 없이 규칙 검증 |
| `scripts/embed-docs.py` | fingerprint·cached-only·atomic write·실패 시 기존 파일 유지 |
| `scripts/ai-control.sh`, `scripts/ai-control-status.py` | 기존 명령 유지, 전체 control-plane 안전한 status |
| `scripts/test_publication_gate.py`, `scripts/test_embedding_freshness.py`, `scripts/test_ai_control_status.py` | 경계·실패 보존·상태 회귀 fixture |
| `AGENTS.md`, `README.md`, `README.ko.md`, `00_CURRENT_SYSTEM.md` | 현재 운영·쓰기·RAG 경계 정정 |
| `docs/2026-09-13-architecture-audit.md`, `docs/STAGE_0R_REBASELINE.md` | 과거 감사 표시 및 최신 결과 |
| `.ua/embeddings.json`, `.ua/drone-knowledge-graph.json` | 로컬 파생자료 갱신, 기존 파일 백업; Git 미추적 영역 |

`~/projectm/drone-wiki-web/`:

| 파일 | 변경 이유 |
|---|---|
| `scripts/sync-wiki.sh` | unconditional 공개 sync/deploy를 audit-only로 제한 |
| `lib/rag.ts` | 배포 document vector와 query runtime 주석 분리; 검색 로직 유지 |
| `middleware.ts` → `proxy.ts` | Next.js 16 파일/export 개명; 쿠키 로직 유지 |
| `scripts/self-update-pipeline.ts` | 실제 launchd 호출 설명 정정 |
| `README.md`, `docs/2026-09-13-architecture-audit.md`, `docs/STAGE_0R_REBASELINE.md` | 구조·파일명·쓰기에 관한 drift 정정 |

로컬 운영 파일 `~/.hermes/scripts/dronewiki-sync.sh`는 위 repository gate로 위임하도록 수정,
`~/.hermes/scripts/dronewiki-self-update.sh`는 실제 시각/쓰기 설명만 수정했다.
기존 사용자 수정 `extract-knowledge-graph.py`, `fetch-inbox.sh`, canonical/raw/index/log와 `site-audit/`는 건드리지 않았다.

## 검증 결과

- Next.js production build **PASS**. Proxy 경로 인식 확인.
- Proxy UUID 쿠키 신규 발급/기존 쿠키 유지 **PASS**.
- snapshot keyword RAG·GraphRAG smoke **PASS**, local hybrid score **PASS**.
- 기존 온톨로지 테스트 4/4 **PASS** (선행 TypeScript 컴파일 후 실행).
- Publication/pipeline 경계 8개 + embedding 3개 + status 2개 fixture **PASS**.
- 실제 kinetic `--check`: 3개 research 세션, 규칙4 변경 0/규칙6 위반 0. 지식 쓰기/알림 없음.
- 기존 공개 snapshot 전체 596개 파일 해시 동일, 삭제 0.
- 전체 canonical lint: 376개 검사, 기존 위반 **13건** → preflight 차단 정상.
- Graph: 376문서/374 unique slugs, 375 nodes/1697 edges. slug 중복 **2건**, 잔존 노드 **1개**.
- Discovery: 1463 nodes/1501 edges, 현재 미처리 **2개**. 기존 extraction은 실패 문서도 processed로 표시할 수 있어 과거 성공 완전성 UNKNOWN.
- 전체 ESLint: 기존 **20 errors**. 변경한 RAG는 주석만 바뀌었고, 오류는 기존 코드에 존재한다. 빌드 성공을 lint 성공으로 확대하지 않는다.
- 순차 coordinator의 실 운영 전환/end-to-end generate→deploy는 **NOT RUN**.

## Rollback과 운영상 주의

현재 audit-only로 인해 다음 예약 sync는 기존처럼 공개 내용을 갱신하지 않는다. 현재 서비스 snapshot은 보존되지만
신규 콘텐츠 발행은 blocker 해결과 승인까지 보류된다. next launchd exit는 검증 실패에 따라 2가 될 수 있으며 정상 배포로 해석하면 안 된다.

1. **안전한 기본 복구:** 현재 gate와 기존 snapshot을 유지한 채 원인을 해결한다. 전체 `git reset --hard`/`git add .`는 금지한다.
2. **운영본 복구가 명시적으로 필요할 때만:**
   `.ua/stage0r-backups/operational-sync-before.sh` → `~/.hermes/scripts/dronewiki-sync.sh`,
   `.ua/stage0r-backups/repository-sync-before.sh` → DroneWiki `scripts/sync-wiki.sh`로 복사할 수 있다.
   **이 복구는 과거 자동 push/deploy도 다시 활성화하므로 별도 승인 전 실행하지 않는다.**
3. **파생자료만 복구:** 백업 embeddings와 `canonical-graph-before.json`을 각각 `.ua` 원래 경로로 복사한다.
   knowledge 원문과 public snapshot에는 영향이 없다.
4. **코드/문서 복구:** 이번 로컬 커밋/변경 파일만 선택적으로 되돌린다. 사용자 기존 변경을 함께 되돌리지 않는다.
5. **Proxy 복구:** `proxy.ts`를 `middleware.ts`로 되돌리고 export 이름만 복구한 뒤 build/쿠키 테스트를 다시 실행한다.
6. plist/loaded schedule을 변경하지 않았으므로 이번 작업에 대한 launchctl rollback은 없다.

## 미해결 항목과 종료 조건

Stage 0-R은 **아직 종료할 수 없다**. 다음을 남긴다.

1. 의미 있는 근거를 확인해 기존 canonical lint 13건·slug 충돌/잔존 graph node를 정리한다. 이번에는 임의 링크 생성/자동 병합·삭제하지 않았다.
2. 신규 파생자료와 self-update state의 publication 정책을 검토한다. existing public 기준이 곧 새 내용 공개 승인은 아니다.
3. Discovery 2건 및 legacy 실패 추적 정확성을 해결한다. 이번에 유료 LLM extraction을 추가 실행하지 않았다.
4. 중복 calendar triggers와 수동 writer를 통제한 후 순차 pipeline을 로컬 dry-run부터 검증한다.
5. public candidate 영향 검토가 끝난 뒤에만 별도 push/production deploy 승인을 받는다.

Vercel live function log, root/system scheduler 전체 범위, 배포 후 새 runtime 동작은 UNKNOWN으로 남긴다.
Production hybrid와 신규 인프라 확장은 이번 종료 조건에 넣지 않는다.
