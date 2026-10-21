---
title: "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, ai, uncertainty, safety, bayesian]
sources: [inbox/processed/hw-20261021-ai-uncertainty-mc-dropout-gal-2015.md]
confidence: medium
contested: false
contradictions: []
---

# Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning

- 원문: https://arxiv.org/abs/1506.02142^[inbox/processed/hw-20261021-ai-uncertainty-mc-dropout-gal-2015.md]
- 저자: Yarin Gal, Zoubin Ghahramani^[inbox/processed/hw-20261021-ai-uncertainty-mc-dropout-gal-2015.md]
- 발행: 2015-06-06 (v6 2016-10-04, ICML 2016)^[inbox/processed/hw-20261021-ai-uncertainty-mc-dropout-gal-2015.md]

## 핵심 내용
드롭아웃 학습을 깊은 가우시안 과정의 근사 베이지안 추론으로 해석해, 기존 드롭아웃 네트워크에서 큰 추가 연산이나 정확도 손실 없이 모델 불확실성을 얻는 방법을 제시한다. 회귀·분류(MNIST 예)에서 예측 로그우도와 RMSE 개선을 보고하고 심층 강화학습에도 적용했다.^[inbox/processed/hw-20261021-ai-uncertainty-mc-dropout-gal-2015.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 정량 수치는 초록에 없음.^[inbox/processed/hw-20261021-ai-uncertainty-mc-dropout-gal-2015.md]
- 시사점: 이미 드롭아웃을 쓰는 모델은 재학습 없이 불확실성 추정 가능(원문 서술).^[inbox/processed/hw-20261021-ai-uncertainty-mc-dropout-gal-2015.md]

## 한계·미확인
추론 시 다중 샘플링이 필요한지, 그 지연 비용은 초록에서 미확인.^[inbox/processed/hw-20261021-ai-uncertainty-mc-dropout-gal-2015.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
