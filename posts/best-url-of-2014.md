<!--
.. title: Best URL of 2014
.. slug: best-url-of-2014
.. date: 2019-01-31 18:04:30 UTC+01:00
.. tags: ml
.. category: 
.. link: 
.. description: 
.. type: text
-->

That'd be this [2014 post on the topology of manifolds and how they relate to neural networks][1]. The visualizations are great, and it basically blew my mind. I didn't know of the manifold hypothesis until now.

> The manifold hypothesis is that natural data forms lower-dimensional manifolds in its embedding space. There are both theoretical and experimental reasons to believe this to be true. If you believe this, then the task of a classification algorithm is fundamentally to separate a bunch of tangled manifolds.

I don't understand the whole post, or the whole argument (yet? not to a great level of detail anyway), but: if you want to build a neural network that distinguishes cat and dog pictures, in the worst case that would seem to require a huge network with *many* more nodes/layers (say, a function of the size of the image) than the number that seems to work reasonably well in practice (six or some other low constant number observed in reality). So the number of dimensions over which the "images" are potentially spread is huge, but it'd seem that in the real world one can rearrange the dog and cat images in a "shape" that then allows for relatively easy disentanglement, and these shapes can probably be realized in much lower dimensions (as per the example, six?). This could explain the observed predictive power of relatively small neural networks.

P.D.: almost unrelated, but the author's [pic][2] is pretty awesome. I mean it.

[1]: http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/
[2]: http://colah.github.io/about.html
