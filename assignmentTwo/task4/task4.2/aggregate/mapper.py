#!/usr/bin/python

import sys

for line in sys.stdin:
    owner, ct, arr = line.strip().split('\t')
    print('{0}\t{1}\t{2}'.format(owner, ct, arr))
