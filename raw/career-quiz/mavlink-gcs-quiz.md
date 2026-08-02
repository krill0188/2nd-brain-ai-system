---
source: "career-bot/store/questions.json#MAVLink/GCS"
ingested: 2026-08-02
captured: 2026-08-02
type: quiz-compilation
evidence_tier: non-primary-reconstruction
category: "MAVLink/GCS"
question_count: 61
author: "DroneAI Lab 커리어 문항은행 (비공개 실무자 재구성)"
sha256: "76984ebe28a3f8dbf92b544ce46eb228379b5b830511a920d5d88c0a319a41a5"
tags: [career, quiz, mavlink-gcs-quiz]
---

# MAVLink/GCS — 커리어 대비 퀴즈 재구성 컴필레이션 (61문항)

> ⚠️ **비-1차-증거 고지**: 이 문서는 방산/드론/AI 커리어 대비용으로 재구성된
> 객관식 퀴즈 모음이다. 각 항목에 원출처 인용이 없으므로 `research/` AI
> 연구 루프의 Retriever/Verifier는 이 문서를 **1차 증거(raw evidence)로
> 취급해서는 안 된다**. Critic/Verifier가 근거로 인용할 경우 반드시
> `verification_status: insufficient_evidence`로 처리하고, 별도의 1차
> 출처(GitHub/arXiv/공식문서 등)로 교차검증한 뒤에만 canonical 승격
> 대상이 될 수 있다. 정답/해설은 원저작자(DroneAI Lab 내부 실무자)의 실무 지식
> 재구성이며 공식 표준 문서가 아니다.

**원본**: `career-bot/store/questions.json` (id 범위: 11–210)
**난이도 분포**: easy=12, hard=19, medium=30

## 문항

### Q11. MAVLink v2의 최대 페이로드 크기는?
- ✅ 255 bytes
-    128 bytes
-    512 bytes
-    1024 bytes

**해설**: MAVLink v2는 최대 255바이트 페이로드를 지원합니다. v1은 최대 255바이트로 동일하지만, v2는 확장 기능(서명 등)을 추가했습니다.

**팁**: MAVLink 패킷 구조(STX, LEN, SEQ, SYS, COMP, MSG ID, PAYLOAD, CRC)를 외워두세요.

### Q12. 드론을 Arm하는 MAVLink 메시지는?
- ✅ COMMAND_LONG (MAV_CMD_COMPONENT_ARM_DISARM)
-    SET_MODE
-    HEARTBEAT
-    MANUAL_CONTROL

**해설**: COMMAND_LONG 메시지에 MAV_CMD_COMPONENT_ARM_DISARM(#400) 커맨드를 담아 전송합니다. param1=1이면 Arm, 0이면 Disarm.

**팁**: COMMAND_LONG의 파라미터 구조와 ACK 처리 흐름을 설명할 수 있으면 좋습니다.

### Q13. HEARTBEAT 메시지에 포함되지 않는 정보는?
- ✅ GPS 좌표
-    시스템 타입
-    비행 모드
-    시스템 상태

**해설**: HEARTBEAT에는 type, autopilot, base_mode, custom_mode, system_status가 포함됩니다. GPS 좌표는 GLOBAL_POSITION_INT 메시지로 전송됩니다.

**팁**: HEARTBEAT의 역할(연결 유지, 시스템 식별)과 1Hz 전송 규칙을 강조하세요.

### Q14. MAVLink 미션 업로드 프로토콜의 올바른 순서는?
- ✅ COUNT → REQUEST → ITEM → ACK
-    ITEM → COUNT → ACK → REQUEST
-    ACK → ITEM → REQUEST → COUNT
-    REQUEST → ITEM → COUNT → ACK

**해설**: GCS가 MISSION_COUNT 전송 → FC가 MISSION_REQUEST로 각 항목 요청 → GCS가 MISSION_ITEM 전송 → FC가 MISSION_ACK로 완료 확인.

**팁**: 이 핸드셰이크 프로토콜의 신뢰성 보장 메커니즘(재전송, 타임아웃)도 알아두세요.

### Q15. MAVLink signing의 목적은?
- ✅ 메시지 인증 및 변조 방지
-    데이터 압축
-    전송 속도 향상
-    암호화

**해설**: MAVLink v2 signing은 SHA-256 기반 서명으로 메시지의 출처를 인증하고 변조를 탐지합니다. 암호화는 아닙니다(내용은 평문).

**팁**: 서명(Authentication)과 암호화(Encryption)의 차이를 명확히 구분하세요.

### Q16. MAVLink v1과 v2의 메시지 ID 크기 차이는?
- ✅ v1: 8bit(256개), v2: 24bit(16M개)
-    v1: 16bit, v2: 32bit
-    v1: 4bit, v2: 8bit
-    차이 없음

**해설**: v1은 8비트 MSG ID로 최대 256개 메시지만 지원했고, v2는 24비트로 약 1,600만 개의 메시지 타입을 지원합니다.

**팁**: v2로의 마이그레이션 이유와 하위 호환성 처리 방법을 설명하세요.

### Q17. COMMAND_LONG과 COMMAND_INT의 차이는?
- ✅ COMMAND_INT는 좌표를 int32로 정밀 전달
-    COMMAND_INT는 더 빠름
-    COMMAND_LONG이 좌표 전용
-    차이 없음

**해설**: COMMAND_INT는 위도/경도를 int32(1e7 스케일)로 전달하여 float의 정밀도 손실을 방지합니다. 좌표 관련 명령에 권장됩니다.

**팁**: float32의 정밀도 한계(약 7자리)로 인한 GPS 좌표 오차 문제를 구체적 수치로 설명하세요.

### Q18. 다중 GCS 환경에서 드론 제어권을 관리하는 방법은?
- ✅ SYS_ID/COMP_ID로 식별, 제어 우선순위 설정
-    불가능
-    IP 주소로 구분
-    시간순 우선

**해설**: 각 GCS와 드론은 고유한 SYS_ID와 COMP_ID를 가지며, 제어 우선순위와 권한 레벨로 다중 GCS 상황을 관리합니다.

**팁**: 실제 다중 GCS 운용 경험(예: 비행 GCS + 페이로드 GCS)을 사례로 들면 좋습니다.

### Q19. 텔레메트리 전송 주기(rate)를 최적화하는 방법은?
- ✅ 메시지별 rate 조정 (REQUEST_DATA_STREAM)
-    모든 메시지를 최대 속도로
-    텔레메트리 비활성화
-    고정 rate만 사용

**해설**: REQUEST_DATA_STREAM 또는 SET_MESSAGE_INTERVAL로 메시지별 전송 주기를 개별 조정하여 대역폭을 효율적으로 사용합니다.

**팁**: 군집 환경에서의 텔레메트리 대역폭 분배 전략을 설명할 수 있으면 차별화됩니다.

### Q20. MAVLink FTP의 주요 용도는?
- ✅ 비행 로그 파일 원격 다운로드
-    실시간 영상 전송
-    펌웨어 업로드
-    모터 제어

**해설**: MAVLink FTP 프로토콜로 FC의 SD카드에 저장된 비행 로그(.ulg)를 텔레메트리 링크를 통해 원격으로 다운로드할 수 있습니다.

**팁**: 로그 분석(Flight Review, PlotJuggler)과 연계한 디버깅 워크플로우를 설명하세요.

### Q72. MAVLink 메시지의 CRC Extra 바이트 목적은?
- ✅ 메시지 정의 버전 불일치 탐지
-    암호화
-    압축
-    라우팅

**해설**: CRC Extra는 메시지 정의(필드 구성)의 해시값으로, 송수신 측의 메시지 정의 버전이 다를 때 이를 탐지하여 잘못된 파싱을 방지합니다.

**팁**: MAVLink XML 정의 파일과 코드 생성(mavgenerate) 프로세스를 설명하세요.

### Q161. MAVLink 메시지에서 HEARTBEAT 메시지의 주요 역할은?
- ✅ 기체의 생존 신호 및 현재 상태(비행 모드, Arming 상태)를 주기적으로 전송
-    모터 출력 명령을 GCS에 전달
-    GPS 위치 데이터를 실시간 스트리밍
-    파라미터 변경 확인 응답

**해설**: HEARTBEAT(#0) 메시지는 1Hz로 전송되며 기체가 활성 상태임을 알리고 type, autopilot, base_mode, custom_mode, system_status 필드로 현재 상태를 전달합니다.

**팁**: GCS는 HEARTBEAT 수신이 3초 이상 없으면 링크 손실로 판단합니다. GCS도 드론에게 HEARTBEAT를 전송해야 합니다.

### Q162. MAVLink v1과 v2의 가장 큰 차이점은?
- ✅ v2는 메시지 서명(Signing) 지원과 255 바이트 이상의 페이로드 확장 지원
-    v2는 v1보다 더 빠른 전송 속도
-    v1은 암호화를 지원하고 v2는 지원하지 않음
-    v2는 TCP 전용이고 v1은 UDP 전용

**해설**: MAVLink v2는 서명(인증) 기능 추가, 255 바이트를 초과하는 대형 메시지 지원, 컴포넌트 확장성 개선이 핵심 변경사항입니다. v1과의 하위 호환성을 유지합니다.

**팁**: MAVLink v2 헤더는 10바이트(v1은 6바이트)이며 magic byte가 0xFD(v1은 0xFE)입니다.

### Q163. MAVLink에서 System ID와 Component ID의 역할은?
- ✅ System ID는 기체(드론/GCS) 식별, Component ID는 동일 기체 내 컴포넌트(FC/카메라/짐벌) 식별
-    System ID는 메시지 우선순위, Component ID는 전송 채널 식별
-    두 ID 모두 암호화 키로 사용
-    System ID는 IP 주소, Component ID는 포트 번호에 해당

**해설**: MAVLink 네트워크에서 System ID(1~255)는 기체를 구별하고, Component ID(1~255)는 같은 기체 내 FC, 카메라, 짐벌 등을 구별합니다. GCS는 보통 sysid=255, compid=190을 사용합니다.

**팁**: 군집 드론에서는 각 기체가 고유한 System ID를 가져야 합니다. SYSID_THISMAV 파라미터로 설정합니다.

### Q164. COMMAND_LONG 메시지의 용도는?
- ✅ 기체에 명령을 전송하며 COMMAND_ACK로 실행 결과를 확인
-    텔레메트리 데이터를 실시간 스트리밍
-    파라미터 값을 읽고 쓰기
-    웨이포인트 좌표를 전송

**해설**: COMMAND_LONG(#76)은 MAV_CMD 열거형에 정의된 명령(이륙, 착륙, RTL, 모드 변경 등)을 기체에 전송합니다. 기체는 명령 수행 후 COMMAND_ACK로 결과(SUCCESS/FAIL)를 응답합니다.

**팁**: COMMAND_INT(#75)는 위치 관련 명령에 더 정밀한 정수형 좌표를 사용합니다. GPS 좌표를 포함하는 명령에는 COMMAND_INT가 권장됩니다.

### Q165. QGroundControl(QGC)에서 드론과 통신하기 위한 기본 연결 방식이 아닌 것은?
- ✅ 블루투스 LE(BLE) 직접 연결
-    USB/Serial
-    UDP(WiFi/이더넷)
-    TCP

**해설**: QGC는 Serial, UDP, TCP 연결을 지원하지만 Bluetooth LE 직접 MAVLink 연결은 기본 지원하지 않습니다. 일부 기체에서 컴패니언 앱으로 BLE를 사용하지만 QGC 표준 기능이 아닙니다.

**팁**: QGC 연결 설정에서 UDP 14550 포트가 기본 멀티캐스트 설정으로 SITL 시뮬레이터와 바로 연결됩니다.

### Q166. MAVLink MISSION_ITEM_INT 메시지에서 frame 필드의 역할은?
- ✅ 좌표계 참조 프레임 지정 (MAV_FRAME_GLOBAL_RELATIVE_ALT 등)
-    메시지의 순서 번호
-    미션 아이템의 실행 순서 우선순위
-    좌표 정밀도 설정

**해설**: frame 필드는 좌표 해석 방식을 지정합니다. MAV_FRAME_GLOBAL(절대 고도), MAV_FRAME_GLOBAL_RELATIVE_ALT(홈 포인트 기준 상대 고도), MAV_FRAME_LOCAL_NED 등을 선택합니다.

**팁**: 대부분의 웨이포인트 미션에서 MAV_FRAME_GLOBAL_RELATIVE_ALT를 사용하여 홈 포인트 이륙 위치 기준 상대 고도로 설정합니다.

### Q167. 텔레메트리 라디오(3DR 또는 SiK 기반)의 기본 전송 속도와 MAVLink 스트림 설정의 관계는?
- ✅ 낮은 텔레메트리 대역폭(57.6kbps)에서는 스트림 속도를 낮게 설정하여 패킷 손실 방지 필요
-    텔레메트리 대역폭에 무관하게 항상 최대 속도로 스트림
-    MAVLink는 UDP만 사용하므로 시리얼 대역폭과 무관
-    스트림 속도는 배터리 잔량에 따라 자동 조정

**해설**: SiK 텔레메트리는 57.6kbps 대역폭을 가지며, 모든 MAVLink 스트림을 높은 속도로 설정하면 대역폭 포화로 패킷 손실이 발생합니다. SR0_POSITION, SR0_EXTRA1 등 스트림 속도를 적절히 조정해야 합니다.

**팁**: ArduPilot에서 SR0_* 파라미터로 각 텔레메트리 포트의 스트림 속도를 개별 설정할 수 있습니다.

### Q168. QGC에서 비행 중 실시간으로 확인 가능한 주요 텔레메트리 데이터가 아닌 것은?
- ✅ 모터 내부 베어링 온도
-    GPS 위치 및 위성 수
-    배터리 전압 및 잔량
-    비행 모드 및 Arming 상태

**해설**: 모터 베어링 온도는 표준 MAVLink 텔레메트리에 포함되지 않습니다. GPS, 배터리, 비행 모드, 자세(Roll/Pitch/Yaw), 고도, 속도 등은 기본 텔레메트리로 실시간 확인됩니다.

**팁**: ESC 텔레메트리(온도, 전류, RPM)는 Bidirectional DSHOT 또는 ESC_STATUS MAVLink 메시지로 전송 가능합니다.

### Q169. MAVLink 파라미터 프로토콜에서 PARAM_REQUEST_LIST 메시지의 역할은?
- ✅ 기체의 모든 파라미터를 PARAM_VALUE 메시지로 전송하도록 요청
-    특정 파라미터 하나의 값을 요청
-    파라미터 값을 변경하는 명령
-    파라미터 저장(SD카드 쓰기) 명령

**해설**: PARAM_REQUEST_LIST는 기체가 보유한 모든 파라미터를 순차적으로 PARAM_VALUE 메시지로 전송하도록 요청합니다. 첫 연결 시 GCS가 파라미터 목록을 동기화할 때 사용합니다.

**팁**: 파라미터가 수백~수천 개이므로 전체 동기화는 시간이 걸립니다. 특정 파라미터만 필요하면 PARAM_REQUEST_READ 사용을 권장합니다.

### Q170. GCS에서 드론에 RTL(Return to Launch) 명령을 전송할 때 사용하는 MAV_CMD는?
- ✅ MAV_CMD_NAV_RETURN_TO_LAUNCH (20)
-    MAV_CMD_NAV_LAND (21)
-    MAV_CMD_DO_GO_HOME (500)
-    MAV_CMD_NAV_WAYPOINT (16)

**해설**: MAV_CMD_NAV_RETURN_TO_LAUNCH(#20)는 기체가 이륙 지점(홈 포인트)으로 돌아오도록 명령합니다. COMMAND_LONG 메시지로 전송하며 param1~7은 일반적으로 0으로 설정합니다.

**팁**: RTL 고도는 RTL_ALT(ArduPilot) 또는 RTL_DESCEND_ALT/RTL_LAND_DELAY(PX4) 파라미터로 설정합니다.

### Q171. MAVLink 미션 업로드 프로토콜에서 MISSION_COUNT → MISSION_REQUEST_INT → MISSION_ITEM_INT → MISSION_ACK 순서의 의미는?
- ✅ GCS가 총 아이템 수 전송 → 기체가 순서대로 아이템 요청 → GCS가 해당 아이템 응답 → 기체가 완료 확인 응답하는 Pull 방식 프로토콜
-    기체가 직접 모든 미션을 GCS에 푸시하는 방식
-    GCS가 모든 미션을 한 번에 전송하는 브로드캐스트 방식
-    양방향 동시 전송으로 속도를 최적화하는 파이프라인 방식

**해설**: MAVLink 미션 프로토콜은 Pull 방식입니다. GCS가 MISSION_COUNT(총 수)를 전송하면 기체가 MISSION_REQUEST_INT로 하나씩 요청하고 GCS가 응답합니다. 모두 완료되면 기체가 MISSION_ACK로 확인합니다.

**팁**: 재전송 로직도 구현해야 합니다. 일정 시간 내 응답 없으면 재요청하거나 MAV_MISSION_RESULT_TIMEOUT 오류를 처리해야 합니다.

### Q172. MAVSDK에서 기체 이륙(takeoff)을 프로그래밍할 때 올바른 순서는?
- ✅ connect → wait_until_health_all_ok → arm → takeoff → 완료 대기
-    takeoff → arm → connect → 완료 대기
-    arm → connect → takeoff → health_check
-    connect → takeoff → arm → health_check

**해설**: MAVSDK 이륙 순서: 1) 연결 확립 2) 센서 준비(health all ok) 확인 3) Arm 4) Takeoff. 건강 상태 확인 없이 Arm하면 Pre-arm 체크 실패로 거부될 수 있습니다.

**팁**: MAVSDK Python에서는 asyncio와 await를 사용하며, drone.action.arm()과 drone.action.takeoff()는 coroutine입니다.

### Q173. QGroundControl에서 파라미터 값을 변경하고 '영구 저장'을 하지 않으면 발생하는 문제는?
- ✅ 기체 재부팅 시 변경된 파라미터가 초기값으로 리셋되어 설정이 사라짐
-    변경된 파라미터가 즉시 비활성화됨
-    다음 미션 시작 시 자동으로 저장됨
-    GCS와의 연결이 끊기면 변경이 취소됨

**해설**: MAVLink PARAM_SET으로 변경된 파라미터는 메모리(RAM)에만 적용됩니다. EEPROM/SD에 영구 저장하려면 MAV_CMD_PREFLIGHT_STORAGE(241) 명령이나 QGC의 '저장' 버튼을 사용해야 합니다.

**팁**: 비행 전 파라미터 변경 후 반드시 Save를 눌러 영구 저장하는 습관이 중요합니다. 특히 캘리브레이션 후 필수입니다.

### Q174. MAVLink 메시지의 CRC_EXTRA 값은 어떤 역할을 하는가?
- ✅ 메시지 정의(필드 구조)의 버전 일관성을 검증하여 송수신 양쪽이 동일한 메시지 정의를 사용하는지 확인
-    데이터 전송 오류 감지를 위한 체크섬
-    메시지 우선순위 결정 필드
-    시스템 ID와 컴포넌트 ID의 XOR 값

**해설**: CRC_EXTRA는 메시지 정의의 필드 이름, 타입, 순서를 해시한 값입니다. 수신측은 자신의 메시지 정의로 계산한 CRC_EXTRA와 수신된 메시지의 CRC를 비교하여 호환성을 확인합니다.

**팁**: 커스텀 MAVLink 메시지 생성 시 mavgen 툴이 CRC_EXTRA를 자동 계산합니다. 직접 계산할 필요가 없습니다.

### Q175. MAVSDK의 Telemetry 플러그인에서 subscribe_position()을 사용할 때 주의사항은?
- ✅ 콜백 함수 내에서 blocking call(대기)을 사용하면 안 되며, 별도 스레드 또는 async 처리 필요
-    위치 데이터는 1초에 한 번만 수신됨
-    subscribe_position()은 GPS 없이도 작동
-    콜백은 메인 스레드에서만 실행 가능

**해설**: 텔레메트리 콜백은 높은 주파수로 호출될 수 있으며, 콜백 내에서 sleep이나 다른 MAVSDK await 호출을 하면 데이터 처리가 지연됩니다. 데이터 저장 후 별도 처리 스레드로 위임하는 패턴을 사용합니다.

**팁**: Python MAVSDK에서는 async for 방식으로 텔레메트리 스트림을 소비하는 패턴이 권장됩니다.

### Q176. QGC의 Plan View에서 Survey(지그재그 격자 탐사) 미션 생성 시 Camera → Ground Resolution 설정의 의미는?
- ✅ 1픽셀이 실제 지면의 몇 cm에 해당하는지 설정하여 비행 고도와 촬영 간격을 자동 계산
-    비행 속도를 지면 해상도로 제어하는 파라미터
-    사진 파일의 해상도(픽셀 수) 설정
-    카메라 센서 크기 설정

**해설**: Ground Resolution(cm/pixel) 설정 시 카메라 사양(초점거리, 센서 크기)과 결합하여 필요 비행 고도와 사진 겹침률(overlap)에 맞는 촬영 간격을 자동 계산합니다.

**팁**: 측량 드론(UAV Mapping) 작업 시 GSD(Ground Sample Distance) 2cm/px를 위해서는 약 80m 고도와 70-80% 전방/측방 겹침이 필요합니다.

### Q177. MAVLink v2 메시지 서명(Signing)에서 사용하는 타임스탬프의 역할은?
- ✅ 재전송 공격(Replay Attack) 방지를 위해 이전에 처리된 타임스탬프보다 큰 값만 허용
-    메시지 생성 시각을 기록하여 지연 시간 측정
-    동기화 목적으로 시스템 시각을 보정
-    암호화 키 생성에 사용

**해설**: MAVLink v2 서명의 타임스탬프(10μs 단위)는 단조 증가(monotonically increasing)해야 합니다. 수신측은 이전에 받은 타임스탬프보다 큰 값만 허용하여 캡처된 패킷의 재전송 공격을 방지합니다.

**팁**: MAVLink 서명 링크키(Link ID + Secret Key 32바이트)는 통신 채널별로 설정하며 반드시 안전하게 보관해야 합니다.

### Q178. PX4에서 micro-RTPS/DDS 브릿지의 역할은?
- ✅ uORB 토픽을 DDS(Fast DDS) 도메인으로 브릿지하여 ROS2 노드가 직접 PX4 내부 데이터에 접근 가능하게 함
-    MAVLink 메시지를 JSON으로 변환하는 미들웨어
-    드론 간 P2P 통신을 위한 메시 네트워크 프로토콜
-    시뮬레이터와 FC 간 UDP 통신 브릿지

**해설**: micro-RTPS(현재는 ROS2 PX4 bridge로 발전)는 PX4의 uORB 메시지를 DDS 프로토콜로 변환하여 ROS2 토픽으로 퍼블리시합니다. 컴패니언 컴퓨터에서 ROS2를 사용한 고급 자율 비행에 필수입니다.

**팁**: 최신 PX4(v1.14+)에서는 PX4-FastRTPS bridge 대신 uXRCE-DDS(Micro-XRCE-DDS)를 사용하며 px4_ros_com 패키지로 통합됩니다.

### Q179. 멀티 기체 GCS 시스템에서 각 드론을 구별하기 위한 MAVLink 라우팅 방법은?
- ✅ 각 기체에 고유한 System ID 부여 후 GCS에서 target_system 필드로 특정 기체에만 명령 전송
-    기체별 전용 주파수 채널 사용
-    IP 주소로 기체를 구별하고 MAVLink ID는 모두 동일하게 설정
-    타임슬롯 방식으로 순차적으로 통신

**해설**: MAVLink 네트워크에서 System ID(1~255)로 기체를 식별합니다. COMMAND_LONG의 target_system 필드를 특정 기체의 System ID로 설정하면 해당 기체만 명령을 처리합니다. Broadcast는 target_system=0으로 설정합니다.

**팁**: 군집 드론 시스템에서는 기체 추가/제거 시 System ID 충돌이 없도록 ID 관리 시스템이 필요합니다.

### Q180. MAVSDK Offboard 모드에서 VelocityBodyYawspeed 명령과 VelocityNedYaw 명령의 차이는?
- ✅ Body는 기체 기준 좌표계(전방/우측/하방), NED는 지구 기준 좌표계(북/동/하방)로 속도 명령을 해석
-    Body는 2D 수평 이동, NED는 3D 이동을 지원
-    VelocityBodyYawspeed는 레이싱 드론 전용
-    두 명령은 결과가 동일하며 좌표계 변환만 다름

**해설**: Body frame은 기체의 현재 기수 방향 기준입니다(전진=+X, 우측=+Y). NED는 지구 고정 좌표계입니다(북=+X, 동=+Y). Body 명령은 기체 방향과 무관한 이동에, NED는 절대 방향 이동에 적합합니다.

**팁**: Indoor 자율 비행에서 장애물 회피 알고리즘은 보통 Body frame 속도 명령을 사용하여 기체 상대적 이동을 제어합니다.

### Q181. QGC의 Analyze Tools에서 MAVLink Inspector의 주요 용도는?
- ✅ 수신되는 모든 MAVLink 메시지와 필드 값을 실시간 모니터링 및 디버깅
-    드론에 커스텀 MAVLink 메시지를 전송하는 개발 도구
-    비행 로그를 MAVLink 형식으로 변환하는 도구
-    QGC의 네트워크 연결 상태 진단

**해설**: MAVLink Inspector는 연결된 기체에서 수신되는 모든 MAVLink 메시지를 실시간으로 나열하고 각 필드 값을 확인할 수 있습니다. 텔레메트리 문제 진단, EKF 상태 확인, 센서 데이터 검증에 유용합니다.

**팁**: 특정 메시지가 수신되지 않는 경우 Inspector에서 확인 후 해당 스트림 SR* 파라미터를 조정하면 해결되는 경우가 많습니다.

### Q182. ArduPilot에서 GCS_FAILSAFE_ENABLE 파라미터가 활성화된 상태에서 GCS와의 MAVLink 연결이 끊기면?
- ✅ 설정된 동작(RTL/Hold/Land/Continue)을 자동으로 실행하여 안전 확보
-    즉시 모터를 꺼서 긴급 착륙
-    마지막 명령 그대로 계속 비행
-    Loiter 모드로만 전환

**해설**: GCS Failsafe는 FS_GCS_ENABLE 파라미터로 설정하며, 활성화 시 GCS 링크 손실 후 설정 시간(기본 5초) 내 복구되지 않으면 RTL 또는 지정된 동작을 실행합니다.

**팁**: 멀티에이전트 시스템에서 GCS Failsafe와 RC Failsafe의 우선순위 및 상호 작용을 사전에 철저히 테스트해야 합니다.

### Q183. MAVLink에서 REQUEST_DATA_STREAM 메시지와 SET_MESSAGE_INTERVAL 메시지의 차이점은?
- ✅ REQUEST_DATA_STREAM은 레거시 그룹 기반 설정, SET_MESSAGE_INTERVAL은 개별 메시지별 정밀 인터벌 설정으로 v2 권장 방식
-    SET_MESSAGE_INTERVAL은 GPS 전용 메시지 설정 도구
-    REQUEST_DATA_STREAM이 더 정밀한 제어를 제공
-    두 메시지는 완전히 동일한 기능

**해설**: REQUEST_DATA_STREAM(#66)은 스트림 ID로 그룹된 메시지들의 전송 주파수를 설정하는 레거시 방식입니다. SET_MESSAGE_INTERVAL(#511, MAVLink Command)은 특정 메시지 ID별로 마이크로초 단위로 인터벌을 설정하는 v2 권장 방식입니다.

**팁**: MAVSDK는 내부적으로 SET_MESSAGE_INTERVAL을 사용합니다. PX4 최신 버전에서는 REQUEST_DATA_STREAM이 더 이상 지원되지 않을 수 있습니다.

### Q184. QGC Plan에서 ROI(Region of Interest) 명령의 기능은?
- ✅ 비행 중 카메라/기수가 특정 지점이나 웨이포인트를 향해 자동으로 지향하도록 설정
-    비행 금지 구역(No-fly Zone) 설정
-    자동 사진 촬영 트리거 영역 지정
-    GPS 신호가 약한 구역 우회 설정

**해설**: MAV_CMD_DO_SET_ROI 명령은 기체 또는 짐벌이 지정된 지점을 향하도록 합니다. 미션 비행 중 특정 위치(건물, 피사체)를 연속 추적하면서 비행하는 관측 임무에 사용합니다.

**팁**: ROI 해제는 MAV_CMD_DO_SET_ROI에 param1=0으로 설정하거나 MAV_CMD_DO_SET_ROI_NONE 명령을 사용합니다.

### Q185. MAVSDK에서 Geofence를 프로그래밍으로 업로드할 때 포함되는 데이터 구조는?
- ✅ Polygon 또는 Circle 형태의 경계 정보와 include/exclude 타입 설정
-    최대 고도만 포함하는 단순 구조
-    KML 파일 경로 문자열만 전달
-    반경과 중심 좌표만 포함

**해설**: MAVSDK Geofence 플러그인은 Polygon(다각형) 또는 Circle(원형) 지오펜스를 지원하며 각각 포함(INCLUSION) 또는 제외(EXCLUSION) 타입을 설정할 수 있습니다.

**팁**: MAVLink로 Geofence를 전송할 때는 MISSION_ITEM_INT 메시지에 MAV_FRAME_GLOBAL_INT와 MAV_CMD_NAV_FENCE_POLYGON_VERTEX_INCLUSION 등의 명령을 사용합니다.

### Q186. 텔레메트리 링크 대역폭 최적화를 위해 링크 QoS(Quality of Service)를 관리하는 방법은?
- ✅ 중요 메시지(HEARTBEAT, STATUS) 높은 우선순위 보장, 고빈도 센서 스트림 압축 또는 속도 제한, 링크 품질에 따른 적응형 데이터 레이트 조정
-    모든 메시지를 동일 우선순위로 전송하여 단순화
-    텔레메트리 대역폭은 FC가 자동으로 관리하므로 GCS 설정 불필요
-    패킷 손실 무시하고 재전송 없이 단방향 스트리밍

**해설**: 저대역폭 링크(텔레메트리 라디오)에서는 메시지 우선순위 설정, 스트림 주파수 최적화, 링크 품질(RADIO_STATUS 메시지의 rssi/noise 필드) 기반 적응형 조절이 중요합니다.

**팁**: SiK 라디오의 RADIO_STATUS(#109) 메시지를 모니터링하여 rssi < -80dBm이면 링크 품질 저하로 판단하고 스트림 속도를 줄이는 GCS 로직을 구현할 수 있습니다.

### Q187. QGC에서 Vehicle Setup → Safety 탭에서 설정 가능한 항목으로 올바른 것은?
- ✅ 배터리 Failsafe 전압 임계값, RC 손실 반응, Geofence 설정, Return to Home 고도
-    모터 순서 및 방향 설정
-    GPS 안테나 위치 오프셋 설정
-    비행 로그 샘플링 주파수 설정

**해설**: Safety 탭에서 배터리 경고/위험 전압 임계값, RC 손실 Failsafe 동작, Geofence 활성화 및 동작, RTL 고도 등 핵심 안전 파라미터를 그래픽 인터페이스로 설정합니다.

**팁**: 방산 드론 운용 전 Safety 파라미터를 임무 환경에 맞게 재검토하는 것이 필수 절차입니다.

### Q188. MAVLink 프로토콜에서 메시지 재전송 없이 UDP를 사용할 때의 위험성과 대응 방법은?
- ✅ UDP는 패킷 손실 보장 없으므로 중요 명령(COMMAND_LONG)은 COMMAND_ACK 수신 확인 후 재전송 로직 구현 필요
-    MAVLink 자체 재전송 기능이 내장되어 있어 별도 처리 불필요
-    TCP로 전환하면 모든 문제 해결
-    MAVLink는 항상 CRC 오류만 검출하면 충분

**해설**: UDP는 패킷 손실이 발생할 수 있으며 MAVLink는 자체 재전송이 없습니다. 중요 명령은 COMMAND_ACK 수신 전까지 타임아웃 후 재전송하는 로직을 애플리케이션 레이어에서 구현해야 합니다.

**팁**: MAVSDK는 내부적으로 명령 재전송 및 ACK 처리를 구현합니다. 직접 MAVLink를 구현할 때는 이 로직을 반드시 추가해야 합니다.

### Q189. QGC의 Fly View에서 기체에 수동으로 Go-To 위치를 지정할 때 사용하는 MAVLink 명령은?
- ✅ MAV_CMD_DO_REPOSITION 또는 SET_POSITION_TARGET_GLOBAL_INT
-    MISSION_ITEM으로 즉시 전송
-    COMMAND_LONG으로 좌표를 직접 파라미터에 포함
-    GO_TO_LOCATION 전용 메시지 사용

**해설**: QGC의 Go-To 기능은 MAV_CMD_DO_REPOSITION(#192) 또는 SET_POSITION_TARGET_GLOBAL_INT(#86) 메시지를 사용합니다. 기체는 현재 고도를 유지하거나 지정된 고도로 이동합니다.

**팁**: DO_REPOSITION는 속도 파라미터도 포함하여 이동 속도를 제어할 수 있습니다.

### Q190. MAVLink 컴포넌트 ID 중 MAV_COMP_ID_AUTOPILOT1(1)과 MAV_COMP_ID_MISSIONPLANNER(190)의 구분이 중요한 이유는?
- ✅ 명령의 target_component 설정에 따라 FC만 또는 GCS만 명령을 처리하므로, 잘못된 컴포넌트 ID로 전송 시 명령이 무시될 수 있음
-    컴포넌트 ID는 네트워크 포트 번호와 같아 라우팅에 사용됨
-    컴포넌트 ID가 다르면 암호화 방식이 달라짐
-    컴포넌트 ID는 디버깅용으로만 사용

**해설**: 각 컴포넌트는 자신의 System ID + Component ID 조합으로만 수신된 메시지를 처리합니다. target_system과 target_component를 올바르게 설정하지 않으면 멀티 컴포넌트 시스템에서 명령이 의도한 컴포넌트에 전달되지 않습니다.

**팁**: GCS는 브로드캐스트(target_component=0)로 전송하면 동일 시스템의 모든 컴포넌트가 수신합니다.

### Q191. MAVLink v2 서명 구현 시 링크 ID(Link ID)를 채널별로 별도 설정해야 하는 이유는?
- ✅ 동일 비밀키를 사용하는 여러 링크에서 재전송 공격 방지를 위해 채널별 독립 타임스탬프 추적이 필요하며, 링크 ID로 각 채널의 마지막 타임스탬프를 별도 관리
-    링크 ID가 암호화 IV(초기벡터) 역할을 하기 때문
-    각 링크가 서로 다른 MAVLink 버전을 사용할 수 있기 때문
-    링크 ID는 단순한 레이블로 보안과는 무관

**해설**: MAVLink v2 서명은 링크 ID별로 마지막 수신 타임스탬프를 별도 추적합니다. 동일 비밀키로 여러 채널(직렬, UDP, TCP)을 사용할 때 한 채널의 패킷을 다른 채널로 재전송하는 크로스 채널 재전송 공격을 방지합니다.

**팁**: 실무에서는 채널(링크)별로 다른 비밀키를 사용하여 채널 격리를 강화하는 것이 권장됩니다.

### Q192. 다수의 기체가 동일 MAVLink 버스를 공유할 때 발생하는 트래픽 충돌 문제와 QoS 설계 방법은?
- ✅ 각 기체의 스트림 주파수 합산이 링크 대역폭을 초과하지 않도록 기체 수에 비례하여 개별 스트림 속도를 낮추고, 우선순위 큐로 HEARTBEAT와 COMMAND_ACK를 우선 처리
-    기체별로 MAVLink 스트림 주파수 상한을 GCS가 REQUEST_DATA_STREAM으로 개별 설정하고, 전체 링크 대역폭 내에서 우선순위별 메시지 큐를 분리 관리
-    각 기체에 고유 MAVLink 컴포넌트 ID를 부여하고 GCS가 ID 기반 라운드로빈 스케줄링으로 전송 슬롯을 배분하며 HEARTBEAT는 최우선 큐로 처리
-    기체 수에 비례하여 각 스트림 메시지의 전송 간격을 동적으로 조정하고 COMMAND_ACK·HEARTBEAT는 전용 고우선순위 채널에서 독립적으로 전송

**해설**: 10대 기체 × 100Hz 스트림 = 실질적인 대역폭 한계 초과 위험. 기체 수에 따라 각 스트림 주파수를 스케일링하고(예: n대→1/n), 생명 안전 메시지를 우선순위 큐로 처리하는 설계가 필요합니다.

**팁**: 군집 드론 GCS 개발 시 기체 수가 증가해도 시스템이 안정적으로 동작하는지 부하 테스트가 필수입니다.

### Q193. MAVSDK와 pyMAVLink를 비교할 때 방산 드론 개발에서 MAVSDK를 선택하는 기술적 이유는?
- ✅ 추상화된 고수준 API, 타입 안전성, C++/Python/Rust 멀티언어 지원, MAVLink 프로토콜 상세 구현 없이 빠른 개발 가능, 내장 재연결/재전송 로직
-    pymavlink은 저수준 직렬 접근으로 패킷 파싱이 빠르고 MAVSDK는 고수준 추상화로 응답 속도가 느려 실시간 제어에 불리하다
-    MAVSDK는 PX4 전용 고수준 SDK이고 pymavlink는 ArduPilot 전용 저수준 라이브러리로, 각각 다른 FC 스택에만 적용 가능하다
-    pymavlink가 MAVLink 2.0 메시지 서명, 컴포넌트 기반 라우팅, 재연결 로직을 기본 내장하여 방산 드론 개발 표준으로 선호된다

**해설**: MAVSDK는 低수준 MAVLink 처리를 숨기고 비즈니스 로직에 집중할 수 있는 고수준 API를 제공합니다. pyMAVLink는 낮은 수준의 세밀한 제어가 가능하지만 프로토콜 구현을 직접 담당해야 합니다.

**팁**: 프로토타이핑과 자율 비행 애플리케이션에는 MAVSDK, MAVLink 라우터/게이트웨이나 커스텀 GCS 개발에는 pyMAVLink(또는 pymavlink)가 적합합니다.

### Q194. QGC 오픈소스 커스터마이징에서 Custom Build를 통해 기업 전용 GCS를 만들 때 주의해야 할 라이선스 이슈는?
- ✅ QGC의 기반 Qt 프레임워크는 LGPL/GPL 라이선스이므로 커스텀 빌드를 상용 배포 시 소스 공개 의무 또는 상용 Qt 라이선스 구매가 필요
-    QGC 자체가 MIT 라이선스이므로 완전 자유 사용 가능
-    Qt 기술 사용료는 무료이며 라이선스 이슈 없음
-    GCS 소스는 공개하되 드론 제어 알고리즘은 비공개 가능

**해설**: QGC는 GPL v3 라이선스이며 Qt 프레임워크는 LGPLv3/GPLv3입니다. 상용 제품에 통합하여 배포하면 소스 공개 의무가 생깁니다. 소스 비공개를 원하면 Qt 상용 라이선스를 구매해야 합니다.

**팁**: 방산 기업 GCS 개발 시 라이선스 컴플라이언스 검토가 선행되어야 합니다. 비공개 요건이 있다면 QGC 대신 자체 개발 또는 상용 GCS 솔루션을 검토하세요.

### Q195. MAVLink 라우터(mavlink-router)를 사용하는 아키텍처에서 단일 직렬 텔레메트리를 여러 GCS 클라이언트에 동시에 제공할 때 발생하는 문제와 해결 방법은?
- ✅ GCS마다 독립 세션을 유지하면서 동일 기체 데이터를 브로드캐스트하되, 여러 GCS의 COMMAND 충돌을 방지하기 위해 마스터 GCS 개념 또는 명령 중재 레이어 필요
-    GCS마다 독립 UDP 포트를 열고 브로드캐스트로 분배하면 COMMAND 충돌 없이 모든 클라이언트가 동시에 기체를 안전하게 제어할 수 있다
-    직렬 포트를 여러 GCS 프로세스가 동시에 open()하면 OS가 자동으로 접근을 중재하므로 별도 소프트웨어 레이어 없이 안전하게 공유된다
-    MAVLink 라우터는 GCS 클라이언트를 최대 2개까지만 지원하도록 설계되어 있어 3개 이상을 사용하려면 별도 직렬 포트를 추가해야 한다

**해설**: MAVLink 라우터는 직렬 포트를 UDP 엔드포인트들에게 브로드캐스트할 수 있습니다. 단 여러 GCS가 동시에 COMMAND를 전송하면 기체가 충돌 명령을 받을 수 있으므로 마스터 권한 제어 또는 명령 필터링 레이어가 필요합니다.

**팁**: mavlink-router의 설정 파일에서 UART, UDP, TCP 엔드포인트를 조합하여 유연한 텔레메트리 분배 아키텍처를 구성할 수 있습니다.

### Q196. PX4의 uXRCE-DDS(Micro-XRCE-DDS) 에이전트를 통한 ROS2 통합에서 도메인 ID 분리의 의미는?
- ✅ ROS2 DDS 도메인 ID를 드론마다 다르게 설정하면 동일 네트워크에서 여러 드론의 토픽이 서로 섞이지 않아 멀티 기체 시스템 격리 가능
-    도메인 ID는 ROS2 버전 선택에 사용
-    도메인 ID가 낮을수록 메시지 우선순위 높음
-    도메인 ID는 암호화 채널 구분에만 사용

**해설**: ROS2의 DDS 통신은 도메인 ID(0~232) 별로 격리됩니다. 기체 1은 domain_id=0, 기체 2는 domain_id=1로 설정하면 ROS2 노드에서 특정 기체의 토픽만 접근 가능합니다. 군집 드론 ROS2 시스템의 핵심 설계 패턴입니다.

**팁**: ROS_DOMAIN_ID 환경 변수 또는 DDS XML 설정으로 변경합니다. uXRCE-DDS 에이전트 실행 시 -d [domain_id] 옵션으로 설정합니다.

### Q197. 군집 드론 GCS에서 COMMAND_LONG을 target_system=0(broadcast)으로 전송할 때의 위험성과 안전한 대안은?
- ✅ 브로드캐스트 명령은 모든 기체가 동시에 실행하여 충돌/상호간섭 위험. 안전 대안은 개별 기체 System ID로 순차 전송 또는 타임 오프셋을 포함한 시간 동기 명령 사용
-    브로드캐스트 명령은 네트워크 지연 없이 모든 기체에 동시 도달하므로 시간 동기 임무에서는 개별 순차 전송보다 안전하고 권장되는 방식이다
-    target_system=0은 브로드캐스트이고 target_system=255는 특정 그라운드 스테이션 전용이므로 기체에는 전달되지 않아 위험이 없다
-    기체별 내부 충돌 회피 알고리즘이 동시 이착륙 명령을 자동으로 직렬화하여 순서대로 처리하므로 브로드캐스트를 사용해도 물리적 충돌 위험이 발생하지 않는다

**해설**: 이륙, 착륙 등을 브로드캐스트로 전송하면 모든 기체가 동시에 동일 동작을 실행하여 공중 충돌 위험이 있습니다. 안전한 방법은 각 기체에 시간 오프셋을 두고 순차 명령하거나 MAV_CMD에 delay 파라미터를 활용하는 것입니다.

**팁**: 군집 이륙 시나리오에서 기체별 이륙 지점을 사전에 할당하고 지정된 좌표로 이동 후 이륙하는 패턴이 안전합니다.

### Q198. MAVLink STATUSTEXT 메시지의 severity 필드 활용과 GCS에서의 처리 방법은?
- ✅ MAV_SEVERITY 레벨(0=EMERGENCY~7=DEBUG)에 따라 GCS에서 경고음, 색상 코딩, 알림 팝업 차별화 처리. EMERGENCY/ALERT/CRITICAL은 즉각 운용자 개입 필요 신호
-    MAV_SEVERITY 값은 지상국 디버그 로그 필터링과 메시지 전송 주기 설정에만 활용되며, GCS UI 팝업·색상 구분·경고음 알림 동작과는 완전히 별개로 처리됨
-    MAV_SEVERITY 7(DEBUG)이 운용자의 즉각 개입을 요구하는 최고 위험 등급이고, 0(EMERGENCY)은 시스템 정상 운항 중 일반 참고 정보 수준에 해당함
-    STATUSTEXT 메시지는 비행 컴퓨터 내부 로그 버퍼에만 저장되며, GCS 실시간 화면 텍스트 출력은 반드시 별도 LOG_DISPLAY 전용 메시지를 통해서만 처리됨

**해설**: MAV_SEVERITY 0(EMERGENCY)~7(DEBUG) 중 낮을수록 심각합니다. EMERGENCY/ALERT는 즉각적인 조치가 필요한 시스템 오류, CRITICAL/ERROR는 중요 기능 장애, WARNING/NOTICE는 주의사항, INFO/DEBUG는 일반 정보입니다.

**팁**: GCS에서 STATUSTEXT를 파싱하여 심각도별 로깅과 알림을 구현하면 운용자가 중요 이벤트를 빠르게 인지할 수 있습니다.

### Q199. 비인가 접근을 방지하기 위한 MAVLink GCS 보안 아키텍처 설계 시 고려해야 할 요소는?
- ✅ MAVLink v2 서명으로 메시지 무결성/인증, TLS/DTLS 터널로 전송 암호화, GCS 접근 통제 목록(ACL), 물리 계층 링크 암호화(AES 기반 텔레메트리 라디오), 명령 이력 감사 로그
-    MAVLink v2의 빌트인 HMAC-SHA256 서명 기능이 메시지 기밀성과 무결성을 완전 보장하므로, 별도의 TLS 터널이나 VPN 추가는 중복 보안 계층에 해당하여 불필요함
-    L4/L7 계층 방화벽 룰셋과 IP 화이트리스트 조합만으로도 MAVLink 비인가 접근, 중간자 공격, 메시지 위변조 등 모든 보안 위협 벡터를 완전히 대응 가능함
-    드론 시스템 IP/MAC 주소 기반 네트워크 ACL 정책 적용만으로도 RF 스니핑, 재전송 공격, 명령 위조 등 모든 무선 기반 보안 위협 벡터를 충분히 차단 가능함

**해설**: MAVLink v2 서명은 메시지 위변조를 방지하지만 내용을 암호화하지 않습니다. 민감 정보(위치, 명령) 보호를 위해 TLS/DTLS 암호화 터널이 필요하며, 물리 계층의 AES 암호화 라디오와 GCS 접근 인증을 결합한 심층 방어(Defense in Depth)가 요구됩니다.

**팁**: 방산 드론 시스템에서는 군용 FIPS 140-2 인증 암호화 모듈 사용과 PKI 기반 인증서 관리가 요구사항이 될 수 있습니다.

### Q200. LTE/5G 기반 Beyond Visual Line of Sight(BVLOS) 드론 운용에서 MAVLink 텔레메트리 지연(latency) 관리 방법은?
- ✅ 100~500ms LTE 지연에 대응하여 GCS 예측 표시(dead reckoning), 명령 큐 최소화, 자율 Failsafe(GCS 링크 손실 시 자체 판단), Adaptive Bitrate 스트리밍 적용
-    LTE는 5ms 이하 초저지연 특성으로 지상 라디오 텔레메트리와 완전히 동일하게 실시간 명령·제어가 가능하므로 별도 dead reckoning 등 latency 보상 로직이 불필요함
-    BVLOS 운용에서는 GCS 텔레메트리 연결이 선택 사항이며, 기체가 사전 업로드된 웨이포인트 미션만으로 완전 자율 비행하므로 GCS 실시간 텔레메트리 통신이 구조적으로 불필요함
-    LTE 지연 문제는 dBi가 높은 고이득 지향성 안테나와 자동 추적 안테나 트래커를 동시 운용·조합하여 RF 수신 신호 강도를 극대화하는 물리적 방법만으로 완전히 해결 가능함

**해설**: LTE의 100~500ms 왕복 지연은 실시간 제어에 한계를 만듭니다. GCS는 마지막 수신 속도/방향으로 현재 위치를 추정(dead reckoning) 표시하고, 기체는 GCS 연결 없이도 계속 임무를 수행하는 자율 로직이 필수입니다.

**팁**: BVLOS 규정에서는 기체가 항상 자율 Failsafe를 보유하고, 링크 손실 시 자동 RTL/Hold가 가능함을 검증해야 합니다.

### Q201. MAVLink 미션 프로토콜에서 MISSION_WRITE_PARTIAL_LIST 사용이 유리한 상황과 주의사항은?
- ✅ 기존 미션의 일부 웨이포인트만 수정할 때 사용하며 효율적이나, 시작/끝 인덱스 범위 오류 시 미션 손상 위험과 기체가 이미 해당 아이템을 실행 중이면 예측 불가능한 동작 발생
-    부분 업로드는 미션 전체 시퀀스 번호를 리셋하지 않아 기체가 아이템을 혼동할 수 없으므로 전체 재업로드보다 항상 안전하고 권장되는 방식이다
-    MISSION_WRITE_PARTIAL_LIST는 MAVLink 2.0 확장 명령으로 구형 MAVLink 1.0 펌웨어가 탑재된 기체에서는 지원되지 않아 무시된다
-    부분 업로드 구간의 아이템이 AUTO 모드로 실행 중이어도 GCS가 HOLD 전환 없이 즉시 수정이 가능하며 기체는 새 명령만 즉시 따르게 된다

**해설**: MISSION_WRITE_PARTIAL_LIST(#38)는 지정된 인덱스 범위만 덮어쓰는 부분 업데이트로 대역폭을 절약합니다. 단 비행 중 현재 실행 중인 미션 아이템 수정은 즉시 동작 변화를 초래할 수 있으므로 범위 검증이 필수입니다.

**팁**: 비행 중 동적 미션 수정이 필요한 시스템에서는 전체 미션을 버퍼로 관리하고 검증 후 전체 재업로드하는 방어적 설계를 권장합니다.

### Q202. MAVLink 기반 컴패니언 컴퓨터에서 GCS 역할과 컴포넌트 ID 설계 시 고려사항은?
- ✅ 컴패니언은 MAV_COMP_ID_ONBOARD_COMPUTER로 등록하고, FC의 HEARTBEAT를 모니터링하여 상태를 파악. GCS 역할 동시 수행 시 GCS component ID와 충돌하지 않도록 ID 분리 필요
-    컴패니언 컴퓨터는 MAVLink 네트워크 주 제어 노드로서 비행 컨트롤러와 동일한 System ID 1, Component ID 1을 설정하여 직접 명령을 주고받는 것이 표준 구성임
-    컴패니언 컴퓨터는 ROS2 DDS pub/sub 토픽 통신만으로 비행 컨트롤러와 직접 연결하고, MAVLink 프로토콜은 사용하지 않으며 MAVROS 브리지 노드가 양방향 프로토콜 변환을 전담함
-    GCS와 컴패니언 컴퓨터가 동일한 Component ID를 공유하더라도 MAVLink 라우터가 수신 타임스탬프를 기준으로 자동 우선순위를 판단하여 명령 충돌 없이 안전하게 처리 가능함

**해설**: 컴패니언 컴퓨터는 MAV_COMP_ID_ONBOARD_COMPUTER(191)로 MAVLink 네트워크에 참여합니다. GCS 역할(지상에서 접속)과 Onboard 역할(기체 탑재)을 동시에 수행하는 경우 컴포넌트 ID를 분리하여 메시지 라우팅 혼란을 방지합니다.

**팁**: MAV_COMP_ID_ONBOARD_COMPUTER ~ MAV_COMP_ID_ONBOARD_COMPUTER4(191~194)까지 여러 온보드 컴퓨터를 구분할 수 있습니다.

### Q203. QGC의 VideoStream 기능에서 RTSP 스트림을 수신할 때 GStreamer 파이프라인 최적화 방법은?
- ✅ 낮은 지연을 위해 H.264/H.265 하드웨어 디코더 사용, 버퍼 크기 최소화(latency=0), rtspsrc의 protocols=tcp 설정으로 UDP 패킷 손실 대응
-    rtspsrc timeout 파라미터를 최대로 설정하고 rtph264depay 앞에 queue 엘리먼트를 추가하여 네트워크 지터를 흡수하고 재생 안정성을 우선
-    H.264 소프트웨어 디코더를 사용하고 GStreamer appsink로 프레임을 캡처하여 QGC 자체 렌더러에 전달하면 플랫폼 독립적 재생이 가능
-    QGC VideoManager가 RTSP URI를 감지하면 자동으로 최적 GStreamer 파이프라인을 생성하므로 수동 파이프라인 편집은 QML에서만 허용

**해설**: 드론 비디오 스트리밍에서 지연은 안전에 직결됩니다. H.265 하드웨어 디코딩, RTP jitter buffer 최소화, latency 파라미터 조정으로 end-to-end 지연을 200ms 이하로 유지하는 것이 목표입니다.

**팁**: QGC는 MAVLink CAMERA_INFORMATION 또는 VIDEO_STREAM_INFORMATION 메시지로 카메라 스트림 URI를 자동 수신하고 GStreamer로 재생합니다.

### Q204. MAVLink 파라미터 프로토콜에서 대규모 파라미터 세트(1000개+) 동기화 시 신뢰성 있는 구현 방법은?
- ✅ PARAM_REQUEST_LIST 후 수신된 파라미터 인덱스 추적, 누락된 인덱스는 PARAM_REQUEST_READ로 개별 재요청, 타임아웃 후 체크섬 또는 카운트 검증으로 완전성 확인
-    PARAM_REQUEST_LIST 전송 후 param_count 필드로 총 개수를 확인하고 수신 완료 시 PARAM_SET으로 검증 파라미터를 재전송하여 에코 비교
-    첫 PARAM_REQUEST_LIST에서 일부 누락 시 PARAM_REQUEST_LIST를 재전송하되 응답 간격을 늘려 재시도하며 param_count 일치 시 완료 처리
-    파라미터 수신 중 param_index와 param_count를 트래킹하여 예상 총 개수와 실제 수신 수를 비교하고, 수신 완료 후 FC에 특정 파라미터를 재요청하여 에코 검증

**해설**: UDP 환경에서 파라미터 전송 중 패킷 손실이 발생하면 일부 파라미터가 누락될 수 있습니다. PARAM_VALUE의 param_index와 param_count 필드로 수신 현황을 추적하고, 누락된 인덱스를 PARAM_REQUEST_READ로 개별 재요청하는 견고한 구현이 필요합니다.

**팁**: PX4 파라미터 수는 ~400~600개이며 ArduPilot은 더 많을 수 있습니다. 첫 연결 동기화 시 GCS의 UI가 응답하지 않는 것처럼 보이지 않도록 비동기 처리를 구현하세요.

### Q205. GCS에서 전자 지도와 드론 위치를 동기화할 때 좌표 참조 시스템(CRS) 변환 처리가 중요한 이유는?
- ✅ MAVLink는 WGS84 좌표를 사용하지만 지도 라이브러리는 Web Mercator(EPSG:3857)를 사용하므로 정확한 좌표 변환 없이는 위치 표시 오차 발생
-    Leaflet과 OpenLayers는 WGS84(EPSG:4326)를 기본 좌표계로 사용하므로 MAVLink 좌표를 별도 변환 없이 직접 마커로 표시할 수 있다
-    드론 운용 고도 500m 이하에서는 Web Mercator 왜곡이 수cm 수준이어서 GCS 지도 표시의 허용 오차 범위 안에 있으므로 변환을 생략할 수 있다
-    MAVLink GLOBAL_POSITION_INT는 1e7 정수형으로 전달되므로 부동소수점으로 나누면 좌표 체계 변환 없이 지도에 바로 사용 가능하다

**해설**: MAVLink GLOBAL_POSITION_INT의 좌표는 WGS84(위도/경도/고도)로 전달됩니다. Leaflet, OpenLayers 등 웹 지도는 EPSG:3857(Web Mercator) 투영을 사용하므로 변환이 필요합니다. 고위도 지역일수록 Mercator 왜곡이 커집니다.

**팁**: proj4js(JavaScript) 또는 pyproj(Python) 라이브러리로 정확한 CRS 변환을 구현하세요. Leaflet의 L.latLng()는 WGS84를 직접 처리합니다.

### Q206. MAVLink COMMAND_LONG의 confirmation 필드 활용과 임계 명령 전송 시 중복 실행 방지 설계는?
- ✅ confirmation=0은 첫 전송, 증가하는 값으로 재전송을 표시하며 기체가 중복 명령을 구별. 임계 명령에는 COMMAND_ACK 수신 후에만 다음 단계를 진행하는 상태 머신 구현 필요
-    confirmation=1은 첫 전송, 0으로 감소하는 값이 재전송임을 나타내며 기체는 값이 일치하는 명령만 실행. 임계 명령은 시퀀스 번호 기반 중복 필터로 추가 보호
-    COMMAND_LONG의 target_system과 target_component를 조합한 고유 키로 중복 명령을 감지하고 COMMAND_ACK 수신 전까지 동일 조합의 명령을 큐에서 보류
-    COMMAND_LONG에 timestamp 확장 필드를 추가하지 않고도 target_system·target_component·command 조합으로 기체가 처리 중인 명령을 식별하여 중복 실행을 차단

**해설**: confirmation 필드는 재전송 시 0, 1, 2...로 증가합니다. 그러나 MAVLink는 멱등성(idempotency)을 보장하지 않으므로, 상태 머신 기반으로 COMMAND_ACK(ACCEPTED)를 수신하기 전까지는 동일 명령을 재전송하지 않는 설계가 중요합니다.

**팁**: COMMAND_ACK의 result 필드가 MAV_RESULT_IN_PROGRESS이면 명령이 실행 중임을 의미하며 기다려야 합니다.

### Q207. PX4 로그에서 flight_phase 분석을 통해 GCS에서 비행 경로 재현(playback)을 구현할 때 핵심 데이터 소스는?
- ✅ vehicle_global_position, vehicle_attitude, vehicle_status, actuator_outputs 토픽 데이터와 ulog 파일을 파싱하여 타임스탬프 기반으로 재현
-    HEARTBEAT 메시지의 custom_mode, base_mode, system_status 필드 이력만을 파싱하면 비행 경로, 자세, 모터 출력을 포함한 전체 재현이 가능함
-    SD카드에 기록된 raw IMU 6축 센서 데이터(3축 가속도·3축 자이로)만으로 비행 위치·자세·모드·액추에이터 출력 전체를 역산하여 완전한 비행 경로 재현이 가능함
-    MAVLink GLOBAL_POSITION_INT·ATTITUDE·SYS_STATUS 메시지를 Wireshark로 캡처한 pcap 파일 단독으로도 완전한 비행 재현이 가능함

**해설**: PX4 ulog 파일에는 모든 uORB 토픽 데이터가 타임스탬프와 함께 기록됩니다. vehicle_global_position(경로), vehicle_attitude(자세), vehicle_status(모드), actuator_outputs(모터 출력)를 파싱하면 완전한 비행 재현이 가능합니다.

**팁**: Flight Review(pyulog 라이브러리 사용)와 PX4 Log Analysis 툴(plot_app)이 이 방식으로 구현되어 있습니다. Python ulog_parse 패키지를 활용하면 커스텀 재현 기능 개발이 가능합니다.

### Q208. Mission Fence(미션 지오펜스)와 GCS 표시 지오펜스가 기체에서 동시에 활성화될 때 우선순위는?
- ✅ 가장 제한적인 조건이 우선 적용되며, 기체 내 Geofence breach 감지는 Commander가 처리하고 GCS의 소프트웨어 지오펜스는 이중 안전망 역할
-    GCS의 소프트웨어 지오펜스가 기체 파라미터보다 항상 우선 적용되며, 기체 내부 Geofence는 GCS 연결 해제 시에만 활성화되는 보조 안전망
-    미션 지오펜스가 비행 중 최우선으로 적용되고, GCS 표시 지오펜스는 위반 감지 시 MAVLink FENCE_STATUS 메시지로 운용자에게 경고만 전송
-    두 지오펜스 중 먼저 위반된 지오펜스가 우선 처리되며, 동시 위반 시 기체 Commander가 더 보수적인 Failsafe 동작을 자동 선택하여 실행

**해설**: PX4와 ArduPilot 모두 기체 내 Geofence 파라미터를 기준으로 동작하며, GCS의 시각적 표시는 운용자 인식을 위한 보조 수단입니다. 가장 제한적인 설정(좁은 반경, 낮은 고도)이 사실상의 실효 경계가 됩니다.

**팁**: 실무에서는 GCS 지오펜스를 기체 지오펜스보다 10~20% 넓게 설정하여 GCS 경고가 먼저 뜨고 기체 자동 Failsafe 전에 운용자가 대응할 시간을 줍니다.

### Q209. MAVLink 기반 다중 GCS 환경에서 '활성 GCS 전환(Active GCS Transfer)' 프로토콜 구현 시 안전 고려사항은?
- ✅ COMMAND_LONG MAV_CMD_CONTROL_HIGH_LATENCY 또는 커스텀 승인 프로토콜로 이전 GCS가 제어권 명시적 해제, 신규 GCS가 HEARTBEAT 확인 후 제어 획득. 전환 중 명령 충돌 방지 인터락 필요
-    두 GCS가 동시에 명령을 전송해도 MAVLink 라우터가 수신 타임스탬프 우선순위와 command_id 시퀀스 번호를 복합 판단 기준으로 적용하여 충돌 명령을 자동으로 중재하여 기체에 전달함
-    MAVLink 표준은 가장 최근에 유효한 HEARTBEAT를 수신한 GCS에 자동으로 제어 우선권을 부여하므로 신규 GCS가 HEARTBEAT 패킷을 전송하는 즉시 기체 제어권이 자동으로 전환됨
-    GCS 간 제어 전환은 비행 컨트롤러 시스템의 전체 재부팅과 파라미터 전면 재초기화 과정을 통해서만 유일하게 가능하며, 런타임 소프트웨어적 핸드오프 프로토콜은 MAVLink 표준에 정의되어 있지 않음

**해설**: 다중 GCS에서 제어권 이양 중 두 GCS가 동시에 상반된 명령(RTL/Continue 등)을 보내면 기체가 예측 불가능하게 동작할 수 있습니다. 명시적 핸드오프 프로토콜과 기체 측의 마지막 명령 소스 추적 기능이 필요합니다.

**팁**: 방산 용도의 이중화 GCS 시스템(주 GCS 장애 시 백업 GCS 자동 전환)에서 이 문제가 핵심 안전 요구사항입니다.

### Q210. 드론 군집 임무에서 MAVLink의 FOLLOW_TARGET(#144) 메시지와 Formation 제어를 결합하는 아키텍처는?
- ✅ 리더 드론이 FOLLOW_TARGET으로 자신의 위치/속도를 브로드캐스트하면 팔로워들이 고정 오프셋을 더한 목표 위치를 계산하여 독립적으로 추종. 오프셋 좌표계와 충돌 회피 레이어 분리 필요
-    GCS가 FOLLOW_TARGET 메시지로 리더 위치를 수신하고 각 팔로워에게 MISSION_ITEM_INT로 개별 웨이포인트를 계산·전송하며 충돌 회피는 GCS가 중앙 처리
-    리더와 팔로워가 모두 GLOBAL_POSITION_INT를 브로드캐스트하고, 각 드론이 로컬 좌표계에서 팀 전체 위치를 계산하여 독립적으로 포메이션 오프셋 유지
-    MAVLink TRAJECTORY_REPRESENTATION_WAYPOINTS로 군집 경로를 공유하고 팔로워가 Bezier 보간으로 리더 궤적을 시간 지연 오프셋으로 추종

**해설**: Leader-Follower 군집 아키텍처에서 리더의 FOLLOW_TARGET 데이터를 모든 팔로워가 구독하고 각자 지정된 오프셋(NED 또는 Body frame)을 더해 목표를 계산합니다. 팔로워 간 상대 거리는 분산 충돌 회피 알고리즘(ORCA, velocity obstacles)으로 처리합니다.

**팁**: 실용적인 군집 시스템에서는 MAVLink 외에 드론 간 직접 통신(MIMO, ad-hoc WiFi, UWB)으로 더 빠른 상대 위치 공유가 필요합니다.

