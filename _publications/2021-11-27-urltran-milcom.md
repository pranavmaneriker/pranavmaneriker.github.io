---
layout: paper
title: "URLTran: Improving Phishing URL Detection Using Transformers"
date:   2021-11-27
categories: nlp+security
comments: true
authors: <b>P Maneriker&#42;</b>, J Stokes&#42;, E G Lazo, D Carutasu, F Tajaddodianfar, A Gururajan
conf: MILCOM 2021
pagespecial: (&#42;shared first authorship)
pdf: https://arxiv.org/pdf/2106.05256
tags-main: nlp security
---


**Abstract:** Browsers often include security features to detect phishing web pages. In the past, some browsers evaluated an unknown URL for inclusion in a list of known phishing pages. However, as the number of URLs and known phishing pages continued to increase at a rapid pace, browsers started to include one or more machine learning classifiers as part of their security services that aim to better protect end users from harm. While additional information could be used, browsers typically evaluate every unknown URL using some classifier in order to quickly detect these phishing pages. Early phishing detection used standard machine learning classifiers, but recent research has instead proposed the use of deep learning models for the phishing URL detection task. Concurrently, text embedding research using transformers has led to state-of-the-art results in many natural language processing tasks. In this work, we perform a comprehensive analysis of transformer models on the phishing URL detection task. We consider standard masked language model and additional domain-specific pre-training tasks, and compare these models to fine-tuned BERT and RoBERTa models. Combining the insights from these experiments, we propose URLTran which uses transformers to significantly improve the performance of phishing URL detection over a wide range of very low false positive rates (FPRs) compared to other deep learning-based methods. For example, URLTran yields a true positive rate (TPR) of 86.80% compared to 71.20% for the next best baseline at an FPR of 0.01%, resulting in a relative improvement of over 21.9%. Further, we consider some classical adversarial black-box phishing attacks such as those based on homoglyphs and compound word splits to improve the robustness of URLTran. We consider additional fine tuning with these adversarial samples and demonstrate that URLTran can maintain low FPRs under these scenarios. 
