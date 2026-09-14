# Stage 0-R 후속 안정화 — 2026-09-14

판정: **HOLD — 로컬 결함 수정 완료 범위와 발행/운영 전환 미완료를 구분한다.**

## 이번 변경과 이유

- `scripts/build-canonical-graph.py`, `update-graph.sh`: 현재 canonical에서 노드 속성을 다시 생성하고 원자적으로 저장한다. 사라진 노드와 깨진 참조는 정리하되, 기존 유효 관계는 검토 표시로 보존한다. 중첩 경로·legacy article ID·최초 legacy seed 호환을 유지한다.
- `scripts/artifact-status.py`: 개수뿐 아니라 원본 fingerprint 일치와 남은 관계 검토량을 보고한다.
- `scripts/extract-knowledge-graph.py`: 실패한 문서를 완료로 기록하지 않고 재시도 대상으로 남긴다. 부분 실패도 실패 exit를 반환한다. graph/state는 개별 원자 저장하며, provider 예외 상세를 출력하지 않는다. 두 파일을 하나의 트랜잭션으로 저장하는 것은 아니다.
- `scripts/embed-docs.py`: 모델·fastembed 버전·입력 형식이 같을 때 문서별 입력 hash로 벡터를 재사용한다. 변경 문서만 계산하고, 계약이 달라지면 전체 재생성한다. 새 실행끼리는 파일 잠금으로 중복 생성을 거부한다. 기존 keyword fallback은 그대로다.
- `scripts/test_graph_refresh.py`, `test_embedding_freshness.py`: 실패 재시도·중복 slug 차단·관계 보존·입력 변경·버전 변경 회귀 검사.
- canonical 13개 문서의 관련 링크 보완, QGroundControl 버전 문서 경로 분리, A2Z 중복 문서의 근거 있는 내용 통합. A2Z 이전 entity 본문은 `_archive/a2z-longtail-dual-entity.md`에 원본 그대로 보관. `index.md` 376개로 일치, `log.md` 추가 기록만 적용. 사용자 선행 변경과 겹쳐 canonical 변경은 강제 staging하지 않았고, 역적용 검사에 통과한 `canonical-own-changes.patch`로 따로 제공한다.
- `00_CURRENT_SYSTEM.md`, README, 이 후속 문서: 이전 미해결 수치와 현재 결과를 구분한다.

## 확인된 결과

- VERIFIED: canonical 376개, lint 위반 0, 중복 slug 0, canonical graph 376 nodes / 1682 edges, 누락·잔존 노드 0.
- VERIFIED: 기존 raw bytes 변경 0, 공개 snapshot 기준 596개 파일의 hash 변경 0, A2Z archive bytes 일치, log append-only.
- VERIFIED: graph consumer의 subgraph 탐색 정상(9 nodes), GraphRAG 호출 정상.
- VERIFIED: discovery 현재 pending 0, 1476 nodes / 1516 edges. **이 수치는 과거 추출 성공을 보증하지 않는다.**
- INFERRED: 현재 Vercel 코드/빌드 구성에서는 query Python 실행 경로가 없어 keyword fallback. 실서비스 invocation log는 UNKNOWN. 이전 snapshot 강제 로컬 fallback 검사는 통과했으며 retrieval 동작은 이번에 수정하지 않았다.

## 종료를 막는 항목과 보존한 불확실성

1. 초기에는 Publication Gate가 신규/변경 32개 파일을 보류했다. 별도 Terminal 작업의 커밋 `dff0925`가 이 32개에 정확한 hash 승인을 추가했고, 현재 정책 검사 결과는 approve 32 / retain 566 / exclude 24 / 삭제 0 / ready true다. 이 승인은 이 작업에서 작성하지 않았으며, 정책상 승인 상태와 실제 public 배포 승인은 구분한다. 초기 `publication-review-queue.json`은 당시 보류 목록이며 최신 판단은 `publication-audit.json`을 따른다.
   격리 candidate 생성도 통과했다(598 files / canonical 378개). 기존 공개 콘텐츠의 삭제를 금지한 retention 정책 때문에 과거 QGroundControl/A2Z duplicate slug 2건은 candidate에도 남아 있다. 원본 canonical은 376개로 정리됐지만 공개 전환 시 이 두 경로의 보존/대체 방침을 별도로 확정해야 한다. 실제 data/wiki 596개 파일은 변하지 않았다.
2. 기존 8개 daily 작업은 여전히 독립 calendar trigger다. `knowledge-pipeline.py`는 순차 실행 후보이며 loaded legacy가 있으면 실행을 거부한다. 실제 schedule 전환·첫 운영 주기의 순서/소요 검증은 미완료다. 시간을 뒤로 미루는 것만으로 순서 보장을 주장하지 않는다.
3. 기존 유효 graph 관계 425개는 현재 본문과 관계 유형까지 동일하게 재현되지 않아 `legacy-source-review-required`로 보존한다. 이 중 410개는 같은 방향의 문서 연결이 현재 본문에도 있지만 관계 유형이 다르고, 15개는 같은 방향 연결이 재현되지 않는다. 처음 계산한 순수 재생성안(1257 edges)은 적용하지 않았다. 실제 적용 결과는 1682 edges다.
4. 과거 discovery state는 실패도 완료 처리할 수 있었으므로, pending 0만으로 과거 전체 성공을 주장하지 않는다. 유료 재추출은 실행하지 않았다.
5. 기존 일부 canonical의 source 경로/태그는 SCHEMA와 맞지 않지만 현재 lint가 검사하지 않는다. lint 0을 전체 schema 준수로 해석하지 않는다.
6. 기존 웹 ESLint 오류 20건은 앞선 검증에서 확인된 별도 부채다. middleware→proxy 변경은 이전 로컬 커밋에 완료되어 있다.

## 현재/목표 실행 체인

```text
CURRENT
launchd 독립 작업 → ~/2nd 원본 + 파생자료
                             │
08:30 sync → preflight → publication-policy 검증
                            (이번 수동 검증 PASS)
                             │
                   기존 data/wiki 유지
                   push/deploy 실행 없음

TARGET (후보 구현, 미활성)
단일 trigger + 공통 lock
 → Generate: fetch → ingest → self-update --apply
 → lint → embeddings --if-stale → discovery → canonical graph
 → Validate: lint + kinetic/static + freshness + coverage + publication
 → Publish: 격리 candidate, 기존 snapshot 유지
 → Deploy: 별도 승인 이후
 → Report: 검증/배포 각각의 실제 결과
```

## 실행 순서 전환 조건과 rollback

- 기존 daily 8개와 주간 writer의 실제 명령/권한/환경을 유지한 migration manifest를 먼저 만든다. 모든 자동·수동 진입점이 공통 lock을 따르기 전에는 새 trigger를 활성화하지 않는다.
- 첫 전환은 배포 없는 candidate 실행으로 검증한다. 실패·시간초과·원본 변경이 있으면 Publish에 도달하지 않아야 한다. 현재 후보는 이 실패 차단을 갖췄지만 운영 주기 전환은 하지 않았다.
- `update-graph.sh` 및 graph builder는 이번 로컬 코드 커밋을 역적용하면 복원 가능하다. graph 이전 artifact는 `.ua/stage0r-backups/graph-followup-before.json`에 보관되어 있다.
- canonical 복원은 이 작업의 `work/canonical-link-fixes-before`, `work/a2z-supersession-before`, `work/followup` 백업과 own-change patch를 사용한다. 사용자 기존 미커밋 변경이 있으므로 전체 reset/checkout을 하지 않는다.
- 임베딩 이전 artifact는 현재 작업의 `work/followup/embeddings-before.json`에 보관한다. 이전 파일 복원 시 freshness가 stale로 판정될 수 있다.
- **과거 sync wrapper를 복원하면 자동 push/deploy가 다시 활성화될 수 있으므로 승인 없이 복원하지 않는다.** 이번에는 audit-only wrapper를 유지한다.
- 원격 push, production deploy, 공개 snapshot 교체, launchd reload는 이번 후속 작업에서 실행하지 않았다.

## 동시 실행 관찰

다른 Terminal의 Claude 프로세스가 동일 임베딩을 생성 중인 것을 프로세스 계층으로 확인했다. 중복 작업을 피하도록 이 작업에서 시작한 프로세스만 종료했다. 외부 프로세스를 종료하거나 재시작하지 않았다. 새 lock은 이미 실행 중이던 구 프로세스에는 소급 적용되지 않는다.

## 최종 QA와 산출물

- 회귀 fixture 19개 PASS: publication 8 / embedding 5 / graph refresh 4 / control status 2. 기존 graph library 6개도 PASS.
- Next.js production build PASS: 컴파일·TypeScript·정적 페이지 399개 생성 완료. 원격 배포는 수행하지 않음.
- Embeddings VERIFIED: 2026-09-14 23:44:18 KST 생성, canonical 376 + raw 204 + news 300 = 880개, 768차원. 현재 입력 fingerprint 일치. `--check` FRESH, `--if-stale`는 모델 실행 없이 0.42초에 종료했다. 생성 자체는 별도 Terminal에서 완료됐고 이 작업은 결과를 독립 검증했다.
- 최종 preflight 5개 항목 모두 PASS: canonical lint / kinetic-static / embedding freshness / graph coverage / publication policy. **이 검사는 원본과 발행 정책 검증이며 legacy schedule ordering을 보장하지 않는다.**
- 순차 pipeline staging과 graph compatibility wrapper의 Python을 프로젝트 venv로 통일해 launchd에서 PyYAML이 없는 system Python을 선택할 위험을 제거했다. 별도 작업의 preflight 수정 `e39cee1`, `dff0925`는 보존하고 재검증했다.
- `runtime-jobs.json`, `control-status.txt`: 12개 loaded jobs와 실제 plist 일정·실행 인자(안전한 경로만)·exit·로그 시각. 수동 검증 성공과 launchd의 과거 last exit는 별개다.
- `candidate-verification.json`, `preservation.json`: 격리 후보·원문·공개 snapshot 보존 증거.
- `canonical-changed-files.json`, `canonical-own-changes.patch`: 문서 변경 목록과 작업 시작 상태로 역적용 가능한 패치. 사용자 선행 변경이 있는 canonical/index/log는 강제 커밋하지 않았다.
- `local-commits.json`: 이번 코드/문서 커밋과 작업 중 별도 터미널에서 관찰된 커밋을 구분.

Stage 0-R 전체 종료는 계속 보류한다. 데이터 정합성·최신성·사전 검증은 통과했지만, 실제 Generate → Validate → Publish → Deploy → Report 운영 순서 전환은 아직 검증하지 않았고 공개 duplicate 경로 전환도 남아 있다. 원격 push/배포 승인 요청 단계에 도달했다고 간주하지 않는다.
