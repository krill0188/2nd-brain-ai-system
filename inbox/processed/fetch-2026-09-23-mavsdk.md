---
title: "mavsdk v4.0.0 Release Notes"
created: 2026-09-23
captured: 2026-09-23
type: release-note
tag: v4.0.0
domain: comms-protocol
source: https://github.com/mavlink/MAVSDK/releases/tag/v4.0.0
tags: [drone, comms-protocol, mavsdk]
---

# mavsdk v4.0.0 Release Notes (2026-09-22)

## Overview

- Some [C++ API changes](https://mavsdk.mavlink.io/v4/en/cpp/api_changes.html)
- Stabilized [MavlinkDirect and MavlinkDirectServer plugins](https://mavsdk.mavlink.io/v4/en/cpp/guide/mavlink_direct.html)
- New Python bindings, see [how to migrate from MAVSDK-Python](https://mavsdk.mavlink.io/v4/en/python/migration.html).
- New C bindings
- New Kotlin bindings

Thanks to @JonasVautherin for the work on the Python, C, and Kotlin bindings.


## What's Changed

* Move to cpp folder by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2763
* Docs: Update broken links and .gitignore for new docs location by @JoC2000 in https://github.com/mavlink/MAVSDK/pull/2765
* core: add set_callback_executor API for custom callback dispatch by @julianoes in https://github.com/mavlink/MAVSDK/pull/2769
* Fix: empty mission now return empty by @jazzvaz in https://github.com/mavlink/MAVSDK/pull/2770
* Shell scripts cleanup by @JoC2000 in https://github.com/mavlink/MAVSDK/pull/2768
* examples: add speed feedback to logfile_download by @julianoes in https://github.com/mavlink/MAVSDK/pull/2772
* Fix: setting current mission item by @jazzvaz in https://github.com/mavlink/MAVSDK/pull/2771
* Add C wrapper to MAVSDK-C++ by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2767
* docs: updates regarding cpp directory by @julianoes in https://github.com/mavlink/MAVSDK/pull/2774
* Add mavsdk server docker with compose by @jazzvaz in https://github.com/mavlink/MAVSDK/pull/2773
* Add devcontainer by @jazzvaz in https://github.com/mavlink/MAVSDK/pull/2775
* ci: remove coverage check by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2780
* build(deps): bump rollup from 4.32.1 to 4.59.0 in /cpp/docs by @dependabot[bot] in https://github.com/mavlink/MAVSDK/pull/2778
* Fix MAVSDK destructor by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2776
* Run proto check for C wrappers, too by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2779
* c: unsubscribe properly before destroy by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2777
* ci: build cmavsdk with musl by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2781
* ci: add manylinux jobs by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2784
* c: add an option to bundle static runtime (for manylinux builds) by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2786
* ci: remove manylinux2014-aarch64 workaround after fix upstream by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2785
* Add pymavsdk by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2787
* fix: docker compose dockerfile path by @kristiyanpd in https://github.com/mavlink/MAVSDK/pull/2788
* core: Fix data race in mission transfer WorkItem dtor by @julianoes in https://github.com/mavlink/MAVSDK/pull/2792
* c: improve cmake install by @JonasVautherin in https://github.com/mavlink/MAVSDK/pull/2798
* ci: build wheel for 
