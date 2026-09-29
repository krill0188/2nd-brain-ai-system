---
title: "SwarmNxt: Open-source Software-Hardware Platform for Fast and Agile Aerial Swarms"
created: 2026-09-12
captured: 2026-09-12
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2609.11382v1
authors: "Charbel Toumieh, Niel Mistry, Benjamin Jarvis, Simon Jeger, Peize Liu, Shaojie Shen, Dario Floreano"
published: "2026-09-10"
tags: [drone, ai-autonomy, paper, arxiv]
---

# SwarmNxt: Open-source Software-Hardware Platform for Fast and Agile Aerial Swarms

**Authors**: Charbel Toumieh, Niel Mistry, Benjamin Jarvis, Simon Jeger, Peize Liu, Shaojie Shen, Dario Floreano
**Published**: 2026-09-10
**arXiv**: http://arxiv.org/abs/2609.11382v1

## Abstract

Aerial robot swarms have the potential to transform time-critical safety, security, and search-and-rescue operations. By coordinating multiple robots, they can rapidly survey disaster sites, map collapsed or GPS-denied environments, and search cluttered areas faster than a single robot, reducing response times and minimizing risks to first responders. Realizing this potential, however, requires robust autonomous swarm navigation, which remains an active research challenge. Progress is further constrained by existing platforms, as commercial drones are often closed-source or lack the onboard computational resources needed for agile, vision-based collective flight. Moreover, developing, deploying, and maintaining software across multiple aerial robots requires significant engineering effort. To address these challenges, we present SwarmNxt, an open-source software platform built on the open-source OmniNxt drone hardware. SwarmNxt provides an end-to-end toolkit, including detailed hardware assembly instructions with a video tutorial, automation tools for parallel software deployment and swarm-wide updates, and a ROS 2-based framework for autonomous navigation. The platform integrates state-of-the-art control, planning, and depth estimation into a single ROS 2 multi-agent system, providing an open research infrastructure for physical swarm experimentation. We validate SwarmNxt through two real-world experiments: a six-drone swarm performing decentralized planning with high-speed inter-drone collision avoidance, and a four-drone swarm executing collective flight with onboard depth estimation in an obstacle-filled environment. Both experiments were run indoors with global position from external motion capture; perception, planning, and control run onboard.
