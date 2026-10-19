---
title: Datalink Communication
created: 2026-07-27
updated: 2026-10-18
type: concept
tags: [datalink, drone-sw, RF, LTE, telemetry, communication, C2]
sources: [inbox/processed/fetch-2026-10-08-kci-multi-dimensional-optimization-of-blocking-aware-resource-al.md, inbox/processed/fetch-2026-10-17-arxiv-uav-based-3d-spectrum-sensing-insights-on-altitude-bandwidth.md, inbox/processed/fetch-2026-10-17-arxiv-experimental-evaluation-of-a-uav-mounted-leo-satellite-backh.md, inbox/processed/fetch-2026-10-17-arxiv-coverage-preserving-self-healing-in-partially-observable-3d-.md, inbox/processed/fetch-2026-10-18-arxiv-a-lyapunov-guided-diffusion-based-reinforcement-learning-app.md]
confidence: medium
domain: comms-protocol
contested: false
contradictions: []
---

# Datalink Communication

Datalink은 드론과 지상국(GCS) 또는 타 드론 간 데이터 통신을 담당하는 물리/링크 계층 시스템이다. C2(Command & Control) 링크와 텔레메트리를 포함한다.

## 통신 계층

```
┌─────────────────────────────────────────┐
│           Application Layer           │
│         MAVLink / Custom API          │
├─────────────────────────────────────────┤
│           Transport Layer             │
│         UDP / TCP / Serial            │
├─────────────────────────────────────────┤
│            Link Layer                 │
│   Radio / WiFi / LTE / Satellite      │
├─────────────────────────────────────────┤
│           Physical Layer              │
│   RF / Optical / Wired / Acoustic     │
└─────────────────────────────────────────┘
```

## 무선 통신 기술

### 1. RF Radio (전통적 텔레메트리)

| 특성 | 설명 |
|------|------|
| **주파수 대역** | 433MHz, 915MHz, 2.4GHz |
| **범위** | 1km ~ 60km (장비에 따라) |
| **속도** | 57.6kbps ~ 250kbps |
| **지연** | 10-100ms |
| **비용** | 저렴 |

**제품 예시:**
- Holybro SiK Telemetry Radio (1km)
- Holybro Microhard (수 km)
- CUAV P9 Radio (~60km)

### 2. WiFi

| 특성 | 설명 |
|------|------|
| **스탠다드** | 802.11n/ac/ax |
| **범위** | 100m ~ 1km (향상형 안테나) |
| **속도** | 150Mbps ~ Gbps |
| **지연** | 1-10ms |
| **용도** | HD 영상, 고속 데이터 |

### 3. LTE/4G/5G

| 특성 | 설명 |
|------|------|
| **범위** | 셀 탑 커버리지 (무제한) |
| **도시환경** | 우수 |
| **고도/해상** | 제한적 |
| **장점** | 글로벌 커버리지, BVLOS |
| **단점** | 월 비용, 네트워크 의존 |

**제품 예시:**
- CUAV LTE Link Kit

### 4. Satellite (위성)

| 특성 | 설명 |
|------|------|
| **범위** | 글로벌 (극지 포함) |
| **비용** | 매우 높음 |
| **지연** | 500ms+ |
| **용도** | 해양, 극지역, 긴급 |

**기술:**
- Iridium
- Starlink (개발 중)
- Inmarsat

## C2 (Command & Control) 링크

| 유형 | 특성 | 용도 |
|------|------|------|
| **RC Radio** | 저지연 (<20ms), 짧은 범위 | 수동 조종 |
| **Telemetry Radio** | MAVLink, 양방향 | 자율 모드 |
| **Hybrid** | RC + 텔레메트리 통합 | 범용 |

## 통신 아키텍처

### 단일 링크

```
GCS ←────MAVLink────→ UAV
     (WiFi/RF/LTE)
```

### 중계 링크 (Relay)

```
GCS ←─→ Relay UAV ←─→ Target UAV
       (MAVProxy)
```

### 멀티 UAV

```
         ┌─── UAV 1
GCS ←──┼─── UAV 2
       └─── UAV 3
```

## 안전 및 보안

| 측면 | 고려사항 |
|------|----------|
| **RC Loss** | Failsafe 동작 (RTL/Hold/Land) |
| **GCS Loss** | 자율 모드 유지 또는 RTL |
| **Jamming** | 주파수 호핑, 다중 링크 |
| **Eavesdropping** | MAVLink 암호화 |
| **Spoofing** | 메시지 서명 |

## 선택 가이드

| 요구사항 | 권장 솔루션 |
|----------|------------|
| 교육/개발 | SiK Radio + WiFi |
| 프로/산업 | Microhard / P9 |
| BVLOS/Cities | LTE |
| 해양/원격 | 위성 |
| HD 영상 | 고출력 WiFi |

## 관련 개념

- [[mavlink-protocol]] — 애플리케이션 프로토콜
- [[dronecan-protocol]] — CAN 버스 통신
- [[swarm-coordination]] — 멀티 드론 통신
- [[flight-controller-hardware]] — 텔레메트리 하드웨어

## 최신 근거 연결 (2026-10-08)

- UAV 가시광통신(VLC) 보조 메시 네트워크의 자원 경쟁·혼잡 완화 연구: [[uav-vlc-wmn-blocking-aware-bandwidth-allocation]]^[inbox/processed/fetch-2026-10-08-kci-multi-dimensional-optimization-of-blocking-aware-resource-al.md]

## 최신 근거 연결 (2026-10-17)

- 실측 기반 3D 라디오 환경 지도(REM)에서 고도·대역폭·안테나 패턴 보정이 정확도를 좌우하며 GPR이 가장 안정적인 기준선이었다: [[uav-3d-spectrum-sensing-rem]]^[inbox/processed/fetch-2026-10-17-arxiv-uav-based-3d-spectrum-sensing-insights-on-altitude-bandwidth.md]
- Starlink Mini를 실은 UAV가 약 200 m 범위까지 업링크 약 30 Mbps를 유지한 LEO 백홀 비상 통신 실험: [[uav-leo-satellite-backhaul-emergency]]^[inbox/processed/fetch-2026-10-17-arxiv-experimental-evaluation-of-a-uav-mounted-leo-satellite-backh.md]
- 분할된 군집망의 토폴로지 복구(시뮬레이션): [[addiff-gt-uav-swarm-self-healing]]^[inbox/processed/fetch-2026-10-17-arxiv-coverage-preserving-self-healing-in-partially-observable-3d-.md]

## 최신 근거 연결 (2026-10-18)

- 저고도 UAV의 V2X 지원에서 채널 할당·전력·고도를 함께 최적화하는 Lyapunov 유도 확산 RL(D3PG)이 실제 차량 궤적 시뮬레이션에서 벤치마크보다 우수하다고 보고했다(초록 기준, 수치 없음, CSI 피드백 지연 고려): [[lyapunov-diffusion-rl-uav-vehicular-networks]]^[inbox/processed/fetch-2026-10-18-arxiv-a-lyapunov-guided-diffusion-based-reinforcement-learning-app.md]
