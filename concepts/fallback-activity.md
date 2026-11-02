---
title: "fallback activity"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [control-theory, mpc, pid, quadrotor, simulation-study]
sources: []
confidence: medium
contradictions: []
domain: navigation-gnss-denied
---

# fallback activity

Quadrotor controller 비교 연구에서, 보정되지 않은 추적 오차 외에 컨트롤러 동작에 영향을 미치는 추가적인 제어 활동을 의미한다. 특히 MPC(모델 예측 제어) 기반 컨트롤러에서 참조(preview) 정보가 부족하거나 최적화 솔루션이 실패했을 때, 대체 제어 정책(예: LQR 폴백)으로 전환되는 현상을 설명한다.

## 개요

컨트롤러 비교 연구에서 단일 추적 오차 값 외에도, 튜닝 노력, 레퍼런스 정보, 액추에이터 예측, 최적화 폴백, 그리고 명령 타이밍 등의 요인이 등급 순위에 영향을 미친다는 사실이 보고된다. 연구에 따르면 기준선 설정과는 다른 튜닝 프로토콜을 적용할 경우, 슬라이딩 모드 제어(SMC)가 마지막으로 위치하던 순위가 첫 번째로 이동하는 등 순위의 변화가 발생한다. 특히 레퍼런스 프리뷰(reference preview)가 적용될 경우 MPC의 추적 오차가 현저히 감소하며, figure-eight 작업의 경우 폴백 활동이 완전히 제거되는 것으로 나타났다. 반면突兀한 스텝 입력(step input) 상황에서는 폴백 활동의존적인 결과가 달라질 수 있다.

## 핵심 파라미터

- **참여 컨트롤러**: cascade PID, hover LQR, boundary-layer sliding-mode control (BL-SMC), linear MPC with LQR fallback (LMPC-F), preview-enabled LMPC-F, geometric $SO(3)$ controller
- **폴백 트리거 조건**: 최적화 솔루션 실패, 레퍼런스 정보 부족, actuator prediction 오차
- **관찰 효과**: 48-candidate 튜닝 예산은 컨트롤러 순위를 변경하지 않는 안정성을 보임

## 활용처

- Quadrotor 제어 알고리즘 비교 및 성능 평가 시, 단순한 RMSE 값 외에도 고려해야 할 부가 요인
- MPC 기반 자율 비행 시스템에서 폴백 정책의 작동 조건 및 영향도 분석
- 고신뢰도 비행을 위한 폴백 활동 최소화 전략 수립

## 관련 페이지

- [[LMPC-F]] — linear MPC with LQR fallback 구현체
- [[reference preview]] — fallback 활동을 감소시키는 레퍼런스 프리뷰 기법

## 출처

- (사용자 재확인 필요)
