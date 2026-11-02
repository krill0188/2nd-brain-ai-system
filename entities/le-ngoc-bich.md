---
title: "Le, Ngoc-Bich"
created: 2026-11-01
updated: 2026-11-01
type: entity
tags: [author, quadrotor, control-theory, mpc, pid, lqr, sliding-mode]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Le, Ngoc-Bich

Le, Ngoc-Bich는 Xuan-Quy Dao, Le-Minh Nguyen와 공동 저자로서 2026년 발표된 "How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study" 논문의 제3 저자이다. 본 연구는 쿼드롯터 컨트롤러 비교 연구에서 튜닝 노력, 레퍼런스 정보, 액추에이터 예측, 최적화 폴백, 명령 타이밍 등이 순위에 미치는 영향을 정량화한 것이 특징이다.

---

## 개요

본 연구는 cascade PID, hover LQR, boundary-layer sliding-mode control (BL-SMC), linear MPC with LQR fallback (LMPC-F), preview-enabled LMPC-F, 및 geometric $SO(3)$ 컨트롤러 등 6종의 쿼드롯터 컨트롤러를 하나의 비선형 플랜트에서 비교 검증한다. 이 플랜트는 로터 기코스코픽 커플링, 모터 랙, 포화 현상을 포함한다. 연구진은 556회 에피소드(50 Hz)의 주요 연구와 1462회 에피소드의 확인 연구를 통해, 매칭된 12 후보 튜닝 프로토콜이 고정 베이스라인 설정에서 얻은 평균-RMSE 순위를 변화시켰음을 확인했다. 이에 따라 BL-SMC가 최하위에서 최상으로 상승했으며, 새로운 순위는 신규 실현에서 재현되었다. 또한 48 후보 예산은 이러한 순위를 고정시켰다. 레퍼런스 프리뷰는 MPC 트래킹 오차를 현저히 감소시키고, Figure-8 과제에서는 폴백 활동을 제거했다. 급격한 스텝 입력에 대한 결과는 논문 본문에서 추가 확인이 필요하다.

## 핵심 파라미터

| 항목 | 내용 |
|------|------|
| 주요 컨트롤러 비교 | cascade PID, hover LQR, BL-SMC, LMPC-F, preview-enabled LMPC-F, geometric $SO(3)$ |
| 플랜트 특성 | 로터 기코스코픽 커플링, 모터 랙, 포화 현상 포함 |
| 에피소드 수 | 주요 연구 556회, 확인 연구 1462회 |
| 제어 주파수 | 50 Hz |
| 튜닝 후보 수 | 12, 24, 48 후보 예산 |

## 활용처

- 쿼드롯터 컨트롤러 성능 비교 및 순위 결정에 관한 연구
- MPC 기반 컨트롤러의 레퍼런스 프리뷰 및 폴백 정책 최적화
- 드론 제어 시스템의 튜닝 효율성과 robustness 분석

## 출처

- (사용자 재확인 필요)

## 참고

[[quadrotor]] [[mpc]]
