---
title: "SIYI RTK Positioning & Orientation Module (UM982 듀얼안테나, 공식 사양)"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: SIYI Technology (思翼科技, 공식 페이지 하단 표기: 思翼科技(深圳)有限公司)
source: https://siyi.biz/en/product/gps-rtk/rtk/spec/
tags: [drone, hardware, gnss, siyi, rtk, dual-antenna, unicore-um982, official]
---

# SIYI RTK Positioning & Orientation Module (UM982 듀얼안테나, 공식 사양)

출처 유형: 제조사 공식 사양 페이지(siyi.biz) + 공식 사용자 매뉴얼 PDF(res.siyi.biz, 매뉴얼 v1.1, 2024.11 개정 이력 표기). 확인 방법: curl로 페이지·PDF 내려받아 Ghostscript 텍스트 추출 후 대조. 두 출처 값 일치.
신뢰도: 높음(제조사 1차). 단 페이지에서 Cold/Hot start·Surveying time 값이 비어 표시됨(페이지 렌더링 누락) → 매뉴얼 값 사용.

## 핵심 사양 (출처에 적힌 값만)

| 항목 | 값 |
|---|---|
| GNSS 수신칩 | Unicore UM982 (매뉴얼) — 공식 사양 페이지에는 칩명 없음 |
| 전자나침반 | PNI RM3100 |
| 위성군 | GPS, GLONASS, BeiDou, Galileo, QZSS |
| 안테나1 신호 | BDS B1I/B2I/B3I; GPS L1C/A, L2P(Y)/L2C, L5; GLONASS L1/L2; Galileo E1/E5a/E5b; QZSS L1/L2/L5 |
| 안테나2 신호 | BDS B1I/B2I/B3I; GPS L1C/A, L2C; GLONASS L1/L2; Galileo E1/E5b; QZSS L1/L2 |
| RTK 정확도 | 수평 0.8 cm + 1 PPM / 고도 1.5 cm + 1 PPM |
| DGPS | 수평 0.4 m + 1 PPM / 고도 0.8 m + 1 PPM (매뉴얼 단위 m; 사양 페이지는 cm로 표기 → 두 출처 표기 불일치, 단위 미확정) |
| 단독측위 | 수평 1.5 m / 고도 2.5 m |
| 방위(듀얼안테나) | 기선 1 m에서 0.2도 |
| 최대 위성 수 | 단독 28+, RTK 50+ |
| 차분 데이터 | RTCM3.X |
| TTFF | Cold start <30 s (매뉴얼), Hot start 값은 텍스트 추출에서 누락 → 미확인 |
| 안테나 이득 | 이동국 2 dBi / 기준국 5.5 dBi (매뉴얼); 사양 페이지는 2 dBi만 표기 |
| 갱신율 | 기본 5 Hz, 최대 20 Hz |
| 인터페이스 | 사양 페이지: UART+I2C 1, UART 1, USB-C 1 / 매뉴얼: UART 2, USB-C 1 (표기 차이) |
| 안테나 커넥터 | MMCX |
| 전압·전력 | 4.5~5.5 V, 1 W |
| 동작 온도 | -30~75 C |
| 크기·무게 | 40 x 30.5 x 15 mm, 22.8 g (안테나 제외) |
| 구성품 | 모듈 1, Quadruple Helix 안테나 2, SMA-MMCX 급전선(550 mm) 2, USB-C 케이블 (매뉴얼) |

## 용도
매뉴얼 문구: 듀얼 안테나로 자기 나침반을 대체하는 방위 산출. ArduPilot 4.4.0 이상 필요, GPS1_TYPE = 25(Unicore Moving Baseline) 또는 24(Unicore Master) 설정, PX4 설정 절차는 매뉴얼 3.2에 있음(세부 파라미터는 이번에 옮기지 않음).

## 호환·인터페이스
UART/USB, RTCM3.X 입력, NTRIP 설정 예시는 매뉴얼에 있음(계정 예시 문자열은 기록하지 않음). DroneCAN 지원은 이 모듈 문서에서 미확인.

## 비고(미확인)
Hot start 시간, DGPS 단위 확정, 인터페이스 개수 표기 차이, RTK 수렴(Surveying time) 값 미확인. 무역·가격·인증 미확인.
