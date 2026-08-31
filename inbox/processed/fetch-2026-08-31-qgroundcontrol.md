---
title: "qgroundcontrol v5.1.4 Release Notes"
created: 2026-08-31
captured: 2026-08-31
type: release-note
tag: v5.1.4
domain: gcs-software
source: https://github.com/mavlink/qgroundcontrol/releases/tag/v5.1.4
tags: [drone, gcs-software, qgroundcontrol]
---

# qgroundcontrol v5.1.4 Release Notes (2026-08-30)

This is the stable release of QGroundControl v5.1.

## What's New

See the [What's New](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/getting_started/whats_new.html) page for a summary of user-facing changes since V5.0.

> [!IMPORTANT]
> The HUD pitch display direction has been corrected in V5.1: pitching nose-down now moves the pitch indicator down, matching the roll convention. See the [HUD documentation](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/fly_view/hud.html) for details.

## Changes in v5.1.4

- fix(PlanView): Land tool showed Land/Alt Land but inserted RTL for rover
- fix(Comms): never leave link worker threads running at destruction
- fix(Video): harden delayed H.265 recording
- fix(Video): parse elementary streams before recording
- fix(AppSettings): normalize section selection when page collapses to one section
- fix(AppSettings): hide unavailable sections
- fix(APM): skip ESC component when motor PWM params are absent
- fix(Settings): navigate settings pages by untranslated page key
- fix(VehicleSetup): use untranslated section IDs for section filtering
- fix(PlanView): remove pending plan rename, restore Save as... including mobile
- fix(APMFirmwarePlugin): start mission correctly for already-armed vehicles
- fix(AppSettings): fill settings sidebar
- fix(PX4): remove dead UAVCAN ESC enumeration from Power setup
- fix(Joystick): match actual update rate to setting
- fix(UI): correct misleading PX4 tuning and video setting labels
- fix(translations): keep %1 placeholder in zh_CN PIDTuning message
- fix(FlyView): use raw meters for forward-flight goto loiter radius
- fix(PX4FirmwarePlugin): detect gripper via PD_GRIPPER_TYPE on PX4 v1.17+
- fix(MissionController): correct inverted flight path segment cache reuse condition

## Installation

See the [Download and Install](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/getting_started/download_and_install.html) page for per-platform installation instructions.

## Reporting Issues

Please report any problems you find on [GitHub Issues](https://github.com/mavlink/qgroundcontrol/issues), noting that you are running v5.1 Stable.
