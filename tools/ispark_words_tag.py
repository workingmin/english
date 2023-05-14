#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import nltk

if __name__ == '__main__':
    root = os.path.abspath(os.path.dirname(os.getcwd()))
    mdfile = os.path.join(root, 'ispark', '星火式.md')

    words = []
    with open(mdfile, 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            word = ''.join(filter(str.isalpha, line))
            if len(word) > 0:
                words.append(word)
    
    d = dict()
    for word in words:
        tokens = nltk.word_tokenize(word)
        tag = nltk.pos_tag(tokens)
        if tag[0][1] in d.keys():
            words = d[tag[0][1]]
            words.append(word)
            d[tag[0][1]] = words
        else:
            words = []
            words.append(word)
            d[tag[0][1]] = words
    
    # nltk.help.upenn_tagset()
    tagdict = nltk.data.load("help/tagsets/upenn_tagset.pickle")
    for tag in d.keys():
        dir = os.path.join(os.path.join(root, 'ispark', tag))
        if not os.path.exists(dir):
            os.makedirs(dir)
        newfile = os.path.join(dir,  "words.md")
        with open(newfile, 'w') as f:
            f.write("# " + tag + "\n\n")
            f.write("[TOC]\n\n")
            f.write("<br>\n\n")
            f.write("## definition\n\n")
            f.write("+ " + tagdict[tag][0] + "\n\n")
            f.write("<br>\n\n")
            f.write("## words\n\n")
            for word in d[tag]:
                f.write("+ " + word + "\n")
