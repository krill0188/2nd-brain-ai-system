---
title: "VLN on the Fly: An Onboard Vision-Language Navigation Stack for Aerial Robots"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: AIModel
tags: [drone, vln, vlm, onboard, jetson-orin-nx, int4, qwen]
sources: [inbox/processed/hw-20261021-model-vln-on-the-fly.md]
confidence: medium
contested: false
contradictions: []
---

# VLN on the Fly: An Onboard Vision-Language Navigation Stack for Aerial Robots

- 원문: https://arxiv.org/abs/2609.20191 ; https://arxiv.org/html/2609.20191^[inbox/processed/hw-20261021-model-vln-on-the-fly.md]
- 제작: 학계 (Marco S. Tayar et al., Marcelo Becker 그룹)^[inbox/processed/hw-20261021-model-vln-on-the-fly.md]

## 핵심 사양 (arXiv, 제출 2026-08-07)
| 항목 | 값 (원문) |
|---|---|
| 파이프라인 | 양자화 VLM이 지시를 이미지 셀로 매핑 -> 깊이로 3D 목표 -> B-spline 궤적 -> 사전학습 RL 정책이 모터 명령 추적 |
| VLM | Qwen-3.5-2B, INT4 |
| 쿼리 지연 | 중앙값 0.79 s, 95퍼센타일 0.88 s, 최대 1.12 s (N=1,865); time-to-first-token 중앙값 0.60 s; VLM 쿼리율 0.5 Hz |
| 하드웨어 | NVIDIA Jetson Orin NX + Pixhawk 6C (모션캡처로 자세 제공, 완전 자립 아님) |
| 실내 비행 | 15회 중 13회 도달(87%, Wilson 95% CI 0.62-0.96), 평균 목표 오차 5.72 cm, 평균 GPU 사용률 39.3% |
| 혼잡 환경 | 6회 시험에서 충돌 없는 궤적 추종 |

## 용도
온보드 VLM 접지 + 고전 플래너 + RL 저수준 정책의 분리형 구조로 추론/제어 계층을 분리.^[inbox/processed/hw-20261021-model-vln-on-the-fly.md]

## 호환·인터페이스
Pixhawk 6C, Jetson Orin NX, RealSense D435i RGB-D(검색 요약 기준, 본문 직접 확인은 일부), OptiTrack 모션캡처 자세.^[inbox/processed/hw-20261021-model-vln-on-the-fly.md]

## 비고(미확인)
- 제어/플래너 주기는 논문에서 미보고. 실외 비행 없음(통제된 실내 볼륨). 저자 보고 수치만.^[inbox/processed/hw-20261021-model-vln-on-the-fly.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[test-time-scaling-vlm-uav]]
