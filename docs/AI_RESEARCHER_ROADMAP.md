# AI_RESEARCHER_ROADMAP.md — Phase 0~5 구현 로드맵

> 작성: 2026-07-31 | 전제: `AI_RESEARCHER_ARCHITECTURE.md` 설계 승인
> 원칙: 최소 변경 · 기존 기능 무폐기 · 각 Phase는 독립 롤백 가능 · Phase 착수는 마스터 지시로만

---

## 전체 순서 요약

```
Phase 0  문서화·스키마 등록          완료 (2026-07-31)
Phase 1  MVP: 연구 루프 + CLI 승인    완료 (2026-08-01) — T1/T2/T3 전부 통과
Phase 2  검색 강화: 임베딩+하이브리드+그래프 스키마 (2~3일)  ← 다음 착수 후보
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

**작업**
1. `scripts/embed-docs.py` 신규 — BGE-M3 ONNX int8(CPU)로 canonical 120편+뉴스 청킹·임베딩 → `.ua/embeddings.json` (문서 단위 + 512토큰 청크 단위). 밤 배치(fetch 체인 뒤) — Intel CPU에서 수 분 소요 예상, 배치라 무관
2. `lib/rag.ts` 개선 (기존 함수 시그니처 유지):
   - 모듈 레벨 문서 캐시(콜드스타트 1회 로드)
   - 하이브리드 점수: `0.5*벡터내적 + 0.3*키워드 + 0.2*그래프 인접 부스트`
   - embeddings.json 없으면 현행 키워드 방식 폴백 (무회귀 보장)
   - 질의 임베딩: Vercel에서는 OpenRouter 임베딩 호출 또는 키워드 폴백 — 구현 시 결정
3. 그래프 스키마 확장 — `update-graph.sh` 산출 엣지에 `type(supports|contradicts|depends-on|part-of|compares|wikilink)`, `evidence[]`, `confidence`, `status(canonical|hypothesis)` 필드 추가. frontmatter `contradictions` → `contradicts` 엣지 자동 생성
4. 노드 ID 통일 — bare slug 표준. Gate C(`article:` prefix) 병합 시 정규화 매핑
5. `sync-wiki.sh`에 embeddings.json 복사 1행 추가

**예상 변경 파일**: 신규 — `scripts/embed-docs.py`. 수정 — `lib/rag.ts`, `scripts/update-graph.sh`, `scripts/sync-wiki.sh`(1행), `drone-wiki-web/scripts/sync-wiki.sh`

**위험**
- rag.ts 회귀 → 폴백 경로 유지 + 기존 Q&A 스모크 테스트
- BGE-M3 설치 실패(Python 3.14 호환) → 대안: onnxruntime 고정 버전, 최후 폴백 OpenRouter 임베딩 API(소액)
- Vercel 스냅샷 크기 증가(벡터 JSON) → float16/8bit 양자화로 120편 기준 수 MB 이내

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
