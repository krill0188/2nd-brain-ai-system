---
title: "Low-Altitude UAV Tracking via Sensing-Assisted Predictive Beamforming"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: rf-datalink-engineering
tags: [drone, isac, tracking, predictive-beamforming]
sources: [inbox/processed/hw-20261021-conv-isac-predictive-beamforming-jiang-2025.md]
confidence: medium
contested: false
contradictions: []
---

# Low-Altitude UAV Tracking via Sensing-Assisted Predictive Beamforming

- 원문: arXiv:2509.12698^[inbox/processed/hw-20261021-conv-isac-predictive-beamforming-jiang-2025.md]
- 저자: Yifan Jiang, Qingqing Wu, Hongxun Hui, Wen Chen, Derrick Wing Kwan Ng^[inbox/processed/hw-20261021-conv-isac-predictive-beamforming-jiang-2025.md]
- 발행: 2025-09-16 (v2 2026-06-30)^[inbox/processed/hw-20261021-conv-isac-predictive-beamforming-jiang-2025.md]

## 핵심 내용
센싱으로 드론 위치를 예측하는 예측 빔포밍이 셀룰러 연결 UAV의 통신 신뢰성에 미치는 영향을 다룬다. 예측 궤적, 센싱 시간 비율, 목표 신호 품질을 공동 최적화해 슬롯별 outage capacity를 최대화한다. 근사 outage 확률식을 유도하고 이분법+SCA 알고리즘과 저복잡도 교대 최적화 알고리즘으로 푼다. 근사가 정확하고 기준선을 능가하며, 최적 예측 궤적은 기지국 안테나 어레이와 거의 평행하되 0이 아닌 거리를 유지(경로손실과 빔 커버리지 균형)한다고 보고.^[inbox/processed/hw-20261021-conv-isac-predictive-beamforming-jiang-2025.md]
원문 인용: "maximize the outage capacity at each time slot"^[inbox/processed/hw-20261021-conv-isac-predictive-beamforming-jiang-2025.md]

## 설계·운용에 쓸 수 있는 지침
- 센싱 시간 비율을 늘리면 예측 정확도와 통신 시간이 상충하므로 변수로 함께 최적화.^[inbox/processed/hw-20261021-conv-isac-predictive-beamforming-jiang-2025.md]

## 한계·미확인
- 초록에 수치 없음.^[inbox/processed/hw-20261021-conv-isac-predictive-beamforming-jiang-2025.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[uav-isac-cross-region]]
