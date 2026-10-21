---
title: "UAV 지원 업링크 전송 에너지 효율 최적화 (확률적 LoS 채널)"
created: 2026-09-04
updated: 2026-10-20
type: concept
domain: comms-protocol
tags: [drone, datalink, comms-protocol]
sources: [inbox/processed/fetch-2026-10-19-arxiv-meteorologically-introduced-impacts-on-aerial-channels-and-u.md, inbox/processed/fetch-2026-10-19-arxiv-joint-resource-management-for-energy-efficient-uav-assisted-.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 지원 업링크 전송 에너지 효율 최적화 (확률적 LoS 채널)

**저자**: Guo Lili (Nantong University, China)  
**학술지**: ICT Express  
**발행연도**: 2026  
**링크**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003377361  
**원문공개**: 비공개(페이월)

## 연구 개요

고정익 UAV가 공중 데이터 수집기(aerial data aggregator)로 기능하는 지상-공중 업링크 전송 시나리오에서, 시스템 에너지 효율을 극대화하는 공동 최적화 알고리즘을 제안한다.

## 최적화 변수

공동 최적화 대상은 세 가지 변수 블록:

1. **타임슬롯 스케줄링**: 지상 사용자(GU)별 전송 순서 결정
2. **지상 사용자 송신 전력 제어**: GU별 전력 최적 배분
3. **UAV 궤적 설계**: 에너지 효율과 커버리지를 동시에 고려한 비행 경로

## 핵심 기법

- **블록 좌표 하강법(BCD)**: 세 변수 블록을 반복적으로 최적화해 수렴 보장
- **확률적 시선(LoS) 채널 모델**: 지상-공중 링크의 현실적인 채널 특성 반영

## 주요 결과

시뮬레이션으로 제안 알고리즘의 효과성과 효율성 확인. 기준선 대비 에너지 효율 유의미한 개선.

## 의의

고정익 UAV의 궤적, 스케줄링, 전력 제어를 통합 최적화하는 실용적 프레임워크로, UAV 릴레이·데이터 수집 임무 설계에 직접 적용 가능하다.

## 관련 페이지

UAV 통신 아키텍처 일반은 [[unet-multi-uav-networking]]를, 드론 데이터링크 기술은 [[datalink-communication]]을 참조한다.

## 최신 근거 연결 (2026-10-20)

- **적용 범위 주의(약화)**: 이 페이지가 요약한 확률적 LoS 채널 모델에는 강수·눈 등 기상 손실이 언급되어 있지 않다(요약 기준, 원문 비공개). 기상 연구는 mmWave에서 비, 근-THz에서 눈이 커버리지에 크게 영향을 준다고 보고하므로 고주파 대역에 이 결과를 옮길 때는 기상 항을 따로 검토해야 한다: [[uav-weather-aerial-channel-impacts]]^[inbox/processed/fetch-2026-10-19-arxiv-meteorologically-introduced-impacts-on-aerial-channels-and-u.md] — 두 논문의 직접 비교 근거는 없어 `contested`로 표시하지 않는다.
- 에너지 효율과 단말 배터리 지속성을 함께 다루는 UAV 지원 SWIPT-MEC의 강화학습 자원 관리(시뮬레이션): [[uav-swipt-mec-drl-resource-management]]^[inbox/processed/fetch-2026-10-19-arxiv-joint-resource-management-for-energy-efficient-uav-assisted-.md]
