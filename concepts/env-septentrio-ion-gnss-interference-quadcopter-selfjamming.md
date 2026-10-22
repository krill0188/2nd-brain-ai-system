---
title: "Septentrio 'GNSS Interference' ION 자료 — 쿼드콥터 카메라 self-jamming 사례"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: hardware
tags: [drone, hardware, gnss, rfi, self-jamming, septentrio, aim-plus]
sources: [inbox/processed/hw-20261023-env-septentrio-ion-gnss-interference-quadcopter-selfjamming.md]
confidence: medium
contested: false
contradictions: []
---

# Septentrio 'GNSS Interference' ION 자료 — 쿼드콥터 카메라 self-jamming 사례

- 원문: https://www.ion.org/gnss/upload/files/2157_Septentrio_GNSS_Interference_A5_LR.pdf^[inbox/processed/hw-20261023-env-septentrio-ion-gnss-interference-quadcopter-selfjamming.md]

## 핵심 내용
출처 유형: 제조사(Septentrio) 백서, ION 사이트 호스팅 PDF. curl 로 다운로드 후 Ghostscript 텍스트 추출(200 OK, 약 2.2 MB). 신뢰도: 중(비동료심사 벤더 자료, 정량 C/N0 수치 없음).^[inbox/processed/hw-20261023-env-septentrio-ion-gnss-interference-quadcopter-selfjamming.md]
- "Internal interference: self-jamming of drones caused by a camera" 절: 소형 드론은 전자장치가 GNSS 안테나 근처에 밀집, "motors or cameras often cause harmful interference that degrades or inhibits GNSS positioning" 이라고 서술.^[inbox/processed/hw-20261023-env-septentrio-ion-gnss-interference-quadcopter-selfjamming.md]
- 사례: 쿼드콥터에 소비자용 액션카메라(GoPro Hero 2) 장착 시 L1 스펙트럼에 24 MHz 간격 피크 3개(MMC/SD 로깅 인터페이스가 원인) 관측(AsteRx4 수신기). RTK 상실은 카메라를 차폐 케이스에 넣고 AIM+ 간섭 완화를 켜서 해결.^[inbox/processed/hw-20261023-env-septentrio-ion-gnss-interference-quadcopter-selfjamming.md]
## 설계에 쓸 수 있는 지침
- 모터보다 카메라·로깅 인터페이스 같은 디지털 소스가 L1 을 직접 오염시킨 실사례. 스펙트럼 뷰로 소스 식별 후 차폐·거리 확보.^[inbox/processed/hw-20261023-env-septentrio-ion-gnss-interference-quadcopter-selfjamming.md]
## 한계·미확인
- "40 cm 이상 이격" 및 "L1 C/N0 12 dB 저하" 문구는 검색 요약에서만 보였고, 출처로 지목된 논문(ResearchGate 'GNSS Interference in Unmanned Aerial Systems')은 403 으로 미열람 → 이 파일에는 수치로 쓰지 않음. 모터/ESC 정량 데이터 없음.^[inbox/processed/hw-20261023-env-septentrio-ion-gnss-interference-quadcopter-selfjamming.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
