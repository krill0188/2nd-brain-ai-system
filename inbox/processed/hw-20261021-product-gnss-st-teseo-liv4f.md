---
title: "STMicroelectronics Teseo-LIV4F tiny dual-band GNSS module"
created: 2026-10-21
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: STMicroelectronics
source: https://www.st.com/resource/en/datasheet/teseo-liv4f.pdf
tags: [drone, hardware, gnss, stmicroelectronics, teseo]
---

# STMicroelectronics Teseo-LIV4F

출처 유형: ST 공식 데이터시트 PDF. st.com 직접 접속은 연결 불가였고 web.archive.org(2026) 보관본에서 내려받아 열람.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 지원 위성군 | GPS/QZSS, Galileo, GLONASS, BeiDou (동시 멀티컨스텔레이션·멀티밴드), IRNSS ready |
| 주파수 대역 | GPS/QZSS L1C/A·L5C, GLONASS L1OF, BeiDou B1i·B2a, Galileo E1·E5a |
| 채널 수 | 미확인 |
| 정밀도 | Submeter positioning accuracy (수치 표는 미추출) |
| RTK/PPK/PPP | RTK 기준국 메시지(RTCM 1005/1006) 언급, 자체 RTK 솔루션 여부 미확인 |
| 갱신율 | 최대 10 Hz |
| 추적 감도 | -162 dBm |
| 인터페이스 | UART, I2C (NMEA 는 UART 와 I2C 모두 지원) |
| 입력 전압·소비전력 | VCC/VBAT 3.0 ~ 3.63 V, 대기 10 uA, L1&L5 추적 48.8 mA |
| 크기·무게 | LCC-18 9.7 x 10.1 mm, 무게 미확인 |
| 시간 펄스 정확도 | 99% 20 ns |
| 동작 온도 | -40 ~ 85 °C |
| 재밍/스푸핑 완화 | 미확인 |

## 용도
Description 에 drones 를 포함한 응용 분야(보험, 물류, 톨링, 도난방지 등)가 열거됨. 원시 측정 데이터 출력 가능, TCXO·RTC 내장.

## 호환·인터페이스
ARK TESEO GPS 기존 파일의 LIV4F 사용 기재와 대응하는 칩 데이터시트.

## 비고(미확인)
채널 수, TTFF 수치 표, 수평 정확도 CEP 수치는 텍스트 추출에서 확정하지 못함. 표 주석: 위성 -130 dBm 조건.
