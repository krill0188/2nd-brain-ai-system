---
title: "MG-MOT: 메타데이터 유도 UAV 해상 다중객체 추적"
created: 2026-10-18
updated: 2026-10-18
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-10-18-arxiv-sea-you-later-metadata-guided-long-term-re-identification-fo.md]
confidence: medium
contested: false
contradictions: []
---

# MG-MOT (UAV 해상 장기 재식별)

**출처**: arXiv 2311.03561 v2 (2023-11-06), Cheng-Yen Yang 외. 초록 기준.

UAV 해상 영상은 작은 표적과 짐벌의 급격한 움직임 때문에 단기 ReID가 어렵고, 외형 다양성이 부족해 장기 ReID도 어렵다.^[inbox/processed/fetch-2026-10-18-arxiv-sea-you-later-metadata-guided-long-term-re-identification-fo.md]

- **방법**: 모션 기반 MOT 알고리즘 MG-MOT가 UAV 메타데이터(GPS 위치, 고도, 카메라 자세)를 활용해 단기 트랙을 일관된 장기 트랙으로 병합한다.
- **결과**: SeaDroneSee 추적 데이터셋 기반 UAV 해상 객체 추적 챌린지에서 테스트 분할 HOTA 69.5%, IDF1 85.9%를 달성했다고 보고한다.

관련: [[computer-vision-drone]], [[high-speed-drone-tracking]], [[kci-ground-target-tracking-retinanet-kalman]].
