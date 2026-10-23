---
title: "Isaac ROS 공식 Performance Summary (release-3.2): AGX Orin / Orin NX / Orin Nano Super 노드·그래프별 fps·지연(ms)"
created: 2026-10-24
updated: 2026-10-24
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, edge-inference, jetson-orin, orin-nx, latency-ms, fps, isaac-ros, stereo-depth, rt-detr]
sources: [inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]
confidence: medium
contested: false
contradictions: []
---

# Isaac ROS 공식 Performance Summary (release-3.2): AGX Orin / Orin NX / Orin Nano Super 노드·그래프별 fps·지연(ms)

- 원문: https://nvidia-isaac-ros.github.io/v/release-3.2/performance/index.html ; 최신판 https://nvidia-isaac-ros.github.io/performance/index.html ; 벤치 저장소 https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_benchmark (release-3.2 README)^[inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]

## 핵심 내용
출처 유형: NVIDIA Isaac ROS 공식 문서(curl + 브라우저 UA로 HTML 열람, 표 파싱). 이전 3회(20261021~23)에 없던 신규 출처이며, **Orin NX 를 포함한 세 모듈(AGX Orin, Orin NX, Orin Nano Super 8GB)이 한 표에** 있는 첫 NVIDIA 공식 표. 신뢰도: 높음(제조사 공식, 자체 측정).^[inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]
조건(원문): 입력 크기 열에 명시(720p/1080p/576p/544p/VGA 등). fps = 입력→노드/그래프→출력 구간의 최대 지속 처리율(입력 발행률을 자동 조정해 프레임 손실 5% 미만 지점, 5회 평균에서 최대·최소 제외). 지연 = 30 Hz 발행 조건에서 측정("@ 30Hz"). release-3.2 가 요구하는 소프트웨어: JetPack 6.1 / 6.2 (getting_started 페이지 System Requirements 표). 정밀도·배치·전력모드는 표에 없음(원문 "전력 설정을 적절히 구성하라"만 언급). 모델: DOPE, PeopleSemSegNet, DetectNet, RT-DETR(SyntheticaDETR), SAM/Mobile SAM, ESS(DNN Stereo Disparity Full/Light) 등 NVIDIA 모델. "–" 는 원문 공란(미측정 또는 메모리 부족 등 사유 미표기).^[inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]
### 표 1. 노드(Node) — release-3.2
| Node | 입력 | AGX Orin (fps / 지연) | Orin NX (fps / 지연) | Orin Nano Super 8GB (fps / 지연) | x86 RTX 4090 |
|---|---|---|---|---|---|
| AprilTag Node | 720p | 178 fps 6.3 ms @ 30Hz | 116 fps 9.4 ms @ 30Hz | 123 fps 8.6 ms @ 30Hz | 596 fps 0.86 ms @ 30Hz |
| Freespace Segmentation Node | 576p | 3340 fps 1.7 ms @ 30Hz | 2530 fps 1.5 ms @ 30Hz | 2140 fps 1.9 ms @ 30Hz | 3500 fps 0.44 ms @ 30Hz |
| Depth Segmentation Node | 576p | 41.4 fps 80 ms @ 30Hz | 28.1 fps 98 ms @ 30Hz | – | 105 fps 25 ms @ 30Hz |
| FoundationPose Pose Estimation Node | 720p | 1.54 fps 780 ms @ 30Hz | – | – | 9.56 fps 110 ms @ 30Hz |
| DNN Stereo Disparity Node Full | 576p | 72.5 fps 17 ms @ 30Hz | 42.1 fps 26 ms @ 30Hz | – | 350 fps 2.1 ms @ 30Hz |
| DNN Stereo Disparity Node Light | 288p | 304 fps 5.9 ms @ 30Hz | 143 fps 9.6 ms @ 30Hz | – | 350 fps 1.6 ms @ 30Hz |
| Stereo Disparity Node | 1080p | 118 fps 11 ms @ 30Hz | 78.1 fps 14 ms @ 30Hz | 83.8 fps 13 ms @ 30Hz | 943 fps 1.6 ms @ 30Hz |
| Rectify Node | 1080p | 800 fps 2.8 ms @ 30Hz | 572 fps 3.3 ms @ 30Hz | 595 fps 3.8 ms @ 30Hz | 2500 fps 0.57 ms @ 30Hz |
| TensorRT Node DOPE | VGA | 30.8 fps 37 ms @ 30Hz | 15.5 fps 55 ms @ 30Hz | 20.8 fps 51 ms @ 30Hz | 298 fps 5.3 ms @ 30Hz |
| Triton Node DOPE | VGA | 31.2 fps 340 ms @ 30Hz | 15.5 fps 55 ms @ 30Hz | 22.2 fps 490 ms @ 30Hz | 277 fps 4.7 ms @ 30Hz |
| TensorRT Node PeopleSemSegNet | 544p | 489 fps 4.6 ms @ 30Hz | 258 fps 7.1 ms @ 30Hz | 269 fps 6.2 ms @ 30Hz | 619 fps 2.2 ms @ 30Hz |
| Triton Node PeopleSemSegNet | 544p | 216 fps 5.5 ms @ 30Hz | 143 fps 8.2 ms @ 30Hz | – | 585 fps 2.5 ms @ 30Hz |
| DNN Image Encoder Node | VGA | 339 fps 13 ms @ 30Hz | 375 fps 12 ms @ 30Hz | – | 480 fps 6.0 ms @ 30Hz |
| Occupancy Grid Localizer Node | ~50 sq. m | 19.6 fps 57 ms @ 30Hz | 8.36 fps 130 ms @ 30Hz | 9.02 fps 120 ms @ 30Hz | 50.1 fps 8.5 ms @ 30Hz |
| H.264 Decoder Node | 1080p | 188 fps 7.3 ms @ 30Hz | – | – | 596 fps 2.6 ms @ 30Hz |
| H.264 Encoder Node I-frame Support | 1080p | 402 fps 12 ms @ 30Hz | – | – | 412 fps 3.2 ms @ 30Hz |
| H.264 Encoder Node P-frame Support | 1080p | 465 fps 11 ms @ 30Hz | – | – | 596 fps 2.0 ms @ 30Hz |
| Nvblox Node | – | 4.94 fps 34.0 ms | 4.94 fps 155 ms | 4.93 fps 87.4 ms | 4.94 fps 200 ms |

### 표 2. 그래프(Graph) — release-3.2
| Graph | 입력 | AGX Orin (fps / 지연) | Orin NX (fps / 지연) | Orin Nano Super 8GB (fps / 지연) | x86 RTX 4090 |
|---|---|---|---|---|---|
| AprilTag Graph | 720p | 178 fps 9.1 ms @ 30Hz | 111 fps 11 ms @ 30Hz | 120 fps 11 ms @ 30Hz | 596 fps 1.4 ms @ 30Hz |
| Freespace Segmentation Graph | 576p | 40.3 fps 79 ms @ 30Hz | 27.6 fps 98 ms @ 30Hz | 31.8 fps 55 ms @ 30Hz | 102 fps 30 ms @ 30Hz |
| Centerpose Pose Estimation Graph | VGA | 44.8 fps 43 ms @ 30Hz | 29.0 fps 51 ms @ 30Hz | 29.8 fps 50 ms @ 30Hz | 50.2 fps 14 ms @ 30Hz |
| DOPE Pose Estimation Graph | VGA | 27.3 fps 54 ms @ 30Hz | 15.2 fps 73 ms @ 30Hz | – | 186 fps 12 ms @ 30Hz |
| DNN Stereo Disparity Graph Full | 576p | 89.8 fps 19 ms @ 30Hz | 35.2 fps 34 ms @ 30Hz | – | 350 fps 5.8 ms @ 30Hz |
| DNN Stereo Disparity Graph Light | 288p | 184 fps 14 ms @ 30Hz | 128 fps 14 ms @ 30Hz | – | 350 fps 5.2 ms @ 30Hz |
| Stereo Disparity Graph | 1080p | 111 fps 15 ms @ 30Hz | 72.2 fps 18 ms @ 30Hz | 77.4 fps 18 ms @ 30Hz | 692 fps 4.6 ms @ 30Hz |
| DetectNet Object Detection Graph | 544p | 55.4 fps 37 ms @ 30Hz | 25.7 fps 45 ms @ 30Hz | 33.0 fps 43 ms @ 30Hz | 262 fps 11 ms @ 30Hz |
| RT-DETR Object Detection Graph SyntheticaDETR | 720p | 56.5 fps 29 ms @ 30Hz | 33.3 fps 40 ms @ 30Hz | 37.3 fps 37 ms @ 30Hz | 450 fps 5.5 ms @ 30Hz |
| TensorRT Graph PeopleSemSegNet | 544p | 436 fps 10 ms @ 30Hz | 212 fps 13 ms @ 30Hz | 224 fps 13 ms @ 30Hz | 587 fps 3.7 ms @ 30Hz |
| SAM Image Segmentation Graph Full SAM | 720p | 2.22 fps 390 ms @ 30Hz | – | – | 14.6 fps 74 ms @ 30Hz |
| SAM Image Segmentation Graph Mobile SAM | 720p | 8.40 fps 120 ms @ 30Hz | 2.22 fps 240 ms @ 30Hz | 2.22 fps 230 ms @ 30Hz | 62.5 fps 22 ms @ 30Hz |

### 표 3. 최신 판(문서 하단 "Last updated on Sep 21, 2026", 현행 페이지) — Orin 계열 열만
| Node/Graph | 입력 | AGX Orin | Orin Nano Super 8GB |
|---|---|---|---|
| AprilTag Node | 720p | 189 fps / 5.3 ms | 104 fps / 9.6 ms |
| Stereo Disparity Node | 1080p | 124 fps / 8.6 ms | 66.1 fps / 17 ms |
| Rectify Node | 1080p | 1220 fps / 0.28 ms | 470 fps / 0.58 ms |
| TensorRT Node DOPE | VGA | 47.4 fps / 1.9 ms | 20.8 fps / (지연 공란) |
| TensorRT Node PeopleSemSegNet | 544p | 481 fps / 1.5 ms | 234 fps / 1.8 ms |
| DNN Stereo Disparity Graph Full | 576p | 66.5 fps / 17 ms | 34.8 fps / 30 ms |
| DNN Stereo Disparity Graph Light | 288p | 75.5 fps / 24 ms | 82.2 fps / 13 ms |
| DetectNet Graph | 544p | 73.5 fps / 15 ms | 30.4 fps / 37 ms |
| RT-DETR Graph (SyntheticaDETR) | 720p | 87.3 fps / 13 ms | 40.0 fps / 27 ms |
| Mobile SAM Graph | 720p | 8.40 fps / (공란) | 4.80 fps / (공란) |
최신 판 방법론 문구는 release-3.2 와 다름: "지연 = 별도 30 Hz 시험에서 첫 송신 프레임~첫 수신 프레임 시간". 따라서 **3.2 와 최신 판의 지연값을 같은 열로 비교하지 말 것**(예: 같은 AGX Orin Stereo Disparity 가 3.2=11 ms, 최신=8.6 ms 이나 방법론 문구가 다르고 SW 버전 차이는 미확인). 최신 판은 Orin NX 열이 없음(3.1·3.2 판에만 NX 존재; 3.1 은 Orin Nano 8GB 표기이며 값이 달라 이번에 옮기지 않음).^[inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]
## 설계에 쓸 수 있는 지침
- Orin NX 와 Nano Super 의 상대 비교는 release-3.2 표 한 장 안에서만. 예(원문): DetectNet 544p 그래프 AGX 55.4 fps/37 ms, NX 25.7 fps/45 ms, Nano Super 33.0 fps/43 ms. 즉 NX 가 Nano Super 보다 항상 빠르지 않음(원문 수치 기준 이 항목은 Nano Super 가 높음).^[inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]
- 스테레오 깊이(ESS) 지연은 Full(576p) 대비 Light(288p) 가 큼직하게 짧다: 3.2 의 Orin NX Full 42.1 fps/26 ms vs Light 143 fps/9.6 ms (노드 기준).^[inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]
- 이 지연은 ROS 2 노드 파이프라인(입력→출력) 값이라 순수 TensorRT 추론 ms 와 다름. Ultralytics 표(전후처리 제외 ms)와 혼합 금지.^[inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]
## 한계·미확인
- JetPack 의 정확한 마이너 버전, TensorRT 버전, 정밀도(FP16/INT8), 배치, 전력모드: 표에 없음(release-3.2 는 JetPack 6.1/6.2 요구라고만 명시). 재확인 필요: isaac_ros_benchmark 저장소 release-3.2 스크립트의 모델 엔진 설정.^[inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]
- 표 파싱은 HTML 셀 단위이며 원문과 1:1 대조는 표 1·2 의 일부(AprilTag, DetectNet, RT-DETR)만 재확인함.^[inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]
- 드론 탑재 관련성: 모델이 로봇(AMR) 위주(DOPE, PeopleSemSegNet 등). 드론 항공 영상 검출 지연이 아님.^[inbox/processed/hw-20261024-data-edge-isaac-ros-performance-summary-release-3-2-orin-nx-nano-agx.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]
