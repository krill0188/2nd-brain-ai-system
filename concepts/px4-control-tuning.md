---
title: PX4 Control & Tuning
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, tuning, pid, rate, attitude, position, control]
sources: []
confidence: medium
domain: flight-control
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# PX4 Control & Tuning

PX4는 Rate → Attitude → Velocity → Position 순차적 제어 아키텍처를 사용한다. 각 단계는 PID 컨트롤러로 구성되어 있으며 적절한 튜닝이 안정적 비행의 핵심이다.

## 제어 아키텍처

```
┌─────────────────────────────────────────────────────┐
│                   Position Setpoint                │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│              Position/PID Controller               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │     P       │  │     I       │  │     D       │  │
│  │   Position  │  │   Integral  │  │   Velocity  │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
└──────────────────┬──────────────────────────────────┘
                   │ Velocity Setpoint
                   ▼
┌─────────────────────────────────────────────────────┐
│              Velocity/Acceleration                  │
│              (MPC_XY_VEL_* / MPC_Z_VEL_*)         │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│              Attitude Setpoint                     │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│              Attitude (Quat) Controller            │
│              (MC_ROLLRATE_P, MC_PITCHRATE_P)       │
└──────────────────┬──────────────────────────────────┘
                   │ Rate Setpoint (body rates)
                   ▼
┌─────────────────────────────────────────────────────┐
│              Rate/PID Controller                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │     P       │  │     I       │  │     D       │  │
│  │   Rate      │  │   Rate      │  │   Rate      │  │
│  │   (MC_P/P)  │  │   (MC_I/I)  │  │   (MC_D/D)  │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
└──────────────────┬──────────────────────────────────┘
                   │ Motor commands
```

## PID Controller Basics

### PID 공식

```
u(t) = Kp × e(t) + Ki × ∫e(t)dt + Kd × de(t)/dt

where:
  e(t) = setpoint - current
  Kp = proportional gain
  Ki = integral gain  
  Kd = derivative gain
```

### PID 용어

| 용어 | 효과 | 과도 시 |
|------|------|---------|
| **Kp (P)** | 반응 속도 | 진동, overshoot |
| **Ki (I)** | 정상 상태 오차 제거 | Windup, 느린 settling |
| **Kd (D)** | 댐핑, 안정성 | 노이즈 증폭 |

## Rate Control (가장 내부 루프)

### 구조

```cpp
// Angular rate control
rate_error = rate_setpoint - gyro_measurement;

// PID
P = MC_ROLLRATE_P * rate_error;
I += MC_ROLLRATE_I * rate_error * dt;  // Integrator
D = MC_ROLLRATE_D * rate_derivative;

torque_cmd = P + I + D;
```

### 파라미터

| 파라미터 | 기본값 | 설명 |
|----------|--------|------|
| **MC_ROLLRATE_P** | 0.15 | Roll rate P gain |
| **MC_ROLLRATE_I** | 0.2 | Roll rate I gain |
| **MC_ROLLRATE_D** | 0.003 | Roll rate D gain |
| **MC_PITCHRATE_P** | 0.15 | Pitch rate P gain |
| **MC_PITCHRATE_I** | 0.2 | Pitch rate I gain |
| **MC_PITCHRATE_D** | 0.003 | Pitch rate D gain |
| **MC_YAWRATE_P** | 0.2 | Yaw rate P gain |
| **MC_YAWRATE_I** | 0.1 | Yaw rate I gain |

### Rate Tuning 과정

```
Step 1: P gain 조정
  - P를 천천히 증가
  - 진동 발생 전까지
  - 약간 뒤로

Step 2: D gain 추가
  - 진동 댐핑
  - 너무 높으면 노이즈

Step 3: I gain 조정
  - 정확한 rate 추적
  - Windup 주의
```

## Attitude Control

### 쿼터니언 에러

```
q_error = q_current⁻¹ ⊗ q_setpoint

// 짧은 경로 선택
if (q_error.w < 0) q_error = -q_error;

// Body rate error
rate_setpoint = 2 × q_error.v × MC_ATT_P
```

### 파라미터

| 파라미터 | 기본값 | 설명 |
|----------|--------|------|
| **MC_ROLL_P** | 6.5 | Roll attitude P gain |
| **MC_PITCH_P** | 6.5 | Pitch attitude P gain |
| **MC_YAW_P** | 2.8 | Yaw attitude P gain |

## Velocity & Position Control

### MPC (Multicopter Position Controller)

```
┌─────────────────────────────────────────────────────────┐
│                    MPC_XY_P / MPC_Z_P                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              MPC_XY_VEL_P/I/D                         │
│              MPC_Z_VEL_P/I/D                          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Acceleration → Thrust + Attitude          │
└─────────────────────────────────────────────────────────┘
```

### 파라미터

| 파라미터 | 기본값 | 설명 |
|----------|--------|------|
| **MPC_XY_P** | 0.95 | XY position P |
| **MPC_Z_P** | 1.0 | Z position P |
| **MPC_XY_VEL_P** | 0.09 | XY velocity P |
| **MPC_XY_VEL_I** | 0.02 | XY velocity I |
| **MPC_XY_VEL_D** | 0.01 | XY velocity D |
| **MPC_Z_VEL_P** | 0.2 | Z velocity P |
| **MPC_Z_VEL_I** | 0.02 | Z velocity I |
| **MPC_Z_VEL_D** | 0.0 | Z velocity D |

## Tuning Process

### 1. Rate 모드 튜닝

```bash
# 안전한 환경에서 시작
param set MC_AIRMODE 2  # Roll/pitch priority

# Roll
param set MC_ROLLRATE_P 0.15
param set MC_ROLLRATE_I 0.2
param set MC_ROLLRATE_D 0.003

# Pitch
param set MC_PITCHRATE_P 0.15
param set MC_PITCHRATE_I 0.2
param set MC_PITCHRATE_D 0.003

# Yaw
param set MC_YAWRATE_P 0.2
param set MC_YAWRATE_I 0.1
```

### 2. Attitude 모드 튜닝

```bash
param set MC_ROLL_P 6.5
param set MC_PITCH_P 6.5
param set MC_YAW_P 2.8
```

### 3. Position 모드 튜닝

```bash
param set MPC_XY_P 0.95
param set MPC_XY_VEL_P 0.09
param set MPC_XY_VEL_I 0.02
param set MPC_XY_VEL_D 0.01
```

## Autotune

### 자동 튜닝 기능 (v1.14+)

```
Step 1: 준비
  - Rate 모드 활성화
  - 충분한 공간 확보
  - 배터리 완충

Step 2: Activation
  - SDLOG_PROFILE = 2 (high rate)
  - AUTOTUNE_ATUNE_MODE = 1

Step 3: Excitation
  - 스틱 움직임으로 excitation
  - PX4이 시스템 ID 수행
  - 파라미터 자동 업데이트

Step 4: Verification
  - 안정적 비행 확인
  - Log analysis
```

## Feed-forward & Trajectory

### Jerk-limited Trajectory

```
Setpoint → Jerk limit → Acceleration limit → Velocity limit → Output

파라미터:
- MPC_JERK_MAX
- MPC_ACC_UP/DOWN_MAX
- MPC_XY_VEL_MAX
```

### Feed-forward

```
Output = Feedback(PID) + Feedforward(model-based)

장점:
- 더 빠른 응답
- 더 정확한 추적
- 낮은 feedback gain 가능
```

## Advanced Features

### Airmode (v1.14+)

| 모드 | 설명 |
|------|------|
| **Disabled** | Standard (thrust > 0 required) |
| **Roll/Pitch** | Roll/pitch authority priority |
| **Roll/Pitch/Yaw** | Full 3D authority |

```bash
param set MC_AIRMODE 2
```

### Thrust Curve

```
Thrust = thrust_coefficient × motor_command^exponent

param set THR_MDL_FAC  // 모델링 factor
param set MOT_THST_EXPO  // Thrust curve exponent
```

### Battery Scaling

```bash
param set BAT_V_LOAD_DROP  // Voltage drop compensation
param set BAT_V_SCALE  // Scale factor
```

## Tuning Tools

### QGroundControl

```
Analyze → Log Download
├── Rate setpoint vs actual
├── Attitude tracking
├── Position accuracy
└── Vibration levels
```

### Flight Review

https://logs.px4.io

```
Plots → Controller:
  - rate_controller_status
  - attitude_estimator_status
  - local_position_setpoint
  - local_position
```

### uORB Inspection

```bash
# 실시간 모니터링
listener rate_ctrl_status
listener vehicle_attitude
listener vehicle_local_position
```

## Troubleshooting

| 증상 | 원인 | 해결 |
|------|------|------|
| **진동** | P 너무 높음 | P 감소, D 증가 |
| **느린 응답** | P 너무 낮음 | P 증가 |
| **Drift** | I 너무 낮음 | I 증가 |
| **Overshoot** | D 부족 | D 증가 |
| **떨림** | 노이즈 + D | 필터링, D 감소 |
| **비대칭** | Roll/Pitch 불균형 | 개별 튜닝 |

## 관련 개념

- [[px4-flight-modes]] — 제어 모드
- [[sensor-calibration]] — 센서 정확도
- [[drone-power-battery]] — 배터리 보상
- [[flight-logging-analysis]] — 튜닝 검증

## 수집 대상

- 실제 드론 튜닝 사례 연구
- Model Predictive Control (MPC)
- Adaptive control 방법론
