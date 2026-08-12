---
title: Voice Control for Drones
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [voice-control, drone-sw, ai-agent, NLP, speech]
sources: []
confidence: medium
domain: ai-autonomy
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# Voice Control for Drones

음성 제어는 자연어 명령을 통해 드론을 조작하는 인간-기계 인터페이스(HMI)다. STT(Speech-to-Text), NLP(Natural Language Processing), 명령 매핑의 파이프라인으로 구성된다.

## 아키텍처

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   음성 입력   │───▶│   STT/ASR   │───▶│   NLP/NLU   │
│  (마이크)   │    │ (Whisper)   │    │ (Intent)    │
└──────────────┘    └──────────────┘    └──────┬───────┘
                                                │
                                         ┌──────┴──────┐
                                         │ Command Map  │
                                         │ (Takeoff→MAV)│
                                         └──────┬──────┘
                                                │
                                         ┌──────┴──────┐
                                         │   Drone      │
                                         │ (MAVLink)    │
                                         └──────────────┘
```

## STT(Speech-to-Text)

### OpenAI Whisper

| 모델 | 파라미터 | VRAM | 지연 |
|------|----------|------|------|
| **tiny** | 39M | ~1GB | 실시간 |
| **base** | 74M | ~1GB | 실시간 |
| **small** | 244M | ~2GB | 수초 |
| **medium** | 769M | ~5GB | 수십초 |
| **large** | 1550M | ~10GB | 수십초 |

### 실시간 스트리밍

```python
import whisper
import speech_recognition as sr

model = whisper.load_model("base")
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    audio = recognizer.listen(source)
    result = model.transcribe(audio.get_wav_data())
    text = result["text"]
```

## NLP/NLU (의도 파악)

### Intent Classification

| 명령 유형 | 예시 | MAVLink 변환 |
|-----------|------|--------------|
| **Action** | "이륙해", "착륙해" | `NAV_CMD_TAKEOFF`, `NAV_CMD_LAND` |
| **Direction** | "왼쪽으로", "위로" | `MAV_CMD_DO_CHANGE_SPEED` |
| **Mode** | "홀드 모드", "RTL" | `MAV_CMD_DO_SET_MODE` |
| **Query** | "배터리 얼마야" | `BATTERY_STATUS` 요청 |

### LLM 기반 파싱

```python
# GPT/Claude를 활용한 명령 파싱
prompt = """
사용자가 드론에 명령했습니다. 다음을 JSON으로 반환하세요:
- action: 이륙/착륙/이동/모드변경/질문
- parameters: 고도/방향/속도/위치
"""
```

## 명령 매핑

### 매핑 테이블

```python
VOICE_COMMANDS = {
    "이륙": MAV_CMD_NAV_TAKEOFF,
    "착륙": MAV_CMD_NAV_LAND,
    "복귀": MAV_CMD_NAV_RETURN_TO_LAUNCH,
    "홀드": (MAV_CMD_DO_SET_MODE, 4),  # Hold mode
    "왼쪽으로": lambda dist: velocity_cmd(-1, 0, 0),
    "오른쪽으로": lambda dist: velocity_cmd(1, 0, 0),
    "위로": lambda alt: position_cmd(rel_z=alt),
}
```

## Wake Word

음성 명령 활성화를 위한 트리거.

| 엔진 | 특성 |
|------|------|
| **Porcupine** | Picovoice, 오프라인 |
| **Snowboy** | 레거시, 커스텀 학습 |
| **Whisper** | VAD + 키워드 |
| **OpenWakeWord** | ONNX 기반 |

```python
# Porcupine 예시
import pvporcupine

porcupine = pvporcupine.create(keyword_paths=["hey_drone.ppn"])
```

## ROS2 통합

```python
# voice_control_node.py
import rclpy
from std_msgs.msg import String
from px4_msgs.msg import VehicleCommand

class VoiceControlNode(Node):
    def __init__(self):
        self.subscription = self.create_subscription(
            String, '/voice/command', self.command_callback, 10)
        self.publisher = self.create_publisher(
            VehicleCommand, '/fmu/in/vehicle_command', 10)
    
    def command_callback(self, msg):
        cmd = self.parse_intent(msg.data)
        mavlink_cmd = self.map_to_mavlink(cmd)
        self.publish_mavlink(mavlink_cmd)
```

## 안전 고려사항

| 위험 | 대응 |
|------|------|
| **오인식** | 확인 프롬프트 ("이륙하시겠습니까?") |
| **지연** | 비상 중단 버튼 (물리) |
| **환경 잡음** | 노이즈 캔슬링 |
| **권한** | 음성 생체 인증 |

## 응용 사례

| 시나리오 | 설명 |
|----------|------|
| **Hand-free** | 장비 들고 조종 |
| **비전 사용자** | 시각 장애인 지원 |
| **멀티태스킹** | GCS 작업 중 음성 명령 |
| **응급 상황** | 빠른 모드 전환 |

## 구현 스택

| 컴포넌트 | 권장 |
|----------|------|
| **Wake Word** | Porcupine |
| **STT** | Whisper (tiny/base) |
| **NLU** | GPT-4 / Claude / Local LLM |
| **MAVLink** | pymavlink / MAVSDK |
| **ROS2** | rclpy |

## 관련 개념

- [[mavlink-protocol]] — 명령 전송 프로토콜
- [[px4-offboard-control]] — 음성 → Offbridge 연결
- [[drone-ai-agents]] — 음성 인터페이스 통합
- [[ros2-drone-integration]] — ROS2 기반 구현

## 수집 대상

- 실제 음성 제어 시스템 사례 (NASA, DJI, etc.)
- Whisper + 드론 통합 오픈소스
- 다국어 음성 명령 데이터셋
- 음성 인증/보안 방법론

## 📰 최근 관련 소식
- Army seeks next-gen missile that could shoot down small drones for less than $150K a pop (DefenseScoop, Tue, 04 Au) — https://news.google.com/rss/articles/CBMie0FVX3lxTE5GbzRtdW9TS3Y4b3JkaW9oazVGWW9nUWRxa0hGY25RV2h1UEg1MVVfQnhSUE1xS1VFMzVSUGRyckRva0VEZFV5aWhqeHZsbngwV2FpTDBLMVEwdllFOWVXYVZyU3g2VDNESS1WekhBLXNYOEdhMWZrenRESQ?oc=5
- Drones Bring Whole Blood Directly to Trauma Scenes (dronelife.com, Mon, 10 Au) — https://dronelife.com/2026/08/10/drones-bring-whole-blood-directly-to-trauma-scenes/
