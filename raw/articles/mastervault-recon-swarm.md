---
source_url: "file://MasterVault/Drone/Swarm/Recon-Swarm-Project.md"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "Master (personal dev notes)"
sha256: "3a7f9c2e5d8b1a4f7c9e2d5a8b1c4d7e9f2a5b8c1d4e7f9a2b5c8d1e4f7a9b2"
tags: [swarm, drone-ai, drone]
---

# 지능형 자율 군집정찰드론

## 프로젝트 개요

- **목표**: 학술연구 기반 자율 군집정찰 시스템
- **FC**: CUAV V7+ (ID:1009) / Holybro 6C (ID:1041)
- **펌웨어**: ArduPilot (커스텀)

## 4단계 로드맵

| 단계 | 내용 | 상태 |
|:----:|------|:----:|
| 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 |
| 2 | 2기 편대비행 + 통신 검증 | 계획 |
| 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 |
| 4 | GPS-denied + 실내 군집 | 계획 |

## 센서 스택

| 센서 | 용도 | 인터페이스 |
|------|------|-----------|
| LiDAR | 장애물 감지/매핑 | UART/I2C |
| 카메라 (RGB) | 정찰/객체 인식 | CSI/USB |
| Radar | 전방위 감지 | SPI |
| Optical Flow | GPS-denied 위치추정 | I2C |
| RTK GPS | 정밀 위치 | UART |

## 안전 시스템

- Geofence (하드웨어+소프트웨어 이중)
- 배터리 페일세이프 (자동 RTL)
- 통신 두절 대응 (독립 귀환)
- 충돌 회피 (최소 이격거리 유지)

## SITL 테스트 환경

```bash
# ArduPilot SITL 멀티 기체
sim_vehicle.py -v ArduCopter --instance 0 -L HOME_LAT,HOME_LNG,ALT,HDG
sim_vehicle.py -v ArduCopter --instance 1 -L HOME_LAT,HOME_LNG,ALT,HDG
```
