---
title: "PPS - Pulse Per Second (Linux kernel documentation)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, time-sync, pps, gnss]
sources: [inbox/processed/hw-20261021-data-sync-linux-pps-kernel.md]
confidence: medium
contested: false
contradictions: []
---

# PPS - Pulse Per Second (Linux kernel documentation)

- 원문: https://docs.kernel.org/driver-api/pps.html^[inbox/processed/hw-20261021-data-sync-linux-pps-kernel.md]
- 저자: Linux kernel community^[inbox/processed/hw-20261021-data-sync-linux-pps-kernel.md]
- 발행: 미확인^[inbox/processed/hw-20261021-data-sync-linux-pps-kernel.md]

## 핵심 내용
PPS는 초당 1회 고정밀 신호를 커널이 타임스탬프해 사용자 공간이 시스템 시계를 보정하게 하는 API이다. 소스는 직렬 포트(DCD 핀), 병렬 포트(ACK 핀), CPU GPIO 등이며 /dev/pps0 같은 문자 장치와 /sys/class/pps/ (assert, clear 파일)로 노출된다. 주 용도는 GPS 수신기와 NTP로 UTC에 서브밀리초 동기화이다. 도구는 pps-tools의 ppstest, 테스트용 소프트웨어 소스는 pps-ktimer 모듈이다.^[inbox/processed/hw-20261021-data-sync-linux-pps-kernel.md]
원문 인용: "sub-millisecond synchronisation to UTC"^[inbox/processed/hw-20261021-data-sync-linux-pps-kernel.md]

## 설계·운용에 쓸 수 있는 지침
- USB-직렬 어댑터는 지연·지터를 더해 클록 불안정 약 +-1ms가 보고됨; USB 2.0은 지터가 약 125 마이크로초로 줄 수 있음.^[inbox/processed/hw-20261021-data-sync-linux-pps-kernel.md]
- Intel Timed I/O 생성기 정밀도 약 20 나노초.^[inbox/processed/hw-20261021-data-sync-linux-pps-kernel.md]
- 센서 동기용 GNSS PPS는 직렬 어댑터 경유보다 GPIO 직결이 유리하다는 점은 위 지터 수치에서 추정되나 문서가 직접 권고하지는 않음(미확인).^[inbox/processed/hw-20261021-data-sync-linux-pps-kernel.md]

## 한계·미확인
- gpsd/chrony 연동은 페이지에 없음. 드론 특정 구성 미확인.^[inbox/processed/hw-20261021-data-sync-linux-pps-kernel.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
