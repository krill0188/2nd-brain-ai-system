---
title: "쿼드로터 RL 제어의 학습 바람장 충실도 비교 (PPO vs PID/SE(3))"
created: 2026-10-08
updated: 2026-10-08
type: concept
domain: flight-control
tags: [drone, drone-ai, drone-sw, research]
sources: [inbox/processed/fetch-2026-10-08-arxiv-statistical-turbulence-and-high-fidelity-disturbance-fields-.md]
confidence: low
contested: false
contradictions: []
---

# 학습 바람장 충실도가 RL 쿼드로터 강건성에 미치는 영향

Xun Huang의 arXiv 논문(2026-09-09 게재). 강화학습 쿼드로터 제어기는 대개 단순화된 바람 모델로 학습되는데, 바람의 크기가 아니라
**충실도(fidelity)** 가 정책 강건성에 미치는 영향은 정량화된 적이 없다는 문제의식에서 출발한다. 초록 단일 출처라 confidence는 low다.^[inbox/processed/fetch-2026-10-08-arxiv-statistical-turbulence-and-high-fidelity-disturbance-fields-.md]

## 실험 설계

- 5단계 충실도: 무풍 → 이산 1-cosine 돌풍 → 통계적 난류 → 합성 coherent structure → 대기경계층 LES(large-eddy simulation) 바람장.
- PPO 에이전트를 충실도별로 학습하고 전 조합을 교차 평가(train×test). 학습 없는 기준선으로 cascaded PID와 geometric SE(3) 제어기를 사용. 풍속 0–12 m/s 스윕.
- 비교 전에 모든 바람 데이터를 검증했다(합성 생성기는 해석해·인증 표준 대비, LES는 imposed log law 대비).

## 결과 (초록 기준)

- 레이싱급 쿼드로터 호버에서 train×test 행렬이 거의 평평했다. 가장 값싼 구조적 학습 바람인 **이산 돌풍 도메인 랜덤화**가 모든 테스트 열에서 1위였고, 바람에 민감한 27 g 기체에서도 같은 순위가 재현됐다.
- 한 번 튜닝한 geometric 제어기가 충돌률 0으로 학습된 PPO 정책들을 능가(bracket)했다.
- 진단상 강건성을 제한하는 것은 바람 현실성이 아니라 **제어 권한(control authority)** 이며, 바람 충실도 투자는 기체의 바람 민감도에 비례해야 한다고 결론짓는다.

## 관련 페이지

- [[agile-quadrotor-learning]] — 실환경 민첩 쿼드로터 비행 학습
- [[pid-tuning-control]] — PID 제어 기준선
- [[drone-simulation]] — 시뮬레이션 환경 총론
