---
title: "HEQUAV K11 듀얼 센서 짐벌 + Scepter 15 컨트롤러"
created: 2026-10-05
updated: 2026-10-05
type: concept
domain: hardware
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-05-yt-im-installing-a-smart-hequav-k11-gimbal-to-try.md]
confidence: low
contested: false
contradictions: []
---

# HEQUAV K11 듀얼 센서 짐벌

Painless360의 설치 예고 영상(2026-10-04, 자막 기준). 아직 비행 성능 검증 전이며 사양은 영상에서 읽은 제조사 값이다.
리뷰어는 Holybro X650 개발 프레임에 장착하고 설정·배선, 실제 비행 두 편을 계획 중이다.
^[inbox/processed/fetch-2026-10-05-yt-im-installing-a-smart-hequav-k11-gimbal-to-try.md]

## K11 짐벌 사양

- 무게 약 195 g, 입력 12~18 V(리뷰어는 12 V 사용, 6S 전원에서 BEC로 강압), 3축 기계식.
- 각도 한계: 피치 -90°~+30°, 요 ±120°, 최대 제어 속도 약 180°/s.
- 통신은 제조사 독자 프로토콜이어서 전용 컨트롤러가 필요.
- 광각+망원 듀얼 센서, 각 48 MP, 4K/30fps, H.264/H.265, JPEG·MP4. 하이브리드 줌 160배, 광학 약 11배.
- 광각: 초점거리 4.49 mm, f/2.8, 수평 FOV 약 71°·수직 약 56°. 망원: 좁은 FOV(수평 약 7°대), f/3.7~4.6.

## Scepter 15 컨트롤러·기체측 구성

- 안드로이드 11, 5.5인치 1080p/50fps 터치 화면(500 cd), 5000 mAh(약 4.5시간 사용), 약 700 g, 최대 통신거리 15 km 주장,
  HDMI 출력, 텔레메트리 수신 및 짐벌 제어. 수신기로서 S.BUS를 PX4/ArduPilot FC에 출력할 수 있다고 설명.
- 기체측: 짐벌/제어 보드와 영상 송수신 유닛이 이더넷 케이블로 연결.
- 리뷰어 평: 매뉴얼이 전문 통합 업체 대상이라 취미 사용자는 진입 장벽이 높으며, 제조사가 피드백을 받아 매뉴얼을 보강 중.

## 관련 개념

- [[drone-payload-systems]] — 드론 페이로드 일반
- [[px4-flight-stack]] — S.BUS 입력을 받을 수 있는 대표 FC 스택
- [[ardupilot]] — 동일

## 📰 최근 관련 소식
- [Painless360] I'm installing a 'smart' HEQUAV K11 gimbal to try... (youtube.com, 2026-10-04) — https://www.youtube.com/watch?v=GdQGXZ3HGYw
