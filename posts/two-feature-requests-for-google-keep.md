<!--
.. title: Two feature requests for Google Keep
.. slug: two-feature-requests-for-google-keep
.. date: 2019-05-13 23:41:24 UTC+01:00
.. tags: rant, keep, ml
.. category: 
.. link: 
.. description: 
.. type: text
.. status:
-->

*I wrote this a few months ago, but never got round to editing and publishing. Now I found myself on a long flight with some time to spare, so here goes.*

## A rant
Google Keep is frustrating — on Chrome sometimes I go to the Keep tab I keep pinned, and it turns out that I'm in a view that doesn't let me take any single action to get to a “create note” flow. Usually it happens when I'm scrolled somewhere into my stack of notes, or when I have a note I'm already working on. This feels, frankly, very cumbersome to me. With the disclaimer that I don't know much about UI/UX, and great people work at Google in these fields: I think this is probably not the right UI for this tool. When I get to Keep I'm usually trying to get what I want quickly, and that is one of two actions:

- Find (to read or edit) a note I've written.
- Write a new note.

Usually I'm in a rush: I'm in the middle of something and I need a note I've written in the past to finish the task; or I have just thought of something or found something and I want to write it down lest I forget (a number, a to-do, a random thought -- I'm a very forgetful person). I want Keep to be the tool that I can use for organizing my life. It shouldn't get in the way.

Unfortunately, Keep fails at both flows listed above in at least some ways. First, what I've already mentioned -- in several contexts, there's no simple way to get to one of the actions I want to take. I'd rather not deal with extra actions like scrolling and searching for the 'Take a note' text area, or pressing escape to exit ‘Search' when I've left Keep on the Search screen, or clicking on different UI elements to do the same. I think 'Search' and 'Write' should always be available, in every view, in a consistent way. Different always-present buttons (say a '+' to compose, like Gmail does?) seem superior to me.

On top of that, the mobile and web versions are inconsistent; whereas in web 'Take a note' eventually shows up at the top of the UI, on mobile it's at the bottom. They should work the same way in this respect. Perhaps mobile is closer to the right UI here, as at least 'Search' and 'Take a note' are in clearly distinct places in the UI.

## Details all the way down

I say this all not to shame the Keep designers and engineers, which I'm sure are brilliant. Designing UIs and writing software is hard. 

Let's assume for a minute that my gripes are representative of a significant fraction of the user base; if it's not mine that are representative, there are others like them. The designers and engineers pretty likely have a good feeling for what's wrong with their app, and in the back of their mind they dream of the time when they will be able to just go ahead and fix it. But the moment keeps slipping -- doing anything is hard, harder than you think, and any UX or architectural change probably takes them not just 10x but perhaps 100x of the effort they feel it *should* take. I know this is how I feel at my own job, at least.

Most software fixes are easy conceptually, but hard in practice. There's details everywhere that need to be taken care of; details all the way down. Change something into something else. Fix the callers. Fix the tests. Perhaps you need a refactor -- that's fine, our tools nowadays can help there. But they can't help with writing most of the actual new logic. Or with shipping a larger scale change (something that changes the server architecture) safely. Some day they may -- if that ever happens, programmers will be able to focus on different things. And software may be noticeably better.

## The wild part

Now for the wild part: I'm not an expert in tooling, but ML-enabled advances in software development tools could make some or most of the steps involved in shipping software changes automatable -- or at least assisted. I'm sure researchers are working on some aspects of these hypothetical toolchain that will get us there; and thinking about the others. I don't have any particular insight into the problem; but I wanted to think a bit about how some of the steps in this process could work, and what it would mean. What it would feel like.

Some wishful thinking: what would happen if ML could tackle parts of what we currently call programming? First of all: programming would probably be redefined, as it usually happens. It may end up being redefined many times as as ML iterates and infringes on this field of human thought, and human activity, the same as elsewhere. Eventually programming may cease to be about C++ or Java, and become more and about reporting the right bugs (in the right format) and sending the right feature requests to some fancy reinforcement learning coder-agent. It will then do the "mindless" thing — write the new method, fix the tests, submit the change and go through the process to shepherd the change through the release process all the way to production. Perhaps even monitor how well it works once it ships. It won't do everything in the previous list right away, of course, but even if it only helped here and there it would add value; these may turn out to be iterative improvements that happen as we progress in this field. I'm not sure about anybody else, but I sort of am looking forward to all of this, honestly.

How could a next generation code writing assistant look like? One idea might be to augment test-based development; you perhaps write the function signature, then you write tests for it, and of course assert what valid input looks like. Sounds familiar? Expected outputs in unit tests sound like a kind of labelling. A generative model (similar to GPT-2) could presumably be trained on a huge amount of code, and potentially learn the utterances that are most likely to yield the expected output. A programmer could probably look at failed solutions and give feedback on high level issues to be fixed, or mutations to be tried. For example: indicate that more code involving a variable should be written (that the programmer can see needs to be transformed in some way). Or, perhaps, add some intermediate logic that the programmer knows should happen eventually: do something for every element in an array; or define a variable with some descriptive name, as a hint that leads the model along the right path.

Anyway, I've added a to-do to my Google Keep list to investigate what the researchers are up to in ML-based code-generation/change assistance. As usual I'm writing mostly naively, and these ideas are very likely very old. But I find writing to be a good way to realize what I'm interested in -- what I clearly don't know, but would like to know.
