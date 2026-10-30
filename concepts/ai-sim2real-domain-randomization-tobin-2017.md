---
title: "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: simulation-test
tags: [drone, ai, sim-to-real, domain-randomization, perception]
sources: [inbox/processed/hw-20261021-ai-sim2real-domain-randomization-tobin-2017.md]
confidence: medium
contested: false
contradictions: []
---

# Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World

- 원문: https://arxiv.org/abs/1703.06907^[inbox/processed/hw-20261021-ai-sim2real-domain-randomization-tobin-2017.md]
- 저자: Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, Pieter Abbeel^[inbox/processed/hw-20261021-ai-sim2real-domain-randomization-tobin-2017.md]
- 발행: 2017-03-20 (IROS 2017 제출)^[inbox/processed/hw-20261021-ai-sim2real-domain-randomization-tobin-2017.md]

## 핵심 내용
비현실적 임의 텍스처로 렌더링을 무작위화한 시뮬레이션 이미지만으로 학습한 물체 위치 추정기가 실제 환경에서 동작함을 보인다. 실제 이미지 사전학습 없이 시뮬레이션 RGB로만 학습한 심층망을 로봇 제어에 처음 전이했다고 주장. 검출기를 복잡한 환경의 파지에 사용.^[inbox/processed/hw-20261021-ai-sim2real-domain-randomization-tobin-2017.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 실세계 검출기 정확도 1.5 cm ('accurate to 1.5cm and robust to distractors and partial occlusions').^[inbox/processed/hw-20261021-ai-sim2real-domain-randomization-tobin-2017.md]
- 과제는 로봇 조작(물체 위치 추정)이며 드론 아님.^[inbox/processed/hw-20261021-ai-sim2real-domain-randomization-tobin-2017.md]

## 한계·미확인
드론/항공 적용은 초록에 없음(미확인).^[inbox/processed/hw-20261021-ai-sim2real-domain-randomization-tobin-2017.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[drone-simulation]]

## 📰 최근 관련 소식
- From Drone Pilot to Cockpit: The Procedural Skills That Transfer (and the Ones That Don’t) (www.suasnews.com, Sun, 25 Oc) — https://www.suasnews.com/2026/10/from-drone-pilot-to-cockpit-the-procedural-skills-that-transfer-and-the-ones-that-dont/
- Skydio Drone Crashes And Burns Feet From FIFA World Cup Crowds In Brooklyn, And The NYPD Has Been Here Before - DroneXL (news.google.com, Wed, 01 Ju) — https://news.google.com/rss/articles/CBMikAFBVV95cUxPTG9TZUtIb3hfZGI1U1BIM0xjb3YzZEpyREh5YTE3NlhmVjJlTVUtOEFfTzVZRDRzamJmQndxSmkya3l2ZGZoTE9aQ1d2elRUOURPemxscGZqTkx2YnMxdzB4SGt6WUlSbXBEWk54cmtsYThYd19qVlg3ekJzQUJldlFubkZrVUo0dDJkOEE3dzM?oc=5
- Remānguys from Tallinn reaches the final of Anduril’s AI Grand Prix, a world race of drones that fly themselves (www.suasnews.com, Mon, 26 Oc) — https://www.suasnews.com/2026/10/remanguys-from-tallinn-reaches-the-final-of-andurils-ai-grand-prix-a-world-race-of-drones-that-fly-themselves/
