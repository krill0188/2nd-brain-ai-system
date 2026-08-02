# Critique

## 채택 후보
- selected: 후보 1 — 해시체인을 통한 파라미터-인식 로그 상호 서명 시스템은 기존 PX4 Logger 미들웨어(raw/articles/mastervault-px4-devnotes.md)와 온보드 VIO/SLAM 추정(concepts/micro-drone-slam-imu-vio-lidar-uav-livox-mid-360-pixhawk-4-m)을 조합하는 정도로 확실히 구현 가능한 반면, 후보 2는 "FC 제조사별 거동 시그니처가 관측 가능할 만큼 airframe/prop/tuning 변수보다 우세하다"는 검증되지 않은 전제에 의존해 실현 경로가 불투명하다.

## Novelty
- score: 6
- rationale: 검색 결과(concepts/gps-uav-imu, concepts/micro-drone-slam-imu-vio-lidar-uav-livox-mid-360-pixhawk-4-m, raw/papers/drone-ai/shapira2025-icdnet.md 등)에는 온보드 VIO/SLAM 상태추정 기법만 있고, FC 파라미터 변경 해시와 인식 스택 출력을 실시간으로 상호 서명하는 사례는 확인되지 않는다. 다만 raw/articles/mastervault-px4-devnotes.md가 보여주듯 PX4는 이미 Logger 미들웨어로 파라미터·센서·상태추정치를 함께 기록하고 있어, "설정값+인식 로그의 결합 기록"이라는 발상 자체는 블랙박스 개념의 연장선에 있다. 즉 조합의 세부(해시체인 상호증명)는 검색 결과 내에서 새롭지만, 상위 개념(무결성 증명 로깅)은 항공/보안 분야에서 이미 흔한 패턴이라 극단적 신규성은 아니다.
- duplicate_of: 없음

## Feasibility
- score: 6
- rationale: 해시 생성·체이닝은 계산량이 미미한 표준 암호 연산이고, 파라미터 변경 이벤트와 자세/모션 추정치 모두 PX4류 FC에서 이미 로깅되는 데이터이므로(raw/articles/mastervault-px4-devnotes.md의 Logger 컴포넌트, concepts/micro-drone-slam-imu-vio-lidar-uav-livox-mid-360-pixhawk-4-m의 온보드 VIO 사례) 엔지니어링 난이도는 낮다. 그러나 "자기증명"이라는 목적에는 근본적 약점이 있다 — FC와 인식 스택이 동일한 물리적 컴퓨팅 환경 위에서 서로를 서명하므로, 그 환경 자체가 침해되면(루트 권한 획득 등) 양쪽 로그를 사후에 동시에 조작해 체인을 재구성할 수 있다. 독립적인 하드웨어 신뢰 루트 없이는 "체크섬"이지 진정한 "제3자 증명"이 아니다.
- missing_pieces: 위변조 불가능한 하드웨어 신뢰 루트(TPM/secure enclave 등)와, FC 내부와 물리적으로 분리된 독립 타임스탬프/앵커링 수단(예: 외부 공개 원장에 주기적 커밋) — 이것이 없으면 상호 서명이 동일 신뢰 도메인 내부에서만 이루어져 증거력이 제한된다.
