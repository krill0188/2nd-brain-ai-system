---
title: "BLDC 모터-프로펠러 디지털 트윈: 정지 추력 예측 (Gauthier 외, 2023)"
created: 2026-10-20
updated: 2026-10-20
type: concept
domain: hardware
tags: [drone, drone-hw]
sources: [inbox/processed/fetch-2026-10-20-arxiv-digital-twin-of-a-dc-brushless-electric-motor-propeller-syst.md]
confidence: medium
contested: false
contradictions: []
---

# BLDC 모터-프로펠러 디지털 트윈 (정지 추력)

**출처**: arXiv 2312.09981 (2023-12-15), 초록 기준.

정지(무이동) 조건에서 추력을 예측하는 BLDC 모터·프로펠러 디지털 트윈이다. 역기전력, 프로펠러 항력, 권선 인덕턴스와 DC 저항에 따른 유한 응답 시간을 반영한다. 교과서형 BLDC 모델과 비교하고 KDE Direct KDE2315XF-885(885 Kv) + 945 프로펠러, Holybro ESC로 구동한 AIR 2216(880 Kv) + 1045 프로펠러 실측과 대조했다. 두 시스템 모두 Group 1 쿼드콥터에서 흔한 구성이다. 정상상태와 과도 응답 모두 문헌의 선형화 모델과 **상당히 어긋났다**. 저자는 모터 동역학과 복잡한 기류에서의 프로펠러 동역학 변화를 분리하는 출발점이라고 설명한다.^[inbox/processed/fetch-2026-10-20-arxiv-digital-twin-of-a-dc-brushless-electric-motor-propeller-syst.md]

관련: [[bldc-motor-esc-characterization-research]], [[multirotor-propeller-test-research]], [[crazyflie-brushless-dynamics-model]].
