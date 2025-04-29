---
layout: paper
title: "Understanding Knowledge Gaps in Visual Question Answering: Implications for Gap Identification and Testing"
date:   2020-07-28
categories: vision+nlp
comments: true
authors: G Bajaj, B Bandyopadhyay, D Schmidt, <b>P Maneriker</b>, C Myers, S Parthasarathy
conf: CVPRW 2020
link: https://openaccess.thecvf.com/content_WACV_2020/html/Chaudhry_LEAF-QA_Locate_Encode__Attend_for_Figure_Question_Answering_WACV_2020_paper.html
pdf: /assets/papers/13_workshop_cvpr2_2020_understanding.pdf
tags-main: nlp vision qa
---

**Abstract:** Traditional Visual Question Answering (VQA) datasets typically contain questions related to the spatial information of objects, object attributes, or general scene questions. Recently, researchers have recognized the need to improve the balance of such datasets to reduce the system's dependency on memorized linguistic features and statistical biases, while aiming for enhanced visual understanding. However, it is unclear whether any latent patterns exist to quantify and explain these failures. As an initial step towards better quantifying our understanding of the performance of VQA models, we use a taxonomy of Knowledge Gaps (KGs) to tag questions with one or more types of KGs. Each KG describes the reasoning abilities needed to arrive at a resolution, and failure to resolve gaps indicates an absence of the required reasoning ability. After identifying KGs for each question, we examine the skew in the distribution of questions for each KG. We then introduce a targeted question generation model to reduce this skew, which allows us to generate new types of questions for an image.