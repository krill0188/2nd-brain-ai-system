---
source_url: "https://docs.px4.io/main/en/concept/px4_systems_architecture.html"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "PX4 Dev Team"
sha256: "7a8f3c2d1e5b9a6f4c8d2e1b5a9f6c3d7e8b2a4f5c9d1e6b3a8f4c7d2e5b9a6f"
tags: [drone-sw, drone]
---

# PX4 System Architecture

## Overview

PX4 provides a comprehensive autopilot system for unmanned aerial vehicles with two primary system configurations: flight controller-only and flight controller combined with companion computer.

## Flight Controller System

A basic PX4 system centers on a flight controller running the PX4 flight stack.

Hardware components:
- **Flight Controller**: Contains internal sensors (IMUs, compass, barometer)
- **Motor Control**: ESCs connected via PWM, DroneCAN, or other interfaces
- **Sensors**: GPS, compass, distance sensors, optical flow, ADSB transponders
- **Payloads**: Cameras and other equipment
- **Communication**: Telemetry radios for ground station connectivity
- **Input**: RC control systems for manual operation

Software stack: drivers, communication modules, controllers, estimators, middleware + QGroundControl GCS.

## Flight Controller + Companion Computer

Advanced systems pair the flight controller with a companion computer (mission computer) connected via serial or IP links using MAVLink protocol.

**Capabilities**: Companion computer typically runs Linux, providing superior development platforms for computer vision, communications, and cloud integration compared to NuttX OS on the flight controller.

**Communication Flow**: Ground stations and cloud services often route through the companion computer, sometimes using MAVLink Router technology.

**Division of Responsibilities**:
- Flight controller: core flight operations, real-time control loops
- Companion computer: advanced autonomous features, processing-intensive tasks (computer vision, SLAM, etc.)

This modular approach allows developers to leverage existing Linux software ecosystems while maintaining reliable flight control operations.
