<!--
.. title: A Chrome extension I want
.. slug: history-chrome-extension
.. date: 2019-01-02 10:18:12 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

I sometimes go on internet reading binges in which I branch out into what end up being hundreds of tabs. As I mentioned earlier, I have a sort of [Wikipedia addiction][1], which doesn't help.

I'd like to have a Chrome extension that lets me analyze my browsing history and get insights from it; perhaps even further suggested reading based on the most productive reading patterns detected.

As an example data point, I've just followed the following path in browsing, starting with a link to Wikipedia in Hacker News:

`Kuleshow Effect -> Uncanny Valley -> Mirror Neuron -> Common Coding Theory`

This is a representative example of a short but interesting (to me) reading session; exposing other similar reading flows to me would be useful. I guess my writing about this flow here is a very basic, relatively low tech version of sharing this flow with the world; it would be interesting if millions of people would voluntarily do this, in a lower effort kind of way (like installing an extension and whitelisting some sites that one reads through thoroughly). Google, Microsoft and Mozilla probably have a good chunk of this information already through their browsers (not sure, I don't know what their default settings all are), but as far as I can tell it doesn't get exposed to the world except through things like Google's ranking algorithm and search autosuggest.

Anyway, I searched for an extension with this functionality for a while and I think [Brancher](https://brancher.io/) may be pretty close to what I want. I'm unsure about their privacy policy, though -- the site mentions that they show all flows in their "trending" section by default, which is a bit worrying to me; I'd be much more comfortable with whitelisting, say, wikipedia.org and whatever comes out of visiting a link in news.ycombinator.com. I will probably update this post with more information after giving it a try.

*Edit (2019-01-12)*: I've removed Brancher. The implementation seems solid, and I liked their tree-based visualizations, but it felt a bit too creepy for my taste. It seems as if initially it defaulted to "all private" mode, in which every browsing "tree" and every bit of browsing information was kept private by default -- makes sense to me. But recently they've changed their settings so even in private mode your browsing shows up in a "trending" section. They say that all Personally Identifiable Information is removed from your browsing before they do so, but they don't say *how* they do this as far as I can tell, or even exactly what it means (what do they consider PII?). Companies have a history of leaking confidential information even after being anonymized, even bigger companies such as Netflix[2], so I'm not ready to trust a random company with this data. My ideal extension would probably be something like Brancher but with a 100% offline mode.

[1]: link://slug/wikipedia
[2]: https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/
