---
title: "INAV 고정익 서보 방향 오류 3단계 점검"
created: 2026-10-07
updated: 2026-10-07
type: concept
domain: flight-control
tags: [drone, drone-sw, workflow]
sources: [inbox/processed/fetch-2026-10-07-yt-why-cant-i-get-my-servos-moving-in-the-right-direction-inav.md]
confidence: low
contested: false
contradictions: []
---

# INAV 고정익 서보 방향 오류 3단계 점검

Painless360의 보충 영상(2026-10-06, 자막 기준)이 정리한 INAV 고정익 서보 방향 문제 해결 순서다. 단일 출처이며
영상 발언을 그대로 옮겼다(confidence low).
^[inbox/processed/fetch-2026-10-07-yt-why-cant-i-get-my-servos-moving-in-the-right-direction-inav.md]

## 점검 항목

1. **라디오 채널은 반전하지 않는다**: 스틱을 우상단으로 두면 에일러론·엘리베이터·스로틀·러더가 모두 최댓값이어야 한다.
   INAV는 올바른 라디오 설정을 전제로 만들어졌으므로 채널 반전이나 트림 조작을 하지 않는다.
2. **FC 설치 방향**: 기체 기수를 들었을 때 INAV Configurator의 가상 기체가 같은 방향으로 움직이면 정상이다. FC에 인쇄된 화살표는
   기수 방향이며, 다른 방향으로 설치하면 Configurator의 board alignment에서 보정한다(영상 예시는 180° 회전).
3. **출력 연결**: 에일러론·엘리베이터·러더를 각 서보 출력에 맞게 꽂는다. INAV는 에일러론 출력을 좌·우 2개로 만들어 독립 관리한다.
   연결이 맞는데 방향만 틀리면 INAV에서 서보를 반전한다.

## 증상별 판단

- 수동 모드에서는 정상인데 Angle 모드에서 보정이 반대이거나 그 반대 경우는 위 세 항목 중 하나를 놓친 것이다.
  영상은 이 세 가지로 약 95%가 해결된다고 말한다.
- 엘레본·V-tail 믹싱이 안 맞을 때는 별도 영상을 참조하라고 안내한다(내용은 자막에 없음).

## 관련 개념

- [[fc-firmware-comparison]] — Betaflight/INAV/ArduPilot 비교
- [[flight-controller-hardware]] — FC 보드와 주변기기
- [[sensor-calibration]] — 센서 보정

## 📰 최근 관련 소식
- [Painless360] Why can't I get my servos moving in the right direction (INAV)? (youtube.com, 2026-10-06) — https://www.youtube.com/watch?v=FdalLhp_I3w
