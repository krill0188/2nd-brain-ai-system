---
title: "ArduPilot GPS Jamming Mediation (EK3_OPTIONS JammingExpected)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: security
tags: [drone, gnss, ardupilot]
sources: [inbox/processed/hw-20261021-jamming-ardupilot-ekf3-jamming-expected-doc.md]
confidence: medium
contested: false
contradictions: []
---

# ArduPilot GPS Jamming Mediation (EK3_OPTIONS JammingExpected)

- 원문: https://ardupilot.org/copter/docs/common-positioning-landing-page.html^[inbox/processed/hw-20261021-jamming-ardupilot-ekf3-jamming-expected-doc.md]
- 저자: ArduPilot 문서^[inbox/processed/hw-20261021-jamming-ardupilot-ekf3-jamming-expected-doc.md]
- 발행: 미확인 (열람일 2026-10-22)^[inbox/processed/hw-20261021-jamming-ardupilot-ekf3-jamming-expected-doc.md]

## 핵심 내용
ArduPilot GPS/Compass 랜딩 페이지의 "GPS Jamming Mediation" 절. EK3_OPTIONS 의 bit 0("JammingExpected")을 켜면, 추측항법(dead reckoning)이 가능한 상태에서 GPS 락이 2초 넘게 끊겼을 때(재밍 추정) 다시 GPS 를 쓰기 전에 EK3_GPS_CHECK / EK3_CHECK_SCALE 로 제어되는 비행 전 정렬 GPS 품질 검사를 다시 통과해야 한다. 재락 즉시 손상된 GPS 데이터가 사용되는 것을 막기 위한 설정이라고 설명한다.^[inbox/processed/hw-20261021-jamming-ardupilot-ekf3-jamming-expected-doc.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 임계 시간: GPS 락 상실 2초 초과^[inbox/processed/hw-20261021-jamming-ardupilot-ekf3-jamming-expected-doc.md]
- 파라미터: EK3_OPTIONS bit 0, EK3_GPS_CHECK, EK3_CHECK_SCALE^[inbox/processed/hw-20261021-jamming-ardupilot-ekf3-jamming-expected-doc.md]

## 한계·미확인
재밍/스푸핑 탐지 자체나 CRPA 같은 RF 방어는 다루지 않음(EKF 측 완화만). 스푸핑에 대한 효과는 문서에 서술 없음.^[inbox/processed/hw-20261021-jamming-ardupilot-ekf3-jamming-expected-doc.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[kci-dual-nis-sac-gnss-ins-spoofing]]
