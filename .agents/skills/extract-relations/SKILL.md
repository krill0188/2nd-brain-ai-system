---
name: extract-relations
description: canonical 페이지 작성/수정 후 지식그래프를 최신화하거나, raw/ 원문 뭉치에서 아직 사람이 못 본 관계를 자동 스캔(discovery)한다. canonical 그래프와 discovery 그래프는 별개이니 섞지 말 것.
---

# Extract Relations

## 언제 쓰나
- canonical 페이지를 새로 만들거나 고쳤을 때 → 그래프 최신화
- raw/ 원문에서 아직 아무도 못 본 관계를 훑어보고 싶을 때 → discovery 스캔

## 이 시스템의 두 갈래 (섞지 말 것)

### (a) canonical 그래프 — 사람이 검토한 것만
```bash
bash scripts/update-graph.sh
```
`concepts/`, `entities/`의 frontmatter와 본문 `[[wikilink]]`를 스캔해 `.ua/drone-knowledge-graph.json`을 갱신한다. wikilink 자체가 사람(또는 이 skill 실행자)이 직접 쓴 것이므로 **자동 승격 개념이 없다** — 이미 검증된 레이어.

### (b) discovery 그래프 — LLM 자동 추출, 미검증
```bash
python3 scripts/extract-knowledge-graph.py --source raw/<kind> --limit N --dry-run   # 미리보기
python3 scripts/extract-knowledge-graph.py --source raw/<kind> --limit N              # 실행
```
raw/ 원문에서 LangChain `LLMGraphTransformer`로 개체·관계를 **자동** 추출해 `.ua/discovery-knowledge-graph.json`에만 저장한다. **canonical에 자동 병합되지 않는다.** `.env`에 `NEO4J_PASSWORD`가 설정돼 있으면 로컬 Neo4j에도 동시 기록하지만(2026-08-10 기준 이 프로젝트는 미설정 — JSON 스냅샷만 생성됨), 그 경우에도 discovery 레이어라는 성격은 그대로다.

승격(discovery → canonical)은 **사람이 discovery 그래프(`/graph`의 discovery 레이어, 또는 JSON 직접 확인)를 보고 가치 있다고 판단한 관계만 골라 concepts/entities/*.md에 직접 `[[wikilink]]`로 옮겨 적는** 방식으로만 이뤄진다. 자동 승격 스크립트는 없다.

## 절차 (canonical 경로)
1. canonical 페이지 작성/수정 완료 확인
2. `bash scripts/update-graph.sh` 실행
3. 노드/엣지 수 증가 확인(`.ua/drone-knowledge-graph.json`)

## 절차 (discovery 경로)
1. `--dry-run`으로 추출 결과 미리보기
2. 실제 실행
3. discovery 그래프에서 결과 검토
4. 가치 있는 관계만 골라 사람이 직접 canonical wikilink로 승격

## 검증
- 관계에 근거 문장/출처가 있는가(추측 연결 금지)
- canonical link validity(각 canonical 페이지 아웃바운드 wikilink 2개 이상) 위반이 새로 생기지 않았는가
- discovery 결과를 canonical인 것처럼 인용하지 않았는가

## 출력
- (a) 갱신된 `.ua/drone-knowledge-graph.json`
- (b) 갱신된 `.ua/discovery-knowledge-graph.json`, (승격 시) canonical 페이지의 신규 wikilink
