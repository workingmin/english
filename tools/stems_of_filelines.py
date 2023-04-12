#!/usr/bin/env python3

import sys
import nltk


def stem(word):
    stemmers = [nltk.stem.porter.PorterStemmer(), nltk.stem.snowball.SnowballStemmer("english"),
                nltk.stem.lancaster.LancasterStemmer()]
    stems = []
    for stemmer in stemmers:
        stems.append(stemmer.stem(word))
    return min(stems, key=len)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: " + sys.argv[0] + " <file>")
        sys.exit(0)
    elif len(sys.argv) >= 2:
        file = sys.argv[1]

    with open(file=file, mode='r') as f:
        for line in f.readlines():
            word = line.strip()
            s = stem(word)
            print(s)