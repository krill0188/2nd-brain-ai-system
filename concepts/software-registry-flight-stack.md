---
title: "드론 비행 스택 SW 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: software-ecosystem
tags: [drone, drone-sw]
sources: [inbox/processed/hw-registry-20261017-software-flight-stack.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 비행 스택 SW 레지스트리

드론과 융합해 쓰는 SW의 비행 스택 분야 제품·오픈소스 13건을 공식 페이지/저장소 기준으로 정리한 레지스트리(2026-10-17 수집)다. 상위 개요는 [[drone-software-ecosystem-registry]].

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| PX4 Autopilot | 오픈소스 | BSD-3-Clause | Dronecode Foundation 산하 PX4 커뮤니티(dronecode.org 소개 기준) | https://github.com/PX4/PX4-Autopilot | uORB 토픽을 ROS 2에 연결(uXRCE-DDS 또는 Zenoh 미들웨어 선택, docs.px4.io ROS 2 가이드) | 공식 문서 https://docs.px4.io ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| ArduPilot (ArduCopter/ArduPlane/ArduRover/ArduSub) | 오픈소스 | GPL-3.0 | ArduPilot 개발팀 | https://github.com/ArduPilot/ardupilot | 저장소 설명: 비행체 4종(Plane/Copter/Rover/Sub) 소스 | 공식 사이트 https://ardupilot.org ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| Betaflight | 오픈소스 | GPL-3.0 | Betaflight 커뮤니티 | https://github.com/betaflight/betaflight | 저장소 설명: 오픈소스 비행 컨트롤러 펌웨어 | 레이싱/FPV 중심 여부는 미확인. 설정 앱 betaflight-configurator 별도 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| INAV | 오픈소스 | GPL-3.0 | iNavFlight 커뮤니티 | https://github.com/iNavFlight/inav | 저장소 설명: 내비게이션 기능을 갖춘 비행제어 소프트웨어 | 설정 앱 inav-configurator 별도 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| EmuFlight | 오픈소스 | GPL-3.0 | EmuFlight 커뮤니티 | https://github.com/EmuFlight/EmuFlight | 저장소 설명: 멀티로터용 비행 컨트롤러 펌웨어 | 미확인 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| Cleanflight | 오픈소스 | GPL-3.0 | Cleanflight 커뮤니티 | https://github.com/cleanflight/cleanflight | 저장소 설명: baseflight 비행제어 펌웨어의 클린코드 버전 | 유지보수 현황 미확인 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| Paparazzi UAV | 오픈소스 | GPL-2.0 | Paparazzi 프로젝트 | https://github.com/paparazzi/paparazzi | 저장소 설명: 무인기용 자유/오픈 하드웨어·소프트웨어 프로젝트의 메인 SW 저장소 | 미확인 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| LibrePilot | 오픈소스 | GPLv3(LICENSE.txt에 명시, 일부 예외 있음) | LibrePilot 프로젝트 | https://github.com/LibrePilot/LibrePilot | GitHub는 미러이며 본 개발은 Bitbucket에서 진행(저장소 설명) | 개발 활성도 미확인 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| Crazyflie firmware | 오픈소스 | GPL-3.0 | Bitcraze | https://github.com/bitcraze/crazyflie-firmware | 저장소 설명: Crazyflie Nano, Crazyflie Bolt 및 Roadrunner Positioning Tag용 메인 펌웨어 | 소형 연구용 기체 전용 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| Rotorflight firmware | 오픈소스 | GPL-3.0 | Rotorflight 프로젝트 | https://github.com/rotorflight/rotorflight-firmware | 미확인 | 저장소 설명 없음. 대상 기체 유형 미확인 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| PX4-ECL (Estimation & Control Library) | 오픈소스 | BSD-3-Clause | PX4 | https://github.com/PX4/PX4-ECL | 저장소 설명: 유도·항법·제어용 추정/제어 라이브러리 | 현재 PX4 본체에 통합 여부는 미확인 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| Apache NuttX | 오픈소스 | Apache-2.0 | Apache Software Foundation | https://github.com/apache/nuttx | 저장소 설명: 실시간 임베디드 OS(RTOS). 비행제어 펌웨어 하부 OS로 쓰이는 사례는 PX4 문서 기준 별도 확인 필요 | PX4 연동 세부는 미확인 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |
| ArduPilot ChibiOS 포크 | 오픈소스 | GPL-3.0 | ArduPilot | https://github.com/ArduPilot/ChibiOS | 저장소 설명: ArduPilot용 ChibiOS 포크 | OS 계층 ^[inbox/processed/hw-registry-20261017-software-flight-stack.md] |

## 한계
- 라이선스와 '드론 연동 포인트'는 저장소·공식 페이지에 적힌 문구만 옮긴 값이며, 표본 대조 전이다. 버전·인기도·가격은 의도적으로 생략했다.
- ROS 공식 사이트 등 봇 차단 사이트는 GitHub 기준으로만 기재했다. 유지보수 상태가 확인되지 않은 항목은 비고에 표시했다.
- 공격 성격의 도구(보안 카테고리)는 방어·승인된 시험 목적의 참고 목록이다.

## 관련 문서
- [[px4-flight-stack]]
- [[ardupilot]]
- [[drone-hw-vendor-registry]]
