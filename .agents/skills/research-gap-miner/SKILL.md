---
name: research-gap-miner
description: canonical 위키 전체를 읽고 연구 공백(반복 한계, 모순, 미비교 방법, 미결합 기술, 평가 부족, 환경 편향, 벤치마크 필요)을 찾아 research/gaps/research-gaps.md 원장을 갱신한다(Weekly). 연구 주제 발굴 시 사용.
---

# Research Gap Miner

산출물은 staging(`research/gaps/`)이며 canonical이 아니다. index.md/log.md에 올리지 않는다.

## 절차
1. `concepts/`, `comparisons/`, `queries/`, `entities/`와 최신 `research/synthesis/*.md`를 읽는다
2. 각 페이지에서 다음 8가지 질문을 반복 적용:
   1. 여러 논문에서 반복되는 한계  2. 서로 모순되는 결과  3. 아직 직접 비교되지 않은 방법
   4. 아직 결합되지 않은 두 기술  5. 평가 데이터가 부족한 가설  6. 특정 환경에서만 검증된 주장
   7. 시간적 인과가 검증되지 않은 연구  8. 새 benchmark가 필요한 영역
3. `research/gaps/research-gaps.md`(롤링 원장)를 읽고 **갱신**한다: 기존 gap은 근거 추가/해소 표시, 신규 gap은 `GAP-NNN` 부여(번호 재사용 금지)
4. 각 gap 항목 형식:
   `### GAP-012 · <제목>` / status: open|narrowing|closed / 유형(1~8) / 근거: `[[page]]` + `^[raw/...]` / 처음 발견일 / 마지막 확인일 / 해소 조건

## 규칙
- 근거 페이지·raw 경로가 없는 gap은 쓰지 않는다. "있을 법한" 공백 금지
- 이번 실행에서 새로 생긴 근거로 닫힌 gap은 삭제하지 말고 `closed` + 사유 기록

## 출력
- 마지막 줄: "gap 신규 a / 갱신 b / 해소 c (총 open N)"
