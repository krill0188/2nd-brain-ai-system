---
title: "충돌각 제약 쿼드로터 군집의 사전정의 시간 협조 유도·제어 (Qian, 2026)"
created: 2026-10-31
updated: 2026-10-31
type: concept
domain: ai-autonomy
tags: [drone, swarm]
sources: [inbox/processed/fetch-2026-10-29-kci-predefined-time-cooperative-integrated-guidance-and-control-.md]
confidence: low
contested: false
contradictions: []
---

# 사전정의 시간 협조 통합 유도·제어 (QCIGC)

Weichen Qian(난징이공대)의 *International Journal of Aeronautical and Space Sciences* 2026 논문. KCI 원문은 비공개이고 초록도 일부 잘려 있어 **초록 앞부분 기준**으로만 요약한다.^[inbox/processed/fetch-2026-10-29-kci-predefined-time-cooperative-integrated-guidance-and-control-.md]

## 내용
- **대상 문제**: 지상 고정 쿼드로터 군집이 공중 표적을 협조 공격하는 시나리오. UAV-표적 상대 운동학과 쿼드로터 동역학으로 QCIGC 모델을 세운다.
- **구조**: 외부 루프가 시선각(LOS)과 충돌 시간을, 내부 루프가 자세 안정화를 맡는 중첩 제어.
- **특징**: 시간 기반 생성 함수(time-base generator)로 LOS 각 추종 명령을 만들고, 지수 감쇠 함수로 LOS 속도 추종 명령을 성형해 초기 유도 단계의 과부하 포화를 완화한다.
- 이후 초록은 잘려 있어 외란 처리·수렴 시간 보장·시뮬레이션 결과는 확인하지 못했다.

## 한계
공격(요격) 시나리오를 다루는 논문이며, 수치 결과는 이 소스로 검증되지 않았다.

## 관련 문서
군집 계획은 [[phased-trajectory-planning-uav-swarm-dynamic-environments]], 쿼드로터 제어 비교는 [[quadrotor-controller-comparison-reproducibility-study]]를 참조한다.
