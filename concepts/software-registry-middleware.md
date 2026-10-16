---
title: "드론 ROS·미들웨어 SW 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: software-ecosystem
tags: [drone, drone-sw]
sources: [inbox/processed/hw-registry-20261017-software-middleware.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 ROS·미들웨어 SW 레지스트리

드론과 융합해 쓰는 SW의 ROS·미들웨어 분야 제품·오픈소스 18건을 공식 페이지/저장소 기준으로 정리한 레지스트리(2026-10-17 수집)다. 상위 개요는 [[drone-software-ecosystem-registry]].

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| ROS 2 (메타저장소) | 오픈소스 | 미확인 | Open Robotics / OSRF 계열 | https://github.com/ros2/ros2 | 저장소 설명: 로봇용 메타 운영체제 | LICENSE 파일을 저장소 최상위에서 확인 못함. 문서 https://docs.ros.org (봇 차단 페이지로 내용 확인 못함) ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| ROS 1 ros_comm | 오픈소스 | 미확인 | Open Robotics | https://github.com/ros/ros_comm | 저장소 설명: roscpp/rospy 등 통신 관련 핵심 패키지 | LICENSE 최상위 확인 못함. wiki.ros.org는 봇 차단 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| rclcpp | 오픈소스 | Apache-2.0 | ROS 2 프로젝트 | https://github.com/ros2/rclcpp | ROS 2 C++ 클라이언트 라이브러리 | 미확인 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| rosbag2 | 오픈소스 | Apache-2.0 | ROS 2 프로젝트 | https://github.com/ros2/rosbag2 | 미확인 | 로그 기록·재생(저장소 설명 없음) ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| ros1_bridge | 오픈소스 | Apache-2.0 | ROS 2 프로젝트 | https://github.com/ros2/ros1_bridge | 저장소 설명: ROS 1과 ROS 2 양방향 통신 브리지 | 미확인 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| micro_ros_setup | 오픈소스 | Apache-2.0 | micro-ROS | https://github.com/micro-ROS/micro_ros_setup | 저장소 설명: micro-ROS 기반 펌웨어 빌드용 매크로 | micro.ros.org는 이전됨 안내 페이지 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| micro-ROS-Agent | 오픈소스 | Apache-2.0 | micro-ROS | https://github.com/micro-ROS/micro-ROS-Agent | 저장소 설명: Micro XRCE-DDS Agent 기반 ROS 2 패키지 | 미확인 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| Micro XRCE-DDS | 오픈소스 | Apache-2.0 | eProsima | https://github.com/eProsima/Micro-XRCE-DDS | 저장소 설명: XRCE-DDS 구현체 | PX4 uXRCE-DDS의 클라이언트 측과의 관계는 PX4 ROS 2 가이드 참조 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| Micro-XRCE-DDS-Agent (PX4 저장소) | 오픈소스 | Apache-2.0 | PX4 프로젝트(eProsima 코드 기반 표시) | https://github.com/PX4/Micro-XRCE-DDS-Agent | 저장소 설명: Micro XRCE-DDS Agent. PX4 ROS 2 가이드에서 에이전트는 컴패니언 컴퓨터에서 실행 | LICENSE 원문 Apache License 2.0 확인 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| Fast DDS | 오픈소스 | Apache-2.0 | eProsima | https://github.com/eProsima/Fast-DDS | 저장소 설명: DDS 구현체 | https://www.eprosima.com ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| Eclipse Cyclone DDS | 오픈소스 | Eclipse 계열(EPL, LICENSE 참조) | Eclipse Foundation | https://github.com/eclipse-cyclonedds/cyclonedds | 사이트 설명: 고성능 오픈소스 OMG DDS 구현체 | https://cyclonedds.io ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| Eclipse Zenoh | 오픈소스 | Apache-2.0 / EPL-2.0 (LICENSE 상단 표기) | Eclipse Zenoh | https://github.com/eclipse-zenoh/zenoh | PX4 ROS 2 가이드: Zenoh를 uORB 브리지 미들웨어 옵션으로 지원 | https://zenoh.io ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| rmw_zenoh | 오픈소스 | Apache-2.0 | ROS 2 프로젝트 | https://github.com/ros2/rmw_zenoh | 저장소 설명: Zenoh를 사용하는 ROS 2 RMW | 미확인 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| RTI Connext DDS | 상용 | 상용(약관 미확인) | RTI | https://www.rti.com/products | 페이지 설명: DDS 기반 physical AI 시스템 개발 아키텍처 | ROS 2 연동 RMW: https://github.com/ros2/rmw_connextdds (Apache-2.0) ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| MAVROS | 오픈소스 | BSD / GPLv3 / LGPLv3 삼중(LICENSE.md 표기) | MAVLink 프로젝트 | https://github.com/mavlink/mavros | 저장소 설명: 지상국 프록시를 포함한 MAVLink-ROS 게이트웨이 | 지원 ROS 버전은 이 조사에서 미확인 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| px4_ros_com | 오픈소스 | BSD-3-Clause | PX4 | https://github.com/PX4/px4_ros_com | 저장소 설명: PX4와 ROS/ROS 2 인터페이스(Fast-RTPS 브리지) | 저장소 설명이 구형일 수 있음. 최신 경로는 PX4 ROS 2 가이드 확인 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| px4_msgs | 오픈소스 | BSD-3-Clause | PX4 | https://github.com/PX4/px4_msgs | 저장소 설명: PX4 uORB 메시지에 대응하는 ROS 2 메시지 | 미확인 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |
| Eclipse iceoryx | 오픈소스 | Apache-2.0 | Eclipse Foundation | https://github.com/eclipse-iceoryx/iceoryx | 저장소 설명: 제로카피 프로세스 간 통신 | 드론 직접 연동은 미확인 ^[inbox/processed/hw-registry-20261017-software-middleware.md] |

## 한계
- 라이선스와 '드론 연동 포인트'는 저장소·공식 페이지에 적힌 문구만 옮긴 값이며, 표본 대조 전이다. 버전·인기도·가격은 의도적으로 생략했다.
- ROS 공식 사이트 등 봇 차단 사이트는 GitHub 기준으로만 기재했다. 유지보수 상태가 확인되지 않은 항목은 비고에 표시했다.
- 공격 성격의 도구(보안 카테고리)는 방어·승인된 시험 목적의 참고 목록이다.

## 관련 문서
- [[ros2-drone-integration]]
- [[ros2-advanced]]
- [[drone-hw-vendor-registry]]
