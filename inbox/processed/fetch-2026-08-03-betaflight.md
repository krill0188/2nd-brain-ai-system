---
title: "betaflight 2026.6.1 Release Notes"
created: 2026-08-03
captured: 2026-08-03
type: release-note
tag: 2026.6.1
domain: flight-control
source: https://github.com/betaflight/betaflight/releases/tag/2026.6.1
tags: [drone, flight-control, betaflight]
---

# betaflight 2026.6.1 Release Notes (2026-08-02)

<!-- Release notes generated using configuration in .github/release.yml at 6dbc4218fd6bc33bf16ea32c670304d4f89321d5 -->

## What's Changed
### Features
* New led functions gps bar battery bar altitude by @jonas-becker in https://github.com/betaflight/betaflight/pull/13404
* Add MSP support for gyro_cal_on_first_arm by @haslinghuis in https://github.com/betaflight/betaflight/pull/13626
* Add RSSI dBm alarm to MSP by @McGiverGim in https://github.com/betaflight/betaflight/pull/13682
* S-term (for wings) by @limonspb in https://github.com/betaflight/betaflight/pull/13679
* Add DEBUG_TASK mode by @SteveCEvans in https://github.com/betaflight/betaflight/pull/13799
* Piecewise linear interpolation routine (for wings) by @limonspb in https://github.com/betaflight/betaflight/pull/13798
* Auto-disarm on landing impact by @ctzsnooze in https://github.com/betaflight/betaflight/pull/13803
* Hyperbolic PID multiplier curve (for wings) by @limonspb in https://github.com/betaflight/betaflight/pull/13805
* Altitude hold for 4.6 by @ctzsnooze in https://github.com/betaflight/betaflight/pull/13816
* Added 'Storage mode' action in Blackbox part of OSD menu by @demvlad in https://github.com/betaflight/betaflight/pull/13899
* Minor CLI update to give a `noreboot` option so `save` and `exit`  by @blckmn in https://github.com/betaflight/betaflight/pull/13904
* Adding CLI command pass through for MSP by @blckmn in https://github.com/betaflight/betaflight/pull/13940
* Update turtle / crashflip mode by @ctzsnooze in https://github.com/betaflight/betaflight/pull/13905
* Log servos in blackbox by @henrywarhurst in https://github.com/betaflight/betaflight/pull/13944
* TPA air speed speed estimation instead of TPA delay (for wings) by @limonspb in https://github.com/betaflight/betaflight/pull/13895
* Yaw type rudder/diff_thrust for TPA calculations (for wings) by @limonspb in https://github.com/betaflight/betaflight/pull/13929
* Add PRBS checking of BB FLASH with USE_FLASH_TEST_PRBS by @SteveCEvans in https://github.com/betaflight/betaflight/pull/13987
* Driver for CADDX camera GM3 gimbal by @SteveCEvans in https://github.com/betaflight/betaflight/pull/13926
* TPA mode PDS + Wing setpoint attenuation (for wings) by @limonspb in https://github.com/betaflight/betaflight/pull/14010
* Collision Detection by @KarateBrot in https://github.com/betaflight/betaflight/pull/13010
* Position hold for 4.6 and Altitude Hold updates by @ctzsnooze in https://github.com/betaflight/betaflight/pull/13975
* PreArm allow Re-Arm (without resetting PreArm AUX) by @nerdCopter in https://github.com/betaflight/betaflight/pull/14013
* LED Dimmer by @jpmreece in https://github.com/betaflight/betaflight/pull/13776
* Chirp signal generator as flight mode by @pichim in https://github.com/betaflight/betaflight/pull/13105
* Added virtual blackbox for SITL by @demvlad in https://github.com/betaflight/betaflight/pull/14325
* hover point throttle curve adjustment by @marc-frank in https://github.com/betaflight/
