#!/usr/bin/python

import sys

acceptedAnswerId = ''
for line in sys.stdin:
    AnsId, val, id_owner = line.strip().split()
    if val == '1':
        acceptedAnswerId = AnsId
    elif val == '2' and AnsId == acceptedAnswerId:
        print("{0}\t{1}".format(id_owner, AnsId))
