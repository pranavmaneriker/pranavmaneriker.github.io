---
layout: paper
title: "LIVE-ITS: LSH-based Interactive Visualization Explorer for Large-Scale Incomplete Time Series"
date:   2024-12-15
categories: large-scale time-series, incomplete time-series, time-series visualization, visualization analytics
comments: true
authors: Hongjie Chen, Aaron D Beachnau, Panos Thomas, <b>Pranav Maneriker</b>, Josh Kimball, Ryan A Rossi
conf: BigData 2024
link: https://ieeexplore.ieee.org/abstract/document/10825096
pdf: /assets/papers/bigdata_2024_liveits.pdf
tags-main: time-series, visualization
---

**Abstract:**
Recent advances in time series research have created a significant demand for better time series visualization techniques, especially for large-scale datasets that contain millions of time series or more. In this paper, we consider a common
use scenario where analysts aim to identify representative time series from a large collection. These representative time series
generalize as many time series as possible and can be used for downstream tasks. Building a visualization system for this scenario involves many challenges, including visualizing, selecting, and highlighting a subset of time series from the overall dataset. Moreover, the potential for time series to be incomplete due to missing records adds an extra layer of difficulty. To address
these challenges, we propose a novel visualization system, called the Locality Sensitive Hashing-based Interactive Visualization Explorer for large-scale Incomplete Time Series (LIVE-ITS). On the frontend, LIVE-ITS allows analysts to interact with the system and select representative time series in areas of interest. In the backend, LIVE-ITS not only selects an optimal subset that represents as many time series as possible, but also achieves the best possible time complexity. Experiments on both synthetic dataset and real-world datasets show that LIVE-ITS exhibits high partition accuracy and high response efficiency, further validating the effectiveness of our proposed visualization system.