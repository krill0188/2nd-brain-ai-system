---
title: "드론 플릿·UTM SW 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: software-ecosystem
tags: [drone, drone-sw]
sources: [inbox/processed/hw-registry-20261017-software-fleet-utm.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 플릿·UTM SW 레지스트리

드론과 융합해 쓰는 SW의 플릿·UTM 분야 제품·오픈소스 22건을 공식 페이지/저장소 기준으로 정리한 레지스트리(2026-10-17 수집)다. 상위 개요는 [[drone-software-ecosystem-registry]].

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| InterUSS DSS | 오픈소스 | Apache-2.0 | InterUSS Platform | https://github.com/interuss/dss | 저장소 설명: ASTM DSS 개념의 RID·비행 조율 구현 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| InterUSS monitoring | 오픈소스 | Apache-2.0 | InterUSS Platform | https://github.com/interuss/monitoring | 저장소 설명: 연합 UTM용 USS 모니터링·자동 테스트 도구 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| uas_standards | 오픈소스 | Apache-2.0 | InterUSS Platform | https://github.com/interuss/uas_standards | 저장소 설명: UAS 관련 표준의 데이터 타입·도구 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| Flight Blender | 오픈소스 | Apache-2.0 (LICENSE 원문) | OpenUTM | https://github.com/openutm/flight-blender | 저장소 설명: 표준 준수 Network Remote ID·비행 승인·지오펜스·교통정보 서버(UTM/U-space) | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| Flight Spotlight | 오픈소스 | Apache-2.0 | OpenUTM | https://github.com/openskies-sh/flight-spotlight | 저장소 설명: 공역 내 비행 실시간 표시 화면 | 저장소 이전: openutm/flight-spotlight ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| Open Drone ID core C library | 오픈소스 | Apache-2.0 | Open Drone ID | https://github.com/opendroneid/opendroneid-core-c | 저장소 설명: Open Drone ID 코어 C 라이브러리 | https://github.com/opendroneid ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| Open Drone ID Android receiver | 오픈소스 | Apache-2.0 | Open Drone ID | https://github.com/opendroneid/receiver-android | 저장소 설명: 무인기 Remote ID용 안드로이드 수신 예제 앱 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| Open Drone ID specs | 오픈소스 | 미확인 | Open Drone ID | https://github.com/opendroneid/specs | 저장소 설명: Open Drone ID 규격 | LICENSE 확인 못함 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| DroneCOT | 오픈소스 | Apache-2.0 | snstac | https://github.com/snstac/dronecot | 저장소 설명: RID/ODID 방송을 TAK로 모니터링·분석 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| Skybrush Server | 오픈소스 | GPL-3.0 | Skybrush | https://github.com/skybrush-io/skybrush-server | 저장소 설명: 군집 관리 프레임워크 서버 | https://skybrush.io ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| DJI FlightHub 2 | 상용 | 상용(약관 미확인) | DJI Enterprise | https://enterprise.dji.com/flighthub-2 | 페이지 설명: 원격 제어, 지능형 비행 스케줄링, 비행경로 관리, 개방형 통합을 제공하는 클라우드 드론 작업 관리 플랫폼 | 지원 기체 목록 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| DJI Cloud API Demo | 오픈소스 | MIT | DJI | https://github.com/dji-sdk/DJI-Cloud-API-Demo | 미확인 | 저장소 설명 없음. 문서 저장소 https://github.com/dji-sdk/Cloud-API-Doc ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| DJI Onboard SDK | 오픈소스 | DJI 자체 약관(License.txt) | DJI | https://github.com/dji-sdk/Onboard-SDK | 저장소 설명: DJI Onboard SDK 공식 저장소 | 소스 공개이나 DJI 약관 적용 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| DJI Payload SDK | 오픈소스 | DJI 자체 약관(LICENSE.txt) | DJI | https://github.com/dji-sdk/Payload-SDK | 저장소 설명: DJI Payload SDK 공식 저장소 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| DJI Mobile SDK V5 (Android) | 오픈소스 | DJI 자체 약관(LICENSE.txt) | DJI | https://github.com/dji-sdk/Mobile-SDK-Android-V5 | 저장소 설명: MSDK V5 샘플 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| Auterion Suite | 상용 | 상용(약관 미확인) | Auterion | https://www.auterion.com/auterion-suite | 페이지 일부: 핵심 데이터 현황을 중앙화하는 업데이트 소개. 회사 소개: 자율 시스템 플랫폼 https://auterion.com | PX4 연동 여부는 공식 페이지에서 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| FlytBase | 상용 | 상용(약관 미확인) | FlytBase | https://flytbase.com | 페이지 설명: 자동화·감사 대응 준수용 엔터프라이즈 물리적 AI 플랫폼, 자율 드론 플릿 운영 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| DroneSense | 상용 | 상용(약관 미확인) | DroneSense | https://dronesense.com | 페이지 설명: 공공안전 기관용 드론 관리·협업 플랫폼 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| Unifly | 상용 | 상용(약관 미확인) | Unifly | https://www.unifly.aero | 페이지 설명: 운영자·감독자용 UTM 솔루션 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| DroneLogbook | 상용 | 상용(약관 미확인) | DroneLogbook | https://www.dronelogbook.com | 페이지 설명: UAV 비행 로그·규정 준수 관리 솔루션 | 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| DroneDeploy | 상용 | 상용(약관 미확인) | DroneDeploy | https://www.dronedeploy.com | 페이지 설명: 리얼리티 캡처·로보틱스·AI | 플릿 관리보다 매핑 성격이 강함 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |
| DroneTeam | 상용 | 미확인 | 미확인 | https://www.droneteam.com | 페이지 제목·설명을 추출하지 못함 | 신뢰도 낮음. URL 응답(200)만 확인, 제품 내용 미확인 ^[inbox/processed/hw-registry-20261017-software-fleet-utm.md] |

## 한계
- 라이선스와 '드론 연동 포인트'는 저장소·공식 페이지에 적힌 문구만 옮긴 값이며, 표본 대조 전이다. 버전·인기도·가격은 의도적으로 생략했다.
- ROS 공식 사이트 등 봇 차단 사이트는 GitHub 기준으로만 기재했다. 유지보수 상태가 확인되지 않은 항목은 비고에 표시했다.
- 공격 성격의 도구(보안 카테고리)는 방어·승인된 시험 목적의 참고 목록이다.

## 관련 문서
- [[drone-regulations]]
- [[drone-hw-vendor-registry]]
