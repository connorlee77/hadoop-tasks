#!/usr/bin/python

import sys
lineCount = 0
wordCount = 0
for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Strip whitespace in inputs
    line = line.split()     
    lineCount += 1
    wordCount += len(line)

print("{0} {1}".format(wordCount, lineCount))

