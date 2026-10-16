---
title: "navigation-slam SW 레지스트리"
created: 2026-10-17
captured: 2026-10-17
type: software-registry
domain: software-ecosystem
category: navigation-slam
tags: [drone, software, navigation-slam]
---
# navigation-slam SW

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| VINS-Mono | 오픈소스 | GPL-3.0 | HKUST Aerial Robotics Group | https://github.com/HKUST-Aerial-Robotics/VINS-Mono | 저장소 설명: 단안 시각-관성 상태 추정기 | 미확인 |
| VINS-Fusion | 오픈소스 | GPL-3.0 | HKUST Aerial Robotics Group | https://github.com/HKUST-Aerial-Robotics/VINS-Fusion | 저장소 설명: 최적화 기반 멀티센서 상태 추정기 | 미확인 |
| ORB-SLAM3 | 오픈소스 | GPL-3.0 | UZ SLAM Lab(Univ. Zaragoza) | https://github.com/UZ-SLAMLab/ORB_SLAM3 | 저장소 설명: 시각/시각-관성/멀티맵 SLAM 라이브러리 | 미확인 |
| OpenVINS | 오픈소스 | GPL-3.0 | RPNG(Univ. Delaware) | https://github.com/rpng/open_vins | 저장소 설명: 시각-관성 항법 연구 플랫폼 | 미확인 |
| R-VIO2 | 오픈소스 | GPL-3.0 | RPNG | https://github.com/rpng/R-VIO2 | 저장소 설명: 제곱근 로봇중심 시각-관성 오도메트리 | 미확인 |
| Kimera-VIO | 오픈소스 | BSD-2-Clause | MIT SPARK Lab | https://github.com/MIT-SPARK/Kimera-VIO | 저장소 설명: SLAM 기능과 3D 메시 생성을 갖춘 VIO | 미확인 |
| Kimera-RPGO | 오픈소스 | BSD-2-Clause | MIT SPARK Lab | https://github.com/MIT-SPARK/Kimera-RPGO | 저장소 설명: 강건 포즈그래프 최적화 | 미확인 |
| SVO Pro (rpg_svo_pro_open) | 오픈소스 | GPL-3.0 | UZH Robotics and Perception Group | https://github.com/uzh-rpg/rpg_svo_pro_open | 미확인 | 저장소 설명 없음 |
| ROVIO | 오픈소스 | 미확인 | ETH ASL | https://github.com/ethz-asl/rovio | 미확인 | LICENSE는 BSD형 문구로 보이나 종류 미확정 |
| OKVIS | 오픈소스 | 미확인 | ETH ASL | https://github.com/ethz-asl/okvis | 저장소 설명: 키프레임 기반 시각-관성 SLAM | LICENSE 문구(Redistribution…)로 BSD형 추정. 종류 미확정 |
| maplab | 오픈소스 | Apache-2.0 | ETH ASL | https://github.com/ethz-asl/maplab | 저장소 설명: 모듈형 멀티모달 매핑 프레임워크 | 미확인 |
| msckf_vio | 오픈소스 | 자체 라이선스(Penn Software MSCKF_VIO, LICENSE.txt) | KumarRobotics(Univ. Pennsylvania) | https://github.com/KumarRobotics/msckf_vio | 저장소 설명: 빠른 자율비행용 강건 스테레오 VIO | 상업 이용 조건은 LICENSE.txt 확인 필요 |
| FAST-LIO | 오픈소스 | GPL-2.0 | HKU MARS Lab | https://github.com/hku-mars/FAST_LIO | 저장소 설명: 계산 효율적이고 강건한 LiDAR-관성 오도메트리 | 미확인 |
| FAST-LIVO2 | 오픈소스 | GPL-2.0 | HKU MARS Lab | https://github.com/hku-mars/FAST-LIVO2 | 저장소 설명: 직접법 LiDAR-관성-시각 오도메트리 | 미확인 |
| LIO-SAM | 오픈소스 | BSD-3-Clause | Tixiao Shan(저장소 소유자) | https://github.com/TixiaoShan/LIO-SAM | 저장소 설명: 스무딩·매핑 기반 LiDAR-관성 오도메트리 | 미확인 |
| A-LOAM | 오픈소스 | 미확인 | HKUST Aerial Robotics Group | https://github.com/HKUST-Aerial-Robotics/A-LOAM | 저장소 설명: LOAM의 개선 구현 | LICENSE에 BSD형 조항 문구 추정, 종류 미확정 |
| hdl_graph_slam | 오픈소스 | BSD-2-Clause | Kenji Koide(koide3) | https://github.com/koide3/hdl_graph_slam | 저장소 설명: 3D LiDAR 그래프 SLAM | 미확인 |
| GLIM | 오픈소스 | MIT | Kenji Koide(koide3) | https://github.com/koide3/glim | 저장소 설명: 포인트클라우드 기반 3D 위치추정·매핑 프레임워크 | 미확인 |
| RTAB-Map | 오픈소스 | 미확인 | IntRoLab(Univ. de Sherbrooke) | https://github.com/introlab/rtabmap | 저장소 설명: RTAB-Map 라이브러리와 독립 실행 앱 | LICENSE 헤더에 저작권 표기 확인, 종류 미확정 |
| Cartographer | 오픈소스 | Apache-2.0 | Cartographer 프로젝트 | https://github.com/cartographer-project/cartographer | 저장소 설명: 2D/3D 실시간 SLAM | 미확인 |
| stella_vslam | 오픈소스 | LICENSE.original / LICENSE.fork 구분(저장소 확인) | stella-cv | https://github.com/stella-cv/stella_vslam | 저장소 설명: OpenVSLAM의 비공식 포크 | 라이선스가 포크 이전/이후로 나뉨, 종류 미확인 |
| GTSAM | 오픈소스 | BSD(저장소 LICENSE: simplified BSD) | Borg Lab(Georgia Tech) | https://github.com/borglab/gtsam | 저장소 설명: 팩터그래프 기반 스무딩·매핑 C++ 라이브러리 | SLAM 백엔드 라이브러리 |
| g2o | 오픈소스 | 미확인 | Rainer Kümmerle 외 | https://github.com/RainerKuemmerle/g2o | 저장소 설명: 그래프 최적화 일반 프레임워크 | LICENSE 최상위 확인 못함 |
| Ceres Solver | 오픈소스 | 미확인 | Google | https://github.com/ceres-solver/ceres-solver | 저장소 설명: 대규모 비선형 최적화 라이브러리 | LICENSE 헤더 Google 저작권, 종류 미확정 |
| Isaac ROS Visual SLAM (cuVSLAM) | 오픈소스 | Apache-2.0 | NVIDIA | https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam | 저장소 설명: NVIDIA 가속 cuVSLAM 기반 시각 SLAM·오도메트리 ROS 패키지 | NVIDIA GPU 필요 여부는 문서 미확인 https://nvidia-isaac-ros.github.io |
| Slamcore | 상용 | 상용(약관 미확인) | Slamcore | https://slamcore.com | 페이지 설명: 시각 SLAM으로 센서 데이터를 공간 이해로 변환 | 드론 FC 연동 여부 미확인 |
| Emesent (SLAM LiDAR 매핑 솔루션) | 상용 | 상용(약관 미확인) | Emesent | https://www.emesent.com | 페이지 설명: SLAM 기반 LiDAR 매핑 전문 | 제품명 'Hovermap'은 페이지에서 확인 못함. 회사 URL만 확인 |
| Spectacular AI | 상용 | 상용(약관 미확인) | Spectacular AI | https://www.spectacularai.com | 페이지에서 설명 미추출 | 제품 세부 미확인 |
