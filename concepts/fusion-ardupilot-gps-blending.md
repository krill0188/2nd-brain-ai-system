---
title: "GPS Blending / Dual GPS (ArduPilot docs)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
ontology_class: GNSS
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-fusion-ardupilot-gps-blending.md]
confidence: medium
contested: false
contradictions: []
---

# GPS Blending / Dual GPS (ArduPilot docs)

- 원문: https://ardupilot.org/copter/docs/common-gps-blending.html^[inbox/processed/hw-20261021-fusion-ardupilot-gps-blending.md]
- 저자: ArduPilot 문서^[inbox/processed/hw-20261021-fusion-ardupilot-gps-blending.md]
- 발행: 미확인^[inbox/processed/hw-20261021-fusion-ardupilot-gps-blending.md]

## 핵심 내용
두 GPS의 측정을 혼합해 단일 GPS 글리치 영향을 줄이는 기능. 위치·속도 정확도를 보고하는 장치만 혼합 가능(u-blox 가능, NMEA 일반적으로 불가). 정확도 스케일이 제조사마다 달라 같은 제조사 2개 사용을 권장한다.^[inbox/processed/hw-20261021-fusion-ardupilot-gps-blending.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- GPS2_TYPE=1(AUTO) 또는 해당 타입, GPS_AUTO_SWITCH=2(Blend) / 1(UseBest)^[inbox/processed/hw-20261021-fusion-ardupilot-gps-blending.md]
- 로그: GPS 인스턴스 0=첫째, 1=둘째, 2=혼합 출력^[inbox/processed/hw-20261021-fusion-ardupilot-gps-blending.md]

## 한계·미확인
지연/전환 지연 파라미터 문서화 없음(미확인).^[inbox/processed/hw-20261021-fusion-ardupilot-gps-blending.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
