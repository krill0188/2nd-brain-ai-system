---
source_url: "https://docs.px4.io/main/en/flight_modes/"
ingested: 2026-07-27
sha256: "$(cat ~/2nd/inbox/test-px4-flight-modes.md | tail -n +7 | sha256sum | cut -d' ' -f1)"
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
