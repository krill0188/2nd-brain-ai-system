---
title: "ED-324 / ARP6983: Development and Assurance guidelines for Aeronautical Systems and Equipment Implemented with Machine Learning (SAE G-34 / EUROCAE WG-114)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: regulations
tags: [drone, certification, machine-learning, do-178c, ed-324, arp6983, ml-constituent]
sources: [inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]
confidence: medium
contested: false
contradictions: []
---

# ED-324 / ARP6983: Development and Assurance guidelines for Aeronautical Systems and Equipment Implemented with Machine Learning (SAE G-34 / EUROCAE WG-114)

- 원문: https://www.eurocae.net/open-consultation-for-ed-324/ ; FAA AI/ML Technical Exchange Meeting slides (Aug 2025) https://na.eventscloud.com/file_uploads/115fca49330a77ce92d7fe04e9874faf_Day1-Jahn-202508ED-324ARP6983presFAAAI-MLTechExchangeMeeting_8-5-25-Read-Only.pdf^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]
- 저자: SAE G-34 / EUROCAE WG-114^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]
- 발행: 초안 의견수렴 2025-08-01 공지 (정식 발행 미확인)^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]

## 핵심 내용
EUROCAE 공지(2025-08-01): "Process Standard for Development and Certification Approval of Aeronautical Products Implementing AI"(ED-324) 초안 공개 의견수렴, 마감 "Mid-September".^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]
SAE/EUROCAE 발표 슬라이드(2025-08, Draft 7 기준, WIP 면책 포함):^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]
- 합동위 2019년 설립. 발행물: ER-022/AIR6988 Statement of Concerns(2021-04-30), ER-027/AIR6987 Taxonomy(2024-12-12). 진행 중: ED-324/ARP6983(발행 목표 2026-06), AIR6994 Use Cases(2026 Q2 계획).^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]
- Statement of Concerns: 기존 ED-12x/DO-178x는 요구사항에서 추적되는 사람이 설계한 소스코드를 전제하나, ML 모델의 저수준 설계는 기계가 만들어 기능 요구사항으로 직접 추적·이해되지 않는다는 공백을 지적.^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]
- Issue 1 범위: Learning Assurance 중심 개발 보증, airborne와 ATM/ANS, 유인·무인 항공기 포함, "Non-adaptive ML in supervised mode, and up to DAL C / AL 3 / SWAL 2", 정보보안과 인간요소는 범위 밖.^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]
- 핵심 개념 ML Constituent(MLC): "A defined and bounded set of one or more ML model(s) and the ML data processing required for their execution ... considered as a single entity for assurance purposes."^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- Issue 1은 최대 DAL C까지, 적응형(온라인 학습) ML 제외이므로 비행 중 학습 모델은 대상 아님.^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]
- 소프트웨어 보증은 ED-12x/DO-178x 위에 MLC 개념을 연결(MLC는 시스템·아이템 사이 전환 지점).^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]

## 한계·미확인
- 현재(2026-10) 정식 발행 여부 미확인. 슬라이드는 SAE 저작권 표기가 있는 발표자료이며 초안 기반이라 변경 가능. 슬라이드 도식(관계도)은 텍스트로 미확인.^[inbox/processed/hw-20261021-ai-cert-ed324-arp6983-ml-assurance-standard.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[drone-regulations]]
