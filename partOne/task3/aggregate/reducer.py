#!/usr/bin/python

import sys
lineCount = 0
wordCount = 0
for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip().split() 
    lineCount += int(line[1])
    wordCount += int(line[0])

print("{0} {1}".format(wordCount, lineCount))

