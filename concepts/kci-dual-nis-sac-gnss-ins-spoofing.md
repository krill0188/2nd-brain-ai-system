---
title: "이중 NIS 보상 SAC 기반 GNSS/INS 무인기 은닉 기만 기법 (KCI)"
created: 2026-09-17
updated: 2026-09-30
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, datalink]
sources:
  - inbox/fetch-2026-09-17-kci-이중-nis-보상을-적용한-sac-기반-gnssins-복합항법-무인기-은닉-기만-기법.md
  - raw/papers/drone-ai/이중-nis-보상을-적용한-sac-기반-gnssins-복합항법-무인기-은닉-기만-기법.md
confidence: medium
contested: false
contradictions: []
---

# 이중 NIS 보상 SAC 기반 GNSS/INS 무인기 은닉 기만 기법 (KCI)

박종일(Duksan Navcours)이 《Journal of Positioning, Navigation, and Timing》
(2026, 오픈 액세스)에 발표한 논문으로, GNSS/INS 복합항법 시스템에 위조 신호를
주입해 표적 UAV를 원하는 지점으로 유도하는 은닉 기만(covert spoofing)
프레임워크를 제안한다.^[inbox/fetch-2026-09-17-kci-이중-nis-보상을-적용한-sac-기반-gnssins-복합항법-무인기-은닉-기만-기법.md]

## 문제의식과 접근

- 기존 기만 기법은 표적 UAV의 내부 항법 파라미터나 비행 궤적을 사전에
  알아야 했으나, 실제 시나리오에서는 이 내부 정보가 기만자에게 원천적으로
  접근 불가능하다는 한계가 있다.
- 이를 해결하기 위해 최대 엔트로피 강화학습 알고리즘인 SAC(Soft
  Actor-Critic)에 이중 은닉(dual-concealment) 보상을 적용한 프레임워크를
  제안, 훈련 중 내부 정보 없이도 은닉 기만이 가능하도록 설계했다. 2026-09-30 Zotero
재인제스트로 동일 논문의 durable 레코드가 raw/papers에 추가돼 출처가 이중 확보됐다.^[raw/papers/drone-ai/이중-nis-보상을-적용한-sac-기반-gnssins-복합항법-무인기-은닉-기만-기법.md]

## 관련 개념

- [[rigid-covert-gnss-spoofing-swarm]] — UAV 군집 GNSS 스푸핑의 상대기하 탐지 사각지대(RigidShift)
- [[gnss-denied-remote-autonomy]] — 상용 DJI 드론 기반 GNSS 차단 환경 원격 자율
