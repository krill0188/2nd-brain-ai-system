---
title: "Review of PPP-RTK: achievements, challenges, and opportunities"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]
confidence: medium
contested: false
contradictions: []
---

# Review of PPP-RTK: achievements, challenges, and opportunities

- 원문: https://doi.org/10.1186/s43020-022-00089-9^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]
- 저자: Xingxing Li, Jiaxin Huang, Xin Li, Zhiheng Shen, Junjie Han, Linyang Li, et al.^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]
- 발행: 2022-12-06 (Satellite Navigation 3, art. 28)^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]

## 핵심 내용
PPP-RTK 리뷰. UPD 추정, 대기 보정 모델링, 빠른 모호정수 결정 등 핵심 기술과 다중 GNSS·다중 주파수, 저가 단일주파수 수신기, 차량 항법 응용을 정리한다. 일본 CLAS와 상용 서비스도 다루며, 도심 신호 차단, 극한 기상 대기 효과, 전리층 교란을 과제로 꼽는다.^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 표준 PPP 수렴 15~30분^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]
- 단일주파수 수렴: 고급 수신기 약 2.5분, 저가 수신기 약 5분^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]
- 유럽 다중 GNSS 시험: 사용자-기준국 평균 거리 약 371 km에서 수평 1 cm 미만, 수직 3 cm 미만^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]
- 삼중주파수 시뮬레이션: NL 모호정수 성공률 65초 내 99% (이중주파수는 150초 내 64%)^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]
- 상용: Trimble CenterPoint-RTX Fast 1분 미만 수렴, u-blox PointPerfect 30초 내 수평 3~6 cm 보고^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]
- 터널·도심 협곡에서는 미터급 이하로 열화^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]

## 한계·미확인
본문 앞 100,000자만 확인. 드론 전용 실험은 아님. 상용 서비스 수치는 본 논문이 인용한 값이며 독립 검증 미확인.^[inbox/processed/hw-20261021-precise-ppp-rtk-review-li-2022.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
