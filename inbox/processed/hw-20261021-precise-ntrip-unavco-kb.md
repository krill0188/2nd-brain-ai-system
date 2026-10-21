---
title: "What is NTRIP? (UNAVCO Knowledge Base 291)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: navigation-gnss-denied
source: https://kb.unavco.org/article/what-is-ntrip-291.html
tags: [drone, gnss, 2-정밀측위]
authors: "UNAVCO Knowledge Base"
published: "2008-11-18 게시, 최종수정 2026-05-28"
---

## 핵심 내용
NTRIP(Networked Transport of RTCM via Internet Protocol)은 독일 BKG가 개발한 DGPS/RTK 보정 데이터 인터넷 스트리밍 프로토콜. NtripServer(기준국 데이터를 캐스터로 전달), NtripCaster(HTTP 서버로 스트림 배포), NtripClient(로버에 보정 적용)의 3요소로 구성된다.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 드론 RTK 링크 설계 시 로버 측은 NtripClient 역할(지상국 또는 컴패니언 컴퓨터)을 수행하고 MAVLink 등으로 FC에 주입하는 구조를 고려
- 3요소: Server / Caster / Client

## 한계·미확인
마운트포인트, 지연·대역폭, 프로토콜 버전별 차이는 이 페이지에 없음. 정량 수치 없음.
