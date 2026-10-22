---
title: "yolo v8.4.182 Release Notes"
created: 2026-10-20
captured: 2026-10-20
type: release-note
tag: v8.4.182
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.182
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.182 Release Notes (2026-10-18)

## 🌟 Summary
YOLO 8.4.182 strengthens dataset label checks to catch invalid bounding boxes before they break validation plotting, and improves Linux drive reporting.

## 📊 Key Changes
- **Rejects negative box widths and heights:** Label verification now flags boxes with negative dimensions, while preserving the existing coordinate tolerance and allowing zero-size boxes.
- **Refreshes dataset caches:** The cache version is bumped so existing dataset caches are rescanned using the updated checks.
- **Reports Linux drives without duplicate mounts:** System logging now selects one mount per block device, avoiding duplicate entries caused by bind mounts.
- **Package version:** Updated to 8.4.182.

## 🎯 Purpose & Impact
- 🧹 Invalid labels are caught earlier, preventing errors when validation tries to draw inverted boxes.
- 🔄 Existing datasets are rechecked automatically through the cache version change.
- 📊 Linux system reports show a clearer, more accurate list of drives—especially on systems with multiple mounts of the same device.

## What's Changed
* Report each Linux block device once in `SystemLogger` drive discovery by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26746
* Reject negative box dimensions during label verification by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26748


**Full Changelog**: https://github.com/ultralytics/ultralytics/compare/v8.4.181...v8.4.182
