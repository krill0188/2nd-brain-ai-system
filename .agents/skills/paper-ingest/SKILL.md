---
name: paper-ingest
description: inbox/raw의 논문 1건을 읽고 핵심 주장·방법·한계·데이터셋을 구조화해 canonical 페이지로 반영한다(Daily = Evidence 2단계). 수집된 논문을 위키 지식으로 바꿀 때 사용.
---

# Paper Ingest

## 언제 쓰나
- inbox/에 처리 대기 논문이 있을 때, 또는 "이 논문 위키에 반영해줘"
- 자동 경로: `Generate:ingest` 단계(`scripts/daily-ingest-Codex.sh`). 이 skill은 그 절차의 논문 특화 체크리스트다.

## 절차 (summarize-note + publish-entry 위에 얹는다)
1. 논문 전체를 읽고 아래 항목을 추출(원문에 없으면 "미기재"로 둔다, 추측 금지):
   - 핵심 주장 / 방법 / 데이터셋·환경 / 지표·결과 / 저자가 밝힌 한계 / 관련 선행연구
2. SCHEMA.md Page thresholds 확인 → 새 페이지 vs 기존 페이지 증거 추가 결정
3. `summarize-note` 절차로 canonical 작성(9개 필수 frontmatter, `domain`, 문장 단위 `^[raw/...]` 마커, 위키링크 ≥2)
4. 기존 페이지와 **충돌하는 주장**은 덮어쓰지 말고 `contested: true` + `contradictions` 기록
5. `publish-entry`로 index.md/log.md 동기화, 처리한 inbox 원본은 `inbox/processed/`로 이동
6. raw/ 수정 금지

## 검증
- `python3 scripts/lint-knowledge.py --recent-hours 1` 통과
- 모든 sources 경로가 실제 존재

## 출력
- 신규/갱신 canonical 경로 목록 + "수집 N개, 컴파일 N개, 실패 N개"
