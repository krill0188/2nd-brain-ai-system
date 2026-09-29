---
title: "yolo v8.4.160 Release Notes"
created: 2026-09-23
captured: 2026-09-23
type: release-note
tag: v8.4.160
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.160
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.160 Release Notes (2026-09-22)

## 🌟 Summary
**Ultralytics 8.4.160 makes dataset edits less likely to go unnoticed and improves memory use, training reliability, and everyday API behavior—without introducing a new model architecture.**

## 📊 Key Changes
- **Dataset cache invalidation (PR #26283):** Cache keys now account for each file’s size and modification time, so editing a label in place—such as changing its class without changing its length—triggers a rescan. Detection, depth, semantic, and other shared-cache users benefit.
- **Lower peak VRAM for SAM3 text prompting:** Text prompts are processed in chunks of up to 16, helping reduce memory use on large prompt sets and avoid out-of-memory errors.
- **More reliable training after out-of-memory errors:** When training retries with a smaller batch size, it now preserves optimizer and scheduler state instead of restarting optimizer state.
- **Clearer validation dataset selection:** Validation uses the checkpoint’s recorded dataset when it can be found; otherwise, it warns and falls back to the task’s default dataset. Users can specify `data` to choose a dataset explicitly. Depth calibration now requires `data`.
- **Lower host RAM during TensorRT 11 INT8 calibration:** Calibration releases consumed batch data and normalizes in place, reducing peak host memory without changing calibration values.
- **Safer and more convenient utilities:** CUDA-backed results can now convert to NumPy; NMS no longer modifies raw prediction tensors; and box-cropping, image-to-label path conversion, and repeated downloads of single-file ZIPs handle common inputs more reliably.
- **Documentation improvements:** Task guides clarify validation behavior, result fields, dataset formats, and training options, including cloud training.

## 🎯 Purpose & Impact
- **More trustworthy dataset updates:** Changed labels are less likely to remain silently stale in cached datasets. Existing caches will rescan once after upgrading; if a file’s size *and* modification time are both preserved, remove the affected cache manually.
- **Better usability across hardware and workflows:** SAM3 can handle more text prompts within available GPU memory, while TensorRT 11 calibration can use less host RAM.
- **More dependable training and inference:** OOM retries retain learned optimizer state, and repeated NMS calls no longer risk corrupting the original predictions.
- **Fewer surprising API failures:** CUDA results and common Python path or box inputs work more consistently.
- **Less ambiguity in validation:** Checkpoint dataset settings are reused when available, with a warning and sensible fallback when they are not.

## What's Changed
* Add https://youtu.be/VxP9kHUwE6o to docs by @RizwanMunawar in https://github.com/ultralytics/ultralytics/pull/26274
* Reduce peak VRAM for SAM3 text prompting via chunked grounding by @Laughing-q in https://github.com/ultralytics/ultralytics/pull/26281
* Validate on the checkpoint's dataset when val gets no data and require data= in calibrate
