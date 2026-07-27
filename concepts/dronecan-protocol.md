---
title: DroneCAN Protocol
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-hw, drone-sw, datalink, CAN-bus]
sources: [raw/articles/px4-dronecan.md]
confidence: high
contested: false
contradictions: []
---

# DroneCAN Protocol

DroneCAN은 **Flight Controller**와 주변기기를 상호 연결하는 오픈소스 CAN 버스 통신 프로토콜이다. UAVCAN v0에서 2022년에 리브랜딩되었다.^[raw/articles/px4-dronecan.md]

## 핵심 장점

| 장점 | 설명 |
|------|------|
| **대규모 하드웨어 생태계** | 센서, 액추에이터, ESC 등 다양한 장치 지원 |
| **견고한 통신** | 상당한 케이블 거리에서도 안정적인 CAN 버스 |
| **양방향 메시징** | health monitoring 및 diagnostics 가능 |
| **단일 버스 아키텍처** | ESC와 주변기기 통합 배선 단순화 |
| **중앙 집중형 펌웨어 업데이트** | PX4를 통해 장치별 펌웨어 갱신 |
| **자동 메타데이터 추적** | 플릿 관리를 위한 장치 정보 자동 수집 |

## 지원 하드웨어 카테고리

| 카테고리 | 예시 |
|---------|------|
| **ESCs & Motor Controllers** | 다양한 DroneCAN 변형 모델 |
| **GNSS Receivers** | ARK, CUAV, Holybro, RaccoonLab, Zubax |
| **Power Monitoring** | CAN 인터페이스 배터리 모니터 |
| **Sensors** | 자력계, 대기 속도, 거리계, optical flow, 기압계 |

## PX4 설정

### DroneCAN 활성화

**파라미터:** `UAVCAN_ENABLE` (값: 0-3, 동적 노드 할당 권장: 2 또는 3)^[raw/articles/px4-dronecan.md]

### 메시지 구독 설정

| 파라미터 패턴 | 설명 |
|--------------|------|
| `UAVCAN_SUB_*` | Inbound 구독 (예: `UAVCAN_SUB_GPS`, `UAVCAN_SUB_FLOW`)
| `UAVCAN_PUB_*` | Outbound 발행 |

> **팁:** 불필요한 버스 혼잡을 방지하려면 구독을 제어하라.

### 펌웨어 업데이트

PX4는 **APDescriptor** (board ID + 버전 메타데이터)를 확인하여 유효한 펌웨어 바이너리(`.bin`)를 식별한다.^[raw/articles/px4-dronecan.md]

**업데이트 파일 위치:** SD 카드 `/fs/microsd/` 또는 `/fs/microsd/ufw_staging/`

## 문제 해결

| 증상 | 해결 방법 |
|------|----------|
| 장치 감지 안 됨 | `UAVCAN_ENABLE` 설정 확인 |
| DNA 서버 비작동 | SD 카드 필요 |
| 모터 제어 문제 | `UAVCAN_ENABLE=3` + `UAVCAN_ESC_IFACE` 설정 |

## 관련 개념

- [[px4-system-architecture]] — PX4 시스템 구성
- [[px4-flight-modes]] — PX4 비행 모드
- [[ros2-drone-integration]] — Companion 연동 스택
