# DroneWiki 아침 점검 이상 3건 — 근본원인 분석 및 조치 보고서

- **대상 시스템**: 2nd Brain(`~/2nd`) → DroneWiki(`drone-wiki-web.vercel.app`) 자동화 파이프라인
- **발생일**: 2026-09-11 (04:00 KST 전후) / **보고서 작성**: 2026-09-12 00:51 KST
- **작성자**: PM(직접 진단·조치) — 마스터 원본 아침 점검 메시지 2건 기반

---

## 0. 마스터가 공유한 원본 아침 점검 메시지

**2026-09-10 (정상)**
```
✅ 새벽 수집: 오늘 뉴스 37건
✅ AI 브리핑: 오늘 2장 생성됨
⚠️ 위키 컴파일: inbox 14건 잔여 — ingest 확인 필요
✅ 웹 배포: 사이트에 오늘 브리핑 게시됨
```

**2026-09-11 (이상 3건)**
```
✅ 새벽 수집: 오늘 뉴스 31건
⚠️ AI 브리핑: 오늘 분 없음 — daily-briefing 확인 필요
⚠️ 위키 컴파일: inbox 28건 잔여 — ingest 확인 필요
⚠️ 웹 배포: 사이트 브리핑 날짜=2026-09-10 — sync/deploy 확인 필요
```

---

## 1. 결론 먼저 — 단일 근본원인

**9/11 04:00 KST 직전, Claude Pro 구독(`claude -p` CLI)의 주간 사용한도가 소진되어 있었고, 리셋 시각(2026-09-11 07:00 KST)보다 새벽 자동화 잡의 실행 시각(03:30~04:30)이 더 이르게 걸려 있었습니다.**

이 때문에 그날 새벽 파이프라인에서 `claude -p`를 호출하는 모든 단계가 연쇄적으로 실패했고, 보고된 3건의 이상 증상은 전부 이 하나의 원인에서 파생된 결과였습니다. `inbox 28건 잔여`(9/10의 14건 + 9/11의 신규 14건 누적)와 `웹 배포 날짜=9/10`은 별개 버그가 아니라 같은 원인의 하위 증상입니다.

**현재 상태: 3건 모두 조치 완료, 실측 검증까지 마쳤습니다.** (2장 참조)

---

## 2. 증거 체인 (실제 로그 원문)

### 2-1. 03:31 — 새벽 수집(fetch) 중 AI 브리핑 생성 실패
`~/2nd/.ua/logs/2nd-daily-fetch.log`
```
[2026-09-11 03:30:00] === START 2nd-daily-fetch ===
...
  ko-summarize: claude 호출 실패 —
  briefing: claude 호출 실패 —
✅ 14개 파일 수집 완료 → inbox/ 에 저장됨 (다음 cron에서 처리)
[2026-09-11 03:31:40] === END 2nd-daily-fetch (exit=0) ===
```
→ 뉴스 수집(31건) 자체는 정상 완료됐으나, 한글요약과 AI 브리핑 생성 단계에서 `claude` 호출이 실패. 스크립트가 실패를 비치명적으로 처리해 `exit=0`으로 종료 — 그래서 마스터 아침 점검에는 "새벽 수집 ✅"로 보였지만 내부적으로 이미 문제가 시작된 상태였습니다.

### 2-2. 04:00 — 위키 컴파일(daily-ingest) 완전 실패
`~/2nd/.ua/logs/ingest.log`
```
You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message
· your weekly limit resets Sep 11 at 7am (Asia/Seoul)
You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message
· your weekly limit resets 7am (Asia/Seoul)
```
`launchctl print`로 확인한 `ai.2nd.daily-ingest`의 `last exit code = 1` — 명확한 실패로 기록되어 있었습니다. 원인 메시지에 리셋 시각(7am)이 명시되어 있어 근본원인을 특정할 수 있었습니다.

### 2-3. 04:30 — 웹 동기화(sync-dronewiki)는 정상 실행, 단 새 내용이 없었음
```
799e2fd sync: 2nd Brain → DroneWiki 2026-09-11 04:30 [569docs]
```
sync 자체는 커밋까지 정상 실행됐습니다. 다만 소스(`~/2nd/.ua/daily-briefing.json`)가 여전히 9/10 날짜였기 때문에, 정상 작동한 sync가 "정상적으로 오래된 데이터"를 그대로 배포한 것입니다. **sync-dronewiki는 무죄** — 2-1의 브리핑 생성 실패가 유일한 원인입니다.

### 2-4. 실측 재현 (2026-09-12 00:xx, curl로 라이브 사이트 직접 확인)
```
$ curl -s https://drone-wiki-web.vercel.app/ | grep -oE "오늘의 드론 소식 \([0-9-]+\)"
오늘의 드론 소식 (2026-09-10)
```
조치 전 시점에 실제 배포 사이트가 여전히 9/10 날짜를 보여주고 있음을 직접 확인 — 마스터가 공유한 아침 점검 메시지가 정확했음을 재확인했습니다.

---

## 3. 조치 내역 (2026-09-12 00:34 ~ 00:42, 전부 완료)

| 순서 | 조치 | 결과 |
|---|---|---|
| 1 | `claude -p` CLI 정상 복구 여부 테스트 | ✅ 정상 응답 확인(주간 한도 이미 리셋됨) |
| 2 | `daily-ingest-claude.sh` 수동 재실행 (28건 백로그 처리) | ✅ 수집 28개, 컴파일 5개(신규 concept), 갱신 2개, 실패 0개 — inbox **28 → 0** |
| 3 | 9/11자 AI 브리핑 백필 생성 (동일 로직 일회성 재현, 스크립트 파일은 미수정) | ✅ `daily-briefing.json` date=2026-09-11, 6장 카드 생성 |
| 4 | `dronewiki-sync.sh` 재실행 (rsync → git commit → push → Vercel 프로덕션 배포) | ✅ 커밋 `f5f31bd`, 573docs, GitHub push 성공, Vercel 배포 성공 |
| 5 | 라이브 사이트 직접 재검증(curl) | ✅ **"오늘의 드론 소식 (2026-09-11)"로 갱신 확인** |

### 3-1. 위키 컴파일 상세 (28건 처리)
- 신규 concept 5건: `yolo-v8-4-146`, `marl-uav-wildfire-exploration`(arXiv 산불대응 UAV 강화학습), `kci-uav-lidar-ground-point-density-dem-accuracy`(KCI 논문), `drone-news-2026-09-10`, `drone-news-2026-09-11`
- 기존 페이지 갱신 2건: `yolo.md`(릴리스 이력), `fcc-military-drone-restrictions.md`(DJI FCC 반발 이슈 추가)
- 나머지(비도메인 강좌, 프로모성 영상, 헤드라인만 있는 얇은 기사 등)는 정상적으로 스킵 처리 — `log.md`에 사유별 기록 완료
- `index.md` 총 페이지 365 → **370**

### 3-2. 9/11 브리핑 백필 내용 (요약)
```
date: 2026-09-11
- 오늘의 종합: 러시아 드론의 젤렌스키 전용기 위협 논란 + 우크라이나 3000km 초장거리 드론 타격
- 뉴스 / 정부사업 / 방산 / 영상 / 논문 — 분야별 카드 각 1장
```

### 3-3. 웹 배포 상세
- git 커밋 `f5f31bd`: `sync: 2nd Brain → DroneWiki 2026-09-12 00:42 [573docs]`
- 신규 4개 concept 파일 포함(9 files changed, 489 insertions)
- `origin/main`에 push 완료, Vercel 프로덕션 배포 성공

---

## 4. 재발 방지 권고

| 우선순위 | 권고 | 근거 |
|---|---|---|
| 높음 | `daily-ingest-claude.sh`/`daily-briefing.sh`에 `claude -p` 실패 시 **재시도 로직**(예: 2~3시간 뒤 1회 재시도하는 후속 launchd 잡) 추가 | 이번 사고의 정확한 트리거는 "주간 리셋 시각(7am)보다 크론 실행 시각(03:30~04:30)이 이름" — 리셋 요일/시각은 사용량에 따라 매주 달라질 수 있어 재발 가능 |
| 중간 | `daily-briefing.sh`/`ko-summarize` 실패 로그의 에러 원문이 비어 있던 문제 — `$ERR` 캡처·로깅 보강 | 2-1 로그에서 "claude 호출 실패 — " 뒤가 비어 있어, 실제 원인(스펜딩 한도)을 특정하려면 04:00 `ingest.log`의 별도 메시지까지 대조해야 했음. `briefing.sh` 자체 로그만으로는 원인 특정이 어려웠던 점은 개선 여지 |
| 낮음 | `daily-ingest-claude.sh`가 실패(exit=1)할 때 Telegram/모닝리포트에 "왜" 실패했는지(예: 한도 소진 vs 다른 오류) 한 줄이라도 원인 태그를 남기면 마스터가 아침에 바로 판단 가능 | 이번엔 원인 특정에 로그 3개 파일을 교차 대조해야 했음 |

**이미 잘 작동한 부분**: 아침 점검 리포트 자체가 문제를 정확하게 잡아냈습니다(inbox 잔여·브리핑 누락·배포 날짜 불일치 3가지 신호 전부 정확). 감시 체계는 정상 작동했고, 원인은 순수하게 "LLM 호출 한도 소진"이라는 외부 요인이었습니다.

---

## 5. 현재 최종 상태 (2026-09-12 00:5x 기준)

| 항목 | 상태 |
|---|---|
| inbox 잔여 | **0건** (28건 전부 처리) |
| AI 브리핑 | **2026-09-11자 존재**(백필 완료, 6장) |
| 사이트 배포 | **2026-09-11로 갱신 확인**(curl 실측) |
| index.md 총 페이지 | 370 |
| 다음 정규 실행 | 오늘(9/12) 03:30 fetch → 04:00 ingest → 04:30 sync, 정상 진행 예상(한도 이미 리셋됨) |

---

## 6. 재현/검증 방법 요약

```bash
# 1. launchd 잡 상태 확인
launchctl list | grep ai.2nd

# 2. 근본원인 로그 확인
tail -100 ~/2nd/.ua/logs/ingest.log
grep "claude 호출 실패" ~/2nd/.ua/logs/2nd-daily-fetch.log

# 3. inbox 백로그 확인
find ~/2nd/inbox -maxdepth 1 -name "*.md" | wc -l

# 4. 라이브 사이트 브리핑 날짜 확인
curl -s https://drone-wiki-web.vercel.app/ | grep -oE "오늘의 드론 소식 \([0-9-]+\)"
```

---

*본 조치는 마스터의 "당장 풀어봐" 지시에 따라 실제 파이프라인(inbox 처리, 브리핑 재생성, git push, Vercel 프로덕션 배포)에 직접 개입해 수행되었습니다. `daily-briefing.sh` 등 기존 스크립트 파일 자체는 수정하지 않고, 동일 로직을 일회성 스크립트로 재현하는 방식으로 백필했습니다.*
