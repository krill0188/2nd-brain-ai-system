---
title: "Trimble BD992"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: Trimble
source: https://www.nikon-trimble.co.jp/pdf/field/0601_autonomous/BD992_datasheet.pdf
tags: [drone, hardware, gnss, trimble, dual-antenna, heading, rtk]
---

# Trimble BD992

출처 유형: 제조사 데이터시트 PDF(PN 022520-004, 01/21) — Nikon-Trimble(일본 법인) 사이트 게재본. trimble.com 제품 URL은 404(Page Not Found)였고 oemgnss.trimble.com 제품 페이지는 200이나 이번엔 PDF 만 사용.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 채널 수 | 2 x 336 channels (Maxwell 7, 안테나 2개 각 336) |
| 지원 신호(Position 안테나) | GPS L1C/A, L2E, L2C, L5; BeiDou B1, B2, B3; GLONASS L1 C/A, L2 C/A, L3 CDMA; Galileo E1, E5A, E5B, E5AltBOC, E6; IRNSS L5; QZSS L1C/A, L1SAIF, L2C, L5; SBAS L1C/A, L5; MSS L-Band OmniSTAR, Trimble RTX |
| 위치 정확도 | RTK 0.008 m (H) / 0.015 m (V); Autonomous 1.00 m (H) / 1.50 m (V); SBAS 0.50 m (H) / 0.85 m (V); DGNSS 0.25 m (H) / 0.50 m (V) (표 열 매핑은 PDF 텍스트 추출 순서 기반; 각주: 1 sigma, Zephyr 2/3 안테나 사용 시, RTK는 +1 ppm) |
| 헤딩 정확도 | <0.09 deg (2 m 기선) |
| RTK 초기화 | typically <8 s, 신뢰도 >99.9% |
| TTFF | Cold <45 s, Warm <30 s, Re-acquisition <2 s |
| 속도 정확도 | 수평 0.007 m/s, 수직 0.020 m/s |
| 최대 갱신율 | Position/Attitude 50 Hz |
| 지연 | <20 ms |
| 크기·무게 | 100 x 60 x 11.6 mm, 60 g |
| 전원 | 3.3 VDC +5%/-3%, 전형 2.3 W (L1/L2 GPS + L1/L2 GLONASS) |
| 안테나 LNA 전원 | 3.3~5 VDC, 최대 400 mA, 최소 LNA 이득 32.0 dB |
| 동작 온도 | -40 ~ +75 C (저장 -55 ~ +85 C) |
| 진동·충격 | MIL810F tailored, random 6.2 gRMS operating; MIL810D +/-40 g 10 ms operating |
| 인터페이스 | USB 2.0 device 1, Ethernet 1, RS232 3 (최대 460,800), CAN 1, PPS 1, Event marker; 커넥터 44-pin 헤더 + MMCX x2 |
| 재밍 관련 | Advanced RF Spectrum Monitoring and Analysis (분석 기능; 완화 수치 미확인) |
| 출력/입력 프로토콜 | CMR, CMR+, sCMRx, RTCM 2.1/2.2/2.3/3.0/3.1/3.2; NMEA-0183, Trimble GSOF, NMEA2000 |
| 동작 한계 | 속도 515 m/s, 고도 18,000 m, 최대 가속 +/-11 g |

## 용도
페이지 문구: 듀얼 안테나 입력으로 정밀 위치와 헤딩. 이동 기선(Moving Baseline) RTK로 이동체 정밀 착륙 용도 언급.

## 호환·인터페이스
PX4/ArduPilot 지원 문구 미확인. 데이터시트상 구성(L1 SBAS~4성좌 3주파 RTK)이 여러 가지라 표는 'full capability' 기준(각주 1).

## 비고(미확인)
표 15개 항목 중 미확인: PX4/ArduPilot 호환, 가격. 위치 정확도 표 열 라벨이 추출 과정에서 분리되어 수치-조건 매핑은 중간 신뢰도.
