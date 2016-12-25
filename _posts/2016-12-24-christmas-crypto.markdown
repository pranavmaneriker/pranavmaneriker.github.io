---
layout: post
title:  "Christmas Cryptopals Crypto Challenges"
date:   2016-12-24 00:00:00
categories: crypto
comments: true
tags-main: crpto
---

I have been seeing [the cryptopals crypto challenges][cryptopals-link] being mentioned in a lot of places. I decided to spend some time looking at and trying to solve as many as I can.

### Set 1 (basics)

When I started with this set, I thought that I would use python. I soon realized that I would be writing a lot of comments, so it would be good to use literate programming. 

This lead to me using ipython (now Jupyter) notebooks which fit my requirements well.

After spending some time to get the configuration fixed (windows ftw! \s) I can finally get down to writing code.

* **Challenge 1:** I spent wasted some time looking up some library functions, but simple overall.
* **Challenge 2:** the main issue is figuring out how XOR for unequal length strings is defined. The answer is: pad the shorter string with leading 0s. Pretty obvious, but important.
* **Challenge 3:** Too much ambiguity => we get started with actual crypto. Brute forced this one first. Then had to run an errand. Finally, I wrote a metric. Due to dinner etc, wasted a lot of time here.
* **Challenge 4:** This one was a short one. It's like 2:30 am now. The next one seems easy enough, but that's a tale for the morning.
* **Challenge 5:** I'm going to cheat a little bit and assume that the latter part of the challenge is just a joke. After some stupid encoding mistakes, this one is done.



Link to  my set 1 solutions [here](https://github.com/pranavmaneriker/cryptopals/blob/master/set1/challenges.ipynb)

[cryptopals-link]: https://cryptopals.com 
