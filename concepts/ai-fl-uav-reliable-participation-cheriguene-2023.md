---
title: "Towards Reliable Participation in UAV-Enabled Federated Edge Learning on Non-IID Data"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, federated-learning, poisoning, client-selection, non-iid]
sources: [inbox/processed/hw-20261021-ai-fl-uav-reliable-participation-cheriguene-2023.md]
confidence: medium
contested: false
contradictions: []
---

# Towards Reliable Participation in UAV-Enabled Federated Edge Learning on Non-IID Data

- 원문: https://arxiv.org/abs/2312.10411^[inbox/processed/hw-20261021-ai-fl-uav-reliable-participation-cheriguene-2023.md]
- 저자: Youssra Cheriguene, Wael Jaafar, Halim Yanikomeroglu, Chaker Abdelaziz Kerrache^[inbox/processed/hw-20261021-ai-fl-uav-reliable-participation-cheriguene-2023.md]
- 발행: 2023-12-16^[inbox/processed/hw-20261021-ai-fl-uav-reliable-participation-cheriguene-2023.md]

## 핵심 내용
UAV를 클라이언트로 하는 연합학습에서 데이터가 매우 비IID이고, 이동성·불가용·저배터리로 이탈이 생기며 악의적 UAV가 포이즈닝 공격을 할 수 있다. 기존 클라이언트 선택은 신뢰도를 무시한다. 빠르고 신뢰도 높은 UAV를 선호하고 악의적 UAV를 배제하는 선택 기법을 제안, 여러 공격 시나리오에서 수렴, 정확도, 전반 성능이 기준 기법보다 낫다고 보고.^[inbox/processed/hw-20261021-ai-fl-uav-reliable-participation-cheriguene-2023.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- 초록은 정량 수치를 제시하지 않음. 신뢰도 기반 참여자 선택이 포이즈닝 대응책이라는 구조만 확인.^[inbox/processed/hw-20261021-ai-fl-uav-reliable-participation-cheriguene-2023.md]

## 한계·미확인
- 초록만 확인. 차등 프라이버시(DP) 적용 여부는 초록에 없음(미확인). 실험 규모 미확인.^[inbox/processed/hw-20261021-ai-fl-uav-reliable-participation-cheriguene-2023.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[swarm-coordination]]
