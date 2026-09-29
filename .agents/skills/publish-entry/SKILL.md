---
name: publish-entry
description: 작성된 canonical 페이지를 index.md/log.md에 반영하거나, research 루프의 승인된 클레임을 canonical로 승격한다. 두 경로는 승인 지점이 다르므로 절대 섞지 말 것.
---

# Publish Entry

## 언제 쓰나
- `summarize-note`로 만든 canonical 페이지 초안을 최종 반영할 때
- `research/` 루프에서 나온 가설(hypothesis)을 canonical로 승격할 때

## 이 시스템의 두 갈래 (승인 지점이 다름 — 섞지 말 것)

### (a) 표준 경로 — 사전 승인 게이트 없음
canonical 페이지 작성 직후, **같은 작업 안에서 바로**:
1. `index.md`의 해당 `type` 섹션에 알파벳순 1줄 추가(요약 포함, 총 개수 = 파일시스템 canonical 개수와 일치해야 함)
2. `log.md`에 append(액션·대상·생성/수정/보관한 모든 파일 경로 기록) — **과거 항목은 절대 재작성/삭제하지 않는다**

자동화(`2nd-daily-ingest`, 매일 04:00, `custom/llm-wiki-ains` 스킬)도 정확히 이 원칙으로 동작한다 — **일상적인 daily-ingest 컴파일에는 사전 승인 절차가 없다.** 조건을 만족하면 즉시 canonical을 생성하고 index.md/log.md를 갱신하며, 매일 아침 텔레그램으로 신규 생성 목록을 마스터에게 **사후** 통지한다(확정을 막는 게이트가 아니라 가시성 확보 목적).

### (b) research 루프 경로 — 이 시스템에서 유일하게 실제로 확정을 막는 게이트
```bash
scripts/research-run.sh approve <session-id>              # 마스터 명시 승인 (필수)
python3 scripts/research-promote.py <session-id> --items C1,C3   # 개별 클레임 지정 승격
```
- `claim_type: fact`(기존 출처의 단순 재진술)는 **승격 자체가 거부**된다
- `verification_status: insufficient_evidence`도 거부된다
- `supporting_sources`에 raw 출처가 1건 이상 없으면 거부
- 활성 canonical로의 wikilink 2개 이상을 확보하지 못하면 거부
- 요청 항목 중 하나라도 검증 실패하면 **전체 중단**(부분 반영 없음)
- `raw/` 파일은 이 과정에서 절대 건드리지 않는다

## 절차 (표준 경로)
1. 9필드 frontmatter 완비 확인
2. wikilink 2개 이상 확인
3. `index.md`에 1줄 추가(해당 type 섹션, 알파벳순)
4. `log.md`에 append
5. 해당 섹션이 50개를 넘으면 하위분류, 전체가 200개를 넘으면 주제별 내비게이션 맵 추가 검토

## 절차 (research 경로)
1. `research-run.sh approve <id>`
2. `research-promote.py <id> --items <목록>`
3. 거부되면 사유(fact/insufficient_evidence/근거부족/wikilink부족) 확인 후 원인 해소하고 재시도

## 검증
- `index.md` 총 개수 = 파일시스템 canonical 페이지 개수 일치
- `log.md`에 이번 작업이 누락 없이 기록됐는가
- (research 경로) claim_type/verification_status/wikilink 조건 전부 통과했는가

## 출력
- 갱신된 `index.md`/`log.md`
- (research 경로) 승격된 canonical 파일
