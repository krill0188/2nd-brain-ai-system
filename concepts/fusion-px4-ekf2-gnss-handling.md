---
title: "PX4 EKF2 tuning: GNSS fusion control, quality gates, dual receivers (PX4 User Guide)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
ontology_class: PX4
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]
confidence: medium
contested: false
contradictions: []
---

# PX4 EKF2 tuning: GNSS fusion control, quality gates, dual receivers (PX4 User Guide)

- 원문: https://docs.px4.io/main/en/advanced_config/tuning_the_ecl_ekf.html^[inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]
- 저자: PX4 문서^[inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]
- 발행: 미확인 (main 브랜치)^[inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]

## 핵심 내용
PX4 EKF2의 GNSS 사용 방식. EKF2_GPS_CTRL 비트마스크(기본 7: 경도/위도/고도/속도, 비트3=+8로 GPS 요 헤딩), EKF2_GPS_MODE(0 자동, 1 데드레코닝), GNSS 품질 게이트(GNSS_CHECK, GNSS_REQ_*), 이중 수신기 선택(SENS_GNSS_PRIME)을 설명한다.^[inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- GNSS_REQ_TIME 기본 10 s 동안 유지 시 GNSS 데이터 수용^[inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]
- 최소 조건: EPH < 3 m, EPV < 5 m, 위성 >= 6, SACC < 0.5 m/s, 3D fix 이상, PDOP < 2.5, 수평 드리프트 < 0.1 m/s, 수직 드리프트 < 0.2 m/s^[inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]
- SENS_GNSS_PRIME: 기본은 메인 시리얼 GPS, -1이면 동등 우선순위; 2초간 미발행 수신기는 제외^[inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]
- 수신기 전환 시 EKF가 수평 위치를 새 수신기로 리셋^[inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]
- EKF2_DELAY_MAX는 각 EKF2_*_DELAY 최댓값 이상이어야 함^[inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]

## 한계·미확인
페이지 후반 40,297자 미열람. EKF2_GPS_DELAY, 노이즈 파라미터 값은 확인 못 함(미확인).^[inbox/processed/hw-20261021-fusion-px4-ekf2-gnss-handling.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
