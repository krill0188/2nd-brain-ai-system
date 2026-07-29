---
title: Flight Logging & Analysis
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, logging, ulog, flight-review, analysis, debugging]
sources: []
confidence: medium
domain: flight-control
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# Flight Logging & Analysis

비행 로깅은 드론의 센서 데이터, 제어 출력, 상태 정보를 기록하여 분석과 디버깅에 활용하는 기능이다. PX4는 uORB 기반 ULog 포맷을 사용한다.

## 로깅 시스템

```
┌─────────────────────────────────────────┐
│           uORB Messages               │
│  Sensor │ Control │ Estimator │ State │
└─────────┴─────────┴─────────┴─────────┘
            │
            ▼
┌─────────────────────────────────────────┐
│           Logger Module               │
│  - Subscription selection             │
│  - Buffer management                  │
│  - File writing                       │
└─────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────┐
│           Storage                     │
│  SD Card │ RAM │ MAVLink stream       │
└─────────────────────────────────────────┘
```

## ULog 포맷

PX4의 기본 로그 포맷. 이진 형식으로 효율적인 저장.

| 특성 | 설명 |
|------|------|
| **Format** | Binary |
| **Extension** | .ulg |
| **Compression** | Optional |
| **Compatibility** | PX4 Flight Review, pyulog |

### ULog 구조

```
Header (16 bytes)
├── Magic (4 bytes): 0x55 0x4C 0x6F 0x67 ("ULog")
├── Version (1 byte)
└── Flags (1 byte)

Definitions
├── Message formats
├── Parameter definitions
└── Subscription list

Data
├── Timestamped messages
└── Dropouts (if any)
```

## 로그 구성

### 기본 구독 항목

| 토픽 | 설명 | 비율 |
|------|------|------|
| `sensor_combined` | 통합 센서 | 100Hz |
| `vehicle_attitude` | 자세 추정 | 250Hz |
| `vehicle_local_position` | 로컬 위치 | 100Hz |
| `vehicle_global_position` | 글로벌 위치 | 50Hz |
| `actuator_outputs` | 액추에이터 출력 | 250Hz |
| `vehicle_status` | 기체 상태 | 2Hz |

### 로그 레벨

| 레벨 | 설명 |
|------|------|
| **Default** | 기본 구독 |
| **Debug** | 추가 디버그 토픽 |
| **Full** | 모든 토픽 |

## 로깅 설정

### 파라미터

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `SDLOG_MODE` | 로깅 모드 | 0 (boot부터) |
| `SDLOG_PROFILE` | 프로파일 | Default |
| `SDLOG_MISSION` | 미션만 | 0 |

### 로깅 모드

| 모드 | 설명 |
|------|------|
| `0` | 부팅부터 시작 |
| `1` | 시동 시 시작 |
| `2` | ARM 시 시작 |

### CLI 명령

```bash
# 로거 상태
logger status

# 로깅 시작
logger start

# 로깅 중지
logger stop

# 로깅 on/off
logger on
logger off
```

## 로그 다운로드

### SD Card

```
/sdcard/log/
├── 2024-01-15/
│   ├── 08_30_00.ulg
│   └── 09_15_30.ulg
└── 2024-01-16/
    └── 10_00_00.ulg
```

### MAVLink 다운로드

```
MAV_CMD_LOGGING_START
MAV_CMD_LOGGING_STOP
LOG_REQUEST_DATA
LOG_DATA
```

## Flight Review

PX4의 웹 기반 로그 분석 도구.

### URL

https://logs.px4.io

### 기능

| 기능 | 설명 |
|------|------|
| **3D View** | 3D 비행 경로 |
| **Plots** | 시계열 그래프 |
| **Parameters** | 파라미터 변경 이력 |
| **GPS** | GPS 품질 |
| **Vibration** | 진동 분석 |
| **Control** | 제어 루프 성능 |

### 업로드 방법

1. SD 카드에서 .ulg 파일 복사
2. https://logs.px4.io 접속
3. 파일 업로드
4. 분석 결과 확인

## pyulog

Python 기반 ULog 처리 라이브러리.

### 설치

```bash
pip install pyulog
```

### 사용

```python
from pyulog import ULog

# 로그 열기
log = ULog('flight.ulg')

# 데이터 추출
data = log.get_dataset('vehicle_attitude')
timestamps = data.data['timestamp']
q = data.data['q']

# CSV로 변환
ulog2csv flight.ulg -o output.csv
```

### CLI 도구

| 명령 | 설명 |
|------|------|
| `ulog_info` | 로그 정보 |
| `ulog_messages` | 메시지 추출 |
| `ulog_params` | 파라미터 추출 |
| `ulog2csv` | CSV 변환 |
| `ulog2kml` | KML 변환 |

## 로그 분석 시나리오

### 1. 비행 문제 디버깅

| 증상 | 확인 항목 |
|------|----------|
| **진동** | `sensor_accel`, `actuator_outputs` |
| **드리프트** | `vehicle_attitude`, `magnetometer` |
| **위치 오차** | `vehicle_global_position`, `gps` |
| **배터리 급감** | `battery_status` |

### 2. 튜닝 검증

| 항목 | 확인 토픽 |
|------|----------|
| **PID 성능** | `rate_ctrl_status` |
| **추적 오차** | `vehicle_attitude_setpoint` vs `vehicle_attitude` |
| **위치 제어** | `vehicle_local_position_setpoint` |

### 3. 안전 분석

| 항목 | 확인 |
|------|------|
| **Failsafe** | `vehicle_status`, `commander_state` |
| **Geofence** | `vehicle_status` flags |
| **Arming** | `actuator_armed` |

## 로그 품질

### Dropout

로그 기록 중 데이터 손실.

| 원인 | 해결 |
|------|------|
| **SD 카드 느림** | 고속 SD 카드 사용 |
| **버퍼 부족** | 로그 레벨 감소 |
| **CPU 부하** | 로그 토픽 선택 |

### 메시지 손실

```
logger: dropout detected
```

## 실시간 로깅

### MAVLink 스트리밍

```
LOGGING_DATA
LOGGING_DATA_ACKED
```

### ROS2 로깅

```python
import rclpy
from px4_msgs.msg import SensorCombined

class LoggerNode:
    def __init__(self):
        self.subscription = self.create_subscription(
            SensorCombined, '/fmu/out/sensor_combined',
            self.callback, 10)
        
        # 로그 파일
        self.log_file = open('ros2_log.csv', 'w')
    
    def callback(self, msg):
        self.log_file.write(f"{msg.timestamp},{msg.accelerometer_m_s2[0]}\n")
```

## 관련 개념

- [[px4-architecture-deep]] — uORB 로깅
- [[drone-safety-failsafe]] — 안전 이벤트 로그
- [[sensor-calibration]] — 캘리브레이션 검증

## 수집 대상

- 실제 비행 로그 분석 사례
- 고급 로그 시각화 도구
- ML 기반 이상 탐지 방법론
