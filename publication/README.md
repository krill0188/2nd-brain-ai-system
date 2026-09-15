# Publication Gate v1

> Status: **FOUNDATION ONLY — NOT WIRED TO PRODUCTION SYNC**

이 디렉터리는 `~/2nd`의 지식이 public DroneWiki로 나가기 전에 적용할 **Default Deny / Explicit Allow** 공개 경계를 정의한다.

## 왜 raw/frontmatter를 수정하지 않는가

`raw/`는 원문 근거 레이어이며 기존 스키마의 불변성 계약을 유지해야 한다. 따라서 공개 여부를 각 raw 문서에 덧붙이지 않고, 별도의 publication manifest와 snapshot builder에서 관리한다.

## v1 안전 모델

1. 현재 DroneWiki의 특정 **Git commit 전체를 불변 baseline**으로 고정한다.
2. builder는 live `~/2nd` 파일을 곧바로 공개하지 않고 baseline commit의 바이트를 그대로 사용한다.
3. 새 파일 또는 변경된 파일은 `approved_source_versions`에 **경로 + 2nd Brain의 full Git commit SHA**가 명시되어야만 다음 공개 snapshot에 반영된다.
4. 삭제/비공개 전환은 `revoked_paths`에 명시한다.
5. `.ua` 파생 산출물은 v1에서 임의 source override를 허용하지 않는다. 이후 단계에서 **승인된 public snapshot만 입력으로 재생성**하도록 파이프라인을 바꾼다.

이 방식은 단순 경로 allowlist보다 강하다. 이미 승인된 경로의 내용이 나중에 바뀌어도 자동으로 public에 노출되지 않는다.

## Manifest

`publication-manifest.json`의 핵심 필드:

- `baseline.commit`: 현재 이미 공개된 DroneWiki의 불변 Git commit
- `baseline.prefix`: `data/wiki`
- `publication_roots`: 공개 후보가 될 수 있는 일반 지식 루트
- `derived_artifacts`: 별도로 취급하는 정확한 `.ua` 공개 파일
- `approved_source_versions`: 검토 후 승인한 `path + source_commit`
- `revoked_paths`: 명시적으로 public snapshot에서 제외할 경로

승인은 branch 이름이나 `latest`가 아니라 반드시 **40자리 commit SHA**를 사용한다.

## 실행

```bash
# 현재 상태만 검사하고 report 생성
python3 scripts/build-publication-snapshot.py --dry-run

# snapshot 생성 (아직 production sync에는 연결하지 않는다)
python3 scripts/build-publication-snapshot.py

# 미승인 신규/변경 파일이 있으면 비정상 종료하는 CI/검사 모드
python3 scripts/build-publication-snapshot.py --dry-run --strict
```

기본 baseline repo 위치는 `$DRONE_WIKI_REPO`, `~/projectm/drone-wiki-web` 순으로 찾으며 `--baseline-repo`로 명시할 수 있다.

생성물:

- `.ua/publication-snapshot/`
- `.ua/publication-report.json`

둘 다 파생 상태이며 기존 `.gitignore`의 `.ua/` 정책 안에 머문다.

## 승인 절차

1. 공개하려는 문서를 `~/2nd`에서 검토한다.
2. 승인할 정확한 상태를 Git commit으로 고정한다.
3. `approved_source_versions`에 해당 `path`와 full `source_commit`을 추가한다.
4. PR에서 변경 내용과 공개 적합성을 검토한다.
5. snapshot builder/test를 통과시킨다.
6. Stage 1 통합 단계에서만 운영 sync가 publication snapshot을 읽도록 전환한다.

## 현재 단계의 비목표

- live launchd/Hermes wrapper 변경
- DroneWiki 자동 배포 경로 변경
- `.ua` 재생성 순서 변경
- production RAG 수정
- 기존 raw/canonical 문서 수정

따라서 이 foundation patch 자체는 현재 production 사이트의 동작을 변경하지 않는다.

## Rollback

아직 production에 연결하지 않았으므로 rollback은 이 branch/PR을 폐기하는 것으로 끝난다. 운영 sync, source knowledge, public deployment는 영향을 받지 않는다.
