---
title: "강화학습 기반 단일 프로펠러 모듈형 UAV의 비행 및 결합 제어"
created: 2026-10-27
updated: 2026-10-27
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, swarm]
sources: [inbox/processed/fetch-2026-10-27-kci-강화학습-기반-단일-프로펠러-모듈형-uav의-비행-및-결합-제어.md]
confidence: low
contested: false
contradictions: []
---

# 강화학습 기반 단일 프로펠러 모듈형 UAV의 비행 및 결합 제어

김현민(국립금오공과대학교)의 2026년 한국소음진동공학회논문집 논문. 원문은 비공개라 초록 앞부분만 근거다.^[inbox/processed/fetch-2026-10-27-kci-강화학습-기반-단일-프로펠러-모듈형-uav의-비행-및-결합-제어.md]

## 내용
- **기체**: 각 유닛이 프로펠러 1개와 베인 4개로 이루어진 정육면체 모듈형 UAV이며, 공중에서 다른 유닛과 결합한다.
- **학습 환경**: 물리 기반 시뮬레이터 NVIDIA Isaac Lab에서 강화학습 정책을 학습한다 ([[nvidia-isaac-lab]]).
- **단일 모듈**: 호버링과 점 대 점 항법을 PPO로 학습한다.
- **다중 모듈**: 3개 모듈의 순차적 공중 결합을 중앙집중 학습·분산 실행 구조의 MAPPO로 학습한다.
- 초록이 중간에서 끊겨 성능 수치와 실기체 검증 여부는 확인되지 않는다.

## 관련 문서
다중 UAV 협조 관점은 [[dynamic-fleet-sizing-uav-relays-post-disaster-mpc]], RL 기반 비행 제어 사례는 [[diffdreamer-world-model-differentiable-simulation]]을 참조한다.

## 📰 최근 관련 소식
- 강화학습 기반 단일 프로펠러 모듈형 UAV의 비행 및 결합 제어 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003395887
