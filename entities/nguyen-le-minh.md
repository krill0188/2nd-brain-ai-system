---
title: "Nguyen, Le-Minh"
created: 2026-11-01
updated: 2026-11-01
type: entity
tags: [person, quadrotor, controller-comparison, pid-controller, lqr, sliding-mode-control, mpc, so3-controller, actuator-modeling]
sources: [dao_2026_quadrotor_controller_comparison]
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Nguyen, Le-Minh

Nguyen, Le-Minh는 2026년 Dao, Xuan-Quy와 Le, Ngoc-Bich가 공동으로 작성한 'How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study' 논문의 제1 저자이다. 이 연구는 다양한 드론 컨트롤러의 비교 평가에 있어 튜닝 노력, 레퍼런스 정보, 액추에이터 예측, 옵티마이저 폴백, 명령 타이밍 등의 요인이 순위에 어떻게 영향을 미치는지를 정량적으로 분석한 것이 특징이다.

## 개요

본 논문은 쿼드로서(Quadrotor) 컨트롤러 비교 연구에서 흔히 단일 추적 오차만 보고하지만, 실제 순위는 튜닝 노력, 레퍼런스 정보, 액추에이터 예측, 폴백 정책, 명령 타이밍 등 다양한 요인에 따라 달라질 수 있음을 보여준다. 연구진은 캐스케이드 PID, �버 LQR, 경계층 슬라이딩 모드 제어(BL-SMC), LQR 폴백이 있는 선형 MPC(LMPC-F), 프리뷰 기능을 갖춘 LMPC-F, 그리고 기하학적 $SO(3)$ 컨트롤러 등 6가지 컨트롤러를 동일한 비선형 플랜트(로터 지로스코픽 커플링, 모터 레그, 위상 포화 포함)에서 평가했다. 주요 연구(556 에피소드, 50Hz)와 확인 연구(1462 에피소드, 50개의 새로운 실현)로 진행되었으며, 12개 후보 튜닝 프로토콜이 기준 설정값으로 얻은 평균-RMSE 순위를 변화시켰으며, BL-SMC를 마지막에서 처음으로 이동시켰다. 이러한 순위는 신규 실현에서도 재현되었으며, 48개 후보 예산은 순위를 변화시키지 않았다. 레퍼런스 프리뷰는 MPC 추적 오차를 substantially(현저히) 감소시키고, figure-eight 태스크에서는 폴백 활동을 제거했다. 급격한 스텝 입력 시에 대한 추가적인 결과가 논문에 언급되나, 원문 발췌 범위를 넘어서는 세부 사항은 재확인 필요하다.

## 핵심 파라미터

| 파라미터 | 내용 |
|---|---|
| 논문 제목 | How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study |
| 연도 | 2026 |
| DOI | 10.48550/arXiv.2610.35165 |
| 평가 컨트롤러 | 캐스케이드 PID, �버 LQR, BL-SMP, LMPC-F, 프리뷰-enabled LMPC-F, $SO(3)$ 컨트롤러 |
| 연구 규모 | 주요 연구 556 에피소드, 확인 연구 1462 에피소드 |
| 튜닝 후보 | 12개, 24개, 48개 бюдже트 |

## 활용처

본 연구는 드론 자율 비행 및 컨트롤러 설계 분야에서, 특정 컨트롤러가 다양한 조건에서 우수한 성능을 보일 뿐 아니라, 튜닝 및 운영 조건에 따라 순위가 어떻게 변하는지를 이해하는 데 기여한다. 특히 MPC 기반 컨트롤러의 프리뷰 기능과 폴백 정책이 추적 성능과 안정성에 미치는 영향을 평가하는 데 유용하다.

## 관련 페이지

- [[quadrotor-controller-comparison]] — 다양한 쿼드로서 컨트롤러의 비교 및 평가에 관한 연구
- [[lqr-controller]] — 쿼드로서를 위한 선형 quadratic regulator 기반 컨트롤러
- [[mpc-controller]] — 모델 예측 제어 기반 드론 컨트롤러

## 출처

- (사용자 재확인 필요) original paper: dao, xuan-quy; nguyen, le-minh; le, ngoc-bich (2026). "How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study." arXiv:2610.35165.

## 참고

[[quadrotor]] [[mpc]]
