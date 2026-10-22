---
title: "CHCNAV M722 (듀얼안테나 포지셔닝·헤딩 모듈) 공식 제품페이지·데이터시트"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: CHC Navigation (CHCNAV, Shanghai Huace Navigation Technology Ltd.)
source: https://navigation.chcnav.com/products/chcnav-m722
tags: [drone, hardware, gnss, chcnav, oem, stellax, official]
---

# CHCNAV M722 (듀얼안테나 포지셔닝·헤딩 모듈) 공식 제품페이지·데이터시트

출처 유형: 제조사 공식 제품 페이지(navigation.chcnav.com) + 같은 페이지의 공식 데이터시트 PDF(M722_DS_EN.pdf). 확인 방법: curl(브라우저 UA)로 페이지와 PDF 직접 내려받아 Ghostscript 텍스트 추출, 두 출처 대조. 신뢰도: 높음(1차). 기존 20261021 파일의 언론 보도 기반 값을 대체/보강.

## 핵심 사양 (데이터시트에 적힌 값만)

| 항목 | 값 |
|---|---|
| 패키지 | 48 pin LGA |
| 크기·무게 | 16.0 x 21.0 x 2.6 mm, 1.88±0.03 g |
| 입력 전압·전력 | 3.0~3.6 V DC, 600 mW 전형, Max VCC ripple 50 mV |
| 헤딩 | 듀얼안테나, 1 m 기선에서 0.1도 |
| 부안테나 신호 | BDS B1I, B2I, B3I, B1C, B2a, B2b; GPS L1C/A, L1C, L2C, L2P(Y), L5; GLONASS G1, G2; Galileo E1, E5a, E5b; QZSS L1C/A, L1C/B, L1C, L2C, L5 |
| TTFF | Cold <15 s, Warm <10 s, Hot <5 s, 재획득 <=2 s |
| RTK 출력율 | 1/2/5/10/20 Hz; Raw data 100 Hz* |
| 감도 | 추적 -163 dBm, 획득 -146 dBm |
| 초기화 신뢰도 | 99.9% |
| 채널 수 | 1892 (데이터시트 각주: 1380 GNSS 채널 + 512 anti-jamming 채널) |
| GNSS 신호(주 안테나) | GPS L1C/A, L1C, L2P(Y), L2C, L5; BDS B1I, B2I, B3I, B1C, B2a, B2b; Galileo E1C, E5a, E5b, E5AltBoC, E6; GLONASS G1, G2, L1OC*, L2OC*, L3OC; QZSS L1C/A(B), L1C, L2C, L5, L6D/E; NavIC L5; SBAS L1, L5 (*는 특정 펌웨어/하드웨어) |
| RTK 정확도(RMS) | 수평 0.8 cm + 1 ppm / 수직 1.5 cm + 1 ppm |
| SPP 정확도(RMS) | 수평 1.5 m / 수직 2.5 m |
| 속도 정확도 | 0.03 m/s |
| 온도 | 동작 -40~+85 C, 저장 -55~+95 C |
| 진동/충격 | GJB150.16A-2009, MIL-STD-810F (충격 GJB150.18A-2009) |
| 습도 | 95% 비응축 |
| 간섭 대응 | JamAegis(단일톤·다중톤·협대역·sweep 간섭 감지·억제), 실시간 스펙트럼 모니터링 |
| PPP 정확도(RMS) | 수평 5 cm / 수직 10 cm, 수렴 <15 min |
| 시간 정확도 | 5 ns |
| 보정 | PointFusion: PointSky, PPP-B2b, Galileo HAS, QZSS CLAS |

## 용도
제품 페이지 문구: UAV, 정밀농업, 로봇 잔디깎이, 휴머노이드 로봇(웹 페이지).

## 호환·인터페이스
UART 3, USB 1, SPI* 1, CAN* 1. 출력 NMEA0183, CHCNAV Protocol.

## 비고(미확인)
헤딩 정확도의 기선 길이별 값은 1 m 외 미확인.
데이터시트 개정: Revision August 2026. ArduPilot/PX4 지원 문구 미확인. 가격·재고 미확인.
