---
title: AI 개인 지식관리
created: 2026-07-21
updated: 2026-08-10
type: concept
tags:
  - knowledge-base
  - knowledge-graph
  - pkm
  - provenance
  - workflow
sources: []
confidence: low
domain: ai-autonomy
contested: false
contradictions: []
note: "Raw source not preserved in repo — found during 2026-08-10 provenance audit, needs recapture"
---

# AI 개인 지식관리

AI 개인 지식관리는 자료를 많이 저장하는 일이 아니라, 원본과 해석의 경계를 보존하면서 검증된 지식을 반복해서 재사용할 수 있게 만드는 운영 체계다.

핵심 단위는 특정 앱이 아니라 추적 가능한 원본, 상호 연결된 Markdown, 명시적인 품질 규칙이다. ^[raw/youtube/📺 How To Build LLM Wiki In Obsidian 🧠 A Memory Layer For Any Agentic AI.md]

## 지식의 세 층

| 층 | 목적 | 보존 원칙 |
| --- | --- | --- |
| 원본 | 논문·웹·영상과 메타데이터 보존 | 수정하지 않고 출처와 수집 시점을 남긴다. |
| 컴파일된 지식 | 개념·비교·질의를 재사용 가능하게 정리 | 출처, 링크, 갱신일과 신뢰도를 유지한다. |
| 집중 탐색 | 제한된 소스 묶음에 질문하고 가설 생성 | 생성 답변을 확정 지식과 구분한다. |

원본 도서관, 컴파일된 위키, 소스 기반 질의 공간을 분리하면 대용량 원본을 Markdown 저장소에 모두 복제하지 않으면서도 근거로 돌아갈 수 있다.

한 도구의 대화 기록이나 독점 형식이 사라져도 핵심 지식과 출처 관계가 남는다는 점도 중요하다. ^[raw/youtube/📺 LLM Wiki를 업그레이드하는 외부 지식 시스템! 연구자를 위한 최강의 조합 Zotero × Notebook × Obsidian x Claude Code.md]

## 운영 순환

1. 원본과 메타데이터를 먼저 보존한다.
2. 반복해서 쓸 가치가 있는 내용만 개념·비교·질의 문서로 컴파일한다.
3. 새 문서를 기존 지식과 연결하고 중복·모순·출처 누락을 검사한다.
4. 지식그래프로 군집, 브리지, 고립 문서와 약한 연결을 탐색한다.
5. 그래프가 제안한 관계를 원본 또는 제한된 소스 묶음으로 검증한다.
6. 검증된 결과만 위키에 환류한다.

이 순환은 [[ai-knowledge-workflow]]의 단계적 흐름과 [[research-feedback-loop]]의 반복 구조를 결합한다. 지식그래프는 문서 관계를 탐색하는 관측 도구이며, 그래프에 나타난 연결 자체가 사실의 증거는 아니다. ^[raw/notebooklm/understand-anything-github.md]

## 편입 기준

- 같은 질문에서 다시 사용할 가능성이 높은가?
- 원본 위치와 근거 문장을 다시 찾을 수 있는가?
- 기존 문서의 갱신으로 충분한가, 새 문서가 필요한가?
- AI 요약, 외부 주장의 사실, 개인 판단을 구분했는가?
- 빠르게 변하는 정보에 날짜와 적절한 신뢰도를 표시했는가?

이 기준을 통과하지 못한 탐색 결과는 임시 메모로 남기고 canonical 위키에는 편입하지 않는다. 구체적인 도구 경계는 [[knowledge-tool-roles]], 연구 중심 구현은 [[second-brain-research-workflow]]에 정리한다.

## 열린 질문

- 어떤 재사용 빈도와 검증 비용을 새 페이지 생성 임계값으로 삼을 것인가?
- 자동화된 그래프 분석과 사람의 의미 검토 사이에 어떤 승인 관문을 둘 것인가?
- 개인 경험에서 나온 지식과 외부 출처 기반 지식을 어떤 구조로 연결할 것인가?

## 📰 최근 관련 소식
- 중국 'AI 군사화' 박차...타이완 '드론군 양성' 맞불 (YTN 사이언스, Thu, 06 Au) — https://news.google.com/rss/articles/CBMijAFBVV95cUxNVnpfR2JOam1zbWthUENVaTVvQkdJdGNGUHF5SThhZmxJOWhteXJ1QjZzdk50akhhT3R4c0pYemtfV25PeXgyMG5SNUZmVlVRY0IzYnFNMjVGZk9XeDMyc3hTN0pUUDBrems4X1VoS2pkWXEtZ1Q0bHlEcmRlLWpVQ1BoX3dNVnFxY2hXbw?oc=5
- [리포트] 니어스랩, 코스닥 출사표···피지컬 AI 드론으로 방산시장 정조준 (팍스경제TV, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiZ0FVX3lxTFAwMVgxZU1Jd3JVdkdUM09BYk9EM3UxZ2dqZVR1Y01rTVQxR1d4SmZ3dXYxaXBCVzl5enV5T3c3dXB3dU1lVy0zcTNNSmNSNHoxZ3ctdHRkZzU0Wlp4RzZYUm1HOXR6SjQ?oc=5
- [IPO챗] 니어스랩 "풍력서 검증한 AI 자율비행으로 글로벌 방산 공략" (연합뉴스, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiYEFVX3lxTE1RSnhlY0xnMnR1aWRISlNkNWc1ZWgyWkN3ZEtQQU1UZnN6eUhHdEU4a2xtSkJ2ZHlvdDBhbUlRWHhjSFIwREp6aUkyWDBmT3lKcnBTSG1ybGMtTHlZWkE3Y9IBYEFVX3lxTE1RSnhlY0xnMnR1aWRISlNkNWc1ZWgyWkN3ZEtQQU1UZnN6eUhHdEU4a2xtSkJ2ZHlvdDBhbUlRWHhjSFIwREp6aUkyWDBmT3lKcnBTSG1ybGMtTHlZWkE3Yw?oc=5
- 니어스랩, 코스닥 출사표..."국내 1호 피지컬 AI 드론으로 방산 시장 공략" (AI타임스, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTE1yNlI4NnpyejdfanZEd0Nfa0tJb3J0TGZnWlZ3dGFNUEN4VFhZdi0zdm82Rm5pZkNuemdZS0g3aVgxRTM5ckJ1a25fODFpLVZFOXNBV3o5UFczTFhJaE0tV3dzWnBHN1BoOWc?oc=5
- ‘피지컬 AI 드론’ 앞세워 상장 도전…니어스랩, “글로벌 방산 기업 도약” (서울경제, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiVkFVX3lxTE0za0dOeHlpZ3drSm9DU2d6RnllVm8ycXFmWmRCOG5LWDlGTFA0bWVUeXVqMkVsS2JWZVFvNXB1US1rOV9Jd1RNb0V6aUlYenNOa1BJZTRR?oc=5
- 전북경찰, 드론으로 농경지 등서 온열질환 사고 예방 순찰 (연합뉴스, Fri, 07 Au) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE56akNTNFFXOXR2V01PZzBaV3JqdGRIV0R6ZU4zRjBtWC13cGJsTG1aREg1cVRzakdMenQ1MElPWVR4QmZqUU13VUduUGd5YWRVWVRtWXdDT0R4MzTSAWBBVV95cUxPT3h1MlQwMFAxY0xha1dYdDVtZmZyVy1XNDRCWVVMYXA4N3pyMHRsUXI4N3JrenlBSUVfYy1nS0JYLUliN0E4THh6bVd2M3JjcTZtOTNNMHdtbmtHaXRXZlQ?oc=5
- ‘광교호수공원서 드론으로 배달시키세요’ (서울경제, Wed, 05 Au) — https://news.google.com/rss/articles/CBMiUkFVX3lxTE5MQzhtV0NtY1g5TGk4OHpOaTRtUGRDY09oQXd6bFRrVTE1RWNzNldKbF9LQkZFdG8yU2RLUmxwZjRSU3BYNDMwV2otbXJubm5YYlHSAVNBVV95cUxPdFBRSk14NXR0V3NjX2JnV2ZCeWxzelJqcjBfRGFQTEZfOE9zRlpDb2ZaLVlwblRMTmtJN2tLYW5TSWRjQmgyUWRsOUlwTUxIMDFzNA?oc=5
- AI 자율주행 드론으로 글로벌 방산시장 공략 (매일경제, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiTkFVX3lxTE9haTRmam0zaWRyT2hnQ3FEeTZMSmx0QlRSaVhwTlBhLVNzcHA0Rzl0X3R0THAxc1VWWnVOMTM3ai0zakNIUy0yMThNeFlxQQ?oc=5
- 니어스랩, AI 자율비행 드론으로 방산부문서 수익성 확보와 성장 가속 (파이낸스스코프, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTE96dDZIZml1WTZXalFOUnF1cDRRblJrVEtTTGRJczVQcVFzRGc1aEtoY05KOWVWRHFDX1BUazFQTmVtV0t3R0kyWElyWGFPbUxTX2R1Qkh2UW84b283ajVhR2p4MkdmcGEwS0E?oc=5
- 풍력발전 점검에서 방산으로…니어스랩, 코스닥 상장 도전 (ekn.kr, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiY0FVX3lxTE1uRi1IQnA1NHQ5WWtfZUVtc1h6STJUYVg3c0VQR1JLMW5lNkt6ODM2MEZzT2t0Qlg3amQtUFM4UTMyYXZ4dlBMNkEwMjBoU1JFT2VVN01qTnh3VTdVbi1XcE90aw?oc=5
- 니어스랩, 풍력 AI 자율비행 기술로 방산 공략 (더스탁(The Stock), Thu, 06 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTFAzVlVjWHVUckxuZFZCeG5tWGI5aDk0SGdvTG9QWmRldDdpMktGbW1veW0tZDNnQURqdlNuRUJlT0JxWjNMdVFmb1JQcDNMcEw4dmNhMFdYLTJpTF9aamdJV1M0dmpsTkZSQ1E?oc=5
- 니어스랩, AI 자율비행 앞세워 방산시장 공략…코스닥 상장 도전 (바이라인네트워크, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiVkFVX3lxTE1CaFFPM1BBajhqVzFUcW5JZTJ1emYwcDJiWGE2QXA5d050ckxhSVlWeGdyQ1pNQlZzUm0xN3o2aURkYzBGTTZCYVlvbzFTSGNiMGdIYWlR?oc=5
- [IPO 현장터치] 니어스랩 “피지컬 AI 드론으로 글로벌 방산시장 공략” (뉴스투데이, Thu, 06 Au) — https://news.google.com/rss/articles/CBMiXkFVX3lxTE9EelE3MmgtRnR2MEVBMXFua3hxNmZxT2pKLWE2QzM1TUk3Vms2am9aOUtKR3hqOXRKM2ZVc0VVaGVzUnM3eXYyVmRkSnRucVRYRFB1WDlsdll5MkxwVVE?oc=5
- 호원대, 드론·AI 융합콘텐츠 제작 교육 운영 실시...남원 시민 참여 - 머니투데이 (머니투데이, Mon, 10 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTFBSOEt3S0Y2LUFZRW1iSVYtNFpDRWtvRERTcmtpSlRaZGtvVWhSVWJETHRldk10SUpkQWllQlNYYk9zNWZRLUYyLXRvaDVxZzdROUVrMXg4eWJteDFHTVJsWGtqTnpEMlpiY3fSAW9BVV95cUxNRU5WZDVmeEw4YTNyc013TkhPaWFGSkNCNTY1SFowSjlXRGZVVmpmaURvM2FVcXV6Mlp1WXBaZHVUWFNjS3FKRXVNQXJmZDd6OTdIMmhSSFF6V3B2X21qN1M0SEE2cG5NVDhaVlVGYjg?oc=5
- '피지컬 AI 기반 자율비행 드론' 니어스랩, 일반 공모 돌입[오늘청약] (edaily.co.kr, Tue, 11 Au) — https://news.google.com/rss/articles/CBMigAFBVV95cUxPMnFfYkhlNHNYYkdEOWNUTjUzcWNJcG04ZXN1R09JbVloVHF5dHpmdUlja0ExdkVyRENnSVZjU1RSckdUSWJrSjVrSG83SDBfTFRXUWRKQV9va2ozVUtSbThrdlo0QWdkSUpTQkdzM3BGai1RNDItNjlHYy16ZFpJeA?oc=5
- AI 드론 기업 니어스랩, 최종 공모가 4만1200원…공모가 밴드 상단으로 확정 (livebiz.today, Tue, 11 Au) — https://news.google.com/rss/articles/CBMibEFVX3lxTE1jLUdNck1CVE8tejlYRnp6dzk3ajV4bWZOaUJ4Q053SEpmS1MtYWREXzVXblp0dGZ5eUhBTEVZMHMxRUYwS2w2bnVjWmd5UU8yNUZEaEMtd0VVckRMR0tSQi11bzF3VkNOZVNubw?oc=5
- 안양시, AI 과학축제 연다…"드론·로봇부터 자율주행까지" - 머니투데이 (머니투데이, Wed, 12 Au) — https://news.google.com/rss/articles/CBMiakFVX3lxTFBkbjVabm5xVUpOaGNFR01taTVPY0tyWWRnTDVEWlB1OHJHeW9GazBHQTlMa0VCX1FsY0pQZjM1a1ZoeVhPV05vYUQwZ2poNDFLN240NHhXVWZKM18ySmZDalVqTWlyTkFMdUHSAW9BVV95cUxNa2gwTnkwR3NRWUU2ZFFOdUlScW1mLXU3djhENnR0VnUwN1k2c0w3dEJXV2RkakNYX1E3OWdiV2h5RDM4Ymhaa0tOa0lhTFhnNlVRWGJjUEo1eFlvY0ZERGZXRjQ1a0t6TDZWLWt2NFk?oc=5
- 니어스랩 공모가 상단 41,200원 확정, 얼어붙은 공모주 시장 뚫었다 (플래텀(Platum), Tue, 11 Au) — https://news.google.com/rss/articles/CBMiSEFVX3lxTFBKSGF1dGE4aTRrelJPUGF0SE9fLVNlWlozQndoZGFDSFR4SHpnX1NQaG1vOGx6NlFkZzF3LVNkRWxDVHJORF83LQ?oc=5
- 폭염철 더 바쁜 드론…논밭 온열질환 살피고 곳곳 피해예방 방송 (매일경제 마켓, Fri, 14 Au) — https://news.google.com/rss/articles/CBMiUkFVX3lxTE5laEhNZ3ZvYW81MWVLMEN3cHVkVmhwM3ZNWWVZT1JqeWkxWlVwbzZSUFA1d3dyLUpxZGJNd1g2X2lpVjY3eUM4dVY4Qm5tdS1xWVE?oc=5
- 0.3초 만에 레이저 '번쩍', 드론까지 출격…첨단무기 타깃은 '모기'[월드콘] - 머니투데이 (머니투데이, Fri, 14 Au) — https://news.google.com/rss/articles/CBMiaEFVX3lxTFBZMGNIUWpaOXBHdmFBcWttQ0FsWlJiQXo1cFBPZ1E0Zk5oUTZubGNkWmM3c3V0RzUza3lSQUtCWWFtcDRzZ3hWdjFqQU9KQUZFc1JaZG1QUjJvZmI5QnVuRTZqLVZZY01i0gFuQVVfeXFMUHpDamd6bUI5eVZ3NVlRQ0lnRFVXbVktdWI5ejJJMVBlbjd0ODBENEpyTzFVZ0lIeUc2UTlVUUtjWkJJRVQ2N1JFdHdTODcxcFFIbmVkUTVBVTRRbkswUGtuOENORVdZNlo1dThpU1E?oc=5
- [핑크랩 PinkLAB] PinkLAB Band - drummer (youtube.com, 2026-08-14) — https://www.youtube.com/watch?v=OIs7R4QU8Vs
- [핑크랩 PinkLAB] PinkLAB Band | Drummer (youtube.com, 2026-08-13) — https://www.youtube.com/watch?v=eF9S3rb5Hwk
