---
title: "SIYI UniGNSS M10 (u-blox M10, DroneCAN GNSS, 공식 사양)"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: SIYI Technology (思翼科技)
source: https://siyi.biz/en/product/gps-rtk/unignss-m10/spec/
tags: [drone, hardware, gnss, siyi, dronecan, m10, official, non-rtk]
---

# SIYI UniGNSS M10 (u-blox M10, DroneCAN GNSS, 공식 사양)

출처 유형: 제조사 공식 사양 페이지. 확인 방법: curl로 페이지 HTML 내려받아 텍스트 추출. 신뢰도: 높음. RTK 모듈이 아닌 일반 GNSS(참고용, RTK 비교 대상 아님).

## 핵심 사양

| 항목 | 값 |
|---|---|
| 수신칩 / 프로세서 | UBX-M10050 / STM32L431 |
| 전자나침반 | IST8310 |
| 신호 | GPS L1 C/A; QZSS L1 C/A, L1S; GLONASS L1OF; BeiDou B1I/B1C; Galileo E1B/C; SBAS L1 C/A |
| 수평 정확도 | 1.5 m CEP |
| 통신 | DroneCAN |
| 감도 | 추적·항법 -167 dBm, 재획득 -160 dBm, Cold -148 dBm, Hot -159 dBm |
| 획득 시간 | Cold 28 s, Assisted 1 s, Hot 1 s |
| 갱신율 | 단일 GNSS 최대 25 Hz, 3개 이상 동시 GNSS 최대 10 Hz |
| 필터 | LNA+SAW |
| 전압·온도 | 4.5~5.5 V, -30~60 C |
| 크기·무게 | 50.6 x 50.6 x 13.6 mm, 31 g |

## 비고(미확인)
소비전력 미확인. 사양 표에 다중대역·RTK 없음. SIYI 사이트의 M9N GPS 사양 URL(/m9n-gps/spec/)은 홈페이지로 리다이렉트되어 이번에 사양 미확인.
