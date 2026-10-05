---
title: "BetaFPV Meteor65 Pro II 브러시리스 휘프"
created: 2026-10-04
updated: 2026-10-04
type: concept
domain: flight-control
tags: [drone, fpv, hardware]
sources: [inbox/processed/fetch-2026-10-04-yt-betafpv-meteor65-pro-ii-one-of-the-most-fun-gets-upgraded.md]
confidence: low
contested: false
contradictions: []
---

# BetaFPV Meteor65 Pro II 브러시리스 휘프

Painless360의 첫인상 리뷰(2026-10-03, 영상 자막 기준) 요약. 단일 리뷰어 의견이며 제조사 주장과 리뷰어
측정이 섞여 있다.^[inbox/processed/fetch-2026-10-04-yt-betafpv-meteor65-pro-ii-one-of-the-most-fun-gets-upgraded.md]

## 사양 (자막에서 언급된 값)

- 70 mm 축거 1S 브러시리스 휘프, 무게 약 22.6 g. 아날로그와 DJI O4 두 버전(HDZero·Walksnail 버전 없음).
- 모터 1802(0.1 mm 스테이터), Gemfan 1409 3엽 프로펠러, 제조사 주장 추력 44% 증가·추력대중량비 5.17:1.
- FC: Matrix 1S 5-in-1 Mark II, 연속 12 A ESC, ExpressLRS 2.4 GHz 수신기(출하 펌웨어 ELRS v3 —
  v4 사용자는 업그레이드 필요). 아날로그 VTX 25–400 mW, 카메라 173° 광각 16:9.
- 비행시간 제조사 주장 5분 50초(Lava 2 1S 480 mAh). 리뷰어는 580 mAh Lava 2를 사용해 잘 작동했다고 언급.
- 완제품과 키트 두 형태 제공, 모터가 FC 커넥터로 연결되어 납땜 없이 교체 가능, 교체 프레임 입수 용이.

## 설정·비행 관찰

- Betaflight 연결에는 어댑터 케이블 필요(USB-C 포트 없음). 가속도계 재보정 필요했음. 포트: UART3 시리얼
  수신기, UART2 TBS SmartAudio, VCP MSP. 자이로/PID 루프 3.2 kHz.
- 기본 모드 설정은 ELRS 표준(ARM CH5, 모드 CH6)이면 바로 작동, OSD는 약간 조정 필요. 바인드 버튼으로 바인딩 성공.
- 호버 스로틀 약 25%로 출력 여유가 크고 angle/horizon에서 관대하며 rate 모드도 가능. 모터 소리가 다른
  1S 휘프보다 다소 크고 덜 부드럽다는 단점 언급(원인 미확인). 카메라는 NTSC 기본이며 PAL 전환 방법은 못 찾음.

## 관련 개념

- [[emax-nanoscout-pro-1s-whoop]] — 비교 대상 1S 휘프
- [[betaflight]] — 설정에 사용된 FC 펌웨어
- [[elrs-41-release]] — ExpressLRS v4 릴리스 맥락
- [[fpv-hardware]] — FPV 하드웨어 허브

## 📰 최근 관련 소식
- [Painless360] BetaFPV Meteor65 PRO II: One of the most fun gets upgraded! (youtube.com, 2026-10-03) — https://www.youtube.com/watch?v=8_ENkPBTnGc
