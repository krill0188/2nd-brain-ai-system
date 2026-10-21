---
title: "Jetson Linux Developer Guide: Software Packages and the Update Mechanism (OTA)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
tags: [drone, edge, jetson, ota, mlops]
sources: [inbox/processed/hw-20261021-data-edge-jetson-ota-update.md]
confidence: medium
contested: false
contradictions: []
---

# Jetson Linux Developer Guide: Software Packages and the Update Mechanism (OTA)

- 원문: https://docs.nvidia.com/jetson/archives/r36.4/DeveloperGuide/SD/SoftwarePackagesAndTheUpdateMechanism.html^[inbox/processed/hw-20261021-data-edge-jetson-ota-update.md]
- 저자: NVIDIA^[inbox/processed/hw-20261021-data-edge-jetson-ota-update.md]
- 발행: 미확인(r36.4 문서)^[inbox/processed/hw-20261021-data-edge-jetson-ota-update.md]

## 핵심 내용
Jetson의 OTA는 두 가지이다. (1) Debian 패키지 기반: NVIDIA APT 저장소로 apt upgrade(점 릴리스) 또는 저장소 릴리스를 바꿔 apt dist-upgrade(마이너 릴리스). 35.x에서 36.x 업그레이드는 미지원. (2) 이미지 기반: 미리 생성한 이미지를 파티션에 써 넣는 방식으로 파티션 레이아웃 변경도 처리하며 지원 소스 릴리스는 35.5.0 이상.^[inbox/processed/hw-20261021-data-edge-jetson-ota-update.md]
원문 인용: "a failsafe way to update the BSP on a Jetson device"^[inbox/processed/hw-20261021-data-edge-jetson-ota-update.md]

## 설계·운용에 쓸 수 있는 지침
- 이미지 기반 절차: 호스트에서 l4t_generate_ota_package.sh로 ota_payload_package.tar.gz 생성(전체, 부트로더만 -b, 루트FS만 -r) 후 자체 OTA 서버에 ota_tools와 함께 올림(NVIDIA는 페이로드 서명·암호화 권장). 기기 클라이언트가 내려받아 검증 후 nv_ota_start.sh 실행, 복구 커널로 재부팅해 적용.^[inbox/processed/hw-20261021-data-edge-jetson-ota-update.md]
- 업데이트 중 전원 손실 시 복구 커널로 재부팅해 재개 가능. 재시도 한도는 OTA_MAX_RETRY_COUNT(기본 0). 실패 로그는 /ota_logs/.^[inbox/processed/hw-20261021-data-edge-jetson-ota-update.md]
- 모델 파일 갱신(앱 계층) OTA 방식은 이 문서 범위 밖.^[inbox/processed/hw-20261021-data-edge-jetson-ota-update.md]

## 한계·미확인
- rootfs A/B 동작 원리는 이 페이지에서 설명 없음(--rootfs-b-uuid 옵션 언급만). 모델 단위 OTA 미확인.^[inbox/processed/hw-20261021-data-edge-jetson-ota-update.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]
