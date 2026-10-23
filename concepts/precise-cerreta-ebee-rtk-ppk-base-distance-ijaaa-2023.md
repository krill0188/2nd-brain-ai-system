---
title: "Accuracy Assessment of the eBee Using RTK and PPK Corrections Methods as a Function of Distance to a GNSS Base Station"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: hardware
tags: [drone, gnss, rtk, ppk, baseline, 실측, uav]
sources: [inbox/processed/hw-20261022-precise-cerreta-ebee-rtk-ppk-base-distance-ijaaa-2023.md]
confidence: medium
contested: false
contradictions: []
---

# Accuracy Assessment of the eBee Using RTK and PPK Corrections Methods as a Function of Distance to a GNSS Base Station

- 원문: https://doi.org/10.58940/2374-6793.1819^[inbox/processed/hw-20261022-precise-cerreta-ebee-rtk-ppk-base-distance-ijaaa-2023.md]
- 저자: Joseph Cerreta, David Thirtyacre, Peter Miller, Scott S. Burgess, William J. Austin^[inbox/processed/hw-20261022-precise-cerreta-ebee-rtk-ppk-base-distance-ijaaa-2023.md]
- 발행: 2023 (International Journal of Aviation, Aeronautics, and Aerospace, vol. 10, iss. 3, art. 4)^[inbox/processed/hw-20261022-precise-cerreta-ebee-rtk-ppk-base-distance-ijaaa-2023.md]

## 핵심 내용
고정익 UAV(senseFly eBee X)를 미국 애리조나 남서부 3개 비행장소에서 33회 비행, RTK/PPK, 로컬 Emlid Reach RS2 기준국 vs CORS(P003) NTRIP, 기준국 거리 2.4~42.0 km 6단계를 비교했다. 평가는 사진측량 모델(Pix4Dmapper)의 검사점 8개 RMSE_XYZ. 방법(RTK/PPK)과 보정원(로컬/NTRIP) 간 차이는 통계적으로 유의하지 않았고, 기준국 거리 간 차이는 유의했다(F(5,33)=11.99, p=0.000).^[inbox/processed/hw-20261022-precise-cerreta-ebee-rtk-ppk-base-distance-ijaaa-2023.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)

| 기준국 거리(km) | 비행 수 N | RMSE_XYZ 평균(m) | SD(m) |
|---|---|---|---|
| 2.4 | 6 | 0.06 | 0.04 |
| 8.4 | 4 | 0.06 | 0.02 |
| 16.2 | 7 | 0.09 | 0.02 |
| 27.8 | 4 | 0.14 | 0.03 |
| 36.5 | 5 | 0.15 | 0.06 |
| 42.0 | 7 | 0.23 | 0.07 |

- RTK 평균 0.13 m(SD 0.07) vs PPK 0.12 m(SD 0.08), p=0.778. 로컬 RS2 0.11 m(SD 0.07) vs NTRIP 0.13 m(SD 0.09), p=0.351.^[inbox/processed/hw-20261022-precise-cerreta-ebee-rtk-ppk-base-distance-ijaaa-2023.md]
- 저자 결론: 기준국이 16.2 km 미만일 때 RMSE_XYZ가 0.09 m 이하. 최고 정확도를 원하면 16.2 km 미만 권고. (Pix4D 기대치 0.09 m 이하라고 표 주석에 기재)^[inbox/processed/hw-20261022-precise-cerreta-ebee-rtk-ppk-base-distance-ijaaa-2023.md]
- 기준국 위치는 OPUS로 결정, 검사점은 별도 RS2 로버로 측정(기준 RMSE는 논문 Table 1).^[inbox/processed/hw-20261022-precise-cerreta-ebee-rtk-ppk-base-distance-ijaaa-2023.md]

## 한계·미확인
열람 범위: 논문 전문 7쪽(Wayback 보관 PDF에서 텍스트 추출)을 읽음. 주의: (1) 값은 GNSS 위치 자체가 아니라 사진측량 모델의 검사점 오차라서 카메라·고도(GSD) 영향이 섞임. (2) 거리가 비행장소·날짜와 묶여 있어(Table 2) 거리와 장소·날씨 효과가 분리되지 않음. (3) 고정익 1기종이라 멀티콥터 일반화는 미확인. (4) 거리별 N이 4~7로 작음. 출처: 저널 공식 페이지(commons.erau.edu)는 Cloudflare 차단이라 web.archive.org 보관 PDF로 본문 확인. 신뢰도: 중상(동료심사 학술지, 수치 직접 확인).^[inbox/processed/hw-20261022-precise-cerreta-ebee-rtk-ppk-base-distance-ijaaa-2023.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]

## 📰 최근 관련 소식
- Signature Aviation and UrbanV Launch Signature UrbanV Alliance to Develop and Operate AAM Infrastructure Across the United States (www.suasnews.com, Wed, 21 Oc) — https://www.suasnews.com/2026/10/signature-aviation-and-urbanv-launch-signature-urbanv-alliance-to-develop-and-operate-aam-infrastructure-across-the-united-states/
