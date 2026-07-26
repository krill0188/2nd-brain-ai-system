# 2nd Brain AI System

[English](README.md) | **한국어**

> 드론 도메인 특화 Markdown + Git 기반 지식관리 시스템 — 5개 AI 도구(OpenCode + Kimi K2 / Claude Code / Codex / Gemini Code Assist / GitHub Copilot) 탑재.

## 프로젝트 소개

이 프로젝트는 **드론 기술** 8개 분야(drone / datalink / swarm / voice-control / drone-hw / drone-sw / drone-ai / ai-agent)에 특화된 개인 지식관리 시스템입니다. 순수 Markdown 파일로 **수집 → 컴파일 → 탐색 → 사람 결정**의 흐름을 실현하며, Obsidian·VS Code·GitHub 등 Markdown 호환 도구라면 어디서든 사용할 수 있습니다.

[ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template) 기반 위에 커스텀 AI 도구 레이어를 추가했습니다.

### 전체 아키텍처

**Evidence → Canonical Memory → Discovery → Human Decision** 네 계층으로 구성됩니다. 원본 자료는 `raw/` 아래 불변 증거로 보존하고, 반복 사용할 지식만 출처 추적이 가능한 canonical Markdown으로 컴파일합니다. [AGENTS.md](AGENTS.md)가 5개 AI 도구의 역할을 정의하여 수집·컴파일·교차검증·최종 판단을 각각 담당합니다.

![Master 2nd Brain AI System 아키텍처](docs/architecture/master-ai-architecture.png)

### 운영 워크플로

**Capture → Compile → Discovery → Human Decision** 순서로 진행하며, 세 단계 무결성 관문(Gate A: raw 무결성 / Gate B: lint/frontmatter / Gate C: 그래프/신선도)을 통과해야 정식 변경이 확정됩니다. 승인된 변경은 canonical 페이지·`index.md`·`log.md`를 하나의 원자적 작업으로 동시에 갱신합니다.

![Master 2nd Brain 운영 워크플로](docs/workflow/master-workflow.png)

### 기술 스택

AI 도구 5종이 지식 파이프라인의 각 단계에 매핑됩니다. 공개 형식 Markdown, 출처 메타데이터, Git 이력이 장기 자산이며 AI 도구는 교체 가능한 레이어입니다.

![Master 2nd Brain 기술 스택](docs/tech-stack/master-tech-stack.png)

## AI 도구 역할

[AGENTS.md](AGENTS.md)에 정의된 5개 도구의 역할입니다.

| 도구 | 인터페이스 | 주요 역할 |
| --- | --- | --- |
| **OpenCode + Kimi K2** | 터미널 (`opencode`) | Markdown 정리, 문서 초안, llm-wiki 컴파일, 반복 작업 전담 |
| **Claude Code** | 터미널 (`claude`) | 아키텍처 분석, 모순 검토, 복합 추론, 최종 판단 |
| **Codex** | 터미널 (`codex`) | 코드 구현, 드론 펌웨어 탐색 (PX4/ArduPilot/ROS2), Git 분석 |
| **Gemini Code Assist** | VS Code 사이드바 | 편집 중 교차검증, 다른 관점 제공, 요약 |
| **GitHub Copilot** | VS Code 인라인 | Markdown·코드 작성 시 자동완성 |

> **비용 원칙**: 반복적인 컴파일 작업은 Kimi K2(토큰 비용)에 위임합니다. Claude는 아키텍처 판단과 모순 해소에만 씁니다. Gemini와 Copilot은 무료이므로 편집 중 자유롭게 사용합니다.

## 드론 도메인 커버리지

주요 지식 도메인은 **드론 기술**이며, 8개 등록 태그로 분류합니다 ([SCHEMA.md](SCHEMA.md), [docs/domain/drone-domain-guide.md](docs/domain/drone-domain-guide.md) 참조).

| 태그 | 범위 |
| --- | --- |
| `drone` | 기체·비행 역학·규정·임무 설계 등 일반 드론 시스템 |
| `datalink` | RF·LTE·MAVLink 텔레메트리·C2 링크·암호화 |
| `swarm` | 멀티드론 협업·편대비행·합의 알고리즘 |
| `voice-control` | 드론 운용을 위한 자연어·음성 명령 인터페이스 |
| `drone-hw` | FC·ESC·모터·배터리·LiDAR·카메라·페이로드 등 하드웨어 |
| `drone-sw` | PX4·ArduPilot·GCS·MAVSDK·ROS/ROS2·MAVROS/MAVROS2·uORB |
| `drone-ai` | 컴퓨터 비전·자율비행·SLAM·객체 탐지·분할 |
| `ai-agent` | AI 에이전트 아키텍처·자율 의사결정·멀티에이전트 시스템 |

수집 우선순위: `drone-sw` → `datalink` → `drone-ai` → `swarm` → 나머지.

## 주요 기능

| 기능 | 설명 |
| --- | --- |
| **원본·출처 보존** | Zotero와 Obsidian Web Clipper로 논문·웹 자료를 수집하고, `raw/`에 원본·메타데이터·SHA-256을 보존해 언제든 근거로 돌아갈 수 있습니다. |
| **검증된 지식 컴파일** | OpenCode + Kimi K2가 원본을 entity·concept·comparison·query 문서로 구조화하고, 출처·신뢰도·모순을 추적합니다. |
| **연결형 Markdown 편집** | Obsidian에서 wikilinks와 백링크로 정식 지식을 탐색·편집하며, Copilot과 Gemini Code Assist가 인라인으로 지원합니다. |
| **멀티 AI 교차검증** | Claude Code와 Gemini가 동일 증거를 독립적으로 분석해 모순을 canonical 승격 전에 표면화합니다. |
| **드론 코드 탐색** | Codex가 PX4·ArduPilot·ROS2/MAVROS2·MAVSDK 소스를 탐색하고 결과를 `drone-sw` canonical 페이지로 통합합니다. |
| **사람 검증 관문** | AI 가설은 사람의 승인 없이 canonical 메모리로 승격되지 않습니다. Gate C 검사가 `index.md`와 `log.md` 갱신 전에 강제됩니다. |

## 사전 설치

### 수집 도구

| 구분 | 도구 | 용도 |
| --- | --- | --- |
| 필수 | [Obsidian](https://obsidian.md/download) | 이 저장소를 로컬 vault로 열어 Markdown 노트를 탐색·편집합니다. |
| 논문 수집 | [Zotero + Zotero Connector](https://www.zotero.org/download/) | 드론 논문·PDF·서지 정보를 관리하고 Chrome에서 메타데이터를 저장합니다. |
| 웹 수집 | [Obsidian Web Clipper](https://obsidian.md/clipper) | 웹 페이지를 `raw/web/` Markdown 파일로 변환·저장합니다. |

### AI 도구

| 도구 | 인증 방식 | 설치 |
| --- | --- | --- |
| [OpenCode](https://opencode.ai) + Kimi K2 | OpenRouter API 키 | `opencode providers login openrouter` |
| [Claude Code](https://claude.ai/code) | Claude Max 구독 | `claude` — 첫 실행 시 브라우저 로그인 |
| [Codex](https://github.com/openai/codex) | ChatGPT Plus 구독 | `codex` — 첫 실행 시 브라우저 로그인 |
| [Gemini Code Assist](https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist) | Google 계정 (무료) | VS Code 확장 설치 후 Google 로그인 |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub 계정 (built-in) | VS Code 1.130+ 내장 — 계정 아이콘 → GitHub 로그인 |

### 권장 설치 순서

1. 저장소를 복제하고 Obsidian vault로 엽니다.
2. Zotero, Zotero Connector, Obsidian Web Clipper를 설치합니다.
3. npm으로 OpenCode·Claude Code CLI·Codex CLI를 설치합니다.
4. VS Code에 Gemini Code Assist 확장을 설치합니다.
5. OpenRouter API 키를 등록합니다: `cd ~/2nd && opencode providers login openrouter`
6. `claude` / `codex` 첫 실행 시 브라우저에서 구독 계정 로그인을 완료합니다.
7. VS Code 계정 아이콘 → GitHub 로그인으로 Copilot을 활성화합니다.

## 폴더 구조

```text
.
├── inbox/                    # 분류를 기다리는 임시 입력
├── raw/                      # 불변 원본 증거
│   ├── articles/             # 기사·웹 클리핑 원문
│   ├── notebooklm/           # NotebookLM 소스 레코드
│   ├── papers/files/         # 논문 첨부 파일 (플레이스홀더)
│   ├── transcripts/          # 음성·영상·회의 전사
│   ├── web/                  # 웹 캡처 (원본 경로 보존)
│   ├── youtube/              # YouTube 메타데이터·전사
│   └── assets/               # 원본 문서가 참조하는 이미지
├── entities/                 # 정식 지식 — 사람·조직·도구
├── concepts/                 # 정식 지식 — 개념·원리
├── comparisons/              # 정식 지식 — 나란히 비교 분석
├── queries/                  # 출처 기반 질의와 종합 결과
├── docs/
│   ├── architecture/         # 시스템 아키텍처 다이어그램
│   ├── domain/               # 드론 도메인 수집 가이드
│   ├── tech-stack/           # 기술 스택 다이어그램
│   └── workflow/             # 운영 워크플로 다이어그램
├── templates/                # frontmatter 템플릿 5종
├── _archive/                 # 대체된 정식 페이지 보관
├── AGENTS.md                 # AI 도구 역할 정의 + 도메인 포커스
├── CLAUDE.md                 # Claude Code 전용 지침
├── SCHEMA.md                 # 데이터 계약 (권위 문서)
├── index.md                  # 활성 정식 지식 전체 목록
└── log.md                    # 덧붙이기 전용 작업 이력
```

## 빠르게 시작하기

### 1. 저장소 복제

```bash
git clone https://github.com/krill0188/2nd-brain-ai-system.git
cd 2nd-brain-ai-system
```

### 2. 편집기에서 열기

- **Obsidian**: `Open folder as vault` → 저장소 폴더 선택.
- **VS Code**: `code .` 또는 `code ~/2nd` (홈에 복제한 경우).

### 3. 지식 작업 세션 시작

```bash
# 일상 컴파일 작업 — Kimi K2
cd ~/2nd && opencode

# 아키텍처·모순 분석 — Claude
cd ~/2nd && claude

# 드론 코드 탐색 — Codex
cd ~/2nd && codex
```

### 4. 운영 기준 확인

지식을 추가하기 전에 [SCHEMA.md](SCHEMA.md)를 읽고, [index.md](index.md)에서 이미 다루는 주제를 확인한 뒤 [log.md](log.md)의 최신 기록을 살펴보세요. 이미 존재하는 주제라면 새 페이지를 만들지 말고 기존 페이지에 증거를 보강합니다.

## 기본 사용 흐름

1. **수집**: Obsidian Web Clipper로 웹 페이지를 `raw/web/`에 저장하고, Zotero로 논문을 받아 `raw/articles/`로 내보냅니다.
2. **분류**: `inbox/`의 항목을 올바른 `raw/` 하위 폴더로 옮기고 `templates/raw-article.md` 양식에 따라 frontmatter를 작성합니다.
3. **컴파일**: OpenCode(Kimi K2)에게 2개 이상의 raw 소스를 바탕으로 알맞은 템플릿을 사용해 canonical 페이지 초안을 요청합니다.
4. **교차검증**: Gemini 또는 Claude에게 초안의 모순·누락 커버리지를 검토하도록 합니다.
5. **승인 및 기록**: 승인 시 `index.md`를 갱신하고 같은 작업에서 `log.md`에 한 항목을 추가합니다.
6. **탐색**: 지식그래프 제안은 가설로만 취급합니다. 사람이 원문을 확인해 승인한 내용만 canonical로 승격합니다.
7. **보관**: 완전히 대체된 페이지만 `_archive/`로 옮기고, 링크를 수정한 뒤 `log.md`에 기록합니다.

## 데이터 관리 원칙

> [!IMPORTANT]
> `README.ko.md`는 사용 안내이며, 실제 데이터 계약은 [SCHEMA.md](SCHEMA.md)가 우선합니다. 규칙이 다르게 보이면 `SCHEMA.md`를 따르세요.

- **원본은 불변입니다.** 최초 캡처 후 `raw/` 본문을 수정하지 않습니다.
- **출처 경로는 실재해야 합니다.** 정식 지식의 `sources`에는 등록된 `raw/` 폴더 아래 실제 Markdown 파일만 기록합니다.
- **정식 지식은 선별해서 만듭니다.** 하나의 원본에서 중심적으로 다루거나 둘 이상에서 반복되는 주제만 페이지로 승격합니다.
- **정식 지식은 서로 연결합니다.** 모든 활성 canonical 페이지는 자신을 제외한 다른 두 페이지 이상에 `[[wikilinks]]`로 연결되어야 합니다.
- **변경은 원자적으로 기록합니다.** canonical 생성·수정·보관은 `index.md`와 `log.md` 갱신까지 완료되어야 끝납니다.
- **API 키는 Git에 올리지 않습니다.** OpenRouter·Zotero 등 모든 API 키와 인증 토큰을 저장소에 커밋하지 않습니다.

## 동기화

```bash
git add .
git commit -m "feat: drone-sw canonical 페이지 추가 (PX4 아키텍처)"
git push
```

Git으로 이력을 관리합니다. API 키·토큰·로그인 세션은 저장소에 절대 저장하지 않습니다.

## 라이선스

[ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template) 기반. 드론 도메인 AI 지식관리를 위해 확장·적용했습니다.
