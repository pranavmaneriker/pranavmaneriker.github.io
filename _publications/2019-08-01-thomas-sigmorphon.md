---
layout: paper
title: "THOMAS: The Hegemonic OSU Morphological Analyzer using Seq2seq"
date:   2019-08-01
categories: shared-task
comments: true
authors: B Oh&#42;, <b>P Maneriker</b>&#42;, N Jiang&#42;
conf: SIGMORPHON workshop, ACL 2019
pagespecial: (&#42;shared first authorship)
pdf: https://www.aclweb.org/anthology/W19-4210.pdf
tags-main: nlp seq2seq
---

**Abstract:** This paper describes the OSU submission to the SIGMORPHON 2019 shared task, Crosslinguality and Context in Morphology. Our system addresses the contextual morphological analysis subtask of Task 2, which is to produce the morphosyntactic description (MSD) of each fully inflected word within a given sentence. We frame this as a sequence generation task and employ a neural encoder-decoder (seq2seq) architecture to generate the sequence of MSD tags given the encoded representation of each token. Follow-up analyses reveal that our system most significantly improves performance on morphologically complex languages whose inflected word forms typically have longer MSD tag sequences. In addition, our system seems to capture the structured correlation between MSD tags, such as that between the “verb” tag and TAM-related tags.
