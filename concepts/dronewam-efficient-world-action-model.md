---
title: "DroneWAM: Efficient World Action Model for Drone Visual Navigation"
created: 2026-09-30
updated: 2026-09-30
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources:
  - inbox/processed/fetch-2026-09-30-arxiv-dronewam-efficient-world-action-model-for-drone-visual-navig.md
  - raw/papers/_unclassified/dronewam-efficient-world-action-model-for-drone-visual-navigation.md
confidence: medium
contested: false
contradictions: []
---

# DroneWAM: Efficient World Action Model for Drone Visual Navigation

2026-09-27 arXiv 공개 논문(2609.33148v1). 드론 시각 내비게이션을 위한 효율적 world-action
model을 제안한다. JEPA 기반 아키텍처로 미래 상태를 표현 공간(latent space)에서 직접 예측해,
명시적 미래 이미지 생성 비용을 피한다.^[inbox/processed/fetch-2026-09-30-arxiv-dronewam-efficient-world-action-model-for-drone-visual-navig.md]

## 핵심 구조

- **JEPA 기반 world model**: 후보 행동이 미래 관측에 미칠 영향을 이미지 대신 표현 공간에서 예측.
- **사전학습 Resampler**: dense encoder 특징을 더 적은 latent 토큰으로 압축해, 매 상상(rollout)
  스텝마다 반복되는 연산량을 절감.
- **Adaptive Rollout**: 선호 학습(preference-trained)된 Gate가 현재 장면에 따라 예측 깊이를
  동적으로 할당. 평균 예측 깊이를 8에서 4.58로 줄이면서 궤적 정확도는 오히려 향상.
- **DroneNav-6D 데이터셋**: RGB 관측·6자유도 비행 궤적·제어 명령·랜덤 바람 교란이 동기화된
  시뮬레이션 시각 내비게이션 데이터셋. 공중 특유의 풍부한 기동 학습을 지원하기 위해 구축.

## 성과

DroneNav-6D 벤치마크에서 비교 대상 방법 중 최고 궤적 정확도를 달성. 적응형 rollout이 연산량
절감과 정확도 향상을 동시에 달성함을 보여, 장면별 예측 연산 할당이 효과적임을 입증했다. 코드와
데이터는 공개 예정(https://github.com/1e12Leon/DroneWAM). Zotero 인제스트로 확보한 완전한
초록판 원문(raw/papers)에서도 동일 수치가 확인되어 최초 inbox 캡처 내용이 재확증됐다.^[raw/papers/_unclassified/dronewam-efficient-world-action-model-for-drone-visual-navigation.md]

## 관련 개념

- [[skyjepa-world-models]] — 드론 응용 JEPA 기반 world model 계열 선행 연구
- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용
- [[drone-ai-agents]] — 드론 AI 자율 의사결정 아키텍처
