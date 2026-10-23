---
title: "Global Shutter \uae30\ubc18 OCC \ub4dc\ub860 \ucc44\ub110\uc744 \uc704\ud55c \uc774\uc911 \ud0dc\uadf8 \uae30\ubc18 ChaCha20-Poly1305 AEAD \uc778\uc99d \ud504\ub85c\ud1a0\ucf5c"
created: 2026-10-23
captured: 2026-10-23
type: paper
domain: ops-mission
source: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003395575
authors: "\uae40\uc720\uac15(\uc544\uc8fc\ub300\ud559\uad50)"
journal: "\uc815\ubcf4\ubcf4\ud638\ud559\ud68c\ub17c\ubb38\uc9c0"
published: "2026"
open_access: true
tags: [drone, ops-mission, paper, kci]
---

# Global Shutter 기반 OCC 드론 채널을 위한 이중 태그 기반 ChaCha20-Poly1305 AEAD 인증 프로토콜

**Authors**: 김유강(아주대학교)
**Journal**: 정보보호학회논문지
**Published**: 2026
**Link**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003395575
**원문 공개**: ✅ 공개(KCI 원문 내려받기 버튼 확인됨)

## Abstract

본 논문은 Global Shutter 기반 OCC 드론 채널을 위한 이중 태그 기반 ChaCha20-Poly1305 인증 구조를 제안한다. 기존 메시지 단위 AEAD는 최종 태그 수신 전까지 위변조 탐지가 지연되고, 패킷 단위 AEAD는 192-bit 패킷에서 128-bit 태그로 인해 오버헤드가 크다. 제안 방식은 일반 패킷에 24-bit mini-tag를 적용해 1차 검증하고, K번째 패킷에 128-bit full-tag를 적용해 인증 주기 전체의 무결성을 최종 검증한다. Mini-tag 검증만으로 복호화·평문 전달을 수행하지 않으며, full-tag 검증 이후에만 최종 복호화 및 전달이 이루어진다. 또한 HKDF-Expand 기반 implicit nonce를 통해 nonce 전송 오버헤드를 줄인다. K=8에서 76.9%의 채널 효율을 달성했으며, 위조 공격 및 ASCON 비교를 통해 제안 방식의 성능과 보안성을 평가하였다.
