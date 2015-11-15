#!/usr/bin/python

import sys

for line in sys.stdin:  # input from standard input
    line = line.strip() # Remove white space in the line.
    print line          # Output the line for lowercasing in the reducer.                 
