---
title: "MAVLink XML File Schema & Format"
created: 2026-07-27
captured: 2026-07-27
type: article
url: "https://mavlink.io/en/guide/xml_schema.html"
author: "MAVLink Dev Team"
sha256: ""
tags: [datalink, drone-sw]
---

# MAVLink XML File Schema / Format

## Core File Structure

```xml
<?xml version="1.0"?>
<mavlink>
    <include>common.xml</include>
    <dialect>8</dialect>
    <enums>...</enums>
    <messages>...</messages>
</mavlink>
```

**Include Tags**: Specify other XML files incorporated into the dialect. Multiple includes supported, nesting up to 5 levels. Generator toolchains merge and append enums from all files.

**Dialect Number**: Unique identifier for the dialect specification.

## Enum Definitions

```xml
<enum name="LANDING_TARGET_TYPE">
    <description>Type of landing target</description>
    <entry value="0" name="LANDING_TARGET_TYPE_LIGHT_BEACON">
        <description>Landing target signaled by light beacon</description>
    </entry>
</enum>
```

**bitmask**: Optional boolean for flag-style enums with power-of-2 values.

## MAVLink Commands (MAV_CMD)

Commands transmit up to 7 numeric parameters. Special attributes:
- **missionOnly**: Boolean — applies only to missions
- **hasLocation**: Displays as standalone location
- **isDestination**: Marks waypoint destinations

Each command has up to 7 `<param>` elements (indices 1-7) with label, units, enum reference, valid ranges.

## Message Definitions

- **id**: Unique index (0-255 for MAVLink 1; 0-16777215 for MAVLink 2)
- **name**: Human-readable identifier

### Field Types
- Signed/unsigned integers (8, 16, 32, 64-bit)
- IEEE754 floating-point (single/double)
- Arrays (e.g., `uint16_t[10]`)

### Field Attributes
- **type**: Data structure size and format
- **enum**: Referenced enumeration
- **units**: SI units
- **instance**: Sensor/battery instance identification
- **invalid**: Marks missing/unavailable data
- **minValue / maxValue / increment**: Validation hints

## Extensions Element

`<extensions />` tag designates MAVLink 2-only fields — preserves backward compatibility. Extensions bypass CRC checks; prefer new messages over extensions when possible.

## Lifecycle Tags

- **WIP**: Work-in-progress, not in release builds
- **Superseded**: Newer alternative exists
- **Deprecated**: Targeted for removal (`removed_by` attribute)
