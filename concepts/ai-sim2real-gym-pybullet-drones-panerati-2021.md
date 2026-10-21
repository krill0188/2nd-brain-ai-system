---
title: "Learning to Fly -- a Gym Environment with PyBullet Physics for Reinforcement Learning of Multi-agent Quadcopter Control"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: simulation-test
tags: [drone, ai, sim-to-real, simulation, reinforcement-learning, multi-agent]
sources: [inbox/processed/hw-20261021-ai-sim2real-gym-pybullet-drones-panerati-2021.md]
confidence: medium
contested: false
contradictions: []
---

# Learning to Fly -- a Gym Environment with PyBullet Physics for Reinforcement Learning of Multi-agent Quadcopter Control

- 원문: https://arxiv.org/abs/2103.02142^[inbox/processed/hw-20261021-ai-sim2real-gym-pybullet-drones-panerati-2021.md]
- 저자: Jacopo Panerati, Hehui Zheng, SiQi Zhou, James Xu, Amanda Prorok, Angela P. Schoellig^[inbox/processed/hw-20261021-ai-sim2real-gym-pybullet-drones-panerati-2021.md]
- 발행: 2021-03-03 (v3 2021-07-25, IROS 2021)^[inbox/processed/hw-20261021-ai-sim2real-gym-pybullet-drones-panerati-2021.md]

## 핵심 내용
PyBullet 기반 OpenAI Gym 형태의 다중 쿼드콥터 시뮬레이션 환경을 공개한다. 다중 에이전트 및 비전 기반 RL 인터페이스를 제공하고 충돌과 공기역학 효과(downwash 등)를 모델링한다. 데모는 PID 궤적 추종, 다중 로봇 비행, 단일·다중 에이전트 안정화 RL 과제를 포함한다. 제어이론과 머신러닝의 결합 연구를 지원하는 것이 목적이다.^[inbox/processed/hw-20261021-ai-sim2real-gym-pybullet-drones-panerati-2021.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 수치 없음(초록 기준).^[inbox/processed/hw-20261021-ai-sim2real-gym-pybullet-drones-panerati-2021.md]
- 시사점: RL 정책 학습 전에 충돌·downwash를 포함한 시뮬레이터에서 PID 기준선과 비교 가능.^[inbox/processed/hw-20261021-ai-sim2real-gym-pybullet-drones-panerati-2021.md]

## 한계·미확인
초록 페이지에 프로젝트명 'gym-pybullet-drones'는 표기되지 않아 이름 확인 못 함. sim-to-real 실비행 검증 결과는 초록에 없음(미확인). ~/2nd/concepts rl-quadrotor-tunable-control와 인접(보강).^[inbox/processed/hw-20261021-ai-sim2real-gym-pybullet-drones-panerati-2021.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[drone-simulation]]
