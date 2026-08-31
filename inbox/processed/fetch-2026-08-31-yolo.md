---
title: "yolo v8.4.136 Release Notes"
created: 2026-08-31
captured: 2026-08-31
type: release-note
tag: v8.4.136
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.136
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.136 Release Notes (2026-08-31)

## 🌟 Summary

Version **8.4.136** improves hyperparameter tuning, inference performance, backend compatibility, and data handling—making YOLO workflows more reliable and efficient. 🚀

## 📊 Key Changes

- **🎯 Smarter hyperparameter tuning — Current PR #25996 by @glenn-jocher**
  - Keeps the existing Gaussian search behavior unchanged during the first 30 completed trials.
  - Learns relationships between promising hyperparameters by analyzing the best-performing results.
  - Uses confidence-weighted, correlated mutations only when enough elite trial data is available.
  - Reflects correlated proposals at search boundaries to avoid repeatedly clipping values.
  - Benchmarking on basketball-hoop detection reported a new best fitness of **0.60576**, outperforming the tested Ray Tune and previous custom Tuner configurations.
  - Updated the [hyperparameter tuning documentation](https://docs.ultralytics.com/guides/hyperparameter-tuning.md).

- **🧠 More robust channels-last inference**
  - `AutoBackend` now owns memory-layout selection during backend construction, avoiding duplicated or unsafe conversions.
  - Automatic channels-last selection is available for supported Linux and Windows x86 CPU environments using PyTorch 1.13 or newer with oneDNN.
  - CUDA support remains available, while ARM64, MPS, older PyTorch versions, and exported backends retain their existing behavior.
  - Fixed compatibility issues affecting PyTorch 1.9 and JetPack 6 systems.

- **⚡ Faster image preprocessing**
  - PIL and NumPy image inputs now use more efficient OpenCV color conversions.
  - Avoids unnecessary image copies while preserving correct channel order and contiguous memory layout.

- **🔍 More reliable prediction filtering**
  - Fixed the CLI `classes` filter for YOLOE and World models when class IDs are supplied numerically.
  - Text-based class prompts continue to work as before.

- **📷 Improved image and visualization handling**
  - TIFF loading now respects uppercase extensions and grayscale flags, preserving multispectral image channels correctly.
  - Pose visualization now scales keypoint coordinates without incorrectly scaling confidence values.
  - Matplotlib backend restoration is safer when the originally configured backend is unavailable.

- **🏃 Tracking and distributed tuning improvements**
  - BoT-SORT sparse optical-flow tracking avoids an unnecessary per-pixel grid allocation, reducing overhead on large frames.
  - MongoDB-based distributed tuning now assigns iteration IDs atomically, preventing duplicate trial numbers from concurrent workers.

- **🧪 Better validation and project maintenance**
  - Dataset YAML files now receive early type validation with clearer error messages.
  - Added CI and PyPI publishing status for the [Ultralytics SDK repository](https://github.com/ultralytics/sdk).
  - Updated the package version to **8.4.136**.

## 🎯 Purpose & Impact

- **Better tuning results:** The Tuner can discover useful relationships between hyperparamet
