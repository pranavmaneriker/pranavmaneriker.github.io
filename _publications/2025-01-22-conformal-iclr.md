---
layout: paper
title: "A Generic Framework for Conformal Fairness"
date:   2025-01-22
categories: conformal-prediction graphs fairness auditing
comments: true
authors: A Vadlamani&#42;, A Srinivasan&#42;, <b>P Maneriker</b>, A Payani, S Parthasarathy
conf: ICLR 2025
pagespecial: (&#42;shared first authorship)
link: https://openreview.net/forum?id=Ed1DBB3sBxiQNfYl33p
pdf: /assets/papers/iclr_2025_conformal.pdf
tags-main: conformal, graph
---

**Abstract:**
Conformal Prediction (CP) is a popular method for uncertainty quantification with machine learning models. While conformal prediction provides probabilistic guarantees regarding the coverage of the true label, these guarantees are agnostic to the presence of sensitive attributes within the dataset. In this work, we formalize \textit{Conformal Fairness}, a notion of fairness using conformal predictors, and provide a theoretically well-founded algorithm and associated framework to control for the gaps in coverage between different sensitive groups. Our framework leverages the exchangeability assumption (implicit to CP) rather than the typical IID assumption, allowing us to apply the notion of Conformal Fairness to data types and tasks that are not IID, such as graph data. Experiments were conducted on graph and tabular datasets to demonstrate that the algorithm can control fairness-related gaps in addition to coverage aligned with theoretical expectations.

