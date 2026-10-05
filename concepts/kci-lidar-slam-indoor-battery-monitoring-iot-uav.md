---
title: "LiDAR-SLAM 기반 실내 배터리 모니터링 IoT-UAV 플랫폼 (KCI)"
created: 2026-10-03
updated: 2026-10-03
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, datalink]
sources: [inbox/processed/fetch-2026-10-03-kci-lidar-slam-기반-실내-배터리-모니터링-iot-uav-플랫폼.md, raw/papers/drone-ai/lidar-slam-기반-실내-배터리-모니터링-iot-uav-플랫폼.md]
confidence: low
contested: false
contradictions: []
---

# LiDAR-SLAM 기반 실내 배터리 모니터링 IoT-UAV 플랫폼

임영훈(한국공학대학교 IT반도체융합공학과)이 융복합지식학회논문지(2026)에 발표한 연구. 실내 배터리
저장시설의 상태 정보를 수집·전송·관리하고, 이동형 플랫폼(UAV)의 실내 위치 정보를 이와 연계하는
IoT-UAV 플랫폼을 제안한다. 원문은 비공개(페이월)이며 초록만
확인했다.^[inbox/processed/fetch-2026-10-03-kci-lidar-slam-기반-실내-배터리-모니터링-iot-uav-플랫폼.md]

## 구성

- **고정형 센서 노드**: MLX90640(열화상 어레이) + MQ-2(가스/연기) 센서.
- **통신**: LoRa 메시지 송수신.
- **제어 서버**: SQLite 기반 데이터 저장·시각화.
- **이동형 UAV 모듈**: F550 기체의 Cartographer(LiDAR-SLAM) 모듈로 2차원 지도 생성과 지도
  좌표계 내 상대 위치 표시.

## 검증 결과(기능시험 수준)

- 센서 데이터 취득 → 상태 분류 → LoRa 송수신 → 저장·시각화가 순차적으로 동작.
- Gazebo 시뮬레이션과 실제 실내 복도에서 2차원 지도 생성 및 상대 위치 표시 기능 확인.
- 고정형 센서 노드와 이동형 UAV 모듈을 하나의 정보 흐름으로 연계하는 **구성요소 수준의 구현
  가능성**을 제시한 것이 결론이다.

## 한계

실제 화재환경에서의 감지 성능, 자율 이동 및 초기 대응을 포함한 폐루프 운용은 후속 검증이
필요하다고 저자가 명시했다. 따라서 본 페이지의 confidence는 low(단일 출처, 초록만 확인).

## 관련 페이지

- [[flight-ready-lidar-inertial-odometry]] — 임베디드 드론용 LIO 시스템
- [[visual-slam-gps-denied-evaluation]] — GPS 미가용 환경 V-SLAM 평가
- [[thermal-drone-wildfire-monitoring]] — 열화상 드론 화재 감시
