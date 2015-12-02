#!/usr/bin/python 

import sys

counter = 0
for line in sys.stdin:
    if counter < 10:
        print line.strip()
    counter += 1
