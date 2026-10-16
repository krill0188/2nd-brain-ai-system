---
title: "simulation SW 레지스트리"
created: 2026-10-17
captured: 2026-10-17
type: software-registry
domain: software-ecosystem
category: simulation
tags: [drone, software, simulation]
---
# simulation SW

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| Gazebo (gz-sim) | 오픈소스 | Apache-2.0 | Open Robotics / Gazebo 프로젝트 | https://github.com/gazebosim/gz-sim | 저장소 설명: 최신 Gazebo 로봇 시뮬레이터 | https://gazebosim.org |
| Gazebo Classic | 오픈소스 | Apache-2.0 (LICENSE 표기) | Open Robotics | https://github.com/gazebosim/gazebo-classic | 저장소 설명: 구 Gazebo. 최신은 gz-sim | 신규 사용은 gz-sim 권장(저장소 안내) |
| ros_gz | 오픈소스 | Apache-2.0 | Gazebo 프로젝트 | https://github.com/gazebosim/ros_gz | 저장소 설명: ROS(1, 2)와 Gazebo 시뮬레이션 통합 | 미확인 |
| PX4 Gazebo 모델 | 오픈소스 | BSD-3-Clause | PX4 | https://github.com/PX4/PX4-gazebo-models | 저장소 설명: app.gazebosim.org용 모델 저장소 | 미확인 |
| PX4-SITL_gazebo-classic | 오픈소스 | 미확인 | PX4 | https://github.com/PX4/PX4-SITL_gazebo-classic | 저장소 설명: OSRF Gazebo에서 SITL·HITL용 플러그인·모델·월드 | LICENSE 확인 못함 |
| jMAVSim | 오픈소스 | BSD-3-Clause | PX4 | https://github.com/PX4/jMAVSim | 저장소 설명: MAVLink 지원 간단 멀티로터 시뮬레이터 | 미확인 |
| PX4-FlightGear-Bridge | 오픈소스 | BSD-3-Clause | PX4 | https://github.com/PX4/PX4-FlightGear-Bridge | 저장소 설명: FlightGear와 PX4 스택 연결 | 미확인 |
| ardupilot_gazebo | 오픈소스 | LGPL-3.0 | ArduPilot | https://github.com/ArduPilot/ardupilot_gazebo | 저장소 설명: ArduPilot SITL 컨트롤러와 Gazebo Sim 플러그인·모델 | 미확인 |
| ardupilot_gz | 오픈소스 | GPL-3.0 | ArduPilot | https://github.com/ArduPilot/ardupilot_gz | 저장소 설명: ROS 2 Humble 환경에서 ArduPilot ROS2 통합·테스트 도구 | 미확인 |
| ArduPilot SITL_Models | 오픈소스 | 미확인 | ArduPilot | https://github.com/ArduPilot/SITL_Models | 저장소 설명: SITL용 기체 모델 | LICENSE 확인 못함 |
| AirSim | 오픈소스 | MIT (LICENSE 표기) | Microsoft AI & Research | https://github.com/microsoft/AirSim | 저장소 설명: Unreal Engine/Unity 기반 자율주행체 시뮬레이터 | 저장소 상태(보관 여부) 미확인 |
| Colosseum | 오픈소스 | MIT 원문 포함(LICENSE) | CodexLabs | https://github.com/CodexLabsLLC/Colosseum | 저장소 설명: Unreal Engine 기반(Unity 지원) 자율 로보틱스 시뮬레이터. AirSim 계승으로 보이나 관계는 미확인 | 미확인 |
| NVIDIA Isaac Sim | 오픈소스 | Apache 2.0 (LICENSE 서두 표기. 의존성별 조건 별도) | NVIDIA | https://github.com/isaac-sim/IsaacSim | 저장소 설명: Omniverse 기반 로봇 개발·시뮬·테스트 앱 | https://developer.nvidia.com/isaac/sim |
| Isaac Lab | 오픈소스 | LICENSE는 README 참조 안내 | NVIDIA / Isaac Lab 프로젝트 | https://github.com/isaac-sim/IsaacLab | 저장소 설명: 로봇 학습 통합 프레임워크 | 라이선스 종류 미확인 |
| Pegasus Simulator | 오픈소스 | BSD-3-Clause | PegasusSimulator 프로젝트 | https://github.com/PegasusSimulator/PegasusSimulator | 저장소 설명: Isaac Sim 위에서 PX4를 지원하는 드론 시뮬 프레임워크 | 미확인 |
| Flightmare | 오픈소스 | MIT | UZH RPG | https://github.com/uzh-rpg/flightmare | 저장소 설명: 개방형 유연 쿼드로터 시뮬레이터 | 미확인 |
| Aerial Gym Simulator | 오픈소스 | BSD-3-Clause | NTNU ARL | https://github.com/ntnu-arl/aerial_gym_simulator | 저장소 설명: 공중 로봇용 Isaac Gym 시뮬레이터 | 미확인 |
| gym-pybullet-drones | 오픈소스 | MIT | UTIAS DSL 계열 | https://github.com/utiasDSL/gym-pybullet-drones | 저장소 설명: 쿼드콥터 단일/멀티에이전트 강화학습 PyBullet Gymnasium 환경 | 저장소 소유 표시가 learnsyslab로 이전된 것으로 보임 |
| RotorS | 오픈소스 | 미확인 | ETH ASL | https://github.com/ethz-asl/rotors_simulator | 저장소 설명: UAV Gazebo 시뮬레이터 | LICENSE 확인 못함 |
| FlightGear | 오픈소스 | GPL-2.0 | FlightGear 프로젝트(미러) | https://github.com/flightgear/flightgear | 저장소 설명: 오픈소스 비행 시뮬레이터(미러) | 미확인 |
| MuJoCo | 오픈소스 | Apache-2.0 | Google DeepMind | https://github.com/google-deepmind/mujoco | 저장소 설명: 범용 물리 시뮬레이터 | 드론 직접 연동 미확인 |
| Unity Robotics Hub | 오픈소스 | Unity 약관 문구(LICENSE.md, 종류 미확정) | Unity Technologies | https://github.com/Unity-Technologies/Unity-Robotics-Hub | 저장소 설명: Unity 로보틱스 시뮬 도구·튜토리얼 허브 | 미확인 |
