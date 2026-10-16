---
title: "Enhancing Multirotor Drone Efficiency: Exploring Minimum Energy Consumption Rate of Forward Flight under Varying Payload"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://arxiv.org/abs/2501.03102
authors: "Ayush Patnaik, Nicolas Michel, Xinfan Lin"
published: "2025-01-06"
tags: [drone, hardware, paper, propulsion, energy-efficiency, forward-flight, payload]
---

# Enhancing Multirotor Drone Efficiency: Exploring Minimum Energy Consumption Rate of Forward Flight under Varying Payload

## 핵심 내용 (방법·결과)

octorotor를 대상으로 전진 비행 중 단위 거리·단위 질량당 에너지 소비율(energy efficiency index)이 다양한 payload 조건에서 어떻게 변화하는지 분석했다. 기존 first-principles 에너지 역학 모델을 기반으로 해석적 유도와 수치 검증을 결합했다.

**핵심 결과:**
- 에너지 소비를 최소화하는 최적 전진 속도(v*)에서 에너지 효율 지수의 최적값은 페이로드를 포함한 기체 질량에 무관하게 **상수**로 유지된다.
- 해당 최적 속도에서 피치 각도도 일정하게 유지된다.
- 이 결과는 임의의 속도에서는 성립하지 않으며, 오직 에너지 최적 속도에서만 적용된다.
- AIAA 2025-2187 논문으로도 발표됨.

## 설계에 쓸 수 있는 지침

- 페이로드가 달라져도 **에너지 최적 전진 속도(v*)만 유지하면** 비행 효율이 일정하게 보장된다 → 페이로드 가변 임무에서 속도 제어 전략에 활용 가능.
- 기체 질량 버짓 설계 시, 페이로드 증가에 따른 에너지 효율 저하는 속도 최적화로 상쇄할 수 있다는 근거로 사용 가능.
- 추진계 선정 시 전진 비행 조건에서의 최적 속도를 우선적으로 도출해야 함.

## 한계·미확인 항목

- 실험적 비행 검증 결과는 미확인 (해석적 도출 + 수치 시뮬레이션만 확인됨).
- octorotor에 특화된 분석이며 quadrotor 등 다른 구성으로의 일반화 여부는 본문 확인 필요.
- 구체적 최적 속도 수치 범위는 미확인 (arXiv 초록에서 미기재).
