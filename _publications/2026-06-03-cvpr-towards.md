---
layout: paper
title: "Towards Sparse Video Understanding and Reasoning"
date:   2026-06-03
categories: video reasoning qa
comments: true
authors: C Xu, Z Ye, S Wu, W Li, Z Wang, Z Xia, L Lu, <b>P Maneriker</b>, F Du, M Li, H Liu
conf: CVPR 2026 (to appear)
link: tbd
tags-main: rl qa video
---


**Abstract:** We present \revise (\underline{Re}asoning with \underline{Vi}deo \underline{S}parsity), a multi-round agent for video question answering (VQA). Instead of uniformly sampling frames, \revise selects a small set of informative frames, maintains a summary-as-state across rounds, and stops early when confident. It supports proprietary vision-language models (VLMs) in a ``plug-and-play'' setting and enables reinforcement fine-tuning for open-source models. For fine-tuning, we introduce EAGER (Evidence-Adjusted Gain for Efficient Reasoning), an annotation-free reward with three terms: (1) Confidence gain: after new frames are added, we reward the increase in the log-odds gap between the correct option and the strongest alternative; (2) Summary sufficiency: at answer time we re-ask using only the last committed summary and reward success; (3) Correct-and-early stop: answering correctly within a small turn budget is rewarded. Across multiple VQA benchmarks, \revise improves accuracy while reducing frames, rounds, and prompt tokens, demonstrating practical sparse video reasoning. 
