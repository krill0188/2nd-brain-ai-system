---
title: "Septentrio mosaic-G5 P8 공식 데이터시트 (789채널·전력·AIM+ 등급)"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: Septentrio
source: https://gps-world.biz/wp-content/uploads/2026/05/Septentrio_mosaic-G5-P8-LR.pdf
tags: [drone, hardware, gnss, septentrio, mosaic-g5, datasheet]
---

# Septentrio mosaic-G5 P8 공식 데이터시트

출처 유형: Septentrio 제조사 데이터시트 PDF의 유통/대리점 게재 사본(gps-world.biz, 하단 2026 표기). septentrio.com 직접 열람은 못 함. 확인 방법: curl 다운로드 후 Ghostscript 텍스트 추출. 신뢰도: 높음(제조사 PDF). 기존 20261021 파일의 '채널 수·전력·크기 미확인' 항목을 채움.

## 핵심 사양 (데이터시트에 적힌 값만)

| 항목 | 값 |
|---|---|
| 하드웨어 채널 | 789 hardware channels (동시 추적) |
| 신호 | GPS L1C/A, L1C, L2C, L2PY, L5; GLONASS L1CA, L2CA, L2P, L3 CDMA; BeiDou B1I, B1C, B2a, B2b, B2I, B3I; Galileo E1, E5a, E5b, E5 AltBoc, E6; QZSS L1C/A, L1 C/B, L2C, L5, L6; NavIC L5; 모듈 내 L-band(단일 안테나 구성) |
| RTK(open sky, RMS) | 수평 0.6 cm + 0.5 ppm / 수직 1 cm + 1 ppm, 초기화 7 s |
| 기타 모드 | Standalone 1.2 m/1.9 m; SBAS 0.6 m/0.9 m; DGNSS 0.4 m/0.7 m; Galileo HAS 0.1 m/0.2 m |
| GNSS 방위(attitude) | 안테나 간격 1 m: heading 0.15도, pitch/roll 0.25도; 5 m: 0.03도 / 0.05도 |
| 속도 정확도 | 3 cm/s |
| 갱신율 | 위치 100 Hz, 측정치 100 Hz; Standalone·DGNSS+attitude 50 Hz, RTK+attitude 50 Hz |
| 지연 | <10 ms |
| TTFF | Cold <35 s, Warm <10 s, 재획득 1 s |
| C/N0 임계 | 추적 20 dB-Hz, 획득 30 dB-Hz |
| 시간 | PPS 5 ns, jitter ±0.7 ns, 이벤트 정확도 <3 ns |
| 크기·무게 | 22.8 x 16.4 x 2.4 mm, 2.2 g, SMT LGA |
| 전력 | 단일 안테나 0.44 W typ / 0.67 W max; 듀얼 안테나 0.6 W typ / 0.785 W max; 입력 3.3 VDC |
| 안테나 급전 | 전치증폭 15~35 dB(단일/듀얼 표기 구분), 바이어스 3.0~5.5 V, 전류제한 150 mA |
| 인터페이스 | UART(LVTTL, 최대 4 Mbps) 2, USB 2.0 HS 1, GPIO 2, PPS 2, 이벤트 마커 2 |
| 온도 | 동작 -40~85 C, 저장 -55~85 C |
| 프로토콜 | SBF, NMEA 0183 v2.3/3.03/4.0, RTCM v3.x(MSM) |
| 보안·재밍 | AIM+ Ultimate(재밍·스푸핑 최상급), Galileo OSNMA, DTLS 기반 인증된 입출력 문구 있음 |

## 비고(미확인)
CAN 지원·PX4/ArduPilot 지원 문구는 데이터시트에 없음(미확인). 주파수별 AIM+ 억제량(dB) 수치 없음. 사본 하단 날짜 기준이라 최신 개정과 같은지 미확인.
