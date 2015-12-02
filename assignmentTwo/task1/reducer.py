#!/usr/bin/python

import sys
import collections
prev = ''
docs = collections.OrderedDict()
for line in sys.stdin:
    line = line.strip().split()
    
    if line[0] == prev:
        fileKey = line[1]
        if fileKey in docs:
            docs[fileKey] += 1
        else:
            docs[fileKey] = 1
    else:
        if prev != '':
            #print out the word + it's files
            fileList = '{'
            for key in docs:
                fileList += '(' + key + ',' + str(docs[key]) + '), '
            print("{0} : {1} : {2}".format(prev, len(docs), fileList.strip()[:-1] + '}'))
        prev = line[0]
        docs = collections.OrderedDict()
        docs[line[1]] = 1
#print out the word + it's files
fileList = '{'
for key in docs:
    fileList += '(' + key + ',' + str(docs[key]) + '), '
print("{0} : {1} : {2}".format(prev, len(docs), fileList.strip()[:-1] + '}'))
        
