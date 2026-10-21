---
title: "Omniverse Replicator (omni.replicator documentation)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: simulation-test
source: https://docs.omniverse.nvidia.com/py/replicator/latest/index.html
authors: "NVIDIA"
published: "미확인"
tags: [drone, synthetic-data, isaac-sim, replicator]
---
## 핵심 내용
Omni Replicator는 합성 데이터 생성(SDG) 도구·파이프라인을 만드는 Omniverse 확장이다. 확장 omni.replicator.core(파이썬 API, OmniGraph 노드)와 omni.replicator.replicator_yaml(YAML 설정)이 있다. 랜덤화 분포(uniform, normal, log-uniform, multinomial, sequence)와 재질·텍스처·조명·자세 랜덤화 노드, 주석기(2D/3D 바운딩 박스, 인스턴스/시맨틱 분할, 카메라 파라미터, 포인트클라우드), Writer 노드, 증강(모션 블러, 대비, cut-mix 등)을 제공한다.
원문 인용: "lets developers easily build custom synthetic data generation (SDG) tools and pipelines."

## 설계·운용에 쓸 수 있는 지침
- 도메인 랜덤화로 드론 시점 합성 학습 데이터를 만들 때 주석기와 Writer를 조합.

## 한계·미확인
- 페이지에 KITTI/COCO 출력 지원이 적혀 있지 않아 미확인. 드론 전용 예제 미확인.
