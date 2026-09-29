---
title: "yolo v8.4.148 Release Notes"
created: 2026-09-12
captured: 2026-09-12
type: release-note
tag: v8.4.148
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.148
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.148 Release Notes (2026-09-11)

## 🌟 Summary

**Ultralytics 8.4.148 makes SAM 3.1 image prediction checkpoints load correctly, enabling reliable point, box, text, and exemplar-based segmentation.** 🎯

## 📊 Key Changes

- **SAM 3.1 checkpoint support** 🧠
  - Added checkpoint-key mapping so `sam3.1_multiplex.pt` works correctly with `SAM` and `SAM3Predictor`.
  - Fixes an issue where SAM 3.1’s prompt encoder, mask decoder, embedding, and neck could be silently initialized with random weights.
  - Existing `sam3.pt` checkpoints remain compatible; the key mapping is effectively a no-op for SAM 3.

- **Supported SAM 3.1 prediction workflows** 🖼️
  - Point and box prompts through `SAM` and `SAM3Predictor`.
  - Text and image-exemplar prompts through `SAM3SemanticPredictor`.
  - SAM 3.1 video tracking with the new Object Multiplex memory architecture is **not yet ported**. Use the original `sam3.pt` with the SAM 3 video predictors for video workflows.

- **Documentation updates** 📚
  - Added SAM 3.1 guidance, supported scope, benchmark comparisons, and gated-weight download instructions.
  - Updated the model index to list `sam3.1_multiplex.pt`.

- **Repository guidance improvements** 🛠️
  - Streamlined the root `AGENTS.md` and moved documentation-specific instructions into a new `docs/AGENTS.md`.
  - Preserved important development, testing, release, and implementation-boundary guidance while reducing duplicated repository walkthroughs.

- **Version update** 📦
  - Bumped the package version from `8.4.147` to `8.4.148`.

## 🎯 Purpose & Impact

- ✅ **Correct segmentation results:** SAM 3.1 image predictors now use the trained checkpoint components instead of silently falling back to randomly initialized prompt-processing layers.
- 🚀 **Easier SAM 3.1 adoption:** Users can load the new checkpoint through the existing Ultralytics SAM interfaces with minimal workflow changes.
- 🔍 **Clearer expectations:** Documentation distinguishes supported SAM 3.1 image prediction from unsupported Object Multiplex video tracking.
- 🔐 **Access requirement:** SAM 3.1 weights remain gated by Meta and must be obtained from the approved [SAM 3.1 model page on Hugging Face](https://huggingface.co/facebook/sam3.1).
- 👩‍💻 **Improved contributor experience:** More focused agent guidance makes repository development instructions easier to discover without changing end-user model behavior.

## What's Changed
* Trim derivable content from AGENTS.md and move docs guidance to docs/AGENTS.md by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26138
* Focus repository guidance and retain scoped agent instructions by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26141
* `ultralytics 8.4.148` Load SAM 3.1 checkpoints into the SAM 3 image predictors by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26144


**Full Changelog**: https://github.com/ultralytics/ultralytics/compare/v8.4.147...v8.4.148
