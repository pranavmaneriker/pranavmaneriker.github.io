---
layout: post
title:  "Sentient Computers (over SSH)"
date:   2015-03-09 20:50:00
categories: jekyll update
comments: true
tags-main: senti-comps
---

Note: The author takes no responsibility in case this trick is used for malicious purposes.

I was successful in convincing one of my friends(but only for a while) that my computer became sentient. Later, he was convinced that I had written a powerful ML program.

The answer, ofcourse, was much simpler. 

{% highlight bash %}

ssh pm@my_ip
espeak -s 100
"I am a sentient laptop"

{% endhighlight %}

For my own little trick, I sshed into my machine using [connectbot][connectbot-link] and ran espeak. 

Since then, I have realised that if you know someone's password or have physical access to a laptop (where you can add your ssh key to the known hosts), this can be used quite deviously (ksaurav _/\\\_)


[connectbot-link]: https://play.google.com/store/apps/details?id=org.connectbot&hl=en 
