# 마스터 2nd Brain AI System — 시스템 아키텍처

> 문서 상태: v1.0  
> 작성일: 2026-07-26  
> 적용 대상: ~/2nd (ains-lab/2nd-brain-template 기반, 마스터 AI 도구 적용)

이 문서는 ains-lab 원본 PKM 아키텍처를 마스터의 실제 도구 체계로 대체한 버전이다.  
아키텍처 다이어그램: `master-ai-architecture.html`

---

## 핵심 구조: 4계층 + AI Control Plane

```
[VS Code · AI Control Plane · 자동화 제어층]
collect-inbox → organize·Kimi → compile·Claude → verify·Gemini → deliver·sync
      ↓               ↓               ↓               ↓               ↓
[Layer 1]       [Layer 2]       [Layer 3]       [Layer 3]       [Layer 4]
Evidence        Canonical       Discovery       Discovery       Decision
```

---

## Layer 1: Evidence (원본·출처)

**역할**: 원본 자료를 수정하지 않고 보존한다.

| 수집 도구 | 저장 위치 | 특징 |
|---|---|---|
| Obsidian Web Clipper | `raw/web/` | 웹 페이지 원본 Markdown |
| Zotero + Connector | `raw/articles/`, `raw/papers/files/` | 논문·서지 메타데이터 |
| YouTube 자동수집 | `raw/youtube/` | 영상 메타데이터·트랜스크립트 |
| NotebookLM 내보내기 | `raw/notebooklm/` | 소스 레코드·AI 질의 결과 |
| 수동 녹취 | `raw/transcripts/` | 강의·회의 녹취 |

**보존 규칙**:
- `raw/` 하위 본문은 절대 수정 금지
- SHA-256 무결성 기록 (캡처 시점)
- AI 합성 결과를 raw에 저장 금지

---

## Layer 2: Canonical Memory (장기 기억)

**역할**: 반복 재사용할 지식을 출처와 함께 구조화한다.

| 담당 도구 | 역할 |
|---|---|
| **OpenCode + Kimi K2** | 문서 정리, llm-wiki 역할, 반복 초안 작성 |
| Obsidian Vault | 읽기·편집·역링크·Graph View |

**저장 위치**:
- `entities/` — 고유 개체 (인물, 프로젝트, 도구)
- `concepts/` — 개념 정의 및 원리
- `comparisons/` — 도구·방법론 비교 분석
- `queries/` — 검증된 질의 결과

**Governance**: `SCHEMA.md` → `index.md` → `log.md` 3중 동기화

---

## Layer 3: Discovery (탐색·가설)

**역할**: AI 도구로 관계를 발견하고 가설을 생성한다. **확정 지식 아님**.

| 담당 도구 | 역할 |
|---|---|
| **Claude Code** | 아키텍처 분석, 복잡한 합성, 설계 검토 |
| **Codex** (ChatGPT Plus) | 코드 탐색, 구현 후보 생성 |
| NotebookLM | 제한된 소스 질의, 질문 생성 |
| `.ua/` knowledge graph | 군집·브리지·공백 후보 식별 |

---

## Layer 4: Decision (검증·재사용)

**역할**: 사람이 검증하고 canonical 승격 여부를 결정한다.

**Human Review Checklist**:
- [ ] 원문과 일치하는가?
- [ ] 중복·모순이 없는가?
- [ ] 출처가 실재하는가?
- [ ] AI 합성·외부 주장·개인 판단이 분리되어 있는가?
- [ ] 재사용 가치가 있는가?

**Accepted 시 액션**:
1. canonical 페이지 생성/갱신
2. `index.md` 동기화
3. `log.md` 이력 추가
4. GitHub push (명시적 승인 후)
5. Notion 동기화 (선택)

---

## AI 도구 역할 구분 (원칙)

| 도구 | 연결 방식 | 역할 |
|---|---|---|
| OpenCode + Kimi K2 | OpenRouter API (환경변수) | 문서 정리, 반복 초안, llm-wiki |
| Claude Code | Claude Max 구독 로그인 | 아키텍처, 복잡한 분석, 최종 검토 |
| Codex | ChatGPT Plus 구독 | 코드 구현, 버그 수정, Git 분석 |
| Gemini Code Assist | VS Code 확장 (구글 계정) | 교차검증, 요약, 대안 탐색 |

**핵심 원칙**: Claude Max / ChatGPT Plus는 OpenCode를 통하지 않는다.  
OpenCode = OpenRouter + Kimi K2 전용이다.

---

## 피드백 루프

```
Discovery 결과 → Human Review Gate
  ├─ Accepted → Canonical Memory (Layer 2) 승격 → index.md + log.md 동기화
  ├─ Disputed → contradictions 기록
  ├─ Deferred → query 보류
  └─ Rejected → 기각 (log.md 기록)
```

**Accepted만 canonical 반영** → OpenCode Cron으로 지식그래프 재생성 → Layer 2 갱신
