---
title: "RGB-IR Fusion for UAV Object Detection"
created: 2026-08-02
updated: 2026-08-02
type: concept
tags: [drone, drone-ai, ai-autonomy]
sources: [inbox/fetch-2026-08-02-crossref-etfnet-an-efficient-transformer-based-rgbir-fusion-network-f.md]
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# RGB-IR Fusion for UAV Object Detection

Transformer 기반 RGB-IR 퓨전 네트워크(ETFNet)를 활용한 UAV 객체 검출 기술. 정보 융합(Information Fusion) 분야 연구.

## Overview

ETFNet은 효율적인 트랜스포머 기반 RGB-IR 퓨전 네트워크로, UAV(무인항공기) 객체 검출에 특화되어 있다. RGB 영상과 적외선(IR) 영상의 상보적 특성을 결합하여 다양한 조명 조건에서의 검출 성능을 향상시킨다.

## Key Research

**ETFNet: An efficient transformer-based RGB–IR fusion network for UAV object detection**^[inbox/fetch-2026-08-02-crossref-etfnet-an-efficient-transformer-based-rgbir-fusion-network-f.md]
- 저자: Nguyen Thi Lan, Tran Cao Truong, Nguyen Dinh Tan
- 게재: Information Fusion (2027-1)
- DOI: https://doi.org/10.1016/j.inffus.2026.104658

## Technical Approach

- **Transformer 기반 퓨전**: 어텐션 메커니즘을 활용한 RGB-IR 특징 융합
- **효율성 중시**: 임베디드 UAV 플랫폼에서의 실시간 처리 가능성
- **객체 검출 특화**: 항공 촬영 관점에서의 소형 객체 검출 문제 해결

## Related Technologies

- [[computer-vision-drone]] — 드론 컴퓨터 비전 기술
- [[yolo]] — 실시간 객체 검출 아키텍처
- [[drone-ai-agents]] — AI 기반 자율 드론 시스템

## Open Questions

- 실제 UAV 임베디드 하드웨어에서의 추론 속도 벤치마크
- 야간/열악한 기상 조건에서의 성능 평가
- 다른 센서 모달리티(예: LiDAR)와의 확장 가능성

## 📰 최근 관련 소식
- Pentagon approves long-range, autonomous counter-UAS system for use across the military after border testing (DefenseScoop, Tue, 09 Ju) — https://news.google.com/rss/articles/CBMiqwFBVV95cUxQQ2ZSVldfYnY3OWlpREdGRVVTaFNfNUFxX3h6TzJnREhOUzVfLU93bFllLXdnMGZkNFVaUWdHVUo4c1dyMkpXbEh4UzJBOFFSclhJdTlxMl9wOUVZTVFEUlFxQzNNZXU2c21QcW9FY1V4NGlHVkhQVzJjUF80dHh4ODZvc3ZCNlBiQ3NrQmd1Y2NEVDFtSFdXMDFKM3hDem9XM0tpb01xVmpSUHc?oc=5
- Linear Stability Analysis of an INDI Pitch-Rate Controller under Model Mismatch for a Tilt-Rotor VTOL UAV (arxiv.org, 2026-07-17) — http://arxiv.org/abs/2607.16471v1
- Army launches search for counter-drone missile priced under $150K (Breaking Defense, Wed, 05 Au) — https://news.google.com/rss/articles/CBMiowFBVV95cUxPd0hFSjR5eV81aHo3Y1RjYkFxYTU0ZlVnck9xNkZjMVhqY0t5V01KaW9TWVdUcDBFeGJJZzYxUE5qSm9XelF6MFZOUktvX29zdlV3bVVCaEdlU0NMeXAyQk9IUVh4ZldQLWRFOUFzNUhLVnRaNmoxbmtGS3JlV0Q1UV92am1ZdENhV091LWZzdlBibUFHbVdzRWVoV0hzRTBSWlQ0?oc=5
- Pentagon launches online marketplace for counter-UAS technology (Defense News, Mon, 10 Au) — https://news.google.com/rss/articles/CBMixAFBVV95cUxNSi0xTzZCaE15Ymd5YlJkME14LWpmbWJsT2FHZW1xbjl1M3ZnNTNXWmtDRUgySGJVSXo5cFN6a1NRRmZrSHBPbTltcWJnWF82a0VFbE5ua2UtUEstSlI3ZW52T3RZLWx2dktiM1g1RFQ2Zmd1SXpyMmJwVGJSSm9yYjBNMWZXUUVKeHJfLUk1VTYxaUpQZEF4MFdwbVdFUF9QdlBPWjEzQjFWWXFNb0FHb0ZMQnlFNXpfTEpISzYzUUV1bU1w?oc=5
