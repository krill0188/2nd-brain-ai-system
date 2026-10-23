---
title: "Latency Reduction and Packet Synchronization in Low-Resource Devices Connected by DDS Networks in Autonomous UAVs"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
ontology_class: TimingLatency
tags: [drone, latency, mavros, xrce-dds, px4, companion-computer, time-sync]
sources: [inbox/processed/hw-20261021-ai-latency-companion-fc-dds-vs-mavros-cotta-2023.md]
confidence: medium
contested: false
contradictions: []
---

# Latency Reduction and Packet Synchronization in Low-Resource Devices Connected by DDS Networks in Autonomous UAVs

- 원문: https://pmc.ncbi.nlm.nih.gov/articles/PMC10674650/ (DOI 10.3390/s23229269)^[inbox/processed/hw-20261021-ai-latency-companion-fc-dds-vs-mavros-cotta-2023.md]
- 저자: Joao Leonardo Silva Cotta, Daniel Agar, Ivan R Bertaska, John P Inness, Hector Gutierrez^[inbox/processed/hw-20261021-ai-latency-companion-fc-dds-vs-mavros-cotta-2023.md]
- 발행: 2023-11-18 (Sensors 23(22):9269)^[inbox/processed/hw-20261021-ai-latency-companion-fc-dds-vs-mavros-cotta-2023.md]

## 핵심 내용
컴패니언 컴퓨터와 RTOS 기반 오픈소스 비행 컨트롤러 사이의 통신 지연을 측정하고, MicroXRCE-DDS(ROS 2) 브리지를 표준 MAVROS-MAVLink와 비교한다. 지연 오프셋과 클럭 스큐를 추정하는 지수이동평균 필터도 제시한다.^[inbox/processed/hw-20261021-ai-latency-companion-fc-dds-vs-mavros-cotta-2023.md]
측정 조건: Holybro Pixhawk 4(PX4 v1.14.0, 일부 수정), Raspberry Pi 4 8GB, FTDI USB-UART 케이블, FCU UART 921600 baud. 메시지 200 Hz, 115 bytes로 조정(MAVROS IMU는 원래 50 Hz를 200 Hz로 수정).^[inbox/processed/hw-20261021-ai-latency-companion-fc-dds-vs-mavros-cotta-2023.md]

Table 3 (단위 마이크로초, 평균 ± 표준편차)^[inbox/processed/hw-20261021-ai-latency-companion-fc-dds-vs-mavros-cotta-2023.md]
| 방식 | 방향 | 지연 µs |
|---|---|---|
| MicroXRCE-DDS-ROS 2 | 컴패니언 → FC | 1329 ± 162 |
| MicroXRCE-DDS-ROS 2 | FC → 컴패니언 | 1752 ± 315 |
| MAVLink-MAVROS | 컴패니언 → FC | 1678 ± 560 |
| MAVLink-MAVROS | FC → 컴패니언 | 2133 ± 1020 |

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 위 조건에서 UART 링크 지연은 약 1.3~2.1 ms 수준(표 값)이며 XRCE-DDS가 평균·표준편차 모두 작음.^[inbox/processed/hw-20261021-ai-latency-companion-fc-dds-vs-mavros-cotta-2023.md]
- 컴패니언-FC 간 센서 타임스탬프 정렬에는 지연 오프셋/클럭 스큐 추정 필터를 사용(논문 제안).^[inbox/processed/hw-20261021-ai-latency-companion-fc-dds-vs-mavros-cotta-2023.md]

## 한계·미확인
- 본문 PDF의 방법 세부(시계 동기 방식 등)는 확인 요약에 의존. Gazebo 시뮬레이션 호스트 환경 포함 여부 등 실기체 조건은 미확인. 추론 지연은 포함하지 않는 순수 통신 지연.^[inbox/processed/hw-20261021-ai-latency-companion-fc-dds-vs-mavros-cotta-2023.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[px4-offboard-control]]
