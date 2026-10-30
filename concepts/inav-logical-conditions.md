---
title: "INAV Logical Conditions (Programming 탭) 개요"
created: 2026-10-26
updated: 2026-10-26
type: concept
domain: flight-control
tags: [drone, drone-sw, workflow]
sources: [inbox/processed/fetch-2026-10-26-yt-inav-logical-conditions-explained-simply.md]
confidence: low
contested: false
contradictions: []
---

# INAV Logical Conditions (Programming 탭) 개요

Painless360 영상(2026-10-25)의 자막 기준 정리. INAV 9 기준으로 Configurator의 Programming 탭이 크게 개선돼 사용이 쉬워졌다고 설명한다. 자막은 앞 8000자만 추출되어 뒷부분(나머지 믹서 규칙 설정)은 확인되지 않는다.^[inbox/processed/fetch-2026-10-26-yt-inav-logical-conditions-explained-simply.md]

## 개념
- 이름과 달리 코딩이 아니라 EdgeTX의 논리 스위치(logical switch)와 유사한 구조다: 어떤 값이 조건(참 여부, 미만, 같음, 근사 같음 등)을 만족하면 내부 논리 스위치가 켜지고, 이를 다른 기능의 활성 조건으로 쓴다.
- 조건끼리 묶거나 수학 연산을 더할 수 있으나, 기본 용도는 단순 테스트부터 시작하길 권한다.

## 자막에 나온 활용 예
- 홈 거리가 기준값을 넘으면 VTX 출력 증가.
- 피토관 등 대기속도 센서 값이 기준 미만이면 플랩 자동 전개(반대로 기준 초과 시 전개 금지).
- 3단 스위치(채널 8: 약 987/1500/2011)의 low/mid/high를 조건 0·1·2로 테스트한 뒤 믹서 규칙의 *Active* 항목에 연결해 글라이더의 기본 / 크로우(플랩 하강+에일러론 상승) / 캠버 구성을 전환.
- 믹서 탭에서 서보 규칙(예: stabilized roll 가중치 100%, 오프셋 규칙)을 특정 logic condition이 활성일 때만 적용. 서보 과구동을 피하려 오프셋 값을 조정한다.

## 참고 문서(영상 설명란)
INAV 공식 `Programming Framework.md`와 `OPERATIONS_REFERENCE.md`가 안내된다.

## 관련 문서
고정익 서보 설정 점검은 [[inav-fixed-wing-servo-direction-checklist]], 오픈소스 FC 펌웨어 비교는 [[betaflight]], 하드웨어는 [[flight-controller-hardware]]를 참조한다.

## 📰 최근 관련 소식
- [Painless360] INAV Logical Conditions Explained Simply (youtube.com, 2026-10-25) — https://www.youtube.com/watch?v=T_HLnNIOCcY
