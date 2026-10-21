---
title: "Allystar TAU1202 / TAU1205"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: Allystar (ALLYSTAR Technology)
source: https://www.euromobile.ru/upload/iblock/8a1/T-5-2006-TAU1202%20TAU1205%20Datasheet-V1.3.pdf
tags: [drone, hardware, gnss, allystar, l1-l5, module]
---

# Allystar TAU1202 / TAU1205

출처 유형: 제조사 데이터시트 PDF(Datasheet V1.3, 2020, 문서에 'Confidential' 표기) — 러시아 유통사(euromobile.ru) 게재 사본. allystar.com 공식 URL은 이번에 열지 못함.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 채널 수 | 40 channels |
| 지원 신호 | GPS/QZSS: L1C/A, L5C; BDS: B1I, B2a; GLONASS: L1OF; Galileo: E1, E5a (TAU1205는 IRNSS L5 단독 모드 추가) |
| 위치 정확도 | <1 m CEP (open sky, dual band, 양호한 외부 LNA 사용 시) |
| 속도·시간 정확도 | 0.1 m/s CEP, 20 ns |
| 갱신율 | 최대 10 Hz |
| TTFF | 1 s / 24 s (Hot / Cold 로 추정되는 순서 — 표 라벨이 추출 중 분리됨) |
| 감도 | -148 / -155 / -158 / -161 dBm (cold / hot / reacquisition / tracking 순서로 보임, 매핑 중간 신뢰도) |
| 재밍 | 'Smart jammer detection and suppression' (특징 문구, 수치 없음) |
| 크기 | 10.1 x 9.7 x 2.5 mm, 18-pin stamp hole |
| 전원 | 1.8~3.6 V; 22 mA@3.3V (GPS+QZSS L1), 41 mA@3.3V (GNSS L1+L5), Standby 12 uA |
| 동작 온도 | -40 ~ +85 C |
| 인터페이스 | UART 1, I2C 1, CAN 1(맞춤 펌웨어만), NMEA 0183 v4.00/4.10 + Cynosure binary |
| 동작 한계 | 속도 515 m/s, 고도 18,000 m |
| 안테나 바이어스 | ANT_BIAS 출력 전류 35 mA 이하; 1010A00 은 외부 바이어스 초크 필요, 1010C00 은 내장 |

## 용도
페이지 문구: 소형 듀얼밴드 GNSS 모듈, 항법 응용용.

## 호환·인터페이스
UART/I2C/CAN 위 표 참조. RTK 지원은 이 데이터시트에 없음(서브미터급).

## 비고(미확인)
RTK/PPK 미지원 또는 미확인, PX4/ArduPilot 지원 미확인. HD8040 은 이번에 사양 미확보(TAU1202 블록 다이어그램에 'HD804XD' 칩명만 등장).
