---
source_url: "https://ardupilot.org/dev/docs/learning-ardupilot-introduction.html"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "ArduPilot Dev Team"
sha256: "2a7f9c4e8d2b5a7f3c6e9d4b8a2f5c7e1d9a6b3f8c4e7d2a5b9f6c3d8e4a7b2"
tags: [drone-sw]
---

# Learning ArduPilot — Introduction

## Basic Structure

ArduPilot's architecture comprises five primary components:

1. **Vehicle code** — Top-level firmware directories defining behavior per vehicle type
2. **Shared libraries** — Sensor drivers, EKF estimation, PID controllers (shared across all vehicle types)
3. **Hardware abstraction layer (AP_HAL)** — Enables portability across platforms
4. **Tools directories** — Autotest infrastructure, log replay utilities
5. **External support code** — Git submodules (ChibiOS, DroneCAN, MAVLink)

## Vehicle Types

Six vehicle types: Plane, Copter, Rover, Sub, Blimp, AntennaTracker. Each directory contains C++ files and a wscript file listing library dependencies.

## Libraries

Shared across all vehicles:
- Sensor drivers
- Attitude and position estimation (EKF — Extended Kalman Filter)
- Control code including PID controllers

## AP_HAL (Hardware Abstraction Layer)

Platform-specific implementations:
- `AP_HAL_ChibiOS` — STM32-based boards
- `AP_HAL_ESP32` — ESP32 boards
- `AP_HAL_Linux` — Linux platforms

## External Support Code (Git Submodules)

- **ChibiOS** — RTOS for STM32-based boards
- **DroneCAN** — CANBUS protocol implementation
- **MAVLink** — Protocol and code generator

## Comparison with PX4

| | ArduPilot | PX4 |
|---|---|---|
| Architecture | HAL-based, vehicle-specific code | uORB pub/sub, unified codebase |
| RTOS | ChibiOS (STM32), NuttX alternative | NuttX (primary) |
| Code language | C++ | C++ |
| Community | Large, broad vehicle support | Dronecode ecosystem focus |
| ROS integration | MAVROS/ROS2 via MAVLink | Native uXRCE-DDS / ROS2 |
