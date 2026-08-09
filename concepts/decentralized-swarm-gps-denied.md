---
title: "Decentralized UAV Swarms in GPS/Communication-Denied Environments"
created: 2026-07-30
updated: 2026-08-10
type: concept
tags: [drone, swarm, datalink, comms-protocol, military, counter-uav]
sources: []
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
note: "Raw source not preserved in repo — found during 2026-08-10 provenance audit, needs recapture"
---

# Decentralized UAV Swarms in GPS/Communication-Denied Environments

GPS 및 통신 차단 환경에서 지상 표적 보호를 위한 분산형 UAV 군집 시스템. 온보드 센서만을 활용하여 표적을 추적하고 군집으로 협업하며, 칼만 필터로 상대 측정만으로 UAV 및 표적 상태를 추정한다.

## 핵심 개념

### 분산 군집 포위 기법
- **Target Tracking**: 온보드 센서 기반 미지 표적 상태 추정
- **Kalman Filters**: 상대 측정만으로 UAV 위치 및 표적 상태 추정
- **Encirclement Strategy**: 표적 운동에 적응하는 분산 포위 기법

### 환경 가정
- GPS 차단 (GPS-denied)
- UAV 간 통신 불가
- 온보드 센서만 의존

### 응용 시나리오
- 군사 표적 방어
- 적대적 UAV 탐지 및 요격
- 실제 로봇 검증 완료

## 관련 페이지

- [[swarm-coordination]] — 군집 드론 운용 모드 및 편대 비행
- [[datalink-communication]] — RF, LTE, WiFi 등 데이터링크 통신
- [[drone-ai-agents]] — 다중 에이전트 협력 및 합의 알고리즘

## 출처

- Silveria et al., "Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-Denied Environments", arXiv:2607.20710, 2026.
