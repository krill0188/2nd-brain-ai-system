---
title: "검색 결과에서 \"micro drone\"으로 명시된 SLAM 사례는 카메라+IMU(VIO) 조합을 사용한 반면, LiDAR-관성 오도메트리 사례는 더 큰 임베디드 UAV 플랫폼(Livox Mid-360/Pixhawk 4 Mini)이나 다중 센서 정찰 드론 프로젝트에서 등장해, 마이크로 스케일에서는 카메라+IMU 조합이 상대적으로 더 구체적인 근거를 갖는다."
created: 2026-08-01
updated: 2026-08-01
type: concept
tags: []
sources:
  - raw/papers/drone-hw/danial2025-microdrone-slam.md
confidence: medium
domain: ai-agent
contested: false
contradictions: []
---
# 검색 결과에서 "micro drone"으로 명시된 SLAM 사례는 카메라+IMU(VIO) 조합을 사용한 반면, LiDAR-관성 오도메트리 사례는 더 큰 임베디드 UAV 플랫폼(Livox Mid-360/Pixhawk 4 Mini)이나 다중 센서 정찰 드론 프로젝트에서 등장해, 마이크로 스케일에서는 카메라+IMU 조합이 상대적으로 더 구체적인 근거를 갖는다.

> 이 페이지는 인간 승인형 AI 연구 세션 `research/runs/20260801-research-1785543589`에서 마스터 승인을 거쳐 승격된 inference 클레임(`C3`)이다. 세션 원본 산출물은 `research/hypotheses/20260801-research-1785543589.md`, `research/reviews/20260801-research-1785543589.md`에 그대로 보존되어 있다.

## 주장

검색 결과에서 "micro drone"으로 명시된 SLAM 사례는 카메라+IMU(VIO) 조합을 사용한 반면, LiDAR-관성 오도메트리 사례는 더 큰 임베디드 UAV 플랫폼(Livox Mid-360/Pixhawk 4 Mini)이나 다중 센서 정찰 드론 프로젝트에서 등장해, 마이크로 스케일에서는 카메라+IMU 조합이 상대적으로 더 구체적인 근거를 갖는다.

## 근거

- [[flight-ready-lidar-inertial-odometry]]
- [[recon-swarm-project]]
- ^[raw/papers/drone-hw/danial2025-microdrone-slam.md]

## 검토 노트 (Critic)

- 반론/모순: 없음
- 한계: recon-swarm-project.md는 학술 문헌이 아니라 마스터 개인 프로젝트 로드맵이며, LiDAR+카메라+Radar+Optical Flow를 모두 탑재하는 계획으로 "마이크로드론"이 아닌 표준 UAV급 플랫폼을 전제로 한다. flight-ready-lidar-inertial-odometry의 Livox Mid-360(약 265g)도 진정한 마이크로드론(보통 250g 미만)에 탑재하기엔 무겁다는 점에서 이 추론은 성립하지만, "구체성의 차이"는 실제로는 검색 카테고리(마이크로드론 vs. 일반 UAV)의 차이에서 기인한 것일 수 있어 인과관계 해석에 유의해야 한다.

## 관련

[[flight-ready-lidar-inertial-odometry]] [[recon-swarm-project]]

## 📰 최근 관련 소식
- Palladyne AI Wins U.S. Army Contracts for Autonomous Drone Swarms and Gremlin-X Tactical UAV Program (uasweekly.com, Tue, 23 Ju) — https://news.google.com/rss/articles/CBMizgFBVV95cUxQMWFVakV3U3c3SVAzaTFpd2UtRFRIMzNBS0o1aW9VcU51bXVEY3M4LXhPMFE2NjI3VVJwdk1MS0RhZGdTc3RuZ0dIR21tZlBDa041WHRQbEhOUDRDQ2ZqZTRBREpmOGpON2FwSmU3UVlPQnlzWTF1T19uREUxVTZTcWlzT0pCZGJnX3FfQ1VtWlFyQWZ1dHJrSXJfNVpvV3dqTHIteGZRc1lfeXZuU25ZMkc4OVhiSU11YnhRMF9qZHgtVll6VXhrak01S2pPUQ?oc=5
- 英해군 정찰 드론 카메라…비밀리에 중국으로 데이터 송신 (아시아투데이, Mon, 10 Au) — https://news.google.com/rss/articles/CBMibkFVX3lxTE0tSjBpdjBNRlpndXV4WW9zclhRck93QjkyWlhtc1ZyM05NcF9CcFprQVFHTXRyNWZ2Y2ZKRXA4TG5IRFVfdUlmNld3WXliZ3pGSmJtTmItVW1VM2JFdkxTeXFoTDNocHhqTkN3Y2Fn?oc=5
- 보잉, 아처에 드론 3사 매각… AI 방산 플랫폼 출범 (글로벌이코노믹, Tue, 11 Au) — https://news.google.com/rss/articles/CBMiiAFBVV95cUxQLTFNbWVNZjUyZWNEVVJ0M2xhVFdmNmRjVnE2Z1NSanlCQjQzc1J4aTI4NDlSUUJNbFRBakNMYTZ2QS03c1AzbjdrdTNiU05FbVR2Wl9DNHpKa2ktaE1lNjg4ak92VXd6X01pWVI2aEpMMlkxSzh0ZmlVUmhpMTFpRm1vVnVuZkNo?oc=5
- K-방산 ‘초저가 자폭드론’ 어디까지 왔나 (아시아투데이, Thu, 13 Au) — https://news.google.com/rss/articles/CBMibkFVX3lxTE4tZHB6eWp4UFpOZFVYUVNUY0dOcXFWT2lqZzc4VEdaREg4YmY5aVlOajhvMjJiWGFDaEgtYjlQT2hLWGloQnpQc2I1cjJpVjBJVGp5ZWw1MWJxeXIzQnQwRXhlSXEzS0NyLUY5Z3pB?oc=5
- [UAV Coach] Drone Prices Are About to Jump (youtube.com, 2026-08-15) — https://www.youtube.com/watch?v=FEiY1ONxd70
- [UAV Coach] FCC “Military Grade” Drone Ban Explained (youtube.com, 2026-08-14) — https://www.youtube.com/watch?v=TMJI78x-lyo
- 아처, 보잉 계열사 3곳 통째로 인수…'방산 드론'까지 품는다 (디지털투데이, Tue, 11 Au) — https://news.google.com/rss/articles/CBMic0FVX3lxTE5BV1pRSzRKc0JNSDJJU0xiZlZtY1VhOWkyQmp2clFNMmJhYkJSWVlkbHh1Y2UwMGJsTWgybHFTLUpSVWN6STRyV09yWExtdkRhZWhmZ2lYOXhtNEpfeWZKdnI1RXphRkJmMGU4NFhYMDZ6NVE?oc=5
- [Joshua Bardwell] Ukraine Fight Drone Simulator // NOT JUST A GAME (youtube.com, 2026-08-13) — https://www.youtube.com/watch?v=_3blDd5NZRM
