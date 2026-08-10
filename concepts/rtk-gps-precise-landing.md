---
title: RTK GPS & Precise Landing
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-hw, rtk, gps, gnss, differential, precision, landing]
sources: []
confidence: medium
domain: hardware
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# RTK GPS & Precise Landing

RTK(Real-Time Kinematic) GPS는 정밀 측위를 위한 차등 GPS 기술로 수 센티미터 수준의 정확도를 제공한다. 드론의 정밀 착륙과 비행 경로 관리에 필수적이다.

## GPS vs RTK

| 특성 | Standard GPS | RTK GPS |
|------|--------------|---------|
| **Accuracy** | 2-5m | 2-3cm + 1ppm |
| **Constellation** | GPS, GLONASS | GPS, GLONASS, Galileo, Beidou |
| **Correction** | 없음 | Base station 필요 |
| **Latency** | <1s | 1-2s |
| **Cost** | $20-100 | $300-1000+ |
| **Setup** | 간단 | Base station 필요 |

## RTK Principle

### 기본 개념

```
Base Station (Known position)
    │
    │ GNSS raw observations
    │
    ▼ Correction calculation
    │
    ▼ RTCM/Radiopacket
    │
    ▼ Rover (Drone)
         │
         ▼ Corrected position
```

### 오차 소스

| 오차 | Standard GPS | RTK 후 |
|------|-------------|---------|
| **Satellite clocks** | ~2m | 제거됨 |
| **Ionospheric delay** | ~5m | 제거됨 |
| **Tropospheric delay** | ~0.5m | 감소됨 |
| **Multipath** | ~0.5m | 남음 |
| **Receiver noise** | ~0.1m | 남음 |

### Carrier Phase

```
Standard: Pseudo-ranges (code measurements)
RTK: Carrier phase + pseudo-ranges

λ (L1 carrier ≈ 19cm) → mm-level accuracy
```

## RTK Modes

### RTK Fixed (Fixed Solution)

| 특성 | 값 |
|------|-----|
| **Accuracy** | 2-3 cm horizontal |
| **Convergence** | 10-60 seconds |
| **Requirement** | >= 5 satellites, base-rover < 30km |
| **Status** | "RTK Fixed" (green in QGC) |

### RTK Float (Float Solution)

| 특성 | 값 |
|------|-----|
| **Accuracy** | 0.5-2m |
| **Convergence** | 즉시 |
| **Requirement** | 부족한 위성, 긴 baseline |
| **Status** | "RTK Float" (yellow in QGC) |

### DGPS (Differential GPS)

```
Code-based correction
Accuracy: 0.5-1m
Faster than RTK, less accurate
```

## Hardware Setup

### RTK Components

| 부품 | 설명 |
|------|------|
| **Base Station** | 고정된 정확한 좌표 |
| **Rover Module** | 드론 탑재 |
| **Radio/Link** | RTCM 전송 |
| **Antenna** | Survey-grade 권장 |

### 일반적인 RTK 모듈

| 모듈 | 특징 | 가격대 |
|------|------|--------|
| **Here+** | Pixhawk 호환, 통합 솔루션 | $$$ |
| **D-RTK** | DJI, M600/M210/M300 | $$$$ |
| **ArduSimple** | 오픈소스, u-blox F9P | $$ |
| **Septentrio** | 고성능, 다중 주파수 | $$$$$ |
| **Reach RS2/RS3** | Emlid, 가성비 | $$$ |

### Base Station 구성

```
Options:
1. CORS (Continuously Operating Reference Station)
   - 국가망 활용 (한국: GNSS 기준점)
   - NTRIP 서비스 필요

2. Self-hosted Base
   - 자체 base station 설치
   - 초기 좌표 측량 필요

3. Mobile Base
   - 이동식 base (정확도 감소)
   - 드론 간 상대적 정확도는 유지
```

## NTRIP Protocol

RTCM correction을 인터넷으로 전송.

### NTRIP 구조

```
┌─────────────┐
│   CASTER    │ ← NTRIP Server (Rover 연결)
│  (ntrip.gnss.co.kr:2101) │
└──────┬──────┘
       │
       │ HTTP-like TCP
       │
┌──────┴──────┐
│   SERVER    │ ← Base station data
└─────────────┘
```

### 한국 NTRIP 서비스

| 서비스 | URL | 비고 |
|--------|-----|------|
| **국토지리정보원** | gnss.co.kr | VRS, FKP |
| **서울시** | seoul.go.kr | 서울 지역 |
| **국가측지정보센터** | ngii.go.kr | 기준점 정보 |

### PX4 NTRIP 설정

```bash
# NTRIP 활성화
param set GPS_UBX_MODE 1  # Moving base

# NTRIP 설정 (Companion computer)
# str2str (RTKLIB) 또는 ntripclient 실행
```

## PX4 RTK Integration

### 파라미터 설정

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `EKF2_GPS_DELAY` | GPS 지연 | 110ms |
| `EKF2_GPS_POS_X/Y/Z` | GPS antenna offset | 0 |
| `GPS_UBX_MODE` | u-blox 모드 | 0 |

### QGC RTK Setup

```
QGroundControl → Application Settings → RTK GPS
├── Survey-in accuracy: 2.0m
├── Survey-in minimum duration: 60s
├── NTRIP server: 입력
└── Auto-connect: Enable
```

### MAVLink RTCM

```
MAVLink Message:
├── GPS_RTCM_DATA — RTCM fragment
├── GPS_INJECT_DATA — Legacy
└── GPS_STATUS — RTK status
```

## Precise Landing

### Landing 시나리오

```
Approach (GNSS guided)
    ↓
Precision Mode Activate (RTK + Vision)
    ↓
Slow Descent (20cm/s)
    ↓
Ground Detection (rangefinder)
    ↓
Disarm
```

### Landing Beacon

| 유형 | 정확도 | 범위 |
|------|--------|------|
| **IR Beacon** | 10cm | 5m |
**RTK-only** | 30cm | 무제한 |
| **ArUco Marker** | 5cm | 10m |
| **UWB** | 10cm | 50m |
| **RTK + Vision** | 5cm | 종속 |

### Precision Landing 설정

```bash
# PX4 precision landing
param set LNDMC_Z_VEL_MAX 0.5  # 상승속도 제한
param set LNDMC_TRIG_AGL 0.5   # 트리거 고도

# Landing target
param set PLD_BTOUT 5  # Beacon timeout
param set PLD_SRCH_ALT 10  # 검색 고도
```

## Moving Base RTK

### 응용

| 시나리오 | 설명 |
|----------|------|
| **Boat Landing** | 이동하는 플랫폼 착륙 |
| **Follow Me** | RTK 기반 추적 |
| **Dynamic Survey** | 고속 이동 측량 |

### 상대 위치 정확도

```
Absolute accuracy: 저하됨
Relative accuracy (Base-Rover): 유지됨

핵심: Baseline length 제한 (< 30km)
```

## Multi-GNSS

### Constellations

| 시스템 | 위성 | 대역 | 주요지역 |
|--------|------|------|----------|
| **GPS** | USA | L1, L2, L5 | Global |
| **GLONASS** | Russia | L1, L2 | Global |
| **Galileo** | EU | E1, E5a, E5b | Global |
| **BeiDou** | China | B1, B2, B3 | Asia-Pacific |

### Benefits

```
Single constellation: 8-12 satellites
Multi-GNSS (4 systems): 20-30 satellites

장점:
- 가시성 향상 (urban canyon)
- Convergence 속도
- RTK 고정률
```

## Troubleshooting

| 증상 | 원인 | 해결 |
|------|------|------|
| **RTK Float 고정** | 위성 부족 | 개방 공간으로 이동 |
| **Baseline too long** | Base-Rover 거리 | Base 가까이 설치 |
| **No RTCM data** | NTRIP 연결 | 인터넷, 인증 확인 |
| **Multipath error** | Reflections | Ground plane 사용 |
| **Latency high** | Radio 딜레이 | 직접 연결 사용 |

## Performance Metrics

| Metric | Target |
|--------|--------|
| **Horizontal accuracy** | < 5 cm (RTK Fixed) |
| **Vertical accuracy** | < 10 cm (RTK Fixed) |
| **Convergence time** | < 30s (hot start) |
| **Update rate** | 5-10 Hz |
| **Latency** | < 500ms |

## 관련 개념

- [[flight-controller-hardware]] — RTK 모듈 선택
- [[mission-planning]] — 정밀 경로
- [[visual-positioning-odometry]] — VIO + RTK 융합
- [[px4-flight-modes]] — Precision landing mode

## 수집 대상

- 드론 배달 실제 RTK 사용 사례
- PPP-RTK (SSR) 기술 동향
- 대규모 드론 swarm RTK 동기화

## 📰 최근 관련 소식
- 수원시, 광교호수공원서 드론배송 서비스 시연 (nsenior.co.kr, Tue, 04 Au) — https://news.google.com/rss/articles/CBMiY0FVX3lxTE51QjIxRlYxRldxTkVPakZyeERiSVg4RUlVai1WWjBOcUphQzF2cV9vZndmaUZla25PVjN2U1JsYmlxczJVTVVCZmxvSVoxb0xVRXR1WFVJRXU4WDBHT3JrTThJdw?oc=5
- 수원시, 광교호수공원서 드론배송 시연 (뉴시스, Wed, 05 Au) — https://news.google.com/rss/articles/CBMieEFVX3lxTFB6LTBDeVpETTlZZlIzM3Rabnp3eDRMRFQxelhGLUt0NzFIaERuaEpWV2ZXRm5MZE5iUmEwYmFsblJUeEZPaDRzYVplUjNYckh0SlhLd05HRWlXU1VWb190RDBLdllOdDBTbHF6c1VTVk82cXhSdlhTbtIBeEFVX3lxTFB6LTBDeVpETTlZZlIzM3Rabnp3eDRMRFQxelhGLUt0NzFIaERuaEpWV2ZXRm5MZE5iUmEwYmFsblJUeEZPaDRzYVplUjNYckh0SlhLd05HRWlXU1VWb190RDBLdllOdDBTbHF6c1VTVk82cXhSdlhTbg?oc=5
