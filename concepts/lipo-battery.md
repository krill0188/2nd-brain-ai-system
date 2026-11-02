---
title: "LiPo Battery"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [hardware, battery, lipo, power-system]
sources: []
confidence: medium
contested: false
contradictions: []
domain: hardware
---

# LiPo Battery

리튬 폴리머 배터리는 고출력 방전 특성과 가벼운 무게로 멀티콥터 및 RC 항공기에서 가장 널리 사용되는 리튬 이온 배터리 유형이다. 주로 고성능 비행에 사용되며, 셀당 전압이 3.7V이며 여러 셀을 직렬·병렬로 연결하여 용량과 전압을 조절할 수 있다.

## 개요

eCalc 등 RC 계산 툴에서 전원 시스템의 핵심 구성 요소로 언급되며, multicopter 계산 시 반드시 정의해야 할 요소 중 하나다. 사용자는 배터리 드롭다운 리스트에서 배터리를 선택하고, 직렬 및 병렬로 구성된 셀 수를 조정한다. 대형 프로펠러를 활용한 효율적인 비행을 위해 배터리 용량과 전압 설정이 중요한 역할을 한다.

## 핵심 파라미터

| 파라미터 | 설명 |
|---|---|
| 셀 구성 | 직렬(S) 및 병렬(P) 연결 방식으로 전압과 용량 조정 가능 |
| 셀당 전압 | nominal 3.7V (완전 충전 시 셀당 4.2V) |
| 방전률(C-rating) | 최대 지속 방전 전력을 나타내는 등급 |
| 용량(mAh) | 배터리에 저장될 수 있는 전력량 |

## 활용처

- 전기 멀티콥터 및 고정익 RC 항공기의 주요 전원 공급원
- eCalc 등 계산 툴을 통한 모터 및 프로펠러 매칭 시 필수 입력값
- 배터리 용량과 전압 설정이 비행 시간과 출력에 직접적인 영향을 미침

## 관련 페이지

- [[Battery]] — 배터리 전반을 아우르는 개념 page
- [[Power System]] — 동력 시스템 전반의 구성 요소 및 원리

## 출처

- (사용자 재확인 필요) original source: eCalc RC Calculator documentation excerpt
- original source: xcopterCalc Help - Hilfe

## 참고

[[amprius-sicore-battery]] [[battery-bar]]
