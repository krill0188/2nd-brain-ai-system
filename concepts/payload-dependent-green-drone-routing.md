---
title: "페이로드 의존 에너지 효율 드론 배송 경로 계획"
created: 2026-10-17
updated: 2026-10-18
type: concept
domain: ops-mission
tags: [drone, ops-mission]
sources: [inbox/processed/fetch-2026-10-17-arxiv-energy-efficient-drone-logistics-for-last-mile-delivery-impl.md, inbox/processed/fetch-2026-10-18-arxiv-physics-aware-truck-and-drone-delivery-planning-using-optimi.md, inbox/processed/fetch-2026-10-18-arxiv-impact-of-spatial-proximity-on-drone-services.md]
confidence: medium
contested: false
contradictions: []
---

# 페이로드 의존 그린 드론 라우팅

**출처**: arXiv 2604.07514 (2026-04-08)

드론 에너지 소비는 거리뿐 아니라 적재 중량에 의존하므로 다중 정차 배송에서 매 배송 후 소비율이 변한다. 에너지 최소화 라우팅 문제를 연구한다.^[inbox/processed/fetch-2026-10-17-arxiv-energy-efficient-drone-logistics-for-last-mile-delivery-impl.md]

## 반직관적 결과
- 더 긴 경로가 더 짧은 경로보다 에너지를 덜 쓸 수 있다.^[inbox/processed/fetch-2026-10-17-arxiv-energy-efficient-drone-logistics-for-last-mile-delivery-impl.md]
- 단일 고객 개별 투어가 다중 정차 투어보다 나을 수 있다.^[inbox/processed/fetch-2026-10-17-arxiv-energy-efficient-drone-logistics-for-last-mile-delivery-impl.md]
- 크기가 다른 드론의 이질 함대가 수요에 용량을 맞춰 더 효율적일 수 있다.^[inbox/processed/fetch-2026-10-17-arxiv-energy-efficient-drone-logistics-for-last-mile-delivery-impl.md]
- 수치 실험: 67% 사례에서 에너지 절감, 평균 2.17%, 최대 5.97%(최소 거리 라우팅 대비).^[inbox/processed/fetch-2026-10-17-arxiv-energy-efficient-drone-logistics-for-last-mile-delivery-impl.md]

## 관련
[[drone-delivery-news]], [[multirotor-energy-power-models]] 참조.

## 최신 근거 연결 (2026-10-18)

- 강화: 비행 물리를 단순화하면 배송 계획이 최적에서 벗어난다는 전제를 별개 논문이 지지한다. 트럭-드론 투어 계획에서 물리 반영 모델이 투어 시간과 에너지를 개선했다(초록 기준, 수치 없음): [[physics-aware-truck-drone-delivery-planning]]^[inbox/processed/fetch-2026-10-18-arxiv-physics-aware-truck-and-drone-delivery-planning-using-optimi.md]
- 근접 비행하는 드론 간 상호 에너지 영향이라는 다른 에너지 요인을 시연형 논문이 다룬다: [[drone-proximity-energy-impact-delivery]]^[inbox/processed/fetch-2026-10-18-arxiv-impact-of-spatial-proximity-on-drone-services.md]
