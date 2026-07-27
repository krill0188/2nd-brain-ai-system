---
title: "PX4 Basic Concepts"
created: 2026-07-27
captured: 2026-07-27
type: article
url: "https://docs.px4.io/main/en/getting_started/px4_basic_concepts.html"
author: "PX4 Dev Team"
sha256: ""
tags: [drone, drone-sw]
---

# Basic Concepts - PX4 Guide

## Overview

This article introduces fundamental drone and PX4 autopilot concepts for users new to unmanned vehicles.

## What is a Drone?

A drone, or Unmanned Vehicle (UV), is an unmanned robotic vehicle controllable manually or autonomously. These systems operate across multiple environments—air, ground, water surfaces, and underwater—serving applications including aerial photography, cargo transport, racing, search operations, and surveying.

The broader term "Unmanned Aerial System (UAS)" encompasses a UAV plus all supporting components: ground control stations, radio controllers, and data processing systems.

## Drone Types

**Multicopters**: Provide precision hovering and vertical takeoff but have limited flight duration. They're popular due to ease of assembly and user-friendly operation.

**Helicopters**: Offer similar benefits to multicopters with greater mechanical efficiency, though they're significantly harder to fly.

**Fixed-wing Aircraft**: Enable longer, faster flights suitable for ground surveys but require more complex landing procedures and cannot hover effectively.

**VTOL (Vertical Takeoff and Landing)**: Hybrid systems combining multicopter hovering with fixed-wing forward flight efficiency, available in tiltrotor, tailsitter, and quadplane configurations.

**Airships/Balloons**: Lighter-than-air vehicles providing high-altitude, extended-duration flight with limited directional control.

**Rovers**: Ground-based vehicles offering simple control and higher payload capacity.

**Boats and Submersibles**: Water-based platforms for surface and underwater operations.

## Autopilots

The drone's "brain"—the autopilot—consists of flight stack software running on real-time operating systems (RTOS) on flight controller hardware. This system provides stabilization, safety features, and pilot assistance for manual and autonomous operations.

Modern autopilots increasingly integrate general-purpose computing alongside flight control functions.

## PX4 Flight Stack

PX4 is an open-source autopilot flight stack running on NuttX RTOS. Key capabilities include:

- Support for multicopters, fixed-wing, VTOLs, ground vehicles, and underwater platforms
- Extensive component compatibility options
- Flexible flight modes and robust safety features
- Deep integration with companion computers and robotics APIs including ROS 2 and MAVSDK

PX4 operates within the broader Dronecode ecosystem alongside QGroundControl, Pixhawk hardware, and MAVSDK.

## Ground Control Stations (GCS)

### QGroundControl

The Dronecode GCS software, QGroundControl, runs on Windows, Android, macOS, or Linux. It provides real-time telemetry monitoring, vehicle control, mission planning, geofencing, and firmware installation capabilities via bidirectional telemetry radio links.

### Auterion Mission Control (AMC)

A pilot-focused GCS optimized for flight operations rather than configuration tasks, compatible with both Auterion and standard PX4 systems.

## Drone Components & Parts

### Flight Controller

Flight controllers are dedicated hardware platforms running PX4 firmware, connected to sensors for state determination and actuators for vehicle control. Options range from Pixhawk Series controllers to Linux computers, with selection depending on physical constraints and mission requirements.

### Sensors

PX4 minimally requires gyroscope, accelerometer, magnetometer, and barometer—typically integrated into Pixhawk boards. Recommended additional sensors include:

- **GNSS/GPS**: Required for autonomous modes
- **Airspeed Sensors**: Highly recommended for fixed-wing and VTOL vehicles
- **Distance Sensors**: Enable smoother landings and terrain following
- **Optical Flow Sensors**: Support GNSS-denied navigation

### Outputs: Motors, Servos, Actuators

Outputs control motor speed through ESCs, flight surfaces, camera triggers, parachutes, and grippers. They connect via PWM ports or DroneCAN nodes.

Flight controllers feature `MAIN` and `AUX` output ports (typically 6-8 each). Output-to-function assignments occur in QGroundControl's actuator configuration interface.

### ESCs & Motors

Brushless motors are controlled via Electronic Speed Controllers (ESCs), which convert flight controller signals into appropriate motor power levels.

### Battery/Power

Lithium-Polymer (LiPo) batteries power most PX4 drones, connected through Power Modules or Power Management Boards that distribute power to flight controllers and ESCs separately.

### Manual Control

Pilots operate vehicles via RC (Radio Control) systems or joystick controllers connected through QGroundControl. RC systems use dedicated ground-based transmitters for low-latency control, while joystick systems encode commands through telemetry channels—appropriate for most non-racing applications.

### Safety Switch

Safety switches prevent arming until manually engaged, typically integrated into GPS modules alongside buzzers and LEDs. They're optional but recommended for accident prevention.

### Buzzer

Integrated into GPS modules, the buzzer provides audible vehicle-state notifications. Disabling occurs through the CBRK_BUZZER parameter.

### LEDs

Superbright UI RGB LEDs indicate flight readiness. Modern implementations place these on GPS modules connected via I2C rather than flight controller boards.

### Data/Telemetry Radios

Telemetry radios establish wireless MAVLink connections between ground stations and vehicles, enabling parameter tuning, real-time telemetry inspection, and mission modifications during flight.

### Offboard/Companion Computer

Companion computers—separate on-vehicle systems running Linux—communicate with PX4 for higher-level command and control. They're connected via serial, Ethernet, or WiFi and typically communicate through MAVSDK or ROS 2.

### SD Cards

SD cards store flight logs and are required for UAVCAN peripheral support and mission execution. Maximum supported capacity is 32GB. Cards are optional but recommended; systems without cards can stream logs to companion computers or store missions in RAM/FLASH.

## Payloads

Payloads accomplish mission objectives—cameras for surveying, inspection instruments, or cargo. PX4 supports numerous cameras and payload types, triggered automatically during missions or manually via RC controller, joystick, or ground station commands.

## Arming and Disarming

Arming powers motors and actuators; disarming removes all power. Vehicles default to disarmed states for safety. Arming typically requires RC stick gestures (bottom-right for one second on Mode 2 transmitters) or alternative methods like switch activation or MAVLink commands.

Safety mechanisms prevent arming if:
- Vehicle health status is poor
- Safety switch remains unengaged
- VTOL vehicles remain in fixed-wing mode
- Optional arming pre-conditions fail (low battery, etc.)

Automatic disarming occurs when vehicles don't take off quickly enough or shortly after landing.

## Flight Modes

**Autonomous modes** execute entirely under autopilot control for tasks like takeoff, landing, mission execution, and GPS beacon following.

**Manual modes** require pilot input via RC controls or joysticks, with varying levels of autopilot assistance. Some modes prevent flipping; others enable acrobatic maneuvers.

## Safety Settings (Failsafe)

Configurable failsafe systems protect vehicles through area restrictions and automated responses. Failsafe triggers include:

- Low battery conditions
- Remote control loss
- Position estimate degradation
- Offboard connection loss
- Ground station telemetry loss
- Geofence boundary violations
