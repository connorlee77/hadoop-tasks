#!/usr/bin/python

import sys

for line in sys.stdin:  # input from standard input
    line = line.strip().split()
    if len(line) == 3:
        print("{1}.{0}.{2}".format(line[0], line[1], line[2]))
    elif len(line) == 4:
        print("{2}.{0}.{1}.{3}".format(line[0], line[1], line[2], line[3]))
