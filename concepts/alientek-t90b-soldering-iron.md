---
title: "ALIENTEK T90B 휴대용 납땜 인두 (드론 수리용)"
created: 2026-10-10
updated: 2026-10-10
type: concept
domain: hardware
tags: [drone, hardware, fpv]
sources: [inbox/processed/fetch-2026-10-10-yt-no-compromises-my-dream-portable-soldering-iron-is-alientek-.md]
confidence: low
contested: false
contradictions: []
---

# ALIENTEK T90B 휴대용 납땜 인두 (드론 수리용)

Joshua Bardwell 영상(2026-10-09)의 리뷰를 정리한다. 자막은 8000자에서 절단돼 있어 후반부 실측 시험은 반영하지 못했다. 단일 출처 리뷰라 confidence는 low다.^[inbox/processed/fetch-2026-10-10-yt-no-compromises-my-dream-portable-soldering-iron-is-alientek-.md]

## 배경: 기존 인두의 한계

- TS100/TS101 계열은 오래 쓰였지만 플라스틱 외관과 긴 팁, 헐거운 체결이 불만이다.
- Secure S99는 JBC 스타일 팁으로 열 성능이 좋고 작지만, USB PD는 약 65 W까지이고 DC 입력은 21 V 한도라 6S 배터리에 쓸 수 없다(5S까지). 12~14 AWG XT60 배선이나 ESC 음극 패드처럼 열용량이 큰 작업에는 부족하다고 평가했다.

## T90B 특성 (자막 기준)

- 알루미늄 구조, 금속 캡과 휴대 손잡이, 컬러 디스플레이. 가속도계로 왼손잡이 모드를 지원한다.
- **JBC C245 표준 팁** 사용. Secure와 달리 변형 팁이 필요 없고, 팁 저항에 따라 약 140 W까지 USB PD와 DC(USB-C 포트)로 낼 수 있다고 한다.
- 프리셋 3개(편집 가능), 최대 450 °C, 입력 전압·전류·전력 표시, 로커 스위치로 프리셋 전환·슬립.
- 6S 배터리 구동은 USB-C↔XT60 케이블을 만들어 시연했다. 켠 직후 표시 전력은 50 W대였고 저자도 이유를 모르겠다고 했다.
- 140 W급 출력엔 그 출력을 단일 포트로 내는 충전기가 필요하다. 220 W 멀티포트 충전기는 포트당 출력이 100 W 미만일 수 있다.

## 관련 개념

- [[fpv-hardware]] — FPV 하드웨어 동향
- [[flight-controller-hardware]] — 수리·배선 대상 FC/ESC 하드웨어
- [[drone-power-battery]] — 6S 배터리 등 전원 맥락

## 📰 최근 관련 소식
- [Joshua Bardwell] No compromises. My DREAM portable soldering iron is ... ALIENTEK T90B (youtube.com, 2026-10-09) — https://www.youtube.com/watch?v=jPXecdg2hcA
