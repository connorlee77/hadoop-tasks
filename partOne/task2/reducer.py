#!/usr/bin/python

import sys

currentSentence = ''
for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Strip whitespace in inputs
    
    if line != currentSentence:
        currentSentence = line
        print line
    

