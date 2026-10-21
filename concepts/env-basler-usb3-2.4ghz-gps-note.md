---
title: "Possible Interference of the USB 3.0 Radio Frequency on 2.4 GHz Wireless Devices (Basler knowledge base)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-env-basler-usb3-2.4ghz-gps-note.md]
confidence: medium
contested: false
contradictions: []
---

# Possible Interference of the USB 3.0 Radio Frequency on 2.4 GHz Wireless Devices (Basler knowledge base)

- 원문: https://docs.baslerweb.com/knowledge/possible-interference-of-the-usb-30-radio-frequency-on-24-ghz-wireless-devices^[inbox/processed/hw-20261021-env-basler-usb3-2.4ghz-gps-note.md]
- 저자: Basler 지식베이스^[inbox/processed/hw-20261021-env-basler-usb3-2.4ghz-gps-note.md]
- 발행: 미확인^[inbox/processed/hw-20261021-env-basler-usb3-2.4ghz-gps-note.md]

## 핵심 내용
USB 3.0 카메라가 2.4 GHz 무선기기를 교란할 수 있고 예로 GPS 신호가 끊기거나 사라질 수 있다고 설명한다. 대책은 카메라와 무선 안테나 거리 확대, USB 3.0 카메라/커넥터 차폐, 고이득 안테나 사용. 기술 상세는 Intel 문서를 참조하라고 안내.^[inbox/processed/hw-20261021-env-basler-usb3-2.4ghz-gps-note.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 이격 거리 최대화, 차폐, 안테나 이득 확대 (정성적)^[inbox/processed/hw-20261021-env-basler-usb3-2.4ghz-gps-note.md]
- 페이지 표현: "a GPS signal may be interrupted or disappear completely"^[inbox/processed/hw-20261021-env-basler-usb3-2.4ghz-gps-note.md]

## 한계·미확인
수치(거리·차폐 사양·이득) 없음. Intel 원문(USB 3.0 RF interference white paper)은 직접 열어 확인하지 못함.^[inbox/processed/hw-20261021-env-basler-usb3-2.4ghz-gps-note.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
