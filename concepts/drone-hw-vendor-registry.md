---
title: "드론 HW 제조사 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: vendor-registry
tags: [drone, drone-hw, company]
sources: [inbox/processed/hw-registry-20261017-vendors-INDEX.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 HW 제조사 레지스트리

드론에 융합되는 HW 15개 분야(프레임·배터리·비행제어기·프로펠러·ESC·모터·카메라·LiDAR·레이더·GNSS/IMU·데이터링크·컴퓨트·전원·투하·지상국)의 제조사 목록. 한국·유럽·미국·중국·일본 제조사와 방산/산업/취미 구분을 담았다.

| 분야 | 레지스트리 | 항목 수 |
|---|---|---|
| 프레임·완기체 | [[vendor-registry-frame]] | 20 |
| 배터리 | [[vendor-registry-battery]] | 16 |
| 비행제어기 | [[vendor-registry-fc]] | 16 |
| 프로펠러 | [[vendor-registry-propeller]] | 15 |
| ESC | [[vendor-registry-esc]] | 16 |
| 모터 | [[vendor-registry-motor]] | 15 |
| 카메라·짐벌 | [[vendor-registry-camera]] | 17 |
| LiDAR | [[vendor-registry-lidar]] | 17 |
| 레이더 | [[vendor-registry-radar]] | 19 |
| GNSS·IMU·센서 | [[vendor-registry-gnss-imu]] | 20 |
| 데이터링크·통신 라디오 | [[vendor-registry-datalink]] | 16 |
| 컴패니언·엣지 컴퓨터 | [[vendor-registry-compute]] | 17 |
| 전원·충전기·BMS | [[vendor-registry-power-charger]] | 18 |
| 투하·윈치·낙하산 | [[vendor-registry-payload-mech]] | 15 |
| 지상국 HW | [[vendor-registry-gcs-hw]] | 17 |
| **합계** | 15개 분야 | **254** |

## 쓰는 법
- 설계 질의에서 후보 부품/도구가 필요하면 분야별 문서에서 제조사·제품군을 찾고, 사양은 제품별 카탈로그나 공식 페이지 원문으로 확인한다.
- 정보 빈틈(예: 모터 최대추력 미확인)이 드러나면 이 레지스트리에서 수집 우선순위를 뽑아 제품별 사양 수집으로 이어간다.
- 연관 레지스트리: [[drone-software-ecosystem-registry]]

## 한계
- 공식 사이트가 봇을 차단하거나 응답하지 않은 곳은 '미확인/접근실패'로 남겼다(상세는 각 분야 문서의 표 참조).
- 국가/본사·라이선스·연동 포인트는 값마다 확인 수준이 달라, 확인되지 않은 칸은 비워 두거나 표시했다.
- 수집 시점(2026-10-17) 기준이며 제품 라인업·정책은 바뀔 수 있다.
