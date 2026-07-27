---
title: PX4 CI/CD Pipeline
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, CI/CD, build, test, github-actions, docker]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Knowledge-based page - no raw source ingested yet"
---

# PX4 CI/CD Pipeline

PX4는 GitHub Actions 기반 CI/CD 파이프라인을 사용하여 코드 품질을 유지하고 다양한 플랫폼에서의 빌드를 검증한다.

## CI/CD 아키텍처

```
┌─────────────────────────────────────────┐
│            GitHub Actions             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ │
│  │ Build   │ │ Test    │ │ Deploy  │ │
│  │ Matrix  │ │ Suite   │ │ Docs    │ │
│  └────┬────┘ └────┬────┘ └────┬────┘ │
└───────┼───────────┼───────────┼──────┘
        │           │           │
   ┌────┴────┐ ┌────┴────┐ ┌────┴────┐
   ▼         ▼ ▼         ▼ ▼         ▼
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│NuttX │ │Linux │ │Tests │ │SITL  │ │Docs  │
│Pixhawk│ │SITL  │ │Unit  │ │Test  │ │Build │
└──────┘ └──────┘ └──────┘ └──────┘ └──────┘
```

## 빌드 시스템

### Makefile 기반 빌드

| 명령 | 설명 |
|------|------|
| `make px4_fmu-v6x_default` | Pixhawk 6X |
| `make px4_sitl` | SITL |
| `make px4_sitl gazebo-classic` | Gazebo 시뮬레이션 |
| `make tests` | 테스트 실행 |
| `make clean` | 빌드 정리 |

### CMake 설정

```bash
# 빌드 디렉토리
cd build/px4_fmu-v6x_default

# 설정
cmake ../.. -DCONFIG=px4_fmu-v6x_default

# 병렬 빌드
make -j$(nproc)
```

## GitHub Actions Workflow

### 주요 Workflow

| Workflow | 설명 | 트리거 |
|----------|------|--------|
| **Build & Test** | 전체 빌드 및 테스트 | PR, Push |
| **SITL Tests** | 시뮬레이션 테스트 | PR, Push |
| **Documentation** | docs.px4.io 빌드 | Push to main |
| **Release** | 릴리스 바이너리 | Tag |

### Build Matrix

```yaml
# .github/workflows/build.yml
strategy:
  matrix:
    board:
      - px4_fmu-v6x
      - px4_fmu-v5x
      - px4_fmu-v4
    config:
      - default
      - test
      - bootloaders
```

## 테스트 전략

### 테스트 유형

| 유형 | 설명 | 도구 |
|------|------|------|
| **Unit Tests** | 모듈 단위 테스트 | gtest |
| **Integration Tests** | 통합 테스트 | SITL |
| **Hardware Tests** | 실제 하드웨어 | Test rack |
| **Code Coverage** | 커버리지 분석 | gcov/lcov |

### SITL 테스트

```bash
# 특정 테스트 실행
make test_MulticopterPositionControl

# 전체 테스트
make tests

# 테스트 상세 출력
make tests TESTARGS="--verbose"
```

## Docker 기반 빌드

### 개발 환경

```bash
# Docker 이미지 빌드
docker build -t px4-dev .

# 컨테이너 실행
docker run -it --rm \
  -v $(pwd):/src/PX4-Autopilot \
  px4-dev \
  bash -c "cd /src/PX4-Autopilot && make px4_sitl"
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3'
services:
  px4-build:
    image: px4io/px4-dev-nuttx-focal
    volumes:
      - .:/src/PX4-Autopilot:cached
    working_dir: /src/PX4-Autopilot
    command: make px4_fmu-v6x_default
```

## 릴리스 프로세스

### 버전 관리

| 버전 | 형식 | 예시 |
|------|------|------|
| **Stable** | v1.x.x | v1.14.0 |
| **Beta** | v1.x.x-beta | v1.15.0-beta1 |
| **Dev** | main | - |

### 릴리스 단계

1. **Feature Freeze**: 기능 동결
2. **Beta Testing**: 베타 테스트
3. **Release Candidate**: RC 빌드
4. **Stable Release**: 안정 버전
5. **Hotfix**: 긴급 수정

## 코드 품질

### 정적 분석

| 도구 | 용도 |
|------|------|
| **clang-tidy** | C++ 정적 분석 |
| **cppcheck** | 코드 검사 |
| **flake8** | Python 스타일 |
| **shellcheck** | Shell 스크립트 |

### 포맷팅

```bash
# 코드 포맷
make format

# 포맷 검사
make check_format
```

## 배포

### Firmware 배포

| 채널 | 설명 |
|------|------|
| **QGC** | QGroundControl 내장 |
| **GitHub Releases** | 바이너리 다운로드 |
| **Docs** | docs.px4.io |

### 문서 빌드

```bash
# 문서 빌드
make docs

# 로컬 서버
make docs_serve
```

## CI/CD 모범 사례

### PR 체크리스트

- [ ] 빌드 통과
- [ ] 테스트 통과
- [ ] 코드 포맷 준수
- [ ] 정적 분석 클린
- [ ] 문서 업데이트

### 개발 워크플로우

```
Feature Branch → PR → CI Checks → Review → Merge → Deploy
```

## 관련 개념

- [[drone-simulation]] — SITL 테스트 환경
- [[px4-architecture-deep]] — 모듈 빌드 구조
- [[ros2-drone-integration]] — ROS2 빌드 통합

## 수집 대상

- 실제 PX4 GitHub Actions workflow 파일
- Docker 이미지 최적화 사례
- 대규모 테스트 자동화 방법론
