---
title: PX4 Tuning & Control
created: 2026-07-27
updated: 2026-08-06
type: concept
tags: [drone-sw, tuning, pid, rate, attitude, control, multicopter]
sources: []
confidence: medium
domain: flight-control
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# PX4 Tuning & Control

PX4의 비행 성능을 최적화하기 위한 PID 튜닝과 제어 기법. Rate/Attitude/Position 제어 루프 계층 구조를 이해하고 적절한 게인 값을 설정하는 것이 핵심이다.

## Control Hierarchy

```
┌─────────────────────────────────────────┐
│      Position Controller (Slow)       │
│   P gains: MPC_XY_P, MPC_Z_P          │
│   Output: Position → Velocity setpoint │
└───────────────────┬─────────────────────┘
                    │
┌───────────────────┴─────────────────────┐
│      Velocity Controller (Medium)       │
│   PID: MPC_XY_VEL_P/I/D                │
│   Feedforward: MPC_XY_VEL_FF             │
│   Output: Velocity → Accel/Thrust       │
└───────────────────┬─────────────────────┘
                    │
┌───────────────────┴─────────────────────┐
│      Acceleration → Attitude            │
│   MPC_TILTMAX_AIR, MPC_TILTMAX_LND       │
└───────────────────┬─────────────────────┘
                    │
┌───────────────────┴─────────────────────┐
│      Attitude Controller (Fast)         │
│   P: MC_PITCH_P, MC_ROLL_P, MC_YAW_P   │
│   Output: Attitude → Rate setpoint      │
└───────────────────┬─────────────────────┘
                    │
┌───────────────────┴─────────────────────┐
│      Rate Controller (Fastest)          │
│   PID: MC_PITCHRATE_P/I/D               │
│        MC_ROLLRATE_P/I/D                │
│        MC_YAWRATE_P/I/D                 │
│   Output: Rate → Motor mix              │
└─────────────────────────────────────────┘
```

## Rate Control

### Rate Loop Structure

| 축 | 게인 | 설명 |
|----|------|------|
| **Pitch Rate** | MC_PITCHRATE_P | Pitch 대응 속도 |
| **Roll Rate** | MC_ROLLRATE_P | Roll 대응 속도 |
| **Yaw Rate** | MC_YAWRATE_P | Yaw 대응 속도 |

### Rate PID

```
Output = P * error + I * ∫error + D * d(error)/dt + FF * setpoint

MC_*RATE_P: Proportional gain
MC_*RATE_I: Integral gain
MC_*RATE_D: Derivative gain
MC_*RATE_FF: Feedforward gain
```

### 기본 Rate 게인

| 파라미터 | 소형 쿼드 | 중형 쿼드 | 대형 헥사 |
|----------|-----------|-----------|-----------|
| `MC_PITCHRATE_P` | 0.15 | 0.1 | 0.08 |
| `MC_PITCHRATE_I` | 0.2 | 0.15 | 0.1 |
| `MC_PITCHRATE_D` | 0.003 | 0.003 | 0.002 |
| `MC_PITCHRATE_FF` | 0.0 | 0.0 | 0.0 |

### Rate 튜닝 절차

1. **Manual Rate 모드**로 전환
2. `P` 게인 증가 (진동 직전까지)
3. `I` 게인으로 정착 오차 제거
4. `D` 게인으로 오버슈트 감소
5. **FF**로 미리 보정

### Rate 실패 증상

| 증상 | 원인 | 조치 |
|------|------|------|
| **진동** | P 게인 너무 높음 | P 감소 |
| **느린 반응** | P 게인 낮음 | P 증가 |
| **수동 밀림** | I 게인 낮음 | I 증가 |
| **오버슈트** | D 부족 | D 증가 |
| **소음** | D 너무 높음 | D 감소 |

## Attitude Control

### Attitude P 게인

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `MC_PITCH_P` | Pitch 제어 | 6.5 |
| `MC_ROLL_P` | Roll 제어 | 6.5 |
| `MC_YAW_P` | Yaw 제어 | 2.8 |

### Attitude 튜닝

```
Attitude error → Rate setpoint

MC_*_P가 높을수록:
- 빠른 응답
- 하지만 진동 위험

일반적으로 6-8 범위가 안정적
```

## Velocity Control

### Velocity PID 게인

| 파라미터 | 설명 |
|----------|------|
| `MPC_XY_VEL_P` | XY 속도 P 게인 |
| `MPC_XY_VEL_I` | XY 속도 I 게인 |
| `MPC_XY_VEL_D` | XY 속도 D 게인 |
| `MPC_XY_VEL_FF` | XY 속도 FF 게인 |
| `MPC_Z_VEL_P/I/D/FF` | Z 방향 동일 |

### Velocity 기본값

```
MPC_XY_VEL_P: 0.09
MPC_XY_VEL_I: 0.02
MPC_XY_VEL_D: 0.01
MPC_XY_VEL_FF: 0.0
MPC_XY_VEL_MAX: 12.0 m/s
MPC_Z_VEL_MAX_UP: 3.0 m/s
MPC_Z_VEL_MAX_DN: 1.5 m/s
```

## Position Control

### P 게인

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `MPC_XY_P` | XY 위치 P | 0.95 |
| `MPC_Z_P` | Z 위치 P | 1.0 |

### Tilt Limit

```
MPC_TILTMAX_AIR: 45° (비행 중)
MPC_TILTMAX_LND: 12° (착륙 중)
MPC_TILTMAX_LV: 10° (수준 비행)
```

## Thrust Curve

### 추력 곡선

```
MPC_THR_HOVER: 0.5 (호버 추력, 전체의 %)

Linearization:
MPC_THR_MDL_FAC: 0.0 ~ 1.0 (선형화 계수)
```

### Thrust 설정

| 파라미터 | 설명 |
|----------|------|
| `MPC_THR_MAX` | 최대 추력 |
| `MPC_THR_MIN` | 최소 추력 |
| `MPC_MANTHR_MIN` | 수동 최소 추력 |

## Motor Mixer

### Output Mapping

```
Rotor 1: Front-Right (CW)
Rotor 2: Back-Right (CCW)
Rotor 3: Back-Left (CW)
Rotor 4: Front-Left (CCW)

Mixing:
- Roll: (Right - Left)
- Pitch: (Front - Back)
- Yaw: (CW - CCW) * thrust
- Throttle: Average
```

### Output Scaling

| 파라미터 | 설명 |
|----------|------|
| `PWM_MIN` | 최소 PWM 값 |
| `PWM_MAX` | 최대 PWM 값 |
| `PWM_DISARMED` | 시동 해제 시 |

## Tuning Procedure

### 1. Preparation

```
- SITL에서 먼저 테스트
- 안전한 비행 공간 확보
- 로깅 활성화 (SDLOG_PROFILE = Default)
```

### 2. Rate Tuning

```
Manual → Stabilized → Position (단계별)

Step 1: MC_PITCHRATE_P = 0.05 → 증가 → 진동 시작점 확인
Step 2: 값의 70%로 설정
Step 3: I 게인으로 steady state 제거
Step 4: D 게인으로 오버슈트 튜닝
```

### 3. Attitude Tuning

```
ACRO 모드 테스트:
- 빠른 반응: P 증가
- 부드러움: P 감소
- 일반적: 6-8
```

### 4. Position Tuning

```
Position 모드 테스트:
- 드리프트: P 증가 또는 I 추가
- 진동: P 감소
- 직선 추적: FF 튜닝
```

## Log Analysis

### Key Topics

| 토픽 | 분석 |
|------|------|
| `rate_ctrl_status` | Rate 루프 성능 |
| `vehicle_rates_setpoint` | Rate 명령 vs 실제 |
| `vehicle_attitude` | Attitude 추적 |
| `actuator_outputs` | 모터 출력 |

### QGC Flight Review

```
Analyze → Log Download → PID Analysis

봐야 할 것:
- Setpoint vs Actual (lag, overshoot)
- Motor saturation
- Vibration
```

## Advanced Tuning

### Gain Scheduling

```
속도에 따른 게인 조정:
MPC_XY_CRUISE: 순항 속도별 게인
```

### Feedforward

```
명령 예측:
- FF 게인으로 명령 선행
- 트랙킹 성능 향상
```

### Inertia

```
MC_INERTIA: 관성 보정
대형 기체에 필요
```

## Troubleshooting

| 문제 | 원인 | 해결 |
|------|------|------|
| **Toilet Bowling** | Compass 간섭 | Compass 재캘리브레이션 |
| **Oscillation** | 게인 높음 | 전반적으로 감소 |
| **Sluggish** | 게인 낮음 | Rate P 증가 |
| **Drift** | I 게인 낮음 | I 증가 |
| **High vibration** | 균형 불량 | 프로펠러/모터 정비 |

## QGC Tuning UI

```
QGroundControl → Vehicle Setup → PID Tuning
├── Rate Controller
│   ├── P, I, D sliders
│   └──实时 그래프
├── Attitude Controller
├── Velocity Controller
└── Position Controller

Advanced:
- Export parameters
- Import parameters
- Reset to defaults
```

## MAVSDK Tuning

```cpp
// 파라미터 설정
param.set_param_int("MC_PITCHRATE_P", 15);
param.set_param_int("MC_PITCHRATE_I", 20);
param.set_param_int("MC_PITCHRATE_D", 0);
```

## 관련 개념

- [[px4-flight-modes]] — 모드별 제어 특성
- [[drone-power-battery]] — Thrust-power 관계
- [[flight-logging-analysis]] — 튜닝 검증
- [[px4-simulation]] — SITL 튜닝

## 심화/버전별 문서

- [[px4-control-tuning]] — 제어 튜닝 심화 노트
- [[px4-pid-tuning]] — PID 튜닝 심화 노트
- [[px4-cicd-pipeline]] — PX4 CI/CD 빌드·테스트 파이프라인
- [[px4-v1-17]] — PX4 v1.17 릴리스
- [[param-diff-px4-1-16-0-1-17-0]] — PX4 1.16.0→1.17.0 파라미터 diff
- [[param-diff-copter-4-6-0-4-7-0]] — ArduCopter 4.6.0→4.7.0 파라미터 diff

## 수집 대상

- 실제 드론 튜닝 사례 연구
- Adaptive gain control
- Model predictive control
