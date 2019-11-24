#!/usr/bin/python3
# Hacky one-off script to chop up my existing idea documents into manageable posts. Just gives me an easier start.

import argparse
import copy
import itertools
import os
import re
from slugify import slugify

parser = argparse.ArgumentParser(description='Parse fuzzily-separated pseudo-posts in a big text file and output individual posts.')

parser.add_argument('file', metavar='FILE', type=str)
args = parser.parse_args()


template = """<!--
.. title: TITLE
.. slug: SLUG
.. date: 2018-12-01 00:00:00 UTC+01:00
.. tags: idea
.. category:
.. link: 
.. description: 
.. type: text
.. status: draft
-->
"""

def make_title(text):
    text = " ".join([word for word in text.split()])
    delimiters = re.compile(r'[.:;?*]')
    sentences = delimiters.split(text)
    if sentences[0] in ('Idea', 'Todo', 'TODO', 'todo'):
        return sentences[0] + ': ' + sentences[1]
    elif len(sentences[0]) < 2:
        return sentences[1]
    else:
        return sentences[0]

def mostly_alpha(text):
    alpha = len([char for char in text if char.isalnum()])
    total = len(text)
    if alpha < total/2:
        return False
    return True

def make_post(title, content):
    filename=slugify(title, max_length=40)
    dirname=args.file + '.output'
    try:
        os.mkdir(dirname)
    except OSError:
        pass
    with open(os.path.join(dirname, filename+'.md'), 'x') as f:
        temp = copy.copy(template)
        temp = temp.replace('TITLE', title)
        temp = temp.replace('SLUG', filename)
        f.write(temp)
        f.write(content)

def main():
    titles = []
    f = open(args.file, 'r')
    for k, v in itertools.groupby(f, key=lambda x: re.match(r'(^\S)\1', x) or x.startswith('—') or x.startswith('_')):
        section = "".join(v)

        if not mostly_alpha(section):
            continue

        title = make_title(section)
        titles.append(title)
        make_post(title, section)

    print("All titles: ", titles)
    print("Number of posts: ", len(titles))
    print("Number of unique titles: ", len(set(titles)))

if __name__ == "__main__":
    main()
