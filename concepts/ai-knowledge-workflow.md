---
title: AI 지식 워크플로
created: 2026-07-21
updated: 2026-08-10
type: concept
tags:
  - automation
  - provenance
  - research
  - workflow
sources: []
confidence: low
domain: ai-autonomy
contested: false
contradictions: []
note: "Raw source not preserved in repo — found during 2026-08-10 provenance audit, needs recapture"
---

# AI 지식 워크플로

AI 지식 워크플로는 원본 수집부터 검토된 지식과 산출물 생성까지를 역할별 계층으로 나누는 운영 방식이다. 개인 지식관리 체계 전체에서 이 흐름이 갖는 의미는 [[ai-personal-knowledge-management]]에 정리한다.

## 기본 흐름

    수집 → 원본 보존 → 탐색·질의 → 위키 컴파일 → 검증 → 산출

- Zotero와 브라우저 클리퍼는 원본과 서지정보를 수집한다.
- NotebookLM은 선택한 소스 묶음을 탐색하고 질문한다.
- LLM Wiki와 Obsidian은 장기 지식과 관계를 Markdown으로 유지한다.
- Understand Anything은 지식 연결과 공백 후보를 그래프로 탐색한다.
- 검토된 지식은 글, 보고서, 프레젠테이션 같은 산출물로 변환한다.

한 도구가 모든 책임을 갖지 않도록 원본 보존, 지식 합성, 구조 분석, 결과 표현을 분리하면 도구를 교체해도 축적된 Markdown과 출처 관계를 유지할 수 있다. ^[raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md]

## 검증 관문

1. 원본과 요약이 분리되어 있는가?
2. 모든 핵심 주장에 추적 가능한 출처가 있는가?
3. 기존 문서와 중복되거나 충돌하지 않는가?
4. 내부 링크가 실제 문서를 가리키는가?
5. 산출물이 목적에 맞는 형식으로 직접 열리고 사용되는가?

## 위험과 제어

- 여러 에이전트가 같은 문서를 서로 다르게 해석할 수 있다.
- 프로젝트 README나 소개 영상의 홍보성 주장이 검증 없이 굳어질 수 있다.
- 자동화가 늘수록 잘못된 메타데이터가 빠르게 전파될 수 있다.

따라서 생성 속도는 출처, 링크, 스키마와 일관성 검사를 자동화할 때 비로소 장기 지식 품질로 이어진다.

구체적인 단계 배치는 [[knowledge-tool-roles]], 반복 운영 모델은 [[research-feedback-loop]], 연구 환경 구현은 [[second-brain-research-workflow]]를 참고한다. ^[raw/notebooklm/2026-07-16-all-notes.md]

## 📰 최근 관련 소식
- [Y르포] 60m 상공서 객체·사물 완벽 인식…안전·치안 구멍 메꾸는 AI드론 (v.daum.net, Mon, 03 Au) — https://news.google.com/rss/articles/CBMiRkFVX3lxTE53NnRpaXN4OVZWTUNYUEJpZ3ljM0lHaFR2SlcxSTExNWhiZWRxaXA3Q0xFcXh4am5wQS1mOEl4YmhQWEdYTUE?oc=5
- 광교호수공원서 드론으로 간식 받는다…수원시, 배송서비스 시작 (v.daum.net, Wed, 05 Au) — https://news.google.com/rss/articles/CBMiVEFVX3lxTE9YSk1CeXY4R25wMGpBYUVHdjRTVk91b1lvZTQxV3NmdnpVS3BSV2N2UFJtY2J1Z1VHLTNoYTNQaUlGTDZWSXFiaU02VW9LZ1loOFhYLQ?oc=5
- [리포트] 니어스랩, 코스닥 출사표···피지컬 AI 드론으로 방산시장 정조준 (팍스경제TV, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiZ0FVX3lxTFAwMVgxZU1Jd3JVdkdUM09BYk9EM3UxZ2dqZVR1Y01rTVQxR1d4SmZ3dXYxaXBCVzl5enV5T3c3dXB3dU1lVy0zcTNNSmNSNHoxZ3ctdHRkZzU0Wlp4RzZYUm1HOXR6SjQ?oc=5
- 중국 'AI 군사화' 박차...타이완 '드론군 양성' 맞불 (YTN 사이언스, Thu, 06 Au) — https://news.google.com/rss/articles/CBMijAFBVV95cUxNVnpfR2JOam1zbWthUENVaTVvQkdJdGNGUHF5SThhZmxJOWhteXJ1QjZzdk50akhhT3R4c0pYemtfV25PeXgyMG5SNUZmVlVRY0IzYnFNMjVGZk9XeDMyc3hTN0pUUDBrems4X1VoS2pkWXEtZ1Q0bHlEcmRlLWpVQ1BoX3dNVnFxY2hXbw?oc=5
- [IPO챗] 니어스랩 "풍력서 검증한 AI 자율비행으로 글로벌 방산 공략" (연합뉴스, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiYEFVX3lxTE1RSnhlY0xnMnR1aWRISlNkNWc1ZWgyWkN3ZEtQQU1UZnN6eUhHdEU4a2xtSkJ2ZHlvdDBhbUlRWHhjSFIwREp6aUkyWDBmT3lKcnBTSG1ybGMtTHlZWkE3Y9IBYEFVX3lxTE1RSnhlY0xnMnR1aWRISlNkNWc1ZWgyWkN3ZEtQQU1UZnN6eUhHdEU4a2xtSkJ2ZHlvdDBhbUlRWHhjSFIwREp6aUkyWDBmT3lKcnBTSG1ybGMtTHlZWkE3Yw?oc=5
- 공항에 폭발물 탑재 드론까지…독일 정부 "새로운 차원 위협"(종합) (v.daum.net, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE14eksyOUl2RnQzUnpsdnA1aG9LQXhQa05BUEg4UWVXN2J3RkFUOUxaa1g0S1lVb2hjR3lmQnFHb2cxOGhqc1pCWXFUd3NtZms?oc=5
- 드론사업 팀 프로젝트 매니저 — 둠둠 (www.wanted.co.kr, 2026-08-07) — https://www.wanted.co.kr/wd/379169
- 니어스랩, 코스닥 출사표..."국내 1호 피지컬 AI 드론으로 방산 시장 공략" (AI타임스, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTE1yNlI4NnpyejdfanZEd0Nfa0tJb3J0TGZnWlZ3dGFNUEN4VFhZdi0zdm82Rm5pZkNuemdZS0g3aVgxRTM5ckJ1a25fODFpLVZFOXNBV3o5UFczTFhJaE0tV3dzWnBHN1BoOWc?oc=5
- ‘피지컬 AI 드론’ 앞세워 상장 도전…니어스랩, “글로벌 방산 기업 도약” (서울경제, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiVkFVX3lxTE0za0dOeHlpZ3drSm9DU2d6RnllVm8ycXFmWmRCOG5LWDlGTFA0bWVUeXVqMkVsS2JWZVFvNXB1US1rOV9Jd1RNb0V6aUlYenNOa1BJZTRR?oc=5
- 열화상 드론으로 보니‥1/3이 밭일하다 숨져 (v.daum.net, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE96azdkckhNeDIxd1BtR0M2RU5SUlJiOVkwZ0tWbVI0SjJqd0Jra0Y4S2JLd1BRb01SUndHNXZqTk1BQ2JLMzN4SGEwM05rWWc?oc=5
- 전북경찰, 드론으로 농경지 등서 온열질환 사고 예방 순찰 (연합뉴스, Fri, 07 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE56akNTNFFXOXR2V01PZzBaV3JqdGRIV0R6ZU4zRjBtWC13cGJsTG1aREg1cVRzakdMenQ1MElPWVR4QmZqUU13VUduUGd5YWRVWVRtWXdDT0R4MzTSAWBBVV95cUxPT3h1MlQwMFAxY0xha1dYdDVtZmZyVy1XNDRCWVVMYXA4N3pyMHRsUXI4N3JrenlBSUVfYy1nS0JYLUliN0E4THh6bVd2M3JjcTZtOTNNMHdtbmtHaXRXZlQ?oc=5
- “북한군 드론전 경험, 결정적 위협 아냐”…강건작 안보실 1차장의 ‘결이 다른 생각’ 보니[반도 앨리스] (경향신문, Fri, 07 Au) — https://news.google.com/rss/articles/CBMiWkFVX3lxTE50LTk3NTJxWXBWWmxhOXBmN2hJS3lfQ0haekRtNEtsTnFvekE5RUxBV3M2UW8xZnRTemgzWlo2aUJMWmlXWWlEa2t1Q3RGcDlsS1lBdmIxU0x0QdIBX0FVX3lxTE9qdG41WmdVclVUV3doYUxtLVh2OW80VXdNamstX0VtbHVmNVFrUXVpVmkxczBLa1ZDSXEwYWg5VUR1ak42enNQUDc3SW5LOXdjSFJpbGFrQnF4Z2hTNHNZ?oc=5
- ‘광교호수공원서 드론으로 배달시키세요’ (서울경제, Wed, 05 Au) — https://news.google.com/rss/articles/CBMiUkFVX3lxTE5MQzhtV0NtY1g5TGk4OHpOaTRtUGRDY09oQXd6bFRrVTE1RWNzNldKbF9LQkZFdG8yU2RLUmxwZjRSU3BYNDMwV2otbXJubm5YYlHSAVNBVV95cUxPdFBRSk14NXR0V3NjX2JnV2ZCeWxzelJqcjBfRGFQTEZfOE9zRlpDb2ZaLVlwblRMTmtJN2tLYW5TSWRjQmgyUWRsOUlwTUxIMDFzNA?oc=5
- AI 자율주행 드론으로 글로벌 방산시장 공략 (매일경제, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiTkFVX3lxTE9haTRmam0zaWRyT2hnQ3FEeTZMSmx0QlRSaVhwTlBhLVNzcHA0Rzl0X3R0THAxc1VWWnVOMTM3ai0zakNIUy0yMThNeFlxQQ?oc=5
- 니어스랩, AI 자율비행 드론으로 방산부문서 수익성 확보와 성장 가속 (파이낸스스코프, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTE96dDZIZml1WTZXalFOUnF1cDRRblJrVEtTTGRJczVQcVFzRGc1aEtoY05KOWVWRHFDX1BUazFQTmVtV0t3R0kyWElyWGFPbUxTX2R1Qkh2UW84b283ajVhR2p4MkdmcGEwS0E?oc=5
- 풍력발전 점검에서 방산으로…니어스랩, 코스닥 상장 도전 (ekn.kr, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiY0FVX3lxTE1uRi1IQnA1NHQ5WWtfZUVtc1h6STJUYVg3c0VQR1JLMW5lNkt6ODM2MEZzT2t0Qlg3amQtUFM4UTMyYXZ4dlBMNkEwMjBoU1JFT2VVN01qTnh3VTdVbi1XcE90aw?oc=5
- 니어스랩, 풍력 AI 자율비행 기술로 방산 공략 (더스탁(The Stock), Thu, 06 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTFAzVlVjWHVUckxuZFZCeG5tWGI5aDk0SGdvTG9QWmRldDdpMktGbW1veW0tZDNnQURqdlNuRUJlT0JxWjNMdVFmb1JQcDNMcEw4dmNhMFdYLTJpTF9aamdJV1M0dmpsTkZSQ1E?oc=5
- 후티 반군 "사우디에 미사일·드론 공격"…모카항·아람코 시설 타격(종합) (v.daum.net, Sun, 09 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE1Kc1MyclU0ZUpjMW4wRjhVWFdQUkN1MmpJNlU4Y3FJYkJpaGtRZUNZM2ltaDY2cHdZTzA3RUNDcmFVZi1HUW9Mb3ZEYk9zV2s?oc=5
- [영상]공중에서 몸통으로 쾅…모기 잡는 ‘육탄 격추 드론’ 떴다 (khan.co.kr, Sun, 09 Au) — https://news.google.com/rss/articles/CBMiWkFVX3lxTE9DdWo2ZmFLMUVmYmJFNlNfaTFuS0RfSTFRRG1rSEtYaHp4TzV1WTJyS2dtVWh2N0NLQ1k1cngteEpFbHk5cHFGLTNtNy1JRktwTndhRmJKWERad9IBX0FVX3lxTE4yUXRiRDFGY195RWN2bjkwNUpfMlhHcG1qZHh0SUpvaFJxTEVNYXlYODZhV19UcFVEdWhBanZBUEFySmFCamYycWtUeDV4VkNiZ0xLVXBaS3J6aFlNNlRN?oc=5
- 니어스랩, AI 자율비행 앞세워 방산시장 공략…코스닥 상장 도전 (바이라인네트워크, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CaFFPM1BBajhqVzFUcW5JZTJ1emYwcDJiWGE2QXA5d050ckxhSVlWeGdyQ1pNQlZzUm0xN3o2aURkYzBGTTZCYVlvbzFTSGNiMGdIYWlR?oc=5
- [비디오머그] 공항에 폭발물 탑재 드론이…"새로운 위협" (v.daum.net, Mon, 10 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE5rT29XYmZpSXlDczdKa0ZQMnNfTFpRMFhYWmRGWDFuOUZCZlY1TzRyRzlhY19PU0pkRFVNTGdrMUVJUzRKSXRUUVdsclhPUm8?oc=5
- [IPO 현장터치] 니어스랩 “피지컬 AI 드론으로 글로벌 방산시장 공략” (뉴스투데이, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiXkFVX3lxTE9EelE3MmgtRnR2MEVBMXFua3hxNmZxT2pKLWE2QzM1TUk3Vms2am9aOUtKR3hqOXRKM2ZVc0VVaGVzUnM3eXYyVmRkSnRucVRYRFB1WDlsdll5MkxwVVE?oc=5
- 호원대, 드론·AI 융합콘텐츠 제작 교육 운영 실시...남원 시민 참여 - 머니투데이 (머니투데이, Mon, 10 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTFBSOEt3S0Y2LUFZRW1iSVYtNFpDRWtvRERTcmtpSlRaZGtvVWhSVWJETHRldk10SUpkQWllQlNYYk9zNWZRLUYyLXRvaDVxZzdROUVrMXg4eWJteDFHTVJsWGtqTnpEMlpiY3fSAW9BVV95cUxNRU5WZDVmeEw4YTNyc013TkhPaWFGSkNCNTY1SFowSjlXRGZVVmpmaURvM2FVcXV6Mlp1WXBaZHVUWFNjS3FKRXVNQXJmZDd6OTdIMmhSSFF6V3B2X21qN1M0SEE2cG5NVDhaVlVGYjg?oc=5
- '피지컬 AI 기반 자율비행 드론' 니어스랩, 일반 공모 돌입[오늘청약] (edaily.co.kr, Tue, 11 Au) — https://news.google.com/rss/articles/CBMigAFBVV95cUxPMnFfYkhlNHNYYkdEOWNUTjUzcWNJcG04ZXN1R09JbVloVHF5dHpmdUlja0ExdkVyRENnSVZjU1RSckdUSWJrSjVrSG83SDBfTFRXUWRKQV9va2ozVUtSbThrdlo0QWdkSUpTQkdzM3BGai1RNDItNjlHYy16ZFpJeA?oc=5
- 안양시, AI 과학축제 연다…"드론·로봇부터 자율주행까지" - 머니투데이 (머니투데이, Wed, 12 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTFBkbjVabm5xVUpOaGNFR01taTVPY0tyWWRnTDVEWlB1OHJHeW9GazBHQTlMa0VCX1FsY0pQZjM1a1ZoeVhPV05vYUQwZ2poNDFLN240NHhXVWZKM18ySmZDalVqTWlyTkFMdUHSAW9BVV95cUxNa2gwTnkwR3NRWUU2ZFFOdUlScW1mLXU3djhENnR0VnUwN1k2c0w3dEJXV2RkakNYX1E3OWdiV2h5RDM4Ymhaa0tOa0lhTFhnNlVRWGJjUEo1eFlvY0ZERGZXRjQ1a0t6TDZWLWt2NFk?oc=5
- [영상] 머리 위로 이스라엘군 드론…청년들 "누굴 찍나" 극도 경계 (연합뉴스, Tue, 11 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE1TQndkYTdLZ3p1Tkl5WmhGODR2NFNtRnhzVWhYVWlHUlJaM1lMQ3dwYWd3Z2p1QkVjZjF6dnQybklnajVjQ0VFaXJlUnUzZ1lwcVB6R0pPTVpyaE3SAWBBVV95cUxOMUZjNDNvSE1fenhoVm9MVS1kUThnVm0zY3dIeUl4OXNBZ1RZeW40N2Y3YVBETVd4Zkp0X0pWVnU2bEYxOFhnY2h3OW9HclFBZ3F2V2pmb3NmWG1DcTFfQVo?oc=5
- 니어스랩 공모가 상단 41,200원 확정, 얼어붙은 공모주 시장 뚫었다 (플래텀(Platum), Tue, 11 Au) — https://news.google.com/rss/articles/CBMiSEFVX3lxTFBKSGF1dGE4aTRrelJPUGF0SE9fLVNlWlozQndoZGFDSFR4SHpnX1NQaG1vOGx6NlFkZzF3LVNkRWxDVHJORF83LQ?oc=5
- 치킨값 나오나?…'니어스랩' 청약, 오늘부터 (위키트리, Wed, 12 Au) — https://news.google.com/rss/articles/CBMiVkFVX3lxTFBsOWF3OXhGMUxZMkV1Ri1yOGlNdi1sSm5BUHk1UVpRY1FuNU1lLWFyZ3JjQVJnLXVlREdadkRrR205dC1iMkZGZG1VR0FUVWVUcTh5Tll3?oc=5
- 폭염철 더 바쁜 드론…논밭 온열질환 살피고 곳곳 피해예방 방송 (매일경제 마켓, Fri, 14 Au) — https://news.google.com/rss/articles/CBMiUkFVX3lxTE5laEhNZ3ZvYW81MWVLMEN3cHVkVmhwM3ZNWWVZT1JqeWkxWlVwbzZSUFA1d3dyLUpxZGJNd1g2X2lpVjY3eUM4dVY4Qm5tdS1xWVE?oc=5
- "AI·드론부터 핵심 부품까지"… 부산은행, 1125억 펀드로 동남권 방산 벤처 실탄 장전 (청년투데이, Thu, 13 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTFBqY0t2dWx1NXNBRERzdVNRaU0zMVJySFFnRXpMTlg5Y1puTVBPWl9faTk3NHVkZXh0T1pja3ZZRVhoX0MyQlljQzhoMzVkNDQzRkFBQnN3eS16SmhSWkhlckFDSVdYVDNwcUE?oc=5
- 0.3초 만에 레이저 '번쩍', 드론까지 출격…첨단무기 타깃은 '모기'[월드콘] - 머니투데이 (머니투데이, Fri, 14 Au) — https://news.google.com/rss/articles/CBMiaEFVX3lxTFBZMGNIUWpaOXBHdmFBcWttQ0FsWlJiQXo1cFBPZ1E0Zk5oUTZubGNkWmM3c3V0RzUza3lSQUtCWWFtcDRzZ3hWdjFqQU9KQUZFc1JaZG1QUjJvZmI5QnVuRTZqLVZZY01i0gFuQVVfeXFMUHpDamd6bUI5eVZ3NVlRQ0lnRFVXbVktdWI5ejJJMVBlbjd0ODBENEpyTzFVZ0lIeUc2UTlVUUtjWkJJRVQ2N1JFdHdTODcxcFFIbmVkUTVBVTRRbkswUGtuOENORVdZNlo1dThpU1E?oc=5
- 미, 중동 다국적 공격드론TF 띄운다…‘무기재고 부족’ 우려 덜까 (v.daum.net, Fri, 14 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE1BYmMwQVJyTTVXcG93NktFbXhsVHdlSXM2anlXUEVxYzhlSUMtVFJlRmZPZ01scTZWSmVCSDhqQzdwaEpUM1ROc0ttM1pXd3M?oc=5
- 軍 ‘K방산 주역’ K2전차 성능개량한다…드론·대전차로켓 대응강화 (v.daum.net, Tue, 11 Au) — https://news.google.com/rss/articles/CBMiRkFVX3lxTFA4bC1IUF9QcnZXWDRHVUJ3NDFZWUVHWDd1SUpXRUFxZkZzN3JxMEV5Y1BlalhfQmFIQXM0NEp4RXNOOGwzWEE?oc=5
- 美, 중동 다국적 공격드론TF 띄운다…'무기재고 부족' 우려 덜까 (연합뉴스, Fri, 14 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE1RS0x1cDdIT3NBTU9KTi1TeHpLN1dxOU1tTXpTQi16Y0ZZOW9IS0FxT1VOOFl2OF82Q050X2VWOHNMSGdyQ1Y0ZTRHeFluMGg5T1dHLU11MTRnSGfSAWBBVV95cUxQUW41cFlVT3FhX2pqdTZWVTBEYWtLS2szOU5ocld1STdoWncyVG44QW5wSEdwOXNUUm9OT3JnLUs3Zk8wVVVQU2h6M2ZhMDMyTjJIbjlKOHJiSGstb0xTY1A?oc=5
- 폭염에 탈진 ‘폐지 노인’, 순찰 드론이 찾아 구조 (동아일보, Sun, 16 Au) — https://news.google.com/rss/articles/CBMidkFVX3lxTFBaaThtSS1lQ01Kd1VPdmFnd0dPWDF1b3hJdmxIWTBLM2c3Vjl1WmFmVDhpTWRvb1ItbFFMSzZnNXJueG8ybE00N2paYVN3ekdaeUoySFNXVnh1cGZwMnRVcjZVMW1ONE01MWhjVGpaOWcxTmNwZkHSAWZBVV95cUxQT3kwR0lmMV9FSC15WnBYXzR2bUJ4WlNKVlRKUVdzbG1vVFllM3NCR0UzcFZlbmlDRDNLV2psWVFmNlpYRFlOS2ZXVGNaRGVmTFM0UHhpN29Lc1ZsbDA1VXpzWFljRVE?oc=5
- "예멘 후티 반군, 드론으로 사우디 아람코 정유시설 공격" (연합인포맥스, Thu, 13 Au) — https://news.google.com/rss/articles/CBMicEFVX3lxTE5vTDlHSi16T2NRc3B5VG5YQWhMejQtUUdxUjZzNzlnZDNKcExEYnRnTHBFZ1MxcldUTVA4OG53WlZLUkltMmdhYWJCeVo4UU8zamlFRHNqdHh0Y25kZXU0Rjd3S3UxWXI1ZFFWQzEyTlY?oc=5
- 드론산업 얼라이언스, 프로젝트 유닛(PU) 사업 공모 (드론저널, Thu, 18 Ju) — https://news.google.com/rss/articles/CBMibEFVX3lxTE9fSTlnd2xkSWJzZDJRMXh2R2pzbk5OQkdjYW1Ea2VjOE14eWNuWF92ZzVXSHNLZ1NvVUprcjdtS0R5RUVFU3Fid1Y3Z1QzM2VPTFk0SVduNGU1cXJDZjVOcEVMRnFWQnVjWWtrTQ?oc=5
- 방산수출 효자 K-2전차 성능 개량… 대드론기능 등 미래전장형 무기로 (v.daum.net, Tue, 11 Au) — https://news.google.com/rss/articles/CBMiS0FVX3lxTE93aGxUeUdrZlR4aWowOGM1endYWmR3VVJsMjVCU09GY3Y0cndVdHhMWlZkRkE3OXdJM1pVTzlHS0xNb2lSNjZCY3IwOA?oc=5
- 안양시, 을지연습 연계 ‘드론 복합위협’ 대비 실제훈련 실시 (경기일보, Wed, 19 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BaDdjb2tSOVlaeGpvY2lyVWsxVWVWcmtwNUo1WlRsU0NWMm83OHpDTG9saXo1UzlwcDJFMFVIV0tIazB2b2JzY3Q4WmRibkdZRXAyZEpmV1NGaUU?oc=5
- 젤렌스키, 새 국방장관 지명…'드론전 영웅' 해임 논란 일단락 (연합뉴스, Tue, 18 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE85SENhbm5kdTVvVktkdUhYbHIxRWd1aUZ3V09WU01Jb0lUR2JzSS13VVJyZldqZ050R0R3TjZxRHRsVjYyQlhxTGFGOFZnMlVDM0JmcjR4bnpHc0HSAWBBVV95cUxNOGtnMzVzWHVHM3Z1b21MNlFsNG1NcExCRnYzSzRMdUdrR3k2c0JsR2xpQ3VUd1BqVE9GdG9XdDNHMlFZV2ZsNGU0Ml9vSUNWTU9VNmVEd2tsUHJzYUFIel8?oc=5
- 전차·장갑차·공중통신까지…K방산, 드론·AI 동맹 확대 (newstomato.com, Wed, 19 Au) — https://news.google.com/rss/articles/CBMiYEFVX3lxTE1acWRjVTNLQ1Q2MTJPdFlmc081eTlMWFJqc3h2UkpZVm81VUxDbFdxcXNnbWJqMTdKLXlrTHVLUkxrU1lFN0U0b3VkWU9YUGNJTlZHYlYtV0UzNExXT0x5TA?oc=5
- 美, 中 드론·배터리 밀어낸다…LG엔솔, 왜 방산 진출 얘기 나오나 (임팩트온, Wed, 19 Au) — https://news.google.com/rss/articles/CBMiaEFVX3lxTFBEVkxZUEtJZ0NBRWgwN2RUaXIzcGRueUViRFZ5R0JDMTNZZkhqdHZvTlhUaWx3MG9jVDJOeUNWTUpMUVJzZ1A5ZHJXZ1ZteHRWdzEwN1RiamtqX0hDcEoxLVNNZlFKZzZU0gFsQVVfeXFMTTh6X3pULTFlN2w2WE5IbmcySG5LdWc1cFhqUC0wMmpnb2lRLWxyZUdJbVBxUHZfbWRIY1poaGFqZWM3WHoxTFB5bWV0UG84N2p2dFZTUnVUOVpFbzFuNnRjSlV5NzV5ZE5hYzZV?oc=5
