---
title: "Physical Adversarial Patch Attacks on Drone Object Detection: Digital-Physical Domain Gap Analysis"
created: 2026-08-23
updated: 2026-08-23
type: concept
tags: [drone, ai-autonomy, adversarial-ml, security, computer-vision]
sources: [inbox/fetch-2026-08-23-kci-드론-기반-객체-탐지-시스템에-대한-물리적-적대적-패치-공격-디지털-물리-도메인-갭-분석-및-완화.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# Physical Adversarial Patch Attacks on Drone Object Detection

KCI paper (2026) analyzing digital-physical domain gaps in adversarial patch attacks against drone-mounted YOLOv5 systems.

## Overview

Deep learning-based object detection models face adversarial patch attacks that succeed in digital environments but degrade significantly in physical world applications. This research experimentally identifies and analyzes key factors causing the digital-physical domain gap.

## Domain Gap Factors

Four categories of domain gap factors identified:

1. **Print media color distortion** — NPS (Print media color distortion)
2. **Camera capture transformation** — Differentiable print-capture simulation pipeline
3. **Time-varying lighting changes** — Natural light EoT (Expectation over Transformation)
4. **Camera resolution and color separation limitations** — Grid-based parameterization and camera profiling

## Mitigation Techniques

- NPS for print media color distortion
- Differentiable print-capture simulation pipeline
- Natural light EoT for lighting variations
- Grid-based parameterization with camera profiling

## Validation

Tested on Intel RealSense D435i equipped custom drone environment. Confirmed consistent success in both misdetection and misclassification attacks.

## Source

- **Author**: 심상훈 (고려대학교)
- **Journal**: 정보보호학회논문지 (2026)
- **Link**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003368967

## Related

- [[yolo]] — YOLO object detection architecture
- [[computer-vision-drone]] — Drone computer vision applications
- [[drone-ai-agents]] — AI agents for drone security
