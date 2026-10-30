---
title: "DIY 21700 4S 파워뱅크 제작 (Joshua Bardwell)"
created: 2026-10-27
updated: 2026-10-27
type: concept
domain: hardware
tags: [drone, drone-hw, fpv]
sources: [inbox/processed/fetch-2026-10-27-yt-ithis-power-bank-i-made-it-myself.md]
confidence: low
contested: false
contradictions: []
---

# DIY 21700 4S 파워뱅크 제작 (Joshua Bardwell)

FPV 유튜버 Joshua Bardwell의 2026-10-26 영상. 자막 앞 8000자만 근거이며 조립 절차 후반부는 확인되지 않는다.^[inbox/processed/fetch-2026-10-27-yt-ithis-power-bank-i-made-it-myself.md]

## 구성
- **팩**: 4S1P, 21700 셀 4개(5,000 mAh급, 개당 5~6달러 이하의 저가 셀). 4S 전압 기준이라 1S 기준으로 표기하는 USB 파워뱅크의 약 20,000 mAh급과 비슷하다고 추정하나 확신하지 않는다고 밝혔다.
- **출력**: XT60와 65 W USB PD 전원 보드. 고글 전원, 작업대 전원, 폰 고속 충전용이다. 출력 전용이며 USB 충전 입력은 없고 XT60로 LiPo 충전기를 써서 충전한다.
- **비고방전**: 비행용 팩이 아니다. 니켈 스트립 0.10 mm는 5~7 A 정도를 감당하며 실사용은 대개 2 A 미만이다.
- **케이스**: 온라인 공개 3D 프린트 케이스를 개조해 셀 베이를 5개로 늘리고 USB 보드가 들어가도록 벽 간격을 넓혔다. USB 보드는 구매 시기에 따라 인덕터가 달라 맞지 않을 수 있다.
- **배선**: XT60와 USB 보드 배선은 18 AWG. 65 W는 낮은 팩 전압에서 5~7 A에 해당한다.

## 제작 방식
- 셀에 직접 납땜하면 과열로 성능 저하나 셀 손상 위험이 있어 **니켈 스트립 스폿 용접**을 쓴다. 절연에는 셀 크기 피시페이퍼 링과 접착식 피시페이퍼를 쓴다. 밸런스 커넥터는 기성품이다.

## 관련 문서
배터리 관리는 [[fpv-battery-maintenance]], 충전 안전은 [[lipo-charging-cabinet-fire-test]]를 참조한다.

## 📰 최근 관련 소식
- [Joshua Bardwell] I💖this power bank! I MADE IT MYSELF! (youtube.com, 2026-10-26) — https://www.youtube.com/watch?v=o9-2A8G34QU
