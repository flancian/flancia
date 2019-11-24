<!--
.. title: Flying
.. slug: flying
.. date: 2019-05-13 23:18:58 UTC+01:00
.. tags: flying, ml
.. category: 
.. link: 
.. description: 
.. type: text
-->

I'm really enjoying "Hands-On Machine Learning with Scikit-Learn and Tensorflow" by Aurélien Géron. It doesn't sound like a page turner immediately, I know, but I've been having great fun just reading it cover to cover in this long flight I'm on. I needed a book that gave me a high level overview of the whole field of Machine Learning, and this is it. It was recommended in the Machine Learning podcast I listened to a few months ago.

The first part of the book covers basics and Scikit-Learn -- no deep learning in it until page 230. I had heard in several places that it was not a good idea to skip to deep learning even if you think you're going to end up using deep learning for your models (I think Andrew Ng also mentions this many times), and I can see why; there's many interesting "shallow" algorithms, and this book covers interesting theory while discussing them. Scikit-Learn also provides a lot of useful goodies that are likely to be used even if you're mostly using Tensorflow: utility functions, and of course simpler ways of getting shallow models working. I particularly liked the way in which Scikit-Learn lets you set up "pipelines" of transformations and trainers. Finally, Scikit-Learn has great support for decision trees -- and it turns out that decision trees are state of the art for many problems, in practice, and have the advantage of yielding explainable ("white box") models, so there's that too. I read that Tensorflow supports the Scikit-Learn API, but at this point I'm not sure what that means and I can't check as I have no internet connection currently on this flight I'm on. I hope you are able to train the whole range of shallow models through it, straight in Tensorflow, as it'd be awkward/annoying to have to set up different systems to train shallow and deep models.

Anyway, I'm now officially in the Tensorflow part of the book and I'm also happy about that. At work I *just* got to the stage in which I am ready to actually go out and train a model for my first ML-related project, so reading more about Tensorflow in preparation for that has been an exciting way of spending the long flight. Some of it I had already used, but reviewing is how I learn. I'm using the first edition of the book, not the fancy new one that's about to come out and covers Tensorflow 2, but I think I made the right call by getting the "old" one (from 2016) instead of waiting for the new edition that I knew was coming out. Sure, some parts are likely outdated (it mentions Tensorflow 1.4 as experimental), but the book is working well for me as it is. The background I'm getting should come in handy for my project; this information wouldn't have been as useful if it had come to me in six months. I'll probably use Tensorflow 1.7 for my first TF project anyway, so there's that too. Having said that, I like the book enough that I may get the second edition depending on the reviews it gets (and exactly what changes in it). Reading the updated version would be yet another way of reviewing.
