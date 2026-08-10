---
title: "MoE 기반 강건한 UAV 멀티모달 객체 탐지"
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [drone, ai-autonomy, paper]
domain: ai-autonomy
sources: [raw/papers/drone-ai/moe-multimodal-uav-detection.md]
confidence: low
contested: false
contradictions: []
---

# MoE 기반 강건한 UAV 멀티모달 객체 탐지

Xi, Lu, Li의 저널 논문("Mixture-of-experts for robust multimodal object detection in UAV imagery with incomplete observations", *Information Fusion*, 2027-2 게재 예정)이 다루는 주제 — UAV 영상에서 일부 센서 관측이 누락되거나 불완전한 상황에서도 강건하게 동작하는 멀티모달 객체 탐지를 Mixture-of-Experts(MoE) 아키텍처로 접근한다.^[raw/papers/drone-ai/moe-multimodal-uav-detection.md]

**주의**: Crossref API가 초록을 제공하지 않아 제목·저자·저널 정보만 확보한 상태다. 구체적인 아키텍처 설계나 정량적 성능 수치는 원문(https://doi.org/10.1016/j.inffus.2026.104678) 확인 전까지 미검증이다 — confidence를 low로 둔 이유.

## 왜 중요한가

드론 탑재 센서(RGB/IR/열화상 등)는 기상·전력·시야각 문제로 특정 모달리티가 누락되는 상황이 흔하다. MoE는 모달리티별 전문가(expert) 네트워크를 조건부로 활성화해, 일부 입력이 없어도 탐지 성능 저하를 최소화하는 방향으로 접근하는 것으로 보인다(제목 기준 추정).

## 관련 개념

- [[drone-ai]] — 드론 AI 기술 전반
- [[rgb-ir-fusion-uav-detection]] — RGB-IR 융합 기반 UAV 탐지(관련 멀티모달 접근)
