---
title: "드론 기반 산불 조기탐지 네트워크의 비용 최적화"
created: 2026-09-18
updated: 2026-10-07
type: concept
domain: ops-mission
tags: [drone, ops-mission, wildfire]
sources:
  - inbox/fetch-2026-09-18-arxiv-rapid-drone-based-wildfire-detection-at-a-fraction-of-curren.md
  - raw/papers/_unclassified/rapid-drone-based-wildfire-detection-at-a-fraction-of-current-prevention-spendin.md
confidence: medium
contested: false
contradictions: []
---

# 드론 기반 산불 조기탐지 네트워크의 비용 최적화

Puech·de Moor·Trišović·Bertsimas(2026-09-16, arXiv)는 감시 인프라 배치와 자율
드론 라우팅을 동시에 최적화해 대규모 조기 산불탐지에 필요한 투자 규모를
정량화했다.^[inbox/fetch-2026-09-18-arxiv-rapid-drone-based-wildfire-detection-at-a-fraction-of-curren.md]
2021~2024년 캘리포니아 발화 사건 3,693건을 표본외(out-of-sample) 평가에 사용했다.

## 핵심 결과

- 5년간 1억 달러 예산(연간 약 2,000만 달러 환산)으로 운영되는 최적화된 드론
  네트워크가 화재의 97.3%를 탐지하고, 그중 74%는 발화 후 1시간 이내 탐지.
- 이 예산은 캘리포니아주 연간 산불예방 지출의 약 5%에 불과.
- 현재 기술 비용 기준으로 드론 기반 감시가 고정식 지상 센서보다 비용 효율이
  훨씬 높음.
- 탐지율은 주로 공간 커버리지가 좌우하고, 탐지 속도는 라우팅 전략이 좌우.

## 시사점

인프라 배치와 드론 라우팅을 결합한 정량적 최적화 프레임워크는 지자체·주정부의
산불 대응 예산 배분 의사결정에 직접 활용 가능한 근거를 제공한다.

2026-09-30 Zotero 재인제스트로 동일 arXiv 논문의 durable 레코드가 raw/papers/_unclassified에
추가돼 출처가 이중 확보됐다.^[raw/papers/_unclassified/rapid-drone-based-wildfire-detection-at-a-fraction-of-current-prevention-spendin.md]

## 관련 개념

- [[thermal-drone-wildfire-monitoring]] — 열화상 드론 산불 감시 및 C-UAS 대응
- [[marl-uav-wildfire-exploration]] — 산불 대응 자율 UAV 탐색을 위한 다중 에이전트 강화학습
- [[pso-uav-bushfire-hazard-management]] — 피해지역 커버리지 최대화 PSO 경로계획(예산·배치 최적화와 상보적, 초록 절단)

## 📰 최근 관련 소식
- 윤준병 “2011년부터 확충한 산림청 드론, 111억원 들이고도 산불 최초 탐지 0건” (브릿지경제, Mon, 05 Oc) — https://news.google.com/rss/articles/CBMiWkFVX3lxTE1RbGpYVjNZOUhsbm5yWEhfUVJfQjBIQlB5MjhHU1I0VGlxZmRPV2g3Mi12ZEptUS1meXplcVhrSS11VDRhOGhnYzlUNnVIc21qWjNtV1lEcjJFUQ?oc=5
