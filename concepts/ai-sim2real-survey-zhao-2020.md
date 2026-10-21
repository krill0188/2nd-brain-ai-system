---
title: "Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: simulation-test
tags: [drone, ai, sim-to-real, reinforcement-learning, survey]
sources: [inbox/processed/hw-20261021-ai-sim2real-survey-zhao-2020.md]
confidence: medium
contested: false
contradictions: []
---

# Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey

- 원문: https://arxiv.org/abs/2009.13303^[inbox/processed/hw-20261021-ai-sim2real-survey-zhao-2020.md]
- 저자: Wenshuai Zhao, Jorge Peña Queralta, Tomi Westerlund^[inbox/processed/hw-20261021-ai-sim2real-survey-zhao-2020.md]
- 발행: 2020-09-24 (v2 2021-07-08, IEEE SSCI 2020)^[inbox/processed/hw-20261021-ai-sim2real-survey-zhao-2020.md]

## 핵심 내용
시뮬레이션에서 학습한 정책이 실제 로봇에서 성능이 떨어지는 sim-to-real gap을 다루는 서베이. 다섯 가지 방법을 검토한다: domain randomization, domain adaptation, imitation learning, meta-learning, knowledge distillation. domain randomization은 시뮬레이터 파라미터를 변화시켜 일반화시키고, domain adaptation은 시뮬·실제 데이터/특징을 정렬한다.^[inbox/processed/hw-20261021-ai-sim2real-survey-zhao-2020.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 정량 수치 없음(서베이 초록).^[inbox/processed/hw-20261021-ai-sim2real-survey-zhao-2020.md]
- 시사점: 격차 완화 수단 5분류를 체크리스트로 사용.^[inbox/processed/hw-20261021-ai-sim2real-survey-zhao-2020.md]

## 한계·미확인
세부 비교 표는 본문 미열람(미확인).^[inbox/processed/hw-20261021-ai-sim2real-survey-zhao-2020.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[drone-simulation]]
