---
title: "Event Camera for Drones"
created: 2026-07-31
updated: 2026-08-10
type: concept
tags: [drone, ai-autonomy, drone-hw, hardware]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Raw source not preserved in repo — found during 2026-08-10 provenance audit, needs recapture"
---

# Event Camera for Drones

이벤트 카메라 기반 드론 비전. RSS 2026 연구.

## Event Camera Characteristics

- 마이크로초 지연 시간으로 비동기 픽셀별 밝기 변화 보고
- 동적 시각 정보를 희소 이벤트 스트림으로 인코딩

## Challenges

- 극단적인 시간 해상도로 인지 시스템에 과부하
- 자체 운동(ego-motion)과 독립적으로 움직이는 객체(IMO) 이벤트 혼재
- 기존 솔루션은 3D 재구성이나 수동 튜닝 필터에 의존

## Solution

- Motion-aware Event Suppression 프레임워크
- 자체 운동과 IMO 이벤트 분리

## Institution

- UZH Robotics and Perception Group

## References

- [[computer-vision-drone]]
- [[drone-ai]]
- [[drone-hw]]
