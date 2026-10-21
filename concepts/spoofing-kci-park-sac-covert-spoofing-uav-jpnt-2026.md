---
title: "SAC-Based Covert Spoofing Technique for GNSS/INS Integrated UAV Using Dual NIS Reward"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: security
tags: [drone, gnss, kci]
sources: [inbox/processed/hw-20261021-spoofing-kci-park-sac-covert-spoofing-uav-jpnt-2026.md]
confidence: medium
contested: false
contradictions: []
---

# SAC-Based Covert Spoofing Technique for GNSS/INS Integrated UAV Using Dual NIS Reward

- 원문: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003381244^[inbox/processed/hw-20261021-spoofing-kci-park-sac-covert-spoofing-uav-jpnt-2026.md]
- 저자: Jong-Il Park, Kyoung-taek Kim, Chansik Park^[inbox/processed/hw-20261021-spoofing-kci-park-sac-covert-spoofing-uav-jpnt-2026.md]
- 발행: 2026 (Journal of Positioning, Navigation, and Timing, vol. 15, no. 3, p. 369; DOI 10.11003/JPNT.2026.15.3.369)^[inbox/processed/hw-20261021-spoofing-kci-park-sac-covert-spoofing-uav-jpnt-2026.md]

## 핵심 내용
KCI 포털 수록 논문(초록 직접 확인). GNSS/INS 복합항법 UAV 를 유도·납치하는 은닉 스푸핑을, 대상 UAV 내부 정보 없이 강화학습(Soft Actor-Critic)으로 수행하는 방법을 제안한다. 학습 때는 UAV 가 계산한 NIS 와 레이더가 예측한 NIS 를 함께 쓰는 이중 은닉 보상을 쓰고, 추론 때는 레이더 예측 NIS 만 사용한다. 방어 관점에서는 스푸핑 공격의 현실적 위협 모델 자료.^[inbox/processed/hw-20261021-spoofing-kci-park-sac-covert-spoofing-uav-jpnt-2026.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 시뮬레이션 1,000회 추론에서 유도 성공률 97.3% (초록)^[inbox/processed/hw-20261021-spoofing-kci-park-sac-covert-spoofing-uav-jpnt-2026.md]
- GNSS/INS 복합 UAV 도 혁신(NIS) 검사만으로는 은닉 스푸핑을 막지 못할 수 있음을 시사(저자 서술, 시뮬레이션 한정)^[inbox/processed/hw-20261021-spoofing-kci-park-sac-covert-spoofing-uav-jpnt-2026.md]

## 한계·미확인
시뮬레이션 결과만. 실비행·방어 대책 수치 미확인. 공격 기법 상세는 본문 미열람이며 이 파일에 절차를 옮기지 않음.^[inbox/processed/hw-20261021-spoofing-kci-park-sac-covert-spoofing-uav-jpnt-2026.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[kci-dual-nis-sac-gnss-ins-spoofing]]
