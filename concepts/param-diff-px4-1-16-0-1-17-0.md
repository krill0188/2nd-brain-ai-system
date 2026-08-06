---
title: "PX4 v1.16.0 → v1.17.0 파라미터 변경 전체 목록"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, flight-control, parameter, diff, px4]
sources: [공식 파라미터 메타데이터 자동 diff]
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# PX4 v1.16.0 → v1.17.0 파라미터 변경 전체 목록

> 공식 메타데이터 자동 비교 (생성일 2026-07-30). 개요 해설은 [[px4-params-by-version]] 참조. 튜닝 배경은 [[px4-tuning-control]] 참조.

## 요약

| 구분 | 개수 |
|---|---|
| v1.16.0 총 파라미터 | 1933 |
| v1.17.0 총 파라미터 | 1912 |
| ➕ 신규 | 40 |
| ➖ 삭제 | 61 |
| 🔧 기본값 변경 | 13 |

## ➕ 신규 파라미터 (40)

**Actuator Outputs** (9): `PWM_AUX_CENT1`, `PWM_AUX_CENT2`, `PWM_AUX_CENT3`, `PWM_AUX_CENT4`, `PWM_AUX_CENT5`, `PWM_AUX_CENT6`, `PWM_AUX_CENT7`, `PWM_AUX_CENT8`, `PWM_AUX_CENT9`

**Airspeed Validator** (1): `ASPD_FALLBACK`

**EKF2** (3): `EKF2_AGP_MODE`, `EKF2_GPS_MODE`, `EKF2_REQ_FIX`

**FW Performance** (1): `FW_AIRSPD_FLP_SC`

**GPS** (1): `GPS_CFG_WIPE`

**MAVLink** (2): `MAV_S_FORWARD`, `MAV_S_MODE`

**Magnetometer** (3): `BMM350_AVG`, `BMM350_DRIVE`, `BMM350_ODR`

**Manual Control** (1): `MAN_DEADZONE`

**RC** (2): `RC_CRSF_TEL_EN`, `RC_GHST_TEL_EN`

**Radio Switches** (2): `RC_MAP_TERM_SW`, `RC_PAYLOAD_MIDTH`

**Rover Rate Control** (3): `RO_YAW_EXPO`, `RO_YAW_RATE_CORR`, `RO_YAW_SUPEXPO`

**Rover Velocity Control** (1): `RO_SPEED_RED`

**SD Logging** (1): `SDLOG_BACKEND`

**Sensors** (2): `SENS_BAR_AUTOCAL`, `SENS_EN_AUAVX`

**Serial** (5): `RC_CRSF_PRT_CFG`, `RC_DSM_PRT_CFG`, `RC_GHST_PRT_CFG`, `RC_SBUS_PRT_CFG`, `SER_RC_BAUD`

**System** (1): `SYS_HF_MAV`

**UAVCAN** (1): `UAVCAN_ESC_IFACE`

**UXRCE-DDS Client** (1): `UXRCE_DDS_NS_IDX`

## ➖ 삭제된 파라미터 (61)

**Airspeed Validator** (1): `ASPD_FALLBACK_GW`

**Autotune** (1): `FW_AT_SYSID_AMP`

**Commander** (1): `COM_POSCTL_NAVL`

**EKF2** (1): `EKF2_RNG_A_IGATE`

**FW NPFG Control** (4): `NPFG_EN_MIN_GSP`, `NPFG_GSP_MAX_TK`, `NPFG_TRACK_KEEP`, `NPFG_WIND_REG`

**Multicopter Position Control** (4): `MPC_HOLD_DZ`, `MPC_XY_MAN_EXPO`, `MPC_YAW_EXPO`, `MPC_Z_MAN_EXPO`

**RC Input** (1): `RC_INPUT_PROTO`

**Radio Calibration** (18): `RC10_DZ`, `RC11_DZ`, `RC12_DZ`, `RC13_DZ`, `RC14_DZ`, `RC15_DZ`, `RC16_DZ`, `RC17_DZ`, `RC18_DZ`, `RC1_DZ`, `RC2_DZ`, `RC3_DZ`, `RC4_DZ`, `RC5_DZ`, `RC6_DZ`, `RC7_DZ`, `RC8_DZ`, `RC9_DZ`

**Runway Takeoff** (2): `RWTO_HDG`, `RWTO_NPFG_PERIOD`

**SD Logging** (3): `SDLOG_ALGORITHM`, `SDLOG_EXCH_KEY`, `SDLOG_KEY`

**Sensors** (3): `SENS_CM8JL65_CFG`, `SENS_CM8JL65_R_0`, `SENS_EN_TRANGER`

**Serial** (1): `RC_PORT_CONFIG`

**UAVCAN GNSS** (5): `gnss.dyn_model`, `gnss.old_fix_msg`, `gnss.warn_dimens`, `gnss.warn_sats`, `uavcan.pubp-pres`

**UAVCAN Motor Parameters** (16): `ctl_bw`, `ctl_dir`, `ctl_gain`, `ctl_hz_idle`, `ctl_start_rate`, `esc_index`, `id_ext_status`, `int_ext_status`, `int_status`, `mot_i_max`, `mot_kv`, `mot_ls`, `mot_num_poles`, `mot_rs`, `mot_v_accel`, `mot_v_max`

## 🔧 기본값 변경 (13)

| 파라미터 | 이전 | 변경 |
|---|---|---|
| `ASPD_WERR_THR` | 0.55 | 2. |
| `COM_FLTT_LOW_ACT` | 3 | 0 |
| `EKF2_GPS_CHECK` | 1023 | 2047 |
| `EKF2_MIN_RNG` | 0.1 | 0.01 |
| `FW_AT_SYSID_F1` | 20. | 10. |
| `FW_AT_SYSID_TYPE` | 0 | 1 |
| `IMU_DGYRO_CUTOFF` | 30.0 | 20.0 |
| `INA238_SHUNT` | 0.0003 | 0.0005 |
| `MAV_PROTO_VER` | 0 | 2 |
| `MC_PITCH_P` | 6.5 | 4.0 |
| `MC_ROLL_P` | 6.5 | 4.0 |
| `MPC_YAWRAUTO_ACC` | 60. | 20. |
| `MPC_YAWRAUTO_MAX` | 45. | 60. |

> ⚠️ 업그레이드 후 백업 파라미터 파일과 diff하여 기체 종속값을 재확인할 것.