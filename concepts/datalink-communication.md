---
title: Datalink Communication
created: 2026-07-27
updated: 2026-10-20
type: concept
tags: [datalink, drone-sw, RF, LTE, telemetry, communication, C2]
sources: [inbox/processed/fetch-2026-10-08-kci-multi-dimensional-optimization-of-blocking-aware-resource-al.md, inbox/processed/fetch-2026-10-17-arxiv-uav-based-3d-spectrum-sensing-insights-on-altitude-bandwidth.md, inbox/processed/fetch-2026-10-17-arxiv-experimental-evaluation-of-a-uav-mounted-leo-satellite-backh.md, inbox/processed/fetch-2026-10-17-arxiv-coverage-preserving-self-healing-in-partially-observable-3d-.md, inbox/processed/fetch-2026-10-18-arxiv-a-lyapunov-guided-diffusion-based-reinforcement-learning-app.md, inbox/processed/fetch-2026-10-19-arxiv-meteorologically-introduced-impacts-on-aerial-channels-and-u.md, inbox/processed/fetch-2026-10-20-arxiv-uav-rotatable-antenna-under-rotation-delay.md, inbox/processed/fetch-2026-10-19-arxiv-joint-resource-management-for-energy-efficient-uav-assisted-.md, inbox/processed/fetch-2026-10-20-arxiv-autonomous-agricultural-monitoring-with-aerial-drones-and-rf.md]
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

## 최신 근거 연결 (2026-10-20)

- 비·안개·눈 조건의 2 GHz~900 GHz 항공 채널 분석에서 mmWave는 중간 강도 비가, 근-THz는 눈이 3D 커버리지 반경에 가장 큰 영향을 주며 주파수가 높을수록 안테나 수 증설로 보상할 수 있다고 한다(초록 기준): [[uav-weather-aerial-channel-impacts]]^[^[inbox/processed/fetch-2026-10-19-arxiv-meteorologically-introduced-impacts-on-aerial-channels-and-u.md]]
- 회전형 안테나는 기계 회전 시간이 전송 가능 시간을 줄여 재방향 이득과 트레이드오프를 이루며, 최소 유효 전송률 최대화를 위해 방향·빔포밍을 공동 설계한다(이론·시뮬레이션): [[uav-rotatable-antenna-rotation-delay]]^[^[inbox/processed/fetch-2026-10-20-arxiv-uav-rotatable-antenna-under-rotation-delay.md]]
- 지상 인프라가 없는 지역에서 UAV가 연산과 무선 전력을 함께 제공하는 SWIPT-MEC를 개선 SAC로 최적화했으나 실기체 검증은 없다: [[uav-swipt-mec-drl-resource-management]]^[^[inbox/processed/fetch-2026-10-19-arxiv-joint-resource-management-for-energy-efficient-uav-assisted-.md]]
- **한계 사례**: 드론 탑재 비콘으로 배터리 없는 센서 태그를 구동하는 AERPAW 실험은 지상 시험에서 안정적이었지만 공중 시험에서는 무선 간섭으로 태그 데이터 검출에 실패했다: [[rf-energy-harvesting-sensor-tags-drone-agriculture]]^[^[inbox/processed/fetch-2026-10-20-arxiv-autonomous-agricultural-monitoring-with-aerial-drones-and-rf.md]]
