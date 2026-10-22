---
title: "Septentrio mosaic-X5 448채널 수치 독립 확인 (3개 사본 + SparkFun 문서)"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: Septentrio
source: https://media.digikey.com/pdf/Data%20Sheets/Septentrio%20PDFs/Mosaic-X5_Datasheet.pdf
tags: [drone, hardware, gnss, septentrio, mosaic-x5, verification]
---

# Septentrio mosaic-X5 448채널 수치 독립 확인

출처 유형: Septentrio 제조사 데이터시트 PDF의 유통사 게재 사본 3종 + SparkFun 공식 문서(2차). septentrio.com 직접 접속은 Bright Data·curl에서 502/403 계열이라 열람하지 못함. 확인 방법: PDF 3종을 curl로 내려받아 Ghostscript 텍스트 추출 후 수치 대조. 신뢰도: 높음(제조사 PDF 원문이 일치) — 단 모두 구판(2019~2020 개정 표기)이며 최신 개정과의 일치는 미확인.

## 확인 결과 (출처에 적힌 값만)

| 사본 | 출처 | 문서 표기 개정 | 채널 | RTK 수평/수직 | 초기화 | 크기·무게 | 전력 |
|---|---|---|---|---|---|---|---|
| A | media.digikey.com (Mosaic-X5_Datasheet.pdf) | 2020 (10/2020) | 448 hardware channels | 0.6 cm + 0.5 ppm / 1 cm + 1 ppm | 7 s | 31 x 31 x 4 mm, 6.8 g | 0.6 W typ / 1.1 W max |
| B | anavs.com (Mosaic-X5_Datasheet.pdf) | 2019 (10/2019) | 448 | 동일 | 7 s | 동일 | 0.6 W typ(동일) |
| C | gps-world.biz (Septentrio_mosaic-X5_LR.pdf, 2022 업로드) | 개정 표기 미확인 | 448 | 동일 | 7 s | 31 x 31 x 4 mm, 약 7 g(본문) | 미추출 |
| D | sparkfun.github.io (mosaic-X5 Hookup Guide) | 2023-10 | 448 Hardware Channels | RTK 0.6 cm(±0.5 ppm) / 1 cm(±1 ppm) | Cold <45 s, Warm <20 s, 재획득 1 s | - | 입력 3.135~3.465 V |

→ 사본 A·B·C(제조사 데이터시트)와 D(SparkFun, 2차)가 모두 448채널. 기존 20261021 파일(components101 사본)의 448과 독립 출처 3개로 재확인됨.

## 추가로 확인된 수치
- 주의: 채널 수는 데이터시트 각주 'Configuration dependent'(동시 추적 신호 구성에 따라 달라짐).
- 기선 <40 km 조건의 RTK 정확도(open sky, RMS), 갱신율 위치 100 Hz, 지연 <10 ms.

## 비고(미확인)
최신 개정(2024 이후)의 채널 수 변동 여부는 septentrio.com 공식 페이지가 열리지 않아 미확인. G5 계열(P1/P6/P8)은 789 채널로 X5와 다름(별도 파일 참조).
