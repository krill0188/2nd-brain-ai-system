---
title: "MCAP Format Specification"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ros-middleware
tags: [drone, flight-log, mcap, ros2]
sources: [inbox/processed/hw-20261021-data-flightlog-mcap-spec.md]
confidence: medium
contested: false
contradictions: []
---

# MCAP Format Specification

- 원문: https://mcap.dev/spec^[inbox/processed/hw-20261021-data-flightlog-mcap-spec.md]
- 저자: MCAP project (Foxglove 주도로 알려져 있으나 페이지에서 미확인)^[inbox/processed/hw-20261021-data-flightlog-mcap-spec.md]
- 발행: 미확인^[inbox/processed/hw-20261021-data-flightlog-mcap-spec.md]

## 핵심 내용
MCAP은 임의 직렬화 형식의 타임스탬프 pub/sub 메시지를 기록하는 컨테이너 형식이다. 파일은 Header, Data 절, 선택적 Summary, Summary Offset, Footer로 구성된다. 파일 처음과 끝에 magic 0x89 M C A P 0x30 \r \n가 오며 "MCAP" 다음 바이트가 major version이다. 레코드는 1바이트 opcode와 길이 접두를 가진다: Header 0x01, Footer 0x02, Schema 0x03, Channel 0x04, Message 0x05, Chunk 0x06, Message Index 0x07, Chunk Index 0x08, Attachment 0x09, Statistics 0x0B, Data End 0x0F. Schema는 0이 아닌 고유 ID를 가지며 이를 쓰는 Channel보다 먼저 나와야 한다. Channel은 토픽과 메시지 인코딩, 선택적 schema ID를 묶는다. Chunk는 압축(zstd, lz4 등)과 CRC32 검증, 인덱싱 단위이다.^[inbox/processed/hw-20261021-data-flightlog-mcap-spec.md]
원문 인용: "all Message records should be written into Chunk records." (Use of chunk records)^[inbox/processed/hw-20261021-data-flightlog-mcap-spec.md]

## 설계·운용에 쓸 수 있는 지침
- opcode 0x01-0x7F는 예약, 0x80-0xFF는 사설용, 0x00은 무효.^[inbox/processed/hw-20261021-data-flightlog-mcap-spec.md]
- 임의 접근/시간 범위 조회가 필요하면 Chunk Index와 Message Index를 둔 chunked 파일로 기록한다.^[inbox/processed/hw-20261021-data-flightlog-mcap-spec.md]
- 비행 로그와 ROS 2 bag을 같은 컨테이너로 다루려면 schema/channel 정의를 먼저 기록한다.^[inbox/processed/hw-20261021-data-flightlog-mcap-spec.md]

## 한계·미확인
- 기본 chunk 크기 등 권장 수치는 본 요약에서 미확인. 작성자/게시일 미확인.^[inbox/processed/hw-20261021-data-flightlog-mcap-spec.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[ros2-drone-integration]]
