---
source: "career-bot/store/questions.json#비행제어"
ingested: 2026-08-02
captured: 2026-08-02
type: quiz-compilation
evidence_tier: non-primary-reconstruction
category: "비행제어"
question_count: 62
author: "DroneAI Lab 커리어 문항은행 (비공개 실무자 재구성)"
sha256: "240ef267a6a5003e831f45c36bb8e5d0703e9436934a2151b3db6668672f04e4"
tags: [career, quiz, flight-control-quiz]
---

# 비행제어 — 커리어 대비 퀴즈 재구성 컴필레이션 (62문항)

> ⚠️ **비-1차-증거 고지**: 이 문서는 방산/드론/AI 커리어 대비용으로 재구성된
> 객관식 퀴즈 모음이다. 각 항목에 원출처 인용이 없으므로 `research/` AI
> 연구 루프의 Retriever/Verifier는 이 문서를 **1차 증거(raw evidence)로
> 취급해서는 안 된다**. Critic/Verifier가 근거로 인용할 경우 반드시
> `verification_status: insufficient_evidence`로 처리하고, 별도의 1차
> 출처(GitHub/arXiv/공식문서 등)로 교차검증한 뒤에만 canonical 승격
> 대상이 될 수 있다. 정답/해설은 원저작자(DroneAI Lab 내부 실무자)의 실무 지식
> 재구성이며 공식 표준 문서가 아니다.

**원본**: `career-bot/store/questions.json` (id 범위: 1–160)
**난이도 분포**: easy=11, hard=20, medium=31

## 문항

### Q1. PX4에서 uORB 토픽을 구독하는 함수는?
- ✅ orb_subscribe()
-    orb_listen()
-    uorb_register()
-    px4_subscribe()

**해설**: uORB(Micro Object Request Broker)는 PX4의 내부 메시지 전달 시스템입니다. orb_subscribe()로 토픽을 구독하고, orb_publish()로 발행합니다.

**팁**: 면접 시 uORB의 pub/sub 패턴과 실시간 데이터 공유 메커니즘을 설명하면 좋습니다.

### Q2. EKF2에서 GPS 신호가 없을 때 사용하는 센서 조합은?
- ✅ Optical Flow + Rangefinder + IMU
-    GPS + Barometer
-    Magnetometer + GPS
-    Accelerometer만

**해설**: GPS-denied 환경에서는 Optical Flow(수평 속도), Rangefinder(고도), IMU(관성)를 융합하여 위치를 추정합니다.

**팁**: GPS-denied 대응은 군용 드론의 핵심 역량입니다. 실제 EKF 파라미터 튜닝 경험을 언급하세요.

### Q3. PX4 PID 튜닝의 올바른 순서는?
- ✅ Rate P → Rate D → Rate I → Angle P
-    Angle P → Rate P → Rate I → Rate D
-    Rate I → Rate P → Rate D → Angle P
-    Rate D → Rate I → Angle P → Rate P

**해설**: Rate(내부 루프)부터 안정화한 후 Angle(외부 루프)를 튜닝합니다. P로 응답성 확보 → D로 진동 억제 → I로 정상 상태 오차 제거.

**팁**: 실제 튜닝 경험과 각 게인이 비행에 미치는 영향을 구체적으로 설명하세요.

### Q4. PX4 Commander 모듈의 주요 역할은?
- ✅ 시스템 상태 관리 및 비행 모드 전환
-    모터 PWM 출력 제어
-    센서 데이터 필터링
-    통신 프로토콜 처리

**해설**: Commander는 PX4의 핵심 상태 머신으로, Arming/Disarming, 비행 모드 전환, Failsafe 트리거 등 시스템 전반의 상태를 관리합니다.

**팁**: Commander의 상태 전이 다이어그램을 그릴 수 있으면 임팩트가 큽니다.

### Q5. ArduPilot의 Lua 스크립팅 기능의 주요 활용은?
- ✅ 현장 커스터마이징 (비행 모드, 센서 로직)
-    운영체제 커널 수정
-    GCS UI 커스터마이징
-    MAVLink 프로토콜 변경

**해설**: Lua 스크립팅으로 펌웨어 재빌드 없이 비행 로직, 센서 처리, 자동화 시퀀스를 현장에서 바로 수정할 수 있습니다.

**팁**: Lua로 구현한 구체적인 사례(자동 착륙 시퀀스, 센서 보정 등)를 준비하세요.

### Q6. PX4가 사용하는 NuttX RTOS의 태스크 스케줄링 방식은?
- ✅ 우선순위 기반 선점형 스케줄링
-    라운드 로빈 스케줄링
-    FIFO 스케줄링
-    협력적(Cooperative) 스케줄링

**해설**: NuttX는 우선순위 기반 선점형(Priority-based Preemptive) RTOS로, 높은 우선순위 태스크가 낮은 우선순위 태스크를 즉시 선점합니다.

**팁**: 실시간 시스템에서 우선순위 역전(Priority Inversion) 문제와 해결책도 알아두세요.

### Q7. Offboard 모드에서 Heartbeat가 끊기면 어떻게 되는가?
- ✅ Failsafe 전환 (Position Hold/RTL)
-    모터 즉시 정지
-    계속 마지막 명령 수행
-    수동 모드로 전환

**해설**: Offboard 모드에서 Heartbeat 타임아웃(기본 500ms) 발생 시 안전을 위해 Position Hold 또는 RTL로 자동 전환됩니다.

**팁**: Failsafe 설정 파라미터(COM_OF_LOSS_T 등)와 실제 테스트 경험을 언급하세요.

### Q8. Motor Mixing Matrix의 역할은?
- ✅ 모터 배치별 추력/토크 변환
-    배터리 전압 보상
-    ESC 신호 타이밍 조절
-    프로펠러 효율 계산

**해설**: Mixing Matrix는 Roll/Pitch/Yaw/Throttle 명령을 각 모터의 개별 출력으로 변환합니다. 기체 형상(쿼드/헥사/옥토)에 따라 행렬이 달라집니다.

**팁**: 커스텀 프레임 설계 시 Mixing Matrix를 직접 계산한 경험이 있으면 차별화됩니다.

### Q9. PX4의 Sensor Voting 메커니즘이 하는 일은?
- ✅ 다중 센서 중 이상치 제외, 중앙값 사용
-    가장 비싼 센서만 사용
-    모든 센서 평균값 사용
-    랜덤으로 센서 선택

**해설**: 다중 동일 센서(예: IMU 3개) 장착 시, 이상치를 보이는 센서를 자동 배제하고 나머지의 중앙값 또는 가중 평균을 사용합니다.

**팁**: TMR(Triple Modular Redundancy) 개념과 함께 설명하면 신뢰성 설계 역량을 어필할 수 있습니다.

### Q10. HITL과 SITL 시뮬레이션의 차이점은?
- ✅ HITL은 실제 FC 하드웨어 사용, SITL은 PC만
-    HITL이 더 느림
-    SITL은 하드웨어 필수
-    차이 없음

**해설**: HITL(Hardware-In-The-Loop)은 실제 FC 보드를 연결하여 시뮬레이션하고, SITL(Software-In-The-Loop)은 PC에서 펌웨어를 에뮬레이션합니다.

**팁**: 개발 단계별 SITL→HITL→실비행 테스트 프로세스를 설명하세요.

### Q71. PX4의 Safety Switch(안전 스위치) 역할은?
- ✅ 실수로 인한 모터 가동 방지 (Arm 전 물리적 확인)
-    GPS 신호 부스트
-    배터리 잔량 표시
-    비행 모드 변경

**해설**: Safety Switch는 소프트웨어 Arm 명령 외에 물리적 버튼 확인을 추가하여, 지상에서의 실수로 인한 모터 가동을 이중으로 방지합니다.

**팁**: 군용 드론에서의 다중 안전 체계(SW Arm + HW Safety + Geofence)를 설명하세요.

### Q78. PX4의 Geofence(지오펜스) 위반 시 기본 동작은?
- ✅ 경고 후 RTL(Return to Launch)
-    모터 정지
-    무시
-    착륙

**해설**: Geofence 위반 시 기본적으로 경고를 발생시키고 RTL 모드로 전환합니다. 설정에 따라 Loiter, Land 등으로 변경 가능합니다.

**팁**: 군용 드론의 Geofence 설계(비행금지구역, 최대 고도/거리)와 실패 시 안전 대책을 설명하세요.

### Q111. PX4 펌웨어에서 비행체의 자세(attitude)를 나타내는 기본 표현 방식은?
- ✅ 오일러 각(Euler Angles)
-    데카르트 좌표(Cartesian Coordinates)
-    극좌표(Polar Coordinates)
-    베지어 곡선(Bezier Curve)

**해설**: 비행제어에서 자세는 Roll, Pitch, Yaw로 구성된 오일러 각으로 표현합니다. 다만 짐벌락 문제로 인해 내부 계산에서는 쿼터니언(Quaternion)을 주로 사용합니다.

**팁**: 오일러 각의 짐벌락 문제와 쿼터니언의 장점을 함께 설명할 수 있으면 좋습니다.

### Q112. 멀티콥터에서 요(Yaw) 회전을 제어하는 방법은?
- ✅ 대각선 방향 모터 쌍의 속도 차이를 이용
-    앞뒤 모터의 속도 차이를 이용
-    좌우 모터의 속도 차이를 이용
-    모든 모터를 동시에 가속/감속

**해설**: 쿼드콥터에서 요(Yaw)는 CW/CCW로 회전하는 대각선 방향 모터 쌍의 속도 차이로 제어합니다. CW 모터들의 속도를 높이면 기체가 CCW 방향으로 회전합니다.

**팁**: 멀티콥터 모터 배치(X형/+형)와 회전 방향에 따른 토크 상쇄 원리를 이해하면 좋습니다.

### Q113. PX4의 Stabilized 모드에서 RC 스틱을 중립으로 놓으면 기체는 어떻게 동작하는가?
- ✅ 수평 자세를 유지하며 현재 위치에서 천천히 이동
-    즉시 정지하고 현재 위치를 유지
-    자동으로 홈 포인트로 복귀
-    엔진이 꺼지고 자유낙하

**해설**: Stabilized 모드에서 스틱 중립은 Roll/Pitch 0도(수평)를 명령합니다. 기체는 수평 자세를 유지하지만 GPS 위치 고정은 없으므로 바람에 의해 천천히 이동할 수 있습니다.

**팁**: Stabilized vs Position 모드의 차이(GPS 위치 고정 여부)를 명확히 구분하세요.

### Q114. ESC(Electronic Speed Controller)의 주요 역할은?
- ✅ FC의 PWM 신호를 받아 모터 회전수를 제어
-    GPS 신호를 처리하여 위치를 계산
-    배터리 충전 상태를 모니터링
-    무선 통신 신호를 처리

**해설**: ESC는 비행 컨트롤러(FC)에서 보내는 PWM 또는 DSHOT 신호를 받아 3상 BLDC 모터의 회전수를 제어합니다. 모터에 공급되는 전류와 타이밍을 조절합니다.

**팁**: BLDC 모터의 3상 전력 공급 원리와 ESC의 전자정류(Electronic Commutation) 개념도 알아두세요.

### Q115. IMU(Inertial Measurement Unit)가 측정하는 데이터는?
- ✅ 가속도와 각속도
-    GPS 위치와 속도
-    기압과 온도
-    자기장 강도와 방향

**해설**: IMU는 3축 가속도계(Accelerometer)와 3축 자이로스코프(Gyroscope)로 구성되어 가속도와 각속도를 측정합니다. 이 데이터로 자세 추정이 가능합니다.

**팁**: IMU의 드리프트(drift) 문제와 이를 보정하기 위한 센서 융합(Magnetometer, Barometer, GPS) 방법을 설명하면 좋습니다.

### Q116. PWM 신호에서 드론 ESC의 최소 스로틀(모터 정지) 신호는 일반적으로 몇 μs인가?
- ✅ 1000 μs
-    500 μs
-    1500 μs
-    2000 μs

**해설**: 표준 RC PWM 프로토콜에서 1000μs는 최소값(0%), 2000μs는 최대값(100%)입니다. ESC는 1000μs 신호에서 모터를 정지 상태로 유지합니다.

**팁**: DSHOT 프로토콜은 디지털 방식으로 PWM의 노이즈 취약성을 극복합니다. DSHOT300/600/1200 숫자는 비트레이트(kbps)입니다.

### Q117. ArduPilot의 Loiter 모드는 어떤 기능을 제공하는가?
- ✅ GPS를 이용하여 현재 위치와 고도를 자동으로 유지
-    자동으로 홈 포인트로 복귀
-    미리 설정된 웨이포인트를 따라 자율 비행
-    원형 궤도를 자동으로 비행

**해설**: Loiter 모드는 GPS와 기압계를 사용하여 현재의 3D 위치(위도, 경도, 고도)를 자동으로 유지하는 모드입니다. 바람이 불어도 제자리를 유지합니다.

**팁**: Loiter vs Position Hold vs Auto Hover의 차이를 펌웨어별(PX4/ArduPilot)로 구분하여 설명할 수 있어야 합니다.

### Q118. PX4에서 HITL(Hardware-In-The-Loop) 시뮬레이션과 SITL(Software-In-The-Loop)의 가장 큰 차이점은?
- ✅ HITL은 실제 FC 하드웨어를 사용하고 SITL은 소프트웨어만 사용
-    HITL이 SITL보다 항상 빠름
-    SITL은 실제 비행 테스트를 포함
-    HITL은 GPS를 사용하지 않음

**해설**: SITL은 모든 것이 소프트웨어로 시뮬레이션되며, HITL은 실제 FC 하드웨어를 시뮬레이터와 연결하여 테스트합니다. HITL이 실제 환경에 더 가깝습니다.

**팁**: HITL은 센서 드라이버, 타이밍 등 하드웨어 종속 코드를 검증할 수 있어 양산 전 최종 검증에 사용됩니다.

### Q119. Failsafe 기능이 동작하는 대표적인 조건은?
- ✅ RC 신호 수신 불량, 배터리 저전압, GPS 신호 손실
-    바람 속도 초과, 온도 이상, 진동 과다
-    카메라 오류, SD카드 불량, 페이로드 이탈
-    프로펠러 불균형, 모터 과열, ESC 오류

**해설**: Failsafe는 RC 링크 끊김, 배터리 전압 임계값 이하, GPS 신호 손실 등의 조건에서 자동으로 동작합니다. 일반적으로 RTL(Return To Launch) 또는 자동 착륙으로 대응합니다.

**팁**: Failsafe 동작 우선순위와 각 Failsafe 유형별 대응 방법(RTL/Land/Hold/Disarm)을 숙지하세요.

### Q120. 드론 캘리브레이션 시 반드시 수행해야 하는 항목이 아닌 것은?
- ✅ 프로펠러 피치 측정
-    가속도계(Accelerometer) 캘리브레이션
-    나침반(Compass) 캘리브레이션
-    ESC 캘리브레이션

**해설**: 프로펠러 피치 측정은 캘리브레이션 항목이 아닙니다. 필수 캘리브레이션은 가속도계, 자이로스코프, 나침반, ESC, 라디오 입력 캘리브레이션입니다.

**팁**: 새 기체 조립 시 캘리브레이션 순서: 가속도계 → 나침반 → 라디오 → ESC → 레벨 캘리브레이션

### Q121. PX4의 uORB에서 orb_check()와 orb_copy()를 함께 사용하는 이유는?
- ✅ 새 데이터 존재 여부 확인 후 복사하여 불필요한 CPU 사용을 줄이기 위해
-    데이터 무결성 검증을 위해 두 번 읽는 것
-    멀티스레드 안전성을 위한 락킹 메커니즘
-    토픽 구독 취소 전 마지막 데이터를 백업하기 위해

**해설**: orb_check()는 새로운 데이터가 발행되었는지 확인하고, 새 데이터가 있을 때만 orb_copy()로 복사합니다. 이를 통해 매 루프마다 데이터를 복사하는 오버헤드를 줄입니다.

**팁**: PX4 최신 버전에서는 uORB::Subscription 클래스의 updated()와 copy() 메서드를 사용하는 C++ 스타일이 권장됩니다.

### Q122. PID 제어에서 D항(미분항)의 주요 역할은?
- ✅ 오차의 변화율에 반응하여 오버슈트를 억제
-    누적 오차를 제거하여 정상상태 오차를 없앰
-    현재 오차에 비례하여 즉각 수정 명령 생성
-    목표값과 현재값의 차이를 증폭

**해설**: D항은 오차의 변화 속도(미분)에 반응합니다. 오차가 빠르게 변하면 큰 반대 방향 힘을 가해 오버슈트를 억제하고 시스템의 댐핑을 증가시킵니다.

**팁**: PID 튜닝 순서: P 먼저 증가 → 오실레이션 발생 → D로 댐핑 → I로 정상상태 오차 제거

### Q123. EKF(Extended Kalman Filter)를 비행 컨트롤러에서 사용하는 주된 이유는?
- ✅ 여러 센서의 노이즈 데이터를 융합하여 최적 상태 추정치를 제공
-    모터 출력 효율을 최대화하기 위한 경로 최적화
-    배터리 소모를 최소화하기 위한 에너지 관리
-    무선 통신의 패킷 손실을 보상

**해설**: EKF는 IMU, GPS, Barometer, Magnetometer 등 여러 센서의 노이즈가 섞인 데이터를 융합하여 위치, 속도, 자세의 최적 추정값을 계산합니다. 비선형 시스템에 적용 가능한 칼만 필터입니다.

**팁**: PX4에서는 ECL EKF2 모듈이 기본으로 사용되며, EKF2_AID_MASK 파라미터로 사용할 센서 소스를 설정합니다.

### Q124. ArduPilot에서 ATC_RAT_RLL_P 파라미터가 의미하는 것은?
- ✅ Roll 자세 rate 루프의 P 게인
-    Roll 자세 angle 루프의 P 게인
-    Pitch rate 루프의 P 게인
-    Roll 속도 제한 파라미터

**해설**: ATC_RAT_RLL_P는 AttitudeControl(ATC) - Rate - Roll - P 게인을 의미합니다. 내부 루프인 rate 컨트롤러의 Roll 축 비례 게인입니다.

**팁**: ArduCopter의 이중 루프 구조: 외부 루프(angle controller) → 내부 루프(rate controller). 파라미터명 패턴 숙지 필요.

### Q125. DSHOT600과 PWM의 차이점을 올바르게 설명한 것은?
- ✅ DSHOT600은 디지털 신호로 노이즈에 강하고 2way 통신(ESC 텔레메트리)을 지원
-    DSHOT600은 아날로그 신호로 높은 해상도를 제공
-    PWM이 DSHOT보다 더 빠른 업데이트 속도를 가짐
-    DSHOT는 개별 모터 캘리브레이션이 필요

**해설**: DSHOT는 디지털 프로토콜로 노이즈에 강하고 체크섬을 통한 오류 검출이 가능합니다. DSHOT600(숫자는 kbps)은 Bidirectional DSHOT를 통해 eRPM 텔레메트리를 FC에 전송할 수 있습니다.

**팁**: DSHOT 300/600/1200의 숫자 차이는 비트레이트이며, 더 긴 케이블에는 낮은 속도(DSHOT300)가 안정적입니다.

### Q126. PX4의 Offboard 모드에서 기체를 제어하기 위해 반드시 유지해야 하는 조건은?
- ✅ 2Hz 이상의 주기로 외부 setpoint 메시지를 지속적으로 전송
-    RC 송신기를 항상 ON 상태로 유지
-    QGroundControl과 MAVLink 연결을 유지
-    최소 8개 이상의 GPS 위성 신호 수신

**해설**: Offboard 모드는 외부 컴퓨터(컴패니언 컴퓨터)가 제어권을 가지며, setpoint 메시지(position, velocity, attitude 등)가 2Hz 이상으로 지속되지 않으면 Failsafe가 발동됩니다.

**팁**: MAVSDK의 offboard 예제에서 start() 전에 반드시 초기 setpoint를 전송해야 모드 전환이 됩니다.

### Q127. GPS 포지셔닝의 정확도를 향상시키기 위한 RTK(Real-Time Kinematic)의 작동 원리는?
- ✅ 기준국(Base Station)의 위상차 보정 데이터를 이동국(Rover)에 실시간 전송하여 cm급 정확도 달성
-    위성 수를 늘려 삼각측량 정확도를 높이는 방법
-    기압계와 GPS를 융합하여 수직 정확도를 향상
-    IMU 데이터로 GPS 오차를 실시간 보정

**해설**: RTK는 고정 위치의 기준국이 GPS 위상차 오차를 계산하여 Rover(드론)에 실시간으로 전송합니다. 이를 통해 일반 GPS의 미터급 오차를 1~2cm까지 줄일 수 있습니다.

**팁**: RTK Fix: 2cm 이하, RTK Float: 수십 cm, DGPS: 수 m, 일반 GPS: 2~5m 정도의 정확도 차이를 기억하세요.

### Q128. ArduPilot의 Auto 모드에서 미션을 수행할 때 WP_RADIUS 파라미터의 역할은?
- ✅ 웨이포인트를 도달한 것으로 인정하는 허용 반경 설정
-    자동 비행 시 최대 속도 제한
-    미션 포인트 간 최소 거리 설정
-    웨이포인트 선회 반경 설정

**해설**: WP_RADIUS는 기체가 웨이포인트에 얼마나 가까이 가야 '도달(reached)'로 판정하는지 설정합니다. 기본값은 2m이며, 이 반경 내에 진입하면 다음 웨이포인트로 이동합니다.

**팁**: WP_RADIUS를 너무 작게 설정하면 오버슈트로 미션이 지연되고, 너무 크면 정밀도가 떨어집니다.

### Q129. PX4에서 MC_ROLL_P 파라미터를 너무 높게 설정했을 때 나타나는 증상은?
- ✅ 기체가 좌우로 빠르게 진동(oscillation)하거나 불안정해짐
-    기체의 응답이 매우 느려짐
-    자동 착륙 속도가 빨라짐
-    배터리 소모가 증가

**해설**: Roll P 게인이 너무 높으면 과도한 보정으로 인해 오실레이션이 발생합니다. 기체가 좌우로 빠르게 떨리는 증상이 나타나며, 심하면 추락할 수 있습니다.

**팁**: PID 튜닝 시 P값을 천천히 증가시키다가 첫 오실레이션이 나타나기 직전 값의 70-80%를 사용하는 방법이 일반적입니다.

### Q130. AHRS(Attitude and Heading Reference System)가 IMU만으로는 부족한 이유는?
- ✅ 자이로스코프 드리프트 누적으로 장기 자세 추정이 불정확하기 때문
-    AHRS가 더 많은 전력을 소비하기 때문
-    IMU가 GPS 신호를 수신하지 못하기 때문
-    IMU의 샘플링 주파수가 너무 낮기 때문

**해설**: 자이로스코프는 각속도를 적분하여 자세를 추정하지만 시간이 지날수록 드리프트가 누적됩니다. AHRS는 가속도계, 자이로, 마그네토미터를 융합하여 드리프트를 보정합니다.

**팁**: Mahony, Madgwick 필터는 경량 AHRS 알고리즘으로 임베디드 시스템에서 자주 사용됩니다.

### Q131. 비행 컨트롤러에서 Mixer(믹서)의 역할은?
- ✅ Roll/Pitch/Yaw/Thrust 명령을 개별 액추에이터 출력값으로 변환
-    여러 센서 입력을 하나의 제어 신호로 합성
-    RC 입력 채널을 비행 모드에 매핑
-    PWM 신호를 DSHOT으로 변환

**해설**: Mixer는 제어 시스템이 계산한 Roll, Pitch, Yaw, Thrust 명령을 기체 형상(quadrotor, hexarotor 등)에 맞는 개별 모터 출력값으로 변환합니다.

**팁**: PX4의 Mixer 파일(.mix)은 기체별로 정의되며 Motors/Servos의 혼합 계수를 지정합니다. 최신 PX4는 Actuator allocation으로 대체 중입니다.

### Q132. Barometer(기압계)로 고도를 추정할 때 발생하는 주요 오차 원인은?
- ✅ 기상 변화, 기체 프레임 내 기압 왜곡, 온도 변화
-    GPS 신호 간섭
-    IMU 드리프트와의 상관
-    자기장 변화에 의한 오차

**해설**: 기압계는 대기압으로 고도를 추정하며 기상 변화(저기압/고기압), 프로펠러 다운워시로 인한 기압 왜곡, 온도 변화에 민감합니다. 일반적으로 ±수 m의 오차를 가집니다.

**팁**: 비행 컨트롤러에서 기압계는 EKF의 고도 추정에 사용되며, 실내에서는 광학 흐름(Optical Flow)이나 레이저로 보완합니다.

### Q133. PX4에서 Position 모드와 Altitude 모드의 차이점은?
- ✅ Position 모드는 GPS 위치 고정, Altitude 모드는 고도만 자동 유지
-    Altitude 모드가 더 많은 센서를 사용
-    Position 모드에서 GPS 없이도 작동 가능
-    Altitude 모드만 자동 착륙을 지원

**해설**: Altitude 모드는 기압계로 고도만 자동 유지하며 수평 위치는 수동 제어합니다. Position 모드는 GPS로 수평 위치와 고도를 모두 자동 유지합니다.

**팁**: GPS 고장 시 Altitude 모드로 자동 전환되는 Failsafe 설정이 일반적입니다.

### Q134. ArduCopter에서 Acro 모드의 특성은?
- ✅ 자이로 기반 rate 제어만 하며 자세 안정화 없음, 레이싱/곡예 비행용
-    완전 수동 조종으로 모든 센서 비활성화
-    자동 수평 유지와 고도 유지를 동시에 수행
-    GPS 없이 위치를 유지하는 모드

**해설**: Acro 모드는 스틱 입력이 각속도(rate) 명령으로 처리되며 자세 안정화 없이 자이로 rate 제어만 합니다. 레이싱 드론이나 에어로바틱 비행에 사용됩니다.

**팁**: Acro 모드에서는 스틱을 놓아도 기체가 기울어진 상태를 유지합니다. Stabilize 모드는 스틱 중립 시 수평으로 복귀합니다.

### Q135. PX4 Commander 모듈의 주요 역할은?
- ✅ 비행 상태 관리, 모드 전환 처리, Failsafe 로직 실행
-    모터 출력 계산 및 PWM 신호 생성
-    GPS 데이터 파싱 및 위치 추정
-    배터리 전압 모니터링 및 알림

**해설**: PX4 Commander는 차량 상태 머신을 관리합니다. Arming/Disarming, 비행 모드 전환, Failsafe 조건 감지 및 대응 동작을 담당하는 핵심 모듈입니다.

**팁**: PX4 아키텍처: Commander(상태 관리) → FlightTask(setpoint 생성) → Controller(제어) → Mixer(액추에이터 출력)

### Q136. 드론의 전자 나침반(Magnetometer) 캘리브레이션이 필요한 이유는?
- ✅ 비행 환경의 자기 간섭(모터, 배터리, 금속)이 측정값을 왜곡하기 때문
-    나침반 센서가 시간이 지나면서 마모되기 때문
-    기압 변화가 자기 센서에 영향을 주기 때문
-    GPS와 나침반 데이터의 동기화를 위해

**해설**: 모터의 자기장, 배터리 전류, 금속 프레임 등이 나침반 측정을 왜곡합니다. 캘리브레이션을 통해 Hard Iron(오프셋)과 Soft Iron(스케일 왜곡) 오차를 보정합니다.

**팁**: 나침반 캘리브레이션은 전원 완전 연결 상태(배터리+모터 전류 인가)에서 해야 실제 비행 환경에 가까운 보정이 됩니다.

### Q137. PX4의 FlightTask 프레임워크에서 각 FlightTask의 역할은?
- ✅ 특정 비행 모드에서의 setpoint(위치/속도/자세 목표값) 생성
-    센서 데이터 수집 및 전처리
-    실제 모터 출력값 계산
-    MAVLink 메시지 송수신 처리

**해설**: 각 FlightTask는 특정 비행 모드(Position, Altitude, Takeoff 등)에 대응하며 Position setpoint, Velocity setpoint, Attitude setpoint 등 제어 루프 입력값을 생성합니다.

**팁**: PX4 FlightTask 구조를 이해하면 새로운 비행 모드를 구현할 때 기존 Task를 상속받아 확장할 수 있습니다.

### Q138. 고도 제어 루프에서 Barometer와 GPS의 역할 차이는?
- ✅ Barometer는 수직 속도와 고도 피드백, GPS는 절대 고도 보정에 활용
-    GPS가 더 정확한 고도를 제공하여 항상 우선
-    Barometer는 실내에서만 사용 가능
-    GPS는 고도 추정에 사용하지 않음

**해설**: 기압계는 빠른 업데이트 속도(50~100Hz)로 수직 속도 추정에 유리합니다. GPS 고도는 노이즈가 크지만 장기 드리프트가 없어 EKF에서 보정 소스로 활용됩니다.

**팁**: GPS의 수직 정확도(~5m)는 수평 정확도(~2m)보다 낮습니다. RTK GPS는 수직도 cm급으로 개선됩니다.

### Q139. PX4 Takeoff 모드에서 자동 이륙 고도를 설정하는 파라미터는?
- ✅ MIS_TAKEOFF_ALT
-    TAKEOFF_HEIGHT
-    MC_AUTO_CLIMB
-    COM_TAKEOFF_ALT

**해설**: MIS_TAKEOFF_ALT 파라미터가 자동 이륙 목표 고도(기본 2.5m)를 설정합니다. 이 값에 도달하면 Takeoff 모드가 완료되고 Hold/Loiter로 전환됩니다.

**팁**: GCS에서 미션 첫 번째 명령으로 TAKEOFF 명령을 넣으면 이 파라미터가 기본값으로 적용됩니다.

### Q140. 모터 동적 특성에서 추력이 모터 RPM의 제곱에 비례한다는 것이 제어 설계에 미치는 영향은?
- ✅ 선형 제어기를 적용하려면 비선형 역모델(역제곱근)로 보상이 필요
-    RPM을 두 배 높이면 추력이 두 배 증가
-    추력 제어는 항상 선형 시스템으로 처리 가능
-    PID 제어는 이 비선형성을 무시해도 됨

**해설**: 추력 T ∝ ω²의 비선형 관계로 인해 스로틀 입력과 추력이 선형적이지 않습니다. PX4에서는 Motor Thrust Model을 통해 추력 → PWM 변환 시 역제곱근 보상을 적용합니다.

**팁**: THR_MDL_FAC 파라미터가 비선형 모터 모델 계수를 설정합니다. 모터 테스트 데이터로 피팅하여 더 정확한 제어가 가능합니다.

### Q141. PX4 EKF2에서 센서 퓨전 상태를 진단할 때 innovation(혁신량)의 의미와 innovation_test_ratio의 임계값 초과 시 발생하는 현상은?
- ✅ innovation은 예측값과 측정값의 차이로, 임계값 초과 시 해당 센서 측정값이 거부되고 EKF 상태 플래그가 설정됨
-    innovation은 새로운 센서 데이터가 추가될 때마다 생성되는 식별자
-    임계값 초과 시 자동으로 EKF가 재초기화됨
-    innovation_test_ratio는 GPS 정확도만을 나타내는 지표

**해설**: Kalman Filter에서 innovation(잔차)은 실제 측정값과 예측값의 차이입니다. innovation_test_ratio = innovation² / (innovation_variance * gate_threshold²)가 1.0을 초과하면 이상치(outlier)로 판단하여 센서 업데이트를 거부합니다. estimator_status 토픽에서 확인 가능합니다.

**팁**: EKF2 진단 시 QGC의 Analyse → MAVLink Inspector에서 ESTIMATOR_STATUS 메시지의 각 sensor flag를 확인하세요.

### Q142. PX4에서 멀티콥터 위치 제어 루프의 계층 구조를 올바르게 나열한 것은?
- ✅ Position Error → Position P → Velocity Setpoint → Velocity PID → Acceleration Setpoint → Attitude Setpoint → Rate PID → Motor Output
-    Rate PID가 각속도 오차를 루프 제어 → Velocity PID가 속도 setpoint 추종·보정 → Position P가 위치 오차를 velocity setpoint로 변환 처리 → Motor Output
-    IMU 원시 측정값 → EKF 상태 추정 필터(3축 위치·속도·자세 동시 추정 처리) → 위치-속도-자세 3중 계층 PID 통합 루프 전체 처리 → Mixer 신호 분배 → Motor Output
-    Position Setpoint 입력 → Attitude Controller(P)가 각도 명령 생성 → Rate PID가 각속도 제어 루프 → Thrust/Torque 계산 분배 → Motor Output

**해설**: PX4 MC 위치 제어는 외부 루프(Position P Controller)가 위치 오차를 속도 setpoint로 변환, 내부 루프(Velocity PID)가 속도 오차를 가속도/추력 setpoint로 변환, 이후 자세 컨트롤러와 레이트 컨트롤러를 거쳐 최종 모터 출력이 계산됩니다.

**팁**: 각 루프의 업데이트 주기: Position(50Hz), Velocity(50Hz), Attitude(250Hz), Rate(1kHz). 내부 루프일수록 빠릅니다.

### Q143. Bidirectional DSHOT에서 eRPM 텔레메트리를 수신하여 RPM 기반 노치 필터를 구현하면 얻을 수 있는 이점은?
- ✅ 모터 불균형으로 인한 특정 주파수 진동을 실시간으로 추적하여 동적 노치 필터로 억제함으로써 자이로 노이즈 감소
-    배터리 수명 연장 및 비행 시간 증가
-    GPS 정확도 향상
-    EKF 수렴 속도 향상

**해설**: 각 모터의 eRPM으로부터 진동 주파수를 계산하고 동적 노치 필터(Dynamic Notch Filter)의 중심 주파수를 실시간으로 조정합니다. 이를 통해 자이로 측정 노이즈를 줄이고 PID 제어 성능이 향상됩니다.

**팁**: PX4의 IMU_GYRO_DNF_EN 파라미터로 활성화하며, Betaflight에서 먼저 도입한 기능으로 레이싱 드론에서 큰 효과가 있습니다.

### Q144. PX4에서 vtol_type 파라미터에서 QuadChute 기능이 동작하는 조건과 그 결과는?
- ✅ 고정익 모드에서 실속(stall) 또는 기울기 임계값 초과 시 자동으로 멀티로터 모드로 전환하여 추락 방지
-    배터리 부족 시 VTOL이 자동 착륙하는 기능
-    QuadChute는 고정익 이륙 시 쿼드 모터를 보조하는 기능
-    VTOL이 수직 이착륙 모드로 전환하는 일반 과정

**해설**: QuadChute는 VTOL 고정익 비행 중 예상치 못한 실속이나 과도한 롤/피치 각도(VTOL_FW_QC_R, VTOL_FW_QC_P) 감지 시 자동으로 멀티로터 모드로 전환하는 안전 기능입니다.

**팁**: VTOL_FW_QC_ALTL 파라미터로 QuadChute 활성화 최소 고도를 설정합니다. 지면 근처에서는 전환보다 착륙이 더 안전할 수 있습니다.

### Q145. 비행 컨트롤러에서 Optical Flow 센서를 사용할 때 EKF에 입력되는 데이터의 형태와 정확도에 영향을 주는 요인은?
- ✅ 픽셀 이동 속도(rad/s)와 고도를 결합한 속도 추정값이 입력되며, 센서 고도 정확도와 이미지 품질, 조명 조건이 정확도에 영향
-    직접 위치값으로 입력되며 GPS와 동일한 정확도
-    각속도 데이터만 제공하여 IMU를 대체
-    Optical Flow는 고도 추정에 특화된 센서

**해설**: Optical Flow는 이미지 픽셀의 이동 속도(angular velocity)를 측정합니다. 속도 = 픽셀 속도 × 고도로 계산되므로 고도 정확도가 핵심입니다. 균일한 텍스처 부족, 낮은 조명, 빠른 이동 시 정확도가 저하됩니다.

**팁**: PX4 EKF2_OF_CTRL 파라미터로 Optical Flow 융합을 활성화하며, 반드시 Range Finder(거리 센서)와 함께 사용해야 정확도가 보장됩니다.

### Q146. PX4 Auto 미션에서 MISSION_ITEM_REACHED와 MISSION_CURRENT 메시지가 각각 발생하는 시점의 차이는?
- ✅ MISSION_CURRENT는 현재 진행 중인 웨이포인트 번호를 지속 발송, MISSION_ITEM_REACHED는 WP 도달 시 1회만 발송
-    두 메시지는 동시에 발생하며 내용이 동일
-    MISSION_ITEM_REACHED가 항상 먼저 발생
-    MISSION_CURRENT는 자동 이륙 완료 시에만 발생

**해설**: MISSION_CURRENT(#42)는 현재 진행 중인 미션 아이템 seq 번호를 포함하며 상태 변경 시 발송됩니다. MISSION_ITEM_REACHED(#46)는 각 웨이포인트에 도달했을 때 한 번 발송되는 이벤트성 메시지입니다.

**팁**: GCS에서 미션 진행 상황을 모니터링할 때는 두 메시지를 함께 구독하여 현재 목표(CURRENT)와 완료 이벤트(REACHED)를 구분하세요.

### Q147. ArduPilot의 Harmonic Notch Filter가 해결하는 문제와 구현 방식은?
- ✅ 모터 회전에서 발생하는 RPM 기반 고조파 진동을 추적하여 자이로 노이즈를 제거하며, 기본 주파수와 그 배수(고조파)를 동적으로 필터링
-    IMU 드리프트를 주기적으로 보정하는 캘리브레이션 필터
-    GPS 신호의 다중 경로 간섭을 제거하는 안테나 필터
-    RC 신호의 고주파 노이즈를 제거하는 저역 통과 필터

**해설**: Harmonic Notch는 모터 RPM의 1배(기본), 2배, 3배 고조파 주파수에 각각 노치 필터를 적용합니다. ESC 텔레메트리나 배터리 전압으로 추정된 RPM을 기반으로 필터 중심 주파수가 동적으로 조정됩니다.

**팁**: ArduPilot INS_HNTCH_ENABLE=1 설정 후 INS_HNTCH_FREQ, INS_HNTCH_BW, INS_HNTCH_ATT로 세부 조정합니다.

### Q148. 멀티콥터의 Motor Failure Mitigation에서 모터 1개 고장 시 쿼드콥터와 헥사콥터의 대응 방식 차이는?
- ✅ 쿼드콥터는 모터 1개 고장 시 제어 불능(대각선 모터도 출력 조정 불가), 헥사콥터는 나머지 5개 모터 재배분으로 제한적 비행 유지
-    두 기체 모두 모터 1개 고장 시 자동 착륙만 가능
-    쿼드콥터가 더 많은 모터 고장을 허용
-    헥사콥터는 모터 고장 감지 기능이 없음

**해설**: 쿼드콥터(4개 모터)는 한 모터 고장 시 토크 균형이 불가능하여 제어를 잃습니다. 헥사콥터(6개 모터)는 모터 1개 고장 시 대각선 모터도 감소시켜 불균형 토크를 상쇄하고 제한적 기동으로 안전하게 착륙할 수 있습니다.

**팁**: 방산 드론의 신뢰성 요구사항에서 모터 이중화를 위해 옥토콥터(8개)를 사용하는 경우도 있습니다.

### Q149. PX4에서 mag_declination(자기 편각) 보정을 적용하지 않으면 어떤 문제가 발생하는가?
- ✅ 나침반이 지리적 북쪽 대신 자기 북쪽을 가리켜 경도 방향 위치 오차와 항법 경로 편차 발생
-    고도 측정이 부정확해짐
-    모터 출력이 불균형해짐
-    GPS 수신 감도가 저하됨

**해설**: 자기 편각은 자기 북쪽과 지리적 북쪽 사이의 각도 차이입니다. 서울 기준 약 8° 서편각이 있으며 보정하지 않으면 EKF의 yaw 추정에 오차가 생겨 자동 비행 시 경로 편차가 발생합니다.

**팁**: PX4의 CAL_MAG_DECL 파라미터로 수동 설정하거나, GPS 신호 유효 시 자동 계산됩니다. 지역별 편각은 NOAA WMM 모델을 참조하세요.

### Q150. 비행 컨트롤러에서 NuttX RTOS를 사용하는 PX4의 태스크 우선순위 설계 원칙과 실시간성 보장 방법은?
- ✅ 센서/IMU 태스크가 최고 우선순위(255), 제어 루프가 높은 우선순위, 통신/로깅이 낮은 우선순위로 설계하며 선점형 스케줄링으로 실시간성 보장
-    모든 태스크가 동일 우선순위로 라운드로빈 실행
-    NuttX는 실시간 스케줄링을 지원하지 않아 별도 타이머 필요
-    우선순위 역전 방지를 위해 모든 태스크가 동일 우선순위 사용

**해설**: PX4는 NuttX POSIX API를 사용하며 IMU 처리(250-1000Hz), 자세 제어, 위치 제어, 믹서 순으로 높은 우선순위를 부여합니다. Priority Inheritance Mutex로 우선순위 역전을 방지합니다.

**팁**: PX4에서 px4_task_spawn_cmd() 또는 SCHED_PRIORITY_DEFAULT 매크로를 이용하여 태스크 우선순위를 설정합니다.

### Q151. ArduPilot의 terrain following 기능을 사용할 때 필요한 조건과 데이터 소스는?
- ✅ 지형 데이터(SRTM 등)를 SD카드에 저장하거나 GCS로부터 MAVLink TERRAIN_DATA로 수신, 레인지파인더 또는 Radar Altimeter 보완 사용
-    SRTM 지형 데이터를 GCS TERRAIN_CHECK 메시지로 요청하고 MAVLink TERRAIN_DATA 응답을 SD카드 캐시에 저장하여 항로 고도 보정에 사용
-    레인지파인더가 실시간 지형 고도를 측정하여 TERRAIN_REPORT로 GCS에 전달하고 FC는 이 데이터로 비행 계획 고도를 연속 보정하며 운용
-    테레인 팔로잉은 고정익과 쿼드플레인에만 지원되며 멀티콥터에서는 TERRAIN_ENABLE 파라미터가 1로 설정되어도 고도 추종 기능이 비활성화됨

**해설**: Terrain Following은 SRTM 1초 분해능(~30m 격자) 지형 데이터를 기반으로 고도를 조절합니다. 데이터는 SD카드 또는 GCS가 MAVLink TERRAIN_REQUEST에 응답하여 공급합니다. 레인지파인더와 병행 시 정확도가 향상됩니다.

**팁**: TERRAIN_ENABLE=1 파라미터 설정 후 Mission Planner의 Grid Load 기능으로 미션 경로 지형 데이터를 미리 다운로드할 수 있습니다.

### Q152. PX4 Commander에서 Geofence 위반 감지 시 동작하는 Failsafe 처리 흐름은?
- ✅ GF_ACTION 파라미터 값에 따라 경고/Hold/RTL/종료 중 하나를 실행하며, 복수 Failsafe 동시 발생 시 가장 심각한 처리를 우선 적용
-    모든 Geofence 위반에서 즉시 모터 꺼짐(Disarm)
-    Geofence는 경고만 하고 자동 복귀 기능 없음
-    GCS에서 수동 명령 없이는 Geofence Failsafe가 자동 실행 불가

**해설**: GF_ACTION=0은 경고만, 1은 Hold, 2는 RTL, 3은 종료(착륙)입니다. 배터리 Failsafe, RC 손실, Geofence 등 복수 조건 동시 발생 시 PX4 Failsafe 우선순위 규칙에 따라 처리됩니다.

**팁**: Geofence는 다각형 구역, 최대 고도, 최대 반경 세 가지를 설정할 수 있으며 각각 독립적인 위반 조건으로 동작합니다.

### Q153. PX4 Actuator Effectiveness Matrix(할당 행렬)의 역할과 Over-actuated 시스템에서의 의사역행렬(Pseudo-inverse) 활용은?
- ✅ 원하는 힘/토크 벡터를 각 액추에이터 입력으로 분배하는 행렬로, 액추에이터 수가 자유도보다 많은 경우 최소 노름 해를 구하는 의사역행렬 사용
-    단순히 모터 번호와 물리적 위치를 매핑하는 테이블
-    믹서 파일을 자동 생성하기 위한 GUI 입력 데이터
-    고정익에서만 사용하는 서보 혼합 알고리즘

**해설**: B_matrix(effectiveness)는 각 액추에이터가 시스템 제어 입력(Roll/Pitch/Yaw/Thrust)에 기여하는 비율입니다. 헥사콥터처럼 액추에이터 수(6)가 DOF(4)보다 많으면 Moore-Penrose 의사역행렬로 최소 에너지 해를 계산합니다.

**팁**: PX4에서 Airframe/Actuator 탭에서 Effectiveness Matrix를 시각적으로 확인할 수 있습니다.

### Q154. RC 링크 손실 Failsafe에서 COM_RC_IN_MODE=1(RC 없이도 동작) 설정이 필요한 상황은?
- ✅ 컴패니언 컴퓨터나 GCS만으로 운용하는 완전 자율 비행 시스템에서 RC 미연결 상태를 정상으로 처리하기 위해
-    RC 컨트롤러의 배터리 절약을 위한 절전 모드
-    군집 드론에서 리더 기체가 팔로워에게 RC 신호를 중계하는 경우
-    HITL 시뮬레이션에서 RC를 가상으로 에뮬레이션하는 경우

**해설**: 완전 자율 시스템이나 컴패니언 컴퓨터 기반 운용에서는 RC 수신기 자체가 없을 수 있습니다. COM_RC_IN_MODE=1 설정으로 RC 신호 없음 상태를 Failsafe로 처리하지 않고 정상 동작을 유지합니다.

**팁**: 방산용 자율 드론은 RC 없이 MAVLink GCS 명령만으로 운용되는 경우가 많으므로 이 설정이 중요합니다.

### Q155. PX4의 System Identification(시스템 식별)을 위한 Accel/Gyro 주파수 응답 분석에서 Anti-aliasing 필터 컷오프 주파수 설정의 중요성은?
- ✅ 샘플링 주파수의 절반(나이퀴스트 주파수) 이하로 설정해야 앨리어싱 없이 진동 특성을 정확히 분석할 수 있음
-    컷오프를 낮출수록 응답이 빠른 시스템 설계 가능
-    Anti-aliasing은 소프트웨어로 보정 가능하여 하드웨어 필터 불필요
-    필터 컷오프는 배터리 전압에 따라 자동 조정

**해설**: 1kHz로 샘플링할 때 나이퀴스트 주파수는 500Hz이므로 Anti-aliasing 필터를 500Hz 이하로 설정해야 합니다. 너무 낮게 설정하면 빠른 진동 성분이 손실되어 PID 튜닝에 필요한 정보를 놓칩니다.

**팁**: PX4의 IMU_GYRO_CUTOFF, IMU_DGYRO_CUTOFF 파라미터로 소프트웨어 저역 통과 필터 컷오프를 설정합니다.

### Q156. 고도 800m 이상에서 MEMS 기압계의 고도 측정 정확도에 영향을 주는 요인과 대응 방법은?
- ✅ 온도 감소로 인한 온도 보상 오차 증가, 대기 밀도 변화로 인한 고도-기압 모델 오차가 발생하며 RTK GPS 고도 융합으로 보완
-    고도가 높아질수록 기압계 정확도는 오히려 향상됨
-    MEMS 기압계는 고도에 무관하게 일정한 오차를 가짐
-    800m 이상에서는 기압계를 사용하지 않고 IMU만으로 고도 추정

**해설**: 고도가 높아지면 기온이 낮아져 MEMS 센서의 온도 보상 범위를 벗어날 수 있습니다. 또한 국제표준대기(ISA) 모델과 실제 대기의 차이가 커져 오차가 증가합니다. 정밀 운용 시 RTK GPS 고도와 융합하거나 기상 데이터를 활용합니다.

**팁**: 군용 드론의 고고도 임무에서는 레이더 고도계(Radar Altimeter)를 추가로 탑재하여 AGL(Above Ground Level) 고도를 측정합니다.

### Q157. PX4에서 log_mode 파라미터 설정에 따른 비행 로그 기록 전략과 포렌식 분석을 위한 최적 설정은?
- ✅ SDLOG_MODE=0: Arming 시 시작, SDLOG_MODE=-1: 부팅 시 시작(Pre-arming 센서 이상 감지 가능). 포렌식에는 -1이 유리
-    모든 로그 모드에서 동일한 데이터가 기록됨
-    SDLOG_MODE=2 이상부터 고해상도 IMU 데이터 기록
-    로그 모드는 비행 시간에만 영향을 주며 데이터 내용에는 무관

**해설**: SDLOG_MODE=-1은 부팅 즉시 로깅을 시작하여 Arm 이전 센서 캘리브레이션, EKF 초기화, 시스템 부팅 과정을 모두 기록합니다. 사고 원인 분석(포렌식) 시 Pre-arm 오류를 추적하는 데 필수입니다.

**팁**: Flight Review(logs.px4.io)에서 ulog 파일을 업로드하면 자동으로 진동, 모터 밸런스, EKF 상태 등을 분석해 줍니다.

### Q158. Wind Estimation과 관련하여 PX4에서 바람 속도를 추정하는 방법과 이것이 Position Mode 제어에 미치는 영향은?
- ✅ GPS 지상 속도와 Airspeed 센서 측정값(또는 EKF 추정 대기 속도)의 벡터 차이로 바람 추정, 위치 제어기에서 feedforward 보상으로 활용
-    GNSS 지상 속도와 EKF 예측 속도의 벡터 차를 사용하지 않고, 기압계 수직 속도 변화로만 바람 세기를 간접 추정하여 활용
-    광류(Optical Flow) 센서의 픽셀 이동 패턴에서 바람 방향을 추정하고, 추력 편차 보정에 단독 활용하는 방식으로 동작
-    EKF2가 바람을 추정하더라도 멀티콥터 위치 제어기는 이를 사용하지 않고 GPS 위치 오차 보정에만 내부적으로 활용하므로 제어 성능에 영향이 없다

**해설**: 멀티콥터에서 EKF2는 GNSS 지상 속도와 기체의 예상 이동 속도 차이로 바람을 추정합니다. 추정된 바람 속도는 위치 제어기에서 feedforward 항으로 활용하여 바람 방향으로의 자세 기울기를 사전 보상합니다.

**팁**: EKF2_WIND_NOISE 파라미터로 바람 추정 모델의 프로세스 노이즈를 조정합니다. 바람 변화가 빠른 환경에서는 값을 높여 추정 반응성을 높입니다.

### Q159. 방산 드론 시스템에서 Anti-Jamming GPS(항재밍 GPS)의 기술적 원리는?
- ✅ Null-steering Antenna Array(배열 안테나)로 방해 신호 방향을 향해 방사 패턴 null을 형성하거나, FHSS/DSSS 스펙트럼 확산 기법으로 재밍 내성 확보
-    Controlled Reception Pattern Antenna(CRPA)가 위성 방향으로 수신 이득을 집중하고 재밍 신호는 소프트웨어 알고리즘으로 실시간 필터링하여 제거
-    GPS 재밍 감지 시 INS 단독 모드로 전환하고 시간 기반 데드레코닝으로 비행을 지속하며, 재밍 해제 후 GPS와 INS 추정값 간 오차를 보정하여 항법 복구
-    지향성 안테나(Directional Antenna)가 GPS 위성 방향으로만 신호를 수신하고 GNSS 수신기 내부 오류 검출 알고리즘으로 재밍 신호를 자동 보정

**해설**: 배열 안테나 방식(CRPA)은 간섭 신호 방향으로 수신 패턴 null을 형성하여 재밍을 억제합니다. 군용 GPS(P(Y) 코드)는 DSSS로 민간 신호보다 재밍에 강합니다. INS(관성항법)와의 복합 항법도 핵심 안티재밍 전략입니다.

**팁**: GPS 재밍 환경에서 INS/Visual Navigation/Terrain Matching으로 항법을 유지하는 복합 항법(Integrated Navigation) 개념은 방산 드론 면접의 단골 주제입니다.

### Q160. PX4에서 MC_AT(Automatic Tuning) 기능의 작동 원리와 기존 수동 PID 튜닝 대비 장단점은?
- ✅ 계단(step) 입력에 대한 시스템 응답을 분석하여 주파수 응답 특성을 추출하고 목표 대역폭 기반으로 PID 게인을 자동 계산. 빠르지만 비선형/복잡한 기체에서는 수동 조정 필요
-    무작위 기동 비행 중 IMU 응답 데이터를 기록하고 오프라인 최적화 알고리즘으로 Rate/Attitude PID 게인 세트를 자동 계산하여 파라미터에 저장
-    기체 물리 모델을 기반으로 Ziegler-Nichols 방법을 자동 적용하여 Rate/Attitude 루프 전체를 순서대로 최적 PID 게인으로 설정
-    MC_AT는 Rate 루프를 계단 응답 분석으로 자동 계산하고 Attitude 루프는 고정 비율 스케일링을 적용하며 Position 루프는 수동 조정이 필요

**해설**: PX4 MC_AT는 정해진 각속도 step 입력 시퀀스를 자동 실행하고 응답을 기록합니다. 주파수 도메인 분석으로 개루프 특성을 추정하고 목표 폐루프 대역폭(MC_AT_BW_XY 파라미터)에 맞는 PID 게인을 계산합니다. 표준적인 기체에는 효과적이나 특수 형상 기체나 비선형 특성이 강한 경우 수동 검증이 필요합니다.

**팁**: 자동 튜닝 후 반드시 낮은 고도에서 소폭 기동으로 검증하고 필요 시 미세 조정하세요. 완전히 새로운 기체에 처음부터 MC_AT만 믿는 것은 위험합니다.

