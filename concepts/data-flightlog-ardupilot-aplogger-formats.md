---
title: "AP_Logger README: format types, units, multipliers (ArduPilot GitHub)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
ontology_class: ArduPilot
tags: [drone, flight-log, dataflash, ardupilot]
sources: [inbox/processed/hw-20261021-data-flightlog-ardupilot-aplogger-formats.md]
confidence: medium
contested: false
contradictions: []
---

# AP_Logger README: format types, units, multipliers (ArduPilot GitHub)

- 원문: https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Logger/README.md^[inbox/processed/hw-20261021-data-flightlog-ardupilot-aplogger-formats.md]
- 저자: ArduPilot contributors^[inbox/processed/hw-20261021-data-flightlog-ardupilot-aplogger-formats.md]
- 발행: 미확인^[inbox/processed/hw-20261021-data-flightlog-ardupilot-aplogger-formats.md]

## 핵심 내용
ArduPilot 로그 필드의 형식 문자(format type)는 C 타입과 항목 저장 크기를 정한다(예: h=int16_t, f=float, Z=char[64], M=uint8_t 비행 모드). 레거시 타입 c, C, e, E는 do not use이며 기본 타입+배율(multiplier)로 대체되었다. 단위는 기본 단위를 쓴다(예: 배터리 용량은 mAh가 아니라 amp-seconds). 배율은 기록된 원시값에 적용된다.^[inbox/processed/hw-20261021-data-flightlog-ardupilot-aplogger-formats.md]
원문 인용: "a GCS shouldn't/mustn't infer any scaling from the unit name."^[inbox/processed/hw-20261021-data-flightlog-ardupilot-aplogger-formats.md]

## 설계·운용에 쓸 수 있는 지침
- 로그 파서는 단위 이름이 아니라 FMT의 배율 정의로 스케일을 적용한다.^[inbox/processed/hw-20261021-data-flightlog-ardupilot-aplogger-formats.md]

## 한계·미확인
- FMT 메시지 구조, 로그 전체 구조, 백엔드 설명은 이 README에 없음: 미확인.^[inbox/processed/hw-20261021-data-flightlog-ardupilot-aplogger-formats.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[ardupilot-architecture]]
