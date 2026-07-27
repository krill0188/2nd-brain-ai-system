---
source_url: "https://docs.px4.io/main/en/dronecan/"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "PX4 Dev Team"
sha256: "9c4d8e2f5a7b3c6d1e9f4a8b2c5d7e1f6a3b9c4d8e2f5a7b3c6d1e9f4a8b2c5"
tags: [drone-hw, drone-sw, datalink]
---

# DroneCAN: Open Protocol for Vehicle Communication

## Overview

DroneCAN is an open-source CAN bus communication protocol enabling flight controllers and peripherals to interconnect. Previously known as UAVCAN v0, rebranded in 2022.

## Key Benefits

- Large hardware ecosystem (sensors, actuators, ESCs)
- CAN bus: robust communication over substantial cable distances
- Bidirectional messaging → health monitoring and diagnostics
- Single-bus architecture for ESCs and peripherals (simplified wiring)
- Centralized firmware updates and device configuration via PX4
- Automatic device metadata tracking for fleet management

## Supported Hardware Categories

| Category | Examples |
|---|---|
| ESCs & Motor Controllers | Various DroneCAN variants |
| GNSS Receivers | ARK, CUAV, Holybro, RaccoonLab, Zubax |
| Power Monitoring | Battery monitors with CAN interface |
| Sensors | Magnetometers, airspeed, rangefinders, optical flow, barometers |

## Configuration

### Enabling DroneCAN

Parameter: `UAVCAN_ENABLE` (values 0-3, recommend 2 or 3 for dynamic node allocation)

### Message Subscriptions

- `UAVCAN_SUB_*` — Inbound subscriptions (e.g., `UAVCAN_SUB_GPS`, `UAVCAN_SUB_FLOW`)
- `UAVCAN_PUB_*` — Outbound publications

Controlling subscriptions prevents unnecessary bus congestion.

### Firmware Updates

PX4 identifies valid firmware binaries (`.bin`) by checking for an APDescriptor (board ID + version metadata). Place firmware files in SD card directory (`/fs/microsd/` or `/fs/microsd/ufw_staging/`) before boot.

## Troubleshooting

| Symptom | Solution |
|---|---|
| Device not detected | Verify `UAVCAN_ENABLE` setting |
| DNA server non-functional | Requires SD card |
| Motor control problems | Set `UAVCAN_ENABLE=3` + configure `UAVCAN_ESC_IFACE` |
