---
title: "Hemisphere GNSS Phantom 40 OEM Board"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: Hemisphere GNSS
source: https://www.hemispheregnss.com/wp-content/uploads/875-0464-10_Phantom40_DataSheet-3.pdf
tags: [drone, hardware, gnss, hemisphere, oem, rtk, atlas]
---

# Hemisphere GNSS Phantom 40 OEM Board

출처 유형: 제조사 공식 데이터시트 PDF(Rev. B2, 2026-05, PN 875-0464-10). Eclipse P328 은 단종 안내(유통사 문구)라 후속인 Phantom 40 을 수집함.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 채널 수 | 800+ |
| 지원 신호 | GPS L1CA/L1P/L1C/L2P/L2C/L5; GLONASS G1/G2/G3, P1/P2; BeiDou B1i/B2i/B3i/B1C/B2A/B2B/ACEBOC; Galileo E1BC/E5a/E5b/E6BC/ALTBOC; QZSS L1CA/L2C/L5/L1C/LEX; IRNSS L5; Atlas L-band |
| 정확도 RMS(67%) | Autonomous 1.2 m; SBAS 0.3 m; Atlas H10 0.04 m; Atlas H30 0.15 m; Atlas Basic 0.50 m; RTK 8 mm + 1 ppm (2DRMS 95%: 2.5 m / 0.6 m / 0.08 m / 0.3 m / 1.0 m / 15 mm + 2 ppm) — 열 매핑은 텍스트 추출 순서 기반 |
| RTK 기선 | Long-range RTK baselines up to 50 km (key features 문구) |
| 갱신율 | 1 Hz 표준, 10/20/50 Hz 옵션(활성화 필요) |
| TTFF | Cold 60 s typical (no almanac/RTC), Warm 30 s, Hot 10 s |
| GPS 감도 | -142 dBm |
| 1PPS 정확도 | 20 ns |
| 최대 속도·고도 | 1,342 kph, 18,000 m |
| 크기·무게 | 100 x 60 x 10 mm, 44 g |
| 전원 | 3.3 VDC +/-5%; <1.8 W (all signals + L-band), 545 mA; 안테나 전압 5 VDC max; 안테나 이득 입력 10~40 dB |
| 동작/저장 온도 | -40~+85 C / -40~+85 C |
| 인터페이스 | 3 x 시리얼(CMOS 2 + RS-232 1), USB host/device 1, Ethernet 10/100 1, CAN 2 (NMEA2000, ISO 11783); 24-pin + 16-pin 2 mm 헤더, MMCX 안테나 |
| 프로토콜 | Hemisphere ROX, RTCM v2.3/v3.2, CMR, CMR+, NMEA 0183, Crescent binary |
| 특징 기술 | aRTK (보정 끊겨도 RTK급 유지), Tracer, Athena GNSS 엔진 |

## 용도
페이지 문구: 기계 제어(machine control)용 다주파 OEM 보드. 드론 전용 문구 없음.

## 호환·인터페이스
다른 제조사 모듈과 핀 호환(industry standard form factor, 문구). PX4/ArduPilot 지원 미확인.

## 비고(미확인)
재밍/스푸핑 완화 수치·IMU·헤딩 미확인. 드론 적용 사례 없음(데이터시트 기준). P-series/Eclipse 후속은 이번에 사양 미확보.
