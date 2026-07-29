---
title: "betaflight 2025.12.5 Release Notes"
created: 2026-07-29
captured: 2026-07-29
type: release-note
tag: 2025.12.5
domain: flight-control
source: https://github.com/betaflight/betaflight/releases/tag/2025.12.5
tags: [drone, flight-control, betaflight]
---

# betaflight 2025.12.5 Release Notes (2026-06-28)

<!-- Release notes generated using configuration in .github/release.yml at 7348054f268f0058574719c134e9f149565bb8ea -->

## What's Changed
### Fixes
* [2025.12] fix(uart): clear ORE when RXNEIE is enabled in HAL uartIrqHandler (fixes #15317, #15306) by @tracycam in https://github.com/betaflight/betaflight/pull/15325
* [2025.12] fix(msp): cancel pendingRequest on '$' only, restoring per-byte lastActivityMs by @nerdCopter in https://github.com/betaflight/betaflight/pull/15324


**Full Changelog**: https://github.com/betaflight/betaflight/compare/2025.12.4...2025.12.5
