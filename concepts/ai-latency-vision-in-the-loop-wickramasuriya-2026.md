---
title: "Hardware- and Vision-in-the-Loop Validation of Deep Monocular Pose Estimation for Autonomous Maritime UAV Flight"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
tags: [drone, latency, delayed-kalman-filter, jetson-orin-nx, perception-in-the-loop]
sources: [inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]
confidence: medium
contested: false
contradictions: []
---

# Hardware- and Vision-in-the-Loop Validation of Deep Monocular Pose Estimation for Autonomous Maritime UAV Flight

- 원문: https://arxiv.org/abs/2606.19176^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]
- 저자: Maneesha Wickramasuriya, Beomyeol Yu, Jaden Shin, Mason Huslig, Taeyoung Lee, Murray Snyder^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]
- 발행: 2026-06-17 (arXiv v1)^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]

## 핵심 내용
선박 기반 UAV 운용을 실내에서 검증하기 위한 vision-in-the-loop 프레임워크. 사실적 해상도 영상을 렌더링하고, 트랜스포머 기반 단안 자세 추정기를 온보드에서 실행하며, 지연된 측정을 고주기 IMU와 지연 칼만필터(DKF)로 융합해 기하학적 제어에 입력한다. 초록은 이륙·궤적추종·착륙 실험에서 안정적 폐루프 비행을 보고. HTML 본문에서 확인한 수치:^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]
- 하드웨어 NVIDIA Jetson Orin NX, IMU VectorNav VN-100 200 Hz, DKF에 들어가는 자세 측정 5 Hz(Sec. III-C).^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]
- Table I (TNN-MO, 병렬 인스턴스 수: 갱신율 Hz / 평균 지연 s, 비행컨트롤러 없음 / 있음): 1개 5.5/4.7, 0.18/0.21; 2개 9.0/8.7, 0.22/0.23; 3개 9.8/9.0, 0.30/0.33; 4개 11.1/10.0, 0.36/0.40.^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]
- 통신 지연 0.08~0.1 s 인용, Fig. 2의 WiFi 지연 0.075 s. 강건성 시험은 인스턴스 2개 약 5 Hz, 총 지연 약 0.55 s.^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- 병렬 인스턴스를 늘리면 갱신율은 오르지만 평균 지연도 함께 증가(표 값).^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]
- 비행컨트롤러와 같은 Jetson에서 돌리면 지연이 늘어남(1개: 0.18 → 0.21 s).^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]
- 느리고 지연된 비전 측정은 지연 칼만필터로 고주기 IMU와 융합하는 구조가 실제 비행에서 사용됨.^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]

## 한계·미확인
- 제어기 주기 미기재(논문). 초록 외 본문은 arXiv HTML 추출 텍스트 기준. 수치 해석은 표 그대로.^[inbox/processed/hw-20261021-ai-latency-vision-in-the-loop-wickramasuriya-2026.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[px4-offboard-control]]

## 📰 최근 관련 소식
- Elistair Unveils Tethered Solution for the Parrot ANAFI UKR (dronelife.com, Wed, 21 Oc) — https://dronelife.com/2026/10/21/elistair-unveils-tethered-solution-for-the-parrot-anafi-ukr/
- Building the Autonomous Warfare Command – DRPM UxS (www.suasnews.com, Fri, 23 Oc) — https://www.suasnews.com/2026/10/building-the-autonomous-warfare-command-drpm-uxs/
- Chuyka 4.5.0. (www.suasnews.com, Fri, 23 Oc) — https://www.suasnews.com/2026/10/chuyka-4-5-0/
- Parrot’s Latest MiniDrone Fits In The Palm Of Your Hand, Plus Jumping Sumo - SingularityHub (news.google.com, Thu, 16 Ja) — https://news.google.com/rss/articles/CBMisAFBVV95cUxQNXY4Rmc3cThiZElyVGJuV09iYVpGV0FXWjFRemZNZ0JKajlRd2RoOW1ydFp2b0xwNHF3Zm9FV2NOdnowdHYwUDVvbzl2Qi1qZ1NZQ2x1bUEwS0czc3JQazVVRk9xSVZlelFlN05TZGtVWXJhTzc4ZU4xU1R4cTktTnZ5bWpmR2VNWnVjb3o5QUJVZTl2ZXlYSUhGZmJxazREbFhfdWowYnZVblN0elR0cg?oc=5
