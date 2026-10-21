---
title: "Problems with interference from USB3 hub (Emlid community forum)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]
confidence: medium
contested: false
contradictions: []
---

# Problems with interference from USB3 hub (Emlid community forum)

- 원문: https://community.emlid.com/t/problems-with-interference-from-usb3-hub/6830^[inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]
- 저자: Emlid 커뮤니티 사용자 및 Emlid 직원 댓글^[inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]
- 발행: 2017-07-24^[inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]

## 핵심 내용
Emlid Reach GNSS 모듈을 RC카에 탑재했을 때 USB 3.0 허브 연결로 GNSS 수신이 붕괴한 사례(일화적 포럼 보고). 허브 연결 시 3~4개 위성만 낮은 SNR로 추적. USB 2.0 기기는 영향이 작고 Wi-Fi은 영향 없었다. 전체를 은박지로 감싸면 개선됐다. Emlid 직원은 USB 3.0이 2.4 GHz와 GPS에 간섭하는 것으로 알려져 있으니 USB 3.0 장비를 차폐하거나 USB 2.0을 쓰라고 조언했다.^[inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 증상: 안테나를 차에서 떼면 2개 이상 위성에서 SNR 40% 초과 및 Float/가끔 Fix, 가까이 두면 해 없음^[inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]
- 허브 연결 시 추적 위성 3~4개, SNR 20% 미만^[inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]
- 은박지로 전체 차폐 시 3개 이상 위성 SNR 약 50%^[inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]
- 한 댓글: 접지판 반경 최소 10 cm 권장(개인 의견, 비공식)^[inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]
- 권고: USB 3.0 장비·케이블 차폐, 저역통과 필터, 또는 USB 2.0 사용^[inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]

## 한계·미확인
공식 시험 자료가 아닌 포럼 일화. 정량 dB·거리 데이터 없음. 신뢰도 낮음.^[inbox/processed/hw-20261021-env-usb3-gnss-emlid-forum-2017.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
