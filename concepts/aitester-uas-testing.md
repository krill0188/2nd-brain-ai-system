---
title: "AITester: Automated System-Level Testing for UAS"
created: 2026-08-24
updated: 2026-08-24
type: concept
tags: [drone, gcs-software, testing, automation, px4, ardupilot]
sources: [inbox/fetch-2026-08-24-arxiv-automated-system-level-testing-of-unmanned-aerial-systems.md]
confidence: medium
contested: false
contradictions: []
domain: gcs-software
---

# AITester: Automated System-Level Testing for UAS

AITester is an automated system-level testing approach for unmanned aerial systems (UAS) that utilizes model-based testing and artificial intelligence techniques to automatically generate, execute, and evaluate test scenarios.

## Overview

Current industrial practice for UAS testing involves manually creating test scenarios and evaluating outcomes. AITester addresses this limitation by generating test scenarios dynamically during execution based on environmental context at runtime.

## Key Features

### Automated Test Generation
- AI-driven scenario creation
- Runtime context awareness
- Dynamic adaptation to system state

### Target Components
- UAV autopilot systems
- Ground Control Station (GCS) cockpit display systems (CDS)
- Safety-critical avionics software

## Methodology

1. **Model-Based Testing**: Formal system models guide test generation
2. **AI Techniques**: Machine learning for scenario optimization
3. **Runtime Generation**: Tests created on-the-fly during execution
4. **Automated Evaluation**: Outcome assessment without manual intervention

## Evaluation Results

Empirical evaluation on core UAS components demonstrated effectiveness:
- Successfully generated scenarios causing deviations from expected UAV autopilot behavior
- Revealed potential flaws in GCS-CDS integration

## Related Topics

- [[px4-flight-stack]] — PX4 flight control software
- [[ardupilot]] — ArduPilot open-source autopilot
- [[drone-simulation]] — Simulation environments for testing
- [[ground-control-station]] — GCS software systems

## Source

^[inbox/fetch-2026-08-24-arxiv-automated-system-level-testing-of-unmanned-aerial-systems.md]

## 📰 최근 관련 소식
- Automated System-level Testing of Unmanned Aerial Systems (arxiv.org, 2024-03-23) — http://arxiv.org/abs/2403.15857v2
- Pentagon’s counter-drone task force inks $500M contract for SkyValor 'detect and defeat' system after border testing (DefenseScoop, Fri, 31 Ju) — https://news.google.com/rss/articles/CBMinwFBVV95cUxOZUpxTkZwc3BESFJYVVVqLUgzdW1qbHNBTm9yWXhNUHNZLUh3c25HT25xZE9OOWw0SU56QlpwN2NJWGIyX0s4TUFaYTF6d2MtckFsZVB3bjAyLVcyV1R4OFJueWJYM2ZsaEYxVFJiM3E3d0o3MGlILTNIQkZQLTJ1cXZhaDUtdU5hNHc4dFk5YWEwMGtGYmQ2d3pwUTNvb2c?oc=5
- AV’s LOCUST® Selected for Nearly $500 million Army Counter-UAS Contract for Enduring-High Energy Laser (E-HEL) Program (Voice of Alexandria, Wed, 02 Se) — https://news.google.com/rss/articles/CBMipgJBVV95cUxQT0ZxMWFjdEZSeWdHM21qMHJ5YmFoZUxmZ2FPVXg5aGRLTHBGc2hPYXd5NlU4YnRHNmhldXFuSm5LcXMtVXc4VXZKVEs0VUhGOW4tNjE5T3NQMUxhWG5UVW5lT3hIemZhMHAzblBjNnVNLWlxTWxmLWdUdURVRXczUk40clVQUnhyM2NuSHNpQUl3TkRITTJvRGJ0RmRteWhhay1wWVdCaTVWc09EeEE1aFp4TTNTa1doM0dreExhVXgwOW5aYmN0LUIxUHoxRlhhX0J0M2NBVDFLMDFoU2pIZUhqbEMtd3hLa1g3UFhjNlMxdEY5dTBGNWsySHpqZWk4TWpHRF81RlhOX2ZmdXB0bmxTeWVLd2FRN2UxcUNxX3FDcHc3NlE?oc=5
- Selected for Nearly $500 million Army Counter-UAS Contract for Enduring-High Energy Laser (E-HEL) Program (Business Wire, Wed, 02 Se) — https://news.google.com/rss/articles/CBMigwJBVV95cUxOZ21KLVZfTXE2aHJBZ010M0JYeXNEcnZyQ0ZmemsxQW5XbHo1NndEMGtJMHV1bXBBVWVTQnZLYi0ybXV0ME5zSHhpUlRjZDZlVnEwMm5sN1c5VEROWmtBM09BQldKSUR3SlBvelo2VnJfREtfVkNTWDlVWnVjVVhMQTd5azMzSjFqNjY0TFdQNkUwNkNyM2w0U2FWRzBWVGs5aXNJUWRaWWlxNzFGMUsxdWx6cUlOdGxJMlZONGtucnZ1ZkJBYlZTTFh5MWpCVVNRenZOQ0pPNWpIT09sUDNiUUdrUXhyZVRPZlg1eGh3M3VVb3RUSUgtSFVuM1RMMGxFZklz?oc=5
- Av's Locust Selected for Nearly $500M Army Counter-UAS Contract for Enduring-high Energy Laser (E-HEL) Program (ASDNews, Tue, 01 Se) — https://news.google.com/rss/articles/CBMi2wFBVV95cUxQTVZQRGEwb1NfSWxPZWQ4ODQwUVpZXzk3S3RMd3A3Q05tNHhwbXlHZFQ4MFdteDVPd1c3LVRBY01vTlU0emJDLW0ySE0wcng2NGJGMXFLY0tuSlJBSTdra1hQQUp5eVNYbVRwWW1lLW1fSTIta2Y3NkwzYlh0b0pXNjhkSC1vemZsQl9UUElOV21CWDZVVkdGS3oweWpkWE8yQ2laSEdqQWxYLTRTWm9DaVh2UGFiWDZuVURobFdtMGhuOTRtX1VyV1hETjNONGdZMVdkaS00LVVYSjg?oc=5
- AV’s LOCUST selected for nearly $500 million Army counter-UAS contract for Enduring-High Energy Laser (E-HEL) program (Defense and Munitions, Fri, 18 Se) — https://news.google.com/rss/articles/CBMi8wFBVV95cUxPQzZfREMweVYzQmpueERDeXUxSlVVNk9yTTFYYm4yTWk0MmxKdHZlR3Z3Z0FqZEFYczlWRXhpbV9DVDNVQ0ZWMXpWaEVKdGotNzZsUTVyVVBFSk5XYWtZZnE4V0FYM3ZMTnBKdjFNUDlnSTJBcF9ydXZYRFdJa1JrXzdYX0ZTcWJHc0xjZVEta1pwOHZDTjc1T19ITjRzUk5yZkZIa3N1VzllelN2Q2ZkajgzUlFGYTJ3Mlp1SHZlV25WRk5WWGp6eTNlSmVIMGdwaUVYR1RjbXN0LWNsZjQ2VlVoQ1Q1by04aUROdThyVjZIM28?oc=5
