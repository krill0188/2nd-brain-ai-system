---
title: "Runway Sign Classifier: A DAL C Certifiable Machine Learning System"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: regulations
tags: [drone, certification, do-178c, dal-c, dnn, redundancy, dissimilar]
sources: [inbox/processed/hw-20261021-ai-cert-do178c-ml-runway-sign-classifier-dal-c-2023.md]
confidence: medium
contested: false
contradictions: []
---

# Runway Sign Classifier: A DAL C Certifiable Machine Learning System

- 원문: https://arxiv.org/abs/2310.06506^[inbox/processed/hw-20261021-ai-cert-do178c-ml-runway-sign-classifier-dal-c-2023.md]
- 저자: Konstantin Dmitriev, Johann Schumann, Islam Bostanov, Mostafa Abdelhamid, Florian Holzapfel^[inbox/processed/hw-20261021-ai-cert-do178c-ml-runway-sign-classifier-dal-c-2023.md]
- 발행: 2023-10-10^[inbox/processed/hw-20261021-ai-cert-do178c-ml-runway-sign-classifier-dal-c-2023.md]

## 핵심 내용 (arXiv 초록)
공항 표지 검출·분류 DNN 기반 기상 시스템 사례. 선행 연구에서 DAL D 준수를 보였고, 이 논문에서 DAL C로 상향. 방법: "two redundant and dissimilar Deep Neural Networks"의 아키텍처 완화 기법 + ML 전용 데이터 관리 기법. ML 모델 추적성·설명가능성 문제와 전통적 커버리지 지표의 부적합을 인증 난제로 명시.^[inbox/processed/hw-20261021-ai-cert-do178c-ml-runway-sign-classifier-dal-c-2023.md]

## 설계에 쓸 수 있는 지침
- DAL C를 노릴 때 이종(dissimilar) 이중 DNN 구성이 실제 사례로 제시됨. 단 EASA Issue 03은 "두 독립 AI/ML 구성요소의 아키텍처 이점 인정은 not accepted"라고 상반된 입장(별도 파일 참고) — 규제 입장과 학술 제안이 다름.^[inbox/processed/hw-20261021-ai-cert-do178c-ml-runway-sign-classifier-dal-c-2023.md]

## 한계·미확인
- 초록만 열람. 정량 성능, 실제 인증기관 수용 여부 미확인(제목은 "certifiable"이며 실제 인증 취득 아님).^[inbox/processed/hw-20261021-ai-cert-do178c-ml-runway-sign-classifier-dal-c-2023.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[drone-regulations]]
