---
title: PX4 PID Control Tuning
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, pid, tuning, control, rate, attitude, multicopter]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# PX4 PID Control Tuning

PID(Proportional-Integral-Derivative) 제어는 드론의 안정성과 응답성을 결정하는 핵심 알고리즘이다. Rate loop와 Attitude loop의 계층 구조로 구성된다.

## 제어 루프 계층

```
┌─────────────────────────────────────────┐
│         Position Controller           │
│         (P controller)                │
└───────────────────┬───────────────────┘
                    │
                    ▼ thrust, yaw
┌─────────────────────────────────────────┐
│         Velocity Controller           │
│         (PID + feedforward)           │
└───────────────────┬───────────────────┘
                    │
                    ▼ acceleration
┌─────────────────────────────────────────┐
│         Attitude Controller           │
│         (P controller)                │
└───────────────────┬───────────────────┘
                    │
                    ▼ attitude rate
┌─────────────────────────────────────────┐
│         Rate Controller               │
│         (PID controller)              │
└───────────────────┬───────────────────┘
                    │
                    ▼ torque
┌─────────────────────────────────────────┐
│         Motor Mixer                   │
│         (allocation)                  │
└─────────────────────────────────────────┘
```

## Rate Controller

가장 낮은 단계의 PID 제어. 각축 회전 속도를 제어.

### PID 수식

```
error = setpoint - measured_rate

P_term = Kp * error
I_term += Ki * error * dt
D_term = Kd * (error - last_error) / dt

output = P_term + I_term + D_term
```

### Rate PID 파라미터

| 축 | P Gain | I Gain | D Gain |
|----|--------|--------|--------|
| **Roll Rate** | `MC_ROLLRATE_P` | `MC_ROLLRATE_I` | `MC_ROLLRATE_D` |
| **Pitch Rate** | `MC_PITCHRATE_P` | `MC_PITCHRATE_I` | `MC_PITCHRATE_D` |
| **Yaw Rate** | `MC_YAWRATE_P` | `MC_YAWRATE_I` | `MC_YAWRATE_D` |

### 기본값 (Quad X)

```
MC_ROLLRATE_P: 0.15
MC_ROLLRATE_I: 0.3  
MC_ROLLRATE_D: 0.003

MC_PITCHRATE_P: 0.15
MC_PITCHRATE_I: 0.3
MC_PITCHRATE_D: 0.003

MC_YAWRATE_P: 0.2
MC_YAWRATE_I: 0.1
MC_YAWRATE_D: 0.0
```

## Attitude Controller

자세(roll/pitch/yaw)를 Rate로 변환하는 P controller.

### Attitude Gain

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `MC_ROLL_P` | Roll attitude P gain | 6.5 |
| `MC_PITCH_P` | Pitch attitude P gain | 6.5 |
| `MC_YAW_P` | Yaw attitude P gain | 2.8 |

### Yaw Weight

```
MC_YAW_WEIGHT: 0.4

의미: Yaw 응답을 roll/pitch 대비 낮춤
이유: 멀티콥터의 yaw authority가 상대적으로 낮음
```

## Tuning Process

### 1. Rate Tuning (Manual)

| 단계 | 동작 | 확인 |
|------|------|------|
| **1** | Roll stick twitch | 오버슈트 확인 |
| **2** | 증가 `MC_ROLLRATE_P` | 빠른 응답, 오버슈트 방지 |
| **3** | 증가 `MC_ROLLRATE_D` | 진동 감소 |
| **4** | 조절 `MC_ROLLRATE_I` | 저속 드리프트 제거 |
| **5** | Pitch 반복 | 위와 동일 |
| **6** | Yaw 조절 | P-I 조합 |

### 2. Tuning with Logs

```
Flight Review → Rate Controller

확인 항목:
- Setpoint vs Actual rate
- Tracking error
- Oscillation
```

### 3. Autotune

```bash
# QGC Safety → Enable autotune
# Flight mode switch to autotune
# Drone oscillates automatically
# Lands and saves parameters
```

## PID Effects

| Gain | 증가 시 | 감소 시 |
|------|---------|---------|
| **P** | 빠른 응답, 오버슈트 | 느린 응답, 오프셋 |
| **I** | 드리프트 제거, 오실레이션 | 드리프트, 느린 정복 |
| **D** | 진동 감소, 노이즈 민감 | 진동, 부드러운 응답 |

## 문제 해결

### Oscillation (진동)

| 원인 | 해결 |
|------|------|
| **P 너무 높음** | P 감소 또는 D 증가 |
| **D 너무 높음** | D 감소, 모터 노이즈 확인 |
| **I 너무 높음** | I 감소 |
| **Mechanical** | 프레임 강화, 프로펠 밸런스 |

### Sluggish (둔함)

| 원인 | 해결 |
|------|------|
| **P 너무 낮음** | P 증가 |
| **Thrust insufficient** | 모터/ESC 업그레이드 |
| **Weight too high** | 무게 감소 |

### Yaw drift

```
MC_YAWRATE_I 증가
또는
MC_YAW_P 증가 (주의: 다른 축에 영향)
```

## Feedforward

Setpoint 변화에 선행 응답.

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `MC_ROLLRATE_FF` | Roll feedforward | 0.0 |
| `MC_PITCHRATE_FF` | Pitch feedforward | 0.0 |
| `MC_YAWRATE_FF` | Yaw feedforward | 0.0 |

### 사용 예시

```
빠른 스틱 입력이 필요할 때:
- Acro mode
- FPV racing
- Aggressive flight

설정: FF = 0.5-1.0
```

## Thrust Curve

### Linearization

```
MC_THR_HOVER: 0.5 (50% throttle = hover)

Thrust curve compensation
"": """"""""""""""""""""""""
```

## MC PID Tuning In-flight

### RC Tuning

```
Parameter: RC_TUNING_ENABLE

Tuning knob mapping:
- Channel 5: Roll rate P
- Channel 6: Pitch rate P
```

## Log Analysis

### Key Messages

| Topic | 확인 항목 |
|-------|----------|
| `rate_ctrl_status` | PID output |
| `actuator_controls` | Output to mixer |
| `sensor_combined` | Gyro data |

### FFT Analysis

```python
# 진동 주파수 분석
import numpy as np
from scipy.fft import fft

# Gyro data FFT
freqs = np.fft.fftfreq(len(gyro_data), dt)
fft_vals = np.abs(fft(gyro_data))

# 모터 주파수 확인 (Hz = RPM/60)
```

## Vehicle-specific Tuning

### Small Quad (<250mm)

```
P: 더 높게 (빠른 응답)
D: 더 높게 (진동 제어)
I: 낮게 (저항력 감소)
```

### Large Hex/Octo (>650mm)

```
P: 더 낮게 (느린 응답)
I: 더 높게 (비행안정)
D: 중간값
```

### Heavy Lifter

```
P: 낮음 (느린 응답)
I: 높음 (위상 유지)
Thrust headroom 확인
```

## Filter Settings

### D-term Notch Filter

```
MC_DTERM_CUTOFF: 30

목적: D-term 노이즈 제거
효과: 모터 진동 감소
```

## 관련 개념

- [[px4-offboard-control]] — 외부 controller 통합
- [[drone-simulation]] — SITL에서 tuning
- [[flight-logging-analysis]] — Log 분석
- [[px4-flight-modes]] — Manual/Acro mode

## 수집 대상

- 실제 튜닝 사례 연구
- MPC (Model Predictive Control)
- Adaptive control
