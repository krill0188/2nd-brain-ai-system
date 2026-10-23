---
title: "rosbag2 (ros2/rosbag2 GitHub README)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ros-middleware
ontology_class: ROS2
tags: [drone, flight-log, rosbag2, mcap, ros2]
sources: [inbox/processed/hw-20261021-data-flightlog-rosbag2.md]
confidence: medium
contested: false
contradictions: []
---

# rosbag2 (ros2/rosbag2 GitHub README)

- 원문: https://github.com/ros2/rosbag2^[inbox/processed/hw-20261021-data-flightlog-rosbag2.md]
- 저자: ROS 2 contributors^[inbox/processed/hw-20261021-data-flightlog-rosbag2.md]
- 발행: 미확인^[inbox/processed/hw-20261021-data-flightlog-rosbag2.md]

## 핵심 내용
rosbag2는 ROS 2의 기록·재생 도구(ros2 bag CLI)이다. 저장 플러그인은 mcap과 sqlite3 두 가지이며 MCAP이 기본이다. ros2 bag record -a는 전체 토픽, --topics는 선택 토픽을 기록하고 -b(크기), -d(시간)로 분할한다. 스냅샷 모드는 메모리 순환 버퍼를 요청 시 디스크에 쓴다. 재생은 ros2 bag play이며 토픽 필터, 서비스 제어(일시정지·탐색·속도) 지원. 압축은 기본 꺼짐이며 --compression-mode(file/message)와 --compression-format을 쓴다. 원문: "Currently, the only compression-format available is zstd." ros2 bag convert로 병합·분할·압축/직렬화 변경·시간 구간 자르기를 YAML 옵션으로 수행한다.^[inbox/processed/hw-20261021-data-flightlog-rosbag2.md]

## 설계·운용에 쓸 수 있는 지침
- 드론 탑재 컴퓨터에서 대용량 센서 토픽 기록 시 파일 분할(-b/-d)과 압축을 병용 가능.^[inbox/processed/hw-20261021-data-flightlog-rosbag2.md]
- 후처리·재생 파이프라인은 MCAP 기본 저장소를 가정해도 되나 sqlite3 호환 확인 필요.^[inbox/processed/hw-20261021-data-flightlog-rosbag2.md]

## 한계·미확인
- docs.ros.org 문서는 접근 차단(Anubis)으로 열지 못하고 GitHub README만 확인.^[inbox/processed/hw-20261021-data-flightlog-rosbag2.md]
- 성능 수치(기록 처리량 등) 미확인.^[inbox/processed/hw-20261021-data-flightlog-rosbag2.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[ros2-drone-integration]]
