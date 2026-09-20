---
title: "Calibrate Once, Fly Any Team — 저충실도 시뮬레이션 기반 드론 군집 훈련"
created: 2026-09-17
updated: 2026-09-17
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, swarm]
sources: [inbox/fetch-2026-09-17-arxiv-calibrate-once-fly-any-team-residual-grounded-low-fidelity-t.md]
confidence: medium
contested: false
contradictions: []
---

# Calibrate Once, Fly Any Team — 저충실도 시뮬레이션 기반 드론 군집 훈련

Maxim Mednikov, Oren Gal(2026-09-15, arXiv)이 제안한 방법으로, 고충실도(HF)
강체물리 시뮬레이션에서의 다중 에이전트 드론 군집 정책 훈련이 팀 규모가
커질수록 접촉 해석 복잡도와 시뮬레이션 내 충돌률이 급증해 비용이 나쁘게
확장되는 문제를 해결한다.^[inbox/fetch-2026-09-17-arxiv-calibrate-once-fly-any-team-residual-grounded-low-fidelity-t.md]

## 핵심 아이디어

- **HF 강화학습 완전 배제**: 공유 분산형 정책을 완전 미분 가능한 JAX 기반
  저충실도(LF) 점질량(point-mass) 시뮬레이터 안에서만 최적화한다.
- **에이전트별 잔차(residual) 보정**: 소규모 배깅 앙상블을 오프라인에서 단
  한 번, HF 시뮬레이터의 짧은 보정 비행(calibration flight)으로 학습한다.
  보정은 드론 1대만 있으면 되므로 데이터 수집 예산이 팀 규모에 비례해
  증가하지 않는다.
- **참조 궤적 생성**: 기존 LF 전용 정책을 롤아웃해 참조 궤적을 만들고,
  훈련 없는 PD 제어기가 HF 시뮬레이터에서 이를 추종한다.

## 결과

- 4가지 협력 드론 임무, 팀 규모 3~18대에 걸쳐 평가.
- 잔차 보정 정책이 보정 없는 LF 베이스라인을 모든 조합에서 능가.
- 처음부터 HF로 훈련한 정책 대비 24개 조합 중 22개에서 우위.
- HF로 파인튜닝한 정책과의 격차는 팀 규모가 커질수록 꾸준히 줄어들며,
  최대 팀 규모에서는 훨씬 적은 연산 비용으로 근접한 성능을 달성하고
  HF 훈련 특유의 높은 충돌률을 완전히 피한다.

## 관련 개념

- [[swarmnxt-aerial-swarm-platform]] — 오픈소스 공중 스웜 SW/HW 플랫폼
- [[agilepe-uav-pursuit-evasion]] — Self-play RL 기반 sim-to-real 전이 유사 접근
