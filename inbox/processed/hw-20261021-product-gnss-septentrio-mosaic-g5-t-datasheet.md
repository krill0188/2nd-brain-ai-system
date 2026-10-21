---
title: "Septentrio mosaic-G5 T (G5 계열 공통 하드웨어 수치 보강)"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: Septentrio
source: https://gps-world.biz/wp-content/uploads/2026/03/Septentrio_mosaic-G5T-LR.pdf
tags: [drone, hardware, gnss, septentrio, mosaic-g5, timing, aim-plus-premium, supplement]
---

# Septentrio mosaic-G5 T (G5 계열 공통 하드웨어 수치 보강)

출처 유형: Septentrio 제조사 데이터시트 PDF(문서 표기 10/2025, 2쪽) — 유통사 gps-world.biz 게재 사본. 주의: 이 문서는 timing 용 mosaic-G5 T 이며 P1/P3/P8 항법용 데이터시트가 아님. 로그인 필요 공식 PDF 는 시도하지 않음. G5 T 와 P3 공통 값(크기 22.8 x 16.4 mm, 2.2 g)은 septentrio.com P3 제품 페이지(보관본)에서도 확인됨.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 하드웨어 채널 수 | 789 hardware channels |
| 지원 신호 | GPS L1C/A, L1C, L2C, L2PY, L5; GLONASS L1CA, L2CA, L2P, L3 CDMA; BeiDou B1I, B1C, B2a, B2b, B2I, B3; Galileo E1, E5a, E5b, E6; QZSS L1C/A, L1 C/B, L2C, L5; NavIC L5; SBAS; on-module L-band; Galileo HAS, OSNMA(향후 SW 업데이트) |
| TTFF(Timing 모델) | Cold <35 s, Warm <10 s, Re-acquisition 1 s |
| 단독 정확도(수평/수직, open sky RMS) | Standalone 1.2 m / 0.9 m(?), SBAS 0.6 m / 0.8 m (열 매핑은 텍스트 추출 기반, 중간 신뢰도) |
| 속도 정확도 | 3 cm/s |
| 최대 갱신율 | Position 5 Hz (timing 모델 한정; 항법용 모델 값 아님) |
| 시간 정밀도 | PPS resolution 1.4 ns, Event accuracy <3 ns |
| C/N0 임계 | Tracking 20 dB-Hz, Acquisition 30 dB-Hz |
| 재밍/스푸핑 | AIM+ Premium (enhanced jamming and spoofing protection, superior wideband resilience, OSNMA authentication). dB 수치 없음 |
| 크기·무게 | 22.8 x 16.4 x 2.4 mm, 2.2 g, SMT LGA |
| 전원 | 3.3 VDC; 0.44 W typ / 0.67 W max; 안테나 바이어스 3.0~5.5 V(150 mA 제한), 전치증폭 15~50 dB |
| 온도·환경 | 동작 -40~85 C, 저장 -55~85 C, 습도 5~95% 비응축, IEC 60721-3-5 5M3, MIL-STD-810H 514.8 Cat 4 / 516.8 Proc I |
| 인터페이스 | UART 2 (LVTTL, 4 Mbps), USB 2.0 HS, GPIO 2, PPS 2, Event marker 2, Clock sync input, 10 MHz Frequency sync input |

## 용도
timing 용 모델. 드론용 P 시리즈의 하드웨어 공통 수치(채널 수 789, 크기·무게)를 간접 확인하는 용도.

## 호환·인터페이스
프로토콜 SBF, NMEA 0183 v3.03/4.0.

## 비고(미확인)
P1/P3/P8 개별 RTK 정확도·초기화 시간·TTFF 는 이번에도 공식 PDF 를 열지 못해 미확인(P3 평가키트 페이지의 initialisation 7 s 는 검색 요약에서만 확인, 직접 열람 못함). 5 Hz 갱신율은 timing 모델 특성.
