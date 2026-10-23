---
title: "Logging (PX4 User Guide)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
ontology_class: PX4
tags: [drone, flight-log, px4, logger]
sources: [inbox/processed/hw-20261021-data-flightlog-px4-logging.md]
confidence: medium
contested: false
contradictions: []
---

# Logging (PX4 User Guide)

- 원문: https://docs.px4.io/main/en/dev_log/logging.html^[inbox/processed/hw-20261021-data-flightlog-px4-logging.md]
- 저자: PX4 project^[inbox/processed/hw-20261021-data-flightlog-px4-logging.md]
- 발행: 미확인^[inbox/processed/hw-20261021-data-flightlog-px4-logging.md]

## 핵심 내용
PX4 logger 모듈은 어떤 uORB 토픽이든 전체 필드로 ULog 형식에 기록한다(필드는 .msg 파일에서 생성). 기본은 arm 시 시작, disarm 시 종료하며 arm 세션마다 새 파일을 만든다(SDLOG_MODE로 조정). 토픽별 최소 간격(ms)을 줄 수 있고 없거나 0이면 최대 속도로 기록한다. etc/logging/logger_topics.txt로 기록 토픽을 추가하고 SDLOG_PROFILE로 EKF2 리플레이, 고속 PID/필터 튜닝, 열 보정 같은 프로파일을 켠다. SD카드 대신 MAVLink 로그 스트리밍도 가능하다.^[inbox/processed/hw-20261021-data-flightlog-px4-logging.md]

## 설계·운용에 쓸 수 있는 지침
- 기본 로깅 대역폭 약 50 KB/s, NuttX 파일 크기 한계 약 4 GB, SDLOG_MAX_SIZE 기본 1024 MB, SDLOG_ROTATE 기본 디스크 90%.^[inbox/processed/hw-20261021-data-flightlog-px4-logging.md]
- NuttX 최대 지원 SD 32 GB. 느린 쓰기 스파이크는 드롭아웃 유발, sd_bench -r 100으로 카드 점검.^[inbox/processed/hw-20261021-data-flightlog-px4-logging.md]
- MAVLink 스트리밍은 약 50 KB/s 링크(WiFi 등), 동시에 클라이언트 1개, MAVLink 2 필요, 설정 MAVLink 속도의 최대 70% 사용.^[inbox/processed/hw-20261021-data-flightlog-px4-logging.md]

## 한계·미확인
- 모든 토픽의 개별 로그율 표는 미확인. 게시일 미확인.^[inbox/processed/hw-20261021-data-flightlog-px4-logging.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[px4-offboard-control]]
