---
title: "Hardware timestamping for drone sensors: NTNU Time Synchronization Overview and Open-Source LiDAR Time Synchronization (GNSS-clock mimic)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, time-synchronization, pps, ptp, imu-camera, kalibr, lidar]
sources: [inbox/processed/hw-20261021-data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock.md]
confidence: medium
contested: false
contradictions: []
---

# Hardware timestamping for drone sensors: NTNU Time Synchronization Overview and Open-Source LiDAR Time Synchronization (GNSS-clock mimic)

- 원문: https://www.ntnu.no/wiki/x/gIFfG ; https://arxiv.org/abs/2107.02625^[inbox/processed/hw-20261021-data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock.md]
- 저자: NTNU Wikihotell (benjabj, 2025-02-19); Marsel Faizullin, Anastasiia Kornilova, Gonzalo Ferrer (arXiv 2021-07-06, ISPCS 2022)^[inbox/processed/hw-20261021-data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock.md]
- 발행: 2025-02-19 ; 2021-07-06^[inbox/processed/hw-20261021-data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock.md]

## 핵심 내용
NTNU 위키(드론 도킹 프로젝트 내부 문서, 비동료심사): SentiBoard v1.3 트리거가 GNSS 수신기 외부 PPS에 잠겨 Synchronized 모드로 동작, PPS마다 Trigger 패킷을 USB로 Jetson Orin NX에 전송, Jetson은 GPIO로 1 PPS를 받아 내부 클럭 드리프트를 억제. PPS를 직렬로 보내는 방식은 "USB jitter could introduce ±0.125ms"라서 배제. Jetson-LattePanda 간 PTP 동기 실측 "+-0.1ms"(유휴, 다른 트래픽 없음). ZED X 카메라는 하드웨어 트리거/캡처 타임스탬프가 없어 RAM 도착 시각으로 스탬프되며 "often delayed by a few frames". 개선안으로 Kalibr 카메라-IMU 보정 제안(미구현 표기).^[inbox/processed/hw-20261021-data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock.md]
arXiv 2107.02625: 마이크로컨트롤러가 GNSS 클럭 신호를 모사해 LiDAR의 하드웨어 동기 인터페이스에 입력, 실제 GNSS 수신기 불필요. LiDAR와 IMU로 시연해 "state 1 microsecond performance"(초록 표기)를 보고하며 ROS 소프트웨어 타임스탬프와 LiDAR 내부 클럭 방식보다 낫다고 주장. 카메라, IMU 등으로 확장 가능.^[inbox/processed/hw-20261021-data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- 하드웨어 PPS 트리거+PTP 조합: 직렬 PPS는 ±0.125 ms 지터, PTP 실측 ±0.1 ms(조건 한정).^[inbox/processed/hw-20261021-data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock.md]
- 소프트웨어 도착 시각 타임스탬프는 수 프레임 지연 가능.^[inbox/processed/hw-20261021-data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock.md]
- 하드웨어 동기화로 약 1 마이크로초 수준 보고(LiDAR+IMU).^[inbox/processed/hw-20261021-data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock.md]

## 한계·미확인
- NTNU 문서는 프로젝트 위키라 신뢰도 낮음. arXiv는 초록만 확인. 카메라 하드웨어 타임스탬프 정량 비교(Kalibr 대비) 자료는 미확보.^[inbox/processed/hw-20261021-data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
