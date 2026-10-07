---
title: "UAM 회랑 바람 관측용 기상드론 유효성 검증 (KCI)"
created: 2026-10-07
updated: 2026-10-07
type: concept
domain: ops-mission
tags: [drone, ops-mission, research]
sources: [raw/papers/_unclassified/uam-회랑-바람-관측을-위한-기상드론-유효성-검증.md]
confidence: low
contested: false
contradictions: []
---

# UAM 회랑 바람 관측용 기상드론 유효성 검증

이지선(국립기상과학원)의 한국항공운항학회지(2026) 논문. UAM 운용에 필요한 0~600 m AGL 바람 정보를
드론으로 관측할 수 있는지 윈드프로파일러(WPF)와 비교해 검증하고, 현장 운용 가능한 비행 프로토콜을
제안했다. 초록이 중간에서 잘려 결론 일부는 확인하지 못했다(confidence low).
^[raw/papers/_unclassified/uam-회랑-바람-관측을-위한-기상드론-유효성-검증.md]

## 실험 설계

- 2024년 8~9월 WPF 서귀포 지점(ID 47884)에서 10~500 m AGL 범위로 총 8회 실험.
- **상승 구간 데이터만** 사용해 로터 유도 기류의 영향을 줄였다.

## 결과

- WPF 대비 평균 편향 **+0.8 m/s**, r = 0.839 (n = 18). 기상청 현장 보정 허용 수준과 비슷하다고 보고.
- 저고도 바람 추정에 흔히 쓰는 멱법칙(power-law) 연직 풍속 분포와 드론 관측을 비교해 한계를 검토했다(세부 수치는 초록에 없음).

## 관련 개념

- [[utm-system]] — 저고도 공역 교통관리
- [[kci-utm-k-flight-path-error-regional-analysis]] — 국내 드론 실증 비행경로 오차 분석
- [[drone-regulations]] — 규제 맥락
