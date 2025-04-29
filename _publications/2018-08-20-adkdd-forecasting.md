---
layout: paper
title: "Forecasting Granular Audience Size for Online Advertising"
date:   2018-08-20
categories: forecasting frequentitemset
comments: true
authors: R Sinha, D Singal, <b>Pranav Maneriker</b>, K Chawla, Y Shrivastava, D Pai, A Sinha
conf: AdKDD 2018
link: http://papers.adkdd.org/2018/papers/adkdd18-sinha-forecasting-granular.pdf
pdf: /assets/papers/07_workshop_adkdd_2018_forecasting.pdf
tags-main: forecasting frequentitemset
---


**Abstract**: Orchestration of campaigns for online display advertising requires marketers to forecast audience size at the granularity of specific attributes of web traffic, characterized by the categorical nature of all attributes (e.g. {US, Chrome, Mobile}). With each attribute taking many values, the very large attribute combination set makes estimating audience size for any specific attribute combination challenging. We modify Eclat, a frequent itemset mining (FIM) algorithm, to accommodate categorical variables. For consequent frequent and infrequent itemsets, we then provide forecasts using time series analysis with conditional probabilities to aid approximation. An extensive simulation, based on typical characteristics of audience data, is built to stress test our modified-FIM approach. In two real datasets, comparison with baselines including neural network models, shows that our method lowers computation time of FIM for categorical data. On hold out samples we show that the proposed forecasting method outperforms these baselines.