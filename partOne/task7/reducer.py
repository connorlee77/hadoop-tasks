#!/usr/bin/python

import sys
row = ''
rowNum = -1
for line in sys.stdin:
    newRow, rolCol, val = line.strip().split('.')
    if rowNum < 0:
        rowNum = newRow
    if newRow != rowNum:
        print str(rowNum) + '\t' + row.strip()
        row = str(val)
    else:
        row = row + ' ' + str(val)
    rowNum = newRow
print str(rowNum) + '\t'+ row.strip()
