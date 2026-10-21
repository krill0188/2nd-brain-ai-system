---
title: "Approach Towards Semi-Automated Certification for Low Criticality ML-Enabled Airborne Applications"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: regulations
tags: [drone, certification, do-178c, yolov8, assurance-profile, reconnaissance]
sources: [inbox/processed/hw-20261021-ai-cert-do178c-ml-semi-automated-sridhar-2025.md]
confidence: medium
contested: false
contradictions: []
---

# Approach Towards Semi-Automated Certification for Low Criticality ML-Enabled Airborne Applications

- 원문: https://arxiv.org/abs/2501.17028^[inbox/processed/hw-20261021-ai-cert-do178c-ml-semi-automated-sridhar-2025.md]
- 저자: Chandrasekar Sridhar, Vyakhya Gupta, Prakhar Jain, Karthik Vaidhyanathan^[inbox/processed/hw-20261021-ai-cert-do178c-ml-semi-automated-sridhar-2025.md]
- 발행: 2025-01-28^[inbox/processed/hw-20261021-ai-cert-do178c-ml-semi-automated-sridhar-2025.md]

## 핵심 내용 (arXiv 초록)
"Traditional standards, like DO 178C ... do not fully cover the unique aspects of ML"이라는 전제. 저위험 ML 시스템용 반자동 인증 접근: 데이터·모델 검증, 복원력(resilience) 평가, 사용성 보증; 시스템 속성에 따른 인증 엄격도 분류; 평가 결과를 ML 구성요소 신뢰도 척도로 합치는 Assurance Profile; 인간 감독 통합. 사례: 정찰·감시 항공기의 군용/민간 차량 실시간 분류 YOLOv8 기반 객체 검출.^[inbox/processed/hw-20261021-ai-cert-do178c-ml-semi-automated-sridhar-2025.md]

## 설계에 쓸 수 있는 지침
- 드론 정찰용 YOLO 검출기를 대상으로 한 인증 접근 사례. 엄격도를 시스템 속성으로 분류해 낮은 위험 기능에 가볍게 적용하는 방식.^[inbox/processed/hw-20261021-ai-cert-do178c-ml-semi-automated-sridhar-2025.md]

## 한계·미확인
- 초록만 열람. Assurance Profile 점수 기준과 수치, 규제기관 수용 여부 미확인. 학술 제안으로 EASA/EUROCAE 요건과의 대응 관계는 미확인.^[inbox/processed/hw-20261021-ai-cert-do178c-ml-semi-automated-sridhar-2025.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[drone-regulations]]
