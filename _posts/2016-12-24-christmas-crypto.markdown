---
layout: post
title:  "Christmas Cryptopals Crypto Challenges"
date:   2016-12-24 00:00:00
categories: crypto
comments: true
tags-main: crpto
---

I have been seeing [the cryptopals crypto challenges][cryptopals-link] being mentioned in a lot of places. I decided to spend some time looking at and trying to solve as many as I can.

---
### Set 1 (basics)

When I started with this set, I thought that I would use python. I soon realized that I would be writing a lot of comments, so it would be good to use literate programming. 

This lead to me using ipython (now Jupyter) notebooks which fit my requirements well.

After spending some time to get the configuration fixed (windows ftw! \s) I can finally get down to writing code.

* **Challenge 1:** I spent wasted some time looking up some library functions, but simple overall.
* **Challenge 2:** the main issue is figuring out how XOR for unequal length strings is defined. The answer is: pad the shorter string with leading 0s. Pretty obvious, but important.
* **Challenge 3:** Too much ambiguity => we get started with actual crypto. Brute forced this one first. Then had to run an errand. Finally, I wrote a metric. Due to dinner etc, wasted a lot of time here.
* **Challenge 4:** This one was a short one. It's like 2:30 am now. The next one seems easy enough, but that's a tale for the morning.
* **Challenge 5:** I'm going to cheat a little bit and assume that the latter part of the challenge is just a joke. After some stupid encoding mistakes, this one is done.
* **Challenge 6:** Got the key, but some of the plaintext is messed up. Can't figure out the bug, so ignoring it for now.
* **Challenge 7:** SO MUCH PAIN. Note: Please follow a guide which describes the standard correctly. It's been so long since I saw the dreaded Vannila Ice lyrics. Onwards then.
* **Challenge 8:** Seems so easy as compared to what lead up to here.


Link to my set 1 solutions [here](https://github.com/pranavmaneriker/cryptopals/blob/master/set1/challenges.ipynb)


---
### Set 2 (block ciphers)

* **Challenge 9:**: What is happening, why are these so much easier?
* **Challenge 10:** Mostly copy/paste the right code, and a little bit of reading the CBC order of operations (do you take the XOR first, or later)


Link to my set 2 solutions [here](https://github.com/pranavmaneriker/cryptopals/blob/master/set2/challenges.ipynb)

[cryptopals-link]: https://cryptopals.com 
