<!--
.. title: On go links
.. slug: go-links
.. date: 2020-08-10 18:51:13 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. status:
-->

I've had several conversations with people surrounding go links recently, over on [Twitter](link://slug/twitter) and Matrix; that made me realize I've been procrastinating on writing something about them, so here I am. Procrastination over.

Before I lose you, let me tell you outright why I think go links could be interesting or even important to you:

1. They are complementary cognitive artifacts.
2. They are URLs made truly democratic.
3. They are a simple, but solid, base for a distributed social knowledge graph.

Did that pique your interest? Then read on.

# A primer
go links originated within Google around 2005 or 2006. They are the invention of Benjamin Staffin, an SRE (like yours truly); as detailed in his interview with [Jon Gaulding from trot.to](https://www.trot.to/blog/2020/07/09/go-links-origin-story/), they were inspired by AOL keywords and were designed to scratch an itch that Benjamin's team was experiencing at the time: people kept asking for trivial redirects to internal pages that were relatively work intensive to set up. Go links emerged as self-service named redirects, essentially: a web service that sets up a redirect from a chosen label (e.g. go/agora) to a target URL (e.g. https://flancia.org/agora). From Google they spread to many other companies, particularly around Silicon Valley. If you walk around their offices (well, if you did before Covid-19 anyway) you will see them in wide use.

In many ways, a go link is like any randomly generated "short link" you can get nowadays around the web as offered by a number of services like <bit.ly>: you can create them quickly, they can point to any valid URL, and they tend to be shorter than the URLs they link to. So far so good. But they have some extra attributes:

 - They tend to carry semantic information in their labels -- you need to choose the go link label anyway, and better names make for easier communication and better recall. Some examples:
    - `go/go-links-history` is better than `https://bit.ly/3iyrl9e` as a pointer to <https://www.trot.to/blog/2020/07/09/go-links-origin-story/>.
    - `go/agora` is better than `https://bit.ly/33Q5F4l` as a pointer to <https://flancia.org/agora>.
 - The chosen-label approach lets you do what I call go-link-driven-development: it is easy to write them down _before they exist_, and backfill references as needed later. This is very convenient when you _know_ that a resource exists (or will exist), but do not want to interrupt the flow you are in to go fetch a reference to it.
 
All in all, go links are good drop-in complements to URLs: every time you are about to use a "bare" URL (and you have it, say, in your clipboard), it's very easy to promote it to a semantically meaningful and easier to remember go link instead. If you visit a go link that doesn't exist, you get a prompt to create it and point it at a target. Browser extensions make this easier even, but honestly you don't even need those and many heavy go links users don't use them.

# Give URLs back to the people
So, what's with the democratic bit earlier? Isn't that a bit grandiose? Perhaps, but I believe not by much.

Back in the early days of the web, the ratio of users that "owned" some part of the URL space to total number of users was quite high. This was due to the fact that many users came from academia and got some personal web space with their campus/research accounts, a la `flanbridge.edu/~flancian`; or, later, relatively tech-savvy and likely to run a domain of their own or be part of an organization that did so. Even as late as the heyday of blogs, around the mid aughts, lots of internet users could claim ownership of some URL space -- and, with it, responsibility over links between resources. Hyperlinks are, of course, the true spirit of the web; it is not the nodes themselves, but rather their connections, that grant the web its power, and define online communities (remember the [blogosphere](https://en.wikipedia.org/wiki/Blogosphere)?).

Then, of course, monolithic social media happened, walled gardens were built -- and everything changed. With the push to mobile apps, which are notoriously hard to link to in a consistent cross-platform way, URLs were further de-prioritized by companies; some went as far as fighting deep linking and seemed to make a concerted effort at making URLs useless -- by making them impermanent, unreliable. As we all know, [cool URIs don't change](https://www.w3.org/Provider/Style/URI).

I posit go links can give back the power of URIs and stable links to the people; this through the fact that some _URL space_ could be shared equally by all users of a public go links instance. Go links are mostly used in companies nowadays, but they could (and, I believe, should) be extended so they can be used by arbitrary groups in the internet, pending the definition of an ACLing system and the imposition of reasonable terms of use.

To illustrate: say you write a Facebook post that you are particularly proud of -- you share the link widely. One day Facebook decides to take you down for any reason -- you're in trouble. You've not only lost your Facebook account and your post -- you've lost the value of all the links you sent out, and any links that people set up! Even if you rewrote the post in a Wordpress blog, or restore from a personal backup, all the links would still point to the old location, and you would have no way to set up redirects after the fact or even let people know that the target is known to be broken.

With go links as a tool, you could have shared `go/about-topic` instead, and just adjusted the target after the Facebook issue. Go links are user-owned arbitrary pointers; a user-friendly overlay that can mediate between said users and the targets controlled oh so often by monolithic platforms that have claimed ownership of most of the URL space that people care about.

# Cognitive artifacts
Cognitive artifacts are "artificial devices that maintain, display, or operate upon information in order to serve a representational function and that affect human cognitive performance"[^1]. They are objects "made by humans for the purpose of aiding, enhancing, or improving cognition"[^2]. Some examples are calendars, to-do lists, computers -- and, with the latter, many of their abstractions.

[^1]: <http://edutechwiki.unige.ch/en/Cognitive_artifact>
[^2]: <https://classes.matthewjbrown.net/teaching-files/cognitive-ethnography/hutchins-artifacts.pdf>

[David Krakauer](http://tuvalu.santafe.edu/~krakauer/Site/Welcome.html) from the Santa Fe Institute volunteers some further useful definitions surrounding cognitive artifacts: they can be _competitive_ or _complementary_. Complementary cognitive artifacts have an interesting property: as you use them, you become better at the same or a related cognitive task, _even in the absence of the artifact_. A common example is the abacus: as it's widely known, people that become proficient at using the abacus for performing arithmetic become better at these tasks even in the absence of an abacus. To some extent, they are able to internalize the abacus. Compare, of course, to the use electronic calculator; lose your calculator and you're back to square one, or perhaps worse off than if you didn't ever have it in the first place. Another example: maps are complementary for most people, whereas step-by-step GPS directions are competitive.

See where this is going? I'd like to make the argument that go links are complementary cognitive artifacts. 

To see this, ask yourself: where is the go link stored? It is somewhere in a database or an HTTP server configuration for an HTTP redirect, of course; and, sure, if you lost that data, you would not be able to retrieve the target anymore. In that sense, for that function, they are competitive. But an often used go link is *also* in your head, and you can easily operate with it in some ways -- even while far away from a computer or an internet connection. You can tell people about a go link; you can write it down on a piece of paper; you can tattoo it on you (you should probably only do this if you can trust whoever runs your instance). All in all, the go link can be operated on in many ways by virtue of the fact that you remember it. And you will remember it often, even without trying -- you may need to use them for a while to believe this, but setting up and using links in spaces interesting to you (and you tend to link interesting things by definition) is clearly reinforcing in my experience.

Note that the alternative to using go links for many use cases is *not* to save and store the target URLs, but rather not to use URLs at all; to rely on search instead. You can notice this every time you ask for a document, or try to surface a document for someone, and find it takes a number of steps and involves opening up an interface (say, Google Docs) and searching. In this sense, giving a resource a go link replaces a relatively unstable procedure in your working cognitive space with a constant operation -- dereferencing the go link retrieves an item. It's a valuable optimization. In my experience it adds up. Once you see this and "get" go links, they become indispensable. They have sticking power. I miss them when I'm not in the day job and have thus spent some of my free time replicating them with [open source tools](https://trot.to).

# Social knowledge graphs
Now, we've covered some social aspects and some cognitive aspects of go links as a tool. This section is a bit of a synthesis of both: I'd like to make the case that go links are a reasonable platform to build a _social knowledge graph_ [^skm].

[^skm]: <https://dl.acm.org/doi/10.1145/3331184.3331410>

Think about it: the users of a go links instance link resources. Some of the resources are "owned" by them in some way -- say, they are the authors of the Google Document, the blog post or the tweet that is being linked. This creates a transitive user-thing-user relationship that can be modelled as implying a user-user relationship. Furthermore, users might also use go links set up by others; this defines yet another relationship of this kind.

Thing-thing relationships are where things get more interesting. A go linked resource might include a go link to another resource in its body in turn. This can define a thing-thing edge in a knowledge graph; two interesting resources that are related. Taken as a whole, this defines a subgraph of the link graph that defines the web; one that happens to have been semantically annotated by users.

Note that there are social platforms, like Twitter, where power users constantly struggle to locate content they've seen before; search is woefully insufficient. Go links could work as a bookmarking tool in this context and be bootstrapped by this social function.

After that I would expect information-heavy communities like that that has formed around tools like [Roam Research](https://roamresearch.com) and [Notion](https://notion.so) to benefit the most. Go links can be a good way to share interesting or relevant information between users; the URLs that these tools (and many others) are often opaque. [Roam Research could even auto-Link nodes](https://twitter.com/flancian/status/1292161170565206016) marked as public, and offer users a way to cross-link nodes with other users' (see also the federation point below).

TLDR: Roam/Wikis/Docs/Twitter plus go links = lightweight distributed social knowledge graph that builds on these platforms but is not directly controlled by any of them.

# Extensions
If you accept one or more of the hypotheses implied above (that go links can be directly useful to users; that they complement existing tools and platforms well; that they might benefit from network effects), further venues for thought seem to open up:

 - In general, go links could function as a hub-like platform for any number of lightweight label-oriented cross-product integrations (see the Roam example above).
 - Hierarchical go links: multi-level/name-spacing.
 - go links feeds: you can subscribe to updates for go links -- or the resources they link. You can subscribe to subgraphs, as well; around things or people.
 - Federation: domains can expose some part of their URL space as go links space. <https://flancia.org/go> is precisely this. Participating domains can cross-link resources that have the same go link within their spaces, e.g. <https://flancia.org/go/go-links> and <https://anagora.org/go/go-links> are automatically linked to each other. Participating pages can include links to each other in a web-ring-like way.
 - go links actions: a set of standard operations that apply to go links or their targets. e.g. <go/share/go-link/person> could make <person> aware of <go-link> via some pre-defined channel. <go/ls/go-link> could list all targets for <go-link> that people around the network have defined.

# Applications
All in all, if you had a distributed social knowledge graph, what would *you* do with it?

I know what *I'd* do. I'd build an [Agora](link://slug/agora).

(See also: <https://medium.com/@golinks/the-full-history-of-go-links-and-the-golink-system-cbc6d2c8bb3>.
