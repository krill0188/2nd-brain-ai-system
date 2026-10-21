---
title: "Swift Navigation Piksi Multi"
created: 2026-10-21
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: Swift Navigation
source: https://www.swiftnav.com/resource-files/Piksi%20Multi/v2.0/Specification/Piksi%20Multi%20Product%20Summary%20v2.0.0.pdf
tags: [drone, hardware, gnss, swift-navigation, rtk]
---

# Swift Navigation Piksi Multi

출처 유형: 제조사 공식 Product Summary PDF v2.0 (2018-08-24). swiftnav.com 제품 URL 은 홈으로 리다이렉트되었으나 resource-files 경로의 PDF 는 열림. ArduPilot 문서에도 지원 RTK 수신기로 올라 있음(본 문서에서는 "Piksi v2 EOL" 언급). 단종·후속 제품 여부는 미확인.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 지원 위성군·신호 | GPS L1/L2, GLONASS G1/G2, BeiDou B1/B2, Galileo E1/E5b, SBAS |
| 채널 수 | 미확인 |
| 정밀도 | SBAS 모드 수평 CEP50 0.75 m; RTK(1σ) 수평 0.010 m + 1 ppm, 수직 0.015 m + 1 ppm; 속도 0.03 m/s RMS; 시간 60 ns RMS |
| RTK 초기화 | 초기화 시간 < 10 s, 신뢰도 > 99%, 솔루션 지연 < 30 ms |
| 갱신율 | 측정값·표준 위치 최대 20 Hz, RTK 위치 최대 10 Hz |
| TTFF | Hot < 5 s / Cold < 60 s / 재획득 < 2 s |
| 인터페이스 | UART-LVTTL 2 (1 Mbps), CAN 2 (1 Mbps), Ethernet 100 Mbps, USB 2.0 x2, MMCX 안테나 포트 |
| 입력 전압·소비전력 | 5 ~ 15 V DC, 일반 2.9 W; 안테나 LNA 전원 출력 4.85 V DC 최대 100 mA |
| 크기·무게 | 48 x 71 x 12.4 mm, 26 g |
| 내장 IMU | 6DOF MEMS IMU 온보드(원시 데이터 스트림) |
| 동작 온도 | -40 ~ +85 °C |
| 재밍/스푸핑 완화 | 미확인 |

## 용도
로보틱스·자율시스템용 저가 멀티밴드 RTK, 온보드 Linux 로 사용자 앱 구동 가능.

## 호환·인터페이스
위 표 참조. 20핀 SAMTEC 1개 + 60핀 고밀도 커넥터 2개.

## 비고(미확인)
2018년 문서이며 현행 판매 여부 미확인. 채널 수 미기재.
