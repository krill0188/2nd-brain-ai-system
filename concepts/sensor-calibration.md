---
title: Sensor Calibration
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, drone-hw, calibration, IMU, compass, accel, gyro, baro]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# Sensor Calibration

센서 캘리브레이션은 드론의 IMU, Compass, Barometer 등 주요 센서의 정확도를 확보하기 위한 필수 절차다. PX4와 ArduPilot은 QGroundControl을 통해 캘리브레이션을 수행한다.

## 캘리브레이션 대상 센서

| 센서 | 목적 | 캘리브레이션 항목 |
|------|------|------------------|
| **Accelerometer** | 가속도 측정 | Offset, Scale |
| **Gyroscope** | 각속도 측정 | Bias |
| **Magnetometer** | 방향 측정 | Hard/Soft iron |
| **Barometer** | 고도 측정 | Offset |
| **Airspeed** | 대기속도 | Offset, Scale |
| **Optical Flow** | 상대 이동 | Scale, Offset |

## Accelerometer Calibration

### 절차

1. **Level** — 수평 면에 놓기
2. **Left** — 왼쪽 면으로 눕히기
3. **Right** — 오른쪽 면으로 눕히기
4. **Nose Down** — 앞으로 눕히기
5. **Nose Up** — 뒤로 눕히기
6. **Back** — 뒤집기

### QGC 명령

```
Sensors → Accelerometer → Start
```

### 파라미터

| 파라미터 | 설명 |
|----------|------|
| `CAL_ACC0_ID` | Accelerometer ID |
| `CAL_ACC0_OFF{X,Y,Z}` | Offset 값 |
| `CAL_ACC0_SCALE` | Scale 값 |

## Compass Calibration

### 외부 간섭 요인

| 간섭원 | 영향 |
|--------|------|
| **Power wires** | 전류 자기장 |
| **Motors** | DC 모터 자기장 |
| **Metal structures** | 자성 재료 |
| **Electronics** | PCB, 배터리 |

### 절차

1. 모든 축을 따라 360° 회전
2. 여러 방향에서 회전 반복
3. QGC에서 "Accept" 클릭

### 파라미터

| 파라미터 | 설명 |
|----------|------|
| `CAL_MAG0_ID` | Compass ID |
| `CAL_MAG0_OFF{X,Y,Z}` | Hard iron offset |
| `CAL_MAG0_ROT` | Orientation |

## Gyroscope Calibration

### 자동 캘리브레이션

PX4는 부팅 시 자동으로 gyro bias를 측정한다.

```
Sensors → Gyroscope → Start
```

### 주의사항

- **정지 상태**에서 수행
- **진동 없는** 환경
- **온도 안정화** 후

## Barometer Calibration

### 고도 기준 설정

```
Sensors → Barometer → Set Ground Pressure
```

### 파라미터

| 파라미터 | 설명 |
|----------|------|
| `SENS_BARO_QNH` | 해수면 기압 |
| `SENS_BARO_RATE` | 업데이트 속도 |

## Airspeed Calibration

### 피토관 캘리브레이션

1. 피토관이 막히지 않았는지 확인
2. 바람이 없는 환경
3. "Calibrate" 클릭
4. 압력 변화 확인

### 파라미터

| 파라미터 | 설명 |
|----------|------|
| `CAL_AIR_C1` | Offset coefficient |
| `CAL_AIR_C2` | Scale coefficient |

## 온도 캘리브레이션

### Thermal Calibration

센서 온도 변화에 따른 드리프트 보정.

```
# 온도 캘리브레이션 활성화
param set TC_ENABLE 1

# 캘리브레이션 실행
sensors status
```

### 온도 보정 파라미터

| 파라미터 | 설명 |
|----------|------|
| `TC_A0`~`TC_A3` | Accel 온도 계수 |
| `TC_G0`~`TC_G3` | Gyro 온도 계수 |
| `TC_B0`~`TC_B3` | Baro 온도 계수 |

## 캘리브레이션 검증

### Pre-flight Check

```
# 센서 상태 확인
sensors status

# IMU 확인
listener sensor_accel
listener sensor_gyro

# Compass 확인
listener sensor_mag
```

### 정상 범위

| 센서 | 정상 범위 |
|------|----------|
| **Accel** | ±0.1 m/s² (정지 시) |
| **Gyro** | ±0.01 rad/s (정지 시) |
| **Mag** | 지구 자기장 ±20% |
| **Baro** | QNH ±5 hPa |

## 문제 해결

| 증상 | 원인 | 해결 |
|------|------|------|
| **Compass variance** | 간섭 | 재배치, 재캘리브레이션 |
| **Accel clipping** | 충격 | 충격 완화 장치 |
| **Gyro drift** | 온도 | thermal calibration |
| **Baro jump** | 바람, 문 개폐 | 보호 커버 |

## MAVLink 캘리브레이션

```
MAV_CMD_PREFLIGHT_CALIBRATION
- Param 1: Gyro (1=calibrate)
- Param 2: Magnetometer (1=calibrate)
- Param 3: Pressure (1=calibrate)
- Param 5: Accel (1=calibrate)
```

## 관련 개념

- [[px4-flight-modes]] — 센서 기반 모드 제한
- [[drone-safety-failsafe]] — 센서 실패 시 failsafe
- [[flight-controller-hardware]] — 센서 배치

## 수집 대상

- 고급 캘리브레이션 알고리즘
- 실시간 캘리브레이션 방법론
- 센서 융합 튜닝 가이드
