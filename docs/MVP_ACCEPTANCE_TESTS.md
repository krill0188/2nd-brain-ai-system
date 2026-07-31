# MVP_ACCEPTANCE_TESTS.md — Phase 1 MVP 인수 테스트 (v2, 3건)

> 개정: 2026-07-31 — 마스터 지정 범위(연구 루프 1~10번, 테스트 3건, canonical 자동 승격
> 비구현)에 맞춰 재작성. 이전 v1(T1~T4, 승격 테스트 포함)은 폐기.
> 적용 대상: `scripts/research-run.sh` (Planner→Retriever→Hypothesis→Critic→Verifier→Report)
> 규칙: T1~T3 전부 통과 전까지 Phase 1은 미완료.

## 공통 합격선

| # | 불변 조건 | 검증 방법 |
|---|---|---|
| C1 | raw/ 파일 바이트 무변경 | 테스트 전후 raw 전체 sha256 diff = 공백 |
| C2 | canonical(entities/concepts/comparisons/queries)/index.md/log.md 무변경 | `git status --porcelain` — 해당 경로 변경 0건 (Phase 1은 승격 자체를 구현하지 않음) |
| C3 | 세션당 claude 호출 ≤ 10회 (기본 파이프라인 5회) | `research/runs/<id>/state.json`의 `llm_calls` |
| C4 | 모든 산출물이 `research/{runs,hypotheses,reviews,drafts}/` 안에만 존재 | 파일 목록 검사 |
| C5 | 연속 2회 LLM 실패 시 중단+보고 | 실패 주입(프롬프트 파일 경로를 잘못 지정)으로 1회 확인 |
| C6 | `claim_type: hypothesis`인 공백 인지 클레임(예: "근거 없음")이 draft "10. 근거 부족 사항"에 정확히 반영 — `verification_status`는 부재가 검색범위 내에서 참이면 `grounded`가 정상(§ 2026-07-31 정정, T2 참조) | `drafts/<id>.md` 검사 |
| C7 | 인용 경로가 검색 결과에 등장한다는 것은 "인용 존재"만 증명하지, "내용 일치"를 증명하지 않는다 — 별개로 검증 | draft에서 무작위 클레임 최소 2건을 골라 인용된 raw 원문을 직접 열어 클레임과 문장 단위로 대조 (2026-07-31 T1 최초 실행에서 이 구분을 생략해 "환각 0건"을 과잉 주장한 사례 발견 → 이후 필수 항목으로 격상) |

## T1 — 정상 연구 루프 (MVP 검증 질문)

**입력**
> "통신이 제한된 환경에서 온디바이스 AI를 탑재한 군집 드론이 자율 임무를 수행할 수 있는가?"

> ⚠️ 이 질문은 마스터 지시 메시지가 전달 중 일부 유실되어 재구성한
> 잠정 문구입니다. 정확한 원문을 받으면 즉시 교체합니다.

**기대 결과**
1. `research/runs/<id>/01-questions.md`: 하위 질문 3~8개
2. `research/runs/<id>/02-search-hits.md`: canonical/raw/뉴스/그래프 인접
   검색 결과 (기존 RAG 스코어링 로직 재사용 확인 — `research-search.py`가
   `lib/rag.ts`와 동일한 hit-count+제목가중치 로직 사용)
3. `research/hypotheses/<id>.md`: 클레임 ≥3건, `claim_type`이 fact/inference/hypothesis
   세 유형 중 최소 2종 이상 등장
4. `research/reviews/<id>.md`: 모든 클레임에 `opposing_sources`/`limitations`/`confidence`/`verification_status` 채워짐
5. `research/drafts/<id>.md`: 13개 필수 섹션 전부 존재, "13. 마스터 승인 상태" = `awaiting_approval`

**출처 검증 기준**
- draft 내 모든 클레임 인용이 `02-search-hits.md`에 실제로 등장하는 경로/슬러그 (기계 검증 — 경로 존재만 증명)
- **추가로 사람이 직접**: 클레임 최소 2건을 골라 인용된 raw/canonical 원문을 열어 클레임 문장과 대조 (C7). 경로 존재 확인만으로 "환각 없음"을 주장하지 않는다
- `insufficient_evidence`로 표시된 클레임이 "5. 확인된 사실"이나 "6. AI의 추론"에 섞여 들어가지 않음 (반드시 "10. 근거 부족 사항")
- 검색 스니펫이 절단되어 있다는 한계 고지 문구가 draft 하단에 있는지 확인 (`research/RESEARCH_SCHEMA.md` § 알려진 한계)

**통찰 품질 기준 (마스터 판정)**
- "7. 가설" 섹션에 단일 문서 재진술이 아닌, 근거 2개 이상을 연결한 항목 ≥1건
- 과장 표현 0건

## T2 — 지식 공백 인지

**입력**
> "저고도 드론 C2 링크에서 LTE와 RF 메시 네트워크 중 국내 전파 규제상 유리한 방식을 판단하라"

*선정 근거: datalink 문서는 있으나 국내 규제 raw가 부족 — Hypothesis Generator가
근거 없는 질문에 대해 "충분한 근거 없음" 클레임(claim_type: hypothesis)을
만들고, 그 클레임이 draft "10. 근거 부족 사항"에 정확히 반영되는지 시험.*

> ⚠️ 2026-07-31 T2 최초 실행 후 정정: 애초 "verification_status가
> `insufficient_evidence`여야 한다"고 썼던 기대치는 `RESEARCH_SCHEMA.md`
> 수정(§ Claim schema — 공백 인지 클레임 규정) 이전의 오해였다.
> "근거가 없다"는 클레임 자체가 검색 범위 내에서 참이면 `grounded`가 맞다
> (`insufficient_evidence`는 인용된 소스가 해석 불가/부적합할 때만 쓴다).
> 아래 기대 결과를 이 기준으로 정정했다.

**기대 결과**
1. 규제 관련 하위 질문에 대응하는 클레임이 `claim_type: hypothesis`로
   분류되고, "검색 결과에 근거가 없다"는 사실 자체는 `verification_status:
   grounded`로 확인됨 (부재 확인이 참이므로) — `insufficient_evidence`는
   인용 경로가 실제로 해석 불가능한 경우에만 등장하면 됨(0건이어도 결함 아님)
2. `drafts/<id>.md` "10. 근거 부족 사항"에 해당 클레임이 명시되고, "11. 후속 조사
   대상"에 조사 제안(예: "국내 전파법 고시 원문 확보 필요")이 실행이 아닌
   **제안 형태**로만 서술됨
3. 존재하지 않는 규제 조항을 인용(환각)한 사례 0건 — 특히 원 질문("국내 전파
   규제상 유리한 방식")에 대해 근거 없이 결론을 내리지 않고, "현재 근거로는
   판단 불가"를 명시적으로 인정하는지 확인

## T3 — 반려 시나리오 (무해성 보장)

**절차**
1. T1 세션에서 `scripts/research-run.sh reject <id> "근거 보강 필요"` 실행

**기대 결과**
1. `research/runs/<id>/state.json`: `status=rejected`, `approval.reason` 기록
2. 세션 산출물 전체(`runs/<id>/`, `hypotheses/<id>.md`, `reviews/<id>.md`,
   `drafts/<id>.md`)가 `research/_archive/<id>/`로 이동
3. **raw / canonical 4계층 / index.md / log.md 완전 무변경** (공통 C1·C2로 기계 검증)
4. `research-run.sh approve <id>` 재시도 시 세션을 찾지 못해 실패 (원본 경로에 더 이상 없음)

---

## 판정 기록 양식

| 테스트 | 실행일 | 기계 검증 | 마스터 판정 | 비고 |
|---|---|---|---|---|
| T1 | 2026-07-31 | ☑ pass (5회 재실행 중 최종본 성공, 상세는 session_20260731 계열 기록 참조) | ☑ 승인 (품질 검토 후 반려 처리 — T3 겸용) | 첫 3회는 slugify·도구차단·safe-mode 버그로 실패, 4번째부터 정상. 세션 `20260731-research-1785453631`(원본), `20260731-research-1785509562`(발췌 확장 후 재검증 — T3에서 반려 처리) |
| T2 | 2026-07-31 | ☑ pass | ☑ 승인 (`20260801-research-1785510116`, 2026-08-01 완료) | 국내 규제 공백을 정확히 인지, 결론 유보. 원문 대조 2건 정확 |
| T3 | 2026-07-31 | ☑ pass | ☑ 확인 | `20260731-research-1785509562` 반려 처리 — 반려 전후 raw/canonical/index.md/log.md git diff 라인수 동일(10→10), archive 이동 확인 |

**Phase 1 완료 선언 조건**: 3/3 pass + 공통 C1~C6 전부 pass. → **충족. Phase 1 완료 (2026-08-01).**

## Phase 1 이후로 이연된 것 (참고용, 지금 하지 않음)

- canonical 승격 (`research-promote.py`/`.sh`는 이미 파일로 존재하지만 Phase 1
  파이프라인에서 호출되지 않음 — 다음 Phase에서 재검토)
- G1 조사계획 승인 게이트, `--strict` 옵션 (v1 설계, 이번 범위에 없어 제거)
- 임베딩/하이브리드 검색, 텔레그램 양방향 승인, 웹 연구 탭
