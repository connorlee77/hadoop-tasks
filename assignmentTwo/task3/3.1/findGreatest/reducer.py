#!/usr/bin/python 

import sys

printed = False
for line in sys.stdin:
    if printed is False:
        print line.strip()
        printed = True
