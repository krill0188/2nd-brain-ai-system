---
title: "yolo v8.4.178 Release Notes"
created: 2026-10-17
captured: 2026-10-17
type: release-note
tag: v8.4.178
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.178
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.178 Release Notes (2026-10-16)

## 🌟 Summary
Release **v8.4.178** makes Platform training links more reliable and brings a broad set of fixes for model validation, tracking, exports, data loading, and training integrations. It also adds a cross-domain benchmark resource and expands Platform documentation.

## 📊 Key Changes
- **Reliable Platform training links (PR #26699):** Training now prints the model URL returned by the server, which knows the final owner, project, and model name. This avoids broken links when those details differ from the local training arguments; if the server provides no URL, no link is printed.
- **Broader model evaluation:** A new Ultralytics Benchmark page describes a fixed evaluation protocol across 37 real-world detection datasets, spanning areas such as medical imaging, retail, industry, and aerial imagery. The YOLO27 documentation also updates its reported performance figures and links to the benchmark.
- **Model and tracking compatibility:** YOLO-NAS receives fixes for loading by model name, prediction, validation, export, and ReID tracking. FastSAM prompts now persist across later images and video frames; SAM tracking preserves object IDs when masks are blank; and oriented-box tracking handles equivalent box representations more consistently.
- **More dependable validation and exports:** Validation now respects non-square input shapes recorded in static exports. Fixes also address TorchScript loading on Apple MPS, dynamic ONNX execution on MPS, and full-integer LiteRT/TensorFlow input handling.
- **Platform reporting improvements:** Validation curves now better match segmentation and pose results, and class labels stay aligned when validation data omits classes. Confusion-matrix logging is corrected for Comet and DVC, including cases where no matrix is available.
- **Training and workflow reliability:** TensorBoard writers close cleanly after training, FP32 optimizer momentum is retained in checkpoints, Ascend NPU training avoids an unsupported reduction, and Docker publishing skips overwriting tags with images built from newer commits.
- **Platform and documentation updates:** Platform guides document paid annotation and image-generation models, new Explore filters, and AI-assisted training diagnosis. Other fixes improve UTF-8 dataset and source-manifest reading, screenshot inputs, ZIP naming, and CLI error messages.

## 🎯 Purpose & Impact
- **Platform users** get working model links and clearer, more accurate training results.
- **Developers** benefit from more consistent behavior across model families, trackers, export formats, and hardware backends.
- **Teams managing experiments and data** get safer Docker releases, cleaner training teardown, and fewer failures caused by encoding, file naming, or configuration-directory issues.
- **Model evaluators** gain a broader reference for comparing performance beyond COCO; the benchmark results are documentation and evaluation resources, not a new model architecture in this release.

## What's Changed
