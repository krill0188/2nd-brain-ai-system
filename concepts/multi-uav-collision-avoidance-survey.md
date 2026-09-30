---
title: "다중 UAV 딥러닝 충돌회피 서베이"
created: 2026-08-07
updated: 2026-09-30
type: concept
tags: [drone, ai-autonomy, paper]
domain: ai-autonomy
sources:
  - inbox/fetch-2026-08-07-crossref-deep-learning-based-collision-avoidance-techniques-in-multi-.md
  - raw/papers/_unclassified/a-conservative-analytical-framework-for-uav-collision-risk-assessment-under-posi.md
confidence: medium
contested: false
contradictions: []
---

# 다중 UAV 딥러닝 충돌회피 서베이

Computer Science Review 저널에 게재된 다중 UAV 네트워크의 딥러닝 기반 충돌 회피 기법 서베이 논문. 초록이 제공되지 않아 원문 확인이 필요하지만, 저널명·주제 특정성으로 볼 때 다중 드론 충돌 회피 분야의 최신 딥러닝 접근법을 체계적으로 정리한 리뷰로 판단된다.^[inbox/fetch-2026-08-07-crossref-deep-learning-based-collision-avoidance-techniques-in-multi-.md]

## 서지 정보

- **제목**: Deep learning-based collision avoidance techniques in multi-UAV networks: A survey
- **저자**: Aoyon Rifat Sarker, Moh Sangman
- **저널**: Computer Science Review
- **원문**: https://doi.org/10.1016/j.cosrev.2026.101045

> 초록 미제공 — 원문 확인 후 구체적 기법 분류를 추가 보강할 필요가 있음(confidence: medium 유지 이유).

## 2026-09-30 추가 근거 (서지정보만 확보)

Wang·Luo·Jiang·Wang·Liu(2027, *Reliability Engineering & System Safety*)가 발표한
"A conservative analytical framework for UAV collision risk assessment under
position uncertainty using noncentral chi-square distributions"가 같은 날
Zotero로 인제스트됐다.^[raw/papers/_unclassified/a-conservative-analytical-framework-for-uav-collision-risk-assessment-under-posi.md]
제목 자체가 밝히는 정보로는, 위치 불확실성 하에서 비중심 카이제곱 분포를 이용해
UAV 충돌 위험을 보수적(conservative)으로 해석적 평가하는 프레임워크다 — 이
서베이 페이지가 다루는 "딥러닝 기반 충돌 회피"와는 별개로 확률적·해석적 위험
평가 축의 보완 문헌으로 분류한다. 초록은 아직 확보되지 않아 정량적 결과는
기록하지 않는다.

## 관련 개념

- [[lightweight-safe-rl-uav]] — 경량 안전 강화학습 충돌회피
- [[swarm-coordination]] — 다중 드론 협업/충돌회피 상위 개념
