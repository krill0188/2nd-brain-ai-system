---
title: "Power Zero - M10077"
created: 2026-10-16
captured: 2026-10-16
type: product
domain: hardware
ontology_class: Battery
category: power-module
manufacturer: mRobotics (mRo)
source: https://docs.mrobotics.io/power-module/power-zero
tags: [drone, hardware, product, power-module]
---

# Power Zero (M10077) — mRo

## 핵심 사양 (공식 문서 게재값)

| 항목 | 값 |
|---|---|
| 입력 전압 | 50.4V (12S LiPo) |
| 최대 전류 센싱 | 90A |
| 전원 출력 | 5.3V, 2A |
| 무게 | 2.50g (0.08 oz) |
| 크기 | 18mm × 18mm |
| 높이 | 7.30mm |
| 커넥터 | 6-pin JST-GH |
| ArduPilot BATT_VOLT_MULT | 15.30 |
| ArduPilot BATT_AMP_PERVLT | 50 |
| ArduPilot BATT_AMP_OFFSET | 0.00 |

## 용도

- ACSP7 기반 개량형 표준 전원 모듈, 기체 전압·전류 측정

## 호환·인터페이스

- 6-pin JST-GH 핀아웃: VCC 5.3V(2핀), CURRENT(3핀, 3V3), VOLTAGE(4핀, 3V3), GND(5·6핀)
- 듀얼 내부 전원 공급으로 홀 센서 안정화 (페이지 Features 기재)
- 기준 파라미터는 보드마다 인쇄된 티켓 값 우선 적용 (부품 편차 보정)

## 비고

- 페이지 경고: "Unmaintained site notice — information may be outdated". 최신 정보는 3DR 문서 확인 권장
- 페이지에 '0.5V offset 제거, 전류 센싱 전용 기준 전압 비교' 개량 내용 기재
- 수집 방식: 공식 문서 페이지 직접 확인(2026-10-16). 외부 검색 요약이 아닌 페이지 본문 기준.
- 출처 신뢰도: 중간 (유지보수 중단 사이트 표기)
