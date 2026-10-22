---
title: "A Generative Neural Network Approach for 3D Multi-Criteria Design Generation and Optimization of an Engine Mount for an Unmanned Air Vehicle"
created: 2026-10-20
captured: 2026-10-20
type: paper
domain: hardware
source: http://arxiv.org/abs/2311.03414v1
authors: "Christoph Petroll, Sebastian Eilermann, Philipp Hoefer, Oliver Niggemann"
published: "2023-11-06"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/a-generative-neural-network-approach-for-3d-multi-criteria-d.html
attachment_type: html
attachment_sha256: 1954c698155999f5b10a4abdb13ea5a87584757e5e5ef49dcdf7641b57b16581
---

# A Generative Neural Network Approach for 3D Multi-Criteria Design Generation and Optimization of an Engine Mount for an Unmanned Air Vehicle

**Authors**: Christoph Petroll, Sebastian Eilermann, Philipp Hoefer, Oliver Niggemann
**Published**: 2023-11-06
**arXiv**: http://arxiv.org/abs/2311.03414v1

## Abstract

One of the most promising developments in computer vision in recent years is the use of generative neural networks for functionality condition-based 3D design reconstruction and generation. Here, neural networks learn dependencies between functionalities and a geometry in a very effective way. For a neural network the functionalities are translated in conditions to a certain geometry. But the more conditions the design generation needs to reflect, the more difficult it is to learn clear dependencies. This leads to a multi criteria design problem due various conditions, which are not considered in the neural network structure so far. In this paper, we address this multi-criteria challenge for a 3D design use case related to an unmanned aerial vehicle (UAV) motor mount. We generate 10,000 abstract 3D designs and subject them all to simulations for three physical disciplines: mechanics, thermodynamics, and aerodynamics. Then, we train a Conditional Variational Autoencoder (CVAE) using the geometry and corresponding multicriteria functional constraints as input. We use our trained CVAE as well as the Marching cubes algorithm to generate meshes for simulation based evaluation. The results are then evaluated with the generated UAV designs. Subsequently, we demonstrate the ability to generate optimized designs under self-defined functionality conditions using the trained neural network.
