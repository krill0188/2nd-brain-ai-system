# Stage 0-R 실행 복구 — 2026-09-15 KST

상태: **기술적 갱신 성공 / 발행 검토 대기 / Stage 0-R HOLD**.

## 완료한 수정

- 임베딩 실패 원인: FastEmbed 기본 임시 캐시에 토크나이저만 있고 ONNX 모델이 미완료 다운로드 상태였다. 모델 로딩 실패를 직접 재현했다.
- 공개 모델의 고정 리비전 e5d116277351513fd260955ece953ecddde7046e 파일을 복구하고 SHA-256 92f682c55d39e728187c6bffd488f17462d4e05e3c5fe86ef9ba6f38d66122ed 일치 검증. 임시 폴더 대신 2nd/.ua/model-cache/fastembed를 명시했다. 모델/차원/생성 계약은 변경하지 않았다.
- shared flock 도구를 추가하고 pipeline, 수동 ai-control ingest, fetch, daily ingest, 주간 lint/summary, kinetic, graph 생성, embedding 생성, self-update CLI에 연결했다. 실제 상속 FD를 확인하며 단순 환경 플래그를 신뢰하지 않는다.
- Python 자식에 pass_fds를 전달하고 self-update는 node --import tsx로 직접 실행해 중간 launcher의 FD 유실을 피한다. 직접 tsx --apply도 잠금 wrapper로 재진입한다.
- --candidate-root로 실행별 고유 후보 경로를 사용한다. 기존 --candidate의 덮어쓰기 거부는 유지한다.
- 기존 07:30 launchd 일정을 보존하고 후보 root 인자를 변경·재로드했다. 즉시 실행 옵션은 추가하지 않았다. 후보 root: /Users/amaster/projectm/drone-wiki-publication-candidates.
- --refresh-derived로 fetch/ingest/self-update를 재실행하지 않고 현재 원본의 파생자료만 복구했다. 실패 단계와 고정 오류 코드를 남기며 비밀/임의 provider 출력은 결과 파일에 보존하지 않는다.

## 실제 검증

| 항목 | 결과 |
|---|---|
| canonical lint | 382개, 위반 0 |
| embeddings | 887개 / 768차원 / FRESH |
| canonical graph | 382 nodes / 1699 edges, missing 0, extra 0, source fresh |
| discovery | 1486 nodes / 1526 edges, pending 0 |
| preflight | lint / kinetic / embeddings / graph 4개 PASS; publication-policy만 차단 |
| source 안정성 | 파생자료 갱신 실행의 원본 fingerprint 검사 통과 |
| 공개 snapshot | 596개 파일, 작업 전후 전체 해시 동일 |
| 테스트 | Python 회귀 27개 PASS; Node 수동/상속/동시 실행 잠금 fixture PASS; 잠금 helper TypeScript 검사 PASS |

## 현재 중단 지점

발행 정책은 approve 22 / retain 550 / hold 30 / block 1 / retire-from-candidate 2 / exclude 24다.
변경된 bytes의 기존 승인 해시가 일치하지 않아 새 검토가 필요하다. 브리핑은 파생 원본 검토가 필요해 별도 block이다.
정책을 자동 승인하거나 차단을 우회하지 않았다. 새 실제 발행 후보는 생성되지 않았다.
공개 데이터 교체, Git commit/push, Vercel 배포는 수행하지 않았다.

## 아직 완료로 주장하지 않는 항목

- 수정 이후 실제 07:30 예약의 첫 성공은 미관찰이다. 재로드된 job의 runs=0은 정상 등록 상태일 뿐 실행 성공 증거가 아니다.
- 이번 검증은 현재 데이터의 파생자료 복구다. fetch부터 시작하는 전체 생성 체인의 새 성공을 의미하지 않는다.
- 위 CLI 경로는 잠금 대상이지만 임의 에디터, 별도 에이전트, 웹 API 내부의 직접 writer까지 통제하는 전역 잠금은 아니다. source fingerprint 검사는 유지한다.
- legacy graph 관계 425개 검토, 과거 discovery 처리 성공 여부 UNKNOWN은 그대로다.
- 공개 서비스 배포 상태는 이번에 조회하지 않았다.

## 다음 단계

아래 31개 자료의 공개 적합성·근거·개인정보 여부를 검토하고 승인/제외를 결정한 뒤 정확한 hash 정책에 반영한다.
그 이후 새 격리 후보를 생성·검증한다. 실제 공개 교체/배포는 별도 승인이다.
예약 실행은 이 승인 검토가 남아 있으면 발행 단계에서 계속 안전하게 중단될 수 있다.

## 발행 검토 목록

| 경로 | 상태 | 사유 |
|---|---|---|
| `.ua/daily-briefing.json` | block | derived-source-review-required |
| `.ua/discovery-knowledge-graph.json` | hold | unapproved-new-or-changed |
| `.ua/drone-knowledge-graph.json` | hold | unapproved-new-or-changed |
| `.ua/embeddings.json` | hold | unapproved-new-or-changed |
| `.ua/news-feed.json` | hold | unapproved-new-or-changed |
| `.ua/self-update-state.json` | hold | unapproved-new-or-changed |
| `concepts/6g-isac-matlab-usrp.md` | hold | unapproved-new-or-changed |
| `concepts/ai-knowledge-workflow.md` | hold | unapproved-new-or-changed |
| `concepts/amprius-sicore-battery.md` | hold | unapproved-new-or-changed |
| `concepts/ardupilot-params-by-version.md` | hold | unapproved-new-or-changed |
| `concepts/china-drone-export-controls.md` | hold | unapproved-new-or-changed |
| `concepts/dame-net-uav-image-restoration.md` | hold | unapproved-new-or-changed |
| `concepts/dji-mavic-4-pro.md` | hold | unapproved-new-or-changed |
| `concepts/drone-news-hardware.md` | hold | unapproved-new-or-changed |
| `concepts/drone-news-ops.md` | hold | unapproved-new-or-changed |
| `concepts/dronuum-computing-continuum.md` | hold | unapproved-new-or-changed |
| `concepts/emax-nanoscout-pro-1s-whoop.md` | hold | unapproved-new-or-changed |
| `concepts/fcc-military-drone-restrictions.md` | hold | unapproved-new-or-changed |
| `concepts/indi-stability-tilt-rotor-vtol.md` | hold | unapproved-new-or-changed |
| `concepts/mavlink-m-interoperability.md` | hold | unapproved-new-or-changed |
| `concepts/micro-drone-slam-imu-vio-lidar-uav-livox-mid-360-pixhawk-4-m.md` | hold | unapproved-new-or-changed |
| `concepts/path-uav-target-handoff.md` | hold | unapproved-new-or-changed |
| `concepts/radial-impeller-drone.md` | hold | unapproved-new-or-changed |
| `concepts/simplesense-dft-seraphimos-air-force.md` | hold | unapproved-new-or-changed |
| `concepts/stl-diffusion-multi-agent-planning.md` | hold | unapproved-new-or-changed |
| `concepts/yolo-v8-4-152.md` | hold | unapproved-new-or-changed |
| `concepts/yolo.md` | hold | unapproved-new-or-changed |
| `entities/kite-aerospace.md` | hold | unapproved-new-or-changed |
| `entities/terra-drone.md` | hold | unapproved-new-or-changed |
| `entities/wingcopter.md` | hold | unapproved-new-or-changed |
| `raw/papers/_unclassified/path-continuous-target-sensing-among-autonomous-cooperative-drones.md` | hold | unapproved-new-or-changed |
