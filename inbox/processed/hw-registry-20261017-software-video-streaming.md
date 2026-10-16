---
title: "video-streaming SW 레지스트리"
created: 2026-10-17
captured: 2026-10-17
type: software-registry
domain: software-ecosystem
category: video-streaming
tags: [drone, software, video-streaming]
---
# video-streaming SW

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| GStreamer | 오픈소스 | LGPL-2.1 (LICENSE 표기) | GStreamer 프로젝트 | https://github.com/GStreamer/gstreamer | 저장소 설명: 오픈소스 멀티미디어 프레임워크 | https://gstreamer.freedesktop.org |
| gst-rtsp-server | 오픈소스 | LGPL-2.1 | GStreamer | https://github.com/GStreamer/gst-rtsp-server | 저장소 설명: GStreamer 기반 RTSP 서버(메인 저장소로 병합 안내) | 미확인 |
| gst-plugins-rs | 오픈소스 | Apache-2.0 (GitHub 표시) | GStreamer | https://github.com/GStreamer/gst-plugins-rs | 저장소 설명: Rust로 작성된 GStreamer 플러그인 | 미확인 |
| FFmpeg | 오픈소스 | 대부분 LGPL v2.1 이상 (LICENSE.md) | FFmpeg 프로젝트(미러) | https://github.com/FFmpeg/FFmpeg | 저장소 설명: 공식 git 미러 | 미확인 |
| MediaMTX | 오픈소스 | MIT | bluenviron(구 aler9) | https://github.com/bluenviron/mediamtx | 저장소 설명: SRT/WebRTC/RTSP/RTMP/LL-HLS/MPEG-TS/RTP 라이브 미디어 서버·프록시 | 구 이름 rtsp-simple-server |
| gortsplib | 오픈소스 | MIT | bluenviron | https://github.com/bluenviron/gortsplib | 저장소 설명: Go용 RTSP 클라이언트·서버 라이브러리 | 미확인 |
| v4l2rtspserver | 오픈소스 | Unlicense | mpromonet | https://github.com/mpromonet/v4l2rtspserver | 저장소 설명: V4L2 장치 캡처용 RTSP 서버(HEVC/H264/JPEG/VP8/VP9) | 미확인 |
| SRT (Secure Reliable Transport) | 오픈소스 | MPL-2.0 | Haivision | https://github.com/Haivision/srt | 저장소 설명: SRT 프로토콜 구현 | 미확인 |
| srtla | 오픈소스 | AGPL-3.0 | irlserver | https://github.com/irlserver/srtla | 저장소 설명: 링크 결합(본딩) 지원 SRT 전송 프록시 | 다중 모뎀 본딩 용도 추정 |
| SRS | 오픈소스 | MIT | ossrs | https://github.com/ossrs/srs | 저장소 설명: RTMP/WebRTC/HLS/HTTP-FLV/SRT/DASH/GB28181 지원 실시간 미디어 서버 | 미확인 |
| Janus WebRTC Server | 오픈소스 | GPL-3.0 | Meetecho | https://github.com/meetecho/janus-gateway | 저장소 설명: WebRTC 서버 | 미확인 |
| LiveKit | 오픈소스 | Apache-2.0 | LiveKit | https://github.com/livekit/livekit | 저장소 설명: 사람과 AI를 잇는 엔드투엔드 실시간 스택 | 드론 연동 사례 미확인 |
| Pion WebRTC | 오픈소스 | MIT | Pion | https://github.com/pion/webrtc | 저장소 설명: WebRTC API의 순수 Go 구현 | 미확인 |
| aiortc | 오픈소스 | BSD-3-Clause | aiortc | https://github.com/aiortc/aiortc | 저장소 설명: asyncio 기반 파이썬 WebRTC/ORTC 구현 | 미확인 |
| webrtc-rs | 오픈소스 | Apache-2.0 | webrtc-rs | https://github.com/webrtc-rs/webrtc | 저장소 설명: 비동기 친화 Rust WebRTC 구현 | 미확인 |
| MAVLink Camera Manager | 오픈소스 | MIT | Blue Robotics | https://github.com/bluerobotics/mavlink-camera-manager | 저장소 설명: MAVLink 카메라 매니저 서비스 | MAVLink 카메라 프로토콜 연계 추정(설명은 서비스 한 줄) |
| BlueOS | 오픈소스 | GPLv3 / BlueOS Custom License 이중(LICENSE.md) | Blue Robotics | https://github.com/bluerobotics/BlueOS | 저장소 설명: ROV·USV 등 로봇 시스템 운영 오픈 플랫폼 | 드론(공중) 적용은 미확인 |
| OpenIPC firmware | 오픈소스 | MIT | OpenIPC 커뮤니티 | https://github.com/OpenIPC/firmware | 저장소 설명: 대체 IP 카메라 펌웨어 | FPV 활용 여부는 이 조사에서 미확인 |
| wfb-ng | 오픈소스 | GPL-3.0 | svpcom | https://github.com/svpcom/wfb-ng | 저장소 설명: 원시 WiFi 라디오 기반 장거리 패킷 라디오 링크 | 미확인 |
| OpenHD | 오픈소스 | GPL-3.0 | OpenHD 커뮤니티 | https://github.com/openhd/OpenHD | 미확인 | 저장소 설명 없음 |
| VDO.Ninja | 오픈소스 | AGPL-3.0 | steveseguin | https://github.com/steveseguin/vdo.ninja | 저장소 설명: WebRTC로 원격 영상을 OBS 등으로 가져오는 도구 | 드론 연동 사례 미확인 |
| OBS Studio | 오픈소스 | GPL-2.0 | OBS 프로젝트 | https://github.com/obsproject/obs-studio | 저장소 설명: 라이브 스트리밍·화면 녹화 SW | 드론 직접 연동 미확인 |
