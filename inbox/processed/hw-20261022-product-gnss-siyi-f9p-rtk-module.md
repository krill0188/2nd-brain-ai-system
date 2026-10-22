---
title: "SIYI F9P RTK Module (u-blox ZED-F9P, 공식 사양)"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: SIYI Technology (思翼科技)
source: https://siyi.biz/en/product/gps-rtk/f9p-rtk/spec/
tags: [drone, hardware, gnss, siyi, rtk, zed-f9p, official]
---

# SIYI F9P RTK Module (u-blox ZED-F9P, 공식 사양)

출처 유형: 제조사 공식 사양 페이지 + 공식 사용자 매뉴얼 PDF(res.siyi.biz, v1.0 2024.4). 확인 방법: curl 다운로드 후 텍스트 추출. 신뢰도: 높음(1차). Cold/Hot start·Surveying time 값은 페이지에서 비어 있음.

## 핵심 사양 (출처에 적힌 값만)

| 항목 | 값 |
|---|---|
| 수신칩 | 184 channel ZED-F9P (u-blox) |
| 전자나침반 | IST8310 |
| 위성군·대역 | GPS L1C/A, L2C; GLONASS L1OF, L2OF; Galileo E1B/C, E5b; BeiDou B1I, B2I; QZSS L1C/A, L2C |
| 위치 정확도 | 1 cm + 1 ppm (RTK) |
| 방위(듀얼안테나) | (0.25 / R)도, R=두 이동국 안테나 간 거리(m) |
| 단독측위 | 1.5 m CEP; SBAS 보조 1.0 m CEP |
| 듀얼 모듈 방향탐지 | 지원, Yaw 정확도 0.35도(참고값) |
| 안테나 이득 | 이동국 2 dBi / 기준국 5.5 dBi |
| 인터페이스 | UART 2, USB-C 1 |
| 안테나 커넥터 | MMCX |
| 전압·전력 | 4.5~5.5 V, 0.6 W |
| 동작 온도 | -30~75 C |
| 크기·무게 | 47 x 33 x 13 mm, 31 g |

## 용도
RTK 센티미터급 측위, 2개 모듈로 방향탐지(컴퍼스 대체) — 매뉴얼 5장 제목에서 확인.

## 호환·인터페이스
오토파일럿용으로 개발됐다고 매뉴얼 서문에 기재. 구체 프로토콜·ArduPilot/PX4 파라미터는 이번에 옮기지 않음.

## 비고(미확인)
Cold/Hot start, 갱신율, RTK 수렴 시간 미확인. 주의: 사양 페이지 Yaw 값 표기 '0.35 edg'는 원문 오타로 보이며 단위는 '도'로 해석(원문 그대로 '참고값').
