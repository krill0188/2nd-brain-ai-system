---
title: "드론 짐벌·데이터링크 제품 사양 카탈로그 (Gremsy T7·SIYI A8 mini·Microhard pMDDL2450·RFD900x)"
created: 2026-10-16
updated: 2026-10-16
type: concept
domain: hardware
ontology_class: Payload
tags: [drone, drone-hw, hardware, datalink]
sources: [inbox/processed/fetch-2026-10-16-hw-product-payload-gremsy-t7.md, inbox/processed/fetch-2026-10-16-hw-product-payload-siyi-a8-mini.md, inbox/processed/fetch-2026-10-16-hw-product-payload-microhard-pmddl2450.md, inbox/processed/fetch-2026-10-16-hw-product-payload-rfdesign-rfd900x.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 짐벌·데이터링크 제품 사양 카탈로그

## 짐벌·카메라
| 모델 | 핵심 사양 |
|---|---|
| Gremsy T7 | 최대 페이로드 3,175 g, 자체 1,860 g, 입력 15~52 V, CAN/UART/S-Bus/PPM/Bluetooth ^[inbox/processed/fetch-2026-10-16-hw-product-payload-gremsy-t7.md] |
| SIYI A8 mini | 95 g, Sony 1/1.7" 8 MP, 4K@25fps, 입력 11~25.2 V, 평균 5 W/피크 12 W, UART·UDP·S.Bus 제어, IP4X ^[inbox/processed/fetch-2026-10-16-hw-product-payload-siyi-a8-mini.md] |

SIYI는 2023-06 이전 로트가 25.2 V를 지원하지 않을 수 있다. 매뉴얼과 스펙 페이지의 각도 범위가 다르다는 언급이 있으나 직접 확인하지 못했다.

## 데이터링크
| 모델 | 핵심 사양 |
|---|---|
| RFD900x | 902~928 MHz(미국), 1 W, 공중 속도 12~750 kbit/s(기본 64), 14.5 g, 30×57×12.8 mm, SiK/MAVLink, AES ^[inbox/processed/fetch-2026-10-16-hw-product-payload-rfdesign-rfd900x.md] |
| Microhard pMDDL2450 | 2.4 GHz, 최대 1 W, 25 Mbps 이상, 이더넷·시리얼·USB, AES 128/256, Mesh/Relay 모드, -40~85 °C ^[inbox/processed/fetch-2026-10-16-hw-product-payload-microhard-pmddl2450.md] |

RFD900x는 판매 페이지에 예상 출시일 2026-12-17이 표기되어 재고 상태가 불명확하다. pMDDL2450의 입력 전압·크기·무게·통신 거리는 페이지에 없다.

센서 페이로드 중 DJI Zenmuse H30T는 [[dji-matrice-350-rtk]]에서 다룬다.

관련: [[drone-payload-systems]], [[datalink-communication]], [[mavlink]], [[hequav-k11-dual-sensor-gimbal]].
