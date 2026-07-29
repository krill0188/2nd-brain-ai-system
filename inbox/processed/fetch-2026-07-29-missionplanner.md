---
title: "missionplanner MissionPlanner1.3.83 Release Notes"
created: 2026-07-29
captured: 2026-07-29
type: release-note
tag: MissionPlanner1.3.83
domain: gcs-software
source: https://github.com/ArduPilot/MissionPlanner/releases/tag/MissionPlanner1.3.83
tags: [drone, gcs-software, missionplanner]
---

# missionplanner MissionPlanner1.3.83 Release Notes (2025-09-10)

## What's Changed
* Improve the uk localization by @FrequentFlyer86 in https://github.com/ArduPilot/MissionPlanner/pull/3385
* MAVLinkParam: fix rounding to 7 digits by @robertlong13 in https://github.com/ArduPilot/MissionPlanner/pull/3389
* FlightPlanner : tweak prefetch, Resolves #2591, resolves #2483 by @Godeffroy in https://github.com/ArduPilot/MissionPlanner/pull/3320
* Also check target_system!=0 when toggling safety switch in ctl-F screen. by @ROSStargh in https://github.com/ArduPilot/MissionPlanner/pull/3317
* InitialConfig: Limit Thrst Expo to 0.80 max by @EosBandi in https://github.com/ArduPilot/MissionPlanner/pull/3397
* Propagation: Add Scale to Elevation/Terrain Overlays by @EosBandi in https://github.com/ArduPilot/MissionPlanner/pull/3401
* HUD: Fix batterycell with icons by @EosBandi in https://github.com/ArduPilot/MissionPlanner/pull/3403
* CurrentState: honor MAVLinkInterface.speechenable by @robertlong13 in https://github.com/ArduPilot/MissionPlanner/pull/3258
* ConfigRawParams: Various bugfixes by @robertlong13 in https://github.com/ArduPilot/MissionPlanner/pull/3246
* ConnectionOptions fixes by @robertlong13 in https://github.com/ArduPilot/MissionPlanner/pull/3254
* AuthKeys: add Mavlink2Signed visible by @meee1 in https://github.com/ArduPilot/MissionPlanner/pull/3411
* Mcast dronecan by @meee1 in https://github.com/ArduPilot/MissionPlanner/pull/3410
* MSI: Update installer.bat by @EosBandi in https://github.com/ArduPilot/MissionPlanner/pull/3406
* Updated NFZ in Portugal. by @lvale in https://github.com/ArduPilot/MissionPlanner/pull/3398
* Config Planner - Choose how to access the map tiles : server, cache or both by @Godeffroy in https://github.com/ArduPilot/MissionPlanner/pull/3319
* WorkFlow: update mac.yml by @meee1 in https://github.com/ArduPilot/MissionPlanner/pull/3414
* Plugin: Create Terrain DAT file for uploading by @EosBandi in https://github.com/ArduPilot/MissionPlanner/pull/3413
* MainV2: remove periph version checking at connect by @robertlong13 in https://github.com/ArduPilot/MissionPlanner/pull/3418
* ConfigDroneCAN: Add disconnect button by @robertlong13 in https://github.com/ArduPilot/MissionPlanner/pull/3420
* FlightData: support alt frames for Guided by @robertlong13 in https://github.com/ArduPilot/MissionPlanner/pull/3430
* paramcompare: remove double inequality check by @robertlong13 in https://github.com/ArduPilot/MissionPlanner/pull/3431
* ConfigSerialInjectGPS.cs: Fix Septentrio config error while connected to ublox and changing away from the config RTK/GPS screen. by @EosBandi in https://github.com/ArduPilot/MissionPlanner/pull/3435
* ADSB: uAvionix Transponder Updates by @nicholas-inocencio in https://github.com/ArduPilot/MissionPlanner/pull/3429
* Increase "Change Alt Button" maximum by @rishabsingh3003 in https://github.com/ArduPilot/MissionPlanner/pull/3436
* Add interface for plugins to add HW and SW config pages by @EosBandi in https://github.com/ArduPilot/MissionPlanne
