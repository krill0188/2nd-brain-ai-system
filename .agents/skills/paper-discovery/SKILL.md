---
name: paper-discovery
description: 논문·기사 후보를 수집해 inbox/·raw/에 증거로 쌓는다(Daily = Evidence 1단계). 새 논문을 찾아 raw에 넣고 싶을 때, 또는 수집 파이프라인 상태를 점검할 때 사용.
---

# Paper Discovery

## 언제 쓰나
- "오늘 새 논문/기사 뭐 들어왔나", "수집 상태 점검" 요청
- 자동 경로: `scripts/knowledge-pipeline.py`의 `Generate:fetch` 단계(`scripts/fetch-inbox.sh`, 매일 07:30) — arXiv 8도메인·KCI·Crossref·YouTube·Zotero. 이 skill은 그 자동 경로를 **대체하지 않고** 수동 보강/점검용이다.

## 절차
1. `.ua/pipeline-result.json`, `.ua/logs/knowledge-pipeline.log` 마지막 실행 결과 확인 (fetch exit_code)
2. 수동 수집이 필요하면 `bash scripts/fetch-inbox.sh` 실행 (공유 락 필요 시 `python3 scripts/with-pipeline-lock.py -- bash scripts/fetch-inbox.sh`). arXiv는 요청 간 sleep 3 유지
3. 개별 논문은 `scripts/zotero-ingest.py`/inbox 레코드로 등록. **raw/는 불변 증거** — 기존 raw 파일을 수정하지 않는다
4. 중복 판정: DOI/arXiv id/제목 정규화로 기존 raw·inbox와 대조, 중복이면 건너뜀

## 검증
- 새 파일 frontmatter에 title/source URL/수집일이 있는가
- 지어낸 메타데이터(저자·연도·DOI)가 없는가 — 확인 불가면 비워둔다

## 출력
- `inbox/`·`raw/papers/` 신규 파일 목록 + "수집 N개, 중복 N개, 실패 N개" 한 줄
- 다음 단계는 `paper-ingest`
