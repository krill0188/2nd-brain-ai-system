---
title: "ArduPilot MAVLink telemetry reliability and latency over an Iridium Certus satellite service (companion UART baud-rate baseline)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
tags: [drone, ardupilot, mavlink, latency, companion-computer, raspberry-pi, uart, mavlink-router]
sources: [inbox/processed/hw-20261021-ai-latency-ardupilot-companion-uart-baud-dade-2026.md]
confidence: medium
contested: false
contradictions: []
---

# ArduPilot MAVLink telemetry reliability and latency over an Iridium Certus satellite service (companion UART baud-rate baseline)

- 원문: https://discuss.ardupilot.org/uploads/short-url/gQs94pbm7pmdI5l6mo3q3B1PYxc.pdf ; 관련 토론 https://discuss.ardupilot.org/t/accurate-timely-control-of-arducopter-by-a-companion-computer/142316^[inbox/processed/hw-20261021-ai-latency-ardupilot-companion-uart-baud-dade-2026.md]
- 저자: Stephen Dade^[inbox/processed/hw-20261021-ai-latency-ardupilot-companion-uart-baud-dade-2026.md]
- 발행: 2026-01^[inbox/processed/hw-20261021-ai-latency-ardupilot-companion-uart-baud-dade-2026.md]

## 핵심 내용 (PDF 본문)
동료심사 논문이 아닌 기술 보고서(ArduPilot 포럼 게시). 지연 정의: "Round-trip time from the ground station (ie Mission Planner) to ArduPilot and back again". 장비: CubeOrange+ (ArduPilot 최신), UART-이더넷 게이트웨이로 CubeNodeEth 또는 Raspberry Pi 3B+(mavlink-router), 종단은 AWS EC2. 각 시험 600초, TCP/UDP 모두. 도구 mavlinklinktester(MLLT, 오픈소스, ping은 TIMESYNC 2 Hz).^[inbox/processed/hw-20261021-ai-latency-ardupilot-companion-uart-baud-dade-2026.md]
직접(FTTP) 기준선 평균/중앙값 지연:^[inbox/processed/hw-20261021-ai-latency-ardupilot-companion-uart-baud-dade-2026.md]
| 경로 | 프로토콜 | 평균 | 중앙값 |
|---|---|---|---|
| CubeNodeEth | TCP / UDP | 19 ms / 19 ms | 19 / 19 ms |
| Raspberry Pi (UART 57600) | TCP / UDP | 70 ms / 60 ms | 53 / 37 ms |
| Raspberry Pi (UART 921600) | TCP / UDP | 22 ms / 18 ms | 20 / 18 ms |
| Wireguard / Zerotier (RPi) | TCP, UDP | 22/19 ms, 22/19 ms | 20/19 ms, 20/19 ms |
패킷 손실·순서 뒤바뀜 0.00%. 결론: 컴패니언 경유 시 FC와의 UART를 "921600 or higher"로 해야 낮은 지연. 위성(Certus 100)에서는 지연 600-1600 ms(요약).^[inbox/processed/hw-20261021-ai-latency-ardupilot-companion-uart-baud-dade-2026.md]
포럼 토론(2026-02, ArduPilot 개발자 stephendade): "MAVLink is only designed for high-level commands in the 10's of Hz at best", 더 빠른 제어는 ROS 2 DDS 인터페이스 또는 온보드 Lua 권고(포럼 의견, 측정 아님).^[inbox/processed/hw-20261021-ai-latency-ardupilot-companion-uart-baud-dade-2026.md]

## 설계에 쓸 수 있는 지침 (원문 수치만)
- 컴패니언-FC UART 보레이트 57600 -> 921600 변경만으로 평균 70 ms -> 22 ms(TCP) 보고.^[inbox/processed/hw-20261021-ai-latency-ardupilot-companion-uart-baud-dade-2026.md]

## 한계·미확인
- 지연이 GCS-네트워크 왕복이며 온보드 컴패니언-FC 단일 홉 지연이 아님. 비행 중 제어 루프 시험 아님. 논문 아님(신뢰도 중간). arXiv 검색은 429 제한으로 ArduPilot 전용 동료심사 논문 확보 실패 -> 이 항목의 학술 논문 공백 지속.^[inbox/processed/hw-20261021-ai-latency-ardupilot-companion-uart-baud-dade-2026.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[px4-offboard-control]]
