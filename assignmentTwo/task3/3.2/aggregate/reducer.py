#!/usr/bin/python 

import sys

prev = ''
count = 0
for line in sys.stdin:
    line = line.strip()
    if prev == line: 
        count += 1    
    else:
        if prev != '':
            print("{0}\t{1}".format(prev, count))
        prev = line
        count = 1

print("{0}\t{1}".format(prev, count))
