---
title: PID Tuning & Control Theory
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, PID, tuning, control, rate, attitude, multicopter, stability]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# PID Tuning & Control Theory

PID(Proportional-Integral-Derivative) 제어는 드론의 자세와 속도를 안정적으로 제어하는 핵심 알고리즘이다. 적절한 튜닝은 비행 성능과 안전성을 결정한다.

## Control Hierarchy

```
┌─────────────────────────────────────────┐
│         Position Controller           │
│    (P controller, NED frame)         │
└───────────────────┬───────────────────┘
                    │ Thrust + Attitude setpoint
                    ▼
┌─────────────────────────────────────────┐
│         Attitude Controller           │
│    (P controller, quaternion)          │
└───────────────────┬───────────────────┘
                    │ Rate setpoint
                    ▼
┌─────────────────────────────────────────┐
│          Rate Controller              │
│    (PID controller, body rates)        │
└───────────────────┬───────────────────┘
                    │ Torque
                    ▼
┌─────────────────────────────────────────┐
│         Motor Mixer                   │
│    ( thrust allocation )              │
└─────────────────────────────────────────┘
```

## Rate Control (Inner Loop)

### PID Controller

```
error = setpoint - measurement

P = Kp × error
I = Ki × ∫error dt
D = Kd × d(error)/dt

output = P + I + D
```

### PX4 Rate PID

| Axis | P | I | D |
|------|---|---|---|
| **Roll** | `MC_ROLLRATE_P` | `MC_ROLLRATE_I` | `MC_ROLLRATE_D` |
| **Pitch** | `MC_PITCHRATE_P` | `MC_PITCHRATE_I` | `MC_PITCHRATE_D` |
| **Yaw** | `MC_YAWRATE_P` | `MC_YAWRATE_I` | `MC_YAWRATE_D` |

### Derivative Filter

```
Low-pass filter on D term:
D_filtered = D_prev + (D_raw - D_prev) × (dt / (τ + dt))

τ = time constant (default: 0.01s)
```

## Attitude Control (Middle Loop)

### Quaternion Error

```
q_error = q_desired ⊗ q_current⁻¹

Where:
- ⊗ = quaternion multiplication
- q_current⁻¹ = conjugate (inverse)

Attitude error vector:
[roll_error, pitch_error, yaw_error] = 2 × [q_x, q_y, q_z] / q_w
```

### Attitude Gains

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `MC_ROLL_P` | Roll proportional | 0.15 |
| `MC_PITCH_P` | Pitch proportional | 0.15 |
| `MC_YAW_P` | Yaw proportional | 2.8 |

## Position Control (Outer Loop)

### P Controller

```
velocity_setpoint = Kp_pos × (position_setpoint - position_current)

thrust_setpoint = mass × (Kp_vel × velocity_error + gravity_compensation)
```

### Position Gains

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `MPC_XY_P` | XY position P | 0.95 |
| `MPC_Z_P` | Z position P | 1.0 |
| `MPC_XY_VEL_P` | XY velocity P | 0.09 |
| `MPC_Z_VEL_P` | Z velocity P | 0.2 |

## Tuning Procedure

### 1. Rate Tuning (Acro/Stabilized)

```
Step 1: Set I = D = 0, start with small P
Step 2: Increase P until oscillation
Step 3: Reduce P by 30%
Step 4: Increase D to dampen oscillation
Step 5: Increase I to eliminate steady-state error
```

### 2. Attitude Tuning

```
Step 1: Rate loop stable 확인
Step 2: Increase attitude P
Step 3: Check for overshoot
Step 4: Balance between response and stability
```

### 3. Position Tuning

```
Step 1: Attitude loop stable 확인
Step 2: Tune velocity loop
Step 3: Tune position loop
Step 4: Check for drift and overshoot
```

## Tuning Indicators

| Symptom | Cause | Fix |
|-----------|-------|-----|
| **Oscillation** | P too high | Reduce P, increase D |
| **Sluggish** | P too low | Increase P |
| **Drift** | I too low | Increase I |
| **Noise** | D too high | Reduce D, add filter |
| **Overshoot** | D too low | Increase D |

## Advanced Tuning

### Feedforward

```
output = PID + Kff × setpoint_rate

Kff = feedforward gain
```

| 파라미터 | 설명 |
|----------|------|
| `MC_ROLLRATE_FF` | Roll rate feedforward |
| `MC_PITCHRATE_FF` | Pitch rate feedforward |
| `MC_YAWRATE_FF` | Yaw rate feedforward |

### Integral Limits

```
Anti-windup: Limit I term accumulation

MC_ROLLRATE_I_MAX
MC_PITCHRATE_I_MAX
MC_YAWRATE_I_MAX
```

### Setpoint Weight

```
Error calculation weighting:
error = (1 - weight) × setpoint - measurement

MC_ROLLRATE_K (default: 1.0)
MC_PITCHRATE_K (default: 1.0)
```

## Multicopter Mixer

### Motor Layout

```
Quad X:
    M1(CW)    M2(CCW)
       \      /
        \    /
         \  /
          FC
         /  \
        /    \
       /      \
    M4(CCW)   M3(CW)

Rotation: M1, M3 = CW
          M2, M4 = CCW
```

### Thrust Allocation

```
[thrust; roll; pitch; yaw] = mixer_matrix × [M1, M2, M3, M4]

M1 = thrust - roll + pitch - yaw
M2 = thrust + roll + pitch + yaw
M3 = thrust + roll - pitch - yaw
M4 = thrust - roll - pitch + yaw
```

## Autotune

### QGroundControl Autotune

```
1. Connect vehicle
2. Go to Vehicle Setup → PID Tuning
3. Select "Automatic" mode
4. Follow prompts (aggressive movements)
5. Review and accept results
```

### Manual Tuning Flight Test

| Test | Mode | What to check |
|------|------|---------------|
| **Rate** | Acro | Quick stick inputs, check oscillation |
| **Attitude** | Stabilized | Step inputs, check overshoot |
| **Position** | Position | Hold position, check drift |
| **Yaw** | Any | Quick yaw, check overshoot |

## Logging for Tuning

### Key uORB Topics

| Topic | Content |
|-------|---------|
| `rate_ctrl_status` | Rate controller output |
| `vehicle_attitude_setpoint` | Desired attitude |
| `vehicle_attitude` | Actual attitude |
| `actuator_outputs` | Motor outputs |

### Analysis

```python
# Check tracking error
attitude_error = attitude_setpoint - attitude_actual

# Check for saturation
saturation = np.abs(actuator_outputs) > 0.95
```

## VTOL Tuning

### Transition

```
Fixed-wing ↔ Multicopter transition tuning:

MPC_XY_CRUISE    # Cruise speed
VT_ARSP_TRANS    # Transition airspeed
VT_F_TRANS_DUR   # Transition duration
```

### Blended Control

```
During transition:
- Multicopter: 100% → 0%
- Fixed-wing: 0% → 100%

Weight based on airspeed
```

## Troubleshooting

| Issue | Diagnostic | Solution |
|-------|------------|----------|
| **Toilet bowl** | Yaw/roll coupling | Check motor alignment, re-calibrate |
| **Wobble** | Mechanical resonance | Add damping, reduce D |
| **Yaw drift** | Compass interference | Relocate compass, calibrate |
| **Altitude drop** | Thrust insufficient | Check battery, increase MOT_THST_HOVER |

## Tools

| Tool | Purpose |
|------|---------|
| **QGC Tuning** | GUI parameter adjustment |
| **Flight Review** | Log analysis |
| **MAVSDK** | Automated testing |
| **MATLAB/Simulink** | Simulation |

## 관련 개념

- [[px4-flight-modes]] — Mode-specific tuning
- [[px4-offboard-control]] — Setpoint generation
- [[drone-simulation]] — Safe tuning environment
- [[flight-logging-analysis]] — Tuning validation

## 수집 대상

- 실제 튜닝 사례 연구
- Adaptive gain scheduling
- Model predictive control (MPC)
