---
title: "Dao, Xuan-Quy"
created: 2026-11-01
updated: 2026-11-01
type: entity
tags: [researcher, quadrotor-control, pid-controller, lqr, sliding-mode-control, mpc, drone-robotics, simulation-study]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Dao, Xuan-Quy

Dao, Xuan-Quy는 2026년 ArXiv에 게시된 "How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study"의 제1저자이다. 본 논문은 50Hz의 고주파 시뮬레이션 환경에서 로터 자이로스코픽 결합, 모터 렉, 포화 현상을 고려한 공통 비선형식물 위상에서 6가지 유형의 쿼드레이터 PID, Hover LQR, BL-SMC, LMPC-F, Preview-enabled LMPC-F, $SO(3)$ 컨트롤러 간의 성능 비교를 수행하였다. 저자는 12가지 매칭 튜닝 후보군과 48-cell MPC 팩토리얼 설계를 통해 컨트롤러 순위를 재평가하였으며, BL-SMC가 고정 베이스라인에서 최하위에서 1위로 도약하는 결과를 도출하였다. 특히 레퍼런스 프리뷰(reference preview) 기능은 MPC의 트래킹 오차를 크게 저감시키며, 피겨-8 궤적에서는 폴백(fallback) 활동을 제거하는 효과를 보였다. 또한 확인 연구(confirmation study)를 통해 50개의 새로운 경우에 대해 12, 24, 48 후보 튜닝 예산 하에서 순위가 재현되었으며, 48 후보 예산에서는 순위가 변화하지 않음을 확인하였다.

## 핵심 파라미터

| 항목 | 내용 |
|------|------|
| 성명 | Dao, Xuan-Quy |
| 소속 | 제1저자 (제1저자로서 제1저자 명단에 포함) |
| 논문 제목 | How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study |
| 발표 연도 | 2026 |
| DOI | 10.48550/arXiv.2610.35165 |
| 주요 연구 주제 | 쿼드레이터 컨트롤러 비교, PID, LQR, 슬라이딩 모드 제어(SMC), MPC, 레퍼런스 프리뷰, 폴백 정책 |
| 연구 환경 | 50Hz 비선형 시뮬레이션 플랜트 (로터 자이로스코픽 결합, 모터 렉, 서보 포화 포함) |
| 주요 발견 | 12 후보 튜닝 프로토콜 변경으로 BL-SMC가 최하위 → 1위 도약; 레퍼런스 프리뷰가 MPC 트래킹 오차 감소 및 폴백 억제 확인 |

## 활용처

- 드론 비행 제어 알고리즘 비교 및 평가 연구
- MPC 기반 컨트롤러 설계에서 튜닝 예산 및 레퍼런스 프리뷰 효과 검증
- 자율 비행 시뮬레이션 연구에서의 컨트롤러 랭킹 기준 수립

## 관련 페이지

- [[quadrotor-controller-comparison]] — 다양한 쿼드레이터 컨트롤러의 시뮬레이션 비교 연구 모음
- [[mpc-fallback-policy]] — MPC 폴백 정책에 대한 연구 및 구현 사례

## 출처

- (사용자 재확인 필요)原文에 명시된 대로 ArXiv preprint (2026) 참조

---

## 참고

[[mpc]] [[abz-innovation]]
