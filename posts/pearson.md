<!--
.. title: Pearson
.. slug: pearson
.. date: 2019-01-26 19:32:22 UTC+01:00
.. tags: compsci, ml
.. category: 
.. link: 
.. description: 
.. type: text
-->

I didn't know about [Pearson correlation coefficient][1] until today. It seems like such a useful thing. From Wikipedia:

 - It is a measure of the linear correlation between two variables X and Y.
 - It has a value between +1 and −1, where 1 is total positive linear correlation, 0 is no linear correlation, and −1 is total negative linear correlation. 

So, if you have points in the plane, it can tell you how well they match `y = x` (that yields 1) or `y = -x` (yields -1) or neither. In ML, it can tell you how likely it is that two features (variables/"input columns") are not independent; and how likely it is that a feature will add information to a model (that happens if `Pearson(feature, target)` is either close to -1 or 1).
 
I'm glad I know about it now.

[1]: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
