# Critique

## 채택 후보
- selected: 후보 1 — 암호학적 서명 검증과 독립된 물리적(시각) 대조 채널이라는 아이디어는 논리적으로 자기완결적이고 기존 기술(마커/특징점 기반 상대 위치 추정)로 구현 경로가 분명한 반면, 후보 2는 검증자가 동일한 "그 순간의 시각 장면"을 어떻게 독립적으로 확보/재현하는지에 대한 프로토콜적 공백이 있어 실현가능성이 크게 떨어진다.

## Novelty
- score: 7
- rationale: 검색 결과 중 `raw/papers/datalink/koubaa2019-mavlink-survey.md`는 MAVLink 보안을 서명·키 관리 등 암호학 계층에서만 다루고, `concepts/rgb-ir-fusion-uav-detection.md`나 `raw/papers/drone-hw/danial2025-microdrone-slam.md`는 OpenCV/비전을 객체 탐지·자기 위치추정(SLAM) 목적으로만 다룬다. 두 계열을 "서명된 주장 vs. 물리적 목격"이라는 상호 검증 구도로 명시적으로 결합한 사례는 canonical/raw 어디에도 없다. 단, `concepts/gps-uav-imu.md`나 스웜 관련 문헌들이 이미 "상대적 비전 기반 센싱"을 다루고 있어 구성 요소 자체는 낯설지 않으므로 만점을 주지는 않는다.
- duplicate_of: 없음

## Feasibility
- score: 6
- rationale: 마커 인식(AprilTag/ArUco류)이나 특징점 매칭을 통한 인접 드론의 상대 궤적 추정은 이미 검증된 컴퓨터 비전 기술이며(`raw/papers/drone-hw/danial2025-microdrone-slam.md`가 보여주듯 단안 카메라+IMU만으로도 자기 위치추정이 가능한 수준), MAVLink2 서명 텔레메트리 방송도 표준 기능이다(`raw/papers/datalink/koubaa2019-mavlink-survey.md`). 두 데이터 스트림을 실시간으로 대조하는 것은 추가 엔지니어링이지만 미래 기술 가정이 필요 없다. 다만 편대 비행 중 상대 거리·조명·각도 변화 속에서 오탐지 없이 안정적으로 "물리 궤적 vs. 방송 텔레메트리" 불일치를 판정하는 임계치 설계는 아직 검증되지 않아 만점은 아니다.
- missing_pieces: (1) 다양한 거리/조명/기동 조건에서 강건한 실시간 상대 위치추정 알고리즘의 편대 규모 검증, (2) 통신 지연과 카메라 프레임레이트 차이를 보정하는 시간 동기화 메커니즘, (3) 오탐지(false alarm)와 실제 스푸핑을 구분할 임계치·통계 모델
