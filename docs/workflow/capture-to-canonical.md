# 캡처 → Canonical 워크플로우

> 작성일: 2026-07-26  
> 참조: SCHEMA.md, AGENTS.md

---

## 전체 흐름

```
[외부 자료]
    ↓ Web Clipper / Zotero / 수동
[inbox/]          ← 임시 보관소 (분류 전)
    ↓ 분류
[raw/<kind>/]     ← 원본 보존 (수정 금지)
    ↓ OpenCode + Kimi K2 (llm-wiki)
[Draft 초안]      ← 합성·정리 (가설 단계)
    ↓ Claude Code (복잡한 분석) 또는 Kimi
[Discovery 결과]  ← 가설·보고서 (.ua/ 또는 queries/)
    ↓ Human Review Gate
[Canonical Page]  ← entities/ concepts/ comparisons/ queries/
    ↓ 동기화
index.md + log.md ← 항상 함께 업데이트
```

---

## Step 1: 수집 (Capture)

**목표**: 원본을 정확히 보존한다.

1. **웹 자료** → Chrome에서 Obsidian Web Clipper 클릭 → `inbox/`에 저장
2. **논문/기사** → Zotero Connector → Zotero에 저장 → `raw/articles/` 또는 `raw/papers/` 내보내기
3. **YouTube** → 트랜스크립트 복사 → `raw/youtube/` 에 저장
4. **수동 메모** → `inbox/` 에 날짜 파일명으로 저장 (`2026-07-26-idea.md`)

**규칙**: raw 파일에는 templates/raw-article.md frontmatter를 복사해서 사용

---

## Step 2: 정리 (Organize)

**담당**: OpenCode + Kimi K2

```bash
cd ~/2nd && opencode
```

Kimi에게 지시:
> "inbox/에 있는 <파일명>을 읽고 raw/<appropriate-dir>/에 맞는 형식으로 정리해줘.
> 원본 본문은 수정하지 말고, frontmatter만 채워줘."

---

## Step 3: 합성 (Compile)

**담당**: OpenCode + Kimi K2 (기본) / Claude Code (복잡한 분석)

Kimi에게 지시:
> "raw/<dir>/<file>.md 를 기반으로 concepts/ 또는 entities/에 canonical 페이지 초안을 만들어줘.
> templates/concept.md 형식을 사용하고, sources에 raw 경로를 기록해줘."

복잡한 설계·모순 분석은 Claude Code에서:
> "이 두 개념의 충돌을 분석하고 contradictions 목록을 채워줘."

---

## Step 4: 탐색 (Discovery)

**담당**: Claude Code / Codex / NotebookLM / Gemini

- NotebookLM에 raw 파일들을 소스로 추가하고 질의
- 결과를 `queries/` 에 templates/query.md 형식으로 저장
- **이 단계의 결과는 가설이다. canonical이 아니다.**

---

## Step 5: 승인 (Human Review)

마스터가 직접 검토:

```
checklist:
- [ ] 원문 경로가 존재하는가? (sources 목록의 raw/ 경로 확인)
- [ ] 중복 페이지가 없는가? (index.md 검색)
- [ ] 충돌하는 canonical 페이지가 없는가?
- [ ] confidence 수준이 적절한가?
```

---

## Step 6: Canonical 등록

**원자적 작업 (3가지 동시 실행)**:

1. canonical 페이지 저장 (`entities/`, `concepts/`, `comparisons/`, `queries/`)
2. `index.md` 업데이트 — 해당 섹션에 한 줄 추가
3. `log.md` 추가 — 날짜·액션·파일 경로 기록

```bash
# Git 커밋 (명시적 승인 후)
git add entities/new-page.md index.md log.md
git commit -m "feat: add canonical page <new-page>"
```

---

## 자주 쓰는 패턴

### 오늘 읽은 글 빠르게 캡처

```
1. Chrome에서 Web Clipper 클릭 → inbox/ 저장
2. opencode 열고: "inbox/오늘글.md raw/web/에 정리해줘"
3. 나중에 canonical로 승격 여부 판단
```

### 아이디어 메모 → concept 생성

```
1. inbox/idea-<날짜>.md 에 자유롭게 메모
2. claude: "이 메모 기반으로 concepts/ 초안 만들어줘"
3. 검토 후 승인 → index.md + log.md 동기화
```

### 코드 관련 지식

```
1. raw/articles/에 기술 문서 저장
2. codex로 코드 탐색·구현 후보 생성
3. Claude Code로 설계 검토
4. 검증된 내용만 concepts/ 또는 entities/ 승격
```
