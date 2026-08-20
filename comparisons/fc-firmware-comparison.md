---
title: "FPV 드론 FC 펌웨어 비교: Betaflight vs INAV vs ArduPilot"
created: 2026-08-09
updated: 2026-08-09
type: comparison
tags: [comparison, drone-sw]
domain: flight-control
sources: [inbox/fetch-2026-08-09-rss-oscarliang-fpv.md]
confidence: medium
contested: false
contradictions: []
---

# FPV 드론 FC 펌웨어 비교: Betaflight vs INAV vs ArduPilot

FPV 드론을 조립할 때 모터·ESC·영상시스템·수신기 선택 못지않게 중요한 결정이 FC(Flight Controller) 펌웨어 선택이다. 세 펌웨어는 서로 다른 용도에 최적화돼 있다.^[inbox/fetch-2026-08-09-rss-oscarliang-fpv.md]

## 용도별 포지셔닝

| 펌웨어 | 주 용도 | 특징 |
|---|---|---|
| **Betaflight** | 레이싱/프리스타일 FPV | 최저 지연·최고 반응성, 수동 조종 중심 |
| **INAV** | 장거리(Long Range)·자율비행 FPV | GPS 내비게이션·웨이포인트, Betaflight보다 안정 위주 |
| **ArduPilot** | 산업/정밀 자율비행 | 가장 정교한 자율 미션 기능, 상대적으로 무거운 스택 |

## 선택 기준

- **순수 레이싱/프리스타일**: Betaflight
- **장거리 FPV + 자율 복귀/웨이포인트**: INAV
- **산업용 정밀 자율 미션**: ArduPilot(또는 PX4)

## 관련 개념

- [[betaflight]] — Betaflight 펌웨어 상세
- [[ardupilot-architecture]] — ArduPilot 아키텍처

## 📰 최근 관련 소식
- 드론 라이다를 이용한 임야 현황경계 추출 및 분석 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003368639
