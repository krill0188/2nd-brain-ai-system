# 마스터 2nd Brain — 기술 스택

> 작성일: 2026-07-26  
> 환경: Intel Mac / macOS Ventura 13.7.8 / x86_64

---

## 에디터 & 인터페이스

| 도구 | 버전 | 용도 |
|---|---|---|
| **VS Code** | 1.130.0 | 주 편집기, 터미널, Git, Gemini 통합 |
| **Obsidian** | 최신 | Markdown 읽기·편집, Graph View, 역링크 |

---

## AI CLI 도구 (인증 방식)

| 도구 | 버전 | 인증 | 역할 |
|---|---|---|---|
| **OpenCode** | 1.18.5 | OpenRouter API key (env var) | Kimi K2 기반 문서 정리 |
| **Claude Code** | 2.1.220 | Claude Max 구독 로그인 | 아키텍처, 복잡한 분석 |
| **Codex CLI** | 0.144.3 | ChatGPT Plus 구독 | 코드 구현, Git 분석 |
| **Gemini** | VS Code 확장 | Google 계정 | 교차검증, 요약 |

---

## AI 모델

| 도구 | 기본 모델 | 대체 모델 |
|---|---|---|
| OpenCode | `moonshotai/kimi-k2` (OpenRouter) | `moonshotai/kimi-k3` |
| Claude Code | Claude Max (Sonnet 4.6) | — |
| Codex | ChatGPT Plus (GPT-4o) | — |

---

## 지식관리 도구

| 도구 | 용도 |
|---|---|
| **Zotero 9.0.6** | 논문·서지·첨부 관리 |
| **Zotero Connector** (Chrome) | 웹에서 Zotero로 직접 저장 |
| **Obsidian Web Clipper** (Chrome) | 웹 페이지 → raw/web/ 저장 |

---

## 개발 인프라

| 항목 | 값 |
|---|---|
| Node.js | v24.14.1 |
| npm | 11.11.0 |
| Git | 2.54.0 |
| Homebrew | /usr/local (Intel) |

---

## 설정 파일 위치

| 파일 | 용도 |
|---|---|
| `~/2nd/opencode.jsonc` | OpenCode 프로젝트 설정 (Kimi, watcher) |
| `~/.config/opencode/config.json` | OpenCode 글로벌 설정 |
| `~/2nd/CLAUDE.md` | Claude Code 전용 지침 |
| `~/2nd/AGENTS.md` | AI 에이전트 공통 규칙 |
| `~/2nd/SCHEMA.md` | 지식 구조 계약 |

---

## 환경 변수 (설정 필요)

```bash
# ~/.zshrc 또는 ~/.bash_profile에 추가
export OPENROUTER_API_KEY="<your-key>"
```

**보안 원칙**: API 키는 파일에 기록하지 않는다. 반드시 환경 변수로만 참조한다.

---

## 도구 실행 명령

```bash
# VS Code 열기
code ~/2nd

# OpenCode 실행 (~/2nd에서)
cd ~/2nd && opencode

# Claude Code 실행
claude

# Codex 실행
codex

# OpenRouter API 키 등록
opencode providers login openrouter
```
