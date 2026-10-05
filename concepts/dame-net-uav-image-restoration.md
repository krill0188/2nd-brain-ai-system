---
title: "DAME-Net: Compositional UAV Image Restoration"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, ai-autonomy, image-restoration, computer-vision]
sources: [inbox/fetch-2026-08-19-arxiv-compositional-degradation-uav-image-restoration-conditional-.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# DAME-Net: 구성적 UAV 이미지 복원

## 개요

Degradation-Aware Mixture-of-Experts Network. 비, 안개, 노이즈 등 복합적 열화 요인이 있는 UAV 이미지 복원을 위한 네트워크.

## 핵심 모듈

### FDPM (Factor-wise Degradation Perception Module)
- 명시적 요인별 열화 신호 제공
- 다중 레이블 예측을 통한 해석 가능한 열화 설명

### CDMM (Conditioned Decoupled MoE Module)
- 단계별 조건 적용
- 공간-주파수 하이브리드 처리
- 마스크 제약 분리 전문가 라우팅

## MDUR 벤치마크

- **Multi-Degradation UAV Restoration benchmark**
- 43가지 열화 구성 (단일~4요인 복합)
- 표준화된 seen/unseen 분할

## 성능

- 기존 통합 복원 방법 대비 일관된 개선
- unseen 및 고차 복합 열화에서 더 큰 이득
- UAV 객체 탐지 다운스트림 작업에서 유효성 검증

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전
- [[yolo]] — 실시간 객체 검출
- [[edge-constrained-uav-small-object-detection]] — 에지 제약 UAV 소형 객체 탐지

## 참고

Jinquan Yan et al., arXiv:2604.09313 (2026)

## 📰 최근 관련 소식
- "러 파병 북한군 현재 8천500명…정찰·공격용 드론부대 포함" (v.daum.net, Sat, 22 Au) — https://news.google.com/rss/articles/CBMiRkFVX3lxTE82bXkwUDZ0WnNmSE4zbVNZRzV6cTVzbTcyYmhtX0U3N0dYQld6MUx2a3JjMDg3eU1fZ09kc1dHQXhTM1dIQ0E?oc=5
- 러, '시속 600㎞' 제트 엔진 드론 공세 확대…우크라 요격 고전 (v.daum.net, Mon, 31 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE54cEpvaUF1b2hGUkdlSzlmVF9YYUNYUTdFcVpwVDFnT24tOUdwVE01R3YwTnpPUXVIZVBkNXA3dVNTTjl3NVAtTGp5WU0tT0k?oc=5
- 폴란드 드론공장 방화…'또 러시아 공작' 의심 (v.daum.net, Mon, 31 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE9OTkdQR2UzdVZ4cGdwVWsyb0pDUUdRaUFmUTViY0FfRURPVDFkcktyYW5pQTJpX0hRMEhTWWtwZXo4UUVoRC1mQ2NabzA3clU?oc=5
- "차세대 對드론 방산 선도"…인천시, 방산혁신 지역협의회 출범 (v.daum.net, Wed, 02 Se) — https://news.google.com/rss/articles/CBMiVEFVX3lxTE1oWWxGSEZFVHpBcXJoVWlfczNyYXBzaUxQTUdEY0FNYkMyVFE0Y1BrSG95Zk9ZNHJINW5RUmhJT1hXUEd0Y0tKZmVUSS01YmNhUFdzdA?oc=5
- 인천, 방산혁신 클러스터 조성… ‘ 對드론 기술 개발’에 초점 (v.daum.net, Wed, 02 Se) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE9FdVEzY3R3c1U4eHFxeUlhQUpoRE9WRDNHcFJ2Mm5tVXAwemwzTTktZHR4bmlmaGRvdGkweTRoMjR0VlAwVTBwVmVMZFQ4Z2s?oc=5
- 참사 열흘 뒤 공개…中경찰 드론에 담긴 네팔 대홍수 (v.daum.net, Mon, 07 Se) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE1RSGlEaHNJLS1FVlZlWjctUDlCbGJhdUw4ZVRsY1FqMU1sYTNmTzNQZUlCNzNGMWhmOG5WWUh3eUlWajl0VUdyWUpNVUpWV2c?oc=5
- 철원 고석정꽃밭 드론으로 촬영한 인생사진 인기 (v.daum.net, Wed, 09 Se) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE0xbUp1MDZaQ1FDeEVmUlBsSEtZSVJkZHNZd0RlRFVxNlJPSHlCalo0QVpxMUstRVVXdGl5ZHdTNUtiam02U0kwSm0zcVhLdk0?oc=5
- 노르웨이 "젤렌스키 비행기, 러 드론에 피격될 뻔"…우 "과장"(종합) (v.daum.net, Thu, 10 Se) — https://news.google.com/rss/articles/CBMiRkFVX3lxTE45eXZ0cVY1TFZ5NzRHdzlaY2F2OXI1ejFkZFJIdk51V2hBLUR4em9tVGRxVzA5dXNiV3k3TVNmam80Qk5SSmc?oc=5
- “드론전쟁 시대…중국의 물량공세 맞설건 오직 한국 공급망뿐” [제27회 세계지식포럼] (v.daum.net, Fri, 11 Se) — https://news.google.com/rss/articles/CBMiRkFVX3lxTFBNUWpJRDR3UWlPNjAxemtLUlJUNmhWQjEwTHpDTWcyallGSDhRbkNUcW5sQW14clVpM1FsNjVHYmozVENCMWc?oc=5
- "러 정보요원, 독일 입국해 공항 폭탄드론 공작" (v.daum.net, Sat, 12 Se) — https://news.google.com/rss/articles/CBMiRkFVX3lxTE9XVGh0N3ZUTUxpMzlla2hsRTc1SW9DTFNuSlBfTE1OVWhGZlVlVmh6MnBVSWlCQW0wWnNDQXluOE1WcTlNZEE?oc=5
- 내달 23∼24일 서울 하늘서 드론 레이싱…10개국 60여명 출격 (v.daum.net, Mon, 14 Se) — https://news.google.com/rss/articles/CBMiT0FVX3lxTFBSc3FhbThwdkRBY1p6WVFYUlNYUTlIM00zcnM4MVN4TFh1bGVMeHJpYnRUQUoxeHhvTDFNTFdxcS1pTkJQeHd3cWlxaFJ6aHM?oc=5
- [설왕설래] 드론 탈옥 (v.daum.net, Tue, 15 Se) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE9TUmpfUEhEbDhINkZ5ZmxvLVlHQ1IwNlJ4Q3B1OFJtRE1RQVZlTXlSS24tWWhnb0pQOFhnN08zX2ZiaEswcnlyNE1IeDVuVjQ?oc=5
- “이란 드론 몇 대에 뚫려? 美 속절없이 펀치 맞았다” (v.daum.net, Wed, 16 Se) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE0yUGlheFA5YnRRbWZsSV9ZY2Fid05BaTdYQUt3RzZZVU5qa1lTX042eml5WFVMbUxVVkw0QjFmYzZEZElHYzM3bWU1enI0SEU?oc=5
- "드론 공습에 아내 잃고 맨몸으로"…후티 진격에 10만명 피란길 (v.daum.net, Tue, 15 Se) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE5mYlBQTUhQcHdtN1lMZXNNZlVBbXBLTHBHcFh5WGlyeGFxU3BYa2NNVW8tM3U4N2Y1eHVsV194YVYzQXUtOW1SeGpXMGYtR00?oc=5
- 이륙하자마자 ‘우수수’ 추락…K-드론, UAE·사우디 앞 망신 (v.daum.net, Fri, 18 Se) — https://news.google.com/rss/articles/CBMiT0FVX3lxTFBzWVFvYlpPMU14dUxEZVpoZXJNdXk1anZnN3JjZ0ZiMEdOMHRrWDZOVWdDcUY2eHRfN2Q4NHBVX1lSSlJEalFLVjk5RmtJRGM?oc=5
- 60m 폭·10m 물속까지 샅샅이…한강 실종자 찾는 수상드론 (v.daum.net, Tue, 29 Se) — https://news.google.com/rss/articles/CBMiT0FVX3lxTFBjeG83WkNNemdINkVXUUxjbXRZdk9GWDNPeEpRZlktWEh3MWQ5YUhWWkcwRFh0UUp1SmRBNy12LXFueldBbkFLdl9fRU9naEk?oc=5
- 네팔 산골에 뜬 800㎏짜리 드론이 향한 곳 (v.daum.net, Wed, 30 Se) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE8tOXBhM0hjQUxfTWFsdmdCMVVmVllsSjJyb0J2RUMxMFVvM1RPRFlrVG5uRzNxM2RTUzZzZkNMaVpRTWtpV05uQXZLS1VoUFE?oc=5
- 李대통령 참석 국군의날 시연행사서 드론 또 추락…"기상 영향" (연합뉴스, Thu, 01 Oc) — https://news.google.com/rss/articles/CBMiW0FVX3lxTFB5VHlTNm1CZVdaSDJWT2pvb2J4T1RrbUV3NmNTcFBVN1NWdVl2NUlad2ZMZHQ4SG96WWJjOTJBY0QxTzloLUp0dERHMGlnZnNUZnIxS2REeUl1V3fSAWBBVV95cUxNQTcxcm45aF9qMzgzVzBWWVRhY285aVFRRE1CWWpEX1ZVQTFIZ2ZocU5fZVdtQ0NCbXJ5MS04VjhYaEs2UmlXWDRkNDJOSDVlRVVxdk4waHJwMlhjS0txbHQ?oc=5
- 李대통령 참석 국군의날 행사서 드론 추락…생중계돼 “공중 기상 영향” (문화일보, Thu, 01 Oc) — https://news.google.com/rss/articles/CBMiUEFVX3lxTE5zeUxSQ2lIcDRKZTR4NkF5LUdsRnZSZXZCMUxPN1F6bERGRjB0MVFHS2hXWFgzWmNrdFJhVmZ3UXYyY2tYdzl3b3g0NDFxeVRq?oc=5
- [단독] 111억원 들인 산림청 드론…산불 최초 발견은 ‘0건’ (v.daum.net, Sat, 03 Oc) — https://news.google.com/rss/articles/CBMiRkFVX3lxTE1PSmN5azMwa3NaUTZteS03VEozRzFESmxuaURUaGRzNHpVMnlJMVQtREl1MWg4dFBQSUNqNWM1SEJkeVFzcnc?oc=5
- 젤렌스키 "러, 북한에 제트추진 드론 기술도 공유한 듯" (v.daum.net, Sun, 04 Oc) — https://news.google.com/rss/articles/CBMiT0FVX3lxTFBSb2E3Z3FxNmlsY3hhbFo0SWZvMm1LRDUzT2RMUzhIWEEyM09tNlJ4ckRTSnQwZ0xtTkNfdWdQV2RvTTd0WXZpa3FPWFowSGM?oc=5
