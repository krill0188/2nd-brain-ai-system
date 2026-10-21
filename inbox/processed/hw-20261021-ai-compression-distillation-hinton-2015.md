---
title: "Distilling the Knowledge in a Neural Network"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: edge-ai-compute
source: https://arxiv.org/abs/1503.02531
authors: Geoffrey Hinton, Oriol Vinyals, Jeff Dean
published: 2015-03-09 (NIPS 2014 Deep Learning Workshop)
tags: [drone, ai, model-compression, distillation, edge-inference]
---
## 핵심 내용
앙상블의 지식을 배포하기 쉬운 단일 모델로 압축하는 증류 기법. MNIST 결과와 상용 음향 모델 개선을 보이고, 전체 모델과 세밀 클래스를 담당하는 다수의 specialist 모델 앙상블도 제안(specialist는 빠르게 병렬 학습 가능).

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 정량 수치는 초록에 없음.
- 시사점: 큰 검출/제어 모델을 엣지용 소형 모델로 옮기는 기본 기법.

## 한계·미확인
수치·드론 적용 미확인.
