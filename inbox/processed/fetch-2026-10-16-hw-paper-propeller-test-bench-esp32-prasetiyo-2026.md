---
title: "Comparative Efficiency Measurement of UAV Propellers Using a Microcontroller-Based Test Bench"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://doi.org/10.48084/etasr.15694
tags: [drone, hardware, propulsion, propeller, test-bench, efficiency]
authors: Erwan Eko Prasetiyo, Erwhin Irmawan, Gaguk Marausna, Ikbal Rizki Putra, Hendriana Helda Pratama, Fadhli Atha Hidayat
published: 2026-02-09 (Engineering, Technology & Applied Science Research vol. 16, no. 1, pp. 31831-31838)
---

# ESP32 기반 프로펠러 효율 측정 벤치 (Prasetiyo et al., 2026)

## 핵심 내용
- ESP32 마이크로컨트롤러로 기계적 추력, 전기 소비 전력, 출구 공기 유속을 동시에 측정하는 저비용 시험대를 구현했다.
- 10×5인치 프로펠러 3종(사출 성형, 실리콘 몰드 주조, 3D 프린팅 제작)을 비교했다.
- 총 추진 효율은 초록 기준 약 18%에서 최고 30%였다. 상용 프로펠러가 가장 효율이 높았다.

## 설계에 쓸 수 있는 지침
- 추력·전력·유속을 한 번에 기록하는 구성은 자체 추진계 검증 벤치를 저비용으로 만드는 참고 구조로 쓸 수 있다.
- 제작 방식(사출·주조·3D 프린팅)에 따라 효율이 달라진다는 점은 프로펠러 소싱 기준으로 참고할 만하다. 자체 제작 프로펠러 사용 시 상용품과 비교 측정이 필요하다.

## 한계·미확인
- 10×5인치 소형 프로펠러 실험이라 중·대형 멀티로터(14인치 이상)에 그대로 적용하기 어렵다.
- 측정 정확도(로드셀 분해능, 오차 범위)와 전력 측정 방식의 수치는 초록에 없어 미확인.
- 3종 샘플 수가 적어 일반화에는 한계가 있다.
