---
title: "MPC"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [mpc, quadrotor, optimal-control, actuator-modeling, reference-preview]
sources: [http://arxiv.org/abs/2610.35165v1]
confidence: medium
contradictions: []
domain: navigation-gnss-denied
---

# MPC

Model Predictive Control (MPC)는 quadrotor의 추적 성능을 최적화하기 위해 시계열 상에서 제어 입력을 최적화하는 최적 제어 기법입니다. 기존 PID나 LQR 방식과 달리, 현재 시점의 제어 입력뿐만 아니라 미래의 참조 신호를 예측하여 제어하므로, 레퍼런스 프리뷰(Reference preview)와 actuator modeling 등을 효과적으로 활용할 수 있습니다.

## 개요

Quadrotor controller 비교 연구에서 MPC는 단순한 추적 오차 외에 튜닝 노력, 레퍼런스 정보, 액추레이터 예측, 옵티마이저 폴백, 명령 타이밍 등 다양한 요인에 따라 성능이 크게 달라지는 것으로 나타났습니다. 연구에서는 cascade PID, hover LQR, 경계층 슬라이딩 모드 제어(BL-SMC), LQR 폴백이 있는 선형 MPC(LMPC-F), 레퍼런스 프리뷰가 가능한 LMPC-F, 그리고 기하학적 $SO(3)$ 컨트롤러를 비교 대상으로 했습니다. 특히 48개의 factorial MPC 설정과 12~48 후보 튜닝 버퍼를 사용한 대규모 시뮬레이션을 통해, MPC의 성능이 레퍼런스 프리뷰와 액추레이터 모델링의 품질에 크게 의존함을 확인했습니다.

## 핵심 파라미터

| 파라미터 | 설명 |
|----------|------|
| Controller Type | Model Predictive Control (최적제어) |
| Fallback Mechanism | LQR 폴백 포함 여부 (LMPC-F) |
| Reference Preview | 미래 레퍼런스 정보 활용 여부 |
| Actuator Modeling | 로터 기구적 커플링, 모터 랙, 포화 고려 모델 |
| Candidate Tuning Budget | 12, 24, 48 후보 튜닝 조합 |

## 활용처

- **고정익 및 멀티콥터 궤도 추적**: figure-eight 태스크 등 정밀한 비행 궤적 수행
- **이동 중 레퍼런스 변화**: 급격한 스텝 커맨드에도 robust하게 반응
- **액추레이터 제한 고려**: 모터 랙과 포화 현상을 모델링하여 실제 비행에 가까운 시뮬레이션 가능

## 관련 페이지

- [[Actuator Modeling]] — MPC에서 액추레이터 특성을 모델링하는 기법
- [[Reference Preview]] — MPC에 미래 레퍼런스 정보를 제공하는 기법
- [[LMPC-F]] — LQR 폴백이 있는 선형 MPC 변형

## 출처

- (사용자 재확인 필요) 원문: http://arxiv.org/abs/2610.35165v1 (2026)

---
