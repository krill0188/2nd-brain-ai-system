---
title: "Modeling Varying Camera-IMU Time Offset in Optimization-Based Visual-Inertial Odometry"
created: 2026-10-22
captured: 2026-10-22
type: paper
domain: ai-autonomy
source: https://arxiv.org/abs/1810.05456 (PDF 본문 열람)
authors: Yonggen Ling, Linchao Bao, Zequn Jie, Fengming Zhu, Ziyang Li, Shanmin Tang, Yongsheng Liu, Wei Liu, Tong Zhang
published: 2018-10-12
tags: [drone, time-synchronization, camera-imu, rolling-shutter, time-offset, vio]
---
## 핵심 내용 (arXiv)
초록: 대부분 연구는 global shutter와 동기화된 측정을 가정하나 소비자 기기는 rolling shutter와 불완전 동기화를 가짐. 카메라-IMU 시간 오프셋을 미지 변수로 둔 비선형 최적화 단안 VIO를 제안하고, 롤링셔터 효과와 불완전 동기를 통합 처리. 본문 실험:
- EuRoC(원래 동기된 데이터)에 오프셋을 0/30/60 ms로 시뮬레이션해 OKVIS, VINS-Mono와 비교: 동기된 경우 VINS-Mono와 제안법은 비슷하고 OKVIS가 가장 나쁨. 오프셋이 커지면 둘 다 악화. 60 ms에서 OKVIS는 시퀀스 2~5에서 추적 실패. 90 ms에서는 OKVIS·VINS-Mono 모두 합리적 추정 불가(비교 생략).
- 모바일 폰 초기화: 시간 오프셋을 고려한 초기화는 20회 중 18회 성공(90%) vs 기존 [28] 방식 14회(70%). 실패한 2개 시퀀스는 카메라-IMU 오프셋이 100 ms 초과라고 본문이 서술.
- 모바일 폰에서 비선형 최적화 1회에 "70±10ms".

## 설계에 쓸 수 있는 지침 (원문 수치만)
- 카메라-IMU 동기가 흐트러진 시스템에서 오프셋 모델이 없으면 30~60 ms 구간에서 추적이 급격히 악화될 수 있음(이 실험 기준).

## 한계·미확인
- 하드웨어 동기와 소프트웨어 동기의 직접 비교는 아님(시뮬레이션 주입). 오프셋-정확도 수치(그림 4)는 표로 추출하지 못함. 드론 시험 아님.
