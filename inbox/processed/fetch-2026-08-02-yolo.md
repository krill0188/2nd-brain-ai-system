---
title: "yolo v8.4.115 Release Notes"
created: 2026-08-02
captured: 2026-08-02
type: release-note
tag: v8.4.115
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.115
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.115 Release Notes (2026-08-01)

## 🌟 Summary

**v8.4.115 transitions Ultralytics from legacy HUB integrations to the streamlined [Ultralytics Platform](https://platform.ultralytics.com/) experience, with simpler authentication and a leaner training codebase.** 🚀

## 📊 Key Changes

- 🔐 **Introduced validated Platform CLI authentication**
  - Log in with `yolo login API_KEY`
  - Remove credentials with `yolo logout`
  - API keys are checked against the Platform before being saved.

- 🔄 **Added settings migration to schema `0.0.7`**
  - Existing compatible settings, such as custom dataset and run directories, are preserved.
  - Legacy HUB configuration and incompatible HUB API keys are removed automatically.
  - Users with old credentials are directed to create a Platform API key.

- 🧹 **Removed the legacy `ultralytics.hub` package**
  - HUB authentication, remote training sessions, model loading, exports, dataset utilities, callbacks, and HUB-specific exceptions have been retired.
  - HUB-related API references, documentation pages, navigation entries, and the HUB example notebook were also removed.

- 🧠 **Simplified model and trainer workflows**
  - Models no longer load directly from HUB URLs.
  - Training no longer manages HUB sessions, remote checkpoints, heartbeats, or HUB-specific training arguments.
  - Platform callbacks remain available for streaming training information.

- 📚 **Updated documentation and examples**
  - Guides, notebooks, CLI help, and API documentation now reference the [Ultralytics Platform](https://platform.ultralytics.com/) instead of HUB.
  - Platform authentication and login commands are included in the quickstart and CLI documentation.

- ✅ **Expanded test coverage**
  - Added tests for settings migration, API-key validation, login, and logout behavior.

## 🎯 Purpose & Impact

- ✨ **A clearer user experience:** Platform is now the primary destination for dataset management, training, and deployment, avoiding confusion between HUB and Platform services.
- ⚡ **Simpler authentication:** The new `yolo login` command validates credentials directly and provides a more intuitive alternative to manually editing settings.
- 🛠️ **Cleaner and easier-to-maintain code:** Removing obsolete HUB components reduces dependencies, integration complexity, and potential maintenance issues.
- 🔒 **Safer upgrades:** Existing user settings are migrated instead of being reset, while outdated or incompatible HUB keys are discarded.
- ⚠️ **Compatibility consideration:** Applications that import `ultralytics.hub`, use HUB training sessions, load models from HUB URLs, or rely on HUB-specific utilities must migrate to [Ultralytics Platform](https://platform.ultralytics.com/) workflows.
- 🚀 **Recommended next step:** Create a Platform API key and authenticate with:

```bash
yolo login YOUR_API_KEY
```

For no-code dataset annotation, training, and deployment, use the [Ultralytics Platform](https://platform.ultralytics.com/).

## What's Changed
* Deprecate HUB in favor of Ultralyt
