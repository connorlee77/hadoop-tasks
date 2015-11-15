#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip().split()
    newCol = line[0]
    for newRow in range(len(line[1:])):
        print("{0}.{1}.{2}".format(newRow, newCol, line[newRow + 1]))
