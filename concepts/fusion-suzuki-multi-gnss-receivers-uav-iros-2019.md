---
title: "Robust UAV Position and Attitude Estimation using Multiple GNSS Receivers for Laser-based 3D Mapping"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: navigation-gnss-denied
tags: [drone, gnss, uav, multipath, rtk, fix-rate, antenna]
sources: [inbox/processed/hw-20261021-fusion-suzuki-multi-gnss-receivers-uav-iros-2019.md]
confidence: medium
contested: false
contradictions: []
---

# Robust UAV Position and Attitude Estimation using Multiple GNSS Receivers for Laser-based 3D Mapping

- 원문: https://arxiv.org/abs/2312.02485 (IEEE DOI 10.1109/IROS40897.2019.8967894)^[inbox/processed/hw-20261021-fusion-suzuki-multi-gnss-receivers-uav-iros-2019.md]
- 저자: Taro Suzuki 외 2명 (arXiv 표기: Taro Suzuki and 2 other authors)^[inbox/processed/hw-20261021-fusion-suzuki-multi-gnss-receivers-uav-iros-2019.md]
- 발행: IROS 2019 (arXiv 2023-12-05 등록)^[inbox/processed/hw-20261021-fusion-suzuki-multi-gnss-receivers-uav-iros-2019.md]

## 핵심 내용
소형 UAV에 저가·경량 GNSS 안테나/수신기 6개를 탑재해 단일주파수 RTK-GNSS 의 fix 비율을 높이고 멀티패스를 감지하는 기법을 제안한다. 두 접근: 여러 안테나의 fix 해를 결합하는 hybrid GNSS fix 와 GNSS 신호 강도의 일관성 검사. 정적 시험에서 다중경로 환경에서 위치·자세 정확도가 향상되었고, 비행 시험에서 5 cm 정확도의 3D 지도를 생성했다고 초록에 서술.^[inbox/processed/hw-20261021-fusion-suzuki-multi-gnss-receivers-uav-iros-2019.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 안테나마다 멀티패스 오차가 달라 여러 안테나/수신기를 쓰면 fix 확률이 올라간다는 설계 근거.^[inbox/processed/hw-20261021-fusion-suzuki-multi-gnss-receivers-uav-iros-2019.md]
- 신호 세기(C/N0) 일관성으로 멀티패스 신호를 가려내 fix 비율과 정확도를 추가로 개선.^[inbox/processed/hw-20261021-fusion-suzuki-multi-gnss-receivers-uav-iros-2019.md]
- 단일주파수 수신기 RTK 에서도 중복 수신기로 fix rate 를 높일 수 있음(초록 문구).^[inbox/processed/hw-20261021-fusion-suzuki-multi-gnss-receivers-uav-iros-2019.md]

## 한계·미확인
초록 수준 열람: fix rate 수치(%), 안테나 배치 도면, 기선 길이는 본문에서 확인하지 못해 미확인. 6개 안테나는 중량·비용 부담이 있음(저자 시스템 한정).^[inbox/processed/hw-20261021-fusion-suzuki-multi-gnss-receivers-uav-iros-2019.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]

## 📰 최근 관련 소식
- [MATLAB] Mapping Between MATLAB and Python | MATLAB and Python for Students (youtube.com, 2026-10-22) — https://www.youtube.com/watch?v=-xy6_XCzcKU
