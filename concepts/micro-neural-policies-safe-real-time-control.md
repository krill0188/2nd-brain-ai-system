---
title: "Micro Neural Policies: 안전한 실시간 로봇 제어용 초소형 신경망 정책"
created: 2026-10-08
updated: 2026-10-10
type: concept
domain: flight-control
tags: [drone, drone-ai, drone-sw, research]
sources: [inbox/processed/fetch-2026-10-08-arxiv-micro-neural-policies-for-safe-real-time-robotic-control.md, raw/papers/drone-ai/micro-neural-policies-for-safe-real-time-robotic-control.md]
confidence: low
contested: false
contradictions: []
---

# Micro Neural Policies (MNP)

Cao, Curcio, Ottaviano, Caccamo의 arXiv 논문(2026-10-06). 연산이 제한된 임베디드 장치에서 안전하고 강건한 실시간 제어를
하기 위해 신경망 정책을 매우 작게 합성하는 방법이다. 초록 단일 출처라 confidence는 low다.^[inbox/processed/fetch-2026-10-08-arxiv-micro-neural-policies-for-safe-real-time-robotic-control.md]^[raw/papers/drone-ai/micro-neural-policies-for-safe-real-time-robotic-control.md]

## 방법과 결과 (초록 기준)

- 정책 탐색에 **진화 전략(ES)** 과 **통계적 모델 검증(SMC)** 기반 검증을 결합하면, 안전성·강건성을 해치지 않고 네트워크 크기를 크게 줄일 수 있다고 주장한다.
- Cartpole과 Quadrotor 제어 과제에서 제어 주파수와 네트워크 구조를 바꿔 가며 대규모 학습·평가를 수행했다.
- 시뮬레이션 검증 후 실제 시스템으로 **zero-shot 전이**에 성공했다고 보고한다.
- 메모리 사용량은 **0.5~7.5 kB**. 마이크로컨트롤러에서 지터 25 ns 미만의 실시간 추론이 가능하고 칩 유휴 시간이 97% 이상이다.

## 한계

초록만 수집했으므로 정량 비교 대상(PID 등 기존 제어기), 쿼드로터 실기 시험 조건, SMC 안전 기준은 확인하지 못했다.

## 관련 페이지

- [[lightweight-safe-rl-uav]] — 밀집 환경 경량 안전 강화학습 UAV 내비게이션
- [[calos-lyapunov-safety-layer-quadrotor-rl]] — 쿼드로터 안전 강화학습용 Lyapunov 안전 레이어
- [[rl-quadrotor-tunable-control]] — RL 기반 쿼드로터 성능 튜닝

- 관련(바람장 충실도 vs 정책 강건성 비교): [[quadrotor-wind-fidelity-ppo-robustness]]
