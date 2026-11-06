---
title: EdgeTX Custom Audio Setup
created: 2026-08-03
updated: 2026-11-04
type: concept
tags: [drone, hardware, fpv, transmitter, edgetx]
sources: [raw/articles/fetch-2026-08-03-rss-oscarliang-fpv.md, inbox/fetch-2026-08-05-yt-edgetx-trainer-setup-using-a-cable-super-simple.md, inbox/processed/fetch-2026-10-21-yt-why-modern-rc-radio-power-buttons-are-safer-than-you-think.md, inbox/processed/fetch-2026-11-04-yt-how-to-change-the-sound-volume-on-your-radio-an-edgetx-quick.md]
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# EdgeTX Custom Audio Setup

EdgeTX 라디오에서 SD 카드의 커스텀 오디오 파일을 재생하고 볼륨을 노브로 조정하는 설정 방법.

## 주요 기능

- **커스텀 오디오**: SD 카드에서 사용자 정의 오디오 파일 재생
- **음성 알림**: 스위치 트리거로 음성 알림, 효과음 재생
- **볼륨 조정**: 로터리 노브 또는 슬라이더로 볼륨 제어
- **활용**: 음악, 시작음, 음성 알림, 효과음 추가 가능

## 트레이너 모드

EdgeTX에서는 케이블을 이용한 트레이너 설정이 가능하다. RadioMaster SBUS 무선 트레이너 모듈 등을 활용하여 마스터/학생 라디오 간 조종권 전환 및 교육용 듀얼 컨트롤이 가능하다.

## 관련 개념

- [[betaflight]] — FPV 드론 비행 제어 소프트웨어
- [[fpv-hardware]] — FPV 하드웨어 동향

## 최신 근거 연결 (2026-10-21)

- EdgeTX 푸시버튼 라디오의 전원 오조작 방지 동작(켜고 끌 때 길게 누르기, ELRS 수신기 연결 시 Enter 확인)은 단일 시연 영상 기준으로 정리했다(confidence low): [[rc-radio-power-button-safety]]^[inbox/processed/fetch-2026-10-21-yt-why-modern-rc-radio-power-buttons-are-safer-than-you-think.md]

## 📰 최근 관련 소식
- [Painless360] New tool! Customise your radio and edit EdgeTX themes easily! (youtube.com, 2026-08-21) — https://www.youtube.com/watch?v=A-4OwLXs6xg
- [Painless360] Why I don't like sharing a fixed wing INAV setup file (diff_all or dump) (youtube.com, 2026-09-01) — https://www.youtube.com/watch?v=VcIYB40QFXw
- [Painless360] 'Pro Grade' ELRS PWM Receivers: The new RadioMaster ER16, ER12 and ER3Pro (youtube.com, 2026-09-10) — https://www.youtube.com/watch?v=3vInqhMlb1I
- [Painless360] How to change the sound volume on your radio (an EdgeTX quick tip!) (youtube.com, 2026-11-03) — https://www.youtube.com/watch?v=afJimVKM7Vo

## 라디오 음량 조절 (2026-11-04)

- SD카드 음성 파일은 사전 녹음된 것이며 파일 자체가 음량을 좌우하지 않는다. 음량은 시스템 메뉴(톱니 → Sound)의 volume/beep/wave/background music 값과 모델 메뉴 Special Functions의 Volume 기능(로터리·슬라이더에 할당)에서 결정된다. Sound 모드는 quiet/alarm/no key/all 중 선택. 슬라이더가 낮게 놓여 있으면 소리가 작아질 수 있다. 근거: Painless360 영상 자막.^[inbox/processed/fetch-2026-11-04-yt-how-to-change-the-sound-volume-on-your-radio-an-edgetx-quick.md]
