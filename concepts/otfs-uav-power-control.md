---
title: "OTFS 기반 지연 SINR 피드백 UAV 전력 제어"
created: 2026-09-23
updated: 2026-09-30
type: concept
domain: comms-protocol
tags: [drone, datalink]
sources:
  - inbox/processed/fetch-2026-09-23-arxiv-otfs-enabled-delayed-sinr-feedback-power-control-for-reliabl.md
  - raw/papers/_unclassified/otfs-enabled-delayed-sinr-feedback-power-control-for-reliable-and-fair-high-mobi.md
confidence: medium
contested: false
contradictions: []
---

## Definition

고기동 UAV 통신을 위한 OTFS(Orthogonal Time Frequency Space) 기반 전력 제어 프레임워크. 순시 채널상태정보(CSI) 대신 **지연된 SINR 피드백만으로** 송신 전력 벡터를 갱신하는 컨트롤러로, 신뢰성·공정성·스펙트럼 효율을 각각 정규화해 결합하는 예측-평활-투영(prediction-smoothing-projection) 규칙을 사용한다.^[inbox/processed/fetch-2026-09-23-arxiv-otfs-enabled-delayed-sinr-feedback-power-control-for-reliabl.md]

## Why It Matters

빠르게 페이딩하는 공중 링크에서는 순시 CSI 확보가 비현실적이므로, 지연 피드백만으로 동작하는 제어기가 실용적 대안이다. 논문 시뮬레이션에 따르면 70 m/s에서 OTFS의 프레임당 유효 SINR 변화가 OFDM 대비 37.8% 작고, 40 m/s에서는 균등 전력 배분 대비 평균 최소 SINR이 1.21 dB 상승하며 Jain 공정성 지수가 0.833→0.970으로 개선된다(합-속도 손실 24.6%).^[inbox/processed/fetch-2026-09-23-arxiv-otfs-enabled-delayed-sinr-feedback-power-control-for-reliabl.md] OTFS의 OFDM 대비 우위는 10 m/s에서 0.18 dB, 90 m/s에서 0.81 dB로 이동속도가 커질수록 확대된다.

## Key Properties

- 지연 SINR 피드백만 사용(순시 CSI 불필요) — 실제 공중 링크 제약에 부합
- 신뢰성·공정성·스펙트럼효율 3요소를 설계자가 가중치로 직접 제어
- 균일 선형 배열(ULA) 기지국이 다수 UAV를 공통 OTFS 프레임으로 서빙
- 고기동(최대 90 m/s)에서 OFDM 대비 우위 확대

2026-09-30 Zotero 재인제스트로 동일 arXiv 논문의 durable 레코드(PDF 첨부 포함)가
raw/papers/_unclassified에 추가돼 출처가 이중 확보됐다.^[raw/papers/_unclassified/otfs-enabled-delayed-sinr-feedback-power-control-for-reliable-and-fair-high-mobi.md]

## Related

- [[datalink-communication]]
- [[active-sensing-uav-communication]]
