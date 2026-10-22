---
title: "카메라-IMU 하드웨어 동기 vs 소프트웨어 동기 직접 정량 비교 — 4차 재조사 (2026-10-24)"
created: 2026-10-24
updated: 2026-10-24
type: concept
domain: ros-middleware
tags: [drone, time-synchronization, camera-imu, hardware-sync, software-sync, vio, negative-result]
sources: [inbox/processed/hw-20261024-conv-camera-imu-sync-hw-vs-sw-search-round4-2026-10-24.md]
confidence: medium
contested: false
contradictions: []
---

# 카메라-IMU 하드웨어 동기 vs 소프트웨어 동기 직접 정량 비교 — 4차 재조사 (2026-10-24)

- 원문: https://arxiv.org/html/2512.20475 ; https://arxiv.org/html/2403.12504v1 ; https://arxiv.org/html/2609.18628 ; https://daischsensor.com/how-are-visual-inertial-odometry-errors-affected-by-microsecond-timing-errors/ ; OpenAlex API 검색^[inbox/processed/hw-20261024-conv-camera-imu-sync-hw-vs-sw-search-round4-2026-10-24.md]

## 핵심 내용
판정: **4차(이번)에도 "같은 알고리즘·같은 데이터로 HW 동기 대 SW 타임스탬프 동기를 ATE 로 비교한 정량 결과"는 찾지 못함 (직접 비교 논문: 미확인).** 이전(20261022~23)과 다른 수단: arXiv 전문 HTML 4건 직접 열람·grep, OpenAlex API 3개 질의(영문 표현 변형), WebSearch 3회(GitHub 이슈 표현 포함). 새로 확인된 간접 근거만 기록.^[inbox/processed/hw-20261024-conv-camera-imu-sync-hw-vs-sw-search-round4-2026-10-24.md]
| 근거 | 내용(원문 확인 범위) | 정량 비교 여부 |
|---|---|---|
| arXiv 2512.20475 (드론 레이싱 VIO, Jetson) §4.1 "Sensor Timings" | 카메라-IMU 사이 하드웨어 동기가 없다고 명시. 카메라는 GStreamer 로 하드웨어 취득 타임스탬프 사용, IMU 는 FC 와 Jetson 시계 사이 "significant time-drift" 가 관찰되어 Jetson 도착 시각 사용(소폭 고주파 지터 있음), 상수 오프셋은 Kalibr 로 추정 | 비교 실험 없음(SW 동기 실무 사례) |
| arXiv 2403.12504 (TON-VIO) 서론·관련연구 | "동기 외부 트리거가 있어도 카메라·IMU 샘플 시점이 엄밀히 정렬된다는 보장이 없다"(장치별 취득·전송 지연). HW 동기=동기 보드 트리거(VersaVIS 인용), SW=Kalibr 등 오프라인/온라인 추정. 시간 오프셋 주입 후 VINS-Fusion·OpenVINS 개선 표(Table III~V)는 있으나 HW 대 SW 비교 아님 | 아님(오프셋 보정 알고리즘 비교) |
| arXiv 2609.18628 (지하 VIO 스트레스 벤치) | 9개 센서 파라미터(IMU 편향·잡음, 내부·외부 파라미터) 교란. 시간 오프셋·동기 교란은 포함하지 않음(전문 grep 확인) | 아님 |
| DAISCH 블로그(IMU 제조사) | "SW 타임스탬프 정확도는 HW 보다 훨씬 낮고 ROS 같은 미들웨어가 큰 오차를 더할 수 있다" 서술, 해석적 분석. 실측 ATE 표는 없음 | 아님(벤더 주장) |
| 20261023 기존 파일 | VersaVIS(동기 vs 비동기 구성, 정성), Qin 2018(오프셋 주입 RMSE) | 부분 |
## 설계에 쓸 수 있는 지침
- "HW 동기가 SW 보다 ATE X% 낫다"는 문장은 출처 없이 쓰지 말 것. 쓸 수 있는 근거: (1) 오프셋이 수 ms 를 넘으면 보정 없는 VIO 악화(Qin 2018, 20261023), (2) HW 트리거만으로 완전 정렬 보장은 아님(TON-VIO), (3) SW 동기 실무는 HW 취득 타임스탬프 + Kalibr 상수 오프셋으로 가능(2512.20475).^[inbox/processed/hw-20261024-conv-camera-imu-sync-hw-vs-sw-search-round4-2026-10-24.md]
## 한계·미확인
- Kalibr/VINS/OpenVINS GitHub 이슈 본문은 열람하지 못함(WebSearch 가 이슈 페이지를 반환하지 않음). NAVI(ION) 임베디드 GNSS-VIO 스위트(HW 동기 30 µs 이내 주장)는 전문 미열람. Bright Data search_engine 호출은 300 초 무응답으로 중단됨.^[inbox/processed/hw-20261024-conv-camera-imu-sync-hw-vs-sw-search-round4-2026-10-24.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[mbse-uav-sysml]]
