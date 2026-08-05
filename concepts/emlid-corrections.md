---
title: Emlid Corrections Service
created: 2026-08-05
updated: 2026-08-05
type: concept
tags: [drone, hardware, gnss, rtk, emlid]
sources: [inbox/fetch-2026-08-05-yt-emlid-corrections-get-centimeter-accuracy-with-your-reach-in.md, inbox/fetch-2026-08-05-yt-how-to-get-an-rtk-fix-with-emlid-corrections.md]
confidence: high
contested: false
contradictions: []
domain: hardware
---

# Emlid Corrections Service

Emlid Corrections는 Emlid Reach 수신기용 RTK 보정 서비스로, 별도의 베이스 스테이션이나 서드파티 NTRIP 없이 1–2cm(서브인치) 수준의 정확도를 제공한다.

## 핵심 기능

- **즉시 사용 가능**: Reach 수신기에서 바로 활성화, 추가 하드웨어 불필요
- **센티미터급 정확도**: 1–2cm (sub-inch) 수준의 RTK Fix
- **글로벌 커버리지**: 미국, EU, 호주, 뉴질랜드 등 지역에서 일관된 성능
- **Point One Navigation 네트워크**: 안정적인 보정 데이터 제공

## 설정 방법

1. Emlid Flow 앱(iOS/Android)에서 Reach 수신기 연결
2. Correction input에서 Emlid Corrections 선택
3. 수 초 내 RTK Fix 획득 후 측량 시작

## 활용 분야

- 정밀 측량 및 매핑
- 농업용 드론 운용
- 건설 및 토목
- GIS 데이터 수집

## 관련 개념

- [[gps-uav-imu]] — GPS 미수신 환경 위치추정 기법
- [[sensor-calibration]] — 센서 캘리브레이션
