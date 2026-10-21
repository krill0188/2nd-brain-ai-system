---
title: "GPS / GNSS How it works (ArduPilot docs)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
ontology_class: GNSS
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-env-ardupilot-gps-how-it-works-doc.md]
confidence: medium
contested: false
contradictions: []
---

# GPS / GNSS How it works (ArduPilot docs)

- 원문: https://ardupilot.org/copter/docs/common-gps-how-it-works.html^[inbox/processed/hw-20261021-env-ardupilot-gps-how-it-works-doc.md]
- 저자: ArduPilot 문서^[inbox/processed/hw-20261021-env-ardupilot-gps-how-it-works-doc.md]
- 발행: 미확인^[inbox/processed/hw-20261021-env-ardupilot-gps-how-it-works-doc.md]

## 핵심 내용
GNSS 기본 원리와 오차 요인 해설. L1(1575.42 MHz), L2(1227.60 MHz) 설명, 멀티패스와 전리층 교란, 환경별 정확도 표, 보정 방식(SBAS, RTK) 요약. 다중 GNSS 수신이 멀티패스 필터링에 유리하다고 설명한다.^[inbox/processed/hw-20261021-env-ardupilot-gps-how-it-works-doc.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 환경별 3D 정확도/가용성: 개활지 2.5 m / 99%, 심한 멀티패스(건물 사이 등) 26 m / 83%, 실내 55 m / 14%^[inbox/processed/hw-20261021-env-ardupilot-gps-how-it-works-doc.md]
- 무료 SBAS로 미터급, 유료 서비스로 데시미터급(DGPS), RTK는 센티미터~밀리미터급^[inbox/processed/hw-20261021-env-ardupilot-gps-how-it-works-doc.md]
- "As a general rule only clear sky view is safe enough for Auto missions !" (Placement 관련 절)^[inbox/processed/hw-20261021-env-ardupilot-gps-how-it-works-doc.md]

## 한계·미확인
표의 출처·시험 조건 미기재. HDOP 기준값·최소 위성 수는 이 페이지에 없음.^[inbox/processed/hw-20261021-env-ardupilot-gps-how-it-works-doc.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
