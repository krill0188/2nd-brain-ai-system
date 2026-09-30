---
name: research-idea-generator
description: research/gaps/ 원장과 위키 근거로 연구 아이디어를 생성하고, 각 아이디어에 Novelty Ledger·Evidence Status를 붙여 research/ideas/idea-NNN.md로 관리한다(Monthly). 기존 아이디어의 novelty 재평가에도 사용.
---

# Research Idea Generator

아이디어는 **살아 있는 객체**다: 생성 → 새 근거로 재평가 → 강화/수정/폐기. staging이며 canonical 승격은 마스터 수동.

## 절차
1. **기존 idea 재평가 먼저**: `research/ideas/idea-*.md` 각각에 대해 지난 달 이후 새 raw/canonical 근거와 비교 → Evidence Status에 월 단위 항목 추가, Novelty Ledger의 "Threat to novelty" 확인, novelty confidence 조정(하락 시 수정/폐기 권고)
2. `research/gaps/research-gaps.md`의 open gap과 최신 synthesis를 읽고 신규 idea 최대 3개 생성(gap 1개 이상 인용 필수)
3. 각 idea 파일 `research/ideas/idea-NNN.md` (번호 재사용 금지), status는 `draft`로 시작:

```
---
id: idea-NNN
title: ...
status: draft            # draft|active|weakened|abandoned
created: YYYY-MM-DD
updated: YYYY-MM-DD
gaps: [GAP-012]
sources: [raw/...]
novelty_confidence: 0.00
---
> ⚠ 미검증 연구 아이디어 — canonical 아님
## Hypothesis
## Why now (근거 요약, [[wikilink]] + ^[raw/...])
## Novelty Ledger
### Known Similar Work      (위키에 있는 것만 [[link]])
### What already exists
### What appears missing
### Potential novelty
### Threat to novelty      (새 논문이 나오면 재평가할 조건)
### Novelty confidence
## Evidence Status
YYYY-MM  근거 N편 → 강화/약화/유지
## Minimal validation plan
```

## 규칙
- Known Similar Work를 지어내지 않는다 — 위키/raw에서 확인된 것만. 검색 불충분하면 novelty_confidence를 낮게 두고 그 이유를 적는다
- index.md/log.md 수정 금지, canonical 수정 금지

## 출력
- 마지막 줄: "idea 신규 a / 재평가 b (강화 x / 약화 y / 폐기권고 z)"
