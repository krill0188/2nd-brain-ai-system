---
title: "PX4 Flight Modes Overview"
source_url: "https://docs.px4.io/main/en/flight_modes/"
captured: 2026-07-27
tags: [drone-sw, PX4]
---

# PX4 Flight Modes

PX4 supports multiple flight modes that provide different levels of autopilot support.

## Manual Modes
- **Manual/Stabilized**: Pilot controls roll/pitch directly. Autopilot stabilizes attitude.
- **Acro**: Full manual rate control. No stabilization.

## Assisted Modes
- **Altitude Control**: Autopilot maintains altitude. Pilot controls roll/pitch/yaw.
- **Position Control**: GPS-based position hold. Easiest to fly.

## Auto Modes
- **Mission**: Executes pre-planned waypoint mission.
- **Return to Launch (RTL)**: Automatically returns to home position.
- **Hold**: Holds current GPS position and altitude.

## Key Parameters
- `COM_RC_LOSS_T`: RC signal loss timeout
- `NAV_RCL_ACT`: RC loss failsafe action
- `MPC_XY_VEL_MAX`: Maximum horizontal velocity in position mode
