#!/usr/bin/python

import sys

for line in sys.stdin:              # input from standard input
    line = line.strip().split()     # Remove white space in the line and splits the string.
     
    for i in range(1, len(line)):
        print("{0}\t{1}".format(' '.join(line[i - 1: i + 1]), 1))
        
         
    
