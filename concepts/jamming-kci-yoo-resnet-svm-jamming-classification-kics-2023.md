---
title: "ResNet/SVM-Based GNSS Jamming Classification Scheme"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: security
ontology_class: GNSSInterferenceSecurity
tags: [drone, gnss, kci]
sources: [inbox/processed/hw-20261021-jamming-kci-yoo-resnet-svm-jamming-classification-kics-2023.md]
confidence: medium
contested: false
contradictions: []
---

# ResNet/SVM-Based GNSS Jamming Classification Scheme

- 원문: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003024330^[inbox/processed/hw-20261021-jamming-kci-yoo-resnet-svm-jamming-classification-kics-2023.md]
- 저자: Seungsoo Yoo, 유재덕, Soeun Heo, Kim Sun Yong^[inbox/processed/hw-20261021-jamming-kci-yoo-resnet-svm-jamming-classification-kics-2023.md]
- 발행: 2023 (한국통신학회논문지, vol. 48, no. 12, p. 1589; DOI 10.7840/kics.2023.48.12.1589)^[inbox/processed/hw-20261021-jamming-kci-yoo-resnet-svm-jamming-classification-kics-2023.md]

## 핵심 내용
KCI 포털 수록 논문(초록 직접 확인). ResNet 전이학습으로 GNSS 단순 재밍 특징을 추출하고 SVM 으로 6가지 재밍 유형 중 하나를 식별하는 기법을 모의실험으로 평가했다.^[inbox/processed/hw-20261021-jamming-kci-yoo-resnet-svm-jamming-classification-kics-2023.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 식별 정확도: ResNet-18 96.33% / ResNet-50 97.25% / ResNet-101 97.50% (10-겹 교차검증 SVM)^[inbox/processed/hw-20261021-jamming-kci-yoo-resnet-svm-jamming-classification-kics-2023.md]
- 처리 계층이 깊을수록 정확도 상승^[inbox/processed/hw-20261021-jamming-kci-yoo-resnet-svm-jamming-classification-kics-2023.md]
- 재밍 유형 6종 분류(유형 목록은 초록에 없음)^[inbox/processed/hw-20261021-jamming-kci-yoo-resnet-svm-jamming-classification-kics-2023.md]

## 한계·미확인
모의실험만. 드론 탑재 연산량·실시간성 미확인.^[inbox/processed/hw-20261021-jamming-kci-yoo-resnet-svm-jamming-classification-kics-2023.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[kci-dual-nis-sac-gnss-ins-spoofing]]
