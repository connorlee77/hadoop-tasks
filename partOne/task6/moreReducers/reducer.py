#!/usr/bin/python

import sys

lineCount = 0
for line in sys.stdin:  
    if lineCount < 20:
        print line.strip()
    lineCount += 1 

