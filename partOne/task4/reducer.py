#!/usr/bin/python

import sys

cachedPhrase = ''
cachedVal = 0
currPhrase = ''
for line in sys.stdin:                               # For ever line in the input from stdin
    currPhrase, val = line.strip().split('\t', 1)           # Strip whitespace in inputs
    val = int(val)

    if cachedPhrase != currPhrase:
        if cachedPhrase != '':
            print("{0}\t{1}".format(cachedPhrase, cachedVal))
        cachedPhrase = currPhrase   
        cachedVal = val
    else:
        cachedVal += val
    
if currPhrase == cachedPhrase:  
    print("{0}\t{1}".format(cachedPhrase, cachedVal))


    





