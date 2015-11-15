#!/usr/bin/python

import sys
lineCounter = 0
for line in sys.stdin:
    line = line.strip().split('.')
    if len(line) == 2 and lineCounter == 0:
        print str(line[0]) + ' at ' + str(line[1]) 
    lineCounter += 1
        
