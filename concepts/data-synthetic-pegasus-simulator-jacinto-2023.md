---
title: "Pegasus Simulator: An Isaac Sim Framework for Multiple Aerial Vehicles Simulation"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: simulation-test
tags: [drone, synthetic-data, isaac-sim, px4, ros2, simulator]
sources: [inbox/processed/hw-20261021-data-synthetic-pegasus-simulator-jacinto-2023.md]
confidence: medium
contested: false
contradictions: []
---

# Pegasus Simulator: An Isaac Sim Framework for Multiple Aerial Vehicles Simulation

- 원문: arXiv:2307.05263^[inbox/processed/hw-20261021-data-synthetic-pegasus-simulator-jacinto-2023.md]
- 저자: Marcelo Jacinto, Joao Pinto, Jay Patrikar, John Keller, Rita Cunha, Sebastian Scherer, Antonio Pascoal^[inbox/processed/hw-20261021-data-synthetic-pegasus-simulator-jacinto-2023.md]
- 발행: 2023-07-11 (v2 2024-04-15; ICUAS 2024)^[inbox/processed/hw-20261021-data-synthetic-pegasus-simulator-jacinto-2023.md]

## 핵심 내용
NVIDIA Isaac Sim 확장 형태의 모듈형 프레임워크로 사실적 가상 환경에서 다수 멀티로터를 실시간 시뮬레이션한다. PX4-Autopilot, ROS 2와 연동하고 GUI를 제공한다. 비선형 제어기를 구현하고 2대가 공격적 기동을 하는 시뮬레이션으로 기능을 시연했다. 코드와 문서는 보충 자료로 제공.^[inbox/processed/hw-20261021-data-synthetic-pegasus-simulator-jacinto-2023.md]
원문 인용: "real-time simulation of multiple multirotor vehicles in photo-realistic environments"^[inbox/processed/hw-20261021-data-synthetic-pegasus-simulator-jacinto-2023.md]

## 설계·운용에 쓸 수 있는 지침
- Isaac Sim 기반 합성 데이터 생성(카메라 등)과 PX4 SITL을 묶는 시작점.^[inbox/processed/hw-20261021-data-synthetic-pegasus-simulator-jacinto-2023.md]

## 한계·미확인
- 초록에 수치 없음. 센서 모델 종류와 합성 데이터 출력 포맷은 미확인.^[inbox/processed/hw-20261021-data-synthetic-pegasus-simulator-jacinto-2023.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[drone-simulation]]
