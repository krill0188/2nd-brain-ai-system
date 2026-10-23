---
title: "VisDrone-Dataset (GitHub README)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: simulation-test
ontology_class: FlightLogData
tags: [drone, dataset, visdrone, detection]
sources: [inbox/processed/hw-20261021-data-dataset-visdrone.md]
confidence: medium
contested: false
contradictions: []
---

# VisDrone-Dataset (GitHub README)

- 원문: https://github.com/VisDrone/VisDrone-Dataset^[inbox/processed/hw-20261021-data-dataset-visdrone.md]
- 저자: VisDrone 팀(저자 미확인)^[inbox/processed/hw-20261021-data-dataset-visdrone.md]
- 발행: 미확인^[inbox/processed/hw-20261021-data-dataset-visdrone.md]

## 핵심 내용
VisDrone 벤치마크는 5개 과제를 다룬다: 영상 내 객체 검출(이미지), 비디오 객체 검출, 단일 객체 추적, 다중 객체 추적, 군중 계수. 규모는 288개 비디오 클립(261,908 프레임), 정지 이미지 10,209장, 수동 주석 바운딩 박스 260만 개 이상. 중국 14개 도시에서 여러 드론 기종으로 도시/농촌, 다양한 날씨·조명, 희소~밀집 조건을 촬영했다. 프레임별 박스와 장면 가시성·객체 클래스·가림 속성이 있다. 각 과제는 trainset, valset, testset-dev, testset-challenge로 나뉘며 testset-challenge는 정답 비공개이다.^[inbox/processed/hw-20261021-data-dataset-visdrone.md]
원문 인용: "The benchmark dataset consists of 288 video clips formed by 261,908 frames and 10,209 static images"^[inbox/processed/hw-20261021-data-dataset-visdrone.md]

## 설계·운용에 쓸 수 있는 지침
- 소형 객체 검출 학습/평가의 공개 기준 데이터로 사용 가능. 군중 계수는 별도 DroneCrowd(ECCV2020) 데이터 사용.^[inbox/processed/hw-20261021-data-dataset-visdrone.md]
- 같은 폴더 ai/research의 VisDrone 논문 파일과 보완 관계.^[inbox/processed/hw-20261021-data-dataset-visdrone.md]

## 한계·미확인
- 파일 포맷과 전체 클래스 목록은 README에 없음: 미확인. 라이선스 미확인.^[inbox/processed/hw-20261021-data-dataset-visdrone.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[drone-simulation]]
