#!/usr/bin/python 

import sys

maxLine = ''
maxCount = 0
for line in sys.stdin: 
    line, count = line.strip().split()
    count = int(count)
    if count > maxCount:
        maxCount = count
        maxLine = line

print("{0}\t{1}".format(maxLine, maxCount))             
