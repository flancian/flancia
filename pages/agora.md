<!--
.. title: In Flancia there is an Agora
.. slug: agora
.. date: 2018-12-16 17:33:15 UTC+01:00
.. tags: flancia
.. link: 
.. description: 
.. type: text
-->

# Status

- This document was mostly written in 2018. The Agora was then just a thought experiment. It has since grown to be a living project.
- As late as 2020-10-17, the Agora barely existed as a concrete implementation -- it was not a single tool but rather many which you could use in tandem following a convention, which I provisionally named [Agora Protocol](https://flancia.org/go/agora-protocol).
- As of 2022-01-02, a reference Agora is online on https://anagora.org. Using terminology gained and derived in the last three years (with the help of the Agora community!), I can now describe it as a [[knowledge commons]].

Regardless of implementation details, an Agora can be assembled out of off-the-shelf parts available on the internet, mostly for free:

- Knowledge management tools used for the purpose of building a [distributed knowledge graph](https://flancia.org/go/distributed-knowledge-graph), following the aforementioned convention based on lazily evaluated [[wikilinks]]. See https://anagora.org/agora-editor for a review of some of the tools in this space, or [Roam Likes](https://flancia.org/go/roam-likes) for an older take.
- Social networks and the constructive bits of the internet as we have them, annotated and enriched using open tools and standards.
- An explicit constructive social contract. For reference you can consult [the anagora.org default](https://anagora.org/CONTRACT).

If you are interested in collaborating on building Agoras or similar constructive spaces, please reach out or peruse the [Git repository](https://flancia.org/go/agora-git).

See also: <https://flancia.org/go/agora-howto>, <https://threadreaderapp.com/thread/1322619094563258370.html>.

# Head
You can think of the Agora as a convention based social network; an optional, user-controlled annotation layer that can be applied over any internet platform which supports user-generated content. 

I think one of the best possible uses for such a network would be to use it to pro-socially maintain a [distributed knowledge graph](https://flancia.org/go/distributed-knowledge-graph) tailored specifically to the goal of solving problems: those of its users and society at large.

Its users, as a cooperative group, could by default take a naive but rational approach to problem solving:

  * For each problem in the set P of all problems:
    * Describe it as thoroughly as possible.
    * Maintain a set of known or argued possible solutions, S(P).
  * For each solution in S(P):
    * Describe it as thoroughly as possible.
    * Maintain a set of resources (people, time, attention, money) needed to implement it, R(S).

Individual users could also *declare* their views on the state of the world explicitly: they define which subsets of P, S and R they *agree* with, in the sense that they believe they are feasible, true, interesting.

Users that agree on their defined subsets can then efficiently collaborate on solutions as they become available by pooling of resources.

We apply some good old recursivity and seed the Agora with the problem of how to build itself. That is, how to build a system that allows participating users and entities to collaborate optimally in the face of adversity (such as biases, irrationality and even actual ill intent)[^charity].

[^charity]: To start with, discussion in the Agora should follow the tried and tested [Principle of Charity](https://en.wikipedia.org/wiki/Principle_of_charity).

The Agora should be built on a federated protocol to limit the harmfulness of diasporas. Groups might temporarily diverge in their views enough to want to run separate Agoras, but different Agoras should be able to cooperate on problems and solutions for which there is enough ideological alignment, and eventually merge.

# Tail

*I have a more focused and detailed unpublished document which will probably replace or complement this chapter soon.*

I know the premise sounds almost like a joke: what the world needs is a new social network. The internet and social networks are technologies we are just barely learning to live with, and the recent cause of a lot of polarization and political escalation and Trump Being President[^trump]. It doesn't sound at first like we should add another stick to that particular dumpster fire. But hear me out.

[^trump]: what if Twitter is already a decent Agora, and Trump just woke up to the fact that it's a superior meme transfer device sooner than others?

We need a designated place in the internet where we can discuss ideas in a constructive way. In particular, where we can discuss possible strategies to face the problems that humanity is facing. This is already happening, for sure; but is it happening somewhere on the internet where everybody can contribute? I don't think so. If the Agora exists already, please point the way -- I'd like to get there, and building it from scratch would be hard. The network of universities and institutes are the closest we have and I love them, but the Agora should be fully open and available to all over the internet, so every participating individual can contribute work and thought. Of course the whole internet could be an Agora; but the internet as a whole is chaotic and disorganized and thus its implicit Agora is entangled with places that are not constructive and not safe. There must be a better way.

Nick Bostrom has a [paper on existential risk](https://nickbostrom.com/papers/vulnerable.pdf) where he talks about a kind of lottery of ideas; humanity is constantly playing this game, the metaphor goes, and drawing ideas out of big lottery wheels of Science and Technology and Culture. Some of the balls in this wheel are colored white; these are good ideas. They contribute to human good, and we're glad we found them.

There are also black balls, though. These are bad[^30]. They are things that, on the whole, produce enough bad to be existential risks to humanity. Nuclear power *seemed* to be this for a while; perhaps mutually assured destruction could have resulted in an apocalypse. But it didn't! Aren't we lucky? If (and it's a big if) things stay this way, we got away with playing with something dangerous. Perhaps we can use the idea for whatever good it holds (cheap and relatively safe energy), or perhaps we decide to bury it underground in a big vault of ideas (this one doesn't have to ever spin again) that says Do Not Go There, Trust Us. For now, though, the idea might still turn out to be black; we could, perhaps, represent this situation as a grey ball of whatever shade we deem most likely.

[^30]: White = good and black = bad is in the original paper. Now, an apology: I don't like the fact that our culture encodes bad things as black, it's associated with death, etc. I think associating black with badness is a bit trite in a world that puts so much stock on being a particular kind of yellow.

We need a social network for discussing ideas. For talking about Bostrom's lottery urn, and what it has in it for us. In the Agora, we discuss ideas and their shades and merit; we discuss, first and foremost, ethics. We talk openly and clearly about how to best move forward as a society of humans, with the knowledge we've gotten and the resources we have.

What if social networks are grey? How dark is their shade? The high modernist in me wants to believe that the structured flow of information is more of a good thing than a bad thing. But we need to be cautious, and this is why I wrote this and you are reading it now.

I need your help.

<!--

If you're some sort of utilitarist: would you like to talk to others and have a stab at maximizing human happiness?

What if there's a way to maximize human happiness while also increasing everybody's happiness? What if there are Good ideas in that urn that everybody likes, or at least the majority prefers (if there is nothing better than democracy)? What if, taking incremental steps that everybody can live with, we get to a post-scarcity society? I think of a sort of average technological utopia where everybody in the world has at least a universal basic income, nobody starves, everybody is free to do what they want with their lives as long as they don't disrupt others. But you can picture your own utopia. That's the beauty of it! I'm not sure I'm right. Everybody can be wrong about mostly everything and still get by. But we only need to each contribute bits of vision, discuss, sometimes reconsider each other's positions. Try not to get that angry all the time. Sort it out.

Well, I'd love to be able to try that. I guess we all need to adopt, perhaps first build, some sort of ethics-and-culture-oriented social network where everybody can freely discuss ideas that don't infringe a minimum set of rules. The set of rules bit is going to be hard -- perhaps different people can even have different set of rules, and fully customizable filters? Unsure. The nice thing is that this place doesn't have to replace Facebook, or Instagram, or anything really -- it should actually leverage it in many ways. I picture as having pointers to your profiles, plus your story for each one if you have it:

Are you honest about what you post? How much? Are you playing a character? There was this story recently of an Instagram couple that proposed to each other in a fully orchestrated way, pretending spontaneity along the way, even though they had acquired sponsors for some of it and all. Perhaps we should talk about how real we want to be at a particular moment. Even if you're not an actor, you don't share all with everybody. It makes sense.

So this place would essentially be an agora, or a set of agoras (you know, this whole thing could just be Reddit, if Reddit just gets their game straight -- I like to think Google could pull off this kind of thing well, but perhaps I'm naive and that ship has sailed). Perhaps the Classical Greeks were on to something, you know. They have a pretty solid track record.

About this Agora:

1. You can share who you are, to whichever extent you want. I, myself, like to think I could go with fully honest. Or, I don't know, 99% honest? Perhaps we should have an honesty bar, just saying.

1. You write about your ideas, or about your positions with regard with certain things. Perhaps you don't think you have ideas; I'm pretty sure you do, everybody does. You might just not notice them, if you're not paying attention.

1. Everybody can participate.

1.. You cannot encourage or endorse any physical violence. About other kinds of violence: the network tries to ensure nothing violent according to your definition crosses your very explicit filters about the kind of stuff you want to even read about. We do this with filter bubbles now, but I think it needs to be very explicit and prominent so everybody can be happier and know exactly what's going on, as much as they want. It's just more ethical that way.

Defining violence is a problem in itself. In a way it ultimately stands for Bad. People will differ on what they consider violent or Bad, of course; discussing what is Bad (the filter itself) is sort of the point of the network after all.

The Agora is located in Flancia.

Because I believe the Agora is a Good idea (a white ball), I think it should exist. As far as I can tell, it doesn't, but I'm pretty sure it could exist, and the world would be better off for it. So I'll try to build it, starting by writing about it. And we should have this thing I described, this Agora; it would be a good thing. Sharing ideas, with the right system, can improve communication even with people you disagree on some, or many, aspects. What if we can somehow find a Middle Way?

Flancia, like I said previously, is a place. Because we do not live in Flancia (things sort of suck in reality; there are so many people in pain out there), it must also be just a site. It's this site. Welcome!

Flancia is also what you do with it. It's really up to you. Life is what we do with the privilege that is living; and with the real world privilege that we have somehow inherited. I guess this is what I do with my own privilege: mostly writing. 

Caveat emptor: most of what I have here is far from "ready". But if I were writing a book about Flancia, the place, these pieces would probably be in the first draft. Writing it would be akin to exploring it.

Here I want to write down the ideas that I have, the beliefs I keep, the good among the wrong. I think you should consider doing the same. I want to find a system to build this Agora, make it work, make it be a force of good -- whatever definition of good the people in it at any given time hold; perhaps the participants can eventually all or almost all agree on a reasonable enough, serviceable definition of common good. Then perhaps work on a plan to get there.

I started with a book, this weird book. You have to start somewhere, you know.
-->

[In Flancia there is no poverty](/poverty).
