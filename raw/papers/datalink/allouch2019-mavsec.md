---
title: "MAVSec: Securing the MAVLink Protocol for Ardupilot/PX4 Unmanned Aerial Systems"
authors:
  - Azza Allouch
  - Omar Cheikhrouhou
  - Anis Koubaa
  - Mohamed Khalgui
  - Tarek Abbes
venue: "IWCMC 2019"
year: 2019
arxiv: "1905.00265"
url: "https://arxiv.org/abs/1905.00265"
pdf: "https://arxiv.org/pdf/1905.00265"
topics: [datalink, mavlink, security, encryption, px4, ardupilot]
abstract: |
  This paper proposes MAVSec, a security protocol specifically designed for MAVLink 
  to address the critical security vulnerabilities in drone communication systems. 
  MAVSec provides authentication, integrity, and confidentiality for MAVLink messages 
  while maintaining the lightweight nature of the protocol. The paper presents a 
  comprehensive security analysis and implementation evaluation for both PX4 and ArduPilot.
ingested: 2026-07-27
---

# MAVSec: Securing the MAVLink Protocol for Ardupilot/PX4 Unmanned Aerial Systems

## Metadata

| 항목 | 내용 |
|------|------|
| **저자** | Azza Allouch, Omar Cheikhrouhou, Anis Koubaa, Mohamed Khalgui, Tarek Abbes |
| **발행처** | IWCMC 2019 (International Wireless Communications and Mobile Computing Conference) |
| **연도** | 2019 |
| **arXiv** | 1905.00265 |
| **PDF** | https://arxiv.org/pdf/1905.00265 |

## 주요 내용

### 연구 목표
- MAVLink 보안 프로토콜(MAVSec) 제안
- 드론 통신 시스템의 보안 취약점 해결

### 제공 기능
- **Authentication**: 메시지 인증
- **Integrity**: 무결성 보장
- **Confidentiality**: 기밀성 제공
- **Lightweight**: 경량 프로토콜 유지

### 대상 시스템
- PX4
- ArduPilot

## 관련 위키 페이지

- [[mavlink2-security]] — MAVLink 2 보안
- [[mavlink-protocol]] — MAVLink 프로토콜
- [[datalink-communication]] — 데이터링크 통신
- [[px4-system-architecture]] — PX4 시스템
- [[ardupilot-architecture]] — ArduPilot 아키텍처

## 인용

```bibtex
@inproceedings{allouch2019mavsec,
  title={MAVSec: Securing the MAVLink Protocol for Ardupilot/PX4 Unmanned Aerial Systems},
  author={Allouch, Azza and Cheikhrouhou, Omar and Koubaa, Anis and Khalgui, Mohamed and Abbes, Tarek},
  booktitle={International Wireless Communications and Mobile Computing Conference (IWCMC)},
  pages={569--574},
  year={2019},
  organization={IEEE}
}
```
