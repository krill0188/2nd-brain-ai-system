# DroneWiki NVIDIA 보조 분석 운영

## 목적

DroneWiki의 `raw/`·`inbox/`·기존 canonical 페이지를 읽기 전용으로 분석하고, NVIDIA NIM을 통해 연구 후보 초안을 만드는 보조 계층이다.

## 경계

```text
NVIDIA NIM → research/drafts/ 후보 초안
사람 검토 → research 승인
명시적 승격 → canonical/index.md/log.md
```

NVIDIA 또는 Hermes가 다음 파일을 자동 수정하지 않는다.

- `raw/`
- `entities/`
- `concepts/`
- `comparisons/`
- `queries/`
- `index.md`
- `log.md`

연구 후보는 사실·추론·가설·반대 근거·추가 확인 항목을 분리해야 한다. 출처 경로는 제공된 실제 경로만 사용하며, AI 출력만으로 canonical 지식을 만들지 않는다.

## 사용

프롬프트만 생성:

```bash
python3 scripts/nvidia_research_assist.py \
  "MAVLink 패킷 손실과 failsafe의 관계를 근거와 한계로 정리해줘" \
  inbox/processed/<실제-자료>.md \
  entities/flight-logging-analysis.md
```

NVIDIA NIM으로 실행하고 연구 초안에 저장:

```bash
python3 scripts/nvidia_research_assist.py \
  "MAVLink 패킷 손실과 failsafe의 관계를 근거와 한계로 정리해줘" \
  inbox/processed/<실제-자료>.md \
  entities/flight-logging-analysis.md \
  --run \
  --output research/drafts/2026-10-15-mavlink-failsafe-nvidia.md
```

이 도구는 `research/drafts/` 이외의 출력 경로를 거부한다. 원본 로그·API 키·분석 산출물을 Git에 넣지 않는다.

## 모델 역할

- NVIDIA Nemotron: 후보 요약, 근거 구조화, 반대 근거와 조사 공백 제안
- codex-lb/Codex: 구현·테스트·Git 변경 검토
- 사람: 근거 확인, 승인, canonical 승격
