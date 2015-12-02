#!/usr/bin/python

import sys

prevOwner = ''
postIDS = []
for line in sys.stdin:
    postID, owner = line.strip().split()
    
    if owner == prevOwner:
        postIDS.append(postID)
    else:
        if prevOwner != '':
            print("{0}\t{1}\t{2}".format(prevOwner, len(postIDS), str(map(int, postIDS)).strip('[]')))
        prevOwner = owner
        postIDS = [postID]
print("{0}\t{1}\t{2}".format(owner, len(postIDS), str(map(int, postIDS)).strip('[]')))
