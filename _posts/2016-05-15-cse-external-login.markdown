---
layout: post
title:  "Logging into the CSE IITK network from outside IITK"
date:   2016-05-15 00:00:00
categories: ssh CSE IITK
comments: true
tags-main: ssh-cse
---

A lot of people were facing issues when trying to log in to the CSE network from outside campus.

You need to add your public key to the login.cse ssh folder. Here is a list of insturctions to help you do so:

* __Generate keys (if not already done)__

You need to generate your public/private key pair for your ssh client. The commands to do this with openssh are:
{% highlight bash %}

ssh-keygen -t rsa

{% endhighlight %}

Your public and private keys are now in the ~/.ssh folder. Copy ~/.ssh/id_rsa.pub to the clipboard.

* __ssh to login.cse__

This is a bit convoluted, if you're not inside the IITK network. You may need to use the [SSL-VPN client][SSL-VPN-link] first.
Then you should be able to ssh into local machines. 

login.cse has this other restriction where password login is only allowed through machines inside the cse network but some of the machines that have been recently updated don't have clients with support for the ciphers that login.cse does. One of the machines which does have support is csews15 (verified by the author at the time of making this post)

Thus, the procedure is: (after SSL-VPN)

{% highlight bash %}

ssh <username>@csews15.cse.iitk.ac.in
<enter password>
ssh login.cse.iitk.ac.in
<enter password again>
{% endhighlight %}

* __Add the key to authorized keys__

Once you are in this machine, use any editor to paste your id_rsa.pub into ~/.ssh/authorized_keys . You may have to create the folder too.

{% highlight bash %}
mkdir .ssh
cd .ssh
echo "<paste pubkey here>" >> authorized_keys
{% endhighlight %}

* __Done!__

Now you can switch SSL-VPN off and you should be able to login to the machine directly. Check this with

{% highlight bash %}

ssh <username>@login.cse.iitk.ac.in

{% endhighlight %}

Make sure that the key that you used is being used by ssh for authentication. You may have to ssh-add key-file for this.

[SSL-VPN-link]: http://www.iitk.ac.in/ccnew/index.php/13-network/99-how-to-use-ssl-vpn
