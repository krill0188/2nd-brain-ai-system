---
title: "qgroundcontrol v5.1.5 Release Notes"
created: 2026-10-02
captured: 2026-10-02
type: release-note
tag: v5.1.5
domain: gcs-software
source: https://github.com/mavlink/qgroundcontrol/releases/tag/v5.1.5
tags: [drone, gcs-software, qgroundcontrol]
---

# qgroundcontrol v5.1.5 Release Notes (2026-10-01)

This is the stable release of QGroundControl v5.1.

## What's New

See the [What's New](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/getting_started/whats_new.html) page for a summary of user-facing changes since V5.0.

> [!IMPORTANT]
> The HUD pitch display direction has been corrected in V5.1: pitching nose-down now moves the pitch indicator down, matching the roll convention. See the [HUD documentation](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/fly_view/hud.html) for details.

## Changes in v5.1.5

- fix(translations): restore missing %1 placeholders in ko_KR, pt_PT, zh_CN
- fix(MAVLink): expose enum values to QML through MAVLinkEnums
- fix(MissionManager): restore mission commands lost to broken enum translations
- fix(Scripting): center download/delete icons on selected script
- Fix ArduPilot lua script list directory not working
- fix(MainWindow): stop critical vehicle message popup stealing keyboard focus
- fix(FTP): preserve paths when removing the MAVFTP URI scheme
- fix(Audio): pronounce acronyms in vehicle status text
- fix(APM): start takeoff when vehicle is already armed on the ground
- fix(Video): show receiver settings for discovered streams
- fix(LogManager): let LoggingCategoriesDialog scroll as a whole instead of nested views
- fix(AppLogging): make filter bar horizontally scrollable, put Categories first
- fix(AnalyzeView): complete 0 byte onboard logs instead of stalling the download
- fix(Settings): show sidebar group dividers and hide dangling ones
- fix(Camera): stop timelapse capture from the shutter button
- fix(Camera): stop zoom slider echoing camera-reported zoom back as a command
- fix(Comms): read link connection state from atomic flag, not thread-affine socket
- fix(RadioCal): keep throttle stick down in diagram for non-centered throttle
- fix(Vehicle): remove initial connect outer timeouts causing slow-link failures

## Installation

See the [Download and Install](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/getting_started/download_and_install.html) page for per-platform installation instructions.

## Reporting Issues

Please report any problems you find on [GitHub Issues](https://github.com/mavlink/qgroundcontrol/issues), noting that you are running v5.1 Stable.
