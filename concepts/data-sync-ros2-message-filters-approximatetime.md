---
title: "message_filters ApproximateTime policy (ROS wiki mirror) and ROS 2 tutorial"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
ontology_class: TimingLatency
tags: [drone, ros2, message-filters, time-synchronization, approximatetime]
sources: [inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]
confidence: medium
contested: false
contradictions: []
---

# message_filters ApproximateTime policy (ROS wiki mirror) and ROS 2 tutorial

- 원문: https://mirror.umd.edu/roswiki/message_filters(2f)ApproximateTime.html ; https://github.com/ros2/message_filters/blob/rolling/doc/Tutorials/Approximate-Synchronizer-Cpp.rst^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]
- 저자: ROS community (wiki mirror), ros2/message_filters 저장소^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]
- 발행: 미확인^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]

## 핵심 내용
docs.ros.org와 wiki.ros.org는 접근 차단(Anubis 봇방어, Access Denied)이라 대체 경로로 대학 미러(ROS 1 위키 사본)와 GitHub 튜토리얼을 열람.^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]
- 알고리즘: 모든 토픽 큐에 메시지가 1개 이상일 때 큐 헤드 중 가장 늦은 것이 pivot. 메시지는 한 번만 사용, 일부는 버려질 수 있음. 세트는 서로 교차하지 않으며 인접(contiguous)하고 최소 크기(세트 크기 = 가장 늦은/이른 타임스탬프 차). 출력은 도착 시각이 아닌 메시지 타임스탬프에만 의존하고, 각 토픽 내 메시지는 순서대로 도착해야 함. 세트 발행 후 오래된 메시지는 폐기.^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]
- 파라미터: AgePenalty 기본 0(후속 구간에 (1+AgePenalty) 가중, 0 초과 시 더 일찍/더 많은 세트, 품질 저하 가능), InterMessageLowerBound 기본 0(출력은 바꾸지 않고 지연만 줄임, 잘못 지정하면 비최적 세트, 일반적 값은 카메라 프레임 간격의 절반 정도), MaxIntervalDuration 기본 비활성(이보다 큰 세트 제외).^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]
- 큐 크기: 타임스탬프 차이가 크면 큐가 충분히 커야 하며 아니면 메시지가 드롭됨.^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]
- ROS 2 튜토리얼(C++): 예시는 500 ms, 550 ms 타이머의 두 토픽, 정책 생성자에서 queue_size = 10, `setAgePenalty(0.50)`(튜토리얼 주석은 "50ms"이나 전달값이 0.50이라 단위 불명확). 모든 퍼블리셔/서브스크라이버의 QoS가 같아야 정렬됨, header stamp 필요.^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- 센서 헤더 stamp는 취득 시각으로 찍어야 함(출력이 stamp에만 의존). 소프트웨어 도착 시각 스탬프는 정렬 품질을 떨어뜨림(해석).^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]
- QoS 일치 필수, 기본 AgePenalty 0, queue_size 예제값 10.^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]

## 한계·미확인
- ROS 2 공식 docs.ros.org 본문과 ros2 저장소 approximate_time.h는 열람 실패(404/차단). 위 알고리즘 설명은 ROS 1 위키 사본 기준이며 ROS 2 구현과 동일한지 미확인. 단위(AgePenalty) 불명확.^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
