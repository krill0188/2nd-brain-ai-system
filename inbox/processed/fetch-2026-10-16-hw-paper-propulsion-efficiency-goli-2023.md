---
title: "Experimental study on efficient propulsion system for multicopter UAV design applications"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://doi.org/10.1016/j.rineng.2023.101555
tags: [drone, hardware, propulsion, motor, propeller, battery, efficiency]
authors: Srikanth Goli, Dilek Funda Kurtuluş, Luai M. Alhems, Azhar M. Memon, Imil Hamda Imran
published: 2023-12-01 (Results in Engineering vol. 20, art. 101555)
---

# 멀티로터 모터·프로펠러·배터리 조합 실험 (Goli et al., 2023)

## 핵심 내용
- 모터, 프로펠러, 배터리 조합을 바꿔 가며 추진계 효율을 실험으로 비교했다. ESC 신호, 전류, 전력, 추력, 토크와 프로펠러 크기의 관계를 측정했다.
- 초록에 적힌 최고 효율 값: 12인치 프로펠러(P4) 12.9%(배터리 B1, 3300 mAh) / 11.4%(B2, 6000 mAh). 700 KV 모터(M1) 64.29%(B1) / 62.01%(B2).
- 같은 프로펠러에서 주어진 RPM의 추력·토크는 배터리 용량과 모터 종류에 따라 비슷했다.
- B2(6000 mAh)는 필요 추력에서 전류가 적고 RPM이 높았으며, 탑재 가능 페이로드는 5.82 N(B2) 대 2.02 N(B1)으로 보고됐다. 두 경우 모두 B2가 체공 시간이 길었다.

## 설계에 쓸 수 있는 지침
- 모터 KV와 프로펠러 크기를 함께 고르는 조합 실험 방식(ESC 신호 → 전류·전력 → 추력·토크) 그대로 자체 벤치 시험 절차로 재사용할 수 있다.
- 배터리 용량 증가가 페이로드와 체공에 직접 영향을 준다는 점을 추진계 선정 초기에 반영한다.

## 한계·미확인
- 보고된 효율(12.9%, 64.29% 등)은 구성품 단위 효율로 보인다. 기체 전체 효율과 직접 비교하면 안 된다. 정의는 본문 확인 필요.
- 체공 시간의 구체 수치(분)는 초록에 없어 미확인.
- 프로펠러 피치, 측정 조건(고도·온도)은 초록에서 확인 불가.
