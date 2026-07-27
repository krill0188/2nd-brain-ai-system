---
source_url: "https://docs.px4.io/main/en/middleware/uorb.html"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "PX4 Dev Team"
sha256: "9g1d8e4f7h0i3j6k9l2m5n8o1p4q7r0s3t6u9v2w5x8y1z4a7b0c3d6e9f2g5h8"
tags: [drone-sw]
---

# uORB Messaging in PX4

## Overview

uORB is an asynchronous publish/subscribe messaging system for inter-thread and inter-process communication in PX4. The system automatically starts early during boot, as many applications depend on it.

## Adding New Topics

New topics are created by adding `.msg` files to the `msg/` directory (or `msg/versioned/` for versioned messages) and listing them in `msg/CMakeLists.txt`. Message definitions follow CamelCase naming convention and automatically generate corresponding C/C++ code.

Topics can be referenced in code by including the generated header (using snake_case) and using the topic ID. For example:

```cpp
#include <uORB/topics/velocity_limits.h>
// Reference: ORB_ID(velocity_limits)
```

## Message Definition Structure

Message definitions require specific elements:

- **Descriptive comment** at the start (lines beginning with `#`)
- **Required field**: `uint64_t timestamp` for logging purposes
- **Versioned messages**: Must include `uint32 MESSAGE_VERSION`
- **Field format**: type, name, and optional descriptive comment

### Advanced Features

**Multi-Topic Messages**: A single definition can create multiple topics using `# TOPICS` syntax with space-separated topic IDs.

**Nested Messages**: Complex structures are created by including other message types within definitions.

**Buffer Configuration**: The `ORB_QUEUE_LENGTH` constant (power of 2) specifies multi-message buffering to prevent message loss at high publication rates.

## Message Versioning

Introduced in PX4 v1.16, versioning maintains compatibility across multiple PX4 and ROS 2 versions. Versioned messages are stored in `msg/versioned/`, with older versions in `msg/px4_msgs_old/` subdirectories.

## Publishing and Subscribing

Publishing can occur from most contexts, including interrupt handlers, but topics must be advertised in non-interrupt context first.

**Multi-instance support**: The `orb_advertise_multi` function creates independent instances of the same topic, allowing multiple sensors of identical type. Subscribers use `orb_subscribe_multi` to target specific instances.

## Monitoring Topics

The `listener` command displays topic content and accepts messages count parameters. The `uorb top` command provides real-time publishing frequency monitoring with metrics including:
- Subscriber counts
- Message frequency
- Lost messages
- Queue sizes
