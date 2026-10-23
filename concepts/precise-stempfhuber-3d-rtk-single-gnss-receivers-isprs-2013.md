---
title: "3D-RTK CAPABILITY OF SINGLE GNSS RECEIVERS"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
ontology_class: PrecisePositioning
tags: [drone, gnss, uav, rtk, single-frequency, baseline]
sources: [inbox/processed/hw-20261021-precise-stempfhuber-3d-rtk-single-gnss-receivers-isprs-2013.md]
confidence: medium
contested: false
contradictions: []
---

# 3D-RTK CAPABILITY OF SINGLE GNSS RECEIVERS

- 원문: https://doi.org/10.5194/isprsarchives-XL-1-W2-379-2013^[inbox/processed/hw-20261021-precise-stempfhuber-3d-rtk-single-gnss-receivers-isprs-2013.md]
- 저자: W. Stempfhuber (Beuth Hochschule für Technik Berlin; 인용 표기상 첫 저자, 공저자 미확인)^[inbox/processed/hw-20261021-precise-stempfhuber-3d-rtk-single-gnss-receivers-isprs-2013.md]
- 발행: 2013 (ISPRS Archives XL-1/W2, 379–384)^[inbox/processed/hw-20261021-precise-stempfhuber-3d-rtk-single-gnss-receivers-isprs-2013.md]

## 핵심 내용
저가 단일주파수(L1) GNSS 수신기와 RTKLib 기반 실시간 RTK 시스템을 UAV 용으로 구성한 학회 논문 소개문. 시스템은 u-blox LEA-4T/6T 수신기, Trimble Bullet III L1 안테나, WLAN 포함 데이터로거, 전원으로 구성되며 하드웨어 수백 유로, 배터리 포함 총 무게 500–800 g 이라고 서술한다. 안테나 최적화(초크링 어댑터 캘리브레이션)가 신호 수신 문제를 줄였다고 서술.^[inbox/processed/hw-20261021-precise-stempfhuber-3d-rtk-single-gnss-receivers-isprs-2013.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 항공체는 차폐가 적어 다중경로 영향이 상대적으로 작다는 서술(저자 주장).^[inbox/processed/hw-20261021-precise-stempfhuber-3d-rtk-single-gnss-receivers-isprs-2013.md]
- L1 반송파 기선 해석은 수 km 로 제한해야 하며, 기준국–로버 거리 5 km 초과 시 데시미터 영역의 오차가 생긴다고 서술(초록/서론 수준 수치).^[inbox/processed/hw-20261021-precise-stempfhuber-3d-rtk-single-gnss-receivers-isprs-2013.md]
- RTK 해를 NMEA 로 출력해 비행제어기와 연동 가능.^[inbox/processed/hw-20261021-precise-stempfhuber-3d-rtk-single-gnss-receivers-isprs-2013.md]
- 단일주파수 기준 설계 시 기준국 기선을 5 km 이내로 두라는 근거로 사용 가능(2013년 시스템 한정).^[inbox/processed/hw-20261021-precise-stempfhuber-3d-rtk-single-gnss-receivers-isprs-2013.md]

## 한계·미확인
초기화 시간·fix 비율의 기선 길이별 표는 열람한 소개문에 없음(본문 PDF 미열람). 2013년 L1 시스템이라 현재의 다주파 모듈(F9P 등)에 그대로 적용하면 안 됨.^[inbox/processed/hw-20261021-precise-stempfhuber-3d-rtk-single-gnss-receivers-isprs-2013.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
