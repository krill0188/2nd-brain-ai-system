---
title: "Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, ai, small-object-detection, aerial, vehicle-detection]
sources: [inbox/processed/hw-20261021-ai-smallobj-sahi-akyon-2022.md]
confidence: medium
contested: false
contradictions: []
---

# Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection

- 원문: https://arxiv.org/abs/2202.06934^[inbox/processed/hw-20261021-ai-smallobj-sahi-akyon-2022.md]
- 저자: Fatih Cagatay Akyon, Sinan Onur Altinuc, Alptekin Temizel^[inbox/processed/hw-20261021-ai-smallobj-sahi-akyon-2022.md]
- 발행: 2022-02-14 (v5 2022-10-24, ICIP 2022)^[inbox/processed/hw-20261021-ai-smallobj-sahi-akyon-2022.md]

## 핵심 내용
영상을 겹치는 조각으로 나눠 추론하고 결과를 병합하는 SAHI(slicing-aided inference)와 슬라이싱 기반 미세조정을 제안한다. 항공 검출 데이터셋 VisDrone과 xView로 평가했고 Detectron2, MMDetection, YOLOv5와 통합되는 오픈소스다.^[inbox/processed/hw-20261021-ai-smallobj-sahi-akyon-2022.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 슬라이싱 추론만으로 AP +6.8%(FCOS), +5.1%(VFNet), +5.3%(TOOD).^[inbox/processed/hw-20261021-ai-smallobj-sahi-akyon-2022.md]
- 슬라이싱 미세조정 추가 시 누적 +12.7%(FCOS), +13.4%(VFNet), +14.5%(TOOD).^[inbox/processed/hw-20261021-ai-smallobj-sahi-akyon-2022.md]
- 소형·고고도 물체 검출 한계를 추론 방식 변경으로 완화하는 접근.^[inbox/processed/hw-20261021-ai-smallobj-sahi-akyon-2022.md]

## 한계·미확인
조각 수 증가에 따른 지연 증가량은 초록에 없음(미확인) - 실시간 제어 루프 적용 전 별도 측정 필요. 개선폭의 단위(퍼센트 vs 퍼센트포인트)는 초록 표기 그대로 옮김.^[inbox/processed/hw-20261021-ai-smallobj-sahi-akyon-2022.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
