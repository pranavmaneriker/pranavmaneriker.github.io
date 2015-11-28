---
layout: post
title:  "Random tmux tip"
date:   2015-10-16 23:00:00
categories: tmux
comments: true
tags-main: tmux multiple
---

In a running tmux session, I was sshed into a machine. 

And I accidentally attached the session open there.

tmux within tmux, how do I detach the inner one?

press Ctrl+b Ctrl+b d and you're done

(side note: Ctrl + b allows the inner tmux to capture your input, so an extra Ctrl + b works great in general)
