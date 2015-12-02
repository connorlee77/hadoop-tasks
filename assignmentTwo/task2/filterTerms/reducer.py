#!/usr/bin/python

import sys
import collections

def printTermCounts(term, counts):
    for key in counts:
        print("{0}\t{1}\t{2}".format(term, key, counts[key]))

termCount = {}
prevTerm = ''
for line in sys.stdin:
    term, fileName = line.strip().split()
    
    if term == prevTerm:
        if fileName in termCount:
            termCount[fileName] += 1
        else: 
            termCount[fileName] = 1
    else:
        if prevTerm != '':
            printTermCounts(prevTerm, termCount)
        prevTerm = term;
        termCount = {fileName : 1}

printTermCounts(prevTerm, termCount)    
