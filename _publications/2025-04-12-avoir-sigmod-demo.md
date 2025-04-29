---
layout: paper
title: "Interactive Fairness Auditing: Leveraging AVOIR for Dynamic Evaluation and Mitigation"
date:   2025-04-12
categories: avoir demo
comments: true
authors: A Meghrazi, <b>P Maneriker<.b>, S Padhee, S Parthasarathy
conf: SIGMOD 2025 Demo (to appear)
link: https://doi.org/10.1145/3722212.3725108
tags-main: avoir demo
---


**Abstract:**
Ensuring fairness in high-stakes machine learning (ML) applications remains a significant challenge. We introduce an interactive, Streamlit-based User Interface (UI) for AVOIR, an automated fairness monitoring framework. This UI allows users to select fairness metrics (e.g., Demographic Parity, Equalized Odds) and explore dataset attributes through dynamic visualizations.
The UI supports iterative refinement, enabling users to define fairness coAnstraints in a domain-specific language (DSL), evaluate models, and address violations via interactive charts. Leveraging AVOIR’s inference and optimization capabilities, it provides probabilistic guarantees and detects biases at runtime. We demonstrate its utility on multiple datasets, showing how fairness violations are identified and mitigated. By combining declarative fairness specifications, rigorous optimization, and intuitive visualizations, our UI empowers stakeholders to deploy ML models responsibly.
