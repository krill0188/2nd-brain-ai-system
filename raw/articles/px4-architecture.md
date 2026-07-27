---
source_url: "https://docs.px4.io/main/en/concept/architecture.html"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "PX4 Dev Team"
sha256: "5c9h1e4g7f0a3d6e9c2f5a8d1e4f7a9b2c5d8e1f4a7b9c2d5e8f1a4b7c9d2e5"
tags: [drone-sw]
---

# PX4 Architectural Overview

## Introduction

PX4 consists of two main layers: the flight stack (estimation and flight control system) and the middleware (general robotics layer supporting autonomous robots). All PX4 airframes share a single codebase including boats, rovers, and submarines. The system follows reactive design principles with exchangeable components and asynchronous message passing.

## High-Level Software Architecture

The architecture diagram shows middleware blocks at the top and flight stack components below. The codebase is organized into self-contained modules. Runtime inspection is possible using the `top` command in shell to see which modules execute, allowing individual start/stop control.

Modules communicate through a publish-subscribe message bus called uORB. This approach provides:
- Reactive, asynchronous updates when data becomes available
- Full parallelization of operations and communication
- Thread-safe component data consumption

**Key Principle**: Any building block can be rapidly replaced, even during runtime.

## Flight Stack

The flight stack encompasses guidance, navigation, and control algorithms for autonomous drones. It includes:

- **Controllers for airframe types**: fixed-wing, multirotor, VTOL
- **Estimators**: attitude and position computation
- **Sensor processing pipeline**: from sensors and RC input through autonomous flight control to motor/servo control

**Estimators** combine sensor inputs to compute vehicle state (example: attitude from IMU data).

**Controllers** receive setpoints and process variables as inputs, outputting corrections to match desired states (example: position controller adjusts attitude/thrust to reach target position).

**Mixers** translate force commands into individual motor commands while respecting limits, accounting for motor arrangement and rotational inertia.

## Middleware

Middleware primarily includes:
- Device drivers for embedded sensors
- External world communication (companion computer, GCS)
- uORB publish-subscribe message bus
- Simulation layer allowing desktop testing of flight code

## Update Rates

Modules wait for message updates, typically driven by driver update frequencies. Most IMU drivers sample at 1kHz, integrate, and publish at 250Hz. Lower-frequency modules like navigator run considerably slower.

Real-time message rates can be inspected using `uorb top` command.

## Runtime Environment

PX4 runs on POSIX-compliant operating systems (Linux, macOS, NuttX, QuRT) with real-time scheduling support (FIFO). Inter-module communication uses shared memory through uORB, with all middleware running in a single address space.

**Design Note**: The architecture permits running each module in separate address space with minimal modifications to uORB, parameter interface, dataman, and performance monitoring.

## Module Execution Methods

**Tasks**: Modules run independently with their own stack and process priority.

**Work queue tasks**: Modules share a work queue, stack, and thread priority with other queue modules. They must behave cooperatively without interrupting each other. Multiple work queues can exist.

Advantages of work queue tasks: reduced RAM usage, fewer task switches.
Disadvantages: cannot sleep, poll messages, or perform blocking I/O.

**Note**: Work queue tasks don't appear in `top` output; use `work_queue status` instead.

## Background Tasks

Tasks spawn using `px4_task_spawn_cmd()` for NuttX or threads for POSIX systems, running independently from parent tasks. The function accepts process name, scheduling type, priority, stack size, main function, and arguments.

## OS-Specific Information

### NuttX

NuttX (Apache BSD-licensed RTOS) is the primary flight-control board operating system. It's lightweight, efficient, and stable. Modules execute as tasks with separate file descriptor lists but shared address space. Tasks can spawn threads sharing file descriptor lists. Fixed-size stacks are monitored periodically for adequate free space.

### Linux/macOS

PX4 runs as a single process with modules executing as separate threads (no task/thread distinction).

## Key Technical Concepts

- **Reactive Architecture**: Asynchronous, non-blocking communication enabling instant updates when data arrives.
- **Module Communication**: uORB handles all inter-module messaging with publish-subscribe semantics.
- **Stack Depth**: Task execution depth includes sensors → estimators → controllers → mixers → actuators.
- **Priority Levels**: Scheduling allows critical flight control loops to run at higher priorities than non-essential components.
