#!/usr/bin/python

import sys
import collections
import math

#Global variables for finding tf-idf of other documents
N = 17
DOC = 'd1.txt'

def initTermCount(doc):
    return {doc : 0, 'other' : 0}

def getScore(scoreParams, doc, n):
    tf = scoreParams[doc]
    #If tf is 0, then tf * idf is 0 so adding 1 to scoreParams['other'] is fine
    idf = math.log10(float(n) / (1 + scoreParams['other'] + 1))
    
    return tf * idf

def printScore(term, doc, scoreParams, n):
    score = getScore(scoreParams, doc, n)
    print("{0}, {1} = {2}".format(term, doc, score))

scoreParams = initTermCount(DOC)
prevTerm = ''
for line in sys.stdin:
    term, fileName, count = line.strip().split()
    
    if term == prevTerm:
        if fileName in scoreParams:
            scoreParams[fileName] += int(count)
        else:
            scoreParams['other'] += 1
    else:
        #calculate score for prevTerm
        if prevTerm != '':
            printScore(prevTerm, DOC, scoreParams, N)
        prevTerm = term
        scoreParams = initTermCount(DOC)
        if fileName in scoreParams:
            scoreParams[fileName] += int(count)
        else:
            scoreParams['other'] += 1

printScore(prevTerm, DOC, scoreParams, N)

