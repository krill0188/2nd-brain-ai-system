---
title: Emlid Corrections Service
created: 2026-08-05
updated: 2026-10-02
type: concept
tags: [drone, hardware, gnss, rtk, emlid]
sources: [inbox/fetch-2026-08-05-yt-emlid-corrections-get-centimeter-accuracy-with-your-reach-in.md, inbox/fetch-2026-08-05-yt-how-to-get-an-rtk-fix-with-emlid-corrections.md, inbox/fetch-2026-08-06-yt-how-to-get-an-rtk-fix-in-seconds.md, inbox/processed/fetch-2026-09-30-yt-why-your-gnss-receiver-wont-lock-fix-and-how-to-fix-it.md, inbox/processed/fetch-2026-10-02-yt-how-gossweiler-cut-site-visits-for-daily-checks-with-emlid-g.md]
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

Emlid CEO가 직접 시연한 데모에서도 위 3단계만으로 수 초 내 RTK Fix를 획득함을 확인했다.^[inbox/fetch-2026-08-06-yt-how-to-get-an-rtk-fix-in-seconds.md]

## FIX 끊김(FLOAT 전환) 트러블슈팅

RTK 솔루션이 FIX와 FLOAT 사이를 오갈 때 현장에서 점검할 4가지 항목:^[inbox/processed/fetch-2026-09-30-yt-why-your-gnss-receiver-wont-lock-fix-and-how-to-fix-it.md]

- **장애물**: 나무, 건물, 지붕 처마 등 상공 시야를 가리는 요소 확인
- **베이스라인 거리**: 베이스 또는 NTRIP 기준국까지의 거리 점검
- **보정 소스**: 인터넷 연결 및 NTRIP 스트림 정상 여부 확인
- **멀티패스/반사면**: 금속, 유리 외벽, 인근 트럭 등 신호 반사 요인 주의

## 현장 사례: Gossweiler (스위스 엔지니어링사, 직원 180명)

측량팀 외 여러 부서에 Emlid GNSS 수신기를 보급하고 **Emlid Flow 360**(클라우드 기반 프로젝트
관리)을 도입해, 측량 전담 인력 없이도 각 부서가 자체적으로 일일 현장 점검을 수행할 수 있도록
운영 방식을 바꾼 사례.^[inbox/processed/fetch-2026-10-02-yt-how-gossweiler-cut-site-visits-for-daily-checks-with-emlid-g.md]

- **대기시간 제거**: 과거에는 측량팀이 바쁠 경우 고객 요청(예: "2시간 내 현장 방문")에 대응이
  지연됐으나, 각 부서가 자체 수신기로 즉시 대응 가능.
- **클라우드 기반 워크플로**: 사무실에서 프로젝트를 미리 설정하면 현장 인력이 사무실 복귀 없이
  바로 다른 현장으로 이동 가능. 기존 PC→USB/SD카드→컨트롤러 수동 전송 방식(데이터 유실 위험
  포함)을 제거.
- **정확도 검증**: 기존 장비 대비 동일한 정확도를 확인 후 점진적으로 도입을 확대.
- **현장 절차**: GNSS 연결 → Fix 획득 대기 → 초기화(initialization) → 기준점 스테이크아웃으로
  좌표계·폴 높이 검증 → 측량 수행.

## 활용 분야

- 정밀 측량 및 매핑
- 농업용 드론 운용
- 건설 및 토목
- GIS 데이터 수집

## 관련 개념

- [[gps-uav-imu]] — GPS 미수신 환경 위치추정 기법
- [[sensor-calibration]] — 센서 캘리브레이션

## 📰 최근 관련 소식
- [Emlid] Why your GNSS receiver won't lock FIX and how to fix it (youtube.com, 2026-09-29) — https://www.youtube.com/watch?v=l2qOaIcsXqQ
- [Emlid] How Gossweiler cut site visits for daily checks with Emlid GNSS (youtube.com, 2026-10-01) — https://www.youtube.com/watch?v=Oz_PFGysHr8
