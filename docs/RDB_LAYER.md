# RDB Layer (SQLite) — 운영 문서

> 상태: 구현됨(2026-10-20). 원본은 Git/Markdown이고 SQLite는 결정론적으로 재생성되는 파생물이다.

## 구성
| 구성 | 위치 | 역할 |
|---|---|---|
| 스키마 | `drone-wiki-web/scripts/knowledge_db_schema.sql` | 테이블·인덱스·FTS5 단일 정의 |
| 생성기 | `drone-wiki-web/scripts/build-knowledge-db.py` | 마크다운+온톨로지 → 텍스트 덤프(`data/knowledge/knowledge.sql`) |
| 시험 | `scripts/test_knowledge_db.py`, `scripts/test-kg-answer.ts` | DB 17건, 질의 시나리오 15건 + 실 NIM 2건 |
| 런타임 | `lib/kdb.ts`, `lib/kg-plan.ts`, `lib/kg-context.ts`, `lib/kg-verify.ts`, `lib/kg-answer.ts` | 적재·질의 계획·NIM context·후검증·JSON 계약 |
| API | `POST /api/kg-answer` | 신규. 기존 API는 `KG_BACKEND=sqlite`일 때만 같은 계획을 사용 |

## 실행
```bash
cd ~/projectm/drone-wiki-web
~/2nd/.venv/bin/python scripts/build-knowledge-db.py --check        # 발행 스냅샷 기준 빌드 + 감사
~/2nd/.venv/bin/python scripts/build-knowledge-db.py --wiki-root ~/2nd --out-sql /tmp/kdb-internal.sql --quality ""   # 내부(비공개 포함) 빌드
~/2nd/.venv/bin/python scripts/test_knowledge_db.py
npx tsx scripts/test-kg-answer.ts [--live]
```

## 보존 규칙
- `documents.domain` = frontmatter 값 그대로(없으면 NULL). 재분류·추론 금지. 시험이 원본 frontmatter와 100% 일치를 확인한다.
- domain / tags / ontology class는 별개. 새 domain·클래스는 제안(`ontology_class_proposals`)으로만 기록.
- discovery 그래프는 적재하지 않는다.
- 위키 문장 claim은 최대 `sourced`(요약이라 원문 인용 대조 불가).
- 출처 경로 해석: 자동 갱신이 `inbox/X` 출처를 `inbox/processed/X`로 옮기므로 해석기가 이동을 따라간다. `^[` 접두가 붙은 sources 항목은 정규화(원본은 수정하지 않음).

## 롤백
- `KG_BACKEND=json`(기본)로 즉시 복귀. 덤프 삭제와 재생성은 원본에 영향이 없다.
