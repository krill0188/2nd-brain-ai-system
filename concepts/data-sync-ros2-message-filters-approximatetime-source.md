---
title: "ros2/message_filters ApproximateTime: official doc (doc/index.rst) and C++ source (jazzy/rolling) defaults"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, ros2, message-filters, time-synchronization, approximatetime, defaults]
sources: [inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]
confidence: medium
contested: false
contradictions: []
---

# ros2/message_filters ApproximateTime: official doc (doc/index.rst) and C++ source (jazzy/rolling) defaults

- 원문: https://github.com/ros2/message_filters/blob/rolling/doc/index.rst ; https://github.com/ros2/message_filters/blob/jazzy/include/message_filters/sync_policies/approximate_time.h ; https://github.com/ros2/message_filters/blob/rolling/include/message_filters/sync_policies/approximate_time.hpp^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]
- 저자: ros2/message_filters 저장소^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]
- 발행: 미확인 (jazzy / rolling 브랜치 2026-10-22 열람)^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]

## 핵심 내용
기존 data-sync-ros2-message-filters-approximatetime.md 는 ROS 1 위키 사본 기준이라 ROS 2 구현 일치가 미확인이었음. GitHub 원본에서 확인:^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]
- 공식 문서(rolling doc/index.rst) 6장: 동기 정책은 3개 "ExactTime, ApproximateEpsilonTime and ApproximateTime". "ApproximateTime policy uses an adaptive algorithm to match messages based on their timestamp." ExactTime은 "exactly the same timestamp", ApproximateEpsilonTime은 epsilon 허용 오차 내 동일 타임스탬프를 요구. 모든 메시지에 header가 있어야 타임스탬프를 읽으며, Python ApproximateTimeSynchronizer는 header가 없는 메시지를 기본 거부하고 `allow_headerless=True`일 때만 현재 ROS 2 시간을 header.stamp 대신 사용.^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]
- C++ 입력은 최대 9개 필터("Up to 9 separate filters"; 출력 M0..M8).^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]
- 소스(jazzy approximate_time.h / rolling approximate_time.hpp): 생성자 `ApproximateTime(uint32_t queue_size)`, 기본 `age_penalty_(0.1)`(ROS 1 위키의 기본 0과 다름), `max_interval_duration_` 기본은 사실상 무제한(int32 최대), `inter_message_lower_bounds_` 기본 Duration(0,0). 코드 주석: queue_size 1이면 "will tend to drop many messages ... At least 2 is recommended." `setAgePenalty`는 음수 불가(assert), 후보 선택 조건에 `(end_time - candidate_end_) * (1 + age_penalty_)`가 사용됨.^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]
- 정책은 header.stamp에만 의존하므로 센서 스탬프가 취득 시점이어야 동기 품질이 보장(해석).^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- ROS 2 Jazzy/Rolling에서 AgePenalty 기본값은 0.1, queue_size는 최소 2 권장.^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]
- 카메라-IMU처럼 주기가 크게 다른 센서는 ApproximateTime이 매칭하는 쌍 간 최대 간격 제한을 `setMaxIntervalDuration`으로 둘 수 있음(기본 무제한).^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]

## 한계·미확인
- docs.ros.org 렌더 본문은 접근 차단이라 GitHub 소스로 대체. 알고리즘 상세(pivot, 후보) 설명은 헤더 코드에서 일부만 확인. 이전 파일의 ROS 1 위키 기본값 0과 불일치하는 이유(버전 차이)는 미확인.^[inbox/processed/hw-20261021-data-sync-ros2-message-filters-approximatetime-source.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
