---
name: summarize-note
description: raw/ 원문 1건을 읽고 canonical 페이지(concepts/entities/comparisons/queries) 초안을 작성한다. 04:00 자동 daily-ingest를 기다리지 않고 지금 바로 canonical화하고 싶을 때 사용.
---

# Summarize Note

## 언제 쓰나
- 마스터가 "이 raw 문서/논문 정리해서 위키에 올려줘"라고 할 때
- 자동화(`2nd-daily-ingest`, 매일 04:00, `custom/llm-wiki-ains` 스킬)를 기다리지 않고 즉시 처리하고 싶을 때

## 먼저 알아야 할 것
이 시스템엔 "note"라는 별도 중간 산출물이 없다. source(raw, 불변 증거)와 note(요약)를 분리하지 않고, **canonical page 1개(concepts/entities/comparisons/queries 중 하나)로 바로 압축**한다(SCHEMA.md Layer 2). 이 skill의 결과물이 곧 최종 형태다 — 이후 별도 "승격" 없이 `publish-entry`로 index.md/log.md만 동기화하면 끝난다(단, `research/` 루프 산출물은 예외 — 그쪽은 실제 승인 게이트가 있다. `publish-entry` 참고).

## 절차
1. `raw/` 원문을 전체 읽는다 — 아직 요약하지 말고 구조부터 파악
2. SCHEMA.md "Page thresholds" 확인: 이 주제가 raw 소스 2개 이상에 등장하거나, 1개 소스에서 중심 주제인가? 아니면 새 페이지를 만들지 말고 **기존 페이지에 증거만 추가**한다
3. `type` 결정: `entity`(사물/조직/제품) / `concept`(개념·기법) / `comparison`(비교) / `query`(질의 종합)
4. `templates/<type>.md`를 복사해 시작
5. 9개 필수 frontmatter 채우기: `title`, `created`, `updated`, `type`, `tags`, `sources`, `confidence`, `contested`, `contradictions`
   - `tags`는 SCHEMA.md에 **이미 등록된 태그만** 사용(신규 태그면 SCHEMA.md "Tag taxonomy"에 먼저 등록)
   - `sources`는 실제 존재하는 `raw/` 경로만(리포지토리 상대경로), 없는 경로를 지어내지 않는다
   - `confidence`는 근거 다양성에 비례: 다중 독립 출처=high, 단일 출처=medium/low
6. 본문 작성: 여러 출처를 종합할 경우 문장 단위 근거 마커 `^[raw/<kind>/<file>.md]` 사용
7. `[[wikilink]]`로 관련 기존 canonical 페이지 최소 2개 연결(canonical link validity 규칙 — 1~2페이지짜리 고립 canonical 세트는 무효)
8. 200줄 넘게 자라면 페이지 분할 고려(SCHEMA.md 권고선)

## 검증
- 원문과 요약이 충돌하지 않는가
- confidence가 실제 근거 수와 맞는가
- wikilink 2개 이상 확보했는가
- 미등록 태그를 쓰지 않았는가

## 출력
- `entities/concepts/comparisons/queries/*.md` 신규 또는 갱신 파일 (index.md/log.md 반영은 `publish-entry`에서)
