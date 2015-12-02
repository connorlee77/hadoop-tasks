#!/usr/bin/python

import sys
import os

terms = set()
for line in file('terms.txt'):
    terms.add(line.strip())

for line in sys.stdin:
    path = os.environ["mapreduce_map_input_file"].split('/')[-1:]
    line = line.strip().split()
    for word in line:
        if word in terms:
            print("{0}\t{1}".format(word, path[0]))    

