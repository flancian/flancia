<!--
.. title: In Flancia there are no walled gardens
.. slug: flanbook
.. date: 2020-08-30 18:00:15 UTC+01:00
.. tags: fiction
.. category:
.. link: 
.. description: 
.. type: text
.. status: 
-->

In Flancia the internet is truly open: they managed to get rid of [walled gardens](https://en.wikipedia.org/wiki/Closed_platform). How they did it is an interesting story.

# Status quo

Let's take just one example; it should suffice to represent the general approach they took. In Flancia they had a social network -- well, they had many of course, same as we do, but one in particular had grown into dominance. People had sort of liked it at some point, then eventually didn't anymore, but they were stuck with it by then; it had developed at just the right time in internet history, and it had done enough things right in the beginning to take over from contenders and really soar in usage. 

As it often was the case in those days, this network was fully controlled by a single corporation, and although at the beginning there were some provisions in place that made it look like a relatively healthy platform eventually the company had chosen to consolidate their dominion; namely close down APIs and turn it into a walled garden. By then network effects had taken over and de facto locked people in, too: the company had gotten users to build up an expansive social graph for them and had succeeding in retaining control over it. They proceeded to use this virtual monopoly on many users' social capital and attention to make billions selling ads -- and gained the ability to significantly steer public opinion in the process, too. Many people recognized problems with this approach, but users at large mostly kept using it. It was that or being locked out of a significant portion of social activity online and offline. 

# X marks the spot

One of the obstacles that Flancians faced when trying to improve on this status quo was that there was no single clearly better platform of choice available; in areas where there were some alternatives there were often too many, so the competitive landscape was fragmented, and that played to the company's advantage. The company also used their ad-fueled wealth to buy most promising contenders and offer them as relatively empty alternatives to their main network, while effectively gaining access to more social data and expanding their influence. After a while network effects and inertia were so strong that competitors all but stopped trying; social networks are known to be hard to decamp from, as most of their value is in the social graph that users build on them; and the oh-so-valuable graph was kept very deep within the company's walled garden. 

Flancians didn't have much when facing this dire state of affairs, but they had one thing, and it was an important one: they had [a machine for solving coordination problems](link://slug/agora). So they used it. First they sketched out a declaration of intents flowing naturally from their publicly espoused values.

 - Useful internet platforms should be open.
  - 'Open' means that no single monolithic entity can fully control them and that their inner workings are transparent to interested parties and appropriately malleable.
  - 'Open' is desirable because otherwise monolithic egotistical entities can gain control of the network and extort value out of its users, or mislead them.

Then they proceeded to write a plan together. The first version was remarkably simple; a sketch to get the real discussion started. It said essentially as follows:

 - For each useful internet platform X that is not open:
  - Let X' be its open replica.
  - Write down a plan to reimplement its core functionality, F(X') ≈ F(X).
  - Write down a plan to reproduce its critical data set, D(X') ≈ D(X).
  - Add X' to the [Catalog of Missing Devices](https://anagora.org/wiki/Missing_Devices) in the Agora. This both marks it as a canonical replica of X and announces it as a priority for Flancians.

Once this bootstrap process was complete, the standard Agora algorithms took over; Flancians would best-effort iterate, improving on plans and resource estimates and executing actions as available to them, until failure or convergence.

Social networks were useful internet platforms; the Agora, after all, was in many ways a social network (a focused, goal-oriented one). So Flancians set out to replicate the company's social network. They named that particular X' *Flanbook* -- after [The Book of Sand](https://en.wikipedia.org/wiki/The_Book_of_Sand), of course. It was fitting because the task of replicating it seemed at that point in time infinite in scope.

# I(X')
Looking around, it turned out that Flancians were relatively lucky. Most of the tools and libraries needed to build an open replica of the social network were available off-the-shelf. From all its algorithms, its ranking algorithms were perhaps the most sophisticated; but Flancians intended to replace those anyways, thinking the community could do better, so that was not an issue. The road to I(X') was not trivial by any means, but it wasn't very interesting for the purpose of telling this particular story.

# D(X')

In the case of social networks, then, it followed that most of their value was in their data; and, from all their data, none was more valuable than their social graph. Here Flancians had an ideological advantage, albeit perhaps not strictly a legal one to begin with, as they were known to often burst into chant in unison in barely appropriate occasions:

*This, which is our data,<br />
will always be our data.<br />
A Flancian and their data<br />
shall never come apart.*<br />

This somewhat awkward ritual came handy sometimes, though. Flancians strongly believed that any information they produced and maintained was theirs; they believed this almost as much as they believed in the Agora. To a Flancian, the idea of their part of the social graph (the piece they had contributed a node and edges to) being out of their reach, locked down somewhere deep in a walled garden, just didn't make sense. They refused to take it. So they just agreed to take their data back.

To perform this kind of task in a scalable way, they built special devices called *syphons*. The simplest came in the form of browser extensions. Whenever a Flancian used a targeted service X, the syphon redirected relevant data in the background to the replica X'. This allowed building up D(X') incrementally so it could eventually function as a drop-in replacement. Flancians agreed to use these devices any time they could in platforms being replicated, even when they were not otherwise directly involved in the replication project.

Now, Flancians are an altogether friendly group, and they have the added advantage of knowing how to use an Agora; but they still do sometimes come into disagreements. Here Flancians disagreed with each other in how to define *relevant* in the above paragraph. Some Flancians, believing closed platforms to be actively dangerous to society, took the position that *all* data could be considered relevant in the noble pursuit of replicating such platforms, and consequently took a relatively aggressive stance and built and used syphons that actively sought to crawl and extract the largest portion of D(X) possible as fast as possible, regardless of provenance of data. Other Flancians, mostly aligned with the Middle Way, built syphons that only extracted data that they could strongly claim to be *theirs* to begin with, according to a shared and public definition:

 - If the user of the syphon added the node or edge, it is considered relevant.
 - If a non-Flancian added the node or edge, and they give explicit consent to extraction, it is relevant.
 - If a Flancian added the node or edge, it is relevant (Flancians consent by default to the rational constructive actions of other Flancians).

The second approach introduced the additional problem of identifying users across platforms and tracking consent. The syphons offered cross-platform validation as a feature; otherwise it could be manually accomplished by cross-posting tokens and declarations of intent publicly in the relevant networks.

Once this system was in place, it would presumably make D(X') converge into a usable dataset.

The company, of course, put up a battle. They correctly identified X' as an existential risk, and sought to attack syphons and their users. This started an arms race. Both groups of Flancians were affected differently, with those subscribing to the Middle Way being on more solid legal footing. The fact that Flancians had enough resources and a platform to organize a united resistance (the Agora) helped them tremendously; also helpful was the fact that relatively small but dense parts of D(X') were sufficient to bootstrap smaller social networks within the network.

It would be perhaps unwise of me to say at this point which group fared better in the end, and precisely when and how the first replication project was brought to effective completion. Suffice it to say that Flanbook was a success, at least for a while, and it remains somewhat popular among the more old school Flancians. I, myself, am more partial to Instaflan.
