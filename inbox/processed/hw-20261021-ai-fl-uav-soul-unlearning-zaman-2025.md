---
title: "Sky of Unlearning (SoUL): Rewiring Federated Machine Unlearning via Selective Pruning"
created: 2026-10-22
captured: 2026-10-22
type: paper
domain: ai-autonomy
source: https://arxiv.org/abs/2504.01705
authors: Md Mahabub Uz Zaman, Xiang Sun, Jingjing Yao
published: 2025-04-02
tags: [drone, federated-learning, unlearning, data-poisoning, model-inversion, internet-of-drones]
---
## 핵심 내용 (arXiv 초록)
Internet of Drones(IoD)의 연합학습은 "data poisoning and model inversion" 같은 공격에 취약하다고 명시. 대응으로 federated unlearning(FU): 적대적 데이터 기여의 영향을 제거. SoUL은 선택적 가지치기로 unlearning에 영향이 큰 뉴런을 식별해 제거하되 전체 성능 영향은 최소화. 시뮬레이션에서 기존 unlearning 방법보다 우수하고 전체 재학습과 비슷한 정확도, 계산·통신 오버헤드 감소를 주장.

## 설계에 쓸 수 있는 지침
- 오염 클라이언트 발견 후 재학습 없이 영향 제거하는 사후 대응 수단으로 unlearning을 포함 검토.

## 한계·미확인
- 초록만 열람. 정확도·오버헤드 수치, 데이터셋, 공격 비율 미확인. 모델 반전에 대한 정량 방어 효과는 초록에 없음.
