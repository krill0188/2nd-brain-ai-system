---
title: "Problems with interference from USB3 hub (Emlid community forum)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: hardware
source: https://community.emlid.com/t/problems-with-interference-from-usb3-hub/6830
tags: [drone, gnss, 3-설치환경]
authors: "Emlid 커뮤니티 사용자 및 Emlid 직원 댓글"
published: "2017-07-24"
---

## 핵심 내용
Emlid Reach GNSS 모듈을 RC카에 탑재했을 때 USB 3.0 허브 연결로 GNSS 수신이 붕괴한 사례(일화적 포럼 보고). 허브 연결 시 3~4개 위성만 낮은 SNR로 추적. USB 2.0 기기는 영향이 작고 Wi-Fi은 영향 없었다. 전체를 은박지로 감싸면 개선됐다. Emlid 직원은 USB 3.0이 2.4 GHz와 GPS에 간섭하는 것으로 알려져 있으니 USB 3.0 장비를 차폐하거나 USB 2.0을 쓰라고 조언했다.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 증상: 안테나를 차에서 떼면 2개 이상 위성에서 SNR 40% 초과 및 Float/가끔 Fix, 가까이 두면 해 없음
- 허브 연결 시 추적 위성 3~4개, SNR 20% 미만
- 은박지로 전체 차폐 시 3개 이상 위성 SNR 약 50%
- 한 댓글: 접지판 반경 최소 10 cm 권장(개인 의견, 비공식)
- 권고: USB 3.0 장비·케이블 차폐, 저역통과 필터, 또는 USB 2.0 사용

## 한계·미확인
공식 시험 자료가 아닌 포럼 일화. 정량 dB·거리 데이터 없음. 신뢰도 낮음.
