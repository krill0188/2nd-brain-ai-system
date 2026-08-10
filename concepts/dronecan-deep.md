---
title: "DroneCAN Deep Dive — CAN 버스 통신 프로토콜"
created: 2026-07-28
updated: 2026-07-28
type: concept
tags: [drone-hw, drone-sw, datalink]
sources:
  - inbox/processed/px4-dronecan.md
confidence: high
domain: comms-protocol
contested: false
contradictions: []
---

# DroneCAN Deep Dive

DroneCAN은 FC와 주변기기를 연결하는 오픈소스 CAN 버스 통신 프로토콜. 2022년 UAVCAN v0에서 재브랜딩.

## 핵심 이점

- 대규모 하드웨어 생태계 (센서, 액추에이터, ESC)
- CAN 버스: 장거리 케이블에서도 강력한 통신
- 양방향 메시징 → 상태 모니터링 및 진단
- ESC와 주변기기용 단일 버스 아키텍처 (배선 간소화)
- PX4를 통한 중앙 집중식 펌웨어 업데이트 및 장치 구성
- 자동 장치 메타데이터 추적 (플릿 관리)

## 지원 하드웨어 카테고리

| 카테고리 | 예시 |
|---|---|
| ESC 및 모터 컨트롤러 | 다양한 DroneCAN 변형 |
| GNSS 수신기 | ARK, CUAV, Holybro, RaccoonLab, Zubax |
| 전력 모니터링 | CAN 인터페이스 배터리 모니터 |
| 센서 | 자력계, 대기속도, 거리측정기, optical flow, 기압계 |

## 설정

### 활성화

파라미터: `UAVCAN_ENABLE` (값 0-3, 동적 노드 할당을 위해 2 또는 3 권장)

### 메시지 구독

- `UAVCAN_SUB_*` — 인바운드 구독 (예: `UAVCAN_SUB_GPS`, `UAVCAN_SUB_FLOW`)
- `UAVCAN_PUB_*` — 아웃바운드 발행

구독 제어로 불필요한 버스 혼잡 방지.

### 펌웨어 업데이트

PX4는 APDescriptor(보드 ID + 버전 메타데이터)로 유효한 펌웨어 바이너리(`.bin`)를 식별. 부팅 전 SD 카드 디렉토리(`/fs/microsd/` 또는 `/fs/microsd/ufw_staging/`)에 펌웨어 파일 배치.

## 문제 해결

| 증상 | 해결책 |
|---|---|
| 장치 감지 안 됨 | `UAVCAN_ENABLE` 설정 확인 |
| DNA 서버 비기능 | SD 카드 필요 |
| 모터 제어 문제 | `UAVCAN_ENABLE=3` + `UAVCAN_ESC_IFACE` 구성 |

## 관련 페이지

- [[dronecan-protocol]] — DroneCAN 개요
- [[flight-controller-hardware]] — FC 하드웨어 연동
- [[px4-offboard-control]] — 오프보드 제어

## 📰 최근 관련 소식
- 폭발물 싣고 독일 공항 날아든 드론···경찰 “기폭 장치 제거” (경향신문, Wed, 05 Au) — https://news.google.com/rss/articles/CBMiWkFVX3lxTE1WS0FOM3RRX2JDNEZWTXpCc2lMMDFCaVJ1NmlVOFQ0NXBSZ1M2Q3B1TVlPYy1SMUxPMC0wTThVX01rd2dnQlA5N2o5TTlyNlY1bFF2OEoyTE13UdIBX0FVX3lxTE12bng0UngtcWxZNTRDLWlMWGlVRzFhblk5cDNtcnVzUGg5QmdCNGgxYzFHRm05V0RCRmcxV3JtbDE5bmRBOHN1elp1TEtJRkdvaUxaMF81aHZZYnBTbXJ3?oc=5
