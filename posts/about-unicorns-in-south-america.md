<!--
.. title: About OpenAI's unsupervised language model, or unicorns in South America
.. slug: about-unicorns-in-south-america
.. date: 2019-02-16 19:32:04 UTC+01:00
.. tags: ml, ai, gpt, unicorns, flancia
.. category: 
.. link: 
.. description: 
.. type: text
-->

I was very entertained by [OpenAI's recent announcement][1] (and [associated paper][3]) on their text generation model based on [Transformer][2] released earlier this week: "GPT-2". I wanted to jot down some thoughts on it, and probably go off on a tangent with some ideas prompted by it. If you haven't read it, I'd recommend you start by reading the announcement and browsing through the eight examples they provide. Note they are manually selected by a human, so we can safely assume many of the non-selected outputs were significantly less successful in following the prompts.

If some or many of the words in this paragraph don't really make sense to you, I encourage you to read the examples and wait for the "primer" below; it may be enough to follow along.

Who am I and why does my opinion matter? Well, in short, and to be clear: it probably doesn't :). I am a software/devops engineer working in a field not closely related to Machine Learning, who has only recently picked up ML as a hobby of sorts and (still?) doesn't understand the state of the art. I also have an (outdated, mostly irrelevant by now) background in linguistics, but no degree. Finally, I have an interest in writing both fiction and non-fiction. My thoughts on this field may (at best) be interesting to others because of this relatively uncommon composite background, but may just as well be irrelevant. So: caveat emptor. But here we go.

![Llamas at Machu Picchu](https://upload.wikimedia.org/wikipedia/commons/0/0c/Llamas_at_Machu_Picchu%2C_Peru.jpg "User:RedRobot [Public domain]")

# The shortest optional primer on ML you may find

I'm relatively new to ML, so this will not be an authoritative description. If you understood the first paragraph here, and the linked announcement, you can probably skip to the next section. I'm also not a great technical writer, so if you don't understand this paragraph, feel free to skip it. The rest doesn't really depend on it that much.

But very, very shortly: ML models are systems that learn from data (they are "trained") and then are able to succeed at tasks that are related to the data they learnt from. Importantly, when such a model works, it can make useful predictions related to the task at hand for new data. Models are usually classified as "supervised" or "unsupervised" depending on whether the data you give them as input includes information on what the prediction or result you expect from them is. The thing you want to predict is called a "label", so you can put it more succinctly by saying that you usually build supervised models with labelled data and unsupervised models with unlabelled data.

A typical supervised task is predicting quantities. Imagine a spreadsheet where each row represents a house in your neighborhood, and each column has some data about the house in question (these are called "features"). For example: area, number of stories, latitude and longitude, and finally price (the "label"). With enough rows representing actual houses, you can build a model that then predicts the price of a home not listed in the spreadsheet (say, yours) based on the other features.

A typical unsupervised task is clustering: you give a model a list of items of different kinds, and their features, and the model learns to group the items according to their qualities. Imagine a spreadsheet where each row is a fruit, and you have features such as colour, weight and shape. You don't have the name of the fruit for any of these (you could build a supervised model if you did), but even without knowing the name (or knowing that names are somehow relevant to the task) the model can learn to group together heavy, oblong, green fruit (watermelon?) and lighter, roughly spherical, red fruit (apples?).

The model we're discussing today is unsupervised, as it learns from a huge database of internet text that doesn't include any labels -- any explicit information on how to construct new texts successfully, or about what makes a "well constructed" text. But it still manages to learn something that feels significantly more complex than just grouping similar webpages together (which would be closer to the fruit example), or other classical unsupervised problems in this space: it learns how to produce new texts, basically by trying to predict how a text (provided, called prompt) is most likely to continue. Note this is a common approach in Natural Language Processing (NLP for short). [Other articles have been written by people better qualified than myself][10] about how exactly this model fits in the overall development of NLP; consensus seems to be that it's an improvement, but not necessarily a breakthrough, and lots of the discussion has actually been about how OpenAI may be trying to gather more publicity that they should by not fully disclosing the model (potentially over-hyping it).

# On the literary merits of the texts produced
I want to start by considering the samples provided as texts, setting aside for a minute both the technical details of how they were generated and the context in which they were produced and released. Reading them, and discussing them with friends, was enjoyable in its own right. The texts themselves take turns at being better and worse than I expected, which is fun. I got the feeling that the model was taking good and wrong turns, and you could tell which were which -- we can tell, but the model can't, as it has no feedback overall on whether what it's producing makes sense or not. It's just trying to produce something that seems likely based on the prompt given and the corpus it was trained on (the internet).

In a sense, and if you allow me to anthropomorphize it for a minute, it sometimes writes like a child. Particularly striking was [sample #6][4], which starts with a homework prompt, and then proceeds to make sense at times and also go off rails at others. You could picture a child with a short attention span and no knack for editing/re-reading turning an essay with some of the same mistakes the model makes. Why is that? One possibility is that it's seen many homework papers, and it's just remixed them into this. Another is that it picked up on the style of such tasks, and it's riffing on it. Without going deeper into how the model works, it's hard (for me anyway) to tell; also, many of the most successful ML models score low on explainability -- meaning that you can get them to work, sometimes surprisingly well, but then have no clue when you need to explain how they work on a per-part basis (in the case of a neural network, which has many neurons organized in layers, that would mean knowing how each neuron or each layer is "processing the input"). So it may or may not be possible.

Leaving all this aside, I liked picturing GPT-2 as a child -- a child that is in awe of the internet; it has just read all of it and doesn't know what to distill of it. Even if "all" the model is achieving is remixing existing ideas and expressions from the internet, it could already be an interesting new way to explore the internet and somehow detect patterns in it. At some point it mixes up Lord of the Rings and Star Wars -- is this because of some pre-existing fanfic, or has it noticed how they are in many ways the same? In the Lord of the Rings spoof, where did the turn of phrase "I take nothing -- but I give my word" come from? Is it somehow new or is it in common use and I just don't know of it?

# On mistakes and creativity 
I have to point out here that the same mistake that ruins an essay or an article may enrich fiction. Essays and articles are grounded in reality, where there is right and wrong (to some extent -- I don't want to get too epistemological here). An essay that is untrue is not a good essay; an article may espouse an opinion that you disagree with factually and still be interesting, but probably not in the way the author intended.

Fiction, though -- fiction is not as anchored by truth and falsehood in the same way. Fiction always contains a set of falsehoods, although which falsehoods are allowed is determined by its genre. In genres where worldbuilding is paramount (sci-fi, fantasy) internal consistency is more important than consistency with the real world.

Consider [sample #1][4], about an expedition that finds unicorns in South America. Sure, the prompt is already wacky, which probably helps -- the model may generate a fair amount of wackiness by itself at all times, so having it in the prompt may make it seem more consistent that it usually is. But the model doesn't miss a beat -- even several paragraphs after the prompt, it's still mostly on-topic, adding relevant details to the overall story: the unicorns originated in Argentina specifically; they have four horns; they not only speak English, but they have a common dialect ("or dialectic").

It has some misses, at least from the point of view of coherency. It mentions "people who lived there before the arrival of humans". And by the last paragraph aliens make an unexpected entrance, although honestly by then it may even add to the charm. Overall I think it works remarkably well as a short story.

Creativity is known to be linked to the ability of making mistakes and learning from them. Even if this model, or its successors, were seen simply as tools for making (somewhat informed) mistakes, they could be useful in aiding creativity. The surrealists were known for making use of mistakes when creating works of art; In writing, the "[exquisite corpse][6]" technique even reminds me a bit of Markov chains -- simpler generative models that estimate the probability of some next step in an evolving system based only on the current state. If this or similar models can even just reproduce that level of creativity, they may be useful already. But they may be able to do more.

# Building on this
OK, so let's assume we do want to use the model's mistakes to aid creativity in some shape or form. How to do so?

A "Writing Assistant" is not a huge stretch of the imagination. You write part of a short story in an UI (or your text editor of choice, with some plugin), then you generate a few paragraphs with the model. You review them, keeping the best and ditching the rest; perhaps even rewrite them whole, just keeping some idea. Then you repeat the process next time you are stuck, or feel like the story needs a turn.

We can do better than this, though. We can point out to the Assistant where it went wrong, and where it went right. A mention of erotic asphyxiation in a story for kids? That's a no-no, with some nope on top, please. Zombies in a period piece? [It could happen][7], but perhaps not today. The protagonist's partner suddenly develops a single-minded passion for mastiffs? Sure, OK, show me what you got. Imagine highlighting sentences and turns of phrase and volunteering critique as feedback (pressing some buttons).

What to do with this feedback from the user? Use it to build a better model, if we can. The feedback is a label, in a sense. My guess is that we could focus on building a separate model, call it an Editor, and have it mediate the production of the Writing Assistant. That may be preferable to trying to incorporate the feedback directly into the Writing Assistant model, as simpler models are easier to understand. In this system, the Writer explores but also makes mistakes -- the Editor points them out and sometimes asks for a redo. The output that reaches the user (the human) is now slightly better, and the process continues.

In ML, having great data is a bit like the Holy Grail. Everybody wants a huge amount of high quality labelled data; if you let it happen, you can end up being overoptimistic about the quality and quantity of your data, and then you run into reality and your model often doesn't train well. In reality data is scarce in many fields, and producing the labelled datasets that you want is hard and expensive. If this Assistant was useful enough, and lots of people used it, labelling could keep pouring in. We've set up a virtuous circle in which humans extract value from the act of labelling.

# The future of fiction
So, now for a bit of futurology: it may very well be that this way "AI" cracks fiction before other kinds of texts, and way before general AIs happens. There's certainly precedent to this idea proper -- Lem's amazing [Cyberiad][8] covered this (and much more) back in the 1960s. If the Assistant approach works, though, we could imagine having a path towards this. I'm skirting over lots of complexity, certainly, but if the quality of the generated results keeps improving based on users' feedback this could at least presumably and eventually happen. The generated texts could become readable over longer spans, approaching the length of longer stories and eventually novels -- even as the human-provided prompts become shorter and shorter.

In the most extreme case in this line of thought, you could imagine a prompt being just a title -- by which point the human user becomes a reader, not a co-writer. 
Ad-hoc fine tuning could also be worth doing once the general model is good enough that biasing towards styles is feasible. How much would a model that generates half-decent Tolkien be worth to his fans?

![Unicorn llama](https://upload.wikimedia.org/wikipedia/commons/2/29/Unicorn_llama.jpg "Amberbunting [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)]")

# Futurology
Thinking about the order in which breakthroughs in AI may happen seems potentially important; it's futurology, of course, but AI being a mathematical field it seems that speculation may be sometimes warranted. Sciences seem to advance in part by performing some amount of meta thinking, which we sometimes call philosophy. It *could* be that text generation ends up having a significant role in the advancement of our knowledge in years to come. It could be that it's a big thing; some people believe it. It's a stretch of the imagination surely, but let's suspend disbelief and assume for a second that it's a line of thought worth exploring.

You may have noticed I wrote AI between scare quotes in the previous section. I did this because ML is not AI, although it's usually seen as a path towards AI. ML may let you build agents that perform specific tasks, mostly around prediction, whereas AI deals with the harder problem of solving general intelligence. But it's all in a spectrum, and a set of models that collaborate to produce an output that exhibits a human quality (creativity) may fit the name even if it'd be hard to argue that the result is generally intelligent. This at least fits well within Minsky's vision of the human mind as a [society of agents][8].

So: if writing fiction did indeed fall to this carefully scoped definition of AI, what would that tell us of the probability that general AIs is to follow -- if anything at all?

One way to think about this is to imagine a subsequent breakthrough that allows a new version of the system to produce output that veers away from fiction onto non-fiction; onto writing about the real world. You could imagine the introduction of a new agent, Fact Checker, that works alongside (or after) Editor and pushes back on non-factual or at least non-checkable information. If such a system worked, it could perhaps perform some of the tasks of an entry-level journalist. A human journalist could probably help steer it in the right direction, too. The journalist would collaborate with the AI, as the human did with the first version of the Writer -- as an editor, before the Editor existed. Just one level of abstraction higher. An expert.

Going in a different direction, opinion pieces could be generated in a similar way; just substituting human opinions for facts. Imagine prompting the model algorithm with a topic or high level idea you'd like to explore: "gamergate was bad". The computer may construct a variety of arguments, some incoherent, some a possible derivation or composition of thinking around the internet. It may thus generate viable ideas that warrant being explored further: "gamergate is somehow related to the end of democracy". Or something inane: "gamergate has to do with zombie unicorns". The user chooses and the model explores.

At the point in which you can generate an AI that produces fact-checked or opinion-based texts, you can probably specialize said AI in different fields. Alongside the Fact Checker could work an Undergrad or Engineer, which is always trained on all the newest papers and can help produce entry-level articles about the latest developments in a field. Guided by a human doing the same job, at first. This human could be said to be an agent in this system -- the Expert. With each iteration, the Expert keeps being promoted to a superior level of abstraction. Hopefully to an interesting ending.

At some point in the process assisted writing may start to feel just like assisted thinking. Perhaps with such a tool we could think of new things; more people would be freed up from relatively mundane aspects of their day jobs and daily lives, and could think about new things with the gained time and focus -- or just be happier. Eventually this could result in improvements in some fields of knowledge. Like AI.


 [1]: https://blog.openai.com/better-language-models/
 [2]: https://arxiv.org/abs/1706.03762
 [3]: https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
 [4]: https://blog.openai.com/better-language-models/#sample1
 [5]: https://blog.openai.com/better-language-models/#sample6
 [6]: https://en.wikipedia.org/wiki/Exquisite_corpse
 [7]: https://en.wikipedia.org/wiki/Pride_and_Prejudice_and_Zombies
 [8]: https://en.wikipedia.org/wiki/The_Cyberiad
 [9]: link://slug/minsky
 [10]: http://approximatelycorrect.com/2019/02/17/openai-trains-language-model-mass-hysteria-ensues/
