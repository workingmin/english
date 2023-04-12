#!/usr/bin/env python3

import sys
import csv
import getopt
from nltk.corpus import names


def usage():
    print("Usage: %s [OPTION]..." % (sys.argv[0]))
    print("  -t, --text=#")
    print("  -o, --outfile=#")


if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], '-t:-f:-o:-I', ['text=', 'outfile=', 'help'])
    
    text = None
    outfile = None
    
    for o, a in opts:
        if o in ("-I", "--help"):
            usage()
            sys.exit()
        elif o in ("-t", "--text"):
            text = a
        elif o in ("-f", "--file"):
            file = a
        elif o in ("-o", "--outfile"):
            outfile = a
        else:
            assert False, "unhandled option"
    
    if text is None:
        usage()
        sys.exit()
        
    tag = []
    tag.append(text)
    if text in names.words('male.txt'):
        tag.append('male')
    elif text in names.words('female.txt'):
        tag.append('female')
    else:
        tag.append('')
    
    if outfile is not None:
        with open(outfile, 'a') as f:
            writer = csv.writer(f)
            writer.writerows(tag)
    else:
        print(tag)
