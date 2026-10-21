---
title: "Toward Certification of Machine-Learning Systems for Low Criticality Airborne Applications"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: regulations
tags: [drone, certification, do-178c, machine-learning, dal-d, airborne]
sources: [inbox/processed/hw-20261021-ai-cert-do178c-ml-dmitriev-low-criticality-2022.md]
confidence: medium
contested: false
contradictions: []
---

# Toward Certification of Machine-Learning Systems for Low Criticality Airborne Applications

- 원문: https://arxiv.org/abs/2209.13975^[inbox/processed/hw-20261021-ai-cert-do178c-ml-dmitriev-low-criticality-2022.md]
- 저자: K. Dmitriev, J. Schumann, F. Holzapfel^[inbox/processed/hw-20261021-ai-cert-do178c-ml-dmitriev-low-criticality-2022.md]
- 발행: 2022-09-28^[inbox/processed/hw-20261021-ai-cert-do178c-ml-dmitriev-low-criticality-2022.md]

## 핵심 내용 (arXiv 초록)
기존 항공 인증 표준은 ML 이전에 만들어져 "fundamental incompatibilities"가 있다고 지적. 현행 표준의 목표(objective)를 분석해, ML 개발 워크플로에 특정 가정을 두면 저위험(low-criticality) ML 시스템에서는 표준의 모든 목표를 달성할 수 있음을 보임.^[inbox/processed/hw-20261021-ai-cert-do178c-ml-dmitriev-low-criticality-2022.md]

## 설계에 쓸 수 있는 지침
- DO-178C 등을 ML에 그대로 적용하려면 개발 워크플로 가정(데이터 관리 등)을 명시해야 함. 저위험 기능부터 적용 가능하다는 근거.^[inbox/processed/hw-20261021-ai-cert-do178c-ml-dmitriev-low-criticality-2022.md]

## 한계·미확인
- 초록만 열람. 어떤 DAL을 대상으로 했는지(초록에는 low criticality만 표기)와 구체 가정 목록, 지원 표준 버전 미확인. 후속 논문(Runway Sign Classifier)이 DAL D 준수를 이 선행 연구로 언급.^[inbox/processed/hw-20261021-ai-cert-do178c-ml-dmitriev-low-criticality-2022.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[drone-regulations]]
