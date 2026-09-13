# 00_CURRENT_SYSTEM — 2nd Brain × DroneWiki

기준: 2026-09-14 KST. Stage 0-R 로컬 안정화 중, **종료 보류**.
기준 HEAD: 2nd `8ff794e`, DroneWiki `ba13767`. 사용자 기존 미커밋 지식 변경을 보존한다.
상세 변경/검증/rollback: [Stage 0-R](docs/STAGE_0R_REBASELINE.md).

## 근거 분류

- VERIFIED: 이번 세션에 파일·설정·테스트·로그로 확인.
- INFERRED: 코드/구성에서 도출했으나 live 호출을 관찰하지 않음.
- UNKNOWN: 근거 부족. 과거 문서의 완료 판정으로 대체하지 않음.

## 시스템 경계

```text
External sources
  → ~/2nd (source of truth)
      raw (불변 원문)
      canonical (entities/concepts/comparisons/queries)
      ontology / discovery / embeddings (.ua 파생자료)
      research (발행 금지, human approval 경계)
  → publication/policy.json
      기존 공개 bytes 해시 보존 + 신규/변경 bytes 명시 승인
      deny 우선 / 기본 review / 파생자료도 검토 대상
  → publication-preflight.py [현재 audit-only]
  → HOLD (기존 data/wiki snapshot 그대로 유지)
  → 향후 승인된 candidate → Git push / Vercel deploy [별도 승인]
```

## 운영 설정 — VERIFIED

현재 12개 ai.2nd.* jobs가 loaded이며 확인 시 last exit는 모두 0이다.
이는 과거 실행 결과이며 새 sync gate의 성공 판정이 아니다.

| Job | StartCalendarInterval (KST) |
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
| weekly-lint | 월요일 05:00 |
| weekly-summary | 월요일 05:30 |
| medic-wiki-fetch | 매일 05:00, 별도 프로젝트 |

실제 sync 호출: launchd → `scripts/hermes-wrap.sh` → `~/.hermes/scripts/dronewiki-sync.sh`
→ DroneWiki `scripts/sync-wiki.sh` → `scripts/publication-preflight.py`.
현재 wrapper는 버전 관리된 audit gate만 호출한다. 과거 unconditional rsync/Git/deploy 본문은 로컬 백업에 보존.
플리스트/loaded 스케줄은 변경하지 않았다. 생성 jobs는 여전히 독립 실행이므로 순서가 보장되지 않는다.

최근 과거 성공: 2026-09-13 17:48:31 sync 시작 → 17:56:28 종료/배포 성공 로그, 584 Markdown.
실측 self-update는 2026-09-12 04:20:05 → 04:30:08로 약 603초. 10분 간격 sync와 겹칠 수 있었다.
Discovery 최근 실측 20초, canonical graph·kinetic 약 1초 이하. Ingest의 정확한 종료 시각/소요는 UNKNOWN.

## 파이프라인 후보 — 구현 존재, 미활성

`scripts/knowledge-pipeline.py` 기본은 plan-only. `--run-local`은 중복 legacy jobs가 loaded이면 중단한다.

```text
Generate: fetch → ingest → self-update --apply
  → 초기 lint → embeddings --if-stale → discovery(limit15) → canonical graph
Validate: 전체 lint → kinetic --check → embeddings --check → graph coverage → publication gate
Publish: 별도 신규 디렉터리에 검토 candidate (기존 snapshot 수정 없음)
Deploy: 별도 승인, 자동 실행 없음
Report: 로컬 결과 JSON (외부 메시지 없음)
```

스케줄 활성화 전 기존 8개 fetch/ingest/self-update/lint/discovery/graph/kinetic/sync calendar trigger를
동시에 교체하고 수동 진입점까지 동일 lock을 사용해야 한다. 새 wrapper 하나만으로 legacy races가 해결되지는 않는다.
주간 lint/summary와 morning-report/medic jobs는 별도 유지하되 쓰기 충돌을 재검토한다.

## 실제 쓰기와 승인 경계

- daily-ingest: Claude CLI로 canonical 작성/정리. 일반 ingest에는 사전 승인 gate가 없다.
- 예약 self-update: `--apply` → `applyProposal` → canonical 파일과 `.ua/self-update-state.json`을 직접 쓴다.
  UI 수동 검토와 예약 자동 적용은 서로 다르다. 기존 proposal-only 설명은 폐기한다.
- Research: human approval 후 claim별 promotion. `research/` 전체는 공개 snapshot 금지.
- Discovery: 미검증 layer. GraphRAG에서 함께 탐색하지만 canonical 사실로 자동 승격하지 않는다.
- Hermes: 스케줄 호출자는 launchd. 레거시 파일 위치, 일부 알림/도구 의존은 여전히 남아 있다.

## RAG / GraphRAG

VERIFIED: `rag.ts`는 WIKI_PATH → HOME/2nd → data/wiki 순서로 경로를 찾는다.
배포 snapshot에 document embeddings가 존재한다. Query embedding은 해당 root의 `.venv/bin/python`을 요구하고,
없거나 실패하면 null → keyword fallback. Vercel 설정에 Python/model 설치 단계가 없다.
따라서 **production keyword-only는 코드/구성 기반 INFERRED**, live function log는 UNKNOWN.
이번에 snapshot 경로를 강제한 로컬 테스트로 keyword fallback은 VERIFIED.

Local hybrid는 같은 모델/768차원 문서·query 벡터와 실행 가능한 Python/model이 있을 때 동작한다.
`drone-knowledge-graph.json`이 canonical 파일, `discovery-knowledge-graph.json`이 미검증 graph다.
`knowledge-graph.json`은 legacy/플러그인 공유 이름이며 현재 canonical 전용 이름과 혼동하지 않는다.
RAG raw 범위와 embed generator raw 범위가 일부 다르므로 raw 전체 hybrid를 주장하지 않는다.

Production hybrid는 이번에 활성화하지 않는다. 별도 공급자를 쓰면 모델·차원뿐 아니라 pooling/정규화까지
같아야 하며, query 실패 시 현재 keyword fallback을 유지해야 한다. 신규 유료 API·상시 서버는 도입하지 않는다.

## Publication / freshness와 미해결

검사한 raw/canonical 문서의 publication 관련 메타데이터는 0건. 이 사실로 private 자료의 존재/부재를 단정하지 않는다.
정책은 기존 snapshot 596개 파일의 해시를 retention 기준으로 고정하고, metadata deny를 우선한다.
발행 정책 미승인 변경·전체 lint 13건·slug 중복 2건·잔존 graph node 1개·discovery pending 2건이 남아 있다.
임베딩 생성 결과와 최종 QA 값은 연결된 Stage 0-R 결과 문서를 따른다.

## 변경 범위

Publication audit/staging, 검증 preflight, 순차 pipeline 후보, embeddings freshness/atomic write,
전체 control-plane status, kinetic read-only check, 문서 정합성, Next.js middleware→proxy 최소 개명.
지식 문서/원문/공개 snapshot 대량 변경, 원격 push, production deploy는 수행하지 않았다.
