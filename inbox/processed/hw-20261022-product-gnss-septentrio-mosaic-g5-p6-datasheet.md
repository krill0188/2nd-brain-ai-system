---
title: "Septentrio mosaic-G5 P6 공식 데이터시트 (789채널·전력·AIM+ 등급)"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: Septentrio
source: https://gps-world.biz/wp-content/uploads/2026/05/Septentrio_mosaic-G5-P6-LR.pdf
tags: [drone, hardware, gnss, septentrio, mosaic-g5, datasheet]
---

# Septentrio mosaic-G5 P6 공식 데이터시트

출처 유형: Septentrio 제조사 데이터시트 PDF의 유통/대리점 게재 사본(gps-world.biz, 하단 2026 표기). septentrio.com 직접 열람은 못 함. 확인 방법: curl 다운로드 후 Ghostscript 텍스트 추출. 신뢰도: 높음(제조사 PDF). 기존 20261021 파일의 '채널 수·전력·크기 미확인' 항목을 채움.

## 핵심 사양 (데이터시트에 적힌 값만)

| 항목 | 값 |
|---|---|
| 하드웨어 채널 | 789 hardware channels |
| 신호 | P8과 동일 계열(GPS L1C/A·L1C·L2C·L2PY·L5, GLONASS, BeiDou B1I/B1C/B2a/B2b/B2I/B3I, Galileo E1/E5a/E5b/AltBoc/E6, QZSS, NavIC L5) |
| RTK(open sky, RMS) | 수평 0.6 cm + 0.5 ppm / 수직 1 cm + 1 ppm, 초기화 7 s |
| 기타 모드 | Standalone 1.2 m/1.9 m; SBAS 0.6 m/0.9 m; DGNSS 0.4 m/0.7 m; Galileo HAS 0.1 m/0.2 m |
| GNSS 방위 | 1 m: 0.15도 / 0.25도; 5 m: 0.03도 / 0.05도 (듀얼 안테나) |
| 갱신율·지연 | 위치 100 Hz, 방위 포함 50 Hz; 지연 <10 ms |
| TTFF | Cold <35 s, Warm <10 s |
| 크기·무게 | 22.8 x 16.4 x 2.4 mm, 2.2 g |
| 전력 | 단일 안테나 0.44 W typ / 0.67 W max; 듀얼 0.6 W typ / 0.785 W max |
| 인터페이스 | UART 2, USB 2.0 HS, GPIO 2, PPS 2, 이벤트 마커 2 |
| 보안·재밍 | AIM+ Premium(강화된 재밍·스푸핑 방어, OSNMA 인증), Galileo HAS |
| 진동 | IEC 60721-3-5 Profile 5M3 |

## 비고(미확인)
P6와 P8의 표 숫자는 거의 동일하고 차이는 AIM+ 등급(Premium vs Ultimate) 문구와 DTLS 인증 입출력 여부. CAN·ArduPilot 지원은 미확인.
