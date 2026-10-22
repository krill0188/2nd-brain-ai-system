---
title: "Design and Installed Performance Analysis of a Miniaturized All-GNSS Bands Antenna Array for Robust Navigation on UAV Platforms (헥사로터 설치 높이 50~130 mm, 로터 없는 측정)"
created: 2026-10-24
updated: 2026-10-24
type: concept
domain: hardware
tags: [drone, hardware, gnss, antenna-placement, installation-height, cn0, multipath, env]
sources: [inbox/processed/hw-20261024-env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi.md]
confidence: medium
contested: false
contradictions: []
---

# Design and Installed Performance Analysis of a Miniaturized All-GNSS Bands Antenna Array for Robust Navigation on UAV Platforms (헥사로터 설치 높이 50~130 mm, 로터 없는 측정)

- 원문: https://doi.org/10.3390/s22249645 (PMC9780917, CC BY 4.0)^[inbox/processed/hw-20261024-env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi.md]
- 저자: Hehenberger, Elmarissi, Caizzone (Crossref 성 표기 기준, 이름 약어 미확인)^[inbox/processed/hw-20261024-env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi.md]
- 발행: 2022-12-09 (Sensors 22(24), 9645)^[inbox/processed/hw-20261024-env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi.md]

## 핵심 내용
열람: PMC XML 전문(NCBI efetch)에서 3.1~4절 확인. 신뢰도: 중상(동료심사 OA), 단 **모터·ESC 전자파 간섭 측정이 아님**.^[inbox/processed/hw-20261024-env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi.md]
- 시뮬레이션: 헥사로터 UAV 플랫폼 위 안테나 어레이 설치 높이(안테나 접지면~기체 상면) 50~130 mm 비교(기체를 완전도체로 모델링한 최악 가정). 원문: 높이가 낮으면 이득 패턴 리플과 후엽이 커지고(특히 L5/E5a), 높이가 늘면 상반구 패턴이 매끄러워짐.^[inbox/processed/hw-20261024-env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi.md]
- 측정: DLR Compact Test Range 에서 **로터를 장착하지 않은** UAV로 110 mm 설치 패턴 측정. 원문 결론: 110 mm 는 안테나를 기체 구조와 이미 충분히 분리(decouple)하며, 초크링 개선은 중·고고도각에서 크지 않음.^[inbox/processed/hw-20261024-env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi.md]
- 24 h 야외 GNSS 측정(안테나 단독 대 UAV 장착 110 mm, 초크링 없음): 하늘도에서 대부분 영역 C/N0 40 dB-Hz 초과, 저고도각은 UAV 장착 시 C/N0 낮음(패턴의 방위각 진동), UAV 장착 시 L5/E5a 에서 C/N0 진동이 더 작은 경향(저자는 멀티패스 영향 가능성 언급). 구체 dB 차이는 그림이라 미확인.^[inbox/processed/hw-20261024-env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi.md]
## 설계에 쓸 수 있는 지침
- 기체 구조에 의한 패턴 왜곡 관점의 근거: 안테나를 기체 상면에서 띄울수록 패턴이 안정(이 논문 범위 50~130 mm, 로터 정지). 모터/ESC/프로펠러 근접 C/N0 저하 정량 근거로 쓰지 말 것.^[inbox/processed/hw-20261024-env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi.md]
## 한계·미확인
- 로터·ESC 가동 상태의 C/N0 측정 없음(패턴 측정은 로터 미장착). 거리별(dB) 표 없음. 야외 측정의 UAV 전원/모터 상태는 본문에 명시 없음 → 미확인.^[inbox/processed/hw-20261024-env-uav-antenna-installation-height-hehenberger-2022-no-motor-emi.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
