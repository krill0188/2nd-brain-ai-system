---
source: "career-bot/store/questions.json#SW개발"
ingested: 2026-08-02
captured: 2026-08-02
type: quiz-compilation
evidence_tier: non-primary-reconstruction
category: "SW개발"
question_count: 62
author: "DroneAI Lab 커리어 문항은행 (비공개 실무자 재구성)"
sha256: "4318da288e48817fe530d1bab8fda65ba4b1af7dcb696c6f52ff97d8e62af744"
tags: [career, quiz, sw-dev-quiz]
---

# SW개발 — 커리어 대비 퀴즈 재구성 컴필레이션 (62문항)

> ⚠️ **비-1차-증거 고지**: 이 문서는 방산/드론/AI 커리어 대비용으로 재구성된
> 객관식 퀴즈 모음이다. 각 항목에 원출처 인용이 없으므로 `research/` AI
> 연구 루프의 Retriever/Verifier는 이 문서를 **1차 증거(raw evidence)로
> 취급해서는 안 된다**. Critic/Verifier가 근거로 인용할 경우 반드시
> `verification_status: insufficient_evidence`로 처리하고, 별도의 1차
> 출처(GitHub/arXiv/공식문서 등)로 교차검증한 뒤에만 canonical 승격
> 대상이 될 수 있다. 정답/해설은 원저작자(DroneAI Lab 내부 실무자)의 실무 지식
> 재구성이며 공식 표준 문서가 아니다.

**원본**: `career-bot/store/questions.json` (id 범위: 61–260)
**난이도 분포**: easy=13, hard=18, medium=31

## 문항

### Q61. TypeScript에서 interface와 type의 차이는?
- ✅ interface: 선언 병합 가능, type: 유니온/인터섹션 지원
-    차이 없음
-    type이 더 빠름
-    interface만 사용 가능

**해설**: interface는 선언 병합(Declaration Merging)이 가능하고, type은 유니온(|), 인터섹션(&), 매핑된 타입 등 고급 타입 조작을 지원합니다.

**팁**: 실무에서의 사용 기준(API 정의=interface, 복잡한 타입 조합=type)을 설명하세요.

### Q62. Node.js Event Loop의 실행 순서는?
- ✅ Microtask → Macrotask → I/O
-    I/O → Microtask → Macrotask
-    Macrotask → Microtask → I/O
-    랜덤

**해설**: Microtask(Promise, queueMicrotask)가 Macrotask(setTimeout, setInterval)보다 먼저 실행됩니다. 각 Macrotask 후 Microtask 큐가 완전히 비워집니다.

**팁**: Promise.resolve().then()과 setTimeout(,0)의 실행 순서를 코드로 설명할 수 있어야 합니다.

### Q63. 다음 코드의 출력 순서는?
console.log(1);
setTimeout(()=>console.log(2),0);
Promise.resolve().then(()=>console.log(3));
console.log(4);
- ✅ 1, 4, 3, 2
-    1, 2, 3, 4
-    4, 3, 2, 1
-    1, 3, 4, 2

**해설**: 동기 코드(1,4) 먼저 → Microtask(Promise→3) → Macrotask(setTimeout→2). 따라서 1, 4, 3, 2 순서.

**팁**: 이벤트 루프의 각 페이즈(timers, pending callbacks, poll, check, close)를 도식으로 설명하세요.

### Q64. SQLite WAL(Write-Ahead Logging) 모드의 장점은?
- ✅ 읽기/쓰기 동시 가능
-    데이터 압축
-    자동 백업
-    암호화

**해설**: WAL 모드에서는 읽기가 쓰기를 차단하지 않아 동시성이 크게 향상됩니다. 변경사항을 WAL 파일에 먼저 기록 후 체크포인트에서 DB에 반영.

**팁**: 봇/서비스에서 SQLite WAL 모드를 사용한 동시 접근 처리 경험을 설명하세요.

### Q65. REST API에서 멱등성(Idempotent)을 보장하는 메서드는?
- ✅ GET, PUT, DELETE
-    POST만
-    PATCH만
-    없음

**해설**: GET(조회), PUT(전체 수정), DELETE(삭제)는 여러 번 실행해도 결과가 동일합니다. POST는 호출마다 새 리소스가 생성될 수 있어 비멱등.

**팁**: 멱등성이 시스템 안정성(재시도 로직)에 미치는 영향을 설명하세요.

### Q66. Python GIL(Global Interpreter Lock)의 영향은?
- ✅ CPU-bound 멀티스레딩 제한
-    I/O 성능 향상
-    메모리 절약
-    관련 없음

**해설**: GIL은 한 시점에 하나의 스레드만 Python 바이트코드를 실행하게 합니다. CPU-bound 작업의 멀티스레딩 성능이 제한되지만, I/O-bound에는 영향이 적습니다.

**팁**: GIL 우회 방법(multiprocessing, C 확장, asyncio)을 구체적으로 설명하세요.

### Q67. Git rebase와 merge의 차이는?
- ✅ merge: 병합 커밋 생성, rebase: 선형 히스토리
-    같은 기능
-    rebase가 더 안전
-    merge가 더 빠름

**해설**: merge: 두 브랜치의 병합 커밋을 생성. rebase: 커밋들을 대상 브랜치 위에 재배치하여 선형 히스토리를 만듦. rebase는 히스토리를 깔끔하게 만들지만 공유 브랜치에서 주의 필요.

**팁**: 팀 프로젝트에서의 브랜치 전략(Git Flow, Trunk-based)과 연계하여 설명하세요.

### Q68. Docker에서 COPY와 ADD의 차이는?
- ✅ ADD: URL/tar 자동 해제 지원, COPY: 단순 복사
-    같은 명령
-    COPY가 더 많은 기능
-    ADD는 삭제 명령

**해설**: ADD는 URL에서 다운로드, tar 자동 해제 기능이 있습니다. COPY는 단순 파일 복사만. 예측 가능성을 위해 COPY 사용이 권장됩니다.

**팁**: 멀티스테이지 빌드에서 COPY --from의 활용법도 알아두세요.

### Q69. WebSocket과 SSE(Server-Sent Events)의 차이는?
- ✅ SSE: 서버→클라이언트 단방향, HTTP 호환
-    WebSocket이 단방향
-    SSE가 양방향
-    차이 없음

**해설**: WebSocket: 양방향 풀듀플렉스 통신. SSE: 서버에서 클라이언트로의 단방향 스트림, HTTP 기반으로 기존 인프라 호환성 높음.

**팁**: 드론 텔레메트리 대시보드에 WebSocket vs SSE 선택 기준을 설명하세요.

### Q70. BullMQ에서 실패한 작업의 재시도 전략은?
- ✅ Exponential backoff
-    즉시 재시도만
-    재시도 없음
-    선형 증가

**해설**: BullMQ는 Exponential backoff(지수 백오프)를 기본 재시도 전략으로 사용합니다. 1초→2초→4초→8초... 로 간격을 늘려 시스템 부하를 방지.

**팁**: Dead Letter Queue, 최대 재시도 횟수 설정 등 실무 운영 전략을 설명하세요.

### Q77. TypeScript에서 제네릭(Generics)의 주요 용도는?
- ✅ 타입 안전성을 유지하면서 재사용 가능한 컴포넌트 작성
-    성능 향상
-    런타임 타입 체크
-    메모리 절약

**해설**: 제네릭은 함수, 클래스, 인터페이스를 특정 타입에 묶지 않으면서도 타입 안전성을 보장합니다. 예: function identity<T>(arg: T): T

**팁**: 실무에서 제네릭을 활용한 유틸리티 타입(Partial, Pick, Record) 커스텀 경험을 설명하세요.

### Q80. CI/CD 파이프라인에서 드론 펌웨어 배포 시 주의점은?
- ✅ OTA 업데이트 실패 시 롤백 메커니즘 필수
-    자동 배포만 하면 됨
-    테스트 불필요
-    수동 배포가 안전

**해설**: 드론 펌웨어 OTA 업데이트 실패는 추락으로 이어질 수 있으므로, A/B 파티션 롤백, 체크섬 검증, 단계적 롤아웃이 필수입니다.

**팁**: 실제 OTA 업데이트 시스템 설계 경험과 안전 메커니즘을 구체적으로 설명하세요.

### Q211. ROS2에서 Node의 기본 개념은?
- ✅ 독립적인 실행 단위로 토픽/서비스/액션으로 다른 노드와 통신
-    데이터베이스 관리를 위한 서버 프로세스
-    하드웨어 드라이버 전용 실행 단위
-    네트워크 패킷 라우팅을 담당하는 컴포넌트

**해설**: ROS2 노드는 특정 기능을 수행하는 독립적인 실행 단위입니다. 각 노드는 Publisher/Subscriber(토픽), Server/Client(서비스), Action Server/Client(액션)을 통해 다른 노드와 통신합니다.

**팁**: ROS1 roscore와 달리 ROS2는 마스터 노드 없이 DDS를 통한 분산 통신을 사용합니다.

### Q212. ROS2에서 Topic과 Service의 차이는?
- ✅ Topic은 단방향 비동기 스트리밍, Service는 요청-응답 동기 통신
-    Topic은 대용량 데이터, Service는 소용량 데이터 전용
-    Service가 항상 더 빠른 통신
-    Topic은 1:1 통신, Service는 1:N 브로드캐스트

**해설**: Topic은 Publisher가 지속적으로 데이터를 발행하고 Subscriber가 비동기로 수신하는 스트리밍 방식입니다. Service는 Client가 요청을 보내고 Server의 응답을 대기하는 동기적 RPC(Remote Procedure Call) 방식입니다.

**팁**: 드론에서 센서 데이터는 Topic, 명령 실행 확인이 필요한 작업은 Service, 장시간 실행 작업은 Action을 사용합니다.

### Q213. Git에서 feature branch 개발 후 main 브랜치에 병합하는 권장 워크플로우는?
- ✅ feature 브랜치에서 개발 → PR(Pull Request) 생성 → 코드 리뷰 → main에 merge → feature 브랜치 삭제
-    main 브랜치에 직접 커밋하여 빠른 개발
-    feature를 main에 force push
-    merge 없이 cherry-pick으로 개별 커밋만 적용

**해설**: Git Flow 또는 GitHub Flow 워크플로우에서는 기능 개발을 별도 브랜치에서 진행하고 PR을 통한 코드 리뷰 후 main에 병합합니다. CI/CD 파이프라인이 PR에서 자동 실행되어 품질을 보장합니다.

**팁**: 드론 소프트웨어처럼 안전이 중요한 시스템에서는 2인 이상 리뷰 승인 후 merge되는 브랜치 보호 규칙이 필수입니다.

### Q214. Docker 컨테이너를 드론 소프트웨어 개발에 사용하는 주요 이점은?
- ✅ 환경 재현성 보장, 의존성 격리, 배포 일관성 유지
-    실시간 성능이 베어메탈보다 우수함
-    GPU 가속을 자동으로 최적화
-    하드웨어 드라이버를 포함하지 않아도 됨

**해설**: Docker는 개발/테스트/프로덕션 환경을 동일하게 유지합니다. ROS2, PX4 SITL 등 복잡한 의존성을 컨테이너로 묶어 '개발 PC에서는 되는데 배포하면 안 됨' 문제를 방지합니다.

**팁**: PX4 공식 Docker 이미지(px4io/px4-dev-*)를 사용하면 컴파일 환경 설정 없이 즉시 PX4 빌드 환경을 갖출 수 있습니다.

### Q215. Python asyncio에서 async/await를 드론 제어 코드에 사용하는 이유는?
- ✅ I/O 대기(네트워크/MAVLink) 중에도 다른 작업을 처리하여 블로킹 없이 효율적인 비동기 프로그래밍
-    멀티스레딩보다 CPU 사용량이 항상 적음
-    실시간 마감 시한(deadline) 보장
-    드론 제어는 반드시 asyncio를 사용해야 함

**해설**: 드론 컨트롤 코드는 MAVLink 응답 대기, 텔레메트리 수신, 여러 센서 폴링을 동시에 해야 합니다. asyncio로 단일 스레드에서 비동기 I/O를 처리하면 컨텍스트 스위칭 오버헤드 없이 효율적입니다.

**팁**: MAVSDK Python은 asyncio 기반으로 설계되어 있으며 모든 API가 coroutine입니다. async main()과 asyncio.run()으로 진입합니다.

### Q216. Gazebo 시뮬레이터와 ROS2를 연동하기 위해 사용하는 패키지는?
- ✅ ros_gz (ros_ign_bridge 후속), gazebo_ros_pkgs
-    gazebo_bridge_core
-    ros2_gazebo_connector
-    px4_gz_simulator

**해설**: ros_gz(구 ros_ign_bridge)는 Gazebo Harmonic/Fortress와 ROS2 사이의 토픽 브릿지를 제공합니다. 기존 gazebo_ros_pkgs는 classic Gazebo(Gazebo 11)용입니다.

**팁**: PX4 v1.14+는 Gazebo(gz)를 기본 시뮬레이터로 사용하며, ros2 launch px4_bringup으로 전체 시뮬레이션 스택을 시작합니다.

### Q217. CI/CD 파이프라인에서 드론 소프트웨어의 단위 테스트 자동화 이점은?
- ✅ 코드 변경마다 자동 테스트 실행으로 회귀 버그 조기 발견 및 배포 신뢰성 향상
-    단위 테스트는 하드웨어 테스트를 완전히 대체
-    CI/CD는 임베디드 코드에는 적용 불가
-    테스트 자동화는 소프트웨어 복잡도를 증가시킴

**해설**: 드론 소프트웨어는 버그가 치명적 사고로 이어질 수 있습니다. GitHub Actions/GitLab CI로 모든 PR에서 단위 테스트, 정적 분석, SITL 비행 테스트를 자동 실행하면 품질 게이트가 강화됩니다.

**팁**: PX4와 ArduPilot 모두 CI에서 SITL 자동 테스트를 수행합니다. 모든 PR이 이 테스트를 통과해야 병합 가능합니다.

### Q218. ROS2에서 QoS(Quality of Service) 프로파일 중 SENSOR_DATA의 특성은?
- ✅ Best Effort 신뢰성, Volatile 내구성, 작은 history depth로 센서 데이터의 최신값 우선 처리
-    Reliable 신뢰성, Transient Local 내구성으로 데이터 손실 없이 전달
-    낮은 주파수 데이터 전용
-    레이턴시보다 처리량을 우선시하는 설정

**해설**: SENSOR_DATA QoS 프로파일은 Best Effort(패킷 손실 허용)와 Volatile(히스토리 없음)로 설정되어 최신 센서 데이터를 낮은 지연으로 처리합니다. 오래된 센서 데이터는 의미가 없기 때문입니다.

**팁**: 기체 위치/자세같은 빠른 센서 토픽에는 SENSOR_DATA, 미션/지오펜스 등 중요 설정 데이터에는 SYSTEM_DEFAULT(Reliable) 사용이 권장됩니다.

### Q219. 임베디드 C에서 volatile 키워드를 사용하는 이유는?
- ✅ 컴파일러 최적화로 인한 레지스터 캐싱을 방지하여 항상 메모리에서 값을 읽도록 강제
-    변수를 상수로 선언하여 변경 불가하게 함
-    인터럽트 우선순위를 높이기 위한 키워드
-    변수를 플래시 메모리에 저장하기 위해

**해설**: 인터럽트 핸들러나 다른 스레드에서 수정되는 변수를 volatile로 선언하면 컴파일러가 최적화로 이전 값을 캐싱하지 않고 매번 메모리에서 읽습니다. 하드웨어 레지스터 접근에도 필수입니다.

**팁**: RTOS 환경에서 태스크 간 공유 변수는 volatile 외에 뮤텍스나 세마포어로 레이스 컨디션도 방지해야 합니다.

### Q220. 드론 소프트웨어에서 단위 테스트 Mock(모의 객체)을 사용하는 이유는?
- ✅ 실제 하드웨어(GPS, IMU) 없이 하드웨어 의존 코드를 테스트하기 위해
-    테스트 속도를 높이기 위해서만 사용
-    Mock은 성능 테스트에만 사용
-    Mock을 사용하면 실제 하드웨어 테스트가 불필요

**해설**: GPS 신호 없음, IMU 오류, 배터리 방전 등 위험한 엣지 케이스를 실제 하드웨어 없이 Mock으로 시뮬레이션하여 안전하게 테스트할 수 있습니다. 테스트 속도와 재현성도 향상됩니다.

**팁**: C++에서는 Google Mock(gMock), Python에서는 unittest.mock이 대표적인 Mock 프레임워크입니다.

### Q221. ROS2에서 LifecycleNode를 일반 Node 대신 사용하는 이유는?
- ✅ 초기화/활성화/비활성화/정리 상태를 명시적으로 관리하여 안전한 시스템 시작/종료 순서 보장
-    LifecycleNode가 일반 Node보다 빠른 통신 성능 제공
-    LifecycleNode는 실시간 제어에만 사용
-    메모리 사용량을 줄이기 위해

**해설**: LifecycleNode는 Unconfigured → Inactive → Active → Finalized 상태 전환을 명시적으로 제어합니다. 드론 시스템에서 센서, 제어기, 통신 노드를 올바른 순서로 초기화하고 오류 시 안전하게 정리하는 데 필수입니다.

**팁**: ros2 lifecycle set /node_name activate 명령으로 노드 상태를 수동 전환하거나, 런치 파일에서 launch.actions.EmitEvent로 자동화할 수 있습니다.

### Q222. FreeRTOS에서 Queue를 사용하여 인터럽트 서비스 루틴(ISR)과 태스크 간 안전하게 데이터를 전달하는 방법은?
- ✅ ISR에서는 xQueueSendFromISR(), 태스크에서는 xQueueReceive()를 사용하며, portYIELD_FROM_ISR()로 컨텍스트 스위치 트리거
-    ISR과 일반 태스크 모두 xQueueSend()를 사용하되 ISR 내부에서 taskENTER_CRITICAL()로 임계 구역을 설정하면 스케줄러 충돌을 방지할 수 있다
-    공유 메모리 영역을 volatile uint8_t 배열로 선언하고 원자적 읽기·쓰기가 보장되는 32비트 레지스터만 사용하면 큐 없이 안전하게 전달된다
-    ISR 내에서 직접 태스크 핸들러 함수를 호출하면 스택이 공유되어 태스크 컨텍스트에서 실행되므로 일반 FreeRTOS API를 그대로 사용 가능하다

**해설**: FreeRTOS는 ISR 전용 API(FromISR 접미사)를 사용해야 합니다. 일반 API는 스케줄러를 호출할 수 있어 ISR에서 사용 불가합니다. portYIELD_FROM_ISR()으로 ISR 종료 후 즉시 컨텍스트 스위치를 요청합니다.

**팁**: FreeRTOS ISR 안전 API: xQueueSendFromISR, xSemaphoreGiveFromISR, xTimerStartFromISR. 일반 API를 ISR에서 사용하면 Hard Fault가 발생합니다.

### Q223. C++ 드론 제어 코드에서 RAII(Resource Acquisition Is Initialization) 패턴의 장점은?
- ✅ 객체 생성 시 리소스 획득, 소멸 시 자동 해제로 예외 발생 시에도 리소스 누수 방지
-    메모리 사용량을 최소화하는 최적화 기법
-    컴파일 시간에 모든 오류를 감지하는 패턴
-    멀티스레드 안전성을 자동으로 보장

**해설**: 드론 제어 코드에서 파일, 네트워크 소켓, 뮤텍스를 RAII로 관리하면 예외나 조기 반환 시에도 소멸자가 항상 호출되어 리소스가 정리됩니다. std::unique_ptr, std::lock_guard가 대표적 RAII입니다.

**팁**: 임베디드 C++에서는 예외를 사용하지 않는 경우도 많지만 RAII는 여전히 리소스 관리에 유용합니다.

### Q224. ROS2 px4_ros_com 패키지를 사용하여 PX4와 통신할 때 uXRCE-DDS 에이전트를 시작하는 방법은?
- ✅ MicroXRCEAgent udp4 -p 8888 명령으로 에이전트를 시작하고 PX4 SITL이나 기체에서 에이전트에 연결
-    rosbridge_server를 사용하여 JSON으로 변환
-    MAVLink ros_mavros 패키지로 대체 가능
-    PX4에서 ROS2 클라이언트 라이브러리를 직접 임포트

**해설**: PX4의 uXRCE-DDS 클라이언트가 에이전트(MicroXRCEAgent)에 연결하면 uORB 토픽이 ROS2 DDS 도메인으로 브릿지됩니다. SITL에서는 UDP, 실기체에서는 직렬(UART) 연결을 사용합니다.

**팁**: MicroXRCEAgent udp4 -p 8888 &로 백그라운드 실행 후 ROS2 노드에서 /fmu/* 토픽이 나타나는지 ros2 topic list로 확인합니다.

### Q225. 드론 REST API 서버 설계에서 /api/v1/command/takeoff 엔드포인트의 HTTP 메서드로 올바른 것은?
- ✅ POST (명령 실행은 부수 효과가 있는 동작으로 POST가 적합)
-    GET (상태 변경 없이 안전)
-    PUT (자원 전체 교체)
-    DELETE (리소스 제거)

**해설**: 이륙 명령처럼 서버 상태를 변경하거나 부수 효과가 있는 동작은 HTTP POST를 사용합니다. GET은 안전한(safe) 조회 전용, PUT은 자원 교체, DELETE는 자원 삭제에 사용합니다.

**팁**: REST API 설계에서 명령(command)과 쿼리(query)를 분리하는 CQRS 패턴을 적용하면 드론 제어 API를 체계적으로 설계할 수 있습니다.

### Q226. Python으로 드론 실시간 텔레메트리를 WebSocket으로 클라이언트에 전송할 때 asyncio와 aiohttp를 사용하는 구조는?
- ✅ asyncio.gather()로 MAVLink 수신 coroutine과 WebSocket 브로드캐스트 coroutine을 동시 실행, asyncio.Queue로 데이터 전달
-    별도 스레드에서 WebSocket 서버 실행, 메인에서 MAVLink 수신
-    동기 방식으로 순차 처리(텔레메트리 수신 후 WebSocket 전송)
-    멀티프로세싱으로 MAVLink와 WebSocket을 별도 프로세스로 분리

**해설**: asyncio.gather()로 여러 coroutine을 동시에 실행하고, asyncio.Queue를 통해 MAVLink 수신 coroutine이 데이터를 큐에 넣으면 WebSocket broadcast coroutine이 소비하는 패턴이 효율적입니다.

**팁**: aiohttp의 WebSocketResponse를 사용하면 asyncio와 자연스럽게 통합됩니다. 연결 관리를 위해 접속한 클라이언트를 Set으로 관리하고 브로드캐스트합니다.

### Q227. ROS2에서 tf2 라이브러리를 드론에 사용하는 주요 목적은?
- ✅ 기체, 센서, 지도 등 여러 좌표 프레임 간 변환(Translation/Rotation)을 시간 기반으로 관리
-    ROS 토픽의 타입 변환 도구
-    센서 데이터의 단위 변환(m/s² ↔ g 등)
-    GPS 좌표를 로컬 좌표로 변환하는 전용 라이브러리

**해설**: tf2는 world → map → odom → base_link → sensor_link와 같은 좌표 프레임 트리를 관리합니다. 특정 시각의 프레임 간 변환을 조회하여 센서 데이터를 다른 프레임으로 변환할 수 있습니다.

**팁**: 드론 SLAM에서 tf2 트리 구성은 필수이며, ros2 run tf2_tools view_frames로 전체 트리를 시각화하여 변환 경로를 확인합니다.

### Q228. Gazebo에서 드론 플러그인을 개발할 때 gz::sim::System 인터페이스에서 PreUpdate(), Update(), PostUpdate() 의 실행 순서와 역할 차이는?
- ✅ PreUpdate는 컨트롤 입력 처리, Update는 물리 시뮬레이션 진행, PostUpdate는 시뮬레이션 결과 읽기(읽기 전용)
-    모든 함수가 동일한 역할이며 순서 무관
-    Update만 존재하며 Pre/Post는 옵션
-    PostUpdate에서 물리 엔진에 힘을 적용

**해설**: Gazebo System 인터페이스: PreUpdate는 물리 스텝 전에 호출되어 모터 힘/토크 등 제어 입력을 ECW에 쓰기, Update는 물리 스텝 실행, PostUpdate는 물리 스텝 후 읽기 전용으로 위치/자세 등 결과를 읽습니다.

**팁**: PostUpdate에서는 ECW 쓰기가 허용되지 않습니다. 물리 결과를 읽어 ROS2 토픽으로 발행하는 코드를 PostUpdate에 구현합니다.

### Q229. 드론 소프트웨어의 메모리 관리에서 동적 메모리 할당(malloc/new)을 비행 중 코드에서 최소화해야 하는 이유는?
- ✅ 힙 단편화로 인한 예측 불가능한 메모리 부족, 할당 시간 변동으로 실시간 제약 위반 가능성
-    동적 할당이 정적 할당보다 항상 느림
-    임베디드 시스템에서 malloc이 미구현
-    동적 메모리는 재부팅 후 해제됨

**해설**: 실시간 시스템에서 malloc/new는 실행 시간이 가변적이며 힙 단편화로 갑자기 실패할 수 있습니다. 비행 중 제어 루프에서는 정적 배열, 스택 메모리, 또는 사전 할당된 풀 메모리를 사용합니다.

**팁**: PX4 펌웨어는 비행 중 new/delete를 금지하는 코드 스타일 가이드를 따릅니다. 초기화 시 한 번만 할당하고 이후 재사용합니다.

### Q230. ROS2 Action Server를 드론 임무 실행에 사용할 때 Service 대신 Action을 선택하는 이유는?
- ✅ 장시간 실행 작업에서 진행 상황 피드백과 중간 취소(Cancel)가 가능
-    Action이 Service보다 빠른 응답 속도
-    Service는 1:1 통신만 가능하지만 Action은 1:N 가능
-    Action은 UDP 기반으로 더 낮은 지연

**해설**: 드론 임무 비행은 수 분이 걸릴 수 있습니다. Service는 응답까지 블로킹이며 취소 불가입니다. Action은 Goal 전송 → 진행 Feedback 스트림 → 최종 Result 구조로 장시간 작업에 적합하며 중간 취소도 가능합니다.

**팁**: Nav2(ROS2 Navigation)도 Action 기반으로 설계되어 있습니다. NavigateToPose Action Goal을 전송하고 피드백으로 현재 위치를 받는 구조입니다.

### Q231. 드론 소프트웨어의 CI/CD에서 정적 분석 도구(clang-tidy, cppcheck)를 사용하는 목적은?
- ✅ 컴파일 없이 소스 코드를 분석하여 널 포인터 역참조, 버퍼 오버플로우, 미초기화 변수 등 버그를 조기 발견
-    런타임 성능 최적화를 위한 프로파일링
-    코드 포맷팅 자동화
-    메모리 누수 감지(실행 기반)

**해설**: 정적 분석(Static Analysis)은 코드를 실행하지 않고 분석하여 논리 오류, 보안 취약점, 코딩 표준 위반을 발견합니다. 임베디드/안전 소프트웨어에서는 MISRA C++ 등 코딩 표준 준수 확인에도 사용됩니다.

**팁**: PX4 CI에서 clang-tidy가 자동 실행되며 위반 시 PR이 거부됩니다. 로컬에서 pre-commit hook으로 설정하면 조기 발견이 가능합니다.

### Q232. ROS2에서 intra-process communication(프로세스 내 통신)을 활성화하면 얻는 이점은?
- ✅ 동일 프로세스 내 노드 간 메시지를 직렬화/복사 없이 포인터로 직접 전달하여 제로 카피(zero-copy) 달성
-    다른 프로세스와의 통신 속도 향상
-    네트워크 보안을 강화
-    DDS 미들웨어를 우회하여 레이턴시 감소

**해설**: intra-process communication을 활성화하면 같은 컴포넌트 컨테이너 내 노드들이 메시지를 복사하지 않고 shared_ptr로 직접 전달합니다. 고주파(1kHz+) 센서 데이터 처리에서 CPU와 메모리 사용량을 크게 줄입니다.

**팁**: rclcpp::Node 생성 시 NodeOptions().use_intra_process_comms(true)로 활성화하며, rclcpp_components::ComponentManager에 로드해야 합니다.

### Q233. SITL 시뮬레이션에서 기체 파라미터 파일을 자동으로 재설정하는 이유와 방법은?
- ✅ 이전 테스트의 파라미터 변경이 다음 테스트에 영향을 주지 않도록 매 테스트 시작 시 기본값으로 초기화. ArduPilot은 -w 플래그, PX4는 param reset all 명령 사용
-    SITL은 기동 시 항상 내장 고정 기본 파라미터 스냅샷에서 재시작하는 구조여서 테스트 간 파라미터 오염이 발생하지 않으므로 별도 초기화 절차가 불필요함
-    파라미터 초기화 플래그(-w)는 내부 플래시 에뮬레이션 영역을 전체 삭제하며, 이는 실제 하드웨어의 플래시 지우기(mass erase all) 동작과 완전히 동일함
-    SITL 환경에서는 파라미터 값이 휘발성 RAM에만 존재하여 프로세스 종료 시 자동 소멸되므로, 소프트웨어 save 명령이나 -w 초기화 명령이 모두 무효임

**해설**: CI/CD 자동 비행 테스트에서 각 테스트는 독립적이어야 합니다. ArduPilot SITL은 sim_vehicle.py에 -w(wipe) 플래그로, PX4 SITL은 부팅 시 param reset을 실행하여 파라미터를 초기화합니다.

**팁**: 테스트 격리를 위해 각 SITL 인스턴스를 별도 임시 디렉토리에서 실행하는 것도 좋은 방법입니다.

### Q234. 드론 컴패니언 컴퓨터에서 웹소켓 서버와 MAVLink 통신을 동시에 처리하는 멀티스레드 아키텍처의 핵심 설계는?
- ✅ MAVLink 수신 스레드 → Thread-safe Queue → 웹소켓 브로드캐스트 스레드 분리, 공유 상태는 뮤텍스로 보호
-    단일 스레드에서 선택적으로 처리(poll 방식)
-    모든 처리를 메인 스레드에서 순차 실행
-    MAVLink와 WebSocket을 동일 소켓으로 다중화

**해설**: MAVLink 수신은 블로킹 I/O이고 WebSocket 브로드캐스트는 지연 없이 처리해야 합니다. 두 기능을 별도 스레드로 분리하고 스레드 안전 큐(thread-safe queue)를 통해 데이터를 교환하는 설계가 안정적입니다.

**팁**: Python에서는 asyncio + aiohttp, C++에서는 Boost.Asio + WebSocketpp 조합이 고성능 비동기 서버 구현에 적합합니다.

### Q235. ROS2 런치 파일에서 드론 소프트웨어 스택을 구성할 때 조건부 노드 시작(기체 타입에 따라 다른 노드 실행)을 구현하는 방법은?
- ✅ launch_arguments와 LaunchConfiguration, IfCondition/UnlessCondition Substitution으로 런치 시 조건부 노드 포함/제외
-    DeclareLaunchArgument와 PushRosNamespace를 조합하여 기체 타입별 네임스페이스를 생성하고 각 네임스페이스 안에서 고정 노드 세트를 일괄 실행
-    런치 파일에서 os.environ으로 환경 변수를 직접 읽고 Python 조건문으로 Node 객체 생성 여부를 제어하여 기체 타입별 노드 구성을 결정
-    ROS2 컴포넌트 컨테이너(Composable Node)를 기체 타입별로 별도 생성하고 LoadComposableNodes 액션으로 런치 시 동적으로 플러그인을 선택 로드

**해설**: ros2 launch ... vehicle_type:=quadrotor와 같이 인수를 전달하면 LaunchConfiguration('vehicle_type')으로 읽고 IfCondition으로 조건부 노드를 포함합니다. 기체 타입별 하드웨어 드라이버를 선택적으로 로드할 수 있습니다.

**팁**: 복잡한 런치 로직은 Python 런치 파일로 구현하고, 재사용 가능한 구성 요소는 별도 런치 파일로 분리 후 IncludeLaunchDescription으로 포함합니다.

### Q236. 실시간 스케줄링(SCHED_FIFO, SCHED_RR)을 드론 컴패니언 컴퓨터 Linux에서 사용할 때 우선순위 역전(Priority Inversion) 문제와 해결책은?
- ✅ 낮은 우선순위 태스크가 자원을 잠그고 높은 우선순위 태스크가 대기하는 현상으로, Priority Inheritance Protocol 지원 뮤텍스(pthread_mutexattr_setprotocol PTHREAD_PRIO_INHERIT)로 해결
-    SCHED_FIFO 스케줄러는 타임 슬라이스 없이 CPU를 독점하므로 낮은 우선순위 태스크가 뮤텍스를 보유 중이라도 높은 우선순위 태스크가 즉시 CPU를 선점 가능하여 우선순위 역전이 구조적으로 발생하지 않음
-    우선순위 역전은 높은 우선순위 태스크에 cpu_setaffinity 시스템 콜로 특정 물리 코어를 고정 할당하면, 다른 코어에서 낮은 우선순위 태스크가 뮤텍스를 잠그더라도 CPU 교차 영향이 완전히 차단되어 해결됨
-    리눅스 커널 v5.x 이상부터는 PREEMPT_RT 패치 없는 기본 메인라인 커널에서도 실시간 스케줄러가 우선순위 역전 상태를 자동으로 감지하여 중간 우선순위 태스크를 일시 중단하고 역전 상태를 방지하여 처리함

**해설**: 우선순위 역전은 낮은 우선순위 T1이 뮤텍스 보유 → 중간 우선순위 T2가 T1을 선점 → 높은 우선순위 T3가 뮤텍스 대기하는 상황입니다. Priority Inheritance 뮤텍스는 T1의 우선순위를 T3 수준으로 임시 상승시켜 해결합니다.

**팁**: 화성 패스파인더 탐사선 사고가 우선순위 역전으로 인한 실시간 시스템 실패의 유명한 사례입니다.

### Q237. ROS2 Executor 설계에서 SingleThreadedExecutor vs MultiThreadedExecutor vs StaticSingleThreadedExecutor의 차이와 드론 시스템에 적합한 선택은?
- ✅ StaticSingleThreadedExecutor는 초기화 시 콜백 그래프를 분석하여 런타임 오버헤드 최소화로 실시간 성능 우선. MultiThreaded는 CPU 병렬성 활용. 제어 루프는 Static, 고수준 계획은 Multi 권장
-    MultiThreadedExecutor는 모든 콜백을 스레드 풀로 분산 처리하여 CPU 코어 수만큼 병렬 실행하므로, 제어 루프·고수준 계획을 구분하지 않고 모든 상황에서 항상 최적의 실시간 성능을 제공함
-    SingleThreadedExecutor는 모든 콜백을 단일 스레드로 순차 처리하고 콜백 간 락 충돌이 없으므로 제어 루프·고수준 계획 구분 없이 드론 시스템 전체에 항상 적용하는 것이 안전하고 검증된 선택임
-    Executor 종류 선택은 코드 구조와 가독성에만 영향을 주며, 동일한 콜백 집합을 등록하면 SingleThreaded·MultiThreaded·StaticSingleThreaded 모두 동일한 레이턴시와 처리량을 보임

**해설**: StaticSingleThreadedExecutor는 런타임에 콜백 추가/제거가 없는 경우 콜백 실행 경로를 사전 계산하여 오버헤드를 최소화합니다. 제어 루프처럼 예측 가능한 타이밍이 중요한 곳에 적합합니다. MultiThreaded는 I/O 바운드 작업의 병렬 처리에 유리합니다.

**팁**: rclcpp::executors::StaticSingleThreadedExecutor executor; executor.add_node(node); executor.spin(); 패턴으로 사용합니다.

### Q238. 드론 소프트웨어에서 상태 머신(State Machine) 패턴을 구현할 때 Boost.Statechart 또는 Boost.MSM 대신 ROS2 생태계의 BehaviorTree.CPP(BT.CPP)를 선택하는 이유는?
- ✅ 행동 트리는 상태 전환 로직을 분리하여 재사용 가능한 노드로 조합하고 런타임 동적 수정이 가능. Groot2 GUI로 시각적 설계/디버깅 가능, ROS2 통합 용이
-    Boost.MSM은 UML2 상태 차트를 코드로 1:1 구현하지만 상태 수 증가 시 컴파일 시간이 지수적으로 증가하고 런타임 수정이 불가능하여 드론 임무 변경에 부적합
-    smach(Python 상태 머신 라이브러리)는 ROS2 네이티브 지원이 부족하고 비동기 상태 전환에 취약하여 실시간 드론 임무 제어 아키텍처에 적합하지 않음
-    Boost.Statechart는 타입 안전 상태 전환을 제공하지만 행동 트리와 달리 선점형 실행 및 서브트리 재사용이 구조적으로 어려워 복잡 임무 조합에 한계

**해설**: 행동 트리(BT)는 반응형 실행(reactive execution)으로 조건 변화에 빠르게 대응합니다. Fallback/Sequence/Parallel 노드 조합으로 복잡한 임무 로직을 가독성 있게 표현하며 Nav2, MoveIt2가 BT.CPP를 표준으로 채택했습니다.

**팁**: BT.CPP와 Groot2를 사용하면 비행 중 행동 트리 실행 상태를 실시간 시각화하여 디버깅할 수 있습니다.

### Q239. 드론 비전 처리 파이프라인에서 CUDA 가속 이미지 처리와 ROS2 제어 노드 간 데이터 공유 시 Zero-Copy 전송을 달성하는 방법은?
- ✅ CUDA IPC(Inter-Process Communication) 핸들 또는 NvBufSurface(Jetson)를 사용하여 GPU 메모리를 복사 없이 공유, rclcpp::LoanedMessage로 DDS 제로카피 활용
-    GPU 처리 후 cudaMemcpy로 CPU 호스트 메모리에 복사하고 cv::Mat로 래핑하여 sensor_msgs/Image로 직렬화하여 토픽으로 발행하는 것이 ROS2 표준 통합 방법임
-    CUDA 커널과 ROS2 노드는 프로세스 메모리 공간이 완전히 분리되어 직접 통합이 구조적으로 불가하므로, 별도 gRPC 서버 프로세스를 통해 직렬화된 Protobuf 데이터를 교환해야 함
-    GPU 추론 결과를 /tmp 공유 메모리 파일 시스템에 저장하고 inotify 파일 변경 이벤트를 통해 제어 노드가 자동으로 감지하여 읽어가는 파일 기반 IPC 방식이 Jetson 표준 구성임

**해설**: Jetson 플랫폼에서 NvBufSurface API로 GPU-CPU 공유 메모리를 사용하면 복사 없이 비전 처리 결과를 제어 노드와 공유할 수 있습니다. rclcpp의 Loaned Message API와 결합하면 DDS 계층에서도 복사를 최소화합니다.

**팁**: NVIDIA Isaac ROS 패키지가 Jetson에서 ROS2와 CUDA를 제로카피로 통합하는 최적화된 구현을 제공합니다.

### Q240. 드론 소프트웨어 릴리즈 전 수행하는 Hardware-In-The-Loop(HITL) CI 자동화 구축 시 핵심 과제는?
- ✅ 실제 FC를 CI 서버에 물리 연결하여 펌웨어 플래시 자동화, 시리얼 포트 할당 관리, 테스트 통과/실패 판단 기준(비행 메트릭) 정의, 하드웨어 오류와 소프트웨어 오류 구분
-    SITL(소프트웨어 인더루프) 테스트를 먼저 완전 자동화하고 결과가 통과된 PR만 HITL 대기열에 진입하도록 CI 워크플로우를 2단계로 구성하여 리소스 절약
-    FC를 USB 연결하지 않고 JTAG/SWD 디버거를 CI 서버에 연결하여 펌웨어를 직접 플래시하고 MAVSDK Python으로 비행 시나리오를 자동 검증
-    self-hosted GitHub Actions 러너를 FC 보드 옆에 물리 배치하고 udev 규칙으로 보드별 고정 경로를 할당하여 병렬 HITL 테스트 파이프라인을 구성

**해설**: HITL CI는 FC를 USB/직렬로 서버에 연결하고 GitHub Actions self-hosted runner 또는 GitLab Runner를 하드웨어 옆에 배치합니다. pyserial로 펌웨어 업로드, MAVSDK 테스트 스크립트로 비행 동작 검증, 결과를 JUnit XML로 리포팅하는 파이프라인을 구성합니다.

**팁**: 다수의 FC 보드를 관리하기 위해 USB 허브와 udev 규칙을 활용하여 보드별 고정 디바이스 경로(/dev/drone_fc_1)를 할당하는 것이 운용에 편리합니다.

### Q241. PX4 모듈에서 px4::WorkItem(work queue 기반)과 px4::ScheduledWorkItem을 일반 태스크(task_spawn) 대신 선택하는 이유는?
- ✅ Work Queue는 단일 스레드로 여러 콜백을 순차 실행하여 태스크별 스레드 생성 오버헤드와 스택 메모리를 줄이며, 주기적/이벤트 기반 처리에 최적화
-    Work Queue가 항상 더 빠른 응답 시간
-    task_spawn은 PX4에서 더 이상 사용되지 않음
-    Work Queue는 실시간 제약이 없는 모듈에만 사용

**해설**: PX4에서 각 모듈을 별도 태스크로 실행하면 많은 스택 메모리와 컨텍스트 스위칭 비용이 발생합니다. Work Queue 기반 모듈은 공유 스레드에서 실행되어 메모리 효율이 높으며 PX4 v1.13+에서 권장되는 패턴입니다.

**팁**: ScheduledWorkItem::ScheduleOnInterval(interval_us)으로 주기적 실행, ScheduleNow()로 즉시 실행을 트리거합니다.

### Q242. 드론 소프트웨어에서 Protobuf(Protocol Buffers)를 MAVLink 대신 내부 컴포넌트 간 통신에 사용하는 장단점은?
- ✅ 장점: 스키마 기반 타입 안전성, 언어 중립, 효율적 직렬화. 단점: MAVLink 기존 도구 미지원, 드론 특화 메시지 없음, 추가 직렬화 레이어 복잡도
-    Protobuf가 MAVLink보다 모든 면에서 우월
-    MAVLink이 Protobuf보다 더 작은 패킷 크기 보장
-    Protobuf는 실시간 시스템에 적합하지 않음

**해설**: Protobuf는 컴패니언 컴퓨터 내부 마이크로서비스 간 통신에 유용합니다. 단, 기존 MAVLink GCS 도구(QGC, MAVSDK)와 직접 호환되지 않으며 드론 특화 메시지(HEARTBEAT, COMMAND 등)를 별도 정의해야 합니다.

**팁**: gRPC + Protobuf 조합은 컴패니언 컴퓨터 내부 마이크로서비스 아키텍처에 적합하며, 외부 MAVLink 인터페이스와 분리하여 설계하면 좋습니다.

### Q243. ROS2 보안(ROS2 Security, SROS2)에서 DDS 보안 플러그인을 통한 드론 시스템 보호 방법은?
- ✅ 인증(Authentication), 접근 제어(Access Control), 암호화(Encryption) 세 가지 DDS 보안 플러그인으로 특정 노드만 지정 토픽에 접근하도록 제한하고 통신을 TLS 암호화
-    ROS2는 별도 보안 프레임워크 없이 호스트 OS 방화벽(iptables/nftables)과 네트워크 격리(VLAN)에 의존하며, SROS2 플러그인은 실험적 단계로 실제 드론 시스템 적용 사례가 없음
-    SROS2의 DDS 보안 플러그인은 AES-256 암호화로 인해 레이턴시가 30~50% 증가하여 1kHz 제어 루프 요구사항을 충족할 수 없으므로 실시간 드론 시스템에서는 사용이 권장되지 않음
-    DDS는 UDP 멀티캐스트 기반이어서 TCP/TLS 스택을 사용하는 표준 암호화 라이브러리를 직접 적용할 수 없으므로, DDS 계층의 통신 암호화 구현은 기술적으로 불가능함

**해설**: SROS2는 PKI 기반 인증서로 노드를 인증하고, XML 정책 파일로 각 노드가 발행/구독 가능한 토픽을 제한합니다. AES-256 암호화로 DDS 트래픽을 보호합니다. ros2 security create_enclave로 노드별 인증서를 생성합니다.

**팁**: SROS2 도입 시 약 10~20%의 레이턴시 오버헤드가 발생할 수 있습니다. 실시간 제어 토픽과 일반 데이터 토픽을 분리하여 선택적으로 적용하는 전략을 검토하세요.

### Q244. 드론 컴패니언 컴퓨터에서 CPU 격리(cpusets)와 실시간 Linux 커널(PREEMPT_RT)을 사용하는 목적과 설정 방법은?
- ✅ 특정 CPU 코어를 제어 루프 전용으로 격리(isolcpus=)하고 PREEMPT_RT 패치로 커널 선점 지연을 최소화하여 마이크로초 단위 실시간 제약 충족
-    CPU 격리는 단순히 처리 속도를 높이기 위한 오버클럭
-    PREEMPT_RT는 드론에 적용 불가능한 서버 전용 기술
-    CPU 격리는 멀티코어 사용을 금지하는 설정

**해설**: isolcpus=2,3 부팅 파라미터로 코어 2,3을 OS 스케줄러에서 격리하고 실시간 태스크에 taskset으로 할당합니다. PREEMPT_RT 패치로 커널 인터럽트 처리 지연을 줄여 50μs 이하의 예측 가능한 레이턴시를 달성합니다.

**팁**: cyclictest 도구로 시스템의 실시간 지연 분포를 측정하여 PREEMPT_RT 적용 전후를 비교할 수 있습니다.

### Q245. PX4 커스텀 uORB 메시지를 추가할 때 필요한 작업 순서는?
- ✅ msg/My_message.msg 파일 정의 → CMakeLists.txt에 등록 → 재빌드로 헤더 자동 생성 → 모듈에서 #include <uORB/topics/my_message.h> 사용
-    C 헤더 파일에 구조체를 직접 정의하고 orb_advertise() 호출 시 토픽 이름·구조체 크기를 수동으로 등록하면 .msg 파일 없이도 커스텀 uORB 토픽을 사용할 수 있음
-    Python 기반 px4_ros2 패키지의 msg_generator.py 스크립트가 커스텀 메시지 생성을 전담하며, .msg 파일 정의와 CMakeLists 수정 없이 Python 코드만으로 메시지 추가가 가능함
-    기존 uORB 메시지의 MSG_INHERIT 지시어를 통해 필드를 상속·확장하면 새 .msg 파일 생성과 재빌드 없이 커스텀 필드를 추가하는 것이 PX4 공식 권장 방법임

**해설**: PX4 uORB 메시지는 .msg 파일로 ROS 메시지 형식과 유사하게 정의합니다. msg/CMakeLists.txt에 등록 후 빌드 시 mavgen과 유사한 도구가 C 헤더를 자동 생성합니다. 토픽 이름은 파일명의 소문자 버전이 됩니다.

**팁**: uORB 메시지는 타임스탬프(uint64 timestamp) 필드를 항상 첫 번째로 포함해야 합니다. 이 필드로 EKF와 다른 소비자가 데이터 신선도를 확인합니다.

### Q246. 드론 소프트웨어에서 하드웨어 추상화 계층(HAL, Hardware Abstraction Layer)을 설계해야 하는 이유와 인터페이스 설계 원칙은?
- ✅ 하드웨어 변경(FC 교체, IMU 다양화) 시 상위 알고리즘 코드 수정 없이 HAL 구현만 교체 가능. 순수 가상 인터페이스로 의존성 역전 원칙(DIP) 적용
-    추상 레이어를 두면 함수 호출 오버헤드가 발생하여 500Hz 이상 제어 루프가 필요한 드론 FC 임베디드에서는 인라인 직접 접근이 권장된다
-    동일 FC 플랫폼을 3년 이상 유지하는 방산 프로젝트에서는 하드웨어 변경 빈도가 낮아 HAL 설계 비용이 실익을 초과하므로 불필요하다
-    HAL은 Linux 커널이나 RTOS 공급업체가 BSP 형태로 제공하는 레이어이므로 드론 애플리케이션 개발자가 별도로 구현해서는 안 된다

**해설**: SOLID 원칙 중 DIP(Dependency Inversion Principle)를 적용하여 상위 제어 알고리즘이 구체적 하드웨어가 아닌 추상 인터페이스에 의존하게 합니다. 단위 테스트 시 Mock HAL로 하드웨어 없이 테스트가 가능해집니다.

**팁**: PX4의 px4::I2CSPIDriver는 I2C/SPI 드라이버의 HAL 패턴 예시입니다. 기체 HW 교체 시 드라이버 레이어만 교체하면 상위 코드 무변경으로 작동합니다.

### Q247. Gazebo Harmonic에서 드론 멀티에이전트 시뮬레이션 시 성능 병목을 해결하기 위한 최적화 기법은?
- ✅ headless 모드(-s serveronly) 실행, 기체별 물리 업데이트 주기 조정(update_rate), 불필요한 플러그인 비활성화, 기체 간 충돌 감지 레이어 분리
-    각 기체 인스턴스를 별도 Docker 컨테이너로 격리하고 컨테이너 간 공유 메모리 통신으로 물리 충돌 감지를 오프로드하여 Gazebo 서버 부하 분산
-    기체 간 물리 충돌 감지를 Gazebo 기본 엔진 대신 외부 커스텀 플러그인으로 처리하고 시각화 레이어를 별도 프로세스로 분리하여 시뮬레이션 성능 개선
-    단일 Gazebo 월드 대신 기체 수에 비례하는 다중 월드 인스턴스를 실행하고 별도 조율 서버가 기체 간 상호작용 데이터를 수집하여 통합 시뮬레이션 구성

**해설**: 대규모 군집 시뮬레이션에서 GUI 렌더링이 큰 오버헤드입니다. --headless 플래그로 렌더링을 비활성화하고, 물리 업데이트 주기를 250Hz에서 100Hz로 낮추면 기체당 CPU 사용량이 크게 줄어듭니다. 기체 간 충돌 감지도 임무에 따라 선택적 비활성화를 검토합니다.

**팁**: Gazebo에서 10개 이상의 드론을 시뮬레이션하려면 최소 64GB RAM과 고성능 CPU(16코어+)가 필요합니다. 클라우드 인스턴스를 활용하는 방법도 고려하세요.

### Q248. 드론 소프트웨어의 Software Bill of Materials(SBOM) 관리와 공급망 보안이 중요한 이유는?
- ✅ 오픈소스 의존성의 CVE 취약점 추적, 라이선스 컴플라이언스 확인, 악성 패키지 주입(Dependency Confusion) 방지를 위해 모든 직간접 의존성 목록과 버전 고정 필요
-    SBOM은 구매자에게 소프트웨어 구성 목록을 마케팅 목적으로 공개하는 문서로, 실제 보안 취약점 추적이나 공급망 위협 방어와는 기능적으로 무관한 법적 요식 행위임
-    오픈소스 컴포넌트는 소스 코드가 공개되어 누구나 감사할 수 있으므로, 폐쇄형 상용 SW와 달리 공급망 보안 위험이 없어 SBOM 관리가 불필요함
-    SBOM 관리는 외부 판매용 상용 소프트웨어 제품에만 규제 의무가 적용되며, 내부 개발 드론 소프트웨어나 오픈소스 기반 시스템에는 해당 의무가 면제됨

**해설**: 방산 드론 소프트웨어는 수백 개의 오픈소스 의존성을 포함합니다. SBOM으로 log4shell 같은 취약점 발견 시 즉시 영향 받는 컴포넌트를 식별할 수 있습니다. Syft, FOSSA 등 SBOM 생성 도구를 CI에 통합합니다.

**팁**: 미국 NIST와 국방부는 방산 SW 조달 시 SBOM 제출을 필수화하는 방향으로 규제가 강화되고 있습니다.

### Q249. 드론 비행 소프트웨어 개발에서 DO-178C(항공 소프트웨어 인증)의 Design Assurance Level(DAL) A~E와 드론 상업화에 미치는 영향은?
- ✅ DAL A(치명적 실패 시 사망 가능성 최고)는 최고 수준의 테스트/검증 요구, 상업 드론은 최소 DAL C~D 요구. DAL A 인증은 수백만 달러의 비용과 수년의 검증 과정 필요
-    DO-178C는 유인 항공기 전용 표준이며 드론에는 ASTM F3269처럼 별도 경량화 표준이 적용되고 DAL 개념 대신 위험 등급(Risk Level)으로 검증 수준을 분류
-    DAL B 이상은 형식 검증(Formal Verification)이 의무화되어 소형 드론도 eVTOL과 동일한 인증 비용이 요구되며 설계 단계부터 독립 감사가 필수
-    DAL 등급이 높을수록 테스트 커버리지 요구는 낮아지고 대신 구조적 설계 문서화 요건이 강화되어 중소 드론 기업은 DAL A 인증이 상대적으로 용이

**해설**: 화물 드론(비거주 지역)은 DAL D~C, 도심 항공 교통(eVTOL, UAM)은 DAL B~A 수준이 요구됩니다. MC/DC(Modified Condition/Decision Coverage) 테스트, 형식 명세(Formal Specification), 추적성 매트릭스 등 엄격한 요구사항이 있습니다.

**팁**: 국내 드론 인증은 항공안전기술원(KIAST)에서 담당하며, 해외 수출 시 FAA (US) 또는 EASA (EU) 인증이 필요합니다.

### Q250. PX4 NuttX 기반 펌웨어에서 메모리 부족(OOM) 상황을 사전에 방지하는 방법은?
- ✅ up_mallinfo()로 힙 사용량 모니터링, SLAB/페이지 할당자 최소화, 스택 크기를 최소로 설정 후 up_check_stack()으로 스택 넘침 감지, 모듈 활성화 최소화
-    NuttX 태스크마다 고정 크기 메모리 풀을 사전 할당하고 동적 malloc 호출을 금지하며 태스크 스케줄러 통계로 최대 힙 사용량을 주기적으로 로깅
-    PX4 모듈을 비활성화하기 전에 uORB 토픽 통계로 각 모듈의 메시지 버퍼 점유량을 측정하고 최대 메모리 소비 모듈부터 순차적으로 스택 크기를 최적화
-    NuttX의 CONFIG_MM_REGIONS 파라미터로 힙 영역을 CCM·SRAM1·SRAM2로 분리하고 각 태스크에 적합한 메모리 영역을 컴파일 타임에 명시적으로 배정

**해설**: STM32 기반 FC의 RAM은 512KB~2MB로 제한적입니다. 각 태스크의 스택 크기를 최소화하고 canary 패턴(스택 끝에 마킹)으로 스택 오버플로우를 감지합니다. free 명령(NuttX shell)으로 실시간 힙 상태를 확인합니다.

**팁**: PX4에서 nsh> free 명령으로 힙 사용량을 확인하고, nsh> top 명령으로 각 태스크의 스택 사용량을 모니터링할 수 있습니다.

### Q251. 드론 군집 소프트웨어에서 분산 합의 알고리즘(Consensus Algorithm)이 필요한 상황은?
- ✅ 리더 선출, 군집 상태 동기화, 충돌 방지 경로 협상에서 기체 간 네트워크 파티션(분할) 상황에서도 일관성 있는 결정을 내리기 위해
-    단순 데이터 브로드캐스트로 충분하며 합의 알고리즘 불필요
-    합의 알고리즘은 서버 클러스터에만 적용
-    GPS가 있으면 합의 없이 중앙 집중 제어로 충분

**해설**: Raft, PBFT 같은 합의 알고리즘은 네트워크 지연이나 기체 장애 시 군집 전체가 일관된 결정(리더 선출, 임무 분배)을 내리게 합니다. 중앙 GCS 의존도를 낮춰 통신 두절 시에도 자율 임무 수행이 가능합니다.

**팁**: ROS2 DDS의 Discovery 메커니즘이 일종의 분산 상태 공유를 제공하지만 완전한 합의 프로토콜은 아닙니다. 단순 군집에는 중앙 조정, 고신뢰 군집에는 분산 합의를 검토하세요.

### Q252. PX4 SITL 자동화 테스트에서 특정 GPS 고장 시나리오(예: GPS 스푸핑)를 시뮬레이션하는 방법은?
- ✅ MAVLink COMMAND_LONG MAV_CMD_SET_GPS_GLOBAL_ORIGIN으로 가짜 GPS 좌표 주입 또는 PX4 SITL의 fault injection API(SYS_HITL 모드)로 GPS 센서 오류 시뮬레이션
-    GPS 스푸핑 시나리오는 실제 RF 신호 재머 장비를 SITL 컴퓨터 근처에 물리적으로 배치하여 소프트웨어 시뮬레이터 UDP 소켓 신호에 직접 간섭을 일으키는 방법만으로 현실적인 재현이 가능함
-    PX4 SITL의 GPS 스푸핑 시뮬레이션은 GPS 드라이버 소스 코드에서 전원 핀 제어용 GPIO 레지스터 값을 강제로 0으로 직접 변경·설정하는 방법인 하드웨어 직접 에뮬레이션 방식만 지원함
-    현행 PX4 SITL은 GPS 정상 동작 시나리오만 공식적으로 지원하며, GPS 스푸핑·재밍·멀티패스·불량 위성 신호 등 다양한 GPS 이상 상태 시뮬레이션 기능은 공식 릴리즈 빌드에 포함되지 않음

**해설**: PX4 SITL에서 failure injection API를 사용하거나 GPS 드라이버의 파라미터(SENS_GPS_MASK)를 수정하여 GPS 이상을 시뮬레이션합니다. 또는 Gazebo에서 GPS 플러그인의 노이즈와 오프셋 파라미터를 조정하여 스푸핑 시나리오를 재현합니다.

**팁**: anti-spoofing 소프트웨어 검증을 위해 Spirent GSS7000 같은 GPS 시뮬레이터를 HITL에 연결하여 실제 스푸핑 신호를 주입하는 방법이 가장 현실적입니다.

### Q253. 드론 소프트웨어의 코드 커버리지 100% 달성이 어렵고 의미가 제한적인 이유는?
- ✅ 라인/브랜치 커버리지 100%도 모든 실행 순서(path)를 보장하지 않으며, 멀티스레드 경쟁 조건과 타이밍 의존 버그는 커버리지로 감지 불가. MC/DC 같은 더 강한 기준 필요
-    구문 커버리지 100%는 각 명령어가 실행됨을 보장하지만 분기 조건 조합을 검증하지 않아 참/거짓 양방향 미실행 경로가 존재할 수 있어 결함 검출에 한계
-    테스트 케이스 수가 증가할수록 커버리지 측정 오버헤드가 지수적으로 증가하여 DO-178C DAL A에서 100% 커버리지 달성 비용이 수백만 달러에 달함
-    코드 커버리지는 실행 경로를 측정하지만 알고리즘의 수학적 정확성·요구사항 누락·경쟁 조건은 탐지 불가하여 안전 소프트웨어 검증 기준으로 단독 사용 불가

**해설**: Line 100% 커버리지는 각 라인이 최소 한 번 실행됨을 의미합니다. 조건 조합(A&&B에서 A=F인 경우)이나 멀티스레드 경쟁 조건은 일반 커버리지로 잡히지 않습니다. DO-178C의 MC/DC는 각 조건이 결과에 독립적으로 영향을 미치는지 검증합니다.

**팁**: 실무에서는 코드 커버리지 80% + 변이 테스트(Mutation Testing) + 정적 분석의 조합으로 테스트 품질을 높이는 것이 효율적입니다.

### Q254. 컴패니언 컴퓨터에서 OpenCV와 ROS2를 통합하여 드론 비전 기반 착륙 마커 탐지 파이프라인 최적화 방법은?
- ✅ image_transport로 압축 이미지 전송, cv_bridge로 ROS↔OpenCV 변환 최소화, CUDA 기반 ArUco 탐지 또는 TensorRT 추론으로 CPU 부하 감소, 탐지 결과를 Pose 토픽으로 직접 발행
-    미압축 Raw BGR8 포맷 원본 이미지를 sensor_msgs/Image 토픽으로 전송하면 ArUco 마커 픽셀 데이터 손실이 전혀 없어 탐지 정확도가 최대화되므로 항상 비압축 전송이 권장됨
-    OpenCV와 ROS2는 메모리 모델이 달라 cv_bridge 없이는 직접 통합이 불가능하고, 별도 Python 프로세스로 ZeroMQ IPC를 통해 이미지를 교환하는 것이 현실적인 유일한 방법임
-    ArUco 마커 탐지는 비행 컨트롤러 내장 하드웨어 가속 DSP에서만 처리해야 하며, 컴패니언 컴퓨터 CPU에서 처리하면 MAVLink 제어 루프에 심각한 응답 지연을 유발하여 안전하지 않음

**해설**: image_transport의 compressed_image로 전송하여 대역폭을 줄이고, cv_bridge::toCvShare()로 메시지 복사 없이 OpenCV Mat 접근이 가능합니다. ArUco 탐지 결과는 geometry_msgs/PoseStamped로 변환하여 landing controller 노드에 전달합니다.

**팁**: Precision Landing에서 IR 마커 + aruco_ros 패키지 + MAVSDK MAV_CMD_NAV_LAND_LOCAL 조합이 자주 사용되는 실용적 구성입니다.

### Q255. 방산 드론 소프트웨어 개발에서 MISRA C++ 2023 적용 시 가장 흔히 위반되는 규칙 유형과 대응 방법은?
- ✅ C 스타일 캐스트 금지(static_cast 사용), 동적 메모리 해제 누락, 초기화되지 않은 변수 사용, 제한된 예외 사용. clang-tidy MISRA 프로파일과 PRQA/Polyspace 도구로 자동 검출
-    MISRA C++ 2023은 들여쓰기 규칙, 중괄호 위치, 변수명 명명 규칙 등 코드 포매팅 스타일을 표준화하는 규정으로, 런타임 동작이나 메모리 안전성 버그와는 직접 관련이 없음
-    C++20의 Concepts, Ranges, Coroutines, Modules 기능은 MISRA C++ 2023에서 명시적으로 승인된 기능으로, 제한 없이 방산 안전 크리티컬 소프트웨어에 완전 적용 가능함
-    MISRA C++ 규칙 준수 여부는 개발자의 코드 리뷰와 수동 체크리스트 검토로만 확인할 수 있으며, 정적 분석 자동화 도구는 MISRA 규칙의 맥락 의존성 때문에 적용이 불가능함

**해설**: MISRA C++ 2023은 결정적 동작(deterministic behavior), 안전한 타입 시스템, 명시적 초기화를 요구합니다. 가장 흔한 위반: C 캐스트, 예외 사용, goto, 동적 타입 식별(typeid), 가변 인자 함수입니다.

**팁**: 방산 프로젝트에서 MISRA 준수를 소스 관리부터 적용하면 기술 부채가 없습니다. 도입이 늦어지면 수천 건의 위반을 소급 수정해야 합니다.

### Q256. 드론 소프트웨어에서 Canary Token(카나리 토큰)을 보안 모니터링에 활용하는 방법은?
- ✅ 구성 파일, API 키, 소스 코드에 고유 추적 토큰을 삽입하여 무단 접근/유출 시 알림 수신. 공격자가 토큰을 실행하거나 접근하면 즉시 이메일/슬랙 알림 발생
-    카나리 토큰은 스택 버퍼 끝에 삽입한 감시값으로 함수 리턴 전 값을 검사하여 버퍼 오버플로우에 의한 리턴 주소 변조를 탐지하는 기술이다
-    에어갭 드론 소프트웨어 개발 환경은 인터넷과 분리되어 토큰 서버로의 콜백이 불가능하므로 Canary Token을 보안 모니터링에 적용할 수 없다
-    카나리 토큰은 TPM 칩 또는 HSM 내부에 주입하여 하드웨어 수준에서 인증서 위변조를 감지하는 용도로만 공식 규격이 정의되어 있다

**해설**: 드론 펌웨어 소스코드 유출 탐지에 Canary Token(예: canarytokens.org)을 사용할 수 있습니다. 특정 함수명이나 주석을 토큰으로 포함하여 외부에서 검색되면 유출 경로를 추적합니다. 내부 개발 서버에도 접근 토큰을 배치하면 침해 조기 감지가 가능합니다.

**팁**: 물리 보안도 중요합니다. 드론 내부 임베디드 코드 추출을 방지하기 위해 JTAG 퓨즈(fuse) 비활성화, 펌웨어 암호화 부팅(Secure Boot) 적용이 필요합니다.

### Q257. ROS2에서 Composition(컴포넌트 컨테이너)을 사용하여 여러 노드를 동일 프로세스에 배포할 때의 아키텍처 결정 기준은?
- ✅ 같은 QoS 요구사항을 가지며 intra-process 통신으로 이익을 얻는 노드들을 동일 컨테이너에 배치. 독립 장애 격리가 필요한 노드는 별도 프로세스로 분리
-    센서 드라이버와 제어 알고리즘 등 모든 노드를 단일 컨테이너에 배치하면 IPC 오버헤드가 제거되어 안정성과 응답 속도가 동시에 극대화된다
-    각 노드를 항상 독립 프로세스로 분리해야 장애 격리와 재시작이 보장되므로 ROS2 표준 가이드라인은 Composition 사용을 비권장 패턴으로 분류한다
-    Composition 컨테이너는 Gazebo 시뮬레이터 전용 빌드 옵션으로 활성화되며 실제 하드웨어 배포 환경에서는 동작하지 않는다

**해설**: 센서 퓨전 노드와 제어기 노드처럼 고주파로 데이터를 교환하는 노드들은 intra-process로 zero-copy 통신이 가능합니다. 반면 카메라 드라이버(하드웨어 크래시 위험)는 별도 프로세스로 격리하여 드라이버 장애가 제어기를 죽이지 않도록 합니다.

**팁**: rclcpp_components::ComponentManager를 이용하면 런타임에 동적으로 컴포넌트를 로드/언로드할 수 있어 시스템 재구성이 유연합니다.

### Q258. 대규모 드론 시스템에서 소프트웨어 정의 네트워킹(SDN)을 활용한 텔레메트리 트래픽 관리 설계는?
- ✅ SDN 컨트롤러가 기체 수와 링크 품질에 따라 텔레메트리 플로우를 동적으로 라우팅하고 QoS 정책 적용. 중요 명령 트래픽 우선 처리, 대역폭 제한 기체는 데이터 압축 정책 자동 적용
-    SDN 기술은 데이터센터와 캠퍼스 네트워크의 스위치·라우터 제어 평면을 중앙화하는 데 사용되며, 라디오 링크 기반 드론 텔레메트리 트래픽 관리에는 적용할 수 없음
-    대규모 드론 텔레메트리 트래픽은 비행 전 사전 정의된 VLAN 및 정적 QoS 정책으로 설계되어야 하며, 런타임 동적 라우팅은 실시간 안전 통신의 예측 불가능성을 높임
-    MAVLink 프로토콜은 고유 시스템 ID·컴포넌트 ID 기반 라우팅 방식을 사용하므로 SDN 플로우 테이블 방식과 구조적으로 호환되지 않아 통합 운용이 불가능함

**해설**: 수십 대 이상의 드론 운용에서 단순 유니캐스트/브로드캐스트 구조는 한계가 있습니다. SDN으로 임무 중요도에 따른 대역폭 할당, 링크 품질 저하 시 자동 경로 변경, 기체별 트래픽 격리를 동적으로 제어하면 대규모 군집 운용의 안정성이 향상됩니다.

**팁**: 실용적인 접근법은 MAVLink Router + 우선순위 큐 + 적응형 비트레이트 제어를 조합하는 소프트웨어 솔루션으로, 전용 SDN 하드웨어 없이도 유사한 효과를 달성할 수 있습니다.

### Q259. 드론 소프트웨어에서 모델 기반 설계(Model-Based Design, MBD)를 MATLAB/Simulink로 구현하고 자동 코드 생성(Embedded Coder)을 사용하는 장단점은?
- ✅ 장점: 제어 알고리즘의 시각적 설계/검증, 시뮬레이션-코드 일관성, DO-178C 인증 지원(IEC Certification Kit). 단점: Toolchain 비용, 생성 코드의 읽기 어려움, 오픈소스 생태계와 통합 어려움
-    Embedded Coder의 자동 생성 코드는 MATLAB 컴파일러 최적화 패스가 수동 코드 대비 항상 더 작은 코드 크기와 낮은 실행 사이클을 보장하므로 성능 면에서 수동 작성보다 우월함
-    Simulink Embedded Coder로 생성된 코드는 소스 추적 가능성(traceability)이 부족하여 DO-178C Software Level A/B 인증이 구조적으로 불가하며 방산 인증에 허용되지 않음
-    Simulink 생성 코드는 x86 PC용 시뮬레이션 실행 파일만 출력하며, ARM Cortex-M 계열 임베디드 MCU용 크로스 컴파일을 공식 지원하지 않아 드론 FC에 직접 배포가 불가능함

**해설**: MATLAB/Simulink MBD는 항공/방산 분야에서 PID, 상태 추정, 임무 관리 알고리즘 개발에 표준적으로 사용됩니다. 모델에서 직접 C 코드를 생성하여 모델-코드 불일치 위험을 없앱니다. 단, 상용 라이선스 비용(연간 수천만 원)이 큰 장벽입니다.

**팁**: 오픈소스 대안으로 Scilab/Xcos, GNU Octave + Modelica가 있지만 인증 도구 지원은 Simulink 대비 제한적입니다.

### Q260. 드론 소프트웨어 업데이트(OTA, Over-the-Air) 시스템 설계에서 A/B 파티션 방식과 롤백 메커니즘의 중요성은?
- ✅ A 파티션(현재 실행)과 B 파티션(신규 업데이트)를 유지하여 업데이트 실패 시 A로 자동 롤백. 업데이트 중 전원 차단이나 부분 플래시 시에도 현재 실행 파티션은 안전
-    롤링 업데이트(Rolling Update) 방식으로 모듈별로 순차 업데이트하고 각 모듈 교체 후 헬스체크가 실패하면 해당 모듈만 이전 버전으로 개별 복구
-    업데이트 전 전체 파티션 스냅샷을 외부 스토리지에 백업하고 OTA 실패 시 백업에서 완전 복원하되 복원 시간이 길어 비행 가능 상태 복구에 지연 발생
-    단일 파티션 업데이트 후 부트로더 CRC 검증에 실패하면 펌웨어를 공장 초기화 이미지로 자동 복원하여 최소한의 비행 기능을 안전하게 유지

**해설**: 드론 현장 운용 중 펌웨어 업데이트 실패는 치명적입니다. A/B 파티션 방식은 Linux(Android Update Engine, OSTree) 또는 임베디드(MCUBoot)에서 구현되며, 업데이트 후 헬스체크 실패 시 자동 롤백으로 기체를 항상 비행 가능 상태로 유지합니다.

**팁**: PX4 FC의 부트로더(Bootloader)가 펌웨어 무결성(CRC)을 확인하고 실패 시 이전 버전으로 복구하는 안전망 역할을 합니다. 컴패니언 컴퓨터는 SWUpdate/Mender 같은 임베디드 Linux OTA 프레임워크를 활용하세요.

