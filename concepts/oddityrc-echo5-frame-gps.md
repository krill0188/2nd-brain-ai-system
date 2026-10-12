---
title: "OddityRC Echo5 5인치 프레임·마이크로 GPS·ELRS 수신기"
created: 2026-10-12
updated: 2026-10-12
type: concept
domain: hardware
tags: [drone, drone-hw, fpv, hardware]
sources: [inbox/processed/fetch-2026-10-12-yt-oddityrc-echo5-5-quad-frame-a-gps-and-an-elrs-rx-too.md]
confidence: low
contested: false
contradictions: []
---

# OddityRC Echo5 5인치 프레임·마이크로 GPS·ELRS 수신기

Painless360 영상(2026-10-11) 자막 기준 정리. 자막이 8000자에서 잘려 결론부(최종 평가·비행 결과)는 없다. 단일 출처, 리뷰어 개인 의견 포함이라 confidence는 low.

## 배경

리뷰어는 중국 수출 제한 때문에 SpeedyBee·Maytech 등의 FC와 좋은 프레임을 구하기 어려워졌고, OddityRC를 실제로 배송받을 수 있는 주문처로 소개한다.^[inbox/processed/fetch-2026-10-12-yt-oddityrc-echo5-5-quad-frame-a-gps-and-an-elrs-rx-too.md] 관련: [[china-drone-export-controls]].

## 마이크로 GPS

- 16×12 mm 크기, 주요 위성군 지원, 10 Hz 갱신, NMEA·u-blox 프로토콜, 3.3~5 V 입력, 커넥터 SH 1.0, 내장 TCXO.
- 4핀 구성이라 **나침반이 없다**. 리뷰어는 iNav 고정익에는 좋지만 쿼드에는 나침반이 있는 쪽을 권한다.^[inbox/processed/fetch-2026-10-12-yt-oddityrc-echo5-5-quad-frame-a-gps-and-an-elrs-rx-too.md]

## ELRS 수신기

2.4 GHz ExpressLRS 모듈과 호환되며 915 MHz 버전도 있는 것으로 "알고 있다"고 말한다(확신 표현 아님). 뒷면 솔더 패드, 앞면 커넥터, T형 안테나 구성. 관련: [[elrs-41-release]].^[inbox/processed/fetch-2026-10-12-yt-oddityrc-echo5-5-quad-frame-a-gps-and-an-elrs-rx-too.md]

## Echo5 프레임 (X형·데드캣형)

| 항목 | 값 |
| --- | --- |
| 축거 | 225 mm |
| 권장 프롭 | 4.9~5 in |
| 무게 | 약 219 g |
| 상판/중판 두께 | 약 2.5 mm |
| 암 두께 | 5.5 mm (12 스타일 카본) |
| FC 마운트 | 20 / 30.5 mm |
| VTX 마운트 | 20 / 25.5 mm |
| 모터 홀 간격 | 16 mm |
| 카메라 마운트 | 19~20 mm |

- 구성: XT60 고정용 TPU 부품, 수평 ELRS 안테나 마운트, V형 HD 안테나 홀더, GPS 마운트, 원격 USB 포트, 밀링 알루미늄 카메라 케이지(진동 격리 포함), 나사 풀림 방지 로크타이 도포.
- 장점: 조립이 쉽고 완성도·디테일이 높다고 평가(SpeedyBee Master 5 프레임급).
- 단점: 상판 고정 나사 10개, 암당 나사 2개(한 나사는 포스트로 들어가 반대편이 풀릴 수 있음)라 필드 수리·빠른 교체에는 불리하다.^[inbox/processed/fetch-2026-10-12-yt-oddityrc-echo5-5-quad-frame-a-gps-and-an-elrs-rx-too.md]

관련 하드웨어 동향: [[fpv-hardware]], [[flight-controller-hardware]].

## 📰 최근 관련 소식
- [Painless360] OddityRC Echo5 5" Quad Frame, a GPS and an ELRS Rx too! (youtube.com, 2026-10-11) — https://www.youtube.com/watch?v=g7I-FGizr9A
