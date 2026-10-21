---
title: "OnFly: Onboard Zero-Shot Aerial Vision-Language Navigation toward Safety and Efficiency"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: AIModel
tags: [drone, vln, vlm, onboard, jetson-orin-nx, qwen3-vl, edge-inference]
sources: [inbox/processed/hw-20261021-model-onfly-onboard-aerial-vln.md]
confidence: medium
contested: false
contradictions: []
---

# OnFly: Onboard Zero-Shot Aerial Vision-Language Navigation toward Safety and Efficiency

- 원문: https://arxiv.org/abs/2603.10682 ; https://arxiv.org/html/2603.10682^[inbox/processed/hw-20261021-model-onfly-onboard-aerial-vln.md]
- 제작: 학계 (Guiyong Zheng, Yueting Ban, Mingjie Zhang, Juepeng Zheng, Boyu Zhou)^[inbox/processed/hw-20261021-model-onfly-onboard-aerial-vln.md]

## 핵심 사양 (arXiv, 제출 2026-03-11)
| 항목 | 값 (원문) |
|---|---|
| 구조 | 공유 지각 이중 에이전트(고빈도 목표 생성 / 저빈도 진행 모니터링), 하이브리드 keyframe+최근 프레임 메모리, semantic-geometric verifier, receding-horizon 플래너 |
| VLM | Qwen3-VL-4B-AWQ (ablation: Qwen3-VL-2B, Qwen3-VL-30B-A3B) |
| 온보드 | NVIDIA Jetson Orin NX (16GB) |
| 의사결정 에이전트 지연 | 3.83 s (baseline) -> 0.81 s (edge 배포), 4.73배 |
| 모니터링 에이전트 지연 | 7.47 s -> 1.98 s -> 1.15 s (Hybrid Memory), 6.50배; 2 s마다 1회 실행 |
| 시뮬레이션(150 과제, UE 10장면) SR | OnFly 67.8%, 최강 baseline SPF 26.4%; 충돌률 2.7% 대 42.7%; 비행시간 27.1 s |
| ablation SR | 이중 에이전트 제거 48.6%, Qwen3-VL-2B 43.4%, 30B-A3B 71.8% |

## 용도
소형 VLM으로 자연어 지시를 따라 비행하는 완전 온보드 VLN. 실기 4개 과제(보행자 추적, 장거리 복도, 잔디 경계 정밀, 다층 장애물 회피)를 수행했다고 서술.^[inbox/processed/hw-20261021-model-onfly-onboard-aerial-vln.md]

## 호환·인터페이스
시뮬레이션은 별도 데스크톱(i9-13900K, RTX 4090), 실기 플랫폼은 Jetson Orin NX 탑재 커스텀 쿼드로터. 코드는 GitHub 공개 예정이라고 초록에 기재.^[inbox/processed/hw-20261021-model-onfly-onboard-aerial-vln.md]

## 비고(미확인)
- 실기 비행의 성공률 수치는 논문에 없음(정성 서술). 제어 주기, 비행컨트롤러 종류, 전력 소모는 미확인.^[inbox/processed/hw-20261021-model-onfly-onboard-aerial-vln.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[test-time-scaling-vlm-uav]]
