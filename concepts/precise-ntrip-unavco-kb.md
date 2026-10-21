---
title: "What is NTRIP? (UNAVCO Knowledge Base 291)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-precise-ntrip-unavco-kb.md]
confidence: medium
contested: false
contradictions: []
---

# What is NTRIP? (UNAVCO Knowledge Base 291)

- 원문: https://kb.unavco.org/article/what-is-ntrip-291.html^[inbox/processed/hw-20261021-precise-ntrip-unavco-kb.md]
- 저자: UNAVCO Knowledge Base^[inbox/processed/hw-20261021-precise-ntrip-unavco-kb.md]
- 발행: 2008-11-18 게시, 최종수정 2026-05-28^[inbox/processed/hw-20261021-precise-ntrip-unavco-kb.md]

## 핵심 내용
NTRIP(Networked Transport of RTCM via Internet Protocol)은 독일 BKG가 개발한 DGPS/RTK 보정 데이터 인터넷 스트리밍 프로토콜. NtripServer(기준국 데이터를 캐스터로 전달), NtripCaster(HTTP 서버로 스트림 배포), NtripClient(로버에 보정 적용)의 3요소로 구성된다.^[inbox/processed/hw-20261021-precise-ntrip-unavco-kb.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 드론 RTK 링크 설계 시 로버 측은 NtripClient 역할(지상국 또는 컴패니언 컴퓨터)을 수행하고 MAVLink 등으로 FC에 주입하는 구조를 고려^[inbox/processed/hw-20261021-precise-ntrip-unavco-kb.md]
- 3요소: Server / Caster / Client^[inbox/processed/hw-20261021-precise-ntrip-unavco-kb.md]

## 한계·미확인
마운트포인트, 지연·대역폭, 프로토콜 버전별 차이는 이 페이지에 없음. 정량 수치 없음.^[inbox/processed/hw-20261021-precise-ntrip-unavco-kb.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
