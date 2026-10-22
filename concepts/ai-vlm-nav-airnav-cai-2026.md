---
title: "AirNav: A Large-Scale UAV Vision-and-Language Navigation Dataset with Natural and Diverse Instructions"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, vln, dataset, mllm, sim2real]
sources: [inbox/processed/hw-20261021-ai-vlm-nav-airnav-cai-2026.md]
confidence: medium
contested: false
contradictions: []
---

# AirNav: A Large-Scale UAV Vision-and-Language Navigation Dataset with Natural and Diverse Instructions

- 원문: https://arxiv.org/abs/2601.03707^[inbox/processed/hw-20261021-ai-vlm-nav-airnav-cai-2026.md]
- 저자: Hengxing Cai, Yijie Rao, Ligang Huang, Zanyang Zhong, Jinhan Dong, Jingjun Tan, Changhao Nai, Jue Hou, Wenhao Lu, Renxin Zhong^[inbox/processed/hw-20261021-ai-vlm-nav-airnav-cai-2026.md]
- 발행: 2026-01-07 (v1), v2 2026-05-15^[inbox/processed/hw-20261021-ai-vlm-nav-airnav-cai-2026.md]

## 핵심 내용
기존 UAV VLN 벤치마크는 현실적 항공 장면, 자연스러운 단계별 지시, 대규모를 동시에 만족하지 못한다. AirNav는 실제 도시 항공 데이터 기반 137K 내비게이션 샘플이며, 지시문은 10개 사용자 페르소나를 사용한 인간-LLM 협업 파이프라인으로 생성. 전통 모델부터 멀티모달 LLM까지 통일 지표로 평가. SFT+강화 파인튜닝으로 학습한 AirVLN-R1은 test-unseen 분할에서 성공률 51.82%(저자 주장 SOTA). 실기 UAV 시험은 시뮬레이션에서 실세계 전이의 예비 증거로 제시. 데이터셋과 코드 공개.^[inbox/processed/hw-20261021-ai-vlm-nav-airnav-cai-2026.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- 137K 샘플, test-unseen 성공률 51.82%.^[inbox/processed/hw-20261021-ai-vlm-nav-airnav-cai-2026.md]

## 한계·미확인
- 초록만 확인. 실기 시험의 구체 조건·수치 미확인.^[inbox/processed/hw-20261021-ai-vlm-nav-airnav-cai-2026.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[test-time-scaling-vlm-uav]]

## 📰 최근 관련 소식
- Axon Vision Accelerates U.S. Growth Strategy with Expanded U.S.Operating Presence and Strategic Leadership (www.suasnews.com, Wed, 21 Oc) — https://www.suasnews.com/2026/10/axon-vision-accelerates-u-s-growth-strategy-with-expanded-u-s-operating-presence-and-strategic-leadership/
