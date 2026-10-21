---
title: "RTK GPS (PX4 User Guide)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
ontology_class: GNSS
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]
confidence: medium
contested: false
contradictions: []
---

# RTK GPS (PX4 User Guide)

- 원문: https://docs.px4.io/main/en/gps_compass/rtk_gps.html^[inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]
- 저자: PX4 문서^[inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]
- 발행: 미확인 (main 브랜치)^[inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]

## 핵심 내용
PX4 RTK 구성 문서. 기지국(QGroundControl 연결)과 로버(기체) 2대의 RTK GNSS가 필요하고, QGC가 Survey-In을 자동 시작해 수 분 걸린다. 완료되면 기체 GPS가 RTK 모드(3D RTK GPS Lock)로 전환된다. 이중 안테나/이동 기준국 헤딩 설정도 포함.^[inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- RTK는 센티미터급 정확도, 기본값 EKF2_GPS_V_NOISE/EKF2_GPS_P_NOISE는 미터급 가정이므로 0.2로 낮출 필요가 있을 수 있음^[inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]
- GPS 헤딩 안테나 간격 최소 30 cm(또는 제조사 사양), 보고된 기선 길이가 설정 이격의 20% 이내일 때만 헤딩 사용^[inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]
- EKF2_GPS_CTRL 비트 3(+8)로 GPS 헤딩 활성, SENS_GNSSn_HDG / OFFX,Y,Z / AUXX,Y,Z 설정^[inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]
- MAV_PROTO_VER = 2, 기지국 위치 고정(이동 금지), 하늘 시야가 트인 곳에 설치^[inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]
- QGC Android/iOS는 RTK 미지원^[inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]

## 한계·미확인
NTRIP·기선 길이별 fix 성능은 이 페이지(확인 범위)에 없음. 페이지 일부 잘림. Survey-In 기본 수치 미확인.^[inbox/processed/hw-20261021-precise-px4-rtk-gps-doc.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
