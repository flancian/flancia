<!--
.. title: About Roam-likes
.. slug: roam-likes
.. date: 2020-10-14 20:02:45 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. status:
-->

Several people have asked me what I think is the best available open source alternative to Roam currently. I've procrastinated writing about this long enough; here go some relatively raw thoughts in lieu of a proper answer. I'll try to keep this updated.

# Foam
As of the time of writing I believe the best Roam-like is Foam (<https://flancia.org/go/foam>). At least that's what I'm currently using. Setup is a bit clunky, if only because it is actually an extension for a text editor, VSCode. But it's a really good text editor -- and I say this as a die hard vim fan, if you know what I mean.

First it was off-putting but now I think it being an extension is kind of genius. It makes it so that you can extend it and compose it with other existing extensions very easily.

Following <https://foambubble.github.io/foam/#getting-started>:

1. First, install VSCode: <https://code.visualstudio.com/download>.
1. Log into github, or create an account there if you don't have it: <https://github.com>.
1. Create an ssh key and upload it to github if you haven't already done it: <https://github.com/settings/keys>. If you don't have a key, on OS X and GNU/Linux you can just run ```ssh-keygen``` to generate it; the result (what you need to upload to github in this step) will be in ```.ssh/id_rsa.pub``` (could also be in ```.ssh/id_dsa.pub``` depending on your SSH version).
1. Create a new repository using the Foam template: <https://github.com/foambubble/foam-template/generate>.
1. Clone the repository in your computer, using the git client (if you have it) or the git extension in VSCode.
1. Open the repository in VSCode and follow the instructions. Accept installing the recommended extensions (Foam is actually a package of other extensions; that's part of its power). If for some reason VSCode doesn't recommend installing Foam, you can search for it and install it by pressing ctrl-shift-p and typing "install extensions".
1. press alt-d to generate a daily note. Then get writing! :)

If you add text [[that looks like this]], it becomes a link -- it's a [[wikilink]]. You can control+click to follow it, which will create a file if necessary or open it if it already exists.

Once in a while, commit your changes in VSCode/git. It will automatically back up your notes to github. If you want to keep them private, you should flip that setting on github.com.

That's it!

# A note on Athens
Athens (<https://flancia.org/go/athens>) is only in closed beta. Once it's out, it might provide the best out-of-the-box Roam-like experience; it is looking like it'll be amazing really great. From all the tools listed here, note that only Athens supports block references. If you care about them, you'll want to try it out.

# Migrating from Obsidian
I mean, you don't actually need to migrate from [Obsidian](https://obsidian.md). Obsidian is actually pretty great! I prefer Foam because of its extensibility and because it's open source; but I like Obsidian. Its community forums are also great.

I'd still recommend you commit your Obsidian repository to git; this way you maintain full control over it, and you can even contribute it to the Agora directly too -- functionally the whole setup can be very similar to Foam. You can just set up an empty repository in github, clone it in your computer, and then copy/create your Obsidian notes directory to it. After that you need to manually run git one in a while to update it:

```
$ cd garden
$ git commit -a -m "Some message saying what's in this commit."
$ git push
```

Remember to set your repo as private if you want to keep it that way.

# Migrating from Roam Research
You can export your database to Markdown, and import that directly into Foam or Obsidian. Obsidian even has a "Markdown import fixer" that solves some issues with it (unclear to me right now exactly what the list of issues fixed is).

# Agora
Now you have a digital garden of your own, please consider adding it to the Agora: <https://flancia.org/go/agora-howto>. The Agora contains a repository of digital gardens. With such a "digital forest" we could build a <https://flancia.org/go/distributed-knowledge-graph> by convention.

If you need help, please reach out to me anytime at <0@flancia.org>, <https://flancia.org/go/twitter> or <https://flancia.org/go/mastodon>.
