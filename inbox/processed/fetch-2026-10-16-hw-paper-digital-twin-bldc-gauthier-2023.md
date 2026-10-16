---
title: "Digital Twin of a DC Brushless Electric Motor-Propeller System with Application to Drone Dynamics"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://arxiv.org/abs/2312.09981
authors: "D. J. Gauthier, N. Biederman, B. Gyovai, J. P. Wilhelm"
published: "2023-12-15"
tags: [drone, hardware, paper, BLDC, motor, propeller, digital-twin, ESC, thrust-model]
---

# Digital Twin of a DC Brushless Electric Motor-Propeller System with Application to Drone Dynamics

## 핵심 내용 (방법·결과)

BLDC 모터와 프로펠러 조합의 **정지 추력(static thrust)을 예측하는 디지털 트윈** 모델을 제시했다. 역기전력(back-EMF), 프로펠러 드래그, 권선 인덕턴스·저항에 의한 응답 지연을 모두 포함하며, Group 1 드론(소형) 두 가지 구성으로 실험 검증:
- KDE Direct 모터 + 945 프로펠러 + Holybro ESC
- AIR 2216/880 KV 모터 + 1045 프로펠러

**핵심 결과:**
- 정상상태 및 과도 응답 모두 기존 선형화 모델과 **상당히 다른 특성** 확인.
- sensorless ESC 환경에서 추력은 PWM 신호의 비선형 함수 (특히 저 PWM 영역에서 현저).
- 기존 교과서적 BLDC 모델과 비교하여 더 높은 정확도 달성.

## 설계에 쓸 수 있는 지침

- **선형 추력 모델(T ∝ ω²)은 실제 ESC 환경에서 오차 발생** → 특히 저속·저추력 영역에서 비선형 모델 필요.
- 모터-프로펠러 매칭 시 PWM 전 영역에서 실험 교정 필요; 호버링 포인트에서만 검증하면 부족.
- 인덕턴스·저항 파라미터는 드론 동역학 시뮬레이션의 정확도에 직접 영향 → 제조사 데이터시트값 그대로 사용 주의.

## 한계·미확인 항목

- 정량 추력 오차(%) 및 측정 조건: 미확인 (초록에서 수치 미기재, 본문 확인 필요).
- 동적 비행 조건(전진 비행, 기류)에서의 검증 여부: 미확인.
- 모터 열 모델은 포함되지 않음.
