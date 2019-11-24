<!--
.. title: Simulation
.. slug: simulation
.. date: 2019-08-27 15:52:07 UTC+02:00
.. tags:
.. category: 
.. link: 
.. description: 
.. type: text
.. status: draft
-->

I sometimes wonder if we are not all characters, or (using a metaphor which is very apropos at the time of writing) processes. Perhaps characters, people and processes are aspects of the same thing. Or possible instantiations of one another. Perhaps a character in a movie is in a way sad when they cry, and feels horrible just when they're about to die when the plot requires it. They are a kind of process, like we are -- just not one very well described, because of limitations of the medium. Their qualias exist, but they are perhaps weaker than ours. Did you get that? If not, it's alright. We'll be on the same page someday. Now please read this short story:

You once watched a movie in which a character first cried and then died, and you remembered it when you read or wrote the previous paragraph, and now you're reading or writing something that someone calls a short story on the internet. Really, that happened. 

I'd like to simulate utopias; that is, simulate worlds unlike ours. This means thinking about them, writing about them. But perhaps also building software models that can, in some way, actually simulate them. It's fine if you don't know how to do it; I don't know how to do it myself, right now. But I intend to try to figure it out, even if I'll always be limited by my knowledge and capacity. I may also just write about simulating an utopia, and plan for how to do it, and it might not ever work in any useful sense; but if you read it as a story, and believed me for a second, did it really not work? If you dream about it with me, perhaps that is enough. Everything is fiction and non-fiction at the right place, at the right time.

Is life a dream? Where are we? If we are all in a way just processes, or characters, or people (whatever that means) -- are we destined to always halt, stop being performed, die? Or can we endure?

So now we keep writing and reading together, all together; we are all writers and readers in a blog post, book, social network, simulation; we are all interested in solving some unknowns, and helping each other. You read a post that your husband made you read in a very annoying way; or you read something that someone pretentious with 15 followers on Twitter linked. Or just something that you found on the internet. This is what is happening now. You did your laundry, perhaps -- you're fine. You're a functioning member of society. But now you decide you'll write stuff, in the beginning only for yourself -- perhaps forever for yourself -- but that is a lifestyle too, I guess. You may also just read, perhaps save the writing for later, or for somebody else. That is fine too. I myself woke up today and decided to to start writing and become an Utopian. But did I choose it? What is free will? Did I really chose to be the person that decides to write down *his deepest thoughts*, that risks being called a crank or pretentious or egocentric? Perhaps I didn't choose it, and you didn't choose to read it, but here we are together now.

I'll call reading and writing just talking, because we are both here, reader and writer, and communicating with each other; it's close enough to talking. What should we talk about?

I'll call my project an utopia then, even if the term has historical baggage, or precisely because some of the baggage makes sense to me to adopt.

With the risk of alienating some of my better educated readers (just groan and move on; it won't last long) I have to clarify that utopia means not-a-place and not a beautiful place; the latter would be eutopia, which is another word that Thomas More used. The two fused at some point, and utopia ended up with the meaning of eutopia, in particular as opposed to dystopia. I think this ambivalence may be a good thing, because as I said earlier, I'm unsure if what I'm doing is the right thing or it will work out at all. Perhaps someday someone better than me will actually produce an eutopia out of their utopia; until then, I see an utopia as a plan and an intention, an unstable arrangement that must resolve into eutopia or dystopia or just nothingness eventually.

When we think of the world we do it through models, even when we're not aware of it; the world in our minds is not the real world, but it resembles that of the real world in enough ways to be useful (evolutionarily, socially).

What I'm interested in is not only the end state, but also a way of potentially getting there. For this purpose, I plan to build an explicit model of the world, and of the utopia, or both at once; this is, I know, a crazy undertaking, but in failing I will succeed according to my definitions.

Thus I will do the following: start an open source project in github, choose a language (possibly Python), and get on it -- design an architecture to model my project. If you don't know what I'm talking about specifically, don't worry about it: it means I intend to write part of this model as code, and part as human readable text; hopefully over time the two parts will converge. Allow me to explain further:

I will model objects in a world -- a very limited world to begin with; think of a grid. Objects will have properties and may react to the environment; some of the objects will also be agents, in the sense that they will act of their own volition (for some definition). I expect each object that acts o reacts to the environment to look like this:

 - Python code that implements actions. This is, basically, hardcoding of behaviour that humans actually sit down and write for the object in question.
 - Neural networks that implement object-specific actions, or aid in the implementing of actions: pattern recognition with a convnet, action suggestion with deep Q networks trained with RL, natural language generation using transformers, etc.

We'll also need a protocol for objects to interact. Nothing necessarily fancy -- perhaps core Object Oriented concepts built into Python will suffice for a while. If we ever get to model humans (to any extent, even if risible) I could see having them using natural language to communicate directly; then they would be something like chat bots who also have some awareness of an environment. It should be fun.

Eventually I'd like to apply ML to the hardcoded facet of agents; think genetic algorithms that introduce code mutations and evaluate fitness of the resulting agents.

This is a naive simulation; it may, at best, top out at the stage of making a reasonably fun game (for nerds like me). Simulating intelligence has been tried many times before, starting in the 60s (and way before, if you count non-implemented projects); it's always failed, of course. I could see it being more successful now, to some degree, by virtue of us having access to more advanced deep learning architectures now. But for all I know this has also been tried thousands of times already.

So why do it?  

Well, I think it's a useful exercise, even if it won't work for any useful definition of the word. We can learn something from it. And we can use it as a model to learn to think in new ways of the world.

I plan to call the codebase, this naive simulation framework and implementation, *utopia*. It will model, no matter how simply, a place that doesn't exist. With it I hope I'll also be able to model Flancia, one of many possible places; the one that is, to me, both an utopia and an eutopia.

Previously: [relics](/relics).

Next up: [fiction](/fiction).
