#!/usr/bin/python 

import sys

for line in sys.stdin: 
    host, count = line.strip().split()
    print("{0}\t{1}".format(host, count))
