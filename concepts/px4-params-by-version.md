---
title: "PX4 버전별 주요 파라미터 변경점 (v1.14~v1.17)"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, flight-control, px4, parameter, version]
sources: [PX4 공식 릴리즈노트 기반 정리]
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# PX4 버전별 주요 파라미터 변경점 (v1.14~v1.17)

PX4는 마이너 버전마다 파라미터가 신설·개명·폐기된다. **업그레이드 후 QGC에서 파라미터 diff 확인이 필수**다. 보드별 설정은 [[fc-vendor-param-guide]] 참조.

## v1.14 (2023)

- 배터리 파라미터 `BAT_*` → `BAT1_*`/`BAT2_*` 다중 배터리 체계 정착
- `SYS_MC_EST_GROUP` 폐기 → EKF2 단일화 (`EKF2_EN`)
- Dynamic control allocation 도입: `CA_*` 계열 신설 (`CA_ROTOR_COUNT`, `CA_ROTORn_*`) — 믹서 파일 폐지의 시작

## v1.15 (2024)

- 액추에이터 설정 QGC UI 통합 — `PWM_MAIN_*`/`PWM_AUX_*` 대신 `PWM_MAIN_FUNCn`·`CA_*` 조합이 표준
- `MPC_LAND_SPEED` 등 착륙 프로파일 세분화, `COM_OBL_RC_ACT` 폐기 계열 정리
- EKF2 다중 인스턴스 기본화: `EKF2_MULTI_IMU`, `SENS_IMU_MODE`

## v1.16 (2025)

- `FD_*` (Failure Detector) 확장 — `FD_ACT_EN` 액추에이터 고장 감지
- Fixed-wing TECS 재정리: `FW_T_*` 일부 기본값 변경 (업그레이드 시 고도 유지 거동 재튜닝 권장)
- `RC_CRSF_TEL_EN` 등 CRSF 텔레메트리 정식화

## v1.17 (2026-05)

- **Altitude Cruise 모드** 신설 관련: `MPC_CRUISE_*` 계열 (멀티콥터 스틱 릴리스 시 순항 유지)
- Fixed Wing Takeoff 개선: 내비 손실 시 수평 유지 상승 — `FW_TKO_*` 확장
- ROS2/uXRCE-DDS 통합 강화: `UXRCE_DDS_*` 기본 활성 보드 확대
- 신규 INS 드라이버 추가에 따른 `SENS_EN_*` 항목 증가

## 업그레이드 체크리스트

1. 현재 파라미터 파일 백업 (QGC → Tools → Save)
2. 펌웨어 업그레이드 → 기본값 리셋 권장 (메이저 점프 시 필수)
3. 백업본에서 기체 종속값만 선별 복원 (배율·방향·튜닝 게인)
4. 폐기 파라미터 경고(QGC 상단 배너) 전부 해소 후 시험 비행

## 공식 참조

- 릴리즈노트: https://github.com/PX4/PX4-Autopilot/releases
- 파라미터 레퍼런스(버전 선택 가능): https://docs.px4.io/main/en/advanced_config/parameter_reference.html
