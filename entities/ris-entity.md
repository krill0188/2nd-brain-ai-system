---
title: "RIS"
created: 2026-10-24
updated: 2026-10-24
type: entity
tags: [ris, uav-noma, downlink-composites, bilevel-optimization, outage-performance]
sources: ["arXiv:2610.30410"]
confidence: medium
contradictions: []
domain: comms-protocol
contested: false
---

# RIS

RIS(Reflecting Intelligent Surface)는 NOMA 기반 UAV downlink 통신에서 BS가 다수의 UAV 그룹을 서비스하는 cluster-based UAV-NOMA framework를 구축하는 데 사용되는 partitionable(RIS) 요소입니다. 직접 링크, RIS-only 간접 링크, 그리고 복합 링크를 고려하여 Nakagami-$m$ 및 double Nakagami-$m$ 페이딩 환경하에서 imperfect SIC를 반영한 수신 SNR 및 outage 성능을 분석합니다. scalable transmission을 위해 UAV를 spatial 및 channel-related features에 기반해 grouping하는 greedy RIS-aware (GRIS) clustering 방법이 도입되었습니다.

## 개요

본 문서는 RIS를 활용한 UAV-NOMA 시스템의 outage 성능을 분석하고, cluster별 효율성과 신뢰성을 균형 있게 최적화하는 bilevel optimization 문제를 정의합니다. RIS는 UAV群간 간섭 관측과 전력 코efficient 할당을 가능하게 하는 수동 반사 요소를 의미하며, UAV와 BS가 RIS를 사용하여 통신 범위를 확장하고 품질을 향상시키는 방식으로 운영됩니다. 특히 GRIS clustering method에 따라 UAV가 그룹화되며, 각 cluster 내에서는 outer efficiency problem(평균 throughput 최대화)과 inner reliability problem(최악의 UAV outage 확률 최소화)이 반복적으로 수행됩니다.

## 핵심 파라미터

| 파라미터 | 내용 |
|----------|------|
| Fading Model | Nakagami-$m$, Double Nakagami-$m$ |
| SIC Condition | Imperfect SIC |
| Clustering Method | Greedy RIS-aware (GRIS) |
| Optimization Structure | Two-level iterative framework |
| Link Types | Direct, RIS-only indirect, Composite |

## 활용처

- UAV 통신 군에서 기지국 coverage 확대 및 품질 향상
- NOMA 스케일링 한계 극복을 위한 cluster 기반 트래픽 처리
- RIS 기반 무선 환경 재구성을 통한 outage 확률 최소화

## 관련 페이지

- [[Nakagami_m_fading]] — RIS가 동작하는 페이딩 모델
- [[Double_Nakagami_m_fading]] — RIS 환경에서 고려되는 이중 페이딩 모델
- [[UAV-NOMA]] — RIS가 적용되는 NOMA 기반 UAV 네트워크
- [[BS]] — RIS와 연계된 기지국
- [[GRIS]] — RIS 기반 클러스터링 알고리즘

## 출처

- (사용자 재확인 필요)

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
