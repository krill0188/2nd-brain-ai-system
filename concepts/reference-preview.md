---
title: "Reference preview"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [mpc, tracking, actuator-modeling, fallback-policy, quadrotor-comparison]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Reference preview

Reference preview는 quadrotor 제어기 비교 평가에서 기준 추적 오차를 보정하고 MPC(모델 예측 제어) 성능을 향상시키는 기법을 의미한다. 참조 정보(preview)를 활용함으로써 MPC의 추적 오차가 실질적으로 감소하고, 플라이어웨이(Figure-eight) 과제에서 폴백(fallback) 활동이 제거되는 효과가 확인됐다.

## 개요

Quadrotor controller 비교 연구에서 단일 추적 오차만 보고하는 한, 실제 순위는 컨트롤러 튜닝 노력, 기준 정보(reference information), 액추이터 예측(actuator prediction), 옵티마이저 폴백(optimizer fallback), 명령 타이밍(command timing) 등에 따라 달라질 수 있다. 본 개념은 이러한 요인 중에서 '참조 미리보기(reference preview)'가 제어 성능에 미치는 영향을 다룬다. 연구에 따르면 참조 미리보기를 적용하면 MPC 계열 제어기의 추적 오차가 현저히 감소하며, 특히 복잡한 궤적인 figure-eight(task) 수행 시 폴백 활동이 억제되는 것으로 나타났다. 이는 actuator modeling과 fallback policy의 튜닝이 quadrotor 제어 비교 결과에 미치는 중요성을 보여주는 사례다.

## 핵심 파라미터

아래 표는 연구에서 확인한 주요 findings를 요약한 것이다. 수치는 원문(paper)에 명시된 결과이며, 재확인 필요하다.

| 파라미터 | 내용 |
|----------|------|
| 추적 오차 감소 | Reference preview 적용 시 MPC의 mean-RMSE가 감소 |
| 폴백 활동 | Figure-eight 과제에서 폴백 활동 제거 확인 |
| 급격한 단계 입력 | Abstract 후반부 절단된 문단 언급 (재확인 필요) |

## 활용처

- MPC 기반 quadrotor 제어기 성능 향상
- 기준 추적 오차가 큰 상황에서 예측 성능 보정
- figure-eight 등 주기적/복잡한 궤적 비행에서 폴백 최소화

## 관련 페이지

- [[MPC]] — Model Predictive Control 개념 문서
- [[Actuator modeling]] — 액추이터 모델링 개념 문서
- [[Fallback policy]] — 폴백 정책 개념 문서

## 출처

- -(사용자 재확인 필요) — 위 내용은 2026년 arXiv 발표 논문의 초록(Abstract) 일부를 기반으로 하였으나, 급격한 단계 입력(outcome)에 대한 언급이 절단된 상태임. 원문 전체를 재확인할 것.

## 참고

[[mpc]] [[actuator-modeling]]
