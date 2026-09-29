---
title: "yolo v8.4.141 Release Notes"
created: 2026-09-06
captured: 2026-09-06
type: release-note
tag: v8.4.141
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.141
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.141 Release Notes (2026-09-05)

## 🌟 Summary

**Ultralytics 8.4.141 updates Axelera support to Voyager SDK 1.8.0, adds batched inference, and improves model compatibility, dependency management, and CI reliability.** 🚀

## 📊 Key Changes

- **Axelera integration upgraded to Voyager SDK 1.8.0** 🔧
  - Export and inference now use matching `axelera-devkit` and `axelera-rt` 1.8.0 packages.
  - Axelera export environments move to **Python 3.13** and support a wider compatible PyTorch range.
  - Removed the previous NumPy version ceiling and improved SDK version checks before compiler loading.
  - Export now ensures the correct SDK environment tools are available on `PATH` and safely restores environment variables afterward.

- **Batched Axelera inference is now supported** 📦
  - Predictions with `batch>1` are routed through the Voyager scheduler.
  - Outputs are returned in the original input order for both single- and multi-output models.
  - Models are still compiled for a single image, so batching improves workflow compatibility but does not necessarily increase end-to-end speed on one device.

- **Axelera deployment requirements are documented more clearly** 📚
  - Voyager SDK 1.8.0 requires the **Metis kernel driver 1.6.2 or newer**.
  - Models exported with an older SDK must be re-exported because SDK 1.8 uses a newer compiled model format.
  - YOLO26 semantic segmentation is documented as supported, while YOLO26 instance segmentation remains unavailable through the Ultralytics export command.

- **Fixed legacy SPPF model reconstruction** 🛠️
  - Pre-YOLO26 YAML configurations once risked rebuilding `SPPF` layers with the wrong activation behavior.
  - Legacy models now restore their original activation settings, preserving released model graphs and outputs.
  - Regression coverage now checks multiple YOLO configurations, including YOLO8, YOLO10, YOLO11, and YOLO26.

- **OpenVINO dependencies are now opt-in** 📦
  - OpenVINO and NNCF moved from `export-base` to a dedicated `export-openvino` extra.
  - The aggregate `export` extra still includes OpenVINO support.
  - This reduces unnecessary installations for users who only need the common export stack.

- **Conda CI dependency resolution improved** ⚡
  - CI now uses only `conda-forge` with strict channel priority and removes inherited default channels.
  - Installation is noninteractive and has a 20-minute timeout, preventing stalled dependency solves from consuming the full job.

## 🎯 Purpose & Impact

- **Axelera users** can use the latest SDK, run inference on image batches, and benefit from more reliable automatic dependency handling. Existing Axelera models may need to be re-exported after upgrading. ⚠️
- **Deployment compatibility** is improved, but users must keep the Metis driver aligned with Voyager SDK 1.8.0.
- **Legacy Ultralytics models** are safer to rebuild from YAML without silently changing SPPF behavior.
- **General installations** become lighter when OpenVINO is not required, while OpenVINO export remains availab
