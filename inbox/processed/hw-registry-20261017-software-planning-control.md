---
title: "planning-control SW 레지스트리"
created: 2026-10-17
captured: 2026-10-17
type: software-registry
domain: software-ecosystem
category: planning-control
tags: [drone, software, planning-control]
---
# planning-control SW

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| Nav2 | 오픈소스 | 부분별 복수 라이선스(LICENSE 서두에 LGPL-2.1-or-later 등 열거) | Open Navigation | https://github.com/ros-navigation/navigation2 | 저장소 설명: ROS 2 내비게이션 프레임워크·시스템 | https://nav2.org. 비행체 직접 지원 여부는 미확인(지상 로봇 중심 추정) |
| MoveIt 2 | 오픈소스 | BSD-3-Clause | MoveIt 프로젝트 | https://github.com/moveit/moveit2 | 저장소 설명: ROS 2용 MoveIt | https://moveit.ai. 매니퓰레이터 중심, 드론 직접 연동 미확인 |
| Fast-Planner | 오픈소스 | GPL-3.0 | HKUST Aerial Robotics Group | https://github.com/HKUST-Aerial-Robotics/Fast-Planner | 저장소 설명: 쿼드로터용 강건·효율 궤적 계획기 | 미확인 |
| Teach-Repeat-Replan | 오픈소스 | GPL-3.0 | HKUST Aerial Robotics Group | https://github.com/HKUST-Aerial-Robotics/Teach-Repeat-Replan | 저장소 설명: 복잡 환경 공격 비행용 시스템 | 미확인 |
| EGO-Planner | 오픈소스 | GPL-3.0 | ZJU FAST Lab | https://github.com/ZJU-FAST-Lab/ego-planner | 미확인 | 저장소 설명 없음 |
| EGO-Planner-Swarm | 오픈소스 | GPL-3.0 | ZJU FAST Lab | https://github.com/ZJU-FAST-Lab/ego-planner-swarm | 저장소 설명: 멀티콥터용 단일/멀티에이전트 궤적 계획기 | 미확인 |
| EGO-Planner-v2 (Swarm Playground) | 오픈소스 | GPL-3.0 | ZJU FAST Lab | https://github.com/ZJU-FAST-Lab/EGO-Planner-v2 | 저장소 설명: 논문 'Swarm of micro flying robots in the wild' 코드베이스 | 미확인 |
| Fast-Drone-250 | 오픈소스 | 미확인 | ZJU FAST Lab | https://github.com/ZJU-FAST-Lab/Fast-Drone-250 | 저장소 설명: 250mm 자율 드론의 HW·SW 설계 | LICENSE 확인 못함 |
| acados | 오픈소스 | BSD-2-Clause (LICENSE 표기) | acados 개발진 | https://github.com/acados/acados | 저장소 설명: 비선형 최적제어/NMPC용 고속 임베디드 솔버 | 미확인 |
| do-mpc | 오픈소스 | LGPL-3.0 | do-mpc 개발진 | https://github.com/do-mpc/do-mpc | 저장소 설명: MPC 파이썬 툴박스 | 미확인 |
| CasADi | 오픈소스 | LGPL-3.0 | CasADi 개발진 | https://github.com/casadi/casadi | 저장소 설명: 자동미분 기반 수치최적화 심볼릭 프레임워크 | 미확인 |
| Ipopt | 오픈소스 | EPL-2.0 | COIN-OR | https://github.com/coin-or/ipopt | 저장소 설명: 내점법 최적화기 | 미확인 |
| OSQP | 오픈소스 | Apache-2.0 | OSQP 개발진 | https://github.com/osqp/osqp | 저장소 설명: 연산자 분할 QP 솔버 | 미확인 |
| rpg_mpc | 오픈소스 | GPL-3.0 | UZH Robotics and Perception Group | https://github.com/uzh-rpg/rpg_mpc | 저장소 설명: 쿼드로터 MPC 및 perception-aware MPC 확장 | 미확인 |
| rpg_quadrotor_control | 오픈소스 | MIT | UZH RPG | https://github.com/uzh-rpg/rpg_quadrotor_control | 저장소 설명: 쿼드로터 제어 프레임워크 | 미확인 |
| rpg_time_optimal | 오픈소스 | GPL-3.0 | UZH RPG | https://github.com/uzh-rpg/rpg_time_optimal | 저장소 설명: 쿼드로터 웨이포인트 비행 시간최적 계획 | 미확인 |
| mav_trajectory_generation | 오픈소스 | Apache-2.0 | ETH ASL | https://github.com/ethz-asl/mav_trajectory_generation | 저장소 설명: 회전익 MAV용 다항 궤적 생성·최적화 | 미확인 |
| mav_control_rw | 오픈소스 | Apache-2.0 | ETH ASL | https://github.com/ethz-asl/mav_control_rw | 저장소 설명: ROS 기반 회전익 MAV 제어 전략 | 미확인 |
| mav_voxblox_planning | 오픈소스 | BSD-3-Clause | ETH ASL | https://github.com/ethz-asl/mav_voxblox_planning | 저장소 설명: voxblox 지도 기반 MAV 계획 도구 | 미확인 |
| mavros_controllers | 오픈소스 | BSD-3-Clause | Jaeyoung Lim | https://github.com/Jaeyoung-Lim/mavros_controllers | 저장소 설명: PX4 기체용 MAVROS 기반 공격적 궤적 추종 | 미확인 |
| PX4-Avoidance | 오픈소스 | BSD-3-Clause | PX4 | https://github.com/PX4/PX4-Avoidance | 저장소 설명: PX4용 장애물 탐지·회피 ROS 노드 | 미확인 |
| OMPL | 오픈소스 | BSD 3-clause (LICENSE 표기) | OMPL 개발진 | https://github.com/ompl/ompl | 저장소 설명: 오픈 모션 플래닝 라이브러리 | 미확인 |
| Pinocchio | 오픈소스 | BSD-2-Clause | Stack-of-Tasks / LAAS-CNRS | https://github.com/stack-of-tasks/pinocchio | 저장소 설명: 강체 동역학 알고리즘 구현 | 미확인 |
| Crocoddyl | 오픈소스 | BSD-3-Clause | LAAS-CNRS 계열 | https://github.com/loco-3d/crocoddyl | 저장소 설명: 접촉 시퀀스 로봇 최적제어 라이브러리 | 드론 직접 연동 미확인 |
| Agilicious | 오픈소스 | 미확인 | UZH RPG | https://github.com/uzh-rpg/agilicious | 저장소 설명: 'Agile flight done right!' | LICENSE 확인 못함 |
