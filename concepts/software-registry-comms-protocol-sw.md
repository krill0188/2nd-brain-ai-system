---
title: "드론 통신 프로토콜 SW SW 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: software-ecosystem
tags: [drone, drone-sw]
sources: [inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 통신 프로토콜 SW SW 레지스트리

드론과 융합해 쓰는 SW의 통신 프로토콜 SW 분야 제품·오픈소스 23건을 공식 페이지/저장소 기준으로 정리한 레지스트리(2026-10-17 수집)다. 상위 개요는 [[drone-software-ecosystem-registry]].

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| MAVLink (프로토콜·생성기) | 오픈소스 | 생성기 (L)GPL v3 등(COPYING 참조) | MAVLink 프로젝트 / Dronecode | https://github.com/mavlink/mavlink | 저장소 설명: 드론용 메시지 마샬링·통신 라이브러리. MAVLink 2는 메시지 서명 지원(mavlink-devguide) | 정확한 조항 구분은 COPYING 원문 확인 필요 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| MAVLink C 라이브러리 v2 | 오픈소스 | 미확인 | MAVLink 프로젝트 | https://github.com/mavlink/c_library_v2 | 저장소 설명: v2 프로토콜 공식 참조 C/C++ 라이브러리 | LICENSE 파일 확인 못함 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| rust-mavlink | 오픈소스 | Apache-2.0 | MAVLink 프로젝트 | https://github.com/mavlink/rust-mavlink | 저장소 설명: Rust MAVLink 구현 | 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| pymavlink | 오픈소스 | (L)GPL v3 생성기 등(COPYING 참조) | ArduPilot | https://github.com/ArduPilot/pymavlink | 저장소 설명: 파이썬 MAVLink 인터페이스·유틸리티 | 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| mavlink-router | 오픈소스 | Apache-2.0 | mavlink-router 프로젝트(구 intel 저장소) | https://github.com/mavlink-router/mavlink-router | 저장소 설명: 엔드포인트 간 MAVLink 패킷 라우팅 | intel/mavlink-router 도 접근 가능(동일 설명) ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| mavlink2rest | 오픈소스 | MIT | patrickelectric / Blue Robotics 계열 | https://github.com/mavlink/mavlink2rest | 저장소 설명: MAVLink 소스에서 REST 서버 제공 | 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| mavlink-server (Blue Robotics) | 오픈소스 | MIT | Blue Robotics | https://github.com/bluerobotics/mavlink-server | 저장소 설명: REST API, WebSocket, UDP, TCP, 시리얼, TLog 등 지원 MAVLink 서버 | 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| MAVSDK-Swift | 오픈소스 | BSD-3-Clause | MAVLink 프로젝트 | https://github.com/mavlink/MAVSDK-Swift | 저장소 설명: MAVSDK Swift 클라이언트 | 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| MAVSDK-Java | 오픈소스 | 미확인 | MAVLink 프로젝트 | https://github.com/mavlink/MAVSDK-Java | 저장소 설명: MAVSDK Java 클라이언트 | LICENSE 확인 못함 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| MAVSDK-Proto | 오픈소스 | 미확인 | MAVLink 프로젝트 | https://github.com/mavlink/MAVSDK-Proto | 저장소 설명: MAVSDK gRPC용 proto 파일 모음 | LICENSE 확인 못함 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| DroneCAN DSDL | 오픈소스 | MIT | DroneCAN | https://github.com/DroneCAN/DSDL | 사이트 설명: ArduPilot·PX4의 CAN 주변장치 통신용 주 프로토콜 | https://dronecan.github.io ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| pydronecan | 오픈소스 | MIT | DroneCAN | https://github.com/dronecan/pydronecan | 저장소 설명: 파이썬 DroneCAN 코드 생성·인터페이스·유틸리티 | 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| DroneCAN GUI Tool | 오픈소스 | MIT | DroneCAN | https://github.com/DroneCAN/gui_tool | 미확인 | 저장소 설명 없음 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| libcanard (DroneCAN) | 오픈소스 | MIT | DroneCAN | https://github.com/dronecan/libcanard | 미확인 | 저장소 설명 없음 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| libuavcan (DroneCAN) | 오픈소스 | MIT | DroneCAN | https://github.com/dronecan/libuavcan | 미확인 | 저장소 설명 없음 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| pycyphal | 오픈소스 | MIT | OpenCyphal | https://github.com/OpenCyphal/pycyphal | 저장소 설명: Cyphal 프로토콜 스택 파이썬 구현 | Cyphal은 DroneCAN과 별개 프로토콜. ArduPilot/PX4 지원 여부는 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| rosbridge_suite | 오픈소스 | BSD-3-Clause | RobotWebTools | https://github.com/RobotWebTools/rosbridge_suite | 저장소 설명: rosbridge v2 프로토콜 서버 구현 | 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| Foxglove ws-protocol | 오픈소스 | MIT | Foxglove | https://github.com/foxglove/ws-protocol | 미확인 | 저장소 설명 없음 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| PyTAK | 오픈소스 | Apache-2.0 | Sensors & Signals LLC(snstac) | https://github.com/snstac/pytak | 저장소 설명: TAK(Team Awareness Kit) 연동용 파이썬 패키지 | 개발 주체 표기는 GitHub 조직명 기준 추정 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| DroneCOT | 오픈소스 | Apache-2.0 | snstac | https://github.com/snstac/dronecot | 저장소 설명: Remote ID(ODID) 방송을 TAK 생태계로 모니터링·분석 | 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| FreeTAKServer | 오픈소스 | EPL-2.0 | FreeTAKTeam | https://github.com/FreeTAKTeam/FreeTakServer | 저장소 설명: TAK 클라이언트 호환 상황인식 서버 | 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| TAK Server (공개 저장소) | 오픈소스 | GPL-3.0 (LICENSE.md) | TAK Product Center | https://github.com/TAK-Product-Center/Server | 저장소 설명: TAK Server | 미확인 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |
| ATAK-CIV | 오픈소스 | GPL-3.0 (LICENSE.md) | 미국 국방부(deptofdefense 조직) | https://github.com/deptofdefense/AndroidTacticalAssaultKit-CIV | 미확인 | 저장소 설명 없음 ^[inbox/processed/hw-registry-20261017-software-comms-protocol-sw.md] |

## 한계
- 라이선스와 '드론 연동 포인트'는 저장소·공식 페이지에 적힌 문구만 옮긴 값이며, 표본 대조 전이다. 버전·인기도·가격은 의도적으로 생략했다.
- ROS 공식 사이트 등 봇 차단 사이트는 GitHub 기준으로만 기재했다. 유지보수 상태가 확인되지 않은 항목은 비고에 표시했다.
- 공격 성격의 도구(보안 카테고리)는 방어·승인된 시험 목적의 참고 목록이다.

## 관련 문서
- [[mavlink]]
- [[dronecan-protocol]]
- [[drone-hw-vendor-registry]]
