---
title: "트럭 허브 드론 VRP 분지-가격-절단 정확해법"
created: 2026-10-15
updated: 2026-10-15
type: concept
domain: ops-mission
tags: [drone, ops-mission]
sources: [inbox/processed/fetch-2026-10-15-arxiv-an-exact-branch-price-and-cut-algorithm-for-a-truck-as-hub-v.md, raw/papers/_unclassified/an-exact-branch-price-and-cut-algorithm-for-a-truck-as-hub-vehicle-routing-probl.md]
confidence: medium
contested: false
contradictions: []
---

# 트럭 허브 드론 VRP 분지-가격-절단 정확해법

arXiv 2610.15016 (Pu 외, 2026-10-10) 초록 기준. 원문 파일의 도메인 라벨은 comms-protocol이었지만 내용은 물류 운용 최적화라 ops-mission으로 분류했다.

## 문제 정의

농촌 라스트마일 배송 문제다. 여러 트럭이 각자 전용 드론 편대를 싣고, 드론의 이륙·회수는 사전 지정된 수동 동기화 패드에서만 가능하다. 트럭은 패드에서 이동 허브가 되어 드론 여러 대를 동시에 띄울 수 있고, 모든 드론이 돌아올 때까지 기다린 뒤 이동한다.^[inbox/processed/fetch-2026-10-15-arxiv-an-exact-branch-price-and-cut-algorithm-for-a-truck-as-hub-v.md]^[raw/papers/_unclassified/an-exact-branch-price-and-cut-algorithm-for-a-truck-as-hub-vehicle-routing-probl.md]

## 방법과 결과

- 고객 지연, 트럭 복귀 시간, 운용 비용을 함께 다루는 혼합정수 2차계획(MIQP) 모형.
- 트럭-드론 네트워크를 변환해 각 실현 가능 경로를 단일 경로로 표현하고, 전용 pricing·cutting·branching·병렬 계산을 갖춘 branch-price-and-cut을 개발했다.
- 대규모 사례 대부분에서 최적성을 증명했고 나머지는 최적성 갭 4% 이하다. 컴팩트 정식화에 Gurobi를 직접 적용하면 대규모 사례 전부가 1,800초 제한에 걸렸다.
- 민감도 분석: 드론 운용비와 관리 우선순위가 드론 활용도와 고객 지연에 크게 영향을 준다.^[inbox/processed/fetch-2026-10-15-arxiv-an-exact-branch-price-and-cut-algorithm-for-a-truck-as-hub-v.md]^[raw/papers/_unclassified/an-exact-branch-price-and-cut-algorithm-for-a-truck-as-hub-vehicle-routing-probl.md]

관련: [[kci-drone-human-hybrid-delivery-milp]], [[drone-delivery-news]].
