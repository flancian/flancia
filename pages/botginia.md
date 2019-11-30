<!--
.. title: Botginia Woolf
.. slug: botginia
.. date: 2018-12-16 17:33:15 UTC+01:00
.. tags: flancia
.. link: 
.. description: 
.. type: text
-->

I made a simple Twitter bot that posts lines from Virginia Woolf's works: 
[@botginia](https://twitter.com/botginia). 

I have long been a fan and her turns of phrase are just so beautiful. One of the best writers I've read.

Unsure what the "right" cadence for posting would be. Currently set to run once a day, around 9PM CET.

I'd like to eventually get her to be more sophisticated:

  * Score phrases using heuristics.
  * Generate phrases not actually present in the corpus.
  * Train a generative ML model.
    * Fine tune GPT-2 or BERT.
    * Use social interactions in Twitter (likes and polls) as labelling.
    * Optimize for which phrases are "more beautiful" for whatever definition the users are using.
    * Optimize for which phrases "fool" the users more often, as in: they vote that they were *not* generated. 
  * Adversarial-like approach, although this situation seems win-win: the users do the work of labelling, but they get "interestingness" as a payoff.

But for now... random sampling :) Code is at [github](https://github.com/flancian/botginia).
