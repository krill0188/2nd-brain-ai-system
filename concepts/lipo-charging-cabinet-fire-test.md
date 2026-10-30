---
title: "LiPo 충전·보관 캐비닛 화재 테스트 (Joshua Bardwell)"
created: 2026-10-18
updated: 2026-10-18
type: concept
domain: hardware
ontology_class: Battery
tags: [drone, drone-hw, fpv]
sources: [inbox/processed/fetch-2026-10-18-yt-i-exploded-a-lipo-in-a-600-safe-it-shot-flames.md]
confidence: low
contested: false
contradictions: []
---

# LiPo 충전·보관 캐비닛 화재 테스트

**출처**: Joshua Bardwell YouTube (2026-10-17), 자막 기반. 단일 제품·단일 시연이라 일반화하기 어렵다.

LiPo를 금속 캐비닛에 넣고 충전 중 의도적으로 발화시켜 캐비닛 성능을 확인한 영상이다. 진행자는 대부분의 사용자가 LiPo를 방화 환경에서 충전·보관하지 않는다고 말하고, YolinTech 리튬 배터리 충전 캐비닛을 시험했다.^[inbox/processed/fetch-2026-10-18-yt-i-exploded-a-lipo-in-a-600-safe-it-shot-flames.md]

## 캐비닛 구성 (영상 설명 기준)
- **이중 벽 구조**: 외벽과 내벽 사이에 공간이 있어 단일 철판처럼 열을 바로 전달하지 않는다. 단열 패딩 유무는 진행자도 확신하지 못했다.
- **온도 센서 + 환기 팬**: 설정 온도를 넘으면 한쪽 흡기, 반대쪽 팬이 작동한다. 냉방 장치는 없어 주변 공기 이상으로는 낮추지 못한다.
- **잠금 도어**: 키 잠금과 자물쇠를 걸 수 있는 핸들이 있어 아이 등의 무단 접근을 줄인다.
- **전원 멀티탭 + 소화 포드 2개**(상단·하단 선반): 열을 감지하면 소화제를 방출한다. 성분은 진행자도 모른다고 했다.
- 진행자는 금속 캐비닛만으로는 LiPo 화재를 막지 못하며, 열이 두꺼운 금속을 통해서도 인접 물체를 발화시킬 수 있다고 설명했다.

## 시험 결과 (자막 관찰)
- 충전 중 내부 온도 약 30°C, 충전기 약 40°C, 배터리 약 35°C, 주변 18~19°C 부근에서 팬이 내부 온도를 유지했다.
- 이후 배터리에 핫스팟(약 50°C 언급)이 생기고 부풀었으며 14.6 V 시점에 셀이 차례로 터졌다(3셀 언급).
- 첫 폭발 후에도 추가 폭발이 있었고, 문 앞쪽으로 불꽃·스파크가 새어 나왔다. 진행자는 "화염이 잘 격리됐다"고 말하다가 "그렇지 않았다"고 정정했다.
- 외부 온도는 약 57~60°C로, 근처 가연물을 발화시킬 정도는 아니라고 평가했다. 개방 후 배터리는 150°C를 표시했다.
- 소화 포드가 작동한 것으로 보였으나 효과는 알 수 없다고 했다. 같은 충전기(D6 Duo)는 이후에도 켜졌다.
- 진행자는 현재 대부분의 사용자 방식보다는 낫다고 결론 냈다.

## 한계
자막이 마지막에서 끊겨 최종 결론 전문은 확인되지 않는다. 영상 앞부분은 스폰서 광고이며, 제품 할인 코드가 설명란에 있다. 배터리 사양·충전 조건은 자막에 없다.

관련: [[drone-power-battery]], [[fpv-battery-maintenance]], [[uav-battery-soh-transfer-learning]].

## 📰 최근 관련 소식
- [Joshua Bardwell] I Exploded a LiPo in a $600 Safe (It Shot Flames) (youtube.com, 2026-10-17) — https://www.youtube.com/watch?v=H_eHspF-6KM
- [Joshua Bardwell] Tactical backpacks are better. Why I switched! // PGYTECH ONEMO TACTICAL BACKPACK (youtube.com, 2026-10-21) — https://www.youtube.com/watch?v=lJRyfqrutTE
- [Joshua Bardwell] I💖this power bank! I MADE IT MYSELF! (youtube.com, 2026-10-26) — https://www.youtube.com/watch?v=o9-2A8G34QU
