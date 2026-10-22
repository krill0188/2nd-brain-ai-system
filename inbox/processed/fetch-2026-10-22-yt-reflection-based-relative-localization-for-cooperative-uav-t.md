---
title: "Reflection-Based Relative Localization for Cooperative UAV Teams Using Active Markers"
created: 2026-10-22
captured: 2026-10-22
type: video
domain: ai-autonomy
source: https://www.youtube.com/watch?v=PAtPNwVovnM
channel: "Multi-robot Systems Group at FEE-CTU in Prague"
published: "2026-10-21"
tags: [drone, ai-autonomy, video, youtube]
transcript: true
---

# Reflection-Based Relative Localization for Cooperative UAV Teams Using Active Markers

**채널**: Multi-robot Systems Group at FEE-CTU in Prague (공신력 화이트리스트)
**게시**: 2026-10-21
**영상**: https://www.youtube.com/watch?v=PAtPNwVovnM

## 설명 요약

Abstract: Reflections of active markers in the environment are a common source of ambiguity in onboard visual relative localization. This work presents a novel approach that exploits these typically unwanted reflections for onboard relative localization in heterogeneous multi-UAV teams operating over specular, near-planar surfaces such as calm water and flat indoor floors. Using only a camera, active markers, and a single-beam rangefinder, the method requires no prior knowledge of robot size, ma

## 자막 (자동 추출, 최대 8000자)

In this video, we present our recent work on reflection-based relative localization for cooperative UAV teams using active markers. Reflections of active markers attached to team members are typically seen as a source of ambiguity in onboard visual relative localization and are usually considered undesirable. Our system instead leverages these reflections to estimate the relative positions of the other team members. We propose a method that is independent of the surface properties, its texture or any other surface related information. Our system requires only a camera from which the direction vector towards the target UAV is extracted and the height above the ground. Around the direction vector towards the target UAV, shown here in blue, we construct an ellypoid cone that accounts for sensor uncertainties. The reflections created by the targets active markers usually appear elongated in the observer's image. Therefore, we create an ellipse around the surface reflection shown here in red. The position of this ellipse is computed from the known distance between the UAV and the reflecting surface. This ellipse is then used to construct an elliptical cone from the reflection pattern. For computing the relative position, we sample random points on and inside this cone and retain only those points that also lie within the blue cone highlighted here in green. To further improve robustness, we introduce a particle filter illustrated in the following animation. The particle filter is based on a constant velocity motion model and predicts the new particle positions accordingly. In the update step, each particle receives a weight based on how well it aligns with the sampled inlayer points from the cone intersection. We use a Koshi kernel for this waiting, which makes the filter more tolerant to outliers. Afterwards, the particles are resampled, concentrating them around the regions of high likelihood. Finally, the updated particle cloud is used to compute the state estimate, giving us the final 3D position of the target UAV, highlighted here in yellow. We evaluated our approach in a range of indoor and outdoor experiments under different lighting conditions. The target carried ultraviolet LEDs while the observer used ultraviolet sensitive cameras with ultraviolet band pass filters. In the indoor experiments, we attached a circular LED array on top of the UAV to demonstrate that our method works independently of the robot size and the size of the LEDs. We tested the system on multiple surface types and under various lighting conditions. Throughout all trials, our method was able to reliably extract and track the 3D position of the target UAV. Additionally, multi-UV experiments were conducted with three UAVs flying simultaneously. The method ran on board all platforms in real time, including a microerial vehicle equipped with a Raspberry Pi 5 as the onboard computer. This figure shows the estimated relative position from the observer to another UAV, while this figure shows the estimation to the microerial vehicle. The system reliably estimated the relative position of all team members throughout the experiments. For the outdoor experiments, we compared our method to the state-of-the-art UVR system. In UVR, the markers are mounted on the arms of the target and their known spacing is used to estimate the relative 3D position. Relying on the known spacing has a significant drawback. At larger distances, the intermarker separation projects to only a few pixels, making the estimation increasingly unreliable. As a result, our system consistently outperformed UVR in all outdoor experiments, especially at distances beyond 30 m.
