---
title: pymavlink
created: 2026-07-29
updated: 2026-07-29
type: concept
tags: [drone, drone-sw, datalink]
sources: [inbox/fetch-2026-07-29-pymavlink.md]
confidence: high
contested: false
contradictions: []
domain: comms-protocol
---

# pymavlink

pymavlink는 MAVLink 프로토콜을 위한 Python 구현체이다. 드론과 GCS 간 통신을 위한 파서, 생성기, 유틸리티를 제공한다.

## 핵심 기능

- **MAVLink 메시지 파싱/생성**: 바이너리 MAVLink 스트림 처리
- **로그 도구**: `.tlog`, `.bin` 로그 파일 분석
- **유틸리티**: `mavproxy`, `mavlogdump` 등 명령줄 도구
- **다중 언어 지원**: Python, C, C++, JavaScript 등으로 코드 생성

## 최신 릴리스: v2.4.49 (2025-08-01)

### 주요 변경사항

- **mavlogdump**: 로그 트리밍 시 단위 및 형식 보존
- **DFReader**: 대부분의 메시지에 대한 인스턴스 인덱싱 수정
- **타입 어노테이션**: 생성된 Python 코드에서 `cast(...)`를 타입 어노테이션으로 대체
- **JavaScript 생성기**: Node와 브라우저 모두에서 작동하도록 개선
- **Spin2 생성기**: 여러 문제 수정
- **새로운 도구**: `mavtranslatelog.py` 추가 — tlog 파일 업데이트용
- **WebSocket**: WebSocket 지원 수정

## 관련 개념

- [[mavlink-protocol]] — pymavlink가 구현하는 프로토콜
- [[mavsdk]] — MAVLink 기반 고수준 SDK
- [[ground-control-station]] — pymavlink를 사용하는 GCS
