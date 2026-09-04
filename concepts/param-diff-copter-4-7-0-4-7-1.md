---
title: "ArduPilot Copter 4.7.0 → 4.7.1 파라미터 변경 전체 목록"
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [drone, flight-control, parameter, diff, copter]
sources: [공식 파라미터 메타데이터 자동 diff]
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# ArduPilot Copter 4.7.0 → 4.7.1 파라미터 변경 전체 목록

> 공식 메타데이터 자동 비교 (생성일 2026-09-05). 개요 해설은 [[ardupilot-params-by-version]] 참조.

## 요약

| 구분 | 개수 |
|---|---|
| 4.7.0 총 파라미터 | 5145 |
| 4.7.1 총 파라미터 | 5145 |
| ➕ 신규 | 2 |
| ➖ 삭제 | 2 |

## ➕ 신규 파라미터 (2)

**PSC** (2): `PSC_D_JERK`, `PSC_NE_JERK`

## ➖ 삭제된 파라미터 (2)

**PSC** (2): `PSC_JERK_D`, `PSC_JERK_NE`

> ⚠️ 업그레이드 후 백업 파라미터 파일과 diff하여 기체 종속값을 재확인할 것.