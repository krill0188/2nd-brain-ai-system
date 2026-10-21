---
title: "Jet-HR2 비행 휴머노이드: 덕티드 팬 추력 벡터 제어"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, drone-hw]
sources: [inbox/processed/fetch-2026-10-21-arxiv-design-of-a-flying-humanoid-robot-based-on-thrust-vector-con.md]
confidence: medium
contested: false
contradictions: []
---

# Jet-HR2 비행 휴머노이드: 덕티드 팬 추력 벡터 제어

Li 등(arXiv 2108.11557, 2021-08)이 제안한 비행 휴머노이드 로봇 Jet-HR2 설계 논문이다. 초록 기준 요약이며 본문 수치는 확인하지 않았다.^[inbox/processed/fetch-2026-10-21-arxiv-design-of-a-flying-humanoid-robot-based-on-thrust-vector-con.md]

## 설계
- 관절 10개를 BLDC 모터와 하모닉 드라이브로 구동한다.
- 추진부는 덕티드 팬 4개: 허리에 2개 고정, 발에 2개 장착. 비행 중 발의 자세를 바꿔 추력 벡터를 제어한다.
- 낮은 추력 대 중량비에서 안정적으로 이륙하려는 목적이다. 단순화 모델과 제어 전략으로 질량 오차·관절 위치 오차가 일으키는 자세 불안정을 다룬다.

## 결과
- 발 덕티드 팬의 추력 벡터 제어로 이륙 중 회전(spin)과 다이브(dive) 거동이 억제됐다.
- 추력 대 중량비 1.17(17 kg / 20 kg)에서 이륙에 성공하고 자세를 유지했으며 이륙 높이는 1000 mm를 넘었다.

## 드론 관점
멀티로터가 아닌 덕티드 팬 + 추력 편향 방식의 비행체 사례다. 추력 대 중량비 여유가 작아도 추력 벡터로 자세를 잡는다는 점이 핵심이다. 하이브리드 지상·공중 기체 사례는 [[capsulebot-hybrid-aerial-ground-bicopter]], 추진 선정 기준은 [[fpv-motor-selection-guide]], 전원 측면은 [[drone-power-battery]] 참조.

## 📰 최근 관련 소식
- Design of a Flying Humanoid Robot Based on Thrust Vector Control (arxiv.org, 2021-08-26) — http://arxiv.org/abs/2108.11557v1
