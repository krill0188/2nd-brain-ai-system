---
title: "Impact of Additional Antenna Groundplanes on RTK-GNSS Positioning Accuracy of UAVs (본문 수치 보강)"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: hardware
tags: [drone, gnss, ground-plane, rtk, 정량, 보강]
sources: [inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]
confidence: medium
contested: false
contradictions: []
---

# Impact of Additional Antenna Groundplanes on RTK-GNSS Positioning Accuracy of UAVs (본문 수치 보강)

- 원문: https://ars.copernicus.org/articles/20/23/2023/ars-20-23-2023.pdf^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]
- 저자: Stefan Punzet, Thomas F. Eibert^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]
- 발행: 2023-03-21 (Advances in Radio Science, vol. 20, pp. 23-28; DOI 10.5194/ars-20-23-2023)^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]

## 핵심 내용
20261021 파일(초록만 열람)의 보강판. 이번에는 공개 PDF 본문 전체(6쪽)를 읽었다. 실험: u-blox ZED-F9P 2대(로버·RTK 기준국), 안테나 3종(u-blox ANN-MB 세라믹 패치, TOPGNSS AN506G 패치, Beitian BT-560 헬리컬)에 접지판 5종(없음, 지름10cm 원형 PCB, 10x10cm 정사각 PCB, 지름15cm 알루미늄, 30x30cm 알루미늄)을 바꿔 장착하고, 야외 고정 위치(지상 1.5 m)에서 600 s(5 Hz, 3000샘플) 기록해 평균 주변의 수평 표준편차 σ2D, 수직 표준편차 σAlt를 비교.^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만, 단위 cm)

로버 접지판별 σ2D / σAlt (기준국 접지판이 지름15cm 알루미늄일 때):^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]

| 로버 접지판 | TOPGNSS AN506G | Beitian BT-560 |
|---|---|---|
| 없음(내장만) | 0.29 / 0.18 | 0.26 / 0.71 |
| 지름10cm PCB | 0.20 / 0.41 | 0.26 / 2.34 |
| 10x10cm PCB | 0.21 / 0.82 | 0.11 / 0.41 |
| 지름15cm 알루미늄 | 0.20 / 0.00 | 0.25 / 0.48 |
| 30x30cm 알루미늄 | 0.09 / 0.00 | 0.65 / 0.00 |

같은 로버 조건에서 기준국 접지판이 30x30cm 알루미늄일 때는 값이 크게 나빠짐: TOPGNSS 접지판 없음 3.31 / 3.85, Beitian 접지판 없음 1.37 / 4.14.^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]

- 기준국 안테나(ANN-MB)는 지름 12 cm 미만 접지판에서는 GNSS 수신 자체가 안 됨(저자 기술, u-blox 데이터시트도 접지판 필요).^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]
- 기준국 접지판을 30x30cm 정사각에서 지름15cm 원형 알루미늄으로 바꾸면 σAlt 최대 21배, σ2D 최대 11배 개선. 로버에 보조 접지판을 달면 σAlt 최대 9배, σ2D 최대 22배 개선(저자 서술).^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]
- 최상 조합: ANN-MB(기준국, 30x30cm 알루미늄) + TOPGNSS(로버, 30x30cm 알루미늄)에서 σ2D 0.09 cm, σAlt 0.00 cm. 그러나 30x30cm 알루미늄은 1.455 kg이라 UAV에 비현실적(저자 명시). 지름15cm 알루미늄은 231.8 g, 10 cm PCB는 약 21~24 g.^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]
- 결론 문구: 최적 접지판 크기·형상은 안테나마다 다르므로 안테나별로 실험해야 한다.^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]

## 한계·미확인
(1) 비행 중이 아니라 지상 1.5 m 고정 위치의 정지 시험임. 그래서 '로터 근처 간섭'이나 진동·자세 변화는 측정되지 않음. (2) 각 조합당 600 s 1회라 반복·통계 검정 없음. (3) 표는 σ(편차)이지 절대 위치 오차가 아님. (4) 안테나 3종 한정. 열람 범위: 본문 전체(Copernicus 공개 PDF). 신뢰도: 중상(동료심사 학회 특집 논문).^[inbox/processed/hw-20261022-env-punzet-groundplane-rtk-uav-ars-2023-fulltext.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
