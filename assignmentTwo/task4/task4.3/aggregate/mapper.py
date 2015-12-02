#!/usr/bin/python

import sys

for line in sys.stdin:
    owner, ct = line.strip().split()
    print('{0}\t{1}'.format(owner, ct))
