# 드론 도메인 지식 가이드

> 작성일: 2026-07-26  
> 이 파일은 도메인 가이드입니다. canonical 페이지가 아닙니다.  
> canonical 페이지는 raw 소스가 2개 이상 확보된 후 entities/ concepts/ comparisons/ queries/ 에 작성합니다.

---

## 도메인 구조 (8개 카테고리)

```
드론 (drone)
├── 드론 HW        (drone-hw)     — 기체·FC·ESC·배터리·센서·카메라
├── 드론 SW        (drone-sw)     — 펌웨어·GCS·미들웨어·SDK
├── 드론 데이터링크 (datalink)     — RF·LTE·MAVLink·C2링크·텔레메트리
├── 드론 군집화    (swarm)        — 편대비행·임무분배·합의 알고리즘
├── 드론 음성인식  (voice-control) — 음성명령·자연어 인터페이스
├── 드론 AI 융합   (drone-ai)     — 컴퓨터비전·자율비행·SLAM·탐지
└── 드론 AI Agent  (ai-agent)     — 자율 의사결정·멀티에이전트 아키텍처
```

---

## 카테고리별 수집 방향

### 드론 (drone) — 일반
수집 대상: 드론 규제·형식승인·임무 설계·기체 선택 기준  
주요 키워드: UAV, UAS, 형식증명, 드론 운용 규정, BVLOS, VLOS

### 드론 데이터링크 (datalink)
수집 대상: 무선 통신 프로토콜, 링크 예산, 간섭 대응, 암호화  
주요 키워드: MAVLink, C2 link, RF link budget, LTE drone, 텔레메트리, FHSS, DSSS

### 드론 군집화 (swarm)
수집 대상: 편대 비행 알고리즘, 충돌 회피, 분산 제어, 시뮬레이션  
주요 키워드: swarm drone, formation flight, collision avoidance, consensus algorithm, 군집비행

### 드론 음성인식 (voice-control)
수집 대상: 음성 명령 인터페이스, 자연어 → 드론 제어 파이프라인  
주요 키워드: voice command drone, NLP drone control, Whisper, wake word, 드론 음성제어

### 드론 HW (drone-hw)
수집 대상: 비행 컨트롤러 비교, ESC, 배터리, 센서 선택  
주요 키워드: Pixhawk, Cube Orange, STM32, ESC 프로토콜, LiPo, LiDAR, depth camera

### 드론 SW (drone-sw)
수집 대상: 펌웨어 아키텍처, GCS 개발, SDK, 미들웨어 설계, ROS/ROS2 통합  
주요 키워드: PX4, ArduPilot, QGroundControl, MAVSDK, ROS/ROS2, MAVROS, MAVROS2, uORB, DroneKit

### 드론 AI 융합 (drone-ai)
수집 대상: 탑재 컴퓨터 비전, 자율비행, SLAM, 객체 탐지  
주요 키워드: YOLOv8 drone, SLAM drone, autonomous navigation, object detection UAV, 드론 AI

### 드론 AI Agent (ai-agent)
수집 대상: 드론에 AI 에이전트 통합, 자율 의사결정, 멀티에이전트 협업  
주요 키워드: LLM drone, AI agent UAV, autonomous mission planning, multi-agent drone, 드론 에이전트

---

## raw/ 수집 분류 기준

```
raw/articles/      ← 논문·기술 기사 (Zotero → PDF/Markdown 내보내기)
raw/papers/files/  ← PDF 원본 첨부 (Zotero 첨부파일)
raw/web/           ← 웹 클리핑 (Web Clipper)
raw/youtube/       ← YouTube 트랜스크립트
raw/transcripts/   ← 강의·컨퍼런스·미팅 녹취
raw/notebooklm/    ← NotebookLM 소스 레코드 및 질의 결과
```

파일명 규칙:
```
raw/articles/2026-07-26-mavlink-protocol-deep-dive.md
raw/web/2026-07-26-px4-vs-ardupilot-comparison.md
raw/youtube/2026-07-26-swarm-drone-formation-algorithm.md
```

---

## canonical 페이지 생성 기준

SCHEMA.md 규칙에 따름:
- 동일 주제가 raw 소스 **2개 이상**에 등장 → canonical 페이지 생성
- 하나의 소스에서 **핵심 주제**로 다뤄진 경우 → 생성 가능
- 지나가는 언급, 사소한 세부사항 → 생성 금지

**entities/ 생성 예시** (고유 개체):
- `entities/px4-autopilot.md` — PX4 오픈소스 비행 제어 소프트웨어
- `entities/mavlink.md` — MAVLink 통신 프로토콜
- `entities/pixhawk.md` — Pixhawk 비행 컨트롤러 시리즈

**concepts/ 생성 예시** (개념·원리):
- `concepts/drone-c2-link.md` — 드론 지휘통제 링크 아키텍처
- `concepts/swarm-formation-control.md` — 편대 비행 제어 이론
- `concepts/drone-ai-fusion-pipeline.md` — 드론 AI 파이프라인 구조

---

## 수집 우선순위 (초기 단계)

| 우선순위 | 카테고리 | 이유 |
|---|---|---|
| 1 | drone-sw (PX4/ArduPilot) | 가장 많은 파생 주제의 기반 |
| 2 | datalink (MAVLink) | 통신 레이어 이해 필수 |
| 3 | drone-ai (컴퓨터 비전) | AI 융합의 핵심 |
| 4 | swarm | 군집화는 위 두 가지 기반 필요 |
| 5 | drone-hw, voice-control, ai-agent | 이후 단계 |
