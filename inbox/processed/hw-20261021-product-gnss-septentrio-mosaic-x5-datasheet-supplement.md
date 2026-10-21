---
title: "Septentrio mosaic-X5 데이터시트 보강 (채널·정확도·TTFF·AIM+)"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: Septentrio
source: https://components101.com/sites/default/files/2020-09/Mosaic-X5-Datasheet.pdf
tags: [drone, hardware, gnss, septentrio, mosaic-x5, aim-plus, supplement]
---

# Septentrio mosaic-X5 데이터시트 보강 (채널·정확도·TTFF·AIM+)

출처 유형: Septentrio 제조사 데이터시트 PDF(문서 하단 표기 2019, 'Specifications subject to change without notice') — 부품 정보 사이트 components101.com 게재 사본. 최신판이 아닐 수 있어 기존 septentrio-mosaic-x5.md(공식 페이지 2026-01 보관본)의 값과 다를 경우 그쪽이 최신. 이 파일은 기존 파일의 '미확인' 항목(채널·정확도·TTFF·전력·크기)을 채우는 보강용.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 하드웨어 채널 수 | 448 hardware channels (simultaneous tracking of all visible supported satellite signals; 일부는 configuration dependent) |
| RTK 정확도(open sky, RMS, 기선 <40 km) | 수평 0.6 cm + 0.5 ppm, 수직 1 cm + 1 ppm |
| RTK 초기화 시간 | 7 s |
| 단독 정확도(수평/수직) | Standalone 1.2 m / 1.9 m; SBAS 0.6 m / 0.8 m; DGNSS 0.4 m / 0.7 m; SECORX(PPP, 수렴 후, 구독 필요) 0.04 m / 0.06 m (열 매핑은 텍스트 추출 순서 기반) |
| 속도 정확도 | 3 cm/s |
| 최대 갱신율 | Position 100 Hz, Measurements 100 Hz |
| 지연 | <10 ms (99.9%) |
| 시간 정밀도 | xPPS out 5 ns, Event accuracy <20 ns |
| TTFF | Cold start <45 s (almanac·대략 위치 없음), Warm start <20 s, Re-acquisition 1 s |
| 추적/획득 C/N0 임계 | Tracking 20 dB-Hz, Acquisition 33 dB-Hz |
| 재밍 완화 | AIM+ (narrow band, wide band, chirp jammers) 문구. 억제 dB 수치는 데이터시트에 없음 |
| 기타 GNSS+ 기능 | LOCK+, APME+, IONO+, RAIM, Moving base RTK(출력 20 Hz) |
| 크기·무게 | 31 x 31 x 4 mm, 6.8 g (본문은 <7 g) |
| 입력 전압 | 3.3 VDC +/-5% (모듈 전원); 안테나 바이어스 3.0~5.5 V (내장 전류 제한 150 mA); 안테나 전치증폭 범위 15~50 dB |
| 소비전력 | 0.6 W typ / 1.1 W max |
| 동작/저장 온도 | -40~85 C / -55~85 C; Vibration MIL-STD-810G |
| 인터페이스 | UART 4 (LVTTL, 최대 4 Mbps), Ethernet(RMII) 10/100, USB 2.0 HS, SDIO, GPIO 2, CAN(하드웨어 준비), Event marker 2, PPS 1 |

## 용도
페이지 문구: 로봇·자율시스템·UAV 등 대중 시장용 소형 저전력 모듈.

## 호환·인터페이스
프로토콜: SBF, NMEA 0183 v2.3/3.03/4.0, RINEX v2/v3, RTCM v2/v3(MSM), CMR v2.0 (out/in), CMR+ (input only).

## 비고(미확인)
이 문서는 mosaic-X5 초기(2019) 판. 이후 판에서 지원 신호(예: B2b, Galileo E6 등)와 위치 갱신율이 달라졌을 수 있음. 기존 파일 값 '채널 수 미확인' → 본 파일 448 (구판 기준).
