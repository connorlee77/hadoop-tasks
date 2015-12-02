#!/usr/bin/python

import sys

arr = []
prevOwner = ''
for line in sys.stdin:
    owner, ans = line.strip().split()
    
    if owner == prevOwner:
        arr.append(ans)
    else:
        if prevOwner != '':
            print("{0}\t{1}\t{2}".format(prevOwner, len(arr), str(map(int, arr))))
        prevOwner = owner
        arr = [ans]
