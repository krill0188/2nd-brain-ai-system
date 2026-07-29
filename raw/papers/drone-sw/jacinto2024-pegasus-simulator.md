---
title: "Pegasus Simulator: An Isaac Sim Framework for Multiple Aerial Vehicles Simulation"
authors:
  - Marcelo Jacinto
  - João Pinto
  - Jay Patrikar
  - John Keller
  - Rita Cunha
  - Sebastian Scherer
  - António Pascoal
venue: "IEEE ICUAS 2024"
year: 2024
doi: "10.1109/ICUAS60882.2024.10556959"
arxiv: "10.48550/arXiv.2307.05263"
url: "https://arxiv.org/abs/2307.05263"
pdf: "https://arxiv.org/pdf/2307.05263"
topics: [drone-sw, swarm, simulation, px4, ros2, isaac-sim]
abstract: |
  Developing and testing novel control and motion planning algorithms for aerial 
  vehicles can be a challenging task, with the robotics community relying more than 
  ever on 3D simulation technologies to evaluate the performance of new algorithms 
  in a variety of conditions and environments. In this work, we introduce the 
  Pegasus Simulator, a modular framework implemented as an NVIDIA Isaac Sim extension 
  that enables real-time simulation of multiple multirotor vehicles in photo-realistic 
  environments, while providing out-of-the-box integration with the widely adopted 
  PX4-Autopilot and ROS2 through its modular implementation and intuitive graphical 
  user interface. To demonstrate some of its capabilities, a nonlinear controller 
  was implemented and simulation results for two drones performing aggressive flight 
  maneuvers are presented.
source_code: "https://github.com/PegasusSimulator/PegasusSimulator"
ingested: 2026-07-27
---

# Pegasus Simulator: An Isaac Sim Framework for Multiple Aerial Vehicles Simulation

## Metadata

| 항목 | 내용 |
|------|------|
| **저자** | Marcelo Jacinto, João Pinto, Jay Patrikar, John Keller, Rita Cunha, Sebastian Scherer, António Pascoal |
| **발행처** | IEEE ICUAS 2024 (arXiv:2307.05263) |
| **연도** | 2024 |
| **DOI** | 10.1109/ICUAS60882.2024.10556959 |
| **PDF** | https://arxiv.org/pdf/2307.05263 |
| **소스코드** | https://github.com/PegasusSimulator/PegasusSimulator |

## 주요 내용

### 연구 목표
- NVIDIA Isaac Sim 기반 드론 시뮬레이터 개발
- 다중 멀티로터 실시간 시뮬레이션
- PX4-Autopilot 및 ROS2 통합

### 핵심 기술
- **NVIDIA Isaac Sim Extension**: 포토리얼리스틱 환경
- **PX4-Autopilot Integration**: 즉시 사용 가능한 PX4 연동
- **ROS2 Integration**: ROS2 브리지 지원
- **GUI**: 직관적 그래픽 인터페이스

### 시연
- 비선형 컨트롤러 구현
- 2대 드론 공격적 비행 기동 시뮬레이션

## 관련 위키 페이지

- [[drone-simulation]] — 드론 시뮬레이션 개요
- [[px4-system-architecture]] — PX4 시스템
- [[ros2-drone-integration]] — ROS2 드론 연동
- [[swarm-coordination]] — 스웜 편대 비행

## 인용

```bibtex
@inproceedings{jacinto2024pegasus,
  title={Pegasus Simulator: An Isaac Sim Framework for Multiple Aerial Vehicles Simulation},
  author={Jacinto, Marcelo and Pinto, João and Patrikar, Jay and Keller, John and Cunha, Rita and Scherer, Sebastian and Pascoal, António},
  booktitle={IEEE International Conference on Unmanned Aircraft Systems (ICUAS)},
  year={2024},
  doi={10.1109/ICUAS60882.2024.10556959}
}
```
