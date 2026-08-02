# Critique

## 채택 후보
- selected: 후보 2 — 실시간 저지연 제약이 없는 사후 분석이라 후보 1보다 하드웨어·성능 요구가 낮고, 기존 optical flow/모션 추정 기술로 더 직접 커버된다.

## Novelty
- score: 7
- rationale: canonical 검색에서 `wallefpv.md`는 순수 하드웨어 스펙 정보만 있고, `gps-uav-imu.md`·`micro-drone-slam-imu-vio-lidar-uav-livox-mid-360-pixhawk-4-m.md`·`rgb-ir-fusion-uav-detection.md` 등은 모두 "자율비행을 위한 온보드 비전"(SLAM, 객체 검출)이 목적이지, 인간 조종사용 FPV 영상을 사후에 꺼내 "선언된 파라미터 대비 실제 조작 패턴"을 대조하는 컴플라이언스 감사 용도는 이 결과들에 없다. `drone-first-responder-dfr.md`가 규제/감사 맥락과 가장 가깝지만 그쪽은 경로계획·출동 지원이지 사후 행동 검증이 아니다. 다만 "영상에서 궤적·모션을 추출한다"는 기법 자체는 SLAM/VIO 계열 연구(예: `danial2025-microdrone-slam`, `shapira2025-icdnet`)와 원리적으로 겹치므로 완전히 새로운 기법은 아니며, 새로운 것은 응용 목적(사후 정책 준수 검증)뿐이다 — 그래서 만점권은 아니다.
- duplicate_of: 없음

## Feasibility
- score: 6
- rationale: 영상에서 optical flow·특징점 추적으로 상대적 모션(급선회, 고도 변화 추정)을 뽑는 것은 기존에 검증된 기술(예: `danial2025-microdrone-slam`, `shapira2025-icdnet`가 카메라+IMU만으로 SLAM급 정밀도를 내는 사례)이라 원리적으로 지금 존재하는 하드웨어·알고리즘으로 구현 가능하다. 다만 FPV 카메라는 짐벌 없이 조종사가 임의로 프레임을 흔드는 경우가 많아 "카메라 자체 회전/움직임"과 "기체 모션"을 영상만으로 분리하는 것이 SLAM 연구에서 전제하는 조건(안정적 카메라, 알려진 내부 파라미터)보다 훨씬 열악하고, IMU 로그 없이 영상만으로 절대 고도·속도를 복원하는 것은 스케일 모호성(monocular scale ambiguity) 문제로 정밀도가 크게 떨어진다.
- missing_pieces: (1) FPV 카메라 내부/외부 파라미터(FOV, 짐벌 유무) 사전 캘리브레이션 절차, (2) monocular 영상만으로 절대 스케일(속도·고도)을 복원하는 방법 — 검색 결과의 SLAM 사례들은 대부분 IMU 융합을 전제로 하는데 이 후보는 "영상만으로"라고 명시해 이 전제를 빼고 있음, (3) "선언된 파라미터/규제 설정"을 기계가 판독 가능한 형태로 인코딩하는 표준(현재 검색 결과에 이런 표준·포맷 존재 안 함).
