#!/usr/bin/python 

import sys

for line in sys.stdin:
    host, _ = line.strip().split()
    print("{0}".format(host))
