---
name: ingest-source
description: 논문/웹 문서/영상/메모 등 자료 1건을 raw/(+inbox/)에 등록한다. 마스터가 특정 자료를 "지금 바로" 수집해달라고 할 때 사용 — 매일 03:30 자동수집(fetch-inbox.sh)과 별개로 단건 요청 시 쓴다.
---

# Ingest Source

## 언제 쓰나
- 마스터가 특정 논문/링크/PDF/텔레그램 링크 1건을 지금 바로 등록해달라고 할 때
- 자동수집(`fetch-inbox.sh`, 매일 03:30)이 놓친 자료를 수동으로 채울 때

## 이 시스템의 두 갈래 (섞지 말 것)

### (a) Zotero 경유 논문
Zotero Connector(Chrome)로 스크랩 → Zotero 라이브러리 → `scripts/zotero-ingest.py`.

```bash
python3 scripts/zotero-ingest.py --dry-run          # 미리보기
python3 scripts/zotero-ingest.py                    # 실제 실행
python3 scripts/zotero-ingest.py --topic drone-sw    # 특정 토픽만
```

생성물:
- `raw/papers/<topic>/<slug>.md` — 메타데이터 레코드
- `raw/papers/files/<topic>/<slug>.pdf` — 원문 첨부 사본(2026-08-10 추가, git 미추적·로컬 전용)
- `inbox/zotero-<slug>.md` — 다음 04:00 `2nd-daily-ingest`가 canonical 후보로 컴파일하도록 사본 배치

Zotero 앱이 실행 중이고 Settings → Advanced → "Allow other applications"가 켜져 있어야 한다.
기존 레코드에 첨부만 소급 반영하려면 `--backfill-attachments`.

### (b) 그 외 전부 (웹/유튜브/일반 PDF/텍스트 메모)
`raw/{web,youtube,transcripts,articles}/`에 SCHEMA.md 규칙대로 직접 Markdown을 작성한다(자동화 스크립트 없음 — Codex가 그 자리에서 수행).

## 절차 (직접 캡처 경로)
1. 원문을 확보한다(URL fetch 또는 파일 읽기) — **아직 가공하지 않는다**
2. `SCHEMA.md`의 Directory roles 표에서 맞는 하위 디렉토리를 고른다(`raw/web/`, `raw/youtube/` 등은 importer-preserved 경로 규칙이 있으니 기존 파일 예시를 먼저 확인)
3. frontmatter 작성: 최소 title/created/type/source(또는 url)
4. 본문은 원문 그대로 보존한다 — raw는 불변 증거 계층(SCHEMA.md "Raw source integrity"), 요약·해석은 여기서 하지 않는다
5. `sha256` 필드 = frontmatter 종료 `---` 이후 본문 바이트의 SHA-256

## 검증
- 이미 같은 출처가 raw/에 있는가(중복 확인)
- 출처 URL/식별자가 유효한가
- sha256이 정확히 "frontmatter 이후 본문"만을 대상으로 계산됐는가

## 출력
- 새 `raw/<kind>/*.md` 파일 경로
- (Zotero 경로면) `attachment_path`/`attachment_sha256` 포함 여부

## 참고
대량/정기 수집은 자동화(`fetch-inbox.sh` 03:30, `zotero-ingest.py`를 마스터가 수동 실행)가 이미 처리한다. 이 skill은 "지금 이거 하나만" 요청에 쓴다.
