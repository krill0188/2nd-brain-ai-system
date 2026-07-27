---
title: "PX4 Flight Modes — Developer Reference"
created: 2026-07-27
captured: 2026-07-27
type: article
url: "https://docs.px4.io/main/en/concept/flight_modes.html"
author: "PX4 Dev Team"
sha256: ""
tags: [drone-sw]
---

# Flight Modes (Developers)

Modes represent specialized operational states that dictate how the autopilot responds to user commands and manages vehicle movement. These modes fall into three general categories: manual, assisted, and autonomous, reflecting the degree of autopilot intervention. Pilots switch between modes using remote control switches or ground control station commands.

Implementation can occur through either PX4 internal modes on the flight controller or PX4 external (ROS2) modes operating on companion computers. From a ground station perspective using MAVLink, the mode origin remains indistinguishable.

## Supported Modes

Different vehicle types support different mode sets:
- Flight Modes (Multicopter)
- Flight Modes (Fixed-Wing)
- Flight Modes (VTOL)
- Drive Modes (Rover)

## Internal vs External Modes

PX4 external modes cannot be used when:
- Operating vehicles without companion computers
- Requiring low-level access, strict timing, and high update rates (e.g. multicopter direct motor control)
- Implementing safety-critical functionality like Return mode
- Unable to utilize ROS for any reason

External modes advantages:
- Simpler implementation without embedded system constraints
- Easier maintenance through well-defined, stable integration APIs
- Better portability across PX4 versions
- Automatic fallback to internal modes if the ROS 2 mode terminates
- Capability to override existing modes with enhanced versions
- Access to high-level programming environments and Linux libraries

The PX4 ROS 2 Control Interface (introduced in v1.15) remains experimental.

## Mode Restrictions

PX4 modes specify conditions through restrictions defined in the `FailsafeFlags` uORB topic under "Per mode requirements":

- `mode_req_angular_velocity`
- `mode_req_attitude`
- `mode_req_local_alt`
- `mode_req_local_position`
- `mode_req_local_position_relaxed`
- `mode_req_global_position`
- `mode_req_mission`
- `mode_req_offboard_signal`
- `mode_req_home_position`
- `mode_req_wind_and_flight_time_compliance`
- `mode_req_prevent_arming`
- `mode_req_manual_control`
- `mode_req_other`

Mode requirements are configured in `getModeRequirements()` within `src/modules/commander/ModeUtil/mode_requirements.cpp`.

## MAVLink Integration

PX4 implements the MAVLink Standard Modes Protocol beginning with v1.15, enabling mode discovery, current mode identification, and mode selection.
