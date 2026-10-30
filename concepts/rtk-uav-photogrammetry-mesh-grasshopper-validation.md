---
title: "RTK-UAV 사진측량 3D 메시의 Grasshopper 독립 검증과 건축 실무 연계"
created: 2026-10-27
updated: 2026-10-27
type: concept
domain: ops-mission
tags: [drone, ops-mission]
sources: [inbox/processed/fetch-2026-10-27-kci-rtk-uav-사진측량-기반-3d-메시의-grasshopper-검증-방법론과-건축-실무-연계-프로세스-연구-.md]
confidence: low
contested: false
contradictions: []
---

# RTK-UAV 사진측량 3D 메시의 Grasshopper 독립 검증과 건축 실무 연계

양현수(동아대학교)의 대한건축학회연합논문집(2026) 논문. 원문 비공개, 초록 기준이다.^[inbox/processed/fetch-2026-10-27-kci-rtk-uav-사진측량-기반-3d-메시의-grasshopper-검증-방법론과-건축-실무-연계-프로세스-연구-.md]

## 방법과 결과
- **대상**: 제주 덕천리 132,922㎡ 부지의 시나리오 B(비행고도 70m) SfM 3D 메시. 선행연구에서 정밀도·효율이 검증된 데이터다.
- **독립 검증**: VRS-GNSS(Trimble R12i) 검사점 27개 중 유효 19개 사용. 수목 밀집 구역 중심부 1개 지점은 측정 불가로 추가 제외됐다.
- **결과**: 수직 RMSE 0.0522 m(95% 신뢰구간 3.80~6.64 cm)로 건축 실무 허용오차 10 cm 이내. DJI Terra 내부 검증값 4.86 cm와 0.36 cm 차이라 이종 환경에서 수직 정밀도가 동등하다고 평가했다.
- **연계**: 검증된 데이터를 Rhino에서 사이트 현황 분석과 원지형 모델링에 직접 쓸 수 있음을 실증했다.

## 관련 문서
RTK 드론 측량 사례는 [[precise-kci-hwang-rtk-drone-river-survey-kosham-2024]], 국내 네트워크 RTK 접속은 [[korea-ngii-network-rtk-g-vrs-drone-access-recheck-2026-10-24]]를 참조한다.

## 📰 최근 관련 소식
- RTK-UAV 사진측량 기반 3D 메시의 Grasshopper 검증 방법론과 건축 실무 연계 프로세스 연구 - 건축 실무 설계 연계를 위한 Rhino-Grasshopper 독립 검증 프로세스 - (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003395783
