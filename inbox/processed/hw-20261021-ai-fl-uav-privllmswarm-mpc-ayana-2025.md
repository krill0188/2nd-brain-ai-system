---
title: "PrivLLMSwarm: Privacy-Preserving LLM-Driven UAV Swarms for Secure IoT Surveillance"
created: 2026-10-22
captured: 2026-10-22
type: paper
domain: ai-autonomy
source: https://arxiv.org/abs/2512.06747
authors: Jifar Wakuma Ayana, Huang Qiming
published: 2025-12-07
tags: [drone, privacy, mpc, llm, swarm, differential-privacy-comparison]
---
## 핵심 내용 (arXiv 초록)
LLM 기반 UAV 군집이 민감 운용 데이터를 평문 처리하는 문제를 Secure Multi-Party Computation(MPC)으로 해결. MPC에 맞춘 transformer 구성요소(비선형 활성화 근사), RL로 강화된 미세조정 GPT 명령 생성기. 도시 규모 시뮬레이션에서 "high semantic accuracy, low encrypted inference latency, robust formation control"을 주장하고, 차등 프라이버시·연합학습·평문 기준선보다 privacy-utility 균형이 우수하다고 비교. 코드와 합성 데이터 공개.

## 설계에 쓸 수 있는 지침
- DP와 FL 대안으로 MPC 추론이 제시되었으나 정량 지연은 초록에 없어 탑재 가능성은 별도 검증 필요.

## 한계·미확인
- 초록만 열람. 지연(ms), 정확도, 암호화 오버헤드 수치 미확인. 실기체 시험 아님(시뮬레이션). 이 논문은 DP를 비교 기준선으로만 다룸.
