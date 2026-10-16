---
title: "드론 GCS SW 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: software-ecosystem
tags: [drone, drone-sw]
sources: [inbox/processed/hw-registry-20261017-software-gcs.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 GCS SW 레지스트리

드론과 융합해 쓰는 SW의 GCS 분야 제품·오픈소스 14건을 공식 페이지/저장소 기준으로 정리한 레지스트리(2026-10-17 수집)다. 상위 개요는 [[drone-software-ecosystem-registry]].

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| QGroundControl | 오픈소스 | Apache-2.0 (GitHub 표시 기준) | Dronecode Foundation(dronecode.org 소개 기준) | https://github.com/mavlink/qgroundcontrol | 저장소 설명: 드론용 크로스플랫폼 GCS(Android/iOS/macOS/Linux/Windows) | https://qgroundcontrol.com ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| Mission Planner | 오픈소스 | GPL-3.0 | ArduPilot 커뮤니티 | https://github.com/ArduPilot/MissionPlanner | 저장소 설명: ArduPilot용 GCS(C# .NET) | 공식 문서 https://ardupilot.org/planner ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| MAVProxy | 오픈소스 | GPL-3.0 | ArduPilot | https://github.com/ArduPilot/MAVProxy | 저장소 설명: MAVLink 프록시 및 커맨드라인 지상국 | 미확인 ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| MAVSDK (C++) | 오픈소스 | BSD-3-Clause | Dronecode / MAVLink 프로젝트 | https://github.com/mavlink/MAVSDK | 저장소 설명: MAVLink 호환 시스템용 C++ API·라이브러리 | GCS 자체 개발용 SDK. 문서 https://mavsdk.mavlink.io ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| MAVSDK-Python | 오픈소스 | BSD-3-Clause | MAVLink 프로젝트 | https://github.com/mavlink/MAVSDK-Python | 저장소 설명: MAVSDK 파이썬 클라이언트 | 미확인 ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| DroneKit-Python | 오픈소스 | Apache-2.0 | DroneKit | https://github.com/dronekit/dronekit-python | 저장소 설명: MAVLink로 드론과 통신하는 파이썬 라이브러리 | 유지보수 현황 미확인 ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| pymavlink | 오픈소스 | (L)GPL v3 생성기 + 별도 조항(COPYING 참조) | ArduPilot | https://github.com/ArduPilot/pymavlink | 저장소 설명: 파이썬 MAVLink 인터페이스·유틸리티 | 정확한 조항 구분은 COPYING 원문 확인 필요 ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| Betaflight Configurator | 오픈소스 | GPL-3.0 | Betaflight | https://github.com/betaflight/betaflight-configurator | 저장소 설명: Betaflight 펌웨어용 크로스플랫폼 설정·관리 앱 | Betaflight 전용 ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| INAV Configurator | 오픈소스 | GPL-3.0 | iNavFlight | https://github.com/iNavFlight/inav-configurator | 미확인 | INAV 전용 설정 앱 ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| Skybrush Server | 오픈소스 | GPL-3.0 | Skybrush(skybrush.io) | https://github.com/skybrush-io/skybrush-server | 저장소 설명: 드론 라이트쇼·군집 관리 프레임워크의 서버 컴포넌트 | Skybrush Suite 일부. 상용 서비스 병행 여부는 미확인 https://skybrush.io ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| Crazyflie client (cfclient) | 오픈소스 | 미확인 | Bitcraze | https://github.com/bitcraze/crazyflie-clients-python | 저장소 설명: Crazyflie용 파이썬 호스트 애플리케이션·라이브러리 | 라이선스 파일(LICENSE.txt)은 있으나 종류 판독 못함 ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| UgCS | 상용 | 상용(약관 미확인) | SPH Engineering(ugcs.com 푸터 기준 미확인) | https://www.ugcs.com | 페이지 제목: 전문 드론 미션 플래닝 SW. 지원 FC 세부는 미확인 | ArduPilot 전용 안내 페이지 https://www.ugcs.com/ugcs-ardupilot 존재(내용 미확인) ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| FlytBase | 상용 | 상용(약관 미확인) | FlytBase | https://www.flytbase.com | 페이지 설명: 엔터프라이즈급 물리적 AI 플랫폼, 자율 드론 플릿 운영 | 지원 FC 미확인 ^[inbox/processed/hw-registry-20261017-software-gcs.md] |
| OpenHD | 오픈소스 | GPL-3.0 | OpenHD 커뮤니티 | https://github.com/OpenHD/OpenHD | 미확인 | 저장소 설명 없음. 영상/데이터 링크 SW로 알려졌으나 이 조사에서 문서 확인 못함 ^[inbox/processed/hw-registry-20261017-software-gcs.md] |

## 한계
- 라이선스와 '드론 연동 포인트'는 저장소·공식 페이지에 적힌 문구만 옮긴 값이며, 표본 대조 전이다. 버전·인기도·가격은 의도적으로 생략했다.
- ROS 공식 사이트 등 봇 차단 사이트는 GitHub 기준으로만 기재했다. 유지보수 상태가 확인되지 않은 항목은 비고에 표시했다.
- 공격 성격의 도구(보안 카테고리)는 방어·승인된 시험 목적의 참고 목록이다.

## 관련 문서
- [[ground-control-station]]
- [[drone-hw-vendor-registry]]
