# AI_RESEARCHER_ROADMAP.md — Phase 0~5 구현 로드맵

> 작성: 2026-07-31 | 전제: `AI_RESEARCHER_ARCHITECTURE.md` 설계 승인
> 원칙: 최소 변경 · 기존 기능 무폐기 · 각 Phase는 독립 롤백 가능 · Phase 착수는 마스터 지시로만

---

## 전체 순서 요약

```
Phase 0  문서화·스키마 등록          완료 (2026-07-31)
Phase 1  MVP: 연구 루프 + CLI 승인    완료 (2026-08-01) — T1/T2/T3 전부 통과
Phase 2  검색 강화: 임베딩+하이브리드 (2026-08-01, 부분완료 — 그래프 스키마 확장·노드ID 통일은 이연)
Phase 3  텔레그램 승인 게이트         (1일)
Phase 4  검증 자동화(Critic/Verifier 심화) (1~2일)
Phase 5  웹 연구 탭(읽기 전용)        (1일)
```

각 Phase 완료 기준 미충족 시 다음 Phase 착수 금지 (QA Layer 규칙 준수).

> **Phase 1 실제 구현 결과 (2026-08-01)**: 아래 원안보다 마스터의 후속
> 상세 스펙에 따라 더 단순화되어 구현됨 — 5단계 LLM 파이프라인
> (Planner→Hypothesis→Critic→Verifier→Report), 카테고리 기반 저장구조
> (`research/{runs,hypotheses,reviews,drafts}/`), G1/G3 게이트 제거,
> canonical 승격 완전 이연. 실사용 테스트 중 결함 5건 발견·수정
> (한글 슬러그 처리, `claude -p` 도구 접근 차단, CLAUDE.md 격리,
> 검색 스니펫 절단 완화, 테스트 기준서 자체의 오류). 상세는
> `AI_RESEARCHER_ARCHITECTURE.md` 상단 대조표와 `MVP_ACCEPTANCE_TESTS.md`
> 판정 기록 참조. 아래 Phase 1 섹션은 최초 설계안 그대로 보존한다.

---

## Phase 0 — 문서화·스키마 등록

**작업**
1. 본 문서 5종을 `~/2nd/docs/`에 저장 ✅ (본 커밋)
2. `AGENTS.md`에 "Research Layer" 섹션 추가 (research/ 계층 정의, 쓰기 권한 계약)
3. `SCHEMA.md` 디렉터리 역할 표에 `research/` 1행 추가 ("연구 세션 스테이징 — canonical 아님, 배포 대상 아님")

**예상 변경 파일**: `docs/` 5개 신규, `AGENTS.md`, `SCHEMA.md` (각 1개 섹션/1행)

**위험**: 없음 (문서만)
**완료 기준**: weekly-lint가 research/를 canonical 감사 대상에서 제외함을 확인
**롤백**: 추가 섹션 삭제

---

## Phase 1 — MVP: 연구 루프 + CLI 승인 ★

**작업**
1. `research/RESEARCH_SCHEMA.md` 작성 (아키텍처 문서 부록 A 확정)
2. `research/prompts/` 역할 프롬프트 7종 (planner/retriever/analyst/gap/hypothesis/critic/verifier+writer)
3. `scripts/research-run.sh` — Orchestrator 상태 머신:
   - `research-run.sh new "<연구 목표>"` → 세션 생성 → ①~⑧ 순차 실행 → G2 대기
   - `--resume`, `--from <stage>`, `--strict`(G1 대기) 옵션
   - claude -p 호출 시 **프롬프트 stdin 전달** (기존 확인된 패턴: --allowedTools 사용 시 stdin 필수)
   - 연속 2회 실패 시 중단 + 텔레그램 보고 (Safety Guard)
   - 세션당 LLM 호출 ≤10회 하드 리밋
4. `scripts/research-promote.sh` — G3 승격:
   - `--approve [--items ...]` / `--reject` / 항목 단위 선별 승격
   - canonical 페이지 생성(frontmatter 9필드, confidence low|medium 강제, wikilink≥2 검증) + index.md + log.md 원자적 3동작
   - 사후 검증: 생성 페이지 SCHEMA lint + raw sha256 무변경 확인

**예상 변경 파일**: 신규 — `research/RESEARCH_SCHEMA.md`, `research/prompts/*.md`(7), `scripts/research-run.sh`, `scripts/research-promote.sh`. 기존 수정 — 없음.

**위험**
- LLM 산출 품질 편차 → 역할 프롬프트에 출력 형식 강제 + 실패 시 1회 재시도
- 가설이 근거 없이 단정될 위험 → Verifier 단계에서 `[근거 부족]` 마킹 의무화, promote가 근거 없는 항목 승격 거부
- 듀얼코어에서 claude 세션 부하 → 순차 실행만(병렬 금지), 기존 max_parallel 규칙 준수

**완료 기준**: `MVP_ACCEPTANCE_TESTS.md` T1~T4 전부 통과
**롤백**: `research/` 삭제 + scripts 2개 삭제 — canonical/raw/기존 자동화 무영향

---

## Phase 2 — 검색 강화: 임베딩 + 하이브리드 + 그래프 스키마

> **1·2·5번 완료 (2026-08-01), 3·4번은 다음 증분으로 이연.** 아래는 원안
> 그대로 보존.

**작업**
1. ✅ `scripts/embed-docs.py` 신규 — ~~BGE-M3~~ **multilingual-mpnet** ONNX(CPU)로 canonical 132편+raw 33편+뉴스 300건=465건 임베딩 → `.ua/embeddings.json`. **청킹 없이 문서당 앞 2000자**로 스코프 축소(원안은 512토큰 청크 단위였으나 소규모 코퍼스에 과설계 판단). Python 3.14는 onnxruntime 미지원 확인되어 `~/2nd/.venv`(Python 3.11) 격리 환경 구성
2. ✅ `lib/rag.ts` 개선:
   - 모듈 레벨 문서 캐시 구현
   - 하이브리드 점수: `0.6*코사인 + 0.4*정규화 키워드` (원안의 그래프 부스트 0.2는 이미 `expandGraphNeighbors`가 별도 UI 경로로 처리 중이라 점수 결합에서는 제외 — 중복 방지)
   - embeddings.json 없으면 키워드 폴백 — tsx로 실측 확인, 회귀 없음
   - 질의 임베딩: `.venv` 존재 여부로 자동 분기 — 로컬 dev/연구 파이프라인은 하이브리드 활성, Vercel(venv 미배포)은 자동 키워드 폴백. **2026-08-01 마스터 결정: 프로덕션 웹 Q&A는 현상태(키워드 전용) 유지 확정.** OpenRouter `/api/v1/embeddings`(`https://openrouter.ai/api/v1/embeddings`, OpenAI 호환, 예: `openai/text-embedding-3-small`)가 실존함을 검증했으나, 로컬 문서 벡터(multilingual-mpnet)와 다른 모델이라 그대로 섞으면 벡터공간이 달라 무의미한 코사인 값이 나온다는 문제를 발견 — 프로덕션 적용 시 (a) 문서·질의 전체 재구성 또는 (b) 웹 배포 전용 별도 임베딩 파일 중 하나가 필요하며, 두 경로 모두 **매 웹 질문마다 영구적인 유료 API 비용**이 발생. 마스터가 이 반복비용 대비 이득이 크지 않다고 판단해 보류. 재검토 조건: 키워드 검색의 실사용자 불만이 실제로 누적되거나, 무료/저비용 임베딩 API 대안이 생길 때.
3. ⏸ 그래프 스키마 확장(`type/evidence/confidence/status` 필드) — 이연
4. ⏸ 노드 ID 통일(bare slug ↔ `article:` prefix) — 이연
5. ✅ `sync-wiki.sh`에 embeddings.json 복사 추가 (내용 불변 시 git diff 없어 매일 커밋되지 않음 확인)

**실측 검증**: 한글 전용 질의("위치 인식 불가 상황에서 스스로 길을 찾는 기술", 영단어 0개)로 `decentralized-swarm-gps-denied` 등 검색 성공 — 기존 키워드 방식이면 0건. 기존 강한 키워드 질의("PX4 ArduPilot EKF 비교") 무회귀 확인. `research-search.py`(Python)와 `rag.ts`(TS) 두 구현이 동일 질의에 대해 거의 동일한 점수 산출 확인(로직 일관성).

**예상 변경 파일**: 신규 — `scripts/embed-docs.py`. 수정 — `lib/rag.ts`, `scripts/research-search.py`, `scripts/sync-wiki.sh`(drone-wiki-web)

**위험 (실제 발생분 포함)**
- rag.ts 회귀 → 폴백 경로 유지 + tsx 스모크 테스트로 실측 확인
- **실제 발생**: BGE-M3가 채택 라이브러리(fastembed)에 없음을 뒤늦게 발견 → multilingual-mpnet로 교체(실측 검증 완료, `TECHNOLOGY_DECISION_RECORD.md` 정정)
- **실제 발생**: 시스템 Python 3.14가 onnxruntime 미지원 → Python 3.11 venv로 격리
- Vercel 스냅샷 크기 증가 → 465건 3.65MB로 확인, 문제 없는 수준
- 자동 배포 파이프라인(2nd-sync-dronewiki, 매일 04:30) 통한 3.65MB 파일 최초 1회 자동 커밋·푸시·배포 발생 예정 — 마스터 인지 필요

**완료 기준**: 한글 질의("군집 비행 충돌 회피") → 영문 문서(`swarm-coordination` 등) top-5 검색 성공. 기존 영문 질의 무회귀
**롤백**: embeddings.json 삭제 → 자동 키워드 폴백. rag.ts 이전 커밋 복원

---

## Phase 3 — 텔레그램 승인 게이트

**작업**
1. G2 도달 시 Hermes로 보고서 요약 + 세션 ID 텔레그램 전달 (`hermes send -t telegram` — 기존 확인된 즉석 발송 경로)
2. 승인 응답 처리 — 2안 중 구현 시 선택:
   - A안: Hermes Agent(@dronewikibot) 대화로 "승인 <id>" 수신 → promote 트리거 (Hermes 양방향 처리 검증 필요)
   - B안: AI Fleet HITL 텔레그램 승인게이트(2026-07-06 구축) 재사용 — 기존 검증된 승인 흐름
3. 메시지 prefix `[연구]`로 weekly-summary와 채널 구분

**예상 변경 파일**: `scripts/research-run.sh`(G2 전달부), Hermes 훅 또는 fleet 승인게이트 연결 스크립트

**위험**: 텔레그램 오승인(오타) → 승인 명령에 세션 ID 전체 요구 + promote가 재확인 요약 출력
**완료 기준**: 텔레그램에서 승인 → 승격까지 E2E 1건 성공
**롤백**: CLI 승인으로 복귀 (Phase 1 경로는 항상 유지)

---

## Phase 4 — 검증 자동화 심화

**작업**
1. `scripts/verify-claims.sh` 신규 — canonical/연구보고서의 `^[raw/...]` 마커 전수 검증(경로 실존 + 해당 raw에 관련 내용 존재 여부 LLM 스팟체크)
2. 모순 배치 탐지 — 주간(weekly-lint 뒤) 신규/변경 canonical 쌍의 contradicts 후보를 LLM으로 탐지 → **자동 기록 금지**, 마스터 승인 큐로만 제안
3. Critic 강화 — 구현 가능성 평가에 하드웨어/규제 제약 체크리스트(기존 domain 태그 기반) 주입

**예상 변경 파일**: 신규 — `scripts/verify-claims.sh`. 수정 — `research/prompts/critic.md`, Hermes cron 1잡 추가(주간)

**위험**: 모순 오탐 → 제안만 하고 기록은 승인 후. LLM 비용 → claude 구독 내 배치, 주 1회 한정
**완료 기준**: 기존 canonical 120편 검증 리포트 산출 + 오탐률 마스터 확인
**롤백**: cron 잡 제거, 스크립트 삭제

---

## Phase 5 — 웹 연구 탭 (읽기 전용)

**작업**
1. `drone-wiki-web/app/research/` — 승인 완료 세션 목록·보고서 열람·승인 이력
2. sync-wiki.sh에 **G3 승인 완료 세션만** 스냅샷 포함 (state.json의 approvals.G3=true 필터)

**예상 변경 파일**: 신규 — `app/research/page.tsx` 등 2~3파일. 수정 — `scripts/sync-wiki.sh`

**위험**: 미승인 노출 → 필터를 sync 스크립트와 페이지 양쪽에서 이중 적용
**완료 기준**: 미승인 세션이 배포 스냅샷에 부재함을 파일 목록으로 확인
**롤백**: 라우트 삭제 + sync 필터 제거

---

## Phase 간 의존성

- Phase 1은 Phase 2 없이 동작 (검색은 현행 키워드 방식 사용) — **MVP를 검색 개선에 인질 잡히지 않게 함**
- Phase 3~5는 각각 독립 — 순서 교체 가능 (마스터 우선순위에 따름)
- 전 Phase 공통 불변 조건: raw 무수정 · 승인 전 canonical 무변경 · 기존 cron 6잡 무중단
