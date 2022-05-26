# -*- coding: utf-8 -*-

import nltk


def stem(word):
    stemmers = [nltk.stem.porter.PorterStemmer(), nltk.stem.snowball.SnowballStemmer("english"),
                nltk.stem.lancaster.LancasterStemmer()]

    stems = []
    for stemmer in stemmers:
        stems.append(stemmer.stem(word))

    return min(stems, key=len)
