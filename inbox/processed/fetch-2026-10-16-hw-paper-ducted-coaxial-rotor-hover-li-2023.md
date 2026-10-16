---
title: "Experimental Investigation on Hover Performance of a Ducted Coaxial-Rotor UAV"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://doi.org/10.3390/s23146413
authors: "Hai Li, Zaibin Chen, Hongguang Jia"
published: "2023-07-14"
tags: [drone, hardware, paper, coaxial-rotor, duct, hover, thrust, efficiency, figure-of-merit]
---

# Experimental Investigation on Hover Performance of a Ducted Coaxial-Rotor UAV

## 핵심 내용 (방법·결과)

중국과학원 창춘광학정밀기계물리연구소 팀이 풍동 시험으로 소형 UAV의 덕티드(duct가 있는) 동축 이중 로터 시스템의 호버 성능을 실험적으로 측정했다. Sensors 2023, 23(14):6413 게재. (PMC10386733)

**실험 파라미터:** 로터 회전수 1,000~7,000 rpm, 블레이드 팁 레이놀즈수 0.43×10⁵ ~ 3.01×10⁵

**핵심 정량 결과:**
- **로터 간격 최적값:** H/R = 0.40 (간격 변화는 효율보다 추력 분배에 주로 영향)
- **덕트 내 로터 위치 최적:** 덕트 입구로부터 0.31Cd 위치(P5)에서 단일 로터 대비 **약 20% 파워 로딩 향상**
- **팁 간격:** δ ≤ 0.015R 조건에서 누설 손실 최소화
- **동축 시스템:** 단일 로터 2개 합산 추력 대비 **14~16% 손실**, 파워 로딩은 단일 로터 대비 **약 5.8% 향상**
- **덕티드 동축 최우수 구성(S1 간격):** 비행 성능 지수(FOM) **0.61** → 비덕티드 동축 대비 약 12% 향상

## 설계에 쓸 수 있는 지침

- 소형 UAV에서 덕트 추가 시 파워 로딩 ~20% 향상 가능 → 같은 배터리로 체공 시간 연장 효과.
- 동축 설계 시 로터 간격 H/R=0.40 기준점으로 최적화 시작.
- 팁 클리어런스 δ ≤ 0.015R 이하 제작 정밀도 확보 → 조립 허용 공차 설정 기준.
- FOM 0.61은 동축+덕트 조합의 현실적 달성 목표값으로 활용 가능.

## 한계·미확인 항목

- 전진 비행 또는 바람 조건에서의 성능 변화: 미확인 (정지 호버 실험만).
- 덕트 형상(입구 반경, 확산각 등) 최적화는 별도 연구 필요.
- 장기 운용 시 덕트 내부 오염·마모 영향: 미확인.
