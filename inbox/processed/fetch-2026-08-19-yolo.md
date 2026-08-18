---
title: "yolo v8.4.121 Release Notes"
created: 2026-08-19
captured: 2026-08-19
type: release-note
tag: v8.4.121
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.121
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.121 Release Notes (2026-08-17)

## 🌟 Summary

**v8.4.121 improves OpenVINO INT8 export reliability for YOLO26 models while delivering broad Platform API, dataset, annotation, deployment, and documentation updates.** 🚀

## 📊 Key Changes

- **Fixed OpenVINO INT8 detection-head handling** by @glenn-jocher:
  - Replaced fragile PyTorch-based layer matching with exact names from the converted OpenVINO graph.
  - Keeps Detect decoding, DFL, and Sigmoid operations in floating point as intended.
  - Preserves strict NNCF validation during quantization.
  - Verified with a successful YOLO26n-P2 INT8 export using **55 exact ignored operations**, with no unwanted `FakeQuantize` nodes. ✅
  - This directly addresses export failures reported in Sentry and is the most important change in this release.

- **Expanded Ultralytics Platform API documentation**:
  - Documented the generated `ultralytics-platform` Python SDK alongside REST examples.
  - Updated endpoint paths, authentication, pagination, rate limits, response formats, and OpenAPI guidance.
  - Added coverage for images, dataset ingestion, exports, storage integrations, billing, usage, trash, training, deployments, and account APIs.
  - Clarified that workspace API keys have owner-level permissions and are managed by workspace owners.

- **Improved Platform dataset and annotation workflows** 🏷️:
  - Added clearer documentation for URL, cloud-storage, and On Premise dataset imports.
  - Documented class merging/deletion, conflict handling, dataset readiness checks, clustering, version restore, and expanded annotation controls.
  - Added support documentation for COCO and NDJSON imports, while clarifying that Pascal VOC XML labels are not imported.
  - Documented annotation visibility controls, copy/paste workflows, and new keyboard shortcuts.

- **Updated Platform account, billing, and team documentation** 💳:
  - Added the Usage tab, detailed credit metering, monthly credit expiration, auto top-up behavior, seat billing, renewals, and downgrade effects.
  - Clarified workspace roles, owner-only API keys, team invitations, seat reuse, ownership transfer, and team deletion.
  - Expanded activity exports, trash permissions, storage usage, and account deletion guidance.

- **Improved deployment and inference documentation** 🌐:
  - Clarified dedicated endpoint lifecycle operations, authentication, rate limits, model replacement, health checks, metrics, logs, and capacity behavior.
  - Documented video inference, endpoint-specific API references, depth response options, and generated deployment URLs.

- **Security and CI improvements** 🔒:
  - Prevented checkout credentials from being copied into Docker images.
  - Moved workflow secrets into environment variables instead of embedding them in scripts.
  - Updated self-hosted runner cleanup actions to v1.4.39.
  - Reduced individual SlowTests attempts from 180 to 120 minutes while retaining one retry.
  - Changed Dependabot GitHub Actions checks from daily to weekly.

- **Dependency and docum
