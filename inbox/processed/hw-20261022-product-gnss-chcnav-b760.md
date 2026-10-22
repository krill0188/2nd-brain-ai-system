---
title: "CHCNAV B760 (OEM GNSS 보드) 공식 제품페이지·데이터시트"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: CHC Navigation (CHCNAV, Shanghai Huace Navigation Technology Ltd.)
source: https://navigation.chcnav.com/products/chcnav-b760
tags: [drone, hardware, gnss, chcnav, oem, stellax, official]
---

# CHCNAV B760 (OEM GNSS 보드) 공식 제품페이지·데이터시트

출처 유형: 제조사 공식 제품 페이지(navigation.chcnav.com) + 같은 페이지의 공식 데이터시트 PDF(B760_DS_EN.pdf). 확인 방법: curl(브라우저 UA)로 페이지와 PDF 직접 내려받아 Ghostscript 텍스트 추출, 두 출처 대조. 신뢰도: 높음(1차). 기존 20261021 파일의 언론 보도 기반 값을 대체/보강.

## 핵심 사양 (데이터시트에 적힌 값만)

| 항목 | 값 |
|---|---|
| 크기 | 100.0 x 60.0 x 7.4 mm (웹: 무게 43.3±3 g) |
| 입력 전압·전력 | 3.2~3.4 V DC, 800 mW 전형, Max VCC ripple 50 mV |
| 초기화 | 시간 <3 s, 신뢰도 >99.99% |
| TTFF | Cold <15 s |
| RTK 출력율 | 1/2/5/10/20 Hz, 100 Hz* |
| 인터페이스 | UART 3, ECLOCK 1(10M/20M), CLOCK_OUT 1(10M), LAN 1(100M), PPS 1, EVENT 1 |
| 관측치 정확도(RMS) | 의사거리 10 cm(GLONASS 15 cm), 반송파 위상 1 mm; E5 AltBOC 의사거리 1 cm |
| 채널 수 | 1892 (데이터시트 각주: 1380 GNSS 채널 + 512 anti-jamming 채널) |
| GNSS 신호(주 안테나) | GPS L1C/A, L1C, L2P(Y), L2C, L5; BDS B1I, B2I, B3I, B1C, B2a, B2b; Galileo E1C, E5a, E5b, E5AltBoC, E6; GLONASS G1, G2, L1OC*, L2OC*, L3OC; QZSS L1C/A(B), L1C, L2C, L5, L6D/E; NavIC L5; SBAS L1, L5 (*는 특정 펌웨어/하드웨어) |
| RTK 정확도(RMS) | 수평 0.8 cm + 1 ppm / 수직 1.5 cm + 1 ppm |
| SPP 정확도(RMS) | 수평 1.5 m / 수직 2.5 m |
| 속도 정확도 | 0.03 m/s |
| 온도 | 동작 -40~+85 C, 저장 -55~+95 C |
| 진동/충격 | GJB150.16A-2009, MIL-STD-810F (충격 GJB150.18A-2009) |
| 습도 | 95% 비응축 |
| 간섭 대응 | JamAegis(단일톤·다중톤·협대역·sweep 간섭 감지·억제), 실시간 스펙트럼 모니터링 |
| PPP / PPP-AR / PPP-RTK | PPP 수평 5 cm 수직 10 cm(<15 min); PPP-AR 수평 2.5 cm 수직 5 cm(<3 min); PPP-RTK 수평 2.5 cm 수직 5 cm(<1 min) |
| 시간 | 동기 정확도 5 ns(데이터시트), 웹 문구는 'better than 3 ns' 및 외부 클럭 입출력 |

## 용도
제품 페이지 문구: 정적 측량, 모니터링 스테이션, CORS 기준국 (UAV 탑재용 아님, 100x60 mm 보드). 100 Hz 원시 관측치.

## 호환·인터페이스
데이터 프로토콜 NMEA0183, RTCM3.X, CHCNAV Protocol.

## 비고(미확인)
시간 정확도 5 ns(데이터시트) vs better than 3 ns(웹 문구) 불일치. UAV 탑재 가능성은 크기·전력으로 판단하지 않음(미확인).
데이터시트 개정: Revision September 2026. ArduPilot/PX4 지원 문구 미확인. 가격·재고 미확인.
