---
title: "pymavlink v2.4.49 Release Notes"
created: 2026-07-29
captured: 2026-07-29
type: release-note
tag: v2.4.49
domain: comms-protocol
source: https://github.com/ArduPilot/pymavlink/releases/tag/v2.4.49
tags: [drone, comms-protocol, pymavlink]
---

# pymavlink v2.4.49 Release Notes (2025-08-01)

## What's Changed
* Tools: mavlogdump: preseve units allong with format when trimming logs by @IamPete1 in https://github.com/ArduPilot/pymavlink/pull/1078
* DFReader: fixed instance indexing for most messages by @tridge in https://github.com/ArduPilot/pymavlink/pull/1097
* tools/mavextra.py: use the correct origin by @rishabsingh3003 in https://github.com/ArduPilot/pymavlink/pull/1101
* mavutil: dump both in-link (from timestamp bits) and out-link (if sig… by @peterbarker in https://github.com/ArduPilot/pymavlink/pull/1100
* Replace cast(...) in generated Python code with type annotations by @ntamas in https://github.com/ArduPilot/pymavlink/pull/1089
* mavgen_objc.py: rename BOOL to MAV_BOOL by @andrewvoznytsa in https://github.com/ArduPilot/pymavlink/pull/1098
* allow javascript generator to work with both node and browser by @tridge in https://github.com/ArduPilot/pymavlink/pull/1103
* .github: Bump pypa/cibuildwheel from 3.0.1 to 3.1.1 in the github-actions group by @dependabot[bot] in https://github.com/ArduPilot/pymavlink/pull/1102
* Fixed several issues in the spin2 generator implmentation. by @RbtsEvrwhr-Riley in https://github.com/ArduPilot/pymavlink/pull/1083
* build(deps): bump nanoid and mocha in /generator/javascript_stable by @dependabot[bot] in https://github.com/ArduPilot/pymavlink/pull/1076
* build(deps): bump cross-spawn from 6.0.5 to 6.0.6 in /generator/javascript by @dependabot[bot] in https://github.com/ArduPilot/pymavlink/pull/1075
* tools: Add mavtranslatelog.py for updating tlog files by @Maarrk in https://github.com/ArduPilot/pymavlink/pull/1055
* mavutil: websocket fixes by @tridge in https://github.com/ArduPilot/pymavlink/pull/1106

## New Contributors
* @noahredon made their first contribution in https://github.com/ArduPilot/pymavlink/pull/1042
* @RbtsEvrwhr-Riley made their first contribution in https://github.com/ArduPilot/pymavlink/pull/1061
* @tpwrules made their first contribution in https://github.com/ArduPilot/pymavlink/pull/1067
* @oneWayOut made their first contribution in https://github.com/ArduPilot/pymavlink/pull/1093
* @rishabsingh3003 made their first contribution in https://github.com/ArduPilot/pymavlink/pull/1101
* @andrewvoznytsa made their first contribution in https://github.com/ArduPilot/pymavlink/pull/1098
* @Maarrk made their first contribution in https://github.com/ArduPilot/pymavlink/pull/1055

**Full Changelog**: https://github.com/ArduPilot/pymavlink/compare/v2.4.47...v2.4.49
