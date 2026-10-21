---
title: "Reaching the Limit in Autonomous Racing: Optimal Control versus Reinforcement Learning"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: simulation-test
tags: [drone, ai, sim-to-real, reinforcement-learning, drone-racing, domain-randomization]
sources: [inbox/processed/hw-20261021-ai-sim2real-racing-oc-vs-rl-song-2023.md]
confidence: medium
contested: false
contradictions: []
---

# Reaching the Limit in Autonomous Racing: Optimal Control versus Reinforcement Learning

- 원문: https://arxiv.org/abs/2310.10943^[inbox/processed/hw-20261021-ai-sim2real-racing-oc-vs-rl-song-2023.md]
- 저자: Yunlong Song, Angel Romero, Matthias Mueller, Vladlen Koltun, Davide Scaramuzza^[inbox/processed/hw-20261021-ai-sim2real-racing-oc-vs-rl-song-2023.md]
- 발행: 2023-10-17 (Science Robotics 2023)^[inbox/processed/hw-20261021-ai-sim2real-racing-oc-vs-rl-song-2023.md]

## 핵심 내용
자율 드론 레이싱에서 RL로 학습한 신경망 제어기가 최적 제어(OC)를 능가했다. 저자들은 우위의 이유를 목적함수를 더 잘 최적화해서가 아니라 더 나은 목적을 최적화해서라고 설명한다(OC는 궤적 같은 중간 표현이 행동 표현력을 제한). RL은 과제 수준 목적을 직접 최적화하고 domain randomization으로 모델 불확실성을 다룬다.^[inbox/processed/hw-20261021-ai-sim2real-racing-oc-vs-rl-song-2023.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 최대 가속도 중력가속도의 12배 초과, 최대 속도 108 km/h, 표준 워크스테이션에서 수 분 학습으로 'superhuman control'(원문).^[inbox/processed/hw-20261021-ai-sim2real-racing-oc-vs-rl-song-2023.md]
- 모델 불확실성 대응에 domain randomization 사용.^[inbox/processed/hw-20261021-ai-sim2real-racing-oc-vs-rl-song-2023.md]

## 한계·미확인
랩타임과 sim-to-real 격차 지표는 초록에 없음(미확인). 계산 환경 상세 미확인.^[inbox/processed/hw-20261021-ai-sim2real-racing-oc-vs-rl-song-2023.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[drone-simulation]]
