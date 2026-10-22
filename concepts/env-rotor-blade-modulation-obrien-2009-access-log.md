---
title: "O'Brien·Hayhurst·Gupta 2009 'Effects of Rotor Blade Modulation on GNSS Receiver Measurements' 접근 기록 + 인접 공개 논문(Barbiero 2013)"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: hardware
tags: [drone, hardware, gnss, rotor-blade-modulation, antenna, access-log]
sources: [inbox/processed/hw-20261023-env-rotor-blade-modulation-obrien-2009-access-log.md]
confidence: medium
contested: false
contradictions: []
---

# O'Brien·Hayhurst·Gupta 2009 'Effects of Rotor Blade Modulation on GNSS Receiver Measurements' 접근 기록 + 인접 공개 논문(Barbiero 2013)

- 원문: https://ece.osu.edu/news/2009/10/ece-faculty-and-students-earn-three-best-presentation-awards-institute-navigation-confe ; https://core.ac.uk/works/7436298 ; https://hal-onera.archives-ouvertes.fr/hal-00996725^[inbox/processed/hw-20261023-env-rotor-blade-modulation-obrien-2009-access-log.md]

## 핵심 내용
- O'Brien 2009: 제목·저자·발표(ION GNSS 2009, 세션 E2 최우수 발표상)는 OSU ECE 뉴스(검색 결과 기준)로만 확인. 전문 미확인. 내용은 헬리콥터 등 회전익의 블레이드 변조이며 모터 전기 노이즈 연구가 아님(제목 기준).^[inbox/processed/hw-20261023-env-rotor-blade-modulation-obrien-2009-access-log.md]
- 접근 시도: ION 논문 페이지/검색(유료·검색 미노출), ResearchGate(403), CORE/HAL(HAL은 Anubis 봇 차단 → 우회 안 함), oatao.univ-toulouse.fr PDF(curl 연결 실패, Bright Data scrape 빈 응답).^[inbox/processed/hw-20261023-env-rotor-blade-modulation-obrien-2009-access-log.md]
- 인접 공개 자료(초록만 열람, CORE 페이지): Barbiero, Letestu, Deloues, Vincent 등, "Effects of rotor blade modulation on GNSS anti-jamming algorithms" (HAL/Toulouse 2013-12-31 등록). 헬리콥터 장착 안테나 신호를 EM 근사법으로 시뮬레이션, 세 가지 STAP 알고리즘의 post-C/N0 와 공분산 추정 비교, EC-120 헬리콥터 + L-band CW 재머 실험으로 확인. "RBM can degrade significantly anti-jamming performance"(초록 문구). 정량 dB 값은 본문 미열람.^[inbox/processed/hw-20261023-env-rotor-blade-modulation-obrien-2009-access-log.md]
## 한계·미확인
- O'Brien 2009 본문·정량값 전부 미확인. 멀티콥터 로터 근접 안테나 C/N0 저하 측정 논문은 이번에도 확인 못 함(대신 env-uas-onboard-rfi-cn0-stubbs-akos-2016 의 기체 ON/OFF 실측을 참조).^[inbox/processed/hw-20261023-env-rotor-blade-modulation-obrien-2009-access-log.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
