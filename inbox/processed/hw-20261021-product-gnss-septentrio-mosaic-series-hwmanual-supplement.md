---
title: "Septentrio mosaic GNSS Module Hardware Manual v1.11.0 (mosaic-X5/T/H 공통 사양 보강)"
created: 2026-10-21
captured: 2026-10-21
type: product
domain: hardware
category: gnss
manufacturer: Septentrio
source: https://web.archive.org/web/20260116041522if_/https://www.septentrio.com/system/files/support/mosaic_hardware_manual_v1.11.0.pdf
tags: [drone, hardware, gnss, septentrio, supplement]
---

# Septentrio mosaic 시리즈 하드웨어 매뉴얼 기반 보강 (기존 mosaic-X5 파일의 미확인 항목)

출처 유형: 제조사 공식 PDF(mosaic Hardware Manual v1.11.0)를 web.archive.org 보관본(2026-01-16 스냅샷)에서 내려받아 열람. 제품 데이터시트 PDF는 링크를 찾지 못했고(페이지의 버튼은 #resources 앵커) 추정 URL 3개는 404. 따라서 채널 수·위치 정확도는 이번에도 미확인. 이 매뉴얼은 mosaic-X5, mosaic-T, mosaic-H(듀얼 안테나) 계열 공통 문서이며 mosaic-G5 전용 값은 아님.

## 핵심 사양 (매뉴얼에 적힌 값만)

| 항목 | 값 |
|---|---|
| 모듈 크기 | PCB 31 x 31 mm (±0.15 mm), 총 높이 4.17 mm (±0.3 mm) |
| 무게 | 6.8 g |
| 주 전원 | 단일 3.3 V (VDD_3V3, 3.3 V ±5 %), 최소 전원 공급 능력 500 mA 권장 표기 |
| 안테나 전원 | VANT 3~5.5 V DC 공급, 최대 150 mA, 과전류 시 자동 차단·재시도 |
| 소비전력(3.3 V, 개활지 평균, 단일안테나 모듈) | GPS L1 C/A 단독(1 Hz) 550 mW / 167 mA; GPS L1/L2 RTK(1 Hz) 670 mW / 203 mA; GPS+GLONASS L1/L2 + Galileo L1/E5a RTK + BeiDou B1C/B2a(1 Hz) 850 mW / 258 mA, (100 Hz) 930 mW / 282 mA; 전 위성군 전 신호 Static(1 Hz) 910 mW / 276 mA, (100 Hz) 1080 mW / 327 mA; 전 신호 RTK+heading(10 Hz) 1060 mW / 321 mA |
| 동작 온도 | -40 ~ +85 °C (보관 -55 ~ +85 °C) |
| 타이밍 | 이벤트 입력 2, PPS 출력(1.8 V LVTTL), 10 MHz 외부 기준 입력(REF_I) 지원 |
| 안테나 입력 수 | mosaic-X5 1 / mosaic-T 1 / mosaic-H 2 (표 기재) |

## 용도
기존 mosaic-X5 / G5 파일의 크기·무게·전력·온도 미확인 행을 채우는 보강 자료. mosaic-G5 와 값이 같은지는 미확인(매뉴얼은 X5/T/H 중심).

## 호환·인터페이스
LGA 모듈, 3.3 V 로직 계열, 이벤트·PPS 는 1.8 V 로직(레벨 변환 필요 표기).

## 비고(미확인)
채널 수, 위치 정확도(수평/수직), TTFF 는 이 문서에서 못 찾음. mosaic-G5 P1/P8, ARK mosaic-X5 완제품에 같은 값을 적용하지 않았음.
