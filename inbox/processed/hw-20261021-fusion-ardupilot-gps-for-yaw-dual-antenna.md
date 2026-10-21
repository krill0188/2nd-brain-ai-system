---
title: "GPS for Yaw / Moving Baseline (ArduPilot docs)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: hardware
source: https://ardupilot.org/copter/docs/common-gps-for-yaw.html
tags: [drone, gnss, 5-GNSS/INS융합]
authors: "ArduPilot 문서"
published: "미확인"
---

## 핵심 내용
이중 안테나 GPS(이동 기준선)로 요 헤딩을 얻는 ArduPilot 설정. 이중 F9P(시리얼/DroneCAN), 단일 유닛(NMEA, Unicore UM982, DroneCAN) 구성과 검증 방법을 설명한다.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 안테나 간격 최소 30 cm: "The antennas must be separated by at least 30cm on the vehicle." (Baseline Recommendations)
- 드라이버 검증: 로버 GPS fix 타입 6(고정 RTK), 측정 거리가 설정 거리의 20% 이내, 높이차가 자세와 20% 이내 일치
- 주요 파라미터: AHRS_EKF_TYPE=3, EK3_ENABLE=1, EK3_SRC1_YAW=2(컴퍼스 병용 시 3), GPS_AUTO_SWITCH는 2(Blend) 금지
- F9P 이중 시리얼: GPS1_TYPE=17(base), GPS2_TYPE=18(rover); DroneCAN: 22/23
- 오프셋: GPS1_MB_OFS_X/Y/Z, GPS1_POS_X/Y/Z(CG 기준)

## 한계·미확인
헤딩 정확도(deg) 수치는 페이지에 없음(미확인).
