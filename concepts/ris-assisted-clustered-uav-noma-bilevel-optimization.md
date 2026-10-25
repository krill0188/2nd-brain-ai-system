---
title: "RIS 보조 군집형 UAV-NOMA 망의 outage 분석과 이중 최적화"
created: 2026-10-24
updated: 2026-10-24
type: concept
domain: comms-protocol
tags: [drone, datalink]
sources: [raw/papers/_unclassified/outage-analysis-and-bilevel-resource-optimization-in-ris-assisted-clustered-uav-.md]
confidence: low
contested: false
contradictions: []
---

# RIS 보조 군집형 UAV-NOMA 망의 outage 분석과 이중 최적화

Ghazikor 외, arXiv 2610.30410 (2026-10-21). **초록 기준**이다.

## 요지
- 문제: UAV 수가 늘면 기존 NOMA는 확장이 어렵다. 기지국이 분할 가능한 RIS를 이용해 여러 UAV 그룹을 서빙하는 클러스터 기반 하향링크 구조를 제안한다.^[raw/papers/_unclassified/outage-analysis-and-bilevel-resource-optimization-in-ris-assisted-clustered-uav-.md]
- 분석: 직접·RIS 간접·복합 링크를 구분하고, Nakagami-m 및 이중 Nakagami-m 페이딩과 불완전 SIC 하에서 수신 SNR·outage 해석 모델을 유도한다.^[raw/papers/_unclassified/outage-analysis-and-bilevel-resource-optimization-in-ris-assisted-clustered-uav-.md]
- 클러스터링: 공간·채널 특징으로 UAV를 묶는 greedy RIS-aware(GRIS) 방식.^[raw/papers/_unclassified/outage-analysis-and-bilevel-resource-optimization-in-ris-assisted-clustered-uav-.md]
- 최적화: 외부 문제는 클러스터 평균 처리량 최대화(기지국 전력 배분), 내부 문제는 클러스터 내 최악 UAV의 outage 확률 최소화(NOMA 전력 계수, RIS 소자 할당). 외부 solver(IOS)와 내부 solver(I2S, 격자 탐색 GPS + 신뢰도 기반 RIS 소자 재할당)의 2단계 반복으로 푼다.^[raw/papers/_unclassified/outage-analysis-and-bilevel-resource-optimization-in-ris-assisted-clustered-uav-.md]
- 결과: 수치 실험에서 GRIS 클러스터링의 효과와 효율-신뢰성 트레이드오프를 보이고, 기준선 비교·ablation에서 joint 최적화의 중요성을 주장한다.^[raw/papers/_unclassified/outage-analysis-and-bilevel-resource-optimization-in-ris-assisted-clustered-uav-.md]

## 관련
[[uav-irs-dqn-power-allocation-6g]], [[ris-secure-uav-communications]], [[fluid-antenna-system]] 참조.

## 한계
수치 결과와 시뮬레이션 파라미터는 초록에 없다.

## 📰 최근 관련 소식
- Outage Analysis and Bilevel Resource Optimization in RIS-Assisted Clustered UAV-NOMA Networks (arxiv.org, 2026-10-21) — http://arxiv.org/abs/2610.30410v1
