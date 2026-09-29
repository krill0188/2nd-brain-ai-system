---
title: "yolo v8.4.156 Release Notes"
created: 2026-09-20
captured: 2026-09-20
type: release-note
tag: v8.4.156
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.156
tags: [drone, ai-autonomy, yolo]
sha256: 2b5073b7555e255665acbf10ee45dc61e5ccd72f16182ab1197a99ecf3b8413c
---

# yolo v8.4.156 Release Notes (2026-09-19)

## 🌟 Summary

**v8.4.156 improves remote NDJSON dataset reliability and makes INT8 TensorRT exports faster while preserving accuracy.** 🚀

## 📊 Key Changes

- **🔄 Reliable remote NDJSON conversion — PR #26242 by @cainiao33**
  - Refreshes the remote NDJSON manifest inside the existing conversion lock, preventing stale dataset manifests from being silently reused.
  - Uses a private temporary download directory so similarly named manifests from different URLs cannot overwrite one another.
  - Keeps the normalized content hash as the conversion cache:
    - Unchanged datasets—including those with rotated signed URLs—reuse existing labels and images without unnecessary downloads.
    - Changed manifests generate a new dataset directory, preserving files used by active training jobs.
  - Removes NDJSON-specific deletion behavior from the general `check_file` utility, making file handling more predictable.
  - Validated across detection, classification, depth, local sources, concurrent downloads, interrupted conversions, and URL basename collisions.

- **⚡ Faster and more accurate INT8 TensorRT exports — PR #26171 by @Y-T-G**
  - QAT now quantizes more of the model head while keeping accuracy-sensitive final output layers and DFL operations in floating point.
  - BatchNorm layers are fused during export, prediction, and validation, reducing runtime overhead.
  - Quantization ranges are adjusted when BatchNorm is fused so INT8 values remain effectively unchanged.
  - PTQ exports now keep the most accuracy-sensitive head operations out of INT8 and use FP16 where appropriate.
  - TensorRT precision handling was refined for both newer and older TensorRT versions.

- **🧪 More robust testing — PR #26217 by @glenn-jocher**
  - A restricted-load model test now uses tolerant numerical comparison rather than requiring bit-for-bit identical outputs across all hardware backends.
  - This reduces false failures without weakening validation of model weights, criteria, or fused layers.

- **🛠️ Maintenance and documentation**
  - Updated the self-hosted GitHub Actions cleanup runner from `v1.4.39` to `v1.4.40`.
  - Refreshed the embedded video in the Security Alarm System guide.
  - Updated the export documentation to describe the more precise QAT head behavior.

## 🎯 Purpose & Impact

- **More trustworthy dataset updates:** Remote NDJSON publishers can change manifests without users accidentally training on outdated data. ✅
- **Less unnecessary network and disk usage:** Identical datasets are reused efficiently, even when signed image URLs rotate.
- **Safer ongoing training:** Changed datasets receive separate directories, so existing jobs continue using the files they started with.
- **Improved INT8 deployment performance:** TensorRT engines should export and run more efficiently while retaining accuracy-sensitive operations in higher precision. ⚡
- **Better cross-platform stability:** Testing is less likely to fail because of harmless backend-level numerical diffe
