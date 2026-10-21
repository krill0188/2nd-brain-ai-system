---
title: "Model-Based Systems Engineering Framework for SysML-Driven Design of Autonomous UAVs"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: simulation-test
source: arXiv:2608.09547
authors: "Deekshitha Angadi, Naveena Budda, Vikas Agarwal, Mohamed Samshad, Bharath Kumar Suryadevara, Narsimlu Kemsaram"
published: "2026-08-10 (ICAAV-2026 채택, 2026-08-20~21 Bengaluru)"
tags: [drone, mbse, sysml, ros2]
---
## 핵심 내용
자율 UAV 설계를 SysML로 하는 MBSE 프레임워크. 개발을 이해관계자 요구, 기능 분해, 논리 아키텍처, 물리/소프트웨어 할당의 4개 연결 계층으로 정리한다. 논리 아키텍처는 ROS 2 소프트웨어 아키텍처로 매핑되어 SysML 블록이 노드, 포트와 커넥터가 토픽 등이 된다. 이륙, 웨이포인트 항법, 장애물 회피 시나리오로 예시하며 시뮬레이션·배포 전 모호성을 줄이고 추적성을 높이는 것이 목표다.
원문 인용: "uses the Systems Modeling Language (SysML) as a formal design backbone"

## 설계·운용에 쓸 수 있는 지침
- SysML 블록-ROS 2 노드, 포트/커넥터-토픽 대응 규칙으로 요구에서 코드 골격까지 추적 가능.

## 한계·미확인
- 초록에 수치 없음. 기존 ~/2nd mbse-uav-sysml 문서와 같은 논문인지는 ID 검색에서 일치 없음(별개로 판단). 자동 코드 생성 여부 미확인.
