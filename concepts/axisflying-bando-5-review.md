---
title: "AXISFLYING Bando 5 알루미늄 프레임 5인치 드론 리뷰"
created: 2026-10-15
updated: 2026-10-15
type: concept
domain: hardware
tags: [drone, drone-hw, fpv, hardware]
sources: [inbox/processed/fetch-2026-10-15-yt-this-durable-drone-is-awful-axisflying-bando-5.md]
confidence: low
contested: false
contradictions: []
---

# AXISFLYING Bando 5 알루미늄 프레임 5인치 드론 리뷰

Joshua Bardwell 영상(2026-10-14) 자막 기준. 자막이 8000자에서 잘려 실제 충돌 내구 테스트 결과와 최종 결론은 없다. 단일 출처이고 리뷰어 의견이 섞여 있어 confidence는 low. 같은 제조사의 이전 리뷰는 [[axisflying-vertex-5-review]] 참조.

## 구조

- 5인치 기체 대부분은 카본 프레임이지만 Bando 5는 중앙부를 밀링 알루미늄으로 만들고 암과 상·하판은 카본이다. 이름대로 벽·구조물 충돌(bando) 용도에서 더 튼튼하다는 발상이다.^[inbox/processed/fetch-2026-10-15-yt-this-durable-drone-is-awful-axisflying-bando-5.md]
- 하단은 TPU로 보이는 플라스틱 칩 범퍼가 있고, 후방에는 아래로 늘어진 커패시터를 보호하는 부품이 있다. XT60은 3D 프린트 벌크헤드 방식이 아니라 일반 방식이어서 충돌 시 뽑혀 나가는 문제가 적다고 평가했다.^[inbox/processed/fetch-2026-10-15-yt-this-durable-drone-is-awful-axisflying-bando-5.md]
- ESC·FC는 AxisFlying 자체 제품이고 수신기는 ExpressLRS이다.^[inbox/processed/fetch-2026-10-15-yt-this-durable-drone-is-awful-axisflying-bando-5.md]

## 리뷰어의 재료 논거 (의견)

- 카본은 휘었다가 복원되는 탄성이 있지만 알루미늄은 한 번 변형되면 되돌아오지 않는다. 변형된 알루미늄 부품은 교체 비용이 카본 판재보다 훨씬 커서, 카본보다 몇 배 오래 버텨야 손익이 맞는다는 주장이다.^[inbox/processed/fetch-2026-10-15-yt-this-durable-drone-is-awful-axisflying-bando-5.md]
- 알루미늄이 충격을 그대로 전달해 카본 암을 더 빨리 부러뜨릴 가능성과, 암이 프레임에 들어가는 지점이 응력 집중부가 될 가능성을 검증 대상으로 제시했다. 결과는 자막에 없다.^[inbox/processed/fetch-2026-10-15-yt-this-durable-drone-is-awful-axisflying-bando-5.md]

## 출하 설정 문제 (리뷰 유닛 기준)

- 아날로그 기체인데 OSD 비디오 포맷이 HD로, UART1이 VTX MSP DisplayPort로 설정되어 있었다. 즉 디지털 VTX용 Betaflight 설정이 들어 있었다. 리뷰어는 리뷰용 샘플이라 그럴 수 있다고 단서를 달았다.^[inbox/processed/fetch-2026-10-15-yt-this-durable-drone-is-awful-axisflying-bando-5.md]
- GPS 관련 설정이 켜져 있었고, 확인해 보니 GPS가 GoPro 마운트 아래에 실제로 달려 있었다(GoPro를 얹으면 수신에 지장이 생길 수 있다는 지적).^[inbox/processed/fetch-2026-10-15-yt-this-durable-drone-is-awful-axisflying-bando-5.md]
- 펌웨어는 Betaflight 2025.12.1을 기반으로 한 커스텀 빌드로 HD·SD 빌드 옵션이 모두 포함되어 있었고 VTX 테이블은 비어 있었다.^[inbox/processed/fetch-2026-10-15-yt-this-durable-drone-is-awful-axisflying-bando-5.md]

관련: [[betaflight]], [[fpv-hardware]].

## 📰 최근 관련 소식
- [Joshua Bardwell] This "durable" drone is awful // Axisflying Bando 5 (youtube.com, 2026-10-14) — https://www.youtube.com/watch?v=Mo15TyjLqgs
