---
title: "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, ai, uncertainty, safety, robustness]
sources: [inbox/processed/hw-20261021-ai-uncertainty-deep-ensembles-lakshminarayanan-2016.md]
confidence: medium
contested: false
contradictions: []
---

# Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles

- 원문: https://arxiv.org/abs/1612.01474^[inbox/processed/hw-20261021-ai-uncertainty-deep-ensembles-lakshminarayanan-2016.md]
- 저자: Balaji Lakshminarayanan, Alexander Pritzel, Charles Blundell^[inbox/processed/hw-20261021-ai-uncertainty-deep-ensembles-lakshminarayanan-2016.md]
- 발행: 2016-12-05 (v3 2017-11-04, NIPS 2017)^[inbox/processed/hw-20261021-ai-uncertainty-deep-ensembles-lakshminarayanan-2016.md]

## 핵심 내용
베이지안 신경망의 대안으로 deep ensemble을 제안한다. 구현이 간단하고 병렬화가 쉬우며 하이퍼파라미터 튜닝이 거의 필요 없다. 분류·회귀에서 근사 베이지안 신경망과 같거나 나은 보정된 불확실성을 보고하며, 분포 밖(out-of-distribution) 예제에서 더 높은 불확실성을 표현한다. ImageNet에서 확장성도 평가.^[inbox/processed/hw-20261021-ai-uncertainty-deep-ensembles-lakshminarayanan-2016.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 정량 수치는 초록에 없음.^[inbox/processed/hw-20261021-ai-uncertainty-deep-ensembles-lakshminarayanan-2016.md]
- 시사점: 검출·제어 모델의 OOD 입력 감지용 불확실성 신호로 앙상블 사용 가능(다만 추론 비용이 모델 수만큼 증가 - 엣지 비용 수치는 미확인).^[inbox/processed/hw-20261021-ai-uncertainty-deep-ensembles-lakshminarayanan-2016.md]

## 한계·미확인
엣지·지연 비용 수치 없음(미확인). 드론 직접 적용 없음.^[inbox/processed/hw-20261021-ai-uncertainty-deep-ensembles-lakshminarayanan-2016.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
