# AI 개발환경 구성 문서

> 작성일: 2026-07-26  
> Mac: Intel x86_64 / macOS Ventura 13.7.8

---

## 1. 설치된 프로그램과 버전

| 프로그램 | 버전 | 설치 경로 |
|---|---|---|
| Git | 2.54.0 | `/usr/local/bin/git` |
| Node.js | v24.14.1 | `/usr/local/bin/node` |
| npm | 11.11.0 | `/usr/local/bin/npm` |
| VS Code | 1.130.0 | `/Applications/Visual Studio Code.app` |
| VS Code CLI | 1.130.0 | `~/.zshrc` / `~/.bash_profile` PATH 등록 |
| OpenCode | 1.18.5 | `~/.npm-global/bin/opencode` |
| Claude CLI | 2.1.220 | `~/.local/bin/claude` |
| Codex CLI | 0.144.3 | `~/.npm-global/bin/codex` |
| ripgrep | 15.1.0 | `/usr/local/bin/rg` |
| jq | 1.8.1 | `/usr/local/bin/jq` |

---

## 2. 각 도구 실행 명령

```bash
# OpenCode + Kimi (OpenRouter)
opencode

# Claude Code (Claude Max 구독)
claude

# Codex (ChatGPT Plus 구독 또는 API)
codex

# VS Code
code .
```

---

## 3. 인증 방식

| 도구 | 인증 방식 | 비고 |
|---|---|---|
| OpenCode | `OPENROUTER_API_KEY` 환경변수 | 아래 설정 방법 참조 |
| Claude Code | Claude Max 구독 계정 로그인 | API 키 방식 아님 |
| Codex | OpenAI API 키 또는 ChatGPT Plus 로그인 | 현재 API 키 방식 |
| Gemini | Google Gemini Code Assist (VS Code 확장) | `google.geminicodeassist` |

---

## 4. OpenRouter API 키 설정 방법

터미널에서 아래 명령 실행 (키는 절대 파일에 저장하지 않음):

```bash
# 환경변수 임시 설정 (현재 세션만)
export OPENROUTER_API_KEY="여기에_키_입력"

# 영구 설정 (~/.zshrc 또는 ~/.bash_profile에 추가)
echo 'export OPENROUTER_API_KEY="여기에_키_입력"' >> ~/.zshrc

# 또는 OpenCode 공식 로그인 명령 사용
opencode providers login openrouter
```

OpenRouter 키 발급: https://openrouter.ai/keys

---

## 5. 모델 선택

| 도구 | 기본 모델 | 설정 파일 |
|---|---|---|
| OpenCode | `openrouter/moonshotai/kimi-k2` | `~/.config/opencode/config.json` |
| OpenCode (프로젝트) | 글로벌 설정 상속 | `~/2nd/opencode.json` |

사용 가능한 Kimi 모델:
- `openrouter/moonshotai/kimi-k2` (표준)
- `openrouter/moonshotai/kimi-k3` (최신)
- `openrouter/moonshotai/kimi-k2.7-code` (코드 특화)
- `openrouter/~moonshotai/kimi-latest` (무료 프로모션)

---

## 6. 역할 구분

| 도구 | 용도 |
|---|---|
| OpenCode + Kimi | Markdown 정리, 반복 코드 초안, 문서 분류, 저장소 요약 |
| Claude Code | 시스템 아키텍처, 복잡한 디버깅, 다중 파일 리팩터링, 설계 검토 |
| Codex | 코드 구현, 버그 수정, 기능 추가, Git 변경사항 분석 |
| Gemini | 결과 교차검증, 자료 요약, 대안 탐색 (VS Code 확장 또는 웹) |

---

## 7. 예상 과금 구조

| 구성요소 | 과금 방식 |
|---|---|
| VS Code | 무료 |
| Claude Code | Claude Max 구독 한도 내 |
| Codex | ChatGPT Plus 구독 한도 내 |
| OpenRouter/Kimi | 종량제 (호출량 기반) |
| Gemini Code Assist | 무료 한도 내 (Google AI Studio) |

> **주의**: OpenRouter 자동충전은 비활성화 상태를 유지한다.

---

## 8. 문제 발생 시 복구 방법

```bash
# 설정 백업 위치
ls ~/ai-dev-backup/

# OpenCode 재설치
npm install -g opencode-ai

# Claude CLI 재설치
npm install -g @anthropic-ai/claude-code

# Codex 재설치
npm install -g @openai/codex

# VS Code CLI PATH 재등록 (zsh)
echo 'export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"' >> ~/.zshrc
source ~/.zshrc
```

---

## 9. 설정 파일 위치

| 파일 | 역할 |
|---|---|
| `~/2nd/opencode.json` | OpenCode 프로젝트 설정 (API 키는 환경변수) |
| `~/.config/opencode/config.json` | OpenCode 글로벌 설정 |
| `~/2nd/AGENTS.md` | 모든 AI 에이전트 공통 규칙 |
| `~/2nd/CLAUDE.md` | Claude Code 전용 지침 |
| `~/2nd/.vscode/settings.json` | VS Code 워크스페이스 설정 |

---

## 10. 자주 사용하는 명령

```bash
# VS Code로 2nd 폴더 열기
code ~/2nd

# OpenCode 시작
cd ~/2nd && opencode

# OpenCode 모델 목록 확인
opencode models openrouter | grep kimi

# Claude Code 시작
claude

# Codex 시작
codex

# 설치된 도구 버전 전체 확인
git --version && node --version && npm --version && opencode --version && claude --version && codex --version
```
