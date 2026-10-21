---
title: "GPS Blending / Dual GPS (ArduPilot docs)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: navigation-gnss-denied
source: https://ardupilot.org/copter/docs/common-gps-blending.html
tags: [drone, gnss, 5-GNSS/INS융합]
authors: "ArduPilot 문서"
published: "미확인"
---

## 핵심 내용
두 GPS의 측정을 혼합해 단일 GPS 글리치 영향을 줄이는 기능. 위치·속도 정확도를 보고하는 장치만 혼합 가능(u-blox 가능, NMEA 일반적으로 불가). 정확도 스케일이 제조사마다 달라 같은 제조사 2개 사용을 권장한다.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- GPS2_TYPE=1(AUTO) 또는 해당 타입, GPS_AUTO_SWITCH=2(Blend) / 1(UseBest)
- 로그: GPS 인스턴스 0=첫째, 1=둘째, 2=혼합 출력

## 한계·미확인
지연/전환 지연 파라미터 문서화 없음(미확인).
