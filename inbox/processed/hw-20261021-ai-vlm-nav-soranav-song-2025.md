---
title: "SoraNav: Adaptive UAV Task-Centric Navigation via Zeroshot VLM Reasoning"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: ai-autonomy
source: https://arxiv.org/abs/2510.25191
authors: Hongyu Song, Rishabh Dev Yadav, Cheng Guo, Wei Pan
published: 2025-10-29 (v1), v3 2026-03-04
tags: [drone, vlm, zero-shot, navigation, px4, micro-uav]
---
## 핵심 내용
자연어 지시 기반 UAV 내비게이션. VLM의 정밀 공간 추론 약점은 Multi-modal Visual Annotation(3D 기하 정보를 2D 입력에 인코딩)으로, VLM 출력의 환각/기하적 비실현 문제는 Adaptive Decision Making(탐색 이력으로 제안 검증, 실패 시 기하 기반 탐색으로 폴백)으로 보완. 커스텀 PX4 기반 마이크로 UAV에서 구동. 기존 SOTA 대비 2.5D 시나리오에서 SR +25.7%, SPL +17.3%, 복잡 3D에서 SR +39.3%, SPL +24.7%.

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- VLM 제안을 이력/기하로 검증하는 폴백 구조가 위 개선 수치와 함께 보고됨.

## 한계·미확인
- 초록만 확인. VLM이 온보드인지 오프보드인지, 지연 수치 미확인.
