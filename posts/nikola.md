<!--
.. title: Nikola
.. slug: nikola
.. date: 2018-12-27 12:00:00 UTC+01:00
.. tags: tech, meta
.. category: 
.. link: 
.. description: 
.. type: text
-->

This blog is built with [Nikola][1], a Python-based static blog/site generator in the spirit of the more well known Ruby-based Jekyll. It's my first time using it ever, and my first time setting up any kind of internet facing website for some time. I'm liking it so far -- it doesn't get in the way much, and I can tailor the writing experience as much as I'd like. This is what the overall setup I ended up with looks like:

# Setting up Nikola
Pretty straightforward:

```shell
$ pip3 install nikola
$ mkdir blog
$ cd blog
$ nikola init
```

`nikola init` asked a few questions about the blog (address, title, etc.). It also offered the option to set up a comment system and I chose disqus, although I expect I won't be getting much in the way of comments anytime soon.

After this, you'll get a blog root with the following interesting files:

* `conf.py`, where all the blog configuration lives. You'll need to change this to switch themes, etc.
* `posts/`, a directory where each file will result in a published post (unless marked as a draft). Posts can be written in reStructuredText (which is the default) or a variety of formats. I use Markdown.
* `pages/`, a directory where each file will result in a one-off page in the resulting site. Pages need to be added to a map in `conf.py` too.

# Writing posts and keeping the blog updated
You can create a post by running `nikola new_post` in the blog root. But you can also just create a new `.md` or `.rst` file in the `posts/` directory, as per the above.

After each change, the blog must be rebuilt with `nikola build`. This updates the static version in `output/`. Then, changes may be deployed to the configured web root (specified in `conf.py`, same as as everything) with `nikola deploy`.

I'm lazy so I ended up writing a wrapper that just rebuilds and redeploys the whole thing when something changes:

```shell
cd /home/$USER/blog
when-changed conf.py pages posts -c 'nikola build && nikola deploy'
```

when-changed is a Python util based on inotify, installable with `pip3 install when-changed`.

I then [added the resulting script as a service to systemd][2] to make sure it's always running in the background.

# Serving the static pages
As mentioned above, `nikola deploy` deploys the static content to the web root (`/var/www/blog`), which nginx then dutifully serves in flancia.org.

This blog is HTTPS only, so I set up a redirect for port 80 in nginx. I'm using letsencrypt for the HTTPS certificate.

That's it, nothing fancy here.

# Ancillary stuff
* I use git for versioning posts and the blog scaffolding required by Nikola. I push it to a private gitlab repository from time to time as a way of backing up and being able to also write posts easily when I don't have an internet connection.
* I use vim for writing posts. It's old school, but I'm still the happiest writing in vim -- and in particular editing in vim. For some reason I really enjoy using vim and I otherwise don't use it for writing nowadays, as most of my writing at work is based on Google Docs. Being able to base my writing experience on vim was the main driver towards going the full geek approach instead of using something like Wordpress or even Medium.
* I wrote a sort of throwaway parser in Python to port my previous private diaries/idea dumps from a set of loosely structured monolithic Google docs to individual Markdown posts. I need to translate, edit and censor them, though, which is going to be the bulk of the work if I ever go that way (I'm still partially unsure about the kind of things I would like to write about here), so writing this script may have been yet another exercise in procrastination in a sense. At least it was fun.

All this is running in a $10/mo. micro dedicated server. Seems to work well enough.

[1]: https://getnikola.com
[2]: https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6
