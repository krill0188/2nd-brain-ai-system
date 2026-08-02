# Critique

## 채택 후보
- selected: 후보 1 — 구체적 프로토콜 확장 메커니즘과 검증 가능한 구현 경로가 있는 반면, 후보 2는 "재귀 창작 루프를 취약점 탐색에 재적용한다"는 메타 서술만 있고 산출물의 실제 유효성(진짜 취약점인지 환각인지)을 판정할 기준이 제안 자체에 없다(그 문제를 스스로 "다음 질문"으로 던지고 있다는 점이 이를 방증).

## Novelty
- score: 7
- rationale: raw 검색 결과 중 `allouch2019-mavsec`(MAVSec)는 인증·무결성·기밀성만 다루고, `entity-mavlink-protocol`과 `mastervault-mavlink-reference`도 MAVLink 2의 서명(HMAC-SHA256)을 "위조 여부" 검증으로만 기술한다. 세 출처 어디에도 필드 값의 출처(온보드 직접측정/드론 중계/지상국 추정)를 구분해 인식론적 신뢰도를 메시지에 임베드하는 방식은 등장하지 않는다. 다만 이 판단은 로컬 코퍼스에 한정된 것이라 — 외부 학계의 "provenance-aware sensor fusion" 또는 "trust-weighted swarm consensus" 계열 연구와 무관하다고 단정할 근거는 없다. 그래서 만점권(8-10)이 아니라 7점.
- duplicate_of: 없음

## Feasibility
- score: 6
- rationale: MAVLink 2는 이미 서명 필드, component targeting, 사용자 정의 메시지(ID 180-229 범위) 확장 슬롯을 제공하므로 "신뢰도 등급 필드"를 추가하는 것 자체는 기존 확장 메커니즘 안에서 구현 가능하다. 단일 벤더 폐쇄형 시스템(예: 자체 스웜 플릿)에서는 바로 시도할 수 있다. 하지만 제안이 전제하는 "스웜 내 다중 드론 간 중계"는 MAVLink의 기본 point-to-point/브로드캐스트 모델을 넘어서는 라우팅 계층(mavlink-router 등)이 필요하고, 중계 과정에서 출처 메타데이터가 소실되지 않도록 보존하는 로직은 표준에 없다. 또한 "신뢰도 등급 taxonomy"를 PX4·ArduPilot 양쪽 생태계가 합의해야 상호운용 가능한 표준으로서 의미가 생기는데, 이 합의 절차는 기술이 아니라 거버넌스 문제라 시간이 걸린다.
- missing_pieces: 신뢰도 등급 taxonomy의 벤더 간 표준화, 다중 홉 중계 시 출처 메타데이터를 보존하는 라우팅 계층, PX4/ArduPilot 양쪽의 채택 합의
