---
title: "yolo v8.4.170 Release Notes"
created: 2026-10-01
captured: 2026-10-01
type: release-note
tag: v8.4.170
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.170
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.170 Release Notes (2026-09-30)

## 🌟 Summary
**Ultralytics 8.4.170 restores the established disk-cache naming, so existing caches are reused instead of rebuilt.** It also documents video frame skipping for Platform inference.

## 📊 Key Changes
- 💾 **Reverted the disk-cache filename change:** Detection and classification datasets again save cache files as `image.npy`, rather than `image.jpg.npy`.
- 🎥 **Documented `vid_stride` for Platform inference:** The parameter controls how often video frames are processed; its default of `1` processes every frame, and images are unaffected.
- 📖 **Updated video-response docs:** They now clarify that results are returned for each *processed* frame.

## 🎯 Purpose & Impact
- ✅ Users with existing `cache=disk` datasets can reuse their original cache files without rebuilding a second copy, saving time and disk space.
- ⚠️ This restores compatibility but gives up the previous change’s handling of same-named images with different extensions in one folder. For detection datasets, those images also share a label file, limiting the practical benefit of separate cache names.
- 🚀 Platform users can use `vid_stride` to process fewer video frames when the API supports it, potentially reducing inference work. **No model architecture changes are included.**

## What's Changed
* Avoid disk cache collisions for same-stem images by @aswanth-07 in https://github.com/ultralytics/ultralytics/pull/26457
* Document vid_stride for Platform predict by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26458
* ultralytics 8.4.170 Revert disk cache naming from #26457 by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26460


**Full Changelog**: https://github.com/ultralytics/ultralytics/compare/v8.4.169...v8.4.170
