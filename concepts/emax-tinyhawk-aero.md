---
title: "EMAX Tinyhawk Aero 65mm 1S 레이싱 웁"
created: 2026-10-15
updated: 2026-10-15
type: concept
domain: hardware
tags: [drone, drone-hw, fpv, hardware]
sources: [inbox/processed/fetch-2026-10-15-yt-just-out-emax-tinyhawk-aero-their-first-ever-custom-built-ra.md]
confidence: low
contested: false
contradictions: []
---

# EMAX Tinyhawk Aero 65mm 1S 레이싱 웁

Painless360 영상(2026-10-14) 자막 기준. 자막 후반이 잘려 있고 단일 출처라 confidence는 low이며, 수치는 리뷰어가 읽어 준 값이다. 같은 제조사의 다른 웁은 [[emax-nanoscout-pro-1s-whoop]] 참조.

## 사양 (리뷰어 발언)

- 휠베이스 65mm, 크기 85×85×40mm. EMAX 최초의 레이싱 전용 웁이다.^[inbox/processed/fetch-2026-10-15-yt-just-out-emax-tinyhawk-aero-their-first-ever-custom-built-ra.md]
- 무게: 건조 16.3g(프리스타일 아날로그, 리뷰어 저울 17g). 아날로그판 약 17g, HDZero판 19g 미만.
- 0702 B 모터를 27~35kV 범위의 세 가지 kV 버전(프리스타일·레이싱·최대 추력용)으로 판매하며, 성능 세팅에서 추력 약 174g, 추력 대 중량비 6.7:1이라고 했다. 리뷰 유닛은 27,000kV.
- 가격은 약 130달러로 알려졌다. 아날로그와 HDZero 옵션이 있고 Walksnail·Ascent 버전은 없다. 전용 배터리 커넥터(EM 2.0)를 쓰므로 다른 배터리를 쓰려면 커넥터 교체가 필요하다. LiftOff 시뮬레이터에도 추가되었다.

## 설정 (Betaflight / ExpressLRS)

- 수신기는 ExpressLRS 내장이며 60초간 전원을 켜 두면 Wi-Fi 모드로 들어간다. 펌웨어가 ELRS 3 계열이라 이미 4로 올린 환경이라면 플래시가 필요하다. 관련: [[elrs-41-release]].
- 자이로 8K, PID 루프 4K, CPU 부하 약 50%. 가속도계만 켜져 있고 구성된 포트는 TBS SmartAudio용 하나와 수신기용 하나뿐이다.
- 채널 맵이 기본(AETR)이 아니라 TAER 1234로 설정되어 있어 리뷰어가 혼동했다(양산품은 다를 수 있다고 함). 연결에는 동봉 케이블을 쓴다.
- 비행 인상: 실내 호버 스로틀 약 1/3, 소음이 작고 스로틀 반응이 즉각적이며 튜닝은 입문자에 맞춘 보수적인 값이다. 레이싱용으로는 레이트 조정이 필요하다고 평가했다.

관련: [[betaflight]], [[fpv-hardware]].

## 📰 최근 관련 소식
- [Painless360] Just out! EMAX Tinyhawk Aero, their first ever custom built 'racer' (youtube.com, 2026-10-14) — https://www.youtube.com/watch?v=O5ISivEChw0
