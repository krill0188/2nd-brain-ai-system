---
title: "ULog File Format (PX4 User and Developer Guide)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
tags: [drone, flight-log, ulog, px4]
sources: [inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]
confidence: medium
contested: false
contradictions: []
---

# ULog File Format (PX4 User and Developer Guide)

- 원문: https://docs.px4.io/main/en/dev_log/ulog_file_format.html^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]
- 저자: PX4 project^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]
- 발행: 미확인(문서 페이지, 개정 상시)^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]

## 핵심 내용
ULog는 PX4 로거의 로그 형식이며 자기기술형(self-describing)이다. 파일 안에 기록된 uORB 메시지 타입의 정의가 함께 들어간다. 모든 값은 little-endian이다. 파일은 Header(고정 16바이트), Definitions, Data 세 부분이다. Header는 7바이트 magic(ASCII "ULog" + 0x01 0x12 0x35), 1바이트 version, 8바이트 uint64 시작 타임스탬프(마이크로초)로 구성된다. Definitions 절에는 소프트웨어 버전, 메시지 형식, 초기 파라미터가 있으며 메시지 종류는 Flag Bits(B), Format(F), Information(I), Multi Information(M), Parameter(P), Default Parameter(Q)이다. Data 절에는 Subscription(A), Unsubscription(R), Logged Data(D), Logged String(L), Tagged Logged String(C), Synchronization(S), Dropout(O) 등이 있다.^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]

원문 인용: "The format is self-describing, i.e. it contains the format and uORB message types that are logged." (Introduction)^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]

## 설계·운용에 쓸 수 있는 지침
- 메시지 헤더 3바이트: uint16 size(헤더 제외) + uint8 type.^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]
- Flag Bits 메시지 40바이트(compat 8, incompat 8, appended_offsets 3x8), 헤더 직후 첫 메시지여야 함.^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]
- 손상 후 재동기화용 sync magic: 0x2F 0x73 0x13 0x20 0x25 0x0C 0xBB 0x12.^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]
- 로그 레벨 0(EMERG)~7(DEBUG), 타임스탬프 단위 마이크로초.^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]
- 자체 파서 작성 시 위 구조로 Definitions를 먼저 읽어 Data 메시지를 해석한다.^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]

## 한계·미확인
- 페이지 내 버전 서술이 불일치(헤더 절은 version 1, 이력 절은 version 2 변경 언급)하여 현행 버전은 미확인.^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]
- 각 필드별 상세 레이아웃(Format 메시지 문자열 문법 등)은 본 요약에서 미확인.^[inbox/processed/hw-20261021-data-flightlog-px4-ulog-format.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[px4-offboard-control]]
