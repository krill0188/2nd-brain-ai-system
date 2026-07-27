---
title: "MAVLink Messaging in PX4"
created: 2026-07-27
captured: 2026-07-27
type: article
url: "https://docs.px4.io/main/en/mavlink/"
author: "PX4 Dev Team"
sha256: ""
tags: [drone-sw, datalink]
---

# MAVLink Messaging in PX4

## Overview

MAVLink serves as PX4's communication protocol for exchanging data with ground stations and external components. The protocol emphasizes efficiency, making it suitable for unreliable low-bandwidth radio links.

## Core Concepts

**Messages** form the foundation of MAVLink communication. They consist of a name (like ATTITUDE), an ID, and data fields. These lightweight structures support streaming telemetry or status information without built-in resending or acknowledgement mechanisms.

**Microservices** represent higher-level protocols built atop MAVLink messages. Notable examples include:
- Command Protocol — acknowledged commands using MAV_CMD definitions; automatically resent if no acknowledgment received
- File Transfer Protocol
- Camera Protocol
- Parameter Protocol
- Mission Protocol

## XML Definition Files

MAVLink standardizes definitions through hierarchical XML files:
- **minimal.xml** — Bare essentials
- **standard.xml** — Widely implemented definitions
- **common.xml** — Common UAV use cases (PX4 default)
- **development.xml** — Proposed standards under testing

PX4 builds against `common.xml` by default to ensure the greatest compatibility with MAVLink ground stations, libraries, and external components.

## Security Warning

MAVLink messages are unauthenticated by default. Production systems must implement message signing and follow security hardening guidelines to prevent unauthorized command execution.

## PX4 Implementation

PX4 includes the MAVLink repository as a submodule. The build system generates MAVLink 2 C header files at compile time, with dialect selection configurable per-board through the `CONFIG_MAVLINK_DIALECT` variable.
