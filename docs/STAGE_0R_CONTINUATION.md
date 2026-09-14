# Stage 0-R — 공개 경로 전환 및 실행 체인 보완

기준: 2026-09-15 KST. **후보의 중복 경로 문제 해결, 예약 실행 전환은 미완료.**

## 변경 파일과 이유

2nd Brain 저장소(`/Users/amaster/2nd`):

| 파일 | 변경 이유 |
|---|---|
| `publication/policy.json` | 이전 QGroundControl/A2Z entity 경로 두 개의 정확한 hash 및 대체 문서를 명시. 실제 공개 파일 삭제 승인과는 별개인 격리 후보 전용 제외 정책. |
| `scripts/publication-gate.py` | 최대 2개 canonical 경로만 후보에서 제외. baseline hash, 원본의 이전 경로 부재, 승인된 대체 문서 hash를 모두 검사. 검사 후 원본·snapshot 변경도 후보 생성 전후에 확인. |
| `scripts/knowledge-pipeline.py` | kinetic 정상 적용을 생성 단계에 복원. news feed와 발행 정책을 원본 fingerprint에 포함. `--validate-existing`로 유료 생성·메시지 없이 검증→격리 후보를 순서대로 실행. 결과 보고서를 원자 저장. |
| `scripts/apply-kinetic-rules.py` | `--no-notify`로 규칙 적용 기능은 보존하면서 외부 메시지만 생략. 기존 기본 명령과 `--check`는 유지. |
| `scripts/test_publication_gate.py` | 후보 제외 조건, hash 불일치, 일괄 제외 차단, 원본 재등장, 검사 후 private 변경의 실패 차단 검증. |
| `scripts/test_pipeline_safety.py` | 기존 데이터 검증 모드가 생성기를 호출하지 않는지, 실패 후 후보 생성이 차단되는지, news 변경 감지 및 kinetic 알림 생략 검증. |
| `00_CURRENT_SYSTEM.md`, `docs/STAGE_0R_CONTINUATION.md` | 최신 후보 수치·해결 범위·미활성 조건 반영. |

기존 사용자 변경인 `extract-knowledge-graph.py`의 max_tokens와 `fetch-inbox.sh`, canonical/index/log 등은 이번 커밋에 포함하지 않는다. 이번에는 canonical 및 raw를 편집하지 않았다.

## VERIFIED — 실제 검사 결과

- `--validate-existing` 실행: Validate:all 0 → Publish:isolated-candidate 0. 외부 생성기/메시지/배포 호출 없음.
- 후보 596 files, canonical 376개, unique slug 376개, 중복 0건.
- 웹의 실제 `getAllPages` 및 `getPageBySlug`로 기존 `qgroundcontrol`, 새 `qgroundcontrol-v5-1-0`, 기존 `a2z-longtail-dual` 주소가 모두 해석됨을 확인.
- 정책 결과: approve 32 / retain 564 / retire-from-candidate 2 / exclude 24. **실제 공개 snapshot 삭제 0, 기준 596개 파일 hash 변경 0.**
- 회귀 fixture 26개 PASS(publication 12, embedding 5, graph 4, status 2, pipeline 3), 기존 graph library 6개 PASS.
- preflight 5개 항목 모두 PASS: lint / kinetic check / embedding freshness / graph coverage / publication policy.
- 기존 12개 ai.2nd jobs는 loaded. plist와 예약 시각은 변경하지 않았다. 이번에는 웹 코드 변경이 없어 기존 production build PASS 결과를 반복 실행하지 않고 후보 로더를 직접 검증했다.

## 현재와 목표 실행 체인

```text
검증한 현재 경로
~/2nd current source + artifacts
  → Validate(lint / kinetic check / freshness / graph / publication)
  → source stability 확인
  → 격리 candidate (596 files, canonical 376, 중복 0)
  → source stability 재확인
  → local Report
  → 실제 data/wiki 교체 및 Deploy: 실행 안 함

보완한 생성 체인 후보 — 예약 미활성
fetch → ingest → self-update --apply → kinetic apply --no-notify
  → lint → embeddings --if-stale → discovery(limit 15) → canonical graph
  → Validate → isolated Publish candidate → 승인 후 Deploy → Report
```

`--validate-existing`는 현재 데이터 검증용이다. 생성 순서의 운영 검증으로 주장하지 않는다. 실행 중인 주요 launchd job이 있으면 시작을 거부하며, 독립 수동 writer는 fingerprint와 gate의 입력 hash 재검사로 변화를 감지한다. 이 검사가 공통 writer lock을 대신한다는 뜻은 아니다.

## 아직 남은 예약 전환 — 구체적 영향 범위

PM의 읽기 전용 재검토 결과:

- 기존 8개 daily calendar를 단일 07:30 체인으로 전환해야 한다. 단순히 sync 시각만 뒤로 미루면 긴 작업과의 race를 해결하지 못한다.
- 공통 lock 참여 대상: fetch, daily-ingest, self-update, kinetic, discovery, update-graph, `ai-control.sh run-ingest`, 각 legacy 수동 진입점. 자식 호출이 부모 lock을 상속하도록 구현해야 중첩 교착을 피한다. **이 공유 lock 전환은 아직 구현하지 않았다.**
- 주간 lint/summary는 보고 전용 의도지만 Bash까지 강제로 제한한 reader는 아니다. 일관된 완료 상태를 읽도록 함께 조정해야 한다.
- morning-report의 11:30 전송은 현재 독립 실행이다. pipeline 완료/실패/진행중 상태를 보고에 연결해야 한다. medic은 별도 저장소이므로 분리 유지한다.
- 다음 안전한 활성화 순서: 위 진입점의 공통 lock 구현·실패 fixture 검증 → plist backup 및 idle 확인 → 기존 8개 calendar 제거(명령/label 보존) → 단일 job 설치(`RunAtLoad`/`KeepAlive` 없음) → 배포 없는 첫 주기 검증. 설치 실패 시 이전 plist 복원.
- discovery backlog가 limit 15 뒤에도 남으면 preflight가 차단하는 비용 제한은 유지한다.

이번에는 이 조건을 건너뛰어 launchd를 전환하지 않았다. **Stage 0-R 전체 완료 판정은 여전히 불가**이며, 남은 핵심 작업은 공유 lock·단일 예약 전환·첫 실행 주기의 관찰이다. 기존 graph 관계 425개 및 과거 discovery 성공 여부 같은 이전 보고서의 검토/UNKNOWN도 그대로 유지한다.

## 복원과 증거

- 실제 공개 snapshot은 바뀌지 않아 public rollback은 필요 없다.
- 후보의 두 경로를 다시 보존하려면 `candidate_retirements`만 제거하고 새 격리 후보를 생성하면 된다. 기존 후보를 덮어쓰지 않는다.
- 변경 전 gate/policy는 현재 작업의 `work/continuation/publication-gate-before.py`, `policy-before.json`에 보관했다. 과거 배포 wrapper 복원은 자동 push/deploy를 재활성화할 수 있으므로 하지 않는다.
- `verification.json`, `candidate-audit.json`, `pipeline-result.json`, `preflight.json`, `qa.json`, `schedule-inventory.json`에 최신 근거를 기록했다.
- 원격 push / production deploy / 공개 snapshot 교체 / launchd reload / 외부 메시지 실행 없음.
