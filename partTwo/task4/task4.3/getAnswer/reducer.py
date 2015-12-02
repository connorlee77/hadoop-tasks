#!/usr/bin/python

import sys

count = 0
for line in sys.stdin:
    if count == 0:
        owner, ct, arr = line.strip().split('\t')
        print("{0} -> {1}, {2}".format(owner, ct, arr.strip('[]')))
    count += 1
