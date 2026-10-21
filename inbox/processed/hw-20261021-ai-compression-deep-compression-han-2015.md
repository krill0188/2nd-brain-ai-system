---
title: "Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: edge-ai-compute
source: https://arxiv.org/abs/1510.00149
authors: Song Han, Huizi Mao, William J. Dally
published: 2015-10-01 (v5 2016-02-15, ICLR 2016 oral)
tags: [drone, ai, model-compression, pruning, quantization]
---
## 핵심 내용
가지치기, 학습된 양자화, 허프만 부호화의 3단계 파이프라인으로 정확도 손실 없이 저장 용량을 35x~49x 줄인다.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- AlexNet 240MB -> 6.9MB(35x), VGG-16 552MB -> 11.3MB(49x), 정확도 손실 없음.
- 가지치기로 연결 수 9x~13x 감소, 연결당 비트 32 -> 5.
- CPU·GPU·모바일 GPU에서 레이어 단위 3x~4x 속도 향상, 3x~7x 에너지 효율 향상.

## 한계·미확인
2015년 CNN(AlexNet/VGG) 기준이라 현대 검출기(YOLO 등)에 그대로 적용된다는 근거는 없음(미확인).
