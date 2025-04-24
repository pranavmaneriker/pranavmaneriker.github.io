---
layout: paper
title: "A Generic Framework for Conformal Fairness"
date:   2025-01-22
categories: large-scale time-series, incomplete time-series, time-series visualization, visualization analytics
comments: true
authors: Hongjie Chen, Aaron D Beachnau, Panos Thomas, <b>Pranav Maneriker</b>, Josh Kimball, Ryan A Rossi
conf: BigData 2024
link: https://ieeexplore.ieee.org/abstract/document/10825096
pdf: /assets/papers/bigdata_2024_liveits.pdf
tags-main: time-series, visualization
---

**Abstract:**
Conformal Prediction (CP) is a popular method for uncertainty quantification with machine learning models. While conformal prediction provides probabilistic guarantees regarding the coverage of the true label, these guarantees are agnostic to the presence of sensitive attributes within the dataset. In this work, we formalize \textit{Conformal Fairness}, a notion of fairness using conformal predictors, and provide a theoretically well-founded algorithm and associated framework to control for the gaps in coverage between different sensitive groups. Our framework leverages the exchangeability assumption (implicit to CP) rather than the typical IID assumption, allowing us to apply the notion of Conformal Fairness to data types and tasks that are not IID, such as graph data. Experiments were conducted on graph and tabular datasets to demonstrate that the algorithm can control fairness-related gaps in addition to coverage aligned with theoretical expectations.

