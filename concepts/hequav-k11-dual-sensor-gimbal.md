---
title: "HEQUAV K11 듀얼 센서 짐벌 + Scepter 15 컨트롤러"
created: 2026-10-05
updated: 2026-11-01
type: concept
domain: hardware
ontology_class: Gimbal
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-05-yt-im-installing-a-smart-hequav-k11-gimbal-to-try.md, inbox/processed/fetch-2026-11-01-yt-hequav-k11-and-scepter-15-android-radio-my-setup-steps.md]
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

## 배선·연결 구성 (Painless360 후속 영상, 2026-10-31, 자막 기준)

Holybro X650 프레임 + Pixhawk 6C(ArduPilot) 조합에 K11과 Scepter 15를 설치한 리뷰어의 배선 설명이다. 영상 자막은 앞부분만 확보돼 있어 바인딩·라디오 설정·QGC FPV 추가 부분은 자막에서 확인되지 않는다.^[inbox/processed/fetch-2026-11-01-yt-hequav-k11-and-scepter-15-android-radio-my-setup-steps.md]

- **전원**: Maytech 12 V BEC로 6S 비행 배터리를 12 V로 낮춰 수신기/VTX 유닛과 짐벌 카메라에 함께 공급(XT30으로 배전반에 연결). 리뷰어는 전압이 높으면 내부 강압 발열이 커진다며 허용 범위의 낮은 쪽을 쓴다.
- **영상**: 수신기/VTX 유닛과 짐벌 사이는 이더넷 연결(키트 케이블에 이미 결선, 짐벌 커넥터의 상당수 핀이 이더넷용)이며 영상 전송에 쓰인다.
- **S.BUS**: 수신기 출력이 FC와 짐벌 양쪽으로 들어간다. 상위 채널이 팬·틸트에 매핑되고 스틱 극단에서 줌도 처리한다.
- **MAVLink 텔레메트리**: FC의 여분 UART 2개를 MAVLink 2, 115200 baud로 설정한다. 하나는 수신기/VTX로 텔레메트리를 보내 라디오의 QGC에서 비행을 모니터링하고, 다른 하나(TX/RX 쌍)는 짐벌 쪽 연결이다. ArduPilot에서 SERIAL1·SERIAL2(TELEM1·TELEM2)를 MAVLink 2/115200으로 맞췄다.
- **케이블 주의**: 키트 케이블은 매뉴얼 기준 결선이라 Holybro 6C 커넥터에 맞게 핀을 다시 배열해야 했다. 루프 케이블이 S.BUS 외에는 모두 검은색이라 TX↔RX 교차 연결을 신중히 확인해야 한다.
- **확인 결과**: 최초 전원 투입 때 ArduPilot·Mission Planner에서 S.BUS 움직임이 확인됐다. 실제 비행 시험은 아직이었다.
- 리뷰어 평: 필요한 설정 정보 상당수가 매뉴얼에 없었고, 제조사가 피드백을 받아 매뉴얼에 배선도를 추가했다.

관련: [[holybro-6c]], [[qgroundcontrol]], [[mavlink-protocol]]

## 관련 개념

- [[drone-payload-systems]] — 드론 페이로드 일반
- [[px4-flight-stack]] — S.BUS 입력을 받을 수 있는 대표 FC 스택
- [[ardupilot]] — 동일

## 📰 최근 관련 소식
- [Painless360] HEQUAV K11 and Scepter 15 Android Radio: My Setup Steps (youtube.com, 2026-10-31) — https://www.youtube.com/watch?v=PqD0aSRnZ_I
- [Painless360] I'm installing a 'smart' HEQUAV K11 gimbal to try... (youtube.com, 2026-10-04) — https://www.youtube.com/watch?v=GdQGXZ3HGYw
