---
title: "CubePilot Here 4 (HEX/ProfiCNC) Multiband RTK GNSS"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: CubePilot (HEX/ProfiCNC)
source: https://docs.cubepilot.org/user-guides/here-4/here-4-manual
tags: [drone, hardware, gnss, here4, dronecan, f9p, rtk, ardupilot]
---

# CubePilot Here 4 (HEX/ProfiCNC) Multiband RTK GNSS

출처 유형: 제조사 공식 문서(CubePilot docs) Here 4 Manual. 'ProfiCNC' 명칭은 검색 결과의 유통사 표기이며 공식 문서에선 CubePilot 로 표기됨.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| GNSS 칩 | u-blox NEO-F9P |
| 프로세서 | STM32H757 |
| 지원 위성군 | GPS, GLONASS, Galileo, BeiDou + SBAS, QZSS; 동시 최대 4 성좌 |
| 대역 | B1I, B2a, E1B/C, E5a, L1C/A, L1OF, L5 |
| 위치 정확도 | 0.01 m + 1 ppm CEP |
| RTK 갱신율 | 최대 20 Hz |
| RTK 수렴 시간 | <10 sec |
| TTFF | Cold 25 s, Aided 2 s, Hot 2 s |
| 감도 | Tracking -167, Cold -148, Hot -157, Reacq -160 dBm |
| IMU·자기계·기압계 | ICM42688 + RM3100, MS5611 |
| 통신 | DroneCAN 8 Mbit/s, CAN 2포트(현 펌웨어는 1포트만 지원) |
| 프로토콜 | NMEA, UBX binary, RTCM 3.3, SPARTN 2.0.1 |
| 크기·무게 | 16 x 68 mm, 60 g (케이블 포함) |
| 동작 온도 | -40~+85 C |
| 재밍/스푸핑 | Advanced anti-spoofing algorithms (문구, 수치 없음) |
| 최대 속도 | 500 m/s |
| 기타 | Taoglas 듀얼밴드 L1/L5 안테나, Drone-ID(Blue 버전), 8 PWM/BDSHOT 출력 시 FC 기능 가능 |

## 용도
페이지 문구: 전문가용 듀얼밴드 RTK 항법 모듈, 브레이크아웃 보드 연결 시 비행제어 기능.

## 호환·인터페이스
AP_Periph 펌웨어, DroneCAN. 입력 전압 5V(핀표).

## 비고(미확인)
페이지 문구 'dual-band' 이나 칩 F9P 일반 사양상 L1/L5 변형 여부는 공식 문서에서 모델 접미사(-15B 등) 미기재.
