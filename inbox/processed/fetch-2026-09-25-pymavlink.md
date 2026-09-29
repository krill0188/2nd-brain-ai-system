---
title: "pymavlink v2.4.50 Release Notes"
created: 2026-09-25
captured: 2026-09-25
type: release-note
tag: v2.4.50
domain: comms-protocol
source: https://github.com/ArduPilot/pymavlink/releases/tag/v2.4.50
tags: [drone, comms-protocol, pymavlink]
---

# pymavlink v2.4.50 Release Notes (2026-09-24)

## What's Changed
* Add RATE_ACRO and TURTLE modes by @andyp1per in https://github.com/ArduPilot/pymavlink/pull/1107
* mavfft_pid.py: correct sample rate to logging rate when using fast rate by @andyp1per in https://github.com/ArduPilot/pymavlink/pull/1109
* setup: detect if python dev package is installed by @tridge in https://github.com/ArduPilot/pymavlink/pull/1111
* [new] adding new unit of consumption: L/h by @TomasTwardzik in https://github.com/ArduPilot/pymavlink/pull/1023
* mavutil: allow ws/wss to reconnect attempt even after initial failure. by @khancyr in https://github.com/ArduPilot/pymavlink/pull/1112
* build(deps): bump cross-spawn from 6.0.5 to 6.0.6 in /generator/javascript_stable by @dependabot[bot] in https://github.com/ArduPilot/pymavlink/pull/1104
* build(deps): bump brace-expansion from 1.1.11 to 1.1.12 in /generator/javascript_stable by @dependabot[bot] in https://github.com/ArduPilot/pymavlink/pull/1105
* .github: bump pypa/cibuildwheel from 3.1.1 to 3.1.3 in the github-actions group by @dependabot[bot] in https://github.com/ArduPilot/pymavlink/pull/1108
* mavutil: port field is reserved by @tridge in https://github.com/ArduPilot/pymavlink/pull/1116
* mavlogdump.py follow argument non-functional by @rrhan0 in https://github.com/ArduPilot/pymavlink/pull/1119
* allow the signing timestamp limit to be set by @tridge in https://github.com/ArduPilot/pymavlink/pull/1126
* Pymavlink: add Wireshark Mavlink Telemetry Log (TLOG) file reader by @shancock884 in https://github.com/ArduPilot/pymavlink/pull/1128
* .github: Bump the github-actions group across 1 directory with 5 updates by @dependabot[bot] in https://github.com/ArduPilot/pymavlink/pull/1130
* mavutil.py: rename variable called 'type' to 't' by @peterbarker in https://github.com/ArduPilot/pymavlink/pull/1114
* mavgen_lua.py: copy with MAV_BOOL / int8 type bitmask by @peterbarker in https://github.com/ArduPilot/pymavlink/pull/1134
* Mavgen WLua: Update Wireshark LUA test cases to use latest Mavlink XML by @shancock884 in https://github.com/ArduPilot/pymavlink/pull/1135
* Lint the code with ruff, pylint and mypy by @amilcarlucas in https://github.com/ArduPilot/pymavlink/pull/1021
* Fix use of Set() in mavftp by @andyp1per in https://github.com/ArduPilot/pymavlink/pull/1136
* .github: Bump pypa/cibuildwheel from 3.2.0 to 3.2.1 in the github-actions group by @dependabot[bot] in https://github.com/ArduPilot/pymavlink/pull/1137
* Bump brace-expansion in /generator/javascript by @dependabot[bot] in https://github.com/ArduPilot/pymavlink/pull/1131
* generate WIP warnings on the use of WIP messages in C code by @tridge in https://github.com/ArduPilot/pymavlink/pull/240
* .github: Bump the github-actions group across 1 directory with 3 updates by @dependabot[bot] in https://github.com/ArduPilot/pymavlink/pull/1141
* .github: add test_branch_conventions to workflows by @peterbarker in https://github.com/ArduPilot/pymavlink/pull/1140
* mavschema.xsd: add superse
