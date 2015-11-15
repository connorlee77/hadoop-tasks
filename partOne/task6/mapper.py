#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip().split()
    print("{0}.{1}.{2}".format(line[2], line[0], line[1])) 
