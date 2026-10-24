---
title: "드론 군집·멀티에이전트 SW 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: software-ecosystem
ontology_class: VendorRegistry
tags: [drone, drone-sw]
sources: [inbox/processed/hw-registry-20261017-software-swarm-multiagent.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 군집·멀티에이전트 SW 레지스트리

드론과 융합해 쓰는 SW의 군집·멀티에이전트 분야 제품·오픈소스 14건을 공식 페이지/저장소 기준으로 정리한 레지스트리(2026-10-17 수집)다. 상위 개요는 [[drone-software-ecosystem-registry]].

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| Aerostack2 | 오픈소스 | BSD-3-Clause | Aerostack2 프로젝트 | https://github.com/aerostack2/aerostack2 | 저장소 설명: 자율 멀티에어리얼로봇 시스템용 ROS 2 프레임워크 | 문서 https://aerostack2.github.io ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| Crazyswarm | 오픈소스 | MIT | USC ACT Lab | https://github.com/USC-ACTLab/crazyswarm | 저장소 설명: 대규모 쿼드콥터 군집 | Crazyflie 계열 대상 추정(저장소 설명에는 미명시) ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| Crazyswarm2 | 오픈소스 | MIT | IMRC Lab | https://github.com/IMRCLab/crazyswarm2 | 저장소 설명: 대규모 쿼드콥터 군집 | ROS 2 대응 여부는 이름 기준, 문서 미확인 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| Buzz | 오픈소스 | MIT | MIST Lab(Polytechnique Montréal) | https://github.com/buzz-lang/Buzz | 저장소 설명: 로봇 군집용 프로그래밍 언어 | 미확인 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| ROSBuzz | 오픈소스 | 미확인 | MIST Lab | https://github.com/MISTLab/ROSBuzz | 저장소 설명: ROS 패키지로 제공되는 Buzz | LICENSE 확인 못함 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| Skybrush Server | 오픈소스 | GPL-3.0 | Skybrush | https://github.com/skybrush-io/skybrush-server | 저장소 설명: 드론 라이트쇼·군집 관리 프레임워크 서버 | https://skybrush.io ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| MRS UAV System | 오픈소스 | BSD-3-Clause | CTU MRS Group | https://github.com/ctu-mrs/mrs_uav_system | 저장소 설명: MRS UAV 시스템 진입점 | 미확인 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| mrs_uav_core | 오픈소스 | BSD-3-Clause | CTU MRS Group | https://github.com/ctu-mrs/mrs_uav_core | 저장소 설명: UAV 제어·상태추정·궤적 생성/추종 ROS 메타패키지 | 미확인 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| Open-RMF | 오픈소스 | Apache-2.0 | Open Robotics 계열(open-rmf) | https://github.com/open-rmf/rmf | 저장소 설명: RMF 소프트웨어 루트 저장소 | 멀티로봇 상호운용. 드론 직접 사용 사례 미확인 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| rmf_ros2 | 오픈소스 | Apache-2.0 | open-rmf | https://github.com/open-rmf/rmf_ros2 | 저장소 설명: RMF 내부 ROS 인프라 | 미확인 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| EGO-Planner-Swarm | 오픈소스 | GPL-3.0 | ZJU FAST Lab | https://github.com/ZJU-FAST-Lab/ego-planner-swarm | 저장소 설명: 단일/멀티에이전트 궤적 계획기 | 미확인 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| px4-offboard (Jaeyoung-Lim) | 오픈소스 | BSD-3-Clause | Jaeyoung Lim | https://github.com/Jaeyoung-Lim/px4-offboard | 저장소 설명: 파이썬 ROS 2로 microDDS 경유 PX4 오프보드 제어 예제 | 멀티 기체 지원 여부 미확인 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| osrf/swarm | 오픈소스 | Apache-2.0 | OSRF | https://github.com/osrf/swarm | 저장소 설명: 군집 시뮬레이션 | 유지보수 현황 미확인 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |
| Dronecode 재단 (소개 페이지) | 오픈소스 | 해당 없음(재단) | Linux Foundation 산하 Dronecode | https://dronecode.org | 페이지 설명: PX4, MAVLink, QGroundControl 등의 중립적 거처 | 군집 SW 자체는 아님. 참고용 ^[inbox/processed/hw-registry-20261017-software-swarm-multiagent.md] |

## 한계
- 라이선스와 '드론 연동 포인트'는 저장소·공식 페이지에 적힌 문구만 옮긴 값이며, 표본 대조 전이다. 버전·인기도·가격은 의도적으로 생략했다.
- ROS 공식 사이트 등 봇 차단 사이트는 GitHub 기준으로만 기재했다. 유지보수 상태가 확인되지 않은 항목은 비고에 표시했다.
- 공격 성격의 도구(보안 카테고리)는 방어·승인된 시험 목적의 참고 목록이다.

## 관련 문서
- [[swarm-coordination]]
- [[drone-hw-vendor-registry]]
