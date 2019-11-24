<!--
.. title: GPT-2 and Philip K. Dick
.. slug: gpt-pkd
.. date: 2019-03-24 17:02:19 UTC+01:00
.. tags: ml, gpt, literature, pkd
.. category: 
.. link: 
.. description: 
.. type: text
.. status:
-->

Since [my earlier take on GPT-2][1] there's been a steady trickle of articles about experimenting with it -- well, I should say GPT-2 small, as GPT-2 hasn't been released in full as we know. I wonder how much better the current batch of amateur experiments based on GPT-2 would be if they were based on the full model. Anyway.

[1]: link://slug/about-unicorns-in-south-america

The past weekend I read these two related articles: [gwern's experiment with generating poetry with GPT-2](https://www.gwern.net/RNN-metadata#finetuning-the-gpt-2-small-transformer-for-english-poetry-generation) and [slatestarcodex's coverage of the same](https://slatestarcodex.com/2019/03/14/gwerns-ai-generated-poetry/). Inspired by them I decided to go ahead and try my hand at some re-training of my own. I chose corpora that were interesting to me, albeit small -- so the risk of overfitting is big: 

1. All of Philip K. Dick's novels in Project Gutenberg (14), concatenated. I'll call the resulting model "PKD".
2. All of Jane Austen's from the same source (7), concatenated. I'll call this "JA", and probably cover it in a different post.

I count them both among my favourite writers, although clearly they are very different. I trained models on both corpora until cross-entropy was <1. It really didn't take long -- only about 600 iterations as counted by GPT-2's train.py, around 12 hours of training on CPUs (GPT-2 doesn't fit in my puny GPU), which seems awfully quick. I'm pretty sure this all means the model is overfitted, but of course I had to give it a try anyway. These are some lightly cherry picked results I got, but otherwise representative examples (say, 75th percentile quality wise, instead of the 50th percentile that you'd expect from a perfectly uniform sampling?).

# Unconditional Samples

Some unprompted results first:

> Reinhart touched his wristwatch. "Keep
moving. Wait until you see something." He pushed through the
tracking screen, into the main section of the ship.
>
> "I see what he's doing now. He started in a new city called
Sherikov's, about two hundred miles off. We're sure he's been
silent enough to him to know something was coming. He started up the
ramp at the same time."
>
> "Thank God." Reinhart snapped the screen off. "He'll come after
you, Commissioner. After all, he's just trying to get
his control."

The characters mentioned all come from novels in the corpus, and most of the verbs are used somewhere in it -- but I didn't spot anything memorized here, and names and parts of speech are being recombined in ways that sometimes make sense. I didn't write down at which stage in training this sample was generated, unfortunately, but the model seemed to focus a lot on one or two novels at an earlier stage -- likely because it was training on those first? I have written down a to-do to understand how the training samples are being generated.

> Nothing but a ruined building. A group of guards
> standing around him. A City beyond all Terrans--and
> his possessions. A place far off, a City set in the sky
> with a certain beauty.

I was impressed by "A place far off, a City set in the sky with a certain beauty." I checked the corpus and this wasn't memorized. This is one of the phrases that made me think "I could use that" -- something a writing assistant could produce for me, as per the idea in my [earlier post][1].

> "No. All she remembers is that he kept a goat."
> 
> "Oh?"
> 
> "He kept a goat?"
>
> "I remember he kept a goat. I was an officer in the goat's fleet. He was a
> little by the way. When we were younger he kept a goat."

PKD (the person) had a thing with animals (and paranoia, and mutants, and parts of the female anatomy...). I haven't read the novel in the corpus where the goat reference comes from, but I feel this managed somehow to capture some of his weirdness with animals.

> Major nodded. "That's what we're built to carry. The passengers are the very last to
> go, the passengers, the very last to leave Terra. All this is
> part of aplan."
> 
> "What are you thinking about?"
> 
> "The ship is guided by a living creature called
> by radioactive breath. But the pilot, none of us knows what it is."

Nice creepy/suspenseful last phrase here.

> "So what's the matter?" Kramer said.
> 
> "The brain is not conscious. It's only a habit."
> 
> "And what does it matter?" Gross said.
> 
> "It's the same old story, old and very old. But how can we
> break from the surface? Too old."

Ominous. As usual, I checked and none of the "ideas" here come straight from the corpus. So PKD seems to be working quite well so far.

# Conditional Samples
I couldn't resist prompting PKD (the model) with one of my favourite lines from PKD (the writer) that are not in this corpus. This comes from "A Scanner Darkly", which is not yet in the public domain.

> Model prompt >>> Stooping down, Bruce picked one of the stubbled blue plants, then placed it in his right shoe, slipping
> it down out of sight. A present for my friends, he thought, and looked forward in side his mind, where no one could see,
> to Thanksgiving.
> 
> He watched the whole thing from behind the wheel, the engine running through the fog, and the little girl slowly walking
> toward the car. He looked out the window.
> 
> Bruce sat there, silently, for a moment. He remembered his father's birthday party. He saw his father in the car. He
> felt sad. He felt sick. He felt miserable. He knew it was just a bad day. He felt hor rible. He didn't even know that.
> He knew the pain and the guilt that kept him from coming out. He needed something to live for.
> 
> He looked back down at the sun. It was cold outside. It was hard to see when his feet were shaking from the wind. He
> couldn't even remember the last time he had felt this way. He couldn't even remember the day he left his family and
> moved to Ohio. He couldn't remember how he felt. He couldn't even remember the day he moved to Ohio.
> 
> "Hey, Bruce," he said to himself. He looked at his father. He looked at his mother, who was holding the baby. He looked
> at his mother, who was crying. He looked at his father, who had been in the car fo r more than an hour, trying to calm
> his tears. He looked at his father, who was still weeping. He looked at his mother, who was crying. He looked at his
> mother, who was holding the baby.
> 
> "Hey, Bruce, I'm sorry," his mother said to Bruce. "Sorry that I didn't do my best to help you."

I think this result only sort of works. The rhythm of the phrases is quite good, even if it of course goes into a loop there at the end. It remembers the name. But it seems to forget about some of the other things that could have been relevant (and, in the novel, are): the plants, and his friends.

It begins to show what I believe is one of the issues with this model: it doesn't seem to react to "external" prompt elements (defined as names, or things, that aren't in the "retraining" corpus). For the sake of brevity I'll skip them here, but I have many examples of ignored prompts with outputs that look exactly like an unconditional sample. It's like PKD has forgotten about the world outside the new corpus. 

I have the impression this is because it's over-fitted, so it sort of tends to take a shortcut from any prompt back into one of its deep grooves -- so to speak. But I still don't understand GPT-2 or many others sophisticated models -- I'm more at the stage of implementing linear/logistic regression, solving MNIST in Tensorflow, and reading introductory books -- so I'm unsure if it's that or some deeper issue; I don't know how the process of retraining on a new corpus actually works yet (another to-do there). I think the knowledge of grammar and the language that GPT-2 brings to the table is still there, but other things are just gone. Hopefully I will get to a point in my ML studies where I can understand this problem better -- perhaps in a few months?

# Comparing GPT-2 and PKD
To test this hypothesis, anyway, I tried a few prompts in both standard GPT-2 small (which usually does quite well at picking up prompt queues) and PKD. In the following section, PKD goes first and GPT-2 "vanilla" goes second:

## Borges
> Model prompt >>> My favourite short story of Borges is
>
> that he
> would do something; you read, you took this book, this
> universe, and turned it around around."
> 
> "Wait," my mother said. "What did he say?"
> 
> "Nothing." He watched her struggling, trying to remember. "He said he'd do something."
> 
> "Wait? What? What? What did he say?"
> 
> "Nothing." He watched her silently. "What was he talking about?"

Not much here.

> Model prompt >>> My favourite short story of Borges is
> "The Time-Lost Manuscript," in which a ship's captain (Robert Duvall) becomes the villain of a short story, and the
> book's author is a character who never really existed. That's kind of the big story here. I think Borges was a very
> good, very funny man (and also one of mine). He had a very well received reputation for his wit, his writing. And he
> would make great characters out of his characters. But sometimes, though, you just don't believe in the character.             
>                                                                                                                                                                 
> [Crowd applause]           

The crowd bit cracked me up. Not sure where it came from -- perhaps GPT-2 dreamt this up as a sort of talk show interview? But in any case the effect is funny. Also, "the book's author is a character who never really existed" actually does sound like Borges or Calvino. So... a hit for GPT-2, overall.

## Fan fiction
> Model prompt >>> Darth Vader and Luke walk into a bar.
>
> The
> vidsender--it doesn't work."
> 
> "How did you happen to have an A-class leady come along?"
> 
> "The same old story. The leady after a heavy-set Erickson put a couple of
> systems back in the
> center of the street. The story doesn't fit.
> 
> "They say you didn't build it up, didn't they?"
> 
> "That's true," Bob said. "You didn't build it up
> up yourselves. We're going to have to do it alone. And if
> you do the whole thing again they'll be surprised."
Once again, PKD just ignores the prompt as far as I can tell.

> Model prompt >>> Darth Vader and Luke walk into a bar.
>
> They're talking about the latest episode of the hit Star Wars series, "Luke Cage," which stars Luke Cage and Ben
> Affleck.                                                                                       
> 
> "I thought, 'There's no way they're going to go to jail, and that's the only way they're going to get out,'" a source
> told THR. "But it's not like the show actually airs anymore. This was a time when Luke Cage was just something that was
> a part of the story and he was a part of the story. That's not how it's going to be."          

Here GPT-2 got the Vader right (it produces a mention of Star Wars), but the Luke wrong. But it's something; it was at least partially "hearing" me.

> Model prompt >>> Darth Vader looked at Harry Potter wistfully.
>
> "Do you think he--"
> 
> "The Old Man. I know he won't. I know it. I've seen his every
> vlog."
> 
> "How many of you have been watching?"
> 
> "I can count on one count." He reached into his coat. "Letters, all right."
> 
> The manila envelope was filling up. The Russians pulled him out of the room,
> toward the whiteboard. The message plate was on the wall, up the side of
> the wall.

PKD just packed up and went back to familiar territory.

> Model prompt >>> Darth Vader looked at Harry Potter wistfully.
>
> "Darth, I can't take this from you, you know you're a very handsome man," he said. "I need to see some respect for this 
> boy, and the respect that his family has for you." 
>  
> Harry Potter looked at Voldemort and said, "I'm just going to put my wand on him so I can take him to Dumbledore and get 
> his name out of his mind, but I'm not going to tell him what to do." 
>  
> Harry Potter said, "The truth is, you're not going to tell me what to do, but you're going to ask him questions. He's 
> going to ask questions, he's going to ask questions about you." 

GPT-2 nailed it. GPT-2 really jumps at the opportunity to write fanfic.

# Conclusion
PKD is always all PKD, and little or no GPT-2 -- it shows no general knowledge of the world. It's good for generating unconditional mashups of the corpus I've used, sometimes even interesting ones, but cannot react to a wide variety of prompts.

It seems I've succeeded at overwriting GPT-2 with PKD, at least in some sense. What I wanted to see from PKD's output in the previous section was Star Wars fan fiction or a Star Wars-Harry Potter erotic crossover (both of which clearly exist somewhere in the internet), written by PKD (ideally the human)... but I just got the ramblings of PKD (the model) instead. PKD is locked inside a room (a Chinese Room? Perhaps a Russian or Japanese one, in the case of PKD) producing rehashes of his old work instead of hearing me reaching out to him from the future.

PKD could produce a pastiche in which Darth Vader is a bit paranoid and fears his ex-wife, Padme, is collaborating with the Russians. But it doesn't.

Not yet, anyway.

# Update: 2019-03-26
By now I'm pretty sure that there was something wrong with my first model's training. After updating to the latest version in [nshepperd's github](https://github.com/nshepperd/gpt-2.git), I started a new training batch and I noticed that 1) it's *significantly* slower to train now, and 2) the samples in early iterations read a lot more like GPT-2, whereas before they looked like direct derivations from the "retraining" corpus from the get go.

These two things make me believe that there was a bug in my training process, or a disconnect between what I was passing to train.py and what it actually used (argument processing was one of the things that changed between versions). Could it be that I was training the model *from scratch* on the new corpus? I need to run some more experiments to see if this would even work with GPT-2, it seems like the training I did was not nearly enough to be able to produce relatively convincing text on its own. In any case, this may all invalidate my complaints about lack of generality above :)

I quickly retrained PKD to only a loss of ~2 and gave it another whirl. I got this:

> Model prompt >>> Harry Potter looked at the rocket and said:
> "This is a failure. Something has gone wrong. What are we going to do?"
> 
> Beside him, the others were moving back.
> 
> "I'm afraid not," Gryffindor Potter said. "I doubt it. We might as well go to the
> other side. After all, this is Terra and Mars."
> 
> "Well," said the Professor, "we'll just have to figure out what we're going to do."
> 
> They were moving away from the bunker, and he could see the huge
> projectiles moving away from the bunker. The Professor moved toward them.
> 
> "There it is," he murmured. "I suppose we'll find a way back. But--"
> 
> The Professor looked around. "It's all right, Professor. The whole place is
> wiped out. The whole town is decimated, destroyed and leveled, with
> the ruins of a village, the ruins of a town. The only way we
> can get back is by the use of the Terrans."

This is a decent enough cross-over. PKD2 latches on to the Harry Potter reference and takes names from it, but thematically this is otherwise close to PKD. So even though the fragment is not particularly interesting to read, I think it's an improvement in that sense.
