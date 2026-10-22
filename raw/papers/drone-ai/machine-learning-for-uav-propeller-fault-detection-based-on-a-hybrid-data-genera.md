---
title: "Machine Learning for UAV Propeller Fault Detection based on a Hybrid Data Generation Model"
created: 2026-10-22
updated: 2026-10-22
type: paper
item_type: preprint
authors: "Tong, J. J.; Zhang, W.; Liao, F.; Li, C. F.; Zhang, Y. F."
year: "2023"
doi: "10.48550/arXiv.2302.01556"
url: "http://arxiv.org/abs/2302.01556v1"
zotero_key: VX8F2MAT
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/machine-learning-for-uav-propeller-fault-detection-based-on-a-hybrid-data-genera.pdf
attachment_sha256: cb60b7b67194ad5cba8e4fb92319d2726606455c3bd63ee7c731384e107d6c5f
sha256: 80dc38d48c147643
---

# Machine Learning for UAV Propeller Fault Detection based on a Hybrid Data Generation Model

**Authors**: Tong, J. J.; Zhang, W.; Liao, F.; Li, C. F.; Zhang, Y. F.  
**Year**: 2023  
**DOI**: 10.48550/arXiv.2302.01556  
**URL**: http://arxiv.org/abs/2302.01556v1

## Abstract

This paper describes the development of an on-board data-driven system that can monitor and localize the fault in a quadrotor unmanned aerial vehicle (UAV) and at the same time, evaluate the degree of damage of the fault under real scenarios. To achieve offline training data generation, a hybrid approach is proposed for the development of a virtual data-generative model using a combination of data-driven models as well as well-established dynamic models that describe the kinematics of the UAV. To effectively represent the drop in performance of a faulty propeller, a variation of the deep neural network, a LSTM network is proposed. With the RPM of the propeller as input and based on the fault condition of the propeller, the proposed propeller model estimates the resultant torque and thrust. Then, flight datasets of the UAV under various fault scenarios are generated via simulation using the developed data-generative model. Lastly, a fault classifier using a CNN model is proposed to identify as well as evaluate the degree of damage to the damaged propeller. The scope of this paper focuses on the identification of faulty propellers and classification of the fault level for quadrotor UAVs using RPM as well as flight data. Doing so allows for early minor fault detection to prevent serious faults from occurring if the fault is left unrepaired. To further validate the workability of this approach outside of simulation, a real-flight test is conducted indoors. The real flight data is collected and a simulation to real sim-real test is conducted. Due to the imperfections in the build of our experimental UAV, a slight calibration approach to our simulation model is further proposed and the experimental results obtained show that our trained model can identify the location of propeller fault as well as the degree/type of damage. Currently, the diagnosis accuracy on the testing set is over 80%.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
