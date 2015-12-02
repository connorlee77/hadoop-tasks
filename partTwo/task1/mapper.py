#!/usr/bin/python

import sys
import os

for line in sys.stdin:  # input from standard input
    path = os.environ["mapreduce_map_input_file"].split('/')[-1:]
    line = line.strip().split()
    
    for word in line:
        print("{0}\t{1}".format(word, path[0]))

         
